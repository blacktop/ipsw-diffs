## PhotosUIPrivate

> `/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate`

```diff

-916.45.110.0.0
-  __TEXT.__text: 0x5830dc
-  __TEXT.__objc_methlist: 0x4f73c
-  __TEXT.__const: 0x1ae88
+916.51.202.0.0
+  __TEXT.__text: 0x584368
+  __TEXT.__objc_methlist: 0x4f654
+  __TEXT.__const: 0x1af50
   __TEXT.__dlopen_cstrs: 0x69b
-  __TEXT.__swift5_typeref: 0x1747a
-  __TEXT.__constg_swiftt: 0xb144
+  __TEXT.__swift5_typeref: 0x174a0
+  __TEXT.__constg_swiftt: 0xb174
   __TEXT.__swift5_builtin: 0x744
-  __TEXT.__swift5_reflstr: 0x8a57
-  __TEXT.__swift5_fieldmd: 0x747c
-  __TEXT.__swift5_assocty: 0x1930
-  __TEXT.__cstring: 0x35057
-  __TEXT.__swift5_capture: 0x5888
+  __TEXT.__swift5_reflstr: 0x8b47
+  __TEXT.__swift5_fieldmd: 0x74dc
+  __TEXT.__swift5_assocty: 0x18e8
+  __TEXT.__cstring: 0x35248
+  __TEXT.__swift5_capture: 0x593c
   __TEXT.__swift5_proto: 0xd0c
-  __TEXT.__swift5_types: 0x794
+  __TEXT.__swift5_types: 0x798
   __TEXT.__swift5_protos: 0xa8
   __TEXT.__swift_as_entry: 0x310
   __TEXT.__swift_as_ret: 0x390
   __TEXT.__swift_as_cont: 0x7d0
-  __TEXT.__oslogstring: 0x1545d
+  __TEXT.__oslogstring: 0x155fe
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__gcc_except_tab: 0x8978
+  __TEXT.__gcc_except_tab: 0x8908
   __TEXT.__ustring: 0x146
-  __TEXT.__unwind_info: 0x1e3a8
-  __TEXT.__eh_frame: 0x9568
+  __TEXT.__unwind_info: 0x1e418
+  __TEXT.__eh_frame: 0x9588
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc5c8
+  __DATA_CONST.__const: 0xc5d0
   __DATA_CONST.__objc_classlist: 0x1e08
   __DATA_CONST.__objc_catlist: 0x1b8
   __DATA_CONST.__objc_catlist2: 0x10
-  __DATA_CONST.__objc_protolist: 0x1420
+  __DATA_CONST.__objc_protolist: 0x1410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a1c8
-  __DATA_CONST.__objc_protorefs: 0x508
+  __DATA_CONST.__objc_selrefs: 0x2a168
+  __DATA_CONST.__objc_protorefs: 0x500
   __DATA_CONST.__objc_superrefs: 0x10a8
   __DATA_CONST.__vfx_script_tbl: 0x10
   __DATA_CONST.__objc_arraydata: 0x1508
-  __DATA_CONST.__got: 0x58a8
-  __AUTH_CONST.__const: 0x19ab8
-  __AUTH_CONST.__cfstring: 0x25e00
-  __AUTH_CONST.__objc_const: 0x83fe0
+  __DATA_CONST.__got: 0x58d0
+  __AUTH_CONST.__const: 0x19d90
+  __AUTH_CONST.__cfstring: 0x25ec0
+  __AUTH_CONST.__objc_const: 0x84108
   __AUTH_CONST.__objc_arrayobj: 0xde0
   __AUTH_CONST.__objc_intobj: 0x1560
   __AUTH_CONST.__objc_dictobj: 0x398
   __AUTH_CONST.__objc_doubleobj: 0x210
-  __AUTH_CONST.__auth_got: 0x5670
-  __AUTH.__objc_data: 0x18ff0
-  __AUTH.__data: 0x51f8
-  __DATA.__objc_ivar: 0x5b6c
-  __DATA.__data: 0x14748
+  __AUTH_CONST.__auth_got: 0x56c8
+  __AUTH.__objc_data: 0x19048
+  __AUTH.__data: 0x5208
+  __DATA.__objc_ivar: 0x5b70
+  __DATA.__data: 0x14778
   __DATA.__objc_stublist: 0x28
   __DATA.__common: 0x350
   __DATA_DIRTY.__objc_data: 0x2318

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 42638
-  Symbols:   48877
-  CStrings:  8012
+  Functions: 42707
+  Symbols:   48865
+  CStrings:  8031
 
Symbols:
+ +[PUSharingErrorPresentationController _provenanceProcessingFailedErrorInChain:]
+ -[PUCleanupToolController _handleGenerativeEditError:cleanupRequest:cleanupRequestDuration:modelResolution:]
+ -[PUCleanupToolController _isVerticallyConstrainedWithBottomControls]
+ -[PUCropPerspectiveView setImage:animated:]
+ -[PUCropToolController animateNextRenderUpdate]
+ -[PUCropToolController cropObscurer]
+ -[PUCropToolController setAnimateNextRenderUpdate:]
+ -[PUCropToolController setCropObscurer:]
+ -[PUCropTransformedImageView setImage:animated:]
+ -[PUErrorPresentationController preferredAlertAction]
+ -[PUErrorPresentationController setPreferredAlertAction:]
+ -[PUOneUpBarsController _invalidateWantsLibraryButton]
+ -[PUOneUpBarsController _libraryImageButton]
+ -[PUOneUpBarsController _updateWantsLibraryButton]
+ -[PUOneUpBarsController setWantsLibraryButton:]
+ -[PUOneUpBarsController wantsLibraryButton]
+ -[PUOneUpViewController _updateZoomPhotosToFillIfNeeded]
+ -[PUPXPhotoKitPresentSelectionReviewActionPerformer entryPoint]
+ -[PUPhotoEditViewController _clearTransientStatusBadgeConstraints]
+ -[PUPhotoEditViewController _visibleOutOfNavBarCenterView]
+ -[PUPhotosGridViewController _gridHeaderEditButtonTapped:]
+ -[PUPhotosGridViewController _logAnalyticsEventForGridHeaderControlTapped:]
+ -[PUPickerCoordinator entryPoint]
+ -[PUVideoEditOverlayViewController subjectFocusStateDidChange:forBadge:]
+ GCC_except_table10116
+ GCC_except_table10133
+ GCC_except_table10144
+ GCC_except_table10145
+ GCC_except_table10175
+ GCC_except_table10243
+ GCC_except_table10283
+ GCC_except_table10285
+ GCC_except_table10292
+ GCC_except_table10296
+ GCC_except_table10399
+ GCC_except_table10457
+ GCC_except_table10490
+ GCC_except_table1056
+ GCC_except_table10756
+ GCC_except_table10758
+ GCC_except_table10873
+ GCC_except_table10980
+ GCC_except_table1101
+ GCC_except_table11146
+ GCC_except_table1118
+ GCC_except_table11187
+ GCC_except_table11189
+ GCC_except_table11218
+ GCC_except_table11227
+ GCC_except_table1125
+ GCC_except_table11269
+ GCC_except_table11270
+ GCC_except_table11272
+ GCC_except_table11273
+ GCC_except_table11276
+ GCC_except_table11300
+ GCC_except_table11612
+ GCC_except_table11642
+ GCC_except_table11648
+ GCC_except_table11721
+ GCC_except_table1199
+ GCC_except_table1203
+ GCC_except_table12037
+ GCC_except_table12038
+ GCC_except_table12088
+ GCC_except_table12092
+ GCC_except_table1217
+ GCC_except_table1220
+ GCC_except_table1227
+ GCC_except_table12388
+ GCC_except_table12408
+ GCC_except_table12421
+ GCC_except_table12435
+ GCC_except_table12455
+ GCC_except_table1246
+ GCC_except_table12503
+ GCC_except_table1260
+ GCC_except_table1263
+ GCC_except_table12655
+ GCC_except_table12673
+ GCC_except_table12678
+ GCC_except_table12681
+ GCC_except_table12684
+ GCC_except_table12695
+ GCC_except_table12743
+ GCC_except_table12756
+ GCC_except_table12795
+ GCC_except_table12832
+ GCC_except_table12850
+ GCC_except_table12884
+ GCC_except_table12979
+ GCC_except_table12986
+ GCC_except_table1318
+ GCC_except_table13250
+ GCC_except_table1326
+ GCC_except_table13326
+ GCC_except_table13340
+ GCC_except_table13347
+ GCC_except_table13364
+ GCC_except_table13367
+ GCC_except_table13375
+ GCC_except_table13490
+ GCC_except_table13492
+ GCC_except_table13554
+ GCC_except_table13599
+ GCC_except_table13662
+ GCC_except_table13687
+ GCC_except_table13715
+ GCC_except_table13739
+ GCC_except_table13767
+ GCC_except_table13781
+ GCC_except_table13791
+ GCC_except_table13801
+ GCC_except_table13814
+ GCC_except_table13824
+ GCC_except_table13835
+ GCC_except_table13844
+ GCC_except_table13857
+ GCC_except_table13869
+ GCC_except_table13874
+ GCC_except_table13876
+ GCC_except_table13881
+ GCC_except_table13882
+ GCC_except_table13883
+ GCC_except_table13903
+ GCC_except_table13949
+ GCC_except_table14097
+ GCC_except_table14241
+ GCC_except_table14327
+ GCC_except_table14346
+ GCC_except_table14350
+ GCC_except_table14361
+ GCC_except_table14385
+ GCC_except_table14388
+ GCC_except_table14395
+ GCC_except_table14397
+ GCC_except_table14445
+ GCC_except_table14837
+ GCC_except_table15271
+ GCC_except_table15272
+ GCC_except_table15281
+ GCC_except_table15284
+ GCC_except_table15287
+ GCC_except_table15295
+ GCC_except_table1531
+ GCC_except_table15330
+ GCC_except_table15365
+ GCC_except_table15443
+ GCC_except_table15517
+ GCC_except_table15523
+ GCC_except_table15527
+ GCC_except_table15569
+ GCC_except_table15620
+ GCC_except_table15622
+ GCC_except_table15623
+ GCC_except_table15632
+ GCC_except_table15641
+ GCC_except_table15646
+ GCC_except_table15648
+ GCC_except_table1566
+ GCC_except_table15672
+ GCC_except_table15684
+ GCC_except_table15692
+ GCC_except_table15694
+ GCC_except_table15698
+ GCC_except_table15705
+ GCC_except_table15708
+ GCC_except_table15710
+ GCC_except_table15712
+ GCC_except_table15717
+ GCC_except_table15735
+ GCC_except_table15742
+ GCC_except_table15746
+ GCC_except_table15757
+ GCC_except_table1576
+ GCC_except_table15768
+ GCC_except_table15815
+ GCC_except_table15888
+ GCC_except_table16002
+ GCC_except_table16005
+ GCC_except_table16011
+ GCC_except_table16043
+ GCC_except_table16060
+ GCC_except_table16118
+ GCC_except_table16148
+ GCC_except_table16205
+ GCC_except_table16226
+ GCC_except_table16323
+ GCC_except_table16324
+ GCC_except_table16343
+ GCC_except_table16352
+ GCC_except_table16359
+ GCC_except_table16366
+ GCC_except_table16372
+ GCC_except_table16382
+ GCC_except_table16389
+ GCC_except_table16573
+ GCC_except_table16584
+ GCC_except_table16587
+ GCC_except_table16589
+ GCC_except_table16596
+ GCC_except_table16598
+ GCC_except_table16600
+ GCC_except_table16603
+ GCC_except_table16685
+ GCC_except_table16694
+ GCC_except_table16695
+ GCC_except_table16722
+ GCC_except_table16727
+ GCC_except_table16925
+ GCC_except_table16951
+ GCC_except_table17114
+ GCC_except_table17221
+ GCC_except_table17222
+ GCC_except_table17348
+ GCC_except_table17382
+ GCC_except_table17424
+ GCC_except_table17429
+ GCC_except_table17458
+ GCC_except_table17460
+ GCC_except_table17462
+ GCC_except_table17608
+ GCC_except_table17611
+ GCC_except_table17620
+ GCC_except_table17787
+ GCC_except_table17788
+ GCC_except_table17822
+ GCC_except_table17841
+ GCC_except_table17843
+ GCC_except_table17908
+ GCC_except_table17981
+ GCC_except_table17998
+ GCC_except_table17999
+ GCC_except_table18002
+ GCC_except_table18009
+ GCC_except_table18010
+ GCC_except_table18018
+ GCC_except_table18031
+ GCC_except_table18041
+ GCC_except_table18052
+ GCC_except_table18198
+ GCC_except_table18200
+ GCC_except_table18202
+ GCC_except_table18210
+ GCC_except_table18503
+ GCC_except_table18504
+ GCC_except_table18522
+ GCC_except_table18524
+ GCC_except_table18557
+ GCC_except_table18568
+ GCC_except_table18577
+ GCC_except_table18592
+ GCC_except_table18593
+ GCC_except_table18597
+ GCC_except_table18616
+ GCC_except_table18734
+ GCC_except_table18746
+ GCC_except_table18794
+ GCC_except_table18804
+ GCC_except_table18819
+ GCC_except_table18822
+ GCC_except_table18824
+ GCC_except_table18825
+ GCC_except_table18826
+ GCC_except_table18827
+ GCC_except_table1888
+ GCC_except_table18915
+ GCC_except_table18922
+ GCC_except_table19004
+ GCC_except_table19059
+ GCC_except_table19219
+ GCC_except_table19236
+ GCC_except_table19415
+ GCC_except_table19581
+ GCC_except_table19669
+ GCC_except_table19693
+ GCC_except_table1987
+ GCC_except_table20100
+ GCC_except_table20104
+ GCC_except_table20135
+ GCC_except_table20146
+ GCC_except_table20197
+ GCC_except_table20246
+ GCC_except_table20494
+ GCC_except_table20642
+ GCC_except_table20647
+ GCC_except_table20788
+ GCC_except_table20798
+ GCC_except_table20800
+ GCC_except_table20843
+ GCC_except_table20897
+ GCC_except_table20898
+ GCC_except_table20988
+ GCC_except_table21179
+ GCC_except_table21183
+ GCC_except_table21262
+ GCC_except_table21263
+ GCC_except_table21271
+ GCC_except_table21350
+ GCC_except_table21384
+ GCC_except_table21466
+ GCC_except_table21467
+ GCC_except_table21521
+ GCC_except_table21647
+ GCC_except_table21842
+ GCC_except_table21843
+ GCC_except_table21860
+ GCC_except_table21864
+ GCC_except_table21881
+ GCC_except_table2196
+ GCC_except_table2199
+ GCC_except_table21993
+ GCC_except_table2208
+ GCC_except_table22313
+ GCC_except_table22354
+ GCC_except_table22447
+ GCC_except_table22471
+ GCC_except_table22486
+ GCC_except_table2259
+ GCC_except_table22606
+ GCC_except_table22642
+ GCC_except_table22645
+ GCC_except_table22647
+ GCC_except_table22652
+ GCC_except_table22684
+ GCC_except_table22690
+ GCC_except_table22755
+ GCC_except_table2277
+ GCC_except_table22771
+ GCC_except_table23044
+ GCC_except_table23048
+ GCC_except_table23050
+ GCC_except_table23057
+ GCC_except_table23058
+ GCC_except_table23061
+ GCC_except_table23063
+ GCC_except_table23165
+ GCC_except_table2322
+ GCC_except_table23267
+ GCC_except_table23304
+ GCC_except_table2331
+ GCC_except_table2334
+ GCC_except_table23366
+ GCC_except_table23379
+ GCC_except_table2346
+ GCC_except_table23467
+ GCC_except_table23474
+ GCC_except_table23476
+ GCC_except_table23478
+ GCC_except_table23497
+ GCC_except_table23502
+ GCC_except_table23508
+ GCC_except_table23524
+ GCC_except_table2369
+ GCC_except_table23725
+ GCC_except_table23748
+ GCC_except_table23759
+ GCC_except_table23862
+ GCC_except_table2388
+ GCC_except_table23917
+ GCC_except_table23924
+ GCC_except_table23928
+ GCC_except_table2394
+ GCC_except_table23942
+ GCC_except_table23945
+ GCC_except_table24076
+ GCC_except_table24104
+ GCC_except_table24121
+ GCC_except_table24171
+ GCC_except_table2423
+ GCC_except_table24325
+ GCC_except_table24394
+ GCC_except_table24404
+ GCC_except_table24412
+ GCC_except_table2460
+ GCC_except_table24628
+ GCC_except_table24644
+ GCC_except_table2771
+ GCC_except_table2827
+ GCC_except_table2831
+ GCC_except_table2834
+ GCC_except_table2923
+ GCC_except_table2927
+ GCC_except_table2949
+ GCC_except_table2950
+ GCC_except_table2958
+ GCC_except_table3010
+ GCC_except_table3073
+ GCC_except_table3076
+ GCC_except_table3089
+ GCC_except_table3298
+ GCC_except_table3328
+ GCC_except_table3351
+ GCC_except_table3374
+ GCC_except_table3377
+ GCC_except_table3583
+ GCC_except_table3820
+ GCC_except_table3823
+ GCC_except_table3829
+ GCC_except_table3958
+ GCC_except_table4006
+ GCC_except_table4026
+ GCC_except_table4064
+ GCC_except_table4068
+ GCC_except_table4069
+ GCC_except_table4072
+ GCC_except_table4151
+ GCC_except_table4284
+ GCC_except_table4401
+ GCC_except_table4413
+ GCC_except_table4414
+ GCC_except_table4477
+ GCC_except_table4504
+ GCC_except_table4611
+ GCC_except_table4626
+ GCC_except_table4785
+ GCC_except_table4808
+ GCC_except_table4894
+ GCC_except_table5088
+ GCC_except_table5139
+ GCC_except_table5148
+ GCC_except_table5155
+ GCC_except_table5156
+ GCC_except_table5157
+ GCC_except_table5179
+ GCC_except_table5201
+ GCC_except_table5325
+ GCC_except_table5332
+ GCC_except_table5734
+ GCC_except_table5772
+ GCC_except_table5792
+ GCC_except_table5794
+ GCC_except_table5803
+ GCC_except_table5832
+ GCC_except_table5835
+ GCC_except_table5859
+ GCC_except_table5885
+ GCC_except_table5909
+ GCC_except_table5943
+ GCC_except_table5953
+ GCC_except_table6251
+ GCC_except_table6252
+ GCC_except_table6259
+ GCC_except_table6394
+ GCC_except_table6447
+ GCC_except_table6451
+ GCC_except_table6454
+ GCC_except_table6471
+ GCC_except_table6503
+ GCC_except_table6532
+ GCC_except_table6576
+ GCC_except_table6614
+ GCC_except_table6621
+ GCC_except_table6692
+ GCC_except_table6723
+ GCC_except_table6828
+ GCC_except_table6835
+ GCC_except_table6838
+ GCC_except_table6905
+ GCC_except_table6917
+ GCC_except_table6927
+ GCC_except_table6931
+ GCC_except_table7070
+ GCC_except_table7080
+ GCC_except_table7089
+ GCC_except_table7097
+ GCC_except_table7171
+ GCC_except_table7227
+ GCC_except_table7235
+ GCC_except_table7378
+ GCC_except_table7394
+ GCC_except_table7435
+ GCC_except_table7440
+ GCC_except_table7448
+ GCC_except_table7453
+ GCC_except_table7458
+ GCC_except_table7487
+ GCC_except_table7608
+ GCC_except_table7609
+ GCC_except_table7974
+ GCC_except_table8047
+ GCC_except_table8159
+ GCC_except_table8172
+ GCC_except_table8237
+ GCC_except_table8267
+ GCC_except_table8268
+ GCC_except_table8422
+ GCC_except_table8611
+ GCC_except_table8619
+ GCC_except_table8620
+ GCC_except_table8628
+ GCC_except_table8641
+ GCC_except_table8653
+ GCC_except_table8659
+ GCC_except_table8678
+ GCC_except_table8682
+ GCC_except_table8708
+ GCC_except_table8760
+ GCC_except_table8888
+ GCC_except_table8972
+ GCC_except_table9020
+ GCC_except_table9104
+ GCC_except_table9116
+ GCC_except_table9156
+ GCC_except_table9181
+ GCC_except_table9225
+ GCC_except_table9252
+ GCC_except_table9266
+ GCC_except_table9274
+ GCC_except_table9314
+ GCC_except_table9327
+ GCC_except_table9329
+ GCC_except_table9333
+ GCC_except_table9334
+ GCC_except_table9400
+ GCC_except_table9403
+ GCC_except_table9543
+ GCC_except_table9548
+ GCC_except_table9550
+ GCC_except_table9599
+ GCC_except_table9674
+ GCC_except_table9683
+ GCC_except_table9825
+ GCC_except_table9877
+ GCC_except_table9923
+ GCC_except_table9927
+ GCC_except_table9931
+ GCC_except_table9949
+ _NUPixelRectIsNull
+ _OBJC_CLASS_$_PIDiffusionCleanupPipeline
+ _OBJC_IVAR_$_PUCropToolController._animateNextRenderUpdate
+ _OBJC_IVAR_$_PUCropToolController._cropObscurer
+ _OBJC_IVAR_$_PUErrorPresentationController._preferredAlertAction
+ _OBJC_IVAR_$_PUOneUpBarsController._wantsLibraryButton
+ _OBJC_IVAR_$_PUOneUpViewController._zoomPhotosToFillEnabled
+ _PAMediaConversionErrorIsTransient
+ _PAMediaConversionIsProvenanceClientUpgradeRequiredError
+ _PXAnalyticsEventGridHeaderControlTapped
+ _PXAnalyticsGridHeaderCollectionTypeFromAssetCollection
+ _PXAnalyticsPayloadGridHeaderCollectionTypeKey
+ _PXAnalyticsPayloadGridHeaderControlKey
+ _PXDeviceIsV68
+ _PXSidebarEmptyAlbumPlaceholderBackgroundColor
+ _UIListContentImageStandardDimension
+ __OBJC_$_INSTANCE_METHODS_PUStagingAreaViewController(PhotosUIPrivate|PhotosUIPrivate1|PhotosUIPrivate2|PhotosUIPrivate3)
+ __OBJC_$_PROP_LIST_PUStagingAreaViewControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PUStagingAreaViewController(PhotosUIPrivate|PhotosUIPrivate1|PhotosUIPrivate2|PhotosUIPrivate3)
+ __PROTOCOL_PROPERTIES_PUStagingAreaViewControllerDelegate
+ ___58-[PUImportActionCoordinator _importItems:allowDuplicates:]_block_invoke_2
+ ___69-[PUDepthToggleEditOperationPerformer _handleLoadResult:imageValues:]_block_invoke_5
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96s104s112r_e20_v16?0"NUResponse"8ls32l8s40l8r112l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e8_v12?0B8ls32l8s40l8s48l8s56l8
+ ___swift_closure_destructor.184Tm
+ ___swift_closure_destructor.210Tm
+ ___swift_get_extra_inhabitant_index.152Tm
+ ___swift_store_extra_inhabitant_index.153Tm
+ _associated conformance 15PhotosUIPrivate21StagingAreaEntryPointOSHAASQ
+ _associated conformance 15PhotosUIPrivate34StagingAreaContainerViewControllerC16PresentationMode33_8899651E4862903A4EC932FDCF8F741DLLOSHAASQ
+ _symbolic So16PXAssetReferenceC
+ _symbolic So21PUPickerConfigurationCSg
+ _symbolic _____ 15PhotosUIPrivate20StagingAreaAnalyticsO
+ _symbolic _____ 15PhotosUIPrivate21StagingAreaEntryPointO
+ _symbolic _____ 15PhotosUIPrivate34StagingAreaContainerViewControllerC16PresentationMode33_8899651E4862903A4EC932FDCF8F741DLLO
+ _symbolic _____3top_AA6bottomt 12CoreGraphics7CGFloatV
+ _symbolic _____ySSSo8NSObjectCG s17_NativeDictionaryV
+ _symbolic _____y__________G s15WritableKeyPathC 12PhotosUICore17PhotoStyleElementC08SemanticG0V So7CGPointV
- +[PUPhotoEditLayoutSupport editAIToolHasWideMediaLayoutForView:]
- -[PUCleanupToolController _handleGenerativeEditError:cleanupRequest:cleanupRequestDuration:]
- -[PUCropPerspectiveView setImage:]
- -[PUCropToolController _invalidateCropCanvasConstraintsIfOutfillReservationChanged]
- -[PUCropToolController _reservesSpaceForOutfillStatusView]
- -[PUCropTransformedImageView imageCropRectForViewRect:]
- -[PUCropTransformedImageView viewCropRectForImageRect:]
- -[PUImportActionCoordinator _continueImportingItems:]
- -[PUImportActionCoordinator _filterItemsForImport:allowDuplicates:]
- -[PUImportActionCoordinator _importItemsContainProvenanceData:completionHandler:]
- -[PUImportActionCoordinator _presentProvenanceImportWarningForItems:completionHandler:]
- -[PULivePhotoVideoOverlayTileViewController _finishPlaybackEndTeardownForGeneration:]
- -[PULivePhotoVideoOverlayTileViewController playbackGeneration]
- -[PULivePhotoVideoOverlayTileViewController setPlaybackGeneration:]
- -[PUOneUpBarsController _allPhotosImageButton]
- -[PUOneUpBarsController _invalidateWantsAllPhotosButton]
- -[PUOneUpBarsController _updateWantsAllPhotosButton]
- -[PUOneUpBarsController setWantsAllPhotosButton:]
- -[PUOneUpBarsController wantsAllPhotosButton]
- -[PUOneUpViewController _draggableCurrentAsset]
- -[PUOneUpViewController _isDragOutEnabled]
- -[PUOneUpViewController _updateDragOutInteraction]
- -[PUOneUpViewController dragInteraction:itemsForBeginningSession:]
- -[PUOneUpViewController dragInteraction:previewForLiftingItem:session:]
- -[PUOneUpViewController dragOutInteraction]
- -[PUOneUpViewController setDragOutInteraction:]
- -[PUPhotoEditMediaToolController horizontalPrimaryViewPaddingOffset]
- -[PUVideoEditOverlayViewController subjectFocusStateDidChange:forBadge:focusedDisparity:]
- GCC_except_table10126
- GCC_except_table10143
- GCC_except_table10154
- GCC_except_table10155
- GCC_except_table10185
- GCC_except_table10253
- GCC_except_table10293
- GCC_except_table10295
- GCC_except_table10306
- GCC_except_table10312
- GCC_except_table10409
- GCC_except_table10467
- GCC_except_table10500
- GCC_except_table1054
- GCC_except_table10766
- GCC_except_table10768
- GCC_except_table10883
- GCC_except_table1099
- GCC_except_table10990
- GCC_except_table11156
- GCC_except_table1116
- GCC_except_table11197
- GCC_except_table11199
- GCC_except_table11228
- GCC_except_table1123
- GCC_except_table11237
- GCC_except_table11279
- GCC_except_table11282
- GCC_except_table11283
- GCC_except_table11286
- GCC_except_table11290
- GCC_except_table11310
- GCC_except_table11622
- GCC_except_table11658
- GCC_except_table11662
- GCC_except_table11731
- GCC_except_table1197
- GCC_except_table1201
- GCC_except_table12047
- GCC_except_table12048
- GCC_except_table12098
- GCC_except_table12102
- GCC_except_table1215
- GCC_except_table1216
- GCC_except_table1225
- GCC_except_table12405
- GCC_except_table12425
- GCC_except_table12438
- GCC_except_table1244
- GCC_except_table12452
- GCC_except_table12471
- GCC_except_table12519
- GCC_except_table1256
- GCC_except_table1261
- GCC_except_table12671
- GCC_except_table12689
- GCC_except_table12694
- GCC_except_table12697
- GCC_except_table12700
- GCC_except_table12711
- GCC_except_table12759
- GCC_except_table12772
- GCC_except_table12811
- GCC_except_table12864
- GCC_except_table12866
- GCC_except_table12900
- GCC_except_table12995
- GCC_except_table13002
- GCC_except_table1316
- GCC_except_table1324
- GCC_except_table13266
- GCC_except_table13342
- GCC_except_table13356
- GCC_except_table13379
- GCC_except_table13380
- GCC_except_table13383
- GCC_except_table13390
- GCC_except_table13505
- GCC_except_table13507
- GCC_except_table13569
- GCC_except_table13614
- GCC_except_table13677
- GCC_except_table13702
- GCC_except_table13730
- GCC_except_table13754
- GCC_except_table13782
- GCC_except_table13796
- GCC_except_table13806
- GCC_except_table13816
- GCC_except_table13829
- GCC_except_table13839
- GCC_except_table13850
- GCC_except_table13859
- GCC_except_table13872
- GCC_except_table13884
- GCC_except_table13889
- GCC_except_table13891
- GCC_except_table13896
- GCC_except_table13897
- GCC_except_table13898
- GCC_except_table13918
- GCC_except_table13964
- GCC_except_table14112
- GCC_except_table14256
- GCC_except_table14344
- GCC_except_table14363
- GCC_except_table14367
- GCC_except_table14378
- GCC_except_table14402
- GCC_except_table14405
- GCC_except_table14412
- GCC_except_table14414
- GCC_except_table14462
- GCC_except_table14854
- GCC_except_table15288
- GCC_except_table15289
- GCC_except_table1529
- GCC_except_table15298
- GCC_except_table15301
- GCC_except_table15304
- GCC_except_table15312
- GCC_except_table15347
- GCC_except_table15382
- GCC_except_table15460
- GCC_except_table15534
- GCC_except_table15540
- GCC_except_table15544
- GCC_except_table15586
- GCC_except_table15637
- GCC_except_table15639
- GCC_except_table1564
- GCC_except_table15640
- GCC_except_table15649
- GCC_except_table15658
- GCC_except_table15663
- GCC_except_table15665
- GCC_except_table15689
- GCC_except_table15709
- GCC_except_table15711
- GCC_except_table15715
- GCC_except_table15718
- GCC_except_table15722
- GCC_except_table15725
- GCC_except_table15727
- GCC_except_table15729
- GCC_except_table15734
- GCC_except_table1574
- GCC_except_table15752
- GCC_except_table15759
- GCC_except_table15763
- GCC_except_table15774
- GCC_except_table15785
- GCC_except_table15832
- GCC_except_table15905
- GCC_except_table16017
- GCC_except_table16020
- GCC_except_table16026
- GCC_except_table16058
- GCC_except_table16075
- GCC_except_table16133
- GCC_except_table16163
- GCC_except_table16220
- GCC_except_table16256
- GCC_except_table16338
- GCC_except_table16339
- GCC_except_table16358
- GCC_except_table16367
- GCC_except_table16374
- GCC_except_table16381
- GCC_except_table16387
- GCC_except_table16397
- GCC_except_table16404
- GCC_except_table16588
- GCC_except_table16599
- GCC_except_table16602
- GCC_except_table16604
- GCC_except_table16611
- GCC_except_table16613
- GCC_except_table16615
- GCC_except_table16633
- GCC_except_table16700
- GCC_except_table16709
- GCC_except_table16710
- GCC_except_table16737
- GCC_except_table16742
- GCC_except_table16940
- GCC_except_table16966
- GCC_except_table17129
- GCC_except_table17236
- GCC_except_table17237
- GCC_except_table17363
- GCC_except_table17397
- GCC_except_table17439
- GCC_except_table17444
- GCC_except_table17473
- GCC_except_table17475
- GCC_except_table17477
- GCC_except_table17623
- GCC_except_table17626
- GCC_except_table17635
- GCC_except_table17802
- GCC_except_table17803
- GCC_except_table17837
- GCC_except_table17856
- GCC_except_table17858
- GCC_except_table17923
- GCC_except_table17996
- GCC_except_table18013
- GCC_except_table18014
- GCC_except_table18017
- GCC_except_table18024
- GCC_except_table18025
- GCC_except_table18033
- GCC_except_table18046
- GCC_except_table18054
- GCC_except_table18065
- GCC_except_table18211
- GCC_except_table18213
- GCC_except_table18215
- GCC_except_table18223
- GCC_except_table18516
- GCC_except_table18517
- GCC_except_table18535
- GCC_except_table18537
- GCC_except_table18570
- GCC_except_table18581
- GCC_except_table18590
- GCC_except_table18605
- GCC_except_table18610
- GCC_except_table18619
- GCC_except_table18629
- GCC_except_table18747
- GCC_except_table18759
- GCC_except_table18807
- GCC_except_table18817
- GCC_except_table18835
- GCC_except_table18837
- GCC_except_table18838
- GCC_except_table18839
- GCC_except_table18840
- GCC_except_table18845
- GCC_except_table1886
- GCC_except_table18928
- GCC_except_table18935
- GCC_except_table19017
- GCC_except_table19072
- GCC_except_table19232
- GCC_except_table19249
- GCC_except_table19428
- GCC_except_table19594
- GCC_except_table19682
- GCC_except_table19706
- GCC_except_table1985
- GCC_except_table20126
- GCC_except_table20130
- GCC_except_table20148
- GCC_except_table20159
- GCC_except_table20210
- GCC_except_table20259
- GCC_except_table20507
- GCC_except_table20655
- GCC_except_table20660
- GCC_except_table20801
- GCC_except_table20811
- GCC_except_table20813
- GCC_except_table20856
- GCC_except_table20910
- GCC_except_table20911
- GCC_except_table21001
- GCC_except_table21192
- GCC_except_table21196
- GCC_except_table21275
- GCC_except_table21276
- GCC_except_table21284
- GCC_except_table21363
- GCC_except_table21397
- GCC_except_table21479
- GCC_except_table21480
- GCC_except_table21534
- GCC_except_table21660
- GCC_except_table21855
- GCC_except_table21856
- GCC_except_table21873
- GCC_except_table21877
- GCC_except_table21894
- GCC_except_table2194
- GCC_except_table2195
- GCC_except_table22006
- GCC_except_table2206
- GCC_except_table22325
- GCC_except_table22366
- GCC_except_table22459
- GCC_except_table22483
- GCC_except_table22498
- GCC_except_table2257
- GCC_except_table22618
- GCC_except_table22654
- GCC_except_table22657
- GCC_except_table22659
- GCC_except_table22664
- GCC_except_table22696
- GCC_except_table22702
- GCC_except_table2275
- GCC_except_table22767
- GCC_except_table22783
- GCC_except_table23056
- GCC_except_table23062
- GCC_except_table23069
- GCC_except_table23070
- GCC_except_table23072
- GCC_except_table23073
- GCC_except_table23075
- GCC_except_table23177
- GCC_except_table2320
- GCC_except_table23279
- GCC_except_table2328
- GCC_except_table2329
- GCC_except_table23316
- GCC_except_table23378
- GCC_except_table23391
- GCC_except_table2344
- GCC_except_table23479
- GCC_except_table23486
- GCC_except_table23488
- GCC_except_table23490
- GCC_except_table23509
- GCC_except_table23514
- GCC_except_table23520
- GCC_except_table23536
- GCC_except_table2367
- GCC_except_table23737
- GCC_except_table23760
- GCC_except_table23771
- GCC_except_table2384
- GCC_except_table23874
- GCC_except_table2390
- GCC_except_table23929
- GCC_except_table23936
- GCC_except_table23940
- GCC_except_table23954
- GCC_except_table23957
- GCC_except_table24088
- GCC_except_table24116
- GCC_except_table24133
- GCC_except_table24183
- GCC_except_table2421
- GCC_except_table24337
- GCC_except_table24406
- GCC_except_table24416
- GCC_except_table24424
- GCC_except_table2458
- GCC_except_table24640
- GCC_except_table24656
- GCC_except_table2767
- GCC_except_table2825
- GCC_except_table2829
- GCC_except_table2832
- GCC_except_table2921
- GCC_except_table2925
- GCC_except_table2947
- GCC_except_table2948
- GCC_except_table2956
- GCC_except_table3008
- GCC_except_table3071
- GCC_except_table3074
- GCC_except_table3087
- GCC_except_table3296
- GCC_except_table3326
- GCC_except_table3349
- GCC_except_table3372
- GCC_except_table3375
- GCC_except_table3581
- GCC_except_table3818
- GCC_except_table3821
- GCC_except_table3827
- GCC_except_table3956
- GCC_except_table4004
- GCC_except_table4024
- GCC_except_table4062
- GCC_except_table4065
- GCC_except_table4066
- GCC_except_table4070
- GCC_except_table4147
- GCC_except_table4282
- GCC_except_table4399
- GCC_except_table4411
- GCC_except_table4412
- GCC_except_table4475
- GCC_except_table4502
- GCC_except_table4609
- GCC_except_table4624
- GCC_except_table4783
- GCC_except_table4806
- GCC_except_table4892
- GCC_except_table5085
- GCC_except_table5136
- GCC_except_table5145
- GCC_except_table5152
- GCC_except_table5153
- GCC_except_table5154
- GCC_except_table5176
- GCC_except_table5198
- GCC_except_table5322
- GCC_except_table5329
- GCC_except_table5728
- GCC_except_table5766
- GCC_except_table5786
- GCC_except_table5788
- GCC_except_table5797
- GCC_except_table5826
- GCC_except_table5829
- GCC_except_table5853
- GCC_except_table5879
- GCC_except_table5902
- GCC_except_table5936
- GCC_except_table5946
- GCC_except_table6246
- GCC_except_table6247
- GCC_except_table6254
- GCC_except_table6389
- GCC_except_table6442
- GCC_except_table6446
- GCC_except_table6449
- GCC_except_table6466
- GCC_except_table6498
- GCC_except_table6527
- GCC_except_table6570
- GCC_except_table6608
- GCC_except_table6615
- GCC_except_table6686
- GCC_except_table6717
- GCC_except_table6822
- GCC_except_table6826
- GCC_except_table6829
- GCC_except_table6899
- GCC_except_table6911
- GCC_except_table6921
- GCC_except_table6925
- GCC_except_table7064
- GCC_except_table7074
- GCC_except_table7083
- GCC_except_table7091
- GCC_except_table7165
- GCC_except_table7221
- GCC_except_table7229
- GCC_except_table7372
- GCC_except_table7388
- GCC_except_table7423
- GCC_except_table7434
- GCC_except_table7442
- GCC_except_table7447
- GCC_except_table7452
- GCC_except_table7481
- GCC_except_table7602
- GCC_except_table7603
- GCC_except_table7968
- GCC_except_table8041
- GCC_except_table8153
- GCC_except_table8160
- GCC_except_table8231
- GCC_except_table8261
- GCC_except_table8262
- GCC_except_table8417
- GCC_except_table8606
- GCC_except_table8614
- GCC_except_table8615
- GCC_except_table8623
- GCC_except_table8630
- GCC_except_table8631
- GCC_except_table8646
- GCC_except_table8658
- GCC_except_table8664
- GCC_except_table8683
- GCC_except_table8687
- GCC_except_table8713
- GCC_except_table8765
- GCC_except_table8893
- GCC_except_table8982
- GCC_except_table9025
- GCC_except_table9111
- GCC_except_table9123
- GCC_except_table9139
- GCC_except_table9142
- GCC_except_table9167
- GCC_except_table9192
- GCC_except_table9236
- GCC_except_table9263
- GCC_except_table9277
- GCC_except_table9284
- GCC_except_table9324
- GCC_except_table9337
- GCC_except_table9339
- GCC_except_table9343
- GCC_except_table9344
- GCC_except_table9410
- GCC_except_table9413
- GCC_except_table9553
- GCC_except_table9558
- GCC_except_table9560
- GCC_except_table9609
- GCC_except_table9684
- GCC_except_table9693
- GCC_except_table9835
- GCC_except_table9887
- GCC_except_table9933
- GCC_except_table9937
- GCC_except_table9941
- GCC_except_table9959
- _OBJC_CLASS_$_PHImportAsset
- _OBJC_CLASS_$_UIDragInteraction
- _OBJC_CLASS_$_UIDragPreviewTarget
- _OBJC_CLASS_$_UITargetedDragPreview
- _OBJC_IVAR_$_PULivePhotoVideoOverlayTileViewController._playbackGeneration
- _OBJC_IVAR_$_PUOneUpBarsController._wantsAllPhotosButton
- _OBJC_IVAR_$_PUOneUpViewController._dragOutInteraction
- _OBJC_IVAR_$_PUPhotoEditMediaToolController._horizontalPrimaryViewPaddingOffset
- _PUOneUpSideBySideInfoPanelMinimumAspectRatio
- __OBJC_$_INSTANCE_METHODS_PUStagingAreaViewController(PhotosUIPrivate|PhotosUIPrivate1|PhotosUIPrivate2|PhotosUIPrivate3|PhotosUIPrivate4)
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIDragInteractionDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIDragInteractionDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIDragInteractionDelegate
- __OBJC_$_PROTOCOL_REFS_UIDragInteractionDelegate
- __OBJC_CLASS_PROTOCOLS_$_PUStagingAreaViewController(PhotosUIPrivate|PhotosUIPrivate1|PhotosUIPrivate2|PhotosUIPrivate3|PhotosUIPrivate4)
- __OBJC_LABEL_PROTOCOL_$_UIDragInteractionDelegate
- __OBJC_PROTOCOL_$_UIDragInteractionDelegate
- ___53-[PUImportActionCoordinator _continueImportingItems:]_block_invoke
- ___53-[PUImportActionCoordinator _continueImportingItems:]_block_invoke_2
- ___67-[PUImportActionCoordinator _filterItemsForImport:allowDuplicates:]_block_invoke
- ___81-[PUImportActionCoordinator _importItemsContainProvenanceData:completionHandler:]_block_invoke
- ___81-[PUImportActionCoordinator _importItemsContainProvenanceData:completionHandler:]_block_invoke_2
- ___83-[PULivePhotoVideoOverlayTileViewController livePhotoView:didEndPlaybackWithStyle:]_block_invoke
- ___83-[PULivePhotoVideoOverlayTileViewController livePhotoView:didEndPlaybackWithStyle:]_block_invoke_2
- ___86-[PULivePhotoVideoOverlayTileViewController livePhotoView:willBeginPlaybackWithStyle:]_block_invoke_2
- ___87-[PUImportActionCoordinator _presentProvenanceImportWarningForItems:completionHandler:]_block_invoke
- ___87-[PUImportActionCoordinator _presentProvenanceImportWarningForItems:completionHandler:]_block_invoke_2
- ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96s104r_e20_v16?0"NUResponse"8ls32l8s40l8r104l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_64_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
- ___swift_closure_destructor.180Tm
- ___swift_closure_destructor.199Tm
- ___swift_get_extra_inhabitant_index.148Tm
- ___swift_store_extra_inhabitant_index.149Tm
- _associated conformance So34PUAssetExplorerReviewScreenOptionsVs10SetAlgebraSCSQ
- _associated conformance So34PUAssetExplorerReviewScreenOptionsVs10SetAlgebraSCs25ExpressibleByArrayLiteral
- _associated conformance So34PUAssetExplorerReviewScreenOptionsVs9OptionSetSCSY
- _associated conformance So34PUAssetExplorerReviewScreenOptionsVs9OptionSetSCs0G7Algebra
- _get_enum_tag_for_layout_string 15PhotosUIPrivate34StagingAreaContainerViewControllerC8DataMode33_8899651E4862903A4EC932FDCF8F741DLLO
- _symbolic So22PXSelectionCoordinatorC09selectionB0_So21PUPickerConfigurationC06pickerE0t
- _symbolic _____ 15PhotosUIPrivate34StagingAreaContainerViewControllerC8DataMode33_8899651E4862903A4EC932FDCF8F741DLLO
- _symbolic _____ So34PUAssetExplorerReviewScreenOptionsV
- _type_layout_string 15PhotosUIPrivate34StagingAreaContainerViewControllerC8DataMode33_8899651E4862903A4EC932FDCF8F741DLLO
CStrings:
+ ", expected PUPXAssetReference;"
+ "Custom suggestion given no identifiers"
+ "Custom suggestion unavailable: none of %{public}ld identifier(s) resolved to an asset in this library"
+ "Expected a PXPhotoKitAssetsDataSource, got %@"
+ "No index path in the staging area data source %{public}ld for reference %{public}ld"
+ "PECleanupResetWarningTitle"
+ "PROVENANCE_ALERT_CLIENT_UPGRADE_MESSAGE"
+ "PROVENANCE_ALERT_CLIENT_UPGRADE_NOT_NOW_BUTTON"
+ "PROVENANCE_ALERT_CLIENT_UPGRADE_TITLE"
+ "PROVENANCE_ALERT_CLIENT_UPGRADE_UPDATE_BUTTON"
+ "PROVENANCE_ALERT_FATAL_MESSAGE"
+ "PROVENANCE_ALERT_FATAL_TITLE"
+ "PROVENANCE_ALERT_TRANSIENT_MESSAGE"
+ "PROVENANCE_ALERT_TRANSIENT_TITLE"
+ "PUONEUP_QUICK_ACTION_SHOW_IN_LIBRARY"
+ "PUOneUpBarButtonItemIdentifierLibrary"
+ "Picker opening on the All tab: %{public}ld suggestion(s) offered, %{public}ld available, requested default absent or unavailable"
+ "PickerSuggestions"
+ "Provenance Processing Failed"
+ "Staging area 1up got "
+ "[ContentProvenance] Export failure classified as provenance-processing failure. Error: %@"
+ "[ContentProvenance] Presenting %{public}@ provenance alert. Underlying error: %@"
+ "client upgrade required"
+ "com.apple.photos.CPAnalytics.stagingArea.selectionCommitted"
+ "fatal"
+ "finalSelectedCount"
+ "initialSelectedCount"
+ "modifiedOptionsMenu"
+ "openedOptionsMenu"
+ "pickerShouldIncludeCaption"
+ "transient"
+ "\xf0\xf0\x91\xf0Q"
- "%@ %f"
- "%{public}@: Import contains provenance data. Presenting warning before continuing."
- "IMPORT_PROVENANCE_WARNING_IMPORT_ACTION"
- "IMPORT_PROVENANCE_WARNING_MESSAGE"
- "IMPORT_PROVENANCE_WARNING_TITLE"
- "In lockdown mode. Excluding caption by default in share sheet, which could require format conversions during export."
- "PHOTOEDIT_CINEMATIC_FOCUS_STATE_FIXED_DISTANCE_FMT"
- "PUONEUP_QUICK_ACTION_REVEAL_IN_ALLPHOTOS"
- "PUOneUpBarButtonItemIdentifierAllPhotos"
- "importAsset"
- "pickerShouldStripCaption"
- "plus"
- "\xf0\xf0\x91\xf0a"
```
