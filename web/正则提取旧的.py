import re
import glob
path = "/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/合并*9"
for filename in glob.glob(path):
    with open(filename, encoding='gbk', errors='ignore') as f:

# 读入文件
#with open('合并637000000-637999999.html', encoding='gbk', errors='ignore') as f:
      file = f.read()

    # 使用正则表达式匹配相应的内容, 使用findall匹配，返回列表类型，但是属于字符数组
      file = re.findall(r'(.+?\"name\"\:\")(Ntropic Group|PET.+?RILLA|VisualCreatures|Gwen Ghelid|Alexander Hammer|Malloy Brothers|B Pictures|benz.+?ne|Alex Bartz|Mathieu Plainfoss.+?C|Park Pictures|Reset|Brad Rushing|Ways.+?Means|David Baum|LANE Archive|Christian Breslauer|Pulse Films|MINDED|Color Collective|Roman White|Trey Fanjoy|Johan Renck|Rock Paper Scissors|Nomad Editing Company Inc\.|The Den|Modern Post|Ramone Anderson|Johnny Richards|CheekyFilms|Lauri Laukkanen|IC|Supermega Films|Big Branch Productions|NoCap Shows|Psyop|Kenneth T Shimm|DeNovaMedia|Grayskull.tv|CA|FRIEND|Trim Editing|Ed Rutherford|Omer Ganai|TRAFIC|Gang Films|Jeremy Alter|Daniel Pearl.+?ASC|Airship|Soho House|Vicky Lawton|OPTIX|Agile Films|Max McGill|josh forbes|Evgeny Bystrov|Mason W.+?Dixon|CHEAT|Fancy Content|Sam Wrench|Tuff Contender|Larkin Seiple|Universal Music Publishing.+>?|THE YOUNG ASTRONAUTS|brooks|JOE SILL|Thomas Grove Carter|Remy Naidoo|iHeartRadio Events|TheFlyFamily|Beggars Group|Taylor Vandegrift|Raja Virdi|Jeremy Gosch|Neutra Production|Goldheart Post|Miles Trahan|Bruzier|Mutter .+?Productions GmbH|Bruno Ilogti|Rick Wilson|MM8|Davy Duhamel|Baris Aladag|Senior Post|WE WRK WKNDS|BEN GOODMAN|Ulrik Boel Bentzen|KIBORZ|Janssen Powers|Casey McPerry|Hellfire Creative|Hellfire Creative|Wild Stag Studio|Danila Volkov|Outside Lands Music Festival|Motion Eccentric.+?|TA Films|Kode Media|WJF|XIMedia|Mutt .+? Man|Sequitur Cinema|Doug Porter|Chris Westlund|Nick Pezzillo|Derek Hansen|Oren Soffer|Matt Schaff|Sam Care.+?Cinematographer|Amazon Music|Jacob Lees Johnson|Bryant Jansen|Dillon Schneider DP|BRADLEY .+?PABLO|The Quarry|dick clark productions|Ross Richardson|NYLA PROJECTS|HUNTER LYON|Patrick Lawler|WGTAM|Domino Recording Co|WE|BPI|Tim Nackashi|industry plant.+?|Jonny Tully|Eli Arenson|Austin City Limits|Sholight Live|Concord|Burning Reel|Baeblemusic|Johnny Marchetta|riffraff films|Antiest.+?ico|Thievery Studio|GLASSWORKS VFX|ALL OF IT NOW|JOHN TASHIRO|Jon Chema|Will Ngo|HAUS Pictures|DCP|LiveXLive|Urban Strom|Alex Bartz|Chris Davis|Warner Music.+?|Myriad Video|Symphonic Distribution|wash|Moon|Carlos Veron|L.+?Castle Studios|C3 Presents|Brooke James Productions|simian.+?la|ACNE|Epic Records|Forest of Black|Pinecone|Neema Sadeghi|La Blogotheque|Anthony Mark Saul|Joe Shahood|ATLANTIC VIDEO CONTENT|Sunset Edit|anonymous content|ed|Max Colt|OPERANDI MGMT|Cut.+?Run|Diane MartelThe Directors Bureau|Carbon|Mathematic Studio|Adam Zuckerman|Hound|MAAVVEN|reen Glow Films|Hans Carrillo|Jonas .+?kerlund Film|Sesler|Luti Media|Final Cut|Electric Theatre Collective|Moxie Pictures|Black Dog Films|Chris Roebuck|PAUL DUGDALE|Therapy Studios|RASCAL|Jason Zada|Greyson A.+?Welch|Supply.+?Demand|Scheme Engine|Company 3|James|Jamie Yuan|Dempsey Productions|Alex Chaloff|Ben Backhaus|BEMO|Lord Danger|Georgie Edelstein|Emma Rose Mead|Charlotte Russe Films|Cinema Giants Inc Film\/TV|Eric Bader|iHeartMedia|Riveting Entertainment|The Saline Project|TRASH FACTORY|Electric Light Studios|Cal Laird|HPLA|Biscuit Filmworks|Forever|david m\. helman|Loma Vista|FILM TANK|Cabin Editing Company|Magic Seed|Noah Clark \- Station 22|FAMILIA|Object .+?Animal|Gevorg Gev Juguryan|andresdp|VH POST|Exile Edit|BW|Fela|We Make Them Wonder|CanadaPost|Directors.+?DoPs|Gilbert Soliz|tempomedia|Swords .+?Eagles|Lacey Duke|A\-Frame Agency|argentinacine.+?referencias|Dan Kennedy|Matt Eastwood|Ammolite Inc|Tobias Rupp|The Funnel Creative|PAUL DUGDALE|JAX HARNEY|Trevor Wineman|Adam Zuckerman|Gil Green|CY|Untold Studios|Work Editorial|Justin Clough|Diane Martel|SONY MUSIC UK|London Alley|Colin Tilley|Metropolitana|Time Based Arts|Stereohorse|Happy Street|Warner Music|Electric Light Studios|BendEditor|Andrew Sandler|Darren Miller|Isaac Bauman|Coffee .+?TV|Luti Media|Edit Egg|adria petty|Rogue Films|Phillip Lopez|Grant Singer|Skulley Effects|Tomorrow|Jason McCormick|Jeremy Cross|Son.+?Heir|Greatcoat Films|Santiago Gonzalez|Supermega Films|Aya Tanimura|Tacklebox Upload|NtropicStudios|joel kefali|Bill Pollock|Sebastian Zotoff|Jack Begert|Malia James|2 Wolves Films|hangman|Tom Banks|Loren White|Paul B|The Rella Group|Brielle Hubert|Benjamin Kitchens|Michael Belcher|arnau valls colomer|Black Label Content|Arrad|Ben Carey|David Foulkes|AVIDDIVA|chriscottamfilms|Warner Records|Allie Avital|ARTJAIL|HELO|isaacrentz|Max Goldman|malik sayeed|Schafler Artists|Justin Hamilton|Huffman Creative|Riveting Entertainment|Happy Place|MAMAG STUDIOS|Blindeye Films|Color by Gloss|JONATHAN LAGACHE|Betterdays|Syndicate Entertainment|Marz Miller|Forager|Erik Sohlström|Max Vitali|Rock Paper Scissors|Pieter Mattheus Snyman III|sophie muller|Flaura Atkinson|Cut.+?Run|EAGER!|Lacey Duke|Drive Studios|Dennis Leupold|Carlos Lopez Estrada|XO MGMT|Mike Ho|Lux Artists|Constellation Jones|Dave Meyers|Rich Lee|PRETTYBIRD|Mute|RankinFilm|No.8|Bonch|XL RECORDINGS|P.R. Brown|DIVISION|My Accomplice|LAMAR BROTHERS|Tomás Whitmore|Benoit Soler|RSA Films|Outsider|Nate Gross|Farah X|declan whitebloom|Emilie Aubry|Les Umberger|MLM POST|ATLANTIC RECORDS VIDEO|Chris Dooley|Mathematic Studio|Merman|Octopus Inc|OBB Pictures|Velem|TK McKamy|Swords .+?Eagles|Jonathan Chou|PHILIPPA PRICE|ANTON TAMMI|Pine|Simon Hilton|BUF|Iconic Talent Agency|Xiaolong Liu|Memory Man|Obsidian|Flawless Post|Diktator|Lalim Edit|Incolor Inc\.|BWGTBLD|Lisa Ryan Smith|nabil elderkin|Andrew Stroud|Molly Manning Walker|Dan Lightening|MP Clubhouse|RadicalMedia|Marcus Domleo|MAAVVEN|Hound|Loom|Mike Reyes|Bucket Pictures|Contrast Films|SMUGGLER|Benoit Delhomme|Malloy Brothers|Max Colt|Christopher Ripley|Roisín Audrey Moloney|Caviar|BRTHR|Serial Pictures|Kaname Onoyama|Jonathan Walton|Lockt Editorial|Kai Saul|Vision Film Co|Believe Media.+?\.|Scheme Engine)(\".*)', file)

