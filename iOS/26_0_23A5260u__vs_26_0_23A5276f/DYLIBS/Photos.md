## Photos

> `/System/Library/Frameworks/Photos.framework/Photos`

```diff

-800.14.111.0.0
-  __TEXT.__text: 0x28b458
-  __TEXT.__auth_stubs: 0x2b00
-  __TEXT.__objc_methlist: 0x23e74
+800.20.101.0.0
+  __TEXT.__text: 0x28e37c
+  __TEXT.__auth_stubs: 0x2b20
+  __TEXT.__objc_methlist: 0x2405c
   __TEXT.__const: 0x1180
   __TEXT.__dlopen_cstrs: 0x239
   __TEXT.__swift5_typeref: 0x336

   __TEXT.__constg_swiftt: 0x344
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_fieldmd: 0xec
-  __TEXT.__cstring: 0x2b26d
+  __TEXT.__cstring: 0x2b5b9
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_capture: 0x6c
-  __TEXT.__gcc_except_tab: 0x9abc
-  __TEXT.__oslogstring: 0x1c518
+  __TEXT.__gcc_except_tab: 0x9b88
+  __TEXT.__oslogstring: 0x1caa2
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x8500
+  __TEXT.__unwind_info: 0x8540
   __TEXT.__eh_frame: 0x100
-  __TEXT.__objc_classname: 0x36c1
-  __TEXT.__objc_methname: 0x6abc0
-  __TEXT.__objc_methtype: 0x6d12
-  __TEXT.__objc_stubs: 0x39540
-  __DATA_CONST.__got: 0x26c8
-  __DATA_CONST.__const: 0x7df0
-  __DATA_CONST.__objc_classlist: 0xda8
+  __TEXT.__objc_classname: 0x3704
+  __TEXT.__objc_methname: 0x6b2a5
+  __TEXT.__objc_methtype: 0x6d86
+  __TEXT.__objc_stubs: 0x39800
+  __DATA_CONST.__got: 0x26e0
+  __DATA_CONST.__const: 0x7ee8
+  __DATA_CONST.__objc_classlist: 0xdb8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12d78
+  __DATA_CONST.__objc_selrefs: 0x12e38
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0xb38
+  __DATA_CONST.__objc_superrefs: 0xb48
   __DATA_CONST.__objc_arraydata: 0x948
-  __AUTH_CONST.__auth_got: 0x1590
+  __AUTH_CONST.__auth_got: 0x15a0
   __AUTH_CONST.__const: 0x3c28
-  __AUTH_CONST.__cfstring: 0x27fc0
-  __AUTH_CONST.__objc_const: 0x3ce40
-  __AUTH_CONST.__objc_intobj: 0x1fe0
+  __AUTH_CONST.__cfstring: 0x281a0
+  __AUTH_CONST.__objc_const: 0x3d3a0
+  __AUTH_CONST.__objc_intobj: 0x1ff8
   __AUTH_CONST.__objc_arrayobj: 0x6d8
   __AUTH_CONST.__objc_doubleobj: 0x130
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0x6ee8
+  __AUTH.__objc_data: 0x6fd8
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x31bc
+  __DATA.__objc_ivar: 0x3230
   __DATA.__data: 0x2920
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1868
+  __DATA.__bss: 0x1888
   __DATA.__common: 0x55
-  __DATA_DIRTY.__objc_data: 0x19c0
+  __DATA_DIRTY.__objc_data: 0x1970
   __DATA_DIRTY.__data: 0x148
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1E752021-DB84-30A2-AE42-0E95695C4B65
-  Functions: 13434
-  Symbols:   44963
-  CStrings:  28788
+  UUID: 2056D10B-FC6F-3620-B08A-8EA5F77D9ED3
+  Functions: 13488
+  Symbols:   45137
+  CStrings:  28893
 
Symbols:
+ +[PHAnalysisCoalescer _analyzeBufferedAssets:inLibrary:]
+ +[PHAnalysisCoalescer _logFailureIfNeededForResult:andFeature:]
+ +[PHAssetCollection fetchMomentsNeedingThemeAnalysisWithAdapterVersion:uemVersion:options:]
+ +[PHInternalAssetExportRequest isHDRScreenshotAsset:withCurrentType:]
+ +[PHPhotoLibraryChangeObserverRegistrar _isInternalObserver:]
+ +[PHQuery queryForContributorForComment:options:]
+ +[PHSearchQuery _triggerQueryTimeoutTapToRadarForQuery:]
+ +[PHSensitiveContentAnalysisUtility sensitivityAnalysisFromAsset:outError:]
+ +[PHShareParticipant fetchContributorForComment:options:]
+ -[PHAnalysisCoalescer .cxx_destruct]
+ -[PHAnalysisCoalescer _snapshotOfBufferedAssets]
+ -[PHAnalysisCoalescer coalesceAndAnalyzeAssets:forFeature:]
+ -[PHAnalysisCoalescer initWithLibrary:]
+ -[PHAssetCollection modificationDate]
+ -[PHAssetResourceRequest retryInterval]
+ -[PHAssetResourceRequest setRetryInterval:]
+ -[PHAssetResourceUploadJobChangeRequest initForNewObjectWithRequestData:]
+ -[PHAssetResourceUploadJobChangeRequest initWithUUID:objectID:requestData:]
+ -[PHAssetResourceWriteRequest retryInterval]
+ -[PHAssetResourceWriteRequest setRetryInterval:]
+ -[PHCollection modificationDate]
+ -[PHCollectionList modificationDate]
+ -[PHCollectionShare cloudItemCount]
+ -[PHCollectionShare cloudPhotoCount]
+ -[PHCollectionShare cloudVideoCount]
+ -[PHFetchResult _handleInitWithInvalidConfigurationDetails:library:]
+ -[PHFetchResult initWithMediaTypeCounts:library:]
+ -[PHFetchResult initWithQuery:library:]
+ -[PHFetchResult initWithQuery:library:oids:registerIfNeeded:usingManagedObjectContext:]
+ -[PHFetchResult initWithQuery:library:registerIfNeeded:]
+ -[PHMediaRequest retryInterval]
+ -[PHMediaRequest setRetryInterval:]
+ -[PHMomentChangeRequest adapterVersionForEmptyThemeAssignment]
+ -[PHMomentChangeRequest adapterVersionForVersionOverwrite]
+ -[PHMomentChangeRequest addAssetSearchEntityWithLabel:identifier:type:confidence:localeIdentifier:dateInterval:synonyms:]
+ -[PHMomentChangeRequest assignEmptyThemeWithAdapterVersion:uemVersion:]
+ -[PHMomentChangeRequest assignThemeNamed:adapterVersion:uemVersion:confidence:]
+ -[PHMomentChangeRequest resetThemeAssignmentVersions]
+ -[PHMomentChangeRequest setAdapterVersionForEmptyThemeAssignment:]
+ -[PHMomentChangeRequest setAdapterVersionForVersionOverwrite:]
+ -[PHMomentChangeRequest setShouldOverwriteExistingThemeVersions:]
+ -[PHMomentChangeRequest setUemVersionForEmptyThemeAssignment:]
+ -[PHMomentChangeRequest setUemVersionForVersionOverwrite:]
+ -[PHMomentChangeRequest shouldOverwriteExistingThemeVersions]
+ -[PHMomentChangeRequest uemVersionForEmptyThemeAssignment]
+ -[PHMomentChangeRequest uemVersionForVersionOverwrite]
+ -[PHMomentShare cloudItemCount]
+ -[PHMomentShare cloudPhotoCount]
+ -[PHMomentShare cloudVideoCount]
+ -[PHMomentThemeAssignment adapterVersion]
+ -[PHMomentThemeAssignment initWithThemeName:confidence:adapterVersion:uemVersion:]
+ -[PHMomentThemeAssignment uemVersion]
+ -[PHPerformChangesRequest setWaitForDelayedSaveActions:]
+ -[PHPerformChangesRequest waitForDelayedSaveActions]
+ -[PHPhotoLibrary _addChangeObservers:authorizationStatus:]
+ -[PHPhotoLibrary _addCloudStatusObservers:authorizationStatus:]
+ -[PHPhotoLibrary _processCPLStatusDidChange:]
+ -[PHPhotoLibrary _publishCloudStatusUpdate:]
+ -[PHPhotoLibrary _removeChangeObserver:]
+ -[PHPhotoLibrary _removeCloudStatusObserver:]
+ -[PHPhotoLibrary _setupLazyCPLStatusIfNecessary]
+ -[PHPhotoLibrary analysisCoalescer]
+ -[PHPhotoLibrary registerCloudStatusObserver:]
+ -[PHPhotoLibrary setWaitForDelayedSaveActions:]
+ -[PHPhotoLibrary unregisterCloudStatusObserver:]
+ -[PHPhotoLibrary waitForDelayedSaveActions]
+ -[PHPhotoLibrary(AssetAnalysis) coalesceAndAnalyzeAssets:forFeature:]
+ -[PHPhotoLibraryChangeObserverRegistrar .cxx_destruct]
+ -[PHPhotoLibraryChangeObserverRegistrar _lock_clearOIDCache]
+ -[PHPhotoLibraryChangeObserverRegistrar _lock_hasChangeObservers]
+ -[PHPhotoLibraryChangeObserverRegistrar _lock_pauseChangeHandlingIfNeeded]
+ -[PHPhotoLibraryChangeObserverRegistrar _lock_resumeChangeHandlingIfNeeded]
+ -[PHPhotoLibraryChangeObserverRegistrar addObservers:authorizationStatus:]
+ -[PHPhotoLibraryChangeObserverRegistrar clearIsChangeProcessingPending]
+ -[PHPhotoLibraryChangeObserverRegistrar clearsOIDCacheAfterFetchResultDealloc]
+ -[PHPhotoLibraryChangeObserverRegistrar countOfRegisteredFetchResults]
+ -[PHPhotoLibraryChangeObserverRegistrar dealloc]
+ -[PHPhotoLibraryChangeObserverRegistrar getObserversWithBlock:]
+ -[PHPhotoLibraryChangeObserverRegistrar initWithLibraryBundle:changeHandlingDebugger:uniqueObjectIDCache:]
+ -[PHPhotoLibraryChangeObserverRegistrar postsPersistentHistoryChangedNotifications]
+ -[PHPhotoLibraryChangeObserverRegistrar publishChangesToObserversOnQueue:withDebugEvent:block:]
+ -[PHPhotoLibraryChangeObserverRegistrar registerFetchResult:]
+ -[PHPhotoLibraryChangeObserverRegistrar removeObserver:]
+ -[PHPhotoLibraryChangeObserverRegistrar setClearsOIDCacheAfterFetchResultDealloc:]
+ -[PHPhotoLibraryChangeObserverRegistrar setPostsPersistentHistoryChangedNotifications:]
+ -[PHPhotoLibraryChangeObserverRegistrar throttlePendingChangesTimerFiredWithBlock:]
+ -[PHPhotoLibraryChangeObserverRegistrar throttlePendingChangesWithDebugEvent:block:]
+ -[PHPhotoLibraryChangeObserverRegistrar unregisterFetchResult:]
+ -[PHPhotoLibraryCloudStatus firstSyncCompletionDate]
+ -[PHPhotoLibraryCloudStatus hash]
+ -[PHPhotoLibraryCloudStatus initWithCPLStatus:isEnabled:]
+ -[PHPhotoLibraryCloudStatus lastSyncProgressDate]
+ -[PHPhotoLibraryCloudStatus statusDescription]
+ -[PHPhotoLibraryCloudStatusObserverRegistrar .cxx_destruct]
+ -[PHPhotoLibraryCloudStatusObserverRegistrar _lock_hasCloudStatusObservers]
+ -[PHPhotoLibraryCloudStatusObserverRegistrar _lock_pauseCloudStatusHandlingIfNeeded]
+ -[PHPhotoLibraryCloudStatusObserverRegistrar _lock_resumeCloudStatusHandlingIfNeeded]
+ -[PHPhotoLibraryCloudStatusObserverRegistrar addObservers:authorizationStatus:]
+ -[PHPhotoLibraryCloudStatusObserverRegistrar beginObservingCloudStatusBlock]
+ -[PHPhotoLibraryCloudStatusObserverRegistrar dealloc]
+ -[PHPhotoLibraryCloudStatusObserverRegistrar getObserversWithBlock:]
+ -[PHPhotoLibraryCloudStatusObserverRegistrar hasObservers]
+ -[PHPhotoLibraryCloudStatusObserverRegistrar initWithLibraryBundle:]
+ -[PHPhotoLibraryCloudStatusObserverRegistrar removeObserver:]
+ -[PHPhotoLibraryCloudStatusObserverRegistrar setBeginObservingCloudStatusBlock:]
+ -[PHSearchEntityCreationRequest addSearchRankingWithLabel:identifier:type:rankingScore:localeIdentifier:synonyms:]
+ -[_PHValidation assert:code:failureType:format:]
+ GCC_except_table10029
+ GCC_except_table10033
+ GCC_except_table10052
+ GCC_except_table10057
+ GCC_except_table10127
+ GCC_except_table10220
+ GCC_except_table10360
+ GCC_except_table10397
+ GCC_except_table10487
+ GCC_except_table10515
+ GCC_except_table11008
+ GCC_except_table11163
+ GCC_except_table11166
+ GCC_except_table11171
+ GCC_except_table11177
+ GCC_except_table11181
+ GCC_except_table11187
+ GCC_except_table11293
+ GCC_except_table11314
+ GCC_except_table11316
+ GCC_except_table11318
+ GCC_except_table11353
+ GCC_except_table11400
+ GCC_except_table11407
+ GCC_except_table11409
+ GCC_except_table11411
+ GCC_except_table11417
+ GCC_except_table11454
+ GCC_except_table11600
+ GCC_except_table11612
+ GCC_except_table11654
+ GCC_except_table11656
+ GCC_except_table11669
+ GCC_except_table11768
+ GCC_except_table11772
+ GCC_except_table11811
+ GCC_except_table11815
+ GCC_except_table11824
+ GCC_except_table11825
+ GCC_except_table11832
+ GCC_except_table11869
+ GCC_except_table11876
+ GCC_except_table11920
+ GCC_except_table12004
+ GCC_except_table12007
+ GCC_except_table12013
+ GCC_except_table12015
+ GCC_except_table12055
+ GCC_except_table12074
+ GCC_except_table12083
+ GCC_except_table12137
+ GCC_except_table12139
+ GCC_except_table12199
+ GCC_except_table12343
+ GCC_except_table12351
+ GCC_except_table12388
+ GCC_except_table12412
+ GCC_except_table12419
+ GCC_except_table12627
+ GCC_except_table12869
+ GCC_except_table12946
+ GCC_except_table12991
+ GCC_except_table13038
+ GCC_except_table13048
+ GCC_except_table13066
+ GCC_except_table13081
+ GCC_except_table13110
+ GCC_except_table13123
+ GCC_except_table13125
+ GCC_except_table13127
+ GCC_except_table13146
+ GCC_except_table13228
+ GCC_except_table13234
+ GCC_except_table13250
+ GCC_except_table1389
+ GCC_except_table1408
+ GCC_except_table1708
+ GCC_except_table1712
+ GCC_except_table1726
+ GCC_except_table1741
+ GCC_except_table1927
+ GCC_except_table1931
+ GCC_except_table1933
+ GCC_except_table1935
+ GCC_except_table1937
+ GCC_except_table1939
+ GCC_except_table1944
+ GCC_except_table1951
+ GCC_except_table1953
+ GCC_except_table1955
+ GCC_except_table1967
+ GCC_except_table1999
+ GCC_except_table2001
+ GCC_except_table2003
+ GCC_except_table2005
+ GCC_except_table2007
+ GCC_except_table2009
+ GCC_except_table2011
+ GCC_except_table2013
+ GCC_except_table2015
+ GCC_except_table2017
+ GCC_except_table2019
+ GCC_except_table2021
+ GCC_except_table2023
+ GCC_except_table2025
+ GCC_except_table2027
+ GCC_except_table2032
+ GCC_except_table2034
+ GCC_except_table2036
+ GCC_except_table2038
+ GCC_except_table2043
+ GCC_except_table2048
+ GCC_except_table2050
+ GCC_except_table2052
+ GCC_except_table2080
+ GCC_except_table2088
+ GCC_except_table2194
+ GCC_except_table2199
+ GCC_except_table2207
+ GCC_except_table2217
+ GCC_except_table2257
+ GCC_except_table2436
+ GCC_except_table2451
+ GCC_except_table2472
+ GCC_except_table2478
+ GCC_except_table2511
+ GCC_except_table2516
+ GCC_except_table2572
+ GCC_except_table2668
+ GCC_except_table2679
+ GCC_except_table2681
+ GCC_except_table2715
+ GCC_except_table2789
+ GCC_except_table2794
+ GCC_except_table2802
+ GCC_except_table2812
+ GCC_except_table2823
+ GCC_except_table2828
+ GCC_except_table2959
+ GCC_except_table2966
+ GCC_except_table3033
+ GCC_except_table3041
+ GCC_except_table3070
+ GCC_except_table3074
+ GCC_except_table3079
+ GCC_except_table3195
+ GCC_except_table3228
+ GCC_except_table3234
+ GCC_except_table3237
+ GCC_except_table3251
+ GCC_except_table3257
+ GCC_except_table3268
+ GCC_except_table3279
+ GCC_except_table3284
+ GCC_except_table3295
+ GCC_except_table3296
+ GCC_except_table3312
+ GCC_except_table3321
+ GCC_except_table3418
+ GCC_except_table3442
+ GCC_except_table3444
+ GCC_except_table3491
+ GCC_except_table3518
+ GCC_except_table3549
+ GCC_except_table3551
+ GCC_except_table3571
+ GCC_except_table3574
+ GCC_except_table3784
+ GCC_except_table3786
+ GCC_except_table3808
+ GCC_except_table3843
+ GCC_except_table3851
+ GCC_except_table3853
+ GCC_except_table3871
+ GCC_except_table3873
+ GCC_except_table3910
+ GCC_except_table3911
+ GCC_except_table4173
+ GCC_except_table4179
+ GCC_except_table4206
+ GCC_except_table4231
+ GCC_except_table4235
+ GCC_except_table4240
+ GCC_except_table4251
+ GCC_except_table4255
+ GCC_except_table4268
+ GCC_except_table4334
+ GCC_except_table4645
+ GCC_except_table4652
+ GCC_except_table4716
+ GCC_except_table4722
+ GCC_except_table4724
+ GCC_except_table4727
+ GCC_except_table4796
+ GCC_except_table4801
+ GCC_except_table4830
+ GCC_except_table4977
+ GCC_except_table5332
+ GCC_except_table5381
+ GCC_except_table5411
+ GCC_except_table5424
+ GCC_except_table5426
+ GCC_except_table5454
+ GCC_except_table5458
+ GCC_except_table5463
+ GCC_except_table5471
+ GCC_except_table5475
+ GCC_except_table5484
+ GCC_except_table5488
+ GCC_except_table5525
+ GCC_except_table5533
+ GCC_except_table5563
+ GCC_except_table5593
+ GCC_except_table5597
+ GCC_except_table5615
+ GCC_except_table5621
+ GCC_except_table5625
+ GCC_except_table5639
+ GCC_except_table5642
+ GCC_except_table5645
+ GCC_except_table5666
+ GCC_except_table5710
+ GCC_except_table5721
+ GCC_except_table5768
+ GCC_except_table5799
+ GCC_except_table5802
+ GCC_except_table5808
+ GCC_except_table5812
+ GCC_except_table5841
+ GCC_except_table5871
+ GCC_except_table5897
+ GCC_except_table5899
+ GCC_except_table5910
+ GCC_except_table5957
+ GCC_except_table6033
+ GCC_except_table6038
+ GCC_except_table6043
+ GCC_except_table6175
+ GCC_except_table6178
+ GCC_except_table6191
+ GCC_except_table6215
+ GCC_except_table6225
+ GCC_except_table6228
+ GCC_except_table6265
+ GCC_except_table6302
+ GCC_except_table6304
+ GCC_except_table6689
+ GCC_except_table6702
+ GCC_except_table6715
+ GCC_except_table6732
+ GCC_except_table6761
+ GCC_except_table6764
+ GCC_except_table6766
+ GCC_except_table6768
+ GCC_except_table6770
+ GCC_except_table6778
+ GCC_except_table6821
+ GCC_except_table6834
+ GCC_except_table6867
+ GCC_except_table6869
+ GCC_except_table6908
+ GCC_except_table7168
+ GCC_except_table7169
+ GCC_except_table7179
+ GCC_except_table7186
+ GCC_except_table7202
+ GCC_except_table7204
+ GCC_except_table7205
+ GCC_except_table7206
+ GCC_except_table7207
+ GCC_except_table7208
+ GCC_except_table7209
+ GCC_except_table7220
+ GCC_except_table7221
+ GCC_except_table7222
+ GCC_except_table7379
+ GCC_except_table7597
+ GCC_except_table7623
+ GCC_except_table7642
+ GCC_except_table7643
+ GCC_except_table7726
+ GCC_except_table7730
+ GCC_except_table7736
+ GCC_except_table7787
+ GCC_except_table7946
+ GCC_except_table7948
+ GCC_except_table7995
+ GCC_except_table8035
+ GCC_except_table8039
+ GCC_except_table8041
+ GCC_except_table8043
+ GCC_except_table8055
+ GCC_except_table8060
+ GCC_except_table8100
+ GCC_except_table8128
+ GCC_except_table8254
+ GCC_except_table8312
+ GCC_except_table8332
+ GCC_except_table8335
+ GCC_except_table8354
+ GCC_except_table8416
+ GCC_except_table8420
+ GCC_except_table8424
+ GCC_except_table8433
+ GCC_except_table8435
+ GCC_except_table8475
+ GCC_except_table8539
+ GCC_except_table8696
+ GCC_except_table8737
+ GCC_except_table8742
+ GCC_except_table8987
+ GCC_except_table8991
+ GCC_except_table8995
+ GCC_except_table8997
+ GCC_except_table9023
+ GCC_except_table9024
+ GCC_except_table9116
+ GCC_except_table9126
+ GCC_except_table9158
+ GCC_except_table9209
+ GCC_except_table9243
+ GCC_except_table9263
+ GCC_except_table9290
+ GCC_except_table9313
+ GCC_except_table9346
+ GCC_except_table9348
+ GCC_except_table9438
+ GCC_except_table9529
+ GCC_except_table9648
+ GCC_except_table9754
+ GCC_except_table9755
+ GCC_except_table9756
+ GCC_except_table9757
+ GCC_except_table9758
+ GCC_except_table9759
+ GCC_except_table9760
+ GCC_except_table9761
+ GCC_except_table9762
+ GCC_except_table9763
+ GCC_except_table9764
+ GCC_except_table9765
+ GCC_except_table9766
+ GCC_except_table9767
+ GCC_except_table9768
+ GCC_except_table9769
+ GCC_except_table9770
+ GCC_except_table9771
+ GCC_except_table9772
+ GCC_except_table9773
+ GCC_except_table9774
+ GCC_except_table9775
+ GCC_except_table9776
+ GCC_except_table9777
+ GCC_except_table9778
+ GCC_except_table9779
+ GCC_except_table9780
+ GCC_except_table9781
+ GCC_except_table9782
+ GCC_except_table9783
+ GCC_except_table9784
+ GCC_except_table9785
+ GCC_except_table9786
+ GCC_except_table9787
+ GCC_except_table9788
+ GCC_except_table9789
+ GCC_except_table9790
+ GCC_except_table9791
+ GCC_except_table9792
+ GCC_except_table9888
+ GCC_except_table9897
+ GCC_except_table9898
+ GCC_except_table9899
+ GCC_except_table9900
+ GCC_except_table9901
+ GCC_except_table9903
+ GCC_except_table9908
+ GCC_except_table9926
+ GCC_except_table9954
+ GCC_except_table9964
+ GCC_except_table9984
+ GCC_except_table9985
+ GCC_except_table9986
+ GCC_except_table9987
+ GCC_except_table9988
+ GCC_except_table9990
+ GCC_except_table9991
+ GCC_except_table9992
+ _OBJC_CLASS_$_PHAnalysisCoalescer
+ _OBJC_CLASS_$_PHPhotoLibraryChangeObserverRegistrar
+ _OBJC_CLASS_$_PHPhotoLibraryCloudStatusObserverRegistrar
+ _OBJC_CLASS_$_PLSearchIndexCountrySynonymProvider
+ _OBJC_IVAR_$_PHAnalysisCoalescer._lock
+ _OBJC_IVAR_$_PHAnalysisCoalescer._lock_assetUUIDsByFeature
+ _OBJC_IVAR_$_PHAnalysisCoalescer._lock_pendingBlock
+ _OBJC_IVAR_$_PHAnalysisCoalescer._photoLibrary
+ _OBJC_IVAR_$_PHAnalysisCoalescer._queue
+ _OBJC_IVAR_$_PHAssetCollection._modificationDate
+ _OBJC_IVAR_$_PHAssetResourceRequest._retryInterval
+ _OBJC_IVAR_$_PHCollection._modificationDate
+ _OBJC_IVAR_$_PHCollectionList._modificationDate
+ _OBJC_IVAR_$_PHCollectionShare._cloudItemCount
+ _OBJC_IVAR_$_PHCollectionShare._cloudPhotoCount
+ _OBJC_IVAR_$_PHCollectionShare._cloudVideoCount
+ _OBJC_IVAR_$_PHMediaRequest._retryInterval
+ _OBJC_IVAR_$_PHMomentChangeRequest._adapterVersionForEmptyThemeAssignment
+ _OBJC_IVAR_$_PHMomentChangeRequest._adapterVersionForVersionOverwrite
+ _OBJC_IVAR_$_PHMomentChangeRequest._shouldOverwriteExistingThemeVersions
+ _OBJC_IVAR_$_PHMomentChangeRequest._uemVersionForEmptyThemeAssignment
+ _OBJC_IVAR_$_PHMomentChangeRequest._uemVersionForVersionOverwrite
+ _OBJC_IVAR_$_PHMomentShare._cloudItemCount
+ _OBJC_IVAR_$_PHMomentShare._cloudPhotoCount
+ _OBJC_IVAR_$_PHMomentShare._cloudVideoCount
+ _OBJC_IVAR_$_PHMomentThemeAssignment._adapterVersion
+ _OBJC_IVAR_$_PHMomentThemeAssignment._uemVersion
+ _OBJC_IVAR_$_PHPerformChangesRequest._waitForDelayedSaveActions
+ _OBJC_IVAR_$_PHPhotoLibrary._changeObserverRegistrar
+ _OBJC_IVAR_$_PHPhotoLibrary._cloudStatusHandlerQueue
+ _OBJC_IVAR_$_PHPhotoLibrary._cloudStatusObserverRegistrar
+ _OBJC_IVAR_$_PHPhotoLibrary._cplStatusDelegateQueue
+ _OBJC_IVAR_$_PHPhotoLibrary._lazyAnalysisCoalescer
+ _OBJC_IVAR_$_PHPhotoLibrary._waitForDelayedSaveActions
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._changeHandlingDebugger
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._lock
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._lock_clearsOIDCacheAfterFetchResultDealloc
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._lock_externalChangeObservers
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._lock_fetchResults
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._lock_internalChangeObservers
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._lock_isChangeHandlingActive
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._lock_isChangeHandlingAuthorized
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._lock_postsPersistentHistoryChangedNotifications
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._pendingLock
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._pendingLock_isChangeProcessingPending
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._pendingLock_lastChangeProcessingStarted
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._photoLibraryBundle
+ _OBJC_IVAR_$_PHPhotoLibraryChangeObserverRegistrar._uniqueObjectIDCache
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatus._cloudSyncEnabled
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatus._firstSyncCompletionDate
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatus._lastSyncProgressDate
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverRegistrar._beginObservingCloudStatusBlock
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverRegistrar._lock
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverRegistrar._lock_cloudStatusObservers
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverRegistrar._lock_isCloudStatusHandlingActive
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverRegistrar._lock_isCloudStatusHandlingAuthorized
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverRegistrar._photoLibraryBundle
+ _OBJC_METACLASS_$_PHAnalysisCoalescer
+ _OBJC_METACLASS_$_PHPhotoLibraryChangeObserverRegistrar
+ _OBJC_METACLASS_$_PHPhotoLibraryCloudStatusObserverRegistrar
+ _PFIsPhotosAppAnyPlatform
+ _PFIsPhotosPicker
+ _PFMicrosecondAccurateStringFromDate
+ _PHAssetCanPerformAdditionalProcessingOnAsset.onceToken.345
+ _PHErrorIsServerUnavailableError
+ _PHValidationFailureTypeErrorKey
+ _PHValidationFailureTypeIsForLivePhotoPairingIdentifier
+ _PHValidatorError
+ _SensitiveContentAnalysisLibraryCore.frameworkLibrary.19184
+ _SensitiveContentAnalysisLibraryCore.frameworkLibrary.22367
+ _SensitiveContentAnalysisLibraryCore.frameworkLibrary.36453
+ __OBJC_$_CLASS_METHODS_PHAnalysisCoalescer
+ __OBJC_$_CLASS_METHODS_PHPhotoLibraryChangeObserverRegistrar
+ __OBJC_$_INSTANCE_METHODS_PHAnalysisCoalescer
+ __OBJC_$_INSTANCE_METHODS_PHPhotoLibraryChangeObserverRegistrar
+ __OBJC_$_INSTANCE_METHODS_PHPhotoLibraryCloudStatusObserverRegistrar
+ __OBJC_$_INSTANCE_VARIABLES_PHAnalysisCoalescer
+ __OBJC_$_INSTANCE_VARIABLES_PHPhotoLibraryChangeObserverRegistrar
+ __OBJC_$_INSTANCE_VARIABLES_PHPhotoLibraryCloudStatusObserverRegistrar
+ __OBJC_$_PROP_LIST_PHAssetResourceRequest.276
+ __OBJC_$_PROP_LIST_PHPhotoLibraryChangeObserverRegistrar
+ __OBJC_$_PROP_LIST_PHPhotoLibraryCloudStatusObserverRegistrar
+ __OBJC_$_PROP_LIST_PHRetryableRequest
+ __OBJC_$_PROP_LIST_PHShare.146
+ __OBJC_CLASS_RO_$_PHAnalysisCoalescer
+ __OBJC_CLASS_RO_$_PHPhotoLibraryChangeObserverRegistrar
+ __OBJC_CLASS_RO_$_PHPhotoLibraryCloudStatusObserverRegistrar
+ __OBJC_METACLASS_RO_$_PHAnalysisCoalescer
+ __OBJC_METACLASS_RO_$_PHPhotoLibraryChangeObserverRegistrar
+ __OBJC_METACLASS_RO_$_PHPhotoLibraryCloudStatusObserverRegistrar
+ __PFThrowMethodNotImplemented
+ __UTTypeMXIFile
+ ___103-[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:reply:]_block_invoke.485
+ ___137-[PHAssetExportRequest handleResultWithFileURLs:cancelled:withError:forAsset:withOptions:progress:processingUnitCount:completionHandler:]_block_invoke.428
+ ___137-[PHAssetExportRequest handleResultWithFileURLs:cancelled:withError:forAsset:withOptions:progress:processingUnitCount:completionHandler:]_block_invoke.430
+ ___145-[PHShareAssetChangeRequestHelper addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:outKeyAssetIdentifier:outContainsEPPAssets:]_block_invoke.223
+ ___36-[PHPhotoLibrary _resetCachedValues]_block_invoke_2
+ ___36-[PHPhotoLibrary _resetCachedValues]_block_invoke_3
+ ___38-[PHAssetResourceRequest startRequest]_block_invoke.41
+ ___38-[PHAssetResourceRequest startRequest]_block_invoke_2.42
+ ___44-[PHPhotoLibrary _publishCloudStatusUpdate:]_block_invoke
+ ___45-[PHPhotoLibrary _processCPLStatusDidChange:]_block_invoke
+ ___46-[PHPhotoLibrary registerCloudStatusObserver:]_block_invoke
+ ___47+[PHAssetCollection propertiesToFetchWithHint:]_block_invoke.88
+ ___48-[PHAnalysisCoalescer _snapshotOfBufferedAssets]_block_invoke
+ ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_6.441
+ ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_7.446
+ ___55-[PHPhotoLibrary _processPendingChangesWithDebugEvent:]_block_invoke.690
+ ___56+[PHAnalysisCoalescer _analyzeBufferedAssets:inLibrary:]_block_invoke
+ ___56+[PHAnalysisCoalescer _analyzeBufferedAssets:inLibrary:]_block_invoke_2
+ ___56+[PHAnalysisCoalescer _analyzeBufferedAssets:inLibrary:]_block_invoke_3
+ ___56-[PHPhotoLibraryChangeObserverRegistrar removeObserver:]_block_invoke
+ ___57+[PHShareParticipant fetchContributorForComment:options:]_block_invoke
+ ___58-[PHPhotoLibraryCloudStatusObserverRegistrar hasObservers]_block_invoke
+ ___59-[PHAnalysisCoalescer coalesceAndAnalyzeAssets:forFeature:]_block_invoke
+ ___59-[PHSearchQuery _executeSpotlightSearchWithResultsHandler:]_block_invoke.172
+ ___59-[PHSearchQuery _executeSpotlightSearchWithResultsHandler:]_block_invoke.174
+ ___60-[PHPhotoLibraryChangeObserverRegistrar _lock_clearOIDCache]_block_invoke
+ ___61-[PHPhotoLibraryChangeObserverRegistrar registerFetchResult:]_block_invoke
+ ___61-[PHPhotoLibraryCloudStatusObserverRegistrar removeObserver:]_block_invoke
+ ___61-[PHSearchQuery _executeSpotlightSearchWithResultsHandlerV2:]_block_invoke.177
+ ___63-[PHPhotoLibraryChangeObserverRegistrar getObserversWithBlock:]_block_invoke
+ ___63-[PHPhotoLibraryChangeObserverRegistrar unregisterFetchResult:]_block_invoke
+ ___68-[PHFetchResult _handleInitWithInvalidConfigurationDetails:library:]_block_invoke
+ ___68-[PHPhotoLibraryCloudStatusObserverRegistrar getObserversWithBlock:]_block_invoke
+ ___70-[PHPhotoLibraryChangeObserverRegistrar countOfRegisteredFetchResults]_block_invoke
+ ___71-[PHPhotoLibraryChangeObserverRegistrar clearIsChangeProcessingPending]_block_invoke
+ ___74-[PHAssetResourceManager retryAssetResourceRequest:afterFailureWithError:]_block_invoke.143
+ ___74-[PHPhotoLibraryChangeObserverRegistrar addObservers:authorizationStatus:]_block_invoke
+ ___78-[PHPhotoLibraryChangeObserverRegistrar clearsOIDCacheAfterFetchResultDealloc]_block_invoke
+ ___79-[PHPhotoLibraryCloudStatusObserverRegistrar addObservers:authorizationStatus:]_block_invoke
+ ___81-[PHSearchFeedbackDiagnostics _collectPhotosAppOnScreenSearchDetailsWithHandler:]_block_invoke.229
+ ___82-[PHPhotoLibraryChangeObserverRegistrar setClearsOIDCacheAfterFetchResultDealloc:]_block_invoke
+ ___83-[PHPhotoLibraryChangeObserverRegistrar postsPersistentHistoryChangedNotifications]_block_invoke
+ ___84-[PHPhotoLibraryChangeObserverRegistrar throttlePendingChangesWithDebugEvent:block:]_block_invoke
+ ___87-[PHPhotoLibraryChangeObserverRegistrar setPostsPersistentHistoryChangedNotifications:]_block_invoke
+ ___88-[PHAssetExportRequest bundleResourcesIfNeededForAsset:withFileURLs:options:completion:]_block_invoke.451
+ ___91+[PHAssetCollection fetchMomentsNeedingThemeAnalysisWithAdapterVersion:uemVersion:options:]_block_invoke
+ ___91+[PHAssetCollection fetchMomentsNeedingThemeAnalysisWithAdapterVersion:uemVersion:options:]_block_invoke_2
+ ___95-[PHPhotoLibraryChangeObserverRegistrar publishChangesToObserversOnQueue:withDebugEvent:block:]_block_invoke
+ ___95-[PHPhotoLibraryChangeObserverRegistrar publishChangesToObserversOnQueue:withDebugEvent:block:]_block_invoke.33
+ ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke.124
+ ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_2.126
+ ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_3.127
+ ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_4.128
+ ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_9
+ ___Block_byref_object_copy_.10392
+ ___Block_byref_object_copy_.11135
+ ___Block_byref_object_copy_.11396
+ ___Block_byref_object_copy_.11555
+ ___Block_byref_object_copy_.12400
+ ___Block_byref_object_copy_.12653
+ ___Block_byref_object_copy_.13134
+ ___Block_byref_object_copy_.14763
+ ___Block_byref_object_copy_.15509
+ ___Block_byref_object_copy_.17497
+ ___Block_byref_object_copy_.18472
+ ___Block_byref_object_copy_.20133
+ ___Block_byref_object_copy_.20299
+ ___Block_byref_object_copy_.20623
+ ___Block_byref_object_copy_.21091
+ ___Block_byref_object_copy_.21670
+ ___Block_byref_object_copy_.22186
+ ___Block_byref_object_copy_.22374
+ ___Block_byref_object_copy_.24202
+ ___Block_byref_object_copy_.25096
+ ___Block_byref_object_copy_.2533
+ ___Block_byref_object_copy_.26774
+ ___Block_byref_object_copy_.27303
+ ___Block_byref_object_copy_.28024
+ ___Block_byref_object_copy_.28319
+ ___Block_byref_object_copy_.2964
+ ___Block_byref_object_copy_.29842
+ ___Block_byref_object_copy_.30810
+ ___Block_byref_object_copy_.31556
+ ___Block_byref_object_copy_.31850
+ ___Block_byref_object_copy_.33227
+ ___Block_byref_object_copy_.33818
+ ___Block_byref_object_copy_.34374
+ ___Block_byref_object_copy_.34516
+ ___Block_byref_object_copy_.34951
+ ___Block_byref_object_copy_.3522
+ ___Block_byref_object_copy_.35531
+ ___Block_byref_object_copy_.35814
+ ___Block_byref_object_copy_.36786
+ ___Block_byref_object_copy_.37206
+ ___Block_byref_object_copy_.38807
+ ___Block_byref_object_copy_.39364
+ ___Block_byref_object_copy_.4126
+ ___Block_byref_object_copy_.43436
+ ___Block_byref_object_copy_.43856
+ ___Block_byref_object_copy_.44067
+ ___Block_byref_object_copy_.44295
+ ___Block_byref_object_copy_.45639
+ ___Block_byref_object_copy_.46048
+ ___Block_byref_object_copy_.46566
+ ___Block_byref_object_copy_.46868
+ ___Block_byref_object_copy_.47244
+ ___Block_byref_object_copy_.47731
+ ___Block_byref_object_copy_.48226
+ ___Block_byref_object_copy_.49105
+ ___Block_byref_object_copy_.49303
+ ___Block_byref_object_copy_.49513
+ ___Block_byref_object_copy_.49550
+ ___Block_byref_object_copy_.51713
+ ___Block_byref_object_copy_.52002
+ ___Block_byref_object_copy_.52736
+ ___Block_byref_object_copy_.53539
+ ___Block_byref_object_copy_.5622
+ ___Block_byref_object_copy_.6670
+ ___Block_byref_object_copy_.7141
+ ___Block_byref_object_copy_.8874
+ ___Block_byref_object_copy_.9142
+ ___Block_byref_object_copy_.9690
+ ___Block_byref_object_dispose_.10393
+ ___Block_byref_object_dispose_.11136
+ ___Block_byref_object_dispose_.11397
+ ___Block_byref_object_dispose_.11556
+ ___Block_byref_object_dispose_.12401
+ ___Block_byref_object_dispose_.12654
+ ___Block_byref_object_dispose_.13135
+ ___Block_byref_object_dispose_.14764
+ ___Block_byref_object_dispose_.15510
+ ___Block_byref_object_dispose_.17498
+ ___Block_byref_object_dispose_.18473
+ ___Block_byref_object_dispose_.20134
+ ___Block_byref_object_dispose_.20300
+ ___Block_byref_object_dispose_.20624
+ ___Block_byref_object_dispose_.21092
+ ___Block_byref_object_dispose_.21671
+ ___Block_byref_object_dispose_.22187
+ ___Block_byref_object_dispose_.22375
+ ___Block_byref_object_dispose_.24203
+ ___Block_byref_object_dispose_.25097
+ ___Block_byref_object_dispose_.2534
+ ___Block_byref_object_dispose_.26775
+ ___Block_byref_object_dispose_.27304
+ ___Block_byref_object_dispose_.28025
+ ___Block_byref_object_dispose_.28320
+ ___Block_byref_object_dispose_.2965
+ ___Block_byref_object_dispose_.29843
+ ___Block_byref_object_dispose_.30811
+ ___Block_byref_object_dispose_.31557
+ ___Block_byref_object_dispose_.31851
+ ___Block_byref_object_dispose_.33228
+ ___Block_byref_object_dispose_.33819
+ ___Block_byref_object_dispose_.34375
+ ___Block_byref_object_dispose_.34517
+ ___Block_byref_object_dispose_.34952
+ ___Block_byref_object_dispose_.3523
+ ___Block_byref_object_dispose_.35532
+ ___Block_byref_object_dispose_.35815
+ ___Block_byref_object_dispose_.36787
+ ___Block_byref_object_dispose_.37207
+ ___Block_byref_object_dispose_.38808
+ ___Block_byref_object_dispose_.39365
+ ___Block_byref_object_dispose_.4127
+ ___Block_byref_object_dispose_.43437
+ ___Block_byref_object_dispose_.43857
+ ___Block_byref_object_dispose_.44068
+ ___Block_byref_object_dispose_.44296
+ ___Block_byref_object_dispose_.45640
+ ___Block_byref_object_dispose_.46049
+ ___Block_byref_object_dispose_.46567
+ ___Block_byref_object_dispose_.46869
+ ___Block_byref_object_dispose_.47245
+ ___Block_byref_object_dispose_.47732
+ ___Block_byref_object_dispose_.48227
+ ___Block_byref_object_dispose_.49106
+ ___Block_byref_object_dispose_.49304
+ ___Block_byref_object_dispose_.49514
+ ___Block_byref_object_dispose_.49551
+ ___Block_byref_object_dispose_.51714
+ ___Block_byref_object_dispose_.52003
+ ___Block_byref_object_dispose_.52737
+ ___Block_byref_object_dispose_.53540
+ ___Block_byref_object_dispose_.5623
+ ___Block_byref_object_dispose_.6671
+ ___Block_byref_object_dispose_.7142
+ ___Block_byref_object_dispose_.8875
+ ___Block_byref_object_dispose_.9143
+ ___Block_byref_object_dispose_.9691
+ ___PHAssetCanPerformAdditionalProcessingOnAsset_block_invoke.346
+ ___SensitiveContentAnalysisLibraryCore_block_invoke.19185
+ ___SensitiveContentAnalysisLibraryCore_block_invoke.22368
+ ___SensitiveContentAnalysisLibraryCore_block_invoke.36454
+ ____fetchNonHintResources_block_invoke.225
+ ___block_descriptor_40_e18_v16?0"PLResult"8l
+ ___block_descriptor_40_e8_32s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e30_v24?0"NSError"8"NSString"16lr32l8r40l8
+ ___block_descriptor_56_e8_32s40s_e18_v16?0"PLResult"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s_e39_"PHFetchResult"16?0"PHFetchOptions"8ls32l8
+ ___block_descriptor_64_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0lr56l8s32l8s40l8r64l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r_e36_v40?0q8Q16"NSString"24"NSError"32ls32l8r48l8r56l8s40l8
+ ___block_descriptor_91_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.1000
+ ___block_literal_global.1002
+ ___block_literal_global.1004
+ ___block_literal_global.1006
+ ___block_literal_global.1008
+ ___block_literal_global.1010
+ ___block_literal_global.1012
+ ___block_literal_global.1014
+ ___block_literal_global.1016
+ ___block_literal_global.1018
+ ___block_literal_global.1020
+ ___block_literal_global.1022
+ ___block_literal_global.1024
+ ___block_literal_global.1026
+ ___block_literal_global.1028
+ ___block_literal_global.1030
+ ___block_literal_global.1032
+ ___block_literal_global.1034.36644
+ ___block_literal_global.1036
+ ___block_literal_global.1038
+ ___block_literal_global.1040
+ ___block_literal_global.1042
+ ___block_literal_global.1044
+ ___block_literal_global.1046
+ ___block_literal_global.1048
+ ___block_literal_global.1050
+ ___block_literal_global.10516
+ ___block_literal_global.1052
+ ___block_literal_global.1054
+ ___block_literal_global.1056.36642
+ ___block_literal_global.1058.36640
+ ___block_literal_global.1060
+ ___block_literal_global.1062
+ ___block_literal_global.1064
+ ___block_literal_global.1066
+ ___block_literal_global.1068
+ ___block_literal_global.1070
+ ___block_literal_global.1072
+ ___block_literal_global.1074
+ ___block_literal_global.1076
+ ___block_literal_global.1078
+ ___block_literal_global.1080
+ ___block_literal_global.1082.36639
+ ___block_literal_global.1084
+ ___block_literal_global.1086
+ ___block_literal_global.1088
+ ___block_literal_global.1090
+ ___block_literal_global.1092.36636
+ ___block_literal_global.1094
+ ___block_literal_global.1096
+ ___block_literal_global.1098
+ ___block_literal_global.1100
+ ___block_literal_global.1102
+ ___block_literal_global.1104
+ ___block_literal_global.1106
+ ___block_literal_global.1108
+ ___block_literal_global.1110
+ ___block_literal_global.1112
+ ___block_literal_global.1114
+ ___block_literal_global.1116
+ ___block_literal_global.1118
+ ___block_literal_global.112.41132
+ ___block_literal_global.1120
+ ___block_literal_global.11217
+ ___block_literal_global.1122
+ ___block_literal_global.1124
+ ___block_literal_global.1126
+ ___block_literal_global.1128
+ ___block_literal_global.1130
+ ___block_literal_global.1132
+ ___block_literal_global.1134
+ ___block_literal_global.1136
+ ___block_literal_global.1138
+ ___block_literal_global.1140
+ ___block_literal_global.11412
+ ___block_literal_global.1142
+ ___block_literal_global.1144
+ ___block_literal_global.1146
+ ___block_literal_global.1148
+ ___block_literal_global.1150
+ ___block_literal_global.1152
+ ___block_literal_global.1154
+ ___block_literal_global.1156
+ ___block_literal_global.1158
+ ___block_literal_global.1160
+ ___block_literal_global.1162
+ ___block_literal_global.1164
+ ___block_literal_global.1166
+ ___block_literal_global.1171
+ ___block_literal_global.1173
+ ___block_literal_global.1175
+ ___block_literal_global.1177
+ ___block_literal_global.11789
+ ___block_literal_global.1179
+ ___block_literal_global.1181
+ ___block_literal_global.1183
+ ___block_literal_global.1185
+ ___block_literal_global.1187
+ ___block_literal_global.1189
+ ___block_literal_global.1191
+ ___block_literal_global.1193
+ ___block_literal_global.1195
+ ___block_literal_global.1197
+ ___block_literal_global.1199
+ ___block_literal_global.1201
+ ___block_literal_global.1203
+ ___block_literal_global.1205
+ ___block_literal_global.1207
+ ___block_literal_global.1209
+ ___block_literal_global.1211
+ ___block_literal_global.1213
+ ___block_literal_global.1215
+ ___block_literal_global.1217
+ ___block_literal_global.12700
+ ___block_literal_global.13363
+ ___block_literal_global.134.47791
+ ___block_literal_global.1351
+ ___block_literal_global.1360
+ ___block_literal_global.1375
+ ___block_literal_global.1385
+ ___block_literal_global.1404
+ ___block_literal_global.14443
+ ___block_literal_global.146.38775
+ ___block_literal_global.14831
+ ___block_literal_global.155
+ ___block_literal_global.15504
+ ___block_literal_global.168
+ ___block_literal_global.169.52823
+ ___block_literal_global.17076
+ ___block_literal_global.1724
+ ___block_literal_global.176
+ ___block_literal_global.17732
+ ___block_literal_global.18501
+ ___block_literal_global.18552
+ ___block_literal_global.19758
+ ___block_literal_global.20049
+ ___block_literal_global.206.28599
+ ___block_literal_global.20640
+ ___block_literal_global.21066
+ ___block_literal_global.213
+ ___block_literal_global.215.29514
+ ___block_literal_global.217.13916
+ ___block_literal_global.217.29498
+ ___block_literal_global.21979
+ ___block_literal_global.224.14719
+ ___block_literal_global.22841
+ ___block_literal_global.234.34108
+ ___block_literal_global.24110
+ ___block_literal_global.25458
+ ___block_literal_global.2560
+ ___block_literal_global.26131
+ ___block_literal_global.27003
+ ___block_literal_global.27726
+ ___block_literal_global.2794
+ ___block_literal_global.28001
+ ___block_literal_global.28630
+ ___block_literal_global.28900
+ ___block_literal_global.28979
+ ___block_literal_global.29501
+ ___block_literal_global.2961
+ ___block_literal_global.29958
+ ___block_literal_global.3.11417
+ ___block_literal_global.3.2960
+ ___block_literal_global.30339
+ ___block_literal_global.30536
+ ___block_literal_global.30821
+ ___block_literal_global.31239
+ ___block_literal_global.3131
+ ___block_literal_global.32083
+ ___block_literal_global.32225
+ ___block_literal_global.32697
+ ___block_literal_global.33333
+ ___block_literal_global.34111
+ ___block_literal_global.34388
+ ___block_literal_global.34467
+ ___block_literal_global.34613
+ ___block_literal_global.34792
+ ___block_literal_global.348
+ ___block_literal_global.35269
+ ___block_literal_global.35819
+ ___block_literal_global.359
+ ___block_literal_global.3606
+ ___block_literal_global.36321
+ ___block_literal_global.37.32129
+ ___block_literal_global.37.47363
+ ___block_literal_global.37076
+ ___block_literal_global.37267
+ ___block_literal_global.373
+ ___block_literal_global.3760
+ ___block_literal_global.37813
+ ___block_literal_global.38120
+ ___block_literal_global.38850
+ ___block_literal_global.39108
+ ___block_literal_global.39537
+ ___block_literal_global.40135
+ ___block_literal_global.40346
+ ___block_literal_global.40830
+ ___block_literal_global.41138
+ ___block_literal_global.417
+ ___block_literal_global.42445
+ ___block_literal_global.425
+ ___block_literal_global.43025
+ ___block_literal_global.43439
+ ___block_literal_global.4386
+ ___block_literal_global.44121
+ ___block_literal_global.4426
+ ___block_literal_global.44312
+ ___block_literal_global.44932
+ ___block_literal_global.45724
+ ___block_literal_global.458
+ ___block_literal_global.46080
+ ___block_literal_global.462
+ ___block_literal_global.46398
+ ___block_literal_global.46489
+ ___block_literal_global.466
+ ___block_literal_global.47152
+ ___block_literal_global.47370
+ ___block_literal_global.47810
+ ___block_literal_global.47958
+ ___block_literal_global.4799
+ ___block_literal_global.48718
+ ___block_literal_global.4891
+ ___block_literal_global.49070
+ ___block_literal_global.493
+ ___block_literal_global.49515
+ ___block_literal_global.49563
+ ___block_literal_global.4965
+ ___block_literal_global.49872
+ ___block_literal_global.50.26099
+ ___block_literal_global.50145
+ ___block_literal_global.51456
+ ___block_literal_global.52826
+ ___block_literal_global.53393
+ ___block_literal_global.545
+ ___block_literal_global.557
+ ___block_literal_global.5654
+ ___block_literal_global.586
+ ___block_literal_global.666
+ ___block_literal_global.675
+ ___block_literal_global.6755
+ ___block_literal_global.678
+ ___block_literal_global.680
+ ___block_literal_global.7148
+ ___block_literal_global.7796
+ ___block_literal_global.8024
+ ___block_literal_global.8195
+ ___block_literal_global.85.53371
+ ___block_literal_global.8866
+ ___block_literal_global.8945
+ ___block_literal_global.9359
+ ___block_literal_global.94
+ ___block_literal_global.980.36813
+ ___block_literal_global.982.36807
+ ___block_literal_global.984
+ ___block_literal_global.986
+ ___block_literal_global.988
+ ___block_literal_global.990
+ ___block_literal_global.992.36933
+ ___block_literal_global.994
+ ___block_literal_global.996
+ ___block_literal_global.998
+ ___getSCSensitivityAnalysisClass_block_invoke.19183
+ ___getSCSensitivityAnalysisClass_block_invoke.22366
+ ___getSCSensitivityAnalysisClass_block_invoke.36452
+ __currentTimestampString.s_formatter.47364
+ __currentTimestampString.s_onceToken.47362
+ _allowedEntities.pl_once_object_83
+ _allowedEntities.pl_once_object_84
+ _allowedEntities.pl_once_token_83
+ _allowedEntities.pl_once_token_84
+ _allowedInfoKeys.allowedKeys.18756
+ _allowedInfoKeys.allowedKeys.40635
+ _allowedInfoKeys.onceToken.18755
+ _allowedInfoKeys.onceToken.40634
+ _audit_stringSensitiveContentAnalysis.19194
+ _audit_stringSensitiveContentAnalysis.22372
+ _audit_stringSensitiveContentAnalysis.36464
+ _corePropertiesToFetch.array.22844
+ _corePropertiesToFetch.array.28627
+ _corePropertiesToFetch.array.34112
+ _corePropertiesToFetch.onceToken.22843
+ _corePropertiesToFetch.onceToken.28626
+ _corePropertiesToFetch.onceToken.34110
+ _defaultManager.onceToken.51789
+ _dispatch_block_cancel
+ _entityKeyMap.pl_once_object_15.11198
+ _entityKeyMap.pl_once_object_15.11800
+ _entityKeyMap.pl_once_object_15.13354
+ _entityKeyMap.pl_once_object_15.13658
+ _entityKeyMap.pl_once_object_15.27717
+ _entityKeyMap.pl_once_object_15.28990
+ _entityKeyMap.pl_once_object_15.32688
+ _entityKeyMap.pl_once_object_15.36311
+ _entityKeyMap.pl_once_object_15.40167
+ _entityKeyMap.pl_once_object_15.44335
+ _entityKeyMap.pl_once_object_15.46071
+ _entityKeyMap.pl_once_object_15.46481
+ _entityKeyMap.pl_once_object_15.4791
+ _entityKeyMap.pl_once_object_15.47955
+ _entityKeyMap.pl_once_object_15.50020
+ _entityKeyMap.pl_once_object_15.50939
+ _entityKeyMap.pl_once_object_15.8030
+ _entityKeyMap.pl_once_object_16.34100
+ _entityKeyMap.pl_once_object_16.34454
+ _entityKeyMap.pl_once_object_16.40333
+ _entityKeyMap.pl_once_object_16.4373
+ _entityKeyMap.pl_once_object_16.47140
+ _entityKeyMap.pl_once_object_16.53380
+ _entityKeyMap.pl_once_token_15.11197
+ _entityKeyMap.pl_once_token_15.11799
+ _entityKeyMap.pl_once_token_15.13353
+ _entityKeyMap.pl_once_token_15.13657
+ _entityKeyMap.pl_once_token_15.27716
+ _entityKeyMap.pl_once_token_15.28989
+ _entityKeyMap.pl_once_token_15.32687
+ _entityKeyMap.pl_once_token_15.36310
+ _entityKeyMap.pl_once_token_15.40166
+ _entityKeyMap.pl_once_token_15.44334
+ _entityKeyMap.pl_once_token_15.46070
+ _entityKeyMap.pl_once_token_15.46480
+ _entityKeyMap.pl_once_token_15.4790
+ _entityKeyMap.pl_once_token_15.47954
+ _entityKeyMap.pl_once_token_15.50019
+ _entityKeyMap.pl_once_token_15.50938
+ _entityKeyMap.pl_once_token_15.8029
+ _entityKeyMap.pl_once_token_16.34099
+ _entityKeyMap.pl_once_token_16.34453
+ _entityKeyMap.pl_once_token_16.40332
+ _entityKeyMap.pl_once_token_16.4372
+ _entityKeyMap.pl_once_token_16.47139
+ _entityKeyMap.pl_once_token_16.53379
+ _getSCSensitivityAnalysisClass.19181
+ _getSCSensitivityAnalysisClass.22364
+ _getSCSensitivityAnalysisClass.36445
+ _getSCSensitivityAnalysisClass.softClass.19182
+ _getSCSensitivityAnalysisClass.softClass.22365
+ _getSCSensitivityAnalysisClass.softClass.36451
+ _handleNilPhotoLibraryError
+ _identifierPropertiesToFetch.array.35270
+ _identifierPropertiesToFetch.onceToken.35268
+ _objc_msgSend$_addChangeObservers:authorizationStatus:
+ _objc_msgSend$_addCloudStatusObservers:authorizationStatus:
+ _objc_msgSend$_analyzeBufferedAssets:inLibrary:
+ _objc_msgSend$_handleInitWithInvalidConfigurationDetails:library:
+ _objc_msgSend$_lock_hasCloudStatusObservers
+ _objc_msgSend$_lock_pauseCloudStatusHandlingIfNeeded
+ _objc_msgSend$_lock_resumeCloudStatusHandlingIfNeeded
+ _objc_msgSend$_logFailureIfNeededForResult:andFeature:
+ _objc_msgSend$_processCPLStatusDidChange:
+ _objc_msgSend$_publishCloudStatusUpdate:
+ _objc_msgSend$_removeChangeObserver:
+ _objc_msgSend$_removeCloudStatusObserver:
+ _objc_msgSend$_setCachedCloudStatus:
+ _objc_msgSend$_setupLazyCPLStatusIfNecessary
+ _objc_msgSend$_snapshotOfBufferedAssets
+ _objc_msgSend$_triggerQueryTimeoutTapToRadarForQuery:
+ _objc_msgSend$adapterVersion
+ _objc_msgSend$analysisCoalescer
+ _objc_msgSend$assert:code:failureType:format:
+ _objc_msgSend$assetsWithAvalancheUUID:sourceType:inManagedObjectContext:
+ _objc_msgSend$assignEmptyThemesWithAdapterVersion:uemVersion:
+ _objc_msgSend$assignThemeNamed:adapterVersion:uemVersion:withConfidence:
+ _objc_msgSend$beginObservingCloudStatusBlock
+ _objc_msgSend$coalesceAndAnalyzeAssets:forFeature:
+ _objc_msgSend$fetchMomentIDsNotAnalyzedForThemesInContext:adapterVersion:uemVersion:
+ _objc_msgSend$fileRadarUserNotificationWithHeader:message:radarTitle:radarDescription:radarComponent:diagnosticTTRType:attachments:extensionItem:
+ _objc_msgSend$firstSyncCompletionDate
+ _objc_msgSend$getNilPhotoLibraryReasonAndName:
+ _objc_msgSend$hasMasterThumb
+ _objc_msgSend$hasObservers
+ _objc_msgSend$initForNewObjectWithRequestData:
+ _objc_msgSend$initWithCPLStatus:isEnabled:
+ _objc_msgSend$initWithQuery:library:
+ _objc_msgSend$initWithQuery:library:oids:registerIfNeeded:usingManagedObjectContext:
+ _objc_msgSend$initWithQuery:library:registerIfNeeded:
+ _objc_msgSend$initWithSceneTaxonomyProvider:csuTaxonomyObjectStore:locale:calendar:indexDateFormatter:countrySynonymProvider:delegate:
+ _objc_msgSend$initWithThemeName:confidence:adapterVersion:uemVersion:
+ _objc_msgSend$initWithUUID:objectID:requestData:
+ _objc_msgSend$initWithUUID:sourceType:photoLibrary:
+ _objc_msgSend$isFinderSyncedAsset
+ _objc_msgSend$isHDRScreenshotAsset:withCurrentType:
+ _objc_msgSend$lastSyncProgressDate
+ _objc_msgSend$photoLibraryDidUpdateCloudStatus:
+ _objc_msgSend$queryForContributorForComment:options:
+ _objc_msgSend$requestData
+ _objc_msgSend$resetStateForMediaProcessingTaskID:assetIdentifiers:resetOptions:error:
+ _objc_msgSend$retryInterval
+ _objc_msgSend$sensitivityAnalysisFromAsset:outError:
+ _objc_msgSend$setBeginObservingCloudStatusBlock:
+ _objc_msgSend$setDelegateQueue:
+ _objc_msgSend$setNilPhotoLibraryReason:name:
+ _objc_msgSend$setPostDelayedSaveActionsReply:
+ _objc_msgSend$setRetryInterval:
+ _objc_msgSend$setThemeAssignmentsToAdapterVersion:uemVersion:
+ _objc_msgSend$setWaitForDelayedSaveActions:
+ _objc_msgSend$sharedPersistentStoreCoordinatorWithError:
+ _objc_msgSend$uemVersion
+ _objc_msgSend$waitForDelayedSaveActions
+ _propertiesToFetch.pl_once_object_24.33814
+ _propertiesToFetch.pl_once_token_24.33813
+ _propertiesToFetchWithHint:.array.11213
+ _propertiesToFetchWithHint:.array.11807
+ _propertiesToFetchWithHint:.array.13682
+ _propertiesToFetchWithHint:.array.23338
+ _propertiesToFetchWithHint:.array.27727
+ _propertiesToFetchWithHint:.array.29000
+ _propertiesToFetchWithHint:.array.32698
+ _propertiesToFetchWithHint:.array.36322
+ _propertiesToFetchWithHint:.array.40188
+ _propertiesToFetchWithHint:.array.46081
+ _propertiesToFetchWithHint:.array.47959
+ _propertiesToFetchWithHint:.array.50033
+ _propertiesToFetchWithHint:.array.50967
+ _propertiesToFetchWithHint:.array.8058
+ _propertiesToFetchWithHint:.onceToken.11212
+ _propertiesToFetchWithHint:.onceToken.11806
+ _propertiesToFetchWithHint:.onceToken.13362
+ _propertiesToFetchWithHint:.onceToken.13681
+ _propertiesToFetchWithHint:.onceToken.22837
+ _propertiesToFetchWithHint:.onceToken.23337
+ _propertiesToFetchWithHint:.onceToken.27725
+ _propertiesToFetchWithHint:.onceToken.28629
+ _propertiesToFetchWithHint:.onceToken.28999
+ _propertiesToFetchWithHint:.onceToken.32696
+ _propertiesToFetchWithHint:.onceToken.34104
+ _propertiesToFetchWithHint:.onceToken.36320
+ _propertiesToFetchWithHint:.onceToken.40187
+ _propertiesToFetchWithHint:.onceToken.4384
+ _propertiesToFetchWithHint:.onceToken.46079
+ _propertiesToFetchWithHint:.onceToken.47957
+ _propertiesToFetchWithHint:.onceToken.50032
+ _propertiesToFetchWithHint:.onceToken.50966
+ _propertiesToFetchWithHint:.onceToken.8057
+ _propertiesToFetchWithHint:.pl_once_object_15.34468
+ _propertiesToFetchWithHint:.pl_once_object_15.40347
+ _propertiesToFetchWithHint:.pl_once_object_15.47153
+ _propertiesToFetchWithHint:.pl_once_object_15.53394
+ _propertiesToFetchWithHint:.pl_once_token_15.34466
+ _propertiesToFetchWithHint:.pl_once_token_15.40345
+ _propertiesToFetchWithHint:.pl_once_token_15.47151
+ _propertiesToFetchWithHint:.pl_once_token_15.53392
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.13365
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.22839
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.28632
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.34106
+ _propertiesToFetchWithHint:.propertyQueue.13364
+ _propertiesToFetchWithHint:.propertyQueue.22838
+ _propertiesToFetchWithHint:.propertyQueue.28631
+ _propertiesToFetchWithHint:.propertyQueue.34105
+ _propertiesToPrefetch.onceToken.22380
+ _propertiesToPrefetch.onceToken.28297
+ _propertiesToPrefetch.onceToken.33795
+ _propertiesToPrefetch.propertiesToPrefetch.22381
+ _propertiesToPrefetch.propertiesToPrefetch.28298
+ _propertiesToPrefetch.propertiesToPrefetch.33796
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.13120
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.28483
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.34074
+ _propertySetAccessorsByPropertySet.onceToken.13119
+ _propertySetAccessorsByPropertySet.onceToken.28482
+ _propertySetAccessorsByPropertySet.onceToken.34073
+ _propertySetClassForPropertySet:.onceToken.13122
+ _propertySetClassForPropertySet:.onceToken.28490
+ _propertySetClassForPropertySet:.onceToken.34082
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.13123
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.28491
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.34083
+ _sharedDecoder.s_onceToken.50144
+ _sharedDecoder.s_shared.50146
+ _sharedLazyPhotoLibraryForCMM.pl_once_object_49
+ _sharedLazyPhotoLibraryForCMM.pl_once_token_49
+ _transformValueExpression:forKeyPath:._passThroughSet.11181
+ _transformValueExpression:forKeyPath:._passThroughSet.11796
+ _transformValueExpression:forKeyPath:._passThroughSet.13343
+ _transformValueExpression:forKeyPath:._passThroughSet.13643
+ _transformValueExpression:forKeyPath:._passThroughSet.22792
+ _transformValueExpression:forKeyPath:._passThroughSet.27696
+ _transformValueExpression:forKeyPath:._passThroughSet.28615
+ _transformValueExpression:forKeyPath:._passThroughSet.28986
+ _transformValueExpression:forKeyPath:._passThroughSet.32679
+ _transformValueExpression:forKeyPath:._passThroughSet.34088
+ _transformValueExpression:forKeyPath:._passThroughSet.36305
+ _transformValueExpression:forKeyPath:._passThroughSet.40156
+ _transformValueExpression:forKeyPath:._passThroughSet.4362
+ _transformValueExpression:forKeyPath:._passThroughSet.44317
+ _transformValueExpression:forKeyPath:._passThroughSet.46059
+ _transformValueExpression:forKeyPath:._passThroughSet.47952
+ _transformValueExpression:forKeyPath:._passThroughSet.50917
+ _transformValueExpression:forKeyPath:._passThroughSet.53342
+ _transformValueExpression:forKeyPath:.onceToken.11180
+ _transformValueExpression:forKeyPath:.onceToken.11795
+ _transformValueExpression:forKeyPath:.onceToken.13342
+ _transformValueExpression:forKeyPath:.onceToken.13642
+ _transformValueExpression:forKeyPath:.onceToken.22791
+ _transformValueExpression:forKeyPath:.onceToken.27695
+ _transformValueExpression:forKeyPath:.onceToken.28614
+ _transformValueExpression:forKeyPath:.onceToken.28985
+ _transformValueExpression:forKeyPath:.onceToken.32678
+ _transformValueExpression:forKeyPath:.onceToken.34087
+ _transformValueExpression:forKeyPath:.onceToken.36304
+ _transformValueExpression:forKeyPath:.onceToken.40155
+ _transformValueExpression:forKeyPath:.onceToken.4361
+ _transformValueExpression:forKeyPath:.onceToken.44316
+ _transformValueExpression:forKeyPath:.onceToken.46058
+ _transformValueExpression:forKeyPath:.onceToken.47951
+ _transformValueExpression:forKeyPath:.onceToken.50916
+ _transformValueExpression:forKeyPath:.onceToken.53341
+ _uniqueObjectIDCache.pl_once_object_82
+ _uniqueObjectIDCache.pl_once_token_82
- +[PHAssetCollection fetchMomentsNeedingThemeAnalysisWithAlgorithmVersion:options:]
- +[PHAssetCollection fetchMomentsNeedingThemeAnalysisWithOptions:]
- +[PHInternalAssetExportRequest isHDRScreenshotWithAlphaChannelAsset:withCurrentType:]
- +[PHPhotoLibraryObserverRegistrar _isInternalObserver:]
- +[PHSensitiveContentAnalysisUtility _sensitivityAnalysisFromAsset:outError:]
- -[PHAssetComment _plObject]
- -[PHAssetComment commenterDisplayName]
- -[PHAssetComment commenterEmail]
- -[PHAssetComment commenterFirstName]
- -[PHAssetComment commenterFullName]
- -[PHAssetComment commenterLastName]
- -[PHAssetComment shouldNotifyAsNotificationWithMediaStreamInfo:asCaptionOnly:]
- -[PHAssetResourceUploadJobChangeRequest initForNewObject]
- -[PHAssetResourceUploadJobChangeRequest initWithUUID:objectID:]
- -[PHChange cloudStatus]
- -[PHChange hasCloudStatusChanges]
- -[PHChange initWithCloudStatus:library:]
- -[PHCollectionShare uploadedPhotosCount]
- -[PHCollectionShare uploadedVideosCount]
- -[PHFetchResult initWithMediaTypeCounts:]
- -[PHFetchResult initWithQuery:]
- -[PHFetchResult initWithQuery:oids:registerIfNeeded:usingManagedObjectContext:]
- -[PHFetchResult initWithQuery:registerIfNeeded:]
- -[PHMomentChangeRequest addAssetSearchEntityWithLabel:identifier:type:confidence:dateInterval:synonyms:]
- -[PHMomentChangeRequest algorithmVersionForEmptyThemeAssignment]
- -[PHMomentChangeRequest algorithmVersionForVersionOverwrite]
- -[PHMomentChangeRequest assignEmptyThemeWithAlgorithmVersion:]
- -[PHMomentChangeRequest assignEmptyTheme]
- -[PHMomentChangeRequest assignThemeNamed:algorithmVersion:withConfidence:]
- -[PHMomentChangeRequest assignThemeNamed:withConfidence:]
- -[PHMomentChangeRequest setAlgorithmVersionForEmptyThemeAssignment:]
- -[PHMomentChangeRequest setAlgorithmVersionForVersionOverwrite:]
- -[PHMomentChangeRequest setShouldOverwriteExistingThemeAlgorithmVersion:]
- -[PHMomentChangeRequest setThemeAssignmentsToAlgorithmVersion:]
- -[PHMomentChangeRequest shouldOverwriteExistingThemeAlgorithmVersion]
- -[PHMomentShare uploadedPhotosCount]
- -[PHMomentShare uploadedVideosCount]
- -[PHMomentThemeAssignment algorithmVersion]
- -[PHMomentThemeAssignment initWithThemeName:confidence:algorithmVersion:]
- -[PHPhotoLibrary _addObservers:authorizationStatus:]
- -[PHPhotoLibrary _publishCloudStatusChangeWithDebugEvent:]
- -[PHPhotoLibrary _removeObserver:]
- -[PHPhotoLibraryCloudStatus firstSyncDate]
- -[PHPhotoLibraryCloudStatus initWithCPLStatus:]
- -[PHPhotoLibraryCloudStatus lastSyncDate]
- -[PHPhotoLibraryObserverRegistrar .cxx_destruct]
- -[PHPhotoLibraryObserverRegistrar _lock_clearOIDCache]
- -[PHPhotoLibraryObserverRegistrar _lock_hasChangeObservers]
- -[PHPhotoLibraryObserverRegistrar _lock_pauseChangeHandlingIfNeeded]
- -[PHPhotoLibraryObserverRegistrar _lock_resumeChangeHandlingIfNeeded]
- -[PHPhotoLibraryObserverRegistrar addObservers:authorizationStatus:]
- -[PHPhotoLibraryObserverRegistrar clearIsChangeProcessingPending]
- -[PHPhotoLibraryObserverRegistrar clearsOIDCacheAfterFetchResultDealloc]
- -[PHPhotoLibraryObserverRegistrar countOfRegisteredFetchResults]
- -[PHPhotoLibraryObserverRegistrar dealloc]
- -[PHPhotoLibraryObserverRegistrar getObserversWithBlock:]
- -[PHPhotoLibraryObserverRegistrar initWithLibraryBundle:changeHandlingDebugger:uniqueObjectIDCache:]
- -[PHPhotoLibraryObserverRegistrar postsPersistentHistoryChangedNotifications]
- -[PHPhotoLibraryObserverRegistrar publishChangesToObserversOnQueue:withDebugEvent:block:]
- -[PHPhotoLibraryObserverRegistrar registerFetchResult:]
- -[PHPhotoLibraryObserverRegistrar removeObserver:]
- -[PHPhotoLibraryObserverRegistrar setClearsOIDCacheAfterFetchResultDealloc:]
- -[PHPhotoLibraryObserverRegistrar setPostsPersistentHistoryChangedNotifications:]
- -[PHPhotoLibraryObserverRegistrar throttlePendingChangesTimerFiredWithBlock:]
- -[PHPhotoLibraryObserverRegistrar throttlePendingChangesWithDebugEvent:block:]
- -[PHPhotoLibraryObserverRegistrar unregisterFetchResult:]
- -[PHResourceChooserListResourceInfo prepareForReuse]
- -[PHSearchEntityCreationRequest addSearchRankingWithLabel:identifier:type:rankingScore:synonyms:]
- -[PHValidator getLivePhotoImageMetadataFromURL:pairingIdentifier:]
- -[_PHValidation assert:code:format:]
- GCC_except_table10012
- GCC_except_table10017
- GCC_except_table10087
- GCC_except_table10180
- GCC_except_table10319
- GCC_except_table10356
- GCC_except_table10446
- GCC_except_table10474
- GCC_except_table10967
- GCC_except_table11122
- GCC_except_table11125
- GCC_except_table11130
- GCC_except_table11136
- GCC_except_table11140
- GCC_except_table11146
- GCC_except_table11252
- GCC_except_table11271
- GCC_except_table11273
- GCC_except_table11275
- GCC_except_table11277
- GCC_except_table11359
- GCC_except_table11366
- GCC_except_table11368
- GCC_except_table11370
- GCC_except_table11376
- GCC_except_table11412
- GCC_except_table11556
- GCC_except_table11568
- GCC_except_table11609
- GCC_except_table11611
- GCC_except_table11624
- GCC_except_table11723
- GCC_except_table11727
- GCC_except_table11765
- GCC_except_table11769
- GCC_except_table11778
- GCC_except_table11779
- GCC_except_table11786
- GCC_except_table11823
- GCC_except_table11830
- GCC_except_table11874
- GCC_except_table11957
- GCC_except_table11960
- GCC_except_table11966
- GCC_except_table11968
- GCC_except_table12008
- GCC_except_table12027
- GCC_except_table12036
- GCC_except_table12134
- GCC_except_table12278
- GCC_except_table12282
- GCC_except_table12286
- GCC_except_table12323
- GCC_except_table12354
- GCC_except_table12452
- GCC_except_table12456
- GCC_except_table12458
- GCC_except_table12460
- GCC_except_table12575
- GCC_except_table12817
- GCC_except_table12894
- GCC_except_table12939
- GCC_except_table12986
- GCC_except_table12996
- GCC_except_table13014
- GCC_except_table13029
- GCC_except_table13069
- GCC_except_table13071
- GCC_except_table13073
- GCC_except_table13092
- GCC_except_table13174
- GCC_except_table13180
- GCC_except_table13196
- GCC_except_table1388
- GCC_except_table1407
- GCC_except_table1706
- GCC_except_table1709
- GCC_except_table1723
- GCC_except_table1738
- GCC_except_table1924
- GCC_except_table1928
- GCC_except_table1930
- GCC_except_table1932
- GCC_except_table1934
- GCC_except_table1936
- GCC_except_table1938
- GCC_except_table1948
- GCC_except_table1950
- GCC_except_table1952
- GCC_except_table1964
- GCC_except_table1996
- GCC_except_table1998
- GCC_except_table2000
- GCC_except_table2002
- GCC_except_table2004
- GCC_except_table2006
- GCC_except_table2008
- GCC_except_table2010
- GCC_except_table2012
- GCC_except_table2014
- GCC_except_table2016
- GCC_except_table2018
- GCC_except_table2020
- GCC_except_table2022
- GCC_except_table2024
- GCC_except_table2026
- GCC_except_table2031
- GCC_except_table2033
- GCC_except_table2035
- GCC_except_table2037
- GCC_except_table2042
- GCC_except_table2047
- GCC_except_table2049
- GCC_except_table2077
- GCC_except_table2079
- GCC_except_table2191
- GCC_except_table2196
- GCC_except_table2204
- GCC_except_table2214
- GCC_except_table2254
- GCC_except_table2432
- GCC_except_table2447
- GCC_except_table2469
- GCC_except_table2475
- GCC_except_table2508
- GCC_except_table2513
- GCC_except_table2569
- GCC_except_table2665
- GCC_except_table2676
- GCC_except_table2678
- GCC_except_table2712
- GCC_except_table2786
- GCC_except_table2791
- GCC_except_table2796
- GCC_except_table2809
- GCC_except_table2820
- GCC_except_table2822
- GCC_except_table2956
- GCC_except_table2960
- GCC_except_table3030
- GCC_except_table3038
- GCC_except_table3067
- GCC_except_table3071
- GCC_except_table3076
- GCC_except_table3191
- GCC_except_table3224
- GCC_except_table3230
- GCC_except_table3233
- GCC_except_table3243
- GCC_except_table3253
- GCC_except_table3256
- GCC_except_table3275
- GCC_except_table3280
- GCC_except_table3291
- GCC_except_table3292
- GCC_except_table3308
- GCC_except_table3317
- GCC_except_table3414
- GCC_except_table3436
- GCC_except_table3438
- GCC_except_table3487
- GCC_except_table3514
- GCC_except_table3544
- GCC_except_table3546
- GCC_except_table3564
- GCC_except_table3566
- GCC_except_table3779
- GCC_except_table3781
- GCC_except_table3803
- GCC_except_table3838
- GCC_except_table3846
- GCC_except_table3848
- GCC_except_table3863
- GCC_except_table3866
- GCC_except_table3900
- GCC_except_table3906
- GCC_except_table4171
- GCC_except_table4177
- GCC_except_table4204
- GCC_except_table4227
- GCC_except_table4233
- GCC_except_table4238
- GCC_except_table4249
- GCC_except_table4253
- GCC_except_table4266
- GCC_except_table4332
- GCC_except_table4641
- GCC_except_table4650
- GCC_except_table4712
- GCC_except_table4714
- GCC_except_table4720
- GCC_except_table4723
- GCC_except_table4790
- GCC_except_table4795
- GCC_except_table4824
- GCC_except_table4971
- GCC_except_table5326
- GCC_except_table5375
- GCC_except_table5393
- GCC_except_table5418
- GCC_except_table5420
- GCC_except_table5446
- GCC_except_table5448
- GCC_except_table5451
- GCC_except_table5465
- GCC_except_table5469
- GCC_except_table5478
- GCC_except_table5482
- GCC_except_table5519
- GCC_except_table5527
- GCC_except_table5555
- GCC_except_table5581
- GCC_except_table5585
- GCC_except_table5606
- GCC_except_table5612
- GCC_except_table5616
- GCC_except_table5630
- GCC_except_table5633
- GCC_except_table5636
- GCC_except_table5657
- GCC_except_table5696
- GCC_except_table5707
- GCC_except_table5750
- GCC_except_table5779
- GCC_except_table5782
- GCC_except_table5788
- GCC_except_table5792
- GCC_except_table5820
- GCC_except_table5850
- GCC_except_table5876
- GCC_except_table5878
- GCC_except_table5889
- GCC_except_table5936
- GCC_except_table6012
- GCC_except_table6017
- GCC_except_table6022
- GCC_except_table6154
- GCC_except_table6157
- GCC_except_table6170
- GCC_except_table6194
- GCC_except_table6204
- GCC_except_table6207
- GCC_except_table6244
- GCC_except_table6281
- GCC_except_table6283
- GCC_except_table6668
- GCC_except_table6681
- GCC_except_table6694
- GCC_except_table6711
- GCC_except_table6740
- GCC_except_table6743
- GCC_except_table6745
- GCC_except_table6747
- GCC_except_table6749
- GCC_except_table6757
- GCC_except_table6800
- GCC_except_table6813
- GCC_except_table6846
- GCC_except_table6848
- GCC_except_table6887
- GCC_except_table7136
- GCC_except_table7137
- GCC_except_table7147
- GCC_except_table7154
- GCC_except_table7170
- GCC_except_table7172
- GCC_except_table7173
- GCC_except_table7174
- GCC_except_table7175
- GCC_except_table7176
- GCC_except_table7177
- GCC_except_table7188
- GCC_except_table7189
- GCC_except_table7190
- GCC_except_table7347
- GCC_except_table7565
- GCC_except_table7591
- GCC_except_table7610
- GCC_except_table7611
- GCC_except_table7672
- GCC_except_table7694
- GCC_except_table7698
- GCC_except_table7755
- GCC_except_table7913
- GCC_except_table7915
- GCC_except_table7962
- GCC_except_table8002
- GCC_except_table8006
- GCC_except_table8008
- GCC_except_table8010
- GCC_except_table8022
- GCC_except_table8027
- GCC_except_table8067
- GCC_except_table8095
- GCC_except_table8222
- GCC_except_table8280
- GCC_except_table8300
- GCC_except_table8303
- GCC_except_table8322
- GCC_except_table8384
- GCC_except_table8388
- GCC_except_table8392
- GCC_except_table8401
- GCC_except_table8403
- GCC_except_table8443
- GCC_except_table8507
- GCC_except_table8664
- GCC_except_table8703
- GCC_except_table8708
- GCC_except_table8953
- GCC_except_table8957
- GCC_except_table8961
- GCC_except_table8963
- GCC_except_table8988
- GCC_except_table8989
- GCC_except_table9081
- GCC_except_table9091
- GCC_except_table9123
- GCC_except_table9174
- GCC_except_table9208
- GCC_except_table9228
- GCC_except_table9253
- GCC_except_table9276
- GCC_except_table9309
- GCC_except_table9311
- GCC_except_table9401
- GCC_except_table9492
- GCC_except_table9609
- GCC_except_table9623
- GCC_except_table9624
- GCC_except_table9631
- GCC_except_table9634
- GCC_except_table9657
- GCC_except_table9658
- GCC_except_table9659
- GCC_except_table9660
- GCC_except_table9661
- GCC_except_table9664
- GCC_except_table9665
- GCC_except_table9666
- GCC_except_table9667
- GCC_except_table9668
- GCC_except_table9669
- GCC_except_table9672
- GCC_except_table9674
- GCC_except_table9675
- GCC_except_table9676
- GCC_except_table9677
- GCC_except_table9678
- GCC_except_table9679
- GCC_except_table9680
- GCC_except_table9682
- GCC_except_table9683
- GCC_except_table9684
- GCC_except_table9685
- GCC_except_table9686
- GCC_except_table9687
- GCC_except_table9688
- GCC_except_table9689
- GCC_except_table9690
- GCC_except_table9691
- GCC_except_table9692
- GCC_except_table9693
- GCC_except_table9694
- GCC_except_table9695
- GCC_except_table9710
- GCC_except_table9720
- GCC_except_table9848
- GCC_except_table9857
- GCC_except_table9858
- GCC_except_table9859
- GCC_except_table9860
- GCC_except_table9861
- GCC_except_table9863
- GCC_except_table9868
- GCC_except_table9886
- GCC_except_table9910
- GCC_except_table9911
- GCC_except_table9912
- GCC_except_table9913
- GCC_except_table9914
- GCC_except_table9924
- GCC_except_table9944
- GCC_except_table9945
- GCC_except_table9946
- GCC_except_table9947
- GCC_except_table9948
- GCC_except_table9949
- _OBJC_CLASS_$_PHPhotoLibraryObserverRegistrar
- _OBJC_IVAR_$_PHChange._cloudStatus
- _OBJC_IVAR_$_PHCollectionShare._uploadedPhotosCount
- _OBJC_IVAR_$_PHCollectionShare._uploadedVideosCount
- _OBJC_IVAR_$_PHMomentChangeRequest._algorithmVersionForEmptyThemeAssignment
- _OBJC_IVAR_$_PHMomentChangeRequest._algorithmVersionForVersionOverwrite
- _OBJC_IVAR_$_PHMomentChangeRequest._shouldOverwriteExistingThemeAlgorithmVersion
- _OBJC_IVAR_$_PHMomentShare._uploadedPhotosCount
- _OBJC_IVAR_$_PHMomentShare._uploadedVideosCount
- _OBJC_IVAR_$_PHMomentThemeAssignment._algorithmVersion
- _OBJC_IVAR_$_PHPhotoLibrary._observerRegistrar
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._changeHandlingDebugger
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_clearsOIDCacheAfterFetchResultDealloc
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_externalChangeObservers
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_fetchResults
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_internalChangeObservers
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_isChangeHandlingActive
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_isChangeHandlingAuthorized
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._lock_postsPersistentHistoryChangedNotifications
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._pendingLock
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._pendingLock_isChangeProcessingPending
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._pendingLock_lastChangeProcessingStarted
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._photoLibraryBundle
- _OBJC_IVAR_$_PHPhotoLibraryObserverRegistrar._uniqueObjectIDCache
- _OBJC_METACLASS_$_PHPhotoLibraryObserverRegistrar
- _PFMethodNotImplementedException
- _PHAssetCanPerformAdditionalProcessingOnAsset.onceToken.343
- _PLLocalizedNameWithFirstAndLastName
- _PLShouldBoostLogLevelForResourceRecipeID
- _SensitiveContentAnalysisLibraryCore.frameworkLibrary.19192
- _SensitiveContentAnalysisLibraryCore.frameworkLibrary.22384
- _SensitiveContentAnalysisLibraryCore.frameworkLibrary.36331
- __OBJC_$_CLASS_METHODS_PHPhotoLibraryObserverRegistrar
- __OBJC_$_INSTANCE_METHODS_PHPhotoLibraryObserverRegistrar
- __OBJC_$_INSTANCE_VARIABLES_PHPhotoLibraryObserverRegistrar
- __OBJC_$_PROP_LIST_PHAssetResourceRequest.266
- __OBJC_$_PROP_LIST_PHPhotoLibraryObserverRegistrar
- __OBJC_$_PROP_LIST_PHShare.144
- __OBJC_CLASS_RO_$_PHPhotoLibraryObserverRegistrar
- __OBJC_METACLASS_RO_$_PHPhotoLibraryObserverRegistrar
- ___103-[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:reply:]_block_invoke.479
- ___137-[PHAssetExportRequest handleResultWithFileURLs:cancelled:withError:forAsset:withOptions:progress:processingUnitCount:completionHandler:]_block_invoke.425
- ___137-[PHAssetExportRequest handleResultWithFileURLs:cancelled:withError:forAsset:withOptions:progress:processingUnitCount:completionHandler:]_block_invoke.429
- ___145-[PHShareAssetChangeRequestHelper addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:outKeyAssetIdentifier:outContainsEPPAssets:]_block_invoke.222
- ___155+[PHSensitiveContentAnalysisUtility protectImageManagerResult:outImage:infoDictionary:outInfoDictionary:forImageRequestFromAsset:applyLiveBlurIfSensitive:]_block_invoke
- ___32-[PHAssetComment commenterEmail]_block_invoke
- ___35-[PHAssetComment commenterFullName]_block_invoke
- ___35-[PHAssetComment commenterLastName]_block_invoke
- ___36-[PHAssetComment commenterFirstName]_block_invoke
- ___38-[PHAssetResourceRequest startRequest]_block_invoke_3
- ___38-[PHAssetResourceRequest startRequest]_block_invoke_4
- ___47+[PHAssetCollection propertiesToFetchWithHint:]_block_invoke.85
- ___50-[PHPhotoLibraryObserverRegistrar removeObserver:]_block_invoke
- ___54-[PHPhotoLibraryObserverRegistrar _lock_clearOIDCache]_block_invoke
- ___55-[PHPhotoLibrary _processPendingChangesWithDebugEvent:]_block_invoke.684
- ___55-[PHPhotoLibraryObserverRegistrar registerFetchResult:]_block_invoke
- ___57-[PHPhotoLibraryObserverRegistrar getObserversWithBlock:]_block_invoke
- ___57-[PHPhotoLibraryObserverRegistrar unregisterFetchResult:]_block_invoke
- ___58-[PHPhotoLibrary _publishCloudStatusChangeWithDebugEvent:]_block_invoke
- ___59-[PHSearchQuery _executeSpotlightSearchWithResultsHandler:]_block_invoke.135
- ___59-[PHSearchQuery _executeSpotlightSearchWithResultsHandler:]_block_invoke.137
- ___61-[PHSearchQuery _executeSpotlightSearchWithResultsHandlerV2:]_block_invoke.140
- ___64-[PHPhotoLibraryObserverRegistrar countOfRegisteredFetchResults]_block_invoke
- ___65-[PHPhotoLibraryObserverRegistrar clearIsChangeProcessingPending]_block_invoke
- ___68-[PHPhotoLibrary resetFaceAnalysisWithResetLevel:completionHandler:]_block_invoke
- ___68-[PHPhotoLibraryObserverRegistrar addObservers:authorizationStatus:]_block_invoke
- ___72-[PHPhotoLibraryObserverRegistrar clearsOIDCacheAfterFetchResultDealloc]_block_invoke
- ___76-[PHPhotoLibraryObserverRegistrar setClearsOIDCacheAfterFetchResultDealloc:]_block_invoke
- ___77-[PHPhotoLibraryObserverRegistrar postsPersistentHistoryChangedNotifications]_block_invoke
- ___78-[PHPhotoLibraryObserverRegistrar throttlePendingChangesWithDebugEvent:block:]_block_invoke
- ___81-[PHPhotoLibraryObserverRegistrar setPostsPersistentHistoryChangedNotifications:]_block_invoke
- ___81-[PHSearchFeedbackDiagnostics _collectPhotosAppOnScreenSearchDetailsWithHandler:]_block_invoke.228
- ___82+[PHAssetCollection fetchMomentsNeedingThemeAnalysisWithAlgorithmVersion:options:]_block_invoke
- ___82+[PHAssetCollection fetchMomentsNeedingThemeAnalysisWithAlgorithmVersion:options:]_block_invoke_2
- ___88-[PHAssetExportRequest bundleResourcesIfNeededForAsset:withFileURLs:options:completion:]_block_invoke.450
- ___89-[PHPhotoLibraryObserverRegistrar publishChangesToObserversOnQueue:withDebugEvent:block:]_block_invoke
- ___89-[PHPhotoLibraryObserverRegistrar publishChangesToObserversOnQueue:withDebugEvent:block:]_block_invoke.33
- ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke.120
- ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_2.123
- ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_3.124
- ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_4.125
- ___Block_byref_object_copy_.10383
- ___Block_byref_object_copy_.11121
- ___Block_byref_object_copy_.11380
- ___Block_byref_object_copy_.11539
- ___Block_byref_object_copy_.12384
- ___Block_byref_object_copy_.12643
- ___Block_byref_object_copy_.13130
- ___Block_byref_object_copy_.14776
- ___Block_byref_object_copy_.15551
- ___Block_byref_object_copy_.17522
- ___Block_byref_object_copy_.18488
- ___Block_byref_object_copy_.20123
- ___Block_byref_object_copy_.20289
- ___Block_byref_object_copy_.20613
- ___Block_byref_object_copy_.21080
- ___Block_byref_object_copy_.21680
- ___Block_byref_object_copy_.22203
- ___Block_byref_object_copy_.22390
- ___Block_byref_object_copy_.24152
- ___Block_byref_object_copy_.25041
- ___Block_byref_object_copy_.2538
- ___Block_byref_object_copy_.26715
- ___Block_byref_object_copy_.27241
- ___Block_byref_object_copy_.27957
- ___Block_byref_object_copy_.28248
- ___Block_byref_object_copy_.29780
- ___Block_byref_object_copy_.2983
- ___Block_byref_object_copy_.30751
- ___Block_byref_object_copy_.31497
- ___Block_byref_object_copy_.31779
- ___Block_byref_object_copy_.33159
- ___Block_byref_object_copy_.33710
- ___Block_byref_object_copy_.34266
- ___Block_byref_object_copy_.34408
- ___Block_byref_object_copy_.34836
- ___Block_byref_object_copy_.3541
- ___Block_byref_object_copy_.35416
- ___Block_byref_object_copy_.35702
- ___Block_byref_object_copy_.36640
- ___Block_byref_object_copy_.37080
- ___Block_byref_object_copy_.38680
- ___Block_byref_object_copy_.39235
- ___Block_byref_object_copy_.4157
- ___Block_byref_object_copy_.43309
- ___Block_byref_object_copy_.43730
- ___Block_byref_object_copy_.43941
- ___Block_byref_object_copy_.44166
- ___Block_byref_object_copy_.45498
- ___Block_byref_object_copy_.45899
- ___Block_byref_object_copy_.46412
- ___Block_byref_object_copy_.46707
- ___Block_byref_object_copy_.47081
- ___Block_byref_object_copy_.47566
- ___Block_byref_object_copy_.48884
- ___Block_byref_object_copy_.49082
- ___Block_byref_object_copy_.49292
- ___Block_byref_object_copy_.49329
- ___Block_byref_object_copy_.49756
- ___Block_byref_object_copy_.51512
- ___Block_byref_object_copy_.51805
- ___Block_byref_object_copy_.52536
- ___Block_byref_object_copy_.53326
- ___Block_byref_object_copy_.5629
- ___Block_byref_object_copy_.6674
- ___Block_byref_object_copy_.7147
- ___Block_byref_object_copy_.8864
- ___Block_byref_object_copy_.9129
- ___Block_byref_object_copy_.9677
- ___Block_byref_object_dispose_.10384
- ___Block_byref_object_dispose_.11122
- ___Block_byref_object_dispose_.11381
- ___Block_byref_object_dispose_.11540
- ___Block_byref_object_dispose_.12385
- ___Block_byref_object_dispose_.12644
- ___Block_byref_object_dispose_.13131
- ___Block_byref_object_dispose_.14777
- ___Block_byref_object_dispose_.15552
- ___Block_byref_object_dispose_.17523
- ___Block_byref_object_dispose_.18489
- ___Block_byref_object_dispose_.20124
- ___Block_byref_object_dispose_.20290
- ___Block_byref_object_dispose_.20614
- ___Block_byref_object_dispose_.21081
- ___Block_byref_object_dispose_.21681
- ___Block_byref_object_dispose_.22204
- ___Block_byref_object_dispose_.22391
- ___Block_byref_object_dispose_.24153
- ___Block_byref_object_dispose_.25042
- ___Block_byref_object_dispose_.2539
- ___Block_byref_object_dispose_.26716
- ___Block_byref_object_dispose_.27242
- ___Block_byref_object_dispose_.27958
- ___Block_byref_object_dispose_.28249
- ___Block_byref_object_dispose_.29781
- ___Block_byref_object_dispose_.2984
- ___Block_byref_object_dispose_.30752
- ___Block_byref_object_dispose_.31498
- ___Block_byref_object_dispose_.31780
- ___Block_byref_object_dispose_.33160
- ___Block_byref_object_dispose_.33711
- ___Block_byref_object_dispose_.34267
- ___Block_byref_object_dispose_.34409
- ___Block_byref_object_dispose_.34837
- ___Block_byref_object_dispose_.35417
- ___Block_byref_object_dispose_.3542
- ___Block_byref_object_dispose_.35703
- ___Block_byref_object_dispose_.36641
- ___Block_byref_object_dispose_.37081
- ___Block_byref_object_dispose_.38681
- ___Block_byref_object_dispose_.39236
- ___Block_byref_object_dispose_.4158
- ___Block_byref_object_dispose_.43310
- ___Block_byref_object_dispose_.43731
- ___Block_byref_object_dispose_.43942
- ___Block_byref_object_dispose_.44167
- ___Block_byref_object_dispose_.45499
- ___Block_byref_object_dispose_.45900
- ___Block_byref_object_dispose_.46413
- ___Block_byref_object_dispose_.46708
- ___Block_byref_object_dispose_.47082
- ___Block_byref_object_dispose_.47567
- ___Block_byref_object_dispose_.48885
- ___Block_byref_object_dispose_.49083
- ___Block_byref_object_dispose_.49293
- ___Block_byref_object_dispose_.49330
- ___Block_byref_object_dispose_.49757
- ___Block_byref_object_dispose_.51513
- ___Block_byref_object_dispose_.51806
- ___Block_byref_object_dispose_.52537
- ___Block_byref_object_dispose_.53327
- ___Block_byref_object_dispose_.5630
- ___Block_byref_object_dispose_.6675
- ___Block_byref_object_dispose_.7148
- ___Block_byref_object_dispose_.8865
- ___Block_byref_object_dispose_.9130
- ___Block_byref_object_dispose_.9678
- ___PHAssetCanPerformAdditionalProcessingOnAsset_block_invoke.344
- ___SensitiveContentAnalysisLibraryCore_block_invoke.19193
- ___SensitiveContentAnalysisLibraryCore_block_invoke.22385
- ___SensitiveContentAnalysisLibraryCore_block_invoke.36332
- ____fetchNonHintResources_block_invoke.227
- ___block_descriptor_48_e8_32r40r_e41_v32?0"NSArray"8"NSArray"16"NSArray"24lr32l8r40l8
- ___block_descriptor_56_e8_32s40s48s_e22_v24?0"NSString"8^B16ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48r56r_e33_v32?0q8"NSString"16"NSError"24ls32l8r48l8r56l8s40l8
- ___block_literal_global.1001
- ___block_literal_global.1003
- ___block_literal_global.1005.36872
- ___block_literal_global.1007.36867
- ___block_literal_global.1009
- ___block_literal_global.1011
- ___block_literal_global.1013
- ___block_literal_global.1015
- ___block_literal_global.1017
- ___block_literal_global.1019
- ___block_literal_global.1021
- ___block_literal_global.1023
- ___block_literal_global.1025
- ___block_literal_global.1027
- ___block_literal_global.1029
- ___block_literal_global.1031
- ___block_literal_global.1033
- ___block_literal_global.1035
- ___block_literal_global.1037
- ___block_literal_global.1039
- ___block_literal_global.1041
- ___block_literal_global.1043
- ___block_literal_global.1045
- ___block_literal_global.1047
- ___block_literal_global.1049
- ___block_literal_global.10501
- ___block_literal_global.1051
- ___block_literal_global.1053
- ___block_literal_global.1055
- ___block_literal_global.1057
- ___block_literal_global.1059
- ___block_literal_global.1061
- ___block_literal_global.1063.36500
- ___block_literal_global.1065
- ___block_literal_global.1067
- ___block_literal_global.1069
- ___block_literal_global.1071
- ___block_literal_global.1073
- ___block_literal_global.1075
- ___block_literal_global.1077
- ___block_literal_global.1079
- ___block_literal_global.1081
- ___block_literal_global.1083
- ___block_literal_global.1085
- ___block_literal_global.1087
- ___block_literal_global.1089
- ___block_literal_global.1091
- ___block_literal_global.1093
- ___block_literal_global.1095
- ___block_literal_global.1097
- ___block_literal_global.1099
- ___block_literal_global.1101
- ___block_literal_global.1103
- ___block_literal_global.1105
- ___block_literal_global.1107
- ___block_literal_global.1109
- ___block_literal_global.1111
- ___block_literal_global.1113
- ___block_literal_global.1115
- ___block_literal_global.1117
- ___block_literal_global.1119
- ___block_literal_global.112.41004
- ___block_literal_global.11201
- ___block_literal_global.1121
- ___block_literal_global.1123
- ___block_literal_global.1125
- ___block_literal_global.1127
- ___block_literal_global.1129
- ___block_literal_global.1131
- ___block_literal_global.1133
- ___block_literal_global.1135
- ___block_literal_global.1137
- ___block_literal_global.1139
- ___block_literal_global.11396
- ___block_literal_global.1141
- ___block_literal_global.1143
- ___block_literal_global.1145
- ___block_literal_global.1147
- ___block_literal_global.1149
- ___block_literal_global.1151
- ___block_literal_global.1153
- ___block_literal_global.1155
- ___block_literal_global.1157
- ___block_literal_global.1159
- ___block_literal_global.1161
- ___block_literal_global.1163
- ___block_literal_global.1168
- ___block_literal_global.1170
- ___block_literal_global.1172
- ___block_literal_global.1174
- ___block_literal_global.1176
- ___block_literal_global.11773
- ___block_literal_global.1178
- ___block_literal_global.1180
- ___block_literal_global.1182
- ___block_literal_global.1184
- ___block_literal_global.1186
- ___block_literal_global.1188
- ___block_literal_global.1190
- ___block_literal_global.1192
- ___block_literal_global.1194
- ___block_literal_global.1196
- ___block_literal_global.1198
- ___block_literal_global.1200
- ___block_literal_global.1202
- ___block_literal_global.1204
- ___block_literal_global.1206
- ___block_literal_global.1208
- ___block_literal_global.1210
- ___block_literal_global.1212
- ___block_literal_global.1214
- ___block_literal_global.12695
- ___block_literal_global.130
- ___block_literal_global.1325
- ___block_literal_global.1334
- ___block_literal_global.13365
- ___block_literal_global.134.47626
- ___block_literal_global.1349
- ___block_literal_global.1359
- ___block_literal_global.1378
- ___block_literal_global.144.38649
- ___block_literal_global.14442
- ___block_literal_global.14844
- ___block_literal_global.149
- ___block_literal_global.15547
- ___block_literal_global.170
- ___block_literal_global.170.29438
- ___block_literal_global.17118
- ___block_literal_global.1720
- ___block_literal_global.17755
- ___block_literal_global.18517
- ___block_literal_global.18568
- ___block_literal_global.19773
- ___block_literal_global.20040
- ___block_literal_global.206.28531
- ___block_literal_global.20630
- ___block_literal_global.21055
- ___block_literal_global.211
- ___block_literal_global.217.13917
- ___block_literal_global.217.29450
- ___block_literal_global.219.29433
- ___block_literal_global.21998
- ___block_literal_global.224.14726
- ___block_literal_global.22838
- ___block_literal_global.234.34000
- ___block_literal_global.24060
- ___block_literal_global.25402
- ___block_literal_global.2565
- ___block_literal_global.26074
- ___block_literal_global.26942
- ___block_literal_global.27659
- ___block_literal_global.27934
- ___block_literal_global.2808
- ___block_literal_global.28562
- ___block_literal_global.28831
- ___block_literal_global.28910
- ___block_literal_global.29436
- ___block_literal_global.2980
- ___block_literal_global.29896
- ___block_literal_global.3.11401
- ___block_literal_global.3.2979
- ___block_literal_global.30281
- ___block_literal_global.30478
- ___block_literal_global.30762
- ___block_literal_global.31179
- ___block_literal_global.3150
- ___block_literal_global.32011
- ___block_literal_global.32153
- ___block_literal_global.32627
- ___block_literal_global.33265
- ___block_literal_global.335
- ___block_literal_global.34003
- ___block_literal_global.342
- ___block_literal_global.34280
- ___block_literal_global.34359
- ___block_literal_global.34505
- ___block_literal_global.34678
- ___block_literal_global.35154
- ___block_literal_global.355
- ___block_literal_global.35707
- ___block_literal_global.36207
- ___block_literal_global.3625
- ___block_literal_global.36950
- ___block_literal_global.37.32057
- ___block_literal_global.37.47200
- ___block_literal_global.37141
- ___block_literal_global.37687
- ___block_literal_global.3779
- ___block_literal_global.37994
- ___block_literal_global.38721
- ___block_literal_global.38979
- ___block_literal_global.39408
- ___block_literal_global.40006
- ___block_literal_global.40217
- ___block_literal_global.40702
- ___block_literal_global.41010
- ___block_literal_global.416.21878
- ___block_literal_global.42318
- ___block_literal_global.424
- ___block_literal_global.42898
- ___block_literal_global.43312
- ___block_literal_global.43995
- ___block_literal_global.4409
- ___block_literal_global.44183
- ___block_literal_global.4449.22544
- ___block_literal_global.44801
- ___block_literal_global.452
- ___block_literal_global.45581
- ___block_literal_global.456
- ___block_literal_global.45931
- ___block_literal_global.46248
- ___block_literal_global.46339
- ___block_literal_global.465
- ___block_literal_global.46989
- ___block_literal_global.47207
- ___block_literal_global.47645
- ___block_literal_global.47793
- ___block_literal_global.481
- ___block_literal_global.4814
- ___block_literal_global.48497
- ___block_literal_global.48849
- ___block_literal_global.4907
- ___block_literal_global.49294
- ___block_literal_global.49342
- ___block_literal_global.49651
- ___block_literal_global.4982
- ___block_literal_global.49946
- ___block_literal_global.50.26042
- ___block_literal_global.51257
- ___block_literal_global.52609
- ___block_literal_global.53181
- ___block_literal_global.539
- ___block_literal_global.551.22836
- ___block_literal_global.5666
- ___block_literal_global.580
- ___block_literal_global.660
- ___block_literal_global.669
- ___block_literal_global.672
- ___block_literal_global.674
- ___block_literal_global.6759
- ___block_literal_global.7154
- ___block_literal_global.7800
- ___block_literal_global.8021
- ___block_literal_global.8188
- ___block_literal_global.82.4906
- ___block_literal_global.88
- ___block_literal_global.8856
- ___block_literal_global.8933
- ___block_literal_global.9346
- ___block_literal_global.977
- ___block_literal_global.979
- ___block_literal_global.981
- ___block_literal_global.983
- ___block_literal_global.985
- ___block_literal_global.987
- ___block_literal_global.989
- ___block_literal_global.991
- ___block_literal_global.993
- ___block_literal_global.995
- ___block_literal_global.997
- ___block_literal_global.999
- ___getSCSensitivityAnalysisClass_block_invoke.19191
- ___getSCSensitivityAnalysisClass_block_invoke.22383
- ___getSCSensitivityAnalysisClass_block_invoke.36330
- __currentTimestampString.s_formatter.47201
- __currentTimestampString.s_onceToken.47199
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_Photos
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_Photos
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_Photos
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_Photos
- _allowedEntities.pl_once_object_80
- _allowedEntities.pl_once_object_81
- _allowedEntities.pl_once_token_80
- _allowedEntities.pl_once_token_81
- _allowedInfoKeys.allowedKeys.18772
- _allowedInfoKeys.allowedKeys.40506
- _allowedInfoKeys.onceToken.18771
- _allowedInfoKeys.onceToken.40505
- _audit_stringSensitiveContentAnalysis.19202
- _audit_stringSensitiveContentAnalysis.22389
- _audit_stringSensitiveContentAnalysis.36337
- _corePropertiesToFetch.array.22841
- _corePropertiesToFetch.array.28559
- _corePropertiesToFetch.array.34004
- _corePropertiesToFetch.onceToken.22840
- _corePropertiesToFetch.onceToken.28558
- _corePropertiesToFetch.onceToken.34002
- _defaultManager.onceToken.51592
- _entityKeyMap.pl_once_object_15.11182
- _entityKeyMap.pl_once_object_15.11784
- _entityKeyMap.pl_once_object_15.13356
- _entityKeyMap.pl_once_object_15.13659
- _entityKeyMap.pl_once_object_15.27650
- _entityKeyMap.pl_once_object_15.28921
- _entityKeyMap.pl_once_object_15.32618
- _entityKeyMap.pl_once_object_15.36197
- _entityKeyMap.pl_once_object_15.40038
- _entityKeyMap.pl_once_object_15.44203
- _entityKeyMap.pl_once_object_15.45922
- _entityKeyMap.pl_once_object_15.46331
- _entityKeyMap.pl_once_object_15.47790
- _entityKeyMap.pl_once_object_15.4806
- _entityKeyMap.pl_once_object_15.49821
- _entityKeyMap.pl_once_object_15.50740
- _entityKeyMap.pl_once_object_15.8027
- _entityKeyMap.pl_once_object_16.33992
- _entityKeyMap.pl_once_object_16.34346
- _entityKeyMap.pl_once_object_16.40204
- _entityKeyMap.pl_once_object_16.4396
- _entityKeyMap.pl_once_object_16.46977
- _entityKeyMap.pl_once_object_16.53168
- _entityKeyMap.pl_once_token_15.11181
- _entityKeyMap.pl_once_token_15.11783
- _entityKeyMap.pl_once_token_15.13355
- _entityKeyMap.pl_once_token_15.13658
- _entityKeyMap.pl_once_token_15.27649
- _entityKeyMap.pl_once_token_15.28920
- _entityKeyMap.pl_once_token_15.32617
- _entityKeyMap.pl_once_token_15.36196
- _entityKeyMap.pl_once_token_15.40037
- _entityKeyMap.pl_once_token_15.44202
- _entityKeyMap.pl_once_token_15.45921
- _entityKeyMap.pl_once_token_15.46330
- _entityKeyMap.pl_once_token_15.47789
- _entityKeyMap.pl_once_token_15.4805
- _entityKeyMap.pl_once_token_15.49820
- _entityKeyMap.pl_once_token_15.50739
- _entityKeyMap.pl_once_token_15.8026
- _entityKeyMap.pl_once_token_16.33991
- _entityKeyMap.pl_once_token_16.34345
- _entityKeyMap.pl_once_token_16.40203
- _entityKeyMap.pl_once_token_16.4395
- _entityKeyMap.pl_once_token_16.46976
- _entityKeyMap.pl_once_token_16.53167
- _getSCSensitivityAnalysisClass.19189
- _getSCSensitivityAnalysisClass.22381
- _getSCSensitivityAnalysisClass.36323
- _getSCSensitivityAnalysisClass.softClass.19190
- _getSCSensitivityAnalysisClass.softClass.22382
- _getSCSensitivityAnalysisClass.softClass.36329
- _identifierPropertiesToFetch.array.35155
- _identifierPropertiesToFetch.onceToken.35153
- _kMSASInfoNotInterestingKey
- _objc_msgSend$_addObservers:authorizationStatus:
- _objc_msgSend$_plObject
- _objc_msgSend$_removeObserver:
- _objc_msgSend$_sensitivityAnalysisFromAsset:outError:
- _objc_msgSend$assert:code:format:
- _objc_msgSend$assetsWithAvalancheUUID:inManagedObjectContext:
- _objc_msgSend$assignEmptyThemeWithAlgorithmVersion:
- _objc_msgSend$assignEmptyThemesWithAlgorithmVersion:
- _objc_msgSend$assignThemeNamed:algorithmVersion:withConfidence:
- _objc_msgSend$cloudSharedCommentWithGUID:inLibrary:
- _objc_msgSend$cloudStatus
- _objc_msgSend$commenterEmail
- _objc_msgSend$commenterFirstName
- _objc_msgSend$commenterFullName
- _objc_msgSend$commenterLastName
- _objc_msgSend$fetchMomentIDsNotAnalyzedForThemesInContext:withAlgorithmVersion:
- _objc_msgSend$fetchMomentsNeedingThemeAnalysisWithAlgorithmVersion:options:
- _objc_msgSend$firstSyncDate
- _objc_msgSend$getLivePhotoImageMetadataFromURL:pairingIdentifier:
- _objc_msgSend$hasAlphaChannel
- _objc_msgSend$hasCloudStatusChanges
- _objc_msgSend$initWithCPLStatus:
- _objc_msgSend$initWithCloudStatus:library:
- _objc_msgSend$initWithQuery:oids:registerIfNeeded:usingManagedObjectContext:
- _objc_msgSend$initWithQuery:registerIfNeeded:
- _objc_msgSend$initWithSceneTaxonomyProvider:csuTaxonomyObjectStore:locale:calendar:indexDateFormatter:delegate:
- _objc_msgSend$initWithThemeName:confidence:algorithmVersion:
- _objc_msgSend$initWithUUID:photoLibrary:
- _objc_msgSend$isCaption
- _objc_msgSend$isHDRScreenshotWithAlphaChannelAsset:withCurrentType:
- _objc_msgSend$isOpen
- _objc_msgSend$lastSyncDate
- _objc_msgSend$redactedDescriptionForPath:
- _objc_msgSend$resetFaceAnalysisWithResetLevel:completionHandler:
- _objc_msgSend$setThemeAssignmentsToAlgorithmVersion:
- _objc_msgSend$sharedPersistentStoreCoordinator
- _propertiesToFetch.pl_once_object_24.33706
- _propertiesToFetch.pl_once_token_24.33705
- _propertiesToFetchWithHint:.array.11197
- _propertiesToFetchWithHint:.array.11791
- _propertiesToFetchWithHint:.array.13684
- _propertiesToFetchWithHint:.array.23294
- _propertiesToFetchWithHint:.array.27660
- _propertiesToFetchWithHint:.array.28931
- _propertiesToFetchWithHint:.array.32628
- _propertiesToFetchWithHint:.array.36208
- _propertiesToFetchWithHint:.array.40059
- _propertiesToFetchWithHint:.array.45932
- _propertiesToFetchWithHint:.array.47794
- _propertiesToFetchWithHint:.array.49834
- _propertiesToFetchWithHint:.array.50768
- _propertiesToFetchWithHint:.array.8051
- _propertiesToFetchWithHint:.onceToken.11196
- _propertiesToFetchWithHint:.onceToken.11790
- _propertiesToFetchWithHint:.onceToken.13364
- _propertiesToFetchWithHint:.onceToken.13683
- _propertiesToFetchWithHint:.onceToken.22832
- _propertiesToFetchWithHint:.onceToken.23293
- _propertiesToFetchWithHint:.onceToken.27658
- _propertiesToFetchWithHint:.onceToken.28561
- _propertiesToFetchWithHint:.onceToken.28930
- _propertiesToFetchWithHint:.onceToken.32626
- _propertiesToFetchWithHint:.onceToken.33996
- _propertiesToFetchWithHint:.onceToken.36206
- _propertiesToFetchWithHint:.onceToken.40058
- _propertiesToFetchWithHint:.onceToken.4407
- _propertiesToFetchWithHint:.onceToken.45930
- _propertiesToFetchWithHint:.onceToken.47792
- _propertiesToFetchWithHint:.onceToken.49833
- _propertiesToFetchWithHint:.onceToken.50767
- _propertiesToFetchWithHint:.onceToken.8050
- _propertiesToFetchWithHint:.pl_once_object_15.34360
- _propertiesToFetchWithHint:.pl_once_object_15.40218
- _propertiesToFetchWithHint:.pl_once_object_15.46990
- _propertiesToFetchWithHint:.pl_once_object_15.53182
- _propertiesToFetchWithHint:.pl_once_token_15.34358
- _propertiesToFetchWithHint:.pl_once_token_15.40216
- _propertiesToFetchWithHint:.pl_once_token_15.46988
- _propertiesToFetchWithHint:.pl_once_token_15.53180
- _propertiesToFetchWithHint:.propertiesToFetchByHint.13367
- _propertiesToFetchWithHint:.propertiesToFetchByHint.22834
- _propertiesToFetchWithHint:.propertiesToFetchByHint.28564
- _propertiesToFetchWithHint:.propertiesToFetchByHint.33998
- _propertiesToFetchWithHint:.propertyQueue.13366
- _propertiesToFetchWithHint:.propertyQueue.22833
- _propertiesToFetchWithHint:.propertyQueue.28563
- _propertiesToFetchWithHint:.propertyQueue.33997
- _propertiesToPrefetch.onceToken.22396
- _propertiesToPrefetch.onceToken.28226
- _propertiesToPrefetch.onceToken.33687
- _propertiesToPrefetch.propertiesToPrefetch.22397
- _propertiesToPrefetch.propertiesToPrefetch.28227
- _propertiesToPrefetch.propertiesToPrefetch.33688
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.13117
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.28411
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.33966
- _propertySetAccessorsByPropertySet.onceToken.13116
- _propertySetAccessorsByPropertySet.onceToken.28410
- _propertySetAccessorsByPropertySet.onceToken.33965
- _propertySetClassForPropertySet:.onceToken.13118
- _propertySetClassForPropertySet:.onceToken.28418
- _propertySetClassForPropertySet:.onceToken.33974
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.13119
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.28419
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.33975
- _sharedDecoder.s_onceToken.49945
- _sharedDecoder.s_shared.49947
- _sharedLazyPhotoLibraryForCMM.pl_once_object_48
- _sharedLazyPhotoLibraryForCMM.pl_once_token_48
- _transformValueExpression:forKeyPath:._passThroughSet.11165
- _transformValueExpression:forKeyPath:._passThroughSet.11780
- _transformValueExpression:forKeyPath:._passThroughSet.13345
- _transformValueExpression:forKeyPath:._passThroughSet.13644
- _transformValueExpression:forKeyPath:._passThroughSet.22787
- _transformValueExpression:forKeyPath:._passThroughSet.27629
- _transformValueExpression:forKeyPath:._passThroughSet.28547
- _transformValueExpression:forKeyPath:._passThroughSet.28917
- _transformValueExpression:forKeyPath:._passThroughSet.32609
- _transformValueExpression:forKeyPath:._passThroughSet.33980
- _transformValueExpression:forKeyPath:._passThroughSet.36191
- _transformValueExpression:forKeyPath:._passThroughSet.40027
- _transformValueExpression:forKeyPath:._passThroughSet.4387
- _transformValueExpression:forKeyPath:._passThroughSet.44188
- _transformValueExpression:forKeyPath:._passThroughSet.45910
- _transformValueExpression:forKeyPath:._passThroughSet.47787
- _transformValueExpression:forKeyPath:._passThroughSet.50718
- _transformValueExpression:forKeyPath:._passThroughSet.53129
- _transformValueExpression:forKeyPath:.onceToken.11164
- _transformValueExpression:forKeyPath:.onceToken.11779
- _transformValueExpression:forKeyPath:.onceToken.13344
- _transformValueExpression:forKeyPath:.onceToken.13643
- _transformValueExpression:forKeyPath:.onceToken.22786
- _transformValueExpression:forKeyPath:.onceToken.27628
- _transformValueExpression:forKeyPath:.onceToken.28546
- _transformValueExpression:forKeyPath:.onceToken.28916
- _transformValueExpression:forKeyPath:.onceToken.32608
- _transformValueExpression:forKeyPath:.onceToken.33979
- _transformValueExpression:forKeyPath:.onceToken.36190
- _transformValueExpression:forKeyPath:.onceToken.40026
- _transformValueExpression:forKeyPath:.onceToken.4386
- _transformValueExpression:forKeyPath:.onceToken.44187
- _transformValueExpression:forKeyPath:.onceToken.45909
- _transformValueExpression:forKeyPath:.onceToken.47786
- _transformValueExpression:forKeyPath:.onceToken.50717
- _transformValueExpression:forKeyPath:.onceToken.53128
- _uniqueObjectIDCache.pl_once_object_79
- _uniqueObjectIDCache.pl_once_token_79
CStrings:
+ "\n----------------------------------------\n"
+ "%@ %p initWithLibraryBundle:%@"
+ "%@ [last-update:%@ first-complete:%@]"
+ "%@: \"%@\"\n\n"
+ "%p: qos: %@, obs: %tu, sync: %d"
+ "%{public}@ video request chose video resource: %{public}@ for asset: %{public}@"
+ "%{public}@ video request found zero playable videos for asset: %{public}@, retrying, returned video may not be playable"
+ "%{public}@ video request found zero videos for asset: %{public}@"
+ "(L-%d: %@)"
+ "(SPL: %@)"
+ "-[PHPhotoLibrary urlForApplicationDataFolderIdentifier:]"
+ "3"
+ "@\"PHPhotoLibraryChangeObserverRegistrar\""
+ "@\"PHPhotoLibraryCloudStatusObserverRegistrar\""
+ "@52@0:8@16@24@32B40@44"
+ "@64@0:8@16@24Q32d40@48@56"
+ "Asset resource with type %{public}@ has incompatible CPLResourceType %{public}@, defaulting to CPLResourceTypeUnknown"
+ "Attempting to create %@"
+ "Attempting to move asset %@ that cannot be moved to personal library. Check with -[PHAsset canPerformEditOperation:PHAssetEditOperationMoveToPersonalLibrary] first"
+ "Attempting to move asset %@ that cannot be moved to shared library. Check with -[PHAsset canPerformEditOperation:PHAssetEditOperationMoveToSharedLibrary] first"
+ "Attempting to move assets to a LibraryScope that doesn't have a current user participant. This is an invalid action."
+ "Attempting to reject an asset %@ that is not in a suggested state"
+ "Attempting to remove an asset %@ that is not in a suggested state"
+ "Attempting to unreject an asset %@ that does not have a suggested bit set"
+ "Attempting to unreject an asset %@ that is not in a manually rejected state"
+ "BOOL PHAssetExportRequestProcessingRequiredForAssetWithOptions(PHAsset *__strong _Nonnull, PHAssetExportRequestOptions *__strong _Nonnull, PFMetadata *__strong _Nullable, NSDictionary<PHAssetExportRequestFileURLKey,NSURL *> *__strong _Nullable)"
+ "Container has nil PSC. %@"
+ "Could not write file to path: %@ because of: %@"
+ "Error analyzing assets for analysis coordinator feature: %lu error: %@"
+ "Error analyzing video for safety: %{public}@, error: %@"
+ "Error intializing SCSensitivityAnalysis for asset: %{public}@ error: %@"
+ "Error intializing SCSensitivityAnalysis for assetID: %{public}@ error: %@"
+ "PHAnalysisCoalescer"
+ "PHAnalysisCoalescer attempted to analyze assets without a photoLibrary"
+ "PHAssetResourceManager.retryRequest"
+ "PHExternalAssetResource: Unable to issue sandbox extension for %@"
+ "PHExternalAssetResource: fallback to readonly sandbox extension for %@"
+ "PHFetchResult init with invalid config: %{public}@, library: %{public}@ %@\n\terror: %@\n\tpsc error: %@\n\tself: %@"
+ "PHPhotoLibraryChangeObserverRegistrar"
+ "PHPhotoLibraryCloudStatusObserverRegistrar"
+ "PHValidationFailureTypeErrorKey"
+ "PHValidator: NON-FATAL error, invalid or missing video duration. (Error: %@)"
+ "PhotosSuggester is attempting to reject an asset %@ that is already added to shared zone"
+ "PhotosSuggester is attempting to reject an asset %@ that is already in a rejected state"
+ "Query: %@\n"
+ "RETRY: Read metadata success: %{BOOL}d Invalid image metadata. (Error: %@)"
+ "RETRY: Read metadata success: %{public}@ Invalid video metadata (%{public}@). (Error: %@)"
+ "Report Time: %@\n"
+ "Search Query Hang Issue"
+ "Skipping analysis for asset %{public}@, with thumbnailIndex %lu"
+ "Spotlight query string: %@\n"
+ "Successfully wrote blob data to: %@"
+ "T@\"CPLStatus\",R,C,N"
+ "T@\"NSDate\",R,V_firstSyncCompletionDate"
+ "T@\"NSDate\",R,V_lastSyncProgressDate"
+ "T@\"PHAnalysisCoalescer\",R"
+ "T@?,C,V_beginObservingCloudStatusBlock"
+ "TB,N,V_shouldOverwriteExistingThemeVersions"
+ "TB,R,GisCloudSyncEnabled,V_cloudSyncEnabled"
+ "TB,V_waitForDelayedSaveActions"
+ "TTR: Detected search query hang/timeout"
+ "Timeout: %.0fs\n"
+ "Tq,N,V_adapterVersionForEmptyThemeAssignment"
+ "Tq,N,V_adapterVersionForVersionOverwrite"
+ "Tq,N,V_uemVersionForEmptyThemeAssignment"
+ "Tq,N,V_uemVersionForVersionOverwrite"
+ "Tq,R,N,V_adapterVersion"
+ "Tq,R,N,V_uemVersion"
+ "Unable to delete file at path %@ - error: %@"
+ "Unexpected error registering change observer, could not access photo library"
+ "Unexpected error registering cloud status observer, could not access photo library"
+ "Your search query has experienced an unexpected hang/timeout, please file a Radar to diagnose the issue"
+ "[PHAssetExportRequest] Asset %{public}@ live photo metadata is invald, processing required to fixup, error: %@"
+ "[PHAssetExportRequest] Export request processing required for asset %{public}@: %{BOOL}d (metadataOperationLocation=%td, metadataOperationCaption=%td, metadataOperationCaptionAccessibilityDescription=%td, metadataChangeCustomDate=%{private}@, livePhotoMetadataFixup=%{BOOL}d producingNewFilesForExport=%{BOOL}d, options.variant=%td, requiresSloMoFlattening=%{BOOL}d, videoExportPreset=%{public}@, type = %{public}@)"
+ "[PHInternalAssetExportRequest] Asset %{public}@ is an HDR screenshot in the HEIC format. Using PNG as compatible variant instead of JPG"
+ "[RM] %{public}@ In library perform for video with progress: %{public}@, asset: %{public}@ %{public}@"
+ "[RM] %{public}@ In library perform to make resource available for asset: %{public}@ %{public}@, resource: %{public}@"
+ "[RM] %{public}@ asset resource request retrying after %f due to error: %@"
+ "[RM] %{public}@ asset resource request sending make available request for asset: %{public}@ %{public}@, resource: %{public}@"
+ "[RM] %{public}@ could not load asset %{public}@ with error: %@"
+ "[RM] %{public}@ could not load asset: %{public}@ for video request with error: %@"
+ "[RM] %{public}@ media request retrying after %f due to error: %@"
+ "_adapterVersion"
+ "_adapterVersionForEmptyThemeAssignment"
+ "_adapterVersionForVersionOverwrite"
+ "_addChangeObservers:authorizationStatus:"
+ "_addCloudStatusObservers:authorizationStatus:"
+ "_addObservers:authorizationStatus: waiting for authorization (%@)"
+ "_analyzeBufferedAssets:inLibrary:"
+ "_beginObservingCloudStatusBlock"
+ "_changeObserverRegistrar"
+ "_cloudStatusHandlerQueue"
+ "_cloudStatusObserverRegistrar"
+ "_cplStatusDelegateQueue"
+ "_firstSyncCompletionDate"
+ "_handleInitWithInvalidConfigurationDetails:library:"
+ "_lastSyncProgressDate"
+ "_lazyAnalysisCoalescer"
+ "_lock_assetUUIDsByFeature"
+ "_lock_cloudStatusObservers"
+ "_lock_hasCloudStatusObservers"
+ "_lock_isCloudStatusHandlingActive"
+ "_lock_isCloudStatusHandlingAuthorized"
+ "_lock_pauseCloudStatusHandlingIfNeeded"
+ "_lock_pendingBlock"
+ "_lock_resumeCloudStatusHandlingIfNeeded"
+ "_logFailureIfNeededForResult:andFeature:"
+ "_pauseCloudStatusHandlingIfNeeded - observers: %tu isActive: %d"
+ "_processCPLStatusDidChange:"
+ "_publishCloudStatusUpdate:"
+ "_removeChangeObserver:"
+ "_removeCloudStatusObserver:"
+ "_resumeCloudStatusHandlingIfNeeded - observers: %tu isActive: %d authorized: %d"
+ "_retryInterval"
+ "_setupLazyCPLStatusIfNecessary"
+ "_shouldOverwriteExistingThemeVersions"
+ "_snapshotOfBufferedAssets"
+ "_triggerQueryTimeoutTapToRadarForQuery:"
+ "_uemVersion"
+ "_uemVersionForEmptyThemeAssignment"
+ "_uemVersionForVersionOverwrite"
+ "_waitForDelayedSaveActions"
+ "adapterVersion"
+ "adapterVersionForEmptyThemeAssignment"
+ "adapterVersionForOverwrite"
+ "adapterVersionForVersionOverwrite"
+ "addAssetSearchEntityWithLabel:identifier:type:confidence:localeIdentifier:dateInterval:synonyms:"
+ "addSearchRankingWithLabel:identifier:type:rankingScore:localeIdentifier:synonyms:"
+ "analysisCoalescer"
+ "assert:code:failureType:format:"
+ "assetsWithAvalancheUUID:sourceType:inManagedObjectContext:"
+ "assignEmptyThemeWithAdapterVersion:uemVersion:"
+ "assignEmptyThemesWithAdapterVersion:uemVersion:"
+ "assignThemeNamed:adapterVersion:uemVersion:confidence:"
+ "assignThemeNamed:adapterVersion:uemVersion:withConfidence:"
+ "beginObservingCloudStatusBlock"
+ "coalesceAndAnalyzeAssets:forFeature:"
+ "collectionShareComments"
+ "com.apple.photos.CPLStatusDelegate-queue"
+ "com.apple.photos.PHPhotoLibraryCloudStatus-queue"
+ "com.apple.photos.analysisCoalescer"
+ "disabled"
+ "enabled"
+ "failed to create _PHFetchRequestWrapper"
+ "fetchContributorForComment:options:"
+ "fetchMomentIDsNotAnalyzedForThemesInContext:adapterVersion:uemVersion:"
+ "fetchMomentsNeedingThemeAnalysisWithAdapterVersion:uemVersion:options:"
+ "fileRadarUserNotificationWithHeader:message:radarTitle:radarDescription:radarComponent:diagnosticTTRType:attachments:extensionItem:"
+ "firstSyncCompletionDate"
+ "getNilPhotoLibraryReasonAndName:"
+ "hasObservers"
+ "initForNewObjectWithRequestData:"
+ "initWithCPLStatus:isEnabled:"
+ "initWithMediaTypeCounts:library:"
+ "initWithQuery:library:"
+ "initWithQuery:library:oids:registerIfNeeded:usingManagedObjectContext:"
+ "initWithQuery:library:registerIfNeeded:"
+ "initWithSceneTaxonomyProvider:csuTaxonomyObjectStore:locale:calendar:indexDateFormatter:countrySynonymProvider:delegate:"
+ "initWithThemeName:confidence:adapterVersion:uemVersion:"
+ "initWithUUID:objectID:requestData:"
+ "initWithUUID:sourceType:photoLibrary:"
+ "isFinderSyncedAsset"
+ "isHDRScreenshotAsset:withCurrentType:"
+ "lastSyncProgressDate"
+ "nil query"
+ "photoLibraryDidUpdateCloudStatus:"
+ "query for person with no share participant provided"
+ "query for share participant with no person provided"
+ "query has nil fetch request"
+ "queryForContributorForComment:options:"
+ "registerCloudStatusObserver:"
+ "resetThemeAssignmentVersions"
+ "retryInterval"
+ "sensitivityAnalysisFromAsset:outError:"
+ "setAdapterVersionForEmptyThemeAssignment:"
+ "setAdapterVersionForVersionOverwrite:"
+ "setBeginObservingCloudStatusBlock:"
+ "setDelegateQueue:"
+ "setNilPhotoLibraryReason:name:"
+ "setPostDelayedSaveActionsReply:"
+ "setRetryInterval:"
+ "setShouldOverwriteExistingThemeVersions:"
+ "setThemeAssignmentsToAdapterVersion:uemVersion:"
+ "setUemVersionForEmptyThemeAssignment:"
+ "setUemVersionForVersionOverwrite:"
+ "setWaitForDelayedSaveActions:"
+ "sharedPersistentStoreCoordinatorWithError:"
+ "shouldOverwriteExistingThemeVersions"
+ "uemVersion"
+ "uemVersionForEmptyThemeAssignment"
+ "uemVersionForOverwrite"
+ "uemVersionForVersionOverwrite"
+ "unregisterCloudStatusObserver:"
+ "v24@?0@\"NSError\"8@\"NSString\"16"
+ "v32@0:8q16q24"
+ "v40@?0q8Q16@\"NSString\"24@\"NSError\"32"
+ "v44@0:8B16q20Q28@36"
+ "v48@0:8@16q24q32@40"
+ "v60@0:8@16^@24@32^@40@48B56"
+ "v72@0:8@16@24Q32d40@48@56@64"
+ "waitForDelayedSaveActions"
- "%p: qos: %@, int: %tu, ext: %tu, sync: %d"
- "%{public}@ video request found zero playable videos for asset: %@, retrying, returned video may not be playable"
- ": %@ [last:%@ first:%@]"
- "@\"PHPhotoLibraryObserverRegistrar\""
- "@56@0:8@16@24Q32d40@48"
- "Attemping to PhotosSuggester reject an asset %@ that is already added to shared zone"
- "Attemping to PhotosSuggester reject an asset %@ that is already in a rejected state"
- "Attemping to move asset %@ that cannot be moved to personal library. Check with -[PHAsset canPerformEditOperation:PHAssetEditOperationMoveToPersonalLibrary] first"
- "Attemping to move asset %@ that cannot be moved to shared library. Check with -[PHAsset canPerformEditOperation:PHAssetEditOperationMoveToSharedLibrary] first"
- "Attemping to move assets to a LibraryScope that doesn't have a current user participant. This is an invalid action."
- "Attemping to reject an asset %@ that is not in a suggested state"
- "Attemping to remove an asset %@ that is not in a suggested state"
- "Attemping to unreject an asset %@ that does not have a suggested bit set"
- "Attemping to unreject an asset %@ that is not in a manually rejected state"
- "Attempting to create %{public}@"
- "B32@0:8@16^B24"
- "BOOL PHAssetExportRequestProcessingRequiredForAssetWithOptions(PHAsset *__strong _Nonnull, PHAssetExportRequestOptions *__strong _Nonnull, PFMetadata *__strong _Nullable)"
- "Could not write file to path: %{public}@ because of: %@"
- "DISABLED"
- "ENABLED"
- "Error analyzing asset thumbnail for safety: %@, error: %@"
- "Error analyzing video for safety: %@, error: %@"
- "Error intializing SCSensitivityAnalysis for asset: %@ error: %@"
- "Error intializing SCSensitivityAnalysis for assetID: %@ error: %@"
- "Notifications: Ignoring comment notification because mstreamd says it's not interesting and is not a caption"
- "Notifications: mstreamd says comment is not interesting, but allowing as caption"
- "PHExternalAssetResource: Unable to issue sandbox extension for %@ (%{public}@)"
- "PHExternalAssetResource: fallback to readonly sandbox extension for %@ (%{public}@)"
- "PHFetchRequest failed to create _PHFetchRequestWrapper from fetch request %@"
- "PHFetchRequest initialized with invalid query, nil fetch request %@"
- "PHFetchRequest initialized with nil query"
- "PHPhotoLibraryObserverRegistrar"
- "RETRY: Invalid video metadata (%@). (Error: %@)"
- "Successfully wrote blob data to: %{public}@"
- "T@\"CPLStatus\",R,N"
- "T@\"NSDate\",N"
- "TB,N,V_shouldOverwriteExistingThemeAlgorithmVersion"
- "TQ,R,N,V_uploadedPhotosCount"
- "TQ,R,N,V_uploadedVideosCount"
- "Tq,N,V_algorithmVersionForEmptyThemeAssignment"
- "Tq,N,V_algorithmVersionForVersionOverwrite"
- "Unable to delete file at path %{public}@ - error: %@"
- "Unexpected error, could not access photo library"
- "[PHAssetExportRequest] Export request processing required for asset %{public}@: %{BOOL}d (metadataOperationLocation=%td, metadataOperationCaption=%td, metadataOperationCaptionAccessibilityDescription=%td, metadataChangeCustomDate=%{private}@, producingNewFilesForExport=%{BOOL}d, options.variant=%td, requiresSloMoFlattening=%{BOOL}d, videoExportPreset=%{public}@, type = %{public}@)"
- "[PHInternalAssetExportRequest] Asset %{public}@ is a screenshot in the HEIC format with an alpha channel. Using PNG as compatible variant insead of JPG"
- "[RM] %{public}@ asset resource request retrying due to error: %@"
- "[RM] %{public}@ media request retrying due to error: %@"
- "_addObservers:authorizationStatus:"
- "_algorithmVersionForEmptyThemeAssignment"
- "_algorithmVersionForVersionOverwrite"
- "_cloudStatus"
- "_observerRegistrar"
- "_plObject"
- "_publishCloudStatusChangeWithDebugEvent:"
- "_removeObserver:"
- "_sensitivityAnalysisFromAsset:outError:"
- "_shouldOverwriteExistingThemeAlgorithmVersion"
- "_uploadedPhotosCount"
- "_uploadedVideosCount"
- "addAssetSearchEntityWithLabel:identifier:type:confidence:dateInterval:synonyms:"
- "addSearchRankingWithLabel:identifier:type:rankingScore:synonyms:"
- "algorithmVersionForEmptyThemeAssignment"
- "algorithmVersionForOverwrite"
- "algorithmVersionForVersionOverwrite"
- "assert:code:format:"
- "assetsWithAvalancheUUID:inManagedObjectContext:"
- "assignEmptyTheme"
- "assignEmptyThemeWithAlgorithmVersion:"
- "assignEmptyThemesWithAlgorithmVersion:"
- "assignThemeNamed:algorithmVersion:withConfidence:"
- "assignThemeNamed:withConfidence:"
- "cloudSharedCommentWithGUID:inLibrary:"
- "commenterDisplayName"
- "commenterEmail"
- "commenterFirstName"
- "commenterFullName"
- "commenterLastName"
- "fetchMomentIDsNotAnalyzedForThemesInContext:withAlgorithmVersion:"
- "fetchMomentsNeedingThemeAnalysisWithAlgorithmVersion:options:"
- "fetchMomentsNeedingThemeAnalysisWithOptions:"
- "firstSyncDate"
- "getLivePhotoImageMetadataFromURL:pairingIdentifier:"
- "hasAlphaChannel"
- "hasCloudStatusChanges"
- "initWithCPLStatus:"
- "initWithCloudStatus:library:"
- "initWithMediaTypeCounts:"
- "initWithQuery:oids:registerIfNeeded:usingManagedObjectContext:"
- "initWithQuery:registerIfNeeded:"
- "initWithSceneTaxonomyProvider:csuTaxonomyObjectStore:locale:calendar:indexDateFormatter:delegate:"
- "initWithThemeName:confidence:algorithmVersion:"
- "initWithUUID:photoLibrary:"
- "isHDRScreenshotWithAlphaChannelAsset:withCurrentType:"
- "isOpen"
- "lastSyncDate"
- "redactedDescriptionForPath:"
- "setAlgorithmVersionForEmptyThemeAssignment:"
- "setAlgorithmVersionForVersionOverwrite:"
- "setShouldOverwriteExistingThemeAlgorithmVersion:"
- "setThemeAssignmentsToAlgorithmVersion:"
- "sharedPersistentStoreCoordinator"
- "shouldNotifyAsNotificationWithMediaStreamInfo:asCaptionOnly:"
- "shouldOverwriteExistingThemeAlgorithmVersion"
- "uploadedPhotosCount"
- "uploadedVideosCount"
- "v32@0:8@16^@24"
- "v32@?0q8@\"NSString\"16@\"NSError\"24"
- "v36@0:8B16q20@28"
- "v64@0:8@16@24Q32d40@48@56"
- "video duration"
- "\xa1"
- "\xd1"

```
