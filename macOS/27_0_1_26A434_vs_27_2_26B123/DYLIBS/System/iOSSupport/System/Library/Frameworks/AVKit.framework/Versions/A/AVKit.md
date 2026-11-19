## AVKit

> `/System/iOSSupport/System/Library/Frameworks/AVKit.framework/Versions/A/AVKit`

```diff

-1360.75.5.3.0
-  __TEXT.__text: 0x160fc0
-  __TEXT.__objc_methlist: 0x193e0
+1385.14.5.1.0
+  __TEXT.__text: 0x163140
+  __TEXT.__objc_methlist: 0x19668
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__const: 0x2270
   __TEXT.__constg_swiftt: 0x9d0

   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0x88
   __TEXT.__swift5_types: 0x70
-  __TEXT.__cstring: 0xc354
+  __TEXT.__cstring: 0xc4ff
   __TEXT.__swift5_capture: 0x448
   __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_cont: 0x50
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__gcc_except_tab: 0x3690
-  __TEXT.__oslogstring: 0x4dba
+  __TEXT.__gcc_except_tab: 0x36dc
+  __TEXT.__oslogstring: 0x4ec9
   __TEXT.__ustring: 0x3c
-  __TEXT.__unwind_info: 0x5d18
+  __TEXT.__unwind_info: 0x5da0
   __TEXT.__eh_frame: 0xc28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2670
-  __DATA_CONST.__objc_classlist: 0x878
+  __DATA_CONST.__objc_classlist: 0x890
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x460
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa8d8
-  __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x698
+  __DATA_CONST.__objc_selrefs: 0xa9c0
+  __DATA_CONST.__objc_protorefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0x168
-  __DATA_CONST.__got: 0x1060
-  __AUTH_CONST.__const: 0x3050
-  __AUTH_CONST.__cfstring: 0x5a00
-  __AUTH_CONST.__objc_const: 0x2e298
+  __DATA_CONST.__got: 0x1080
+  __AUTH_CONST.__const: 0x3070
+  __AUTH_CONST.__cfstring: 0x5a80
+  __AUTH_CONST.__objc_const: 0x2e8d0
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x210
-  __AUTH_CONST.__auth_got: 0xf48
-  __AUTH_CONST.__auth_ptr: 0x538
-  __AUTH.__objc_data: 0x4b90
-  __AUTH.__data: 0x3e8
-  __DATA.__objc_ivar: 0x28e8
+  __AUTH_CONST.__auth_got: 0xf50
+  __AUTH_CONST.__auth_ptr: 0x540
+  __AUTH.__objc_data: 0x4658
+  __AUTH.__data: 0x3c0
+  __DATA.__objc_ivar: 0x2954
   __DATA.__data: 0x3a40
-  __DATA.__bss: 0x14c8
+  __DATA.__bss: 0x14d8
   __DATA.__common: 0xe8
-  __DATA_DIRTY.__objc_data: 0x1128
-  __DATA_DIRTY.__data: 0x80
+  __DATA_DIRTY.__objc_data: 0x1750
+  __DATA_DIRTY.__data: 0xa0
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9526
-  Symbols:   20181
-  CStrings:  1679
+  Functions: 9586
+  Symbols:   20319
+  CStrings:  1690
 
Symbols:
+ +[AVCaptureDeviceDescriptor descriptorWithStateDescriptor:]
+ +[AVCaptureDeviceDirectionCoordinator _buildDefaultMapWithUtilities:]
+ +[AVCaptureDeviceDirectionCoordinator _isLegacyDevice]
+ +[AVCaptureDeviceDirectionMap mapWithForwardFacingDeviceDescriptors:backwardFacingDeviceDescriptors:]
+ -[AVCaptureDeviceDescriptor .cxx_destruct]
+ -[AVCaptureDeviceDescriptor _initWithStateDescriptor:]
+ -[AVCaptureDeviceDescriptor debugDescription]
+ -[AVCaptureDeviceDescriptor description]
+ -[AVCaptureDeviceDescriptor deviceType]
+ -[AVCaptureDeviceDescriptor hash]
+ -[AVCaptureDeviceDescriptor isEqual:]
+ -[AVCaptureDeviceDescriptor localizedName]
+ -[AVCaptureDeviceDescriptor mediaTypes]
+ -[AVCaptureDeviceDescriptor position]
+ -[AVCaptureDeviceDescriptor uniqueID]
+ -[AVCaptureDeviceDirectionCoordinator .cxx_destruct]
+ -[AVCaptureDeviceDirectionCoordinator _updateCurrentMap]
+ -[AVCaptureDeviceDirectionCoordinator deviceDirections]
+ -[AVCaptureDeviceDirectionCoordinator initWithView:deviceTypes:changeHandler:]
+ -[AVCaptureDeviceDirectionMap .cxx_destruct]
+ -[AVCaptureDeviceDirectionMap _initWithForwardFacingDeviceDescriptors:backwardFacingDeviceDescriptors:]
+ -[AVCaptureDeviceDirectionMap backwardFacingDeviceDescriptors]
+ -[AVCaptureDeviceDirectionMap debugDescription]
+ -[AVCaptureDeviceDirectionMap description]
+ -[AVCaptureDeviceDirectionMap forwardFacingDeviceDescriptors]
+ -[AVCaptureDeviceDirectionMap hash]
+ -[AVCaptureDeviceDirectionMap isEqual:]
+ -[AVControlsViewController effectiveAutoHideInterval]
+ -[AVMenuButton _contextMenu]
+ -[AVMobileChromelessPlaybackControlsView sizeThatFits:]
+ -[AVMobileGlassContentTabsView _updateContentTabsChildMarginsIfNeeded]
+ -[AVMobileGlassControlsStyleSheet contentTabsAdditionalRightInset]
+ -[AVMobileGlassControlsView isEffectivelyFullScreen]
+ -[AVMobileGlassControlsView setEffectivelyFullScreen:]
+ -[AVMobileGlassControlsViewController _updateControlsViewArrangedAndWide]
+ -[AVMobileGlassControlsViewController effectiveAutoHideInterval]
+ -[AVMobileGlassControlsViewController isEffectivelyFullScreen]
+ -[AVMobileGlassControlsViewController setEffectivelyFullScreen:]
+ -[AVMobileGlassDisplayModeControlsView isEffectivelyFullScreen]
+ -[AVMobileGlassDisplayModeControlsView rightBarInsetReservedByOwner]
+ -[AVMobileGlassDisplayModeControlsView setEffectivelyFullScreen:]
+ -[AVMobileGlassDisplayModeControlsView setRightBarInsetReservedByOwner:]
+ -[AVMobileGlassPlaybackControlsView _paddingForAvailableSpace:]
+ -[AVMobileGlassVolumeControlsView isEffectivelyFullScreen]
+ -[AVMobileGlassVolumeControlsView rightBarInsetReservedByOwner]
+ -[AVMobileGlassVolumeControlsView setEffectivelyFullScreen:]
+ -[AVMobileGlassVolumeControlsView setRightBarInsetReservedByOwner:]
+ -[AVPlayerViewController controlsViewControllerWillEvaluateContentTabPresentationInfo:]
+ -[AVPlayerViewControllerContentView _updateControlsViewControllerArrangementLayoutPlaneIfNeeded]
+ -[AVPlayerViewControllerContentView _updateControlsViewControllerEffectivelyFullScreenIfNeeded]
+ -[UIView(AVAdditions) avkit_defaultCompactStatusBarRightInset:isEffectivelyFullScreen:]
+ -[UIView(AVAdditions) avkit_horizontalEdgeInsetsForBarOnEdge:extent:reservedRightInset:]
+ -[UIView(AVAdditions) avkit_reservedRightInsetForBarWithExtent:controlsViewLayoutPlane:isEffectivelyFullScreen:]
+ -[UIWindow(AVAdditions_Internal_Mobile) avkit_isInsetFromScreenRightEdge]
+ -[UIWindowScene(AVAdditions) avkit_coversScreen]
+ GCC_except_table1000
+ GCC_except_table1101
+ GCC_except_table1128
+ GCC_except_table1141
+ GCC_except_table1208
+ GCC_except_table1215
+ GCC_except_table1223
+ GCC_except_table1234
+ GCC_except_table1246
+ GCC_except_table1250
+ GCC_except_table1251
+ GCC_except_table1281
+ GCC_except_table1282
+ GCC_except_table1294
+ GCC_except_table1302
+ GCC_except_table1308
+ GCC_except_table1322
+ GCC_except_table1327
+ GCC_except_table1364
+ GCC_except_table1372
+ GCC_except_table1374
+ GCC_except_table1379
+ GCC_except_table1430
+ GCC_except_table1436
+ GCC_except_table1444
+ GCC_except_table1445
+ GCC_except_table1446
+ GCC_except_table1460
+ GCC_except_table1760
+ GCC_except_table1763
+ GCC_except_table1799
+ GCC_except_table1850
+ GCC_except_table1929
+ GCC_except_table1930
+ GCC_except_table1938
+ GCC_except_table1981
+ GCC_except_table1986
+ GCC_except_table2001
+ GCC_except_table2069
+ GCC_except_table2191
+ GCC_except_table2391
+ GCC_except_table2394
+ GCC_except_table2425
+ GCC_except_table2426
+ GCC_except_table2522
+ GCC_except_table2545
+ GCC_except_table2781
+ GCC_except_table2932
+ GCC_except_table3108
+ GCC_except_table3130
+ GCC_except_table3310
+ GCC_except_table3315
+ GCC_except_table3317
+ GCC_except_table3321
+ GCC_except_table3344
+ GCC_except_table3350
+ GCC_except_table3354
+ GCC_except_table3356
+ GCC_except_table3361
+ GCC_except_table3369
+ GCC_except_table3384
+ GCC_except_table3397
+ GCC_except_table3435
+ GCC_except_table3444
+ GCC_except_table3449
+ GCC_except_table3483
+ GCC_except_table3495
+ GCC_except_table3523
+ GCC_except_table3529
+ GCC_except_table3543
+ GCC_except_table3606
+ GCC_except_table3632
+ GCC_except_table3641
+ GCC_except_table3675
+ GCC_except_table3676
+ GCC_except_table3702
+ GCC_except_table3759
+ GCC_except_table3835
+ GCC_except_table3836
+ GCC_except_table3921
+ GCC_except_table3982
+ GCC_except_table4015
+ GCC_except_table4090
+ GCC_except_table4111
+ GCC_except_table4302
+ GCC_except_table4415
+ GCC_except_table4576
+ GCC_except_table4977
+ GCC_except_table4983
+ GCC_except_table4991
+ GCC_except_table5003
+ GCC_except_table5024
+ GCC_except_table5033
+ GCC_except_table5035
+ GCC_except_table5093
+ GCC_except_table5145
+ GCC_except_table5423
+ GCC_except_table5424
+ GCC_except_table5425
+ GCC_except_table5435
+ GCC_except_table5597
+ GCC_except_table5628
+ GCC_except_table5631
+ GCC_except_table5637
+ GCC_except_table5642
+ GCC_except_table5682
+ GCC_except_table571
+ GCC_except_table5766
+ GCC_except_table5955
+ GCC_except_table5964
+ GCC_except_table5998
+ GCC_except_table6000
+ GCC_except_table6011
+ GCC_except_table6055
+ GCC_except_table610
+ GCC_except_table6104
+ GCC_except_table6120
+ GCC_except_table624
+ GCC_except_table6258
+ GCC_except_table6278
+ GCC_except_table6344
+ GCC_except_table6455
+ GCC_except_table6462
+ GCC_except_table6573
+ GCC_except_table6594
+ GCC_except_table6596
+ GCC_except_table6705
+ GCC_except_table6734
+ GCC_except_table6735
+ GCC_except_table6769
+ GCC_except_table6771
+ GCC_except_table684
+ GCC_except_table6891
+ GCC_except_table6995
+ GCC_except_table7084
+ GCC_except_table7104
+ GCC_except_table7108
+ GCC_except_table7120
+ GCC_except_table7223
+ GCC_except_table7226
+ GCC_except_table7229
+ GCC_except_table7231
+ GCC_except_table7364
+ GCC_except_table7433
+ GCC_except_table7464
+ GCC_except_table7465
+ GCC_except_table7466
+ GCC_except_table7467
+ GCC_except_table7471
+ GCC_except_table7488
+ GCC_except_table751
+ GCC_except_table7511
+ GCC_except_table7530
+ GCC_except_table7606
+ GCC_except_table7739
+ GCC_except_table7741
+ GCC_except_table7755
+ GCC_except_table7994
+ GCC_except_table8000
+ GCC_except_table8139
+ GCC_except_table8161
+ GCC_except_table8289
+ GCC_except_table8296
+ GCC_except_table8310
+ GCC_except_table8494
+ GCC_except_table8510
+ GCC_except_table8511
+ GCC_except_table8515
+ GCC_except_table8523
+ GCC_except_table8559
+ GCC_except_table8581
+ GCC_except_table8635
+ GCC_except_table881
+ GCC_except_table905
+ OBJC_IVAR_$_AVCaptureDeviceDescriptor._deviceType
+ OBJC_IVAR_$_AVCaptureDeviceDescriptor._localizedName
+ OBJC_IVAR_$_AVCaptureDeviceDescriptor._mediaTypes
+ OBJC_IVAR_$_AVCaptureDeviceDescriptor._position
+ OBJC_IVAR_$_AVCaptureDeviceDescriptor._uniqueID
+ OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._changeHandler
+ OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._currentMap
+ OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._defaultMap
+ OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._deviceTypes
+ OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._hasPublishedInitialMap
+ OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._lock
+ OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._stateCoordinatorUtilities
+ OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._utilitiesQueue
+ OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._view
+ OBJC_IVAR_$_AVCaptureDeviceDirectionMap._backwardFacingDeviceDescriptors
+ OBJC_IVAR_$_AVCaptureDeviceDirectionMap._forwardFacingDeviceDescriptors
+ OBJC_IVAR_$_AVControlItem._menu
+ OBJC_IVAR_$_AVMobileGlassControlsStyleSheet._contentTabsAdditionalRightInset
+ OBJC_IVAR_$_AVMobileGlassControlsView._effectivelyFullScreen
+ OBJC_IVAR_$_AVMobileGlassControlsView._topControlsRightInsetReserve
+ OBJC_IVAR_$_AVMobileGlassControlsViewController._controlsViewArrangedAndWide
+ OBJC_IVAR_$_AVMobileGlassControlsViewController._effectivelyFullScreen
+ OBJC_IVAR_$_AVMobileGlassDisplayModeControlsView._effectivelyFullScreen
+ OBJC_IVAR_$_AVMobileGlassDisplayModeControlsView._rightBarInsetReservedByOwner
+ OBJC_IVAR_$_AVMobileGlassVolumeControlsView._effectivelyFullScreen
+ OBJC_IVAR_$_AVMobileGlassVolumeControlsView._rightBarInsetReservedByOwner
+ OBJC_IVAR_$_AVMobileGlassVolumeControlsView._volumeSliderContainer
+ _MGCopyAnswer
+ _OBJC_CLASS_$_AVCaptureDeviceDescriptor
+ _OBJC_CLASS_$_AVCaptureDeviceDirectionCoordinator
+ _OBJC_CLASS_$_AVCaptureDeviceDirectionMap
+ _OBJC_CLASS_$_AVCaptureDeviceStateCoordinatorUtilities
+ _OBJC_METACLASS_$_AVCaptureDeviceDescriptor
+ _OBJC_METACLASS_$_AVCaptureDeviceDirectionCoordinator
+ _OBJC_METACLASS_$_AVCaptureDeviceDirectionMap
+ __OBJC_$_CLASS_METHODS_AVCaptureDeviceDescriptor
+ __OBJC_$_CLASS_METHODS_AVCaptureDeviceDirectionCoordinator
+ __OBJC_$_CLASS_METHODS_AVCaptureDeviceDirectionMap
+ __OBJC_$_INSTANCE_METHODS_AVCaptureDeviceDescriptor
+ __OBJC_$_INSTANCE_METHODS_AVCaptureDeviceDirectionCoordinator
+ __OBJC_$_INSTANCE_METHODS_AVCaptureDeviceDirectionMap
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureDeviceDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureDeviceDirectionCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureDeviceDirectionMap
+ __OBJC_$_PROP_LIST_AVCaptureDeviceDescriptor
+ __OBJC_$_PROP_LIST_AVCaptureDeviceDirectionCoordinator
+ __OBJC_$_PROP_LIST_AVCaptureDeviceDirectionMap
+ __OBJC_CLASS_RO_$_AVCaptureDeviceDescriptor
+ __OBJC_CLASS_RO_$_AVCaptureDeviceDirectionCoordinator
+ __OBJC_CLASS_RO_$_AVCaptureDeviceDirectionMap
+ __OBJC_METACLASS_RO_$_AVCaptureDeviceDescriptor
+ __OBJC_METACLASS_RO_$_AVCaptureDeviceDirectionCoordinator
+ __OBJC_METACLASS_RO_$_AVCaptureDeviceDirectionMap
+ __OBJC_PROTOCOL_REFERENCE_$_AVMenuButtonDelegate
+ ___54+[AVCaptureDeviceDirectionCoordinator _isLegacyDevice]_block_invoke
+ ___78-[AVCaptureDeviceDirectionCoordinator initWithView:deviceTypes:changeHandler:]_block_invoke
+ ___78-[AVCaptureDeviceDirectionCoordinator initWithView:deviceTypes:changeHandler:]_block_invoke_2
+ __swift_closure_destructor.111Tm
+ __swift_closure_destructor.57Tm
+ __swift_closure_destructor.6Tm
+ _isLegacyDevice.isLegacyDevice
+ _isLegacyDevice.onceToken
+ _objc_msgSend$_buildDefaultMapWithUtilities:
+ _objc_msgSend$_initWithForwardFacingDeviceDescriptors:backwardFacingDeviceDescriptors:
+ _objc_msgSend$_initWithStateDescriptor:
+ _objc_msgSend$_isLegacyDevice
+ _objc_msgSend$_updateCurrentMap
+ _objc_msgSend$avkit_defaultCompactStatusBarRightInset:isEffectivelyFullScreen:
+ _objc_msgSend$avkit_horizontalEdgeInsetsForBarOnEdge:extent:reservedRightInset:
+ _objc_msgSend$avkit_reservedRightInsetForBarWithExtent:controlsViewLayoutPlane:isEffectivelyFullScreen:
+ _objc_msgSend$backwardFacingDeviceDescriptors
+ _objc_msgSend$contentTabsAdditionalRightInset
+ _objc_msgSend$controlsViewControllerWillEvaluateContentTabPresentationInfo:
+ _objc_msgSend$descriptorWithStateDescriptor:
+ _objc_msgSend$effectiveAutoHideInterval
+ _objc_msgSend$forwardFacingDeviceDescriptors
+ _objc_msgSend$initWithTypes:
+ _objc_msgSend$isFitnessApp
+ _objc_msgSend$localizedName
+ _objc_msgSend$mapWithForwardFacingDeviceDescriptors:backwardFacingDeviceDescriptors:
+ _objc_msgSend$mediaTypes
+ _objc_msgSend$setAccessibilityElementsHidden:
+ _objc_msgSend$setEffectivelyFullScreen:
+ _objc_msgSend$setRightBarInsetReservedByOwner:
+ _objc_msgSend$stateAForPosition:deviceAngle:
+ _objc_msgSend$stateBForPosition:deviceAngle:
- -[AVMobileGlassControlsViewController _prefersVolumeSliderIncluded]
- GCC_except_table1099
- GCC_except_table1126
- GCC_except_table1139
- GCC_except_table1205
- GCC_except_table1212
- GCC_except_table1220
- GCC_except_table1231
- GCC_except_table1244
- GCC_except_table1248
- GCC_except_table1249
- GCC_except_table1279
- GCC_except_table1280
- GCC_except_table1290
- GCC_except_table1300
- GCC_except_table1304
- GCC_except_table1318
- GCC_except_table1323
- GCC_except_table1362
- GCC_except_table1369
- GCC_except_table1371
- GCC_except_table1376
- GCC_except_table1427
- GCC_except_table1433
- GCC_except_table1438
- GCC_except_table1442
- GCC_except_table1443
- GCC_except_table1457
- GCC_except_table1755
- GCC_except_table1758
- GCC_except_table1794
- GCC_except_table1844
- GCC_except_table1923
- GCC_except_table1924
- GCC_except_table1932
- GCC_except_table1975
- GCC_except_table1980
- GCC_except_table1995
- GCC_except_table2063
- GCC_except_table2185
- GCC_except_table2377
- GCC_except_table2387
- GCC_except_table2418
- GCC_except_table2419
- GCC_except_table2515
- GCC_except_table2538
- GCC_except_table2770
- GCC_except_table2918
- GCC_except_table3094
- GCC_except_table3116
- GCC_except_table3293
- GCC_except_table3296
- GCC_except_table3301
- GCC_except_table3303
- GCC_except_table3330
- GCC_except_table3336
- GCC_except_table3340
- GCC_except_table3341
- GCC_except_table3342
- GCC_except_table3347
- GCC_except_table3370
- GCC_except_table3383
- GCC_except_table3420
- GCC_except_table3429
- GCC_except_table3434
- GCC_except_table3468
- GCC_except_table3480
- GCC_except_table3508
- GCC_except_table3514
- GCC_except_table3528
- GCC_except_table3591
- GCC_except_table3617
- GCC_except_table3626
- GCC_except_table3660
- GCC_except_table3661
- GCC_except_table3687
- GCC_except_table3744
- GCC_except_table3820
- GCC_except_table3821
- GCC_except_table3906
- GCC_except_table3967
- GCC_except_table4000
- GCC_except_table4075
- GCC_except_table4095
- GCC_except_table4286
- GCC_except_table4399
- GCC_except_table4560
- GCC_except_table4961
- GCC_except_table4967
- GCC_except_table4971
- GCC_except_table4975
- GCC_except_table5008
- GCC_except_table5017
- GCC_except_table5019
- GCC_except_table5077
- GCC_except_table5129
- GCC_except_table5407
- GCC_except_table5408
- GCC_except_table5409
- GCC_except_table5419
- GCC_except_table5580
- GCC_except_table5611
- GCC_except_table5614
- GCC_except_table5620
- GCC_except_table5625
- GCC_except_table5665
- GCC_except_table570
- GCC_except_table5748
- GCC_except_table5937
- GCC_except_table5946
- GCC_except_table5962
- GCC_except_table5982
- GCC_except_table5993
- GCC_except_table6037
- GCC_except_table606
- GCC_except_table6086
- GCC_except_table6102
- GCC_except_table622
- GCC_except_table6240
- GCC_except_table6260
- GCC_except_table6326
- GCC_except_table6437
- GCC_except_table6444
- GCC_except_table6555
- GCC_except_table6576
- GCC_except_table6578
- GCC_except_table6686
- GCC_except_table6715
- GCC_except_table6716
- GCC_except_table6750
- GCC_except_table6752
- GCC_except_table682
- GCC_except_table6872
- GCC_except_table6976
- GCC_except_table7055
- GCC_except_table7059
- GCC_except_table7071
- GCC_except_table7174
- GCC_except_table7177
- GCC_except_table7180
- GCC_except_table7182
- GCC_except_table7315
- GCC_except_table7384
- GCC_except_table7414
- GCC_except_table7415
- GCC_except_table7416
- GCC_except_table7417
- GCC_except_table7421
- GCC_except_table7438
- GCC_except_table7460
- GCC_except_table7479
- GCC_except_table749
- GCC_except_table7554
- GCC_except_table7686
- GCC_except_table7688
- GCC_except_table7702
- GCC_except_table7937
- GCC_except_table7943
- GCC_except_table8082
- GCC_except_table8104
- GCC_except_table8232
- GCC_except_table8239
- GCC_except_table8253
- GCC_except_table8437
- GCC_except_table8453
- GCC_except_table8454
- GCC_except_table8458
- GCC_except_table8466
- GCC_except_table8502
- GCC_except_table8524
- GCC_except_table8578
- GCC_except_table879
- GCC_except_table903
- GCC_except_table998
- __swift_closure_destructor.107Tm
- __swift_closure_destructor.53Tm
- _objc_msgSend$defaultStatusBarHeightInOrientation:
CStrings:
+ "%s Initialized AVCaptureDeviceDirectionCoordinator for UIView: %@"
+ "%s Legacy device, published default map: %@."
+ "%s reserve: %f (statusBarCompact: %d, statusBarOrientationDefault: %d, layoutPlane: %ld, effectivelyFullScreen: %d)"
+ "-[AVCaptureDeviceDirectionCoordinator _updateCurrentMap]"
+ "-[AVCaptureDeviceDirectionCoordinator initWithView:deviceTypes:changeHandler:]"
+ "-[AVMobileGlassControlsView _rightInsetReserveForTopControls]"
+ "Error: setAllowInfoMetadataSubpanel is only available on the TV app, the Artemis app and the Fitness app."
+ "HWModelStr"
+ "Non-Legacy Device Detected. Returning self."
+ "V68"
+ "com.apple.avkit.direction-coordinator"
+ "deviceType: %@, mediaTypes: %@, position: %ld, uniqueID: %@, localizedName: %@"
+ "forwardFacingDeviceDescriptors: %@, backwardFacingDeviceDescriptors: %@"
+ "\xf0\xf0\xf0\xf0\xf0\xf01"
+ "\xfb"
- "Error: setAllowInfoMetadataSubpanel is only available on the TV app and the Artemis app."
- "\xeb"
- "\xf0A"
- "\xf0\xf0\xf0\xf0\xf0\xf0!"
```
