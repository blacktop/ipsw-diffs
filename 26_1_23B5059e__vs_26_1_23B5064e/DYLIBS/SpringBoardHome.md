## SpringBoardHome

> `/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome`

```diff

-169.100.0.0.0
-  __TEXT.__text: 0x327f84
-  __TEXT.__auth_stubs: 0x2cc0
-  __TEXT.__objc_methlist: 0x3bbfc
+172.101.0.0.0
+  __TEXT.__text: 0x3299f8
+  __TEXT.__auth_stubs: 0x2ce0
+  __TEXT.__objc_methlist: 0x3bdb4
   __TEXT.__const: 0x62d4
-  __TEXT.__cstring: 0x1b38f
+  __TEXT.__cstring: 0x1b3ff
   __TEXT.__gcc_except_tab: 0x3e74
   __TEXT.__oslogstring: 0xdd80
   __TEXT.__dlopen_cstrs: 0x4c6
   __TEXT.__ustring: 0x620
   __TEXT.__swift5_typeref: 0x179c
-  __TEXT.__constg_swiftt: 0x83c
+  __TEXT.__constg_swiftt: 0x84c
   __TEXT.__swift5_reflstr: 0x46a
   __TEXT.__swift5_fieldmd: 0x584
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_assocty: 0x318
   __TEXT.__swift5_proto: 0xd4
   __TEXT.__swift5_types: 0x98
-  __TEXT.__swift5_capture: 0xfb8
+  __TEXT.__swift5_capture: 0xfd8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0xe318
+  __TEXT.__unwind_info: 0xe3a8
   __TEXT.__eh_frame: 0x990
-  __TEXT.__objc_classname: 0x6db8
-  __TEXT.__objc_methname: 0x99900
-  __TEXT.__objc_methtype: 0x19312
-  __TEXT.__objc_stubs: 0x58fa0
+  __TEXT.__objc_classname: 0x6dbb
+  __TEXT.__objc_methname: 0x99eb8
+  __TEXT.__objc_methtype: 0x19352
+  __TEXT.__objc_stubs: 0x592a0
   __DATA_CONST.__got: 0x2258
-  __DATA_CONST.__const: 0x96c0
+  __DATA_CONST.__const: 0x96c8
   __DATA_CONST.__objc_classlist: 0x1268
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0xb28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b7d8
+  __DATA_CONST.__objc_selrefs: 0x1b8b0
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe38
   __DATA_CONST.__objc_arraydata: 0x6d8
-  __AUTH_CONST.__auth_got: 0x1670
-  __AUTH_CONST.__const: 0x6230
+  __AUTH_CONST.__auth_got: 0x1680
+  __AUTH_CONST.__const: 0x62a8
   __AUTH_CONST.__cfstring: 0x15ca0
-  __AUTH_CONST.__objc_const: 0x54e30
+  __AUTH_CONST.__objc_const: 0x55070
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH.__objc_data: 0x6118
+  __AUTH.__objc_data: 0x6128
   __AUTH.__data: 0x568
-  __DATA.__objc_ivar: 0x3ad8
-  __DATA.__data: 0x88a8
+  __DATA.__objc_ivar: 0x3afc
+  __DATA.__data: 0x88b8
   __DATA.__bss: 0x21f8
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x5c58

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6F98990F-FCE4-3DC6-9282-EB080D9B8074
-  Functions: 22427
-  Symbols:   63935
-  CStrings:  30527
+  UUID: C7B6CB0A-5D84-3279-BAD4-0E0E4CD4D140
+  Functions: 22480
+  Symbols:   64047
+  CStrings:  30579
 
Symbols:
+ +[SBHClockApplicationIconImageView _displayLinkFired:]
+ +[SBHClockApplicationIconImageView _tickTimerFired:]
+ +[SBHClockApplicationIconImageView sweepsSecondHandDidChange]
+ +[SBHClockApplicationIconImageView sweepsSecondsHand]
+ +[SBIcon makeIconLayerFromImage:]
+ +[SBIconListModel gridCellInfoIconTypeForIcon:]
+ -[SBDockView _applyGlass]
+ -[SBHClockBackgroundIconDataSource uniqueIdentifier]
+ -[SBHFloatyFolderVisualConfiguration isTitleVerticallyCentered]
+ -[SBHIconDragAutoScrollAssistant initWithDelegate:referenceView:vertical:]
+ -[SBIconImageView backdropGroupName]
+ -[SBIconImageView isGlassHidden]
+ -[SBIconImageView setBackdropGroupName:]
+ -[SBIconImageView setGlassHidden:]
+ -[SBIconListModel _otherGridCellInfoOptionsForGridCellInfoOptions:]
+ -[SBIconListModel _otherListForGridCellInfoOptions:createIfNecessary:]
+ -[SBIconListModel _updateOtherListWithGridCellInfoOptions:mutationOptions:createIfNecessary:usingBlock:]
+ -[SBIconListModel representsSelf:]
+ -[SBIconListModel saveCurrentLocationAsFixedForIcon:gridCellInfo:]
+ -[SBIconListModel saveCurrentLocationAsFixedForIcon:gridCellInfoOptions:]
+ -[SBIconListModel shouldRemoveAlreadyContainedIconWhenRemovingFromOtherPositionsInHierarchy:gridCellInfoOptions:mutationOptions:]
+ -[SBIconListView iconViewBackdropGroupName]
+ -[SBIconListView iconViewsAllowGlassGrouping]
+ -[SBIconListView isIconViewGlassHidden]
+ -[SBIconListView setIconViewBackdropGroupName:]
+ -[SBIconListView setIconViewGlassHidden:]
+ -[SBIconListView setIconViewsAllowGlassGrouping:]
+ -[SBIconView iconImageAllowsGlassGrouping]
+ -[SBIconView iconImageBackdropGroupName]
+ -[SBIconView isIconImageGlassHidden]
+ -[SBIconView setIconImageAllowsGlassGrouping:]
+ -[SBIconView setIconImageBackdropGroupName:]
+ -[SBIconView setIconImageGlassHidden:]
+ -[SBLeafIcon dataSourceIconServicesIconForImage]
+ -[SBRotatedIconListModel representsSelf:]
+ -[SBRotatedIconListModel shouldRemoveAlreadyContainedIconWhenRemovingFromOtherPositionsInHierarchy:gridCellInfoOptions:mutationOptions:]
+ GCC_except_table156
+ GCC_except_table161
+ GCC_except_table172
+ GCC_except_table201
+ GCC_except_table203
+ GCC_except_table206
+ GCC_except_table211
+ GCC_except_table225
+ GCC_except_table252
+ GCC_except_table259
+ GCC_except_table266
+ GCC_except_table279
+ GCC_except_table331
+ GCC_except_table348
+ GCC_except_table357
+ GCC_except_table363
+ GCC_except_table371
+ GCC_except_table383
+ GCC_except_table397
+ GCC_except_table399
+ GCC_except_table408
+ GCC_except_table409
+ GCC_except_table411
+ GCC_except_table416
+ GCC_except_table440
+ GCC_except_table443
+ GCC_except_table472
+ GCC_except_table474
+ GCC_except_table512
+ GCC_except_table545
+ GCC_except_table55
+ GCC_except_table564
+ GCC_except_table577
+ GCC_except_table633
+ GCC_except_table665
+ GCC_except_table749
+ GCC_except_table751
+ _OBJC_IVAR_$_SBHIconDragAutoScrollAssistant._vertical
+ _OBJC_IVAR_$_SBIconImageView._backdropGroupName
+ _OBJC_IVAR_$_SBIconImageView._glassHidden
+ _OBJC_IVAR_$_SBIconListView._iconViewBackdropGroupName
+ _OBJC_IVAR_$_SBIconListView._iconViewGlassHidden
+ _OBJC_IVAR_$_SBIconListView._iconViewsAllowGlassGrouping
+ _OBJC_IVAR_$_SBIconView._disallowsGlassGrouping
+ _OBJC_IVAR_$_SBIconView._iconImageBackdropGroupName
+ _OBJC_IVAR_$_SBIconView._iconImageGlassHidden
+ _SBIconZoomContractionAnimationWillBeginNotification
+ __PROPERTIES__TtC15SpringBoardHomeP33_14F9E5E684559CC7FCC39AA4C6A93D2732GenericApplicationIconDataSource
+ __SBClockIconResetTickTimer
+ ___33+[SBIcon makeIconLayerFromImage:]_block_invoke
+ ___41-[SBIconListView setIconViewGlassHidden:]_block_invoke
+ ___47-[SBIconListView setIconViewBackdropGroupName:]_block_invoke
+ ___49-[SBIconListView setIconViewsAllowGlassGrouping:]_block_invoke
+ ___66-[SBHIconDragAutoScrollAssistant _autoScrollDirectionForLocation:]_block_invoke_3
+ ___66-[SBHIconDragAutoScrollAssistant _autoScrollDirectionForLocation:]_block_invoke_4
+ ___79-[SBHIconManager pushExpandedIcon:location:context:animated:completionHandler:]_block_invoke.529
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.601
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.604
+ ___block_descriptor_117_e8_32s40s48s56s_e47_q24?0{SBHIconGridRange=Q{SBHIconGridSize=SS}}8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e28_q24?0"SBIconListModel"8Q16ls32l8s40l8s48l8
+ ___block_literal_global.102
+ ___block_literal_global.104
+ ___block_literal_global.107
+ ___block_literal_global.117
+ ___block_literal_global.1245
+ ___block_literal_global.2739
+ ___block_literal_global.603
+ ___displayLink
+ _block_copy_helper.254
+ _block_copy_helper.263
+ _block_copy_helper.271
+ _block_copy_helper.279
+ _block_copy_helper.289
+ _block_copy_helper.299
+ _block_copy_helper.309
+ _block_copy_helper.317
+ _block_copy_helper.327
+ _block_copy_helper.337
+ _block_copy_helper.347
+ _block_copy_helper.357
+ _block_copy_helper.367
+ _block_copy_helper.377
+ _block_copy_helper.387
+ _block_copy_helper.397
+ _block_copy_helper.407
+ _block_copy_helper.417
+ _block_copy_helper.427
+ _block_copy_helper.438
+ _block_copy_helper.448
+ _block_copy_helper.458
+ _block_copy_helper.468
+ _block_copy_helper.478
+ _block_copy_helper.488
+ _block_copy_helper.498
+ _block_copy_helper.504
+ _block_copy_helper.514
+ _block_copy_helper.524
+ _block_copy_helper.534
+ _block_copy_helper.544
+ _block_copy_helper.554
+ _block_copy_helper.564
+ _block_copy_helper.573
+ _block_copy_helper.583
+ _block_copy_helper.594
+ _block_copy_helper.604
+ _block_copy_helper.615
+ _block_copy_helper.626
+ _block_copy_helper.636
+ _block_copy_helper.646
+ _block_copy_helper.656
+ _block_copy_helper.666
+ _block_copy_helper.677
+ _block_copy_helper.687
+ _block_copy_helper.698
+ _block_copy_helper.709
+ _block_copy_helper.720
+ _block_copy_helper.731
+ _block_copy_helper.742
+ _block_copy_helper.753
+ _block_copy_helper.764
+ _block_copy_helper.774
+ _block_copy_helper.784
+ _block_copy_helper.794
+ _block_copy_helper.804
+ _block_copy_helper.815
+ _block_copy_helper.96
+ _block_descriptor.256
+ _block_descriptor.265
+ _block_descriptor.273
+ _block_descriptor.281
+ _block_descriptor.291
+ _block_descriptor.301
+ _block_descriptor.311
+ _block_descriptor.319
+ _block_descriptor.329
+ _block_descriptor.339
+ _block_descriptor.349
+ _block_descriptor.359
+ _block_descriptor.369
+ _block_descriptor.379
+ _block_descriptor.389
+ _block_descriptor.399
+ _block_descriptor.409
+ _block_descriptor.419
+ _block_descriptor.429
+ _block_descriptor.440
+ _block_descriptor.450
+ _block_descriptor.460
+ _block_descriptor.470
+ _block_descriptor.480
+ _block_descriptor.490
+ _block_descriptor.500
+ _block_descriptor.506
+ _block_descriptor.516
+ _block_descriptor.526
+ _block_descriptor.536
+ _block_descriptor.546
+ _block_descriptor.556
+ _block_descriptor.566
+ _block_descriptor.575
+ _block_descriptor.585
+ _block_descriptor.596
+ _block_descriptor.606
+ _block_descriptor.617
+ _block_descriptor.628
+ _block_descriptor.638
+ _block_descriptor.648
+ _block_descriptor.658
+ _block_descriptor.668
+ _block_descriptor.679
+ _block_descriptor.689
+ _block_descriptor.700
+ _block_descriptor.711
+ _block_descriptor.722
+ _block_descriptor.733
+ _block_descriptor.744
+ _block_descriptor.755
+ _block_descriptor.766
+ _block_descriptor.776
+ _block_descriptor.786
+ _block_descriptor.796
+ _block_descriptor.806
+ _block_descriptor.817
+ _block_descriptor.98
+ _block_destroy_helper.255
+ _block_destroy_helper.264
+ _block_destroy_helper.272
+ _block_destroy_helper.280
+ _block_destroy_helper.290
+ _block_destroy_helper.300
+ _block_destroy_helper.310
+ _block_destroy_helper.318
+ _block_destroy_helper.328
+ _block_destroy_helper.338
+ _block_destroy_helper.348
+ _block_destroy_helper.358
+ _block_destroy_helper.368
+ _block_destroy_helper.378
+ _block_destroy_helper.388
+ _block_destroy_helper.398
+ _block_destroy_helper.408
+ _block_destroy_helper.418
+ _block_destroy_helper.428
+ _block_destroy_helper.439
+ _block_destroy_helper.449
+ _block_destroy_helper.459
+ _block_destroy_helper.469
+ _block_destroy_helper.479
+ _block_destroy_helper.489
+ _block_destroy_helper.499
+ _block_destroy_helper.505
+ _block_destroy_helper.515
+ _block_destroy_helper.525
+ _block_destroy_helper.535
+ _block_destroy_helper.545
+ _block_destroy_helper.555
+ _block_destroy_helper.565
+ _block_destroy_helper.574
+ _block_destroy_helper.584
+ _block_destroy_helper.595
+ _block_destroy_helper.605
+ _block_destroy_helper.616
+ _block_destroy_helper.627
+ _block_destroy_helper.637
+ _block_destroy_helper.647
+ _block_destroy_helper.657
+ _block_destroy_helper.667
+ _block_destroy_helper.678
+ _block_destroy_helper.688
+ _block_destroy_helper.699
+ _block_destroy_helper.710
+ _block_destroy_helper.721
+ _block_destroy_helper.732
+ _block_destroy_helper.743
+ _block_destroy_helper.754
+ _block_destroy_helper.765
+ _block_destroy_helper.775
+ _block_destroy_helper.785
+ _block_destroy_helper.795
+ _block_destroy_helper.805
+ _block_destroy_helper.816
+ _block_destroy_helper.97
+ _objc_msgSend$_applyGlass
+ _objc_msgSend$_otherGridCellInfoOptionsForGridCellInfoOptions:
+ _objc_msgSend$_otherListForGridCellInfoOptions:createIfNecessary:
+ _objc_msgSend$_updateOtherListWithGridCellInfoOptions:mutationOptions:createIfNecessary:usingBlock:
+ _objc_msgSend$dataSourceIconServicesIconForImage
+ _objc_msgSend$fireDate
+ _objc_msgSend$gridCellInfoIconTypeForIcon:
+ _objc_msgSend$iconDragManager:wantsAutoScrollInDirection:
+ _objc_msgSend$iconImageAllowsGlassGrouping
+ _objc_msgSend$iconImageBackdropGroupName
+ _objc_msgSend$iconViewBackdropGroupName
+ _objc_msgSend$iconViewsAllowGlassGrouping
+ _objc_msgSend$initWithDelegate:referenceView:vertical:
+ _objc_msgSend$isGlassHidden
+ _objc_msgSend$isIconImageGlassHidden
+ _objc_msgSend$isIconViewGlassHidden
+ _objc_msgSend$isTitleVerticallyCentered
+ _objc_msgSend$representsSelf:
+ _objc_msgSend$saveCurrentLocationAsFixedForIcon:gridCellInfo:
+ _objc_msgSend$sbh_applyDockGlassWithGrouping:userInterfaceStyle:highlightsDisplayAngle:
+ _objc_msgSend$setGlassHidden:
+ _objc_msgSend$setIconImageAllowsGlassGrouping:
+ _objc_msgSend$setIconImageBackdropGroupName:
+ _objc_msgSend$setIconImageGlassHidden:
+ _objc_msgSend$setIconViewBackdropGroupName:
+ _objc_msgSend$setIconViewsAllowGlassGrouping:
+ _objc_msgSend$shouldRemoveAlreadyContainedIconWhenRemovingFromOtherPositionsInHierarchy:gridCellInfoOptions:mutationOptions:
+ _objc_msgSend$sweepsSecondHandDidChange
+ _objc_msgSend$sweepsSecondsHand
- +[SBHClockApplicationIconImageView _minuteTimerFired:]
- +[SBHClockApplicationIconImageView _timerFired:]
- -[SBHFloatyFolderVisualConfiguration titleVerticallyCentered]
- GCC_except_table154
- GCC_except_table160
- GCC_except_table171
- GCC_except_table202
- GCC_except_table204
- GCC_except_table207
- GCC_except_table212
- GCC_except_table222
- GCC_except_table260
- GCC_except_table280
- GCC_except_table288
- GCC_except_table325
- GCC_except_table345
- GCC_except_table354
- GCC_except_table358
- GCC_except_table365
- GCC_except_table378
- GCC_except_table394
- GCC_except_table396
- GCC_except_table400
- GCC_except_table402
- GCC_except_table405
- GCC_except_table410
- GCC_except_table434
- GCC_except_table446
- GCC_except_table467
- GCC_except_table469
- GCC_except_table507
- GCC_except_table539
- GCC_except_table54
- GCC_except_table558
- GCC_except_table572
- GCC_except_table628
- GCC_except_table660
- GCC_except_table741
- GCC_except_table743
- GCC_except_table88
- __SBClockIconResetMinuteTimer
- ___33-[SBIcon makeIconLayerFromImage:]_block_invoke
- ___77-[SBIconListModel replaceIcon:withIcons:gridCellInfoOptions:mutationOptions:]_block_invoke_2
- ___77-[SBIconListModel replaceIcon:withIcons:gridCellInfoOptions:mutationOptions:]_block_invoke_3
- ___79-[SBHIconManager pushExpandedIcon:location:context:animated:completionHandler:]_block_invoke.527
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.599
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.602
- ___block_descriptor_108_e8_32s40s48s_e47_q24?0{SBHIconGridRange=Q{SBHIconGridSize=SS}}8ls32l8s40l8s48l8
- ___block_descriptor_48_e8_32s40s_e25_v16?0"SBIconListModel"8ls32l8s40l8
- ___block_literal_global.101
- ___block_literal_global.106
- ___block_literal_global.116
- ___block_literal_global.1231
- ___block_literal_global.136
- ___block_literal_global.2725
- ___block_literal_global.312
- ___block_literal_global.601
- ___block_literal_global.99
- ___minuteTimer
- _block_copy_helper.253
- _block_copy_helper.262
- _block_copy_helper.270
- _block_copy_helper.278
- _block_copy_helper.288
- _block_copy_helper.298
- _block_copy_helper.308
- _block_copy_helper.316
- _block_copy_helper.326
- _block_copy_helper.336
- _block_copy_helper.346
- _block_copy_helper.356
- _block_copy_helper.366
- _block_copy_helper.376
- _block_copy_helper.386
- _block_copy_helper.396
- _block_copy_helper.406
- _block_copy_helper.416
- _block_copy_helper.426
- _block_copy_helper.437
- _block_copy_helper.447
- _block_copy_helper.457
- _block_copy_helper.467
- _block_copy_helper.477
- _block_copy_helper.487
- _block_copy_helper.497
- _block_copy_helper.503
- _block_copy_helper.513
- _block_copy_helper.523
- _block_copy_helper.533
- _block_copy_helper.543
- _block_copy_helper.553
- _block_copy_helper.563
- _block_copy_helper.572
- _block_copy_helper.582
- _block_copy_helper.593
- _block_copy_helper.603
- _block_copy_helper.614
- _block_copy_helper.625
- _block_copy_helper.635
- _block_copy_helper.645
- _block_copy_helper.655
- _block_copy_helper.665
- _block_copy_helper.676
- _block_copy_helper.686
- _block_copy_helper.697
- _block_copy_helper.708
- _block_copy_helper.719
- _block_copy_helper.730
- _block_copy_helper.741
- _block_copy_helper.752
- _block_copy_helper.763
- _block_copy_helper.773
- _block_copy_helper.783
- _block_copy_helper.793
- _block_copy_helper.803
- _block_copy_helper.814
- _block_descriptor.255
- _block_descriptor.264
- _block_descriptor.272
- _block_descriptor.280
- _block_descriptor.290
- _block_descriptor.300
- _block_descriptor.310
- _block_descriptor.318
- _block_descriptor.328
- _block_descriptor.338
- _block_descriptor.348
- _block_descriptor.358
- _block_descriptor.368
- _block_descriptor.378
- _block_descriptor.388
- _block_descriptor.398
- _block_descriptor.408
- _block_descriptor.418
- _block_descriptor.428
- _block_descriptor.439
- _block_descriptor.449
- _block_descriptor.459
- _block_descriptor.469
- _block_descriptor.479
- _block_descriptor.489
- _block_descriptor.499
- _block_descriptor.505
- _block_descriptor.515
- _block_descriptor.525
- _block_descriptor.535
- _block_descriptor.545
- _block_descriptor.555
- _block_descriptor.565
- _block_descriptor.574
- _block_descriptor.584
- _block_descriptor.595
- _block_descriptor.605
- _block_descriptor.616
- _block_descriptor.627
- _block_descriptor.637
- _block_descriptor.647
- _block_descriptor.657
- _block_descriptor.667
- _block_descriptor.678
- _block_descriptor.688
- _block_descriptor.699
- _block_descriptor.710
- _block_descriptor.721
- _block_descriptor.732
- _block_descriptor.743
- _block_descriptor.754
- _block_descriptor.765
- _block_descriptor.775
- _block_descriptor.785
- _block_descriptor.795
- _block_descriptor.805
- _block_descriptor.816
- _block_destroy_helper.254
- _block_destroy_helper.263
- _block_destroy_helper.271
- _block_destroy_helper.279
- _block_destroy_helper.289
- _block_destroy_helper.299
- _block_destroy_helper.309
- _block_destroy_helper.317
- _block_destroy_helper.327
- _block_destroy_helper.337
- _block_destroy_helper.347
- _block_destroy_helper.357
- _block_destroy_helper.367
- _block_destroy_helper.377
- _block_destroy_helper.387
- _block_destroy_helper.397
- _block_destroy_helper.407
- _block_destroy_helper.417
- _block_destroy_helper.427
- _block_destroy_helper.438
- _block_destroy_helper.448
- _block_destroy_helper.458
- _block_destroy_helper.468
- _block_destroy_helper.478
- _block_destroy_helper.488
- _block_destroy_helper.498
- _block_destroy_helper.504
- _block_destroy_helper.514
- _block_destroy_helper.524
- _block_destroy_helper.534
- _block_destroy_helper.544
- _block_destroy_helper.554
- _block_destroy_helper.564
- _block_destroy_helper.573
- _block_destroy_helper.583
- _block_destroy_helper.594
- _block_destroy_helper.604
- _block_destroy_helper.615
- _block_destroy_helper.626
- _block_destroy_helper.636
- _block_destroy_helper.646
- _block_destroy_helper.656
- _block_destroy_helper.666
- _block_destroy_helper.677
- _block_destroy_helper.687
- _block_destroy_helper.698
- _block_destroy_helper.709
- _block_destroy_helper.720
- _block_destroy_helper.731
- _block_destroy_helper.742
- _block_destroy_helper.753
- _block_destroy_helper.764
- _block_destroy_helper.774
- _block_destroy_helper.784
- _block_destroy_helper.794
- _block_destroy_helper.804
- _block_destroy_helper.815
- _objc_msgSend$initWithDelegate:referenceView:
- _objc_msgSend$sbh_applyDockGlass
- _objc_msgSend$sbh_pauseSpecularHighlightAnimationOnDockGlass
- _objc_msgSend$sbh_resumeSpecularHighlightAnimationOnDockGlass
- _objc_msgSend$titleVerticallyCentered
CStrings:
+ "@\"SBFolderController\"24@0:8@\"SBIconDragManager\"16"
+ "@28@0:8Q16B24"
+ "GenericApplication"
+ "SBIconZoomContractionAnimationWillBeginNotification"
+ "T@\"NSString\",C,N,V_iconImageBackdropGroupName"
+ "T@\"NSString\",C,N,V_iconViewBackdropGroupName"
+ "TB,N,GisGlassHidden,V_glassHidden"
+ "TB,N,GisIconImageGlassHidden"
+ "TB,N,GisIconViewGlassHidden,V_iconViewGlassHidden"
+ "TB,N,GisTitleVerticallyCentered,V_titleVerticallyCentered"
+ "TB,N,V_iconViewsAllowGlassGrouping"
+ "_applyGlass"
+ "_disallowsGlassGrouping"
+ "_glassHidden"
+ "_iconImageBackdropGroupName"
+ "_iconImageGlassHidden"
+ "_iconViewBackdropGroupName"
+ "_iconViewGlassHidden"
+ "_iconViewsAllowGlassGrouping"
+ "_isGlassHidden"
+ "_otherGridCellInfoOptionsForGridCellInfoOptions:"
+ "_otherListForGridCellInfoOptions:createIfNecessary:"
+ "_tickTimerFired:"
+ "_updateOtherListWithGridCellInfoOptions:mutationOptions:createIfNecessary:usingBlock:"
+ "dataSourceIconServicesIconForImage"
+ "fireDate"
+ "glassHidden"
+ "gridCellInfoIconTypeForIcon:"
+ "iconDragManager:wantsAutoScrollInDirection:"
+ "iconImageAllowsGlassGrouping"
+ "iconImageBackdropGroupName"
+ "iconImageGlassHidden"
+ "iconViewBackdropGroupName"
+ "iconViewGlassHidden"
+ "iconViewsAllowGlassGrouping"
+ "initWithDelegate:referenceView:vertical:"
+ "isGlassHidden"
+ "isIconImageGlassHidden"
+ "isIconViewGlassHidden"
+ "isTitleVerticallyCentered"
+ "q24@?0@\"SBIconListModel\"8Q16"
+ "representsSelf:"
+ "saveCurrentLocationAsFixedForIcon:gridCellInfo:"
+ "saveCurrentLocationAsFixedForIcon:gridCellInfoOptions:"
+ "sbh_applyDockGlassWithGrouping:userInterfaceStyle:highlightsDisplayAngle:"
+ "setGlassHidden:"
+ "setIconImageAllowsGlassGrouping:"
+ "setIconImageBackdropGroupName:"
+ "setIconImageGlassHidden:"
+ "setIconViewBackdropGroupName:"
+ "setIconViewGlassHidden:"
+ "setIconViewsAllowGlassGrouping:"
+ "shouldRemoveAlreadyContainedIconWhenRemovingFromOtherPositionsInHierarchy:gridCellInfoOptions:mutationOptions:"
+ "sweepsSecondHandDidChange"
+ "sweepsSecondsHand"
+ "v32@0:8@\"SBIconDragManager\"16q24"
+ "v32@0:8B16q20B28"
+ "v44@0:8Q16Q24B32@?36"
+ "\xd1"
- "@\"SBRootFolderController\"24@0:8@\"SBIconDragManager\"16"
- "SBHApplicationBundleIdentifier"
- "SBHIconTypeIdentifier"
- "TB,N,V_titleVerticallyCentered"
- "_minuteTimerFired:"
- "_timerFired:"
- "sbh_pauseSpecularHighlightAnimationOnDockGlass"
- "sbh_resumeSpecularHighlightAnimationOnDockGlass"

```
