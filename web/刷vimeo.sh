#!/bin/bash
num=$1

python3 /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/链接.py -n $num -t /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/链接.txt
ulimit -n 2048

sed -i 's|https://crowncloud.362227.top|http://362227.top|g' /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/链接.txt






# 插入的内容
insert_text="https-proxy=127.0.0.1:1083"

# 每个插入间隔
insert_interval=1000

# 使用 awk 在原始文件中直接进行编辑
awk -i inplace -v insert_text="$insert_text" -v insert_interval="$insert_interval" '
    BEGIN {
        count = 0
    }
    {
        if ($0 ~ /out=/) {
            count++
            if (count % (2 * insert_interval) <= insert_interval) {
                print $0
                print insert_text
            } else {
                print $0
            }
        } else {
            print $0
        }
    }
' "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/链接.txt"






FILE_PATH="/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/链接.txt"
LINES_PER_BATCH=$(($(wc -l < $FILE_PATH)/4 + 1))  # 计算每部分的行数
TOTAL_LINES=$(wc -l < $FILE_PATH)
BATCHES=$((TOTAL_LINES/LINES_PER_BATCH))

for ((i=0;i<$BATCHES;i++)); do
    start=$((i*LINES_PER_BATCH+1))
    end=$(((i+1)*LINES_PER_BATCH))
    sed -n "$start,${end}p" $FILE_PATH > batch_$i.txt
    aria2c --check-certificate=false --referer=http://friendlondon.tv -i batch_$i.txt --file-allocation=none --max-concurrent-downloads=120 --disk-cache=0 --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/01 --max-download-result=20000000 | tee -a /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999.log"
    rm batch_$i.txt
done

# Download the remaining lines
if [ $((BATCHES*LINES_PER_BATCH)) -lt $TOTAL_LINES ]; then
    start=$((BATCHES*LINES_PER_BATCH+1))
    end=$TOTAL_LINES
    sed -n "$start,${end}p" $FILE_PATH > batch_$BATCHES.txt
    aria2c --check-certificate=false --referer=http://friendlondon.tv -i batch_$BATCHES.txt --file-allocation=none --max-concurrent-downloads=120 --disk-cache=0 --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/01 --max-download-result=20000000 | tee -a /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999.log" 
    rm batch_$BATCHES.txt
fi




#python /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/从log文件提取有ref的链接.py > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/有ref的链接.txt
#IP=( "https://trimediting.com/"  "https://somesuch.co/ " "https://www.petgorilla.com/"  "http://malloybrothers.com/" "http://alexanderhammer.com/"  "http://ways-means.co" "http://www.romanwhite.com" ); IP1=( "http://loucloutercasting.com/" "https://www.themill.com/"  "https://www.ntropic.com/"  "http://coffeeand.tv" "http://believemedia.com" "http://modernpost.com" "http://www.treyfanjoy.com/" ) ; for i in "${IP[@]}";do aria2c  --referer=$i -i "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/有ref的链接.txt" --file-allocation=none --max-concurrent-downloads=500 --disk-cache=0 --check-certificate=false --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/ref; done & for i1 in "${IP1[@]}";do aria2c  --referer=$i1 -i "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/有ref的链接.txt" --file-allocation=none --max-concurrent-downloads=494 --disk-cache=0 --check-certificate=false --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/ref; done  &


