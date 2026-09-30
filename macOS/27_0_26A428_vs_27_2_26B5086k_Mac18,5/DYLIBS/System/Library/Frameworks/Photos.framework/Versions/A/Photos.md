## Photos

> `/System/Library/Frameworks/Photos.framework/Versions/A/Photos`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x2efa10
-  __TEXT.__objc_methlist: 0x26024
-  __TEXT.__const: 0x17f8
+916.41.100.0.0
+  __TEXT.__text: 0x2f2680
+  __TEXT.__objc_methlist: 0x2620c
+  __TEXT.__const: 0x17d8
   __TEXT.__dlopen_cstrs: 0x280
   __TEXT.__constg_swiftt: 0x67c
   __TEXT.__swift5_typeref: 0x547

   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x44
   __TEXT.__swift5_capture: 0x198
-  __TEXT.__cstring: 0x327c1
+  __TEXT.__cstring: 0x32ef7
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__oslogstring: 0x22520
+  __TEXT.__oslogstring: 0x22ae6
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x9394
+  __TEXT.__gcc_except_tab: 0x9334
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xb750
+  __TEXT.__unwind_info: 0xb7f8
   __TEXT.__eh_frame: 0x4d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3218
-  __DATA_CONST.__objc_classlist: 0xed0
+  __DATA_CONST.__objc_classlist: 0xee8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13fb8
+  __DATA_CONST.__objc_selrefs: 0x140e8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0xc20
+  __DATA_CONST.__objc_superrefs: 0xc30
   __DATA_CONST.__objc_arraydata: 0x878
-  __DATA_CONST.__got: 0x2878
-  __AUTH_CONST.__const: 0xb648
+  __DATA_CONST.__got: 0x28d0
+  __AUTH_CONST.__const: 0xb678
   __AUTH_CONST.__cfstring: 0x2cc60
-  __AUTH_CONST.__objc_const: 0x40820
+  __AUTH_CONST.__objc_const: 0x40d58
   __AUTH_CONST.__objc_intobj: 0x2490
   __AUTH_CONST.__objc_arrayobj: 0x7c8
   __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x16d8
-  __AUTH.__objc_data: 0x5138
+  __AUTH.__objc_data: 0x5228
   __AUTH.__data: 0x3c0
-  __DATA.__objc_ivar: 0x34a0
+  __DATA.__objc_ivar: 0x34cc
   __DATA.__data: 0x29c0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x49
   __DATA_DIRTY.__objc_data: 0x4300
   __DATA_DIRTY.__data: 0x1a8
-  __DATA_DIRTY.__bss: 0x3c8
+  __DATA_DIRTY.__bss: 0x418
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AudioUnit.framework/Versions/A/AudioUnit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14828
-  Symbols:   33511
-  CStrings:  8689
+  Functions: 14880
+  Symbols:   33639
+  CStrings:  8718
 
