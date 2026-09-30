## PhotosFormats

> `/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats`

```diff

-912.0.235.0.0
-  __TEXT.__text: 0xd9ce4
-  __TEXT.__objc_methlist: 0xcfc0
+916.40.110.0.0
+  __TEXT.__text: 0xdb550
+  __TEXT.__objc_methlist: 0xd1e8
   __TEXT.__const: 0x33a0
   __TEXT.__dlopen_cstrs: 0x1b7
-  __TEXT.__cstring: 0xe147
+  __TEXT.__cstring: 0xe177
   __TEXT.__constg_swiftt: 0xa0
   __TEXT.__swift5_typeref: 0xeb
   __TEXT.__swift5_reflstr: 0x162
   __TEXT.__swift5_fieldmd: 0xf4
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0x2da4
-  __TEXT.__oslogstring: 0x7954
+  __TEXT.__gcc_except_tab: 0x2ddc
+  __TEXT.__oslogstring: 0x7b40
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x41b0
+  __TEXT.__unwind_info: 0x4240
   __TEXT.__eh_frame: 0x380
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2b18
-  __DATA_CONST.__objc_classlist: 0x590
+  __DATA_CONST.__const: 0x2b20
+  __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x64f0
+  __DATA_CONST.__objc_selrefs: 0x6550
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x3c0
+  __DATA_CONST.__objc_superrefs: 0x3d0
   __DATA_CONST.__objc_arraydata: 0x800
-  __DATA_CONST.__got: 0x17a0
+  __DATA_CONST.__got: 0x17d0
   __AUTH_CONST.__const: 0x1da8
-  __AUTH_CONST.__cfstring: 0xcc80
-  __AUTH_CONST.__objc_const: 0x15380
+  __AUTH_CONST.__cfstring: 0xccc0
+  __AUTH_CONST.__objc_const: 0x156a8
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__objc_intobj: 0x900
+  __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH_CONST.__auth_got: 0x10e8
-  __AUTH.__objc_data: 0x7a0
+  __AUTH.__objc_data: 0x840
   __AUTH.__data: 0xd0
-  __DATA.__objc_ivar: 0xd8c
+  __DATA.__objc_ivar: 0xdb0
   __DATA.__data: 0xe58
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3020

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5090
-  Symbols:   12022
-  CStrings:  2616
+  Functions: 5138
+  Symbols:   12115
+  CStrings:  2625
 
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
+ GCC_except_table1162
+ GCC_except_table1541
+ GCC_except_table1548
+ GCC_except_table1551
+ GCC_except_table1586
+ GCC_except_table1600
+ GCC_except_table1706
+ GCC_except_table1780
+ GCC_except_table1782
+ GCC_except_table1858
+ GCC_except_table1862
+ GCC_except_table1873
+ GCC_except_table1912
+ GCC_except_table1914
+ GCC_except_table1940
+ GCC_except_table1951
+ GCC_except_table1977
+ GCC_except_table1985
+ GCC_except_table1988
+ GCC_except_table2003
+ GCC_except_table2033
+ GCC_except_table2038
+ GCC_except_table2049
+ GCC_except_table2154
+ GCC_except_table2185
+ GCC_except_table2192
+ GCC_except_table2195
+ GCC_except_table2201
+ GCC_except_table2205
+ GCC_except_table2219
+ GCC_except_table2283
+ GCC_except_table2292
+ GCC_except_table2312
+ GCC_except_table2388
+ GCC_except_table2391
+ GCC_except_table2398
+ GCC_except_table2502
+ GCC_except_table2518
+ GCC_except_table2616
+ GCC_except_table2617
+ GCC_except_table2624
+ GCC_except_table2626
+ GCC_except_table2627
+ GCC_except_table2629
+ GCC_except_table2632
+ GCC_except_table2676
+ GCC_except_table2699
+ GCC_except_table2701
+ GCC_except_table2829
+ GCC_except_table303
+ GCC_except_table3110
+ GCC_except_table3177
+ GCC_except_table3180
+ GCC_except_table3182
+ GCC_except_table3183
+ GCC_except_table3187
+ GCC_except_table3189
+ GCC_except_table3192
+ GCC_except_table3193
+ GCC_except_table3195
+ GCC_except_table3196
+ GCC_except_table3204
+ GCC_except_table3205
+ GCC_except_table3206
+ GCC_except_table3208
+ GCC_except_table3209
+ GCC_except_table3210
+ GCC_except_table3212
+ GCC_except_table3220
+ GCC_except_table3222
+ GCC_except_table3259
+ GCC_except_table3261
+ GCC_except_table3262
+ GCC_except_table3268
+ GCC_except_table3269
+ GCC_except_table3270
+ GCC_except_table3271
+ GCC_except_table3272
+ GCC_except_table3278
+ GCC_except_table3281
+ GCC_except_table3338
+ GCC_except_table3487
+ GCC_except_table3488
+ GCC_except_table3489
+ GCC_except_table3494
+ GCC_except_table3495
+ GCC_except_table3496
+ GCC_except_table3500
+ GCC_except_table3513
+ GCC_except_table3516
+ GCC_except_table3517
+ GCC_except_table3519
+ GCC_except_table3524
+ GCC_except_table3525
+ GCC_except_table3526
+ GCC_except_table3532
+ GCC_except_table3539
+ GCC_except_table3540
+ GCC_except_table3557
+ GCC_except_table3603
+ GCC_except_table3607
+ GCC_except_table3610
+ GCC_except_table3611
+ GCC_except_table3661
+ GCC_except_table3670
+ GCC_except_table3745
+ GCC_except_table3813
+ GCC_except_table3815
+ GCC_except_table3832
+ GCC_except_table3842
+ GCC_except_table3857
+ GCC_except_table3859
+ GCC_except_table3948
+ GCC_except_table4183
+ GCC_except_table4185
+ GCC_except_table4187
+ GCC_except_table4194
+ GCC_except_table4199
+ GCC_except_table4209
+ GCC_except_table4280
+ GCC_except_table4281
+ GCC_except_table4282
+ GCC_except_table4288
+ GCC_except_table4296
+ GCC_except_table4299
+ GCC_except_table4306
+ GCC_except_table4308
+ GCC_except_table4310
+ GCC_except_table4311
+ GCC_except_table4312
+ GCC_except_table4319
+ GCC_except_table4320
+ GCC_except_table4323
+ GCC_except_table4328
+ GCC_except_table4329
+ GCC_except_table4332
+ GCC_except_table4335
+ GCC_except_table4348
+ GCC_except_table4355
+ GCC_except_table4360
+ GCC_except_table4361
+ GCC_except_table4404
+ GCC_except_table4405
+ GCC_except_table4406
+ GCC_except_table4407
+ GCC_except_table4408
+ GCC_except_table4410
+ GCC_except_table4415
+ GCC_except_table4416
+ GCC_except_table4418
+ GCC_except_table4419
+ GCC_except_table4421
+ GCC_except_table4422
+ GCC_except_table4423
+ GCC_except_table4424
+ GCC_except_table4425
+ GCC_except_table4426
+ GCC_except_table4428
+ GCC_except_table4430
+ GCC_except_table4431
+ GCC_except_table4432
+ GCC_except_table4433
+ GCC_except_table4436
+ GCC_except_table4508
+ GCC_except_table4575
+ GCC_except_table4581
+ GCC_except_table4650
+ GCC_except_table4654
+ GCC_except_table4656
+ GCC_except_table4659
+ GCC_except_table4678
+ GCC_except_table4694
+ GCC_except_table4695
+ GCC_except_table4696
+ GCC_except_table4698
+ GCC_except_table4700
+ GCC_except_table4978
+ GCC_except_table4985
+ GCC_except_table4987
+ GCC_except_table651
+ GCC_except_table667
+ GCC_except_table670
+ GCC_except_table729
+ GCC_except_table736
+ GCC_except_table780
+ GCC_except_table793
+ GCC_except_table794
+ GCC_except_table797
+ GCC_except_table798
+ GCC_except_table805
+ GCC_except_table807
+ GCC_except_table808
+ GCC_except_table809
+ GCC_except_table810
+ GCC_except_table826
+ GCC_except_table832
+ GCC_except_table833
+ GCC_except_table835
+ GCC_except_table836
+ GCC_except_table838
+ GCC_except_table840
+ GCC_except_table841
+ GCC_except_table842
+ GCC_except_table845
+ GCC_except_table847
+ GCC_except_table848
+ GCC_except_table849
+ GCC_except_table850
+ GCC_except_table854
+ GCC_except_table859
+ GCC_except_table873
+ GCC_except_table875
+ GCC_except_table876
+ GCC_except_table877
+ _AVMetadataIdentifierQuickTimeMetadataRatingUser
+ _AVMetadataQuickTimeMetadataKeyRatingUser
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetStarRating
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetTitle
+ _OBJC_IVAR_$_PFContentProvenanceProcessedImageInfo._certificateChainDERData
+ _OBJC_IVAR_$_PFImageMetadataChangePolicySetStarRating._starRating
+ _OBJC_IVAR_$_PFImageMetadataChangePolicySetTitle._title
+ _OBJC_IVAR_$_PFMetadataBuilder._starRating
+ _OBJC_IVAR_$_PFSharingRemakerOptions._customStarRating
+ _OBJC_IVAR_$_PFSharingRemakerOptions._customTitle
+ _OBJC_IVAR_$_PFSharingRemakerOptions._shouldStripRating
+ _OBJC_IVAR_$_PFSharingRemakerOptions._shouldStripTitle
+ _OBJC_IVAR_$_PFVideoSharingOperation._customStarRating
+ _OBJC_IVAR_$_PFVideoSharingOperation._customTitle
+ _OBJC_IVAR_$_PFVideoSharingOperation._shouldStripRating
+ _OBJC_IVAR_$_PFVideoSharingOperation._shouldStripTitle
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
+ ___block_descriptor_104_e8_32s40r48r56r64r72r80r88r96r_e5_v8?0lr40l8s32l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8
+ _kCGImagePropertyIPTCStarRating
+ _kCMPhotoCompressionOption_Tiling
+ _kCMPhotoDecompressionOption_ApplyTransform
+ _kCMPhotoDecompressionOption_MaxPixelSize
+ _kCMPhotoProvenanceResult_CertificateChainData
+ _objc_msgSend$addStarRating:toAVMetadata:
+ _objc_msgSend$addTitle:toAVMetadata:
+ _objc_msgSend$customStarRating
+ _objc_msgSend$customTitle
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
- GCC_except_table1142
- GCC_except_table1520
- GCC_except_table1527
- GCC_except_table1530
- GCC_except_table1565
- GCC_except_table1579
- GCC_except_table1685
- GCC_except_table1738
- GCC_except_table1761
- GCC_except_table1837
- GCC_except_table1841
- GCC_except_table1852
- GCC_except_table1891
- GCC_except_table1893
- GCC_except_table1919
- GCC_except_table1930
- GCC_except_table1956
- GCC_except_table1964
- GCC_except_table1967
- GCC_except_table1982
- GCC_except_table2007
- GCC_except_table2012
- GCC_except_table2017
- GCC_except_table2131
- GCC_except_table2162
- GCC_except_table2169
- GCC_except_table2172
- GCC_except_table2178
- GCC_except_table2182
- GCC_except_table2196
- GCC_except_table2260
- GCC_except_table2269
- GCC_except_table2289
- GCC_except_table2357
- GCC_except_table2360
- GCC_except_table2367
- GCC_except_table2471
- GCC_except_table2487
- GCC_except_table2583
- GCC_except_table2584
- GCC_except_table2591
- GCC_except_table2593
- GCC_except_table2594
- GCC_except_table2596
- GCC_except_table2599
- GCC_except_table2643
- GCC_except_table2666
- GCC_except_table2668
- GCC_except_table2796
- GCC_except_table285
- GCC_except_table3076
- GCC_except_table3142
- GCC_except_table3143
- GCC_except_table3146
- GCC_except_table3148
- GCC_except_table3149
- GCC_except_table3153
- GCC_except_table3155
- GCC_except_table3157
- GCC_except_table3158
- GCC_except_table3159
- GCC_except_table3161
- GCC_except_table3162
- GCC_except_table3169
- GCC_except_table3170
- GCC_except_table3171
- GCC_except_table3172
- GCC_except_table3174
- GCC_except_table3175
- GCC_except_table3178
- GCC_except_table3186
- GCC_except_table3188
- GCC_except_table3194
- GCC_except_table3201
- GCC_except_table3202
- GCC_except_table3227
- GCC_except_table3234
- GCC_except_table3238
- GCC_except_table3244
- GCC_except_table3247
- GCC_except_table3304
- GCC_except_table3451
- GCC_except_table3453
- GCC_except_table3454
- GCC_except_table3455
- GCC_except_table3457
- GCC_except_table3458
- GCC_except_table3460
- GCC_except_table3461
- GCC_except_table3462
- GCC_except_table3466
- GCC_except_table3472
- GCC_except_table3479
- GCC_except_table3482
- GCC_except_table3483
- GCC_except_table3490
- GCC_except_table3498
- GCC_except_table3505
- GCC_except_table3523
- GCC_except_table3569
- GCC_except_table3573
- GCC_except_table3576
- GCC_except_table3577
- GCC_except_table3627
- GCC_except_table3636
- GCC_except_table3711
- GCC_except_table3779
- GCC_except_table3781
- GCC_except_table3798
- GCC_except_table3808
- GCC_except_table3823
- GCC_except_table3825
- GCC_except_table3914
- GCC_except_table4149
- GCC_except_table4151
- GCC_except_table4153
- GCC_except_table4160
- GCC_except_table4165
- GCC_except_table4175
- GCC_except_table4246
- GCC_except_table4247
- GCC_except_table4248
- GCC_except_table4252
- GCC_except_table4254
- GCC_except_table4261
- GCC_except_table4262
- GCC_except_table4265
- GCC_except_table4272
- GCC_except_table4274
- GCC_except_table4276
- GCC_except_table4277
- GCC_except_table4278
- GCC_except_table4285
- GCC_except_table4287
- GCC_except_table4289
- GCC_except_table4294
- GCC_except_table4297
- GCC_except_table4298
- GCC_except_table4301
- GCC_except_table4314
- GCC_except_table4326
- GCC_except_table4327
- GCC_except_table4336
- GCC_except_table4371
- GCC_except_table4372
- GCC_except_table4373
- GCC_except_table4374
- GCC_except_table4376
- GCC_except_table4381
- GCC_except_table4382
- GCC_except_table4384
- GCC_except_table4385
- GCC_except_table4387
- GCC_except_table4388
- GCC_except_table4389
- GCC_except_table4390
- GCC_except_table4391
- GCC_except_table4392
- GCC_except_table4394
- GCC_except_table4396
- GCC_except_table4397
- GCC_except_table4398
- GCC_except_table4402
- GCC_except_table4474
- GCC_except_table4541
- GCC_except_table4547
- GCC_except_table4616
- GCC_except_table4620
- GCC_except_table4622
- GCC_except_table4625
- GCC_except_table4626
- GCC_except_table4644
- GCC_except_table4661
- GCC_except_table4662
- GCC_except_table4664
- GCC_except_table4666
- GCC_except_table4930
- GCC_except_table4937
- GCC_except_table4939
- GCC_except_table633
- GCC_except_table649
- GCC_except_table652
- GCC_except_table710
- GCC_except_table717
- GCC_except_table756
- GCC_except_table760
- GCC_except_table761
- GCC_except_table770
- GCC_except_table773
- GCC_except_table774
- GCC_except_table777
- GCC_except_table778
- GCC_except_table785
- GCC_except_table786
- GCC_except_table787
- GCC_except_table788
- GCC_except_table789
- GCC_except_table795
- GCC_except_table802
- GCC_except_table812
- GCC_except_table813
- GCC_except_table814
- GCC_except_table818
- GCC_except_table819
- GCC_except_table820
- GCC_except_table825
- GCC_except_table827
- GCC_except_table828
- GCC_except_table829
- GCC_except_table830
- GCC_except_table853
- GCC_except_table855
- GCC_except_table856
- GCC_except_table857
- _OBJC_IVAR_$_PFContentProvenanceResourceInfo._developmentStatus
- _OBJC_IVAR_$_PFContentProvenanceResourceInfo._timestampStatus
- _OBJC_IVAR_$_PFMetadataBuilder._peopleNames
- ___block_descriptor_88_e8_32s40r48r56r64r72r80r_e5_v8?0lr40l8s32l8r48l8r56l8r64l8r72l8r80l8
- _kCGImagePropertyIPTCExtPersonInImage
- _objc_msgSend$combinedKeywordsAndPeople
- _objc_msgSend$peopleNames
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
+ "Adding star rating to video"
+ "Adding title to video: %{private}@"
+ "PFAssetBundleMetadataStarRatingKey"
+ "Unknown AppleMakerNoteCamera: %ld, assuming non-front camera"
+ "[PFSharingRemaker] Beginning remake with options:\nshouldStripLocation: %@\nshouldStripCaption: %@\nshouldStripAccessibilityDescription: %@\nshouldStripKeywords: %@\nshouldStripRating: %@\nshouldStripTitle: %@\nshouldStripAllMetadata: %@\nshouldConvertToSRGB: %@\ncustomLocation: %{private}@\ncustomDate: %{private}@\ncustomCaption: %{private}@\ncustomAccessibilityLabel: %{private}@\ncustomKeywords: %{private}@\ncustomStarRating: %{private}@\ncustomTitle: %{private}@\noutputDirectoryURL: %{public}@\noutputFilename: %{public}@\nexportPreset: %{public}@\nexportFileType: %{public}@\n"
+ "[PFVideoSharingOperation] Applying custom star rating to metadata: %{private}@"
+ "[PFVideoSharingOperation] Applying custom title to metadata: %{private}@"
+ "[PFVideoSharingOperation] Stripping star rating from metadata"
+ "[PFVideoSharingOperation] Stripping title from metadata"
+ "starRating"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
- "[PFSharingRemaker] Beginning remake with options:\nshouldStripLocation: %@\nshouldStripCaption: %@\nshouldStripAccessibilityDescription: %@\nshouldStripKeywords: %@\nshouldStripAllMetadata: %@\nshouldConvertToSRGB: %@\ncustomLocation: %{private}@\ncustomDate: %{private}@\ncustomCaption: %{private}@\ncustomAccessibilityLabel: %{private}@\ncustomKeywords: %{private}@\noutputDirectoryURL: %{public}@\noutputFilename: %{public}@\nexportPreset: %{public}@\nexportFileType: %{public}@\n"
```
