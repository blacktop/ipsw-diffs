## smb_ntlmv2.so

> `/usr/lib/sasl2/smb_ntlmv2.so`

```diff

 195.0.0.0.0
-  __TEXT.__text: 0x2068 sha256:77bc250a8d5a806bd51dbac4d44f4e357058cd23485c134d23f2d0678c62bd76
+  __TEXT.__text: 0x206c sha256:145811d8b1cd1120c6884e53b491c0c35c2c398ce09f5dfe0a857ae3df3e2f20
   __TEXT.__auth_stubs: 0x190 sha256:6b8c4fba953657b1dfd4a21e3a42bbabe24be9dcd37a423ef6bbf8c3fd26d822
-  __TEXT.__cstring: 0x6fb sha256:d52c113ee1fb8a392b329a3993be45c01d59893674bcb20e38461d54dd45b0c4
-  __TEXT.__unwind_info: 0xc0 sha256:cc4ce5b66b354888c66ab1414ec306485c2dacf9246a674903630032541d7e70
-  __DATA_CONST.__const: 0x20 sha256:aa3e3820574f25aad05ad40dbcd3d9fb96036b43d3854f123f11b6c0fcbb930f
+  __TEXT.__cstring: 0x6fb sha256:813f18145494a8a87934c0b8f4f6b871b18dac515d41bace2bac6fa097c05433
+  __TEXT.__unwind_info: 0xc0 sha256:45dda830914736cbd3a3f6639b9f7450653937f02e68f54766ab1b1836b138a4
+  __DATA_CONST.__const: 0x20 sha256:31ac3add8cf92cb872e10f62104011b67f0eb5d60b43dc0f26619f1361913b53
   __DATA_CONST.__auth_got: 0xc8 sha256:8dbb4e970afcca96d9901fb3800c860238c5a83b07da1217b50bfdbc868c48ab
   __DATA_CONST.__got: 0x10 sha256:3a34334c69f400044263b55b4df4170e9fe388ebd9f9d85ee72fcfcfd519c490
-  __DATA.__data: 0x1c8 sha256:98d322e50d0804751968434beb26de2fd83e056fdeda49d095df569b3b077c11
+  __DATA.__data: 0x1c8 sha256:eca08c152564143a8a22e31c1c970d1a72cd4f9111ea289f72f5dc5b100e67d1
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/PasswordServer.framework/Versions/A/PasswordServer
   - /usr/lib/libSystem.B.dylib
-  UUID: 474B502B-2A43-3B93-8031-C188D2BC7ED9
+  UUID: C450C789-0FE8-3CC9-A19B-0487A527BFA9
   Functions: 27
   Symbols:   57
   CStrings:  37
Functions:
~ _CStringToUnicode : sha256 e29135cf2680c4dcf6ce432d574dee8207964a58bca88af8e3a235f85ac6d692 -> 06a4687a0da2ca897a0cd0d39ad8c83a7c6402c954aac862de76465a37a419c8
~ _apsasl_des_set_odd_parity : sha256 60fcf4efbc39017d071011cbf3f5305588259a86dd45a5116dc984ca6518a34f -> 37ffc6fcc74081e508568c009d404d4b92ddd4350bdf14303f9b77787140a111
~ _V2 : sha256 81dd1c52075ddb9e28b5940609f31ee69b01b361f11bd844cfa20a0805562699 -> 76bb21fd710673be7ad416913a0118494683d3fb48c7ecf245214062796237d9
~ _ntlmv2_server_plug_init : sha256 91dadc1feaf82f5ba818b58d50b5511f1a9473751e10d959c9542f57a38622dd -> f554100d0929af56ba88db23976a43bf31edfff970a51f2c05144835557e8dea
~ _ntlmv2_client_plug_init : sha256 af31aa2dca0e091e0d03700dd329f2aa9e201466c11224d2373786c1eb159527 -> 2ef8605c441f7922a5dea549051f6a24e1208f74053af86c1a050c98bfac70df
~ _ntlmv2_server_mech_new : sha256 4a63280896035db7c3781d29985caf8c85c2b91cc679ac0c409ab18e9984e975 -> 26ac37cfa6d12327faf5361b1b06b91d122bbcae116c79f1173dffff836536a7
~ _ntlmv2_server_mech_step : 1796 -> 1772
~ _ntlmv2_both_mech_dispose : sha256 5b84fa14d6a9bcc8b60f2c21dbd77aa146ea5f7484a50fae96ce7b73d2eaed4b -> e9cde8ebe91c1d8083314db01d98fecfe0414b2a374bf60c9137e4db0b57c61e
~ _ntlmv2_client_mech_new : sha256 5091d3ada6f6a3fe49d96ec860858d902a61c2fb02f220138d3fe99a9c2efc7c -> 932fe0f05ba996637437d185d42379ff6cc39ced846a64e71f6fbed713494a01
~ _ntlmv2_client_mech_step : sha256 a2074bfd71b7a37c2c28cc111fb59301b8c330760b1c37079d136975445e506e -> ba9fa0887f214f9905ec0a26521bc89ea23435e8630419fd3282fed225f18840
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 497fcb59e039fa2b76e1329918123158d5a284265e23dab668fa6bcf1a86e841 -> e90a4c4d57d6a87248fdcd5f9f092c7016268923962e151c5b9630900eb064ae
~ __plug_strdup : sha256 c2b77b656f9ed438883ebc85402bd617acb47e316fafb79cbcaa7e0fa945b6d7 -> dee5c6a20c3fc4f302e43560666e0555a2b05d16e14b71ce5249560869324b12
~ __plug_free_string : sha256 62d5c1a48843b8e4c26f0e61287270f0a546f0b42294e81aff1ecee486674050 -> c050f483f53934b9c3efd9fb2c9f7dfc7a72f2e37d2dd8c50d8ae04ba4f80cb4
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 b0cdee9ec31438ef46d183472df40ffe7db03603b54cff552dafc9053332b68e -> 646a9a8c065078e6d162f0b38b7969fc1ff809832a5d62a56703178f19e47c40
~ __plug_get_password : 368 -> 360
~ __plug_challenge_prompt : sha256 c4c42aca642da31468bc35c2977afcd0a65a1afa7e0a42cee46e4a9eb28a37c8 -> 0bd9a3406e39b0c4670989ffc83c0ae73cdc9d5ee8d1a71954191cce4072f3b7
~ __plug_get_realm : sha256 1375fb3d7691683c87627698256555ec819d9ad7d2778f5875fcef962d99404e -> c99aceb00748255430017609e32ccbf14d659af40726549db47a90d93eddaea2
~ __plug_make_prompts : sha256 5cbca47d947e3794e0849091582b440aba792fb8b94a7848c76e26840a2d3915 -> 06009c896ed091aac3bf95e59b1460d3e62cca1625cf7591ef6345cb266e045f
~ __plug_decode : sha256 cc816226740def22502c73a8b77c78f0f3940550461f11be5e96f0170597a3e3 -> 838c03631ca9ef326fb0c6bb6552e19c001a8833a122593a680f28889ffca50e
~ __plug_parseuser : sha256 68ae2b7e2aa84dd7d3fc9a5207ef4c6e2661cde50152815ef4c6edceed5f4204 -> 5da4597dc95710a7f69a0b69c30c24f2e825b620a4b667a5d8064ebf7fdbbcd7
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/ntlmv2.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/ntlmv2.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/ntlmv2.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/ntlmv2.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
