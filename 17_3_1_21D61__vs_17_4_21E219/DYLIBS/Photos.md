## Photos

> `/System/Library/Frameworks/Photos.framework/Photos`

```diff

-630.0.150.0.0
-  __TEXT.__text: 0x1fb590
-  __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_methlist: 0x1a928
-  __TEXT.__const: 0xc20
+646.1.102.0.0
+  __TEXT.__text: 0x1fef5c
+  __TEXT.__auth_stubs: 0x2400
+  __TEXT.__objc_methlist: 0x1abb0
+  __TEXT.__const: 0xc00
   __TEXT.__constg_swiftt: 0xac
   __TEXT.__swift5_typeref: 0x1c3
   __TEXT.__swift5_reflstr: 0x70

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0xc
-  __TEXT.__cstring: 0x21611
-  __TEXT.__gcc_except_tab: 0x4b34
-  __TEXT.__oslogstring: 0x146e0
+  __TEXT.__cstring: 0x2197c
+  __TEXT.__gcc_except_tab: 0x4c20
+  __TEXT.__oslogstring: 0x14c20
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x6c1c
-  __TEXT.__eh_frame: 0x98
-  __TEXT.__objc_classname: 0x2a3c
-  __TEXT.__objc_methname: 0x51bf1
-  __TEXT.__objc_methtype: 0x594a
-  __TEXT.__objc_stubs: 0x2c980
+  __TEXT.__unwind_info: 0x6d84
+  __TEXT.__eh_frame: 0x108
+  __TEXT.__objc_classname: 0x2aaa
+  __TEXT.__objc_methname: 0x52485
+  __TEXT.__objc_methtype: 0x5a5a
+  __TEXT.__objc_stubs: 0x2d080
   __DATA_CONST.__got: 0xb20
-  __DATA_CONST.__const: 0x6630
-  __DATA_CONST.__objc_classlist: 0xab0
+  __DATA_CONST.__const: 0x6718
+  __DATA_CONST.__objc_classlist: 0xac8
   __DATA_CONST.__objc_catlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x248
+  __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x28ad0
-  __DATA_CONST.__objc_selrefs: 0xe9f8
+  __DATA_CONST.__objc_const: 0x29060
+  __DATA_CONST.__objc_selrefs: 0xeb70
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x11f0
+  __DATA_CONST.__objc_superrefs: 0x8e0
   __DATA_CONST.__objc_arraydata: 0x800
-  __AUTH_CONST.__const: 0x3178
-  __AUTH_CONST.__cfstring: 0x1e520
-  __AUTH_CONST.__objc_const: 0x9588
+  __AUTH_CONST.__const: 0x31b8
+  __AUTH_CONST.__cfstring: 0x1e820
+  __AUTH_CONST.__objc_const: 0x96a8
   __AUTH_CONST.__objc_intobj: 0x1bf0
   __AUTH_CONST.__objc_arrayobj: 0x5b8
   __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x1218
-  __AUTH.__objc_data: 0x54b0
+  __AUTH_CONST.__auth_got: 0x1210
+  __AUTH.__objc_data: 0x5550
   __AUTH.__data: 0xa8
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x11c0
-  __DATA.__objc_superrefs: 0x8c8
-  __DATA.__objc_ivar: 0x25e4
+  __DATA.__objc_ivar: 0x2658
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0x2590
+  __DATA.__data: 0x2660
   __DATA.__common: 0x55
-  __DATA.__bss: 0xdf8
-  __DATA_DIRTY.__objc_data: 0x15e0
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA.__bss: 0xdb0
+  __DATA_DIRTY.__objc_data: 0x1630
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10577
-  Symbols:   35333
-  CStrings:  18426
+  Functions: 10653
+  Symbols:   35608
+  CStrings:  18573
 
Symbols:
+ +[PHImageManager(VideoUtilities) exportVideoFileForTimeRange:fromVideoMediaItemMakerData:forAssetUuid:toOutputFileURL:fingerPrint:signpostId:completion:]
+ +[PHImageManager(VideoUtilities) fileTypeForOutputURL:]
+ +[PHImageManager(VideoUtilities) mediaItemURLForAssetUuid:fingerPrint:outOfBandPresentationHints:]
+ +[PHImageManager(VideoUtilities) startExportSession:assetUuid:signpostId:completion:]
+ +[PHPhotoLibrary checkAuthorizationStatusForAPIAccessLevel:suppressPrompt:]
+ +[PHPhotoLibraryObserverRegistrar _isInternalObserver:]
+ -[PHChangeHandlingDebugEvent deletedCount]
+ -[PHChangeHandlingDebugEvent description]
+ -[PHChangeHandlingDebugEvent distributeExternalTimestamp]
+ -[PHChangeHandlingDebugEvent distributeInternalTimestamp]
+ -[PHChangeHandlingDebugEvent endTimestamp]
+ -[PHChangeHandlingDebugEvent externalObserversCount]
+ -[PHChangeHandlingDebugEvent fetchResultCount]
+ -[PHChangeHandlingDebugEvent initWithStartTimestamp:]
+ -[PHChangeHandlingDebugEvent init]
+ -[PHChangeHandlingDebugEvent insertedCount]
+ -[PHChangeHandlingDebugEvent internalObserversCount]
+ -[PHChangeHandlingDebugEvent qosClass]
+ -[PHChangeHandlingDebugEvent reset]
+ -[PHChangeHandlingDebugEvent setDeletedCount:]
+ -[PHChangeHandlingDebugEvent setDistributeExternalTimestamp:]
+ -[PHChangeHandlingDebugEvent setDistributeInternalTimestamp:]
+ -[PHChangeHandlingDebugEvent setEndTimestamp:]
+ -[PHChangeHandlingDebugEvent setExternalObserversCount:]
+ -[PHChangeHandlingDebugEvent setFetchResultCount:]
+ -[PHChangeHandlingDebugEvent setInsertedCount:]
+ -[PHChangeHandlingDebugEvent setInternalObserversCount:]
+ -[PHChangeHandlingDebugEvent setQosClass:]
+ -[PHChangeHandlingDebugEvent setStartTimestamp:]
+ -[PHChangeHandlingDebugEvent setUnknownMergeEvent:]
+ -[PHChangeHandlingDebugEvent setUpdatedCount:]
+ -[PHChangeHandlingDebugEvent startTimestamp]
+ -[PHChangeHandlingDebugEvent unknownMergeEvent]
+ -[PHChangeHandlingDebugEvent updatedCount]
+ -[PHChangeHandlingDebugger .cxx_destruct]
+ -[PHChangeHandlingDebugger beginProcessPendingChanges]
+ -[PHChangeHandlingDebugger changeHandlingActiveStateDidChange:]
+ -[PHChangeHandlingDebugger endProcessPendingChanges]
+ -[PHChangeHandlingDebugger initWithMaxPreviousEvents:]
+ -[PHChangeHandlingDebugger init]
+ -[PHChangeHandlingDebugger stateCaptureDictionary]
+ -[PHImportDeviceSource iconSymbolName]
+ -[PHImportSource iconSymbolName]
+ -[PHPerson keyFacePickSource]
+ -[PHPhotoLibrary countOfFetchResultsRegisteredForChangeNotifications]
+ -[PHPhotoLibrary stateCaptureDictionary]
+ -[PHPhotoLibraryObserverRegistrar .cxx_destruct]
+ -[PHPhotoLibraryObserverRegistrar _lock_clearOIDCache]
+ -[PHPhotoLibraryObserverRegistrar _lock_hasChangeObservers]
+ -[PHPhotoLibraryObserverRegistrar _lock_pauseChangeHandlingIfNeeded]
+ -[PHPhotoLibraryObserverRegistrar _lock_resumeChangeHandlingIfNeeded]
+ -[PHPhotoLibraryObserverRegistrar addObservers:authorizationStatus:]
+ -[PHPhotoLibraryObserverRegistrar clearsOIDCacheAfterFetchResultDealloc]
+ -[PHPhotoLibraryObserverRegistrar countOfRegisteredFetchResults]
+ -[PHPhotoLibraryObserverRegistrar dealloc]
+ -[PHPhotoLibraryObserverRegistrar getObserversWithBlock:]
+ -[PHPhotoLibraryObserverRegistrar initWithLibraryBundle:changeHandlingDebugger:uniqueObjectIDCache:]
+ -[PHPhotoLibraryObserverRegistrar postsPersistentHistoryChangedNotifications]
+ -[PHPhotoLibraryObserverRegistrar registerFetchResult:]
+ -[PHPhotoLibraryObserverRegistrar removeObserver:]
+ -[PHPhotoLibraryObserverRegistrar setClearsOIDCacheAfterFetchResultDealloc:]
+ -[PHPhotoLibraryObserverRegistrar setPostsPersistentHistoryChangedNotifications:]
+ -[PHPhotoLibraryObserverRegistrar unregisterFetchResult:]
+ -[PHServerResourceRequestRunner startDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:needsDownload:shouldApplyTimeRange:reply:]
+ -[PHServerResourceRequestRunner startWalrusTimeRangeDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:partialVideoURL:reply:]
+ -[PHUniqueObjectIDCache uniquedOIDs:]
+ GCC_except_table1000
+ GCC_except_table1016
+ GCC_except_table10168
+ GCC_except_table10239
+ GCC_except_table10264
+ GCC_except_table10298
+ GCC_except_table10326
+ GCC_except_table10341
+ GCC_except_table10380
+ GCC_except_table10382
+ GCC_except_table10384
+ GCC_except_table10403
+ GCC_except_table1072
+ GCC_except_table1120
+ GCC_except_table1244
+ GCC_except_table1247
+ GCC_except_table1260
+ GCC_except_table1452
+ GCC_except_table1456
+ GCC_except_table1458
+ GCC_except_table1460
+ GCC_except_table1462
+ GCC_except_table1464
+ GCC_except_table1466
+ GCC_except_table1469
+ GCC_except_table1478
+ GCC_except_table1481
+ GCC_except_table1493
+ GCC_except_table1529
+ GCC_except_table1531
+ GCC_except_table1533
+ GCC_except_table1535
+ GCC_except_table1537
+ GCC_except_table1539
+ GCC_except_table1545
+ GCC_except_table1547
+ GCC_except_table1549
+ GCC_except_table1551
+ GCC_except_table1553
+ GCC_except_table1555
+ GCC_except_table1558
+ GCC_except_table1560
+ GCC_except_table1562
+ GCC_except_table1564
+ GCC_except_table1566
+ GCC_except_table1569
+ GCC_except_table1571
+ GCC_except_table1574
+ GCC_except_table1604
+ GCC_except_table1606
+ GCC_except_table1609
+ GCC_except_table1612
+ GCC_except_table1661
+ GCC_except_table1666
+ GCC_except_table1674
+ GCC_except_table1676
+ GCC_except_table1688
+ GCC_except_table1859
+ GCC_except_table1864
+ GCC_except_table1918
+ GCC_except_table2026
+ GCC_except_table2100
+ GCC_except_table2105
+ GCC_except_table2107
+ GCC_except_table2110
+ GCC_except_table2120
+ GCC_except_table2131
+ GCC_except_table2133
+ GCC_except_table2136
+ GCC_except_table2270
+ GCC_except_table2274
+ GCC_except_table2336
+ GCC_except_table2344
+ GCC_except_table2373
+ GCC_except_table2377
+ GCC_except_table2382
+ GCC_except_table2461
+ GCC_except_table2493
+ GCC_except_table2499
+ GCC_except_table2502
+ GCC_except_table2512
+ GCC_except_table2516
+ GCC_except_table2522
+ GCC_except_table2529
+ GCC_except_table2533
+ GCC_except_table2544
+ GCC_except_table2549
+ GCC_except_table2560
+ GCC_except_table2561
+ GCC_except_table2577
+ GCC_except_table2679
+ GCC_except_table2702
+ GCC_except_table2704
+ GCC_except_table2706
+ GCC_except_table2749
+ GCC_except_table2772
+ GCC_except_table2805
+ GCC_except_table2809
+ GCC_except_table2812
+ GCC_except_table2958
+ GCC_except_table2991
+ GCC_except_table2999
+ GCC_except_table3012
+ GCC_except_table3014
+ GCC_except_table3039
+ GCC_except_table3044
+ GCC_except_table3045
+ GCC_except_table3291
+ GCC_except_table3322
+ GCC_except_table3331
+ GCC_except_table3333
+ GCC_except_table3337
+ GCC_except_table3342
+ GCC_except_table3353
+ GCC_except_table3358
+ GCC_except_table3371
+ GCC_except_table3434
+ GCC_except_table3692
+ GCC_except_table3700
+ GCC_except_table3728
+ GCC_except_table3730
+ GCC_except_table3732
+ GCC_except_table3795
+ GCC_except_table3819
+ GCC_except_table4270
+ GCC_except_table4323
+ GCC_except_table4350
+ GCC_except_table4407
+ GCC_except_table4423
+ GCC_except_table4429
+ GCC_except_table4443
+ GCC_except_table4446
+ GCC_except_table4449
+ GCC_except_table4462
+ GCC_except_table4500
+ GCC_except_table4511
+ GCC_except_table4549
+ GCC_except_table4575
+ GCC_except_table4578
+ GCC_except_table4584
+ GCC_except_table4589
+ GCC_except_table4612
+ GCC_except_table4639
+ GCC_except_table4665
+ GCC_except_table4667
+ GCC_except_table4678
+ GCC_except_table4716
+ GCC_except_table4787
+ GCC_except_table4792
+ GCC_except_table4910
+ GCC_except_table4913
+ GCC_except_table4926
+ GCC_except_table4945
+ GCC_except_table4958
+ GCC_except_table4988
+ GCC_except_table5022
+ GCC_except_table5024
+ GCC_except_table5328
+ GCC_except_table5341
+ GCC_except_table5354
+ GCC_except_table5369
+ GCC_except_table5395
+ GCC_except_table5398
+ GCC_except_table5400
+ GCC_except_table5402
+ GCC_except_table5404
+ GCC_except_table5435
+ GCC_except_table5468
+ GCC_except_table5470
+ GCC_except_table5504
+ GCC_except_table5693
+ GCC_except_table5850
+ GCC_except_table6043
+ GCC_except_table6112
+ GCC_except_table6134
+ GCC_except_table6138
+ GCC_except_table6144
+ GCC_except_table6195
+ GCC_except_table6301
+ GCC_except_table6303
+ GCC_except_table6349
+ GCC_except_table6389
+ GCC_except_table6391
+ GCC_except_table6393
+ GCC_except_table6405
+ GCC_except_table6410
+ GCC_except_table6446
+ GCC_except_table6469
+ GCC_except_table6556
+ GCC_except_table6559
+ GCC_except_table6577
+ GCC_except_table6634
+ GCC_except_table6637
+ GCC_except_table6655
+ GCC_except_table6719
+ GCC_except_table6799
+ GCC_except_table6928
+ GCC_except_table6933
+ GCC_except_table7218
+ GCC_except_table7228
+ GCC_except_table7259
+ GCC_except_table7349
+ GCC_except_table7397
+ GCC_except_table7399
+ GCC_except_table7483
+ GCC_except_table7557
+ GCC_except_table7575
+ GCC_except_table7660
+ GCC_except_table7674
+ GCC_except_table7767
+ GCC_except_table7768
+ GCC_except_table7769
+ GCC_except_table7770
+ GCC_except_table7771
+ GCC_except_table7772
+ GCC_except_table7773
+ GCC_except_table7774
+ GCC_except_table7775
+ GCC_except_table7776
+ GCC_except_table7777
+ GCC_except_table7778
+ GCC_except_table7779
+ GCC_except_table7780
+ GCC_except_table7781
+ GCC_except_table7782
+ GCC_except_table7783
+ GCC_except_table7784
+ GCC_except_table7785
+ GCC_except_table7786
+ GCC_except_table7787
+ GCC_except_table7788
+ GCC_except_table7789
+ GCC_except_table7790
+ GCC_except_table7791
+ GCC_except_table7792
+ GCC_except_table7793
+ GCC_except_table7873
+ GCC_except_table7882
+ GCC_except_table7883
+ GCC_except_table7884
+ GCC_except_table7885
+ GCC_except_table7886
+ GCC_except_table7905
+ GCC_except_table7924
+ GCC_except_table7952
+ GCC_except_table7953
+ GCC_except_table7954
+ GCC_except_table7955
+ GCC_except_table7956
+ GCC_except_table7957
+ GCC_except_table7958
+ GCC_except_table7959
+ GCC_except_table7988
+ GCC_except_table7992
+ GCC_except_table8011
+ GCC_except_table8016
+ GCC_except_table8083
+ GCC_except_table8173
+ GCC_except_table8238
+ GCC_except_table8276
+ GCC_except_table8353
+ GCC_except_table8372
+ GCC_except_table858
+ GCC_except_table875
+ GCC_except_table8854
+ GCC_except_table8860
+ GCC_except_table8864
+ GCC_except_table8870
+ GCC_except_table8976
+ GCC_except_table8995
+ GCC_except_table8997
+ GCC_except_table8999
+ GCC_except_table9001
+ GCC_except_table9031
+ GCC_except_table9091
+ GCC_except_table9191
+ GCC_except_table9203
+ GCC_except_table9242
+ GCC_except_table9244
+ GCC_except_table9257
+ GCC_except_table9292
+ GCC_except_table9334
+ GCC_except_table9338
+ GCC_except_table9347
+ GCC_except_table9348
+ GCC_except_table9355
+ GCC_except_table9392
+ GCC_except_table9399
+ GCC_except_table9501
+ GCC_except_table9507
+ GCC_except_table9509
+ GCC_except_table9555
+ GCC_except_table9571
+ GCC_except_table9581
+ GCC_except_table9663
+ GCC_except_table9751
+ GCC_except_table9755
+ GCC_except_table9759
+ GCC_except_table9787
+ GCC_except_table9950
+ GCC_except_table9960
+ _OBJC_CLASS_$_NSInvocation
+ _OBJC_CLASS_$_PFStateCaptureHandler
+ _OBJC_CLASS_$_PHChangeHandlingDebugEvent
+ _OBJC_CLASS_$_PHChangeHandlingDebugger
+ _OBJC_CLASS_$_PHPhotoLibraryObserverRegistrar
+ _OBJC_IVAR_$_PHChangeHandlingDebugEvent._deletedCount
+ _OBJC_IVAR_$_PHChangeHandlingDebugEvent._distributeExternalTimestamp
+ _OBJC_IVAR_$_PHChangeHandlingDebugEvent._distributeInternalTimestamp
+ _OBJC_IVAR_$_PHChangeHandlingDebugEvent._endTimestamp
+ _OBJC_IVAR_$_PHChangeHandlingDebugEvent._externalObserversCount
+ _OBJC_IVAR_$_PHChangeHandlingDebugEvent._fetchResultCount
+ _OBJC_IVAR_$_PHChangeHandlingDebugEvent._insertedCount
+ _OBJC_IVAR_$_PHChangeHandlingDebugEvent._internalObserversCount
+ _OBJC_IVAR_$_PHChangeHandlingDebugEvent._qosClass
+ _OBJC_IVAR_$_PHChangeHandlingDebugEvent._startTimestamp
+ _OBJC_IVAR_$_PHChangeHandlingDebugEvent._unknownMergeEvent
+ _OBJC_IVAR_$_PHChangeHandlingDebugEvent._updatedCount
+ _OBJC_IVAR_$_PHChangeHandlingDebugger._activeLock
+ _OBJC_IVAR_$_PHChangeHandlingDebugger._activeLock_isActive
+ _OBJC_IVAR_$_PHChangeHandlingDebugger._activeLock_isActiveTimestamp
+ _OBJC_IVAR_$_PHChangeHandlingDebugger._lock
+ _OBJC_IVAR_$_PHChangeHandlingDebugger._lock_currentEvent
+ _OBJC_IVAR_$_PHChangeHandlingDebugger._lock_nextEvent
+ _OBJC_IVAR_$_PHChangeHandlingDebugger._lock_previousEvents
+ _OBJC_IVAR_$_PHChangeHandlingDebugger._maxPreviousEvents
+ _OBJC_IVAR_$_PHPerson._keyFacePickSource
+ _OBJC_IVAR_$_PHPhotoLibrary._changeHandlingDebugger
+ _OBJC_IVAR_$_PHPhotoLibrary._observerRegistrar
+ _OBJC_IVAR_$_PHPhotoLibrary._stateCaptureHandler
+ _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._changeHandlingDebugger
+ _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock
+ _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_clearsOIDCacheAfterFetchResultDealloc
+ _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_externalChangeObservers
+ _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_fetchResults
+ _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_internalChangeObservers
+ _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_isChangeHandlingActive
+ _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_isChangeHandlingAuthorized
+ _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_postsPersistentHistoryChangedNotifications
+ _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._photoLibraryBundle
+ _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._uniqueObjectIDCache
+ _OBJC_METACLASS_$_PHChangeHandlingDebugEvent
+ _OBJC_METACLASS_$_PHChangeHandlingDebugger
+ _OBJC_METACLASS_$_PHPhotoLibraryObserverRegistrar
+ _PLShouldBoostLogLevelForResourceRecipeID
+ __OBJC_$_CLASS_METHODS_PHPhotoLibraryObserverRegistrar
+ __OBJC_$_CLASS_PROP_LIST_PHAssetPropertySet.2207
+ __OBJC_$_CLASS_PROP_LIST_PHFacePropertySet.674
+ __OBJC_$_CLASS_PROP_LIST_PHMemoryPropertySet.1210
+ __OBJC_$_CLASS_PROP_LIST_PHPersonPropertySet.527
+ __OBJC_$_INSTANCE_METHODS_PHChangeHandlingDebugEvent
+ __OBJC_$_INSTANCE_METHODS_PHChangeHandlingDebugger
+ __OBJC_$_INSTANCE_METHODS_PHPhotoLibraryObserverRegistrar
+ __OBJC_$_INSTANCE_VARIABLES_PHChangeHandlingDebugEvent
+ __OBJC_$_INSTANCE_VARIABLES_PHChangeHandlingDebugger
+ __OBJC_$_INSTANCE_VARIABLES_PHPhotoLibraryObserverRegistrar
+ __OBJC_$_PROP_LIST_PHAssetPropertySet.2214
+ __OBJC_$_PROP_LIST_PHAssetResourceRequest.263
+ __OBJC_$_PROP_LIST_PHChangeHandlingDebugEvent
+ __OBJC_$_PROP_LIST_PHChangeRequest.168
+ __OBJC_$_PROP_LIST_PHImportExceptionRecorder.84
+ __OBJC_$_PROP_LIST_PHPhotoLibraryObserverRegistrar
+ __OBJC_$_PROP_LIST_PHShare.124
+ __OBJC_$_PROP_LIST_PHThumbnailAsset.146
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PFStateCaptureProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PFStateCaptureProvider
+ __OBJC_$_PROTOCOL_REFS_PFStateCaptureProvider
+ __OBJC_CLASS_RO_$_PHChangeHandlingDebugEvent
+ __OBJC_CLASS_RO_$_PHChangeHandlingDebugger
+ __OBJC_CLASS_RO_$_PHPhotoLibraryObserverRegistrar
+ __OBJC_LABEL_PROTOCOL_$_PFStateCaptureProvider
+ __OBJC_METACLASS_RO_$_PHChangeHandlingDebugEvent
+ __OBJC_METACLASS_RO_$_PHChangeHandlingDebugger
+ __OBJC_METACLASS_RO_$_PHPhotoLibraryObserverRegistrar
+ __OBJC_PROTOCOL_$_PFStateCaptureProvider
+ ___103-[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:reply:]_block_invoke.259
+ ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke.108
+ ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke_2.109
+ ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke_3.111
+ ___152-[PHServerResourceRequestRunner startWalrusTimeRangeDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:partialVideoURL:reply:]_block_invoke
+ ___152-[PHServerResourceRequestRunner startWalrusTimeRangeDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:partialVideoURL:reply:]_block_invoke.140
+ ___152-[PHServerResourceRequestRunner startWalrusTimeRangeDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:partialVideoURL:reply:]_block_invoke.143
+ ___152-[PHServerResourceRequestRunner startWalrusTimeRangeDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:partialVideoURL:reply:]_block_invoke.144
+ ___153+[PHImageManager(VideoUtilities) exportVideoFileForTimeRange:fromVideoMediaItemMakerData:forAssetUuid:toOutputFileURL:fingerPrint:signpostId:completion:]_block_invoke
+ ___156-[PHServerResourceRequestRunner startDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:needsDownload:shouldApplyTimeRange:reply:]_block_invoke
+ ___156-[PHServerResourceRequestRunner startDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:needsDownload:shouldApplyTimeRange:reply:]_block_invoke.139
+ ___38+[PHPerson propertiesToFetchWithHint:]_block_invoke.102
+ ___40-[PHPhotoLibrary _processPendingChanges]_block_invoke_2
+ ___50-[PHChangeHandlingDebugger stateCaptureDictionary]_block_invoke
+ ___50-[PHChangeHandlingDebugger stateCaptureDictionary]_block_invoke_2
+ ___50-[PHChangeHandlingDebugger stateCaptureDictionary]_block_invoke_3
+ ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke.218
+ ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_2.219
+ ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_3.220
+ ___50-[PHPhotoLibraryObserverRegistrar removeObserver:]_block_invoke
+ ___52-[PHChangeHandlingDebugger endProcessPendingChanges]_block_invoke
+ ___54-[PHChangeHandlingDebugger beginProcessPendingChanges]_block_invoke
+ ___54-[PHPhotoLibraryObserverRegistrar _lock_clearOIDCache]_block_invoke
+ ___55-[PHPhotoLibraryObserverRegistrar registerFetchResult:]_block_invoke
+ ___57-[PHPhotoLibraryObserverRegistrar getObserversWithBlock:]_block_invoke
+ ___57-[PHPhotoLibraryObserverRegistrar unregisterFetchResult:]_block_invoke
+ ___63-[PHChangeHandlingDebugger changeHandlingActiveStateDidChange:]_block_invoke
+ ___63-[PHImageManager requestAVProxyForAsset:options:resultHandler:]_block_invoke.649
+ ___64-[PHPhotoLibraryObserverRegistrar countOfRegisteredFetchResults]_block_invoke
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.591
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.595
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.598
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_2.596
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_2.600
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_3.597
+ ___68-[PHPhotoLibraryObserverRegistrar addObservers:authorizationStatus:]_block_invoke
+ ___72-[PHPhotoLibraryObserverRegistrar clearsOIDCacheAfterFetchResultDealloc]_block_invoke
+ ___76-[PHPhotoLibraryObserverRegistrar setClearsOIDCacheAfterFetchResultDealloc:]_block_invoke
+ ___76-[PHServerResourceRequestRunner makeResourceUnavailableWithRequest:library:]_block_invoke.103
+ ___77-[PHPhotoLibraryObserverRegistrar postsPersistentHistoryChangedNotifications]_block_invoke
+ ___81-[PHPhotoLibraryObserverRegistrar setPostsPersistentHistoryChangedNotifications:]_block_invoke
+ ___83-[PHImageManager requestContentEditingInputForAsset:withOptions:completionHandler:]_block_invoke.632
+ ___85+[PHImageManager(VideoUtilities) startExportSession:assetUuid:signpostId:completion:]_block_invoke
+ ___85-[PHServerResourceRequestRunner chooseVideoWithRequest:library:clientBundleID:reply:]_block_invoke.122
+ ___85-[PHServerResourceRequestRunner chooseVideoWithRequest:library:clientBundleID:reply:]_block_invoke.126
+ ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.567
+ ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.571
+ ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.576
+ ___89-[PHImageManager requestNewCGImageForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.621
+ ___95-[PHServerResourceRequestRunner makeResourceAvailableWithRequest:library:clientBundleID:reply:]_block_invoke.75
+ ___95-[PHServerResourceRequestRunner makeResourceAvailableWithRequest:library:clientBundleID:reply:]_block_invoke.86
+ ___95-[PHServerResourceRequestRunner makeResourceAvailableWithRequest:library:clientBundleID:reply:]_block_invoke.94
+ ___95-[PHServerResourceRequestRunner makeResourceAvailableWithRequest:library:clientBundleID:reply:]_block_invoke_2.88
+ ___95-[PHServerResourceRequestRunner makeResourceAvailableWithRequest:library:clientBundleID:reply:]_block_invoke_2.98
+ ___95-[PHServerResourceRequestRunner makeResourceAvailableWithRequest:library:clientBundleID:reply:]_block_invoke_3.99
+ ___Block_byref_object_copy_.10515
+ ___Block_byref_object_copy_.11143
+ ___Block_byref_object_copy_.1194
+ ___Block_byref_object_copy_.13274
+ ___Block_byref_object_copy_.1452
+ ___Block_byref_object_copy_.14817
+ ___Block_byref_object_copy_.14983
+ ___Block_byref_object_copy_.15282
+ ___Block_byref_object_copy_.15749
+ ___Block_byref_object_copy_.16302
+ ___Block_byref_object_copy_.16463
+ ___Block_byref_object_copy_.1788
+ ___Block_byref_object_copy_.18388
+ ___Block_byref_object_copy_.19536
+ ___Block_byref_object_copy_.20045
+ ___Block_byref_object_copy_.20384
+ ___Block_byref_object_copy_.20655
+ ___Block_byref_object_copy_.21537
+ ___Block_byref_object_copy_.21848
+ ___Block_byref_object_copy_.2225
+ ___Block_byref_object_copy_.22702
+ ___Block_byref_object_copy_.23303
+ ___Block_byref_object_copy_.24708
+ ___Block_byref_object_copy_.25292
+ ___Block_byref_object_copy_.26114
+ ___Block_byref_object_copy_.26356
+ ___Block_byref_object_copy_.2646
+ ___Block_byref_object_copy_.27373
+ ___Block_byref_object_copy_.27856
+ ___Block_byref_object_copy_.28964
+ ___Block_byref_object_copy_.29448
+ ___Block_byref_object_copy_.32501
+ ___Block_byref_object_copy_.32920
+ ___Block_byref_object_copy_.33155
+ ___Block_byref_object_copy_.34080
+ ___Block_byref_object_copy_.34463
+ ___Block_byref_object_copy_.34641
+ ___Block_byref_object_copy_.34930
+ ___Block_byref_object_copy_.35608
+ ___Block_byref_object_copy_.36508
+ ___Block_byref_object_copy_.3657
+ ___Block_byref_object_copy_.36617
+ ___Block_byref_object_copy_.37445
+ ___Block_byref_object_copy_.38446
+ ___Block_byref_object_copy_.38733
+ ___Block_byref_object_copy_.39255
+ ___Block_byref_object_copy_.4658
+ ___Block_byref_object_copy_.4891
+ ___Block_byref_object_copy_.6016
+ ___Block_byref_object_copy_.6996
+ ___Block_byref_object_copy_.7634
+ ___Block_byref_object_copy_.7838
+ ___Block_byref_object_copy_.8006
+ ___Block_byref_object_copy_.8574
+ ___Block_byref_object_copy_.8820
+ ___Block_byref_object_copy_.9287
+ ___Block_byref_object_copy_.9717
+ ___Block_byref_object_dispose_.10516
+ ___Block_byref_object_dispose_.11144
+ ___Block_byref_object_dispose_.1195
+ ___Block_byref_object_dispose_.13275
+ ___Block_byref_object_dispose_.1453
+ ___Block_byref_object_dispose_.14818
+ ___Block_byref_object_dispose_.14984
+ ___Block_byref_object_dispose_.15283
+ ___Block_byref_object_dispose_.15750
+ ___Block_byref_object_dispose_.16303
+ ___Block_byref_object_dispose_.16464
+ ___Block_byref_object_dispose_.1789
+ ___Block_byref_object_dispose_.18389
+ ___Block_byref_object_dispose_.19537
+ ___Block_byref_object_dispose_.20046
+ ___Block_byref_object_dispose_.20385
+ ___Block_byref_object_dispose_.20656
+ ___Block_byref_object_dispose_.21538
+ ___Block_byref_object_dispose_.21849
+ ___Block_byref_object_dispose_.2226
+ ___Block_byref_object_dispose_.22703
+ ___Block_byref_object_dispose_.23304
+ ___Block_byref_object_dispose_.24709
+ ___Block_byref_object_dispose_.25293
+ ___Block_byref_object_dispose_.26115
+ ___Block_byref_object_dispose_.26357
+ ___Block_byref_object_dispose_.2647
+ ___Block_byref_object_dispose_.27374
+ ___Block_byref_object_dispose_.27857
+ ___Block_byref_object_dispose_.28965
+ ___Block_byref_object_dispose_.29449
+ ___Block_byref_object_dispose_.32502
+ ___Block_byref_object_dispose_.32921
+ ___Block_byref_object_dispose_.33156
+ ___Block_byref_object_dispose_.34081
+ ___Block_byref_object_dispose_.34464
+ ___Block_byref_object_dispose_.34642
+ ___Block_byref_object_dispose_.34931
+ ___Block_byref_object_dispose_.35609
+ ___Block_byref_object_dispose_.36509
+ ___Block_byref_object_dispose_.3658
+ ___Block_byref_object_dispose_.36618
+ ___Block_byref_object_dispose_.37446
+ ___Block_byref_object_dispose_.38447
+ ___Block_byref_object_dispose_.38734
+ ___Block_byref_object_dispose_.39256
+ ___Block_byref_object_dispose_.4659
+ ___Block_byref_object_dispose_.4892
+ ___Block_byref_object_dispose_.6017
+ ___Block_byref_object_dispose_.6997
+ ___Block_byref_object_dispose_.7635
+ ___Block_byref_object_dispose_.7839
+ ___Block_byref_object_dispose_.8007
+ ___Block_byref_object_dispose_.8575
+ ___Block_byref_object_dispose_.8821
+ ___Block_byref_object_dispose_.9288
+ ___Block_byref_object_dispose_.9718
+ ____fetchNonHintResources_block_invoke.175
+ ___block_descriptor_100_e8_32s40s48s56s64s72s80bs_e30_v32?0"NSError"8q16"NSURL"24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96bs_e62_v48?0"NSURL"8"NSData"16"NSDate"24"NSString"32"NSError"40ls32l8s96l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_32_e46_"NSString"16?0"PHChangeHandlingDebugEvent"8l
+ ___block_descriptor_48_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_56_e8_32r40r48r_e41_v32?0"NSArray"8"NSArray"16"NSArray"24lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56r64r72n11_8_8_s0_t8w8_e18_v16?0"PHChange"8l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e20_v20?0B8"NSError"12ls32l8s80l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.10203
+ ___block_literal_global.1039
+ ___block_literal_global.1048
+ ___block_literal_global.10569
+ ___block_literal_global.1063
+ ___block_literal_global.107
+ ___block_literal_global.1081
+ ___block_literal_global.109
+ ___block_literal_global.112.30760
+ ___block_literal_global.1196
+ ___block_literal_global.1233
+ ___block_literal_global.12785
+ ___block_literal_global.131.28969
+ ___block_literal_global.13307
+ ___block_literal_global.13361
+ ___block_literal_global.140
+ ___block_literal_global.14487
+ ___block_literal_global.146
+ ___block_literal_global.1471
+ ___block_literal_global.14810
+ ___block_literal_global.15238
+ ___block_literal_global.161
+ ___block_literal_global.16111
+ ___block_literal_global.162
+ ___block_literal_global.16940
+ ___block_literal_global.17699
+ ___block_literal_global.1785
+ ___block_literal_global.18735
+ ___block_literal_global.19226
+ ___block_literal_global.1940
+ ___block_literal_global.19734
+ ___block_literal_global.200.15970
+ ___block_literal_global.20361
+ ___block_literal_global.20958
+ ___block_literal_global.210.10020
+ ___block_literal_global.21161
+ ___block_literal_global.21548
+ ___block_literal_global.21959
+ ___block_literal_global.22135
+ ___block_literal_global.223.14811
+ ___block_literal_global.22333
+ ___block_literal_global.22435
+ ___block_literal_global.2252
+ ___block_literal_global.22714
+ ___block_literal_global.228
+ ___block_literal_global.22901
+ ___block_literal_global.2308
+ ___block_literal_global.232
+ ___block_literal_global.2338
+ ___block_literal_global.2352
+ ___block_literal_global.23520
+ ___block_literal_global.23650
+ ___block_literal_global.238
+ ___block_literal_global.2407
+ ___block_literal_global.24078
+ ___block_literal_global.243
+ ___block_literal_global.2437
+ ___block_literal_global.247
+ ___block_literal_global.24986
+ ___block_literal_global.252
+ ___block_literal_global.25240
+ ___block_literal_global.25445
+ ___block_literal_global.25851
+ ___block_literal_global.259.24961
+ ___block_literal_global.261
+ ___block_literal_global.261.20805
+ ___block_literal_global.26361
+ ___block_literal_global.2670
+ ___block_literal_global.26811
+ ___block_literal_global.2688
+ ___block_literal_global.2705
+ ___block_literal_global.2733
+ ___block_literal_global.27721
+ ___block_literal_global.2775
+ ___block_literal_global.2802
+ ___block_literal_global.28439
+ ___block_literal_global.2866
+ ___block_literal_global.28709
+ ___block_literal_global.2893
+ ___block_literal_global.29007
+ ___block_literal_global.2905
+ ___block_literal_global.29262
+ ___block_literal_global.2932
+ ___block_literal_global.29561
+ ___block_literal_global.2965
+ ___block_literal_global.3.1783
+ ___block_literal_global.3.7859
+ ___block_literal_global.30078
+ ___block_literal_global.304.27545
+ ___block_literal_global.30458
+ ___block_literal_global.3052
+ ___block_literal_global.307
+ ___block_literal_global.30766
+ ___block_literal_global.308.8989
+ ___block_literal_global.319
+ ___block_literal_global.319.34552
+ ___block_literal_global.32136
+ ___block_literal_global.32504
+ ___block_literal_global.3269
+ ___block_literal_global.3296
+ ___block_literal_global.3313
+ ___block_literal_global.33173
+ ___block_literal_global.332
+ ___block_literal_global.33469
+ ___block_literal_global.3360
+ ___block_literal_global.3399
+ ___block_literal_global.34167
+ ___block_literal_global.34492
+ ___block_literal_global.345
+ ___block_literal_global.35182
+ ___block_literal_global.35273
+ ___block_literal_global.35695
+ ___block_literal_global.35840
+ ___block_literal_global.359
+ ___block_literal_global.3645
+ ___block_literal_global.36473
+ ___block_literal_global.36619
+ ___block_literal_global.3697
+ ___block_literal_global.37.35266
+ ___block_literal_global.37128
+ ___block_literal_global.37447
+ ___block_literal_global.3747
+ ___block_literal_global.3803
+ ___block_literal_global.38214
+ ___block_literal_global.3845
+ ___block_literal_global.3876
+ ___block_literal_global.3893
+ ___block_literal_global.3925
+ ___block_literal_global.3931
+ ___block_literal_global.39326
+ ___block_literal_global.3943
+ ___block_literal_global.3948
+ ___block_literal_global.3969
+ ___block_literal_global.39810
+ ___block_literal_global.3987
+ ___block_literal_global.3998
+ ___block_literal_global.4009
+ ___block_literal_global.450
+ ___block_literal_global.456
+ ___block_literal_global.459
+ ___block_literal_global.462
+ ___block_literal_global.4730
+ ___block_literal_global.4941
+ ___block_literal_global.51.7692
+ ___block_literal_global.5306
+ ___block_literal_global.549
+ ___block_literal_global.5520
+ ___block_literal_global.5668
+ ___block_literal_global.575
+ ___block_literal_global.6190
+ ___block_literal_global.684
+ ___block_literal_global.7097
+ ___block_literal_global.716
+ ___block_literal_global.741.27213
+ ___block_literal_global.7697
+ ___block_literal_global.77
+ ___block_literal_global.7854
+ ___block_literal_global.8099
+ ___block_literal_global.81.39790
+ ___block_literal_global.823.27211
+ ___block_literal_global.8877
+ ___block_literal_global.894.27166
+ ___block_literal_global.896.27164
+ ___block_literal_global.9556
+ ___copy_helper_block_e8_72n11_8_8_s0_t8w8
+ ___destroy_helper_block_e8_72n4_8_s0
+ __currentTimestampString.s_formatter.35267
+ __currentTimestampString.s_onceToken.35265
+ __unnamed_array_storage.10592
+ __unnamed_array_storage.1200
+ __unnamed_array_storage.12065
+ __unnamed_array_storage.13446
+ __unnamed_array_storage.14.8044
+ __unnamed_array_storage.16083
+ __unnamed_array_storage.162.35657
+ __unnamed_array_storage.1635
+ __unnamed_array_storage.16653
+ __unnamed_array_storage.18701
+ __unnamed_array_storage.19.8042
+ __unnamed_array_storage.20820
+ __unnamed_array_storage.21570
+ __unnamed_array_storage.249
+ __unnamed_array_storage.254
+ __unnamed_array_storage.26903
+ __unnamed_array_storage.2818
+ __unnamed_array_storage.29591
+ __unnamed_array_storage.30095
+ __unnamed_array_storage.30780
+ __unnamed_array_storage.30873
+ __unnamed_array_storage.317
+ __unnamed_array_storage.32143
+ __unnamed_array_storage.34565
+ __unnamed_array_storage.35709
+ __unnamed_array_storage.38901
+ __unnamed_array_storage.39239
+ __unnamed_array_storage.39784
+ __unnamed_array_storage.5643
+ __unnamed_array_storage.6177
+ __unnamed_array_storage.8032
+ __unnamed_array_storage.9006
+ __unnamed_array_storage.9326
+ _allowedEntities.pl_once_object_62
+ _allowedEntities.pl_once_object_63
+ _allowedEntities.pl_once_token_62
+ _allowedEntities.pl_once_token_63
+ _allowedInfoKeys.allowedKeys.13523
+ _allowedInfoKeys.allowedKeys.30262
+ _allowedInfoKeys.onceToken.13522
+ _allowedInfoKeys.onceToken.30261
+ _corePropertiesToFetch.array.16943
+ _corePropertiesToFetch.array.20955
+ _corePropertiesToFetch.array.24987
+ _corePropertiesToFetch.onceToken.16942
+ _corePropertiesToFetch.onceToken.20954
+ _corePropertiesToFetch.onceToken.24985
+ _defaultManager.onceToken.38522
+ _entityKeyMap.pl_once_object_0.24069
+ _entityKeyMap.pl_once_object_0.5525
+ _entityKeyMap.pl_once_object_0.8110
+ _entityKeyMap.pl_once_object_2.20949
+ _entityKeyMap.pl_once_object_2.26801
+ _entityKeyMap.pl_once_object_2.30110
+ _entityKeyMap.pl_once_object_2.33193
+ _entityKeyMap.pl_once_object_2.34483
+ _entityKeyMap.pl_once_object_2.35837
+ _entityKeyMap.pl_once_object_2.7679
+ _entityKeyMap.pl_once_object_2.9545
+ _entityKeyMap.pl_once_object_2.9762
+ _entityKeyMap.pl_once_object_3.24976
+ _entityKeyMap.pl_once_object_3.39798
+ _entityKeyMap.pl_once_token_0.24068
+ _entityKeyMap.pl_once_token_0.5524
+ _entityKeyMap.pl_once_token_0.8109
+ _entityKeyMap.pl_once_token_2.20948
+ _entityKeyMap.pl_once_token_2.26800
+ _entityKeyMap.pl_once_token_2.30109
+ _entityKeyMap.pl_once_token_2.33192
+ _entityKeyMap.pl_once_token_2.34482
+ _entityKeyMap.pl_once_token_2.35836
+ _entityKeyMap.pl_once_token_2.7678
+ _entityKeyMap.pl_once_token_2.9544
+ _entityKeyMap.pl_once_token_2.9761
+ _entityKeyMap.pl_once_token_3.24975
+ _entityKeyMap.pl_once_token_3.39797
+ _getCKMediaItemMakerClass
+ _identifierPropertiesToFetch.array.25852
+ _identifierPropertiesToFetch.onceToken.25850
+ _objc_msgSend$_lock_clearOIDCache
+ _objc_msgSend$_lock_hasChangeObservers
+ _objc_msgSend$_lock_pauseChangeHandlingIfNeeded
+ _objc_msgSend$_lock_resumeChangeHandlingIfNeeded
+ _objc_msgSend$addObservers:authorizationStatus:
+ _objc_msgSend$beginProcessPendingChanges
+ _objc_msgSend$changeHandlingActiveStateDidChange:
+ _objc_msgSend$checkAuthorizationStatusForAPIAccessLevel:suppressPrompt:
+ _objc_msgSend$countOfRegisteredFetchResults
+ _objc_msgSend$deletedCount
+ _objc_msgSend$distributeExternalTimestamp
+ _objc_msgSend$distributeInternalTimestamp
+ _objc_msgSend$endProcessPendingChanges
+ _objc_msgSend$endTimestamp
+ _objc_msgSend$exportVideoFileForTimeRange:fromVideoMediaItemMakerData:forAssetUuid:toOutputFileURL:fingerPrint:signpostId:completion:
+ _objc_msgSend$externalObserversCount
+ _objc_msgSend$fetchResultCount
+ _objc_msgSend$fileTypeForOutputURL:
+ _objc_msgSend$getObserversWithBlock:
+ _objc_msgSend$getReturnValue:
+ _objc_msgSend$initWithLibraryBundle:changeHandlingDebugger:uniqueObjectIDCache:
+ _objc_msgSend$initWithMaxPreviousEvents:
+ _objc_msgSend$initWithProvider:
+ _objc_msgSend$initWithStartTimestamp:
+ _objc_msgSend$insertedCount
+ _objc_msgSend$internalObserversCount
+ _objc_msgSend$invocationWithMethodSignature:
+ _objc_msgSend$invoke
+ _objc_msgSend$isNetworkVolume
+ _objc_msgSend$mediaItemURLForAssetUuid:fingerPrint:outOfBandPresentationHints:
+ _objc_msgSend$methodSignatureForSelector:
+ _objc_msgSend$outputURL
+ _objc_msgSend$postsPersistentHistoryChangedNotifications
+ _objc_msgSend$redactedDescriptionForFileURL:
+ _objc_msgSend$reset
+ _objc_msgSend$setArgument:atIndex:
+ _objc_msgSend$setDeletedCount:
+ _objc_msgSend$setDistributeExternalTimestamp:
+ _objc_msgSend$setDistributeInternalTimestamp:
+ _objc_msgSend$setEndTimestamp:
+ _objc_msgSend$setExternalObserversCount:
+ _objc_msgSend$setFetchResultCount:
+ _objc_msgSend$setInsertedCount:
+ _objc_msgSend$setInternalObserversCount:
+ _objc_msgSend$setPostsPersistentHistoryChangedNotifications:
+ _objc_msgSend$setQosClass:
+ _objc_msgSend$setSelector:
+ _objc_msgSend$setStartTimestamp:
+ _objc_msgSend$setTarget:
+ _objc_msgSend$setUnknownMergeEvent:
+ _objc_msgSend$setUpdatedCount:
+ _objc_msgSend$startDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:needsDownload:shouldApplyTimeRange:reply:
+ _objc_msgSend$startExportSession:assetUuid:signpostId:completion:
+ _objc_msgSend$startTimestamp
+ _objc_msgSend$startWalrusTimeRangeDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:partialVideoURL:reply:
+ _objc_msgSend$stateCaptureDictionary
+ _objc_msgSend$stringFromRelativeTimeInterval:
+ _objc_msgSend$stringFromTimestamp:
+ _objc_msgSend$systemSymbolName
+ _objc_msgSend$typeForFilenameExtensionOrLastPathComponent:
+ _objc_msgSend$unknownMergeEvent
+ _objc_msgSend$updatedCount
+ _propertiesToFetchWithHint:.array.17377
+ _propertiesToFetchWithHint:.array.24079
+ _propertiesToFetchWithHint:.array.26812
+ _propertiesToFetchWithHint:.array.30131
+ _propertiesToFetchWithHint:.array.34493
+ _propertiesToFetchWithHint:.array.35841
+ _propertiesToFetchWithHint:.array.37016
+ _propertiesToFetchWithHint:.array.37754
+ _propertiesToFetchWithHint:.array.5550
+ _propertiesToFetchWithHint:.array.7688
+ _propertiesToFetchWithHint:.array.8117
+ _propertiesToFetchWithHint:.array.9787
+ _propertiesToFetchWithHint:.onceToken.16936
+ _propertiesToFetchWithHint:.onceToken.17376
+ _propertiesToFetchWithHint:.onceToken.20957
+ _propertiesToFetchWithHint:.onceToken.24077
+ _propertiesToFetchWithHint:.onceToken.24981
+ _propertiesToFetchWithHint:.onceToken.26810
+ _propertiesToFetchWithHint:.onceToken.2865
+ _propertiesToFetchWithHint:.onceToken.30130
+ _propertiesToFetchWithHint:.onceToken.34491
+ _propertiesToFetchWithHint:.onceToken.35839
+ _propertiesToFetchWithHint:.onceToken.37015
+ _propertiesToFetchWithHint:.onceToken.37753
+ _propertiesToFetchWithHint:.onceToken.5549
+ _propertiesToFetchWithHint:.onceToken.7687
+ _propertiesToFetchWithHint:.onceToken.8116
+ _propertiesToFetchWithHint:.onceToken.9555
+ _propertiesToFetchWithHint:.onceToken.9786
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.16938
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.20960
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.24983
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.9558
+ _propertiesToFetchWithHint:.propertyQueue.16937
+ _propertiesToFetchWithHint:.propertyQueue.20959
+ _propertiesToFetchWithHint:.propertyQueue.24982
+ _propertiesToFetchWithHint:.propertyQueue.9557
+ _propertiesToPrefetch.onceToken.16472
+ _propertiesToPrefetch.onceToken.20632
+ _propertiesToPrefetch.onceToken.24686
+ _propertiesToPrefetch.propertiesToPrefetch.16473
+ _propertiesToPrefetch.propertiesToPrefetch.20633
+ _propertiesToPrefetch.propertiesToPrefetch.24687
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.20806
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.24948
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.9274
+ _propertySetAccessorsByPropertySet.onceToken.20804
+ _propertySetAccessorsByPropertySet.onceToken.24947
+ _propertySetAccessorsByPropertySet.onceToken.9273
+ _propertySetClassForPropertySet:.onceToken.20812
+ _propertySetClassForPropertySet:.onceToken.24956
+ _propertySetClassForPropertySet:.onceToken.9275
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.20813
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.24957
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.9276
+ _sharedDecoder.s_onceToken.37127
+ _sharedDecoder.s_shared.37129
+ _transformValueExpression:forKeyPath:._passThroughSet.16909
+ _transformValueExpression:forKeyPath:._passThroughSet.20941
+ _transformValueExpression:forKeyPath:._passThroughSet.24060
+ _transformValueExpression:forKeyPath:._passThroughSet.24964
+ _transformValueExpression:forKeyPath:._passThroughSet.26795
+ _transformValueExpression:forKeyPath:._passThroughSet.2854
+ _transformValueExpression:forKeyPath:._passThroughSet.30099
+ _transformValueExpression:forKeyPath:._passThroughSet.33178
+ _transformValueExpression:forKeyPath:._passThroughSet.34474
+ _transformValueExpression:forKeyPath:._passThroughSet.35834
+ _transformValueExpression:forKeyPath:._passThroughSet.39758
+ _transformValueExpression:forKeyPath:._passThroughSet.7652
+ _transformValueExpression:forKeyPath:._passThroughSet.8106
+ _transformValueExpression:forKeyPath:._passThroughSet.9540
+ _transformValueExpression:forKeyPath:._passThroughSet.9743
+ _transformValueExpression:forKeyPath:.onceToken.16908
+ _transformValueExpression:forKeyPath:.onceToken.20940
+ _transformValueExpression:forKeyPath:.onceToken.24059
+ _transformValueExpression:forKeyPath:.onceToken.24963
+ _transformValueExpression:forKeyPath:.onceToken.26794
+ _transformValueExpression:forKeyPath:.onceToken.2853
+ _transformValueExpression:forKeyPath:.onceToken.30098
+ _transformValueExpression:forKeyPath:.onceToken.33177
+ _transformValueExpression:forKeyPath:.onceToken.34473
+ _transformValueExpression:forKeyPath:.onceToken.35833
+ _transformValueExpression:forKeyPath:.onceToken.39757
+ _transformValueExpression:forKeyPath:.onceToken.7651
+ _transformValueExpression:forKeyPath:.onceToken.8105
+ _transformValueExpression:forKeyPath:.onceToken.9539
+ _transformValueExpression:forKeyPath:.onceToken.9742
+ _uniqueObjectIDCache.pl_once_object_61
+ _uniqueObjectIDCache.pl_once_token_61
- +[PHPhotoLibrary _checkAuthorizationStatusForAPIAccessLevel:suppressPrompt:]
- -[PHPhotoLibrary _hasChangeObservers]
- -[PHPhotoLibrary _pauseChangeHandlingIfNeeded]
- -[PHPhotoLibrary _resumeChangeHandlingIfNeeded]
- -[PHPhotoLibrary externalChangeObservers]
- -[PHPhotoLibrary fetchResultsRegisteredForChangeNotifications]
- -[PHPhotoLibrary internalChangeObservers]
- -[PHPhotoLibrary isChangeHandlingActive]
- -[PHPhotoLibrary isChangeHandlingAuthorized]
- -[PHPhotoLibrary setExternalChangeObservers:]
- -[PHPhotoLibrary setFetchResultsRegisteredForChangeNotifications:]
- -[PHPhotoLibrary setInternalChangeObservers:]
- -[PHPhotoLibrary setIsChangeHandlingActive:]
- -[PHPhotoLibrary setIsChangeHandlingAuthorized:]
- GCC_except_table10094
- GCC_except_table10165
- GCC_except_table10190
- GCC_except_table10224
- GCC_except_table10234
- GCC_except_table10252
- GCC_except_table10267
- GCC_except_table10306
- GCC_except_table10310
- GCC_except_table10329
- GCC_except_table1044
- GCC_except_table1092
- GCC_except_table1216
- GCC_except_table1219
- GCC_except_table1232
- GCC_except_table1424
- GCC_except_table1428
- GCC_except_table1430
- GCC_except_table1432
- GCC_except_table1434
- GCC_except_table1436
- GCC_except_table1438
- GCC_except_table1441
- GCC_except_table1450
- GCC_except_table1453
- GCC_except_table1465
- GCC_except_table1497
- GCC_except_table1499
- GCC_except_table1501
- GCC_except_table1503
- GCC_except_table1505
- GCC_except_table1507
- GCC_except_table1509
- GCC_except_table1511
- GCC_except_table1513
- GCC_except_table1515
- GCC_except_table1517
- GCC_except_table1519
- GCC_except_table1521
- GCC_except_table1523
- GCC_except_table1530
- GCC_except_table1532
- GCC_except_table1534
- GCC_except_table1536
- GCC_except_table1538
- GCC_except_table1546
- GCC_except_table1548
- GCC_except_table1550
- GCC_except_table1581
- GCC_except_table1584
- GCC_except_table1633
- GCC_except_table1638
- GCC_except_table1646
- GCC_except_table1648
- GCC_except_table1660
- GCC_except_table1831
- GCC_except_table1836
- GCC_except_table1890
- GCC_except_table1998
- GCC_except_table2069
- GCC_except_table2072
- GCC_except_table2074
- GCC_except_table2086
- GCC_except_table2097
- GCC_except_table2099
- GCC_except_table2102
- GCC_except_table2235
- GCC_except_table2239
- GCC_except_table2301
- GCC_except_table2309
- GCC_except_table2338
- GCC_except_table2342
- GCC_except_table2347
- GCC_except_table2426
- GCC_except_table2458
- GCC_except_table2464
- GCC_except_table2467
- GCC_except_table2477
- GCC_except_table2481
- GCC_except_table2487
- GCC_except_table2490
- GCC_except_table2494
- GCC_except_table2498
- GCC_except_table2509
- GCC_except_table2514
- GCC_except_table2526
- GCC_except_table2542
- GCC_except_table2644
- GCC_except_table2667
- GCC_except_table2669
- GCC_except_table2671
- GCC_except_table2714
- GCC_except_table2737
- GCC_except_table2770
- GCC_except_table2774
- GCC_except_table2777
- GCC_except_table2923
- GCC_except_table2956
- GCC_except_table2964
- GCC_except_table2974
- GCC_except_table2977
- GCC_except_table2979
- GCC_except_table3004
- GCC_except_table3010
- GCC_except_table3256
- GCC_except_table3261
- GCC_except_table3287
- GCC_except_table3298
- GCC_except_table3302
- GCC_except_table3307
- GCC_except_table3318
- GCC_except_table3323
- GCC_except_table3336
- GCC_except_table3399
- GCC_except_table3657
- GCC_except_table3658
- GCC_except_table3665
- GCC_except_table3695
- GCC_except_table3697
- GCC_except_table3760
- GCC_except_table3784
- GCC_except_table4235
- GCC_except_table4288
- GCC_except_table4315
- GCC_except_table4376
- GCC_except_table4381
- GCC_except_table4397
- GCC_except_table4416
- GCC_except_table4419
- GCC_except_table4422
- GCC_except_table4435
- GCC_except_table4480
- GCC_except_table4491
- GCC_except_table4531
- GCC_except_table4557
- GCC_except_table4560
- GCC_except_table4566
- GCC_except_table4571
- GCC_except_table4594
- GCC_except_table4621
- GCC_except_table4647
- GCC_except_table4649
- GCC_except_table4660
- GCC_except_table4698
- GCC_except_table4769
- GCC_except_table4774
- GCC_except_table4892
- GCC_except_table4895
- GCC_except_table4908
- GCC_except_table4927
- GCC_except_table4940
- GCC_except_table4970
- GCC_except_table5004
- GCC_except_table5006
- GCC_except_table5310
- GCC_except_table5323
- GCC_except_table5336
- GCC_except_table5351
- GCC_except_table5377
- GCC_except_table5380
- GCC_except_table5382
- GCC_except_table5384
- GCC_except_table5386
- GCC_except_table5417
- GCC_except_table5450
- GCC_except_table5452
- GCC_except_table5486
- GCC_except_table5675
- GCC_except_table5832
- GCC_except_table6025
- GCC_except_table6094
- GCC_except_table6116
- GCC_except_table6120
- GCC_except_table6126
- GCC_except_table6177
- GCC_except_table6282
- GCC_except_table6284
- GCC_except_table6329
- GCC_except_table6365
- GCC_except_table6369
- GCC_except_table6371
- GCC_except_table6373
- GCC_except_table6390
- GCC_except_table6426
- GCC_except_table6449
- GCC_except_table6536
- GCC_except_table6539
- GCC_except_table6557
- GCC_except_table6594
- GCC_except_table6617
- GCC_except_table6635
- GCC_except_table6695
- GCC_except_table6772
- GCC_except_table6901
- GCC_except_table6906
- GCC_except_table7191
- GCC_except_table7201
- GCC_except_table7232
- GCC_except_table7295
- GCC_except_table7370
- GCC_except_table7372
- GCC_except_table7456
- GCC_except_table7530
- GCC_except_table7548
- GCC_except_table7633
- GCC_except_table7647
- GCC_except_table7656
- GCC_except_table7676
- GCC_except_table7677
- GCC_except_table7678
- GCC_except_table7679
- GCC_except_table7680
- GCC_except_table7681
- GCC_except_table7682
- GCC_except_table7684
- GCC_except_table7685
- GCC_except_table7686
- GCC_except_table7688
- GCC_except_table7689
- GCC_except_table7690
- GCC_except_table7691
- GCC_except_table7692
- GCC_except_table7693
- GCC_except_table7694
- GCC_except_table7695
- GCC_except_table7697
- GCC_except_table7698
- GCC_except_table7699
- GCC_except_table7700
- GCC_except_table7701
- GCC_except_table7702
- GCC_except_table7714
- GCC_except_table7723
- GCC_except_table7846
- GCC_except_table7855
- GCC_except_table7856
- GCC_except_table7857
- GCC_except_table7858
- GCC_except_table7859
- GCC_except_table7878
- GCC_except_table7897
- GCC_except_table7898
- GCC_except_table7899
- GCC_except_table7903
- GCC_except_table7927
- GCC_except_table7928
- GCC_except_table7929
- GCC_except_table7931
- GCC_except_table7932
- GCC_except_table7961
- GCC_except_table7965
- GCC_except_table7984
- GCC_except_table7989
- GCC_except_table8056
- GCC_except_table8146
- GCC_except_table8211
- GCC_except_table8249
- GCC_except_table830
- GCC_except_table8326
- GCC_except_table8345
- GCC_except_table847
- GCC_except_table8918
- GCC_except_table8937
- GCC_except_table8939
- GCC_except_table8941
- GCC_except_table8943
- GCC_except_table8973
- GCC_except_table9032
- GCC_except_table9132
- GCC_except_table9144
- GCC_except_table9183
- GCC_except_table9185
- GCC_except_table9198
- GCC_except_table9233
- GCC_except_table9237
- GCC_except_table9275
- GCC_except_table9279
- GCC_except_table9288
- GCC_except_table9289
- GCC_except_table9333
- GCC_except_table9340
- GCC_except_table9442
- GCC_except_table9448
- GCC_except_table9450
- GCC_except_table9496
- GCC_except_table9512
- GCC_except_table9522
- GCC_except_table9604
- GCC_except_table9692
- GCC_except_table9696
- GCC_except_table9700
- GCC_except_table972
- GCC_except_table9728
- GCC_except_table988
- _OBJC_IVAR_$_PHPhotoLibrary._externalChangeObservers
- _OBJC_IVAR_$_PHPhotoLibrary._fetchResultsRegisteredForChangeNotifications
- _OBJC_IVAR_$_PHPhotoLibrary._internalChangeObservers
- _OBJC_IVAR_$_PHPhotoLibrary._isChangeHandlingActive
- _OBJC_IVAR_$_PHPhotoLibrary._isChangeHandlingAuthorized
- _OBJC_IVAR_$_PHPhotoLibrary._postsPersistentHistoryChangedNotifications
- _PLResourceRecipeIDIsDeferredProcessing
- __OBJC_$_CLASS_PROP_LIST_PHAssetPropertySet.2206
- __OBJC_$_CLASS_PROP_LIST_PHFacePropertySet.673
- __OBJC_$_CLASS_PROP_LIST_PHMemoryPropertySet.1209
- __OBJC_$_CLASS_PROP_LIST_PHPersonPropertySet.519
- __OBJC_$_PROP_LIST_PHAssetPropertySet.2213
- __OBJC_$_PROP_LIST_PHAssetResourceRequest.262
- __OBJC_$_PROP_LIST_PHChangeRequest.167
- __OBJC_$_PROP_LIST_PHImportExceptionRecorder.83
- __OBJC_$_PROP_LIST_PHShare.123
- __OBJC_$_PROP_LIST_PHThumbnailAsset.145
- ___103-[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:reply:]_block_invoke.261
- ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke.105
- ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke_2.106
- ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke_3.108
- ___34-[PHPhotoLibrary _removeObserver:]_block_invoke
- ___38+[PHPerson propertiesToFetchWithHint:]_block_invoke.99
- ___38-[PHPhotoLibrary registerFetchResult:]_block_invoke
- ___40-[PHPhotoLibrary unregisterFetchResult:]_block_invoke
- ___40-[PHPhotoLibrary unregisterFetchResult:]_block_invoke_2
- ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke.221
- ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_2.222
- ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_3.223
- ___52-[PHPhotoLibrary _addObservers:authorizationStatus:]_block_invoke
- ___60-[PHPhotoLibrary postsPersistentHistoryChangedNotifications]_block_invoke
- ___63-[PHImageManager requestAVProxyForAsset:options:resultHandler:]_block_invoke.647
- ___64-[PHPhotoLibrary setPostsPersistentHistoryChangedNotifications:]_block_invoke
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.589
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.593
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.596
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_2.594
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_2.598
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_3.595
- ___76-[PHServerResourceRequestRunner makeResourceUnavailableWithRequest:library:]_block_invoke.100
- ___83-[PHImageManager requestContentEditingInputForAsset:withOptions:completionHandler:]_block_invoke.630
- ___85-[PHServerResourceRequestRunner chooseVideoWithRequest:library:clientBundleID:reply:]_block_invoke.119
- ___85-[PHServerResourceRequestRunner chooseVideoWithRequest:library:clientBundleID:reply:]_block_invoke.123
- ___85-[PHServerResourceRequestRunner chooseVideoWithRequest:library:clientBundleID:reply:]_block_invoke.131
- ___85-[PHServerResourceRequestRunner chooseVideoWithRequest:library:clientBundleID:reply:]_block_invoke.133
- ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.566
- ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.569
- ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.574
- ___89-[PHImageManager requestNewCGImageForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.619
- ___95-[PHServerResourceRequestRunner makeResourceAvailableWithRequest:library:clientBundleID:reply:]_block_invoke.80
- ___95-[PHServerResourceRequestRunner makeResourceAvailableWithRequest:library:clientBundleID:reply:]_block_invoke.91
- ___95-[PHServerResourceRequestRunner makeResourceAvailableWithRequest:library:clientBundleID:reply:]_block_invoke_2.85
- ___95-[PHServerResourceRequestRunner makeResourceAvailableWithRequest:library:clientBundleID:reply:]_block_invoke_2.95
- ___95-[PHServerResourceRequestRunner makeResourceAvailableWithRequest:library:clientBundleID:reply:]_block_invoke_3.96
- ___Block_byref_object_copy_.10310
- ___Block_byref_object_copy_.10930
- ___Block_byref_object_copy_.1192
- ___Block_byref_object_copy_.13063
- ___Block_byref_object_copy_.14621
- ___Block_byref_object_copy_.1466
- ___Block_byref_object_copy_.14783
- ___Block_byref_object_copy_.15078
- ___Block_byref_object_copy_.15546
- ___Block_byref_object_copy_.16147
- ___Block_byref_object_copy_.16305
- ___Block_byref_object_copy_.1789
- ___Block_byref_object_copy_.18263
- ___Block_byref_object_copy_.19405
- ___Block_byref_object_copy_.19911
- ___Block_byref_object_copy_.20248
- ___Block_byref_object_copy_.20516
- ___Block_byref_object_copy_.2124
- ___Block_byref_object_copy_.21391
- ___Block_byref_object_copy_.21703
- ___Block_byref_object_copy_.22493
- ___Block_byref_object_copy_.23095
- ___Block_byref_object_copy_.24498
- ___Block_byref_object_copy_.25084
- ___Block_byref_object_copy_.2529
- ___Block_byref_object_copy_.25894
- ___Block_byref_object_copy_.26141
- ___Block_byref_object_copy_.27136
- ___Block_byref_object_copy_.27586
- ___Block_byref_object_copy_.28691
- ___Block_byref_object_copy_.29172
- ___Block_byref_object_copy_.32563
- ___Block_byref_object_copy_.32797
- ___Block_byref_object_copy_.33717
- ___Block_byref_object_copy_.34100
- ___Block_byref_object_copy_.34276
- ___Block_byref_object_copy_.34562
- ___Block_byref_object_copy_.3513
- ___Block_byref_object_copy_.35244
- ___Block_byref_object_copy_.36146
- ___Block_byref_object_copy_.36255
- ___Block_byref_object_copy_.38031
- ___Block_byref_object_copy_.38318
- ___Block_byref_object_copy_.38837
- ___Block_byref_object_copy_.4519
- ___Block_byref_object_copy_.4758
- ___Block_byref_object_copy_.5881
- ___Block_byref_object_copy_.6876
- ___Block_byref_object_copy_.7474
- ___Block_byref_object_copy_.7680
- ___Block_byref_object_copy_.7846
- ___Block_byref_object_copy_.8420
- ___Block_byref_object_copy_.8661
- ___Block_byref_object_copy_.9114
- ___Block_byref_object_copy_.9510
- ___Block_byref_object_dispose_.10311
- ___Block_byref_object_dispose_.10931
- ___Block_byref_object_dispose_.1193
- ___Block_byref_object_dispose_.13064
- ___Block_byref_object_dispose_.14622
- ___Block_byref_object_dispose_.1467
- ___Block_byref_object_dispose_.14784
- ___Block_byref_object_dispose_.15079
- ___Block_byref_object_dispose_.15547
- ___Block_byref_object_dispose_.16148
- ___Block_byref_object_dispose_.16306
- ___Block_byref_object_dispose_.1790
- ___Block_byref_object_dispose_.18264
- ___Block_byref_object_dispose_.19406
- ___Block_byref_object_dispose_.19912
- ___Block_byref_object_dispose_.20249
- ___Block_byref_object_dispose_.20517
- ___Block_byref_object_dispose_.2125
- ___Block_byref_object_dispose_.21392
- ___Block_byref_object_dispose_.21704
- ___Block_byref_object_dispose_.22494
- ___Block_byref_object_dispose_.23096
- ___Block_byref_object_dispose_.24499
- ___Block_byref_object_dispose_.25085
- ___Block_byref_object_dispose_.2530
- ___Block_byref_object_dispose_.25895
- ___Block_byref_object_dispose_.26142
- ___Block_byref_object_dispose_.27137
- ___Block_byref_object_dispose_.27587
- ___Block_byref_object_dispose_.28692
- ___Block_byref_object_dispose_.29173
- ___Block_byref_object_dispose_.32564
- ___Block_byref_object_dispose_.32798
- ___Block_byref_object_dispose_.33718
- ___Block_byref_object_dispose_.34101
- ___Block_byref_object_dispose_.34277
- ___Block_byref_object_dispose_.34563
- ___Block_byref_object_dispose_.3514
- ___Block_byref_object_dispose_.35245
- ___Block_byref_object_dispose_.36147
- ___Block_byref_object_dispose_.36256
- ___Block_byref_object_dispose_.38032
- ___Block_byref_object_dispose_.38319
- ___Block_byref_object_dispose_.38838
- ___Block_byref_object_dispose_.4520
- ___Block_byref_object_dispose_.4759
- ___Block_byref_object_dispose_.5882
- ___Block_byref_object_dispose_.6877
- ___Block_byref_object_dispose_.7475
- ___Block_byref_object_dispose_.7681
- ___Block_byref_object_dispose_.7847
- ___Block_byref_object_dispose_.8421
- ___Block_byref_object_dispose_.8662
- ___Block_byref_object_dispose_.9115
- ___Block_byref_object_dispose_.9511
- ____fetchNonHintResources_block_invoke.174
- ___block_descriptor_72_e8_32s40r48r56n11_8_8_s0_t8w8_e18_v16?0"PHChange"8l
- ___block_descriptor_80_e8_32s40r48r56r64r72r_e5_v8?0lr40l8s32l8r48l8r56l8r64l8r72l8
- ___block_descriptor_93_e8_32s40s48s56s64s72bs_e30_v32?0"NSError"8q16"NSURL"24ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.10000
- ___block_literal_global.102
- ___block_literal_global.103
- ___block_literal_global.10365
- ___block_literal_global.1044
- ___block_literal_global.1053.16033
- ___block_literal_global.1068
- ___block_literal_global.1086
- ___block_literal_global.112.30480
- ___block_literal_global.1194
- ___block_literal_global.1232
- ___block_literal_global.12576
- ___block_literal_global.13096
- ___block_literal_global.131.28696
- ___block_literal_global.13150
- ___block_literal_global.136
- ___block_literal_global.14291
- ___block_literal_global.143
- ___block_literal_global.14615
- ___block_literal_global.1486
- ___block_literal_global.15034
- ___block_literal_global.157
- ___block_literal_global.15969
- ___block_literal_global.160
- ___block_literal_global.16820
- ___block_literal_global.17576
- ___block_literal_global.1786
- ___block_literal_global.18607
- ___block_literal_global.19094
- ___block_literal_global.1946
- ___block_literal_global.19602
- ___block_literal_global.200.15824
- ___block_literal_global.20225
- ___block_literal_global.20816
- ___block_literal_global.210.9814
- ___block_literal_global.21016
- ___block_literal_global.21403
- ___block_literal_global.21814
- ___block_literal_global.21985
- ___block_literal_global.2207
- ___block_literal_global.22126
- ___block_literal_global.22228
- ___block_literal_global.223.14616
- ___block_literal_global.225.24775
- ___block_literal_global.22505
- ___block_literal_global.2251
- ___block_literal_global.22693
- ___block_literal_global.229.24773
- ___block_literal_global.230.8696
- ___block_literal_global.23312
- ___block_literal_global.2337
- ___block_literal_global.23441
- ___block_literal_global.235
- ___block_literal_global.2351
- ___block_literal_global.23867
- ___block_literal_global.240
- ___block_literal_global.2406
- ___block_literal_global.2436
- ___block_literal_global.244
- ___block_literal_global.24778
- ___block_literal_global.249
- ___block_literal_global.25032
- ___block_literal_global.25235
- ___block_literal_global.256
- ___block_literal_global.25635
- ___block_literal_global.258.20663
- ___block_literal_global.26146
- ___block_literal_global.263
- ___block_literal_global.26594
- ___block_literal_global.2669
- ___block_literal_global.2687
- ___block_literal_global.2704
- ___block_literal_global.2732
- ___block_literal_global.27452
- ___block_literal_global.2752
- ___block_literal_global.2774
- ___block_literal_global.2790
- ___block_literal_global.2801
- ___block_literal_global.28168
- ___block_literal_global.28440
- ___block_literal_global.28735
- ___block_literal_global.2892
- ___block_literal_global.28986
- ___block_literal_global.29284
- ___block_literal_global.2931
- ___block_literal_global.2964
- ___block_literal_global.29801
- ___block_literal_global.3.1784
- ___block_literal_global.3.7701
- ___block_literal_global.30178
- ___block_literal_global.304.27284
- ___block_literal_global.30486
- ___block_literal_global.3051
- ___block_literal_global.308.8817
- ___block_literal_global.309
- ___block_literal_global.3164
- ___block_literal_global.318
- ___block_literal_global.31856
- ___block_literal_global.321
- ___block_literal_global.3228
- ___block_literal_global.3268
- ___block_literal_global.32815
- ___block_literal_global.331
- ___block_literal_global.33110
- ___block_literal_global.3312
- ___block_literal_global.33804
- ___block_literal_global.3398
- ___block_literal_global.34129
- ___block_literal_global.346
- ___block_literal_global.34815
- ___block_literal_global.34906
- ___block_literal_global.35331
- ___block_literal_global.35476
- ___block_literal_global.358
- ___block_literal_global.36111
- ___block_literal_global.36257
- ___block_literal_global.3644
- ___block_literal_global.36766
- ___block_literal_global.3696
- ___block_literal_global.37.34899
- ___block_literal_global.3746
- ___block_literal_global.37783
- ___block_literal_global.3802
- ___block_literal_global.3844
- ___block_literal_global.3875
- ___block_literal_global.38909
- ___block_literal_global.3892
- ___block_literal_global.3924
- ___block_literal_global.3930
- ___block_literal_global.39392
- ___block_literal_global.3942
- ___block_literal_global.3947
- ___block_literal_global.3968
- ___block_literal_global.3986
- ___block_literal_global.3997
- ___block_literal_global.4008
- ___block_literal_global.451
- ___block_literal_global.457
- ___block_literal_global.4588
- ___block_literal_global.460
- ___block_literal_global.463
- ___block_literal_global.4808
- ___block_literal_global.51.7536
- ___block_literal_global.5173
- ___block_literal_global.5388
- ___block_literal_global.541
- ___block_literal_global.5533
- ___block_literal_global.574
- ___block_literal_global.6061
- ___block_literal_global.683.27188
- ___block_literal_global.6941
- ___block_literal_global.714
- ___block_literal_global.741.26997
- ___block_literal_global.7541
- ___block_literal_global.7696
- ___block_literal_global.7939
- ___block_literal_global.81.39372
- ___block_literal_global.823.26995
- ___block_literal_global.8715
- ___block_literal_global.894.26950
- ___block_literal_global.896.26948
- ___block_literal_global.9347
- ___copy_helper_block_e8_56n11_8_8_s0_t8w8
- ___destroy_helper_block_e8_56n4_8_s0
- __currentTimestampString.s_formatter.34900
- __currentTimestampString.s_onceToken.34898
- __unnamed_array_storage.10388
- __unnamed_array_storage.11862
- __unnamed_array_storage.1198
- __unnamed_array_storage.13235
- __unnamed_array_storage.14.7884
- __unnamed_array_storage.15941
- __unnamed_array_storage.162.35293
- __unnamed_array_storage.1636
- __unnamed_array_storage.16509
- __unnamed_array_storage.18574
- __unnamed_array_storage.19.7882
- __unnamed_array_storage.20680
- __unnamed_array_storage.21426
- __unnamed_array_storage.246.35198
- __unnamed_array_storage.251
- __unnamed_array_storage.26686
- __unnamed_array_storage.2698
- __unnamed_array_storage.29314
- __unnamed_array_storage.29816
- __unnamed_array_storage.30500
- __unnamed_array_storage.30593
- __unnamed_array_storage.31863
- __unnamed_array_storage.319
- __unnamed_array_storage.34200
- __unnamed_array_storage.35345
- __unnamed_array_storage.38486
- __unnamed_array_storage.38821
- __unnamed_array_storage.39366
- __unnamed_array_storage.5508
- __unnamed_array_storage.6048
- __unnamed_array_storage.7872
- __unnamed_array_storage.8828
- __unnamed_array_storage.9155
- _allowedEntities.pl_once_object_65
- _allowedEntities.pl_once_object_66
- _allowedEntities.pl_once_token_65
- _allowedEntities.pl_once_token_66
- _allowedInfoKeys.allowedKeys.13312
- _allowedInfoKeys.allowedKeys.29983
- _allowedInfoKeys.onceToken.13311
- _allowedInfoKeys.onceToken.29982
- _corePropertiesToFetch.array.16823
- _corePropertiesToFetch.array.20813
- _corePropertiesToFetch.array.24779
- _corePropertiesToFetch.onceToken.16822
- _corePropertiesToFetch.onceToken.20812
- _corePropertiesToFetch.onceToken.24777
- _defaultManager.onceToken.38108
- _entityKeyMap.pl_once_object_0.23858
- _entityKeyMap.pl_once_object_0.5393
- _entityKeyMap.pl_once_object_0.7950
- _entityKeyMap.pl_once_object_2.20807
- _entityKeyMap.pl_once_object_2.26584
- _entityKeyMap.pl_once_object_2.29831
- _entityKeyMap.pl_once_object_2.32835
- _entityKeyMap.pl_once_object_2.34120
- _entityKeyMap.pl_once_object_2.35473
- _entityKeyMap.pl_once_object_2.7520
- _entityKeyMap.pl_once_object_2.9339
- _entityKeyMap.pl_once_object_2.9551
- _entityKeyMap.pl_once_object_3.24764
- _entityKeyMap.pl_once_object_3.39380
- _entityKeyMap.pl_once_token_0.23857
- _entityKeyMap.pl_once_token_0.5392
- _entityKeyMap.pl_once_token_0.7949
- _entityKeyMap.pl_once_token_2.20806
- _entityKeyMap.pl_once_token_2.26583
- _entityKeyMap.pl_once_token_2.29830
- _entityKeyMap.pl_once_token_2.32834
- _entityKeyMap.pl_once_token_2.34119
- _entityKeyMap.pl_once_token_2.35472
- _entityKeyMap.pl_once_token_2.7519
- _entityKeyMap.pl_once_token_2.9338
- _entityKeyMap.pl_once_token_2.9550
- _entityKeyMap.pl_once_token_3.24763
- _entityKeyMap.pl_once_token_3.39379
- _identifierPropertiesToFetch.array.25636
- _identifierPropertiesToFetch.onceToken.25634
- _objc_msgSend$_checkAuthorizationStatusForAPIAccessLevel:suppressPrompt:
- _objc_msgSend$_hasChangeObservers
- _objc_msgSend$_pauseChangeHandlingIfNeeded
- _objc_msgSend$_resumeChangeHandlingIfNeeded
- _objc_msgSend$clearsOIDCacheAfterFetchResultDealloc
- _objc_msgSend$removeAllUniquedOIDs
- _os_transaction_create
- _propertiesToFetchWithHint:.array.17256
- _propertiesToFetchWithHint:.array.23868
- _propertiesToFetchWithHint:.array.26595
- _propertiesToFetchWithHint:.array.29852
- _propertiesToFetchWithHint:.array.34130
- _propertiesToFetchWithHint:.array.35477
- _propertiesToFetchWithHint:.array.36654
- _propertiesToFetchWithHint:.array.37323
- _propertiesToFetchWithHint:.array.5418
- _propertiesToFetchWithHint:.array.7532
- _propertiesToFetchWithHint:.array.7957
- _propertiesToFetchWithHint:.array.9576
- _propertiesToFetchWithHint:.onceToken.16817
- _propertiesToFetchWithHint:.onceToken.17255
- _propertiesToFetchWithHint:.onceToken.20815
- _propertiesToFetchWithHint:.onceToken.23866
- _propertiesToFetchWithHint:.onceToken.24769
- _propertiesToFetchWithHint:.onceToken.26593
- _propertiesToFetchWithHint:.onceToken.2751
- _propertiesToFetchWithHint:.onceToken.29851
- _propertiesToFetchWithHint:.onceToken.34128
- _propertiesToFetchWithHint:.onceToken.35475
- _propertiesToFetchWithHint:.onceToken.36653
- _propertiesToFetchWithHint:.onceToken.37322
- _propertiesToFetchWithHint:.onceToken.5417
- _propertiesToFetchWithHint:.onceToken.7531
- _propertiesToFetchWithHint:.onceToken.7956
- _propertiesToFetchWithHint:.onceToken.9346
- _propertiesToFetchWithHint:.onceToken.9575
- _propertiesToFetchWithHint:.propertiesToFetchByHint.16819
- _propertiesToFetchWithHint:.propertiesToFetchByHint.20818
- _propertiesToFetchWithHint:.propertiesToFetchByHint.24771
- _propertiesToFetchWithHint:.propertiesToFetchByHint.9349
- _propertiesToFetchWithHint:.propertyQueue.16818
- _propertiesToFetchWithHint:.propertyQueue.20817
- _propertiesToFetchWithHint:.propertyQueue.24770
- _propertiesToFetchWithHint:.propertyQueue.9348
- _propertiesToPrefetch.onceToken.16320
- _propertiesToPrefetch.onceToken.20494
- _propertiesToPrefetch.onceToken.24477
- _propertiesToPrefetch.propertiesToPrefetch.16321
- _propertiesToPrefetch.propertiesToPrefetch.20495
- _propertiesToPrefetch.propertiesToPrefetch.24478
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.20664
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.24739
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.9102
- _propertySetAccessorsByPropertySet.onceToken.20662
- _propertySetAccessorsByPropertySet.onceToken.24738
- _propertySetAccessorsByPropertySet.onceToken.9101
- _propertySetClassForPropertySet:.onceToken.20672
- _propertySetClassForPropertySet:.onceToken.24747
- _propertySetClassForPropertySet:.onceToken.9103
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.20673
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.24748
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.9104
- _sharedDecoder.s_onceToken.36765
- _sharedDecoder.s_shared.36767
- _transformValueExpression:forKeyPath:._passThroughSet.16797
- _transformValueExpression:forKeyPath:._passThroughSet.20799
- _transformValueExpression:forKeyPath:._passThroughSet.23849
- _transformValueExpression:forKeyPath:._passThroughSet.24752
- _transformValueExpression:forKeyPath:._passThroughSet.26578
- _transformValueExpression:forKeyPath:._passThroughSet.2740
- _transformValueExpression:forKeyPath:._passThroughSet.29820
- _transformValueExpression:forKeyPath:._passThroughSet.32820
- _transformValueExpression:forKeyPath:._passThroughSet.34111
- _transformValueExpression:forKeyPath:._passThroughSet.35470
- _transformValueExpression:forKeyPath:._passThroughSet.39340
- _transformValueExpression:forKeyPath:._passThroughSet.7493
- _transformValueExpression:forKeyPath:._passThroughSet.7946
- _transformValueExpression:forKeyPath:._passThroughSet.9334
- _transformValueExpression:forKeyPath:._passThroughSet.9535
- _transformValueExpression:forKeyPath:.onceToken.16796
- _transformValueExpression:forKeyPath:.onceToken.20798
- _transformValueExpression:forKeyPath:.onceToken.23848
- _transformValueExpression:forKeyPath:.onceToken.24751
- _transformValueExpression:forKeyPath:.onceToken.26577
- _transformValueExpression:forKeyPath:.onceToken.2739
- _transformValueExpression:forKeyPath:.onceToken.29819
- _transformValueExpression:forKeyPath:.onceToken.32819
- _transformValueExpression:forKeyPath:.onceToken.34110
- _transformValueExpression:forKeyPath:.onceToken.35469
- _transformValueExpression:forKeyPath:.onceToken.39339
- _transformValueExpression:forKeyPath:.onceToken.7492
- _transformValueExpression:forKeyPath:.onceToken.7945
- _transformValueExpression:forKeyPath:.onceToken.9333
- _transformValueExpression:forKeyPath:.onceToken.9534
- _uniqueObjectIDCache.pl_once_object_64
- _uniqueObjectIDCache.pl_once_token_64
CStrings:
+ "\x03\x13"
+ "\x0f\x02\x11$\x16\x15"
+ " distribute external: %+.3f"
+ " distribute internal: %+.3f"
+ " end: %+.3f"
+ " fetch results: %tu"
+ " inserts: %tu, updates: %tu, deletes: %tu: unknown: %@"
+ " internal: %tu, external %tu"
+ " now: %+.3f"
+ "%@ %p dealloc"
+ "%@ %p initWithLibraryBundle:%@ changeHandlingDebugger:%@ uniqueObjectIDCache:%@"
+ "%@: QoS: %@"
+ "2A0"
+ "<unused: %p>"
+ "@\"NSString\"16@?0@\"PHChangeHandlingDebugEvent\"8"
+ "@\"PFStateCaptureHandler\""
+ "@\"PHChangeHandlingDebugEvent\""
+ "@\"PHChangeHandlingDebugger\""
+ "@\"PHPhotoLibraryObserverRegistrar\""
+ "@\"PHUniqueObjectIDCache\""
+ "@60@0:8@16@24@32B40B44B48@?52"
+ "ADP time range export session completed unsuccessfully for asset %@: status=%td, error: %@"
+ "AssetExportInactive"
+ "Attempt to change user-picked keyFacePickSource on person %@"
+ "CMTIMERANGE_IS_VALID(timeRange)"
+ "Import Asset Delete/Eject"
+ "Incompatible video %@ (compatible=%d, valid=%d, timeout=%d)"
+ "Media item maker %@ failed to create export session for asset %@"
+ "PFStateCaptureProvider"
+ "PHChangeHandlingDebugEvent"
+ "PHChangeHandlingDebugger"
+ "PHPhotoLibraryObserverRegistrar"
+ "Performing Cache Delete requests from this process is NOT POSSIBLE due to entitlements or network volume, so falling back to just checking for available disk space, and failing if not."
+ "Resetting user-picked keyFace on person %{public}@ because it's in the list of rejected faces"
+ "Resetting user-picked keyFace on person %{public}@ because it's not in the list of faces"
+ "STATEDUMP: State information for PHPhotoLibrary-%p at path %@"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSDate\",?,R,&,N"
+ "T@\"NSMutableOrderedSet\",?,R,&,N"
+ "T@\"NSSet\",?,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSURL\",?,R,C"
+ "T@\"NSURL\",?,R,C,V_primaryPresentedItemURL"
+ "TB,V_unknownMergeEvent"
+ "TI,V_qosClass"
+ "TQ,?,N"
+ "TQ,V_deletedCount"
+ "TQ,V_externalObserversCount"
+ "TQ,V_fetchResultCount"
+ "TQ,V_insertedCount"
+ "TQ,V_internalObserversCount"
+ "TQ,V_updatedCount"
+ "Td,V_distributeExternalTimestamp"
+ "Td,V_distributeInternalTimestamp"
+ "Td,V_endTimestamp"
+ "Td,V_startTimestamp"
+ "Ts,R,N,V_keyFacePickSource"
+ "Unable to deserialize media item maker for asset %@ to create export session: %@"
+ "Unable to map path extension %{public}@ to AVFileType: %{public}@"
+ "Unable to perform ADP video partial time range export, failed to deserialize media item maker"
+ "Unable to perform ADP video partial time range export, media item maker does not support makeAVAssetExportSession:options:presetName: on this platform/SDK"
+ "Unable to perform ADP video partial time range export, media item maker failed to create export session"
+ "[RM] %{public}@ PLVideoRecipeID_VidCmp_Pri_DeferredProcessingFinalVideo resource is no longer available, requesting original video"
+ "[RM]: %{public}@ ADP time range video download complete with url: %@"
+ "[RM]: %{public}@ ADP time range video export failed, unable to create parent directories: %@"
+ "[RM]: %{public}@ ADP time range video export failed: %@"
+ "[RM]: %{public}@ requesting video %{public}@, partial ADP download=%d"
+ "[outputURL isFileURL]"
+ "_activeLock"
+ "_activeLock_isActive"
+ "_activeLock_isActiveTimestamp"
+ "_changeHandlingDebugger"
+ "_deletedCount"
+ "_distributeExternalTimestamp"
+ "_distributeInternalTimestamp"
+ "_endTimestamp"
+ "_externalObserversCount"
+ "_fetchResultCount"
+ "_insertedCount"
+ "_internalObserversCount"
+ "_keyFacePickSource"
+ "_lock_clearOIDCache"
+ "_lock_clearsOIDCacheAfterFetchResultDealloc"
+ "_lock_currentEvent"
+ "_lock_externalChangeObservers"
+ "_lock_fetchResults"
+ "_lock_hasChangeObservers"
+ "_lock_internalChangeObservers"
+ "_lock_isChangeHandlingActive"
+ "_lock_isChangeHandlingAuthorized"
+ "_lock_nextEvent"
+ "_lock_pauseChangeHandlingIfNeeded"
+ "_lock_postsPersistentHistoryChangedNotifications"
+ "_lock_previousEvents"
+ "_lock_resumeChangeHandlingIfNeeded"
+ "_maxPreviousEvents"
+ "_observerRegistrar"
+ "_qosClass"
+ "_startTimestamp"
+ "_stateCaptureHandler"
+ "_uniqueObjectIDCache"
+ "_updatedCount"
+ "accommodatePresentedItemEvictionWithCompletionHandler:"
+ "addObservers:authorizationStatus:"
+ "assetUuid"
+ "beginProcessPendingChanges"
+ "changeHandling"
+ "changeHandlingActiveStateDidChange:"
+ "checkAuthorizationStatusForAPIAccessLevel:suppressPrompt:"
+ "com.apple.photos.backend.adpExportVideoFileTimeRange.exportSession"
+ "com.apple.photos.backend.adpExportVideoTimeRange"
+ "com.apple.photos.backend.adpExportVideoTimeRange.makeExportSession"
+ "com.apple.photos.backend.chooseVideo.adpVideoTimeRangeDownload"
+ "com.apple.photos.backend.chooseVideo.adpVideoTimeRangeDownload.streamingUrl"
+ "countOfFetchResultsRegisteredForChangeNotifications"
+ "countOfRegisteredFetchResults"
+ "currentEvent"
+ "deletedCount"
+ "distributeExternalTimestamp"
+ "distributeInternalTimestamp"
+ "endProcessPendingChanges"
+ "endProcessPendingChanges: Unexpected nil debugger event"
+ "endTimestamp"
+ "exportVideoFileForTimeRange:fromVideoMediaItemMakerData:forAssetUuid:toOutputFileURL:fingerPrint:signpostId:completion:"
+ "externalObserversCount"
+ "fetchResultCount"
+ "fileTypeForOutputURL:"
+ "getObserversWithBlock:"
+ "getReturnValue:"
+ "iconSymbolName"
+ "initWithLibraryBundle:changeHandlingDebugger:uniqueObjectIDCache:"
+ "initWithMaxPreviousEvents:"
+ "initWithProvider:"
+ "initWithStartTimestamp:"
+ "insertedCount"
+ "internalObserversCount"
+ "invocationWithMethodSignature:"
+ "invoke"
+ "isActive"
+ "isActiveTimestamp"
+ "isNetworkVolume"
+ "makeAVAssetExportSession:options:presetName:"
+ "mediaItemURLForAssetUuid:fingerPrint:outOfBandPresentationHints:"
+ "methodSignatureForSelector:"
+ "originalCompletion"
+ "outputURL"
+ "previousEvents"
+ "qosClass"
+ "redactedDescriptionForFileURL:"
+ "setArgument:atIndex:"
+ "setDeletedCount:"
+ "setDistributeExternalTimestamp:"
+ "setDistributeInternalTimestamp:"
+ "setEndTimestamp:"
+ "setExternalObserversCount:"
+ "setFetchResultCount:"
+ "setInsertedCount:"
+ "setInternalObserversCount:"
+ "setQosClass:"
+ "setSelector:"
+ "setStartTimestamp:"
+ "setTarget:"
+ "setUpdatedCount:"
+ "startDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:needsDownload:shouldApplyTimeRange:reply:"
+ "startExportSession:assetUuid:signpostId:completion:"
+ "startTimestamp"
+ "startWalrusTimeRangeDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:partialVideoURL:reply:"
+ "stateCaptureDictionary"
+ "stringFromRelativeTimeInterval:"
+ "stringFromTimestamp:"
+ "systemSymbolName"
+ "typeForFilenameExtensionOrLastPathComponent:"
+ "updatedCount"
+ "v112@0:8{?={?=qiIq}{?=qiIq}}16@64@72@80@88Q96@?104"
+ "v32@?0@\"NSArray\"8@\"NSArray\"16@\"NSArray\"24"
+ "v48@0:8@16@24Q32@?40"
+ "v60@0:8@16@24@32B40@44@?52"
- "\x0f\x01\x11\"\x19\x15"
- "%K = %@ AND %K IN %@"
- "0A0"
- "Deduping graph-verified persons, but did not find a picked key face to set, key face will not sync and may be nondeterministic, for personUUID = %@"
- "Import Asser Delete/Eject"
- "Performing Cache Delete requests from this process is NOT POSSIBLE due to entitlements, so falling back to just checking for available disk space, and failing if not."
- "T@\"NSHashTable\",&,N,V_externalChangeObservers"
- "T@\"NSHashTable\",&,N,V_fetchResultsRegisteredForChangeNotifications"
- "T@\"NSHashTable\",&,N,V_internalChangeObservers"
- "T@\"NSURL\",R,C,V_primaryPresentedItemURL"
- "TB,N,V_isChangeHandlingActive"
- "TB,N,V_isChangeHandlingAuthorized"
- "[RM]: %{public}@ requesting video %{public}@"
- "_checkAuthorizationStatusForAPIAccessLevel:suppressPrompt:"
- "_externalChangeObservers"
- "_fetchResultsRegisteredForChangeNotifications"
- "_hasChangeObservers"
- "_internalChangeObservers"
- "_isChangeHandlingActive"
- "_isChangeHandlingAuthorized"
- "_pauseChangeHandlingIfNeeded"
- "_postsPersistentHistoryChangedNotifications"
- "_resumeChangeHandlingIfNeeded"
- "com.apple.photokit.unregisterfetchresult"
- "externalChangeObservers"
- "fetchResultsRegisteredForChangeNotifications"
- "internalChangeObservers"
- "isChangeHandlingActive"
- "isChangeHandlingAuthorized"
- "setExternalChangeObservers:"
- "setFetchResultsRegisteredForChangeNotifications:"
- "setInternalChangeObservers:"
- "setIsChangeHandlingActive:"
- "setIsChangeHandlingAuthorized:"

```
