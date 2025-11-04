## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1837.40.71.0.0
-  __TEXT.__text: 0x300de8
-  __TEXT.__auth_stubs: 0x2c90
+1837.60.20.0.0
+  __TEXT.__text: 0x300d28
+  __TEXT.__auth_stubs: 0x2ca0
   __TEXT.__objc_stubs: 0x24480
   __TEXT.__objc_methlist: 0x1130c
   __TEXT.__const: 0x7bd18
   __TEXT.__objc_methname: 0x41547
   __TEXT.__objc_classname: 0xf07
   __TEXT.__objc_methtype: 0x41d1
-  __TEXT.__cstring: 0x3d87b
-  __TEXT.__oslogstring: 0x55d87
-  __TEXT.__gcc_except_tab: 0xd980
+  __TEXT.__cstring: 0x3d88b
+  __TEXT.__oslogstring: 0x55d57
+  __TEXT.__gcc_except_tab: 0xd9a0
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x14cc
   __TEXT.__constg_swiftt: 0x18a8

   __TEXT.__swift5_capture: 0x30
   __TEXT.__unwind_info: 0x60d8
   __TEXT.__eh_frame: 0x346c
-  __DATA_CONST.__auth_got: 0x1658
+  __DATA_CONST.__auth_got: 0x1660
   __DATA_CONST.__got: 0x878
   __DATA_CONST.__auth_ptr: 0xac8
-  __DATA_CONST.__const: 0x9c58
+  __DATA_CONST.__const: 0x9c50
   __DATA_CONST.__cfstring: 0x2f6a0
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D0C9FC81-4681-37C9-90AB-82DBBC54FCAF
+  UUID: 30196F88-E677-33EA-AEE2-FF2520F4C22B
   Functions: 9440
-  Symbols:   17317
-  CStrings:  24553
+  Symbols:   17316
+  CStrings:  24552
 
Symbols:
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1216
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1262
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1331
+ ___MABrainStartupTransaction
+ __block_literal_global.1213
+ __block_literal_global.1215
+ __block_literal_global.1378
+ __handleCacheDeletePurgeCallbackForVolume_block_invoke.1162
+ __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1158
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1213
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1259
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1328
- __block_literal_global.1210
- __block_literal_global.1212
- __block_literal_global.1375
- __handleCacheDeletePurgeCallbackForVolume_block_invoke.1159
- __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1155
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit_$_MobileAssetKeyManager
Functions:
~ +[MADAutoAssetScheduler isAssetTypeAtAggressiveFrequency:] : 136 -> 156
~ _mobileassetd_main : 1852 -> 1956
~ +[MABAACertManager _checkIsSupported] : 732 -> 636
~ _cckeccak_squeeze : 288 -> 276
~ sub_28b1f0 -> sub_28b1c0 : 4608 -> 4588
~ sub_29c1cc -> sub_29c188 : 2052 -> 2024
~ sub_29cbec -> sub_29cb8c : 3580 -> 3500
~ sub_29d9e8 -> sub_29d938 : 3124 -> 3040
~ sub_29e61c -> sub_29e518 : 1908 -> 1904
~ _Shift : 360 -> 368
CStrings:
+ "LuckCSeed"
+ "Starting built-in MobileAsset brain built Oct 21 2025 17:00:04"
+ "Starting downloaded MobileAsset brain (version: %@) built Oct 21 2025 17:00:04"
+ "supports-startup-transaction"
- "LuckB"
- "MABAACertManager not supported with hactivation"
- "ShouldHactivate"
- "Starting built-in MobileAsset brain built Oct 22 2025 22:26:22"
- "Starting downloaded MobileAsset brain (version: %@) built Oct 22 2025 22:26:22"

```
