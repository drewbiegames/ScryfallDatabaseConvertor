import json
import csv
import sys

#open the input json file
with open(sys.argv[1]) as f:
	data = json.load(f)

#create the output.csv file
with open('output.csv', 'w', newline='') as csvfile:

	thewriter = csv.DictWriter(csvfile,fieldnames=headers,extrasaction='ignore')

	#only writes the columns defined here.
	headers = ["id","name","set","set_name","image","rarity","type_line","oracle_text","flavor_text","cmc","mana_cost",
	"loyalty","power","toughness","colors","color_identity","watermark","collector_number","border_color","foil","nonfoil","full_art","frame_effect",
	"oversized","promo","lang","layout"]

	thewriter.writeheader()
	
	for card in data:
		if 'lang' in card:
			if card['lang'] != 'en':
				continue
			else:
				#Only save the 'normal' sized image link to the CSV
				if 'image_uris' in card:
					card["image"] = card['image_uris']['normal']
				#only use front facing card face if there are multiple faces
				if 'card_faces' in card:
					if 'image_uris' in card['card_faces'][0]:
						card["image"] = card['card_faces'][0]['image_uris']['normal']
					name = card['name']
					if 'type_line' in card:
						type = card['type_line']
					card.update(card['card_faces'][0])
					card['name'] = name
					if type is not None:
						card['type_line'] = type
			thewriter.writerow(card)
