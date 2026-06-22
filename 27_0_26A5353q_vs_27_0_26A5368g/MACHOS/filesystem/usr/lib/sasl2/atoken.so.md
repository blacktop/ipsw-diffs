## atoken.so

> `/usr/lib/sasl2/atoken.so`

```diff

 195.0.0.0.0
-  __TEXT.__text: 0x14bc sha256:51be42c0bdf93e018e863e0f133fba2e28ac50cd586f8e890442b9b1e412338a
+  __TEXT.__text: 0x14d8 sha256:27504e81c7a253ba9532a3f763f8335f11847555f3b8a8d2882edc699ea710ca
   __TEXT.__auth_stubs: 0xa0 sha256:0f73579e3b77f170acf64140cdb9cdda03d3b281474061a0d50b94cb11a607f3
-  __TEXT.__cstring: 0x3a9 sha256:a56baa65856d5b6ee8e4bfefaa0c25153f4510c4fba6949032792d045758a2c4
-  __TEXT.__unwind_info: 0xb0 sha256:a857c9e43aaee6bc96c5347a738782aba9538a286ed10e4b7bd4def5a19341cb
+  __TEXT.__cstring: 0x3a9 sha256:9330fa244d87feee7524fc9f49dfc638df220807aca0ce860d438e6d8059b98f
+  __TEXT.__unwind_info: 0xb0 sha256:bd5bf779d2d9d47eece8962c542e6f88d8c8d4a788317a508943c4e390f2c966
   __DATA_CONST.__auth_got: 0x50 sha256:d0afeb17ae3c6f2bbf48f7670673900580b84d4fea07168e4558474a49f85f46
   __DATA_CONST.__got: 0x8 sha256:3052b4ee5b2db9dda29ec6da48feba3fc4043f1b4b2432ce1a9040a7f870a0eb
-  __DATA.__data: 0x60 sha256:2877bdb2d374b421801349e269422aec8737ce82a7bb95d474c42fd7b56bb90d
+  __DATA.__data: 0x60 sha256:106f55303befb0f0a4c340b1013f56973e3ee11722a9f6cd16279b1354e0d0c7
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libsasl2.2.dylib
-  UUID: DD0C7A48-CADD-3400-B9C7-05ABC7BD775A
+  UUID: D0B342C8-6B7B-3EE5-A5A3-48F3889619DD
   Functions: 19
   Symbols:   31
   CStrings:  14
Functions:
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 95084689597ec24108aa759b38dc3afc9de8cc891ce47f39684d2b6607db12d6 -> 1b032bf8f10325a7d90ec49a5f4452da008062d309c74fd82bedd52c25ec6e3c
~ __plug_strdup : sha256 2ca5f531a91f95fe923c20976c68159705937605a8097f4a4a93c5659dec7acc -> 98dc17aea74107579bf20b92d4113334981b3e9d8ad24faad047591f57a2829a
~ __plug_free_string : sha256 4230fcc64b55cc7b7e2f08973a41c3f5e12d94e87ff4a06c344d4b2de3e63d8f -> 95c55985f9e8a4a0f817142eeff85d6a0ee435d56806170c8256dff699638fd4
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 03e97fb3c06ae7c72d2adfc88e10f9c930352cbb9220f81724a688db81d94602 -> 41f795696f992971d0a5887e7beb2b2c422d5417e560b20cb606134574c3c327
~ __plug_get_password : 368 -> 360
~ __plug_challenge_prompt : sha256 1e320b31f235c39878e35d995ef79ab77c4f8957b6b93f5a18051a5ebae00cfe -> 206c667e7b02a4c31dc05c017255470ce924b2b97802749210c2c34c6fdca10b
~ __plug_get_realm : sha256 b8b8bd55797dccde927c4acc290c9e99dcd8647a0250e4990e3458ee0ede71f2 -> 3a67f82165a05a1b2c06bc9fa9055170e00e87628354a5c458dff938b43c98eb
~ __plug_make_prompts : sha256 18ef77549e9bba8ecf6941d30efdeaf0ece12a9b62cd61d46ab92fdd66c7d8db -> 5db815daae98b64b814aee16200f0f21944d48ce6f84eff48b998c4a1dddead0
~ __plug_decode : sha256 bb051eb6c8dffd4eb0d17e3d5e909516120f198c1771e312dbc505d0040ba399 -> 0d688da92029c1582e6f4933d56026977b1a2c23958a93fb4a9c5a9c2e6a267d
~ __plug_parseuser : sha256 990c1d51638f4293f8f5024078c1ee3dcc14b8dcf11f9d1ce844f1260fb107a1 -> 971ff874b2658bf710ea6dfbc9ccc4f07f3a28571da9f8d17401e4e82c99d0a0
~ _atoken_client_plug_init : sha256 e76347175acbcf2620452c3770957f3d5c24c49a998b239ead14710d7fe3c5d7 -> d9dbba2318f5e119d8b34a4f8cf30f2ece999c6b7d34166958a3087fb81cccf5
~ _atoken_client_mech_new : sha256 45171c3ef4423473e66ba246308be19a2b6e63162f06c0b7f1d2648005100f22 -> db0e280e4f58a7be41b96b75dd712000edef03517bbfb6ab2ba9b73f6b050e40
~ _atoken_client_mech_step : sha256 ec2a5ef03f66f9daf9049d7fb4aafac32dab921da15f026d0cfb7b5afaf1c77c -> 202746f8533dd5efdd5e980ed70074d5967e2579c03b37b0fe189265f6dd4edc
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/atoken.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/atoken.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
