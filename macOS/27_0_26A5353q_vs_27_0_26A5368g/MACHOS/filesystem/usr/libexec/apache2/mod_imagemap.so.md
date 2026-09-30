## mod_imagemap.so

> `/usr/libexec/apache2/mod_imagemap.so`

```diff

-886.0.0.0.0
-  __TEXT.__text: 0x24b8 sha256:b8463aff44bcf31d73f076d63150212af55acc7605160b0e29c0ca55bc096081
+888.0.0.0.0
+  __TEXT.__text: 0x24a8 sha256:529901f2137ae91ea47ac4d44fc5b00060d74eb896d38044353a164783bb3712
   __TEXT.__auth_stubs: 0x1d0 sha256:37f40f382bb69563fa363230611dc98aa6e82822f0e48da517d30dd30d3cb5fc
-  __TEXT.__cstring: 0x463 sha256:627d510111e223fcfc4488b8a760a06d1c6b8973d92ff75781a375c6c4e2e29a
-  __TEXT.__unwind_info: 0x88 sha256:8bb770082a64029b77d3d126161903ee6e9172a2d1291417bcdd809449fea8dc
-  __DATA_CONST.__const: 0xa0 sha256:fb8e711d961bad46944a5719f1c5dcd57500d70d9e27a618cae0a3ed0ba3ab92
+  __TEXT.__cstring: 0x463 sha256:8455aa987930ad574ed4f9cc7657f95a8ef76d62d58ed511fd164391dee7826c
+  __TEXT.__unwind_info: 0x88 sha256:7fc234e70b32ba9535e212dbe5861eec5308d68a9f9481b16dba5a221f1904f4
+  __DATA_CONST.__const: 0xa0 sha256:fde6d3c72a5d2cc0c2d274246474207746b1f38198ebf3502e0130cdb6e4ce72
   __DATA_CONST.__auth_got: 0xe8 sha256:6b4d544a3a7550c1f30da98e76c6023afccf3db4b0b1473672cff6d7244e916e
   __DATA_CONST.__got: 0x8 sha256:d3dcad02fb108167f5c7d8f998f3a13063bc112dfa5e8da29a62da62a67fdba0
   __DATA_CONST.__auth_ptr: 0x8 sha256:559fb82325873e25df572d4bbc8cdf239be5ac699e08b957b04baaef1bf67032
-  __DATA.__data: 0x70 sha256:96c1e4940adc4196091ceb9fc3e84179ab67e776d096dcbca27bcf4e78fd3e41
+  __DATA.__data: 0x70 sha256:5b1d6c3d125d1fc67a531851f425f1b9de86b7e9243a58fba0c26676ade1287c
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: A68A2010-9434-3934-BF3F-253A61C23B84
+  UUID: 62BB575A-53FC-344B-B860-E2DB21DE1AD8
   Functions: 21
   Symbols:   55
   CStrings:  51
Functions:
~ _create_imap_dir_config : sha256 bac70e1b8a9127536a4ff7596bc2623a850ea4839d054d4129ae62b00aa3cdc5 -> e2b4085e8fd38673fd12f57e5e5254f6e6241a7434c555a615e279f9d0305980
~ _merge_imap_dir_configs : sha256 63d7934577f5206963d89eaf12c460ea88230dc723c837466da9855bea4eff96 -> d29b096475b1c2793b70337b6388a42a36788fa19381ef20cca303669327eb11
~ _register_hooks : sha256 29709d124f6867841d47c43613c1dd3085ecd94ffe94ad9403e44d0fd5479348 -> 32b70d9ff005ea34c71e565080ff965376cb6ca3d96d62a907b7b25c7f2d4f3d
~ _imap_handler : sha256 d458978f449bbafd256c1c71554aea1f3407ae10810c891d16a3486843ddb967 -> 56ef5f24e3cb7172571e2552e366ad3f4a18b657c6d38ad42f0f0da04df90a42
~ _imap_handler_internal : 2856 -> 2848
~ _imap_url : sha256 56a5698f5cf82c06260087583af3895fad3c6838cd5a4252bc8cce48dd46a15e -> a8cb2a43df25b3fe8487cda86cdf49753d439de48a7b3eef5c77f88c33a50a1c
~ _get_x_coord : sha256 d21612a51b8ad6e6c4ba71f66be6af0f17d19f4525fabaf22457da1bc3a62435 -> 82a5e389ec78f671ba7d3b2d6f46a84394d4604af61dfad88b022bbaf5628f15
~ _get_y_coord : sha256 381509eaae395d16566a3d397f971a44c3b01cfb60ac38d03b0dd780ed26546a -> d8cfd70d4525ce01d6b12b8c49844d50619439024d0c1947b78ae9b37e053e07
~ _menu_header : sha256 4821b894a48cfc0a6c6f6ddd8611ae6fcd92376577eee06688d4d415628dd20c -> 09d26854bb1a7d0e846c4a5b0284384d6a5c91bddb9c4e78ae712dc225cd7211
~ _menu_blank : sha256 25df90422d28fde6b25798b917c912af725de5df095a1a1e0a31a04ea1820a59 -> 42380bb126aa19ef774642dce0fe7155f9574d0ad18c86664dcef979ed300f1a
~ _menu_comment : sha256 f83d5896c365cd6ff962cdb8bc4ea4620d40ad09763adb3920e5265f09a4fb04 -> be7d52e083199682ce279fdc75ce544ef6389fc3be306c47da18be8a204cf0a3
~ _read_quoted : sha256 825939b36b96507a8f846586c055b02022f0af78856dd01ddaeb75ceeb8bf6e9 -> 826393952124d0bb7cce705db0e357055dbd8efed904731fe5986eb1d036322a
~ _menu_default : sha256 e77de98358d59083f983c6dfb3360a535f8e7282e0b58783a5ddb20a64f257f2 -> d7da65ce8bde9ae5c31bb1c77dfa7884ae7983a250860079e76dbd9de70a441d
~ _menu_directive : sha256 0e15f859a8568465094fbcc08ac76854f743428ea7d77313849aae96830d1010 -> 86ec57f31566cfe70150f909619fa9e8d3960ad42eba62bd3f4204471b5f1f24
~ _pointinpoly : 856 -> 848
~ _imap_reply : sha256 2f0c6cdde31f19b9c4c2470a52cba1a9d0fbc50085cc335959f37e5e6ead13a9 -> 23dfc59196ebf3622695638a6d233bc6d040d75b3a5a187c9060aa2d695fa563
~ _menu_footer : sha256 786cd9d27e5df69cb5372919e1f94bc5b9e7b124babae735e7a8f58c52cfdbcc -> 9bef0cb3a73ab496376466a5016eadb81e5576f4aef5fc160e896ae248d8c7f5
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRbjugDs63E_nh9LrKXIzNhaKOKGLV_zLQv5WSg/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/mappers/mod_imagemap.c"
- "/AppleInternal/Library/BuildRoots/4~CQCNugBXuVk5QyWQghtZ7Xdpnx7s5XYALnb8teQ/Library/Caches/com.apple.xbs/TemporaryDirectory.AuKlu0/Sources/apache/httpd/modules/mappers/mod_imagemap.c"

```
