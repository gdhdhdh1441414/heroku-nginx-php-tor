#!/bin/bash
num=$1
ulimit -n 2048

aria2c -x16 https://crowncloud.362227.top/remote/data/%E5%90%88%E5%B9%B6$num"000000"-$num"999999".log.404.txt -c --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据 -o oembed链接合并$num"000000"-$num"999999".log.404.txt
sed -i 's/^http/https:\/\/362227.top\/rss\/刷vimeojson跳转地址.php?url=http/g'  /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/oembed链接合并$num"000000"-$num"999999".log.404.txt

filesize=$(stat -c%s "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/oembed链接合并${num}000000-${num}999999.log.404.txt")



aria2c  --referer=http://friendlondon.tv --check-certificate=false -i "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/oembed链接合并$num"000000"-$num"999999".log.404.txt" --file-allocation=none --max-concurrent-downloads=38 --disk-cache=0 --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/ --max-download-result=20000000




find "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/" -maxdepth 1 -type f -name "*" | xargs sed 'a\' > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash待提取链接


echo 提取json里的hash链接并转化player（https://player.vimeo.com/video/459308754?h=96d00201ea）
python3 /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/提取json里的hash链接player.py /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash待提取链接 > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash链接player.txt


aria2c  --referer=http://friendlondon.tv --check-certificate=false -i "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash链接player.txt" --file-allocation=none --max-concurrent-downloads=700 --disk-cache=0 --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/hash --max-download-result=20000000 


#python /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/从log文件提取有ref的链接.py > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/有ref的链接.txt
#IP=( "https://trimediting.com/"  "https://somesuch.co/ " "https://www.petgorilla.com/"  "http://malloybrothers.com/" "http://alexanderhammer.com/"  "http://ways-means.co" "http://www.romanwhite.com" ); IP1=( "http://loucloutercasting.com/" "https://www.themill.com/"  "https://www.ntropic.com/"  "http://coffeeand.tv" "http://believemedia.com" "http://modernpost.com" "http://www.treyfanjoy.com/" ) ; for i in "${IP[@]}";do aria2c  --referer=$i -i "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/有ref的链接.txt" --file-allocation=none --max-concurrent-downloads=500 --disk-cache=0 --check-certificate=false --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/ref; done & for i1 in "${IP1[@]}";do aria2c  --referer=$i1 -i "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/有ref的链接.txt" --file-allocation=none --max-concurrent-downloads=494 --disk-cache=0 --check-certificate=false --dir=/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/ref; done  &



echo 删除重复小文件hash
find "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/hash"  -type f -name "*.*" -delete


echo 合并为大文件hash
find "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/temp/hash"  -type f -name "*" | xargs sed 'a\' > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash大文件

echo 提取合并为大文件hash里的403链接
grep -a -E '^.{30,60}$' /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash大文件 > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash403纯链接


echo 提取最终数据$num"000000"-$num"999999".hash

