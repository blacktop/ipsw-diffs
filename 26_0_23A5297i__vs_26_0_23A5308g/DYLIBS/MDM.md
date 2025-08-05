## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-49.0.0.0.0
-  __TEXT.__text: 0x55ccc
+50.0.0.0.0
+  __TEXT.__text: 0x55d38
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__objc_methlist: 0x417c
   __TEXT.__const: 0x1a2
   __TEXT.__gcc_except_tab: 0x1110
   __TEXT.__cstring: 0x5592
-  __TEXT.__oslogstring: 0x6ca5
+  __TEXT.__oslogstring: 0x6cfa
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x68

   __TEXT.__unwind_info: 0x1210
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_classname: 0x6c4
-  __TEXT.__objc_methname: 0xeb1e
+  __TEXT.__objc_methname: 0xeb2b
   __TEXT.__objc_methtype: 0x1b90
-  __TEXT.__objc_stubs: 0xb980
+  __TEXT.__objc_stubs: 0xb9a0
   __DATA_CONST.__got: 0x11a8
   __DATA_CONST.__const: 0x1f10
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3490
+  __DATA_CONST.__objc_selrefs: 0x3498
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x68

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 9B6A3236-94E8-375D-8D2A-EC8C6A68DCFD
+  UUID: E9F6599F-98F2-3188-B1C8-7397073D1D99
   Functions: 1647
-  Symbols:   6658
-  CStrings:  4261
+  Symbols:   6659
+  CStrings:  4263
 
Symbols:
+ ___184-[MDMParser _performInstallApplicationRequestWithManifestURL:iTunesStoreIDObj:bundleId:flagsObj:attributes:configuration:manageChangeStr:purchaseMethodValue:personaID:completionBlock:]_block_invoke.1351
+ ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1200
+ ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1201
+ ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1496
+ ___68-[MDMParser _processRequest:accessRights:assertion:completionBlock:]_block_invoke.980
+ ___block_literal_global.1047
+ ___block_literal_global.1091
+ ___block_literal_global.1108
+ ___block_literal_global.1196
+ ___block_literal_global.1198
+ ___block_literal_global.1210
+ ___block_literal_global.1375
+ ___block_literal_global.1377
+ ___block_literal_global.1415
+ ___block_literal_global.1420
+ ___block_literal_global.1487
+ ___block_literal_global.945
+ ___block_literal_global.947
+ ___block_literal_global.949
+ ___block_literal_global.951
+ ___block_literal_global.953
+ ___block_literal_global.960
+ _kMDMSettingsURLProfilesUI
+ _objc_msgSend$evaluateNags
- ___184-[MDMParser _performInstallApplicationRequestWithManifestURL:iTunesStoreIDObj:bundleId:flagsObj:attributes:configuration:manageChangeStr:purchaseMethodValue:personaID:completionBlock:]_block_invoke.1348
- ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1197
- ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1198
- ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1493
- ___68-[MDMParser _processRequest:accessRights:assertion:completionBlock:]_block_invoke.977
- ___block_literal_global.1044
- ___block_literal_global.1088
- ___block_literal_global.1105
- ___block_literal_global.1193
- ___block_literal_global.1195
- ___block_literal_global.1207
- ___block_literal_global.1372
- ___block_literal_global.1374
- ___block_literal_global.1412
- ___block_literal_global.1417
- ___block_literal_global.1484
- ___block_literal_global.942
- ___block_literal_global.944
- ___block_literal_global.946
- ___block_literal_global.948
- ___block_literal_global.950
- ___block_literal_global.957
- _kMCSettingsURLProfilesOverview
Functions:
~ -[MDMMigrationManager stopNagging] : 236 -> 272
~ -[MDMServerCore initWithChannelType:] : 992 -> 1000
~ ___47-[MDMServerCore _memberQueueRRTSTimeoutReached]_block_invoke : 392 -> 456
CStrings:
+ "Skipping RRTS machinery because device hasn't been setup (still in Setup Assistant)!"
+ "evaluateNags"

```
