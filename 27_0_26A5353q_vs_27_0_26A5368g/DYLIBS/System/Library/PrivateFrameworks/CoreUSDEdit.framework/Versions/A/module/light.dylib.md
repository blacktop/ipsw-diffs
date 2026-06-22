## light.dylib

> `/System/Library/PrivateFrameworks/CoreUSDEdit.framework/Versions/A/module/light.dylib`

```diff

-28.0.0.501.1
-  __TEXT.__text: 0x14bc sha256:85718772ae7e8cb4cb55de84810c8e75927fd18c09c107e1c45ac78fb8bce8ae
-  __TEXT.__gcc_except_tab: 0x3c sha256:36e68d67b4d18c88474503dbc16fb325ff26fc7cbbfcec63b16835d43dbfe45e
+28.0.2.0.5
+  __TEXT.__text: 0x1558 sha256:fdfc140d420a520ef6ab4eca3f58da732b8642272fa5d492a02e93ea3bb4f417
+  __TEXT.__gcc_except_tab: 0x48 sha256:c45412b6ebea68dd7bf4bc198befb4a2fa33df8899c6ec1cf76dd4f7b426a408
   __TEXT.__const: 0xeb sha256:7aadb332a07a3b427b372ebd971f2d14ff06a68f9ae849096b189c82b5d23c2f
   __TEXT.__cstring: 0x79b sha256:822812181457622ebf2258efac3e41f7e90ea12f5c57619534854680f89f1a81
-  __TEXT.__unwind_info: 0xc0 sha256:0cf5ae38af56cad43c48d6b307dd393dc076896791b780d978448b32ce01e279
+  __TEXT.__unwind_info: 0xc0 sha256:25f1ad77bd05bcb6b45f86548428cfe3213afd626f1ff5f14115d799bbceeab0
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x138 sha256:e532215ca797e4e69cb74afdfffaa944c19e35507179c1c1e2dd84b410d4889d
-  __AUTH_CONST.__weak_auth_got: 0x20 sha256:b7a04fda26841a0040c3791c7f7affdc0629031506fbb84d682fccd222e021f0
+  __DATA_CONST.__weak_got: 0x10 sha256:c675a8266f004da31cfe0663300a1b3a4f53f961dbff69b6db326e0ae20d45c6
+  __AUTH_CONST.__const: 0x138 sha256:b4611a4515a01d946211fd6eefc76f38c39c8a365fa58de81fb325b6b47e5c3e
+  __AUTH_CONST.__weak_auth_got: 0x20 sha256:396e67293ba6b13027ef3965f36dc8d7505225f73159bf94255b9e4c198352ac
   __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0xd0 sha256:46f531b7ea0428fbf2c3ca2b60e8dc33d6bbfa000e0fd1b489c5e39140a47006
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/usd/libusd_ms.dylib
-  UUID: 434C4E27-3C55-3B1D-B877-F546CE47A39B
+  UUID: 542CB89C-0940-3A25-BAB1-D0E82195570D
   Functions: 18
-  Symbols:   73
+  Symbols:   78
   CStrings:  33
 
Symbols:
+ __ZGVZN14CoreLogHandler12main_handlerEvE18s_main_log_handler
+ __ZN14CoreLogHandlerC1Ev
+ __ZZN14CoreLogHandler12main_handlerEvE18s_main_log_handler
+ ___cxa_guard_abort
+ ___cxa_guard_acquire
+ ___cxa_guard_release
- __ZN14CoreLogHandler18s_main_log_handlerE
Functions:
~ _on_register_module : sha256 5f40ed087d628efce2f7cc84e120bd888c92280505243094a59c2c8f69da1ec0 -> 1e23fb94d2da6a92553019dfcdb8e3b61b6441d90bb6e20ff520aabd7c147ccb
~ __ZL10create_cmaPK7CtxEval : sha256 bae3b2fdd184368f82da4a4ca0010f6168baa559595a8301e5bc1f2ae9051f76 -> 1cbd4c70a47304953c0872b253c821880144b4f1434d501c0b6451289c0ae69a
~ __ZN22_ModuleLightCallbacks_14declare_moduleER8OfObjectR15OfObjectFactory : sha256 d501376c65dbf45a4086631c22b0a445fdb0e376d802104a6d7d7bddfdb278e6 -> 4d0da6ec11a7fcc1ae5b3b619eca0d5fa203321a7c33ecbe4e1bf611390989c2
~ __ZN22_ModuleLightCallbacks_19on_attribute_changeER8OfObjectRK6OfAttrRiRKi : 148 -> 144
~ __ZN22_ModuleLightCallbacks_8paint_glER8OfObjectR10GlUtilsCtx : 276 -> 436
~ __ZN13CoreLogStreamD1Ev : sha256 23c33195fe338ca9f53c814306742e723959a52b535e80fadfa0ef22ca43e157 -> 5c44834b75f975084fed688a44f380c44a6c5681d139889162cb5e0cfba39f3a
~ __ZN22_ModuleLightCallbacks_D1Ev : sha256 d6691792da7742aefa316ffe8b3d7cde15b1bc7f1e1a70c804b2799ec4a63444 -> 1a7510f4d23287a5531fa93521601c46e844168260e118856a11315268b1f58c
~ __ZN22_ModuleLightCallbacks_D0Ev : sha256 327a484846c837cd3bdd40d30be926d62dd2b189cee1004dc9096d5f51d2da52 -> 7cd57528affb1092871052685ead90ff9d27273bd25bf09715e952a929782d59
~ __ZN24ModuleSceneItemCallbacks14init_callbacksER16OfClassCallbacks : sha256 3c57a570697867d547b0e0118b0f14ab3f8c985dd4fff543a00660bad31fbf1c -> 991fdf4a130f7773cb9db5b556f892a9c279ca6f203d7be3f87e5dec48517a36
~ __ZN8CmaLightD1Ev : sha256 98a44ad6a4ea40a39f79addf0d73b6f4f4a459d52315df3500ee02060e7cd6a4 -> 048d1752f630b7ff9aad633658518c6076802bf332d9a0a5e15001793689141d
~ __ZN8CmaLightD0Ev : sha256 e17fb9e65427e6b82f2785aca408e68cfafb5a650992559926bc040065ffd790 -> 312c7c2f50131b27b539701d07458feccd5ef7d67e40dd2adbfcebcfd273ebc1
~ __ZNK9ModuleCma14get_class_infoEv : sha256 fe0596366326ff031e8848e59326b56b8a1ccf2e2844b76b97899af14d94ba2d -> 0c4d77022d76955c5b3adff54be35aa057105aa14b3e738f1b806ec0e9d2e533
~ __ZN8CmaLight21sync_attribute_valuesERK8OfObject : sha256 80f68d62dd9b2dd7a5f3b94ee103eccd3af3ca671b52c9dd3b717e50a2b9e02b -> e3e7866103adaade917e4ba2364511b7412f0ed2f170c81c05c0bc613ed184ce
~ __ZN13CoreLogStreamD0Ev : sha256 c90d14ecb359e0b1dcc4e4fbb456952011c16aa6c7c55b81d961d02ad41dc6e1 -> 7a2868843f0ad12c046ebd8b2e50d68388e488d5bb521d7662abe60e2871681a
~ __ZNK13CoreLogStream14get_class_infoEv : sha256 fd42cf23f45a6a8bb9d0ba55c5c8b786bff09532f3736271c6d4fa1123cbb276 -> b422b08d8fb05e9f334b561014814fcfb5e6631102e7a892d259f092ebdc5b21

```
