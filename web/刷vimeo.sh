#!/bin/bash
num=$1

python3 /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/链接.py -n $num -t /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/链接.txt
ulimit -n 2048

sed -i 's|https://crowncloud.362227.top|http://362227.top|g' /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/链接.txt




FILE_PATH="/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/链接.txt"
LINES_PER_BATCH=$(($(wc -l < $FILE_PATH)/4 + 1))  # 计算每部分的行数
TOTAL_LINES=$(wc -l < $FILE_PATH)
BATCHES=$((TOTAL_LINES/LINES_PER_BATCH))

for ((i=0;i<$BATCHES;i++)); do
    start=$((i*LINES_PER_BATCH+1))
    end=$(((i+1)*LINES_PER_BATCH))
    sed -n "$start,${end}p" $FILE_PATH > batch_$i.txt
    aria2c --check-certificate=false --referer=http://friendlondon.tv -i batch_$i.txt --file-allocation=none --max-concurrent-downloads=320 --disk-cache=0 --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/01 --max-download-result=20000000 | tee -a /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999.log"
    rm batch_$i.txt
done

# Download the remaining lines
if [ $((BATCHES*LINES_PER_BATCH)) -lt $TOTAL_LINES ]; then
    start=$((BATCHES*LINES_PER_BATCH+1))
    end=$TOTAL_LINES
    sed -n "$start,${end}p" $FILE_PATH > batch_$BATCHES.txt
    aria2c --check-certificate=false --referer=http://friendlondon.tv -i batch_$BATCHES.txt --file-allocation=none --max-concurrent-downloads=320 --disk-cache=0 --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/01 --max-download-result=20000000 | tee -a /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999.log" 
    rm batch_$BATCHES.txt
fi




#python /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/从log文件提取有ref的链接.py > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/有ref的链接.txt
#IP=( "https://trimediting.com/"  "https://somesuch.co/ " "https://www.petgorilla.com/"  "http://malloybrothers.com/" "http://alexanderhammer.com/"  "http://ways-means.co" "http://www.romanwhite.com" ); IP1=( "http://loucloutercasting.com/" "https://www.themill.com/"  "https://www.ntropic.com/"  "http://coffeeand.tv" "http://believemedia.com" "http://modernpost.com" "http://www.treyfanjoy.com/" ) ; for i in "${IP[@]}";do aria2c  --referer=$i -i "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/有ref的链接.txt" --file-allocation=none --max-concurrent-downloads=500 --disk-cache=0 --check-certificate=false --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/ref; done & for i1 in "${IP1[@]}";do aria2c  --referer=$i1 -i "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/有ref的链接.txt" --file-allocation=none --max-concurrent-downloads=494 --disk-cache=0 --check-certificate=false --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/ref; done  &


echo 下载失败的链接
python3 /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/从log文件提取下载失败的链接.py > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/遗漏文件链接合并.txt
aria2c - --referer=http://friendlondon.tv --check-certificate=false -i "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/遗漏文件链接合并.txt" --file-allocation=none --max-concurrent-downloads=200 --disk-cache=0 --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/遗漏文件 --max-download-result=1000




echo 删除重复小文件
find "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/01"  -type f -name "*.*" -delete
find "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/02"  -type f -name "*.*" -delete
find "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/ref"  -type f -name "*.*" -delete
find "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/遗漏文件"  -type f -name "*.*" -delete

echo 合并为大文件
find "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/01"  -type f -name "*" | xargs sed 'a\' > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999"
find "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/02"  -type f -name "*" | xargs sed 'a\' >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999"
find "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/ref"  -type f -name "*" | xargs sed 'a\' >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999"
find "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/遗漏文件"  -type f -name "*" | xargs sed 'a\' >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999"

echo 提取hash链接
#egrep -i '[0-9]{5,11}:[a-z0-9]{8,11}' 合并$num"000000"-$num"999999" > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并hash链接$num"000000"-$num"999999"

#echo 提取大文件有效信息（egrep命令，提取有avc_url的行）
#egrep -i '\"avc_url\"'  /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999"temp > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999"

#rm -rf /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999"temp

#echo 进一步删除无效信息（sed命令）
#sed -i s/.*video\"\:\{\"id\"//g  /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999"

#echo 整理好数据，进一步精简
#python /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/正则预处理.py -t /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999"



