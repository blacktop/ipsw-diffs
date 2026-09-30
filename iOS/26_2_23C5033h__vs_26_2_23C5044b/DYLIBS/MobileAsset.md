## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-1837.60.34.0.0
+1837.62.1.0.0
   __TEXT.__text: 0x84d34
   __TEXT.__auth_stubs: 0x9f0
   __TEXT.__objc_methlist: 0x68ec
-  __TEXT.__const: 0x2a8
+  __TEXT.__const: 0x298
   __TEXT.__cstring: 0x11933
   __TEXT.__oslogstring: 0xa67c
   __TEXT.__gcc_except_tab: 0x13bc

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F032F31-7E79-3CBF-A006-812B716B6EF0
+  UUID: D45E91CA-BE8F-3637-8C0D-EB17455FB949
   Functions: 2894
   Symbols:   8742
   CStrings:  7324
Symbols:
+ ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.947
+ ___119+[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke.415
+ ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.563
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1127
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1128
+ ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1116
+ ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1153
+ ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.917
+ ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.602
+ ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.595
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1122
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1123
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1126
+ ___Block_byref_object_copy_.1293
+ ___Block_byref_object_copy_.708
+ ___Block_byref_object_copy_.782
+ ___Block_byref_object_dispose_.1294
+ ___Block_byref_object_dispose_.709
+ ___Block_byref_object_dispose_.783
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
+ ___block_literal_global.438
+ ___block_literal_global.469
+ ___block_literal_global.475
+ ___block_literal_global.477
+ ___block_literal_global.537
+ ___block_literal_global.654
+ ___block_literal_global.699
+ ___block_literal_global.705
+ ___block_literal_global.707
+ ___block_literal_global.800
+ ___block_literal_global.805
+ ___block_literal_global.807
+ ___block_literal_global.987
+ ___block_literal_global.989
+ ___block_literal_global.991
+ ___block_literal_global.994
- ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.956
- ___119+[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke.424
- ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.572
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1136
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1137
- ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1125
- ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1162
- ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.926
- ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.611
- ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.604
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1131
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1132
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1135
- ___Block_byref_object_copy_.1302
- ___Block_byref_object_copy_.717
- ___Block_byref_object_copy_.791
- ___Block_byref_object_dispose_.1303
- ___Block_byref_object_dispose_.718
- ___Block_byref_object_dispose_.792
- ____MAensureExtension_block_invoke.1309
- ____MAsendDownloadAsset_block_invoke.1211
- ____MAsendPMVCancelDownload_block_invoke.1229
- ____MAsendPMVDownload_block_invoke.1217
- ___block_literal_global.1000
- ___block_literal_global.1003
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
- ___block_literal_global.1381
- ___block_literal_global.1386
- ___block_literal_global.1388
- ___block_literal_global.1409
- ___block_literal_global.1432
- ___block_literal_global.2824
- ___block_literal_global.2826
- ___block_literal_global.2828
- ___block_literal_global.2830
- ___block_literal_global.447
- ___block_literal_global.478
- ___block_literal_global.484
- ___block_literal_global.486
- ___block_literal_global.546
- ___block_literal_global.663
- ___block_literal_global.708
- ___block_literal_global.714
- ___block_literal_global.716
- ___block_literal_global.814
- ___block_literal_global.816
- ___block_literal_global.818
- ___block_literal_global.996
- ___block_literal_global.998

```
