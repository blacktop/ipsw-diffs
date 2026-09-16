## Photos

> `/System/Library/Frameworks/Photos.framework/Photos`

```diff

-912.0.235.0.0
-  __TEXT.__text: 0x2d484c
-  __TEXT.__objc_methlist: 0x26f6c
-  __TEXT.__const: 0x17e0
+916.40.110.0.0
+  __TEXT.__text: 0x2d73c0
+  __TEXT.__objc_methlist: 0x27154
+  __TEXT.__const: 0x17f0
   __TEXT.__dlopen_cstrs: 0x280
   __TEXT.__constg_swiftt: 0x67c
   __TEXT.__swift5_typeref: 0x547

   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x44
   __TEXT.__swift5_capture: 0x198
-  __TEXT.__cstring: 0x33122
+  __TEXT.__cstring: 0x33883
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__oslogstring: 0x24831
+  __TEXT.__oslogstring: 0x24df7
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x985c
+  __TEXT.__gcc_except_tab: 0x980c
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xba18
+  __TEXT.__unwind_info: 0xbac8
   __TEXT.__eh_frame: 0x4d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x90f0
-  __DATA_CONST.__objc_classlist: 0xf40
+  __DATA_CONST.__const: 0x9118
+  __DATA_CONST.__objc_classlist: 0xf58
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14900
+  __DATA_CONST.__objc_selrefs: 0x14a30
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0xc60
+  __DATA_CONST.__objc_superrefs: 0xc70
   __DATA_CONST.__objc_arraydata: 0x940
-  __DATA_CONST.__got: 0x2a40
+  __DATA_CONST.__got: 0x2a98
   __AUTH_CONST.__const: 0x4778
-  __AUTH_CONST.__cfstring: 0x2da60
-  __AUTH_CONST.__objc_const: 0x42728
+  __AUTH_CONST.__cfstring: 0x2da80
+  __AUTH_CONST.__objc_const: 0x42c60
   __AUTH_CONST.__objc_intobj: 0x24f0
   __AUTH_CONST.__objc_arrayobj: 0x7b0
   __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1918
-  __AUTH.__objc_data: 0x7e38
+  __AUTH_CONST.__auth_got: 0x1920
+  __AUTH.__objc_data: 0x7f28
   __AUTH.__data: 0x3c0
-  __DATA.__objc_ivar: 0x3638
+  __DATA.__objc_ivar: 0x3664
   __DATA.__data: 0x2c18
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0x1a60
   __DATA_DIRTY.__data: 0x148
-  __DATA_DIRTY.__bss: 0x120
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15026
-  Symbols:   34248
-  CStrings:  8957
+  Functions: 15078
+  Symbols:   34378
+  CStrings:  8987
 
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
+ GCC_except_table10037
+ GCC_except_table1009
+ GCC_except_table10128
+ GCC_except_table10260
+ GCC_except_table10274
+ GCC_except_table10282
+ GCC_except_table10285
+ GCC_except_table10331
+ GCC_except_table10417
+ GCC_except_table10418
+ GCC_except_table10419
+ GCC_except_table10420
+ GCC_except_table10421
+ GCC_except_table10422
+ GCC_except_table10423
+ GCC_except_table10424
+ GCC_except_table10425
+ GCC_except_table10426
+ GCC_except_table10546
+ GCC_except_table10547
+ GCC_except_table10548
+ GCC_except_table10549
+ GCC_except_table10550
+ GCC_except_table10551
+ GCC_except_table10552
+ GCC_except_table10563
+ GCC_except_table10581
+ GCC_except_table1061
+ GCC_except_table10614
+ GCC_except_table10615
+ GCC_except_table10616
+ GCC_except_table10617
+ GCC_except_table10628
+ GCC_except_table10646
+ GCC_except_table10647
+ GCC_except_table10648
+ GCC_except_table10649
+ GCC_except_table10650
+ GCC_except_table10651
+ GCC_except_table10652
+ GCC_except_table10653
+ GCC_except_table10654
+ GCC_except_table10655
+ GCC_except_table10692
+ GCC_except_table10693
+ GCC_except_table10697
+ GCC_except_table10717
+ GCC_except_table10722
+ GCC_except_table10804
+ GCC_except_table1088
+ GCC_except_table10897
+ GCC_except_table1092
+ GCC_except_table1101
+ GCC_except_table1103
+ GCC_except_table11065
+ GCC_except_table11084
+ GCC_except_table11087
+ GCC_except_table11088
+ GCC_except_table11114
+ GCC_except_table11116
+ GCC_except_table11206
+ GCC_except_table11234
+ GCC_except_table11768
+ GCC_except_table11925
+ GCC_except_table11928
+ GCC_except_table11934
+ GCC_except_table11942
+ GCC_except_table11946
+ GCC_except_table11948
+ GCC_except_table11952
+ GCC_except_table11958
+ GCC_except_table12064
+ GCC_except_table12084
+ GCC_except_table12086
+ GCC_except_table12088
+ GCC_except_table12090
+ GCC_except_table12125
+ GCC_except_table12181
+ GCC_except_table12183
+ GCC_except_table12185
+ GCC_except_table12191
+ GCC_except_table12228
+ GCC_except_table12359
+ GCC_except_table1237
+ GCC_except_table12385
+ GCC_except_table12397
+ GCC_except_table12439
+ GCC_except_table12441
+ GCC_except_table12454
+ GCC_except_table1253
+ GCC_except_table12559
+ GCC_except_table12563
+ GCC_except_table12604
+ GCC_except_table12608
+ GCC_except_table12617
+ GCC_except_table12618
+ GCC_except_table12625
+ GCC_except_table12663
+ GCC_except_table12670
+ GCC_except_table12682
+ GCC_except_table12687
+ GCC_except_table12737
+ GCC_except_table1280
+ GCC_except_table12832
+ GCC_except_table12838
+ GCC_except_table12840
+ GCC_except_table12880
+ GCC_except_table12910
+ GCC_except_table12975
+ GCC_except_table12983
+ GCC_except_table12989
+ GCC_except_table12991
+ GCC_except_table13056
+ GCC_except_table13134
+ GCC_except_table13138
+ GCC_except_table13142
+ GCC_except_table13179
+ GCC_except_table13204
+ GCC_except_table13211
+ GCC_except_table13351
+ GCC_except_table13364
+ GCC_except_table13458
+ GCC_except_table13525
+ GCC_except_table13731
+ GCC_except_table13810
+ GCC_except_table13852
+ GCC_except_table1389
+ GCC_except_table13901
+ GCC_except_table13911
+ GCC_except_table13931
+ GCC_except_table13946
+ GCC_except_table13974
+ GCC_except_table13976
+ GCC_except_table13989
+ GCC_except_table13991
+ GCC_except_table13993
+ GCC_except_table14012
+ GCC_except_table14158
+ GCC_except_table14169
+ GCC_except_table14196
+ GCC_except_table14202
+ GCC_except_table14218
+ GCC_except_table14288
+ GCC_except_table14290
+ GCC_except_table14336
+ GCC_except_table14338
+ GCC_except_table14365
+ GCC_except_table14369
+ GCC_except_table14370
+ GCC_except_table14382
+ GCC_except_table14399
+ GCC_except_table14402
+ GCC_except_table14556
+ GCC_except_table1478
+ GCC_except_table1570
+ GCC_except_table1595
+ GCC_except_table1641
+ GCC_except_table1716
+ GCC_except_table1814
+ GCC_except_table1915
+ GCC_except_table1919
+ GCC_except_table1939
+ GCC_except_table1944
+ GCC_except_table1948
+ GCC_except_table1958
+ GCC_except_table2149
+ GCC_except_table2153
+ GCC_except_table2155
+ GCC_except_table2157
+ GCC_except_table2159
+ GCC_except_table2161
+ GCC_except_table2163
+ GCC_except_table2166
+ GCC_except_table2173
+ GCC_except_table2175
+ GCC_except_table2177
+ GCC_except_table2189
+ GCC_except_table2221
+ GCC_except_table2223
+ GCC_except_table2225
+ GCC_except_table2227
+ GCC_except_table2229
+ GCC_except_table2231
+ GCC_except_table2233
+ GCC_except_table2245
+ GCC_except_table2247
+ GCC_except_table2249
+ GCC_except_table2254
+ GCC_except_table2256
+ GCC_except_table2258
+ GCC_except_table2260
+ GCC_except_table2262
+ GCC_except_table2265
+ GCC_except_table2267
+ GCC_except_table2270
+ GCC_except_table2272
+ GCC_except_table2274
+ GCC_except_table2303
+ GCC_except_table2305
+ GCC_except_table2308
+ GCC_except_table2311
+ GCC_except_table2351
+ GCC_except_table2419
+ GCC_except_table2424
+ GCC_except_table2439
+ GCC_except_table2451
+ GCC_except_table2489
+ GCC_except_table2660
+ GCC_except_table2673
+ GCC_except_table2701
+ GCC_except_table2716
+ GCC_except_table2735
+ GCC_except_table2745
+ GCC_except_table2782
+ GCC_except_table2787
+ GCC_except_table2849
+ GCC_except_table2952
+ GCC_except_table2963
+ GCC_except_table2965
+ GCC_except_table2971
+ GCC_except_table2979
+ GCC_except_table3011
+ GCC_except_table3089
+ GCC_except_table3094
+ GCC_except_table3102
+ GCC_except_table3111
+ GCC_except_table3123
+ GCC_except_table3129
+ GCC_except_table3134
+ GCC_except_table3257
+ GCC_except_table3261
+ GCC_except_table3264
+ GCC_except_table3331
+ GCC_except_table3339
+ GCC_except_table3374
+ GCC_except_table3378
+ GCC_except_table3383
+ GCC_except_table3511
+ GCC_except_table3548
+ GCC_except_table3554
+ GCC_except_table3557
+ GCC_except_table3567
+ GCC_except_table3571
+ GCC_except_table3577
+ GCC_except_table3580
+ GCC_except_table3585
+ GCC_except_table3589
+ GCC_except_table3600
+ GCC_except_table3605
+ GCC_except_table3616
+ GCC_except_table3617
+ GCC_except_table3634
+ GCC_except_table3643
+ GCC_except_table3740
+ GCC_except_table3767
+ GCC_except_table3769
+ GCC_except_table3771
+ GCC_except_table3818
+ GCC_except_table3846
+ GCC_except_table3877
+ GCC_except_table3879
+ GCC_except_table3897
+ GCC_except_table3899
+ GCC_except_table3902
+ GCC_except_table4065
+ GCC_except_table4099
+ GCC_except_table4107
+ GCC_except_table4109
+ GCC_except_table4124
+ GCC_except_table4127
+ GCC_except_table4129
+ GCC_except_table4162
+ GCC_except_table4167
+ GCC_except_table4168
+ GCC_except_table4435
+ GCC_except_table4442
+ GCC_except_table4472
+ GCC_except_table4496
+ GCC_except_table4503
+ GCC_except_table4508
+ GCC_except_table4519
+ GCC_except_table4545
+ GCC_except_table4558
+ GCC_except_table4559
+ GCC_except_table4619
+ GCC_except_table4944
+ GCC_except_table4954
+ GCC_except_table5016
+ GCC_except_table5018
+ GCC_except_table5022
+ GCC_except_table5024
+ GCC_except_table5027
+ GCC_except_table5097
+ GCC_except_table5102
+ GCC_except_table5132
+ GCC_except_table5262
+ GCC_except_table5266
+ GCC_except_table5614
+ GCC_except_table5646
+ GCC_except_table5692
+ GCC_except_table5717
+ GCC_except_table5723
+ GCC_except_table5735
+ GCC_except_table5768
+ GCC_except_table5771
+ GCC_except_table5773
+ GCC_except_table5789
+ GCC_except_table5793
+ GCC_except_table5802
+ GCC_except_table5806
+ GCC_except_table5845
+ GCC_except_table5878
+ GCC_except_table5883
+ GCC_except_table5907
+ GCC_except_table5915
+ GCC_except_table5937
+ GCC_except_table5945
+ GCC_except_table5959
+ GCC_except_table5962
+ GCC_except_table5965
+ GCC_except_table5988
+ GCC_except_table6038
+ GCC_except_table6047
+ GCC_except_table6089
+ GCC_except_table6121
+ GCC_except_table6124
+ GCC_except_table6130
+ GCC_except_table6134
+ GCC_except_table6145
+ GCC_except_table6176
+ GCC_except_table6205
+ GCC_except_table6232
+ GCC_except_table6234
+ GCC_except_table6248
+ GCC_except_table6318
+ GCC_except_table6396
+ GCC_except_table6401
+ GCC_except_table6406
+ GCC_except_table6564
+ GCC_except_table6567
+ GCC_except_table6581
+ GCC_except_table6606
+ GCC_except_table6616
+ GCC_except_table6619
+ GCC_except_table6658
+ GCC_except_table6695
+ GCC_except_table6697
+ GCC_except_table7097
+ GCC_except_table7117
+ GCC_except_table7130
+ GCC_except_table7143
+ GCC_except_table7162
+ GCC_except_table7196
+ GCC_except_table7198
+ GCC_except_table7200
+ GCC_except_table7202
+ GCC_except_table7211
+ GCC_except_table7259
+ GCC_except_table7273
+ GCC_except_table7311
+ GCC_except_table7313
+ GCC_except_table7352
+ GCC_except_table7605
+ GCC_except_table7608
+ GCC_except_table7637
+ GCC_except_table7655
+ GCC_except_table7656
+ GCC_except_table7657
+ GCC_except_table7658
+ GCC_except_table7659
+ GCC_except_table7660
+ GCC_except_table7671
+ GCC_except_table7672
+ GCC_except_table7673
+ GCC_except_table7830
+ GCC_except_table8049
+ GCC_except_table8094
+ GCC_except_table8112
+ GCC_except_table8113
+ GCC_except_table814
+ GCC_except_table815
+ GCC_except_table816
+ GCC_except_table817
+ GCC_except_table8173
+ GCC_except_table818
+ GCC_except_table8195
+ GCC_except_table820
+ GCC_except_table8206
+ GCC_except_table8260
+ GCC_except_table8460
+ GCC_except_table8462
+ GCC_except_table8509
+ GCC_except_table8549
+ GCC_except_table8553
+ GCC_except_table8555
+ GCC_except_table8557
+ GCC_except_table8569
+ GCC_except_table8574
+ GCC_except_table8614
+ GCC_except_table8642
+ GCC_except_table8684
+ GCC_except_table8777
+ GCC_except_table8835
+ GCC_except_table8855
+ GCC_except_table8858
+ GCC_except_table8877
+ GCC_except_table8945
+ GCC_except_table8946
+ GCC_except_table8947
+ GCC_except_table8950
+ GCC_except_table8952
+ GCC_except_table8956
+ GCC_except_table8967
+ GCC_except_table8970
+ GCC_except_table8991
+ GCC_except_table9035
+ GCC_except_table907
+ GCC_except_table9102
+ GCC_except_table9259
+ GCC_except_table9300
+ GCC_except_table9306
+ GCC_except_table9309
+ GCC_except_table9572
+ GCC_except_table9576
+ GCC_except_table9580
+ GCC_except_table9600
+ GCC_except_table9601
+ GCC_except_table9707
+ GCC_except_table9740
+ GCC_except_table9792
+ GCC_except_table9837
+ GCC_except_table9857
+ GCC_except_table9883
+ GCC_except_table9911
+ GCC_except_table9944
+ GCC_except_table9946
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveObserver
+ _OBJC_CLASS_$_PHPhotoLibraryCloudStatusObserverCoordinator
+ _OBJC_CLASS_$_PHResourceRequestReplyGuard
+ _OBJC_CLASS_$_PHShareCommentChangeRequest
+ _OBJC_IVAR_$_PHAssetExportRequestOptions._forceRatingMetadataBaking
+ _OBJC_IVAR_$_PHAssetExportRequestOptions._shouldExportTitle
+ _OBJC_IVAR_$_PHAssetExportRequestOptions._shouldStripRating
+ _OBJC_IVAR_$_PHPhotoLibrary._cloudStatusObserverCoordinator
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._cloudStatusHandlerQueue
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._cplStatusDelegateQueue
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._lazyCPLStatus
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._observerRegistrar
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._pauseLock
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._pauseLock_isObservingCloudPauseNotification
+ _OBJC_IVAR_$_PHPhotoLibraryCloudStatusObserverCoordinator._photoLibrary
+ _OBJC_IVAR_$_PHResourceRequestReplyGuard._delivered
+ _OBJC_IVAR_$_PHServerResourceRequestRunner._replyGuard
+ _OBJC_IVAR_$_PHShareComment._lastEditedDate
+ _OBJC_IVAR_$_PHShareCommentChangeRequest._commentText
+ _OBJC_IVAR_$_PHShareCommentChangeRequest._didSetCommentText
+ _OBJC_IVAR_$_PHSharePost._lastEditedDate
+ _OBJC_METACLASS_$_PHPhotoLibraryCloudStatusObserverCoordinator
+ _OBJC_METACLASS_$_PHResourceRequestReplyGuard
+ _OBJC_METACLASS_$_PHShareCommentChangeRequest
+ _PFIsLockScreenCamera
+ _PHAssetExportRequestStarRatingMetadataOperationForAssetWithOptions
+ _PHAssetExportRequestTitleMetadataOperationForAssetWithOptions
+ _PHAssetOriginalStarRatingForAsset
+ _PHAssetOriginalTitleForAsset
+ _PLCameraBundleId
+ _PLCloudPhotoLibraryPauseDidChangeNotification
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
+ ___69-[PHPhotoLibraryCloudStatusObserverCoordinator initWithPhotoLibrary:]_block_invoke_2
+ ___69-[PHServerResourceRequestRunner _newProgressWithReplyOnCancellation:]_block_invoke
+ ___74-[PHPhotoLibraryCloudStatusObserverCoordinator _processCPLStatusDidChange]_block_invoke
+ ___74-[PHPhotoLibraryCloudStatusObserverCoordinator _publishCloudStatusUpdate:]_block_invoke
+ ___78+[PHCloudFeedEntry fetchEntriesInCollectionShare:filter:earliestDate:options:]_block_invoke
+ ___84-[PHPhotoLibraryCloudStatusObserverCoordinator _stopObservingCloudPauseNotification]_block_invoke
+ ___84-[PHPhotoLibraryCloudStatusObserverCoordinator getCloudStatusWithCompletionHandler:]_block_invoke
+ ___84-[PHPhotoLibraryCloudStatusObserverCoordinator getCloudStatusWithCompletionHandler:]_block_invoke_2
+ ___84-[PHPhotoLibraryCloudStatusObserverCoordinator getCloudStatusWithCompletionHandler:]_block_invoke_3
+ ___84-[PHPhotoLibraryCloudStatusObserverCoordinator getCloudStatusWithCompletionHandler:]_block_invoke_4
+ ___84-[PHPhotoLibraryCloudStatusObserverCoordinator getCloudStatusWithCompletionHandler:]_block_invoke_5
+ ___96-[PHPhotoLibraryCloudStatusObserverCoordinator _startObservingCloudPauseNotificationIfNecessary]_block_invoke
+ ___block_descriptor_40_e8_32w_e39_v24?0"PLCPLClientStatus"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32s40bs_e39_v24?0"PLCPLClientStatus"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e17_v16?0"NSError"8ls32l8r56l8s40l8s48l8
+ __cloudPauseDidChange
+ _allowedEntities.pl_once_object_70
+ _allowedEntities.pl_once_object_71
+ _allowedEntities.pl_once_token_70
+ _allowedEntities.pl_once_token_71
+ _angelPhotoLibrary
+ _angelPhotoLibraryLock
+ _kPLImageWriterBatchImageDictionaries
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
+ _sharedLazyPhotoLibraryForCMM.pl_once_object_44
+ _sharedLazyPhotoLibraryForCMM.pl_once_token_44
+ _uniqueObjectIDCache.pl_once_object_69
+ _uniqueObjectIDCache.pl_once_token_69
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
- GCC_except_table10027
- GCC_except_table10118
- GCC_except_table10240
- GCC_except_table10264
- GCC_except_table10265
- GCC_except_table10272
- GCC_except_table10298
- GCC_except_table10299
- GCC_except_table10300
- GCC_except_table10301
- GCC_except_table10302
- GCC_except_table10303
- GCC_except_table10304
- GCC_except_table10305
- GCC_except_table10317
- GCC_except_table10326
- GCC_except_table10351
- GCC_except_table1044
- GCC_except_table10527
- GCC_except_table10536
- GCC_except_table10538
- GCC_except_table10539
- GCC_except_table10540
- GCC_except_table10541
- GCC_except_table10542
- GCC_except_table10553
- GCC_except_table10571
- GCC_except_table10604
- GCC_except_table10605
- GCC_except_table10606
- GCC_except_table10607
- GCC_except_table10608
- GCC_except_table10636
- GCC_except_table10637
- GCC_except_table10638
- GCC_except_table10639
- GCC_except_table10640
- GCC_except_table10641
- GCC_except_table10642
- GCC_except_table10643
- GCC_except_table10644
- GCC_except_table10645
- GCC_except_table10682
- GCC_except_table10683
- GCC_except_table10687
- GCC_except_table10706
- GCC_except_table1071
- GCC_except_table10711
- GCC_except_table1075
- GCC_except_table10793
- GCC_except_table1084
- GCC_except_table1086
- GCC_except_table10886
- GCC_except_table11054
- GCC_except_table11073
- GCC_except_table11076
- GCC_except_table11077
- GCC_except_table11103
- GCC_except_table11105
- GCC_except_table11195
- GCC_except_table11223
- GCC_except_table11757
- GCC_except_table11914
- GCC_except_table11917
- GCC_except_table11923
- GCC_except_table11931
- GCC_except_table11935
- GCC_except_table11937
- GCC_except_table11941
- GCC_except_table11947
- GCC_except_table12053
- GCC_except_table12073
- GCC_except_table12075
- GCC_except_table12077
- GCC_except_table12079
- GCC_except_table12114
- GCC_except_table12163
- GCC_except_table12170
- GCC_except_table12172
- GCC_except_table12180
- GCC_except_table1220
- GCC_except_table12217
- GCC_except_table12348
- GCC_except_table1236
- GCC_except_table12374
- GCC_except_table12386
- GCC_except_table12428
- GCC_except_table12430
- GCC_except_table12443
- GCC_except_table12548
- GCC_except_table12552
- GCC_except_table12593
- GCC_except_table12597
- GCC_except_table12606
- GCC_except_table12607
- GCC_except_table12614
- GCC_except_table1263
- GCC_except_table12652
- GCC_except_table12659
- GCC_except_table12671
- GCC_except_table12676
- GCC_except_table12726
- GCC_except_table12818
- GCC_except_table12821
- GCC_except_table12827
- GCC_except_table12869
- GCC_except_table12888
- GCC_except_table12961
- GCC_except_table12964
- GCC_except_table12978
- GCC_except_table12980
- GCC_except_table13045
- GCC_except_table13123
- GCC_except_table13127
- GCC_except_table13131
- GCC_except_table13168
- GCC_except_table13192
- GCC_except_table13199
- GCC_except_table13338
- GCC_except_table13350
- GCC_except_table13444
- GCC_except_table13511
- GCC_except_table1355
- GCC_except_table13717
- GCC_except_table13796
- GCC_except_table13838
- GCC_except_table13887
- GCC_except_table13897
- GCC_except_table13917
- GCC_except_table13932
- GCC_except_table13960
- GCC_except_table13962
- GCC_except_table13975
- GCC_except_table13977
- GCC_except_table13979
- GCC_except_table13998
- GCC_except_table14144
- GCC_except_table14155
- GCC_except_table14182
- GCC_except_table14188
- GCC_except_table14204
- GCC_except_table14274
- GCC_except_table14276
- GCC_except_table14322
- GCC_except_table14324
- GCC_except_table14348
- GCC_except_table14351
- GCC_except_table14505
- GCC_except_table1461
- GCC_except_table1553
- GCC_except_table1578
- GCC_except_table1624
- GCC_except_table1699
- GCC_except_table1797
- GCC_except_table1898
- GCC_except_table1902
- GCC_except_table1922
- GCC_except_table1927
- GCC_except_table1931
- GCC_except_table1941
- GCC_except_table2130
- GCC_except_table2134
- GCC_except_table2136
- GCC_except_table2138
- GCC_except_table2140
- GCC_except_table2142
- GCC_except_table2144
- GCC_except_table2154
- GCC_except_table2156
- GCC_except_table2158
- GCC_except_table2170
- GCC_except_table2202
- GCC_except_table2204
- GCC_except_table2206
- GCC_except_table2208
- GCC_except_table2210
- GCC_except_table2212
- GCC_except_table2214
- GCC_except_table2216
- GCC_except_table2218
- GCC_except_table2220
- GCC_except_table2222
- GCC_except_table2224
- GCC_except_table2226
- GCC_except_table2228
- GCC_except_table2230
- GCC_except_table2232
- GCC_except_table2246
- GCC_except_table2248
- GCC_except_table2253
- GCC_except_table2255
- GCC_except_table2284
- GCC_except_table2286
- GCC_except_table2289
- GCC_except_table2292
- GCC_except_table2332
- GCC_except_table2400
- GCC_except_table2405
- GCC_except_table2416
- GCC_except_table2428
- GCC_except_table2466
- GCC_except_table2637
- GCC_except_table2650
- GCC_except_table2678
- GCC_except_table2693
- GCC_except_table2712
- GCC_except_table2722
- GCC_except_table2759
- GCC_except_table2764
- GCC_except_table2826
- GCC_except_table2929
- GCC_except_table2940
- GCC_except_table2942
- GCC_except_table2948
- GCC_except_table2956
- GCC_except_table2988
- GCC_except_table3064
- GCC_except_table3069
- GCC_except_table3074
- GCC_except_table3077
- GCC_except_table3087
- GCC_except_table3098
- GCC_except_table3100
- GCC_except_table3107
- GCC_except_table3234
- GCC_except_table3238
- GCC_except_table3241
- GCC_except_table3308
- GCC_except_table3316
- GCC_except_table3351
- GCC_except_table3355
- GCC_except_table3360
- GCC_except_table3490
- GCC_except_table3527
- GCC_except_table3533
- GCC_except_table3536
- GCC_except_table3546
- GCC_except_table3550
- GCC_except_table3556
- GCC_except_table3559
- GCC_except_table3564
- GCC_except_table3568
- GCC_except_table3579
- GCC_except_table3584
- GCC_except_table3595
- GCC_except_table3596
- GCC_except_table3613
- GCC_except_table3622
- GCC_except_table3719
- GCC_except_table3725
- GCC_except_table3748
- GCC_except_table3750
- GCC_except_table3797
- GCC_except_table3825
- GCC_except_table3856
- GCC_except_table3858
- GCC_except_table3876
- GCC_except_table3878
- GCC_except_table3881
- GCC_except_table4044
- GCC_except_table4078
- GCC_except_table4086
- GCC_except_table4088
- GCC_except_table4103
- GCC_except_table4106
- GCC_except_table4108
- GCC_except_table4141
- GCC_except_table4146
- GCC_except_table4147
- GCC_except_table4414
- GCC_except_table4421
- GCC_except_table4451
- GCC_except_table4475
- GCC_except_table4477
- GCC_except_table4482
- GCC_except_table4487
- GCC_except_table4502
- GCC_except_table4536
- GCC_except_table4537
- GCC_except_table4597
- GCC_except_table4922
- GCC_except_table4932
- GCC_except_table4991
- GCC_except_table4993
- GCC_except_table4997
- GCC_except_table4999
- GCC_except_table5002
- GCC_except_table5072
- GCC_except_table5077
- GCC_except_table5107
- GCC_except_table5237
- GCC_except_table5241
- GCC_except_table5589
- GCC_except_table5620
- GCC_except_table5666
- GCC_except_table5685
- GCC_except_table5691
- GCC_except_table5697
- GCC_except_table5709
- GCC_except_table5742
- GCC_except_table5745
- GCC_except_table5747
- GCC_except_table5754
- GCC_except_table5767
- GCC_except_table5776
- GCC_except_table5819
- GCC_except_table5852
- GCC_except_table5857
- GCC_except_table5881
- GCC_except_table5885
- GCC_except_table5889
- GCC_except_table5917
- GCC_except_table5921
- GCC_except_table5935
- GCC_except_table5938
- GCC_except_table5941
- GCC_except_table5964
- GCC_except_table5998
- GCC_except_table6019
- GCC_except_table6028
- GCC_except_table6067
- GCC_except_table6079
- GCC_except_table6113
- GCC_except_table6116
- GCC_except_table6122
- GCC_except_table6126
- GCC_except_table6138
- GCC_except_table6171
- GCC_except_table6200
- GCC_except_table6227
- GCC_except_table6229
- GCC_except_table6243
- GCC_except_table6312
- GCC_except_table6390
- GCC_except_table6395
- GCC_except_table6400
- GCC_except_table6558
- GCC_except_table6561
- GCC_except_table6574
- GCC_except_table6599
- GCC_except_table6609
- GCC_except_table6612
- GCC_except_table6651
- GCC_except_table6688
- GCC_except_table6690
- GCC_except_table7090
- GCC_except_table7110
- GCC_except_table7123
- GCC_except_table7136
- GCC_except_table7155
- GCC_except_table7186
- GCC_except_table7189
- GCC_except_table7191
- GCC_except_table7195
- GCC_except_table7204
- GCC_except_table7252
- GCC_except_table7266
- GCC_except_table7304
- GCC_except_table7306
- GCC_except_table7345
- GCC_except_table7598
- GCC_except_table7601
- GCC_except_table7623
- GCC_except_table7646
- GCC_except_table7648
- GCC_except_table7649
- GCC_except_table7650
- GCC_except_table7651
- GCC_except_table7652
- GCC_except_table7664
- GCC_except_table7665
- GCC_except_table7666
- GCC_except_table7823
- GCC_except_table802
- GCC_except_table8042
- GCC_except_table805
- GCC_except_table806
- GCC_except_table807
- GCC_except_table808
- GCC_except_table8087
- GCC_except_table809
- GCC_except_table8105
- GCC_except_table8106
- GCC_except_table8166
- GCC_except_table8188
- GCC_except_table8192
- GCC_except_table8253
- GCC_except_table8453
- GCC_except_table8455
- GCC_except_table8502
- GCC_except_table8542
- GCC_except_table8546
- GCC_except_table8548
- GCC_except_table8550
- GCC_except_table8562
- GCC_except_table8567
- GCC_except_table8607
- GCC_except_table8635
- GCC_except_table8677
- GCC_except_table8769
- GCC_except_table8827
- GCC_except_table8847
- GCC_except_table8850
- GCC_except_table8869
- GCC_except_table889
- GCC_except_table8928
- GCC_except_table8932
- GCC_except_table8937
- GCC_except_table8938
- GCC_except_table8939
- GCC_except_table8942
- GCC_except_table8959
- GCC_except_table8962
- GCC_except_table8983
- GCC_except_table9027
- GCC_except_table9092
- GCC_except_table9249
- GCC_except_table9290
- GCC_except_table9296
- GCC_except_table9299
- GCC_except_table9562
- GCC_except_table9566
- GCC_except_table9570
- GCC_except_table9590
- GCC_except_table9591
- GCC_except_table9687
- GCC_except_table9730
- GCC_except_table9782
- GCC_except_table9827
- GCC_except_table9847
- GCC_except_table9873
- GCC_except_table9901
- GCC_except_table9934
- GCC_except_table9936
- GCC_except_table994
- _NSFilePosixPermissions
- _OBJC_IVAR_$_PHPhotoLibrary._cachedCloudStatus
- _OBJC_IVAR_$_PHPhotoLibrary._cloudStatusHandlerQueue
- _OBJC_IVAR_$_PHPhotoLibrary._cloudStatusObserverRegistrar
- _OBJC_IVAR_$_PHPhotoLibrary._cplStatusDelegateQueue
- _OBJC_IVAR_$_PHPhotoLibrary._lazyCPLStatus
- _OBJC_IVAR_$_PHSharePost._lastModifiedDate
- _PHIsImageAssetResourceType
- _PHIsVideoAssetResourceType
- _PLGatekeeperXPCGetLog
- _PLIsCamera
- _PLIsSharedCollectionsFeatureEnabled
- _PLSafeEntityForNameInManagedObjectContext
- ___151-[PHAssetExportRequest _processResourcesAtFileURLs:forAsset:withOptions:progress:processingUnitCount:replacementLivePhotoPairingIdentifier:completion:]_block_invoke_4
- ___151-[PHAssetExportRequest _processResourcesAtFileURLs:forAsset:withOptions:progress:processingUnitCount:replacementLivePhotoPairingIdentifier:completion:]_block_invoke_5
- ___151-[PHAssetExportRequest _processResourcesAtFileURLs:forAsset:withOptions:progress:processingUnitCount:replacementLivePhotoPairingIdentifier:completion:]_block_invoke_6
- ___151-[PHAssetExportRequest _processResourcesAtFileURLs:forAsset:withOptions:progress:processingUnitCount:replacementLivePhotoPairingIdentifier:completion:]_block_invoke_7
- ___151-[PHAssetExportRequest _processResourcesAtFileURLs:forAsset:withOptions:progress:processingUnitCount:replacementLivePhotoPairingIdentifier:completion:]_block_invoke_8
- ___151-[PHAssetExportRequest _processResourcesAtFileURLs:forAsset:withOptions:progress:processingUnitCount:replacementLivePhotoPairingIdentifier:completion:]_block_invoke_9
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
- ___block_descriptor_48_e8_32bs40w_e39_v24?0"PLCPLClientStatus"8"NSError"16ls32l8w40l8
- ___block_descriptor_48_e8_32s40w_e39_v24?0"PLCPLClientStatus"8"NSError"16lw40l8s32l8
- _allowedEntities.pl_once_object_74
- _allowedEntities.pl_once_object_75
- _allowedEntities.pl_once_token_74
- _allowedEntities.pl_once_token_75
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
- _sharedLazyPhotoLibraryForCMM.pl_once_object_46
- _sharedLazyPhotoLibraryForCMM.pl_once_token_46
- _uniqueObjectIDCache.pl_once_object_73
- _uniqueObjectIDCache.pl_once_token_73
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
+ "Asset playback style is unsupported for export."
+ "No PLPhotoLibrary for current queue (wellKnownIdentifier=%td, isSystemPhotoLibrary=%d, mainThread=%d, qos=%@)"
+ "Not direct uploading Share asset %@ after resource download - asset is missing or was not fully copied"
+ "PHAssetExportRequestMetadataOperation PHAssetExportRequestAccessibilityDescriptionMetadataOperationForAssetWithOptions(PHAsset *__strong _Nonnull, PHAssetExportRequestOptions *__strong _Nonnull, PFMetadata *__strong _Nullable, NSString * _Nullable __autoreleasing * _Nullable)"
+ "PHAssetExportRequestMetadataOperation PHAssetExportRequestStarRatingMetadataOperationForAssetWithOptions(PHAsset *__strong _Nonnull, PHAssetExportRequestOptions *__strong _Nonnull, PFMetadata *__strong _Nullable, NSNumber * _Nullable __autoreleasing * _Nullable)"
+ "PHAssetExportRequestMetadataOperation PHAssetExportRequestTitleMetadataOperationForAssetWithOptions(PHAsset *__strong _Nonnull, PHAssetExportRequestOptions *__strong _Nonnull, PFMetadata *__strong _Nullable, NSString * _Nullable __autoreleasing * _Nullable)"
+ "PHFetchResult init with no fetch request; fetchError from %{public}s: %@\n\tself: %@"
+ "PHPhotosErrorCollectionShareNotEnabled"
+ "PHPhotosErrorShareNeedsToRequestAccess"
+ "PLImageWriterStashCameraJob"
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
+ "com.apple.camera.lockscreen"
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
