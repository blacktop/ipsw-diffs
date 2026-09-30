## apop.so

> `/usr/lib/sasl2/apop.so`

```diff

 195.0.0.0.0
-  __TEXT.__text: 0x1afc sha256:f71b20c5d63acd098d849b404869697805589f1a2a8e5a7a0897a59608880f63
-  __TEXT.__auth_stubs: 0xd0 sha256:19cc6ef31ab0fdc58813e6d7c110d470982a57c3b1b9ab407e4fbfb0a610e31e
-  __TEXT.__cstring: 0x5be sha256:d300786f2e779a669ce7bce915ce9cafffb7e3aa14a0e612e0759139f3b812df
-  __TEXT.__unwind_info: 0xb8 sha256:12093862e70164f29a4c321704d2b6459ee1888928192ce2f42948a71e685be9
+  __TEXT.__text: 0x1b28 sha256:e4c047f00bad7155e5d467cd75f798978d76e73b1d4eb8abee6f74ca951fda37
+  __TEXT.__auth_stubs: 0xd0 sha256:89fac914ad659d706673228b6f5b56d9b1a7010591b6da1ace002878fd36774a
+  __TEXT.__cstring: 0x5be sha256:d0ac4e8ddeca3d37df0acd6951c37101df14199d05470e97941bc4c8f18edae6
+  __TEXT.__unwind_info: 0xb8 sha256:c7bdb4f14d3280e1d8e70d6f0c747f82a795e364c94de596c973659c2233e408
   __DATA_CONST.__auth_got: 0x68 sha256:a42ed8a77a30481fc8fd0a630cfb1de6d66fcd27e534230be90ce4cdc76c60d5
   __DATA_CONST.__got: 0x8 sha256:a6df5982d56315f421efc4431b0ba029704a6764a61641c417f6ea13f888afdc
-  __DATA.__data: 0xc8 sha256:14ddfed0cc00d9bc516b7e7d42078945778b1c8c71178555e5db26b35bbcfad9
+  __DATA.__data: 0xc8 sha256:84b7230f4527ab42ed395ec14e978b7c332cd191034e7ecb784cda08b6a0d73f
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libsasl2.2.dylib
-  UUID: EA5004B5-B269-3C36-850B-7BDAB6059DD2
+  UUID: 09E0DB7B-C9CD-366B-A120-38CA337512B6
   Functions: 24
   Symbols:   40
   CStrings:  25
Functions:
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 2bf5e6c87007b92503324def7ebb15af39cfc4b56810b438f6a496102f643e13 -> 8937bd178e0cebec82ae8aa85f3bebc9424d26292a5f26344726957c3d724095
~ __plug_strdup : sha256 40df32b9e1b13e9038290898b412ca292cca566de968e2ff1cb048035f10f3fc -> 2de7c65cb4d1a5f0ee959faa3eb7049a5194587ac6719b0ad66b74830bd38867
~ __plug_free_string : sha256 7fb849cd225fdd90c442559179e1cdfa77eab4ac1170e0f822c92ab29fc7e250 -> b6d9366e2381a41c0fd580e6eb9faf5842e8a65345dd801168c3f93e860b35c9
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 cd9353cc48e9a55f195a60b9f132fb76227d31c252c4d705addabd702af28bdc -> 45039600adcbb1e3db6e2633b8c9ad17ab63cc6d0560ef910f75f5ff52754869
~ __plug_get_password : 368 -> 360
~ __plug_challenge_prompt : sha256 7fc3b423949504b60db031e1f119581a8a371071ce1fc38db4a64c9c9f4f0845 -> 5a3ea71ca02af2d78b7cd5dcc32dfb0d2e441fad7dc7456bb0c9f7727208e7ee
~ __plug_get_realm : sha256 847a868c7e939c5a0427e121f00a0a41f1e84fb0a5fe8c2d0e27ac58c8a4b07d -> 98124363623347a80005cd237529789c1573401497610463cd6064faf7d252b0
~ __plug_make_prompts : sha256 475b61cd0e3f7236785f5874159a0fbf76b32f9560c3a41a8b175cc4e412277c -> 5baccaa18ba7d52b8aeb9a7b8b0e71523ac0604ae58e0f230876e50485c31dad
~ __plug_decode : sha256 c737193eb87b3d5cedcab69081496587696c2e41da7a18315eff8d8c45dba926 -> 0ecc9fa7960d1ae48548c792fc9cd727cc084fca69086924243985f4069ffded
~ __plug_parseuser : sha256 1ae239665d62cae9168725bda39182669e2a7a93f5e73837c8d1f2b160214444 -> e9268cac82be5bf722196c24d79090dceb53339673d1e397eedabe28c6be6c82
~ _apop_server_plug_init : sha256 85f44c5f47de5312ba31d067b73e5400a802bcb64faa860fce7d5d6f56ed2d3a -> 2226f05f913fb57abf9daa1604554d4f449c43d777afbc11c9bb1aa3bbda11d1
~ _apop_client_plug_init : sha256 4c6e8d67f8f8fc2540ea7f5732bed08a08f77f7271f9fdf850993607ca3108cc -> e68b4ee568ec726cc51d03b83e85de2e43a1a69c71795ae4a8ffb1b75009749a
~ _apop_server_mech_new : sha256 e9328e3041e600cd98559e484d17b1a87ae3c0c022a9d8ee242aa4aeca0cb07c -> 7fe3621091eabe16bef8c78c438d8c18b24b2f87e4ff071417af852548c0b7c6
~ _apop_server_mech_step : 912 -> 928
~ _apop_both_mech_dispose : sha256 fb58b06bc033d0bae2023290e7b0cb27071ccdecb8181a8dfef1faa0f0cf7120 -> f7da604c1f7e4891b37eaed412c598bc0c1010e413592cd09e5a6a4a20f143c6
~ _apop_client_mech_new : sha256 e2426e946ddc4e9d554b4d2a8adb59c0156937a78e9479fd13fcd46fe8200119 -> 5ead3c13f4bfc355f7fe712674d37d0c7210698465879eaf3426ace25d6dde34
~ _apop_client_mech_step : sha256 d3f81fb2179bc2bbded79f85a9a037c5d6b9fe9700d301f3c16324a9fde41067 -> 8d195cd5be847d9459df17e1919cfb1f2ef19aa4c3411766f78af15d0d63be7b
~ _sasl_client_plug_init : sha256 7c0faf0ec34595909351eba11d28d27a38593d30e183a3fcea95cee7665b1ad9 -> e8b6a7ca5eb234d218b33ed09560881a525d8ec1f9ca73b163f90db70ed6533d
~ _sasl_server_plug_init : sha256 b28a4abc85d787c1351e81132141949162bce22ffae6c21a03715ba3f4994471 -> e426a582d1199147c73eea0d9b2f5c0059dbda5467df0c6d193a89bfb36cfeb2
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/apop.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/apop.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/apop.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/apop.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
