## PhotosFormats

> `/System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0xe4910
-  __TEXT.__objc_methlist: 0xce18
+916.58.114.0.0
+  __TEXT.__text: 0xe74c0
+  __TEXT.__objc_methlist: 0xd090
   __TEXT.__const: 0x3390
   __TEXT.__dlopen_cstrs: 0x43
-  __TEXT.__cstring: 0xe28e
+  __TEXT.__cstring: 0xe339
   __TEXT.__constg_swiftt: 0xa0
   __TEXT.__swift5_typeref: 0xeb
   __TEXT.__swift5_reflstr: 0x162
   __TEXT.__swift5_fieldmd: 0xf4
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0x2c34
-  __TEXT.__oslogstring: 0x7137
+  __TEXT.__gcc_except_tab: 0x2cc4
+  __TEXT.__oslogstring: 0x74cb
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x3540
+  __TEXT.__unwind_info: 0x35c0
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
+  __DATA_CONST.__objc_selrefs: 0x6448
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x3b8
+  __DATA_CONST.__objc_superrefs: 0x3c8
   __DATA_CONST.__objc_arraydata: 0x800
-  __DATA_CONST.__got: 0x1758
+  __DATA_CONST.__got: 0x17b0
   __AUTH_CONST.__const: 0x3568
-  __AUTH_CONST.__cfstring: 0xcda0
-  __AUTH_CONST.__objc_const: 0x15050
+  __AUTH_CONST.__cfstring: 0xce20
+  __AUTH_CONST.__objc_const: 0x153c8
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__objc_intobj: 0x900
+  __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x208
-  __AUTH_CONST.__auth_got: 0x10a0
+  __AUTH_CONST.__auth_got: 0x10a8
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x7a0
-  __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0xd74
-  __DATA.__data: 0xda8
+  __DATA.__objc_ivar: 0xd9c
+  __DATA.__data: 0xe0
   __DATA.__bss: 0xdf8
-  __DATA_DIRTY.__objc_data: 0x2f80
+  __DATA_DIRTY.__objc_data: 0x37c0
+  __DATA_DIRTY.__data: 0xd88
   __DATA_DIRTY.__bss: 0x748
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5109
-  Symbols:   11954
-  CStrings:  2586
+  Functions: 5165
+  Symbols:   12066
+  CStrings:  2603
 
Symbols:
+ +[PFContentProvenanceEmbeddedImageWriter outputContentTypeForRegularImageContentType:]
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
+ -[PFMetadata sizeAndDateResourceValues]
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
+ GCC_except_table1182
+ GCC_except_table1563
+ GCC_except_table1570
+ GCC_except_table1573
+ GCC_except_table1608
+ GCC_except_table1624
+ GCC_except_table1730
+ GCC_except_table1783
+ GCC_except_table1809
+ GCC_except_table1811
+ GCC_except_table1895
+ GCC_except_table1899
+ GCC_except_table1910
+ GCC_except_table1949
+ GCC_except_table1976
+ GCC_except_table1987
+ GCC_except_table2022
+ GCC_except_table2025
+ GCC_except_table2064
+ GCC_except_table2069
+ GCC_except_table2074
+ GCC_except_table2085
+ GCC_except_table2192
+ GCC_except_table2231
+ GCC_except_table2295
+ GCC_except_table2306
+ GCC_except_table2328
+ GCC_except_table2404
+ GCC_except_table2409
+ GCC_except_table2416
+ GCC_except_table2520
+ GCC_except_table2625
+ GCC_except_table2626
+ GCC_except_table2633
+ GCC_except_table2635
+ GCC_except_table2636
+ GCC_except_table2638
+ GCC_except_table2641
+ GCC_except_table2672
+ GCC_except_table2695
+ GCC_except_table2697
+ GCC_except_table2825
+ GCC_except_table3106
+ GCC_except_table313
+ GCC_except_table3172
+ GCC_except_table3173
+ GCC_except_table3176
+ GCC_except_table3178
+ GCC_except_table3183
+ GCC_except_table3187
+ GCC_except_table3188
+ GCC_except_table3189
+ GCC_except_table3191
+ GCC_except_table3199
+ GCC_except_table3200
+ GCC_except_table3201
+ GCC_except_table3202
+ GCC_except_table3204
+ GCC_except_table3205
+ GCC_except_table3206
+ GCC_except_table3208
+ GCC_except_table3221
+ GCC_except_table3224
+ GCC_except_table3231
+ GCC_except_table3232
+ GCC_except_table3233
+ GCC_except_table3255
+ GCC_except_table3257
+ GCC_except_table3258
+ GCC_except_table3264
+ GCC_except_table3265
+ GCC_except_table3266
+ GCC_except_table3267
+ GCC_except_table3268
+ GCC_except_table3274
+ GCC_except_table3279
+ GCC_except_table3336
+ GCC_except_table3486
+ GCC_except_table3487
+ GCC_except_table3489
+ GCC_except_table3490
+ GCC_except_table3492
+ GCC_except_table3493
+ GCC_except_table3494
+ GCC_except_table3504
+ GCC_except_table3511
+ GCC_except_table3514
+ GCC_except_table3515
+ GCC_except_table3517
+ GCC_except_table3522
+ GCC_except_table3523
+ GCC_except_table3524
+ GCC_except_table3530
+ GCC_except_table3537
+ GCC_except_table3538
+ GCC_except_table3558
+ GCC_except_table3610
+ GCC_except_table3614
+ GCC_except_table3617
+ GCC_except_table3618
+ GCC_except_table3668
+ GCC_except_table3677
+ GCC_except_table3752
+ GCC_except_table3831
+ GCC_except_table3833
+ GCC_except_table3850
+ GCC_except_table3874
+ GCC_except_table3876
+ GCC_except_table3965
+ GCC_except_table4200
+ GCC_except_table4202
+ GCC_except_table4204
+ GCC_except_table4211
+ GCC_except_table4216
+ GCC_except_table4226
+ GCC_except_table4298
+ GCC_except_table4300
+ GCC_except_table4306
+ GCC_except_table4313
+ GCC_except_table4314
+ GCC_except_table4317
+ GCC_except_table4326
+ GCC_except_table4328
+ GCC_except_table4329
+ GCC_except_table4330
+ GCC_except_table4338
+ GCC_except_table4339
+ GCC_except_table4347
+ GCC_except_table4349
+ GCC_except_table4350
+ GCC_except_table4353
+ GCC_except_table4366
+ GCC_except_table4373
+ GCC_except_table4378
+ GCC_except_table4379
+ GCC_except_table4388
+ GCC_except_table4417
+ GCC_except_table4422
+ GCC_except_table4423
+ GCC_except_table4424
+ GCC_except_table4425
+ GCC_except_table4426
+ GCC_except_table4428
+ GCC_except_table4433
+ GCC_except_table4434
+ GCC_except_table4436
+ GCC_except_table4437
+ GCC_except_table4439
+ GCC_except_table4440
+ GCC_except_table4441
+ GCC_except_table4442
+ GCC_except_table4443
+ GCC_except_table4444
+ GCC_except_table4446
+ GCC_except_table4448
+ GCC_except_table4449
+ GCC_except_table4450
+ GCC_except_table4451
+ GCC_except_table4454
+ GCC_except_table4526
+ GCC_except_table4593
+ GCC_except_table4599
+ GCC_except_table4668
+ GCC_except_table4672
+ GCC_except_table4677
+ GCC_except_table4698
+ GCC_except_table4716
+ GCC_except_table4717
+ GCC_except_table4718
+ GCC_except_table4720
+ GCC_except_table4722
+ GCC_except_table5000
+ GCC_except_table5009
+ GCC_except_table5013
+ GCC_except_table666
+ GCC_except_table687
+ GCC_except_table690
+ GCC_except_table746
+ GCC_except_table753
+ GCC_except_table799
+ GCC_except_table800
+ GCC_except_table809
+ GCC_except_table815
+ GCC_except_table816
+ GCC_except_table817
+ GCC_except_table820
+ GCC_except_table824
+ GCC_except_table825
+ GCC_except_table826
+ GCC_except_table827
+ GCC_except_table828
+ GCC_except_table834
+ GCC_except_table840
+ GCC_except_table841
+ GCC_except_table852
+ GCC_except_table853
+ GCC_except_table854
+ GCC_except_table855
+ GCC_except_table857
+ GCC_except_table858
+ GCC_except_table859
+ GCC_except_table860
+ GCC_except_table861
+ GCC_except_table864
+ GCC_except_table866
+ GCC_except_table867
+ GCC_except_table868
+ GCC_except_table869
+ GCC_except_table878
+ GCC_except_table892
+ GCC_except_table894
+ GCC_except_table895
+ GCC_except_table896
+ OBJC_IVAR_$_PFContentProvenanceProcessedImageInfo._certificateChainDERData
+ OBJC_IVAR_$_PFImageMetadataChangePolicySetStarRating._starRating
+ OBJC_IVAR_$_PFImageMetadataChangePolicySetTitle._title
+ OBJC_IVAR_$_PFMetadata._sizeAndDateResourceValues
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
+ _CMPhotoCodecSessionPoolFlush
+ _NSURLContentModificationDateKey
+ _NSURLCreationDateKey
+ _NSURLFileSizeKey
+ _NSURLIsAliasFileKey
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetStarRating
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetTitle
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicySetStarRating
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicySetTitle
+ _PFAssetBundleMetadataStarRatingKey
+ _PFFigDecodeOptionsWithMaxPixelSize
+ _PFFigEncodeOptionsWithTilingEnabled
+ _PFMetadataRealPathFromFileAlias
+ _PFPosterSanitizedNormalizedFrame
+ __OBJC_$_CLASS_METHODS_PFContentProvenanceEmbeddedImageWriter
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
+ __PFDecodeImageFromSource
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
+ _objc_msgSend$outputContentTypeForRegularImageContentType:
+ _objc_msgSend$resourceValuesForKeys:error:
+ _objc_msgSend$setCertificateChainDERData:
+ _objc_msgSend$setCustomStarRating:
+ _objc_msgSend$setCustomTitle:
+ _objc_msgSend$setShouldStripRating:
+ _objc_msgSend$setShouldStripTitle:
+ _objc_msgSend$setStarRating:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$shouldStripRating
+ _objc_msgSend$shouldStripTitle
+ _objc_msgSend$sizeAndDateResourceValues
+ _objc_msgSend$starRating
+ _objc_msgSend$starRatingItem
+ _objc_msgSend$writeToFile:options:error:
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
- GCC_except_table1962
- GCC_except_table1989
- GCC_except_table1997
- GCC_except_table2000
- GCC_except_table2044
- GCC_except_table2049
- GCC_except_table2060
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
- GCC_except_table2634
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
- GCC_except_table3169
- GCC_except_table3177
- GCC_except_table3182
- GCC_except_table3193
- GCC_except_table3194
- GCC_except_table3219
- GCC_except_table3225
- GCC_except_table3226
- GCC_except_table3227
- GCC_except_table3228
- GCC_except_table3229
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
- GCC_except_table3499
- GCC_except_table3519
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
- GCC_except_table4295
- GCC_except_table4296
- GCC_except_table4297
- GCC_except_table4305
- GCC_except_table4307
- GCC_except_table4308
- GCC_except_table4311
- GCC_except_table4331
- GCC_except_table4336
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
- GCC_except_table4412
- GCC_except_table4484
- GCC_except_table4551
- GCC_except_table4557
- GCC_except_table4626
- GCC_except_table4630
- GCC_except_table4632
- GCC_except_table4635
- GCC_except_table4636
- GCC_except_table4656
- GCC_except_table4675
- GCC_except_table4676
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
- GCC_except_table793
- GCC_except_table794
- GCC_except_table798
- GCC_except_table802
- GCC_except_table803
- GCC_except_table804
- GCC_except_table805
- GCC_except_table806
- GCC_except_table807
- GCC_except_table818
- GCC_except_table819
- GCC_except_table823
- GCC_except_table830
- GCC_except_table831
- GCC_except_table832
- GCC_except_table833
- GCC_except_table836
- GCC_except_table837
- GCC_except_table838
- GCC_except_table839
- GCC_except_table842
- GCC_except_table844
- GCC_except_table846
- GCC_except_table847
- GCC_except_table856
- GCC_except_table870
- GCC_except_table872
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
- _objc_msgSend$writeToFile:atomically:
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
+ "Adding star rating to video"
+ "Adding title to video: %{private}@"
+ "Could not mark live photo bundle at '%{public}@' as a package: %{public}@"
+ "Couldn't read file resource values for URL '%@' (ERROR: %@)"
+ "Decoded PFPosterEditConfiguration contains a degenerate %{public}@ %{public}@, ignored."
+ "Failed to write asset bundle to '%@' for an unknown reason"
+ "PFAssetBundleMetadataStarRatingKey"
+ "PFImageDecoding: decode rejected the image format, retrying with a fresh decode session"
+ "[PFAssetBundle] Could not mark asset bundle at '%{public}@' as a package: %{public}@"
+ "[PFSharingRemaker] Beginning remake with options:\nshouldStripLocation: %@\nshouldStripCaption: %@\nshouldStripAccessibilityDescription: %@\nshouldStripKeywords: %@\nshouldStripRating: %@\nshouldStripTitle: %@\nshouldStripAllMetadata: %@\nshouldConvertToSRGB: %@\ncustomLocation: %{private}@\ncustomDate: %{private}@\ncustomCaption: %{private}@\ncustomAccessibilityLabel: %{private}@\ncustomKeywords: %{private}@\ncustomStarRating: %{private}@\ncustomTitle: %{private}@\noutputDirectoryURL: %{public}@\noutputFilename: %{public}@\nexportPreset: %{public}@\nexportFileType: %{public}@\n"
+ "[PFVideoSharingOperation] Applying custom star rating to metadata: %{private}@"
+ "[PFVideoSharingOperation] Applying custom title to metadata: %{private}@"
+ "[PFVideoSharingOperation] Stripping star rating from metadata"
+ "[PFVideoSharingOperation] Stripping title from metadata"
+ "failed to write live photo bundle to '%@' for an unknown reason"
+ "newVisibleFrame after horizontal clamp 1: %@"
+ "newVisibleFrame after horizontal clamp 2: %@"
+ "starRating"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
- "[PFSharingRemaker] Beginning remake with options:\nshouldStripLocation: %@\nshouldStripCaption: %@\nshouldStripAccessibilityDescription: %@\nshouldStripKeywords: %@\nshouldStripAllMetadata: %@\nshouldConvertToSRGB: %@\ncustomLocation: %{private}@\ncustomDate: %{private}@\ncustomCaption: %{private}@\ncustomAccessibilityLabel: %{private}@\ncustomKeywords: %{private}@\noutputDirectoryURL: %{public}@\noutputFilename: %{public}@\nexportPreset: %{public}@\nexportFileType: %{public}@\n"
```
