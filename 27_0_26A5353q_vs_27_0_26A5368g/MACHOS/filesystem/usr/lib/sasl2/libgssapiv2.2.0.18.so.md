## libgssapiv2.2.0.18.so

> `/usr/lib/sasl2/libgssapiv2.2.0.18.so`

```diff

-215.0.0.0.0
-  __TEXT.__text: 0x3ab8 sha256:728ca7f3238853b20ffb64a09e604614865dce0fb753acb478a13c50cbbe910b
+217.0.0.0.0
+  __TEXT.__text: 0x3a64 sha256:d3a9871b49ef3ac1c61b9279a48659e195184eb367d87675fa057dc14f29f371
   __TEXT.__const: 0x10 sha256:9722a7e22fcb78dd4278669ac01e407cd1bd0ab448a710a8ac03edb643a8408d
-  __TEXT.__cstring: 0x792 sha256:d0ccc869acd0f6a070e3818c03a1e267fb0d5694ccebbc71dbb6a2a01f794187
-  __TEXT.__unwind_info: 0xd8 sha256:bf720e03a826a86af83d7e558d1607c2e59be95cfd5328130dbb7317dfbe5b8a
+  __TEXT.__cstring: 0x792 sha256:f3aede19add8341ebf8949a42806b2412a0f1563280a30d407febc40bdb4687a
+  __TEXT.__unwind_info: 0xd8 sha256:a67c3f940553a43e1964932c38a066bfd7a21c86316d63b7f2e60f9846d12480
   __TEXT.__auth_stubs: 0x290 sha256:990a1cce8d9909eed5b058d524957351d30acf4afc2c4b2b6d8a02896050df05
   __DATA_CONST.__got: 0x28 sha256:9c21d953ae12611b43256b758b8c05e3b2e4b46791558f7e06a4963a3a526ae3
   __AUTH_CONST.__auth_got: 0x148 sha256:9ecc7f9b2ef5fda3f1ff0b759ca8b5d94e4459d3e78034ebe1208d6721a22dd4
-  __AUTH.__data: 0xc8 sha256:881b45479f59e490e1aad05aa3ed25925ab22bc8473d5660d73a03162fe9afbc
+  __AUTH.__data: 0xc8 sha256:cac065dce6322e1092a50e21dac19c12d9bf0deb7a80aa18413a28abe7ba72cb
   __DATA.__bss: 0x8 sha256:6eca5cc86a53c80d74e777fffd48ee46b98f06a8b448d18106af49ac0862b875
   - /System/Library/Frameworks/Kerberos.framework/Versions/A/Kerberos
   - /usr/lib/libSystem.B.dylib
-  UUID: F8CDEEB3-9FCF-3033-8F09-5C61E501309A
+  UUID: 9A9027AB-BD82-3D01-BA3E-B08F8E29EE70
   Functions: 36
   Symbols:   86
   CStrings:  37
Functions:
~ _gssapiv2_client_plug_init : sha256 f2efea616f367188c33c4b0545d88ac51b25d5cc8a70a464ba308d3c14cfa953 -> 41cb88955606177670e45365fdb6428edf6ef222cc38573a2f3cd48babadab3c
~ _gssapi_server_mech_new : sha256 cab745a657697d83f5974701f808bd5b3c5a18ede1732e60c0093db464d6add8 -> b4ceef3a0feadde9ecf98c0699c52e14a6c411ed05a7c27dc9b0bde7a39e5607
~ _gssapi_server_mech_step : sha256 174b2562aee2e0af010025fb84c70f46d79c79ac5fea2f6168cce28ef99e835c -> 5961239a0b9e759ee147a863698f52e87fa0c9cb5161a098e99b1ba277dffc8b
~ _gssapi_common_mech_dispose : sha256 3e1bacd4c5aa024888b510c31f1718da2768bbcd036aaee663b5f2dc52c55d6b -> 12501b8ea2fa6dc1ca6407c7c5cb40e14626b9e8557f3f9430fca2ba15dcb72e
~ _sasl_gss_seterror_ : 800 -> 796
~ _sasl_gss_free_context_contents : sha256 607a6849b4fa0db2ac1ba8d35512278eee797faacfd9b9323642026704cea66f -> bdc01f1d6dabda22e8a5feba023b6c8dd0a1b7d31587bba103bf5cf92e3b4494
~ _gssapi_decode : sha256 e12e7825dea96fa0af752f82fa78e92c0f4085d3ec077f67d4256fe6f3af080b -> eba8b92f8e8d11c5d0af92b16ea462647e70142421182cf5778dfe413b8a52fb
~ _sasl_gss_encode : sha256 995f5ae32fc04620faf01a4b892f37c3d7e7fe021aed10393631a699c36da4ba -> 022818dc02c2d81c5997562ef6decdbe35284880179c6c87cd86c799f476055a
~ _gssapi_decode_packet : sha256 69e2fa50428df300d715a058a4cf8c8d30448dc0fbb02f115fa94be907c07fa4 -> 29b97a2ed63d5b796ac779526dd46ed185e42d1db7ae063caee49db8933c44a2
~ _gssapi_client_mech_new : sha256 7ee32150216c40c3218dea3d2479a8be790c9c429c846f85ff33734b45c4134b -> e7576b7e768b6d891d4bb7a82e9f77074c4a432e5972eab3e47420e4953412f2
~ _gssapi_client_mech_step : 3900 -> 3792
~ _sasl_server_plug_init : sha256 f997e65b9632d21f3a64a32f4545081736b184e313d2f57e6409fe097656adfe -> 1d599bc53154d5859bd2e3e08368b3a31de0ffbbde05d678e94205783c8db8a4
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 5efe114027c1a17dc5cc49e780d98e4cd44bf7fd967ea2694dcbdd684915e2f3 -> 6aa355c0cbe0b1aa7d28829f917c726e7f4c395ee533f32e5caf641143c16b68
~ __plug_strdup : sha256 8b74219bdd92fc83ce8971a08cfdd97690a8ec1528db1c78a6f356b303f01d10 -> edeb71f5dc4c27a325230d35d5ee799bb8fee1fd4aab4029d8b4e6720e149f2f
~ __plug_free_string : sha256 38951b1bf67e029c7971dc8d8c1943075ef9393946fe5ee5eae5bbb261c3ebfe -> ab3ae78d77441ce529fe73ba28b3be802c054b9dba323024134a25c00c8e9ec6
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 23cf166298246e5b40185c895d6e6e06121d6fb6918cefcbd3388ac821beca47 -> 83f981b130cfe4687a3d0b9017224bf50399f397cc8d721cf24143889a9e2257
~ __plug_get_password : 372 -> 364
~ __plug_challenge_prompt : sha256 df83d034c4e394cf44f67880ae9cdbf311531ebed23361033b4d85628adfedec -> ec0cfc0deb02ec855c01f1d8d0a023e81b95e060ab6239c069d5610bf2a4f31f
~ __plug_get_realm : sha256 42efaaef195a13c4786590da484292dfad19d0affa09c290a4f327d492446cb4 -> 88c810a319be0d652a0928dd21ce01ccf5ddb0c2b88e47cbb24072ba66b984e8
~ __plug_make_prompts : sha256 5f9d29e6f51c44cb9bb3ecdfb48fb535d276cd69c13bf7bfdb33ab6c55ee882d -> 3a1e2fadee1081e9d80ca0f31e6e9afabf82e1f8002d4be61b140fca50126458
~ __plug_decode : sha256 8450da998baf3fa544c87b86fbd1d0c326b33418d724ad38302a129a37cf25e9 -> fe0e1ab94b02fec9e08a68eee1565d5493b1a4f94111fe5a1b1cc32a2384d08e
~ __plug_parseuser : sha256 064b69d06e90aa515bd6eae0e393dfff514eed8268182936294450e461e62ed5 -> bcf3000c52473bc1af99d46bf38db4b0777cf770f33d51cf38c96eae6913cd7b
~ __plug_make_fulluser : sha256 a89d18a14ad432515738183001878a487aecce6adabb72ff0e89572a1f1d98cb -> 67198aa3a1052721e9c1348d78c306531c1aeb5b24e5d47bc2e32c2e5bbfbeaa
~ __plug_get_error_message : sha256 0dfda8c1105fb5fbc80659fa071803b59744452d832d5536b8a5198f4ebde2db -> 83bee021a25d1ae363d19b94270bb926f94c088edfe1b4c1251fc5db44ebdef6
~ __plug_snprintf_os_info : sha256 6110f2bffb80e84fbd9427981824b2895d9bd7ccd30f1acf22bd87224af88d7e -> 4576df469249079eb07bf36831d7b0a371c47d7962d7376dc74d17fc8e189847
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugBdM_YJSeaNF8WiMK84y08sXlOaxK9gu1k/Library/Caches/com.apple.xbs/TemporaryDirectory.RGKFME/Sources/passwordserver_saslkerberos/cyrus_sasl/plugins/gssapi.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugBdM_YJSeaNF8WiMK84y08sXlOaxK9gu1k/Library/Caches/com.apple.xbs/TemporaryDirectory.RGKFME/Sources/passwordserver_saslkerberos/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugBdM_YJSeaNF8WiMK84y08sXlOaxK9gu1k/Library/Caches/com.apple.xbs/TemporaryDirectory.RGKFME/Sources/passwordserver_saslkerberos/cyrus_sasl/plugins/gssapi.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugBdM_YJSeaNF8WiMK84y08sXlOaxK9gu1k/Library/Caches/com.apple.xbs/TemporaryDirectory.RGKFME/Sources/passwordserver_saslkerberos/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA1eg9KKydwxFp6mZXHXV992cDZRuf1Mtg/Library/Caches/com.apple.xbs/TemporaryDirectory.NLXfwK/Sources/passwordserver_saslkerberos/cyrus_sasl/plugins/gssapi.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA1eg9KKydwxFp6mZXHXV992cDZRuf1Mtg/Library/Caches/com.apple.xbs/TemporaryDirectory.NLXfwK/Sources/passwordserver_saslkerberos/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA1eg9KKydwxFp6mZXHXV992cDZRuf1Mtg/Library/Caches/com.apple.xbs/TemporaryDirectory.NLXfwK/Sources/passwordserver_saslkerberos/cyrus_sasl/plugins/gssapi.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA1eg9KKydwxFp6mZXHXV992cDZRuf1Mtg/Library/Caches/com.apple.xbs/TemporaryDirectory.NLXfwK/Sources/passwordserver_saslkerberos/cyrus_sasl/plugins/plugin_common.c near line %d"

```