echo 下载失败的链接
python3 /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/从log文件提取下载失败的链接.py > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/遗漏文件链接合并.txt
aria2c - --referer=http://friendlondon.tv --check-certificate=false -i "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/遗漏文件链接合并.txt" --file-allocation=none --max-concurrent-downloads=100 --disk-cache=0 --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/遗漏文件 --max-download-result=1000




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
egrep -a -i '(.+?\"name\"\:\")(AVIDDIVA®️|DEARCUT|ICONOCLAST|Saint George Studio|MYGOSH|Spectraevenko|FORTRESS LA|spacebar.+?louis palacios|COMPULSORY\.|Warner Global Catalog|Rhino Entertainment|Derec Dunn|Lou Clouter Casting|Forgotten Sundays|Somesuch Archive|The Mill|Andrew Donoho|The Banquet|Spearing Films|Feel Films|Jo Jo Lam|Feel Films|AFX Creative|Sam Siske|Warp Records|Powell Robinson|Dylan Rucker|Gear Seven|Tim Mattia|Alex Southam|Peter Zavadil|Tim Nackashi|Taillight|Taillight - Rough Cuts|Justin Clough|David Waterston|Taylor James|Family Creative|Legion Post|Matt Wise|patarakina|Jump VFX|jack pyland|Inez & Vinoodh|Anchor Light|KMOYES PICTURES|Adric Watson|Vania Heymann|Gal Muggia|Daniel Bronks|Simona Cristea|Duncan Russell|Jordan Bahat|Eric Wysocki|arnau valls colomer|Johnny Richards|ImagePartnership|Greatcoat Films|GUS BLACK|Andrew Thomas Huang|Joel Honeywell|Mack Fisher Cinematography|Nicholas Bupp|Ntropic Group|PET.+?RILLA|VisualCreatures|Gwen Ghelid|Alexander Hammer|Malloy Brothers|B Pictures|benz.+?ne|Alex Bartz|Mathieu Plainfoss.+?C|Park Pictures|Reset|Brad Rushing|Ways.+?Means|David Baum|LANE Archive|Christian Breslauer|Pulse Films|MINDED|Color Collective|Roman White|Trey Fanjoy|Johan Renck|Rock Paper Scissors|Nomad Editing Company Inc\.|The Den|Modern Post|Ramone Anderson|Johnny Richards|CheekyFilms|Lauri Laukkanen|IC|Supermega Films|Big Branch Productions|NoCap Shows|Psyop|Kenneth T Shimm|DeNovaMedia|Grayskull.tv|CA|FRIEND|Trim Editing|Ed Rutherford|Omer Ganai|TRAFIC|Gang Films|Jeremy Alter|Daniel Pearl.+?ASC|Airship|Soho House|Vicky Lawton|OPTIX|Agile Films|Max McGill|josh forbes|Evgeny Bystrov|Mason W.+?Dixon|CHEAT|Fancy Content|Sam Wrench|Tuff Contender|Larkin Seiple|Universal Music Publishing.+>?|THE YOUNG ASTRONAUTS|brooks|JOE SILL|Thomas Grove Carter|Remy Naidoo|iHeartRadio Events|TheFlyFamily|Beggars Group|Taylor Vandegrift|Raja Virdi|Jeremy Gosch|Neutra Production|Goldheart Post|Miles Trahan|Bruzier|Mutter .+?Productions GmbH|Bruno Ilogti|Rick Wilson|MM8|Davy Duhamel|Baris Aladag|Senior Post|WE WRK WKNDS|BEN GOODMAN|Ulrik Boel Bentzen|KIBORZ|Janssen Powers|Casey McPerry|Hellfire Creative|Hellfire Creative|Wild Stag Studio|Danila Volkov|Outside Lands Music Festival|Motion Eccentric.+?|TA Films|Kode Media|WJF|XIMedia|Mutt .+? Man|Sequitur Cinema|Doug Porter|Chris Westlund|Nick Pezzillo|Derek Hansen|Oren Soffer|Matt Schaff|Sam Care.+?Cinematographer|Amazon Music|Jacob Lees Johnson|Bryant Jansen|Dillon Schneider DP|BRADLEY .+?PABLO|The Quarry|dick clark productions|Ross Richardson|NYLA PROJECTS|HUNTER LYON|Patrick Lawler|WGTAM|Domino Recording Co|WE|BPI|Tim Nackashi|industry plant.+?|Jonny Tully|Eli Arenson|Austin City Limits|Sholight Live|Concord|Burning Reel|Baeblemusic|Johnny Marchetta|riffraff films|Antiest.+?ico|Thievery Studio|GLASSWORKS VFX|ALL OF IT NOW|JOHN TASHIRO|Jon Chema|Will Ngo|HAUS Pictures|DCP|LiveXLive|Urban Strom|Alex Bartz|Chris Davis|Warner Music.+?|Myriad Video|Symphonic Distribution|wash|Moon|Carlos Veron|L.+?Castle Studios|C3 Presents|Brooke James Productions|simian.+?la|ACNE|Epic Records|Forest of Black|Pinecone|Neema Sadeghi|La Blogotheque|Anthony Mark Saul|Joe Shahood|ATLANTIC VIDEO CONTENT|Sunset Edit|anonymous content|ed|Max Colt|OPERANDI MGMT|Cut.+?Run|Diane MartelThe Directors Bureau|Carbon|Mathematic Studio|Adam Zuckerman|Hound|MAAVVEN|reen Glow Films|Hans Carrillo|Jonas .+?kerlund Film|Sesler|Luti Media|Final Cut|Electric Theatre Collective|Moxie Pictures|Black Dog Films|Chris Roebuck|PAUL DUGDALE|Therapy Studios|RASCAL|Jason Zada|Greyson A.+?Welch|Supply.+?Demand|Scheme Engine|Company 3|James|Jamie Yuan|Dempsey Productions|Alex Chaloff|Ben Backhaus|BEMO|Lord Danger|Georgie Edelstein|Emma Rose Mead|Charlotte Russe Films|Cinema Giants Inc Film\/TV|Eric Bader|iHeartMedia|Riveting Entertainment|The Saline Project|TRASH FACTORY|Electric Light Studios|Cal Laird|HPLA|Biscuit Filmworks|Forever|david m\. helman|Loma Vista|FILM TANK|Cabin Editing Company|Magic Seed|Noah Clark \- Station 22|FAMILIA|Object .+?Animal|Gevorg Gev Juguryan|andresdp|VH POST|Exile Edit|BW|Fela|We Make Them Wonder|CanadaPost|Directors.+?DoPs|Gilbert Soliz|tempomedia|Swords .+?Eagles|Lacey Duke|A\-Frame Agency|argentinacine.+?referencias|Dan Kennedy|Matt Eastwood|Ammolite Inc|Tobias Rupp|The Funnel Creative|PAUL DUGDALE|JAX HARNEY|Trevor Wineman|Adam Zuckerman|Gil Green|CY|Untold Studios|Work Editorial|Justin Clough|Diane Martel|SONY MUSIC UK|London Alley|Colin Tilley|Metropolitana|Time Based Arts|Stereohorse|Happy Street|Warner Music|Electric Light Studios|BendEditor|Andrew Sandler|Darren Miller|Isaac Bauman|Coffee .+?TV|Luti Media|Edit Egg|adria petty|Rogue Films|Phillip Lopez|Grant Singer|Skulley Effects|Tomorrow|Jason McCormick|Jeremy Cross|Son.+?Heir|Greatcoat Films|Santiago Gonzalez|Supermega Films|Aya Tanimura|Tacklebox Upload|NtropicStudios|joel kefali|Bill Pollock|Sebastian Zotoff|Jack Begert|Malia James|2 Wolves Films|hangman|Tom Banks|Loren White|Paul B|The Rella Group|Brielle Hubert|Benjamin Kitchens|Michael Belcher|arnau valls colomer|Black Label Content|Arrad|Ben Carey|David Foulkes|AVIDDIVA|chriscottamfilms|Warner Records|Allie Avital|ARTJAIL|HELO|isaacrentz|Max Goldman|malik sayeed|Schafler Artists|Justin Hamilton|Huffman Creative|Riveting Entertainment|Happy Place|MAMAG STUDIOS|Blindeye Films|Color by Gloss|JONATHAN LAGACHE|Betterdays|Syndicate Entertainment|Marz Miller|Forager|Erik Sohlström|Max Vitali|Rock Paper Scissors|Pieter Mattheus Snyman III|sophie muller|Flaura Atkinson|Cut.+?Run|EAGER!|Lacey Duke|Drive Studios|Dennis Leupold|Carlos Lopez Estrada|XO MGMT|Mike Ho|Lux Artists|Constellation Jones|Dave Meyers|Rich Lee|PRETTYBIRD|Mute|RankinFilm|No.8|Bonch|XL RECORDINGS|P.R. Brown|DIVISION|My Accomplice|LAMAR BROTHERS|Tomás Whitmore|Benoit Soler|RSA Films|Outsider|Nate Gross|Farah X|declan whitebloom|Emilie Aubry|Les Umberger|MLM POST|ATLANTIC RECORDS VIDEO|Chris Dooley|Mathematic Studio|Merman|Octopus Inc|OBB Pictures|Velem|TK McKamy|Swords .+?Eagles|Jonathan Chou|PHILIPPA PRICE|ANTON TAMMI|Pine|Simon Hilton|BUF|Iconic Talent Agency|Xiaolong Liu|Memory Man|Obsidian|Flawless Post|Diktator|Lalim Edit|Incolor Inc\.|BWGTBLD|Lisa Ryan Smith|nabil elderkin|Andrew Stroud|Molly Manning Walker|Dan Lightening|MP Clubhouse|RadicalMedia|Marcus Domleo|MAAVVEN|Hound|Loom|Mike Reyes|Bucket Pictures|Contrast Films|SMUGGLER|Benoit Delhomme|Malloy Brothers|Max Colt|Christopher Ripley|Roisín Audrey Moloney|Caviar|BRTHR|Serial Pictures|Kaname Onoyama|Jonathan Walton|Lockt Editorial|Kai Saul|Vision Film Co|Believe Media.+?\.|Scheme Engine|Darren Grant|ra.+?gonzo|DREW KIRSCH|Miles Trahan|Brandon Dermer|alexandre moors|Match Music|Santiago Gonzalez|BRTHR|Tom.+?Whitmore|Huffman Creative|Darren Doane|Bo Mirhosseni|Green Glow Films|olivier Cariou|Favourite Colour.+?Black|HULK|D O M \& N I C|Aaron A|Gil Green|Dikayl Rimmaschla|Isaac Ravishankara|Corey C\. Waters|Brook Linder|Vania Heymann|Gal Muggia|J. A. Moreno|Angel Barroeta SVC|Daniel Broadley|AdamBecht|Andrew Sandler|APLUSFILMZ|Malia James|JM Films|Psycho Films|Theo Adams Company|David Bolen|Adam Newport-Berra|Kai Blamey Nguyen)(\".*)'  /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999" >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html
echo "<h3>艺人搜索</h3>" >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html
egrep -a -i '(title.+?\b)(prores|vfx|Nick[^a-zA-Z0-9]*Jonas|Chris[^a-zA-Z0-9]*Brown|The[^a-zA-Z0-9]*Streets|Ice[^a-zA-Z0-9]*Spice|PinkPantheress|Kasabian|Nightwish|Sam[^a-zA-Z0-9]*Feldt|ROSALÍA|Nine[^a-zA-Z0-9]*Inch[^a-zA-Z0-9]*Nails|Pvris|Within[^a-zA-Z0-9]*Temptation|C\.Tangana|Rauw[^a-zA-Z0-9]*Alejandro|Li.+?Tjay|Portugal[^a-zA-Z0-9]*The[^a-zA-Z0-9]*Man|Tate[^a-zA-Z0-9]*McRae|Depeche[^a-zA-Z0-9]*Mode|Natti[^a-zA-Z0-9]*Natasha|Summer[^a-zA-Z0-9]*Walker|Ashnikko|Billy[^a-zA-Z0-9]*Idol|Rolling[^a-zA-Z0-9]*Stones|Tangana|Emeli[^a-zA-Z0-9]*Sandé|Emeli[^a-zA-Z0-9]*Sande|Duran[^a-zA-Z0-9]*Duran|Jonas[^a-zA-Z0-9]*Blue|J[^a-zA-Z0-9]*Balvin|Noah[^a-zA-Z0-9]*Cyrus|Sarah[^a-zA-Z0-9]*Brightman|Dermot[^a-zA-Z0-9]*Kennedy|Lizzo|RUDIMENTAL|The[^a-zA-Z0-9]*Fray|PVRIS|Ryan[^a-zA-Z0-9]*Tedder|Charlotte[^a-zA-Z0-9]*OC|Dove[^a-zA-Z0-9]*Cameron|Yellowcard|London[^a-zA-Z0-9]*Grammar|Ty[^a-zA-Z0-9]*Dolla|Popcaan|Rich[^a-zA-Z0-9]*Brian|Bryson[^a-zA-Z0-9]*Tiller|King[^a-zA-Z0-9]*Princess|Sigrid|Shane[^a-zA-Z0-9]*Filan|TONES[^a-zA-Z0-9]*AND[^a-zA-Z0-9]*I|Silk[^a-zA-Z0-9]*Sonic|Ladyhawke|Lil[^a-zA-Z0-9]*Tecca|Mick[^a-zA-Z0-9]*Jagger|Robin[^a-zA-Z0-9]*Schulz|MOD[^a-zA-Z0-9]*SUN|Ashlee[^a-zA-Z0-9]*Simpson|Trippie[^a-zA-Z0-9]*Redd|Metronomy|Busta[^a-zA-Z0-9]*Rhymes|Angel[^a-zA-Z0-9]*Olsen|H\.E\.R\.|Johnny[^a-zA-Z0-9]*Orlando|Gallant|Swedish[^a-zA-Z0-9]*House[^a-zA-Z0-9]*Mafia|The[^a-zA-Z0-9]*Strokes|Fiona[^a-zA-Z0-9]*Apple|Pabllo[^a-zA-Z0-9]*Vittar|Royal[^a-zA-Z0-9]*Blood|Bleachers|Skrillex|Pet[^a-zA-Z0-9]*Shop[^a-zA-Z0-9]*Boys|Foals|DJ[^a-zA-Z0-9]*SMASH|Princess[^a-zA-Z0-9]*Nokia|GAYLE|DJ[^a-zA-Z0-9]*Mustard|Brandi[^a-zA-Z0-9]*Carlile|Doechii|Sam[^a-zA-Z0-9]*Fender|Metallica|SZA|Niall[^a-zA-Z0-9]*Horan|Jason[^a-zA-Z0-9]*Derulo|JP[^a-zA-Z0-9]*Saxe|Swedish[^a-zA-Z0-9]*House[^a-zA-Z0-9]*Mafia|Jorja[^a-zA-Z0-9]*Smith|AJ[^a-zA-Z0-9]*Mitchell|American[^a-zA-Z0-9]*Rejects|Cheat[^a-zA-Z0-9]*Codes|Luke[^a-zA-Z0-9]*Hemmings|London[^a-zA-Z0-9]*Grammar|Kristian[^a-zA-Z0-9]*Kostov|Alec[^a-zA-Z0-9]*Benjamin|Ryan[^a-zA-Z0-9]*Tedder|Emeli[^a-zA-Z0-9]*Sand́e|Big[^a-zA-Z0-9]*Sean|Kendrick[^a-zA-Z0-9]*Lamar|Khalid|Travie[^a-zA-Z0-9]*McCoy|Juice[^a-zA-Z0-9]*WRLD|Pussycat[^a-zA-Z0-9]*Dolls|Young[^a-zA-Z0-9]*Thug|Jhene[^a-zA-Z0-9]*Aiko|The[^a-zA-Z0-9]*Wanted|ABBA|H\.E\.R\.|James[^a-zA-Z0-9]*Bay|Ace[^a-zA-Z0-9]*Of[^a-zA-Z0-9]*Base|Keyshia[^a-zA-Z0-9]*Cole|Idina[^a-zA-Z0-9]*Menzel|Sam[^a-zA-Z0-9]*Hunt|Roddy[^a-zA-Z0-9]*Ricch|Jason[^a-zA-Z0-9]*Mraz|Justin[^a-zA-Z0-9]*Bieber|Justin[^a-zA-Z0-9]*Timberlake|Nicki[^a-zA-Z0-9]*Minaj|Becky[^a-zA-Z0-9]*G|Ed[^a-zA-Z0-9]*Sheeran|Lana[^a-zA-Z0-9]*Del[^a-zA-Z0-9]*Rey|Katy[^a-zA-Z0-9]*Perry|Mike[^a-zA-Z0-9]*Posner|JLS|Lawson|Coldplay|Nicole[^a-zA-Z0-9]*Scherzinger|The[^a-zA-Z0-9]*Vamps|Selena[^a-zA-Z0-9]*Gomez|Leighton[^a-zA-Z0-9]*Meester|GORILLAZ|Dua[^a-zA-Z0-9]*Lipa|Demi[^a-zA-Z0-9]*Lovato|Christina[^a-zA-Z0-9]*Perri|Black[^a-zA-Z0-9]*Eyed[^a-zA-Z0-9]*Peas|Seconds[^a-zA-Z0-9]*To[^a-zA-Z0-9]*Mars|Birdy|Dappy|Hailee[^a-zA-Z0-9]*Steinfeld|Michael[^a-zA-Z0-9]*Bubl|MIKA|The[^a-zA-Z0-9]*Script|Boyzone|Machine[^a-zA-Z0-9]*Gun[^a-zA-Z0-9]*Kelly|Jessie[^a-zA-Z0-9]*J|Taio[^a-zA-Z0-9]*Cruz|Marshmello|Diplo|Pia[^a-zA-Z0-9]*Mia|Billie[^a-zA-Z0-9]*Eilish|Christina[^a-zA-Z0-9]*Perri|Rebecca[^a-zA-Z0-9]*Black|Patrick[^a-zA-Z0-9]*Stump|Fall[^a-zA-Z0-9]*Out[^a-zA-Z0-9]*Boy|Owl[^a-zA-Z0-9]*City|Lady[^a-zA-Z0-9]*Gaga|Tegan[^a-zA-Z0-9]*and[^a-zA-Z0-9]*Sara|Darin|Bridgit[^a-zA-Z0-9]*Mendler|Jesse[^a-zA-Z0-9]*McCartney|The[^a-zA-Z0-9]*Veronicas|Sufjan[^a-zA-Z0-9]*Stevens|Avicii|Craig[^a-zA-Z0-9]*David|Carrie[^a-zA-Z0-9]*Underwood|We[^a-zA-Z0-9]*the[^a-zA-Z0-9]*Kings|Cassadee[^a-zA-Z0-9]*Pope|One[^a-zA-Z0-9]*Direction|Christina[^a-zA-Z0-9]*Aguilera|Cardi[^a-zA-Z0-9]*B|Polo[^a-zA-Z0-9]*G|Kelly[^a-zA-Z0-9]*Clarkson|DaBaby|Kanye[^a-zA-Z0-9]*West|Troye[^a-zA-Z0-9]*Sivan|Diddy[^a-zA-Z0-9]*Dirty[^a-zA-Z0-9]*Money|Keyshia[^a-zA-Z0-9]*Cole|Becky[^a-zA-Z0-9]*Hill|Tyga|Daft[^a-zA-Z0-9]*Punk|Ozuna|Jake[^a-zA-Z0-9]*Bugg|Blake[^a-zA-Z0-9]*Shelton|Luke[^a-zA-Z0-9]*Bryan|Paris[^a-zA-Z0-9]*Jackson|Dido|Wiz[^a-zA-Z0-9]*Khalifa|Birdman|Boyzone|Ronan[^a-zA-Z0-9]*Keating|Britt[^a-zA-Z0-9]*Nicole|Gwen[^a-zA-Z0-9]*Stefani|Mary[^a-zA-Z0-9]*J[^a-zA-Z0-9]*Blige|Imagine[^a-zA-Z0-9]*Dragons|Echosmith|Patrick[^a-zA-Z0-9]*Stump|Willow[^a-zA-Z0-9]*Smith|La[^a-zA-Z0-9]*Roux|Priyanka[^a-zA-Z0-9]*Chopra|Tinie[^a-zA-Z0-9]*Tempah|Union[^a-zA-Z0-9]*J|Sophie[^a-zA-Z0-9]*Ellis[^a-zA-Z0-9]*Bextor|Victoria[^a-zA-Z0-9]*Justice|Jay[^a-zA-Z0-9]*Sean|Paramore|Ella[^a-zA-Z0-9]*Henderson|Hayley[^a-zA-Z0-9]*Williams|OneRepublic|Christina[^a-zA-Z0-9]*Aguilera|Conor[^a-zA-Z0-9]*Maynard|Lorde|Macklemore|Tinashe|Jedward|Shawn[^a-zA-Z0-9]*Mendes|Zendaya|ZEDD|Pixie[^a-zA-Z0-9]*Lott|Madonna|Jennifer[^a-zA-Z0-9]*Lopez|Sky[^a-zA-Z0-9]*Ferreira|HAIM|Sara[^a-zA-Z0-9]*Bareilles|Florence.+?The[^a-zA-Z0-9]*Machine|The[^a-zA-Z0-9]*Verve|Kacey[^a-zA-Z0-9]*Musgraves|Ke\$ha|Lady[^a-zA-Z0-9]*A|Anjulie|Hey[^a-zA-Z0-9]*Monday|Robbie[^a-zA-Z0-9]*Williams|Alan[^a-zA-Z0-9]*Walker|Doja[^a-zA-Z0-9]*Cat|Post[^a-zA-Z0-9]*Malone|24k[^a-zA-Z0-9]*Goldn|Grimes|Lauv|Aurora|Tokio[^a-zA-Z0-9]*Hotel|Tove[^a-zA-Z0-9]*Lo|Rita[^a-zA-Z0-9]*Ora|Liam[^a-zA-Z0-9]*Gallagher|DJ[^a-zA-Z0-9]*Khaled|Kelela|Benny[^a-zA-Z0-9]*Benassi|Calum[^a-zA-Z0-9]*Scott|Dizzee[^a-zA-Z0-9]*Rasca|KT[^a-zA-Z0-9]*Tunstall|Alicia[^a-zA-Z0-9]*Keys|Keri[^a-zA-Z0-9]*Hilson|Bj.+?rk|Alan[^a-zA-Z0-9]*Walker|Scissor[^a-zA-Z0-9]*Sisters|Gabrielle[^a-zA-Z0-9]*Aplin|Markus[^a-zA-Z0-9]*Feehilly|Kim[^a-zA-Z0-9]*Petras|Weeknd|Crystal[^a-zA-Z0-9]*Fighters|Keane|The[^a-zA-Z0-9]*Corrs|James[^a-zA-Z0-9]*Blunt|Lil[^a-zA-Z0-9]*Nas[^a-zA-Z0-9]*X|Sabrina[^a-zA-Z0-9]*Carpenter|Samantha[^a-zA-Z0-9]*Jade|Kimbra|Delta[^a-zA-Z0-9]*Goodrem|Eva[^a-zA-Z0-9]*Simons|Cheryl[^a-zA-Z0-9]*Cole|Edward[^a-zA-Z0-9]*Maya|Skylar[^a-zA-Z0-9]*Grey|Foster[^a-zA-Z0-9]*The[^a-zA-Z0-9]*People|You[^a-zA-Z0-9]*Me[^a-zA-Z0-9]*At[^a-zA-Z0-9]*Six|Gorgon[^a-zA-Z0-9]*City|Kazaky|ZAYN|Joshua[^a-zA-Z0-9]*Bassett|Bruno[^a-zA-Z0-9]*Mars|Betty[^a-zA-Z0-9]*Who|Beyonce|Mylene[^a-zA-Z0-9]*Farmer|Lindsey[^a-zA-Z0-9]*Stirling|Victoria[^a-zA-Z0-9]*Monét|Liam[^a-zA-Z0-9]*Gallagher|Pablo[^a-zA-Z0-9]*Alboran|Sarah[^a-zA-Z0-9]*Bareilles|olly[^a-zA-Z0-9]*alexander|linkin[^a-zA-Z0-9]*park|Sam[^a-zA-Z0-9]*Hunt|Mat[^a-zA-Z0-9]*Kearney|Kris[^a-zA-Z0-9]*Allen|Goldfrapp|Olivia[^a-zA-Z0-9]*Rodrigo|John[^a-zA-Z0-9]*Mayer|Michelle[^a-zA-Z0-9]*Branch|Tame[^a-zA-Z0-9]*Impala|Ashley[^a-zA-Z0-9]*Tisdale|Florida[^a-zA-Z0-9]*Georgia[^a-zA-Z0-9]*Line|Anne[^a-zA-Z0-9]*Marie|Maroon[^a-zA-Z0-9]*5|Steve[^a-zA-Z0-9]*Aoki|Charli[^a-zA-Z0-9]*XCX|Vance[^a-zA-Z0-9]*Joy|James[^a-zA-Z0-9]*Bay|Robyn|Tove[^a-zA-Z0-9]*Styrke|American[^a-zA-Z0-9]*Authors|Adam[^a-zA-Z0-9]*Lambert|Cobra[^a-zA-Z0-9]*Starship|Natasha[^a-zA-Z0-9]*Bedingfeld|Gorgon[^a-zA-Z0-9]*City|Lil[^a-zA-Z0-9]*Yachty|Say[^a-zA-Z0-9]*Lou[^a-zA-Z0-9]*Lou|Rihanna|Ariana[^a-zA-Z0-9]*Grande|Gabrielle[^a-zA-Z0-9]*Aplin|Arcade[^a-zA-Z0-9]*Fire|NOTD|2Chainz|Asher[^a-zA-Z0-9]*Angel|Megan[^a-zA-Z0-9]*Thee[^a-zA-Z0-9]*Stallion|Daya|PRETTYMUCH|LEWIS[^a-zA-Z0-9]*CAPALDI|Charlie[^a-zA-Z0-9]*Puth|JAMES[^a-zA-Z0-9]*ARTHUR|FKA[^a-zA-Z0-9]*twigs|Howie[^a-zA-Z0-9]*Day|SHAKIRA|Havana[^a-zA-Z0-9]*Brown|Travis[^a-zA-Z0-9]*Barker|Cody[^a-zA-Z0-9]*Simpson|Avril[^a-zA-Z0-9]*Lavigne|Jonas[^a-zA-Z0-9]*Brothers|Cyndi[^a-zA-Z0-9]*Lauper|Matoma|Miriam[^a-zA-Z0-9]*Bryant|XXXTENTACION|Dillon[^a-zA-Z0-9]*Francis|Vanessa[^a-zA-Z0-9]*Hudgens|Kygo|Aloe[^a-zA-Z0-9]*Blacc|Grace[^a-zA-Z0-9]*VanderWaal|Soulja[^a-zA-Z0-9]*Boy|David[^a-zA-Z0-9]*Archuleta|AlunaGeorge|Rick[^a-zA-Z0-9]*Ross|Ava[^a-zA-Z0-9]*Max|Martin[^a-zA-Z0-9]*Garrix|Hayley[^a-zA-Z0-9]*Kiyoko|Rag[^a-zA-Z0-9]*Bone[^a-zA-Z0-9]*Man|P!NK|ROSALÍA|Capital[^a-zA-Z0-9]*Cities|Ellie[^a-zA-Z0-9]*Goulding|Little[^a-zA-Z0-9]*Mix|Janet[^a-zA-Z0-9]*Jackson|Eminem|Solange|slowthai|Enya|Snoop Dogg|YUNGBLUD|Pitbull|One[^a-zA-Z0-9]*Pilots|Lykke[^a-zA-Z0-9]*Li|SKY[^a-zA-Z0-9]*FERREIRA|Kat[^a-zA-Z0-9]*DeLuna|Jessie[^a-zA-Z0-9]*Ware|X[^a-zA-Z0-9]*AMBASSADORS|SAM[^a-zA-Z0-9]*SMITH|SAINt[^a-zA-Z0-9]*JHN|Black[^a-zA-Z0-9]*Atlass|Celiné[^a-zA-Z0-9]*Dion|RUN[^a-zA-Z0-9]*THE[^a-zA-Z0-9]*JEWELS|Zella[^a-zA-Z0-9]*Day|Tom[^a-zA-Z0-9]*Grennan|Green[^a-zA-Z0-9]*Day|blur|Enrique[^a-zA-Z0-9]*Iglesias|Melanie[^a-zA-Z0-9]*C|Azealia[^a-zA-Z0-9]*Banks|Michael[^a-zA-Z0-9]*Bublé|Sebastián[^a-zA-Z0-9]*Yatra|Nothing[^a-zA-Z0-9]*But[^a-zA-Z0-9]*Thieves|Sixpence[^a-zA-Z0-9]*None[^a-zA-Z0-9]*The[^a-zA-Z0-9]*Richer|Paloma[^a-zA-Z0-9]*Faith|David[^a-zA-Z0-9]*Guetta|Zara[^a-zA-Z0-9]*Larsson|Taylor[^a-zA-Z0-9]*Swift|Noel[^a-zA-Z0-9]*Gallagher|SOFIA[^a-zA-Z0-9]*CARSON|Miley[^a-zA-Z0-9]*Cyrus|Anitta|Weezer|Shayne[^a-zA-Z0-9]*Ward|Hunter[^a-zA-Z0-9]*Hayes|Halsey|Mark[^a-zA-Z0-9]*Ronson|Conan[^a-zA-Z0-9]*Gray|Jake[^a-zA-Z0-9]*Miller|Travis[^a-zA-Z0-9]*Scott|Harry[^a-zA-Z0-9]*Styles|Luis[^a-zA-Z0-9]*Fonsi|DJ[^a-zA-Z0-9]*Snake|Don[^a-zA-Z0-9]*Diablo|Icona[^a-zA-Z0-9]*Pop|NE\-YO|NEYO|Lil[^a-zA-Z0-9]*Uzi[^a-zA-Z0-9]*Vert|J.[^a-zA-Z0-9]*Balvin|Gnarls[^a-zA-Z0-9]*Barkley|Maluma|Mike[^a-zA-Z0-9]*Shinoda|Paul[^a-zA-Z0-9]*McCartney|Sugababes|St\.[^a-zA-Z0-9]*Vincent|Grimes|The[^a-zA-Z0-9]*XX|Jamie[^a-zA-Z0-9]*XX|Goldfrapp|Cheryl|Vampire[^a-zA-Z0-9]*Weekend|Britney|Britney[^a-zA-Z0-9]*Spears|Kylie|Shania[^a-zA-Z0-9]*Twain|JLO|Drake|Maren[^a-zA-Z0-9]*Morris|Red[^a-zA-Z0-9]*Hot[^a-zA-Z0-9]*Chilli[^a-zA-Z0-9]*Peppers|RHCP|Depeche[^a-zA-Z0-9]*Mode|No[^a-zA-Z0-9]*Doubt|Passenger|Liam[^a-zA-Z0-9]*Payne|Liam[^a-zA-Z0-9]*Payne|WESTLIFE|Backstreet[^a-zA-Z0-9]*Boys|Simple[^a-zA-Z0-9]*Plan|OK[^a-zA-Z0-9]*GO|Suede|Timbaland|Mariah[^a-zA-Z0-9]*Carey|years.+?years|Nickelback|Idina[^a-zA-Z0-9]*Menzel|Snow[^a-zA-Z0-9]*Patrol|Missy[^a-zA-Z0-9]*Elliott|Gotye|Annie[^a-zA-Z0-9]*Lennox|Adele|Gabby[^a-zA-Z0-9]*Barrett|Kane[^a-zA-Z0-9]*Brown|Luke[^a-zA-Z0-9]*Combs|Chris[^a-zA-Z0-9]*Stapleton|Florida[^a-zA-Z0-9]*Georgia[^a-zA-Z0-9]*Line|Camila[^a-zA-Z0-9]*Cabello|take[^a-zA-Z0-9]*that|My[^a-zA-Z0-9]*Chemical[^a-zA-Z0-9]*Romance|Arctic[^a-zA-Z0-9]*Monkeys|Sam[^a-zA-Z0-9]*Hunt|Mac[^a-zA-Z0-9]*Miller|Norah[^a-zA-Z0-9]*Jones|Joss[^a-zA-Z0-9]*Stone|Amy[^a-zA-Z0-9]*Winehouse|Marina|Hilary[^a-zA-Z0-9]*Duff|Hey[^a-zA-Z0-9]*Monday|M\Ø|Carly[^a-zA-Z0-9]*Rae[^a-zA-Z0-9]*Jepsen|Far[^a-zA-Z0-9]*East[^a-zA-Z0-9]*Movement|Girls[^a-zA-Z0-9]*Aloud|A[^a-zA-Z0-9]*Great[^a-zA-Z0-9]*Big[^a-zA-Z0-9]*World|Barbra[^a-zA-Z0-9]*Streisand|Alexandra[^a-zA-Z0-9]*Burke|Evanescence|YNW[^a-zA-Z0-9]*Melly|Alexandra[^a-zA-Z0-9]*Stan|Daddy[^a-zA-Z0-9]*Yankee|Calvin[^a-zA-Z0-9]*Harris|Hozier|Ace[^a-zA-Z0-9]*Of[^a-zA-Z0-9]*Base|Brandy|Meghan[^a-zA-Z0-9]*Trainor|Fergie|Ashanti|Faith[^a-zA-Z0-9]*Hill|Tim[^a-zA-Z0-9]*McGraw|Keith[^a-zA-Z0-9]*Urban|Ciara|Toni[^a-zA-Z0-9]*Braxton|Nelly[^a-zA-Z0-9]*Furtado|Natasha[^a-zA-Z0-9]*Bedingfield|Ricky[^a-zA-Z0-9]*Martin|Emeli[^a-zA-Z0-9]*Sand|Kings[^a-zA-Z0-9]*Of[^a-zA-Z0-9]*Leon|Robin[^a-zA-Z0-9]*Thicke|Leona[^a-zA-Z0-9]*Lewis|Kelly[^a-zA-Z0-9]*Rowland|Matchbox[^a-zA-Z0-9]*Twenty|Meek[^a-zA-Z0-9]*Mill|Ludacris|AP[^a-zA-Z0-9]*Rocky|Snoop[^a-zA-Z0-9]*Dogg|Rich[^a-zA-Z0-9]*Brian|Gucci[^a-zA-Z0-9]*Mane|Ace[^a-zA-Z0-9]*Hood|Rich[^a-zA-Z0-9]*Homie[^a-zA-Z0-9]*Quan|Olly[^a-zA-Z0-9]*Murs|Soulja[^a-zA-Z0-9]*Boy|Kehlani|Wretch[^a-zA-Z0-9]*32|Trey[^a-zA-Z0-9]*Songz|Danny[^a-zA-Z0-9]*Brown|Hurts|Jess[^a-zA-Z0-9]*Glynne|Trina|Saweetie|Roddy[^a-zA-Z0-9]*Ricch|LMFAO|David[^a-zA-Z0-9]*Bowie|M2M|LeAnn[^a-zA-Z0-9]*Rimes|John[^a-zA-Z0-9]*Legend|Tiëst|Conor[^a-zA-Z0-9]*Maynard|Iggy[^a-zA-Z0-9]*Azaela|The[^a-zA-Z0-9]*Pretty[^a-zA-Z0-9]*Reckless)([^a-z].+?from )(.+?<\/title>.+?)(\"duration\"\:[0-9]{3,}\,)(.+?account\_type\"\:\")(未知|advanced|starter|standard|custom|business|business_lapsed|pro_lapsed|plus_lapsed|pro|plus|premium|enterprise|live\_premium)(\".*)'  /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999" >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".html
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
