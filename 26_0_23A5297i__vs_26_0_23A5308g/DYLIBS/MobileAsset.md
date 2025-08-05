## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-1837.0.31.0.1
-  __TEXT.__text: 0x7feec
+1837.0.53.0.0
+  __TEXT.__text: 0x81c64
   __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x627c
-  __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x10379
+  __TEXT.__objc_methlist: 0x6294
+  __TEXT.__const: 0x298
+  __TEXT.__cstring: 0x1037b
   __TEXT.__oslogstring: 0xa457
   __TEXT.__gcc_except_tab: 0x13a4
-  __TEXT.__unwind_info: 0x1b80
+  __TEXT.__unwind_info: 0x1b88
   __TEXT.__objc_classname: 0x884
-  __TEXT.__objc_methname: 0x14d3f
+  __TEXT.__objc_methname: 0x14d99
   __TEXT.__objc_methtype: 0x1788
-  __TEXT.__objc_stubs: 0x8020
-  __DATA_CONST.__got: 0x400
+  __TEXT.__objc_stubs: 0x8080
+  __DATA_CONST.__got: 0x408
   __DATA_CONST.__const: 0x20a8
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3060
+  __DATA_CONST.__objc_selrefs: 0x3078
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x300
   __AUTH_CONST.__auth_got: 0x500
-  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__const: 0x700
   __AUTH_CONST.__cfstring: 0xda60
   __AUTH_CONST.__objc_const: 0x97d0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__objc_intobj: 0x270
   __AUTH.__objc_data: 0x960
   __DATA.__objc_ivar: 0x7e4
-  __DATA.__data: 0x360
-  __DATA.__bss: 0x190
+  __DATA.__data: 0x358
+  __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0xdc0
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x1c8
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x1f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5DB6D5A9-CC4E-3038-A582-511FBDED0058
-  Functions: 2750
-  Symbols:   8307
-  CStrings:  6878
+  UUID: 7AD4E267-AD89-3EB5-A195-33411BB3A5AF
+  Functions: 2755
+  Symbols:   8323
+  CStrings:  6882
 
Symbols:
+ +[MAAutoAssetError mapAutoAssetErrorIndications]
+ +[MAAutoAssetError mapAutoAssetErrorIndications].cold.1
+ +[MAAutoAssetError stringForCode:]
+ _OBJC_CLASS_$_SUCoreErrorInformation
+ ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.944
+ ___119+[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke.412
+ ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.560
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1103
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1104
+ ___48+[MAAutoAssetError mapAutoAssetErrorIndications]_block_invoke
+ ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1092
+ ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1129
+ ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.914
+ ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.599
+ ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.592
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1098
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1099
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1102
+ ___Block_byref_object_copy_.1269
+ ___Block_byref_object_copy_.705
+ ___Block_byref_object_copy_.779
+ ___Block_byref_object_dispose_.1270
+ ___Block_byref_object_dispose_.706
+ ___Block_byref_object_dispose_.780
+ ____MAensureExtension_block_invoke.1276
+ ____MAsendDownloadAsset_block_invoke.1178
+ ____MAsendPMVCancelDownload_block_invoke.1196
+ ____MAsendPMVDownload_block_invoke.1184
+ ___block_literal_global.1087
+ ___block_literal_global.1091
+ ___block_literal_global.1095
+ ___block_literal_global.1097
+ ___block_literal_global.1098
+ ___block_literal_global.1136
+ ___block_literal_global.1142
+ ___block_literal_global.1152
+ ___block_literal_global.1157
+ ___block_literal_global.1181
+ ___block_literal_global.1342
+ ___block_literal_global.1347
+ ___block_literal_global.1349
+ ___block_literal_global.1376
+ ___block_literal_global.1399
+ ___block_literal_global.2785
+ ___block_literal_global.2787
+ ___block_literal_global.2789
+ ___block_literal_global.2791
+ ___block_literal_global.435
+ ___block_literal_global.466
+ ___block_literal_global.472
+ ___block_literal_global.474
+ ___block_literal_global.520
+ ___block_literal_global.651
+ ___block_literal_global.679
+ ___block_literal_global.685
+ ___block_literal_global.687
+ ___block_literal_global.797
+ ___block_literal_global.802
+ ___block_literal_global.804
+ ___block_literal_global.806
+ ___block_literal_global.984
+ ___block_literal_global.986
+ ___block_literal_global.991
+ _mapAutoAssetErrorIndications.autoAssetErrorInfoOnce
+ _mapV2ErrorIndications
+ _objc_msgSend$attributesOfErrorForDomain:withCode:codeName:
+ _objc_msgSend$mapAutoAssetErrorIndications
+ _objc_msgSend$stringForCode:
- ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.941
- ___119+[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke.409
- ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.557
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1085
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1086
- ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1074
- ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1111
- ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.911
- ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.596
- ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.589
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1080
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1081
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1084
- ___Block_byref_object_copy_.1251
- ___Block_byref_object_copy_.702
- ___Block_byref_object_copy_.776
- ___Block_byref_object_dispose_.1252
- ___Block_byref_object_dispose_.703
- ___Block_byref_object_dispose_.777
- ____MAensureExtension_block_invoke.1258
- ____MAsendDownloadAsset_block_invoke.1160
- ____MAsendPMVCancelDownload_block_invoke.1178
- ____MAsendPMVDownload_block_invoke.1166
- ___block_literal_global.1069
- ___block_literal_global.1073
- ___block_literal_global.1077
- ___block_literal_global.1079
- ___block_literal_global.1080
- ___block_literal_global.1118
- ___block_literal_global.1124
- ___block_literal_global.1134
- ___block_literal_global.1139
- ___block_literal_global.1163
- ___block_literal_global.1324
- ___block_literal_global.1329
- ___block_literal_global.1331
- ___block_literal_global.1358
- ___block_literal_global.1381
- ___block_literal_global.2763
- ___block_literal_global.2765
- ___block_literal_global.2767
- ___block_literal_global.2769
- ___block_literal_global.432
- ___block_literal_global.463
- ___block_literal_global.469
- ___block_literal_global.471
- ___block_literal_global.517
- ___block_literal_global.648
- ___block_literal_global.676
- ___block_literal_global.682
- ___block_literal_global.684
- ___block_literal_global.794
- ___block_literal_global.799
- ___block_literal_global.801
- ___block_literal_global.803
- ___block_literal_global.981
- ___block_literal_global.983
- ___block_literal_global.985
CStrings:
+ "attributesOfErrorForDomain:withCode:codeName:"
+ "mapAutoAssetErrorIndications"
+ "stringForCode:"

```
