# Language Processor API

Used to clean raw text (lemmatization, contractions, tokenization) and then summarize the text.
A Doc2Vec model is used to generate an embedding of the text. There can be mulitple language processor api cloud functions deployed 
each loading a different Doc2Vec model trained for a specific type of text ie: Health, Tech ...


## Endpoints

**Sample Request**
```json
{
    "text": "Donald Trump is speaking Mandarin.\n\nThis is happening in the city of Tianjin, about an hours drive south of Beijing, within a gleaming office building that belongs to iFlytek, one of Chinas [...] he says: Artificial intelligence is transforming the world."
}
```

**Sample Response**
```json
{
    "summary": "Donald Trump is speaking Mandarin. This is happening in the city of Tianjin, about an hours drive south of Beijing, within a gleaming office building that belongs to iFlytek, one of Chinas rapidly rising artificial-intelligence companies. A more advanced chip industry will help China realize its dream of becoming a true technology superpower. China wont be playing catch-up with these new chips, as it has done with more conventional chips for decades. Chinas chip ambitions have geopolitical implications, too. A successful chip industry would make China more economically competitive and independent. They will be the largest and most sophisticated chip factories ever built by a Chinese company. Chinas big economic rival, the US, accounts for about half of global sales and half of Chinas chip imports. Why does China still struggle to make advanced chips when it has become so good at so much else? In 2015, he says, he suggested that Baidu make a specialized AI chip. But Yu thinks these chips will be everywhere before long.",
    "embedding": [
        -0.964398980140686,
        -0.10468921065330505,
        0.32673707604408264,
        -0.17476022243499756,
        -0.24372659623622894,
        0.2653709352016449,
        -0.30546990036964417,
        -0.735837996006012,
        -0.4078308045864105,
        0.12073676288127899,
        0.4797339141368866,
        -0.3681146800518036,
        -0.15254539251327515,
        -0.15352441370487213,
        -0.4835189878940582,
        0.2509464919567108,
        0.1620272845029831,
        -0.063379667699337,
        -0.27952736616134644,
        0.3387085795402527,
        0.4816349744796753,
        0.39262789487838745,
        -0.05172761529684067,
        0.19196908175945282,
        -0.2264808714389801,
        -0.03499132767319679,
        -0.3071638345718384,
        0.3406519889831543,
        0.176544651389122,
        0.07095552980899811,
        0.24215734004974365,
        -0.04492326080799103,
        0.38004621863365173,
        -0.2013835906982422,
        0.15120966732501984,
        -0.1038454994559288,
        0.654754638671875,
        0.5779673457145691,
        -0.08663947135210037,
        0.3406130373477936,
        0.8508926033973694,
        0.35733601450920105,
        0.001642379560507834,
        -0.8894984126091003,
        -0.028225084766745567,
        0.026177814230322838,
        0.2365918904542923,
        -0.1091604083776474,
        0.06058339402079582,
        0.4513152241706848,
        -0.34827667474746704,
        0.004022406414151192,
        -0.32506299018859863,
        0.24683590233325958,
        -0.4819050133228302,
        0.1869194656610489,
        -0.06546969711780548,
        0.250237375497818,
        -0.2860965132713318,
        0.2635567784309387,
        -0.1321711391210556,
        -0.06303172558546066,
        0.002768752397969365,
        -0.6052999496459961,
        -0.24716906249523163,
        0.15391317009925842,
        0.17986389994621277,
        0.07397344708442688,
        -0.04776354879140854,
        -0.06625886261463165,
        -0.5025747418403625,
        0.37756213545799255,
        0.05930440127849579,
        -0.34772664308547974,
        -0.13885259628295898,
        -0.04431430995464325,
        0.15867741405963898,
        -0.08187486231327057,
        -0.08209221065044403,
        0.007928071543574333,
        0.46236658096313477,
        -0.3254617154598236,
        -0.04181351512670517,
        -0.02396230399608612,
        0.43454253673553467,
        -0.6971055269241333,
        0.19688092172145844,
        0.042505860328674316,
        0.5317695736885071,
        -0.6581388115882874,
        0.3962506353855133,
        0.18932709097862244,
        -0.3222704529762268,
        -0.24127545952796936,
        0.0150535237044096,
        0.23415321111679077,
        -0.342570424079895,
        -0.25648269057273865,
        0.04573375731706619,
        -0.25065550208091736,
        0.2860799729824066,
        -0.29269224405288696,
        0.4258614778518677,
        -0.8959380388259888,
        -0.17054523527622223,
        0.20280194282531738,
        0.14671456813812256,
        -0.20818796753883362,
        0.37287554144859314,
        -0.13297395408153534,
        -0.2374359369277954,
        -0.14997905492782593,
        -0.18884988129138947,
        0.09095694869756699,
        -0.480939656496048,
        0.3275657892227173,
        -0.14831486344337463,
        0.3995925486087799,
        0.0803816094994545,
        0.21486303210258484,
        0.48553666472435,
        -0.30302852392196655,
        0.4671565890312195,
        -0.3667093515396118,
        0.10059643536806107,
        0.7777633666992188,
        -0.20207175612449646,
        -0.0344112403690815,
        -0.8191185593605042,
        -0.2781130075454712,
        -0.05608496814966202,
        -0.28242334723472595,
        0.22890430688858032,
        0.1969071626663208,
        0.00644039548933506,
        -0.1357646882534027,
        0.10995372384786606,
        -0.3415144979953766,
        -0.035953596234321594,
        0.007296730298548937,
        -0.3639412522315979,
        0.5749172568321228,
        0.035705696791410446,
        0.14991395175457,
        -0.44529959559440613,
        -0.35592353343963623,
        -0.10237491875886917,
        0.10900098830461502,
        -0.27863016724586487,
        0.4063105285167694,
        0.11204087734222412,
        0.4833582639694214,
        -0.17863963544368744,
        0.20052100718021393,
        0.3431317210197449,
        -0.14049310982227325,
        -0.10015656799077988,
        0.45782098174095154,
        -0.024672865867614746,
        -0.04885038733482361,
        0.0020486973226070404,
        -0.14926674962043762,
        -0.2719012200832367,
        -0.1525988131761551,
        0.5246030688285828,
        0.018741043284535408,
        0.13139696419239044,
        0.11290828883647919,
        -0.11654185503721237,
        0.48333820700645447,
        -0.2749207019805908,
        0.20549428462982178,
        -0.00435853935778141,
        0.1639045923948288,
        -0.18658173084259033,
        -0.1997414529323578,
        -0.24151557683944702,
        -0.024599995464086533,
        0.3874393403530121,
        -0.07268315553665161,
        -0.35301828384399414,
        -0.3928872346878052,
        -0.3789616525173187,
        -0.28650233149528503,
        -0.26439496874809265,
        0.31643494963645935,
        0.4845896363258362,
        0.14381380379199982,
        0.16618116199970245,
        -0.27854642271995544,
        0.42116525769233704,
        -0.0520436130464077,
        0.0718383863568306,
        0.026832636445760727,
        -0.23280222713947296,
        -0.2713139057159424,
        0.17597021162509918,
        -0.344795286655426,
        0.1747315675020218,
        -0.5175426006317139,
        0.09150086343288422,
        -0.1662183552980423,
        -0.7032978534698486,
        -0.27571672201156616,
        0.19785630702972412,
        0.40398651361465454,
        0.6307662725448608,
        -0.03704988211393356,
        0.02889689803123474,
        -0.18508942425251007,
        -0.4984131157398224,
        -0.5342563986778259,
        0.24681374430656433,
        -0.10685133934020996,
        0.7579016089439392,
        0.11487288028001785,
        -0.37781912088394165,
        -0.1850719004869461,
        -0.4586138129234314,
        0.011773205362260342,
        -0.44509363174438477,
        0.29425716400146484,
        0.14895641803741455,
        0.22314150631427765,
        0.32061970233917236,
        0.26042258739471436,
        -0.0035211595240980387,
        0.3346478044986725,
        0.05575639382004738,
        0.6753683686256409,
        0.2540196180343628,
        -0.1075008437037468,
        -0.15580129623413086,
        -0.2225109040737152,
        0.17859919369220734,
        -0.00892441812902689,
        -0.22934246063232422,
        0.194252148270607,
        0.46732842922210693,
        -0.12376688420772552,
        0.026105986908078194,
        -0.1094796285033226,
        0.1548091471195221,
        0.09361577033996582,
        -0.24918422102928162,
        0.81936115026474,
        0.4211854636669159,
        0.005887675564736128,
        -0.3354305922985077,
        -0.2203943133354187
    ]
}
```



## Deployment
Create a zip of all the files in language_processor_api. Upload this zip file to Google Cloud Functions. Make sure to specify 2GB
memory when deploying the cloud function to provide enough memory for the Doc2Vec model.