for item in file:
    print(item)
    
path1 = "合并644000000-644999999"
for filename in glob.glob(path):
    with open(filename, encoding='gbk', errors='ignore') as f:

# 读入文件
#with open('合并637000000-637999999.html', encoding='gbk', errors='ignore') as f:
      file1 = f.read()

    # 使用正则表达式匹配相应的内容, 使用findall匹配，返回列表类型，但是属于字符数组
      file1 = re.findall(r'(title.+?[^a-zA-Z])(prores|vfx|The *Streets|Kasabian|Katie* Melua|Katy *B|Kate *Nash|Kate *Bush|Pj *Harvey|Foals|Royal *Blood|Mcfly|Mcbusted|Busted|Imogen *Heap|Ellis\-Bextor|Stereophonics|Sugababes|Girls *Aloud|Atomic *Kitten|Olly *Murs)([^a-z].+?from )(.+?<\/title>.+?)(\"duration\"\:[0-9]{3,}\,)(.+?account\_type\"\:\")(未知|business|pro|plus|premium|enterprise|live\_premium)(\".*)', file1,re.I)
print("<br><br><br><h1>艺人</h1><br>")
for item1 in file1:
    print(item1)





path2 = "合并644000000-644999999"
for filename in glob.glob(path):
    with open(filename, encoding='gbk', errors='ignore') as f:

# 读入文件
#with open('合并637000000-637999999.html', encoding='gbk', errors='ignore') as f:
      file2 = f.read()

    # 使用正则表达式匹配相应的内容, 使用findall匹配，返回列表类型，但是属于字符数组
      file2 = re.findall(r'(title>.+?)(3200x1800|4444 |pr422|422hq|bitmax|gbuv|usuv|usum|uswv|usrv|ussm|usatv)(.+? from .+?<\/title>.+?)(\"duration\"\:[0-9]{3,}\,).+?account\_type\"\:\"(未知|business|pro|plus|premium|enterprise|live\_premium)(\".*)', file2,re.I)

for item2 in file2:
    print(item2)



#111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
