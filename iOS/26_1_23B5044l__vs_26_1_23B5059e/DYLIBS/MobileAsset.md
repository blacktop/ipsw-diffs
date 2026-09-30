## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-1837.40.40.0.0
-  __TEXT.__text: 0x84a68
+1837.40.63.0.0
+  __TEXT.__text: 0x84bd4
   __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x68d4
+  __TEXT.__objc_methlist: 0x68ec
   __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x11814
+  __TEXT.__cstring: 0x11865
   __TEXT.__oslogstring: 0xa612
   __TEXT.__gcc_except_tab: 0x13bc
   __TEXT.__unwind_info: 0x1bc8
   __TEXT.__objc_classname: 0x8ad
-  __TEXT.__objc_methname: 0x16fc2
-  __TEXT.__objc_methtype: 0x1794
+  __TEXT.__objc_methname: 0x1702a
+  __TEXT.__objc_methtype: 0x17b2
   __TEXT.__objc_stubs: 0x8880
   __DATA_CONST.__got: 0x410
   __DATA_CONST.__const: 0x20d8

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3460
+  __DATA_CONST.__objc_selrefs: 0x3470
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x2f8
   __AUTH_CONST.__auth_got: 0x500
   __AUTH_CONST.__const: 0x700
-  __AUTH_CONST.__cfstring: 0xe4c0
+  __AUTH_CONST.__cfstring: 0xe500
   __AUTH_CONST.__objc_const: 0xa3e0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH.__objc_data: 0x9b0
   __DATA.__objc_ivar: 0x8d4
   __DATA.__data: 0x358
-  __DATA.__bss: 0x170
+  __DATA.__bss: 0x168
   __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x1f0
+  __DATA_DIRTY.__bss: 0x1f8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EC88E774-A42F-3848-BFA4-DD5B1493A428
-  Functions: 2891
-  Symbols:   8731
-  CStrings:  7302
+  UUID: EA9FBB8E-E1AA-388A-80C5-9753373072EB
+  Functions: 2893
+  Symbols:   8735
+  CStrings:  7309
 
Symbols:
+ -[MASecureManifestStorage _storeManifest:manifestType:infoPlist:stage:error:]
+ -[MASecureManifestStorage storeManifest:manifestType:infoPlist:stage:error:]
+ -[MASecureMobileAssetTypes supportsLoadableTrustCache:]
+ GCC_except_table8
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1136
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1137
+ ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1125
+ ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1162
+ ___77-[MASecureManifestStorage _storeManifest:manifestType:infoPlist:stage:error:]_block_invoke
+ ___77-[MASecureManifestStorage _storeManifest:manifestType:infoPlist:stage:error:]_block_invoke_2
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1131
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1132
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1135
+ ___Block_byref_object_copy_.1302
+ ___Block_byref_object_dispose_.1303
+ ____MAensureExtension_block_invoke.1309
+ ____MAsendDownloadAsset_block_invoke.1211
+ ____MAsendPMVCancelDownload_block_invoke.1229
+ ____MAsendPMVDownload_block_invoke.1217
+ ___block_literal_global.1120
+ ___block_literal_global.1124
+ ___block_literal_global.1128
+ ___block_literal_global.1130
+ ___block_literal_global.1131
+ ___block_literal_global.1169
+ ___block_literal_global.1175
+ ___block_literal_global.1185
+ ___block_literal_global.1190
+ ___block_literal_global.1214
+ ___block_literal_global.1378
+ ___block_literal_global.1383
+ ___block_literal_global.1385
+ ___block_literal_global.1409
+ ___block_literal_global.1432
+ ___block_literal_global.2824
+ ___block_literal_global.2826
+ ___block_literal_global.2828
+ ___block_literal_global.2830
+ _objc_msgSend$_storeManifest:manifestType:infoPlist:stage:error:
+ _objc_msgSend$storeManifest:manifestType:infoPlist:stage:completion:
- -[MASecureManifestStorage _storeManifest:infoPlist:stage:error:]
- GCC_except_table7
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1103
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1104
- ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1092
- ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1129
- ___64-[MASecureManifestStorage _storeManifest:infoPlist:stage:error:]_block_invoke
- ___64-[MASecureManifestStorage _storeManifest:infoPlist:stage:error:]_block_invoke_2
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1098
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1099
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1102
- ___Block_byref_object_copy_.1269
- ___Block_byref_object_dispose_.1270
- ____MAensureExtension_block_invoke.1276
- ____MAsendDownloadAsset_block_invoke.1178
- ____MAsendPMVCancelDownload_block_invoke.1196
- ____MAsendPMVDownload_block_invoke.1184
- ___block_literal_global.1087
- ___block_literal_global.1091
- ___block_literal_global.1095
- ___block_literal_global.1097
- ___block_literal_global.1098
- ___block_literal_global.1136
- ___block_literal_global.1142
- ___block_literal_global.1152
- ___block_literal_global.1157
- ___block_literal_global.1181
- ___block_literal_global.1342
- ___block_literal_global.1347
- ___block_literal_global.1349
- ___block_literal_global.1376
- ___block_literal_global.1399
- ___block_literal_global.2791
- ___block_literal_global.2793
- ___block_literal_global.2795
- ___block_literal_global.2797
- _objc_msgSend$_storeManifest:infoPlist:stage:error:
- _objc_msgSend$storeManifest:infoPlist:stage:completion:
CStrings:
+ "/.nofollow/private/var/run/MobileAssetStartupActivation.doneThisBoot"
+ "B52@0:8@16Q24@32B40^@44"
+ "SecureUnableToGraftDeviceLocked"
+ "SupportsLoadableTrustCache"
+ "[domain:%@|setID:%@|config:%ld|AIs:%ld(newer:%@[%ld])(latest:%@[%ld])|lookupRsp:%@(forConfig:%@)|user:%@|locks:%@|availErr:%@]"
+ "_storeManifest:manifestType:infoPlist:stage:error:"
+ "storeManifest:manifestType:infoPlist:stage:completion:"
+ "storeManifest:manifestType:infoPlist:stage:error:"
+ "supportsLoadableTrustCache:"
+ "v52@0:8@\"NSData\"16Q24@\"NSData\"32B40@?<v@?@\"NSError\">44"
+ "v52@0:8@16Q24@32B40@?44"
- "/private/var/run/MobileAssetStartupActivation.doneThisBoot"
- "B44@0:8@16@24B32^@36"
- "[domain:%@|setID:%@|config:%ld|AIs:%ld(newer:%@[%ld])(latest:%@[%ld])|lookupRsp:%@(forConfig:%@)|user:%@|locks:%@]"
- "_storeManifest:infoPlist:stage:error:"
- "storeManifest:infoPlist:stage:completion:"
- "v44@0:8@\"NSData\"16@\"NSData\"24B32@?<v@?@\"NSError\">36"

```
