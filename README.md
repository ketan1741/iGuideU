# iGuideU-An Indoor Mapping System.

## 1) How to run the code:

**Important note:**

* Library Required:

-> matplotlib.pyplot python package is needed for the code to run successfully and give a output path.



* Unzip the project folder which contains the model.py file and map, directional signs as images.
* Open and run the model.py file code. (Note that the code file should be in the folder directory for it to load the images.)


## 2) Giving Input:

* As the hardware part isn't included in the project as of now, the scanned encoded number in the RFID tag will be 
given as input so that source location is loaded.

* For the input -

 i.   "Main Entrance": [0],
 	
ii. 'Entrance/Exit2 (Balaji Store)':[2], 

iii.    "TT Gallery1/Shakespeare Gallery":[5],	

iv. "Main Lift1":[15],

v.    "Entrance/Exit1 (SBI ATM)":[10],	

vi. "Gents Washroom":[8],

vii.    "Ladies Washroom":[6],	

viii. "Room: 38,37":[0,1],	

ix. "Room: 35,36":[1,2],

x.   "Room: 30-32":[3,5],	

xi. "Room: 33,34":[2,3],	

x. "Room: 25-27":[5,6],

xi.    'CTS':[7],	

xii. "Room: 15,14":[7,8],	

xiii. "Room: 12,13":[8,9],	

xiv. "Room: 10,11":[9,10],

xv.  "Room: 6 to 9":[10,12], 	

xvi. "Room: 3-5":[12,13],	

xvii. "Room: 1,2,20":[13,0],

xviii.  "Room: 18,19,21,22":[8,14],		

xix. "Lift2 & Stairs":[7],	

xx. "Room: 39 to 43":[6,1],

xxi.    "Nescafe":[4],	

xxii. 'Amphitheatre':[11]}

* These values will be encoded in the RFID tags and placed at those locations.

* Enter the corresponding number stored in the dictionary values as your source location. 
	EX: If you are at Gents Washroom, enter 8.

* If the value consists of multiple values, enter the first value as the source location.
	EX: If you are in between Room 30 and 32, enter 3.


* After that the user selects the desired destination from the displayed list.
* A map is generated and saved in the folder with the name 'path.png'
* This map will be displayed to the user via mobile application.