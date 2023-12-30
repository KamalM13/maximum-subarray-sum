---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
def max_subarray(A[0...n]):
    max_so_far = max_ending_here = A[0]
    for i from 1 to n:
        max_ending_here = max(A[i], max_ending_here + A[i])
        max_so_far = max(max_so_far, max_ending_here)
    return best_sum ^SsWFETNk

[1,-3,2,1,-1] ^8YZpw8j2

Maximum Sum ^V5jfwj8l

Kamal Mohamed

Maximum Subarray problem (Dynamic Programming)  ^g0qtu3Ou

[1,-3,2,1,-1] ^acp6iFVK

[1,-3,2,1,-1] ^ZlBUwH4n

Not contiguous ^YBA3bvn6

Contiguous subarray ^djlWZGhD

[1,-3,2,1,-1] ^WG4Ft5Q6

j-th ^gNYLdCqt

max ^k0KUuJ8F

max ^pXrZ667W

Dynamic Programming ^P8NVsMEX

max(j, current_sum + j) ^pe4WnEnt

[X] ^CBhVR9Vn

or ^0LBPX5gy

[ ,X] ^WdjXko9S

Kadane's Algorithm ^TAKz5rxX

M ^h02VtzoH

max_ending_here =  ^JsYontNq

i ^2DmZEIqT

c ^DEVa3Mnx

b ^7ycf7a5S

-2 ^c0wa1p3H

-2 ^l1lIobLc

3 ^3kJnPgCX

3 ^Hs8Xof1V

5 ^35nz1PfF

5 ^rxdgCHxq

1 ^ipXd6bku

2 ^t3MdNkAZ

3 ^QhGI0iI4

4 ^9zoFYFZW

5 ^UXQ3BzGS

[-2,3,2,-1] ^mFuFw2xX

[-3,1,-1] ^Wivvn8jB

2 Brute-force approaches ^0Jg7gHHB

max_so_far ^h5oejXSa

= ^QsRL1jGq

Not a subarray ^MZgcE4LR

int max_sum = 0
    for(i = 0 to n-1)
    {
       for(j = i to n-1) 
       {  
          int sum = 0
          for(k = i to j)
             sum = sum + A[k]
          if(sum > max_sum)
             max_sum = sum
       }
    }  ^3A6RTFa6

int max_sum = 0
    for ( i = 0 to n-1)
    {   
       sum=0
       for( j = i to n-1) 
       {  
         sum = sum +  A[j]
         if (sum > max_sum)
             max_sum = sum
        }
    } ^KFASrgve

o(n ) ^6UD5Ts5M

3 ^3SAyA6It

o(n ) ^xXFJi4rE

2 ^RgY5UCm5

running sum ^BgRI1moP

auxiliary array ^36mJaQ4P

[i-1] ^u8XKlzyT

X ^ndNXJmH1

M ^9KsECvpH

aux[0] = a[0] ^w2J2FrYn

time: o(n)
space: o(n) ^CgXdnYJw

[1,-3,2,1,-1] ^NE4WNp2I

[2] ^DIUorbzF

[1,-3,2] ^Tq5h12El

max_ending_here ^UhQqyLqd

[2] ^g7uve15V

max_ending_here ^XYVLgQ82

m ^CokMILx9

x ^Ok3HepwK

max_so_far = 1 ^afsehUA2


