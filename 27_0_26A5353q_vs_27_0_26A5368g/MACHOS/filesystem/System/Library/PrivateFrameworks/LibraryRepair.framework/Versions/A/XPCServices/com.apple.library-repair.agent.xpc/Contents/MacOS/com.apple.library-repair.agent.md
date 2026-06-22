## com.apple.library-repair.agent

> `/System/Library/PrivateFrameworks/LibraryRepair.framework/Versions/A/XPCServices/com.apple.library-repair.agent.xpc/Contents/MacOS/com.apple.library-repair.agent`

```diff

 21.0.0.0.0
-  __TEXT.__text: 0x2718 sha256:84c1e1c15f7a2da9580ecef86d2d7b2ba733c395149bf7ab142582554b70f700
+  __TEXT.__text: 0x272c sha256:477c86940d62d0e5867c6f92f01d7df73a572ee8f58ebc21e46f544a5f52b9b0
   __TEXT.__auth_stubs: 0x650 sha256:8c73634b4cda25f03280e9156306580d14023cfb34a0bbacca59116bbe4e0aca
   __TEXT.__objc_stubs: 0x2e0 sha256:3b2e0a7bb144ca798846178c879516cf23078c2f576c93211457252af1ae55db
   __TEXT.__const: 0x48 sha256:27e58dd0ef129a1e94da39319dbd50f74bf184e68667862dab846f6f0f0745e9
   __TEXT.__cstring: 0x12bf sha256:b781e75ffe7c286a0e520ffc8bc29ad9295ab9c7cfc47f364b8c34c8abe875b1
   __TEXT.__objc_methname: 0x1b7 sha256:de71ca04f0cda9d7ac350095317f64f578858707a2dc592c1701afe36557bbdd
-  __TEXT.__unwind_info: 0x90 sha256:383535c4b85f9b82306034a23389d91917567024c3ed9a8d0b27e61c80e619b2
-  __DATA_CONST.__const: 0xa8 sha256:b10c56912d2b92edd6bb30fc3e7b35250763c6c20d56e6b8bb9f85f1a1edb18e
-  __DATA_CONST.__cfstring: 0x240 sha256:556b801365c2cbe67ab4f7b30a7f0f43121279f3ccb3495f56ca08e76daf30ff
+  __TEXT.__unwind_info: 0x90 sha256:32f328a25a07ff5b9dd7830c014aa7e4fc4df85f872815acbb3d0e50c6b2f469
+  __DATA_CONST.__const: 0xa8 sha256:55e7278ab1324566a1a4f96235948d95df1e9a69a1562622befe55d27501dad9
+  __DATA_CONST.__cfstring: 0x240 sha256:9e0bf49ea767001d8a7d3b99d152c92ba207bab75b639fc9a4d4db521dd80d89
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
   __DATA_CONST.__auth_got: 0x330 sha256:1f9c90a2ba42e3a3d750f38a64ba9c1e1a56609eb474327abb2ca28b1496b259
   __DATA_CONST.__got: 0xa0 sha256:5871eb7053721cf4a7f296908ee260057f1a4b04a991e84cbd8d732e0cbbc041
-  __DATA.__objc_selrefs: 0xb8 sha256:cb02b7719f6bf0497ff809ccff6a4cfb0c0fbe2045506148ae50a67058e81b1b
+  __DATA.__objc_selrefs: 0xb8 sha256:4f566158b9a5705ec70e2693853a033b1118e74a930a17972f561a6abe9f5e8b
   __DATA.__bss: 0x9 sha256:3e7077fd2f66d689e0cee6a7cf5b37bf2dca7c979af356d0a31cbc5c85605c7d
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/ConfigurationProfiles.framework/Versions/A/ConfigurationProfiles
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 763BCE35-CABA-3A34-95F0-53DAE7E8C57A
+  UUID: B0FA820C-0646-3D93-A097-7C17FE3C1487
   Functions: 16
   Symbols:   134
   CStrings:  159
Functions:
~ _main : sha256 f20ff13906828f281abe4d299cb1c65c0aff08b7c49de792239d586efbe16349 -> bac11283967cc76f1298e3a9740031b55fbd31fcfc04f10d797474fea8d51b01
~ sub_100000978 : 1728 -> 1724
~ sub_100001038 -> sub_100001034 : sha256 279a354b590f843ac8b3a94c1b215cee297443d266066553c50e034ab8862ad1 -> 2521eacf1c87ccc101c373071a192ffbc95a23c4a90df9e670830f9cc63d4383
~ sub_100001084 -> sub_100001080 : 2260 -> 2284
~ sub_100001958 -> sub_10000196c : sha256 eb60fa25947f0fca160110a85350ba8f01ab3f0a4b63ae34eb46e128a2592704 -> 5328fd870d2cbac3b20ce215e2bb58a22cd295fcccbc7bbb3ca67c70e0463da4
~ sub_100001a4c -> sub_100001a60 : sha256 f2f6b56c047cc1373bb4c705c26e6459d6d62277d6a6be89ec6a7304c5b390f9 -> 1aae3aeb3153a2e79d6dc5b3c1cf0f51dbf245cca86dd4433d1aac3d6095075a
~ sub_100001b14 -> sub_100001b28 : sha256 86a2f33cacf8625135151691c93b2b5e6ee93f6b62a09301609645d69dd664cb -> 5ef438d0fdcde6813abb4aa64b24414b8b5fbe6dfba922f42bf6093582a832b6
~ sub_100001c7c -> sub_100001c90 : sha256 22275bbd3b5883e8060394da5382d1c6f057be77d7362325aaa18bae2630235e -> 3b6b891189da7f07a3b891ffb1f21d0ee7dda0dcbdbda30faf5883ff3dea133d
~ sub_100002c84 -> sub_100002c98 : sha256 f13b0f9809b7097e11ba30d99b2561019c6db9751a247b79d3c0f9522c7af25d -> 7a318bda5de40db6f871d034c621e27f115faa469e4f68d1af989916c022dad3
~ sub_100002d9c -> sub_100002db0 : sha256 7d9d526601a0432cb4574929ab86a86e3a7b59b47277c04a4ee3f567b0c141a3 -> b28cc747c6f2537a01be8a123485b96d51ef5ea7b954b5d769a7dae25822426a
~ sub_100002e38 -> sub_100002e4c : sha256 ed06d704084753dcdd7a41f8663d33a971d9ae6e0682d384ee2d90a5c2a14c92 -> f0f893a427251a9908d61ae8ff82ea5012939eccc5bf4b2936b0454afc431496
~ sub_100002f8c -> sub_100002fa0 : sha256 f1b30c7b4dc12f4c8aae1e935a124e965b32378530747edcb5e01984ba4245f0 -> 0b04c621ffcd7573d01de98abdb8cb098d15f204b19cbf779cd55b5b6cad1327
~ sub_100003024 -> sub_100003038 : sha256 96c259ab732187502eabcead835afa447116f8e7f52da4d4b4540ff9d4316376 -> ca5a57310419ec6faae07d9f0290bcd28892f013cd8055fc9fe879bb43ed2c73

```
