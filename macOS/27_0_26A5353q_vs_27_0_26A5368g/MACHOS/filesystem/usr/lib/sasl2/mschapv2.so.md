## mschapv2.so

> `/usr/lib/sasl2/mschapv2.so`

```diff

 195.0.0.0.0
-  __TEXT.__text: 0x2490 sha256:1266a16e5ff83c7c29249afb87c0ee7ce763cab82d622d5f154c7ca1e1b96c3a
+  __TEXT.__text: 0x24c0 sha256:0a1d869a8d441a0bd61b694cb556861baa34c0ba106dc80d40a48fe98cbc6042
   __TEXT.__auth_stubs: 0x1b0 sha256:0561da4ebf499fbf2943843c82c6c4623e3192dc0c20f94361fed91b37510387
   __TEXT.__const: 0xb0 sha256:1217e8215ea008882060556cd980d24d99f813414efbd740d3df33e2a60bfd35
-  __TEXT.__cstring: 0x6b6 sha256:5c6fd20f6d70d90ce86663a7ac04cf436c1312799745458628b5e55a47e1bcc7
-  __TEXT.__unwind_info: 0xe0 sha256:7bab367cc353f1e07260531c9965681baef93d9687a5be31937adff32bd8c251
-  __DATA_CONST.__const: 0x18 sha256:3b9d9c399571e2faade55b53134d931a458d3e1f5571a6d56bb7c86fa2767d43
+  __TEXT.__cstring: 0x6b6 sha256:02998f4e1f62b6638cd72147e057cab6dac5ef9da5f880aac225f206f486dae1
+  __TEXT.__unwind_info: 0xe0 sha256:f60db30fb60eddfb36b2f08e9eb0059efedbb97dcbd1cf5610f45adf08c627c5
+  __DATA_CONST.__const: 0x18 sha256:74d4057b9e4a5e1f610eca14978711cef536ab78b3c5f08b3f33d64ff0c7e827
   __DATA_CONST.__auth_got: 0xd8 sha256:74b1f610eb69f548ed94373f82b0e1c9d4e406931bc0aa23fa2218cdad04e863
   __DATA_CONST.__got: 0x10 sha256:1db937dc8851601866650c6c4cda04e189e84cc39f42e48dda1cb09efc370dce
-  __DATA.__data: 0x1c8 sha256:9355bcf5362109e20bb702ea3881af8bb1b2edd9e16ec9cca9538d19a6d6e4d3
+  __DATA.__data: 0x1c8 sha256:56481a2b7882fac283fa0a294c6a6e0e10c03300e513fef574be0cff5f4e4d5b
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/PasswordServer.framework/Versions/A/PasswordServer
   - /usr/lib/libSystem.B.dylib
-  UUID: 53D71DEA-DBF6-3A1D-A197-F0588F9C7918
+  UUID: 2C3673EA-4A21-371B-A253-F64E532B5810
   Functions: 34
   Symbols:   66
   CStrings:  34
Functions:
~ _sasl_client_plug_init : sha256 1ff6be60a1f89cd5f9ce786aecba93e2fe5db87693a6b2de912f258524d05a03 -> d543b16d2cde891e67dc4621de29fe77d05ea078941fe509697bf9d6120bb4c7
~ _sasl_server_plug_init : sha256 3bd43fd7d2b6845b584a9bcbe36968f00fab2a8a2aa6e81f324a8417a06e840d -> 8fa573e7d5aaa03b40bc55cbd598630bd85bfd79ba06de6d1be870a038b8f9cc
~ _GenerateAuthenticatorResponse : 384 -> 380
~ _chap_server_plug_init : sha256 12af1ba667e41b1be16bf9dd083adcb606daac451ebe3bc76ada876c939fc601 -> 0a08608f4b4e22219730edbc7bb176ccb1683bf887f4f5761f244cc4e07e2bee
~ _chap_client_plug_init : sha256 2be7eb7e850c4dff972af51f5b705a0b6702502fabd905563252402b66ec81d0 -> 18e2a9a48ebcc422b2a83916766c9134a449f89bc110d2b6bcd029d200eab3dd
~ _chap_server_mech_new : sha256 4ee624c63b2fb5e467872b0d02f3e6d8e948b4a0f97eab4b9efff03c2593c2bc -> f61c6a3653e9587f6d2f2f721d393a0cec845de6a90761dd1a64047c2e74dc45
~ _chap_server_mech_step : 1384 -> 1392
~ _chap_both_mech_dispose : sha256 1e0dbe6eb6b2fc4b80aa8d21f849df9a7c0544594af508cc8f363417c5bf7121 -> 74295d665fcef16d825be65c8d5247b8f6ba216a7dcf81e66f161d1730bec244
~ _chap_client_mech_new : sha256 8d3fbb86dc642e27a5d179dfd3e802d211ca09813b416d5a88d5d96b983746f2 -> f926c5e19e3fb1865d4cc5e7a70b5c3ee51a93da176bbc97a551c38ca0690781
~ _chap_client_mech_step : sha256 7b580c8f134319acc4c74905b5f93bb382b17a4cad95e5ff29b83870d480d995 -> 7d7b062222251c1794260cb214925dd841365c05a20f929230951953b2d676fb
~ _ChallengeResponse : sha256 39a6f420fbbe01f71a6b0ecd129aa1e1cc5678973c496badd08f7d252595f131 -> 5143d9d9154d3e3639268a250a65bea5a76ac2f689c9212d53174900fd2ab45e
~ _DesEncrypt : sha256 6b628285e71b0c6f9ef226592f01c66e008b5564953070c95165c31978e908d5 -> 8af2ce8fc918b34a5966d7c2008e636d66aa30bf36d9ecc13ba4b78bd062b8dc
~ _ChallengeHash : sha256 d6c849d3b8736a0921edcf5287d4953070b62ffac05af827df5b4e9ea7e54592 -> 2299fae3f58b53547f646bc762ce80b2b738d60a94c768a042d63ceaca6801b7
~ _NTPasswordHash : sha256 0dd07a109f3ba5d751e46a1e54308b24a201bb71d0aec12c3f3033d172f96041 -> 7ac8562aa459fd8e4c57d775df69b819391d1e3d3319426cbb78d70b139840e8
~ _ChapMS : sha256 2bb571fd40cbcdf0b38559d9cb37b788dc6b2d4c125b32531d08f27e9912120a -> fc74da735b5f35b3d2674b192de9dd4970d9ccf63f281cb08f5560c1dd3dccb4
~ _ChapMS2 : 528 -> 532
~ _ascii2unicode : 92 -> 104
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 c293b220d9638c02f87ff5655ac6a6c6abd436a9ea69a862ff395879ce1f6b43 -> 7755fddfb87100c1f21abde8fc11afda57ac8234851592fa8c8e51fbfda0cef7
~ __plug_strdup : sha256 2660d09403ab8c53c802150192a2f048bca70b1bbdbbecc61c72ce504ceabc7f -> 01758b5b2d958aad6de8a65e87977c0684d71530bab3760216c884210c45c6cc
~ __plug_free_string : sha256 72bf4dd6e8c7ec70bc8124cdc996c36f9bce9e581e0f23e141f3350a134dee32 -> 146df4492f7475ecbc90154f0e373f5a4868f6fb37c6f4ff98a41d9d9a54b619
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 e7af234217fde0e0934d9cc95319a9c16c46071785aad77efcf2c62b04fcaa30 -> 236aa138e3efb4d45af769e585e7a6fb2bf41bfa282b1e734315b7bd76bb114b
~ __plug_get_password : 368 -> 360
~ __plug_challenge_prompt : sha256 462e260179b201066ee5ed0255169fe7132fce628e970cad2e31f8eea3c763c3 -> 8d46487ab0a66a070b09c691de716bb8c7a93bd30cd4b44cc529f6b7ce9743f4
~ __plug_get_realm : sha256 59c943c51ba7fd03ec5b1a348d7b8a8bf238138f8222d0597e8d98d4c3928832 -> 06e604b86ffe140b42b87479f35727207b63fdf2f0964c06b245a9d5c3064ad5
~ __plug_make_prompts : sha256 b82eb15ec014c29c1b455f21fc5156abdfec2dac8978f276bae26785af9b53ec -> 5c1015b6ba0e1c752ced9f608c2683cce01daa80e7bc21bfb92e482f4bc81c5c
~ __plug_decode : sha256 a84c2e8e1242cba3af00b7aca122ca4d4b7b55bc9fa0a4287fc35cc9d97809bf -> f6f5652592cddba243cf3cef9c1d427d3b004a653943fa5d698b36bbdf5dd338
~ __plug_parseuser : sha256 5a18e9d9178a25fd2c328c9a8537283829bcd2accabe706b57d51ae087d24f5a -> 54619e4bdd7b00a4a5897c8209d2f939348b9cf4b3def73920ce6ab7cb1298a2
~ _apsasl_des_set_odd_parity : sha256 3142a3e33ffdaf50bf680d5aca6d5088d39887d046dc35cbf9410874f871ca78 -> 7692b0b057209403e80e31b3ca5146ff05409d3cd6ff6119a1718c2243890040
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/mschapv2.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/mschapv2.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/mschapv2.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/mschapv2.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
