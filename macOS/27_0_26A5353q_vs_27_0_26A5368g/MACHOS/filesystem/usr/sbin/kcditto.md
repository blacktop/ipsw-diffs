## kcditto

> `/usr/sbin/kcditto`

```diff

 783.0.0.0.0
-  __TEXT.__text: 0xfdfc sha256:a1dc110e58ec7e601864d4459e450d0b8724a2ae91f364f7b04ad529a946ce2c
-  __TEXT.__auth_stubs: 0xf10 sha256:d1a28ce1a1e19aee6701419da1b3ac8d6c6b4131bf3c8c24ff9cd06b1d28627a
+  __TEXT.__text: 0xfe1c sha256:c00f1b3e014dd5419c8461d93d0967147b2d59e0ef4851625f0e7781788d27ba
+  __TEXT.__auth_stubs: 0xf10 sha256:bfef5fdc87a280018a8745c4da76dbc1ff1866ed4242905bed2e2b2f250d2bd1
   __TEXT.__objc_stubs: 0x200 sha256:43a24875e9471e1fe993de677e602dcf9b3bfabe6a167e45c3f1c677200a3291
-  __TEXT.__cstring: 0x4bdb sha256:5a630003fe84dce15259062732693d069b42d02f19b886941912b870716156ca
+  __TEXT.__cstring: 0x4bdb sha256:d1685ddca11520e0893039943982a28c66312a07009eda3a883fcf0856491e19
   __TEXT.__const: 0x848 sha256:e3b5125d8e6e9fad043bf7354ca78a08256d24c8a27e405ffa9558d835ca51da
   __TEXT.__oslogstring: 0x14e sha256:9aa18b469705f1217c5be699cf1a5ae89e33a34570562c443136f43fbdbea73e
   __TEXT.__objc_methname: 0x178 sha256:3aedf5283990e5b0b12cbdf7a15d2bc98aaf0c1710166bb98e406e4a13c09c04
-  __TEXT.__unwind_info: 0x258 sha256:fc133e3bec621a6b5ca41904eaaf582106a94dc74ba94e3a4e82d83a9cdb0c54
-  __DATA_CONST.__const: 0x50 sha256:f862e6cd67bc5c3a635f6d0a986ea3da22c8e859d046615da703e2579214bf08
-  __DATA_CONST.__cfstring: 0x1140 sha256:8cc52e763d1f7b1180c231e213c6844dfaf501020e35356728aa5b5a1e800c20
+  __TEXT.__unwind_info: 0x258 sha256:43f65f7ab8a3c83a9ba7e299bf88a1a87af13811a1da03754902238769a06ea7
+  __DATA_CONST.__const: 0x50 sha256:3e12f3c38fc44698186cc75330728f503655f0a50f8f0892ba4f158980e5fad5
+  __DATA_CONST.__cfstring: 0x1140 sha256:fd7fd3eced3454bebfda12f16e917a1f8650f0e5468cf5e215498465572dd51e
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
   __DATA_CONST.__auth_got: 0x790 sha256:14bae9e0b9178264e485a2e21411702ac0c7c67b96450c731b0636eaa8059d6d
   __DATA_CONST.__got: 0xb8 sha256:189833d840864d883caa9f249a2ce37b71c54b3dc86dffb5be8ca3e015414541
   __DATA_CONST.__auth_ptr: 0x48 sha256:d85b3c651f5df45329ef513d6af99422146400e31bcddeeae998d809cfb2d445
-  __DATA.__objc_selrefs: 0x80 sha256:a17caddf19670743e6dfbd1765bec75c0079664ce1a092d24f19fb001589146d
+  __DATA.__objc_selrefs: 0x80 sha256:4f3473b04267719f89ef51351371d865f253312c47f89ee0b3260cc01462b3b2
   __DATA.__objc_classrefs: 0x28 sha256:5bb11f80a5125589ac0fb586863c6aa668d888350983ccf84932e67898752f4b
   __DATA.__data: 0x40 sha256:f8629bb2b4ad3333fb6c51ddb8be00f079a8610af763b203c867d375c69273ab
   __DATA.__bss: 0x428 sha256:3b449f81c553e3972dd31acc7df0ccfa308b1a290a103632c751828372f7ba3e

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A0215F62-14F2-30C9-A74E-A8666A7EB7D7
+  UUID: 295DF8C0-82BE-311A-ADDF-712A82CFBFCC
   Functions: 145
   Symbols:   274
   CStrings:  648
Functions:
~ sub_100000ca8 : sha256 59debfbcbf95584f861578c669ba1b8ab8a8cdedbbe4b2fbacfaa8cb5c7f6911 -> 731a57cc287f3656f5214283a4d7a3dab4b018704adb11a31ce50c26e5096756
~ sub_100000e3c : sha256 091b377d43ff111acd2a320edeed43cc49867728e7b3e628ba0c45246a8697a1 -> 6bde712283b892ce7fb119e57dc0a36255e2f3d4c1cdc012c0ef4252fa742b9e
~ sub_100001110 : sha256 6c783b94ed6acafae3cdd2c3a746814f86fedb1f2de0443ab3b1d4b584d988d1 -> e9f6079b3dfd71337f8f637be056c59e4d2fa4d96809c2cf1513657837ddba8f
~ sub_100001330 : sha256 7bde554a585b121db4cd4addbf45d7f7b6a985e07764859f3f5fe021dbaf1a77 -> d029d8e3a7227b57ab295217c5d9481e04f728de01ff706b1d563e5b4cee383d
~ sub_100001444 : sha256 4253d2789605fa02dd2e0b0a70daa197c14c0b52093537c00b433fc75290df26 -> 3c4a831c5ad09117c8382453a91d4a4a0cf1a4b7d15010d3a9f655ebd31be46c
~ sub_100001488 : sha256 27c7b8b673d18954d19ed99d17c0456c9ac6a6973a2480fdb923806848c356be -> 9468d2745c450c7ec0d832aa585beed5621b1ba6426b4f161c3ecf3d5561d543
~ sub_1000015c8 : sha256 d76c12cf7040589302a5bb7c3931c11793729a122ac95ffd421a870764dbd220 -> 333e0f1c220ff96369c2bc8d34e8d8f8cc3012171bbdd9eeae26f2ed5ea2f0e5
~ sub_100001684 : sha256 c8d8375aeeab8ca02e8cf471b8aeea74bc1c882cad0bf8276a5e5c09bb411453 -> 39994d8844bbf5f281be598e2c5704328477098b33d3447489373d1637034675
~ sub_100001730 : sha256 9764005759450e349c50477234dcbc563d8bf4710efab10f8cbcbf07bfd25872 -> 4d65a33b6c50723c480b9359af0419713f9739d896983f97912282be77889186
~ sub_1000017dc : sha256 d96125a629a1f25d923ef43e415b96ed79f903b3b3823413bff7a70bcf8b617b -> 985a9dc68b93f624cb238f43b770ce57533a0994ddf6aaabbb00684fe7d150a6
~ sub_100001960 : sha256 a1843446479a70e7ed70996ccbd2ffc827ec530c8f2fe96a400a3173973cc764 -> c9bea10b97f25a7e695828d8d02782895a04482d526731cf3c8d9c1c6debf25b
~ sub_100001a84 : sha256 ae9a853212074086f78504161ad9f56451610e68da28f04189a7fd4cd0dcffbf -> e8dbf806ecdedb1a50e2557f4ee49f6e2883a7eb619e0c3e763b44b803231de6
~ sub_100001c0c : sha256 fe484ee829d32e96ef5f2933976de94a2f899ba43a221974783966a01a17ac35 -> e601d3c8340c3c36c73242a5c466f0d0570a86f5bda94f6b2a9d96f7d6735844
~ sub_100001dac : sha256 5f365893531e8989de33ef59d8264a042bb407d04427d9d5eb64e413b6aeaa7c -> ee8d9afcb4354cf8ef0286685ea981c0f37e98d5e3571dafcab6f8c46fe1d3c3
~ sub_100001fc4 : sha256 e607f1fd0ac593d73d74336abbe13decb0fb8f345560297a1c94be10962283fd -> 6e862d23238f3f1b4069341969620c7f1f6c02bc7f2f6b8dcdb16520bc73e863
~ sub_1000020e0 : sha256 8cc6b2d04a79b923555d74782beb3da797e86c9bd5dae3570a72c78edeebc5c2 -> d36fda841f61868d3b445caeed5585102257ad565f112a6180c96b1e6c1b0598
~ sub_100002498 : sha256 e815ff8c4dac4afc3e7c1455cc0205bdb83a43635c20f4165e581758cf42633a -> c5b8a787da639d107321e876aeb04b605a8d982f7d22a1cfc8b7e6c297604857
~ sub_100002514 : sha256 7ff6c4f167c003312a4d320ebde1cc56ee881430eedda7ed40335335733cac35 -> b7a60c7f597bef72020a3bbf62fa0ef134405d553b23ce8ef69b87dcd5aa3fa1
~ sub_10000255c : sha256 c78d4b3ae3866700886a6b089a7d7f2bbfdb0935ab6f579ed90c11db632430ff -> b178756607f2f7ee0a66afe66158c96700f998a38530db477e373def1d87c701
~ sub_1000025b0 : sha256 1e1572ff019a5c6d11ac4bad5de75c4f5b78059287bf1640d63fca4b04baf93a -> 0914cf13057caf3e7998ff27e8941e258cb1f2f579912e4e69a463e0662cc90c
~ sub_1000025f8 : sha256 0ead36f983435b2a4c2c78b8d2f9cbf44a2fdb81ae68abc5b486a9789c2a36e2 -> 5acdf4fad884e04cf23331419ed03db125031ae2b4a6d93ba1f4612247714aea
~ sub_100002648 : sha256 1ea98148bae3e9d952c570e8f7af5d0c4c0c45f608c3e4ef533f0593daac1e79 -> 11e92265bfefc2065cd957aba3b00bf76fd3ead52d44c6820150b79aeb577a0b
~ sub_1000026b0 : sha256 56761531afebac6782a4043d5ec4ff764997352825344224ca5c3cbd1c50e26b -> ae932806fffb8bd4599f7626ded21c98c538f8dc0116694a3387867f36a5a179
~ sub_100002724 : sha256 09b0e2ca9e5bac997d09b0da2497e1485416d800807528a10a88b879986a4b9e -> 066ed0edd530e12e4cf203330bde872bebff3ec5f18a36b22b2a31f7a92a6c6a
~ sub_100002890 : sha256 f72b6f518290458fecc8ab3b3925389ae54f67b6aa49a171fb76c6b80a5964d1 -> 55a5895f1025577142403d72d7dd8a8189a2f009e6a0cc3f7cc1f67d6ab66fb3
~ sub_10000293c : sha256 bfd7f4efa8d029086133337b364c9b328eb9d8eb9199fd213fdcb1a1fbfc5fc7 -> 7eae71ad3409326030d4ba63459f20ed059c525767f35602f6a6b632865d8f9e
~ sub_1000029bc : sha256 a9c7b7fc4b6001386882821c4c8ea9111e3e12b4f02d51fcf98f9f4fd9c854cb -> 9234b7b1b5617229eafbdbe004484e7758768c53a2ca5539a533365ef36eab9d
~ sub_100002a80 : sha256 31137a46895fc78ddc1696f3ec1ecf7d5c4874ae43cd1eecf84b7be2b42717f0 -> 2ed8bcb2b1773da4e38e1d4e21171b8e2c692cdc8cbbe5280613f17507585e6c
~ sub_100002cd4 : sha256 dc18066fc40dbf1ecbc51d3c40d3151e19ffab8e66c10b79e978b6b166dd12ce -> 831abb8067cb4a4790c5a8aa04db4ca1407c915f107c789f63fe4e31a2e43e4f
~ sub_100002d44 : 260 -> 264
~ sub_100002e48 -> sub_100002e4c : 212 -> 208
~ sub_100002f1c : 96 -> 108
~ sub_100002f7c -> sub_100002f88 : sha256 fa9fadf38ec0b0d71d7101338969dbf2ff39ef7b1adff04a9cb70a5acb666b41 -> 7a9a3cdd74235f044663e9b977426b981778e9586d2f33410c3671cd5c79f6da
~ sub_100003544 -> sub_100003550 : 796 -> 800
~ sub_100003860 -> sub_100003870 : sha256 eca59883ef879c74442854b5af0fe7041ffe2a25210ba2dde53b4787c59f9863 -> e06d8e703e69d05290a6d74885e155e1c9b0cc8f8b1d33941248460ac3ce36e4
~ sub_100003940 -> sub_100003950 : sha256 6f34bc7ff806663db39b5226b95c6c8a2dc78e75f634266b99bce71a48912dce -> 0492a152e0806856865e8c8951109a638135363d5399463be1f82d3e3fad7f85
~ sub_100003e70 -> sub_100003e80 : 492 -> 476
~ sub_10000405c : sha256 ca04f0a0c2a8ea1582bad73e8d0fe3a2719a4a5335131856ee9f81faf1eba381 -> 08c1bf268fe5d0c9009179ba7eff43f206840c15e2acbeec4cf0c7e1cc18fd98
~ sub_1000042b4 : sha256 bddbc22876f06decc6a394db132d76c91649674fa31294c9600be011424bcbc9 -> 76a688a00e89d38851aa4a6dedc253b28b3f1f05d49095cdbe1035aa79704d1e
~ sub_1000044d4 : sha256 9557efdd732b777fa4777a7dc4cff769c831d12056a1639c965cdb0c933b9d5a -> 60a6109c7f481b91488660f28e64bfb67d71ce9c4138427c0c5daddd9705b01f
~ sub_100004530 : sha256 8ad6946c25887d3918a2f976d84ec75d590eed8ee8bcea409d9dd898830a5392 -> 5b8fb64f3609a3adf08f3b7ebcd1819637512650f89f6157454af5403c54b79b
~ sub_100004690 : sha256 0c08750e09d1dc17ad5bf293585b166e4345c3d5b5e08660baf6116ec46741f5 -> 7b99a2369866c38d6862333135ee93280d11b02749c086f692084b4cef2c03b7
~ sub_100004724 : sha256 d6f4edc2ee7c4a84426a6c9f088a183749273165e2c44a26f9a48c4f7228dc6e -> 29422868728627cefc16f8913c6a18868cb1f0b77778286b7b18b5c893a2043d
~ sub_10000486c : sha256 e4f72729983ca173c498ec113624d3bb5c28aa4d8e23cd0c5ef9bb067dee591d -> 98d57e1efbcfd225b9b20255a46f3ae8f0dd9f3a9615221801d195f5d094946d
~ sub_1000048e4 : sha256 3f6df2d7b08ddba2659ba9194232a0025b8bbc2c09471f102df45a89d9d9d13f -> f51fbfb8278bc84ab18483b6e41bbc375c14d27174c34908da921f399bad162e
~ sub_100004a24 : sha256 e70f34213fef84e0c8abce3f2e542f9d8c18f627277fe8832215df9ce4c2b62d -> 4af995daefa5cef06863c1e9a7c737c4f163fc7c802fbd19c2d32e223e63f515
~ sub_100004ab8 : sha256 e5760598bdd56f834164e63d4f2fe182122322e93f89b6f6fd1d42f880634209 -> a84a154de62f0f90eb279cf2b6c7b7f1c1d724ab2234f383192bb1c8590fc3f4
~ sub_100004b10 : sha256 b2e0da6cd3e746d9b7fba6ab80812dc684c88e7bf6894161856dac87b8b16262 -> 039cf0beac423cf52308f595df9d4f898a28c29a9b2b58263065be3a4793b783
~ sub_100004bbc : sha256 549af09cf2d2e75cd781bcaf54b82c382d46a3a3084a381d70fd381eaeae3315 -> 7e692258df5056fe9dc1b56f0964a5e558df1a0b98778999852f5ab3daf6dd0b
~ sub_100004c44 : sha256 3a6b7b19e087544ba17857137bc7de68ccd0ff1f17e1f24e03ba5f83dde7815a -> 367861f22dbea3ef32cefe082008e91393edcdd9cd0cba14ab1b825fbf9ac79c
~ sub_100004cdc : sha256 61708f5c8c91ef29c3a9d2662dda3f1e125c47b51a096bcf5b36bb764ff47173 -> e62c70afbb1904e82a58a78506686369041b396c412601c0634b137d73a57b42
~ sub_100004d54 : sha256 af425c9ac84ccf2712bded926a94a537e350fbcf4123136aad296aa493099fc4 -> 486f4181c702b05041e064ba379d44d9f9d568cd8cd456ab383e0142bdd6e4df
~ sub_100004e0c : sha256 b7a321045a75241e547ffefe02bb224633b6c7f619a68d2bd699ac8043dce1c6 -> 0d6c8f1caaf60d7cef624f60e3ebe63ea69141cb713d21e64106b2367d6a4893
~ sub_100004e70 : sha256 69da956ebcf16b25415aa24af77a669f398586f88205b25698b714116efcb4ce -> 2f65443ff0420b7328ed5f59233cfc94b1c4fd7ded3e6ae76d059ba50eda2cc7
~ sub_10000500c : sha256 a23250d4af982714f75e245f0faac17b88901829d843468288f99487b23266a5 -> 753786518683ffe8ce2dc1cab7e1c57d3941483c9802ed0ae2cc11cb4c0b99fa
~ sub_100005074 : sha256 afd059355c560bc6f79a4774c18aa83a3e0d710e8abdcd77818cacc59be4315a -> fb729098a884d8df3d471904035b6c812f01251f8ce098c52121507a190069a2
~ sub_1000050fc : sha256 90fc8459e6c8d67fdfc115e63773c0af8401c0d949b8d80821d5c76991a3eb39 -> f7be6281ce74231f55e7157d97d97354e07910ab30832b32ac92f5b309ed375d
~ sub_1000051f0 : sha256 64ba05603aa565f31e7138128179f97cfe70fa9efd32011e607277c980cc4fdc -> 9af572a54221ae61bab4f3cec8ea33291fa076ecb77eb309ef5723c245713d5b
~ sub_1000052bc : sha256 d35bab417f1088123de6aa3c080e03c2c89130951d3d8291ba1516afbc8072f0 -> 94765b63bd539583e28092de90cf6c9e571c92511b7980447155fa7c355a3acd
~ sub_100005370 : sha256 d3cae91d62677a5e4ef4fbe250ef4dca0bd9a8acdd6c1e4a5e4107a217475f46 -> 94ed0d61bd8fc31ff076ff57a8f1faab46771fbb824d6fa2aa4d6a2395b3a8d5
~ sub_100005450 : sha256 f849986bfbba0fedf002dce1953198c7b585f35d05abf2498382b3c3efdcf56f -> ab50ffef39c1b256b1234d3e9aa5cef2d29cb3d0c37bbe4e6651b37f4ce0db39
~ sub_10000549c : sha256 ed4246f8589513a0071d732a6495ac6cc443fbbc170ae88d92347ba021045b70 -> 7f07e26daf634bf037e26358f1c5583e113e1b595b5535496e8a8a4f273e5ad2
~ sub_100005604 : sha256 ec4d9e7f694c68c6402054d3d38a91e176482e6c3a6be542a77d1ef4820ae05c -> ce301a98227ac56d7bb15bfa1c0888f0075bebb6237416d5be7c0bb336b5b326
~ sub_1000057f4 : sha256 8931e75ff14e2e15bba7c4758608ab45a0efabd558cd7074dd8eac0ad831b380 -> 80dd8a5b24a1127e23f50692df74a34d6b9f79b37105d52f3d5d09161146d5b0
~ sub_100005978 : sha256 fb4c9b847f126c0346472423d9754be3eba87485c871f494d47da5405ce6476d -> 53087d1c2f962fcbfa5ea90d7cb34929209c4e6baff54eb8021ee8932e949ecf
~ sub_1000059a0 : 348 -> 352
~ sub_100005afc -> sub_100005b00 : sha256 0927d81e7ed6e2dc75fb49e67bcd5d2eb219614c646f1316e05206fe42ad17af -> 1a0a2b3efbb2e8006b030c1dc97082d90d8ffc92d92de789fb35c9a0447725e0
~ sub_100005e30 -> sub_100005e34 : sha256 0a33893ba0146ceae7368876ae2b52b402047a7fecdd6926fe68709a5748ddc7 -> 4714fd6bea100a2c0a3963c14a4c07fab53a226dd14a81c6de531b9c82fc2614
~ sub_100005f2c -> sub_100005f30 : 224 -> 236
~ sub_10000600c -> sub_10000601c : sha256 d28613fe47da7e36163dc611fc6d84e6157c05be3db930ecc8a2f2131ae27679 -> d2a029375008e30b8c1509479da1d8744f784d0e827b391a5658dfd041b19163
~ sub_1000060c4 -> sub_1000060d4 : sha256 492457ce6d5e3c534e8421877848c545a2dc47bc9bf6b957d5714ddc0ba41cca -> 527b540ee680dce34a951c764c8dc2420799f277ca0eb54229864491cf7db407
~ sub_10000617c -> sub_10000618c : sha256 613077d741c25796cfbea61a9b7abd8d6633e85a5e21bc9935457bb697de96fd -> 7d74fa9ff1e5ef87e2fe9051f2f0f1984389cd02b95826ca18a6a57b3d8de6f3
~ sub_100006238 -> sub_100006248 : sha256 d586e19f173269e30fc48dc6e21cb47f4a989fdece77c106106abeea4aefb4ee -> aa64da323b11d0cd377867a56ca97f5b3f2ffac6ec567f691eee439db4326162
~ sub_1000063cc -> sub_1000063dc : sha256 e451e154c4820027e67b1135866b1ce31f814dee259baa0fb63ac8f2304627f7 -> 46bef3b87a8f1d8d89d2c5277fada8ef66630f733b203f984f9f5c09e8e62e1f
~ sub_1000066e8 -> sub_1000066f8 : sha256 8e7776982b04140372414c676f4cd3c3c9b9caed95e48d627e3ff97a02ef57c0 -> 376b5967bcf1bd580ea24dd04a691f8c2dc272175fa6a3e312a477c32aee5a40
~ sub_100006a4c -> sub_100006a5c : sha256 732c1ab76a18ab8cfecae36c86ca20b73fb75e00da0398e0e7a023d8142112a3 -> 1f1c85de931ab0bc639827b3a785ace55ab36100482254c7b1026e122f8cf935
~ sub_100006b48 -> sub_100006b58 : sha256 548e6a0e9d274cb25d57a418fab26623d4534a80a85719e727fc379ff2631d5a -> e2e19b622ada11cea54855a9a4a439dc4c2ac2e0b14104678954bb024e9688fd
~ sub_1000076d0 -> sub_1000076e0 : sha256 1aaca54dfcc6e1c05ad4e999b0fac32417ca38091796eb302befc4b0953bb8ac -> 70a76126032e70d6f5e55bb8738420f6eb65368495d23917dfc883c33111d288
~ sub_100007820 -> sub_100007830 : sha256 1f97f38c7dc55d1be5d7a13a91d737fe255f4076e59927e132b7edacd2770c1a -> e60c73c9fed5f124db26c32802c3cf5eab6f7cfc60828f0128696e983c3aeb45
~ sub_100007a74 -> sub_100007a84 : sha256 063c50ee6f6c0c1cd7403e73c819f4fb04aaef8bec8f225e26987a8a9b3c8f5f -> c77900d50a17892b3a26877d582b93190eaa8e10553a48fa52823f039d785967
~ sub_100007b34 -> sub_100007b44 : sha256 26c4c083ec7d8ab20764aaeafd0419eccc409d6fd20f8a29270d0d5bd44490cd -> 87ee2ceb4c1da221beaa7e9441ce46a941252511e1826d11b761c54d786eb0aa
~ sub_100007d2c -> sub_100007d3c : sha256 15220ed789d56d2ddcf5b796b73aa8d4644f8772b3840119fd5f3aca5316c9b5 -> 687ee403d14a640b9e0ed0cfdb8573a2bf059998ac7454edf583c8b15c46177d
~ sub_100007f68 -> sub_100007f78 : sha256 81d7f73dd7a97b2b4ed0405708507dd24cc7a91bff353bcb3c9124ff3c10cbf5 -> 3c0ba6040cfe2a33e02906c20dad9c014433be206da0f5e41842642a90140942
~ sub_100008380 -> sub_100008390 : sha256 44b794a9f58971abd792b4eaee5d717e2dae4c3cca6418e61e89fa806f2eaa00 -> c8cb658df06bc06cad92704b4e2659db5d7abb437d28b959c2bf267bd37bd448
~ sub_100008464 -> sub_100008474 : sha256 574cc0d09a9be4ad823c64f1db6295bd0e2aea6b61d85f194d874345a7f2e5fa -> 802257546900459d65fb9544bce6718ea2784d9c7b752921280b21717978b3ec
~ sub_100008580 -> sub_100008590 : sha256 36f730828003882dd424a1e300e4a11c84ce9ef290c860071982792660fa8329 -> ec440603ca39dbba3014203e2f3baad20f4f0b914e214baf6bdc2ec049057136
~ sub_100008790 -> sub_1000087a0 : sha256 866c59336d3fee8bd8870a1d6a32af1fcf00e270305c232d786d51802705bcb1 -> da5945b37b2fd87795a10bdeb567d42f501ce026318f0d940079d03ee9475d7a
~ sub_1000088d4 -> sub_1000088e4 : 1888 -> 1884
~ sub_100009034 -> sub_100009040 : 76 -> 64
~ sub_100009080 : sha256 d962888325f7aafd3a7181d196c6d01df5993b10b3b6d8b50d147026566d151f -> 2bf12b7b1d139fb07d0997094f68a7c9572b28ec3a15a45d97cabf0ec78f9508
~ sub_100009254 : 1184 -> 1144
~ sub_1000096f4 -> sub_1000096cc : sha256 9660540f20778cfea6979fd271c5bc09157795858b3aa418a72ffc9bb0b08926 -> 0e1564d4141c5c3eadbe16dca088bd1040cd7e1ae75f5a77140d18791efa2631
~ sub_100009798 -> sub_100009770 : sha256 5dcdd1aa298393ff2439e24832c08ee47fb3cb9ded1614f3361b447e6e3519bb -> 509348f3fce4d03aedf9a90d8d66c2b09b1a2d5146d02c074ea418b2d432e2b3
~ sub_1000098f4 -> sub_1000098cc : sha256 fe6cee53334dc25368310bcf207ad25ad5fd5900511fb11e4cf4a12ae0d11005 -> 0f2d02a406c6b1a983cd337cb91041e039e10162dfb9a0a50a981abbb7ad35a1
~ sub_100009b48 -> sub_100009b20 : sha256 1829d80de3eaa6ee8645c0d9a684934c3a126bc07c8cdb0740392c9e9257c48b -> 51e48b20ce1c85ba5b85f971e4bfd7f6fdfff3b9148d83980c70677c1fdeb00e
~ sub_10000a09c -> sub_10000a074 : sha256 3d2e01eb1e14f61103a7a79c7690b6e955b1ad523eaa8c851cd32390e4ae5fa3 -> c6585e2fa6907858773ec5d46fde70a5e98c341df3665126245b18392e87cc05
~ sub_10000a4e4 -> sub_10000a4bc : sha256 1b472ec489da47430adddb00f9738f6878bf70b6345258f547ef75ec4ad3392e -> 0eca6385a024d39dbbf01211283045371c8142cffcb9514b11d8da4e7c158b4f
~ sub_10000a5a0 -> sub_10000a578 : sha256 86093d8385159800b32b0cf12eb8da17ab6720f849463632915146af8371a753 -> fd26b72c0f4ebb09bc0d2c16168b23e9c63ba48df024eec837724a7d5ed3b644
~ sub_10000a700 -> sub_10000a6d8 : sha256 1e18962faa2112ba03ee75100ca1547ca901c7f452a94b0c78b3c0c9f13b5a02 -> 461cd869ea66cd778cf605527e462f42c775966e9bd12671f6c2b27fe7d1a6c8
~ sub_10000a948 -> sub_10000a920 : sha256 bafcbbff5df545aac903028ca491f6e5e7a16b57b2a615201ddfa4d753ed5d0d -> 0c515b02a36bc5cd65dfef0e485d062ddc52e2f4ef3a0e057e90a2c5e1ee79e4
~ sub_10000aad0 -> sub_10000aaa8 : sha256 f2060270f82b78601eb2539baab766b009173387fa153ef34a75fac411f6a8af -> e2578acefb2e4c078fe0422666d5a022aff99bfbd61f4fe788fef7f553fb35e9
~ sub_10000af00 -> sub_10000aed8 : sha256 c69c99cb5a54bb1ce098db64b41d1c5fbc2570ba2b415a0c417500c4d6303148 -> ad3c60c006a678cfae8b868bf2f08bd9e27e37f9f34a69e6ae8cffa76d31838d
~ sub_10000b0a8 -> sub_10000b080 : sha256 47f1422c739ff7447ab500411cdbdba4a201536c0e3dba0dfc1c0af17055e918 -> c6f2813ec2bae06c5793c6529b5c99d8ad25e7737921186f8696261ddc8e9179
~ sub_10000b0f0 -> sub_10000b0c8 : sha256 0f11bd12111deebaba39edf553de9970aa3ffcfe2b9f15c204fc0b29de7b865b -> 96b857f7a80d8c20fd7a5e4762e7eba4ee22147b540f8c8c296ba22cb6b23f9a
~ sub_10000b35c -> sub_10000b334 : 308 -> 316
~ sub_10000b490 -> sub_10000b470 : sha256 4416f31fcfae057f649eab01e72b8b5e8f2975207ef9753fd675a8659d966269 -> ff5d681a6ee041a838a4e2d3d17f75365302cd78877bb84d1de2f1afede2366c
~ sub_10000b5a4 -> sub_10000b584 : sha256 6dcbb726b03de0b8ff62954139fe47732f756de4d94fe7d55aa54030107b912f -> 9f1623854efe54131dfe634295434ccb07d3bfd7a94533c7dd3653cae0c7cee8
~ sub_10000b768 -> sub_10000b748 : sha256 a0b5881c573bb40def6a2fe9a061a4d5a268171580564d8004ef1e73735fde68 -> 1f67fc47e3024e545e0d7c3a992f11b6049a0e4e8ff3d9ffc49ca861e72c7343
~ sub_10000b888 -> sub_10000b868 : sha256 880ae92fc905131e96d45c0f5bf13d2367d3e2c6f00207d0d1a1d49001af5a73 -> b158537afdc3bd0d3d529cff8d2baf7df896f9515e915755de2a761d10c83683
~ sub_10000b8c8 -> sub_10000b8a8 : sha256 fc4114b6c5f31339d7b9211ecf3682f1123f7731d5e5ec7d5657e6766eb0efb2 -> 1317d73dc7f2cd3bcabfdb0a941dfea9612c4312d284d2ab0ea236aa786e0659
~ sub_10000b900 -> sub_10000b8e0 : sha256 933e2cad3ad65d31393025d1168091f480ac98ce6ba7d1f5bc69153241494508 -> 1e8e4b54758c9390c0aa384da1272ea13828da65c03a363d54df3570c7f37f99
~ sub_10000b938 -> sub_10000b918 : sha256 0cdd0287d9971a79bdb9f169bf56fca83b96265d548eef501ac77a48808c9e9e -> 638534655f160140bde9e11f03dbe5ab25d2710f9b098dbefb6baa47484efa0b
~ sub_10000b974 -> sub_10000b954 : 3872 -> 3876
~ sub_10000c894 -> sub_10000c878 : 1396 -> 1392
~ sub_10000ce08 -> sub_10000cde8 : sha256 d16952fed45039b7c6514311dcb43b9db42d64e64182533ecf5e7625219af480 -> 1a776ba86daa35225b30b31608e1eb663bb65103143b435bec3d79d58b23fa26
~ sub_10000d174 -> sub_10000d154 : sha256 c0cc8f910519983ec7574c910127b75b33f7b1fa4db963f84b988543e4cde80a -> 67902ee175c26e64f525962ed7e12a09e27c94d64cdde3f54328e6f7ae96ca01
~ sub_10000d220 -> sub_10000d200 : sha256 ba1385a6fdbb9b2da22d43295c1155c05255a109b0de4ee3334fc7e4bad98ac4 -> 3e0a2bc4842445903ff9577edfa3da0bf0afa2dd83f67325513283ea8e2fd25f
~ sub_10000d2d4 -> sub_10000d2b4 : sha256 87d51a8e86b7b7dd90198dfeeb1c52155c24bf2dea3ff1fd653a75025042097e -> df76e05f4c441a20a77047b55e76861c80d0fdac64d4bdb2e1680b706519fbc0
~ sub_10000dc9c -> sub_10000dc7c : sha256 e91aa2dde6ec0f21500fad0c6c0b13ee38c989a4dd6c9c31a90bfb88ad7028a4 -> d4862a59d5bfbb6c8e48d42c409a50ad802bfb0acb9b95f52014b4a455896c69
~ sub_10000de60 -> sub_10000de40 : sha256 538a374d356403ebaaa4b841683138616aef7bed91072fead98fb13bec5d2cd1 -> b32fe51ed547c4df4f6e63092ba2ebfe2401091e71f4fdb46bb1d00ae5350ba6
~ sub_10000df54 -> sub_10000df34 : sha256 06fcd4217592f0bb0ee09e519ca367093cdd86ab6e3b7e149976944f26c29c4a -> 125563d76a1039d3444563606d20a35253339e0c17af58a311151811af81945c
~ sub_10000e72c -> sub_10000e70c : sha256 4988691a3dc6e3dffe573571a7e952b1b9acd7b421a7e678ab1205adb5ea7489 -> 63b623db4c5934a7cca99ffa3aeb3197395b7cbbc7ec5b4859eeb8ae5e67237a
~ sub_10000e79c -> sub_10000e77c : sha256 e823d1be2754766053d05026875d41c2ac1d5c6f86e4020e276f91936ad0ebbd -> 6fc61f228e06c1c173113566e36c65ebdd2f421b45aa35916917540f80a092a8
~ sub_10000e8e8 -> sub_10000e8c8 : sha256 6e7aad21b1d5841f68b0c1cffbd82e82c8687c2410785c32fa10a77bf1f7aa8c -> 50bfadfe4a92d408f6a850ab51c7dafe26c2c8820d9b70f3bec2a3a12954a717
~ sub_10000ea78 -> sub_10000ea58 : sha256 e0f2d53d57f6c3e2375736594c475d2f0f8eae4fbab1f368a21c44b2a1a41702 -> 56e14769dde481a61457c1d8bbb3c5eb06cfd222b75fb65ab5110df63e43070e
~ sub_10000eae0 -> sub_10000eac0 : sha256 26ba1e01004491fc6d097c6fb706a031988a76d58d1afec6efd3eb96efe4e431 -> 480ff1494be04a9c5be9e952752e38d0ed50a275aed0cabba349e68513756573
~ sub_10000eb1c -> sub_10000eafc : sha256 667b6ef8ba8e3dbcedce2583f674629968dd8e27ee229cfeacf21cae9ca3e2fc -> 5b9d2e143e22a3c61ad0118947a59be75b08271fcefd48a0b963146f0424ee7f
~ sub_10000eda4 -> sub_10000ed84 : sha256 0beae580904779ff47a84edbe866dfd7635c4e7d16ad287825e1bcb127cfd8bf -> 21c5c12e6cdf769f18d374b8f39bf8398da9c43e85e3f48a4878c481d22bc5ce
~ sub_10000f0f0 -> sub_10000f0d0 : sha256 34c8d1db86b93e6cc4f962a9a3a6ef0a481c523798d61b97a392e19b0a55c744 -> be9ca71d49342d2188b252f067df0c7ef23c19df3c5103505bf9bcc0a521ceb7
~ sub_10000f2e4 -> sub_10000f2c4 : sha256 f02cdf993d86b31d9541258f73a7ded05b1550ef0ff43120f0dcf565ade3a4cd -> 524d6a39622ca66b54252ab8d438bc8d078b84ab64e2c6ea89acdeeac73a8625
~ sub_10000f5f0 -> sub_10000f5d0 : 1484 -> 1516
~ sub_10000fbbc : sha256 4873e6fd4a7bd4ff42cb04c06d43e25cbb04721cedb8fc8c42d40fc47fcad387 -> 54fdb42a86c4a2d5d452dce30778937f6756b02464c0a0ff768fba64b765f7ed
~ sub_10000fdcc : sha256 eb74866565b1f683710f00e3883fb113c64a1b1b68ef01d8f5cc864e9d6134d9 -> 87b9ebd3d5634efcdaccfc6bfd8a497ff65ad8f37c0322a2d1f6b1fa17178036
~ sub_10000ff48 : sha256 79c649adc337d0dc7269d382f03c5663ed2ee5292d92477a88981336ae8fe384 -> ada43beb6e20e5ad09a56da49ce19344b1fa02fcac7104e451b1288ea7eec65a
~ sub_10001018c : sha256 c6e388831bdf9ef89cd2d1d6e0fc74f2ca11fb369e847618afcb0fb6d5dab189 -> 9d19218d5756d3439ebfceb9446b4bd90483e174528daf37ac488408c3ac8033
~ sub_100010478 : sha256 4e00876704b5fcc017839557ff467417a3ff5b720dd19f727323472b4e8f658f -> a750aa87ded43da4c9a9a24863594069cbe0790ca0854e70c6d040d8372d4d72
~ sub_10001058c : 176 -> 208
~ sub_10001063c -> sub_10001065c : sha256 8bdc075b0c7262cf540686e154a530b36fd77a1a6558599d91f3f1a2b13379be -> 7efa2ee0ead95d3e75a91c67d72508dcfc79687aa0c3e9130c903620e2a0a5a2
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.122: Could not exec %s\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.132: %s returned non-0 exit status\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.188: Could not find volume group UUID for volume device path %s, error %d\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.222: Could not find preboot volume for volume device path %s, error %d\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.228: Found 0 Preboot volumes.\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.279: Encountered error while inspecting path: %s\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.295: Error considering KC copy: srcPath = %s, dstPath = %s\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.29: BOMCopier fatal file error: %d at %s\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.303: Error copying KC: srcPath = %s, dstPath = %s, error %d\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.319: Error creating BOMCopier\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.330: error creating / accessing '%s': %d (%s)\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.34: BOMCopier fatal error: %s\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.379: You must be running as root to manage the kext collection preboot area.\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.386: Error reading bootcaches for volume %s...\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.391: Error reading bootcaches for volume %s - no fileset path?\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.398: Couldn't find volume group UUID for volume %s (%s)\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.39: BOMCopier file error: %d at %s\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.404: Couldn't find preboot mount (or preboot not mounted) for volume %s (%s)\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.432: Error considering preboot KC path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.444: Error considering preboot KC path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.453: Error considering preboot volume for %s...\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.458: Error copying KCs (SystemVolumeUUID): %d\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.462: Error copying KCs (VolGroupUUID): %d\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.474: Error considering preboot PLK path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.485: Error considering preboot PLK path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.494: Error considering preboot PLK path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.499: Error copying prelinked kernels (SystemUUID): %d\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.503: Error copying prelinked kernels (VolGroupUUID): %d\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.542: You must be running as root to manage the prelinked kernel staging area.\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.549: Error reading bootcaches for volume %s...\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.554: Error reading bootcaches for volume %s - no plk path?\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.560: Error reading bootcaches for volume %s - no plk staging path?\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.571: Error considering prelinked staging area...\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.580: Error considering prelinked destination...\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.585: Error copying kernels...\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.68: Could not exec %s\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.78: %s returned non-0 exit status\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.97: Error creating temp preboot mount point %d (%s)\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kcditto_main.m.24: kcditto installs previously built kext collections onto the Preboot volume.\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kcditto_main.m.25: It takes no arguments.\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kcditto_main.m.33: Can't get executable path for (%d)%s: %s\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kcditto_main.m.43: Error copying deferred prelinked kernels (standalone)...\n"
+ "/AppleInternal/Library/BuildRoots/4~CSDtugBKR8v37Yn6R_R6g4saDxA_MxtjMJdfYSE/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kcditto_main.m.49: Error copying KCs (standalone)...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.122: Could not exec %s\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.132: %s returned non-0 exit status\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.188: Could not find volume group UUID for volume device path %s, error %d\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.222: Could not find preboot volume for volume device path %s, error %d\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.228: Found 0 Preboot volumes.\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.279: Encountered error while inspecting path: %s\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.295: Error considering KC copy: srcPath = %s, dstPath = %s\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.29: BOMCopier fatal file error: %d at %s\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.303: Error copying KC: srcPath = %s, dstPath = %s, error %d\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.319: Error creating BOMCopier\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.330: error creating / accessing '%s': %d (%s)\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.34: BOMCopier fatal error: %s\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.379: You must be running as root to manage the kext collection preboot area.\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.386: Error reading bootcaches for volume %s...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.391: Error reading bootcaches for volume %s - no fileset path?\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.398: Couldn't find volume group UUID for volume %s (%s)\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.39: BOMCopier file error: %d at %s\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.404: Couldn't find preboot mount (or preboot not mounted) for volume %s (%s)\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.432: Error considering preboot KC path for %s...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.444: Error considering preboot KC path for %s...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.453: Error considering preboot volume for %s...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.458: Error copying KCs (SystemVolumeUUID): %d\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.462: Error copying KCs (VolGroupUUID): %d\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.474: Error considering preboot PLK path for %s...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.485: Error considering preboot PLK path for %s...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.494: Error considering preboot PLK path for %s...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.499: Error copying prelinked kernels (SystemUUID): %d\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.503: Error copying prelinked kernels (VolGroupUUID): %d\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.542: You must be running as root to manage the prelinked kernel staging area.\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.549: Error reading bootcaches for volume %s...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.554: Error reading bootcaches for volume %s - no plk path?\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.560: Error reading bootcaches for volume %s - no plk staging path?\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.571: Error considering prelinked staging area...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.580: Error considering prelinked destination...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.585: Error copying kernels...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.68: Could not exec %s\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.78: %s returned non-0 exit status\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kc_staging.m.97: Error creating temp preboot mount point %d (%s)\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kcditto_main.m.24: kcditto installs previously built kext collections onto the Preboot volume.\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kcditto_main.m.25: It takes no arguments.\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kcditto_main.m.33: Can't get executable path for (%d)%s: %s\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kcditto_main.m.43: Error copying deferred prelinked kernels (standalone)...\n"
- "/AppleInternal/Library/BuildRoots/4~CQheugCkthdiUsS96iILTVVFS32JeXejYokrpYw/Library/Caches/com.apple.xbs/TemporaryDirectory.zI8ElT/Sources/kext_tools/kcditto_main.m.49: Error copying KCs (standalone)...\n"

```