# Embedded files
1bcfa8476e14766f83773ca3dc9c015f8ebc41fa: $$\sum_{i=1}^n 1 = n-1+1 = n\in O(n)$$
895fef8a839a47fb1639524bc45910bb0a317e8c: [[Pasted Image 20231223162529_173.png]]
0836ea0a1e27ad36a1f57090ffafaf0b951c1356: [[Pasted Image 20231223162808_176.png]]

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.0.10",
	"elements": [
		{
			"type": "text",
			"version": 1011,
			"versionNonce": 1537234242,
			"isDeleted": false,
			"id": "SsWFETNk",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -455.94895417827786,
			"y": 674.0249929135583,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 967.96875,
			"height": 201.60000000000002,
			"seed": 359952780,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 3,
			"text": "def max_subarray(A[0...n]):\n    max_so_far = max_ending_here = A[0]\n    for i from 1 to n:\n        max_ending_here = max(A[i], max_ending_here + A[i])\n        max_so_far = max(max_so_far, max_ending_here)\n    return best_sum",
			"rawText": "def max_subarray(A[0...n]):\n    max_so_far = max_ending_here = A[0]\n    for i from 1 to n:\n        max_ending_here = max(A[i], max_ending_here + A[i])\n        max_so_far = max(max_so_far, max_ending_here)\n    return best_sum",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "def max_subarray(A[0...n]):\n    max_so_far = max_ending_here = A[0]\n    for i from 1 to n:\n        max_ending_here = max(A[i], max_ending_here + A[i])\n        max_so_far = max(max_so_far, max_ending_here)\n    return best_sum",
			"lineHeight": 1.2,
			"baseline": 195
		},
		{
			"type": "text",
			"version": 590,
			"versionNonce": 1831606238,
			"isDeleted": false,
			"id": "8YZpw8j2",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -375.8311882593873,
			"y": -1726.092023589541,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 213.28125,
			"height": 33.6,
			"seed": 697082164,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "Gkt_fjC1eRG7N40TnowFs",
					"type": "arrow"
				}
			],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 3,
			"text": "[1,-3,2,1,-1]",
			"rawText": "[1,-3,2,1,-1]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "[1,-3,2,1,-1]",
			"lineHeight": 1.2,
			"baseline": 27
		},
		{
			"type": "freedraw",
			"version": 681,
			"versionNonce": 1562926338,
			"isDeleted": false,
			"id": "EbK4B6AlDaeivRo9OlOV0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -270.1424926106105,
			"y": -1722.980721028221,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 32.711406777092805,
			"height": 23.511296922972235,
			"seed": 270811020,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5111077214731381
				],
				[
					0.5111077214731381,
					-1.5333231644194143
				],
				[
					0.5111077214731381,
					-2.5555813242667114
				],
				[
					0.5111077214731381,
					-3.577818125663498
				],
				[
					0.5111077214731381,
					-5.111162648533366
				],
				[
					1.0222154429462194,
					-6.133378091479642
				],
				[
					1.0222154429462194,
					-7.666743972800134
				],
				[
					1.0222154429462194,
					-8.688959415746297
				],
				[
					1.0222154429462194,
					-9.71119621714314
				],
				[
					1.5333658813204352,
					-11.244540740013065
				],
				[
					1.5333658813204352,
					-11.755648461486146
				],
				[
					1.5333658813204352,
					-12.777885262882933
				],
				[
					1.5333658813204352,
					-13.80012206427972
				],
				[
					1.5333658813204352,
					-14.311229785752857
				],
				[
					2.0444736027935733,
					-15.333466587149644
				],
				[
					2.0444736027935733,
					-15.844574308622725
				],
				[
					2.0444736027935733,
					-16.35570338854643
				],
				[
					2.0444736027935733,
					-16.866789751569
				],
				[
					2.0444736027935733,
					-17.37791883149265
				],
				[
					2.0444736027935733,
					-17.8890479114163
				],
				[
					2.5555813242667114,
					-17.8890479114163
				],
				[
					3.0666890457397926,
					-17.8890479114163
				],
				[
					3.5777967672129307,
					-17.8890479114163
				],
				[
					4.088904488686069,
					-17.8890479114163
				],
				[
					5.111162648533366,
					-17.8890479114163
				],
				[
					5.622270370006504,
					-17.8890479114163
				],
				[
					7.155636251326939,
					-17.8890479114163
				],
				[
					7.666743972800077,
					-17.8890479114163
				],
				[
					9.200067137219435,
					-17.8890479114163
				],
				[
					10.222325297066789,
					-17.8890479114163
				],
				[
					11.755648461486146,
					-17.8890479114163
				],
				[
					12.777906621333443,
					-17.8890479114163
				],
				[
					14.311229785752857,
					-17.8890479114163
				],
				[
					15.844595667073293,
					-17.8890479114163
				],
				[
					17.37791883149265,
					-17.8890479114163
				],
				[
					18.400176991339947,
					-17.8890479114163
				],
				[
					19.93350015575936,
					-17.8890479114163
				],
				[
					21.466866037079797,
					-17.8890479114163
				],
				[
					22.489081480026016,
					-17.8890479114163
				],
				[
					23.511296922972292,
					-17.8890479114163
				],
				[
					24.53355508281959,
					-17.8890479114163
				],
				[
					25.555770525765865,
					-17.8890479114163
				],
				[
					26.577985968712085,
					-17.8890479114163
				],
				[
					27.0891364070863,
					-17.8890479114163
				],
				[
					27.60024412855944,
					-17.8890479114163
				],
				[
					28.11135185003252,
					-17.8890479114163
				],
				[
					28.622459571505658,
					-17.8890479114163
				],
				[
					29.133567292978796,
					-18.400155632889494
				],
				[
					29.644717731353012,
					-18.400155632889494
				],
				[
					29.644717731353012,
					-18.911284712813142
				],
				[
					30.155825452826093,
					-18.911284712813142
				],
				[
					30.66693317429923,
					-18.911284712813142
				],
				[
					30.66693317429923,
					-19.422371075835656
				],
				[
					31.17804089577237,
					-19.422371075835656
				],
				[
					31.689148617245507,
					-19.422371075835656
				],
				[
					31.689148617245507,
					-18.911284712813142
				],
				[
					31.689148617245507,
					-18.400155632889494
				],
				[
					31.689148617245507,
					-17.8890479114163
				],
				[
					31.689148617245507,
					-17.37791883149265
				],
				[
					31.689148617245507,
					-16.866789751569
				],
				[
					31.689148617245507,
					-16.35570338854643
				],
				[
					31.689148617245507,
					-15.844574308622725
				],
				[
					31.689148617245507,
					-15.333466587149644
				],
				[
					31.689148617245507,
					-14.822358865676506
				],
				[
					31.689148617245507,
					-14.311229785752857
				],
				[
					31.689148617245507,
					-13.80012206427972
				],
				[
					31.689148617245507,
					-13.289014342806638
				],
				[
					31.689148617245507,
					-12.266777541409795
				],
				[
					31.689148617245507,
					-11.244540740013065
				],
				[
					31.689148617245507,
					-10.73343301853987
				],
				[
					31.689148617245507,
					-10.222303938616221
				],
				[
					31.689148617245507,
					-9.71119621714314
				],
				[
					31.689148617245507,
					-9.200067137219492
				],
				[
					31.689148617245507,
					-8.688959415746297
				],
				[
					31.689148617245507,
					-8.177851694273215
				],
				[
					31.689148617245507,
					-7.666743972800134
				],
				[
					31.689148617245507,
					-7.155614892876429
				],
				[
					31.689148617245507,
					-6.64448581295278
				],
				[
					31.689148617245507,
					-6.133378091479642
				],
				[
					31.689148617245507,
					-5.622270370006561
				],
				[
					31.689148617245507,
					-5.111162648533366
				],
				[
					31.689148617245507,
					-4.600033568609717
				],
				[
					31.689148617245507,
					-4.088904488686069
				],
				[
					31.689148617245507,
					-3.577818125663498
				],
				[
					31.689148617245507,
					-3.0666890457397926
				],
				[
					31.689148617245507,
					-2.5555813242667114
				],
				[
					31.689148617245507,
					-2.0444736027935733
				],
				[
					31.689148617245507,
					-1.5333231644194143
				],
				[
					31.689148617245507,
					-1.0222368013967866
				],
				[
					31.689148617245507,
					-0.5111077214731381
				],
				[
					31.689148617245507,
					0
				],
				[
					31.689148617245507,
					0.5111077214731381
				],
				[
					31.689148617245507,
					1.0222368013967866
				],
				[
					32.20025633871859,
					1.0222368013967866
				],
				[
					32.20025633871859,
					1.5333445228698679
				],
				[
					32.20025633871859,
					2.044452244343006
				],
				[
					32.20025633871859,
					2.5555813242667114
				],
				[
					32.20025633871859,
					3.0666890457397926
				],
				[
					32.20025633871859,
					3.5777967672129307
				],
				[
					32.711406777092805,
					3.5777967672129307
				],
				[
					32.711406777092805,
					4.088925847136579
				],
				[
					32.711406777092805,
					4.088925847136579
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "arrow",
			"version": 1604,
			"versionNonce": 769223710,
			"isDeleted": false,
			"id": "Gkt_fjC1eRG7N40TnowFs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -255.01551191765662,
			"y": -1741.9188469836408,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 18.83573109138004,
			"height": 43.28260863931786,
			"seed": 1622116876,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "8YZpw8j2",
				"focus": -0.00020617324352562583,
				"gap": 15.826823394099847
			},
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					18.83573109138004,
					-43.28260863931786
				]
			]
		},
		{
			"type": "text",
			"version": 757,
			"versionNonce": 1205431490,
			"isDeleted": false,
			"id": "V5jfwj8l",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -316.22335202452706,
			"y": -1812.3185826923386,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 177.99594116210938,
			"height": 35,
			"seed": 1082014004,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Maximum Sum",
			"rawText": "Maximum Sum",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Maximum Sum",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "text",
			"version": 576,
			"versionNonce": 1314011230,
			"isDeleted": false,
			"id": "g0qtu3Ou",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -350.2630747466768,
			"y": -2454.0450119248912,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 686.2517700195312,
			"height": 105,
			"seed": 2097891508,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Kamal Mohamed\n\nMaximum Subarray problem (Dynamic Programming) ",
			"rawText": "Kamal Mohamed\n\nMaximum Subarray problem (Dynamic Programming) ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Kamal Mohamed\n\nMaximum Subarray problem (Dynamic Programming) ",
			"lineHeight": 1.25,
			"baseline": 94
		},
		{
			"type": "text",
			"version": 689,
			"versionNonce": 559056002,
			"isDeleted": false,
			"id": "acp6iFVK",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -9.297132088380181,
			"y": -1842.3837101533134,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 213.28125,
			"height": 33.6,
			"seed": 1595078412,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 3,
			"text": "[1,-3,2,1,-1]",
			"rawText": "[1,-3,2,1,-1]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "[1,-3,2,1,-1]",
			"lineHeight": 1.2,
			"baseline": 27
		},
		{
			"type": "text",
			"version": 764,
			"versionNonce": 912751774,
			"isDeleted": false,
			"id": "ZlBUwH4n",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2.077989981932319,
			"y": -1676.5100834443294,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 213.28125,
			"height": 33.6,
			"seed": 744718220,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 3,
			"text": "[1,-3,2,1,-1]",
			"rawText": "[1,-3,2,1,-1]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "[1,-3,2,1,-1]",
			"lineHeight": 1.2,
			"baseline": 27
		},
		{
			"type": "rectangle",
			"version": 636,
			"versionNonce": 1666360386,
			"isDeleted": false,
			"id": "LMp940GagJkxOZBHCZe9O",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 113.13008348779158,
			"y": -1838.7318729951105,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 31.40277099609375,
			"height": 29.942169189453125,
			"seed": 1935720972,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 689,
			"versionNonce": 734673118,
			"isDeleted": false,
			"id": "c1arSp-wQMgrhzCnhPTEH",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 155.42872850732283,
			"y": -1839.3378147675714,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 31.40277099609375,
			"height": 29.942169189453125,
			"seed": 53920564,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 682,
			"versionNonce": 2008599554,
			"isDeleted": false,
			"id": "rXux68PNtCA8rpjGq62kC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 40.626787589354194,
			"y": -1840.8106846406183,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 31.40277099609375,
			"height": 29.942169189453125,
			"seed": 1345280564,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1091,
			"versionNonce": 369847582,
			"isDeleted": false,
			"id": "YBA3bvn6",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -7.376154346630528,
			"y": -1958.7428279356404,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 204.5119171142578,
			"height": 35,
			"seed": 385083444,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Not contiguous",
			"rawText": "Not contiguous",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Not contiguous",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "rectangle",
			"version": 541,
			"versionNonce": 881064898,
			"isDeleted": false,
			"id": "legzfvLLytJhTTeXwA_f3",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 49.36540453271357,
			"y": -1679.5617680146418,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 72.29943847656237,
			"height": 40.166290283203125,
			"seed": 836621364,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 890,
			"versionNonce": 1117526366,
			"isDeleted": false,
			"id": "djlWZGhD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -44.562514528207544,
			"y": -1727.5609924377484,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 279.0198974609375,
			"height": 35,
			"seed": 483076276,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Contiguous subarray",
			"rawText": "Contiguous subarray",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Contiguous subarray",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "freedraw",
			"version": 417,
			"versionNonce": 1473459074,
			"isDeleted": false,
			"id": "luvYvVsSVd33MTa8vZW6G",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 247.2757438881822,
			"y": -1844.6088566376886,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 32.133056640625,
			"height": 20.448333740234375,
			"seed": 734533812,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.73046875,
					0
				],
				[
					2.19091796875,
					0
				],
				[
					2.9212646484375,
					0.730316162109375
				],
				[
					3.6514892578125,
					0.730316162109375
				],
				[
					5.8424072265625,
					2.190887451171875
				],
				[
					7.302978515625,
					3.6514892578125
				],
				[
					8.763671875,
					4.381805419921875
				],
				[
					10.9544677734375,
					5.842376708984375
				],
				[
					13.875732421875,
					8.03326416015625
				],
				[
					16.0665283203125,
					10.22418212890625
				],
				[
					18.9879150390625,
					11.68475341796875
				],
				[
					22.6392822265625,
					13.87567138671875
				],
				[
					24.099853515625,
					15.33624267578125
				],
				[
					26.290771484375,
					16.796844482421875
				],
				[
					28.4815673828125,
					17.52716064453125
				],
				[
					30.6724853515625,
					18.98773193359375
				],
				[
					31.40283203125,
					19.718017578125
				],
				[
					32.133056640625,
					19.718017578125
				],
				[
					32.133056640625,
					20.448333740234375
				],
				[
					32.133056640625,
					20.448333740234375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 412,
			"versionNonce": 684539294,
			"isDeleted": false,
			"id": "d8ar2OUJiAJDhHeKpSco3",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 271.3755974038072,
			"y": -1844.6088566376886,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 24.830078125,
			"height": 21.908905029296875,
			"seed": 192879028,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-5.1119384765625,
					3.6514892578125
				],
				[
					-6.5726318359375,
					4.381805419921875
				],
				[
					-9.493896484375,
					7.302978515625
				],
				[
					-11.684814453125,
					8.763580322265625
				],
				[
					-13.8756103515625,
					10.22418212890625
				],
				[
					-16.06640625,
					12.415069580078125
				],
				[
					-18.2574462890625,
					14.60595703125
				],
				[
					-19.7178955078125,
					16.0665283203125
				],
				[
					-21.1785888671875,
					17.52716064453125
				],
				[
					-22.63916015625,
					18.98773193359375
				],
				[
					-24.099853515625,
					20.448333740234375
				],
				[
					-24.099853515625,
					21.17864990234375
				],
				[
					-24.830078125,
					21.17864990234375
				],
				[
					-24.830078125,
					21.908905029296875
				],
				[
					-24.830078125,
					21.908905029296875
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 1165,
			"versionNonce": 65368898,
			"isDeleted": false,
			"id": "WG4Ft5Q6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1047.5459245555899,
			"y": -152.74924312857715,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 213.28125,
			"height": 33.6,
			"seed": 1434209164,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 3,
			"text": "[1,-3,2,1,-1]",
			"rawText": "[1,-3,2,1,-1]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "[1,-3,2,1,-1]",
			"lineHeight": 1.2,
			"baseline": 27
		},
		{
			"type": "text",
			"version": 737,
			"versionNonce": 768596446,
			"isDeleted": false,
			"id": "gNYLdCqt",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1157.4172451790173,
			"y": -217.18823033186027,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 50.343963623046875,
			"height": 35,
			"seed": 89646,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "Ny44BUbNkHcJe6P6mj09b",
					"type": "arrow"
				}
			],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "j-th",
			"rawText": "j-th",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "j-th",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "arrow",
			"version": 1316,
			"versionNonce": 991542018,
			"isDeleted": false,
			"id": "Ny44BUbNkHcJe6P6mj09b",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1180.5688850782362,
			"y": -180.1527479554655,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 5.01288412558398,
			"height": 32.16604720437738,
			"seed": 1513080972,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "gNYLdCqt",
				"focus": 0.18153995609222218,
				"gap": 2.035482376394782
			},
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					5.01288412558398,
					32.16604720437738
				]
			]
		},
		{
			"type": "text",
			"version": 871,
			"versionNonce": 1756687902,
			"isDeleted": false,
			"id": "k0KUuJ8F",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1085.741716477979,
			"y": -187.25435707540288,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 52.135986328125,
			"height": 35,
			"seed": 360457012,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "max",
			"rawText": "max",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "max",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "freedraw",
			"version": 766,
			"versionNonce": 1542392514,
			"isDeleted": false,
			"id": "j3tdlDJoKJRfndoYSXqt7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1064.4369240312067,
			"y": -139.63190551279484,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 105.27068883290411,
			"height": 18.380598402501334,
			"seed": 281896116,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.4177345249586608
				],
				[
					0.4177345249586324,
					-0.8354690499172932
				],
				[
					0.4177345249586324,
					-1.6709555563546417
				],
				[
					0.8354690499172932,
					-2.50644206279199
				],
				[
					1.2532210313959808,
					-3.7596630941879994
				],
				[
					1.6709555563546417,
					-5.01288412558398
				],
				[
					2.0887075378333293,
					-6.2661051569799895
				],
				[
					2.50644206279199,
					-7.519326188375999
				],
				[
					2.9241765877506225,
					-9.190299201250696
				],
				[
					3.3419111127092833,
					-10.025768251167989
				],
				[
					3.759663094187971,
					-11.279006739084025
				],
				[
					4.177415075666687,
					-12.532227770480034
				],
				[
					4.595149600625348,
					-13.367696820397327
				],
				[
					5.01288412558398,
					-14.203183326834676
				],
				[
					5.01288412558398,
					-15.038669833272024
				],
				[
					5.01288412558398,
					-15.456404358230657
				],
				[
					5.430618650542641,
					-15.874138883189318
				],
				[
					5.430618650542641,
					-16.291890864668005
				],
				[
					5.848370632021329,
					-16.291890864668005
				],
				[
					6.683839681938622,
					-16.291890864668005
				],
				[
					7.51932618837597,
					-16.291890864668005
				],
				[
					8.354830151333374,
					-15.874138883189318
				],
				[
					9.608033726209328,
					-15.874138883189318
				],
				[
					11.27898928256397,
					-15.456404358230657
				],
				[
					12.532227770480006,
					-15.456404358230657
				],
				[
					14.620935308313364,
					-15.038669833272024
				],
				[
					17.545111896064014,
					-15.038669833272024
				],
				[
					19.633819433897344,
					-15.038669833272024
				],
				[
					22.140261496689334,
					-14.620917851793308
				],
				[
					25.4821900659187,
					-14.620917851793308
				],
				[
					28.406366653669323,
					-14.620917851793308
				],
				[
					31.330578154460085,
					-14.620917851793308
				],
				[
					34.67248926716937,
					-14.620917851793308
				],
				[
					38.01441783639871,
					-14.620917851793308
				],
				[
					40.93859442414936,
					-14.620917851793308
				],
				[
					43.862788468420035,
					-14.620917851793308
				],
				[
					46.786965056170686,
					-14.620917851793308
				],
				[
					49.71115910044139,
					-14.620917851793308
				],
				[
					52.21760116323338,
					-14.620917851793308
				],
				[
					54.72404322602537,
					-14.620917851793308
				],
				[
					57.23048528881736,
					-14.620917851793308
				],
				[
					59.31919282665072,
					-14.620917851793308
				],
				[
					61.82563488944271,
					-14.620917851793308
				],
				[
					63.91434242727604,
					-14.620917851793308
				],
				[
					65.58531544015077,
					-14.620917851793308
				],
				[
					67.67400552146404,
					-14.620917851793308
				],
				[
					69.34497853433874,
					-15.038669833272024
				],
				[
					70.59819956573475,
					-15.038669833272024
				],
				[
					71.85142059713073,
					-15.038669833272024
				],
				[
					73.10464162852674,
					-15.038669833272024
				],
				[
					73.94012813496408,
					-15.456404358230657
				],
				[
					75.19334916636006,
					-15.456404358230657
				],
				[
					76.02883567279744,
					-15.456404358230657
				],
				[
					76.86430472271473,
					-15.456404358230657
				],
				[
					77.69979122915208,
					-15.456404358230657
				],
				[
					78.53527773558943,
					-15.456404358230657
				],
				[
					79.78849876698541,
					-15.456404358230657
				],
				[
					80.20623329194407,
					-15.456404358230657
				],
				[
					81.87720630481877,
					-15.456404358230657
				],
				[
					82.71269281125612,
					-15.456404358230657
				],
				[
					83.54816186117341,
					-15.456404358230657
				],
				[
					84.38364836761076,
					-15.456404358230657
				],
				[
					85.21913487404811,
					-15.456404358230657
				],
				[
					86.0546039239654,
					-15.456404358230657
				],
				[
					86.89009043040275,
					-15.456404358230657
				],
				[
					87.30782495536141,
					-15.456404358230657
				],
				[
					88.14334637483887,
					-15.038669833272024
				],
				[
					88.97879796823611,
					-15.038669833272024
				],
				[
					89.81428447467346,
					-15.038669833272024
				],
				[
					90.64975352459075,
					-15.038669833272024
				],
				[
					91.06750550606944,
					-15.038669833272024
				],
				[
					91.90297455598673,
					-15.038669833272024
				],
				[
					92.73846106242408,
					-15.038669833272024
				],
				[
					93.1562130439028,
					-15.038669833272024
				],
				[
					93.99168209382009,
					-15.038669833272024
				],
				[
					94.82716860025744,
					-15.038669833272024
				],
				[
					95.24490312521607,
					-15.038669833272024
				],
				[
					96.08038963165342,
					-15.038669833272024
				],
				[
					96.49815906965219,
					-15.038669833272024
				],
				[
					96.9158761380908,
					-15.038669833272024
				],
				[
					97.75136264452814,
					-15.038669833272024
				],
				[
					98.16909716948678,
					-15.456404358230657
				],
				[
					98.58686660748555,
					-15.456404358230657
				],
				[
					99.00458367592412,
					-15.456404358230657
				],
				[
					99.42231820088278,
					-15.456404358230657
				],
				[
					99.84005272584142,
					-15.456404358230657
				],
				[
					100.25780470732013,
					-15.874138883189318
				],
				[
					101.09327375723743,
					-15.874138883189318
				],
				[
					101.51102573871611,
					-15.874138883189318
				],
				[
					102.34651224515346,
					-16.291890864668005
				],
				[
					102.76426422663218,
					-16.291890864668005
				],
				[
					103.59973327654944,
					-16.291890864668005
				],
				[
					104.01746780150813,
					-16.709625389626666
				],
				[
					104.43520232646677,
					-16.709625389626666
				],
				[
					104.85297176446551,
					-16.709625389626666
				],
				[
					105.27068883290411,
					-17.127377371105354
				],
				[
					105.27068883290411,
					-16.709625389626666
				],
				[
					104.85297176446551,
					-16.291890864668005
				],
				[
					104.85297176446551,
					-15.456404358230657
				],
				[
					104.43520232646677,
					-15.038669833272024
				],
				[
					104.01746780150813,
					-14.203183326834676
				],
				[
					103.59973327654944,
					-12.949962295438695
				],
				[
					103.18198129507078,
					-12.114475789001318
				],
				[
					103.18198129507078,
					-11.279006739084025
				],
				[
					103.18198129507078,
					-10.443520232646677
				],
				[
					102.76426422663218,
					-9.608016269689273
				],
				[
					102.76426422663218,
					-8.77254721977198
				],
				[
					102.76426422663218,
					-8.354812694813347
				],
				[
					102.76426422663218,
					-7.519326188375999
				],
				[
					102.34651224515346,
					-7.101591663417338
				],
				[
					102.34651224515346,
					-6.6838571384587055
				],
				[
					102.34651224515346,
					-6.2661051569799895
				],
				[
					102.34651224515346,
					-5.848370632021357
				],
				[
					102.34651224515346,
					-5.430618650542641
				],
				[
					101.92876026367475,
					-5.01288412558398
				],
				[
					101.92876026367475,
					-4.595149600625348
				],
				[
					101.92876026367475,
					-3.7596630941879994
				],
				[
					101.51102573871611,
					-2.924176587750651
				],
				[
					101.51102573871611,
					-2.0887075378333577
				],
				[
					101.51102573871611,
					-1.253203574875954
				],
				[
					101.51102573871611,
					-0.8354690499172932
				],
				[
					101.51102573871611,
					0
				],
				[
					101.51102573871611,
					0.41775198147868764
				],
				[
					101.51102573871611,
					0.8355039629574037
				],
				[
					101.09327375723743,
					1.2532210313959808
				],
				[
					101.09327375723743,
					1.2532210313959808
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 796,
			"versionNonce": 1718450782,
			"isDeleted": false,
			"id": "al1bzkpY2SOiab_cnu9po",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1112.894862100252,
			"y": -178.48179239911087,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 71.01596900373352,
			"height": 53.47083092288938,
			"seed": 257645492,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.41775198147868764
				],
				[
					0,
					-1.2532297596559943
				],
				[
					0,
					-2.088698809573316
				],
				[
					0,
					-3.3419372974893804
				],
				[
					0.4177345249586608,
					-4.595158328885361
				],
				[
					0.4177345249586608,
					-5.848379360281342
				],
				[
					0.8354690499172932,
					-7.519343644896026
				],
				[
					0.8354690499172932,
					-8.772564676292006
				],
				[
					1.2532210313960093,
					-10.443520232646677
				],
				[
					1.2532210313960093,
					-11.69674999230267
				],
				[
					1.2532210313960093,
					-12.949979751958722
				],
				[
					1.2532210313960093,
					-14.203200783354703
				],
				[
					1.2532210313960093,
					-15.874165067969386
				],
				[
					1.2532210313960093,
					-17.127386099365367
				],
				[
					1.2532210313960093,
					-17.962863877542702
				],
				[
					1.2532210313960093,
					-19.216084908938683
				],
				[
					1.2532210313960093,
					-20.469314668594734
				],
				[
					1.2532210313960093,
					-21.722535699990715
				],
				[
					1.6709555563546417,
					-22.55801347816805
				],
				[
					1.6709555563546417,
					-23.81123450956403
				],
				[
					1.6709555563546417,
					-25.064464269220082
				],
				[
					1.6709555563546417,
					-25.899942047397417
				],
				[
					1.6709555563546417,
					-27.153163078793398
				],
				[
					1.6709555563546417,
					-27.988649585230746
				],
				[
					1.6709555563546417,
					-29.241870616626727
				],
				[
					1.6709555563546417,
					-30.077348394804062
				],
				[
					1.6709555563546417,
					-31.748312679418746
				],
				[
					1.6709555563546417,
					-32.58379918585604
				],
				[
					1.6709555563546417,
					-33.41927696403343
				],
				[
					1.6709555563546417,
					-34.25476347047072
				],
				[
					1.6709555563546417,
					-35.090241248648056
				],
				[
					1.6709555563546417,
					-35.92571902682539
				],
				[
					1.6709555563546417,
					-36.34346228004404
				],
				[
					1.6709555563546417,
					-37.17894878648144
				],
				[
					1.6709555563546417,
					-38.01442656465872
				],
				[
					1.6709555563546417,
					-38.84991307109607
				],
				[
					1.6709555563546417,
					-39.6853908492734
				],
				[
					1.6709555563546417,
					-40.10313410249205
				],
				[
					1.6709555563546417,
					-40.52086862745074
				],
				[
					1.6709555563546417,
					-41.35635513388809
				],
				[
					1.6709555563546417,
					-41.77409838710673
				],
				[
					1.6709555563546417,
					-42.19183291206542
				],
				[
					1.6709555563546417,
					-42.60957616528407
				],
				[
					1.6709555563546417,
					-43.0273106902427
				],
				[
					1.6709555563546417,
					-43.445062671721416
				],
				[
					1.2532210313960093,
					-43.86279719668005
				],
				[
					1.2532210313960093,
					-44.28054044989875
				],
				[
					1.2532210313960093,
					-44.6982837031174
				],
				[
					1.2532210313960093,
					-45.116018228076086
				],
				[
					0.8354690499172932,
					-45.53376148129473
				],
				[
					0.8354690499172932,
					-45.951504734513435
				],
				[
					0.8354690499172932,
					-46.36924798773208
				],
				[
					0.8354690499172932,
					-46.78698251269077
				],
				[
					0.8354690499172932,
					-47.2047170376494
				],
				[
					0.8354690499172932,
					-47.62246901912806
				],
				[
					0.8354690499172932,
					-48.040212272346764
				],
				[
					0.8354690499172932,
					-48.4579467973054
				],
				[
					0.4177345249586608,
					-48.8756900505241
				],
				[
					0.4177345249586608,
					-49.29342457548273
				],
				[
					0.4177345249586608,
					-49.71116782870138
				],
				[
					0.4177345249586608,
					-50.12891108192008
				],
				[
					0.4177345249586608,
					-50.54665433513878
				],
				[
					0.4177345249586608,
					-50.96439758835743
				],
				[
					0.4177345249586608,
					-51.38213211331606
				],
				[
					0.8354690499172932,
					-51.38213211331606
				],
				[
					2.50644206279199,
					-51.38213211331606
				],
				[
					3.3419285692293386,
					-51.79987536653476
				],
				[
					5.01288412558398,
					-51.79987536653476
				],
				[
					7.937078169854686,
					-51.79987536653476
				],
				[
					10.025768251167989,
					-51.79987536653476
				],
				[
					12.949962295438667,
					-51.79987536653476
				],
				[
					15.456404358230657,
					-52.21761861975341
				],
				[
					18.380598402501363,
					-52.21761861975341
				],
				[
					20.887040465293353,
					-52.21761861975341
				],
				[
					23.811217053044004,
					-52.21761861975341
				],
				[
					26.31767657235605,
					-52.21761861975341
				],
				[
					28.82411863514804,
					-52.63536187297211
				],
				[
					30.912826172981397,
					-52.63536187297211
				],
				[
					33.41926823577339,
					-52.63536187297211
				],
				[
					35.92571029856538,
					-52.63536187297211
				],
				[
					38.014417836398735,
					-52.63536187297211
				],
				[
					40.103125374232064,
					-52.63536187297211
				],
				[
					41.77411584362682,
					-52.63536187297211
				],
				[
					43.44503648694135,
					-52.63536187297211
				],
				[
					44.69827497485741,
					-52.63536187297211
				],
				[
					45.95151346277345,
					-52.63536187297211
				],
				[
					47.2047170376494,
					-53.053096397930744
				],
				[
					48.45793806904541,
					-53.053096397930744
				],
				[
					49.29342457548276,
					-53.053096397930744
				],
				[
					50.54664560687874,
					-53.053096397930744
				],
				[
					51.382114656796034,
					-53.053096397930744
				],
				[
					52.63533568819204,
					-53.053096397930744
				],
				[
					53.47082219462936,
					-53.053096397930744
				],
				[
					54.306326157586795,
					-53.053096397930744
				],
				[
					55.55952973246275,
					-53.053096397930744
				],
				[
					56.81275076385873,
					-53.053096397930744
				],
				[
					57.64823727029608,
					-53.053096397930744
				],
				[
					58.48374123325351,
					-53.053096397930744
				],
				[
					60.1546793330881,
					-53.053096397930744
				],
				[
					60.57244877108684,
					-53.053096397930744
				],
				[
					62.24338687092143,
					-53.053096397930744
				],
				[
					63.49660790231741,
					-53.053096397930744
				],
				[
					64.33209440875476,
					-53.053096397930744
				],
				[
					65.58531544015074,
					-53.053096397930744
				],
				[
					66.42078449006806,
					-53.053096397930744
				],
				[
					67.25628845302543,
					-53.053096397930744
				],
				[
					67.67402297798412,
					-53.053096397930744
				],
				[
					68.50949202790139,
					-53.053096397930744
				],
				[
					68.92726146590019,
					-53.053096397930744
				],
				[
					69.34499599085882,
					-53.053096397930744
				],
				[
					69.76273051581745,
					-53.053096397930744
				],
				[
					70.59819956573477,
					-53.47083092288938
				],
				[
					71.01596900373352,
					-53.47083092288938
				],
				[
					71.01596900373352,
					-53.053096397930744
				],
				[
					71.01596900373352,
					-52.63536187297211
				],
				[
					71.01596900373352,
					-52.21761861975341
				],
				[
					70.59819956573477,
					-51.79987536653476
				],
				[
					70.59819956573477,
					-51.38213211331606
				],
				[
					70.18046504077608,
					-50.54665433513878
				],
				[
					70.18046504077608,
					-49.71116782870138
				],
				[
					69.76273051581745,
					-49.29342457548273
				],
				[
					69.76273051581745,
					-48.4579467973054
				],
				[
					69.76273051581745,
					-47.62246901912806
				],
				[
					69.34499599085882,
					-46.78698251269077
				],
				[
					69.34499599085882,
					-45.951504734513435
				],
				[
					69.34499599085882,
					-45.116018228076086
				],
				[
					68.92726146590019,
					-44.28054044989875
				],
				[
					68.92726146590019,
					-43.445062671721416
				],
				[
					68.92726146590019,
					-43.0273106902427
				],
				[
					68.50949202790139,
					-42.19183291206542
				],
				[
					68.50949202790139,
					-41.77409838710673
				],
				[
					68.50949202790139,
					-40.93860315240937
				],
				[
					68.50949202790139,
					-40.52086862745074
				],
				[
					68.50949202790139,
					-40.10313410249205
				],
				[
					68.50949202790139,
					-39.6853908492734
				],
				[
					68.50949202790139,
					-39.26764759605476
				],
				[
					68.50949202790139,
					-38.84991307109607
				],
				[
					68.50949202790139,
					-38.43216981787742
				],
				[
					68.50949202790139,
					-38.01442656465872
				],
				[
					68.50949202790139,
					-37.596683311440074
				],
				[
					68.09175750294276,
					-37.17894878648144
				],
				[
					68.09175750294276,
					-36.76120553326274
				],
				[
					68.09175750294276,
					-36.34346228004404
				],
				[
					68.09175750294276,
					-35.92571902682539
				],
				[
					68.09175750294276,
					-35.50798450186676
				],
				[
					68.09175750294276,
					-35.090241248648056
				],
				[
					68.09175750294276,
					-34.67249799542941
				],
				[
					68.09175750294276,
					-34.25476347047072
				],
				[
					68.09175750294276,
					-33.837020217252075
				],
				[
					68.09175750294276,
					-33.41927696403343
				],
				[
					68.09175750294276,
					-33.001533710814726
				],
				[
					68.09175750294276,
					-32.58379918585604
				],
				[
					68.09175750294276,
					-32.16605593263739
				],
				[
					68.09175750294276,
					-31.748312679418746
				],
				[
					68.09175750294276,
					-31.330569426200043
				],
				[
					68.09175750294276,
					-30.91283490124141
				],
				[
					68.09175750294276,
					-30.495091648022708
				],
				[
					68.09175750294276,
					-30.495091648022708
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 839,
			"versionNonce": 486826626,
			"isDeleted": false,
			"id": "pXrZ667W",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1118.9030499753148,
			"y": -261.7963119476071,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 52.135986328125,
			"height": 35,
			"seed": 453031220,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "max",
			"rawText": "max",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "max",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "text",
			"version": 388,
			"versionNonce": 1841987230,
			"isDeleted": false,
			"id": "P8NVsMEX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -189.3484220959278,
			"y": 62.67866773800722,
			"strokeColor": "#f08c00",
			"backgroundColor": "transparent",
			"width": 278.1239013671875,
			"height": 35,
			"seed": 783736076,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Dynamic Programming",
			"rawText": "Dynamic Programming",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Dynamic Programming",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "text",
			"version": 527,
			"versionNonce": 152617538,
			"isDeleted": false,
			"id": "pe4WnEnt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 994.6666522987248,
			"y": -94.67685385616227,
			"strokeColor": "#f08c00",
			"backgroundColor": "transparent",
			"width": 328.4958801269531,
			"height": 35,
			"seed": 51369524,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "max(j, current_sum + j)",
			"rawText": "max(j, current_sum + j)",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "max(j, current_sum + j)",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "text",
			"version": 600,
			"versionNonce": 1132264158,
			"isDeleted": false,
			"id": "CBhVR9Vn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1850.4423172045204,
			"y": 584.8235185575381,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 44.491973876953125,
			"height": 35,
			"seed": 437892492,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826061,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "[X]",
			"rawText": "[X]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "[X]",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "text",
			"version": 531,
			"versionNonce": 2064329218,
			"isDeleted": false,
			"id": "0LBPX5gy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1790.4936460392892,
			"y": 583.0603237915083,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 27.551986694335938,
			"height": 35,
			"seed": 785851956,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "or",
			"rawText": "or",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "or",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "text",
			"version": 689,
			"versionNonce": 1846931230,
			"isDeleted": false,
			"id": "WdjXko9S",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1744.1350953312137,
			"y": 585.9806051563394,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 65.68797302246094,
			"height": 35,
			"seed": 208597900,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "[ ,X]",
			"rawText": "[ ,X]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "[ ,X]",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "text",
			"version": 563,
			"versionNonce": 433756610,
			"isDeleted": false,
			"id": "TAKz5rxX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 5.944439266855988,
			"x": 7.927179522996539,
			"y": 96.1364323879076,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 164.58877563476562,
			"height": 22.480020391568022,
			"seed": 1625250868,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 17.98401631325442,
			"fontFamily": 1,
			"text": "Kadane's Algorithm",
			"rawText": "Kadane's Algorithm",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Kadane's Algorithm",
			"lineHeight": 1.25,
			"baseline": 15
		},
		{
			"type": "text",
			"version": 547,
			"versionNonce": 1270584386,
			"isDeleted": false,
			"id": "h02VtzoH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1734.6590386878736,
			"y": 583.0602501111821,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 20.720291137695312,
			"height": 33.824528635943864,
			"seed": 429676724,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341884847,
			"link": null,
			"locked": false,
			"fontSize": 27.05962290875509,
			"fontFamily": 1,
			"text": "M",
			"rawText": "M",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "M",
			"lineHeight": 1.25,
			"baseline": 23
		},
		{
			"type": "text",
			"version": 616,
			"versionNonce": 1420169602,
			"isDeleted": false,
			"id": "JsYontNq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2127.969801492077,
			"y": 581.3566898453942,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 277.73187255859375,
			"height": 35,
			"seed": 1049748532,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "max_ending_here = ",
			"rawText": "max_ending_here = ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "max_ending_here = ",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "rectangle",
			"version": 465,
			"versionNonce": 1033846686,
			"isDeleted": false,
			"id": "6qgOTFazNe2qhivhMbdkx",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -398.6305115036359,
			"y": 876.8354889646748,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 449.02745769791363,
			"height": 219.22414455086744,
			"seed": 1112402060,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 411,
			"versionNonce": 1588367682,
			"isDeleted": false,
			"id": "QIR_f2uD2LQT0DO2mbmdF",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -396.8673167376061,
			"y": 923.8540733657237,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 448.43975885604874,
			"height": 0,
			"seed": 1984355724,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					448.43975885604874,
					0
				]
			]
		},
		{
			"type": "line",
			"version": 506,
			"versionNonce": 487693278,
			"isDeleted": false,
			"id": "mzzJvK1FduhhEwAr805El",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -398.6818298508329,
			"y": 992.6954195806765,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 448.49110176335455,
			"height": 0,
			"seed": 80671756,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					448.49110176335455,
					0
				]
			]
		},
		{
			"type": "line",
			"version": 605,
			"versionNonce": 726472962,
			"isDeleted": false,
			"id": "szuPgee0vV2YrMyLbk-DV",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -396.97102179672976,
			"y": 1057.1416360974758,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 447.95574051319875,
			"height": 0,
			"seed": 1554268468,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					447.95574051319875,
					0
				]
			]
		},
		{
			"type": "line",
			"version": 277,
			"versionNonce": 1315860510,
			"isDeleted": false,
			"id": "IO0Y3neSU6sZO8PGAxgbZ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -339.26953918026953,
			"y": 878.5986837307046,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 216.28550298089021,
			"seed": 996761780,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0,
					216.28550298089021
				]
			]
		},
		{
			"type": "line",
			"version": 275,
			"versionNonce": 1778821314,
			"isDeleted": false,
			"id": "xXdyia1D1JiRkB2hKXZiO",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -232.88998245585424,
			"y": 876.8354889646748,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 218.63642114889365,
			"seed": 587995404,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0,
					218.63642114889365
				]
			]
		},
		{
			"type": "line",
			"version": 255,
			"versionNonce": 497466462,
			"isDeleted": false,
			"id": "_A9OJ-pwRv_tohouKUdpQ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -135.91417208377925,
			"y": 876.2477410025923,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4210854715202004e-14,
			"height": 218.6364457090025,
			"seed": 571522612,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-1.4210854715202004e-14,
					218.6364457090025
				]
			]
		},
		{
			"type": "text",
			"version": 212,
			"versionNonce": 41435266,
			"isDeleted": false,
			"id": "2DmZEIqT",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -374.5334836210834,
			"y": 881.2392107569062,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.8839874267578125,
			"height": 45,
			"seed": 345287220,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "i",
			"rawText": "i",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "i",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 246,
			"versionNonce": 814448798,
			"isDeleted": false,
			"id": "DEVa3Mnx",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -377.738184848962,
			"y": 936.7332430805253,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.071990966796875,
			"height": 45,
			"seed": 30971,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "c",
			"rawText": "c",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "c",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 294,
			"versionNonce": 274784322,
			"isDeleted": false,
			"id": "7ycf7a5S",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -378.90669334135976,
			"y": 1000.5165438985978,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.287994384765625,
			"height": 45,
			"seed": 1617416372,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "b",
			"rawText": "b",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "b",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 225,
			"versionNonce": 1254997214,
			"isDeleted": false,
			"id": "c0wa1p3H",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -310.4706995218187,
			"y": 937.9596806141797,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 40.427978515625,
			"height": 45,
			"seed": 1373779980,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "-2",
			"rawText": "-2",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "-2",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 304,
			"versionNonce": 1604290562,
			"isDeleted": false,
			"id": "l1lIobLc",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -310.05712009709583,
			"y": 1005.3988479135728,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 40.427978515625,
			"height": 45,
			"seed": 2042707380,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "-2",
			"rawText": "-2",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "-2",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 382,
			"versionNonce": 301887774,
			"isDeleted": false,
			"id": "3kJnPgCX",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -197.8735675971846,
			"y": 1004.0359583597773,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 24.5159912109375,
			"height": 45,
			"seed": 1321648524,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "3",
			"rawText": "3",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "3",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 280,
			"versionNonce": 1748187074,
			"isDeleted": false,
			"id": "Hs8Xof1V",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -193.52255960808827,
			"y": 935.3979630329234,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 24.5159912109375,
			"height": 45,
			"seed": 16429,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "3",
			"rawText": "3",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "3",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "line",
			"version": 275,
			"versionNonce": 1368300894,
			"isDeleted": false,
			"id": "DPdaniCZ6m0CNJZ9vU7Yg",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -231.7145110917981,
			"y": 875.6600176006186,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 106.96730468649776,
			"height": 47.60630780302267,
			"seed": 748468108,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-106.96730468649776,
					47.60630780302267
				]
			]
		},
		{
			"type": "line",
			"version": 336,
			"versionNonce": 1245376386,
			"isDeleted": false,
			"id": "oxFFdOiiPuAPT7W8Z3Gw2",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -45.20106663800088,
			"y": 876.885370545511,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4210854715202004e-14,
			"height": 218.6364457090025,
			"seed": 55632052,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-1.4210854715202004e-14,
					218.6364457090025
				]
			]
		},
		{
			"type": "text",
			"version": 315,
			"versionNonce": 1053770142,
			"isDeleted": false,
			"id": "35nz1PfF",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -98.16911255532665,
			"y": 935.8560649932141,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 22.24798583984375,
			"height": 45,
			"seed": 1590568244,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "5",
			"rawText": "5",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "5",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 422,
			"versionNonce": 1240837954,
			"isDeleted": false,
			"id": "rxdgCHxq",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -100.37632952713511,
			"y": 1004.1627867612731,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 22.24798583984375,
			"height": 45,
			"seed": 1945017012,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "5",
			"rawText": "5",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "5",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 247,
			"versionNonce": 1022451166,
			"isDeleted": false,
			"id": "ipXd6bku",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -191.42247185191638,
			"y": 878.4626275405336,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.755996704101562,
			"height": 45,
			"seed": 2034140940,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "1",
			"rawText": "1",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "1",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 214,
			"versionNonce": 245909726,
			"isDeleted": false,
			"id": "t3MdNkAZ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -97.98000350132787,
			"y": 877.7872914185022,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 25.631988525390625,
			"height": 45,
			"seed": 33375,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341884851,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "2",
			"rawText": "2",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "2",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 298,
			"versionNonce": 554037790,
			"isDeleted": false,
			"id": "QhGI0iI4",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1.9510570225692732,
			"y": 875.9214667702865,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 24.5159912109375,
			"height": 45,
			"seed": 1886601868,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "3",
			"rawText": "3",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "3",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 352,
			"versionNonce": 1344292546,
			"isDeleted": false,
			"id": "9zoFYFZW",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -11.237317225113372,
			"y": 935.8292944746953,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 23.039993286132812,
			"height": 45,
			"seed": 621958196,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "4",
			"rawText": "4",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "4",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 448,
			"versionNonce": 1979579998,
			"isDeleted": false,
			"id": "UXQ3BzGS",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -7.447299485916858,
			"y": 1001.0606485474624,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 22.24798583984375,
			"height": 45,
			"seed": 780799156,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "5",
			"rawText": "5",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "5",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 1418,
			"versionNonce": 1873682050,
			"isDeleted": false,
			"id": "mFuFw2xX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 67.54477067148088,
			"y": 974.1606654205591,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 180.46875,
			"height": 33.6,
			"seed": 1330003124,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 3,
			"text": "[-2,3,2,-1]",
			"rawText": "[-2,3,2,-1]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "[-2,3,2,-1]",
			"lineHeight": 1.2,
			"baseline": 27
		},
		{
			"type": "text",
			"version": 396,
			"versionNonce": 1084916382,
			"isDeleted": false,
			"id": "Wivvn8jB",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 34.42056002148138,
			"y": -1795.4442915701327,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 127.79995727539062,
			"height": 45,
			"seed": 1044071092,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "[-3,1,-1]",
			"rawText": "[-3,1,-1]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "[-3,1,-1]",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 296,
			"versionNonce": 1462435394,
			"isDeleted": false,
			"id": "0Jg7gHHB",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -791.9423022984332,
			"y": -1225.8247936670562,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 463.2838134765625,
			"height": 45,
			"seed": 1240068020,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "2 Brute-force approaches",
			"rawText": "2 Brute-force approaches",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "2 Brute-force approaches",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 285,
			"versionNonce": 1136426718,
			"isDeleted": false,
			"id": "h5oejXSa",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1946.8304287347323,
			"y": 634.779201185694,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 173.4319305419922,
			"height": 35,
			"seed": 1257513996,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "max_so_far",
			"rawText": "max_so_far",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "max_so_far",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"id": "QsRL1jGq",
			"type": "text",
			"x": 81.74560258573831,
			"y": -1919.7060900019726,
			"width": 17.275985717773438,
			"height": 35,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1673855234,
			"version": 467,
			"versionNonce": 1136980766,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"text": "=",
			"rawText": "=",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "=",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 1053,
			"versionNonce": 2106447298,
			"isDeleted": false,
			"id": "MZgcE4LR",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1.6363156505958614,
			"y": -1892.2254192657958,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 215.93592834472656,
			"height": 35,
			"seed": 149379742,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Not a subarray",
			"rawText": "Not a subarray",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Not a subarray",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"id": "3A6RTFa6",
			"type": "text",
			"x": -1374.1742183539525,
			"y": -1013.5223712709846,
			"width": 475.78125,
			"height": 403.20000000000005,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1584613506,
			"version": 216,
			"versionNonce": 1261756254,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "JAs4vPuDjpsy0fNMQPdrQ",
					"type": "arrow"
				}
			],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"text": "int max_sum = 0\n    for(i = 0 to n-1)\n    {\n       for(j = i to n-1) \n       {  \n          int sum = 0\n          for(k = i to j)\n             sum = sum + A[k]\n          if(sum > max_sum)\n             max_sum = sum\n       }\n    } ",
			"rawText": "int max_sum = 0\n    for(i = 0 to n-1)\n    {\n       for(j = i to n-1) \n       {  \n          int sum = 0\n          for(k = i to j)\n             sum = sum + A[k]\n          if(sum > max_sum)\n             max_sum = sum\n       }\n    } ",
			"fontSize": 28,
			"fontFamily": 3,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 397,
			"containerId": null,
			"originalText": "int max_sum = 0\n    for(i = 0 to n-1)\n    {\n       for(j = i to n-1) \n       {  \n          int sum = 0\n          for(k = i to j)\n             sum = sum + A[k]\n          if(sum > max_sum)\n             max_sum = sum\n       }\n    } ",
			"lineHeight": 1.2
		},
		{
			"id": "KFASrgve",
			"type": "text",
			"x": -108.67034193314919,
			"y": -896.6892543319414,
			"width": 442.96875,
			"height": 369.6,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1060728962,
			"version": 106,
			"versionNonce": 1452395906,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"text": "int max_sum = 0\n    for ( i = 0 to n-1)\n    {   \n       sum=0\n       for( j = i to n-1) \n       {  \n         sum = sum +  A[j]\n         if (sum > max_sum)\n             max_sum = sum\n        }\n    }",
			"rawText": "int max_sum = 0\n    for ( i = 0 to n-1)\n    {   \n       sum=0\n       for( j = i to n-1) \n       {  \n         sum = sum +  A[j]\n         if (sum > max_sum)\n             max_sum = sum\n        }\n    }",
			"fontSize": 28,
			"fontFamily": 3,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 363,
			"containerId": null,
			"originalText": "int max_sum = 0\n    for ( i = 0 to n-1)\n    {   \n       sum=0\n       for( j = i to n-1) \n       {  \n         sum = sum +  A[j]\n         if (sum > max_sum)\n             max_sum = sum\n        }\n    }",
			"lineHeight": 1.2
		},
		{
			"id": "JAs4vPuDjpsy0fNMQPdrQ",
			"type": "arrow",
			"x": -666.2458813706979,
			"y": -1186.0210250116959,
			"width": 319.8685586875912,
			"height": 159.9342984389964,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 931829726,
			"version": 109,
			"versionNonce": 1851605918,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-319.8685586875912,
					159.9342984389964
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "3A6RTFa6",
				"focus": -0.4338848771263049,
				"gap": 12.56435530171484
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "6UD5Ts5M",
			"type": "text",
			"x": -916.2639568594329,
			"y": -1166.8407902749989,
			"width": 63.671966552734375,
			"height": 35,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [
				"3NeGhxFg83FXTF20Prmiz"
			],
			"frameId": null,
			"roundness": null,
			"seed": 229264606,
			"version": 80,
			"versionNonce": 599838018,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"text": "o(n )",
			"rawText": "o(n )",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "o(n )",
			"lineHeight": 1.25
		},
		{
			"id": "3SAyA6It",
			"type": "text",
			"x": -875.0989413580819,
			"y": -1167.0579645154003,
			"width": 11.672454320863622,
			"height": 21.42521752106538,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [
				"3NeGhxFg83FXTF20Prmiz"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1755493378,
			"version": 242,
			"versionNonce": 1166261250,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341884857,
			"link": null,
			"locked": false,
			"text": "3",
			"rawText": "3",
			"fontSize": 17.140174016852306,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "3",
			"lineHeight": 1.25
		},
		{
			"id": "X81lfEuh9Qaj3WmY-xueq",
			"type": "arrow",
			"x": -670.262732248894,
			"y": -1183.8895328219778,
			"width": 430.7425178193412,
			"height": 220.0129278549773,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2086475870,
			"version": 67,
			"versionNonce": 981062914,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					430.7425178193412,
					220.0129278549773
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"type": "text",
			"version": 267,
			"versionNonce": 578515998,
			"isDeleted": false,
			"id": "xXFJi4rE",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -400.4614575697741,
			"y": -1140.6900059924521,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 63.671966552734375,
			"height": 35,
			"seed": 157836702,
			"groupIds": [
				"0pbNqEgcMn7ScRBSsapuC"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "o(n )",
			"rawText": "o(n )",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "o(n )",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "text",
			"version": 405,
			"versionNonce": 312966430,
			"isDeleted": false,
			"id": "RgY5UCm5",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -359.2964420684233,
			"y": -1140.9071802328533,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 12.203798436754356,
			"height": 21.42521752106538,
			"seed": 549847518,
			"groupIds": [
				"0pbNqEgcMn7ScRBSsapuC"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341884857,
			"link": null,
			"locked": false,
			"fontSize": 17.140174016852306,
			"fontFamily": 1,
			"text": "2",
			"rawText": "2",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "2",
			"lineHeight": 1.25,
			"baseline": 15
		},
		{
			"id": "BgRI1moP",
			"type": "text",
			"x": 325.56261372338884,
			"y": -697.22317127321,
			"width": 150.16392517089844,
			"height": 35,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1129721282,
			"version": 184,
			"versionNonce": 1903378526,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"text": "running sum",
			"rawText": "running sum",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "running sum",
			"lineHeight": 1.25
		},
		{
			"id": "36mJaQ4P",
			"type": "text",
			"x": -777.3198523930378,
			"y": 92.5650219893522,
			"width": 202.35589599609375,
			"height": 35,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1146636062,
			"version": 229,
			"versionNonce": 44432514,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"text": "auxiliary array",
			"rawText": "auxiliary array",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "auxiliary array",
			"lineHeight": 1.25
		},
		{
			"id": "u8XKlzyT",
			"type": "text",
			"x": -707.8574058369793,
			"y": 180.0946927839801,
			"width": 52.97596740722656,
			"height": 35,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 794617602,
			"version": 88,
			"versionNonce": 1613202590,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"text": "[i-1]",
			"rawText": "[i-1]",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "[i-1]",
			"lineHeight": 1.25
		},
		{
			"id": "ndNXJmH1",
			"type": "text",
			"x": -1951.8965711048386,
			"y": 475.33376009905,
			"width": 16.743988037109375,
			"height": 35,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 845115102,
			"version": 220,
			"versionNonce": 997661762,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"text": "X",
			"rawText": "X",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "X",
			"lineHeight": 1.25
		},
		{
			"id": "lB16UA3cI_micQiwjcQLw",
			"type": "freedraw",
			"x": -2064.9093835890485,
			"y": 520.7500897581294,
			"width": 97.1698364792864,
			"height": 13.202421155917648,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 129498882,
			"version": 301,
			"versionNonce": 810107102,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.528088901731735
				],
				[
					0,
					-1.05619987153284
				],
				[
					0,
					-1.584288773264575
				],
				[
					0,
					-2.112377674996253
				],
				[
					0,
					-2.640488644797415
				],
				[
					0,
					-3.696666448260828
				],
				[
					0,
					-4.22477741806199
				],
				[
					0,
					-5.28097728959483
				],
				[
					0,
					-5.809066191326565
				],
				[
					0,
					-6.337155093058243
				],
				[
					0.5281109698011619,
					-6.865266062859405
				],
				[
					0.5281109698011619,
					-7.921443866322818
				],
				[
					0.5281109698011619,
					-8.449554836123923
				],
				[
					0.5281109698011619,
					-8.977643737855658
				],
				[
					1.05619987153284,
					-9.505732639587336
				],
				[
					1.05619987153284,
					-10.033843609388498
				],
				[
					1.584310841334002,
					-10.561932511120233
				],
				[
					2.11239974306568,
					-10.561932511120233
				],
				[
					2.640488644797415,
					-10.561932511120233
				],
				[
					3.168599614598577,
					-10.561932511120233
				],
				[
					3.696688516330255,
					-10.561932511120233
				],
				[
					4.752888387863095,
					-10.561932511120233
				],
				[
					5.809066191326508,
					-10.561932511120233
				],
				[
					6.865266062859405,
					-10.033843609388498
				],
				[
					8.449554836123923,
					-10.033843609388498
				],
				[
					10.033843609388498,
					-10.033843609388498
				],
				[
					12.146243352454178,
					-10.033843609388498
				],
				[
					14.258621027450488,
					-10.033843609388498
				],
				[
					15.842909800715006,
					-10.033843609388498
				],
				[
					19.011487347244156,
					-10.033843609388498
				],
				[
					20.595798188578158,
					-10.033843609388498
				],
				[
					23.23626476530609,
					-10.033843609388498
				],
				[
					26.404864379904666,
					-10.033843609388498
				],
				[
					29.045330956632654,
					-10.033843609388498
				],
				[
					31.157730699698334,
					-10.033843609388498
				],
				[
					33.79821934449575,
					-10.033843609388498
				],
				[
					35.91064115563091,
					-10.033843609388498
				],
				[
					38.551107732358844,
					-10.033843609388498
				],
				[
					40.66346333928567,
					-10.033843609388498
				],
				[
					43.303951984083085,
					-10.033843609388498
				],
				[
					45.41635172714882,
					-9.505732639587336
				],
				[
					48.05681830387675,
					-9.505732639587336
				],
				[
					50.69730694867417,
					-9.505732639587336
				],
				[
					52.809706691739905,
					-9.505732639587336
				],
				[
					55.45019533653732,
					-9.505732639587336
				],
				[
					57.562595079603,
					-9.505732639587336
				],
				[
					59.67499482266874,
					-9.505732639587336
				],
				[
					61.78735042959556,
					-9.505732639587336
				],
				[
					63.89975017266124,
					-9.505732639587336
				],
				[
					66.01210577958807,
					-8.977643737855658
				],
				[
					67.59646075706098,
					-8.977643737855658
				],
				[
					69.18072746225607,
					-8.977643737855658
				],
				[
					70.76499416745116,
					-8.977643737855658
				],
				[
					72.34930500878517,
					-8.977643737855658
				],
				[
					73.93357171398031,
					-8.977643737855658
				],
				[
					75.51788255531432,
					-8.449554836123923
				],
				[
					76.57406035877773,
					-8.449554836123923
				],
				[
					78.15837120011173,
					-8.449554836123923
				],
				[
					79.21454900357514,
					-8.449554836123923
				],
				[
					80.27072680703856,
					-8.449554836123923
				],
				[
					81.32694874664082,
					-8.449554836123923
				],
				[
					81.85503764837256,
					-7.921443866322818
				],
				[
					82.38312655010424,
					-7.921443866322818
				],
				[
					82.91121545183597,
					-7.921443866322818
				],
				[
					83.43934848970656,
					-7.921443866322818
				],
				[
					83.96743739143824,
					-7.921443866322818
				],
				[
					84.49552629316997,
					-7.921443866322818
				],
				[
					85.55170409663339,
					-7.921443866322818
				],
				[
					86.07983713450398,
					-7.393354964591083
				],
				[
					86.60792603623565,
					-7.393354964591083
				],
				[
					87.13601493796739,
					-7.393354964591083
				],
				[
					87.66410383969907,
					-7.393354964591083
				],
				[
					88.19219274143074,
					-7.393354964591083
				],
				[
					88.72032577930133,
					-7.393354964591083
				],
				[
					89.24837054489416,
					-7.393354964591083
				],
				[
					89.77650358276475,
					-7.393354964591083
				],
				[
					90.83268138622816,
					-7.393354964591083
				],
				[
					91.36081442409875,
					-7.393354964591083
				],
				[
					92.41694809142331,
					-7.393354964591083
				],
				[
					92.9450811292939,
					-7.393354964591083
				],
				[
					93.47317003102557,
					-7.393354964591083
				],
				[
					94.00130306889616,
					-7.393354964591083
				],
				[
					94.52934783448899,
					-7.393354964591083
				],
				[
					95.05743673622072,
					-7.393354964591083
				],
				[
					95.58556977409131,
					-7.393354964591083
				],
				[
					96.11365867582299,
					-7.393354964591083
				],
				[
					96.64179171369358,
					-7.393354964591083
				],
				[
					96.64179171369358,
					-6.865266062859405
				],
				[
					97.1698364792864,
					-6.865266062859405
				],
				[
					97.1698364792864,
					-6.337155093058243
				],
				[
					97.1698364792864,
					-5.809066191326565
				],
				[
					97.1698364792864,
					-5.28097728959483
				],
				[
					97.1698364792864,
					-4.752866319793668
				],
				[
					97.1698364792864,
					-3.696666448260828
				],
				[
					97.1698364792864,
					-3.16857754652915
				],
				[
					97.1698364792864,
					-2.640488644797415
				],
				[
					96.64179171369358,
					-1.584288773264575
				],
				[
					96.64179171369358,
					-1.05619987153284
				],
				[
					96.11365867582299,
					-0.528088901731735
				],
				[
					96.11365867582299,
					0
				],
				[
					96.11365867582299,
					0.5280889017316781
				],
				[
					95.58556977409131,
					1.05619987153284
				],
				[
					95.58556977409131,
					1.584288773264575
				],
				[
					95.58556977409131,
					2.11239974306568
				],
				[
					95.58556977409131,
					2.640488644797415
				],
				[
					95.05743673622072,
					2.640488644797415
				],
				[
					95.05743673622072,
					2.640488644797415
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				95.05743673622072,
				2.640488644797415
			]
		},
		{
			"id": "9KsECvpH",
			"type": "text",
			"x": -2032.167342048016,
			"y": 474.2775602275172,
			"width": 21.44036351917367,
			"height": 35,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1659122014,
			"version": 259,
			"versionNonce": 1802562498,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341884858,
			"link": null,
			"locked": false,
			"text": "M",
			"rawText": "M",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "M",
			"lineHeight": 1.25
		},
		{
			"id": "4RT47OD3X9o-eujMLWYpR",
			"type": "arrow",
			"x": -2021.0773427032336,
			"y": 486.9518924817031,
			"width": 94.00125893275731,
			"height": 44.360129787546526,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1180747102,
			"version": 474,
			"versionNonce": 1164539166,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-27.989131085099814,
					-44.360129787546526
				],
				[
					-94.00125893275731,
					-30.101530828165494
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "w2J2FrYn",
			"type": "text",
			"x": -765.438221920044,
			"y": 138.80579799806713,
			"width": 176.00662231445312,
			"height": 29.58698724444567,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2083342494,
			"version": 197,
			"versionNonce": 1899374942,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341884859,
			"link": null,
			"locked": false,
			"text": "aux[0] = a[0]",
			"rawText": "aux[0] = a[0]",
			"fontSize": 23.669589795556536,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 20,
			"containerId": null,
			"originalText": "aux[0] = a[0]",
			"lineHeight": 1.25
		},
		{
			"id": "CgXdnYJw",
			"type": "text",
			"x": -761.2135769103998,
			"y": 219.47254513877374,
			"width": 147.50392150878906,
			"height": 70,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1731980098,
			"version": 162,
			"versionNonce": 1761157470,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"text": "time: o(n)\nspace: o(n)",
			"rawText": "time: o(n)\nspace: o(n)",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 59,
			"containerId": null,
			"originalText": "time: o(n)\nspace: o(n)",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 1484,
			"versionNonce": 397060994,
			"isDeleted": false,
			"id": "NE4WNp2I",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -196.27277717999954,
			"y": 145.18973152192123,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 213.28125,
			"height": 33.6,
			"seed": 997741470,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "69HLsSuPiqwyC1qfiNasl",
					"type": "arrow"
				},
				{
					"id": "fqJL1VAClKjC7rcwvHa_b",
					"type": "arrow"
				}
			],
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 3,
			"text": "[1,-3,2,1,-1]",
			"rawText": "[1,-3,2,1,-1]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "[1,-3,2,1,-1]",
			"lineHeight": 1.2,
			"baseline": 27
		},
		{
			"id": "69HLsSuPiqwyC1qfiNasl",
			"type": "arrow",
			"x": -172.21336172140934,
			"y": 224.47575703003017,
			"width": 0,
			"height": 42.77586308235135,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1771310338,
			"version": 404,
			"versionNonce": 239682974,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826062,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-42.77586308235135
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "NE4WNp2I",
				"focus": 0.7743878989963702,
				"gap": 2.910162425757605
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"type": "arrow",
			"version": 667,
			"versionNonce": 1242426178,
			"isDeleted": false,
			"id": "fqJL1VAClKjC7rcwvHa_b",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -124.11519912546873,
			"y": 224.03766051694052,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.3840258595830619,
			"height": 44.247928995019265,
			"seed": 659734430,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "DIUorbzF",
				"focus": -1.5281946903178687,
				"gap": 12.632965894052745
			},
			"endBinding": {
				"elementId": "NE4WNp2I",
				"focus": 0.31787311541980434,
				"gap": 1.0000000000000426
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0.3840258595830619,
					-44.247928995019265
				]
			]
		},
		{
			"id": "6Z91gYv1RZ0b_lWrbB5ih",
			"type": "freedraw",
			"x": -181.71916056520502,
			"y": 157.4074293108398,
			"width": 74.98981572165212,
			"height": 20.067687218776996,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 222408514,
			"version": 193,
			"versionNonce": 378200542,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5280889017316781,
					-0.5280889017317065
				],
				[
					0.5280889017316781,
					-1.5842887732645465
				],
				[
					0.5280889017316781,
					-2.6404665767279596
				],
				[
					1.056221939602267,
					-3.696666448260828
				],
				[
					1.056221939602267,
					-4.752844251724241
				],
				[
					1.584310841334002,
					-5.8090661913265365
				],
				[
					1.584310841334002,
					-7.393332896521656
				],
				[
					1.584310841334002,
					-8.449532768054496
				],
				[
					2.11239974306568,
					-9.505732639587364
				],
				[
					2.11239974306568,
					-10.561932511120204
				],
				[
					2.11239974306568,
					-11.618132382653044
				],
				[
					2.11239974306568,
					-12.674310186116458
				],
				[
					2.640488644797415,
					-13.730510057649326
				],
				[
					2.640488644797415,
					-14.258598959381033
				],
				[
					2.640488644797415,
					-14.786709929182166
				],
				[
					3.168577546529093,
					-14.786709929182166
				],
				[
					3.696710584399682,
					-15.314776762844446
				],
				[
					4.224799486131417,
					-15.314776762844446
				],
				[
					4.752888387863095,
					-15.314776762844446
				],
				[
					5.28097728959483,
					-15.842887732645579
				],
				[
					6.337199229197097,
					-15.842887732645579
				],
				[
					7.39337703266051,
					-16.37099870244674
				],
				[
					8.977687873994512,
					-16.37099870244674
				],
				[
					10.56195457918966,
					-16.37099870244674
				],
				[
					12.146221284384751,
					-16.37099870244674
				],
				[
					13.730532125718753,
					-16.37099870244674
				],
				[
					15.314798830913901,
					-16.899087604178447
				],
				[
					17.42719857397958,
					-16.899087604178447
				],
				[
					19.53964245318417,
					-16.899087604178447
				],
				[
					22.180086961842676,
					-16.899087604178447
				],
				[
					25.348664508371826,
					-16.899087604178447
				],
				[
					27.98915315316924,
					-16.899087604178447
				],
				[
					31.157730699698277,
					-16.899087604178447
				],
				[
					34.32630824622743,
					-16.899087604178447
				],
				[
					38.023018830627166,
					-16.899087604178447
				],
				[
					44.88826282541709,
					-16.899087604178447
				],
				[
					46.47252953061229,
					-16.899087604178447
				],
				[
					49.11301817540971,
					-16.899087604178447
				],
				[
					51.75350682020712,
					-16.899087604178447
				],
				[
					53.8659065632728,
					-16.899087604178447
				],
				[
					55.978262170199514,
					-16.899087604178447
				],
				[
					58.09066191326531,
					-16.899087604178447
				],
				[
					59.67497275459925,
					-16.899087604178447
				],
				[
					61.259239459794344,
					-16.899087604178447
				],
				[
					62.31546139939667,
					-16.899087604178447
				],
				[
					63.89972810459176,
					-16.899087604178447
				],
				[
					64.95590590805523,
					-17.42719857397958
				],
				[
					66.54021674938917,
					-17.42719857397958
				],
				[
					67.59639455285264,
					-17.42719857397958
				],
				[
					68.65261649245485,
					-17.42719857397958
				],
				[
					69.70883843205729,
					-17.42719857397958
				],
				[
					70.23688319765006,
					-17.42719857397958
				],
				[
					71.29310513725227,
					-17.42719857397958
				],
				[
					71.821194038984,
					-17.42719857397958
				],
				[
					72.87737184244747,
					-17.42719857397958
				],
				[
					73.40546074417921,
					-17.42719857397958
				],
				[
					73.93359378204968,
					-17.42719857397958
				],
				[
					74.46168268378142,
					-17.42719857397958
				],
				[
					74.98981572165212,
					-17.42719857397958
				],
				[
					74.98981572165212,
					-16.899087604178447
				],
				[
					74.98981572165212,
					-16.37099870244674
				],
				[
					74.98981572165212,
					-15.842887732645579
				],
				[
					74.98981572165212,
					-15.314776762844446
				],
				[
					74.98981572165212,
					-14.786709929182166
				],
				[
					74.98981572165212,
					-14.258598959381033
				],
				[
					74.98981572165212,
					-13.730510057649326
				],
				[
					74.98981572165212,
					-13.20242115591762
				],
				[
					74.98981572165212,
					-12.674310186116458
				],
				[
					74.98981572165212,
					-11.618132382653044
				],
				[
					74.98981572165212,
					-10.561932511120204
				],
				[
					74.98981572165212,
					-9.505732639587364
				],
				[
					74.98981572165212,
					-8.449532768054496
				],
				[
					74.98981572165212,
					-7.393332896521656
				],
				[
					74.98981572165212,
					-6.337155093058243
				],
				[
					74.98981572165212,
					-5.2809552215253746
				],
				[
					74.98981572165212,
					-4.2247553499925345
				],
				[
					74.98981572165212,
					-3.696666448260828
				],
				[
					74.98981572165212,
					-2.6404665767279596
				],
				[
					74.98981572165212,
					-2.112355606926826
				],
				[
					74.98981572165212,
					-1.056177803463413
				],
				[
					74.98981572165212,
					-0.5280889017317065
				],
				[
					74.98981572165212,
					0
				],
				[
					74.98981572165212,
					0.5281330378705889
				],
				[
					74.98981572165212,
					1.05619987153284
				],
				[
					74.98981572165212,
					1.584310841334002
				],
				[
					74.46168268378142,
					1.584310841334002
				],
				[
					74.46168268378142,
					2.1123997430657084
				],
				[
					74.46168268378142,
					2.640488644797415
				],
				[
					74.46168268378142,
					2.640488644797415
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				74.46168268378142,
				2.640488644797415
			]
		},
		{
			"type": "arrow",
			"version": 546,
			"versionNonce": 359871234,
			"isDeleted": false,
			"id": "V8zzYSrjsx7GkU-SLHFu_",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -89.69683972382109,
			"y": 213.9173554100206,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.2851475575407676,
			"height": 35.910597019492,
			"seed": 294237534,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "DIUorbzF",
				"focus": -0.09644898252980365,
				"gap": 14.78313490193267
			},
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0.2851475575407676,
					-35.910597019492
				]
			]
		},
		{
			"id": "DIUorbzF",
			"type": "text",
			"x": -111.48223323141599,
			"y": 228.70049031195327,
			"width": 47.68397521972656,
			"height": 35,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1759283394,
			"version": 204,
			"versionNonce": 349107742,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "fqJL1VAClKjC7rcwvHa_b",
					"type": "arrow"
				},
				{
					"id": "V8zzYSrjsx7GkU-SLHFu_",
					"type": "arrow"
				}
			],
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"text": "[2]",
			"rawText": "[2]",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "[2]",
			"lineHeight": 1.25
		},
		{
			"id": "Tq5h12El",
			"type": "text",
			"x": -162.70769528603034,
			"y": 263.0268426943196,
			"width": 100.23995971679688,
			"height": 35,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 357536322,
			"version": 202,
			"versionNonce": 475628226,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "2FOqPsIn00IXoUinGbG4w",
					"type": "arrow"
				}
			],
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"text": "[1,-3,2]",
			"rawText": "[1,-3,2]",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "[1,-3,2]",
			"lineHeight": 1.25
		},
		{
			"id": "62qvaqS6A3DCORBy9jNFK",
			"type": "freedraw",
			"x": -150.56142986550674,
			"y": 282.0383079734943,
			"width": 49.11301817540971,
			"height": 20.067687218776996,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 195813342,
			"version": 185,
			"versionNonce": 302416478,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5281330378705889
				],
				[
					0,
					1.0561998715328969
				],
				[
					0,
					1.584288773264575
				],
				[
					0.528088901731735,
					2.640488644797415
				],
				[
					0.528088901731735,
					3.696688516330312
				],
				[
					1.05617780346347,
					4.752866319793725
				],
				[
					1.5843108413340588,
					5.809110327465419
				],
				[
					1.5843108413340588,
					6.865266062859405
				],
				[
					2.1123997430657937,
					7.921465934392245
				],
				[
					2.1123997430657937,
					8.977665805925085
				],
				[
					2.640488644797415,
					10.033843609388498
				],
				[
					2.640488644797415,
					11.090065548990822
				],
				[
					3.16857754652915,
					12.146243352454235
				],
				[
					3.16857754652915,
					13.202421155917648
				],
				[
					3.16857754652915,
					13.730554193788237
				],
				[
					3.696666448260885,
					14.78673199725165
				],
				[
					3.696666448260885,
					15.314820898983328
				],
				[
					3.696666448260885,
					15.842909800715063
				],
				[
					3.696666448260885,
					16.899087604178476
				],
				[
					3.696666448260885,
					17.427220642049065
				],
				[
					3.696666448260885,
					17.955309543780743
				],
				[
					4.224799486131474,
					17.955309543780743
				],
				[
					4.752844251724355,
					17.955309543780743
				],
				[
					5.28097728959483,
					17.955309543780743
				],
				[
					6.3371550930583,
					17.955309543780743
				],
				[
					7.39333289652177,
					17.955309543780743
				],
				[
					8.977643737855715,
					17.955309543780743
				],
				[
					10.561910443050806,
					17.955309543780743
				],
				[
					11.61813238265313,
					17.955309543780743
				],
				[
					13.202399087848221,
					17.955309543780743
				],
				[
					15.314798830914015,
					17.955309543780743
				],
				[
					16.89910967224796,
					17.955309543780743
				],
				[
					19.011465279174786,
					17.955309543780743
				],
				[
					20.595776120508845,
					17.955309543780743
				],
				[
					22.708175863574525,
					17.955309543780743
				],
				[
					24.292442568769616,
					17.955309543780743
				],
				[
					25.876753410103674,
					17.955309543780743
				],
				[
					27.989153153169354,
					17.955309543780743
				],
				[
					30.101508760096067,
					18.483398445512478
				],
				[
					31.685819601430126,
					18.483398445512478
				],
				[
					33.270130442764184,
					18.483398445512478
				],
				[
					35.3824860496909,
					18.483398445512478
				],
				[
					36.966796891024956,
					18.483398445512478
				],
				[
					38.551107732359014,
					18.483398445512478
				],
				[
					40.13537443755399,
					18.483398445512478
				],
				[
					41.19159637715643,
					18.483398445512478
				],
				[
					42.24773004448093,
					18.483398445512478
				],
				[
					43.832085021953844,
					18.483398445512478
				],
				[
					44.36012978754661,
					18.483398445512478
				],
				[
					45.41630759101008,
					18.483398445512478
				],
				[
					45.94444062888056,
					18.483398445512478
				],
				[
					47.00061843234403,
					18.483398445512478
				],
				[
					47.52870733407576,
					18.483398445512478
				],
				[
					48.05679623580738,
					18.483398445512478
				],
				[
					48.05679623580738,
					17.955309543780743
				],
				[
					48.58492927367797,
					17.955309543780743
				],
				[
					48.58492927367797,
					17.427220642049065
				],
				[
					49.11301817540971,
					16.899087604178476
				],
				[
					49.11301817540971,
					16.37104283858565
				],
				[
					49.11301817540971,
					15.842909800715063
				],
				[
					49.11301817540971,
					15.314820898983328
				],
				[
					49.11301817540971,
					14.78673199725165
				],
				[
					49.11301817540971,
					14.258643095519915
				],
				[
					49.11301817540971,
					13.202421155917648
				],
				[
					49.11301817540971,
					12.674332254185913
				],
				[
					49.11301817540971,
					11.6181544507225
				],
				[
					49.11301817540971,
					11.090065548990822
				],
				[
					49.11301817540971,
					9.50575470765682
				],
				[
					49.11301817540971,
					8.449576904193407
				],
				[
					49.11301817540971,
					7.921465934392245
				],
				[
					49.11301817540971,
					6.865266062859405
				],
				[
					49.11301817540971,
					5.809110327465419
				],
				[
					49.11301817540971,
					4.752866319793725
				],
				[
					49.11301817540971,
					3.696688516330312
				],
				[
					49.11301817540971,
					3.168621682668004
				],
				[
					49.11301817540971,
					2.112399743065737
				],
				[
					49.11301817540971,
					1.584288773264575
				],
				[
					49.11301817540971,
					0.5281330378705889
				],
				[
					49.11301817540971,
					0
				],
				[
					49.11301817540971,
					-0.5280889017316781
				],
				[
					49.11301817540971,
					-1.05619987153284
				],
				[
					49.11301817540971,
					-1.5842887732645181
				],
				[
					49.11301817540971,
					-1.5842887732645181
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				49.11301817540971,
				-1.5842887732645181
			]
		},
		{
			"id": "2FOqPsIn00IXoUinGbG4w",
			"type": "arrow",
			"x": -220.79831306315674,
			"y": 330.98999888710273,
			"width": 73.93354964591089,
			"height": 32.21390850316175,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 760039710,
			"version": 261,
			"versionNonce": 1499454082,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					73.93354964591089,
					-32.21390850316175
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "Tq5h12El",
				"focus": -0.08425050804136137,
				"gap": 1
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "UhQqyLqd",
			"type": "text",
			"x": -363.91261223939307,
			"y": 324.28610422218344,
			"width": 232.4558868408203,
			"height": 35,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1332131458,
			"version": 195,
			"versionNonce": 1359120030,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"text": "max_ending_here",
			"rawText": "max_ending_here",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "max_ending_here",
			"lineHeight": 1.25
		},
		{
			"id": "9drGLPWo2EWzoXNp8UK-M",
			"type": "freedraw",
			"x": -67.6501261413922,
			"y": 240.3186668307452,
			"width": 19.011465279174672,
			"height": 21.651975992041514,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1026126530,
			"version": 141,
			"versionNonce": 457521730,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5280889017316213,
					0
				],
				[
					1.0561778034633562,
					0
				],
				[
					1.5842667051950912,
					0
				],
				[
					2.640488644797415,
					0
				],
				[
					4.224755349992506,
					0
				],
				[
					5.28097728959483,
					0
				],
				[
					6.865243994789921,
					0
				],
				[
					7.921465934392245,
					0
				],
				[
					9.505732639587336,
					0
				],
				[
					11.089999344782427,
					0
				],
				[
					12.674310186116486,
					0
				],
				[
					14.258621027450431,
					0
				],
				[
					15.314798830913901,
					0
				],
				[
					16.370976634377257,
					0
				],
				[
					16.899065536108992,
					0
				],
				[
					17.42719857397958,
					0
				],
				[
					17.955287475711202,
					0.5280889017316781
				],
				[
					18.48342051358179,
					1.05619987153284
				],
				[
					18.48342051358179,
					2.112377674996253
				],
				[
					18.48342051358179,
					3.168577546529093
				],
				[
					18.48342051358179,
					4.22479948613136
				],
				[
					18.48342051358179,
					5.280977289594773
				],
				[
					18.48342051358179,
					6.337155093058186
				],
				[
					18.48342051358179,
					7.393354964591083
				],
				[
					18.48342051358179,
					8.449554836123923
				],
				[
					18.48342051358179,
					9.50577677572619
				],
				[
					18.48342051358179,
					10.033843609388498
				],
				[
					18.48342051358179,
					11.090043480921338
				],
				[
					18.48342051358179,
					12.146265420523605
				],
				[
					18.48342051358179,
					13.202421155917591
				],
				[
					18.48342051358179,
					14.78675406532102
				],
				[
					18.48342051358179,
					15.842909800715006
				],
				[
					18.48342051358179,
					16.899109672247846
				],
				[
					18.48342051358179,
					17.955309543780686
				],
				[
					19.011465279174672,
					18.48339844551242
				],
				[
					19.011465279174672,
					19.539576248975834
				],
				[
					19.011465279174672,
					20.067709286846423
				],
				[
					19.011465279174672,
					21.123887090309836
				],
				[
					19.011465279174672,
					21.651975992041514
				],
				[
					19.011465279174672,
					21.651975992041514
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				19.011465279174672,
				21.651975992041514
			]
		},
		{
			"id": "ZVvHm3EaPwkFyKqYgGayc",
			"type": "freedraw",
			"x": -65.00963749659479,
			"y": 276.7573527519689,
			"width": 21.651953923972087,
			"height": 16.370976634377257,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1338884162,
			"version": 152,
			"versionNonce": 309592798,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.5842667051950912,
					0
				],
				[
					2.112355606926826,
					0
				],
				[
					3.1685775465290362,
					0
				],
				[
					4.752844251724241,
					0
				],
				[
					5.809066191326451,
					0
				],
				[
					6.865243994789921,
					0
				],
				[
					7.921465934392245,
					0
				],
				[
					8.977643737855601,
					0
				],
				[
					10.033821541319071,
					0
				],
				[
					11.089999344782427,
					0
				],
				[
					11.618132382653016,
					0
				],
				[
					13.202443223986961,
					0
				],
				[
					13.730487989579842,
					0
				],
				[
					14.786709929182166,
					0
				],
				[
					15.314798830913787,
					0
				],
				[
					16.370976634377257,
					0
				],
				[
					17.42719857397958,
					0
				],
				[
					17.955287475711202,
					0
				],
				[
					18.48342051358179,
					0
				],
				[
					19.011465279174672,
					0
				],
				[
					19.539554180906407,
					0
				],
				[
					20.06764308263803,
					-0.5280447655928242
				],
				[
					20.595776120508617,
					-0.5280447655928242
				],
				[
					21.123909158379206,
					-0.5280447655928242
				],
				[
					21.651953923972087,
					-0.5280447655928242
				],
				[
					21.651953923972087,
					-1.056177803463413
				],
				[
					21.123909158379206,
					-1.056177803463413
				],
				[
					21.123909158379206,
					-1.5842667051950912
				],
				[
					20.595776120508617,
					-2.11239974306568
				],
				[
					20.595776120508617,
					-2.640488644797358
				],
				[
					20.06764308263803,
					-3.1685334103901823
				],
				[
					20.06764308263803,
					-3.696666448260771
				],
				[
					19.539554180906407,
					-4.224755349992506
				],
				[
					19.539554180906407,
					-4.752888387863095
				],
				[
					19.011465279174672,
					-5.280977289594773
				],
				[
					19.011465279174672,
					-5.809022055187597
				],
				[
					18.48342051358179,
					-6.865243994789921
				],
				[
					17.955287475711202,
					-7.393332896521599
				],
				[
					17.955287475711202,
					-8.977643737855601
				],
				[
					17.42719857397958,
					-10.033821541319014
				],
				[
					16.899065536108992,
					-11.089999344782427
				],
				[
					16.899065536108992,
					-11.618132382653016
				],
				[
					16.370976634377257,
					-12.67431018611643
				],
				[
					16.370976634377257,
					-13.730487989579842
				],
				[
					15.842931868784376,
					-14.258621027450431
				],
				[
					15.842931868784376,
					-14.786709929182166
				],
				[
					15.842931868784376,
					-15.314798830913844
				],
				[
					15.842931868784376,
					-15.842887732645579
				],
				[
					15.314798830913787,
					-15.842887732645579
				],
				[
					15.314798830913787,
					-16.370976634377257
				],
				[
					15.314798830913787,
					-16.370976634377257
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				15.314798830913787,
				-16.370976634377257
			]
		},
		{
			"id": "zFbC1jFjwwVBRIPg5gTlp",
			"type": "freedraw",
			"x": -49.694838665681004,
			"y": 260.3863761175916,
			"width": 24.820531470501237,
			"height": 1.056177803463413,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1242401538,
			"version": 128,
			"versionNonce": 15245826,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5281330378705889,
					0
				],
				[
					1.05617780346347,
					0
				],
				[
					2.1123997430657937,
					0
				],
				[
					3.168621682668004,
					0
				],
				[
					4.22475534999262,
					0
				],
				[
					5.28097728959483,
					0
				],
				[
					6.865243994790035,
					0
				],
				[
					7.921465934392245,
					0
				],
				[
					9.50573263958745,
					0
				],
				[
					10.561910443050806,
					0
				],
				[
					12.146221284384865,
					0
				],
				[
					13.202399087848221,
					0
				],
				[
					14.78670992918228,
					0
				],
				[
					15.842887732645636,
					0
				],
				[
					17.42719857397958,
					0.5280889017316781
				],
				[
					18.48337637744305,
					0.5280889017316781
				],
				[
					19.53959831704526,
					0.5280889017316781
				],
				[
					20.59577612050873,
					0.5280889017316781
				],
				[
					21.123865022240466,
					1.056177803463413
				],
				[
					21.651953923972087,
					1.056177803463413
				],
				[
					22.180042825703822,
					1.056177803463413
				],
				[
					22.70817586357441,
					1.056177803463413
				],
				[
					23.236264765306146,
					1.056177803463413
				],
				[
					23.76435366703788,
					1.056177803463413
				],
				[
					24.292442568769502,
					1.056177803463413
				],
				[
					24.820531470501237,
					1.056177803463413
				],
				[
					24.820531470501237,
					1.056177803463413
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				24.820531470501237,
				1.056177803463413
			]
		},
		{
			"id": "0Xqf7R4a50DBDDvV6obmv",
			"type": "freedraw",
			"x": -25.930484998643124,
			"y": 257.7458874727942,
			"width": 12.146221284384751,
			"height": 7.921465934392245,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 873219010,
			"version": 128,
			"versionNonce": 1491859230,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5280889017316213,
					0
				],
				[
					1.0561778034633562,
					0
				],
				[
					1.584310841333945,
					0
				],
				[
					2.11239974306568,
					0
				],
				[
					2.640488644797415,
					0
				],
				[
					3.1685775465290362,
					0
				],
				[
					4.224755349992506,
					0
				],
				[
					5.809066191326451,
					0.5280889017316781
				],
				[
					6.865243994789921,
					1.056177803463413
				],
				[
					7.921465934392245,
					1.5842667051950912
				],
				[
					8.977643737855601,
					2.112355606926826
				],
				[
					10.033821541319071,
					2.640488644797415
				],
				[
					11.090043480921281,
					3.168577546529093
				],
				[
					11.618132382653016,
					3.168577546529093
				],
				[
					12.146221284384751,
					3.696666448260828
				],
				[
					11.090043480921281,
					4.224755349992506
				],
				[
					10.56195457918966,
					4.224755349992506
				],
				[
					9.505732639587336,
					4.224755349992506
				],
				[
					8.977643737855601,
					4.752844251724241
				],
				[
					8.449554836123866,
					5.28097728959483
				],
				[
					7.921465934392245,
					5.28097728959483
				],
				[
					7.39337703266051,
					5.809066191326508
				],
				[
					7.39337703266051,
					6.337155093058243
				],
				[
					6.865243994789921,
					6.865243994789921
				],
				[
					6.865243994789921,
					7.393332896521656
				],
				[
					6.865243994789921,
					7.921465934392245
				],
				[
					6.865243994789921,
					7.921465934392245
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				6.865243994789921,
				7.921465934392245
			]
		},
		{
			"id": "g7uve15V",
			"type": "text",
			"x": -3.7503980368005614,
			"y": 247.1839328936046,
			"width": 47.68397521972656,
			"height": 35,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 581518466,
			"version": 120,
			"versionNonce": 1967722946,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"text": "[2]",
			"rawText": "[2]",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "[2]",
			"lineHeight": 1.25
		},
		{
			"id": "XYVLgQ82",
			"type": "text",
			"x": 52.7559530351308,
			"y": 242.43111070994973,
			"width": 232.4558868408203,
			"height": 35,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1231012510,
			"version": 161,
			"versionNonce": 752575326,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"text": "max_ending_here",
			"rawText": "max_ending_here",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "max_ending_here",
			"lineHeight": 1.25
		},
		{
			"id": "yCvqda-EuFsk73lOBlz6_",
			"type": "rectangle",
			"x": -1936.2468407480656,
			"y": 517.0270078289986,
			"width": 202.3528188458048,
			"height": 33.06418680836475,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 552196382,
			"version": 380,
			"versionNonce": 730171778,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false
		},
		{
			"id": "oHNNwbsES_qk7ZzQl7rsY",
			"type": "freedraw",
			"x": -1920.376048765601,
			"y": 517.0270354626714,
			"width": 1.9838766314808254,
			"height": 30.41903638883889,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [
				"iXdoNdV_KiixFLWYBAcet"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1350151774,
			"version": 293,
			"versionNonce": 1620264862,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6612737880450936
				],
				[
					0,
					1.322547576090244
				],
				[
					-0.6612185206997765,
					1.9838489978080815
				],
				[
					-0.6612185206997765,
					2.645122785853175
				],
				[
					-0.6612185206997765,
					3.967697995616163
				],
				[
					-0.6612185206997765,
					4.628971783661257
				],
				[
					-0.6612185206997765,
					5.951546993424188
				],
				[
					-0.6612185206997765,
					7.274122203187176
				],
				[
					-0.6612185206997765,
					7.935395991232269
				],
				[
					-0.6612185206997765,
					9.2579712009952
				],
				[
					-0.6612185206997765,
					9.919244989040351
				],
				[
					-0.6612185206997765,
					11.241820198803282
				],
				[
					-0.6612185206997765,
					11.903093986848432
				],
				[
					-0.6612185206997765,
					13.225669196611364
				],
				[
					-0.6612185206997765,
					13.886942984656457
				],
				[
					-0.6612185206997765,
					14.548244406374295
				],
				[
					-0.6612185206997765,
					15.209518194419445
				],
				[
					-0.6612185206997765,
					15.870791982464539
				],
				[
					-0.6612185206997765,
					16.532093404182376
				],
				[
					-0.6612185206997765,
					17.193367192227527
				],
				[
					-0.6612185206997765,
					17.85464098027262
				],
				[
					-0.6612185206997765,
					18.515942401990458
				],
				[
					-0.6612185206997765,
					19.17721619003555
				],
				[
					-0.6612185206997765,
					19.83851761175339
				],
				[
					-0.6612185206997765,
					20.49979139979854
				],
				[
					-0.6612185206997765,
					21.161065187843633
				],
				[
					-0.6612185206997765,
					21.82236660956147
				],
				[
					-1.322547576090301,
					22.483640397606564
				],
				[
					-1.322547576090301,
					23.144914185651714
				],
				[
					-1.322547576090301,
					23.806215607369552
				],
				[
					-1.322547576090301,
					24.467489395414646
				],
				[
					-1.322547576090301,
					25.128763183459796
				],
				[
					-1.322547576090301,
					25.790064605177633
				],
				[
					-1.322547576090301,
					26.451338393222727
				],
				[
					-1.322547576090301,
					27.112639814940565
				],
				[
					-1.9838766314808254,
					27.773913602985658
				],
				[
					-1.9838766314808254,
					28.43518739103081
				],
				[
					-1.9838766314808254,
					29.096488812748646
				],
				[
					-1.9838766314808254,
					29.75776260079374
				],
				[
					-1.9838766314808254,
					30.41903638883889
				],
				[
					-1.9838766314808254,
					30.41903638883889
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-1.9838766314808254,
				30.41903638883889
			]
		},
		{
			"id": "J1D_IRGIMu6RmXvc3CRhS",
			"type": "freedraw",
			"x": -1921.0372672863007,
			"y": 517.0270354626714,
			"width": 60.838128045023154,
			"height": 33.7254605964099,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [
				"iXdoNdV_KiixFLWYBAcet"
			],
			"frameId": null,
			"roundness": null,
			"seed": 85011742,
			"version": 403,
			"versionNonce": 450693442,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6612185206997765,
					0
				],
				[
					1.9837660967899637,
					0
				],
				[
					3.3063689402256387,
					0
				],
				[
					5.290190304360976,
					0
				],
				[
					7.274066935841802,
					0
				],
				[
					9.25788829997714,
					0
				],
				[
					11.241764931457965,
					0.6612737880450936
				],
				[
					13.225641562938677,
					0.6612737880450936
				],
				[
					15.870736715119165,
					0.6612737880450936
				],
				[
					17.85461334659999,
					0.6612737880450936
				],
				[
					19.838489978080702,
					0.6612737880450936
				],
				[
					21.822311342216153,
					0.6612737880450936
				],
				[
					24.467461761742015,
					0.6612737880450936
				],
				[
					26.451338393222727,
					0.6612737880450936
				],
				[
					28.43515975735818,
					0.6612737880450936
				],
				[
					29.757762600793853,
					0.6612737880450936
				],
				[
					30.418981121493516,
					0.6612737880450936
				],
				[
					31.74158396492919,
					0.6612737880450936
				],
				[
					32.40285775297423,
					0.6612737880450936
				],
				[
					33.064186808364866,
					0.6612737880450936
				],
				[
					33.72540532906453,
					0.6612737880450936
				],
				[
					34.38667911710968,
					0.6612737880450936
				],
				[
					35.047952905154716,
					0.6612737880450936
				],
				[
					35.70928196054524,
					0.6612737880450936
				],
				[
					36.37061101593588,
					0.6612737880450936
				],
				[
					37.03182953663554,
					0.6612737880450936
				],
				[
					37.69310332468069,
					0.6612737880450936
				],
				[
					38.35437711272573,
					0.6612737880450936
				],
				[
					39.01570616811637,
					0.6612737880450936
				],
				[
					39.676979956161404,
					0.6612737880450936
				],
				[
					40.338253744206554,
					0.6612737880450936
				],
				[
					40.999527532251705,
					0.6612737880450936
				],
				[
					41.66080132029674,
					0.6612737880450936
				],
				[
					42.32207510834189,
					0.6612737880450936
				],
				[
					43.64467795177757,
					0.6612737880450936
				],
				[
					44.967225527867754,
					0.6612737880450936
				],
				[
					45.628499315912904,
					0.6612737880450936
				],
				[
					46.28982837130343,
					0.6612737880450936
				],
				[
					46.95110215934858,
					0.6612737880450936
				],
				[
					47.61237594739373,
					0.6612737880450936
				],
				[
					48.27364973543888,
					0.6612737880450936
				],
				[
					48.93492352348392,
					0.6612737880450936
				],
				[
					49.59625257887444,
					0.6612737880450936
				],
				[
					50.25752636691959,
					0.6612737880450936
				],
				[
					50.91880015496474,
					0.6612737880450936
				],
				[
					51.58007394300989,
					0.6612737880450936
				],
				[
					52.24134773105493,
					0.6612737880450936
				],
				[
					52.902676786445454,
					0.6612737880450936
				],
				[
					52.902676786445454,
					0
				],
				[
					53.563950574490605,
					0
				],
				[
					54.225224362535755,
					0
				],
				[
					54.225224362535755,
					0.6612737880450936
				],
				[
					54.225224362535755,
					1.322547576090244
				],
				[
					54.225224362535755,
					1.9838489978080815
				],
				[
					54.225224362535755,
					3.3063965738983256
				],
				[
					54.225224362535755,
					3.967697995616163
				],
				[
					54.225224362535755,
					5.951546993424188
				],
				[
					54.225224362535755,
					7.274122203187176
				],
				[
					54.225224362535755,
					8.59666977927742
				],
				[
					54.225224362535755,
					9.919244989040351
				],
				[
					54.225224362535755,
					11.241820198803282
				],
				[
					54.225224362535755,
					12.56439540856627
				],
				[
					54.886498150580906,
					13.886942984656457
				],
				[
					54.886498150580906,
					14.548244406374295
				],
				[
					54.886498150580906,
					15.870791982464539
				],
				[
					54.886498150580906,
					16.532093404182376
				],
				[
					54.886498150580906,
					17.193367192227527
				],
				[
					54.886498150580906,
					17.85464098027262
				],
				[
					54.886498150580906,
					18.515942401990458
				],
				[
					54.886498150580906,
					19.17721619003555
				],
				[
					54.886498150580906,
					19.83851761175339
				],
				[
					54.886498150580906,
					20.49979139979854
				],
				[
					54.886498150580906,
					21.161065187843633
				],
				[
					54.886498150580906,
					21.82236660956147
				],
				[
					54.886498150580906,
					22.483640397606564
				],
				[
					54.886498150580906,
					23.144914185651714
				],
				[
					55.54777193862594,
					23.144914185651714
				],
				[
					55.54777193862594,
					23.806215607369552
				],
				[
					55.54777193862594,
					24.467489395414646
				],
				[
					55.54777193862594,
					25.128763183459796
				],
				[
					55.54777193862594,
					25.790064605177633
				],
				[
					55.54777193862594,
					26.451338393222727
				],
				[
					55.54777193862594,
					27.112639814940565
				],
				[
					55.54777193862594,
					27.773913602985658
				],
				[
					55.54777193862594,
					28.43518739103081
				],
				[
					55.54777193862594,
					29.096488812748646
				],
				[
					55.54777193862594,
					29.75776260079374
				],
				[
					55.54777193862594,
					30.41903638883889
				],
				[
					55.54777193862594,
					31.08033781055667
				],
				[
					54.886498150580906,
					31.08033781055667
				],
				[
					54.886498150580906,
					31.74161159860182
				],
				[
					54.225224362535755,
					31.74161159860182
				],
				[
					52.902676786445454,
					31.74161159860182
				],
				[
					52.24134773105493,
					31.74161159860182
				],
				[
					50.91880015496474,
					31.74161159860182
				],
				[
					49.59625257887444,
					31.74161159860182
				],
				[
					48.27364973543888,
					31.74161159860182
				],
				[
					46.95110215934858,
					31.74161159860182
				],
				[
					44.967225527867754,
					31.74161159860182
				],
				[
					43.64467795177757,
					31.74161159860182
				],
				[
					41.66080132029674,
					31.74161159860182
				],
				[
					40.338253744206554,
					31.74161159860182
				],
				[
					38.35437711272573,
					31.74161159860182
				],
				[
					36.37061101593588,
					31.74161159860182
				],
				[
					34.38667911710968,
					31.74161159860182
				],
				[
					33.064186808364866,
					31.74161159860182
				],
				[
					31.080254909538553,
					31.74161159860182
				],
				[
					30.418981121493516,
					31.74161159860182
				],
				[
					28.43515975735818,
					31.74161159860182
				],
				[
					27.112556913922504,
					31.74161159860182
				],
				[
					25.790009337832203,
					31.74161159860182
				],
				[
					24.467461761742015,
					32.402885386646915
				],
				[
					23.80613270635149,
					32.402885386646915
				],
				[
					21.822311342216153,
					32.402885386646915
				],
				[
					20.49970849878048,
					32.402885386646915
				],
				[
					18.515887134645027,
					33.06418680836475
				],
				[
					17.19333955855484,
					33.06418680836475
				],
				[
					15.870736715119165,
					33.06418680836475
				],
				[
					15.209462927074014,
					33.06418680836475
				],
				[
					14.548189139028977,
					33.06418680836475
				],
				[
					13.886915350983827,
					33.06418680836475
				],
				[
					12.564312507548152,
					33.7254605964099
				],
				[
					11.903038719503002,
					33.7254605964099
				],
				[
					11.241764931457965,
					33.7254605964099
				],
				[
					10.580491143412814,
					33.7254605964099
				],
				[
					9.25788829997714,
					33.7254605964099
				],
				[
					8.596614511931989,
					33.7254605964099
				],
				[
					7.935340723886952,
					33.7254605964099
				],
				[
					7.274066935841802,
					33.7254605964099
				],
				[
					6.612793147796651,
					33.7254605964099
				],
				[
					5.951464092406127,
					33.7254605964099
				],
				[
					5.290190304360976,
					33.7254605964099
				],
				[
					4.62891651631594,
					33.7254605964099
				],
				[
					3.967642728270789,
					33.7254605964099
				],
				[
					3.3063689402256387,
					33.7254605964099
				],
				[
					2.645095152180488,
					33.7254605964099
				],
				[
					1.9837660967899637,
					33.7254605964099
				],
				[
					1.3224923087448133,
					33.7254605964099
				],
				[
					0.6612185206997765,
					33.7254605964099
				],
				[
					0,
					33.7254605964099
				],
				[
					-0.6613290553905244,
					33.7254605964099
				],
				[
					-0.6613290553905244,
					33.06418680836475
				],
				[
					-1.322658110781049,
					33.06418680836475
				],
				[
					-1.9839318988261994,
					33.06418680836475
				],
				[
					-1.9839318988261994,
					32.402885386646915
				],
				[
					-2.645205686871236,
					32.402885386646915
				],
				[
					-3.3064242075710126,
					32.402885386646915
				],
				[
					-3.967753262961537,
					32.402885386646915
				],
				[
					-4.629027051006574,
					32.402885386646915
				],
				[
					-5.290356106397212,
					31.74161159860182
				],
				[
					-5.290356106397212,
					31.74161159860182
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-5.290356106397212,
				31.74161159860182
			]
		},
		{
			"id": "CokMILx9",
			"type": "text",
			"x": -1905.8278043592265,
			"y": 511.7367346236196,
			"width": 17.7239990234375,
			"height": 35,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [
				"iXdoNdV_KiixFLWYBAcet"
			],
			"frameId": null,
			"roundness": null,
			"seed": 738442462,
			"version": 277,
			"versionNonce": 1413784542,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"text": "m",
			"rawText": "m",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 24,
			"containerId": null,
			"originalText": "m",
			"lineHeight": 1.25
		},
		{
			"id": "k8mUy7iKX6BRJKFMUYv92",
			"type": "freedraw",
			"x": -1863.5056187161938,
			"y": 517.65280853235,
			"width": 0.6757896961208639,
			"height": 32.438413738686215,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [
				"nB-nvy2ObCAdl1muSVVaU"
			],
			"frameId": null,
			"roundness": null,
			"seed": 579003870,
			"version": 294,
			"versionNonce": 2058260738,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6758179363922998
				],
				[
					0,
					1.351607632513106
				],
				[
					0,
					2.0273973286339695
				],
				[
					0,
					2.7032152650262695
				],
				[
					0,
					3.3790049611470754
				],
				[
					0,
					4.054794657267939
				],
				[
					0,
					4.73061259366024
				],
				[
					0,
					5.406402289781045
				],
				[
					0,
					6.758009922294151
				],
				[
					0,
					7.433799618415016
				],
				[
					0,
					8.109617554807315
				],
				[
					0,
					9.461196947048984
				],
				[
					0,
					10.137014883441225
				],
				[
					0,
					10.81280457956209
				],
				[
					0,
					12.164412212075197
				],
				[
					0,
					12.84020190819606
				],
				[
					0,
					13.51601984458836
				],
				[
					0,
					14.191809540709167
				],
				[
					0,
					14.867599236829973
				],
				[
					0,
					15.543417173222268
				],
				[
					0,
					16.89499656546394
				],
				[
					0,
					17.570814501856244
				],
				[
					0,
					18.246604197977103
				],
				[
					0,
					18.92239389409791
				],
				[
					0,
					19.59821183049021
				],
				[
					0,
					20.274001526611016
				],
				[
					0,
					20.949819463003315
				],
				[
					0,
					21.62560915912418
				],
				[
					0,
					22.301398855244987
				],
				[
					0,
					22.977216791637286
				],
				[
					0,
					23.65300648775809
				],
				[
					0,
					24.328796183878953
				],
				[
					0,
					25.004614120271253
				],
				[
					0,
					25.680403816392065
				],
				[
					0,
					26.356193512512927
				],
				[
					0,
					27.707801145026036
				],
				[
					0,
					28.383619081418335
				],
				[
					0,
					29.059408777539137
				],
				[
					0,
					29.73519847366
				],
				[
					0,
					30.4110164100523
				],
				[
					0.6757896961208639,
					31.08680610617311
				],
				[
					0.6757896961208639,
					31.762595802293973
				],
				[
					0.6757896961208639,
					32.438413738686215
				],
				[
					0.6757896961208639,
					31.762595802293973
				],
				[
					0.6757896961208639,
					31.762595802293973
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				0.6612737880451505,
				31.080337810556728
			]
		},
		{
			"id": "tbgYP19Os6RHdcGPBRVf0",
			"type": "freedraw",
			"x": -1862.829829020073,
			"y": 516.9770188362291,
			"width": 27.03198320863373,
			"height": 32.43838549841477,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [
				"nB-nvy2ObCAdl1muSVVaU"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1184355742,
			"version": 330,
			"versionNonce": 973109278,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6757896961207477,
					0
				],
				[
					2.0274255689053473,
					0
				],
				[
					4.054794657267939,
					0
				],
				[
					5.406430530052423,
					0
				],
				[
					7.433799618415015,
					0
				],
				[
					8.785435491199497,
					0
				],
				[
					10.812804579562089,
					0
				],
				[
					12.164440452346689,
					0.6757896961208057
				],
				[
					14.191809540709166,
					0.6757896961208057
				],
				[
					16.21917862907164,
					0.6757896961208057
				],
				[
					17.57081450185624,
					0.6757896961208057
				],
				[
					18.92245037464084,
					0.6757896961208057
				],
				[
					19.598183590218714,
					0.6757896961208057
				],
				[
					20.27397328633958,
					0.6757896961208057
				],
				[
					20.949819463003312,
					0.6757896961208057
				],
				[
					21.625609159124178,
					0.6757896961208057
				],
				[
					21.625609159124178,
					1.3516076325131055
				],
				[
					21.625609159124178,
					2.0273973286339113
				],
				[
					21.625609159124178,
					2.703187024754775
				],
				[
					22.301455335787914,
					3.3790049611470745
				],
				[
					22.301455335787914,
					4.730584353388744
				],
				[
					22.301455335787914,
					5.4064022897810435
				],
				[
					22.301455335787914,
					6.758009922294149
				],
				[
					22.301455335787914,
					8.10958931453582
				],
				[
					22.301455335787914,
					9.461196947048924
				],
				[
					22.301455335787914,
					10.81280457956203
				],
				[
					22.301455335787914,
					12.164383971803698
				],
				[
					22.301455335787914,
					13.515991604316863
				],
				[
					22.301455335787914,
					14.86759923682997
				],
				[
					22.301455335787914,
					16.219206869343072
				],
				[
					22.301455335787914,
					17.570786261584743
				],
				[
					22.301455335787914,
					18.922393894097905
				],
				[
					22.977188551365792,
					19.598183590218714
				],
				[
					22.977188551365792,
					20.949791222731815
				],
				[
					22.977188551365792,
					21.625609159124117
				],
				[
					22.977188551365792,
					22.301398855244983
				],
				[
					23.652978247486654,
					22.97718855136579
				],
				[
					23.652978247486654,
					23.653006487758084
				],
				[
					23.652978247486654,
					24.32879618387889
				],
				[
					24.32882442415039,
					25.00458587999976
				],
				[
					24.32882442415039,
					25.680403816392058
				],
				[
					24.32882442415039,
					26.35619351251286
				],
				[
					25.00461412027125,
					27.031983208633726
				],
				[
					25.68046029693499,
					27.70780114502603
				],
				[
					25.68046029693499,
					28.38359084114683
				],
				[
					25.68046029693499,
					29.05940877753913
				],
				[
					26.356193512512863,
					29.05940877753913
				],
				[
					26.356193512512863,
					29.73519847365994
				],
				[
					26.356193512512863,
					30.4109881697808
				],
				[
					27.03198320863373,
					31.086806106173103
				],
				[
					27.03198320863373,
					31.762595802293905
				],
				[
					26.356193512512863,
					32.43838549841477
				],
				[
					25.68046029693499,
					32.43838549841477
				],
				[
					24.32882442415039,
					32.43838549841477
				],
				[
					22.977188551365792,
					32.43838549841477
				],
				[
					21.625609159124178,
					32.43838549841477
				],
				[
					20.27397328633958,
					32.43838549841477
				],
				[
					18.92245037464084,
					32.43838549841477
				],
				[
					17.57081450185624,
					32.43838549841477
				],
				[
					15.543445413493764,
					32.43838549841477
				],
				[
					14.191809540709166,
					32.43838549841477
				],
				[
					12.164440452346689,
					32.43838549841477
				],
				[
					10.812804579562089,
					32.43838549841477
				],
				[
					10.137014883441225,
					32.43838549841477
				],
				[
					8.785435491199497,
					32.43838549841477
				],
				[
					8.10958931453576,
					32.43838549841477
				],
				[
					6.75800992229415,
					32.43838549841477
				],
				[
					6.082220226173286,
					32.43838549841477
				],
				[
					5.406430530052423,
					32.43838549841477
				],
				[
					4.730584353388686,
					32.43838549841477
				],
				[
					4.054794657267939,
					32.43838549841477
				],
				[
					3.379004961147075,
					32.43838549841477
				],
				[
					2.7032152650262113,
					32.43838549841477
				],
				[
					2.0274255689053473,
					32.43838549841477
				],
				[
					1.3515793922416117,
					32.43838549841477
				],
				[
					1.3515793922416117,
					32.43838549841477
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				1.3225475760901872,
				31.74161159860182
			]
		},
		{
			"id": "Ok3HepwK",
			"type": "text",
			"x": -1857.4234549705634,
			"y": 516.3012008998369,
			"width": 13.341873168945312,
			"height": 29.68610821264653,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [
				"nB-nvy2ObCAdl1muSVVaU"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1796542402,
			"version": 306,
			"versionNonce": 60957570,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341884860,
			"link": null,
			"locked": false,
			"text": "x",
			"rawText": "x",
			"fontSize": 23.748886570117225,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 20,
			"containerId": null,
			"originalText": "x",
			"lineHeight": 1.25
		},
		{
			"id": "afsehUA2",
			"type": "text",
			"x": -375.9748398029748,
			"y": 278.7329477245013,
			"width": 145.55673217773438,
			"height": 22.522850739181788,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 931432734,
			"version": 374,
			"versionNonce": 430263710,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341884861,
			"link": null,
			"locked": false,
			"text": "max_so_far = 1",
			"rawText": "max_so_far = 1",
			"fontSize": 18.01828059134543,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "max_so_far = 1",
			"lineHeight": 1.25
		},
		{
			"id": "NdyVQPfrE0b_tODP7I2ki",
			"type": "image",
			"x": -584.0595761895137,
			"y": 1115.5032898021693,
			"width": 851.684829734826,
			"height": 361.1247226383229,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 617184926,
			"version": 329,
			"versionNonce": 299612290,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "895fef8a839a47fb1639524bc45910bb0a317e8c",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "owWGEgBy_lbwUHwp28yQR",
			"type": "image",
			"x": -602.5943715829361,
			"y": 929.823644093166,
			"width": 191,
			"height": 116,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1757188894,
			"version": 263,
			"versionNonce": 1429964958,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1703341826063,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "0836ea0a1e27ad36a1f57090ffafaf0b951c1356",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "image",
			"version": 278,
			"versionNonce": 744460510,
			"isDeleted": false,
			"id": "ebY0quJi",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 308.8625360588302,
			"y": 1259.5111008248712,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 497.6522053669782,
			"height": 108.1852620362996,
			"seed": 10712,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341907336,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "1bcfa8476e14766f83773ca3dc9c015f8ebc41fa",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "image",
			"version": 239,
			"versionNonce": 836457090,
			"isDeleted": true,
			"id": "zmWTYaVH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -321.08339548180436,
			"y": 1719.4411658527906,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 443.28155608179406,
			"height": 86.7290001029597,
			"seed": 76551,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703341900560,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "f8c13161e486107270ba56d3ae4fb72ed0f74562",
			"scale": [
				1,
				1
			]
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#e03131",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 0.5,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 0,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 28,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 1717.9409381883384,
		"scrollY": 1788.575556713348,
		"zoom": {
			"value": 0.620619754476315
		},
		"currentItemRoundness": "sharp",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		}
	},
	"files": {}
}
```
%%