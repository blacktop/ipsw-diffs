## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-55.60.7.0.0
-  __TEXT.__text: 0x55c58
+55.80.2.0.0
+  __TEXT.__text: 0x55ca0
   __TEXT.__auth_stubs: 0xf50
   __TEXT.__objc_methlist: 0x4194
   __TEXT.__const: 0x1aa
   __TEXT.__gcc_except_tab: 0x1130
   __TEXT.__cstring: 0x55a2
-  __TEXT.__oslogstring: 0x6ccc
+  __TEXT.__oslogstring: 0x6cfb
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x68

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5C8E5655-F9A0-37A5-83C1-B1EB58FF4089
+  UUID: 7AE99C78-6B95-37B7-9DBC-DCF06E7ACE6B
   Functions: 1646
   Symbols:   6652
-  CStrings:  4264
+  CStrings:  4265
 
Symbols:
+ ___184-[MDMParser _performInstallApplicationRequestWithManifestURL:iTunesStoreIDObj:bundleId:flagsObj:attributes:configuration:manageChangeStr:purchaseMethodValue:personaID:completionBlock:]_block_invoke.1352
+ ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1201
+ ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1202
+ ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1497
+ ___68-[MDMParser _processRequest:accessRights:assertion:completionBlock:]_block_invoke.980
+ ___block_literal_global.1048
+ ___block_literal_global.1092
+ ___block_literal_global.1109
+ ___block_literal_global.1197
+ ___block_literal_global.1199
+ ___block_literal_global.1211
+ ___block_literal_global.1376
+ ___block_literal_global.1378
+ ___block_literal_global.1416
+ ___block_literal_global.1421
+ ___block_literal_global.1488
+ ___block_literal_global.945
+ ___block_literal_global.947
+ ___block_literal_global.949
+ ___block_literal_global.951
+ ___block_literal_global.953
- ___184-[MDMParser _performInstallApplicationRequestWithManifestURL:iTunesStoreIDObj:bundleId:flagsObj:attributes:configuration:manageChangeStr:purchaseMethodValue:personaID:completionBlock:]_block_invoke.1361
- ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1210
- ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1211
- ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1506
- ___68-[MDMParser _processRequest:accessRights:assertion:completionBlock:]_block_invoke.989
- ___block_literal_global.1057
- ___block_literal_global.1101
- ___block_literal_global.1118
- ___block_literal_global.1206
- ___block_literal_global.1208
- ___block_literal_global.1220
- ___block_literal_global.1385
- ___block_literal_global.1387
- ___block_literal_global.1425
- ___block_literal_global.1430
- ___block_literal_global.1497
- ___block_literal_global.954
- ___block_literal_global.956
- ___block_literal_global.958
- ___block_literal_global.962
- ___block_literal_global.969
Functions:
~ -[MDMServerCore migrateMDMWithContext:completion:] : 244 -> 316
CStrings:
+ "Device is on seed build. Skip the random delay"

```
