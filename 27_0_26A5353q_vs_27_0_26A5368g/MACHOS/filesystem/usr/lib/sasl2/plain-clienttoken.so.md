## plain-clienttoken.so

> `/usr/lib/sasl2/plain-clienttoken.so`

```diff

 195.0.0.0.0
-  __TEXT.__text: 0x1460 sha256:c9a614c95c84d46ec079633c94f76cf827ddd102ac6f223ac9b51a0d083372d4
+  __TEXT.__text: 0x147c sha256:00d1c038a58a1f5dc2cd240873c87b10e11379cd8dd71e955bd21d98d04b8e32
   __TEXT.__auth_stubs: 0xa0 sha256:0f73579e3b77f170acf64140cdb9cdda03d3b281474061a0d50b94cb11a607f3
-  __TEXT.__cstring: 0x4b6 sha256:5f93dce7e09aa2c8d80b6fbf822756518ce630a472a92996f577d98bf89aa262
-  __TEXT.__unwind_info: 0xb0 sha256:7ef725358bf6f4f6722772b74ab29c4b435cbfbab5c98c1737fded6723097387
+  __TEXT.__cstring: 0x4b6 sha256:e5dc3bed900f27ef0a74cd4ef269ab7dc3d933d51ab9d0c897dd19a09ff7017c
+  __TEXT.__unwind_info: 0xb0 sha256:fd426db0bd98664fd11a8be25cf8a3a7fdd885f320583711acaa666b8e68430b
   __DATA_CONST.__auth_got: 0x50 sha256:d0afeb17ae3c6f2bbf48f7670673900580b84d4fea07168e4558474a49f85f46
   __DATA_CONST.__got: 0x8 sha256:3052b4ee5b2db9dda29ec6da48feba3fc4043f1b4b2432ce1a9040a7f870a0eb
-  __DATA.__data: 0x60 sha256:dd93604393e036b31e8d68885241f504cc8e7e11cb25d0783d468f358a7faea7
+  __DATA.__data: 0x60 sha256:55732eb611ede186823979a708ae9f3824026cf522c2b83756e435c55072bbb2
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libsasl2.2.dylib
-  UUID: 1BE04063-A622-344A-98B1-ED9E2D39B1FE
+  UUID: 2242D6E3-24AE-3361-AAEC-8FC206B8055C
   Functions: 19
   Symbols:   31
   CStrings:  16
Functions:
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 1592623e957c0eceb5963dd76ca96870e9340aa21e31fbc1a2ba5f5a3e34a57d -> b918f574a7c04a090d188dc6454b7efd267759ca028cba095de34d3e7dc72b7a
~ __plug_strdup : sha256 5ecb31ef6e666bff1ded68a35aff968b479ebd4b4eed6e23414bc41215843f0f -> 4129a77778dcb5d74e96423d80b57a619fb4300d96fc14b34c5d045cf4162e5c
~ __plug_free_string : sha256 2e5e136030926eb8381798cfa54704489a6024d4ede4639ca1d7357f2c16faf1 -> 638fdd6faacae8280016d56a44828ad500b981eb88c34c16086f0bad02f698a1
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 7f2b417cc7ad811cea6a0f0617f994790744c202a21ba269e7d5556c9b953384 -> e40effd25abf7d2bd30c03084aa39f55a9bcd71cac11a2e1d38cd60a445d4f35
~ __plug_get_password : 368 -> 360
~ __plug_challenge_prompt : sha256 ad6a3861333709b20b7ad76a2957bcdb52d0a79dffe1179bdade958b6243dfd0 -> 971258266957665c721574d6e7b18d6a102a558da7cf8063a1d2442c16d848ef
~ __plug_get_realm : sha256 6b9dfa4fd4a0127a3e990d7e85882ea7125ae639be0e8efd14b5406925585d65 -> 9cd7c17d1314d500b7f50edd94044b9f82324b0cb8e299c523d5f7b44e91ebbd
~ __plug_make_prompts : sha256 deaf9b2d9f8c0701e556ee89b3eccddd753a60452033c4b5717ebff1d6dcce8b -> ebd82df6a644bbcf7b5b589c5eaee036c82515e456b671d15869015c45d92a36
~ __plug_decode : sha256 19d944578410d9fcaeb427e7c2257f3367293671f70acff3bbeb659b3c27bcf1 -> b6014376436ed5b2a629ab7a3a9f0df45eb41aed1a63007401662261d17069e5
~ __plug_parseuser : sha256 3cd1a926816333cd9ac513a21b7ea9fa7a70ad8eff683b178ff4f1282c1ee154 -> eb27e7c51f0c45b3a52c1b66421875dec74cef81a34b57a5d9ef560fa89df9b8
~ _plain_clienttoken_client_plug_init : sha256 799bec7f39825c7ac2e53c44a7136fa8ac0669a139c7b058329ca7635268e90f -> fffd290082391f6b9b5c5a3d0272df0643728777921dbf9ddb796153d55c53f0
~ _plain_clienttoken_client_mech_new : sha256 a9ec264833c30a263ec2ad3591fae4660dee39a6d6ca0584074a850f33f23ce2 -> 8c1a9fbb7a11dc1ab6c23981c050705986d0d0738168d82246a4b0e30fe6f922
~ _plain_clienttoken_client_mech_step : sha256 690eb4f2f6884a79c57d96fe13166532e81fc06bf6308581ba6ffe048343aa2d -> bc6c1f33fe93b9eda3291b179e3769e95ab38c2d42377da21bb542987a20608c
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plain_clienttoken.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plain_clienttoken.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plain_clienttoken.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plain_clienttoken.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
