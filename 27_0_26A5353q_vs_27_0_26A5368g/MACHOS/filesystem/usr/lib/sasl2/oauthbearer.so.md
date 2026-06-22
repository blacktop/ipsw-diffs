## oauthbearer.so

> `/usr/lib/sasl2/oauthbearer.so`

```diff

 195.0.0.0.0
-  __TEXT.__text: 0x160c sha256:fdae8f58cb3cd2fee6f4b624e1188a662f155bfa7b31a3a3b5898c66661ddddf
+  __TEXT.__text: 0x162c sha256:52e2fa819a9ab417a808c4da010b28095b9df3a2a41d8465ad04791958f5a2f8
   __TEXT.__auth_stubs: 0xf0 sha256:6cfe3815f95f0a0b64695ebcc5039c7b338285422e9b9d1724bd0eaadf248966
-  __TEXT.__cstring: 0x526 sha256:5c127edc10e282ad892579d86d99517906d2b81daaa9a02387faf36eee0fec08
-  __TEXT.__unwind_info: 0xb0 sha256:c9eaab1489821ec1214b513f529b7e333d5d95af62bde07d4131d2a0980f6cf0
+  __TEXT.__cstring: 0x526 sha256:9bc3eab9c711f771012449746c25f78d6954d4e2939d1dbd3f280221799eb0e1
+  __TEXT.__unwind_info: 0xb0 sha256:1586c32c495cd364b50de41fd93e2924b48815cbe144b2bdae3c434df8452a30
   __DATA_CONST.__auth_got: 0x78 sha256:38c345cb9cf8745099627a43c391a1581c0c6e90e4af5679a2e9737df975dec9
   __DATA_CONST.__got: 0x8 sha256:342c14f50cc87ae753fbb43ed5599d9575578190e65d4f72909a50c20c019698
-  __DATA.__data: 0xc0 sha256:cc44f1cd0c45daeb22899548a94dd24c250a1a6177678ca6bf905d3d4e02405e
+  __DATA.__data: 0xc0 sha256:4e470c3da566d485b12fb86f12478c16275171c7900284eb8c6780e13df5fe22
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libsasl2.2.dylib
-  UUID: 7BD408D3-0586-3C85-83A5-4AB4DA2F22C3
+  UUID: 6301098F-515B-3433-8677-560FCBC5E592
   Functions: 20
   Symbols:   37
   CStrings:  22
Functions:
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 3c9c2b348f2aaca002da4ec0c09b6a21e43b4870fc92ebe3b58590dc7dd67384 -> 539c403d14190010b69cc70ee59eebd416bb73460224e139fe234bdb105cd9d8
~ __plug_strdup : sha256 a30a85c5c2004da0ac7ac582d0d69d0f543d87bd2ee2ca25e4eb004eec6a477b -> 99db690c60360817d046723c59bcd9ff35cc1f629bca3586554411c6eb12d774
~ __plug_free_string : sha256 d01aedd5619f89ea862dc9c3f76014a369ed847712345fabea6c9ed0a221a26a -> 7f75598710a0ccf355dd91b82b205bf60b4899d96f79693917a405695cdaf502
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 e6c491f4df8593b85e7df19d0fe5bd859ff858671c0d5d5b9e38be97ada29921 -> a352544e8d0b05cc8e52c1b638680525daea83bd7bd5f9543e08a404a06bceb6
~ __plug_get_password : 368 -> 360
~ __plug_challenge_prompt : sha256 b13e25793e9d5075e7ef04ba215f8abb5738d24e544966abadcf7475adf3718c -> 8b88cb203a950d755b2ae0858e367aa5b5d81968fc1e3432c27ce1e829210f90
~ __plug_get_realm : sha256 aa0a41ac76508056388a464cb3860c749860bb2960ef08c542bbb0659ba6267a -> 8c519a0552008e4e9e797cefb20225a7ec1d72820d27abc4e20da9cbab39805a
~ __plug_make_prompts : sha256 d664b21cfe359c68e686bba2a88134a3d52afa6201ae6b95bbd815ef85115821 -> e4e61418ca275ef827f82fc0260f4db580eaeec1c1420020e917f929cc5423e5
~ __plug_decode : sha256 b4223c68759db3fcbfb8367a6b4126ce3bd111f48f8cf3fa7f16d6864d1b35c1 -> 8aed305ed245ab8cf0782781b2639c2ebdf33bf865b7efcc58d47fc89e6becb9
~ __plug_parseuser : sha256 79052d4c2f9389692852698e4e7c3c972379c1c337aaa59c1e034d92b42d5dd0 -> 9394262d2a217790e36830a715c3e7d45ab9b80204e6316c4ce1c60520d82729
~ _oauthbearer_client_plug_init : sha256 e332e65ecdbd265c61410f5959689f6097afd43ff5a2437110cf30608cfc1e7f -> 210c170315e9d79a3d921728743cf62393a93c92812434b02ff99f50fb4072dc
~ _oauthbearer_client_mech_new : sha256 c9e2ec63a452b8900b0d52ae0c17b89282726707de64707ec7e743d7193b4e48 -> a49b9906b3b64338facf2d9a12c8224427843e3fe184389d8eeea52f4fd0312b
~ _oauthbearer_client_mech_step : 1316 -> 1320
~ _xoauth2_client_mech_new : sha256 aeb03433caaa0603ce95bf6f9d8659ab6514def60a3e0c48e2adbb9180f53287 -> 8046f58cebb70822f9af606042d972447e2b9720a73c2c113416e27e1c4d9b1f
~ _sasl_client_plug_init : sha256 b8b14e1eadf411cb37d57f77533b5293b3173f9972bd04e87fb9eac6398881aa -> 2e80a9abacbc3b63ad7f2e8ae163e72e75d67e671fb47a321a213eb4963f4b0a
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/oauthbearer.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/oauthbearer.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
