## PhotosFormats

> `/System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0xe03ac
-  __TEXT.__objc_methlist: 0xce18
+916.41.100.0.0
+  __TEXT.__text: 0xe2528
+  __TEXT.__objc_methlist: 0xd068
   __TEXT.__const: 0x3390
   __TEXT.__dlopen_cstrs: 0x43
-  __TEXT.__cstring: 0xe28e
+  __TEXT.__cstring: 0xe2be
   __TEXT.__constg_swiftt: 0xa0
   __TEXT.__swift5_typeref: 0xeb
   __TEXT.__swift5_reflstr: 0x162
   __TEXT.__swift5_fieldmd: 0xf4
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0x2c34
-  __TEXT.__oslogstring: 0x7137
+  __TEXT.__gcc_except_tab: 0x2c6c
+  __TEXT.__oslogstring: 0x737d
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x41b0
+  __TEXT.__unwind_info: 0x4248
   __TEXT.__eh_frame: 0x380
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15c8
-  __DATA_CONST.__objc_classlist: 0x580
+  __DATA_CONST.__const: 0x15d0
+  __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x63c0
+  __DATA_CONST.__objc_selrefs: 0x6430
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x3b8
+  __DATA_CONST.__objc_superrefs: 0x3c8
   __DATA_CONST.__objc_arraydata: 0x800
-  __DATA_CONST.__got: 0x1758
+  __DATA_CONST.__got: 0x1788
   __AUTH_CONST.__const: 0x3568
-  __AUTH_CONST.__cfstring: 0xcda0
-  __AUTH_CONST.__objc_const: 0x15050
+  __AUTH_CONST.__cfstring: 0xcde0
+  __AUTH_CONST.__objc_const: 0x15398
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__objc_intobj: 0x900
+  __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH_CONST.__auth_got: 0x10a0
-  __AUTH.__objc_data: 0x7a0
+  __AUTH.__objc_data: 0x840
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0xd74
+  __DATA.__objc_ivar: 0xd98
   __DATA.__data: 0xda8
   __DATA_DIRTY.__objc_data: 0x2f80
   __DATA_DIRTY.__bss: 0x748

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5109
-  Symbols:   11954
-  CStrings:  2586
+  Functions: 5160
+  Symbols:   12051
+  CStrings:  2597
 
Symbols:
+ +[PFImageMetadataChangePolicySetStarRating policyWithStarRating:]
+ +[PFImageMetadataChangePolicySetStarRating supportsSecureCoding]
+ +[PFImageMetadataChangePolicySetTitle policyWithTitle:]
+ +[PFImageMetadataChangePolicySetTitle supportsSecureCoding]
+ +[PFSharingUtilities addStarRating:toAVMetadata:]
+ +[PFSharingUtilities addTitle:toAVMetadata:]
+ -[PFAssetBundle setStarRating:]
+ -[PFAssetBundle starRating]
+ -[PFContentProvenanceProcessedImageInfo certificateChainDERData]
+ -[PFContentProvenanceProcessedImageInfo setCertificateChainDERData:]
+ -[PFDisplayConfigurationProvider deviceConfigurationForDisplayContext:]
+ -[PFImageMetadataBuilder setStarRating:]
+ -[PFImageMetadataChangePolicySetStarRating .cxx_destruct]
+ -[PFImageMetadataChangePolicySetStarRating encodeWithCoder:]
+ -[PFImageMetadataChangePolicySetStarRating initWithCoder:]
+ -[PFImageMetadataChangePolicySetStarRating metadataNeedsProcessing:]
+ -[PFImageMetadataChangePolicySetStarRating processMetadata:]
+ -[PFImageMetadataChangePolicySetStarRating setStarRating:]
+ -[PFImageMetadataChangePolicySetStarRating starRating]
+ -[PFImageMetadataChangePolicySetTitle .cxx_destruct]
+ -[PFImageMetadataChangePolicySetTitle encodeWithCoder:]
+ -[PFImageMetadataChangePolicySetTitle initWithCoder:]
+ -[PFImageMetadataChangePolicySetTitle metadataNeedsProcessing:]
+ -[PFImageMetadataChangePolicySetTitle processMetadata:]
+ -[PFImageMetadataChangePolicySetTitle setTitle:]
+ -[PFImageMetadataChangePolicySetTitle title]
+ -[PFMetadata starRating]
+ -[PFMetadataBuilder setStarRating:]
+ -[PFMetadataBuilder starRating]
+ -[PFMetadataImage starRating]
+ -[PFMetadataMovie starRating]
+ -[PFPosterLayout isAnyFrameUsingHeadroom]
+ -[PFPosterOrientedLayout isAnyFrameUsingHeadroom]
+ -[PFSharingRemakerOptions customStarRating]
+ -[PFSharingRemakerOptions customTitle]
+ -[PFSharingRemakerOptions setCustomStarRating:]
+ -[PFSharingRemakerOptions setCustomTitle:]
+ -[PFSharingRemakerOptions setShouldStripRating:]
+ -[PFSharingRemakerOptions setShouldStripTitle:]
+ -[PFSharingRemakerOptions shouldStripRating]
+ -[PFSharingRemakerOptions shouldStripTitle]
+ -[PFVideoMetadataBuilder starRatingItem]
+ -[PFVideoSharingOperation customStarRating]
+ -[PFVideoSharingOperation customTitle]
+ -[PFVideoSharingOperation setCustomStarRating:]
+ -[PFVideoSharingOperation setCustomTitle:]
+ -[PFVideoSharingOperation setShouldStripRating:]
+ -[PFVideoSharingOperation setShouldStripTitle:]
+ -[PFVideoSharingOperation shouldStripRating]
+ -[PFVideoSharingOperation shouldStripTitle]
+ GCC_except_table1180
+ GCC_except_table1559
+ GCC_except_table1566
+ GCC_except_table1569
+ GCC_except_table1604
+ GCC_except_table1620
+ GCC_except_table1726
+ GCC_except_table1779
+ GCC_except_table1805
+ GCC_except_table1807
+ GCC_except_table1891
+ GCC_except_table1895
+ GCC_except_table1906
+ GCC_except_table1945
+ GCC_except_table1947
+ GCC_except_table1972
+ GCC_except_table1983
+ GCC_except_table2010
+ GCC_except_table2018
+ GCC_except_table2021
+ GCC_except_table2035
+ GCC_except_table2065
+ GCC_except_table2070
+ GCC_except_table2081
+ GCC_except_table2188
+ GCC_except_table2227
+ GCC_except_table2291
+ GCC_except_table2302
+ GCC_except_table2324
+ GCC_except_table2400
+ GCC_except_table2405
+ GCC_except_table2412
+ GCC_except_table2516
+ GCC_except_table2621
+ GCC_except_table2622
+ GCC_except_table2629
+ GCC_except_table2631
+ GCC_except_table2632
+ GCC_except_table2637
+ GCC_except_table2668
+ GCC_except_table2691
+ GCC_except_table2693
+ GCC_except_table2821
+ GCC_except_table3102
+ GCC_except_table313
+ GCC_except_table3168
+ GCC_except_table3172
+ GCC_except_table3174
+ GCC_except_table3175
+ GCC_except_table3181
+ GCC_except_table3183
+ GCC_except_table3184
+ GCC_except_table3187
+ GCC_except_table3188
+ GCC_except_table3195
+ GCC_except_table3196
+ GCC_except_table3197
+ GCC_except_table3198
+ GCC_except_table3200
+ GCC_except_table3201
+ GCC_except_table3202
+ GCC_except_table3204
+ GCC_except_table3212
+ GCC_except_table3214
+ GCC_except_table3217
+ GCC_except_table3220
+ GCC_except_table3251
+ GCC_except_table3253
+ GCC_except_table3254
+ GCC_except_table3260
+ GCC_except_table3261
+ GCC_except_table3262
+ GCC_except_table3263
+ GCC_except_table3264
+ GCC_except_table3270
+ GCC_except_table3275
+ GCC_except_table3332
+ GCC_except_table3479
+ GCC_except_table3481
+ GCC_except_table3482
+ GCC_except_table3486
+ GCC_except_table3488
+ GCC_except_table3489
+ GCC_except_table3490
+ GCC_except_table3494
+ GCC_except_table3500
+ GCC_except_table3507
+ GCC_except_table3510
+ GCC_except_table3511
+ GCC_except_table3513
+ GCC_except_table3518
+ GCC_except_table3520
+ GCC_except_table3526
+ GCC_except_table3533
+ GCC_except_table3534
+ GCC_except_table3554
+ GCC_except_table3606
+ GCC_except_table3610
+ GCC_except_table3613
+ GCC_except_table3614
+ GCC_except_table3664
+ GCC_except_table3673
+ GCC_except_table3748
+ GCC_except_table3827
+ GCC_except_table3829
+ GCC_except_table3846
+ GCC_except_table3870
+ GCC_except_table3872
+ GCC_except_table3961
+ GCC_except_table4196
+ GCC_except_table4198
+ GCC_except_table4200
+ GCC_except_table4207
+ GCC_except_table4212
+ GCC_except_table4222
+ GCC_except_table4293
+ GCC_except_table4294
+ GCC_except_table4301
+ GCC_except_table4309
+ GCC_except_table4312
+ GCC_except_table4319
+ GCC_except_table4321
+ GCC_except_table4323
+ GCC_except_table4325
+ GCC_except_table4332
+ GCC_except_table4333
+ GCC_except_table4334
+ GCC_except_table4342
+ GCC_except_table4344
+ GCC_except_table4345
+ GCC_except_table4348
+ GCC_except_table4361
+ GCC_except_table4368
+ GCC_except_table4373
+ GCC_except_table4374
+ GCC_except_table4378
+ GCC_except_table4417
+ GCC_except_table4418
+ GCC_except_table4419
+ GCC_except_table4420
+ GCC_except_table4421
+ GCC_except_table4423
+ GCC_except_table4428
+ GCC_except_table4429
+ GCC_except_table4431
+ GCC_except_table4432
+ GCC_except_table4434
+ GCC_except_table4435
+ GCC_except_table4436
+ GCC_except_table4437
+ GCC_except_table4438
+ GCC_except_table4439
+ GCC_except_table4441
+ GCC_except_table4443
+ GCC_except_table4444
+ GCC_except_table4445
+ GCC_except_table4446
+ GCC_except_table4449
+ GCC_except_table4521
+ GCC_except_table4588
+ GCC_except_table4594
+ GCC_except_table4663
+ GCC_except_table4667
+ GCC_except_table4669
+ GCC_except_table4672
+ GCC_except_table4673
+ GCC_except_table4693
+ GCC_except_table4711
+ GCC_except_table4712
+ GCC_except_table4713
+ GCC_except_table4715
+ GCC_except_table4717
+ GCC_except_table4995
+ GCC_except_table5004
+ GCC_except_table5008
+ GCC_except_table665
+ GCC_except_table686
+ GCC_except_table689
+ GCC_except_table744
+ GCC_except_table751
+ GCC_except_table797
+ GCC_except_table810
+ GCC_except_table811
+ GCC_except_table814
+ GCC_except_table815
+ GCC_except_table822
+ GCC_except_table824
+ GCC_except_table825
+ GCC_except_table826
+ GCC_except_table827
+ GCC_except_table843
+ GCC_except_table849
+ GCC_except_table850
+ GCC_except_table852
+ GCC_except_table853
+ GCC_except_table855
+ GCC_except_table857
+ GCC_except_table858
+ GCC_except_table859
+ GCC_except_table862
+ GCC_except_table864
+ GCC_except_table865
+ GCC_except_table866
+ GCC_except_table867
+ GCC_except_table871
+ GCC_except_table876
+ GCC_except_table890
+ GCC_except_table892
+ GCC_except_table893
+ GCC_except_table894
+ OBJC_IVAR_$_PFContentProvenanceProcessedImageInfo._certificateChainDERData
+ OBJC_IVAR_$_PFImageMetadataChangePolicySetStarRating._starRating
+ OBJC_IVAR_$_PFImageMetadataChangePolicySetTitle._title
+ OBJC_IVAR_$_PFMetadataBuilder._starRating
+ OBJC_IVAR_$_PFSharingRemakerOptions._customStarRating
+ OBJC_IVAR_$_PFSharingRemakerOptions._customTitle
+ OBJC_IVAR_$_PFSharingRemakerOptions._shouldStripRating
+ OBJC_IVAR_$_PFSharingRemakerOptions._shouldStripTitle
+ OBJC_IVAR_$_PFVideoSharingOperation._customStarRating
+ OBJC_IVAR_$_PFVideoSharingOperation._customTitle
+ OBJC_IVAR_$_PFVideoSharingOperation._shouldStripRating
+ OBJC_IVAR_$_PFVideoSharingOperation._shouldStripTitle
+ _AVMetadataIdentifierQuickTimeMetadataRatingUser
+ _AVMetadataQuickTimeMetadataKeyRatingUser
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetStarRating
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetTitle
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicySetStarRating
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicySetTitle
+ _PFAssetBundleMetadataStarRatingKey
+ _PFFigDecodeOptionsWithMaxPixelSize
+ _PFFigEncodeOptionsWithTilingEnabled
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicySetStarRating
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicySetTitle
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicySetStarRating
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicySetTitle
+ __OBJC_$_INSTANCE_VARIABLES_PFImageMetadataChangePolicySetStarRating
+ __OBJC_$_INSTANCE_VARIABLES_PFImageMetadataChangePolicySetTitle
+ __OBJC_$_PROP_LIST_PFImageMetadataChangePolicySetStarRating
+ __OBJC_$_PROP_LIST_PFImageMetadataChangePolicySetTitle
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicySetStarRating
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicySetTitle
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicySetStarRating
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicySetTitle
+ ___29-[PFMetadataMovie starRating]_block_invoke
+ ___42-[PFVideoSharingOperation setCustomTitle:]_block_invoke
+ ___47-[PFVideoSharingOperation setCustomStarRating:]_block_invoke
+ ___47-[PFVideoSharingOperation setShouldStripTitle:]_block_invoke
+ ___48-[PFVideoSharingOperation setShouldStripRating:]_block_invoke
+ ___block_descriptor_104_e8_32s40r48r56r64r72r80r88r96r_e5_v8?0l
+ ___copy_helper_block_e8_32s40r48r56r64r72r80r88r96r
+ ___destroy_helper_block_e8_32s40r48r56r64r72r80r88r96r
+ _kCGImagePropertyIPTCStarRating
+ _kCMPhotoCompressionOption_Tiling
+ _kCMPhotoDecompressionOption_ApplyTransform
+ _kCMPhotoDecompressionOption_MaxPixelSize
+ _kCMPhotoProvenanceResult_CertificateChainData
+ _objc_msgSend$addStarRating:toAVMetadata:
+ _objc_msgSend$addTitle:toAVMetadata:
+ _objc_msgSend$customStarRating
+ _objc_msgSend$customTitle
+ _objc_msgSend$isAnyFrameUsingHeadroom
+ _objc_msgSend$setCertificateChainDERData:
+ _objc_msgSend$setCustomStarRating:
+ _objc_msgSend$setCustomTitle:
+ _objc_msgSend$setShouldStripRating:
+ _objc_msgSend$setShouldStripTitle:
+ _objc_msgSend$setStarRating:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$shouldStripRating
+ _objc_msgSend$shouldStripTitle
+ _objc_msgSend$starRating
+ _objc_msgSend$starRatingItem
- -[PFContentProvenanceResourceInfo developmentStatus]
- -[PFContentProvenanceResourceInfo timestampStatus]
- -[PFImageMetadataBuilder setPeopleNames:]
- -[PFMetadataBuilder combinedKeywordsAndPeople]
- -[PFMetadataBuilder peopleNames]
- -[PFMetadataBuilder setPeopleNames:]
- GCC_except_table1160
- GCC_except_table1538
- GCC_except_table1545
- GCC_except_table1548
- GCC_except_table1583
- GCC_except_table1599
- GCC_except_table1705
- GCC_except_table1758
- GCC_except_table1784
- GCC_except_table1786
- GCC_except_table1870
- GCC_except_table1874
- GCC_except_table1885
- GCC_except_table1924
- GCC_except_table1926
- GCC_except_table1951
- GCC_except_table1962
- GCC_except_table1989
- GCC_except_table1997
- GCC_except_table2000
- GCC_except_table2014
- GCC_except_table2039
- GCC_except_table2044
- GCC_except_table2049
- GCC_except_table2165
- GCC_except_table2204
- GCC_except_table2268
- GCC_except_table2279
- GCC_except_table2301
- GCC_except_table2369
- GCC_except_table2374
- GCC_except_table2381
- GCC_except_table2485
- GCC_except_table2587
- GCC_except_table2588
- GCC_except_table2595
- GCC_except_table2597
- GCC_except_table2598
- GCC_except_table2600
- GCC_except_table2603
- GCC_except_table2657
- GCC_except_table2659
- GCC_except_table2787
- GCC_except_table295
- GCC_except_table3067
- GCC_except_table3133
- GCC_except_table3134
- GCC_except_table3137
- GCC_except_table3139
- GCC_except_table3140
- GCC_except_table3144
- GCC_except_table3146
- GCC_except_table3148
- GCC_except_table3149
- GCC_except_table3150
- GCC_except_table3152
- GCC_except_table3153
- GCC_except_table3160
- GCC_except_table3161
- GCC_except_table3162
- GCC_except_table3163
- GCC_except_table3165
- GCC_except_table3166
- GCC_except_table3167
- GCC_except_table3177
- GCC_except_table3182
- GCC_except_table3192
- GCC_except_table3193
- GCC_except_table3194
- GCC_except_table3216
- GCC_except_table3218
- GCC_except_table3219
- GCC_except_table3225
- GCC_except_table3226
- GCC_except_table3235
- GCC_except_table3240
- GCC_except_table3297
- GCC_except_table3444
- GCC_except_table3446
- GCC_except_table3447
- GCC_except_table3448
- GCC_except_table3450
- GCC_except_table3451
- GCC_except_table3453
- GCC_except_table3454
- GCC_except_table3455
- GCC_except_table3459
- GCC_except_table3465
- GCC_except_table3472
- GCC_except_table3475
- GCC_except_table3476
- GCC_except_table3478
- GCC_except_table3484
- GCC_except_table3491
- GCC_except_table3498
- GCC_except_table3499
- GCC_except_table3571
- GCC_except_table3575
- GCC_except_table3578
- GCC_except_table3579
- GCC_except_table3629
- GCC_except_table3638
- GCC_except_table3713
- GCC_except_table3792
- GCC_except_table3794
- GCC_except_table3811
- GCC_except_table3835
- GCC_except_table3837
- GCC_except_table3926
- GCC_except_table4159
- GCC_except_table4161
- GCC_except_table4163
- GCC_except_table4170
- GCC_except_table4175
- GCC_except_table4185
- GCC_except_table4256
- GCC_except_table4257
- GCC_except_table4258
- GCC_except_table4262
- GCC_except_table4264
- GCC_except_table4271
- GCC_except_table4272
- GCC_except_table4275
- GCC_except_table4282
- GCC_except_table4284
- GCC_except_table4286
- GCC_except_table4287
- GCC_except_table4288
- GCC_except_table4296
- GCC_except_table4297
- GCC_except_table4304
- GCC_except_table4305
- GCC_except_table4307
- GCC_except_table4311
- GCC_except_table4331
- GCC_except_table4337
- GCC_except_table4346
- GCC_except_table4375
- GCC_except_table4380
- GCC_except_table4381
- GCC_except_table4382
- GCC_except_table4384
- GCC_except_table4386
- GCC_except_table4391
- GCC_except_table4392
- GCC_except_table4394
- GCC_except_table4395
- GCC_except_table4397
- GCC_except_table4398
- GCC_except_table4399
- GCC_except_table4400
- GCC_except_table4401
- GCC_except_table4402
- GCC_except_table4404
- GCC_except_table4406
- GCC_except_table4407
- GCC_except_table4408
- GCC_except_table4409
- GCC_except_table4484
- GCC_except_table4551
- GCC_except_table4557
- GCC_except_table4626
- GCC_except_table4630
- GCC_except_table4632
- GCC_except_table4635
- GCC_except_table4636
- GCC_except_table4656
- GCC_except_table4674
- GCC_except_table4675
- GCC_except_table4676
- GCC_except_table4678
- GCC_except_table4680
- GCC_except_table4944
- GCC_except_table4953
- GCC_except_table4957
- GCC_except_table647
- GCC_except_table668
- GCC_except_table671
- GCC_except_table725
- GCC_except_table732
- GCC_except_table773
- GCC_except_table777
- GCC_except_table778
- GCC_except_table787
- GCC_except_table790
- GCC_except_table791
- GCC_except_table794
- GCC_except_table795
- GCC_except_table802
- GCC_except_table803
- GCC_except_table804
- GCC_except_table805
- GCC_except_table806
- GCC_except_table812
- GCC_except_table819
- GCC_except_table829
- GCC_except_table830
- GCC_except_table831
- GCC_except_table835
- GCC_except_table836
- GCC_except_table837
- GCC_except_table842
- GCC_except_table844
- GCC_except_table845
- GCC_except_table846
- GCC_except_table847
- GCC_except_table870
- GCC_except_table872
- GCC_except_table873
- GCC_except_table874
- OBJC_IVAR_$_PFContentProvenanceResourceInfo._developmentStatus
- OBJC_IVAR_$_PFContentProvenanceResourceInfo._timestampStatus
- OBJC_IVAR_$_PFMetadataBuilder._peopleNames
- ___block_descriptor_88_e8_32s40r48r56r64r72r80r_e5_v8?0l
- ___copy_helper_block_e8_32s40r48r56r64r72r80r
- ___destroy_helper_block_e8_32s40r48r56r64r72r80r
- _kCGImagePropertyIPTCExtPersonInImage
- _objc_msgSend$combinedKeywordsAndPeople
- _objc_msgSend$peopleNames
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
+ "Adding star rating to video"
+ "Adding title to video: %{private}@"
+ "PFAssetBundleMetadataStarRatingKey"
+ "Unknown AppleMakerNoteCamera: %ld, assuming non-front camera"
+ "[PFSharingRemaker] Beginning remake with options:\nshouldStripLocation: %@\nshouldStripCaption: %@\nshouldStripAccessibilityDescription: %@\nshouldStripKeywords: %@\nshouldStripRating: %@\nshouldStripTitle: %@\nshouldStripAllMetadata: %@\nshouldConvertToSRGB: %@\ncustomLocation: %{private}@\ncustomDate: %{private}@\ncustomCaption: %{private}@\ncustomAccessibilityLabel: %{private}@\ncustomKeywords: %{private}@\ncustomStarRating: %{private}@\ncustomTitle: %{private}@\noutputDirectoryURL: %{public}@\noutputFilename: %{public}@\nexportPreset: %{public}@\nexportFileType: %{public}@\n"
+ "[PFVideoSharingOperation] Applying custom star rating to metadata: %{private}@"
+ "[PFVideoSharingOperation] Applying custom title to metadata: %{private}@"
+ "[PFVideoSharingOperation] Stripping star rating from metadata"
+ "[PFVideoSharingOperation] Stripping title from metadata"
+ "newVisibleFrame after horizontal clamp 1: %@"
+ "newVisibleFrame after horizontal clamp 2: %@"
+ "starRating"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
- "[PFSharingRemaker] Beginning remake with options:\nshouldStripLocation: %@\nshouldStripCaption: %@\nshouldStripAccessibilityDescription: %@\nshouldStripKeywords: %@\nshouldStripAllMetadata: %@\nshouldConvertToSRGB: %@\ncustomLocation: %{private}@\ncustomDate: %{private}@\ncustomCaption: %{private}@\ncustomAccessibilityLabel: %{private}@\ncustomKeywords: %{private}@\noutputDirectoryURL: %{public}@\noutputFilename: %{public}@\nexportPreset: %{public}@\nexportFileType: %{public}@\n"
```
