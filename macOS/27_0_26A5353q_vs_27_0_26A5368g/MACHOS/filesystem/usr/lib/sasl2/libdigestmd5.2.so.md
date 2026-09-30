## libdigestmd5.2.so

> `/usr/lib/sasl2/libdigestmd5.2.so`

```diff

-215.0.0.0.0
-  __TEXT.__text: 0x7050 sha256:af76742d5de2fe56d86956c3f58da97f76664059d6de689cdb8448a7e1b6b28b
+217.0.0.0.0
+  __TEXT.__text: 0x709c sha256:1a20966b4dcb7edb58962dd52e8ab7fad020e81687b8dc6e3acbde5ee7471845
   __TEXT.__auth_stubs: 0x190 sha256:7d5f4f2340adb56359d0ffd41635e112b449f19039c0638289f8d0a791ec6614
   __TEXT.__const: 0xf8 sha256:ce7c590deea3995c96dc09a4f23e2004a3ead1c42c80a759ee53657ce41d3e54
-  __TEXT.__cstring: 0x138f sha256:52285342243c3648f6f7d532bb3856400912dfe06a8634d8da7b8a526a406652
-  __TEXT.__unwind_info: 0x118 sha256:5d897c121fb962b7b97588f91cc17b6b159cdb0e8845702a6dcc2a534467571c
-  __DATA_CONST.__const: 0x18 sha256:589ced0a042865683f467f82237d3dc0696809ca980d853b8478f60ee4c459a9
+  __TEXT.__cstring: 0x138f sha256:48e0982253b57bc1406e7a871f67b4c0b5465c6667e725699d681ff2a953b822
+  __TEXT.__unwind_info: 0x110 sha256:2d2f6f2ff5a8f067843ee26177ed3c3e2b14eee65789e72a38058a71818209cc
+  __DATA_CONST.__const: 0x18 sha256:635ea2647e1bc2651c56c7217fa986a073bf138ece8903b8c294a784c818d9d1
   __DATA_CONST.__auth_got: 0xc8 sha256:8dbb4e970afcca96d9901fb3800c860238c5a83b07da1217b50bfdbc868c48ab
   __DATA_CONST.__got: 0x10 sha256:3a34334c69f400044263b55b4df4170e9fe388ebd9f9d85ee72fcfcfd519c490
-  __DATA.__data: 0x1c8 sha256:710efcbb32b6fa801964b120683c5cc4fc00c1e74ef3b04d9c6b53e6b305b35a
+  __DATA.__data: 0x1c8 sha256:ac319b7bc54d4fe6e2d727d3ca30950bcb69d83663b5826000467b35c8b7ede1
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /usr/lib/libSystem.B.dylib
-  UUID: 7A917B38-B504-32EA-947D-C6305642BF08
+  UUID: 036CB82C-8FFF-325B-8E7B-B89023AAF667
   Functions: 56
   Symbols:   93
   CStrings:  159
Functions:
~ _DigestCalcResponse : sha256 cddc9bb940ed307681a600fadd5ddf2e267dc01e38a8d64cd275f9f580b70ee1 -> 2e91fc99b93c2094a6a13472065549d18d93fb51dc279d1bd44b120f095b4faa
~ _CvtHex : 92 -> 100
~ _enc_rc4 : sha256 d09b31c40cfec1fe977caa16e88150ac9827e135fd15cae9d6e71795df375317 -> f4b66ef9207a879484f5badae6858c7fa2604044de0db2fd1870f77874765255
~ _init_rc4 : 328 -> 308
~ _digestmd5_server_plug_init : sha256 9ed1bc0efd0dc84345b5a2f442d43abb7bdff941aad5f20b4734b9371b6de422 -> ae1d9ef7a5e75ecaa30ae2439d8e123831665e8b8d30a7eeae22ef431418f8a2
~ _digestmd5_client_plug_init : sha256 d277fcc38d0ac8b06e968822b04587de99aafc7b1d7f841844e7f8906c1f22ff -> 3464263cee7643f4bae3a262c6c0d081ed4e805dfccf3c11dcd0078f16086fd2
~ _digestmd5_server_mech_new : sha256 9bc5a7f17f0bfaa08256a21de10607f458e5662804357057f823bfe653856a24 -> 3cd27bdd3a2cc5200e35f26e0bc82f71b9728394ac65a1306eb22e7ba9506bcc
~ _digestmd5_server_mech_step : 1884 -> 1892
~ _digestmd5_server_mech_dispose : sha256 6861252bcdf31e5d484dd5173d9ab77c7133dc8778a786595f62f70395ac4993 -> 62f8b513b671675d9ccde87faa3b741304ec5cf7245c5862a04544e6cecb11d4
~ _digestmd5_common_mech_free : sha256 81daa973023b56c8cbab4003917b14ae8f2a93ad5e551a2e914046c1a4ceb620 -> 88a433029bf07e325c05db2b0c995c3ff3cf6dbeb9646ed7857052314f6feec9
~ _digestmd5_server_mech_step2 : 5260 -> 5252
~ _get_pair : 592 -> 584
~ _str2ul32 : 156 -> 144
~ _DigestCalcSecret : sha256 6f2b74c825ddcdf74f15a1d08817818898f21a0b2757bbcbfe3c5f7783df445f -> ee2f34651ecbb82b742b07f691dfc9f38f2044b333aeedaef216729f5d6b8c93
~ _digestmd5_encode : sha256 c1bbaa59137e52565e6c741d98bf536eac8274324455919abc180df772541929 -> b1945a8fcb6b4626daab0dd7fbc71a500766dddeb28b293078a713b55f0b0a1d
~ _digestmd5_decode : sha256 1fd34935c916c7915734afb93499b0ff8b14e71f40c2f9c9bdab4520b4d58024 -> feb979c16088dfc7366960522bbd0b392df558f0488454d70bd3ae9a278661a5
~ _create_response : sha256 e2d6090804fb823d85fe0a08232d9e28235a250d72c94ff856cf488a5715d863 -> 02090e86dfaf634be370a7f0378e730d88f579bc4bdda0975ae1a46866b553a6
~ _create_layer_keys : sha256 914b17cd94d8a6eedb86d8fa5a93b2d666cb658a87077b23e764f17a162aae06 -> 4e805194e353cc1f3329279b48c1337ab5351b8c4d086388dcaa7acfd22da624
~ _add_to_challenge : sha256 f03daaf1a3f3fa1d98b44398000dac56bf707158d2c08b217fce458a0d301b0a -> 6e3d86ec12f6622bf12f40d089c6e8a458cf582cb670688e901f3a7ebbb76363
~ _skip_token : 140 -> 144
~ _MD5_UTF8_8859_1 : 296 -> 276
~ _digestmd5_decode_packet : 508 -> 504
~ _create_nonce : sha256 6d9cd8b65a891a34b2d83bec427aac4c2ba03910df53d365bc4e7b008a9db5fb -> 35b8f0a479add6c1cf808d24be6aa852b1318f39e87824d9ae57bdb835f98df8
~ _digestmd5_common_mech_dispose : 372 -> 368
~ _digestmd5_client_mech_new : sha256 e2eb8bcc1ee0c7a05e02be38fdfdaa732385eb5c30898dda7defada77e8d4130 -> 0a62220ca0bb88aa029d246d08105c70dd599eb2033f965beceb3223d5cafa11
~ _digestmd5_client_mech_step : 4000 -> 4084
~ _digestmd5_client_mech_dispose : sha256 987d4ebb859451cff850b1f5201eebc8dc9483d2b6955f644a8345af6a25927a -> 6e33cfe37f664ec1afc1f4279a5986893d1101b9c935b8eac73a4f549b4a2248
~ _digestmd5_client_mech_step1 : sha256 254b6d24c5208489e02ae67fa72006069e4e4f8eb15fbdc04d6fc1df5417dbcb -> 88dd7fec001d8a4044a7a40f3d85ea87dd663798df72349e48d21d536a1bfa43
~ _ask_user_info : 1040 -> 1060
~ _make_client_response : sha256 925b1476d162ab17684133548f01f9fc2f9ab6d77b4bd54450c2a527ace8845d -> 4788d596595edea52dab280fd947f2d598933f8bc0d2ef6d7ba3f159e73fddc3
~ _skip_r_lws : sha256 553724bd40018d81309277cb42440f0356734a73b3ee8acb8d378b3e47757324 -> 6128665b72658b53f452feb51549e0da4554a00ac1779d6c77e2b79bbaf4df44
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 593a4ac08b0ff6f292944ad19919e1000b5e016ecf0ccb48917deba7d87f44b9 -> 152a97c025769c5493ef755dc79e6b25adec3ee2cb6748181ebafb5ce83a39f0
~ __plug_strdup : sha256 ac075e22568bb0b9b0a0713462d95414217b33276846cf27360ecb86a2a9a5a0 -> 67e02764d1dd63bd3b3969ede87d62256a27cef28adcbbc9b6767097fbfd23c1
~ __plug_free_string : sha256 3d58fb921ebbe37754d3d5baa65e1bfb260988c80e49f08baa17492284b77c41 -> c53417a9437e76390550436ea29bef146fd9edd6a568b21a1d87678ab26d41bb
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 9a72c0783c85e819edc3628864e850491dcf79b1b49181f25759b2e7dc2f5e08 -> 96ea43ba6e02bc2146ebe1e4626a96a1fec6f1a619656967a7d9661770063d09
~ __plug_get_password : 372 -> 364
~ __plug_challenge_prompt : sha256 8b3378bf9ba7b7d10202f0a0e287126618516aa174735a18bdb63d0c8ead2e74 -> 5a3a93266489d1d3eccceab287b67474c81c2f4dd13e4711a2c24158cf2ea810
~ __plug_get_realm : sha256 3e99520f747b254247c776de181951e5ee01dbc680f034e0ff1de2cf3829fe1e -> 6e8d07d553391d31fbfc4ee08fdd6b736b01d6d0e75377c1ef21d615cfb77e43
~ __plug_make_prompts : sha256 0f8a2bf16c8f70109ba9d685be1d69f463a6c475f961b90a89af2b086a48ad22 -> aba8450dc6c45c61ec1276454d2fdecaecf8a0e074ebee799d2a923fc0feb5e0
~ __plug_decode : sha256 f721e493d2fc45a06fc0ccda167925bd09bd43d4082d7a22e1ac7d82c50a44cb -> 671fbc725b1678130bf9fc41ad7661fe47b73c0cf66bceb852142aa5c46826ce
~ __plug_parseuser : sha256 ad7d1d0c460b30c53c36f7595d6e8eacf3f95089187fe2402428ac566b33c3b1 -> 6fc6332ecde5898aaaacaeddd87e8bf357d7fcb5b93cd53f23dab1686530bbf1
~ __plug_make_fulluser : sha256 4063391c8a8c4d58ee5c6d07942fb9ee3a4499915bc865ee36060c6683dc05d0 -> e446aa685494ecafbb0b39b52297bfb4392658ee12529f0c6be620739a832622
~ __plug_get_error_message : sha256 e4a86cf44ca2a9759928a3b0bb61307da8bdb4ddf4f20236d83083f950750c23 -> 4c96004530b63e2d00dfa0327599fb29a3193396bfa745cbd3fbb81e78a65c70
~ __plug_snprintf_os_info : sha256 26b4845ee8c566a93245eb1735034658043657c4227a6e7f30e8bf94d0305e62 -> 2977818c3fdb18e2f3265531de2b34099e6a38c5cd1e414a1f2d53b73d356802
~ _sasl_client_plug_init : sha256 d2b0c95f60730cccb35c6e486e1a6b0f16fdd8bf1f8c4f029e9cd593cdad4155 -> 101af89a0da55eb46f898ebea55952d3076c9f4a195e16503656e5a721c41dc5
~ _sasl_server_plug_init : sha256 69a2d61b1675d95c9ecc27c0f6e558df2862067e2931165f805b4ea78dde6ed1 -> eff43dbe0a90d84175720e08814a94d551d6867a01aa16fa047c439311486c75
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/digestmd5.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/digestmd5.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"

```