echo 提取最终数据$num"000000"-$num"999999"
#python /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/正则提取旧的.py > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html
echo "<h3>用户搜索</h3>" > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html
egrep -a -i '(.+?\"name\"\:\")(DEARCUT|ICONOCLAST|Saint George Studio|MYGOSH|Spectraevenko|FORTRESS LA|spacebar.+?louis palacios|COMPULSORY\.|Warner Global Catalog|Rhino Entertainment|Derec Dunn|Lou Clouter Casting|Forgotten Sundays|Somesuch Archive|The Mill|Andrew Donoho|The Banquet|Spearing Films|Feel Films|Jo Jo Lam|Feel Films|AFX Creative|Sam Siske|Warp Records|Powell Robinson|Dylan Rucker|Gear Seven|Tim Mattia|Alex Southam|Peter Zavadil|Tim Nackashi|Taillight|Taillight - Rough Cuts|Justin Clough|David Waterston|Taylor James|Family Creative|Legion Post|Matt Wise|patarakina|Jump VFX|jack pyland|Inez & Vinoodh|Anchor Light|KMOYES PICTURES|Adric Watson|Vania Heymann|Gal Muggia|Daniel Bronks|Simona Cristea|Duncan Russell|Jordan Bahat|Eric Wysocki|arnau valls colomer|Johnny Richards|ImagePartnership|Greatcoat Films|GUS BLACK|Andrew Thomas Huang|Joel Honeywell|Mack Fisher Cinematography|Nicholas Bupp|Ntropic Group|PET.+?RILLA|VisualCreatures|Gwen Ghelid|Alexander Hammer|Malloy Brothers|B Pictures|benz.+?ne|Alex Bartz|Mathieu Plainfoss.+?C|Park Pictures|Reset|Brad Rushing|Ways.+?Means|David Baum|LANE Archive|Christian Breslauer|Pulse Films|MINDED|Color Collective|Roman White|Trey Fanjoy|Johan Renck|Rock Paper Scissors|Nomad Editing Company Inc\.|The Den|Modern Post|Ramone Anderson|Johnny Richards|CheekyFilms|Lauri Laukkanen|IC|Supermega Films|Big Branch Productions|NoCap Shows|Psyop|Kenneth T Shimm|DeNovaMedia|Grayskull.tv|CA|FRIEND|Trim Editing|Ed Rutherford|Omer Ganai|TRAFIC|Gang Films|Jeremy Alter|Daniel Pearl.+?ASC|Airship|Soho House|Vicky Lawton|OPTIX|Agile Films|Max McGill|josh forbes|Evgeny Bystrov|Mason W.+?Dixon|CHEAT|Fancy Content|Sam Wrench|Tuff Contender|Larkin Seiple|Universal Music Publishing.+>?|THE YOUNG ASTRONAUTS|brooks|JOE SILL|Thomas Grove Carter|Remy Naidoo|iHeartRadio Events|TheFlyFamily|Beggars Group|Taylor Vandegrift|Raja Virdi|Jeremy Gosch|Neutra Production|Goldheart Post|Miles Trahan|Bruzier|Mutter .+?Productions GmbH|Bruno Ilogti|Rick Wilson|MM8|Davy Duhamel|Baris Aladag|Senior Post|WE WRK WKNDS|BEN GOODMAN|Ulrik Boel Bentzen|KIBORZ|Janssen Powers|Casey McPerry|Hellfire Creative|Hellfire Creative|Wild Stag Studio|Danila Volkov|Outside Lands Music Festival|Motion Eccentric.+?|TA Films|Kode Media|WJF|XIMedia|Mutt .+? Man|Sequitur Cinema|Doug Porter|Chris Westlund|Nick Pezzillo|Derek Hansen|Oren Soffer|Matt Schaff|Sam Care.+?Cinematographer|Amazon Music|Jacob Lees Johnson|Bryant Jansen|Dillon Schneider DP|BRADLEY .+?PABLO|The Quarry|dick clark productions|Ross Richardson|NYLA PROJECTS|HUNTER LYON|Patrick Lawler|WGTAM|Domino Recording Co|WE|BPI|Tim Nackashi|industry plant.+?|Jonny Tully|Eli Arenson|Austin City Limits|Sholight Live|Concord|Burning Reel|Baeblemusic|Johnny Marchetta|riffraff films|Antiest.+?ico|Thievery Studio|GLASSWORKS VFX|ALL OF IT NOW|JOHN TASHIRO|Jon Chema|Will Ngo|HAUS Pictures|DCP|LiveXLive|Urban Strom|Alex Bartz|Chris Davis|Warner Music.+?|Myriad Video|Symphonic Distribution|wash|Moon|Carlos Veron|L.+?Castle Studios|C3 Presents|Brooke James Productions|simian.+?la|ACNE|Epic Records|Forest of Black|Pinecone|Neema Sadeghi|La Blogotheque|Anthony Mark Saul|Joe Shahood|ATLANTIC VIDEO CONTENT|Sunset Edit|anonymous content|ed|Max Colt|OPERANDI MGMT|Cut.+?Run|Diane MartelThe Directors Bureau|Carbon|Mathematic Studio|Adam Zuckerman|Hound|MAAVVEN|reen Glow Films|Hans Carrillo|Jonas .+?kerlund Film|Sesler|Luti Media|Final Cut|Electric Theatre Collective|Moxie Pictures|Black Dog Films|Chris Roebuck|PAUL DUGDALE|Therapy Studios|RASCAL|Jason Zada|Greyson A.+?Welch|Supply.+?Demand|Scheme Engine|Company 3|James|Jamie Yuan|Dempsey Productions|Alex Chaloff|Ben Backhaus|BEMO|Lord Danger|Georgie Edelstein|Emma Rose Mead|Charlotte Russe Films|Cinema Giants Inc Film\/TV|Eric Bader|iHeartMedia|Riveting Entertainment|The Saline Project|TRASH FACTORY|Electric Light Studios|Cal Laird|HPLA|Biscuit Filmworks|Forever|david m\. helman|Loma Vista|FILM TANK|Cabin Editing Company|Magic Seed|Noah Clark \- Station 22|FAMILIA|Object .+?Animal|Gevorg Gev Juguryan|andresdp|VH POST|Exile Edit|BW|Fela|We Make Them Wonder|CanadaPost|Directors.+?DoPs|Gilbert Soliz|tempomedia|Swords .+?Eagles|Lacey Duke|A\-Frame Agency|argentinacine.+?referencias|Dan Kennedy|Matt Eastwood|Ammolite Inc|Tobias Rupp|The Funnel Creative|PAUL DUGDALE|JAX HARNEY|Trevor Wineman|Adam Zuckerman|Gil Green|CY|Untold Studios|Work Editorial|Justin Clough|Diane Martel|SONY MUSIC UK|London Alley|Colin Tilley|Metropolitana|Time Based Arts|Stereohorse|Happy Street|Warner Music|Electric Light Studios|BendEditor|Andrew Sandler|Darren Miller|Isaac Bauman|Coffee .+?TV|Luti Media|Edit Egg|adria petty|Rogue Films|Phillip Lopez|Grant Singer|Skulley Effects|Tomorrow|Jason McCormick|Jeremy Cross|Son.+?Heir|Greatcoat Films|Santiago Gonzalez|Supermega Films|Aya Tanimura|Tacklebox Upload|NtropicStudios|joel kefali|Bill Pollock|Sebastian Zotoff|Jack Begert|Malia James|2 Wolves Films|hangman|Tom Banks|Loren White|Paul B|The Rella Group|Brielle Hubert|Benjamin Kitchens|Michael Belcher|arnau valls colomer|Black Label Content|Arrad|Ben Carey|David Foulkes|AVIDDIVA|chriscottamfilms|Warner Records|Allie Avital|ARTJAIL|HELO|isaacrentz|Max Goldman|malik sayeed|Schafler Artists|Justin Hamilton|Huffman Creative|Riveting Entertainment|Happy Place|MAMAG STUDIOS|Blindeye Films|Color by Gloss|JONATHAN LAGACHE|Betterdays|Syndicate Entertainment|Marz Miller|Forager|Erik Sohlström|Max Vitali|Rock Paper Scissors|Pieter Mattheus Snyman III|sophie muller|Flaura Atkinson|Cut.+?Run|EAGER!|Lacey Duke|Drive Studios|Dennis Leupold|Carlos Lopez Estrada|XO MGMT|Mike Ho|Lux Artists|Constellation Jones|Dave Meyers|Rich Lee|PRETTYBIRD|Mute|RankinFilm|No.8|Bonch|XL RECORDINGS|P.R. Brown|DIVISION|My Accomplice|LAMAR BROTHERS|Tomás Whitmore|Benoit Soler|RSA Films|Outsider|Nate Gross|Farah X|declan whitebloom|Emilie Aubry|Les Umberger|MLM POST|ATLANTIC RECORDS VIDEO|Chris Dooley|Mathematic Studio|Merman|Octopus Inc|OBB Pictures|Velem|TK McKamy|Swords .+?Eagles|Jonathan Chou|PHILIPPA PRICE|ANTON TAMMI|Pine|Simon Hilton|BUF|Iconic Talent Agency|Xiaolong Liu|Memory Man|Obsidian|Flawless Post|Diktator|Lalim Edit|Incolor Inc\.|BWGTBLD|Lisa Ryan Smith|nabil elderkin|Andrew Stroud|Molly Manning Walker|Dan Lightening|MP Clubhouse|RadicalMedia|Marcus Domleo|MAAVVEN|Hound|Loom|Mike Reyes|Bucket Pictures|Contrast Films|SMUGGLER|Benoit Delhomme|Malloy Brothers|Max Colt|Christopher Ripley|Roisín Audrey Moloney|Caviar|BRTHR|Serial Pictures|Kaname Onoyama|Jonathan Walton|Lockt Editorial|Kai Saul|Vision Film Co|Believe Media.+?\.|Scheme Engine|Darren Grant|ra.+?gonzo|DREW KIRSCH|Miles Trahan|Brandon Dermer|alexandre moors|Match Music|Santiago Gonzalez|BRTHR|Tom.+?Whitmore|Huffman Creative|Darren Doane|Bo Mirhosseni|Green Glow Films|olivier Cariou|Favourite Colour.+?Black|HULK|D O M \& N I C|Aaron A|Gil Green|Dikayl Rimmaschla|Isaac Ravishankara|Corey C\. Waters|Brook Linder|Vania Heymann|Gal Muggia|J. A. Moreno|Angel Barroeta SVC|Daniel Broadley|AdamBecht|Andrew Sandler|APLUSFILMZ|Malia James|JM Films|Psycho Films|Theo Adams Company|David Bolen|Adam Newport-Berra|Kai Blamey Nguyen)(\".*)'  /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999" >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html
echo "<h3>艺人搜索</h3>" >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html
egrep -a -i '(title.+?\b)(prores|vfx|Nick\W?Jonas|Chris\W?Brown|The\W?Streets|Ice\W?Spice|PinkPantheress|Kasabian|Nightwish|Sam\W?Feldt|ROSALÍA|Nine\W?Inch\W?Nails|Pvris|Within\W?Temptation|C\.Tangana|Rauw\W?Alejandro|Li.+?Tjay|Portugal\W?The\W?Man|Tate\W?McRae|Depeche\W?Mode|Natti\W?Natasha|Summer\W?Walker|Ashnikko|Billy\W?Idol|Rolling\W?Stones|Tangana|Emeli\W?Sandé|Emeli\W?Sande|Duran\W?Duran|Jonas\W?Blue|J\W?Balvin|Noah\W?Cyrus|Sarah\W?Brightman|Dermot\W?Kennedy|Lizzo|RUDIMENTAL|The\W?Fray|PVRIS|Ryan\W?Tedder|Charlotte\W?OC|Dove\W?Cameron|Yellowcard|London\W?Grammar|Ty\W?Dolla|Popcaan|Rich\W?Brian|Bryson\W?Tiller|King\W?Princess|Sigrid|Shane\W?Filan|TONES\W?AND\W?I|Silk\W?Sonic|Ladyhawke|Lil\W?Tecca|Mick\W?Jagger|Robin\W?Schulz|MOD\W?SUN|Ashlee\W?Simpson|Trippie\W?Redd|Metronomy|Busta\W?Rhymes|Angel\W?Olsen|H\.E\.R\.|Johnny\W?Orlando|Gallant|Swedish\W?House\W?Mafia|The\W?Strokes|Fiona\W?Apple|Pabllo\W?Vittar|Royal\W?Blood|Bleachers|Skrillex|Pet\W?Shop\W?Boys|Foals|DJ\W?SMASH|Princess\W?Nokia|GAYLE|DJ\W?Mustard|Brandi\W?Carlile|Doechii|Sam\W?Fender|Metallica|SZA|Niall\W?Horan|Jason\W?Derulo|JP\W?Saxe|Swedish\W?House\W?Mafia|Jorja\W?Smith|AJ\W?Mitchell|American\W?Rejects|Cheat\W?Codes|Luke\W?Hemmings|London\W?Grammar|Kristian\W?Kostov|Alec\W?Benjamin|Ryan\W?Tedder|Emeli\W?Sand́e|Big\W?Sean|Kendrick\W?Lamar|Khalid|Travie\W?McCoy|Juice\W?WRLD|Pussycat\W?Dolls|Young\W?Thug|Jhene\W?Aiko|The\W?Wanted|ABBA|H\.E\.R\.|James\W?Bay|Ace\W?Of\W?Base|Keyshia\W?Cole|Idina\W?Menzel|Sam\W?Hunt|Roddy\W?Ricch|Jason\W?Mraz|Justin\W?Bieber|Justin\W?Timberlake|Nicki\W?Minaj|Becky\W?G|Ed\W?Sheeran|Lana\W?Del\W?Rey|Katy\W?Perry|Mike\W?Posner|JLS|Lawson|Coldplay|Nicole\W?Scherzinger|The\W?Vamps|Selena\W?Gomez|Leighton\W?Meester|GORILLAZ|Dua\W?Lipa|Demi\W?Lovato|Christina\W?Perri|Black\W?Eyed\W?Peas|Seconds\W?To\W?Mars|Birdy|Dappy|Hailee\W?Steinfeld|Michael\W?Bubl|MIKA|The\W?Script|Boyzone|Machine\W?Gun\W?Kelly|Jessie\W?J|Taio\W?Cruz|Marshmello|Diplo|Pia\W?Mia|Billie\W?Eilish|Christina\W?Perri|Rebecca\W?Black|Patrick\W?Stump|Fall\W?Out\W?Boy|Owl\W?City|Lady\W?Gaga|Tegan\W?and\W?Sara|Darin|Bridgit\W?Mendler|Jesse\W?McCartney|The\W?Veronicas|Sufjan\W?Stevens|Avicii|Craig\W?David|Carrie\W?Underwood|We\W?the\W?Kings|Cassadee\W?Pope|One\W?Direction|Christina\W?Aguilera|Cardi\W?B|Polo\W?G|Kelly\W?Clarkson|DaBaby|Kanye\W?West|Troye\W?Sivan|Diddy\W?Dirty\W?Money|Keyshia\W?Cole|Becky\W?Hill|Tyga|Daft\W?Punk|Ozuna|Jake\W?Bugg|Blake\W?Shelton|Luke\W?Bryan|Paris\W?Jackson|Dido|Wiz\W?Khalifa|Birdman|Boyzone|Ronan\W?Keating|Britt\W?Nicole|Gwen\W?Stefani|Mary\W?J\W?Blige|Imagine\W?Dragons|Echosmith|Patrick\W?Stump|Willow\W?Smith|La\W?Roux|Priyanka\W?Chopra|Tinie\W?Tempah|Union\W?J|Sophie\W?Ellis\W?Bextor|Victoria\W?Justice|Jay\W?Sean|Paramore|Ella\W?Henderson|Hayley\W?Williams|OneRepublic|Christina\W?Aguilera|Conor\W?Maynard|Lorde|Macklemore|Tinashe|Jedward|Shawn\W?Mendes|Zendaya|ZEDD|Pixie\W?Lott|Madonna|Jennifer\W?Lopez|Sky\W?Ferreira|HAIM|Sara\W?Bareilles|Florence.+?The\W?Machine|The\W?Verve|Kacey\W?Musgraves|Ke\$ha|Lady\W?A|Anjulie|Hey\W?Monday|Robbie\W?Williams|Alan\W?Walker|Doja\W?Cat|Post\W?Malone|24k\W?Goldn|Grimes|Lauv|Aurora|Tokio\W?Hotel|Tove\W?Lo|Rita\W?Ora|Liam\W?Gallagher|DJ\W?Khaled|Kelela|Benny\W?Benassi|Calum\W?Scott|Dizzee\W?Rasca|KT\W?Tunstall|Alicia\W?Keys|Keri\W?Hilson|Bj.+?rk|Alan\W?Walker|Scissor\W?Sisters|Gabrielle\W?Aplin|Markus\W?Feehilly|Kim\W?Petras|Weeknd|Crystal\W?Fighters|Keane|The\W?Corrs|James\W?Blunt|Lil\W?Nas\W?X|Sabrina\W?Carpenter|Samantha\W?Jade|Kimbra|Delta\W?Goodrem|Eva\W?Simons|Cheryl\W?Cole|Edward\W?Maya|Skylar\W?Grey|Foster\W?The\W?People|You\W?Me\W?At\W?Six|Gorgon\W?City|Kazaky|ZAYN|Joshua\W?Bassett|Bruno\W?Mars|Betty\W?Who|Beyonce|Mylene\W?Farmer|Lindsey\W?Stirling|Victoria\W?Monét|Liam\W?Gallagher|Pablo\W?Alboran|Sarah\W?Bareilles|olly\W?alexander|linkin\W?park|Sam\W?Hunt|Mat\W?Kearney|Kris\W?Allen|Goldfrapp|Olivia\W?Rodrigo|John\W?Mayer|Michelle\W?Branch|Tame\W?Impala|Ashley\W?Tisdale|Florida\W?Georgia\W?Line|Anne\W?Marie|Maroon\W?5|Steve\W?Aoki|Charli\W?XCX|Vance\W?Joy|James\W?Bay|Robyn|Tove\W?Styrke|American\W?Authors|Adam\W?Lambert|Cobra\W?Starship|Natasha\W?Bedingfeld|Gorgon\W?City|Lil\W?Yachty|Say\W?Lou\W?Lou|Rihanna|Ariana\W?Grande|Gabrielle\W?Aplin|Arcade\W?Fire|NOTD|2Chainz|Asher\W?Angel|Megan\W?Thee\W?Stallion|Daya|PRETTYMUCH|LEWIS\W?CAPALDI|Charlie\W?Puth|JAMES\W?ARTHUR|FKA\W?twigs|Howie\W?Day|SHAKIRA|Havana\W?Brown|Travis\W?Barker|Cody\W?Simpson|Avril\W?Lavigne|Jonas\W?Brothers|Cyndi\W?Lauper|Matoma|Miriam\W?Bryant|XXXTENTACION|Dillon\W?Francis|Vanessa\W?Hudgens|Kygo|Aloe\W?Blacc|Grace\W?VanderWaal|Soulja\W?Boy|David\W?Archuleta|AlunaGeorge|Rick\W?Ross|Ava\W?Max|Martin\W?Garrix|Hayley\W?Kiyoko|Rag\W?Bone\W?Man|P!NK|ROSALÍA|Capital\W?Cities|Ellie\W?Goulding|Little\W?Mix|Janet\W?Jackson|Eminem|Solange|slowthai|Enya|Snoop Dogg|YUNGBLUD|Pitbull|One\W?Pilots|Lykke\W?Li|SKY\W?FERREIRA|Kat\W?DeLuna|Jessie\W?Ware|X\W?AMBASSADORS|SAM\W?SMITH|SAINt\W?JHN|Black\W?Atlass|Celiné\W?Dion|RUN\W?THE\W?JEWELS|Zella\W?Day|Tom\W?Grennan|Green\W?Day|blur|Enrique\W?Iglesias|Melanie\W?C|Azealia\W?Banks|Michael\W?Bublé|Sebastián\W?Yatra|Nothing\W?But\W?Thieves|Sixpence\W?None\W?The\W?Richer|Paloma\W?Faith|David\W?Guetta|Zara\W?Larsson|Taylor\W?Swift|Noel\W?Gallagher|SOFIA\W?CARSON|Miley\W?Cyrus|Anitta|Weezer|Shayne\W?Ward|Hunter\W?Hayes|Halsey|Mark\W?Ronson|Conan\W?Gray|Jake\W?Miller|Travis\W?Scott|Harry\W?Styles|Luis\W?Fonsi|DJ\W?Snake|Don\W?Diablo|Icona\W?Pop|NE\-YO|NEYO|Lil\W?Uzi\W?Vert|J.\W?Balvin|Gnarls\W?Barkley|Maluma|Mike\W?Shinoda|Paul\W?McCartney|Sugababes|St\.\W?Vincent|Grimes|The\W?XX|Jamie\W?XX|Goldfrapp|Cheryl|Vampire\W?Weekend|Britney|Britney\W?Spears|Kylie|Shania\W?Twain|JLO|Drake|Maren\W?Morris|Red\W?Hot\W?Chilli\W?Peppers|RHCP|Depeche\W?Mode|No\W?Doubt|Passenger|Liam\W?Payne|Liam\W?Payne|WESTLIFE|Backstreet\W?Boys|Simple\W?Plan|OK\W?GO|Suede|Timbaland|Mariah\W?Carey|years.+?years|Nickelback|Idina\W?Menzel|Snow\W?Patrol|Missy\W?Elliott|Gotye|Annie\W?Lennox|Adele|Gabby\W?Barrett|Kane\W?Brown|Luke\W?Combs|Chris\W?Stapleton|Florida\W?Georgia\W?Line|Camila\W?Cabello|take\W?that|My\W?Chemical\W?Romance|Arctic\W?Monkeys|Sam\W?Hunt|Mac\W?Miller|Norah\W?Jones|Joss\W?Stone|Amy\W?Winehouse|Marina|Hilary\W?Duff|Hey\W?Monday|M\Ø|Carly\W?Rae\W?Jepsen|Far\W?East\W?Movement|Girls\W?Aloud|A\W?Great\W?Big\W?World|Barbra\W?Streisand|Alexandra\W?Burke|Evanescence|YNW\W?Melly|Alexandra\W?Stan|Daddy\W?Yankee|Calvin\W?Harris|Hozier|Ace\W?Of\W?Base|Brandy|Meghan\W?Trainor|Fergie|Ashanti|Faith\W?Hill|Tim\W?McGraw|Keith\W?Urban|Ciara|Toni\W?Braxton|Nelly\W?Furtado|Natasha\W?Bedingfield|Ricky\W?Martin|Emeli\W?Sand|Kings\W?Of\W?Leon|Robin\W?Thicke|Leona\W?Lewis|Kelly\W?Rowland|Matchbox\W?Twenty|Meek\W?Mill|Ludacris|AP\W?Rocky|Snoop\W?Dogg|Rich\W?Brian|Gucci\W?Mane|Ace\W?Hood|Rich\W?Homie\W?Quan|Olly\W?Murs|Soulja\W?Boy|Kehlani|Wretch\W?32|Trey\W?Songz|Danny\W?Brown|Hurts|Jess\W?Glynne|Trina|Saweetie|Roddy\W?Ricch|LMFAO|David\W?Bowie|M2M|LeAnn\W?Rimes|John\W?Legend|Tiëst|Conor\W?Maynard|Iggy\W?Azaela|The\W?Pretty\W?Reckless)([^a-z].+?from )(.+?<\/title>.+?)(\"duration\"\:[0-9]{3,}\,)(未知|advanced|starter|standard|custom|business|business_lapsed|pro_lapsed|plus_lapsed|pro|plus|premium|enterprise|live\_premium)(\".*)'  /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999" >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html
echo "<h3>ISRC、视频格式搜索</h3>" >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html
egrep -a -i '(title>.+?)(3200x1800|4444 |pr422|422hq|bitmax|gbuv|usuv|usum|uswv|usrv|ussm|usatv)(.+? from .+?<\/title>.+?)(\"duration\"\:[0-9]{3,}\,).+?account\_type\"\:\"(?:未知|advanced|starter|standard|custom|business|business_lapsed|pro_lapsed|plus_lapsed|pro|plus|premium|enterprise|live\_premium)(\".*)'  /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999" >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html

sed -i 's|"\(https:\/\/vimeo\.com[^"]*\)"|<a href="\1" target="_blank">\1</a>|g' /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html

echo 删除重复行
awk '!seen[$0]++' /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html  > tmpfile && mv tmpfile /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html

txt=$(curl  -F file=@/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html  https://store1.gofile.io/uploadFile | jq -r '.data.downloadPage + "#" + .data.fileName')
curl https://362227.top/rss/file.php?text=$txt 

txt=$(curl  -F file=@/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999"  https://store1.gofile.io/uploadFile | jq -r '.data.downloadPage + "#" + .data.fileName' )
curl https://362227.top/rss/file.php?text=$txt 

txt=$(curl  -F file=@/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999.log"  https://store1.gofile.io/uploadFile | jq -r '.data.downloadPage + "#" + .data.fileName' )
curl https://362227.top/rss/file.php?text=$txt 