egrep -a -i '(title.+?[^a-zA-Z])(prores|vfx|Nick *Jonas|Chris *Brown|The *Streets|Ice *Spice|PinkPantheress|Kasabian|Nightwish|Sam *Feldt|ROSALÍA|Nine *Inch *Nails|Pvris|Within *Temptation|C\.Tangana|Rauw *Alejandro|Li.+?Tjay|Portugal *The *Man|Tate *McRae|Depeche *Mode|Natti *Natasha|Summer *Walker|Ashnikko|Billy *Idol|Rolling *Stones|Tangana|Emeli *Sandé|Emeli *Sande|Duran *Duran|Jonas *Blue|J *Balvin|Noah *Cyrus|Sarah *Brightman|Dermot *Kennedy|Lizzo|RUDIMENTAL|The *Fray|PVRIS|Ryan *Tedder|Charlotte *OC|Dove *Cameron|Yellowcard|London *Grammar|Ty *Dolla|Popcaan|Rich *Brian|Bryson *Tiller|King *Princess|Sigrid|Shane *Filan|TONES *AND *I|Silk *Sonic|Ladyhawke|Lil *Tecca|Mick *Jagger|Robin *Schulz|MOD *SUN|Ashlee *Simpson|Trippie *Redd|Metronomy|Busta *Rhymes|Angel *Olsen|H\.E\.R\.|Johnny *Orlando|Gallant|Swedish *House *Mafia|The *Strokes|Fiona *Apple|Pabllo *Vittar|Royal *Blood|Bleachers|Skrillex|Pet *Shop *Boys|Foals|DJ *SMASH|Princess *Nokia|GAYLE|DJ *Mustard|Brandi *Carlile|Doechii|Sam *Fender|Metallica|SZA|Niall *Horan|Jason *Derulo|JP *Saxe|Swedish *House *Mafia|Jorja *Smith|AJ *Mitchell|American *Rejects|Cheat *Codes|Luke *Hemmings|London *Grammar|Kristian *Kostov|Alec *Benjamin|Ryan *Tedder|Emeli *Sand́e|Big *Sean|Kendrick *Lamar|Khalid|Travie *McCoy|Juice *WRLD|Pussycat *Dolls|Young *Thug|Jhene *Aiko|The *Wanted|ABBA|H\.E\.R\.|James *Bay|Ace *Of *Base|Keyshia *Cole|Idina *Menzel|Sam *Hunt|Roddy *Ricch|Jason *Mraz|Justin *Bieber|Justin *Timberlake|Nicki *Minaj|Becky *G|Ed *Sheeran|Lana *Del *Rey|Katy *Perry|Mike *Posner|JLS|Lawson|Coldplay|Nicole *Scherzinger|The *Vamps|Selena *Gomez|Leighton *Meester|GORILLAZ|Dua *Lipa|Demi *Lovato|Christina *Perri|Black *Eyed *Peas|Seconds *To *Mars|Birdy|Dappy|Hailee *Steinfeld|Michael *Bubl|MIKA|The *Script|Boyzone|Machine *Gun *Kelly|Jessie *J|Taio *Cruz|Marshmello|Diplo|Pia *Mia|Billie *Eilish|Christina *Perri|Rebecca *Black|Patrick *Stump|Fall *Out *Boy|Owl *City|Lady *Gaga|Tegan *and *Sara|Darin|Bridgit *Mendler|Jesse *McCartney|The *Veronicas|Sufjan *Stevens|Avicii|Craig *David|Carrie *Underwood|We *the *Kings|Cassadee *Pope|One *Direction|Christina *Aguilera|Cardi *B|Polo *G|Kelly *Clarkson|DaBaby|Kanye *West|Troye *Sivan|Diddy *Dirty *Money|Keyshia *Cole|Becky *Hill|Tyga|Daft *Punk|Ozuna|Jake *Bugg|Blake *Shelton|Luke *Bryan|Paris *Jackson|Dido|Wiz *Khalifa|Birdman|Boyzone|Ronan *Keating|Britt *Nicole|Gwen *Stefani|Mary *J *Blige|Imagine *Dragons|Echosmith|Patrick *Stump|Willow *Smith|La *Roux|Priyanka *Chopra|Tinie *Tempah|Union *J|Sophie *Ellis *Bextor|Victoria *Justice|Jay *Sean|Paramore|Ella *Henderson|Hayley *Williams|OneRepublic|Christina *Aguilera|Conor *Maynard|Lorde|Macklemore|Tinashe|Jedward|Shawn *Mendes|Zendaya|ZEDD|Pixie *Lott|Madonna|Jennifer *Lopez|Sky *Ferreira|HAIM|Sara *Bareilles|Florence.+?The *Machine|The *Verve|Kacey *Musgraves|Ke\$ha|Lady *A|Anjulie|Hey *Monday|Robbie *Williams|Alan *Walker|Doja *Cat|Post *Malone|24k *Goldn|Grimes|Lauv|Aurora|Tokio *Hotel|Tove *Lo|Rita *Ora|Liam *Gallagher|DJ *Khaled|Kelela|Benny *Benassi|Calum *Scott|Dizzee *Rasca|KT *Tunstall|Alicia *Keys|Keri *Hilson|Bj.+?rk|Alan *Walker|Scissor *Sisters|Gabrielle *Aplin|Markus *Feehilly|Kim *Petras|Weeknd|Crystal *Fighters|Keane|The *Corrs|James *Blunt|Lil *Nas *X|Sabrina *Carpenter|Samantha *Jade|Kimbra|Delta *Goodrem|Eva *Simons|Cheryl *Cole|Edward *Maya|Skylar *Grey|Foster *The *People|You *Me *At *Six|Gorgon *City|Kazaky|ZAYN|Joshua *Bassett|Bruno *Mars|Betty *Who|Beyonce|Mylene *Farmer|Lindsey *Stirling|Victoria *Monét|Liam *Gallagher|Pablo *Alboran|Sarah *Bareilles|olly *alexander|linkin *park|Sam *Hunt|Mat *Kearney|Kris *Allen|Goldfrapp|Olivia *Rodrigo|John *Mayer|Michelle *Branch|Tame *Impala|Ashley *Tisdale|Florida *Georgia *Line|Anne *Marie|Maroon *5|Steve *Aoki|Charli *XCX|Vance *Joy|James *Bay|Robyn|Tove *Styrke|American *Authors|Adam *Lambert|Cobra *Starship|Natasha *Bedingfeld|Gorgon *City|Lil *Yachty|Say *Lou *Lou|Rihanna|Ariana *Grande|Gabrielle *Aplin|Arcade *Fire|NOTD|2Chainz|Asher *Angel|Megan *Thee *Stallion|Daya|PRETTYMUCH|LEWIS *CAPALDI|Charlie *Puth|JAMES *ARTHUR|FKA *twigs|Howie *Day|SHAKIRA|Havana *Brown|Travis *Barker|Cody *Simpson|Avril *Lavigne|Jonas *Brothers|Cyndi *Lauper|Matoma|Miriam *Bryant|XXXTENTACION|Dillon *Francis|Vanessa *Hudgens|Kygo|Aloe *Blacc|Grace *VanderWaal|Soulja *Boy|David *Archuleta|AlunaGeorge|Rick *Ross|Ava *Max|Martin *Garrix|Hayley *Kiyoko|Rag *Bone *Man|P!NK|ROSALÍA|Capital *Cities|Ellie *Goulding|Little *Mix|Janet *Jackson|Eminem|Solange|slowthai|Enya|Snoop Dogg|YUNGBLUD|Pitbull|One *Pilots|Lykke *Li|SKY *FERREIRA|Kat *DeLuna|Jessie *Ware|X *AMBASSADORS|SAM *SMITH|SAINt *JHN|Black *Atlass|Celiné *Dion|RUN *THE *JEWELS|Zella *Day|Tom *Grennan|Green *Day|blur|Enrique *Iglesias|Melanie *C|Azealia *Banks|Michael *Bublé|Sebastián *Yatra|Nothing *But *Thieves|Sixpence *None *The *Richer|Paloma *Faith|David *Guetta|Zara *Larsson|Taylor *Swift|Noel *Gallagher|SOFIA *CARSON|Miley *Cyrus|Anitta|Weezer|Shayne *Ward|Hunter *Hayes|Halsey|Mark *Ronson|Conan *Gray|Jake *Miller|Travis *Scott|Harry *Styles|Luis *Fonsi|DJ *Snake|Don *Diablo|Icona *Pop|NE\-YO|NEYO|Lil *Uzi *Vert|J. *Balvin|Gnarls *Barkley|Maluma|Mike *Shinoda|Paul *McCartney|Sugababes|St\. *Vincent|Grimes|The *XX|Jamie *XX|Goldfrapp|Cheryl|Vampire *Weekend|Britney|Britney *Spears|Kylie|Shania *Twain|JLO|Drake|Maren *Morris|Red *Hot *Chilli *Peppers|RHCP|Depeche *Mode|No *Doubt|Passenger|Liam *Payne|Liam *Payne|WESTLIFE|Backstreet *Boys|Simple *Plan|OK *GO|Suede|Timbaland|Mariah *Carey|years.+?years|Nickelback|Idina *Menzel|Snow *Patrol|Missy *Elliott|Gotye|Annie *Lennox|Adele|Gabby *Barrett|Kane *Brown|Luke *Combs|Chris *Stapleton|Florida *Georgia *Line|Camila *Cabello|take *that|My *Chemical *Romance|Arctic *Monkeys|Sam *Hunt|Mac *Miller|Norah *Jones|Joss *Stone|Amy *Winehouse|Marina|Hilary *Duff|Hey *Monday|M\Ø|Carly *Rae *Jepsen|Far *East *Movement|Girls *Aloud|A *Great *Big *World|Barbra *Streisand|Alexandra *Burke|Evanescence|YNW *Melly|Alexandra *Stan|Daddy *Yankee|Calvin *Harris|Hozier|Ace *Of *Base|Brandy|Meghan *Trainor|Fergie|Ashanti|Faith *Hill|Tim *McGraw|Keith *Urban|Ciara|Toni *Braxton|Nelly *Furtado|Natasha *Bedingfield|Ricky *Martin|Emeli *Sand|Kings *Of *Leon|Robin *Thicke|Leona *Lewis|Kelly *Rowland|Matchbox *Twenty|Meek *Mill|Ludacris|AP *Rocky|Snoop *Dogg|Rich *Brian|Gucci *Mane|Ace *Hood|Rich *Homie *Quan|Olly *Murs|Soulja *Boy|Kehlani|Wretch *32|Trey *Songz|Danny *Brown|Hurts|Jess *Glynne|Trina|Saweetie|Roddy *Ricch|LMFAO|David *Bowie|M2M|LeAnn *Rimes|John *Legend|Tiëst|Conor *Maynard|Iggy *Azaela|The *Pretty *Reckless)([^a-z].+?from )(.+?<\/title>.+?)(\"duration\"\:[0-9]{3,}\,)(.+?account\_type\"\:\")(未知|business|business_lapsed|pro_lapsed|plus_lapsed|pro|plus|premium|enterprise|live\_premium)(\".*)'  /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash大文件 > /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash.html
egrep -a -i '(.+?\"name\"\:\")(Spectraevenko|FORTRESS LA|spacebar.+?louis palacios|COMPULSORY\.|Warner Global Catalog|Rhino Entertainment|Derec Dunn|Lou Clouter Casting|Forgotten Sundays|Somesuch Archive|The Mill|Andrew Donoho|The Banquet|Spearing Films|Feel Films|Jo Jo Lam|Feel Films|AFX Creative|Sam Siske|Warp Records|Powell Robinson|Dylan Rucker|Gear Seven|Tim Mattia|Alex Southam|Peter Zavadil|Tim Nackashi|Taillight|Taillight - Rough Cuts|Justin Clough|David Waterston|Taylor James|Family Creative|Legion Post|Matt Wise|patarakina|Jump VFX|jack pyland|Inez & Vinoodh|Anchor Light|KMOYES PICTURES|Adric Watson|Vania Heymann|Gal Muggia|Daniel Bronks|Simona Cristea|Duncan Russell|Jordan Bahat|Eric Wysocki|arnau valls colomer|Johnny Richards|ImagePartnership|Greatcoat Films|GUS BLACK|Andrew Thomas Huang|Joel Honeywell|Mack Fisher Cinematography|Nicholas Bupp|Ntropic Group|PET.+?RILLA|VisualCreatures|Gwen Ghelid|Alexander Hammer|Malloy Brothers|B Pictures|benz.+?ne|Alex Bartz|Mathieu Plainfoss.+?C|Park Pictures|Reset|Brad Rushing|Ways.+?Means|David Baum|LANE Archive|Christian Breslauer|Pulse Films|MINDED|Color Collective|Roman White|Trey Fanjoy|Johan Renck|Rock Paper Scissors|Nomad Editing Company Inc\.|The Den|Modern Post|Ramone Anderson|Johnny Richards|CheekyFilms|Lauri Laukkanen|IC|Supermega Films|Big Branch Productions|NoCap Shows|Psyop|Kenneth T Shimm|DeNovaMedia|Grayskull.tv|CA|FRIEND|Trim Editing|Ed Rutherford|Omer Ganai|TRAFIC|Gang Films|Jeremy Alter|Daniel Pearl.+?ASC|Airship|Soho House|Vicky Lawton|OPTIX|Agile Films|Max McGill|josh forbes|Evgeny Bystrov|Mason W.+?Dixon|CHEAT|Fancy Content|Sam Wrench|Tuff Contender|Larkin Seiple|Universal Music Publishing.+>?|THE YOUNG ASTRONAUTS|brooks|JOE SILL|Thomas Grove Carter|Remy Naidoo|iHeartRadio Events|TheFlyFamily|Beggars Group|Taylor Vandegrift|Raja Virdi|Jeremy Gosch|Neutra Production|Goldheart Post|Miles Trahan|Bruzier|Mutter .+?Productions GmbH|Bruno Ilogti|Rick Wilson|MM8|Davy Duhamel|Baris Aladag|Senior Post|WE WRK WKNDS|BEN GOODMAN|Ulrik Boel Bentzen|KIBORZ|Janssen Powers|Casey McPerry|Hellfire Creative|Hellfire Creative|Wild Stag Studio|Danila Volkov|Outside Lands Music Festival|Motion Eccentric.+?|TA Films|Kode Media|WJF|XIMedia|Mutt .+? Man|Sequitur Cinema|Doug Porter|Chris Westlund|Nick Pezzillo|Derek Hansen|Oren Soffer|Matt Schaff|Sam Care.+?Cinematographer|Amazon Music|Jacob Lees Johnson|Bryant Jansen|Dillon Schneider DP|BRADLEY .+?PABLO|The Quarry|dick clark productions|Ross Richardson|NYLA PROJECTS|HUNTER LYON|Patrick Lawler|WGTAM|Domino Recording Co|WE|BPI|Tim Nackashi|industry plant.+?|Jonny Tully|Eli Arenson|Austin City Limits|Sholight Live|Concord|Burning Reel|Baeblemusic|Johnny Marchetta|riffraff films|Antiest.+?ico|Thievery Studio|GLASSWORKS VFX|ALL OF IT NOW|JOHN TASHIRO|Jon Chema|Will Ngo|HAUS Pictures|DCP|LiveXLive|Urban Strom|Alex Bartz|Chris Davis|Warner Music.+?|Myriad Video|Symphonic Distribution|wash|Moon|Carlos Veron|L.+?Castle Studios|C3 Presents|Brooke James Productions|simian.+?la|ACNE|Epic Records|Forest of Black|Pinecone|Neema Sadeghi|La Blogotheque|Anthony Mark Saul|Joe Shahood|ATLANTIC VIDEO CONTENT|Sunset Edit|anonymous content|ed|Max Colt|OPERANDI MGMT|Cut.+?Run|Diane MartelThe Directors Bureau|Carbon|Mathematic Studio|Adam Zuckerman|Hound|MAAVVEN|reen Glow Films|Hans Carrillo|Jonas .+?kerlund Film|Sesler|Luti Media|Final Cut|Electric Theatre Collective|Moxie Pictures|Black Dog Films|Chris Roebuck|PAUL DUGDALE|Therapy Studios|RASCAL|Jason Zada|Greyson A.+?Welch|Supply.+?Demand|Scheme Engine|Company 3|James|Jamie Yuan|Dempsey Productions|Alex Chaloff|Ben Backhaus|BEMO|Lord Danger|Georgie Edelstein|Emma Rose Mead|Charlotte Russe Films|Cinema Giants Inc Film\/TV|Eric Bader|iHeartMedia|Riveting Entertainment|The Saline Project|TRASH FACTORY|Electric Light Studios|Cal Laird|HPLA|Biscuit Filmworks|Forever|david m\. helman|Loma Vista|FILM TANK|Cabin Editing Company|Magic Seed|Noah Clark \- Station 22|FAMILIA|Object .+?Animal|Gevorg Gev Juguryan|andresdp|VH POST|Exile Edit|BW|Fela|We Make Them Wonder|CanadaPost|Directors.+?DoPs|Gilbert Soliz|tempomedia|Swords .+?Eagles|Lacey Duke|A\-Frame Agency|argentinacine.+?referencias|Dan Kennedy|Matt Eastwood|Ammolite Inc|Tobias Rupp|The Funnel Creative|PAUL DUGDALE|JAX HARNEY|Trevor Wineman|Adam Zuckerman|Gil Green|CY|Untold Studios|Work Editorial|Justin Clough|Diane Martel|SONY MUSIC UK|London Alley|Colin Tilley|Metropolitana|Time Based Arts|Stereohorse|Happy Street|Warner Music|Electric Light Studios|BendEditor|Andrew Sandler|Darren Miller|Isaac Bauman|Coffee .+?TV|Luti Media|Edit Egg|adria petty|Rogue Films|Phillip Lopez|Grant Singer|Skulley Effects|Tomorrow|Jason McCormick|Jeremy Cross|Son.+?Heir|Greatcoat Films|Santiago Gonzalez|Supermega Films|Aya Tanimura|Tacklebox Upload|NtropicStudios|joel kefali|Bill Pollock|Sebastian Zotoff|Jack Begert|Malia James|2 Wolves Films|hangman|Tom Banks|Loren White|Paul B|The Rella Group|Brielle Hubert|Benjamin Kitchens|Michael Belcher|arnau valls colomer|Black Label Content|Arrad|Ben Carey|David Foulkes|AVIDDIVA|chriscottamfilms|Warner Records|Allie Avital|ARTJAIL|HELO|isaacrentz|Max Goldman|malik sayeed|Schafler Artists|Justin Hamilton|Huffman Creative|Riveting Entertainment|Happy Place|MAMAG STUDIOS|Blindeye Films|Color by Gloss|JONATHAN LAGACHE|Betterdays|Syndicate Entertainment|Marz Miller|Forager|Erik Sohlström|Max Vitali|Rock Paper Scissors|Pieter Mattheus Snyman III|sophie muller|Flaura Atkinson|Cut.+?Run|EAGER!|Lacey Duke|Drive Studios|Dennis Leupold|Carlos Lopez Estrada|XO MGMT|Mike Ho|Lux Artists|Constellation Jones|Dave Meyers|Rich Lee|PRETTYBIRD|Mute|RankinFilm|No.8|Bonch|XL RECORDINGS|P.R. Brown|DIVISION|My Accomplice|LAMAR BROTHERS|Tomás Whitmore|Benoit Soler|RSA Films|Outsider|Nate Gross|Farah X|declan whitebloom|Emilie Aubry|Les Umberger|MLM POST|ATLANTIC RECORDS VIDEO|Chris Dooley|Mathematic Studio|Merman|Octopus Inc|OBB Pictures|Velem|TK McKamy|Swords .+?Eagles|Jonathan Chou|PHILIPPA PRICE|ANTON TAMMI|Pine|Simon Hilton|BUF|Iconic Talent Agency|Xiaolong Liu|Memory Man|Obsidian|Flawless Post|Diktator|Lalim Edit|Incolor Inc\.|BWGTBLD|Lisa Ryan Smith|nabil elderkin|Andrew Stroud|Molly Manning Walker|Dan Lightening|MP Clubhouse|RadicalMedia|Marcus Domleo|MAAVVEN|Hound|Loom|Mike Reyes|Bucket Pictures|Contrast Films|SMUGGLER|Benoit Delhomme|Malloy Brothers|Max Colt|Christopher Ripley|Roisín Audrey Moloney|Caviar|BRTHR|Serial Pictures|Kaname Onoyama|Jonathan Walton|Lockt Editorial|Kai Saul|Vision Film Co|Believe Media.+?\.|Scheme Engine|Darren Grant|ra.+?gonzo|DREW KIRSCH|Miles Trahan|Brandon Dermer|alexandre moors|Match Music|Santiago Gonzalez|BRTHR|Tom.+?Whitmore|Huffman Creative|Darren Doane|Bo Mirhosseni|Green Glow Films|olivier Cariou|Favourite Colour.+?Black|HULK|D O M \& N I C|Aaron A|Gil Green|Dikayl Rimmaschla|Isaac Ravishankara|Corey C\. Waters|Brook Linder|Vania Heymann|Gal Muggia|J. A. Moreno|Angel Barroeta SVC|Daniel Broadley|AdamBecht|Andrew Sandler|APLUSFILMZ|Malia James|JM Films|Psycho Films|Theo Adams Company|David Bolen|Adam Newport-Berra|Kai Blamey Nguyen)(\".*)'  /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash大文件 >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash.html
egrep -a -i '(title>.+?)(3200x1800|4444 |pr422|422hq|bitmax|gbuv|usuv|usum|uswv|usrv|ussm|usatv)(.+? from .+?<\/title>.+?)(\"duration\"\:[0-9]{3,}\,).+?account\_type\"\:\"(?:未知|business|business_lapsed|pro_lapsed|plus_lapsed|pro|plus|premium|enterprise|live\_premium)(\".*)'  /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash大文件 >> /mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash.html


txt=$(curl  -F file=@/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999".hash.html  https://api.anonfiles.com/upload  | grep  '"full"' | sed 's/\\//g' | sed -nE 's/.*"full": "([^"]*)".*/\1/p')
curl https://362227.top/rss/file.php?text=$txt 

txt=$(curl  -F file=@/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并$num"000000"-$num"999999.hash大文件"  https://api.anonfiles.com/upload  | grep  '"full"' | sed 's/\\//g' | sed -nE 's/.*"full": "([^"]*)".*/\1/p' )
curl https://362227.top/rss/file.php?text=$txt 
