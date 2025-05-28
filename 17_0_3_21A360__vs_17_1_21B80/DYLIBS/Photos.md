## Photos

> `/System/Library/Frameworks/Photos.framework/Photos`

```diff

-608.1.119.0.0
-  __TEXT.__text: 0x1fb680
+612.0.160.0.0
+  __TEXT.__text: 0x1fb090
   __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_methlist: 0x1a948
-  __TEXT.__const: 0xc28
+  __TEXT.__objc_methlist: 0x1a918
+  __TEXT.__const: 0xc20
   __TEXT.__constg_swiftt: 0xac
   __TEXT.__swift5_typeref: 0x1c3
   __TEXT.__swift5_reflstr: 0x70

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0xc
-  __TEXT.__cstring: 0x21561
-  __TEXT.__gcc_except_tab: 0x4b24
-  __TEXT.__oslogstring: 0x13ff9
+  __TEXT.__cstring: 0x21592
+  __TEXT.__gcc_except_tab: 0x4b34
+  __TEXT.__oslogstring: 0x14511
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x6c28
+  __TEXT.__unwind_info: 0x6c18
   __TEXT.__eh_frame: 0x98
-  __TEXT.__objc_classname: 0x2a85
-  __TEXT.__objc_methname: 0x51f6d
-  __TEXT.__objc_methtype: 0x58ff
-  __TEXT.__objc_stubs: 0x2cb40
-  __DATA_CONST.__got: 0xb60
-  __DATA_CONST.__const: 0x65b0
-  __DATA_CONST.__objc_classlist: 0xac0
-  __DATA_CONST.__objc_catlist: 0x80
+  __TEXT.__objc_classname: 0x2a3c
+  __TEXT.__objc_methname: 0x51ba5
+  __TEXT.__objc_methtype: 0x5947
+  __TEXT.__objc_stubs: 0x2c940
+  __DATA_CONST.__got: 0xb20
+  __DATA_CONST.__const: 0x6630
+  __DATA_CONST.__objc_classlist: 0xab0
+  __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x28b00
-  __DATA_CONST.__objc_selrefs: 0xeac0
-  __DATA_CONST.__objc_arraydata: 0x7f0
-  __AUTH_CONST.__const: 0x3138
-  __AUTH_CONST.__cfstring: 0x1e5a0
-  __AUTH_CONST.__objc_const: 0x9650
-  __AUTH_CONST.__objc_intobj: 0x1bc0
-  __AUTH_CONST.__objc_arrayobj: 0x5a0
-  __AUTH_CONST.__objc_doubleobj: 0x130
+  __DATA_CONST.__objc_const: 0x28ad0
+  __DATA_CONST.__objc_selrefs: 0xe9e0
+  __DATA_CONST.__objc_arraydata: 0x800
+  __AUTH_CONST.__const: 0x3178
+  __AUTH_CONST.__cfstring: 0x1e540
+  __AUTH_CONST.__objc_const: 0x9588
+  __AUTH_CONST.__objc_intobj: 0x1bf0
+  __AUTH_CONST.__objc_arrayobj: 0x5b8
+  __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0x1218
-  __AUTH.__objc_data: 0x5550
+  __AUTH.__objc_data: 0x54b0
   __AUTH.__data: 0xa8
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x11d8
+  __DATA.__objc_classrefs: 0x11c0
   __DATA.__objc_superrefs: 0x8c8
-  __DATA.__objc_ivar: 0x25d0
+  __DATA.__objc_ivar: 0x25e4
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0x25c8
+  __DATA.__data: 0x2590
   __DATA.__common: 0x55
-  __DATA.__bss: 0xdb0
+  __DATA.__bss: 0xdf8
   __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10569
-  Symbols:   35347
-  CStrings:  18437
+  Functions: 10576
+  Symbols:   35329
+  CStrings:  18422
 
Symbols:
+ +[PHContentEditingInputRequestContext contentEditingInputRequestContextForAsset:requestID:managerID:networkAccessAllowed:downloadIntent:progressHandler:resultHandler:]
+ +[PHContentEditingInputRequestContext shouldUseRAWResourceAsUnadjustedBaseForAsset:options:]
+ +[PHInternalAssetExportRequest knownCompatibleVariantTypeIdentifierForTypeIdentifier:]
+ +[PHResourceLocalAvailabilityRequest isKnownUnsupportedFormatForAsset:]
+ +[PHResourceLocalAvailabilityRequest resourceLocalAvailabilityRequestLog]
+ +[PHSuggestion allShuffleWallpaperAlbumSuggestionSubtypes]
+ +[PHSuggestion predicateForAllShuffleWallpaperAlbumSuggestions]
+ -[PHAssetResource asset]
+ -[PHAssetResourceManager assetResourceRequestDidRequestRetryWithContentEditingInputLoaded:]
+ -[PHAssetResourceRequest configureWithError:]
+ -[PHAssetResourceWriteRequest _lazyDataRequest]
+ -[PHAssetResourceWriteRequest assetResourceRequestDidRequestRetryWithContentEditingInputLoaded:]
+ -[PHAssetResourceWriteRequest configureWithError:]
+ -[PHContentEditingInputRequestOptions disallowFallbackAdjustmentBase]
+ -[PHContentEditingInputRequestOptions setDisallowFallbackAdjustmentBase:]
+ -[PHImageDecoderOptions hdrGain]
+ -[PHImageDecoderOptions setHdrGain:]
+ -[PHImageDecoderOptions setTargetHDRHeadroom:]
+ -[PHImageDecoderOptions targetHDRHeadroom]
+ -[PHImageRequest configureWithError:]
+ -[PHImageRequestBehaviorSpec setTargetHDRHeadroom:]
+ -[PHImageRequestBehaviorSpec targetHDRHeadroom]
+ -[PHImageRequestOptions setTargetHDRHeadroom:]
+ -[PHImageRequestOptions targetHDRHeadroom]
+ -[PHMediaRequest configureWithError:]
+ -[PHMediaRequestContext mediaRequestDidRequestRetryWithContentEditingInputLoaded:]
+ -[PHMediaRequestContext setSupplementaryRequestContext:]
+ -[PHMediaRequestContext supplementaryRequestContext]
+ -[PHMediaResourceRequest assetResourceRequestDidRequestRetryWithContentEditingInputLoaded:]
+ -[PHPhotoLibrary(CloudPhotoLibrary) _cloudInternalClient]
+ -[PHPhotoLibrary(CloudPhotoLibrary) overrideSystemBudgetsForSyncSession:pauseReason:systemBudgets:completionHandler:]
+ -[PHPhotoLibrary(CloudPhotoLibrary) setCloudPhotoLibraryPauseState:reason:]
+ -[PHVideoRequest configureWithError:]
+ GCC_except_table10093
+ GCC_except_table10164
+ GCC_except_table10189
+ GCC_except_table10223
+ GCC_except_table10233
+ GCC_except_table10251
+ GCC_except_table10266
+ GCC_except_table10305
+ GCC_except_table10307
+ GCC_except_table10309
+ GCC_except_table10328
+ GCC_except_table1044
+ GCC_except_table1092
+ GCC_except_table1216
+ GCC_except_table1219
+ GCC_except_table1232
+ GCC_except_table1424
+ GCC_except_table1428
+ GCC_except_table1430
+ GCC_except_table1434
+ GCC_except_table1436
+ GCC_except_table1438
+ GCC_except_table1450
+ GCC_except_table1453
+ GCC_except_table1465
+ GCC_except_table1497
+ GCC_except_table1499
+ GCC_except_table1501
+ GCC_except_table1503
+ GCC_except_table1505
+ GCC_except_table1507
+ GCC_except_table1509
+ GCC_except_table1511
+ GCC_except_table1513
+ GCC_except_table1515
+ GCC_except_table1517
+ GCC_except_table1519
+ GCC_except_table1530
+ GCC_except_table1536
+ GCC_except_table1538
+ GCC_except_table1543
+ GCC_except_table1546
+ GCC_except_table1548
+ GCC_except_table1550
+ GCC_except_table1576
+ GCC_except_table1578
+ GCC_except_table1581
+ GCC_except_table1584
+ GCC_except_table1633
+ GCC_except_table1638
+ GCC_except_table1646
+ GCC_except_table1648
+ GCC_except_table1660
+ GCC_except_table1831
+ GCC_except_table1836
+ GCC_except_table1890
+ GCC_except_table1998
+ GCC_except_table2069
+ GCC_except_table2072
+ GCC_except_table2074
+ GCC_except_table2097
+ GCC_except_table2099
+ GCC_except_table2102
+ GCC_except_table2235
+ GCC_except_table2239
+ GCC_except_table2301
+ GCC_except_table2309
+ GCC_except_table2338
+ GCC_except_table2342
+ GCC_except_table2347
+ GCC_except_table2426
+ GCC_except_table2458
+ GCC_except_table2464
+ GCC_except_table2477
+ GCC_except_table2481
+ GCC_except_table2487
+ GCC_except_table2490
+ GCC_except_table2494
+ GCC_except_table2498
+ GCC_except_table2509
+ GCC_except_table2514
+ GCC_except_table2525
+ GCC_except_table2526
+ GCC_except_table2542
+ GCC_except_table2644
+ GCC_except_table2667
+ GCC_except_table2669
+ GCC_except_table2671
+ GCC_except_table2714
+ GCC_except_table2737
+ GCC_except_table2770
+ GCC_except_table2774
+ GCC_except_table2777
+ GCC_except_table2923
+ GCC_except_table2964
+ GCC_except_table2974
+ GCC_except_table2977
+ GCC_except_table2979
+ GCC_except_table3004
+ GCC_except_table3009
+ GCC_except_table3010
+ GCC_except_table3256
+ GCC_except_table3261
+ GCC_except_table3287
+ GCC_except_table3296
+ GCC_except_table3298
+ GCC_except_table3302
+ GCC_except_table3307
+ GCC_except_table3318
+ GCC_except_table3323
+ GCC_except_table3336
+ GCC_except_table3399
+ GCC_except_table3657
+ GCC_except_table3658
+ GCC_except_table3665
+ GCC_except_table3693
+ GCC_except_table3695
+ GCC_except_table3697
+ GCC_except_table3760
+ GCC_except_table3784
+ GCC_except_table4235
+ GCC_except_table4288
+ GCC_except_table4315
+ GCC_except_table4376
+ GCC_except_table4381
+ GCC_except_table4397
+ GCC_except_table4402
+ GCC_except_table4416
+ GCC_except_table4419
+ GCC_except_table4422
+ GCC_except_table4435
+ GCC_except_table4480
+ GCC_except_table4491
+ GCC_except_table4531
+ GCC_except_table4557
+ GCC_except_table4560
+ GCC_except_table4566
+ GCC_except_table4571
+ GCC_except_table4594
+ GCC_except_table4621
+ GCC_except_table4646
+ GCC_except_table4648
+ GCC_except_table4659
+ GCC_except_table4697
+ GCC_except_table4768
+ GCC_except_table4773
+ GCC_except_table4891
+ GCC_except_table4894
+ GCC_except_table4907
+ GCC_except_table4926
+ GCC_except_table4939
+ GCC_except_table4969
+ GCC_except_table5003
+ GCC_except_table5005
+ GCC_except_table5309
+ GCC_except_table5322
+ GCC_except_table5350
+ GCC_except_table5376
+ GCC_except_table5379
+ GCC_except_table5381
+ GCC_except_table5383
+ GCC_except_table5385
+ GCC_except_table5416
+ GCC_except_table5449
+ GCC_except_table5451
+ GCC_except_table5485
+ GCC_except_table5674
+ GCC_except_table5831
+ GCC_except_table6024
+ GCC_except_table6093
+ GCC_except_table6115
+ GCC_except_table6119
+ GCC_except_table6125
+ GCC_except_table6176
+ GCC_except_table6281
+ GCC_except_table6283
+ GCC_except_table6328
+ GCC_except_table6368
+ GCC_except_table6370
+ GCC_except_table6372
+ GCC_except_table6384
+ GCC_except_table6389
+ GCC_except_table6425
+ GCC_except_table6448
+ GCC_except_table6535
+ GCC_except_table6538
+ GCC_except_table6556
+ GCC_except_table6613
+ GCC_except_table6616
+ GCC_except_table6634
+ GCC_except_table6694
+ GCC_except_table6771
+ GCC_except_table6900
+ GCC_except_table6905
+ GCC_except_table7190
+ GCC_except_table7200
+ GCC_except_table7231
+ GCC_except_table7294
+ GCC_except_table7321
+ GCC_except_table7369
+ GCC_except_table7371
+ GCC_except_table7455
+ GCC_except_table7529
+ GCC_except_table7547
+ GCC_except_table7632
+ GCC_except_table7646
+ GCC_except_table7745
+ GCC_except_table7746
+ GCC_except_table7747
+ GCC_except_table7748
+ GCC_except_table7749
+ GCC_except_table7750
+ GCC_except_table7751
+ GCC_except_table7752
+ GCC_except_table7753
+ GCC_except_table7754
+ GCC_except_table7755
+ GCC_except_table7756
+ GCC_except_table7757
+ GCC_except_table7758
+ GCC_except_table7759
+ GCC_except_table7760
+ GCC_except_table7761
+ GCC_except_table7762
+ GCC_except_table7763
+ GCC_except_table7764
+ GCC_except_table7765
+ GCC_except_table7845
+ GCC_except_table7854
+ GCC_except_table7855
+ GCC_except_table7857
+ GCC_except_table7858
+ GCC_except_table7896
+ GCC_except_table7897
+ GCC_except_table7898
+ GCC_except_table7902
+ GCC_except_table7924
+ GCC_except_table7925
+ GCC_except_table7926
+ GCC_except_table7927
+ GCC_except_table7928
+ GCC_except_table7929
+ GCC_except_table7930
+ GCC_except_table7931
+ GCC_except_table7960
+ GCC_except_table7964
+ GCC_except_table7983
+ GCC_except_table7988
+ GCC_except_table8055
+ GCC_except_table8145
+ GCC_except_table8210
+ GCC_except_table8248
+ GCC_except_table830
+ GCC_except_table8325
+ GCC_except_table8344
+ GCC_except_table847
+ GCC_except_table8917
+ GCC_except_table8936
+ GCC_except_table8940
+ GCC_except_table8942
+ GCC_except_table8972
+ GCC_except_table9031
+ GCC_except_table9131
+ GCC_except_table9143
+ GCC_except_table9182
+ GCC_except_table9184
+ GCC_except_table9232
+ GCC_except_table9236
+ GCC_except_table9274
+ GCC_except_table9278
+ GCC_except_table9287
+ GCC_except_table9288
+ GCC_except_table9295
+ GCC_except_table9332
+ GCC_except_table9339
+ GCC_except_table9441
+ GCC_except_table9447
+ GCC_except_table9449
+ GCC_except_table9495
+ GCC_except_table9511
+ GCC_except_table9521
+ GCC_except_table9603
+ GCC_except_table9691
+ GCC_except_table9699
+ GCC_except_table972
+ GCC_except_table9727
+ GCC_except_table988
+ _OBJC_CLASS_$_PLCodec
+ _OBJC_IVAR_$_PHAssetResource._asset
+ _OBJC_IVAR_$_PHAssetResourceManager._requestsLock
+ _OBJC_IVAR_$_PHAssetResourceManager._requestsLock_requestsByID
+ _OBJC_IVAR_$_PHAssetResourceManager._requestsLock_supplementaryContextsByID
+ _OBJC_IVAR_$_PHAssetResourceRequest._configuredError
+ _OBJC_IVAR_$_PHContentEditingInputRequestOptions._disallowFallbackAdjustmentBase
+ _OBJC_IVAR_$_PHImageDecoderOptions._hdrGain
+ _OBJC_IVAR_$_PHImageDecoderOptions._targetHDRHeadroom
+ _OBJC_IVAR_$_PHImageRequestBehaviorSpec._targetHDRHeadroom
+ _OBJC_IVAR_$_PHImageRequestOptions._targetHDRHeadroom
+ _OBJC_IVAR_$_PHMediaRequestContext._supplementaryRequestContext
+ _PHErrorIsGenerateAdjustmentFileNotFound
+ _PHNextImageAndAssetResourceManagerID
+ _PHNextImageAndAssetResourceManagerID.managerID
+ _PHNextImageAndAssetResourceManagerID.onceToken
+ _PLErrorOrUnderlyingErrorHasDomainAndCode
+ _PLSafeResultWithUnfairLock
+ __OBJC_$_CLASS_METHODS_PHContentEditingInputRequestContext
+ __OBJC_$_CLASS_METHODS_PHPhotoLibrary(ImportDeDup|Import|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|PXCPLStatus|CloudPhotoLibrary|CloudIdentifiers|PHBatchFetchingArray|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
+ __OBJC_$_INSTANCE_METHODS_PHPhotoLibrary(ImportDeDup|Import|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|PXCPLStatus|CloudPhotoLibrary|CloudIdentifiers|PHBatchFetchingArray|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
+ __OBJC_$_PROP_LIST_PHAssetResourceRequest.262
+ ___101+[PHResourceLocalAvailabilityRequest indexesForAssetsRequiringResourceRetrieval:requestType:options:]_block_invoke.332
+ ___128-[PHAssetResourceManager _requestForAssetResource:loadURLOnly:options:urlReceivedHandler:dataReceivedHandler:completionHandler:]_block_invoke
+ ___167+[PHContentEditingInputRequestContext contentEditingInputRequestContextForAsset:requestID:managerID:networkAccessAllowed:downloadIntent:progressHandler:resultHandler:]_block_invoke
+ ___41-[PHAssetResourceManager infoForRequest:]_block_invoke
+ ___44-[PHAssetResourceManager cancelDataRequest:]_block_invoke
+ ___47-[PHAssetResourceWriteRequest _lazyDataRequest]_block_invoke
+ ___63-[PHImageManager requestAVProxyForAsset:options:resultHandler:]_block_invoke.647
+ ___66-[PHAssetResourceManager assetResourceRequest:didFinishWithError:]_block_invoke
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.589
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.593
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.596
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_2.594
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_2.598
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_3.595
+ ___68-[PHInternalAssetExportRequest exportWithOptions:completionHandler:]_block_invoke.53
+ ___71+[PHResourceLocalAvailabilityRequest isKnownUnsupportedFormatForAsset:]_block_invoke
+ ___73+[PHResourceLocalAvailabilityRequest resourceLocalAvailabilityRequestLog]_block_invoke
+ ___80-[PHAssetResourceManager reconnectAssets:urlResolvingHandler:completionHandler:]_block_invoke.127
+ ___80-[PHAssetResourceManager reconnectAssets:urlResolvingHandler:completionHandler:]_block_invoke.134
+ ___80-[PHAssetResourceManager reconnectAssets:urlResolvingHandler:completionHandler:]_block_invoke_2.135
+ ___82-[PHMediaRequestContext mediaRequestDidRequestRetryWithContentEditingInputLoaded:]_block_invoke
+ ___82-[PHMediaRequestContext mediaRequestDidRequestRetryWithContentEditingInputLoaded:]_block_invoke_2
+ ___82-[PHMediaRequestContext mediaRequestDidRequestRetryWithContentEditingInputLoaded:]_block_invoke_3
+ ___83-[PHImageManager requestContentEditingInputForAsset:withOptions:completionHandler:]_block_invoke.630
+ ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.566
+ ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.569
+ ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.574
+ ___89-[PHImageManager requestNewCGImageForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.619
+ ___91-[PHAssetResourceManager assetResourceRequestDidRequestRetryWithContentEditingInputLoaded:]_block_invoke
+ ___91-[PHAssetResourceManager assetResourceRequestDidRequestRetryWithContentEditingInputLoaded:]_block_invoke_2
+ ___91-[PHAssetResourceManager assetResourceRequestDidRequestRetryWithContentEditingInputLoaded:]_block_invoke_3
+ ___91-[PHAssetResourceManager assetResourceRequestDidRequestRetryWithContentEditingInputLoaded:]_block_invoke_4
+ ___92-[PHAssetResourceManager requestWriteDataForAssetResource:toFile:options:completionHandler:]_block_invoke
+ ___Block_byref_object_copy_.10325
+ ___Block_byref_object_copy_.10949
+ ___Block_byref_object_copy_.13078
+ ___Block_byref_object_copy_.14636
+ ___Block_byref_object_copy_.14798
+ ___Block_byref_object_copy_.15093
+ ___Block_byref_object_copy_.15550
+ ___Block_byref_object_copy_.16150
+ ___Block_byref_object_copy_.16310
+ ___Block_byref_object_copy_.18278
+ ___Block_byref_object_copy_.19418
+ ___Block_byref_object_copy_.19926
+ ___Block_byref_object_copy_.20263
+ ___Block_byref_object_copy_.20531
+ ___Block_byref_object_copy_.2127
+ ___Block_byref_object_copy_.21405
+ ___Block_byref_object_copy_.21717
+ ___Block_byref_object_copy_.22507
+ ___Block_byref_object_copy_.23109
+ ___Block_byref_object_copy_.24510
+ ___Block_byref_object_copy_.25097
+ ___Block_byref_object_copy_.2551
+ ___Block_byref_object_copy_.25907
+ ___Block_byref_object_copy_.26154
+ ___Block_byref_object_copy_.27142
+ ___Block_byref_object_copy_.27592
+ ___Block_byref_object_copy_.28697
+ ___Block_byref_object_copy_.29178
+ ___Block_byref_object_copy_.32568
+ ___Block_byref_object_copy_.32802
+ ___Block_byref_object_copy_.33722
+ ___Block_byref_object_copy_.34105
+ ___Block_byref_object_copy_.34282
+ ___Block_byref_object_copy_.34568
+ ___Block_byref_object_copy_.35250
+ ___Block_byref_object_copy_.3538
+ ___Block_byref_object_copy_.36152
+ ___Block_byref_object_copy_.36261
+ ___Block_byref_object_copy_.38036
+ ___Block_byref_object_copy_.38322
+ ___Block_byref_object_copy_.38841
+ ___Block_byref_object_copy_.4538
+ ___Block_byref_object_copy_.4777
+ ___Block_byref_object_copy_.5900
+ ___Block_byref_object_copy_.6894
+ ___Block_byref_object_copy_.7490
+ ___Block_byref_object_copy_.7696
+ ___Block_byref_object_copy_.7862
+ ___Block_byref_object_copy_.8436
+ ___Block_byref_object_copy_.8675
+ ___Block_byref_object_copy_.9127
+ ___Block_byref_object_copy_.9523
+ ___Block_byref_object_dispose_.10326
+ ___Block_byref_object_dispose_.10950
+ ___Block_byref_object_dispose_.13079
+ ___Block_byref_object_dispose_.14637
+ ___Block_byref_object_dispose_.14799
+ ___Block_byref_object_dispose_.15094
+ ___Block_byref_object_dispose_.15551
+ ___Block_byref_object_dispose_.16151
+ ___Block_byref_object_dispose_.16311
+ ___Block_byref_object_dispose_.18279
+ ___Block_byref_object_dispose_.19419
+ ___Block_byref_object_dispose_.19927
+ ___Block_byref_object_dispose_.20264
+ ___Block_byref_object_dispose_.20532
+ ___Block_byref_object_dispose_.2128
+ ___Block_byref_object_dispose_.21406
+ ___Block_byref_object_dispose_.21718
+ ___Block_byref_object_dispose_.22508
+ ___Block_byref_object_dispose_.23110
+ ___Block_byref_object_dispose_.24511
+ ___Block_byref_object_dispose_.25098
+ ___Block_byref_object_dispose_.2552
+ ___Block_byref_object_dispose_.25908
+ ___Block_byref_object_dispose_.26155
+ ___Block_byref_object_dispose_.27143
+ ___Block_byref_object_dispose_.27593
+ ___Block_byref_object_dispose_.28698
+ ___Block_byref_object_dispose_.29179
+ ___Block_byref_object_dispose_.32569
+ ___Block_byref_object_dispose_.32803
+ ___Block_byref_object_dispose_.33723
+ ___Block_byref_object_dispose_.34106
+ ___Block_byref_object_dispose_.34283
+ ___Block_byref_object_dispose_.34569
+ ___Block_byref_object_dispose_.35251
+ ___Block_byref_object_dispose_.3539
+ ___Block_byref_object_dispose_.36153
+ ___Block_byref_object_dispose_.36262
+ ___Block_byref_object_dispose_.38037
+ ___Block_byref_object_dispose_.38323
+ ___Block_byref_object_dispose_.38842
+ ___Block_byref_object_dispose_.4539
+ ___Block_byref_object_dispose_.4778
+ ___Block_byref_object_dispose_.5901
+ ___Block_byref_object_dispose_.6895
+ ___Block_byref_object_dispose_.7491
+ ___Block_byref_object_dispose_.7697
+ ___Block_byref_object_dispose_.7863
+ ___Block_byref_object_dispose_.8437
+ ___Block_byref_object_dispose_.8676
+ ___Block_byref_object_dispose_.9128
+ ___Block_byref_object_dispose_.9524
+ ___PHNextImageAndAssetResourceManagerID_block_invoke
+ ____handleKeyUsageFailureDuringChoosing_block_invoke.204
+ ____loadImageFromStoreAndKey_block_invoke.182
+ ___block_descriptor_40_e8_32s_e12_v24?0d8^B16ls32l8
+ ___block_descriptor_44_e8_32s_e5_8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e77_v32?0"PHCompositeMediaResult"8"PHMediaRequest"16"PHMediaRequestContext"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e77_v32?0"PHCompositeMediaResult"8"PHMediaRequest"16"PHMediaRequestContext"24lw40l8s32l8
+ ___block_descriptor_52_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.10015
+ ___block_literal_global.10380
+ ___block_literal_global.1043
+ ___block_literal_global.1052
+ ___block_literal_global.1067
+ ___block_literal_global.1085
+ ___block_literal_global.112.30486
+ ___block_literal_global.12591
+ ___block_literal_global.131.28702
+ ___block_literal_global.13111
+ ___block_literal_global.13165
+ ___block_literal_global.14306
+ ___block_literal_global.144
+ ___block_literal_global.14630
+ ___block_literal_global.15049
+ ___block_literal_global.15974
+ ___block_literal_global.16834
+ ___block_literal_global.17590
+ ___block_literal_global.185
+ ___block_literal_global.18622
+ ___block_literal_global.19109
+ ___block_literal_global.1949
+ ___block_literal_global.19617
+ ___block_literal_global.200.15829
+ ___block_literal_global.20240
+ ___block_literal_global.20829
+ ___block_literal_global.210.9830
+ ___block_literal_global.21030
+ ___block_literal_global.213
+ ___block_literal_global.21417
+ ___block_literal_global.21828
+ ___block_literal_global.21999
+ ___block_literal_global.2210
+ ___block_literal_global.22140
+ ___block_literal_global.22242
+ ___block_literal_global.223.14631
+ ___block_literal_global.225.24787
+ ___block_literal_global.22519
+ ___block_literal_global.22707
+ ___block_literal_global.229.24785
+ ___block_literal_global.230.8710
+ ___block_literal_global.23325
+ ___block_literal_global.23454
+ ___block_literal_global.23882
+ ___block_literal_global.24790
+ ___block_literal_global.25045
+ ___block_literal_global.25248
+ ___block_literal_global.25648
+ ___block_literal_global.257
+ ___block_literal_global.26159
+ ___block_literal_global.262
+ ___block_literal_global.26607
+ ___block_literal_global.27458
+ ___block_literal_global.2777
+ ___block_literal_global.2815
+ ___block_literal_global.28174
+ ___block_literal_global.28446
+ ___block_literal_global.28741
+ ___block_literal_global.28992
+ ___block_literal_global.29290
+ ___block_literal_global.29807
+ ___block_literal_global.3.7717
+ ___block_literal_global.30184
+ ___block_literal_global.304.27290
+ ___block_literal_global.30492
+ ___block_literal_global.306
+ ___block_literal_global.308.8831
+ ___block_literal_global.310
+ ___block_literal_global.31862
+ ___block_literal_global.3189
+ ___block_literal_global.3253
+ ___block_literal_global.32820
+ ___block_literal_global.33115
+ ___block_literal_global.33809
+ ___block_literal_global.34134
+ ___block_literal_global.34821
+ ___block_literal_global.34912
+ ___block_literal_global.35337
+ ___block_literal_global.35482
+ ___block_literal_global.36117
+ ___block_literal_global.36263
+ ___block_literal_global.36772
+ ___block_literal_global.37.34905
+ ___block_literal_global.37789
+ ___block_literal_global.38913
+ ___block_literal_global.39396
+ ___block_literal_global.4607
+ ___block_literal_global.4827
+ ___block_literal_global.51.7552
+ ___block_literal_global.5192
+ ___block_literal_global.5407
+ ___block_literal_global.5552
+ ___block_literal_global.574
+ ___block_literal_global.6080
+ ___block_literal_global.683.27194
+ ___block_literal_global.6960
+ ___block_literal_global.714
+ ___block_literal_global.741.27006
+ ___block_literal_global.7557
+ ___block_literal_global.7712
+ ___block_literal_global.7955
+ ___block_literal_global.81.39376
+ ___block_literal_global.823.27004
+ ___block_literal_global.8729
+ ___block_literal_global.894.26959
+ ___block_literal_global.896.26957
+ ___block_literal_global.9359
+ __currentTimestampString.s_formatter.34906
+ __currentTimestampString.s_onceToken.34904
+ __unnamed_array_storage.10403
+ __unnamed_array_storage.11877
+ __unnamed_array_storage.13250
+ __unnamed_array_storage.14.7900
+ __unnamed_array_storage.15946
+ __unnamed_array_storage.162.35299
+ __unnamed_array_storage.16528
+ __unnamed_array_storage.173
+ __unnamed_array_storage.18589
+ __unnamed_array_storage.187
+ __unnamed_array_storage.19.7898
+ __unnamed_array_storage.192
+ __unnamed_array_storage.20693
+ __unnamed_array_storage.21440
+ __unnamed_array_storage.246.35204
+ __unnamed_array_storage.26698
+ __unnamed_array_storage.2723
+ __unnamed_array_storage.288
+ __unnamed_array_storage.29320
+ __unnamed_array_storage.29822
+ __unnamed_array_storage.30506
+ __unnamed_array_storage.30599
+ __unnamed_array_storage.31869
+ __unnamed_array_storage.34205
+ __unnamed_array_storage.35351
+ __unnamed_array_storage.38490
+ __unnamed_array_storage.38825
+ __unnamed_array_storage.39370
+ __unnamed_array_storage.5527
+ __unnamed_array_storage.6067
+ __unnamed_array_storage.7888
+ __unnamed_array_storage.8842
+ __unnamed_array_storage.9167
+ _allowedInfoKeys.allowedKeys.13327
+ _allowedInfoKeys.allowedKeys.29989
+ _allowedInfoKeys.onceToken.13326
+ _allowedInfoKeys.onceToken.29988
+ _corePropertiesToFetch.array.16837
+ _corePropertiesToFetch.array.20826
+ _corePropertiesToFetch.array.24791
+ _corePropertiesToFetch.onceToken.16836
+ _corePropertiesToFetch.onceToken.20825
+ _corePropertiesToFetch.onceToken.24789
+ _defaultManager.onceToken.38112
+ _entityKeyMap.pl_once_object_0.23873
+ _entityKeyMap.pl_once_object_0.5412
+ _entityKeyMap.pl_once_object_0.7966
+ _entityKeyMap.pl_once_object_2.20820
+ _entityKeyMap.pl_once_object_2.26597
+ _entityKeyMap.pl_once_object_2.29837
+ _entityKeyMap.pl_once_object_2.32840
+ _entityKeyMap.pl_once_object_2.34125
+ _entityKeyMap.pl_once_object_2.35479
+ _entityKeyMap.pl_once_object_2.7536
+ _entityKeyMap.pl_once_object_2.9351
+ _entityKeyMap.pl_once_object_2.9568
+ _entityKeyMap.pl_once_object_3.24776
+ _entityKeyMap.pl_once_object_3.39384
+ _entityKeyMap.pl_once_token_0.23872
+ _entityKeyMap.pl_once_token_0.5411
+ _entityKeyMap.pl_once_token_0.7965
+ _entityKeyMap.pl_once_token_2.20819
+ _entityKeyMap.pl_once_token_2.26596
+ _entityKeyMap.pl_once_token_2.29836
+ _entityKeyMap.pl_once_token_2.32839
+ _entityKeyMap.pl_once_token_2.34124
+ _entityKeyMap.pl_once_token_2.35478
+ _entityKeyMap.pl_once_token_2.7535
+ _entityKeyMap.pl_once_token_2.9350
+ _entityKeyMap.pl_once_token_2.9567
+ _entityKeyMap.pl_once_token_3.24775
+ _entityKeyMap.pl_once_token_3.39383
+ _identifierPropertiesToFetch.array.25649
+ _identifierPropertiesToFetch.onceToken.25647
+ _isKnownUnsupportedFormatForAsset:.cachedPlayableVideoCodecs
+ _isKnownUnsupportedFormatForAsset:.onceToken
+ _objc_msgSend$H264fourCharCode
+ _objc_msgSend$HEVCfourCharCode
+ _objc_msgSend$_cloudInternalClient
+ _objc_msgSend$_lazyDataRequest
+ _objc_msgSend$allShuffleWallpaperAlbumSuggestionSubtypes
+ _objc_msgSend$assetResourceRequestDidRequestRetryWithContentEditingInputLoaded:
+ _objc_msgSend$codec
+ _objc_msgSend$configureWithError:
+ _objc_msgSend$contentEditingInputRequestContextForAsset:requestID:managerID:networkAccessAllowed:downloadIntent:progressHandler:resultHandler:
+ _objc_msgSend$copyCGImageFromImageGenerator:atTime:actualTime:error:
+ _objc_msgSend$disallowFallbackAdjustmentBase
+ _objc_msgSend$getDeletionWarningTitle:message:buttonTitle:forAssets:syndicationAssetCount:clientName:style:
+ _objc_msgSend$hdrGain
+ _objc_msgSend$isKnownUnsupportedFormatForAsset:
+ _objc_msgSend$isPlayableFourCharCodecName:
+ _objc_msgSend$knownCompatibleVariantTypeIdentifierForTypeIdentifier:
+ _objc_msgSend$mediaRequestDidRequestRetryWithContentEditingInputLoaded:
+ _objc_msgSend$now
+ _objc_msgSend$overrideSystemBudgetsForSyncSession:pauseReason:systemBudgets:completionHandler:
+ _objc_msgSend$resourceLocalAvailabilityRequestLog
+ _objc_msgSend$setCloudPhotoLibraryPauseState:reason:
+ _objc_msgSend$setDisallowFallbackAdjustmentBase:
+ _objc_msgSend$setHdrGain:
+ _objc_msgSend$setSupplementaryRequestContext:
+ _objc_msgSend$setTargetHDRHeadroom:
+ _objc_msgSend$shouldUseRAWResourceAsUnadjustedBaseForAsset:options:
+ _objc_msgSend$targetHDRHeadroom
+ _propertiesToFetchWithHint:.array.17270
+ _propertiesToFetchWithHint:.array.23883
+ _propertiesToFetchWithHint:.array.26608
+ _propertiesToFetchWithHint:.array.29858
+ _propertiesToFetchWithHint:.array.34135
+ _propertiesToFetchWithHint:.array.35483
+ _propertiesToFetchWithHint:.array.36660
+ _propertiesToFetchWithHint:.array.37329
+ _propertiesToFetchWithHint:.array.5437
+ _propertiesToFetchWithHint:.array.7548
+ _propertiesToFetchWithHint:.array.7973
+ _propertiesToFetchWithHint:.array.9593
+ _propertiesToFetchWithHint:.onceToken.16831
+ _propertiesToFetchWithHint:.onceToken.17269
+ _propertiesToFetchWithHint:.onceToken.20828
+ _propertiesToFetchWithHint:.onceToken.23881
+ _propertiesToFetchWithHint:.onceToken.24781
+ _propertiesToFetchWithHint:.onceToken.26606
+ _propertiesToFetchWithHint:.onceToken.2776
+ _propertiesToFetchWithHint:.onceToken.29857
+ _propertiesToFetchWithHint:.onceToken.34133
+ _propertiesToFetchWithHint:.onceToken.35481
+ _propertiesToFetchWithHint:.onceToken.36659
+ _propertiesToFetchWithHint:.onceToken.37328
+ _propertiesToFetchWithHint:.onceToken.5436
+ _propertiesToFetchWithHint:.onceToken.7547
+ _propertiesToFetchWithHint:.onceToken.7972
+ _propertiesToFetchWithHint:.onceToken.9358
+ _propertiesToFetchWithHint:.onceToken.9592
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.16833
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.20831
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.24783
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.9361
+ _propertiesToFetchWithHint:.propertyQueue.16832
+ _propertiesToFetchWithHint:.propertyQueue.20830
+ _propertiesToFetchWithHint:.propertyQueue.24782
+ _propertiesToFetchWithHint:.propertyQueue.9360
+ _propertiesToPrefetch.onceToken.16325
+ _propertiesToPrefetch.onceToken.20509
+ _propertiesToPrefetch.onceToken.24489
+ _propertiesToPrefetch.propertiesToPrefetch.16326
+ _propertiesToPrefetch.propertiesToPrefetch.20510
+ _propertiesToPrefetch.propertiesToPrefetch.24490
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.20678
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.24751
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.9115
+ _propertySetAccessorsByPropertySet.onceToken.20677
+ _propertySetAccessorsByPropertySet.onceToken.24750
+ _propertySetAccessorsByPropertySet.onceToken.9114
+ _propertySetClassForPropertySet:.onceToken.20685
+ _propertySetClassForPropertySet:.onceToken.24759
+ _propertySetClassForPropertySet:.onceToken.9116
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.20686
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.24760
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.9117
+ _resourceLocalAvailabilityRequestLog.log
+ _resourceLocalAvailabilityRequestLog.onceToken
+ _sharedDecoder.s_onceToken.36771
+ _sharedDecoder.s_shared.36773
+ _transformValueExpression:forKeyPath:._passThroughSet.16810
+ _transformValueExpression:forKeyPath:._passThroughSet.20812
+ _transformValueExpression:forKeyPath:._passThroughSet.23864
+ _transformValueExpression:forKeyPath:._passThroughSet.24764
+ _transformValueExpression:forKeyPath:._passThroughSet.26591
+ _transformValueExpression:forKeyPath:._passThroughSet.2765
+ _transformValueExpression:forKeyPath:._passThroughSet.29826
+ _transformValueExpression:forKeyPath:._passThroughSet.32825
+ _transformValueExpression:forKeyPath:._passThroughSet.34116
+ _transformValueExpression:forKeyPath:._passThroughSet.35476
+ _transformValueExpression:forKeyPath:._passThroughSet.39344
+ _transformValueExpression:forKeyPath:._passThroughSet.7509
+ _transformValueExpression:forKeyPath:._passThroughSet.7962
+ _transformValueExpression:forKeyPath:._passThroughSet.9346
+ _transformValueExpression:forKeyPath:._passThroughSet.9549
+ _transformValueExpression:forKeyPath:.onceToken.16809
+ _transformValueExpression:forKeyPath:.onceToken.20811
+ _transformValueExpression:forKeyPath:.onceToken.23863
+ _transformValueExpression:forKeyPath:.onceToken.24763
+ _transformValueExpression:forKeyPath:.onceToken.26590
+ _transformValueExpression:forKeyPath:.onceToken.2764
+ _transformValueExpression:forKeyPath:.onceToken.29825
+ _transformValueExpression:forKeyPath:.onceToken.32824
+ _transformValueExpression:forKeyPath:.onceToken.34115
+ _transformValueExpression:forKeyPath:.onceToken.35475
+ _transformValueExpression:forKeyPath:.onceToken.39343
+ _transformValueExpression:forKeyPath:.onceToken.7508
+ _transformValueExpression:forKeyPath:.onceToken.7961
+ _transformValueExpression:forKeyPath:.onceToken.9345
+ _transformValueExpression:forKeyPath:.onceToken.9548
- +[PHAssetResourceManager _nextManagerID]
- +[PHImageManager _nextManagerID]
- +[PHSuggestionWallpaperShuffleUtilities allPotentialSuggestionLocalIdentifierGroupsForPosterConfiguration:fromSuggestionLocalIdentifiersByFeature:withRejectedPersonLocalIdentifiers:]
- +[PHSuggestionWallpaperShuffleUtilities allPotentialSuggestionLocalIdentifiersForPosterConfiguration:fromSuggestionLocalIdentifiersByFeature:withRejectedPersonLocalIdentifiers:]
- +[PHSuggestionWallpaperShuffleUtilities chosenSuggestionLocalIdentifiersForPosterConfiguration:fromSuggestionLocalIdentifiersByFeature:atDate:usingStrategy:withRejectedPersonLocalIdentifiers:]
- +[PHSuggestionWallpaperShuffleUtilities chosenSuggestionLocalIdentifiersFromGroups:atDate:]
- +[PHSuggestionWallpaperShuffleUtilities chosenSuggestionLocalIdentifiersIn:atDate:]
- +[PHSuggestionWallpaperShuffleUtilities chosenSuggestionsForPosterConfiguration:atDate:inPhotoLibrary:]
- +[PHSuggestionWallpaperShuffleUtilities enumerateFeaturesOfPosterConfiguration:withRejectedPersonLocalIdentifiers:usingBlock:]
- +[PHSuggestionWallpaperShuffleUtilities matchingSuggestionInternalPredicateForPosterConfiguration:]
- +[PHSuggestionWallpaperShuffleUtilities mediaFromSuggestions:assetBySuggestionUUID:]
- +[PHSuggestionWallpaperShuffleUtilities setFeaturedStateOfSuggestions:]
- +[PHSuggestionWallpaperShuffleUtilities suggestionLocalIdentifiersByFeatureForPosterConfiguration:inPhotoLibrary:]
- -[AVAsset(Utilities) canPassthroughExport]
- -[AVAsset(Utilities) commonMetadataStringValueForKey:]
- -[AVAsset(Utilities) isMarkedNotSerializable]
- -[AVAsset(Utilities) localizedDisplayName]
- -[AVAsset(Utilities) mainAudioTrack]
- -[AVAsset(Utilities) mainVideoTrackNaturalSize]
- -[AVAsset(Utilities) mainVideoTrackNominalFrameRate]
- -[AVAsset(Utilities) mainVideoTrackPreferredSize]
- -[AVAsset(Utilities) mainVideoTrackPreferredTransform]
- -[AVAsset(Utilities) mainVideoTrack]
- -[AVAsset(Utilities) scaleFactors]
- -[AVAsset(Utilities) valuesForKeysAreFinishedLoading:]
- -[AVAssetTrack(Utilities) commonMetadataStringValueForKey:]
- -[PHAssetChangeRequest removeFromMyPhotoStream]
- -[PHAssetCreationPhotoStreamPublishingRequest .cxx_destruct]
- -[PHAssetCreationPhotoStreamPublishingRequest asset]
- -[PHAssetCreationPhotoStreamPublishingRequest fileURL]
- -[PHAssetCreationPhotoStreamPublishingRequest setAsset:]
- -[PHAssetCreationPhotoStreamPublishingRequest setFileURL:]
- -[PHAssetCreationRequest _photoStreamPublishingRequest]
- -[PHAssetCreationRequest _setPhotoStreamPublishingRequest:]
- -[PHImageManager _shouldUseRAWResourceAsUnadjustedBaseForAsset:options:]
- GCC_except_table10085
- GCC_except_table10158
- GCC_except_table10183
- GCC_except_table10217
- GCC_except_table10227
- GCC_except_table10245
- GCC_except_table10260
- GCC_except_table10299
- GCC_except_table10301
- GCC_except_table10303
- GCC_except_table10321
- GCC_except_table1043
- GCC_except_table1207
- GCC_except_table1210
- GCC_except_table1223
- GCC_except_table1415
- GCC_except_table1419
- GCC_except_table1421
- GCC_except_table1423
- GCC_except_table1425
- GCC_except_table1427
- GCC_except_table1429
- GCC_except_table1444
- GCC_except_table1456
- GCC_except_table1488
- GCC_except_table1490
- GCC_except_table1492
- GCC_except_table1494
- GCC_except_table1496
- GCC_except_table1498
- GCC_except_table1500
- GCC_except_table1502
- GCC_except_table1504
- GCC_except_table1506
- GCC_except_table1508
- GCC_except_table1510
- GCC_except_table1512
- GCC_except_table1514
- GCC_except_table1516
- GCC_except_table1518
- GCC_except_table1529
- GCC_except_table1537
- GCC_except_table1539
- GCC_except_table1567
- GCC_except_table1569
- GCC_except_table1572
- GCC_except_table1575
- GCC_except_table1624
- GCC_except_table1629
- GCC_except_table1637
- GCC_except_table1639
- GCC_except_table1651
- GCC_except_table1822
- GCC_except_table1827
- GCC_except_table1881
- GCC_except_table1985
- GCC_except_table2056
- GCC_except_table2059
- GCC_except_table2061
- GCC_except_table2073
- GCC_except_table2084
- GCC_except_table2089
- GCC_except_table2222
- GCC_except_table2226
- GCC_except_table2288
- GCC_except_table2296
- GCC_except_table2325
- GCC_except_table2329
- GCC_except_table2334
- GCC_except_table2412
- GCC_except_table2444
- GCC_except_table2450
- GCC_except_table2453
- GCC_except_table2463
- GCC_except_table2473
- GCC_except_table2476
- GCC_except_table2480
- GCC_except_table2484
- GCC_except_table2495
- GCC_except_table2500
- GCC_except_table2511
- GCC_except_table2512
- GCC_except_table2524
- GCC_except_table2626
- GCC_except_table2649
- GCC_except_table2651
- GCC_except_table2653
- GCC_except_table2696
- GCC_except_table2719
- GCC_except_table2752
- GCC_except_table2756
- GCC_except_table2759
- GCC_except_table2905
- GCC_except_table2938
- GCC_except_table2946
- GCC_except_table2959
- GCC_except_table2961
- GCC_except_table2986
- GCC_except_table2991
- GCC_except_table2992
- GCC_except_table3246
- GCC_except_table3251
- GCC_except_table3277
- GCC_except_table3286
- GCC_except_table3288
- GCC_except_table3292
- GCC_except_table3297
- GCC_except_table3308
- GCC_except_table3313
- GCC_except_table3326
- GCC_except_table3389
- GCC_except_table3647
- GCC_except_table3648
- GCC_except_table3655
- GCC_except_table3683
- GCC_except_table3685
- GCC_except_table3687
- GCC_except_table3745
- GCC_except_table3771
- GCC_except_table4220
- GCC_except_table4273
- GCC_except_table4300
- GCC_except_table4361
- GCC_except_table4366
- GCC_except_table4382
- GCC_except_table4387
- GCC_except_table4401
- GCC_except_table4404
- GCC_except_table4407
- GCC_except_table4420
- GCC_except_table4465
- GCC_except_table4476
- GCC_except_table4516
- GCC_except_table4542
- GCC_except_table4545
- GCC_except_table4551
- GCC_except_table4556
- GCC_except_table4579
- GCC_except_table4606
- GCC_except_table4631
- GCC_except_table4633
- GCC_except_table4644
- GCC_except_table4682
- GCC_except_table4753
- GCC_except_table4758
- GCC_except_table4876
- GCC_except_table4879
- GCC_except_table4892
- GCC_except_table4911
- GCC_except_table4924
- GCC_except_table4954
- GCC_except_table4988
- GCC_except_table4990
- GCC_except_table5294
- GCC_except_table5307
- GCC_except_table5320
- GCC_except_table5361
- GCC_except_table5364
- GCC_except_table5366
- GCC_except_table5368
- GCC_except_table5370
- GCC_except_table5401
- GCC_except_table5434
- GCC_except_table5436
- GCC_except_table5470
- GCC_except_table5654
- GCC_except_table5811
- GCC_except_table6004
- GCC_except_table6073
- GCC_except_table6095
- GCC_except_table6099
- GCC_except_table6105
- GCC_except_table6156
- GCC_except_table6261
- GCC_except_table6263
- GCC_except_table6308
- GCC_except_table6344
- GCC_except_table6348
- GCC_except_table6350
- GCC_except_table6352
- GCC_except_table6369
- GCC_except_table6405
- GCC_except_table6428
- GCC_except_table6515
- GCC_except_table6518
- GCC_except_table6536
- GCC_except_table6573
- GCC_except_table6596
- GCC_except_table6614
- GCC_except_table6674
- GCC_except_table6751
- GCC_except_table6880
- GCC_except_table6885
- GCC_except_table7170
- GCC_except_table7180
- GCC_except_table7211
- GCC_except_table7274
- GCC_except_table7301
- GCC_except_table7348
- GCC_except_table7350
- GCC_except_table7434
- GCC_except_table7508
- GCC_except_table7526
- GCC_except_table7611
- GCC_except_table7625
- GCC_except_table7634
- GCC_except_table7654
- GCC_except_table7656
- GCC_except_table7657
- GCC_except_table7658
- GCC_except_table7659
- GCC_except_table7660
- GCC_except_table7661
- GCC_except_table7662
- GCC_except_table7663
- GCC_except_table7664
- GCC_except_table7666
- GCC_except_table7667
- GCC_except_table7668
- GCC_except_table7669
- GCC_except_table7670
- GCC_except_table7671
- GCC_except_table7672
- GCC_except_table7673
- GCC_except_table7686
- GCC_except_table7695
- GCC_except_table7824
- GCC_except_table7833
- GCC_except_table7834
- GCC_except_table7835
- GCC_except_table7836
- GCC_except_table7837
- GCC_except_table7875
- GCC_except_table7876
- GCC_except_table7881
- GCC_except_table7903
- GCC_except_table7904
- GCC_except_table7905
- GCC_except_table7906
- GCC_except_table7907
- GCC_except_table7908
- GCC_except_table7909
- GCC_except_table7910
- GCC_except_table7939
- GCC_except_table7943
- GCC_except_table7962
- GCC_except_table7967
- GCC_except_table8034
- GCC_except_table8124
- GCC_except_table8182
- GCC_except_table8219
- GCC_except_table829
- GCC_except_table8293
- GCC_except_table8312
- GCC_except_table846
- GCC_except_table8883
- GCC_except_table8902
- GCC_except_table8904
- GCC_except_table8906
- GCC_except_table8908
- GCC_except_table8997
- GCC_except_table9097
- GCC_except_table9109
- GCC_except_table9147
- GCC_except_table9149
- GCC_except_table9162
- GCC_except_table9201
- GCC_except_table9239
- GCC_except_table9243
- GCC_except_table9252
- GCC_except_table9253
- GCC_except_table9260
- GCC_except_table9297
- GCC_except_table9304
- GCC_except_table9406
- GCC_except_table9412
- GCC_except_table9414
- GCC_except_table9460
- GCC_except_table9476
- GCC_except_table9486
- GCC_except_table9568
- GCC_except_table9656
- GCC_except_table9660
- GCC_except_table9664
- GCC_except_table9707
- GCC_except_table971
- GCC_except_table987
- _AVMediaTypeAudio
- _AVMediaTypeVideo
- _AVMetadataCommonKeyTitle
- _AVMetadataFormatISOUserData
- _AVMetadataFormatQuickTimeMetadata
- _AVMetadataKeySpaceISOUserData
- _AVMetadataKeySpaceQuickTimeMetadata
- _CGAffineTransformIdentity
- _OBJC_CLASS_$_AVAssetTrack
- _OBJC_CLASS_$_NSLocale
- _OBJC_CLASS_$_PFPosterMediaSuggestion
- _OBJC_CLASS_$_PHAssetCreationPhotoStreamPublishingRequest
- _OBJC_CLASS_$_PHSuggestionWallpaperShuffleUtilities
- _OBJC_CLASS_$_PLPhotoStreamsHelper
- _OBJC_IVAR_$_PHAssetChangeRequest._didRemoveFromPhotoStream
- _OBJC_IVAR_$_PHAssetCreationPhotoStreamPublishingRequest._asset
- _OBJC_IVAR_$_PHAssetCreationPhotoStreamPublishingRequest._fileURL
- _OBJC_IVAR_$_PHAssetCreationRequest.__photoStreamPublishingRequest
- _OBJC_IVAR_$_PHAssetResourceManager._lock
- _OBJC_IVAR_$_PHAssetResourceManager._requestsByID
- _OBJC_METACLASS_$_PHAssetCreationPhotoStreamPublishingRequest
- _OBJC_METACLASS_$_PHSuggestionWallpaperShuffleUtilities
- _PHSuggestionWallpaperShuffleMaximumCountPerDay
- _PLIsPreferences
- _PLMyPhotoStreamGetLog
- __OBJC_$_CATEGORY_AVAssetTrack_$_Utilities
- __OBJC_$_CATEGORY_AVAsset_$_Utilities
- __OBJC_$_CLASS_METHODS_PHPhotoLibrary(ImportDeDup|Import|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|PXCPLStatus|CloudIdentifiers|PHBatchFetchingArray|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
- __OBJC_$_CLASS_METHODS_PHSuggestionWallpaperShuffleUtilities
- __OBJC_$_INSTANCE_METHODS_AVAsset(Utilities)
- __OBJC_$_INSTANCE_METHODS_AVAssetTrack(Utilities)
- __OBJC_$_INSTANCE_METHODS_PHAssetCreationPhotoStreamPublishingRequest
- __OBJC_$_INSTANCE_METHODS_PHPhotoLibrary(ImportDeDup|Import|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|PXCPLStatus|CloudIdentifiers|PHBatchFetchingArray|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
- __OBJC_$_INSTANCE_VARIABLES_PHAssetCreationPhotoStreamPublishingRequest
- __OBJC_$_PROP_LIST_PHAssetCreationPhotoStreamPublishingRequest
- __OBJC_$_PROP_LIST_PHAssetResourceRequest.258
- __OBJC_CLASS_RO_$_PHAssetCreationPhotoStreamPublishingRequest
- __OBJC_CLASS_RO_$_PHSuggestionWallpaperShuffleUtilities
- __OBJC_METACLASS_RO_$_PHAssetCreationPhotoStreamPublishingRequest
- __OBJC_METACLASS_RO_$_PHSuggestionWallpaperShuffleUtilities
- ___101+[PHResourceLocalAvailabilityRequest indexesForAssetsRequiringResourceRetrieval:requestType:options:]_block_invoke.317
- ___114+[PHSuggestionWallpaperShuffleUtilities suggestionLocalIdentifiersByFeatureForPosterConfiguration:inPhotoLibrary:]_block_invoke
- ___177+[PHSuggestionWallpaperShuffleUtilities allPotentialSuggestionLocalIdentifiersForPosterConfiguration:fromSuggestionLocalIdentifiersByFeature:withRejectedPersonLocalIdentifiers:]_block_invoke
- ___182+[PHSuggestionWallpaperShuffleUtilities allPotentialSuggestionLocalIdentifierGroupsForPosterConfiguration:fromSuggestionLocalIdentifiersByFeature:withRejectedPersonLocalIdentifiers:]_block_invoke
- ___32+[PHImageManager _nextManagerID]_block_invoke
- ___40+[PHAssetResourceManager _nextManagerID]_block_invoke
- ___42-[AVAsset(Utilities) canPassthroughExport]_block_invoke
- ___43-[PHAssetResourceWriteRequest startRequest]_block_invoke
- ___63-[PHImageManager requestAVProxyForAsset:options:resultHandler:]_block_invoke.640
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.583
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.587
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.590
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_2.588
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_2.592
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_3.589
- ___68-[PHInternalAssetExportRequest exportWithOptions:completionHandler:]_block_invoke.50
- ___71+[PHSuggestionWallpaperShuffleUtilities setFeaturedStateOfSuggestions:]_block_invoke
- ___77-[PHAssetCreationRequest performTransactionCompletionHandlingInPhotoLibrary:]_block_invoke
- ___80-[PHAssetResourceManager reconnectAssets:urlResolvingHandler:completionHandler:]_block_invoke.126
- ___80-[PHAssetResourceManager reconnectAssets:urlResolvingHandler:completionHandler:]_block_invoke.133
- ___80-[PHAssetResourceManager reconnectAssets:urlResolvingHandler:completionHandler:]_block_invoke_2.134
- ___83-[PHImageManager requestContentEditingInputForAsset:withOptions:completionHandler:]_block_invoke.623
- ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.560
- ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.563
- ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.568
- ___89-[PHImageManager requestNewCGImageForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.613
- ___Block_byref_object_copy_.10256
- ___Block_byref_object_copy_.10907
- ___Block_byref_object_copy_.13037
- ___Block_byref_object_copy_.14565
- ___Block_byref_object_copy_.14729
- ___Block_byref_object_copy_.15024
- ___Block_byref_object_copy_.15474
- ___Block_byref_object_copy_.16045
- ___Block_byref_object_copy_.16214
- ___Block_byref_object_copy_.18175
- ___Block_byref_object_copy_.19320
- ___Block_byref_object_copy_.19831
- ___Block_byref_object_copy_.20164
- ___Block_byref_object_copy_.20439
- ___Block_byref_object_copy_.2115
- ___Block_byref_object_copy_.21316
- ___Block_byref_object_copy_.21624
- ___Block_byref_object_copy_.22414
- ___Block_byref_object_copy_.23015
- ___Block_byref_object_copy_.24422
- ___Block_byref_object_copy_.25009
- ___Block_byref_object_copy_.2543
- ___Block_byref_object_copy_.25815
- ___Block_byref_object_copy_.26061
- ___Block_byref_object_copy_.27070
- ___Block_byref_object_copy_.27518
- ___Block_byref_object_copy_.28612
- ___Block_byref_object_copy_.29084
- ___Block_byref_object_copy_.32468
- ___Block_byref_object_copy_.32702
- ___Block_byref_object_copy_.33611
- ___Block_byref_object_copy_.33992
- ___Block_byref_object_copy_.34170
- ___Block_byref_object_copy_.34457
- ___Block_byref_object_copy_.3513
- ___Block_byref_object_copy_.35139
- ___Block_byref_object_copy_.36044
- ___Block_byref_object_copy_.36216
- ___Block_byref_object_copy_.38042
- ___Block_byref_object_copy_.38325
- ___Block_byref_object_copy_.38838
- ___Block_byref_object_copy_.4511
- ___Block_byref_object_copy_.4740
- ___Block_byref_object_copy_.5873
- ___Block_byref_object_copy_.6849
- ___Block_byref_object_copy_.7445
- ___Block_byref_object_copy_.7650
- ___Block_byref_object_copy_.7816
- ___Block_byref_object_copy_.8386
- ___Block_byref_object_copy_.8614
- ___Block_byref_object_copy_.9049
- ___Block_byref_object_copy_.9460
- ___Block_byref_object_dispose_.10257
- ___Block_byref_object_dispose_.10908
- ___Block_byref_object_dispose_.13038
- ___Block_byref_object_dispose_.14566
- ___Block_byref_object_dispose_.14730
- ___Block_byref_object_dispose_.15025
- ___Block_byref_object_dispose_.15475
- ___Block_byref_object_dispose_.16046
- ___Block_byref_object_dispose_.16215
- ___Block_byref_object_dispose_.18176
- ___Block_byref_object_dispose_.19321
- ___Block_byref_object_dispose_.19832
- ___Block_byref_object_dispose_.20165
- ___Block_byref_object_dispose_.20440
- ___Block_byref_object_dispose_.2116
- ___Block_byref_object_dispose_.21317
- ___Block_byref_object_dispose_.21625
- ___Block_byref_object_dispose_.22415
- ___Block_byref_object_dispose_.23016
- ___Block_byref_object_dispose_.24423
- ___Block_byref_object_dispose_.25010
- ___Block_byref_object_dispose_.2544
- ___Block_byref_object_dispose_.25816
- ___Block_byref_object_dispose_.26062
- ___Block_byref_object_dispose_.27071
- ___Block_byref_object_dispose_.27519
- ___Block_byref_object_dispose_.28613
- ___Block_byref_object_dispose_.29085
- ___Block_byref_object_dispose_.32469
- ___Block_byref_object_dispose_.32703
- ___Block_byref_object_dispose_.33612
- ___Block_byref_object_dispose_.33993
- ___Block_byref_object_dispose_.34171
- ___Block_byref_object_dispose_.34458
- ___Block_byref_object_dispose_.3514
- ___Block_byref_object_dispose_.35140
- ___Block_byref_object_dispose_.36045
- ___Block_byref_object_dispose_.36217
- ___Block_byref_object_dispose_.38043
- ___Block_byref_object_dispose_.38326
- ___Block_byref_object_dispose_.38839
- ___Block_byref_object_dispose_.4512
- ___Block_byref_object_dispose_.4741
- ___Block_byref_object_dispose_.5874
- ___Block_byref_object_dispose_.6850
- ___Block_byref_object_dispose_.7446
- ___Block_byref_object_dispose_.7651
- ___Block_byref_object_dispose_.7817
- ___Block_byref_object_dispose_.8387
- ___Block_byref_object_dispose_.8615
- ___Block_byref_object_dispose_.9050
- ___Block_byref_object_dispose_.9461
- ____handleKeyUsageFailureDuringChoosing_block_invoke.203
- ____loadImageFromStoreAndKey_block_invoke.181
- ___block_descriptor_32_e31_v32?0"NSMutableArray"8Q16^B24l
- ___block_descriptor_48_e8_32s40s_e18_v16?0"NSString"8ls32l8s40l8
- ___block_literal_global.10311
- ___block_literal_global.1046
- ___block_literal_global.1055
- ___block_literal_global.1070
- ___block_literal_global.1088
- ___block_literal_global.112.30384
- ___block_literal_global.12553
- ___block_literal_global.130
- ___block_literal_global.13070
- ___block_literal_global.13124
- ___block_literal_global.136.35199
- ___block_literal_global.14246
- ___block_literal_global.14560
- ___block_literal_global.14980
- ___block_literal_global.15864
- ___block_literal_global.16725
- ___block_literal_global.184.35169
- ___block_literal_global.18522
- ___block_literal_global.19010
- ___block_literal_global.1944
- ___block_literal_global.19522
- ___block_literal_global.200.15727
- ___block_literal_global.20141
- ___block_literal_global.20740
- ___block_literal_global.20941
- ___block_literal_global.210.9767
- ___block_literal_global.212.9768
- ___block_literal_global.21328
- ___block_literal_global.21736
- ___block_literal_global.218
- ___block_literal_global.21908
- ___block_literal_global.2198
- ___block_literal_global.22049
- ___block_literal_global.22151
- ___block_literal_global.22426
- ___block_literal_global.225.24700
- ___block_literal_global.22613
- ___block_literal_global.229.24698
- ___block_literal_global.230.8644
- ___block_literal_global.23231
- ___block_literal_global.23360
- ___block_literal_global.23788
- ___block_literal_global.24703
- ___block_literal_global.24957
- ___block_literal_global.25159
- ___block_literal_global.25557
- ___block_literal_global.26066
- ___block_literal_global.26514
- ___block_literal_global.27384
- ___block_literal_global.2767
- ___block_literal_global.2806
- ___block_literal_global.28101
- ___block_literal_global.28373
- ___block_literal_global.28655
- ___block_literal_global.291
- ___block_literal_global.29197
- ___block_literal_global.293
- ___block_literal_global.295
- ___block_literal_global.29706
- ___block_literal_global.3.7671
- ___block_literal_global.30083
- ___block_literal_global.30390
- ___block_literal_global.304.27217
- ___block_literal_global.3164
- ___block_literal_global.31757
- ___block_literal_global.3228
- ___block_literal_global.32720
- ___block_literal_global.33014
- ___block_literal_global.33697
- ___block_literal_global.34021
- ___block_literal_global.34710
- ___block_literal_global.34801
- ___block_literal_global.35227
- ___block_literal_global.35372
- ___block_literal_global.36009
- ___block_literal_global.36218
- ___block_literal_global.36720
- ___block_literal_global.37.34794
- ___block_literal_global.37113
- ___block_literal_global.37794
- ___block_literal_global.38910
- ___block_literal_global.39391
- ___block_literal_global.4580
- ___block_literal_global.4790
- ___block_literal_global.51.7506
- ___block_literal_global.5158
- ___block_literal_global.530
- ___block_literal_global.5373
- ___block_literal_global.5525
- ___block_literal_global.557
- ___block_literal_global.6053
- ___block_literal_global.683.27119
- ___block_literal_global.6915
- ___block_literal_global.709.37984
- ___block_literal_global.741.26928
- ___block_literal_global.7511
- ___block_literal_global.7666
- ___block_literal_global.7905
- ___block_literal_global.81.39371
- ___block_literal_global.823.26926
- ___block_literal_global.8664
- ___block_literal_global.894.26881
- ___block_literal_global.896.26879
- ___block_literal_global.9296
- ___block_literal_global.9954
- __currentTimestampString.s_formatter.34795
- __currentTimestampString.s_onceToken.34793
- __nextManagerID._managerID
- __nextManagerID._managerID.38115
- __nextManagerID.onceToken
- __nextManagerID.onceToken.38114
- __unnamed_array_storage.10334
- __unnamed_array_storage.11842
- __unnamed_array_storage.13209
- __unnamed_array_storage.14.7854
- __unnamed_array_storage.15839
- __unnamed_array_storage.16434
- __unnamed_array_storage.166
- __unnamed_array_storage.180
- __unnamed_array_storage.18489
- __unnamed_array_storage.185
- __unnamed_array_storage.19.7852
- __unnamed_array_storage.20604
- __unnamed_array_storage.21351
- __unnamed_array_storage.246.35093
- __unnamed_array_storage.26610
- __unnamed_array_storage.2712
- __unnamed_array_storage.273
- __unnamed_array_storage.29227
- __unnamed_array_storage.29722
- __unnamed_array_storage.30404
- __unnamed_array_storage.30496
- __unnamed_array_storage.31764
- __unnamed_array_storage.34093
- __unnamed_array_storage.35241
- __unnamed_array_storage.38485
- __unnamed_array_storage.38822
- __unnamed_array_storage.39365
- __unnamed_array_storage.5500
- __unnamed_array_storage.6039
- __unnamed_array_storage.7842
- __unnamed_array_storage.8777
- __unnamed_array_storage.9086
- _allowedInfoKeys.allowedKeys.13286
- _allowedInfoKeys.allowedKeys.29888
- _allowedInfoKeys.onceToken.13285
- _allowedInfoKeys.onceToken.29887
- _corePropertiesToFetch.array.16728
- _corePropertiesToFetch.array.20737
- _corePropertiesToFetch.array.24704
- _corePropertiesToFetch.onceToken.16727
- _corePropertiesToFetch.onceToken.20736
- _corePropertiesToFetch.onceToken.24702
- _defaultManager.onceToken.38116
- _entityKeyMap.pl_once_object_0.23779
- _entityKeyMap.pl_once_object_0.5378
- _entityKeyMap.pl_once_object_0.7916
- _entityKeyMap.pl_once_object_2.20731
- _entityKeyMap.pl_once_object_2.26504
- _entityKeyMap.pl_once_object_2.29737
- _entityKeyMap.pl_once_object_2.32740
- _entityKeyMap.pl_once_object_2.34012
- _entityKeyMap.pl_once_object_2.35369
- _entityKeyMap.pl_once_object_2.7490
- _entityKeyMap.pl_once_object_2.9285
- _entityKeyMap.pl_once_object_2.9508
- _entityKeyMap.pl_once_object_3.24689
- _entityKeyMap.pl_once_object_3.39379
- _entityKeyMap.pl_once_token_0.23778
- _entityKeyMap.pl_once_token_0.5377
- _entityKeyMap.pl_once_token_0.7915
- _entityKeyMap.pl_once_token_2.20730
- _entityKeyMap.pl_once_token_2.26503
- _entityKeyMap.pl_once_token_2.29736
- _entityKeyMap.pl_once_token_2.32739
- _entityKeyMap.pl_once_token_2.34011
- _entityKeyMap.pl_once_token_2.35368
- _entityKeyMap.pl_once_token_2.7489
- _entityKeyMap.pl_once_token_2.9284
- _entityKeyMap.pl_once_token_2.9507
- _entityKeyMap.pl_once_token_3.24688
- _entityKeyMap.pl_once_token_3.39378
- _findMetedataItemInArray
- _identifierPropertiesToFetch.array.25558
- _identifierPropertiesToFetch.onceToken.25556
- _objc_msgSend$_nextManagerID
- _objc_msgSend$_photoStreamPublishingRequest
- _objc_msgSend$_setPhotoStreamPublishingRequest:
- _objc_msgSend$_shouldUseRAWResourceAsUnadjustedBaseForAsset:options:
- _objc_msgSend$allPotentialSuggestionLocalIdentifierGroupsForPosterConfiguration:fromSuggestionLocalIdentifiersByFeature:withRejectedPersonLocalIdentifiers:
- _objc_msgSend$allPotentialSuggestionLocalIdentifiersForPosterConfiguration:fromSuggestionLocalIdentifiersByFeature:withRejectedPersonLocalIdentifiers:
- _objc_msgSend$availableMetadataFormats
- _objc_msgSend$avalanchePickTypeIsVisible
- _objc_msgSend$chosenSuggestionLocalIdentifiersForPosterConfiguration:fromSuggestionLocalIdentifiersByFeature:atDate:usingStrategy:withRejectedPersonLocalIdentifiers:
- _objc_msgSend$chosenSuggestionLocalIdentifiersFromGroups:atDate:
- _objc_msgSend$chosenSuggestionLocalIdentifiersIn:atDate:
- _objc_msgSend$cleanupPhotoStreamMetadataForAssetsWithUUIDs:forStreamID:
- _objc_msgSend$commonMetadataStringValueForKey:
- _objc_msgSend$copyCGImageAtTime:actualTime:error:
- _objc_msgSend$currentLocale
- _objc_msgSend$enqueueAssetForPSPublishing:fullPath:fileSize:reenqueueCount:publicGlobalUUID:
- _objc_msgSend$enumerateFeaturesOfPosterConfiguration:withRejectedPersonLocalIdentifiers:usingBlock:
- _objc_msgSend$getBytes:length:
- _objc_msgSend$getDeletionWarningTitle:message:buttonTitle:forAssets:duplicatePhotoStreamCount:syndicationAssetCount:clientName:style:
- _objc_msgSend$initWithAssetUUID:suggestionUUID:suggestionSubtype:
- _objc_msgSend$initiateDeletionOfOriginalAssets:
- _objc_msgSend$isEnabled
- _objc_msgSend$mainVideoTrack
- _objc_msgSend$mainVideoTrackNaturalSize
- _objc_msgSend$mainVideoTrackPreferredTransform
- _objc_msgSend$matchingSuggestionInternalPredicateForPosterConfiguration:
- _objc_msgSend$metadataForFormat:
- _objc_msgSend$metadataItemsFromArray:withLocale:
- _objc_msgSend$personID
- _objc_msgSend$personLocalIdentifiers
- _objc_msgSend$photoStreamAlbums
- _objc_msgSend$photoStreamsEnabledForPhotoLibraryURL:
- _objc_msgSend$publicGlobalUUID
- _objc_msgSend$setDisableFileSystemPersistency:
- _objc_msgSend$setPhotoStreamTagId:
- _objc_msgSend$setPublicGlobalUUID:
- _objc_msgSend$sharedPhotoStreamsHelper
- _objc_msgSend$shouldHideAvalanchesFromPhotoStream
- _objc_msgSend$shuffleSmartAlbums
- _objc_msgSend$statusOfValueForKey:error:
- _objc_msgSend$suggestionLocalIdentifiersByFeatureForPosterConfiguration:inPhotoLibrary:
- _objc_msgSend$tracks
- _objc_msgSend$tracksWithMediaType:
- _propertiesToFetchWithHint:.array.17160
- _propertiesToFetchWithHint:.array.23789
- _propertiesToFetchWithHint:.array.26515
- _propertiesToFetchWithHint:.array.29758
- _propertiesToFetchWithHint:.array.34022
- _propertiesToFetchWithHint:.array.35373
- _propertiesToFetchWithHint:.array.36608
- _propertiesToFetchWithHint:.array.37342
- _propertiesToFetchWithHint:.array.5403
- _propertiesToFetchWithHint:.array.7502
- _propertiesToFetchWithHint:.array.7923
- _propertiesToFetchWithHint:.array.9533
- _propertiesToFetchWithHint:.onceToken.16722
- _propertiesToFetchWithHint:.onceToken.17159
- _propertiesToFetchWithHint:.onceToken.20739
- _propertiesToFetchWithHint:.onceToken.23787
- _propertiesToFetchWithHint:.onceToken.24694
- _propertiesToFetchWithHint:.onceToken.26513
- _propertiesToFetchWithHint:.onceToken.2766
- _propertiesToFetchWithHint:.onceToken.29757
- _propertiesToFetchWithHint:.onceToken.34020
- _propertiesToFetchWithHint:.onceToken.35371
- _propertiesToFetchWithHint:.onceToken.36607
- _propertiesToFetchWithHint:.onceToken.37341
- _propertiesToFetchWithHint:.onceToken.5402
- _propertiesToFetchWithHint:.onceToken.7501
- _propertiesToFetchWithHint:.onceToken.7922
- _propertiesToFetchWithHint:.onceToken.9295
- _propertiesToFetchWithHint:.onceToken.9532
- _propertiesToFetchWithHint:.propertiesToFetchByHint.16724
- _propertiesToFetchWithHint:.propertiesToFetchByHint.20742
- _propertiesToFetchWithHint:.propertiesToFetchByHint.24696
- _propertiesToFetchWithHint:.propertiesToFetchByHint.9298
- _propertiesToFetchWithHint:.propertyQueue.16723
- _propertiesToFetchWithHint:.propertyQueue.20741
- _propertiesToFetchWithHint:.propertyQueue.24695
- _propertiesToFetchWithHint:.propertyQueue.9297
- _propertiesToPrefetch.onceToken.16231
- _propertiesToPrefetch.onceToken.20416
- _propertiesToPrefetch.onceToken.24397
- _propertiesToPrefetch.propertiesToPrefetch.16232
- _propertiesToPrefetch.propertiesToPrefetch.20417
- _propertiesToPrefetch.propertiesToPrefetch.24398
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.20589
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.24664
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.9037
- _propertySetAccessorsByPropertySet.onceToken.20588
- _propertySetAccessorsByPropertySet.onceToken.24663
- _propertySetAccessorsByPropertySet.onceToken.9036
- _propertySetClassForPropertySet:.onceToken.20596
- _propertySetClassForPropertySet:.onceToken.24672
- _propertySetClassForPropertySet:.onceToken.9038
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.20597
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.24673
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.9039
- _sharedDecoder.s_onceToken.36719
- _sharedDecoder.s_shared.36721
- _transformValueExpression:forKeyPath:._passThroughSet.16692
- _transformValueExpression:forKeyPath:._passThroughSet.20723
- _transformValueExpression:forKeyPath:._passThroughSet.23770
- _transformValueExpression:forKeyPath:._passThroughSet.24677
- _transformValueExpression:forKeyPath:._passThroughSet.26498
- _transformValueExpression:forKeyPath:._passThroughSet.2755
- _transformValueExpression:forKeyPath:._passThroughSet.29726
- _transformValueExpression:forKeyPath:._passThroughSet.32725
- _transformValueExpression:forKeyPath:._passThroughSet.34003
- _transformValueExpression:forKeyPath:._passThroughSet.35366
- _transformValueExpression:forKeyPath:._passThroughSet.39339
- _transformValueExpression:forKeyPath:._passThroughSet.7463
- _transformValueExpression:forKeyPath:._passThroughSet.7912
- _transformValueExpression:forKeyPath:._passThroughSet.9280
- _transformValueExpression:forKeyPath:._passThroughSet.9489
- _transformValueExpression:forKeyPath:.onceToken.16691
- _transformValueExpression:forKeyPath:.onceToken.20722
- _transformValueExpression:forKeyPath:.onceToken.23769
- _transformValueExpression:forKeyPath:.onceToken.24676
- _transformValueExpression:forKeyPath:.onceToken.26497
- _transformValueExpression:forKeyPath:.onceToken.2754
- _transformValueExpression:forKeyPath:.onceToken.29725
- _transformValueExpression:forKeyPath:.onceToken.32724
- _transformValueExpression:forKeyPath:.onceToken.34002
- _transformValueExpression:forKeyPath:.onceToken.35365
- _transformValueExpression:forKeyPath:.onceToken.39338
- _transformValueExpression:forKeyPath:.onceToken.7462
- _transformValueExpression:forKeyPath:.onceToken.7911
- _transformValueExpression:forKeyPath:.onceToken.9279
- _transformValueExpression:forKeyPath:.onceToken.9488
CStrings:
+ "\x01!\x12#\"\x12"
+ "\x01\"\x12U"
+ "\x02\x13?\x01"
+ "\x11\x11\x12\x11\x12%"
+ "@\"<PHAssetResourceOwning>\""
+ "@\"PHMediaRequestContext\""
+ "@64@0:8@16i24Q28B36q40@?48@?56"
+ "CloudPhotoLibrary"
+ "Content editing input request on behalf of asset resource request failed"
+ "H264fourCharCode"
+ "HEVCfourCharCode"
+ "Q\""
+ "ResourcesToShareLookup"
+ "Supplementary content editing request failed"
+ "T@\"<PHAssetResourceOwning>\",R,N,V_asset"
+ "T@\"PHMediaRequestContext\",&,N,V_supplementaryRequestContext"
+ "TB,N,V_disallowFallbackAdjustmentBase"
+ "Td,N,V_targetHDRHeadroom"
+ "Tf,N,V_hdrGain"
+ "Tf,N,V_targetHDRHeadroom"
+ "Unable to start content editing request on behalf of asset resource request that is not backed by PHAsset"
+ "Wallpaper Favorites Smart Album"
+ "Wallpaper User Album"
+ "[PHResourceLocalAvailabilityRequest:%p] Using original/primary resource(s): %{BOOL}d for asset %{public}@ because it is edited: %{BOOL}d, known unsupported: %{BOOL}d, isRAW: %{BOOL}d, dontAllowRAW: %{BOOL}d, should use unmodified original: %{BOOL}d"
+ "[PHResourceLocalAvailabilityRequest] Resources to share duration %.5f, Resource info duration: %.5f"
+ "[PHResourceLocalAvailabilityRequest] Slower \"known unsupported formats\" lookup for asset: %{public}@. Type identifier: %{public}@, codec (if video): %{public}@"
+ "[RM] %ld-%ld Could not find media with base version %{public}@, error: %@"
+ "[RM] %ld-%ld Could not find media with base version %{public}@, retrying with base version %{public}@"
+ "[RM] %ld-%ld No media requests"
+ "[RM] %{public}@ asset resource request requires additional resources to generate adjustment on demand"
+ "[RM] %{public}@ asset resource request requires additional resources to generate adjustment on demand but retry count exceeded"
+ "[RM] %{public}@ media request requires additional resources to generate adjustment on demand"
+ "[RM] %{public}@ media request requires additional resources to generate adjustment on demand but retry count exceeded"
+ "[RM] %{public}@ video request requires additional resources to generate adjustment on demand"
+ "[RM] %{public}@ video request requires additional resources to generate adjustment on demand but retry count exceeded"
+ "[RM]: %@ adjustment data request finished with formatID: %@, version: %@, editor: %@"
+ "[RM]: %@ starting adjustment data request, sync: %@"
+ "_cloudInternalClient"
+ "_configuredError"
+ "_disallowFallbackAdjustmentBase"
+ "_lazyDataRequest"
+ "_requestsLock"
+ "_requestsLock_requestsByID"
+ "_requestsLock_supplementaryContextsByID"
+ "_supplementaryRequestContext"
+ "_targetHDRHeadroom"
+ "allShuffleWallpaperAlbumSuggestionSubtypes"
+ "assetResourceRequestDidRequestRetryWithContentEditingInputLoaded:"
+ "com.adobe.raw-image"
+ "configureWithError:"
+ "contentEditingInputRequestContextForAsset:requestID:managerID:networkAccessAllowed:downloadIntent:progressHandler:resultHandler:"
+ "copyCGImageFromImageGenerator:atTime:actualTime:error:"
+ "disallowFallbackAdjustmentBase"
+ "getDeletionWarningTitle:message:buttonTitle:forAssets:syndicationAssetCount:clientName:style:"
+ "isKnownUnsupportedFormatForAsset:"
+ "isPlayableFourCharCodecName:"
+ "kCGFallbackHDRGain"
+ "knownCompatibleVariantTypeIdentifierForTypeIdentifier:"
+ "mediaRequestDidRequestRetryWithContentEditingInputLoaded:"
+ "now"
+ "overrideSystemBudgetsForSyncSession:pauseReason:systemBudgets:completionHandler:"
+ "predicateForAllShuffleWallpaperAlbumSuggestions"
+ "resourceLocalAvailabilityRequestLog"
+ "setCloudPhotoLibraryPauseState:reason:"
+ "setDisallowFallbackAdjustmentBase:"
+ "setHdrGain:"
+ "setSupplementaryRequestContext:"
+ "setTargetHDRHeadroom:"
+ "shouldUseRAWResourceAsUnadjustedBaseForAsset:options:"
+ "supplementaryRequestContext"
+ "targetHDRHeadroom"
+ "v24@0:8@\"<PHAssetResourceRequest>\"16"
+ "v24@0:8@\"NSError\"16"
+ "v24@0:8B16s20"
+ "v44@0:8B16@20Q28@?36"
+ "\xd1"
- "\x01!\x12#\"\x11"
- "\x01\"\x12T"
- "\x02\x13?\x02"
- "\x11\x11\x12\"%"
- "%K = %d AND %K IN %@"
- "@\"PHAssetCreationPhotoStreamPublishingRequest\""
- "@56@0:8@16@24@32Q40@48"
- "Disk"
- "Failed to enqueue photo for publishing %@"
- "Failed to set featuredState for suggestions error:%@"
- "PHAssetCreationPhotoStreamPublishingRequest"
- "PHSuggestionWallpaperShuffleUtilities"
- "Q\x12"
- "T@\"AVAssetTrack\",R"
- "T@\"PHAssetCreationPhotoStreamPublishingRequest\",&,N,S_setPhotoStreamPublishingRequest:,V__photoStreamPublishingRequest"
- "Tf,R"
- "This API is only available for specific clients"
- "T{CGAffineTransform=dddddd},R"
- "T{CGSize=dd},R"
- "Utilities"
- "[RM] %ld-%ld Could not find media with base version %@, retrying with base version %@"
- "[RM]: %@ starting adjustment data request"
- "__photoStreamPublishingRequest"
- "_didRemoveFromPhotoStream"
- "_nextManagerID"
- "_photoStreamPublishingRequest"
- "_requestsByID"
- "_setPhotoStreamPublishingRequest:"
- "_shouldUseRAWResourceAsUnadjustedBaseForAsset:options:"
- "allPotentialSuggestionLocalIdentifierGroupsForPosterConfiguration:fromSuggestionLocalIdentifiersByFeature:withRejectedPersonLocalIdentifiers:"
- "allPotentialSuggestionLocalIdentifiersForPosterConfiguration:fromSuggestionLocalIdentifiersByFeature:withRejectedPersonLocalIdentifiers:"
- "availableMetadataFormats"
- "avalanchePickTypeIsVisible"
- "canPassthroughExport"
- "chosenSuggestionLocalIdentifiersForPosterConfiguration:fromSuggestionLocalIdentifiersByFeature:atDate:usingStrategy:withRejectedPersonLocalIdentifiers:"
- "chosenSuggestionLocalIdentifiersFromGroups:atDate:"
- "chosenSuggestionLocalIdentifiersIn:atDate:"
- "chosenSuggestionsForPosterConfiguration:atDate:inPhotoLibrary:"
- "cleanupPhotoStreamMetadataForAssetsWithUUIDs:forStreamID:"
- "com.apple.motion.notserializable"
- "com.apple.quicktime.pixeldensity"
- "commonMetadataStringValueForKey:"
- "copyCGImageAtTime:actualTime:error:"
- "currentLocale"
- "didRemoveFromPhotoStream"
- "enqueueAssetForPSPublishing:fullPath:fileSize:reenqueueCount:publicGlobalUUID:"
- "enumerateFeaturesOfPosterConfiguration:withRejectedPersonLocalIdentifiers:usingBlock:"
- "getBytes:length:"
- "getDeletionWarningTitle:message:buttonTitle:forAssets:duplicatePhotoStreamCount:syndicationAssetCount:clientName:style:"
- "heightPixels"
- "heightPoints"
- "initWithAssetUUID:suggestionUUID:suggestionSubtype:"
- "initiateDeletionOfOriginalAssets:"
- "isEnabled"
- "isMarkedNotSerializable"
- "localizedDisplayName"
- "mainAudioTrack"
- "mainVideoTrack"
- "mainVideoTrackNaturalSize"
- "mainVideoTrackNominalFrameRate"
- "mainVideoTrackPreferredSize"
- "mainVideoTrackPreferredTransform"
- "matchingSuggestionInternalPredicateForPosterConfiguration:"
- "mediaFromSuggestions:assetBySuggestionUUID:"
- "metadataForFormat:"
- "metadataItemsFromArray:withLocale:"
- "personID"
- "personLocalIdentifiers"
- "photoStreamAlbums"
- "photoStreamsEnabledForPhotoLibraryURL:"
- "publicGlobalUUID"
- "publicGlobalUUID should be set here"
- "removeFromMyPhotoStream"
- "scaleFactors"
- "setDisableFileSystemPersistency:"
- "setFeaturedStateOfSuggestions:"
- "setPhotoStreamTagId:"
- "setPublicGlobalUUID:"
- "sharedPhotoStreamsHelper"
- "shouldHideAvalanchesFromPhotoStream"
- "shuffleSmartAlbums"
- "statusOfValueForKey:error:"
- "suggestionLocalIdentifiersByFeatureForPosterConfiguration:inPhotoLibrary:"
- "tracks"
- "tracksWithMediaType:"
- "v16@?0@\"NSString\"8"
- "v32@?0@\"NSMutableArray\"8Q16^B24"
- "valuesForKeysAreFinishedLoading:"
- "widthPixels"
- "widthPoints"
- "{CGAffineTransform=dddddd}16@0:8"
- "\xc1"

```
