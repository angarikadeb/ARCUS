import os

rep = """include_once('setDBLocation.php');
$pdo = new PDO('sqlite:'.$dblocation);"""

for file in os.listdir("."):
	if file.endswith(".php"):
		o = open(file)
		d = o.read()
		o.close()
		d = d.replace("$pdo = new PDO('sqlite:../../data/db/CHIELD.sqlite');",rep)
		o = open(file,'w')
		o.write(d)
		o.close()
	