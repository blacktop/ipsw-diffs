## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-1837.120.20.0.0
-  __TEXT.__text: 0x8e6a4
+1837.120.23.0.0
+  __TEXT.__text: 0x8e8d8
   __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_methlist: 0x6ae4
+  __TEXT.__objc_methlist: 0x6b14
   __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x12a43
+  __TEXT.__cstring: 0x12a91
   __TEXT.__oslogstring: 0xb0d8
   __TEXT.__gcc_except_tab: 0x1398
   __TEXT.__unwind_info: 0x1f28
   __TEXT.__objc_classname: 0x94b
-  __TEXT.__objc_methname: 0x178da
+  __TEXT.__objc_methname: 0x1797a
   __TEXT.__objc_methtype: 0x182e
-  __TEXT.__objc_stubs: 0x8b80
+  __TEXT.__objc_stubs: 0x8bc0
   __DATA_CONST.__got: 0x448
   __DATA_CONST.__const: 0x2490
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35a0
+  __DATA_CONST.__objc_selrefs: 0x35c0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x2f0
   __AUTH_CONST.__auth_got: 0x508
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0xf440
-  __AUTH_CONST.__objc_const: 0xa7a0
+  __AUTH_CONST.__cfstring: 0xf480
+  __AUTH_CONST.__objc_const: 0xa800
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x8f0
+  __DATA.__objc_ivar: 0x8f8
   __DATA.__data: 0x358
   __DATA.__bss: 0x1c0
   __DATA_DIRTY.__objc_data: 0xdc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 30F1155C-5C8F-37BE-B1B1-253F17AAC37E
-  Functions: 2982
-  Symbols:   9080
-  CStrings:  7644
+  UUID: 3411D895-A09D-3134-8EA7-FB9C9DA28CED
+  Functions: 2986
+  Symbols:   9092
+  CStrings:  7656
 
Symbols:
+ -[MAMsuDownloadOptions majorDelayPeriod]
+ -[MAMsuDownloadOptions minorDelayPeriod]
+ -[MAMsuDownloadOptions setMajorDelayPeriod:]
+ -[MAMsuDownloadOptions setMinorDelayPeriod:]
+ _OBJC_IVAR_$_MAMsuDownloadOptions._majorDelayPeriod
+ _OBJC_IVAR_$_MAMsuDownloadOptions._minorDelayPeriod
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1236
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1237
+ ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1224
+ ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1265
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1230
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1231
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1235
+ ___Block_byref_object_copy_.1399
+ ___Block_byref_object_dispose_.1400
+ ____MAPreferencesCopyValue_block_invoke.1531
+ ____MAensureExtension_block_invoke.1406
+ ____MAsendDownloadAsset_block_invoke.1310
+ ____MAsendPMVCancelDownload_block_invoke.1328
+ ____MAsendPMVDownload_block_invoke.1316
+ ___block_literal_global.1219
+ ___block_literal_global.1227
+ ___block_literal_global.1229
+ ___block_literal_global.1230
+ ___block_literal_global.1247
+ ___block_literal_global.1271
+ ___block_literal_global.1276
+ ___block_literal_global.1286
+ ___block_literal_global.1291
+ ___block_literal_global.1313
+ ___block_literal_global.1506
+ ___block_literal_global.1530
+ ___block_literal_global.1537
+ ___block_literal_global.1539
+ ___block_literal_global.1546
+ ___block_literal_global.1548
+ ___block_literal_global.1550
+ ___block_literal_global.1553
+ ___block_literal_global.2951
+ ___block_literal_global.2953
+ ___block_literal_global.2955
+ _objc_msgSend$majorDelayPeriod
+ _objc_msgSend$minorDelayPeriod
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1230
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1231
- ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1218
- ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1259
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1224
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1225
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1229
- ___Block_byref_object_copy_.1393
- ___Block_byref_object_dispose_.1394
- ____MAPreferencesCopyValue_block_invoke.1525
- ____MAensureExtension_block_invoke.1400
- ____MAsendDownloadAsset_block_invoke.1304
- ____MAsendPMVCancelDownload_block_invoke.1322
- ____MAsendPMVDownload_block_invoke.1310
- ___block_literal_global.1213
- ___block_literal_global.1217
- ___block_literal_global.1221
- ___block_literal_global.1224
- ___block_literal_global.1241
- ___block_literal_global.1259
- ___block_literal_global.1270
- ___block_literal_global.1280
- ___block_literal_global.1285
- ___block_literal_global.1307
- ___block_literal_global.1500
- ___block_literal_global.1524
- ___block_literal_global.1531
- ___block_literal_global.1533
- ___block_literal_global.1538
- ___block_literal_global.1540
- ___block_literal_global.1542
- ___block_literal_global.1547
- ___block_literal_global.2943
- ___block_literal_global.2945
- ___block_literal_global.2947
CStrings:
+ "%@  + MAMsuDownloadOptions reqProdVersion: %@ reqBuildVersion: %@ delayPeriod: %ld minorDelayPeriod: %ld majorDelayPeriod: %ld managedDevice: %d allowSameVersion: %d prereqBuild: %@ prereqVersion: %@ prereqReleaseType: %@ liveAssetAudienceUUID: %@ purpose: %@"
+ "MajorDelayPeriod"
+ "MinorDelayPeriod"
+ "Tq,N,V_majorDelayPeriod"
+ "Tq,N,V_minorDelayPeriod"
+ "_majorDelayPeriod"
+ "_minorDelayPeriod"
+ "majorDelayPeriod"
+ "minorDelayPeriod"
+ "setMajorDelayPeriod:"
+ "setMinorDelayPeriod:"
- "%@  + MAMsuDownloadOptions reqProdVersion: %@ reqBuildVersion: %@ delayPeriod: %ld managedDevice: %d allowSameVersion: %d prereqBuild: %@ prereqVersion: %@ prereqReleaseType: %@ liveAssetAudienceUUID: %@ purpose: %@"

```