Symbols:
+ +[PHAssetResource _publicMediaDerivativeResourcesFromResources:]
+ +[PHCloudFeedEntry fetchEntriesInCollectionShare:filter:earliestDate:options:]
+ +[PHPerson(VisionService) cancelPersonSuggestionsOperationWithId:inPhotoLibrary:]
+ +[PHPhotoLibrary angelPhotoLibrary]
+ +[PHPhotoLibrary setAngelPhotoLibrary:error:]
+ +[PHQuery queryForEntriesInCollectionShare:filter:earliestDate:options:]
+ +[PHShareCommentChangeRequest changeRequestForShareComment:]
+ -[PHAsset fetchProcessedProvenanceReplacementWithOptions:]
+ -[PHAssetCreationRequest _shouldCopyLocationDataFromSourceAsset]
+ -[PHAssetCreationRequestBridge _shouldStashCameraJobs]
+ -[PHAssetCreationRequestBridge _stashBatchCameraJobIfNeeded:]
+ -[PHAssetCreationRequestBridge _stashCameraJobIfNeeded:]
+ -[PHAssetCreationRequestPlaceholderSupport _directUploadShareAssetAfterResourceDownloadInPhotoLibrary:]
+ -[PHAssetExportRequestOptions forceRatingMetadataBaking]
+ -[PHAssetExportRequestOptions setForceRatingMetadataBaking:]
+ -[PHAssetExportRequestOptions setShouldExportTitle:]
+ -[PHAssetExportRequestOptions setShouldStripRating:]
+ -[PHAssetExportRequestOptions shouldExportTitle]
+ -[PHAssetExportRequestOptions shouldStripRating]
+ -[PHImportAsset rating]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator .cxx_destruct]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator _initializeCPLStatus]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator _processCPLStatusDidChange]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator _publishCloudStatusUpdate:]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator _resetCPLStatus]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator _setupLazyCPLStatusIfNecessary]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator _startObservingCloudPauseNotificationIfNecessary]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator _stopObservingCloudPauseNotification]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator dealloc]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator getCloudStatusWithCompletionHandler:]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator initWithPhotoLibrary:]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator invalidate]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator isWalrusEnabled]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator registerObserver:]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator reset]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator statusDidChange:]
+ -[PHPhotoLibraryCloudStatusObserverCoordinator unregisterObserver:]
+ -[PHResourceChooserListResourceInfo isNonRawImage]
+ -[PHResourceRequestReplyGuard deliverOnce:]
+ -[PHResourceRequestReplyGuard hasDelivered]
+ -[PHServerResourceRequestRunner _newProgressWithReplyOnCancellation:]
+ -[PHShareComment isEdited]
+ -[PHShareComment lastEditedDate]
+ -[PHShareCommentChangeRequest .cxx_destruct]
+ -[PHShareCommentChangeRequest applyMutationsToManagedObject:photoLibrary:error:]
+ -[PHShareCommentChangeRequest commentText]
+ -[PHShareCommentChangeRequest encodeToXPCDict:]
+ -[PHShareCommentChangeRequest initWithUUID:objectID:]
+ -[PHShareCommentChangeRequest initWithXPCDict:request:clientAuthorization:]
+ -[PHShareCommentChangeRequest managedEntityName]
+ -[PHShareCommentChangeRequest setCommentText:]
+ -[PHSharePost isEdited]
+ -[PHSharePost lastEditedDate]
+ -[PHSharePostChangeRequest applyMutationsToManagedObject:photoLibrary:error:]
+ GCC_except_table1000
+ GCC_except_table10098
+ GCC_except_table10108
+ GCC_except_table1011
+ GCC_except_table10123
+ GCC_except_table1013
+ GCC_except_table10130
+ GCC_except_table10133
+ GCC_except_table10163
+ GCC_except_table10178
+ GCC_except_table10188
+ GCC_except_table10264
+ GCC_except_table10265
+ GCC_except_table10266
+ GCC_except_table10267
+ GCC_except_table10268
+ GCC_except_table10269
+ GCC_except_table10270
+ GCC_except_table10271
+ GCC_except_table10272
+ GCC_except_table10273
+ GCC_except_table10274
+ GCC_except_table10394
+ GCC_except_table10395
+ GCC_except_table10396
+ GCC_except_table10397
+ GCC_except_table10398
+ GCC_except_table10399
+ GCC_except_table10411
+ GCC_except_table10429
+ GCC_except_table10462
+ GCC_except_table10463
+ GCC_except_table10464
+ GCC_except_table10466
+ GCC_except_table10476
+ GCC_except_table10494
+ GCC_except_table10495
+ GCC_except_table10496
+ GCC_except_table10497
+ GCC_except_table10498
+ GCC_except_table10499
+ GCC_except_table10500
+ GCC_except_table10501
+ GCC_except_table10502
+ GCC_except_table10503
+ GCC_except_table10540
+ GCC_except_table10541
+ GCC_except_table10545
+ GCC_except_table10566
+ GCC_except_table10573
+ GCC_except_table10655
+ GCC_except_table10748
+ GCC_except_table10916
+ GCC_except_table10936
+ GCC_except_table10939
+ GCC_except_table10940
+ GCC_except_table10966
+ GCC_except_table10968
+ GCC_except_table11058
+ GCC_except_table11076
+ GCC_except_table11595
+ GCC_except_table1165
+ GCC_except_table11752
+ GCC_except_table11755
+ GCC_except_table11761
+ GCC_except_table11769
+ GCC_except_table11773
+ GCC_except_table11775
+ GCC_except_table11779
+ GCC_except_table11785
+ GCC_except_table11891
+ GCC_except_table11911
+ GCC_except_table11913
+ GCC_except_table11915
+ GCC_except_table11917
+ GCC_except_table1192
+ GCC_except_table11952
+ GCC_except_table12008
+ GCC_except_table12010
+ GCC_except_table12012
+ GCC_except_table12018
+ GCC_except_table12055
+ GCC_except_table12186
+ GCC_except_table12212
+ GCC_except_table12224
+ GCC_except_table12266
+ GCC_except_table12280
+ GCC_except_table12366
+ GCC_except_table12370
+ GCC_except_table12411
+ GCC_except_table12415
+ GCC_except_table12424
+ GCC_except_table12425
+ GCC_except_table12432
+ GCC_except_table12470
+ GCC_except_table12477
+ GCC_except_table12487
+ GCC_except_table12492
+ GCC_except_table12542
+ GCC_except_table12637
+ GCC_except_table12643
+ GCC_except_table12645
+ GCC_except_table12685
+ GCC_except_table12715
+ GCC_except_table12780
+ GCC_except_table12788
+ GCC_except_table12794
+ GCC_except_table12796
+ GCC_except_table1286
+ GCC_except_table12861
+ GCC_except_table12939
+ GCC_except_table12943
+ GCC_except_table12947
+ GCC_except_table12984
+ GCC_except_table13009
+ GCC_except_table13016
+ GCC_except_table1305
+ GCC_except_table13147
+ GCC_except_table13160
+ GCC_except_table13255
+ GCC_except_table13322
+ GCC_except_table13528
+ GCC_except_table13607
+ GCC_except_table13649
+ GCC_except_table13698
+ GCC_except_table13708
+ GCC_except_table13728
+ GCC_except_table13743
+ GCC_except_table13771
+ GCC_except_table13773
+ GCC_except_table13786
+ GCC_except_table13788
+ GCC_except_table13790
+ GCC_except_table1380
+ GCC_except_table13809
+ GCC_except_table13955
+ GCC_except_table13966
+ GCC_except_table13993
+ GCC_except_table13999
+ GCC_except_table14015
+ GCC_except_table14085
+ GCC_except_table14087
+ GCC_except_table14133
+ GCC_except_table14135
+ GCC_except_table14162
+ GCC_except_table14166
+ GCC_except_table14167
+ GCC_except_table14179
+ GCC_except_table14196
+ GCC_except_table14199
+ GCC_except_table14353
+ GCC_except_table1474
+ GCC_except_table1499
+ GCC_except_table1545
+ GCC_except_table1620
+ GCC_except_table1720
+ GCC_except_table1822
+ GCC_except_table1826
+ GCC_except_table1852
+ GCC_except_table1857
+ GCC_except_table1861
+ GCC_except_table1871
+ GCC_except_table2060
+ GCC_except_table2062
+ GCC_except_table2072
+ GCC_except_table2074
+ GCC_except_table2076
+ GCC_except_table2079
+ GCC_except_table2086
+ GCC_except_table2088
+ GCC_except_table2090
+ GCC_except_table2102
+ GCC_except_table2146
+ GCC_except_table2148
+ GCC_except_table2150
+ GCC_except_table2152
+ GCC_except_table2154
+ GCC_except_table2156
+ GCC_except_table2162
+ GCC_except_table2164
+ GCC_except_table2169
+ GCC_except_table2171
+ GCC_except_table2173
+ GCC_except_table2175
+ GCC_except_table2178
+ GCC_except_table2180
+ GCC_except_table2183
+ GCC_except_table2185
+ GCC_except_table2187
+ GCC_except_table2216
+ GCC_except_table2218
+ GCC_except_table2221
+ GCC_except_table2224
+ GCC_except_table2264
+ GCC_except_table2332
+ GCC_except_table2337
+ GCC_except_table2355
+ GCC_except_table2369
+ GCC_except_table2409
+ GCC_except_table2582
+ GCC_except_table2595
+ GCC_except_table2623
+ GCC_except_table2640
+ GCC_except_table2659
+ GCC_except_table2669
+ GCC_except_table2706
+ GCC_except_table2711
+ GCC_except_table2773
+ GCC_except_table2878
+ GCC_except_table2889
+ GCC_except_table2891
+ GCC_except_table2897
+ GCC_except_table2905
+ GCC_except_table2937
+ GCC_except_table3019
+ GCC_except_table3025
+ GCC_except_table3033
+ GCC_except_table3042
+ GCC_except_table3056
+ GCC_except_table3062
+ GCC_except_table3070
+ GCC_except_table3195
+ GCC_except_table3199
+ GCC_except_table3202
+ GCC_except_table3269
+ GCC_except_table3277
+ GCC_except_table3312
+ GCC_except_table3316
+ GCC_except_table3321
+ GCC_except_table3443
+ GCC_except_table3480
+ GCC_except_table3486
+ GCC_except_table3489
+ GCC_except_table3499
+ GCC_except_table3514
+ GCC_except_table3517
+ GCC_except_table3527
+ GCC_except_table3531
+ GCC_except_table3545
+ GCC_except_table3551
+ GCC_except_table3562
+ GCC_except_table3563
+ GCC_except_table3580
+ GCC_except_table3589
+ GCC_except_table3686
+ GCC_except_table3714
+ GCC_except_table3716
+ GCC_except_table3718
+ GCC_except_table3765
+ GCC_except_table3793
+ GCC_except_table3824
+ GCC_except_table3844
+ GCC_except_table3846
+ GCC_except_table3849
+ GCC_except_table4009
+ GCC_except_table4043
+ GCC_except_table4051
+ GCC_except_table4053
+ GCC_except_table4068
+ GCC_except_table4071
+ GCC_except_table4073
+ GCC_except_table4106
+ GCC_except_table4111
+ GCC_except_table4112
+ GCC_except_table4379
+ GCC_except_table4386
+ GCC_except_table4419
+ GCC_except_table4441
+ GCC_except_table4444
+ GCC_except_table4449
+ GCC_except_table4454
+ GCC_except_table4465
+ GCC_except_table4469
+ GCC_except_table4491
+ GCC_except_table4504
+ GCC_except_table4505
+ GCC_except_table4565
+ GCC_except_table4890
+ GCC_except_table4900
+ GCC_except_table4963
+ GCC_except_table4967
+ GCC_except_table4969
+ GCC_except_table4972
+ GCC_except_table5042
+ GCC_except_table5047
+ GCC_except_table5079
+ GCC_except_table5209
+ GCC_except_table5213
+ GCC_except_table5560
+ GCC_except_table5592
+ GCC_except_table5638
+ GCC_except_table5664
+ GCC_except_table5697
+ GCC_except_table5702
+ GCC_except_table5726
+ GCC_except_table5730
+ GCC_except_table5734
+ GCC_except_table5764
+ GCC_except_table5778
+ GCC_except_table5781
+ GCC_except_table5784
+ GCC_except_table5807
+ GCC_except_table5858
+ GCC_except_table5869
+ GCC_except_table5911
+ GCC_except_table5946
+ GCC_except_table5952
+ GCC_except_table5956
+ GCC_except_table5967
+ GCC_except_table5998
+ GCC_except_table6027
+ GCC_except_table6054
+ GCC_except_table6056
+ GCC_except_table6069
+ GCC_except_table6139
+ GCC_except_table6217
+ GCC_except_table6222
+ GCC_except_table6227
+ GCC_except_table6385
+ GCC_except_table6390
+ GCC_except_table6404
+ GCC_except_table6429
+ GCC_except_table6439
+ GCC_except_table6442
+ GCC_except_table6481
+ GCC_except_table6518
+ GCC_except_table6520
+ GCC_except_table6920
+ GCC_except_table6940
+ GCC_except_table6953
+ GCC_except_table6966
+ GCC_except_table6985
+ GCC_except_table7016
+ GCC_except_table7019
+ GCC_except_table7021
+ GCC_except_table7023
+ GCC_except_table7025
+ GCC_except_table7034
+ GCC_except_table7082
+ GCC_except_table7096
+ GCC_except_table710
+ GCC_except_table711
+ GCC_except_table712
+ GCC_except_table713
+ GCC_except_table7134
+ GCC_except_table7136
+ GCC_except_table714
+ GCC_except_table716
+ GCC_except_table7175
+ GCC_except_table7428
+ GCC_except_table7431
+ GCC_except_table7453
+ GCC_except_table7460
+ GCC_except_table7482
+ GCC_except_table7483
+ GCC_except_table7484
+ GCC_except_table7485
+ GCC_except_table7486
+ GCC_except_table7487
+ GCC_except_table7498
+ GCC_except_table7499
+ GCC_except_table7500
+ GCC_except_table7657
+ GCC_except_table7877
+ GCC_except_table7922
+ GCC_except_table794
+ GCC_except_table7940
+ GCC_except_table7941
+ GCC_except_table8000
+ GCC_except_table8025
+ GCC_except_table8029
+ GCC_except_table8036
+ GCC_except_table805
+ GCC_except_table8090
+ GCC_except_table8296
+ GCC_except_table8298
+ GCC_except_table8345
+ GCC_except_table8389
+ GCC_except_table8391
+ GCC_except_table8393
+ GCC_except_table8405
+ GCC_except_table8410
+ GCC_except_table8450
+ GCC_except_table8478
+ GCC_except_table8520
+ GCC_except_table8604
+ GCC_except_table8662
+ GCC_except_table8683
+ GCC_except_table8686
+ GCC_except_table8705
+ GCC_except_table8764
+ GCC_except_table8776
+ GCC_except_table8777
+ GCC_except_table8778
+ GCC_except_table8780
+ GCC_except_table8782
+ GCC_except_table8784
+ GCC_except_table8788
+ GCC_except_table8799
+ GCC_except_table8802
+ GCC_except_table8827
+ GCC_except_table8875
+ GCC_except_table8942
+ GCC_except_table909
+ GCC_except_table9099
+ GCC_except_table9140
+ GCC_except_table9146
+ GCC_except_table9149
+ GCC_except_table9412
+ GCC_except_table9416
+ GCC_except_table9420
+ GCC_except_table9444
+ GCC_except_table9445
+ GCC_except_table9543
+ GCC_except_table9553
+ GCC_except_table9586
+ GCC_except_table9638
+ GCC_except_table965
+ GCC_except_table9683
+ GCC_except_table9703
+ GCC_except_table9731
+ GCC_except_table9759
+ GCC_except_table9792
+ GCC_except_table9794
+ GCC_except_table9885
+ GCC_except_table996
+ GCC_except_table9976
+ OBJC_IVAR_$_PHAssetExportRequestOptions._forceRatingMetadataBaking
+ OBJC_IVAR_$_PHAssetExportRequestOptions._shouldExportTitle
+ OBJC_IVAR_$_PHAssetExportRequestOptions._shouldStripRating
+ OBJC_IVAR_$_PHPhotoLibrary._cloudStatusObserverCoordinator
+ OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._cloudStatusHandlerQueue
+ OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._cplStatusDelegateQueue
+ OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._lazyCPLStatus
+ OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._observerRegistrar
+ OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._pauseLock
+ OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._pauseLock_isObservingCloudPauseNotification
+ OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._photoLibrary
+ OBJC_IVAR_$_PHResourceRequestReplyGuard._delivered
+ OBJC_IVAR_$_PHServerResourceRequestRunner._replyGuard
+ OBJC_IVAR_$_PHShareComment._lastEditedDate
+ OBJC_IVAR_$_PHShareCommentChangeRequest._commentText
+ OBJC_IVAR_$_PHShareCommentChangeRequest._didSetCommentText
+ OBJC_IVAR_$_PHSharePost._lastEditedDate
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveObserver
+ _OBJC_CLASS_$_PHPhotoLibraryCloudStatusObserverCoordinator
+ _OBJC_CLASS_$_PHResourceRequestReplyGuard
+ _OBJC_CLASS_$_PHShareCommentChangeRequest
+ _OBJC_METACLASS_$_PHPhotoLibraryCloudStatusObserverCoordinator
+ _OBJC_METACLASS_$_PHResourceRequestReplyGuard
+ _OBJC_METACLASS_$_PHShareCommentChangeRequest
+ _PHAssetExportRequestStarRatingMetadataOperationForAssetWithOptions
+ _PHAssetExportRequestTitleMetadataOperationForAssetWithOptions
+ _PHAssetOriginalStarRatingForAsset
+ _PHAssetOriginalTitleForAsset
+ _PLCloudPhotoLibraryPauseDidChangeNotification
+ __103-[PHAssetCreationRequestPlaceholderSupport _directUploadShareAssetAfterResourceDownloadInPhotoLibrary:]_block_invoke
+ __69-[PHPhotoLibraryCloudStatusObserverCoordinator initWithPhotoLibrary:]_block_invoke
+ __74-[PHPhotoLibraryCloudStatusObserverCoordinator _publishCloudStatusUpdate:]_block_invoke
+ __84-[PHPhotoLibraryCloudStatusObserverCoordinator getCloudStatusWithCompletionHandler:]_block_invoke
+ __84-[PHPhotoLibraryCloudStatusObserverCoordinator getCloudStatusWithCompletionHandler:]_block_invoke_2
+ __OBJC_$_CLASS_METHODS_PHShareCommentChangeRequest
+ __OBJC_$_CLASS_PROP_LIST_PHShareCommentChangeRequest
+ __OBJC_$_INSTANCE_METHODS_PHPhotoLibraryCloudStatusObserverCoordinator
+ __OBJC_$_INSTANCE_METHODS_PHResourceRequestReplyGuard
+ __OBJC_$_INSTANCE_METHODS_PHShareCommentChangeRequest
+ __OBJC_$_INSTANCE_VARIABLES_PHPhotoLibraryCloudStatusObserverCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_PHResourceRequestReplyGuard
+ __OBJC_$_INSTANCE_VARIABLES_PHShareCommentChangeRequest
+ __OBJC_$_PROP_LIST_PHPhotoLibraryCloudStatusObserverCoordinator
+ __OBJC_$_PROP_LIST_PHResourceRequestReplyGuard
+ __OBJC_$_PROP_LIST_PHShareCommentChangeRequest
+ __OBJC_CLASS_PROTOCOLS_$_PHPhotoLibraryCloudStatusObserverCoordinator
+ __OBJC_CLASS_PROTOCOLS_$_PHShareCommentChangeRequest
+ __OBJC_CLASS_RO_$_PHPhotoLibraryCloudStatusObserverCoordinator
+ __OBJC_CLASS_RO_$_PHResourceRequestReplyGuard
+ __OBJC_CLASS_RO_$_PHShareCommentChangeRequest
+ __OBJC_METACLASS_RO_$_PHPhotoLibraryCloudStatusObserverCoordinator
+ __OBJC_METACLASS_RO_$_PHResourceRequestReplyGuard
+ __OBJC_METACLASS_RO_$_PHShareCommentChangeRequest
+ __PLSafeEntityForNameInManagedObjectContext
+ ___103-[PHAssetCreationRequestPlaceholderSupport _directUploadShareAssetAfterResourceDownloadInPhotoLibrary:]_block_invoke
+ ___103-[PHAssetCreationRequestPlaceholderSupport _directUploadShareAssetAfterResourceDownloadInPhotoLibrary:]_block_invoke_2
+ ___142-[PHCloudSharedAssetExportRequest _requestFileURLsForAsset:withOptions:networkAccessAllowed:progressHandler:resultHandler:resultHandlerQueue:]_block_invoke
+ ___23-[PHImportAsset rating]_block_invoke
+ ___35+[PHPhotoLibrary angelPhotoLibrary]_block_invoke
+ ___45+[PHPhotoLibrary setAngelPhotoLibrary:error:]_block_invoke
+ ___53-[PHPhotoLibraryCloudStatusObserverCoordinator reset]_block_invoke
+ ___53-[PHPhotoLibraryCloudStatusObserverCoordinator reset]_block_invoke_2
+ ___58-[PHPhotoLibraryCloudStatusObserverCoordinator invalidate]_block_invoke
+ ___65-[PHPhotoLibraryCloudStatusObserverCoordinator registerObserver:]_block_invoke
+ ___69-[PHPhotoLibraryCloudStatusObserverCoordinator initWithPhotoLibrary:]_block_invoke
+ ___69-[PHServerResourceRequestRunner _newProgressWithReplyOnCancellation:]_block_invoke
+ ___74-[PHPhotoLibraryCloudStatusObserverCoordinator _processCPLStatusDidChange]_block_invoke
+ ___74-[PHPhotoLibraryCloudStatusObserverCoordinator _publishCloudStatusUpdate:]_block_invoke
+ ___78+[PHCloudFeedEntry fetchEntriesInCollectionShare:filter:earliestDate:options:]_block_invoke
+ ___84-[PHPhotoLibraryCloudStatusObserverCoordinator _stopObservingCloudPauseNotification]_block_invoke
+ ___84-[PHPhotoLibraryCloudStatusObserverCoordinator getCloudStatusWithCompletionHandler:]_block_invoke
+ ___84-[PHPhotoLibraryCloudStatusObserverCoordinator getCloudStatusWithCompletionHandler:]_block_invoke_2
+ ___84-[PHPhotoLibraryCloudStatusObserverCoordinator getCloudStatusWithCompletionHandler:]_block_invoke_3
+ ___96-[PHPhotoLibraryCloudStatusObserverCoordinator _startObservingCloudPauseNotificationIfNecessary]_block_invoke
+ ___block_descriptor_40_e8_32w_e39_v24?0"PLCPLClientStatus"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e39_v24?0"PLCPLClientStatus"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s56r_e17_v16?0"NSError"8l
+ __cloudPauseDidChange
+ _angelPhotoLibrary
+ _angelPhotoLibraryLock
+ _kPLImageWriterBatchImageDictionaries
+ _kPLImageWriterDestinationAssetUUID
+ _kPLImageWriterJobCompletionBlock
+ _kPLImageWriterJobTypeBatchImage
+ _kPLImageWriterPhotoDestinationPath
+ _kPLImageWriterPhotoIrisAssetUUID
+ _kPLImageWriterPreviewImageRef
+ _kPLImageWriterReplayedCameraJob
+ _kPLImageWriterVideoDestinationPath
+ _objc_msgSend$_directUploadShareAssetAfterResourceDownloadInPhotoLibrary:
+ _objc_msgSend$_newProgressWithReplyOnCancellation:
+ _objc_msgSend$_publicMediaDerivativeResourcesFromResources:
+ _objc_msgSend$_resetCPLStatus
+ _objc_msgSend$_shouldCopyLocationDataFromSourceAsset
+ _objc_msgSend$_shouldStashCameraJobs
+ _objc_msgSend$_startObservingCloudPauseNotificationIfNecessary
+ _objc_msgSend$_stashBatchCameraJobIfNeeded:
+ _objc_msgSend$_stashCameraJobIfNeeded:
+ _objc_msgSend$_stopObservingCloudPauseNotification
+ _objc_msgSend$addOwnerWritePermissionIfNecessaryToFileAtPath:
+ _objc_msgSend$cancelVisionOperationWithId:
+ _objc_msgSend$conformsToImage
+ _objc_msgSend$conformsToRawImage
+ _objc_msgSend$copyJobContentsToHoldingDirectoryWithUUID:incomingPath:job:
+ _objc_msgSend$deliverOnce:
+ _objc_msgSend$fetchProcessedProvenanceAssetWithOriginatingAssetIdentifier:options:
+ _objc_msgSend$forceRatingMetadataBaking
+ _objc_msgSend$hasDelivered
+ _objc_msgSend$initWithScopeIdentifier:identifier:
+ _objc_msgSend$isNonRawImage
+ _objc_msgSend$isPlaceholderAsset
+ _objc_msgSend$lastEditedDate
+ _objc_msgSend$predicateForPostsFromOthersCreatedAfterSubscriptionSinceDate:
+ _objc_msgSend$queryForEntriesInCollectionShare:filter:earliestDate:options:
+ _objc_msgSend$registerObserver:
+ _objc_msgSend$representsNonRawImage
+ _objc_msgSend$setCustomStarRating:
+ _objc_msgSend$setShouldStripRating:
+ _objc_msgSend$setShouldStripTitle:
+ _objc_msgSend$setStarRating:
+ _objc_msgSend$setStarRatingMetadataBehavior:withStarRating:
+ _objc_msgSend$setTitleMetadataBehavior:withTitle:
+ _objc_msgSend$setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyLocationData:copyProvenanceData:isCurrentUser:library:
+ _objc_msgSend$sharePost
+ _objc_msgSend$shouldExportTitle
+ _objc_msgSend$shouldStripRating
+ _objc_msgSend$shouldStripTitle
+ _objc_msgSend$starRating
+ _objc_msgSend$stringRepresentation
+ _objc_msgSend$unregisterObserver:
+ _objc_msgSend$updateCaption:
+ _objc_msgSend$updateCommentText:
+ _objc_msgSend$wasInvalidated
+ allowedEntities.pl_once_object_74
+ allowedEntities.pl_once_object_75
+ allowedEntities.pl_once_token_74
+ allowedEntities.pl_once_token_75
+ sharedLazyPhotoLibraryForCMM.pl_once_object_44
+ sharedLazyPhotoLibraryForCMM.pl_once_token_44
+ uniqueObjectIDCache.pl_once_object_73
+ uniqueObjectIDCache.pl_once_token_73
- +[PHCloudFeedEntry fetchEntriesInCollectionShare:filter:options:]
- +[PHPhotoLibrary imagePickerPhotoLibrary]
- +[PHPhotoLibrary setImagePickerPhotoLibrary:error:]
- +[PHQuery queryForEntriesInCollectionShare:filter:options:]
- -[PHPhotoLibrary _addCloudStatusObservers:authorizationStatus:]
- -[PHPhotoLibrary _cachedCloudStatus]
- -[PHPhotoLibrary _initializeCPLStatus]
- -[PHPhotoLibrary _processCPLStatusDidChange]
- -[PHPhotoLibrary _publishCloudStatusUpdate:]
- -[PHPhotoLibrary _removeCloudStatusObserver:]
- -[PHPhotoLibrary _setCachedCloudStatus:]
- -[PHPhotoLibrary _setupLazyCPLStatusIfNecessary]
- -[PHPhotoLibrary statusDidChange:]
- -[PHServerResourceRequestRunner _safeReply:]
- -[PHSharePost lastModifiedDate]
- GCC_except_table10087
- GCC_except_table10097
- GCC_except_table10111
- GCC_except_table10112
- GCC_except_table10119
- GCC_except_table10145
- GCC_except_table10146
- GCC_except_table10147
- GCC_except_table10148
- GCC_except_table10149
- GCC_except_table10150
- GCC_except_table10151
- GCC_except_table10152
- GCC_except_table10155
- GCC_except_table10164
- GCC_except_table10165
- GCC_except_table10174
- GCC_except_table10189
- GCC_except_table10199
- GCC_except_table10374
- GCC_except_table10383
- GCC_except_table10384
- GCC_except_table10386
- GCC_except_table10387
- GCC_except_table10388
- GCC_except_table10389
- GCC_except_table10418
- GCC_except_table10451
- GCC_except_table10452
- GCC_except_table10453
- GCC_except_table10454
- GCC_except_table10455
- GCC_except_table10483
- GCC_except_table10484
- GCC_except_table10485
- GCC_except_table10486
- GCC_except_table10487
- GCC_except_table10488
- GCC_except_table10489
- GCC_except_table10490
- GCC_except_table10491
- GCC_except_table10492
- GCC_except_table10529
- GCC_except_table10530
- GCC_except_table10534
- GCC_except_table10554
- GCC_except_table10561
- GCC_except_table10643
- GCC_except_table10736
- GCC_except_table10904
- GCC_except_table10924
- GCC_except_table10927
- GCC_except_table10928
- GCC_except_table10954
- GCC_except_table10956
- GCC_except_table11046
- GCC_except_table11064
- GCC_except_table1129
- GCC_except_table11583
- GCC_except_table1174
- GCC_except_table11740
- GCC_except_table11743
- GCC_except_table11750
- GCC_except_table11758
- GCC_except_table11762
- GCC_except_table11764
- GCC_except_table11768
- GCC_except_table11774
- GCC_except_table11880
- GCC_except_table11900
- GCC_except_table11902
- GCC_except_table11904
- GCC_except_table11906
- GCC_except_table11941
- GCC_except_table11990
- GCC_except_table11997
- GCC_except_table11999
- GCC_except_table12007
- GCC_except_table12044
- GCC_except_table12175
- GCC_except_table12201
- GCC_except_table12213
- GCC_except_table12255
- GCC_except_table12269
- GCC_except_table12355
- GCC_except_table12359
- GCC_except_table12400
- GCC_except_table12404
- GCC_except_table12413
- GCC_except_table12414
- GCC_except_table12421
- GCC_except_table12459
- GCC_except_table12466
- GCC_except_table12476
- GCC_except_table12481
- GCC_except_table12531
- GCC_except_table12623
- GCC_except_table12626
- GCC_except_table12632
- GCC_except_table12674
- GCC_except_table1268
- GCC_except_table12693
- GCC_except_table12766
- GCC_except_table12769
- GCC_except_table12783
- GCC_except_table12785
- GCC_except_table12850
- GCC_except_table1287
- GCC_except_table12928
- GCC_except_table12932
- GCC_except_table12936
- GCC_except_table12973
- GCC_except_table12997
- GCC_except_table13004
- GCC_except_table13134
- GCC_except_table13146
- GCC_except_table13241
- GCC_except_table13308
- GCC_except_table13514
- GCC_except_table13593
- GCC_except_table1362
- GCC_except_table13635
- GCC_except_table13684
- GCC_except_table13694
- GCC_except_table13714
- GCC_except_table13729
- GCC_except_table13757
- GCC_except_table13759
- GCC_except_table13772
- GCC_except_table13774
- GCC_except_table13776
- GCC_except_table13795
- GCC_except_table13941
- GCC_except_table13952
- GCC_except_table13979
- GCC_except_table13985
- GCC_except_table14001
- GCC_except_table14071
- GCC_except_table14073
- GCC_except_table14119
- GCC_except_table14121
- GCC_except_table14145
- GCC_except_table14148
- GCC_except_table14302
- GCC_except_table1456
- GCC_except_table1481
- GCC_except_table1527
- GCC_except_table1602
- GCC_except_table1702
- GCC_except_table1804
- GCC_except_table1808
- GCC_except_table1834
- GCC_except_table1839
- GCC_except_table1843
- GCC_except_table1853
- GCC_except_table2042
- GCC_except_table2046
- GCC_except_table2048
- GCC_except_table2050
- GCC_except_table2052
- GCC_except_table2054
- GCC_except_table2056
- GCC_except_table2059
- GCC_except_table2082
- GCC_except_table2114
- GCC_except_table2116
- GCC_except_table2118
- GCC_except_table2120
- GCC_except_table2122
- GCC_except_table2124
- GCC_except_table2126
- GCC_except_table2128
- GCC_except_table2130
- GCC_except_table2132
- GCC_except_table2147
- GCC_except_table2149
- GCC_except_table2151
- GCC_except_table2153
- GCC_except_table2155
- GCC_except_table2163
- GCC_except_table2165
- GCC_except_table2196
- GCC_except_table2198
- GCC_except_table2201
- GCC_except_table2204
- GCC_except_table2244
- GCC_except_table2312
- GCC_except_table2317
- GCC_except_table2331
- GCC_except_table2345
- GCC_except_table2385
- GCC_except_table2558
- GCC_except_table2571
- GCC_except_table2599
- GCC_except_table2616
- GCC_except_table2635
- GCC_except_table2645
- GCC_except_table2682
- GCC_except_table2687
- GCC_except_table2749
- GCC_except_table2854
- GCC_except_table2865
- GCC_except_table2867
- GCC_except_table2873
- GCC_except_table2881
- GCC_except_table2913
- GCC_except_table2993
- GCC_except_table2999
- GCC_except_table3004
- GCC_except_table3007
- GCC_except_table3017
- GCC_except_table3030
- GCC_except_table3032
- GCC_except_table3039
- GCC_except_table3169
- GCC_except_table3173
- GCC_except_table3176
- GCC_except_table3243
- GCC_except_table3251
- GCC_except_table3286
- GCC_except_table3290
- GCC_except_table3295
- GCC_except_table3419
- GCC_except_table3456
- GCC_except_table3462
- GCC_except_table3465
- GCC_except_table3475
- GCC_except_table3479
- GCC_except_table3490
- GCC_except_table3493
- GCC_except_table3507
- GCC_except_table3521
- GCC_except_table3528
- GCC_except_table3539
- GCC_except_table3540
- GCC_except_table3557
- GCC_except_table3566
- GCC_except_table3663
- GCC_except_table3670
- GCC_except_table3691
- GCC_except_table3695
- GCC_except_table3742
- GCC_except_table3770
- GCC_except_table3801
- GCC_except_table3803
- GCC_except_table3821
- GCC_except_table3823
- GCC_except_table3986
- GCC_except_table4020
- GCC_except_table4028
- GCC_except_table4030
- GCC_except_table4045
- GCC_except_table4048
- GCC_except_table4050
- GCC_except_table4083
- GCC_except_table4088
- GCC_except_table4089
- GCC_except_table4356
- GCC_except_table4363
- GCC_except_table4396
- GCC_except_table4418
- GCC_except_table4421
- GCC_except_table4426
- GCC_except_table4431
- GCC_except_table4442
- GCC_except_table4446
- GCC_except_table4467
- GCC_except_table4480
- GCC_except_table4481
- GCC_except_table4541
- GCC_except_table4866
- GCC_except_table4876
- GCC_except_table4936
- GCC_except_table4940
- GCC_except_table4942
- GCC_except_table4945
- GCC_except_table5015
- GCC_except_table5020
- GCC_except_table5053
- GCC_except_table5183
- GCC_except_table5187
- GCC_except_table5534
- GCC_except_table5565
- GCC_except_table5611
- GCC_except_table5637
- GCC_except_table5670
- GCC_except_table5675
- GCC_except_table5699
- GCC_except_table5703
- GCC_except_table5707
- GCC_except_table5729
- GCC_except_table5735
- GCC_except_table5739
- GCC_except_table5753
- GCC_except_table5759
- GCC_except_table5782
- GCC_except_table5817
- GCC_except_table5838
- GCC_except_table5849
- GCC_except_table5888
- GCC_except_table5900
- GCC_except_table5934
- GCC_except_table5937
- GCC_except_table5947
- GCC_except_table5959
- GCC_except_table5992
- GCC_except_table6021
- GCC_except_table6048
- GCC_except_table6050
- GCC_except_table6063
- GCC_except_table6132
- GCC_except_table6210
- GCC_except_table6215
- GCC_except_table6220
- GCC_except_table6378
- GCC_except_table6383
- GCC_except_table6396
- GCC_except_table6421
- GCC_except_table6431
- GCC_except_table6434
- GCC_except_table6473
- GCC_except_table6510
- GCC_except_table6512
- GCC_except_table6912
- GCC_except_table6932
- GCC_except_table6945
- GCC_except_table6958
- GCC_except_table6977
- GCC_except_table698
- GCC_except_table7008
- GCC_except_table701
- GCC_except_table7011
- GCC_except_table7013
- GCC_except_table7015
- GCC_except_table7017
- GCC_except_table702
- GCC_except_table7026
- GCC_except_table703
- GCC_except_table704
- GCC_except_table705
- GCC_except_table7074
- GCC_except_table7088
- GCC_except_table7126
- GCC_except_table7128
- GCC_except_table7167
- GCC_except_table7420
- GCC_except_table7423
- GCC_except_table7445
- GCC_except_table7452
- GCC_except_table7470
- GCC_except_table7474
- GCC_except_table7475
- GCC_except_table7476
- GCC_except_table7477
- GCC_except_table7479
- GCC_except_table7490
- GCC_except_table7491
- GCC_except_table7492
- GCC_except_table7649
- GCC_except_table785
- GCC_except_table7869
- GCC_except_table7914
- GCC_except_table7932
- GCC_except_table7933
- GCC_except_table796
- GCC_except_table7992
- GCC_except_table8017
- GCC_except_table8021
- GCC_except_table8028
- GCC_except_table8082
- GCC_except_table8288
- GCC_except_table8290
- GCC_except_table8337
- GCC_except_table8377
- GCC_except_table8381
- GCC_except_table8383
- GCC_except_table8397
- GCC_except_table8402
- GCC_except_table8442
- GCC_except_table8470
- GCC_except_table8512
- GCC_except_table8595
- GCC_except_table8653
- GCC_except_table8674
- GCC_except_table8677
- GCC_except_table8696
- GCC_except_table8755
- GCC_except_table8761
- GCC_except_table8767
- GCC_except_table8768
- GCC_except_table8769
- GCC_except_table8771
- GCC_except_table8773
- GCC_except_table8775
- GCC_except_table8790
- GCC_except_table8793
- GCC_except_table8818
- GCC_except_table8866
- GCC_except_table8931
- GCC_except_table894
- GCC_except_table9088
- GCC_except_table9129
- GCC_except_table9135
- GCC_except_table9138
- GCC_except_table9401
- GCC_except_table9405
- GCC_except_table9409
- GCC_except_table9433
- GCC_except_table9434
- GCC_except_table949
- GCC_except_table9532
- GCC_except_table9542
- GCC_except_table9575
- GCC_except_table9627
- GCC_except_table9672
- GCC_except_table9692
- GCC_except_table9720
- GCC_except_table9748
- GCC_except_table978
- GCC_except_table9781
- GCC_except_table9783
- GCC_except_table982
- GCC_except_table9874
- GCC_except_table993
- GCC_except_table995
- GCC_except_table9965
- OBJC_IVAR_$_PHPhotoLibrary._cachedCloudStatus
- OBJC_IVAR_$_PHPhotoLibrary._cloudStatusHandlerQueue
- OBJC_IVAR_$_PHPhotoLibrary._cloudStatusObserverRegistrar
- OBJC_IVAR_$_PHPhotoLibrary._cplStatusDelegateQueue
- OBJC_IVAR_$_PHPhotoLibrary._lazyCPLStatus
- OBJC_IVAR_$_PHSharePost._lastModifiedDate
- _NSFilePosixPermissions
- _PHIsImageAssetResourceType
- _PHIsVideoAssetResourceType
- _PLGatekeeperXPCGetLog
- _PLIsCamera
- _PLIsSharedCollectionsFeatureEnabled
- _PLSafeEntityForNameInManagedObjectContext
- __44-[PHPhotoLibrary _processCPLStatusDidChange]_block_invoke
- __50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_7
- __50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_8
- ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke_3
- ___151-[PHAssetExportRequest _processResourcesAtFileURLs:forAsset:withOptions:progress:processingUnitCount:replacementLivePhotoPairingIdentifier:completion:]_block_invoke_4
- ___151-[PHAssetExportRequest _processResourcesAtFileURLs:forAsset:withOptions:progress:processingUnitCount:replacementLivePhotoPairingIdentifier:completion:]_block_invoke_5
- ___151-[PHAssetExportRequest _processResourcesAtFileURLs:forAsset:withOptions:progress:processingUnitCount:replacementLivePhotoPairingIdentifier:completion:]_block_invoke_6
- ___151-[PHAssetExportRequest _processResourcesAtFileURLs:forAsset:withOptions:progress:processingUnitCount:replacementLivePhotoPairingIdentifier:completion:]_block_invoke_7
- ___36-[PHPhotoLibrary _resetCachedValues]_block_invoke
- ___36-[PHPhotoLibrary _resetCachedValues]_block_invoke_2
- ___36-[PHPhotoLibrary _resetCachedValues]_block_invoke_3
- ___41+[PHPhotoLibrary imagePickerPhotoLibrary]_block_invoke
- ___44-[PHPhotoLibrary _processCPLStatusDidChange]_block_invoke
- ___44-[PHPhotoLibrary _publishCloudStatusUpdate:]_block_invoke
- ___46-[PHPhotoLibrary registerCloudStatusObserver:]_block_invoke
- ___50-[PHPhotoLibrary _invalidateEverythingWithReason:]_block_invoke_2
- ___51+[PHPhotoLibrary setImagePickerPhotoLibrary:error:]_block_invoke
- ___54-[PHPhotoLibrary getCloudStatusWithCompletionHandler:]_block_invoke
- ___54-[PHPhotoLibrary getCloudStatusWithCompletionHandler:]_block_invoke_2
- ___65+[PHCloudFeedEntry fetchEntriesInCollectionShare:filter:options:]_block_invoke
- ___85-[PHServerResourceRequestRunner chooseVideoWithRequest:library:clientBundleID:reply:]_block_invoke_3
- ___95-[PHServerResourceRequestRunner makeResourceAvailableWithRequest:library:clientBundleID:reply:]_block_invoke_2
- ___block_descriptor_48_e8_32bs40w_e39_v24?0"PLCPLClientStatus"8"NSError"16l
- ___block_descriptor_48_e8_32s40w_e39_v24?0"PLCPLClientStatus"8"NSError"16l
- _imagePickerPhotoLibrary
- _imagePickerPhotoLibraryLock
- _objc_msgSend$_addCloudStatusObservers:authorizationStatus:
- _objc_msgSend$_cachedCloudStatus
- _objc_msgSend$_removeCloudStatusObserver:
- _objc_msgSend$_safeReply:
- _objc_msgSend$_setCachedCloudStatus:
- _objc_msgSend$queryForEntriesInCollectionShare:filter:options:
- _objc_msgSend$setAttributes:ofItemAtPath:error:
- _objc_msgSend$setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyProvenanceData:isCurrentUser:library:
- allowedEntities.pl_once_object_78
- allowedEntities.pl_once_object_79
- allowedEntities.pl_once_token_78
- allowedEntities.pl_once_token_79
- sharedLazyPhotoLibraryForCMM.pl_once_object_46
- sharedLazyPhotoLibraryForCMM.pl_once_token_46
- uniqueObjectIDCache.pl_once_object_77
- uniqueObjectIDCache.pl_once_token_77
CStrings:
+ "%@ %p initWithPhotoLibrary:%p"
+ "%{public}@ %p closing (irreversible), reason: %{public}@ / %ld, deallocating=%d"
+ "%{public}@ %p invalidating everything (irreversible), reason: %{public}@ / %ld, wellKnownIdentifier=%td"
+ "+[PHObject objectIDsMatchingEntityFromObjectIDs:context:]"
+ "+[PHQuery combinedFetchRequestForQueries:]"
+ "-[PHAssetCollectionChangeRequest applyMutationsToManagedObject:photoLibrary:error:]"
+ "-[PHAssetCreationRequestPlaceholderSupport _directUploadShareAssetAfterResourceDownloadInPhotoLibrary:]_block_invoke"
+ "-[PHChange _propagatePropertyNamesToSubentityNames:moc:]"
+ "-[PHChangeRequestHelper allowMutationToManagedObject:propertyKey:error:]"
+ "-[PHChangeValidationController _prepare]"
+ "-[PHCollectionListChangeRequest applyMutationsToManagedObject:photoLibrary:error:]"
+ "-[PHMemoryChangeRequest applyMutationsToManagedObject:photoLibrary:error:]"
+ "-[PHObjectDeleteValidator initWithEntityName:managedObjectContext:]"
+ "-[PHQuery _createFetchRequestIncludingBasePredicate:]"
+ "-[PHQuery effectivePredicateForPHClass:includingBasePredicate:]"
+ "-[PHSmartAlbumChangeRequest applyMutationsToManagedObject:photoLibrary:error:]"
+ "<%@: %p, variant: \"%@\", livePhotoAsStill: %d, allowRaw: %d, flattenSlomo: %d, stripLocation: %d, stripProvenance: %d, stripCaption: %d, stripAXDescription: %d, stripKeywords: %d, stripRating: %d, exportTitle: %d, assetBundle: %d, disableMetadataCorrections: %d, unmodifiedOriginals: %d>"
+ "Ambient Face"
+ "Asset playback style is unsupported for export."
+ "No PLPhotoLibrary for current queue (wellKnownIdentifier=%td, isSystemPhotoLibrary=%d, mainThread=%d, qos=%@)"
+ "Not direct uploading Share asset %@ after resource download - asset is missing or was not fully copied"
+ "PHAssetExportRequestMetadataOperation PHAssetExportRequestAccessibilityDescriptionMetadataOperationForAssetWithOptions(PHAsset *__strong _Nonnull, PHAssetExportRequestOptions *__strong _Nonnull, PFMetadata *__strong _Nullable, NSString * _Nullable __autoreleasing * _Nullable)"
+ "PHAssetExportRequestMetadataOperation PHAssetExportRequestStarRatingMetadataOperationForAssetWithOptions(PHAsset *__strong _Nonnull, PHAssetExportRequestOptions *__strong _Nonnull, PFMetadata *__strong _Nullable, NSNumber * _Nullable __autoreleasing * _Nullable)"
+ "PHAssetExportRequestMetadataOperation PHAssetExportRequestTitleMetadataOperationForAssetWithOptions(PHAsset *__strong _Nonnull, PHAssetExportRequestOptions *__strong _Nonnull, PFMetadata *__strong _Nullable, NSString * _Nullable __autoreleasing * _Nullable)"
+ "PHFetchResult init with no fetch request; fetchError from %{public}s: %@\n\tself: %@"
+ "PHPhotosErrorCollectionShareNotEnabled"
+ "PHPhotosErrorShareNeedsToRequestAccess"
+ "PhotoKit Ingest Bridge: %{public}@ Unhandled job type %{public}@ for UUID: %{public}@"
+ "PhotoKit Ingest Bridge: Not stashing %{public}@, no asset UUID in job dictionary"
+ "PhotoKit Ingest Bridge: Not stashing burst job, no camera avalanche UUID in job dictionary"
+ "Publish cloud status update: %@"
+ "The angel photo library URL must match the system photo library URL"
+ "[PHAssetExportRequest] Adjusted processed provenance asset %{public}@ missing original or full-size photo URL."
+ "[PHAssetExportRequest] Asset %{public}@ is unprocessed provenance but we are missing the original photo."
+ "[PHAssetExportRequest] Cancelled while processing resources of asset: %{public}@"
+ "[PHAssetExportRequest] Changing state from \"%{public}@\" to \"%{public}@\" for asset: %{public}@"
+ "[PHAssetExportRequest] Error while processing resources of asset %{public}@: %@"
+ "[PHAssetExportRequest] Export request processing required for asset %{public}@: %{BOOL}d (metadataOperationLocation=%{public}@, metadataOperationProvenance=%{public}@, metadataOperationCaption=%{public}@, metadataOperationCaptionAccessibilityDescription=%{public}@, metadataOperationKeywords=%{public}@, metadataOperationStarRating=%{public}@, metadataOperationTitle=%{public}@, metadataChangeCustomDate=%{private}@, livePhotoMetadataFixup=%{BOOL}d producingNewFilesForExport=%{BOOL}d, options.variant=%{public}@, requiresSloMoFlattening=%{BOOL}d, videoExportPreset=%{public}@, type = %{public}@, needsReplacementLivePhotoIdentifier = %{BOOL}d %{public}@"
+ "[PHAssetExportRequest] Low disk space error while processing resources of asset %{public}@: %@"
+ "[PHAssetExportRequest] Performing additional processing of image resource of asset %{public}@"
+ "[PHAssetExportRequest] Performing additional processing of video resource of asset %{public}@"
+ "[PHAssetExportRequest] Performing slomo flattening of video resource of asset %{public}@"
+ "[PHAssetExportRequest] Performing video to GIF conversion of video resource of asset %{public}@"
+ "[PHAssetExportRequest] Processing retrieved file urls for compatibility and/or metadata corrections for asset: %{public}@"
+ "[PHAssetExportRequest] Returning provenanceMetadataOperation: %ld. Asset provenance state: %hi for asset %{public}@"
+ "[PHAssetExportRequest] We processed fileURLs for asset %{public}@: %@.\nRemoving the DNG and remained with these fileURLs to share: %@"
+ "[PHCloudSharedAssetExportRequest] Unsupported playback style %ld, cannot export asset: %@"
+ "[RM] %{public}@ video request was cancelled before library perform"
+ "_processCPLStatusDidChange nil assetsd client"
+ "lastEditedDate"
+ "live library unavailability"
+ "nil assetsd client"
+ "openAndWaitWithUpgrade short-circuiting on cached open failure %@; this PHPhotoLibrary instance will never reopen"
+ "photoLibraryForCurrentQueueQoS nil (mainThread=%d, qos=%@, invalidated/valid: main=%d/%d userInitiated=%d/%d background=%d/%d)"
+ "previously-recorded bundle nil-library reason"
+ "star rating"
+ "void PHAssetExportRequestPerformMediaConversion(PHMediaFormatConversionSource *__strong, BOOL, BOOL, UTType * _Nullable __strong, PHAssetExportRequestMetadataOperation, CLLocation * _Nullable __strong, NSDate * _Nullable __strong, NSTimeZone * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSArray<NSString *> * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSNumber * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSURL *__strong, NSURL *__strong, NSURL *__strong, NSURL *__strong, BOOL, NSString * _Nullable __strong, NSProgress *__strong, int64_t, NSURL *__strong, BOOL, NSString *__strong, NSString * _Nullable __strong, void (^__strong)(NSURL * _Nullable __strong, NSError * _Nullable __strong))"
+ "void PHAssetExportRequestPerformSlomoFlattening(NSURL *__strong, NSURL *__strong, NSProgress *__strong, int64_t, NSURL *__strong, NSString *__strong, NSString *__strong, NSString *__strong, BOOL, PHAssetExportRequestMetadataOperation, CLLocation * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSArray<NSString *> * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSNumber * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, void (^__strong)(NSURL * _Nullable __strong, NSError * _Nullable __strong))"
- "%@ %p _invalidateEverythingWithReason:%@"
- "%K == nil OR %K >= %K"
- "%K > %@ AND %K.%K == NO"
- "<%@: %p, variant: \"%@\", livePhotoAsStill: %d, allowRaw: %d, flattenSlomo: %d, stripLocation: %d, stripProvenance: %d, stripCaption: %d, stripAXDescription: %d, stripKeywords: %d, assetBundle: %d, disableMetadataCorrections: %d, unmodifiedOriginals: %d>"
- "Cloud status changed: %@"
- "Lemonade"
- "PHAssetExportRequestMetadataOperation PHAssetExportRequestAccessibilityDescriptionMetadataOperationForAssetWithOptions(PHAsset *__strong, PHAssetExportRequestOptions *__strong, PFMetadata *__strong, NSString * _Nullable __autoreleasing * _Nullable)"
- "PHFetchResult init with no fetch request, library not available, setting fetchError to %@\n\tself: %@"
- "PXFeedAssetContainerList"
- "PXFeedAssetsSectionInfo"
- "PXFeedCommentsSectionInfo"
- "PXFeedSubscriptionSectionInfo"
- "PhotoKit Ingest Bridge: Skipping Camera preview image job due to duplicate job from nebulad"
- "The image picker photo library URL must match the system photo library URL"
- "Unable to make read-only imported file writeable with error: %@"
- "Unable to read file attributes at import downloaded file url, error: %@"
- "[PHAssetExportRequest] Adjusted processed provenance asset missing original or full-size photo URL."
- "[PHAssetExportRequest] Asset is unprocessed provenance but we are missing the original photo. "
- "[PHAssetExportRequest] Cancelled while processing resources"
- "[PHAssetExportRequest] Changing state from \"%{public}@\" to \"%{public}@\""
- "[PHAssetExportRequest] Error while processing resources: %@"
- "[PHAssetExportRequest] Export request processing required for asset %{public}@: %{BOOL}d (metadataOperationLocation=%{public}@, metadataOperationProvenance=%{public}@, metadataOperationCaption=%{public}@, metadataOperationCaptionAccessibilityDescription=%{public}@, metadataOperationKeywords=%{public}@, metadataChangeCustomDate=%{private}@, livePhotoMetadataFixup=%{BOOL}d producingNewFilesForExport=%{BOOL}d, options.variant=%{public}@, requiresSloMoFlattening=%{BOOL}d, videoExportPreset=%{public}@, type = %{public}@, needsReplacementLivePhotoIdentifier = %{BOOL}d %{public}@"
- "[PHAssetExportRequest] Low disk space error while processing resources: %@"
- "[PHAssetExportRequest] Processing retrieved file urls for compatibility and/or metadata corrections"
- "[PHAssetExportRequest] Returning provenanceMetadataOperation: %ld. Asset state: %hi"
- "[PHAssetExportRequest] We processed fileURLs %@. Removing the DNG and remained with these fileURLs to share: %@"
- "nil library"
- "void PHAssetExportRequestPerformMediaConversion(PHMediaFormatConversionSource *__strong, BOOL, BOOL, UTType * _Nullable __strong, PHAssetExportRequestMetadataOperation, CLLocation * _Nullable __strong, NSDate * _Nullable __strong, NSTimeZone * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSArray<NSString *> * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSURL *__strong, NSURL *__strong, NSURL *__strong, NSURL *__strong, BOOL, NSString * _Nullable __strong, NSProgress *__strong, int64_t, NSURL *__strong, BOOL, NSString *__strong, NSString * _Nullable __strong, void (^__strong)(NSURL * _Nullable __strong, NSError * _Nullable __strong))"
- "void PHAssetExportRequestPerformSlomoFlattening(NSURL *__strong, NSURL *__strong, NSProgress *__strong, int64_t, NSURL *__strong, NSString *__strong, NSString *__strong, NSString *__strong, BOOL, PHAssetExportRequestMetadataOperation, CLLocation * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSArray<NSString *> * _Nullable __strong, void (^__strong)(NSURL * _Nullable __strong, NSError * _Nullable __strong))"
```
