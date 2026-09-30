## Sharing

> `/System/Library/PrivateFrameworks/Sharing.framework/Sharing`

```diff

-2094.40.31.0.0
-  __TEXT.__text: 0x331424
+2094.40.71.0.0
+  __TEXT.__text: 0x331468
   __TEXT.__auth_stubs: 0x4cf0
   __TEXT.__objc_methlist: 0x14644
-  __TEXT.__const: 0x1ffe4
+  __TEXT.__const: 0x20014
   __TEXT.__cstring: 0x3bfe6
   __TEXT.__gcc_except_tab: 0x34f0
   __TEXT.__oslogstring: 0x9d6e

   __TEXT.__unwind_info: 0xd498
   __TEXT.__eh_frame: 0xcc70
   __TEXT.__objc_classname: 0x1edf
-  __TEXT.__objc_methname: 0x2d4ee
-  __TEXT.__objc_methtype: 0x5ec9
+  __TEXT.__objc_methname: 0x2d502
+  __TEXT.__objc_methtype: 0x5ecc
   __TEXT.__objc_stubs: 0x18b20
   __DATA_CONST.__got: 0x1218
-  __DATA_CONST.__const: 0x7658
+  __DATA_CONST.__const: 0x76a8
   __DATA_CONST.__objc_classlist: 0x880
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x3d8

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 080EC799-066F-369A-977D-C36DC1BC1146
+  UUID: 2F44C6C8-4811-3B20-AE52-7049BAAFEDAA
   Functions: 21644
-  Symbols:   38536
+  Symbols:   38538
   CStrings:  20160
 
Symbols:
+ -[SFAppleIDClient _altDSIDLookupWithEmails:phoneNumbers:fetchType:completion:]
+ -[SFAppleIDClient altDSIDLookupWithEmails:phoneNumbers:fetchType:completion:]
+ ___40-[SFDeviceAssetManager logNetworkStatus]_block_invoke.614
+ ___40-[SFDeviceAssetManager logNetworkStatus]_block_invoke.621
+ ___68-[SFDeviceAssetManager onqueue_updateMetaDataWithCompletionHandler:]_block_invoke.644
+ ___71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke.649
+ ___71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke.649.cold.1
+ ___71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke_2.650
+ ___77-[SFAppleIDClient altDSIDLookupWithEmails:phoneNumbers:fetchType:completion:]_block_invoke
+ ___78-[SFAppleIDClient _altDSIDLookupWithEmails:phoneNumbers:fetchType:completion:]_block_invoke
+ ___78-[SFAppleIDClient _altDSIDLookupWithEmails:phoneNumbers:fetchType:completion:]_block_invoke_2
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_literal_global.1347
+ ___block_literal_global.1360
+ ___block_literal_global.1377
+ ___block_literal_global.1382
+ ___block_literal_global.1389
+ ___block_literal_global.1392
+ ___block_literal_global.1396
+ ___block_literal_global.1413
+ ___block_literal_global.1421
+ ___block_literal_global.1426
+ ___block_literal_global.1431
+ ___block_literal_global.1434
+ ___block_literal_global.1437
+ ___block_literal_global.727
+ ___block_literal_global.731
+ ___block_literal_global.945
+ ___block_literal_global.953
+ _objc_msgSend$_altDSIDLookupWithEmails:phoneNumbers:fetchType:completion:
+ _objc_msgSend$altDSIDLookupWithEmails:phoneNumbers:fetchType:completion:
- -[SFAppleIDClient _altDSIDLookupWithEmails:phoneNumbers:completion:]
- -[SFAppleIDClient altDSIDLookupWithEmails:phoneNumbers:completion:]
- ___40-[SFDeviceAssetManager logNetworkStatus]_block_invoke.605
- ___40-[SFDeviceAssetManager logNetworkStatus]_block_invoke.612
- ___67-[SFAppleIDClient altDSIDLookupWithEmails:phoneNumbers:completion:]_block_invoke
- ___68-[SFAppleIDClient _altDSIDLookupWithEmails:phoneNumbers:completion:]_block_invoke
- ___68-[SFAppleIDClient _altDSIDLookupWithEmails:phoneNumbers:completion:]_block_invoke_2
- ___68-[SFDeviceAssetManager onqueue_updateMetaDataWithCompletionHandler:]_block_invoke.635
- ___71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke.640
- ___71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke.640.cold.1
- ___71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke_2.641
- ___block_literal_global.1338
- ___block_literal_global.1342
- ___block_literal_global.1346
- ___block_literal_global.1359
- ___block_literal_global.1380
- ___block_literal_global.1383
- ___block_literal_global.1387
- ___block_literal_global.1399
- ___block_literal_global.1404
- ___block_literal_global.1412
- ___block_literal_global.1422
- ___block_literal_global.1425
- ___block_literal_global.1428
- ___block_literal_global.718
- ___block_literal_global.722
- ___block_literal_global.936
- ___block_literal_global.940
- ___block_literal_global.944
- _objc_msgSend$_altDSIDLookupWithEmails:phoneNumbers:completion:
- _objc_msgSend$altDSIDLookupWithEmails:phoneNumbers:completion:
Functions:
~ -[SFAppleIDClient altDSIDLookupWithEmails:phoneNumbers:completion:] -> -[SFAppleIDClient altDSIDLookupWithEmails:phoneNumbers:fetchType:completion:] : 228 -> 244
~ ___67-[SFAppleIDClient altDSIDLookupWithEmails:phoneNumbers:completion:]_block_invoke -> ___77-[SFAppleIDClient altDSIDLookupWithEmails:phoneNumbers:fetchType:completion:]_block_invoke : 16 -> 20
~ -[SFAppleIDClient _altDSIDLookupWithEmails:phoneNumbers:completion:] -> -[SFAppleIDClient _altDSIDLookupWithEmails:phoneNumbers:fetchType:completion:] : 328 -> 344
~ ___swift_instantiateConcreteTypeFromMangledNameV2 : 72 -> 84
~ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2 : 72 -> 92
CStrings:
+ "_altDSIDLookupWithEmails:phoneNumbers:fetchType:completion:"
+ "altDSIDLookupWithEmails:phoneNumbers:fetchType:completion:"
+ "v48@0:8@\"NSArray\"16@\"NSArray\"24q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "_altDSIDLookupWithEmails:phoneNumbers:completion:"
- "altDSIDLookupWithEmails:phoneNumbers:completion:"
- "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"

```
