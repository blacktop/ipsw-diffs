## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-1837.40.63.0.0
-  __TEXT.__text: 0x84bd4
+1837.40.71.0.0
+  __TEXT.__text: 0x84c44
   __TEXT.__auth_stubs: 0x9e0
   __TEXT.__objc_methlist: 0x68ec
   __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x11865
+  __TEXT.__cstring: 0x11912
   __TEXT.__oslogstring: 0xa612
   __TEXT.__gcc_except_tab: 0x13bc
   __TEXT.__unwind_info: 0x1bc8

   __TEXT.__objc_methtype: 0x17b2
   __TEXT.__objc_stubs: 0x8880
   __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x20d8
+  __DATA_CONST.__const: 0x20f8
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_arraydata: 0x2f8
   __AUTH_CONST.__auth_got: 0x500
   __AUTH_CONST.__const: 0x700
-  __AUTH_CONST.__cfstring: 0xe500
+  __AUTH_CONST.__cfstring: 0xe5c0
   __AUTH_CONST.__objc_const: 0xa3e0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA9FBB8E-E1AA-388A-80C5-9753373072EB
+  UUID: 0375CD50-168D-3E24-A0E1-0F63A217273E
   Functions: 2893
-  Symbols:   8735
-  CStrings:  7309
+  Symbols:   8739
+  CStrings:  7321
 
Symbols:
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1127
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1128
+ ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1116
+ ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1153
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1122
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1123
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1126
+ ___Block_byref_object_copy_.1293
+ ___Block_byref_object_dispose_.1294
+ ____MAensureExtension_block_invoke.1300
+ ____MAsendDownloadAsset_block_invoke.1202
+ ____MAsendPMVCancelDownload_block_invoke.1220
+ ____MAsendPMVDownload_block_invoke.1208
+ ___block_literal_global.1111
+ ___block_literal_global.1115
+ ___block_literal_global.1119
+ ___block_literal_global.1121
+ ___block_literal_global.1122
+ ___block_literal_global.1160
+ ___block_literal_global.1166
+ ___block_literal_global.1176
+ ___block_literal_global.1181
+ ___block_literal_global.1205
+ ___block_literal_global.1372
+ ___block_literal_global.1377
+ ___block_literal_global.1379
+ ___block_literal_global.1400
+ ___block_literal_global.1423
+ ___block_literal_global.2815
+ ___block_literal_global.2817
+ ___block_literal_global.2819
+ ___block_literal_global.2821
+ _kMobileAssetDisableAutomaticPushNotificationSubscription
+ _kMobileAssetEnforceProductionSigning
+ _kMobileAssetPushNotificationEnvironment
+ _kMobileAssetPushNotificationTestID
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1136
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1137
- ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1125
- ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1162
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1131
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1132
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1135
- ___Block_byref_object_copy_.1302
- ___Block_byref_object_dispose_.1303
- ____MAensureExtension_block_invoke.1309
- ____MAsendDownloadAsset_block_invoke.1211
- ____MAsendPMVCancelDownload_block_invoke.1229
- ____MAsendPMVDownload_block_invoke.1217
- ___block_literal_global.1120
- ___block_literal_global.1124
- ___block_literal_global.1128
- ___block_literal_global.1130
- ___block_literal_global.1131
- ___block_literal_global.1169
- ___block_literal_global.1175
- ___block_literal_global.1185
- ___block_literal_global.1190
- ___block_literal_global.1214
- ___block_literal_global.1378
- ___block_literal_global.1383
- ___block_literal_global.1385
- ___block_literal_global.1409
- ___block_literal_global.1432
- ___block_literal_global.2824
- ___block_literal_global.2826
- ___block_literal_global.2828
- ___block_literal_global.2830
Functions:
~ +[MAAutoAssetError stringForCode:] : 1292 -> 1316
~ ___48+[MAAutoAssetError mapAutoAssetErrorIndications]_block_invoke : 3924 -> 4020
~ -[ASAsset assetStateForStateString:] : 284 -> 276
CStrings:
+ "DisableAutomaticPushNotificationSubscription"
+ "EnforceProductionSigning"
+ "MAPushTestUniqueID"
+ "PushNotificationEnvironment"
+ "SetAtomicInstanceEliminated"
+ "SetAtomicInstanceIncomplete"

```
