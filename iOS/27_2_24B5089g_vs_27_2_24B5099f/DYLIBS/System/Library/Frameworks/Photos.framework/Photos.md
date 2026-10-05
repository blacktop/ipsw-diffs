## Photos

> `/System/Library/Frameworks/Photos.framework/Photos`

```diff

-916.45.110.0.0
-  __TEXT.__text: 0x2d7c80
-  __TEXT.__objc_methlist: 0x2716c
-  __TEXT.__const: 0x17f0
+916.51.202.0.0
+  __TEXT.__text: 0x2d88a0
+  __TEXT.__objc_methlist: 0x271fc
+  __TEXT.__const: 0x1868
   __TEXT.__dlopen_cstrs: 0x280
-  __TEXT.__constg_swiftt: 0x67c
-  __TEXT.__swift5_typeref: 0x547
+  __TEXT.__constg_swiftt: 0x660
+  __TEXT.__swift5_typeref: 0x5ab
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x191
-  __TEXT.__swift5_fieldmd: 0x23c
-  __TEXT.__swift5_assocty: 0xd0
-  __TEXT.__swift5_proto: 0x4c
-  __TEXT.__swift5_types: 0x44
+  __TEXT.__swift5_reflstr: 0x1a1
+  __TEXT.__swift5_fieldmd: 0x220
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__swift5_proto: 0x48
+  __TEXT.__swift5_types: 0x40
   __TEXT.__swift5_capture: 0x198
-  __TEXT.__cstring: 0x339d8
+  __TEXT.__cstring: 0x33c05
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__oslogstring: 0x24fd7
+  __TEXT.__oslogstring: 0x250b6
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x981c
+  __TEXT.__gcc_except_tab: 0x9804
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xbad8
+  __TEXT.__unwind_info: 0xbb58
   __TEXT.__eh_frame: 0x4d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x9140
-  __DATA_CONST.__objc_classlist: 0xf58
+  __DATA_CONST.__objc_classlist: 0xf60
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14a40
+  __DATA_CONST.__objc_selrefs: 0x14aa0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0xc70
+  __DATA_CONST.__objc_superrefs: 0xc78
   __DATA_CONST.__objc_arraydata: 0x940
-  __DATA_CONST.__got: 0x2a98
-  __AUTH_CONST.__const: 0x4798
-  __AUTH_CONST.__cfstring: 0x2dac0
-  __AUTH_CONST.__objc_const: 0x42c50
-  __AUTH_CONST.__objc_intobj: 0x24f0
+  __DATA_CONST.__got: 0x2ac0
+  __AUTH_CONST.__const: 0x4770
+  __AUTH_CONST.__cfstring: 0x2db40
+  __AUTH_CONST.__objc_const: 0x42d70
+  __AUTH_CONST.__objc_intobj: 0x2508
   __AUTH_CONST.__objc_arrayobj: 0x7b0
-  __AUTH_CONST.__objc_doubleobj: 0x140
+  __AUTH_CONST.__objc_doubleobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1920
-  __AUTH.__objc_data: 0x7898
+  __AUTH_CONST.__auth_got: 0x1948
+  __AUTH.__objc_data: 0x78e8
   __AUTH.__data: 0x3c0
-  __DATA.__objc_ivar: 0x3664
-  __DATA.__data: 0x2c08
+  __DATA.__objc_ivar: 0x3670
+  __DATA.__data: 0x2c28
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0x20f0
   __DATA_DIRTY.__data: 0x148
-  __DATA_DIRTY.__bss: 0x120
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15083
-  Symbols:   26182
-  CStrings:  8996
+  Functions: 15116
+  Symbols:   26211
+  CStrings:  9004
 
Symbols:
+ +[PHAssetExportRequest _provenanceRenderURLToShareForAsset:options:fileURLs:]
+ +[PHAssetExportRequest _shouldCombineProvenanceIntoRenderForAsset:options:fileURLs:]
+ +[PHAssetResource assetResourcesForAsset:resourceTypeGroups:]
+ +[PHAssetResource fetchAssetResourcesForAssets:resourceTypeGroups:]
+ +[PHAssetResource fetchAssetResourcesForAssetsArray:resourceTypeGroups:]
+ +[PHAssetResource resources:matchingTypeGroups:]
+ +[PHAssetResourceFetchResult fetchResultWithAssets:resourceTypeGroups:]
+ +[PHResourceLocalAvailabilityRequest _shouldAddOriginalAsProvenanceSourceForAsset:shouldStripProvenance:]
+ +[PHSearch ocrTextLinesForAssetUUID:inPhotoLibrary:includeLowConfidenceText:]
+ +[PHSensitiveContentAnalysisUtility sensitiveContentStateForAsset:]
+ -[PHAssetCreationRequest _creationOptionsPreservingOriginalProvenanceFilenameForResource:]
+ -[PHAssetResource prefetchedMediaMetadata]
+ -[PHAssetResource setPrefetchedMediaMetadata:]
+ -[PHAssetResourceFetchResult initWithAssets:resourceTypeGroups:]
+ -[PHAssetResourceFetchResult typeGroups]
+ -[PHCollectionShare _updateAccessRequestForParticipant:toAcceptanceStatus:completion:]
+ -[PHCollectionShare approveAccessRequestForParticipant:completion:]
+ -[PHCollectionShare blockAccessRequestForParticipant:completion:]
+ -[PHCollectionShare denyAccessRequestForParticipant:completion:]
+ -[PHCollectionShare unblockAccessRequestForParticipant:completion:]
+ -[PHPrefetchedMediaMetadata .cxx_destruct]
+ -[PHPrefetchedMediaMetadata data]
+ -[PHPrefetchedMediaMetadata initWithData:type:]
+ -[PHPrefetchedMediaMetadata type]
+ GCC_except_table10053
+ GCC_except_table10144
+ GCC_except_table10266
+ GCC_except_table10276
+ GCC_except_table10291
+ GCC_except_table10298
+ GCC_except_table10301
+ GCC_except_table10331
+ GCC_except_table10346
+ GCC_except_table10356
+ GCC_except_table10432
+ GCC_except_table10433
+ GCC_except_table10434
+ GCC_except_table10435
+ GCC_except_table10436
+ GCC_except_table10437
+ GCC_except_table10438
+ GCC_except_table10439
+ GCC_except_table10440
+ GCC_except_table10441
+ GCC_except_table10442
+ GCC_except_table10562
+ GCC_except_table10563
+ GCC_except_table10564
+ GCC_except_table10565
+ GCC_except_table10566
+ GCC_except_table10567
+ GCC_except_table10579
+ GCC_except_table10597
+ GCC_except_table10630
+ GCC_except_table10631
+ GCC_except_table10632
+ GCC_except_table10634
+ GCC_except_table10644
+ GCC_except_table10662
+ GCC_except_table10663
+ GCC_except_table10664
+ GCC_except_table10665
+ GCC_except_table10666
+ GCC_except_table10667
+ GCC_except_table10668
+ GCC_except_table10669
+ GCC_except_table10670
+ GCC_except_table10671
+ GCC_except_table10708
+ GCC_except_table10709
+ GCC_except_table10713
+ GCC_except_table10733
+ GCC_except_table10738
+ GCC_except_table10820
+ GCC_except_table10913
+ GCC_except_table11081
+ GCC_except_table11100
+ GCC_except_table11103
+ GCC_except_table11104
+ GCC_except_table11130
+ GCC_except_table11132
+ GCC_except_table11222
+ GCC_except_table11250
+ GCC_except_table11784
+ GCC_except_table11941
+ GCC_except_table11944
+ GCC_except_table11950
+ GCC_except_table11958
+ GCC_except_table11962
+ GCC_except_table11964
+ GCC_except_table11968
+ GCC_except_table11974
+ GCC_except_table12080
+ GCC_except_table12100
+ GCC_except_table12102
+ GCC_except_table12104
+ GCC_except_table12106
+ GCC_except_table12141
+ GCC_except_table12197
+ GCC_except_table12199
+ GCC_except_table12201
+ GCC_except_table12207
+ GCC_except_table12244
+ GCC_except_table12375
+ GCC_except_table12401
+ GCC_except_table12413
+ GCC_except_table12455
+ GCC_except_table12457
+ GCC_except_table12470
+ GCC_except_table12575
+ GCC_except_table12579
+ GCC_except_table12620
+ GCC_except_table12624
+ GCC_except_table12633
+ GCC_except_table12634
+ GCC_except_table12641
+ GCC_except_table12679
+ GCC_except_table12686
+ GCC_except_table12698
+ GCC_except_table12703
+ GCC_except_table12753
+ GCC_except_table12848
+ GCC_except_table12854
+ GCC_except_table12856
+ GCC_except_table12896
+ GCC_except_table12926
+ GCC_except_table12991
+ GCC_except_table12999
+ GCC_except_table13005
+ GCC_except_table13007
+ GCC_except_table13072
+ GCC_except_table13150
+ GCC_except_table13154
+ GCC_except_table13158
+ GCC_except_table13195
+ GCC_except_table13220
+ GCC_except_table13227
+ GCC_except_table13367
+ GCC_except_table13380
+ GCC_except_table13474
+ GCC_except_table13541
+ GCC_except_table13747
+ GCC_except_table13826
+ GCC_except_table13868
+ GCC_except_table13917
+ GCC_except_table13927
+ GCC_except_table13947
+ GCC_except_table13962
+ GCC_except_table13990
+ GCC_except_table13992
+ GCC_except_table14005
+ GCC_except_table14007
+ GCC_except_table14009
+ GCC_except_table14028
+ GCC_except_table14185
+ GCC_except_table14212
+ GCC_except_table14218
+ GCC_except_table14234
+ GCC_except_table14304
+ GCC_except_table14306
+ GCC_except_table14352
+ GCC_except_table14354
+ GCC_except_table14381
+ GCC_except_table14385
+ GCC_except_table14386
+ GCC_except_table14398
+ GCC_except_table14415
+ GCC_except_table14418
+ GCC_except_table14572
+ GCC_except_table2302
+ GCC_except_table2304
+ GCC_except_table2307
+ GCC_except_table2310
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
+ GCC_except_table2783
+ GCC_except_table2788
+ GCC_except_table2850
+ GCC_except_table2953
+ GCC_except_table2964
+ GCC_except_table2966
+ GCC_except_table2972
+ GCC_except_table2980
+ GCC_except_table3012
+ GCC_except_table3090
+ GCC_except_table3095
+ GCC_except_table3103
+ GCC_except_table3112
+ GCC_except_table3124
+ GCC_except_table3130
+ GCC_except_table3135
+ GCC_except_table3258
+ GCC_except_table3262
+ GCC_except_table3332
+ GCC_except_table3340
+ GCC_except_table3375
+ GCC_except_table3379
+ GCC_except_table3384
+ GCC_except_table3512
+ GCC_except_table3549
+ GCC_except_table3555
+ GCC_except_table3568
+ GCC_except_table3572
+ GCC_except_table3578
+ GCC_except_table3586
+ GCC_except_table3590
+ GCC_except_table3601
+ GCC_except_table3606
+ GCC_except_table3617
+ GCC_except_table3618
+ GCC_except_table3635
+ GCC_except_table3644
+ GCC_except_table3741
+ GCC_except_table3747
+ GCC_except_table3768
+ GCC_except_table3770
+ GCC_except_table3772
+ GCC_except_table3819
+ GCC_except_table3847
+ GCC_except_table3878
+ GCC_except_table3880
+ GCC_except_table3898
+ GCC_except_table3900
+ GCC_except_table4066
+ GCC_except_table4100
+ GCC_except_table4108
+ GCC_except_table4110
+ GCC_except_table4125
+ GCC_except_table4130
+ GCC_except_table4163
+ GCC_except_table4168
+ GCC_except_table4169
+ GCC_except_table4436
+ GCC_except_table4443
+ GCC_except_table4474
+ GCC_except_table4498
+ GCC_except_table4505
+ GCC_except_table4510
+ GCC_except_table4521
+ GCC_except_table4525
+ GCC_except_table4547
+ GCC_except_table4560
+ GCC_except_table4561
+ GCC_except_table4621
+ GCC_except_table4946
+ GCC_except_table4956
+ GCC_except_table5018
+ GCC_except_table5024
+ GCC_except_table5029
+ GCC_except_table5099
+ GCC_except_table5104
+ GCC_except_table5134
+ GCC_except_table5264
+ GCC_except_table5268
+ GCC_except_table5625
+ GCC_except_table5657
+ GCC_except_table5704
+ GCC_except_table5723
+ GCC_except_table5729
+ GCC_except_table5735
+ GCC_except_table5747
+ GCC_except_table5749
+ GCC_except_table5780
+ GCC_except_table5783
+ GCC_except_table5785
+ GCC_except_table5792
+ GCC_except_table5801
+ GCC_except_table5805
+ GCC_except_table5814
+ GCC_except_table5818
+ GCC_except_table5857
+ GCC_except_table5890
+ GCC_except_table5895
+ GCC_except_table5923
+ GCC_except_table5927
+ GCC_except_table5957
+ GCC_except_table5971
+ GCC_except_table5974
+ GCC_except_table5977
+ GCC_except_table6000
+ GCC_except_table6050
+ GCC_except_table6059
+ GCC_except_table6101
+ GCC_except_table6133
+ GCC_except_table6136
+ GCC_except_table6142
+ GCC_except_table6146
+ GCC_except_table6157
+ GCC_except_table6188
+ GCC_except_table6217
+ GCC_except_table6244
+ GCC_except_table6246
+ GCC_except_table6260
+ GCC_except_table6330
+ GCC_except_table6408
+ GCC_except_table6413
+ GCC_except_table6418
+ GCC_except_table6576
+ GCC_except_table6579
+ GCC_except_table6593
+ GCC_except_table6618
+ GCC_except_table6628
+ GCC_except_table6631
+ GCC_except_table6670
+ GCC_except_table6707
+ GCC_except_table6709
+ GCC_except_table7109
+ GCC_except_table7129
+ GCC_except_table7142
+ GCC_except_table7155
+ GCC_except_table7174
+ GCC_except_table7205
+ GCC_except_table7208
+ GCC_except_table7210
+ GCC_except_table7212
+ GCC_except_table7214
+ GCC_except_table7223
+ GCC_except_table7271
+ GCC_except_table7285
+ GCC_except_table7323
+ GCC_except_table7325
+ GCC_except_table7364
+ GCC_except_table7617
+ GCC_except_table7620
+ GCC_except_table7642
+ GCC_except_table7649
+ GCC_except_table7665
+ GCC_except_table7667
+ GCC_except_table7668
+ GCC_except_table7669
+ GCC_except_table7670
+ GCC_except_table7671
+ GCC_except_table7672
+ GCC_except_table7683
+ GCC_except_table7684
+ GCC_except_table7685
+ GCC_except_table7842
+ GCC_except_table8061
+ GCC_except_table8106
+ GCC_except_table8124
+ GCC_except_table8125
+ GCC_except_table8185
+ GCC_except_table8207
+ GCC_except_table8211
+ GCC_except_table8218
+ GCC_except_table8272
+ GCC_except_table8478
+ GCC_except_table8480
+ GCC_except_table8527
+ GCC_except_table8567
+ GCC_except_table8571
+ GCC_except_table8575
+ GCC_except_table8587
+ GCC_except_table8592
+ GCC_except_table8632
+ GCC_except_table8660
+ GCC_except_table8702
+ GCC_except_table8796
+ GCC_except_table8854
+ GCC_except_table8874
+ GCC_except_table8877
+ GCC_except_table8896
+ GCC_except_table8955
+ GCC_except_table8959
+ GCC_except_table8963
+ GCC_except_table8964
+ GCC_except_table8965
+ GCC_except_table8966
+ GCC_except_table8967
+ GCC_except_table8969
+ GCC_except_table8975
+ GCC_except_table8986
+ GCC_except_table8989
+ GCC_except_table9010
+ GCC_except_table9054
+ GCC_except_table9121
+ GCC_except_table9278
+ GCC_except_table9319
+ GCC_except_table9325
+ GCC_except_table9328
+ GCC_except_table9588
+ GCC_except_table9592
+ GCC_except_table9596
+ GCC_except_table9616
+ GCC_except_table9617
+ GCC_except_table9713
+ GCC_except_table9723
+ GCC_except_table9756
+ GCC_except_table9808
+ GCC_except_table9853
+ GCC_except_table9873
+ GCC_except_table9899
+ GCC_except_table9927
+ GCC_except_table9960
+ GCC_except_table9962
+ _OBJC_CLASS_$_PHPrefetchedMediaMetadata
+ _OBJC_CLASS_$_PLMediaMetadataVirtualResource
+ _OBJC_IVAR_$_PHAssetResource._prefetchedMediaMetadata
+ _OBJC_IVAR_$_PHAssetResourceFetchResult._typeGroups
+ _OBJC_IVAR_$_PHPrefetchedMediaMetadata._data
+ _OBJC_IVAR_$_PHPrefetchedMediaMetadata._type
+ _OBJC_METACLASS_$_PHPrefetchedMediaMetadata
+ _PAMediaConversionErrorIsProvenanceProcessingError
+ _PHAssetResourceTypeGroupsIncludesTargetGroups
+ _PLIsMediaanalysisd
+ __OBJC_$_INSTANCE_METHODS_PHPrefetchedMediaMetadata
+ __OBJC_$_INSTANCE_VARIABLES_PHPrefetchedMediaMetadata
+ __OBJC_$_PROP_LIST_PHPrefetchedMediaMetadata
+ __OBJC_CLASS_RO_$_PHPrefetchedMediaMetadata
+ __OBJC_METACLASS_RO_$_PHPrefetchedMediaMetadata
+ ___77+[PHSearch ocrTextLinesForAssetUUID:inPhotoLibrary:includeLowConfidenceText:]_block_invoke
+ ___77+[PHSearch ocrTextLinesForAssetUUID:inPhotoLibrary:includeLowConfidenceText:]_block_invoke_2
+ ___86-[PHCollectionShare _updateAccessRequestForParticipant:toAcceptanceStatus:completion:]_block_invoke
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ __fetchTypeForAssetCollectionLocalIdentifierCode.pl_once_object_36
+ __fetchTypeForAssetCollectionLocalIdentifierCode.pl_once_token_36
+ __simpleDeleteValidatorsWithManagedObjectContext:.pl_once_object_16
+ __simpleDeleteValidatorsWithManagedObjectContext:.pl_once_token_16
+ _allowedEntities.pl_once_object_81
+ _allowedEntities.pl_once_object_82
+ _allowedEntities.pl_once_token_81
+ _allowedEntities.pl_once_token_82
+ _analyticsPropertiesToFetch.pl_once_object_15
+ _analyticsPropertiesToFetch.pl_once_token_15
+ _associated conformance So26PHAssetResourceFetchResultCSl6Photos11SubSequenceSl_Sl
+ _associated conformance So26PHAssetResourceFetchResultCSl6Photos5IndexSl_SL
+ _associated conformance So26PHAssetResourceFetchResultCSl6Photos7IndicesSl_Sl
+ _associated conformance So26PHAssetResourceFetchResultCSl6PhotosST
+ _corePropertiesToFetch.pl_once_object_15
+ _corePropertiesToFetch.pl_once_token_15
+ _dateRangeTitleGenerator.pl_once_object_17
+ _dateRangeTitleGenerator.pl_once_token_17
+ _entityKeyMap.pl_once_object_15
+ _entityKeyMap.pl_once_object_16
+ _entityKeyMap.pl_once_token_15
+ _entityKeyMap.pl_once_token_16
+ _handleUnsupportedAssetCollectionFetchTypeForLocalIdentifier.pl_once_object_49
+ _handleUnsupportedAssetCollectionFetchTypeForLocalIdentifier.pl_once_token_49
+ _propertiesToFetch.pl_once_object_19
+ _propertiesToFetch.pl_once_object_23
+ _propertiesToFetch.pl_once_object_28
+ _propertiesToFetch.pl_once_token_19
+ _propertiesToFetch.pl_once_token_23
+ _propertiesToFetch.pl_once_token_28
+ _propertiesToFetchWithHint:.pl_once_object_15
+ _propertiesToFetchWithHint:.pl_once_token_15
+ _publicPHObjectChangeClasses.pl_once_object_29
+ _publicPHObjectChangeClasses.pl_once_token_29
+ _sharedLazyPhotoLibraryForCMM.pl_once_object_55
+ _sharedLazyPhotoLibraryForCMM.pl_once_token_55
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _symbolic $sSl
+ _symbolic SIySo26PHAssetResourceFetchResultCG
+ _symbolic _____ySo26PHAssetResourceFetchResultCG s5SliceV
+ _uniqueObjectIDCache.pl_once_object_80
+ _uniqueObjectIDCache.pl_once_token_80
- +[PHAssetExportRequest _adjustedProvenanceRenderURLToShareForAsset:options:fileURLs:]
- +[PHAssetExportRequest _shouldCombineEditedProvenanceIntoRenderForAsset:options:fileURLs:]
- +[PHAssetResource resources:matchingTypeGroup:]
- +[PHAssetResourceFetchResult fetchResultWithAssets:resourceTypeGroup:]
- +[PHImportAsset scanAssetsForProvenanceData:atEnd:]
- +[PHResourceLocalAvailabilityRequest _shouldAddOriginalProvenanceResourceToResourcesToShareForAsset:shouldStripProvenance:]
- -[PHAssetResourceFetchResult initWithAssets:resourceTypeGroup:]
- -[PHAssetResourceFetchResult typeGroup]
- -[PHImportAsset hasProvenanceMetadata]
- -[PHShareParticipantChangeRequest approveAccessRequest]
- -[PHShareParticipantChangeRequest blockAccessRequest]
- -[PHShareParticipantChangeRequest denyAccessRequest]
- -[PHShareParticipantChangeRequest unblockAccessRequest]
- GCC_except_table10042
- GCC_except_table10133
- GCC_except_table10255
- GCC_except_table10265
- GCC_except_table10279
- GCC_except_table10280
- GCC_except_table10287
- GCC_except_table10313
- GCC_except_table10314
- GCC_except_table10315
- GCC_except_table10316
- GCC_except_table10317
- GCC_except_table10318
- GCC_except_table10319
- GCC_except_table10320
- GCC_except_table10323
- GCC_except_table10332
- GCC_except_table10333
- GCC_except_table10342
- GCC_except_table10357
- GCC_except_table10367
- GCC_except_table10542
- GCC_except_table10551
- GCC_except_table10552
- GCC_except_table10554
- GCC_except_table10555
- GCC_except_table10556
- GCC_except_table10557
- GCC_except_table10586
- GCC_except_table10619
- GCC_except_table10620
- GCC_except_table10621
- GCC_except_table10622
- GCC_except_table10623
- GCC_except_table10651
- GCC_except_table10652
- GCC_except_table10653
- GCC_except_table10654
- GCC_except_table10655
- GCC_except_table10656
- GCC_except_table10657
- GCC_except_table10658
- GCC_except_table10659
- GCC_except_table10660
- GCC_except_table10697
- GCC_except_table10698
- GCC_except_table10702
- GCC_except_table10722
- GCC_except_table10727
- GCC_except_table10809
- GCC_except_table10902
- GCC_except_table11070
- GCC_except_table11089
- GCC_except_table11092
- GCC_except_table11093
- GCC_except_table11119
- GCC_except_table11121
- GCC_except_table11211
- GCC_except_table11239
- GCC_except_table11773
- GCC_except_table11930
- GCC_except_table11933
- GCC_except_table11939
- GCC_except_table11947
- GCC_except_table11951
- GCC_except_table11953
- GCC_except_table11957
- GCC_except_table11963
- GCC_except_table12069
- GCC_except_table12089
- GCC_except_table12091
- GCC_except_table12093
- GCC_except_table12095
- GCC_except_table12130
- GCC_except_table12179
- GCC_except_table12186
- GCC_except_table12188
- GCC_except_table12196
- GCC_except_table12233
- GCC_except_table12364
- GCC_except_table12390
- GCC_except_table12402
- GCC_except_table12444
- GCC_except_table12446
- GCC_except_table12459
- GCC_except_table12564
- GCC_except_table12568
- GCC_except_table12609
- GCC_except_table12613
- GCC_except_table12622
- GCC_except_table12623
- GCC_except_table12630
- GCC_except_table12668
- GCC_except_table12675
- GCC_except_table12687
- GCC_except_table12692
- GCC_except_table12742
- GCC_except_table12834
- GCC_except_table12837
- GCC_except_table12843
- GCC_except_table12885
- GCC_except_table12904
- GCC_except_table12977
- GCC_except_table12980
- GCC_except_table12994
- GCC_except_table12996
- GCC_except_table13061
- GCC_except_table13139
- GCC_except_table13143
- GCC_except_table13147
- GCC_except_table13184
- GCC_except_table13209
- GCC_except_table13216
- GCC_except_table13356
- GCC_except_table13369
- GCC_except_table13463
- GCC_except_table13530
- GCC_except_table13736
- GCC_except_table13815
- GCC_except_table13857
- GCC_except_table13906
- GCC_except_table13916
- GCC_except_table13936
- GCC_except_table13951
- GCC_except_table13979
- GCC_except_table13981
- GCC_except_table13994
- GCC_except_table13996
- GCC_except_table13998
- GCC_except_table14017
- GCC_except_table14163
- GCC_except_table14201
- GCC_except_table14207
- GCC_except_table14223
- GCC_except_table14293
- GCC_except_table14295
- GCC_except_table14341
- GCC_except_table14343
- GCC_except_table14370
- GCC_except_table14374
- GCC_except_table14375
- GCC_except_table14387
- GCC_except_table14404
- GCC_except_table14407
- GCC_except_table14561
- GCC_except_table2303
- GCC_except_table2305
- GCC_except_table2308
- GCC_except_table2311
- GCC_except_table2351
- GCC_except_table2423
- GCC_except_table2428
- GCC_except_table2443
- GCC_except_table2455
- GCC_except_table2493
- GCC_except_table2664
- GCC_except_table2677
- GCC_except_table2705
- GCC_except_table2720
- GCC_except_table2739
- GCC_except_table2749
- GCC_except_table2786
- GCC_except_table2791
- GCC_except_table2853
- GCC_except_table2956
- GCC_except_table2967
- GCC_except_table2969
- GCC_except_table2975
- GCC_except_table2983
- GCC_except_table3015
- GCC_except_table3093
- GCC_except_table3098
- GCC_except_table3106
- GCC_except_table3115
- GCC_except_table3127
- GCC_except_table3133
- GCC_except_table3138
- GCC_except_table3261
- GCC_except_table3268
- GCC_except_table3335
- GCC_except_table3343
- GCC_except_table3378
- GCC_except_table3382
- GCC_except_table3387
- GCC_except_table3515
- GCC_except_table3552
- GCC_except_table3561
- GCC_except_table3571
- GCC_except_table3575
- GCC_except_table3584
- GCC_except_table3589
- GCC_except_table3593
- GCC_except_table3604
- GCC_except_table3609
- GCC_except_table3620
- GCC_except_table3621
- GCC_except_table3638
- GCC_except_table3647
- GCC_except_table3744
- GCC_except_table3750
- GCC_except_table3771
- GCC_except_table3773
- GCC_except_table3775
- GCC_except_table3822
- GCC_except_table3850
- GCC_except_table3881
- GCC_except_table3883
- GCC_except_table3901
- GCC_except_table3906
- GCC_except_table4069
- GCC_except_table4103
- GCC_except_table4111
- GCC_except_table4113
- GCC_except_table4131
- GCC_except_table4133
- GCC_except_table4166
- GCC_except_table4171
- GCC_except_table4172
- GCC_except_table4439
- GCC_except_table4446
- GCC_except_table4476
- GCC_except_table4502
- GCC_except_table4507
- GCC_except_table4512
- GCC_except_table4523
- GCC_except_table4527
- GCC_except_table4549
- GCC_except_table4562
- GCC_except_table4563
- GCC_except_table4623
- GCC_except_table4948
- GCC_except_table4958
- GCC_except_table5022
- GCC_except_table5028
- GCC_except_table5031
- GCC_except_table5101
- GCC_except_table5106
- GCC_except_table5136
- GCC_except_table5266
- GCC_except_table5270
- GCC_except_table5618
- GCC_except_table5650
- GCC_except_table5696
- GCC_except_table5715
- GCC_except_table5721
- GCC_except_table5727
- GCC_except_table5739
- GCC_except_table5741
- GCC_except_table5767
- GCC_except_table5772
- GCC_except_table5777
- GCC_except_table5784
- GCC_except_table5793
- GCC_except_table5797
- GCC_except_table5806
- GCC_except_table5810
- GCC_except_table5849
- GCC_except_table5882
- GCC_except_table5887
- GCC_except_table5911
- GCC_except_table5915
- GCC_except_table5941
- GCC_except_table5963
- GCC_except_table5966
- GCC_except_table5969
- GCC_except_table5992
- GCC_except_table6042
- GCC_except_table6051
- GCC_except_table6093
- GCC_except_table6125
- GCC_except_table6128
- GCC_except_table6134
- GCC_except_table6138
- GCC_except_table6149
- GCC_except_table6180
- GCC_except_table6209
- GCC_except_table6236
- GCC_except_table6238
- GCC_except_table6252
- GCC_except_table6322
- GCC_except_table6400
- GCC_except_table6405
- GCC_except_table6410
- GCC_except_table6568
- GCC_except_table6571
- GCC_except_table6585
- GCC_except_table6610
- GCC_except_table6620
- GCC_except_table6623
- GCC_except_table6662
- GCC_except_table6699
- GCC_except_table6701
- GCC_except_table7101
- GCC_except_table7121
- GCC_except_table7134
- GCC_except_table7147
- GCC_except_table7166
- GCC_except_table7197
- GCC_except_table7200
- GCC_except_table7202
- GCC_except_table7204
- GCC_except_table7206
- GCC_except_table7215
- GCC_except_table7263
- GCC_except_table7277
- GCC_except_table7315
- GCC_except_table7317
- GCC_except_table7356
- GCC_except_table7609
- GCC_except_table7612
- GCC_except_table7634
- GCC_except_table7641
- GCC_except_table7657
- GCC_except_table7659
- GCC_except_table7660
- GCC_except_table7661
- GCC_except_table7662
- GCC_except_table7663
- GCC_except_table7664
- GCC_except_table7675
- GCC_except_table7676
- GCC_except_table7677
- GCC_except_table7834
- GCC_except_table8053
- GCC_except_table8098
- GCC_except_table8116
- GCC_except_table8117
- GCC_except_table8177
- GCC_except_table8199
- GCC_except_table8203
- GCC_except_table8210
- GCC_except_table8264
- GCC_except_table8464
- GCC_except_table8466
- GCC_except_table8513
- GCC_except_table8553
- GCC_except_table8557
- GCC_except_table8559
- GCC_except_table8561
- GCC_except_table8578
- GCC_except_table8618
- GCC_except_table8646
- GCC_except_table8688
- GCC_except_table8781
- GCC_except_table8839
- GCC_except_table8859
- GCC_except_table8862
- GCC_except_table8881
- GCC_except_table8940
- GCC_except_table8944
- GCC_except_table8948
- GCC_except_table8949
- GCC_except_table8950
- GCC_except_table8951
- GCC_except_table8952
- GCC_except_table8954
- GCC_except_table8956
- GCC_except_table8960
- GCC_except_table8974
- GCC_except_table8995
- GCC_except_table9039
- GCC_except_table9106
- GCC_except_table9263
- GCC_except_table9304
- GCC_except_table9310
- GCC_except_table9313
- GCC_except_table9577
- GCC_except_table9581
- GCC_except_table9585
- GCC_except_table9605
- GCC_except_table9606
- GCC_except_table9702
- GCC_except_table9712
- GCC_except_table9745
- GCC_except_table9797
- GCC_except_table9842
- GCC_except_table9862
- GCC_except_table9888
- GCC_except_table9916
- GCC_except_table9949
- GCC_except_table9951
- _OBJC_IVAR_$_PHAssetResourceFetchResult._typeGroup
- ___51+[PHImportAsset scanAssetsForProvenanceData:atEnd:]_block_invoke
- ___51+[PHImportAsset scanAssetsForProvenanceData:atEnd:]_block_invoke_2
- ___52+[PHSearch ocrTextLinesForAssetUUID:inPhotoLibrary:]_block_invoke
- ___52+[PHSearch ocrTextLinesForAssetUUID:inPhotoLibrary:]_block_invoke_2
- __fetchTypeForAssetCollectionLocalIdentifierCode.pl_once_object_25
- __fetchTypeForAssetCollectionLocalIdentifierCode.pl_once_token_25
- __simpleDeleteValidatorsWithManagedObjectContext:.pl_once_object_5
- __simpleDeleteValidatorsWithManagedObjectContext:.pl_once_token_5
- _allowedEntities.pl_once_object_70
- _allowedEntities.pl_once_object_71
- _allowedEntities.pl_once_token_70
- _allowedEntities.pl_once_token_71
- _analyticsPropertiesToFetch.pl_once_object_4
- _analyticsPropertiesToFetch.pl_once_token_4
- _associated conformance So26PHAssetResourceFetchResultC6PhotosE5IndexVSLACSQ
- _corePropertiesToFetch.pl_once_object_4
- _corePropertiesToFetch.pl_once_token_4
- _dateRangeTitleGenerator.pl_once_object_6
- _dateRangeTitleGenerator.pl_once_token_6
- _entityKeyMap.pl_once_object_4
- _entityKeyMap.pl_once_object_5
- _entityKeyMap.pl_once_token_4
- _entityKeyMap.pl_once_token_5
- _handleUnsupportedAssetCollectionFetchTypeForLocalIdentifier.pl_once_object_38
- _handleUnsupportedAssetCollectionFetchTypeForLocalIdentifier.pl_once_token_38
- _propertiesToFetch.pl_once_object_12
- _propertiesToFetch.pl_once_object_17
- _propertiesToFetch.pl_once_object_8
- _propertiesToFetch.pl_once_token_12
- _propertiesToFetch.pl_once_token_17
- _propertiesToFetch.pl_once_token_8
- _propertiesToFetchWithHint:.pl_once_object_4
- _propertiesToFetchWithHint:.pl_once_token_4
- _publicPHObjectChangeClasses.pl_once_object_18
- _publicPHObjectChangeClasses.pl_once_token_18
- _sharedLazyPhotoLibraryForCMM.pl_once_object_44
- _sharedLazyPhotoLibraryForCMM.pl_once_token_44
- _symbolic _____ So26PHAssetResourceFetchResultC6PhotosE5IndexV
- _type_layout_string So26PHAssetResourceFetchResultC6PhotosE5IndexV
- _uniqueObjectIDCache.pl_once_object_69
- _uniqueObjectIDCache.pl_once_token_69
CStrings:
+ "-[PHAssetExportRequest _processResourcesAtFileURLs:forAsset:withOptions:progress:processingUnitCount:replacementLivePhotoPairingIdentifier:completion:]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/Projects/PhotoKit/Sources/PHAssetExportRequest.m"
+ "AssetResourceUploadJobConfiguration is not in correct state."
+ "Edited provenance asset has no full-size render to combine its provenance into"
+ "Exceeded permitted number of AssetResourceUploadJobs."
+ "No AssetResourceUploadJobConfiguration is set for this change request."
+ "Provenance asset needs a full-size render to carry its original's provenance, but none was selected"
+ "Share participant has no UUID"
+ "[PHAssetExportRequest] Unable to create asset bundle at directory '%@' due to following error '%@'"
+ "[PHAssetExportRequest] Unable to create live photo bundle at '%@' due to following error '%@'"
+ "[PHAssetExportRequest][ContentProvenance] Provenance processing error while processing resources of asset %{public}@: %@"
+ "[PHResourceLocalAvailabilityRequest] Provenance asset needs its original carried into a full-size render, but none was selected for asset: %@, resources: %@, options: %@"
+ "[PHResourceLocalAvailabilityRequest] Routing provenance render to FullSizePhotoURLKey (keeping original in PhotoURLKey) for asset:%@"
+ "[RM] %@ Media metadata with version: %ld has no type string"
+ "typeGroups != 0"
- "Configuration is not in correct state."
- "Edited provenance asset selected its original as a provenance source but has no full-size render to carry it"
- "Too many jobs."
- "Unable to create asset bundle at directory '%@' due to following error '%@'"
- "Unable to create live photo bundle at '%@' due to following error '%@'"
- "[PHResourceLocalAvailabilityRequest] Routing edited provenance render to FullSizePhotoURLKey (keeping original in PhotoURLKey) for asset:%@"
- "[PHResourceLocalAvailabilityRequest] Selected original as provenance source but no full-size render is available to carry it for asset: %@, resources: %@, options: %@"
```
