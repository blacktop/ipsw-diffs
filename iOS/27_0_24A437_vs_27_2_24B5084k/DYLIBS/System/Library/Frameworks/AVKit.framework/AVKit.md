## AVKit

> `/System/Library/Frameworks/AVKit.framework/AVKit`

```diff

-1360.75.1.3.0
-  __TEXT.__text: 0x254c10
-  __TEXT.__objc_methlist: 0x1ee14
-  __TEXT.__const: 0x8438
-  __TEXT.__constg_swiftt: 0x2cbc
-  __TEXT.__swift5_typeref: 0x8312
-  __TEXT.__swift5_builtin: 0x1b8
+1385.6.1.11.1
+  __TEXT.__text: 0x256e64
+  __TEXT.__objc_methlist: 0x1f05c
+  __TEXT.__const: 0x84b8
+  __TEXT.__constg_swiftt: 0x2cdc
+  __TEXT.__swift5_typeref: 0x831c
+  __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift5_reflstr: 0x2016
   __TEXT.__swift5_fieldmd: 0x1e58
-  __TEXT.__swift5_assocty: 0x858
-  __TEXT.__swift5_capture: 0x18d8
-  __TEXT.__cstring: 0x13322
-  __TEXT.__swift5_proto: 0x2cc
-  __TEXT.__swift5_types: 0x24c
+  __TEXT.__swift5_assocty: 0x870
+  __TEXT.__swift5_capture: 0x192c
+  __TEXT.__cstring: 0x13314
+  __TEXT.__swift5_proto: 0x2d4
+  __TEXT.__swift5_types: 0x250
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift_as_entry: 0x2e8
   __TEXT.__swift_as_ret: 0x444
   __TEXT.__swift_as_cont: 0x86c
-  __TEXT.__oslogstring: 0xc15b
+  __TEXT.__oslogstring: 0xc276
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__gcc_except_tab: 0x426c
+  __TEXT.__gcc_except_tab: 0x4284
   __TEXT.__dlopen_cstrs: 0x1ef
   __TEXT.__ustring: 0x10c
-  __TEXT.__unwind_info: 0xca88
-  __TEXT.__eh_frame: 0x7a5c
+  __TEXT.__unwind_info: 0xcad8
+  __TEXT.__eh_frame: 0x7a34
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x33b0
-  __DATA_CONST.__objc_classlist: 0xaf8
+  __DATA_CONST.__objc_classlist: 0xb10
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x4e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd488
+  __DATA_CONST.__objc_selrefs: 0xd550
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x808
+  __DATA_CONST.__objc_superrefs: 0x820
   __DATA_CONST.__objc_arraydata: 0x6c0
-  __DATA_CONST.__got: 0x18a8
-  __AUTH_CONST.__const: 0x88f8
-  __AUTH_CONST.__cfstring: 0x9a00
-  __AUTH_CONST.__objc_const: 0x38578
+  __DATA_CONST.__got: 0x18c8
+  __AUTH_CONST.__const: 0x8a78
+  __AUTH_CONST.__cfstring: 0x99c0
+  __AUTH_CONST.__objc_const: 0x38b08
   __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_doubleobj: 0x280
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x1fa8
-  __AUTH.__objc_data: 0x68d8
+  __AUTH_CONST.__auth_got: 0x1fb8
+  __AUTH.__objc_data: 0x69c8
   __AUTH.__data: 0x2148
-  __DATA.__objc_ivar: 0x3054
-  __DATA.__data: 0x5cb8
+  __DATA.__objc_ivar: 0x30b0
+  __DATA.__data: 0x5ca8
   __DATA.__common: 0x1c8
   __DATA_DIRTY.__objc_data: 0x12e0
   __DATA_DIRTY.__data: 0x50

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14871
-  Symbols:   25715
-  CStrings:  3004
+  Functions: 14942
+  Symbols:   25838
+  CStrings:  3008
 
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
+ -[AVMediaPlaybackControls sizeThatFits:]
+ -[AVMobileChromelessPlaybackControlsView sizeThatFits:]
+ -[AVMobileGlassControlsStyleSheet contentTabSelectionAdditionalRightInset]
+ -[AVMobileGlassControlsView isEffectivelyFullScreen]
+ -[AVMobileGlassControlsView setEffectivelyFullScreen:]
+ -[AVMobileGlassControlsViewController _updateControlsViewArrangedAndWide]
+ -[AVMobileGlassControlsViewController effectiveAutoHideInterval]
+ -[AVMobileGlassControlsViewController isEffectivelyFullScreen]
+ -[AVMobileGlassControlsViewController setEffectivelyFullScreen:]
+ -[AVMobileGlassDisplayModeControlsView isEffectivelyFullScreen]
+ -[AVMobileGlassDisplayModeControlsView setEffectivelyFullScreen:]
+ -[AVMobileGlassPlaybackControlsView _paddingForAvailableSpace:]
+ -[AVMobileGlassVolumeControlsView isEffectivelyFullScreen]
+ -[AVMobileGlassVolumeControlsView setEffectivelyFullScreen:]
+ -[AVPlayerViewControllerContentView _updateControlsViewControllerArrangementLayoutPlaneIfNeeded]
+ -[AVPlayerViewControllerContentView _updateControlsViewControllerEffectivelyFullScreenIfNeeded]
+ -[UIView(AVAdditions) avkit_defaultCompactStatusBarRightInset:isEffectivelyFullScreen:]
+ -[UIWindow(AVAdditions_Internal_Mobile) avkit_isInsetFromScreenRightEdge]
+ -[UIWindowScene(AVAdditions) avkit_coversScreen]
+ GCC_except_table10033
+ GCC_except_table10169
+ GCC_except_table10171
+ GCC_except_table10185
+ GCC_except_table10219
+ GCC_except_table10229
+ GCC_except_table10385
+ GCC_except_table10426
+ GCC_except_table10448
+ GCC_except_table10666
+ GCC_except_table10688
+ GCC_except_table1112
+ GCC_except_table1117
+ GCC_except_table1126
+ GCC_except_table1220
+ GCC_except_table1320
+ GCC_except_table1323
+ GCC_except_table1326
+ GCC_except_table1328
+ GCC_except_table1441
+ GCC_except_table1451
+ GCC_except_table1477
+ GCC_except_table1498
+ GCC_except_table1512
+ GCC_except_table1739
+ GCC_except_table1740
+ GCC_except_table1748
+ GCC_except_table1780
+ GCC_except_table1785
+ GCC_except_table1800
+ GCC_except_table1825
+ GCC_except_table1835
+ GCC_except_table1838
+ GCC_except_table1839
+ GCC_except_table1879
+ GCC_except_table1880
+ GCC_except_table1881
+ GCC_except_table1885
+ GCC_except_table1902
+ GCC_except_table1932
+ GCC_except_table1937
+ GCC_except_table1940
+ GCC_except_table2059
+ GCC_except_table2169
+ GCC_except_table2242
+ GCC_except_table2297
+ GCC_except_table2365
+ GCC_except_table2406
+ GCC_except_table2519
+ GCC_except_table2542
+ GCC_except_table2719
+ GCC_except_table2795
+ GCC_except_table2824
+ GCC_except_table3024
+ GCC_except_table3249
+ GCC_except_table3258
+ GCC_except_table3273
+ GCC_except_table3290
+ GCC_except_table3292
+ GCC_except_table3303
+ GCC_except_table3347
+ GCC_except_table3396
+ GCC_except_table3412
+ GCC_except_table3637
+ GCC_except_table3645
+ GCC_except_table3647
+ GCC_except_table3651
+ GCC_except_table3676
+ GCC_except_table3691
+ GCC_except_table3704
+ GCC_except_table3749
+ GCC_except_table3758
+ GCC_except_table3763
+ GCC_except_table3794
+ GCC_except_table3806
+ GCC_except_table3834
+ GCC_except_table3840
+ GCC_except_table3861
+ GCC_except_table3863
+ GCC_except_table3935
+ GCC_except_table3960
+ GCC_except_table3969
+ GCC_except_table4001
+ GCC_except_table4002
+ GCC_except_table4027
+ GCC_except_table4085
+ GCC_except_table4161
+ GCC_except_table4162
+ GCC_except_table4247
+ GCC_except_table4287
+ GCC_except_table4320
+ GCC_except_table4375
+ GCC_except_table4393
+ GCC_except_table4411
+ GCC_except_table4421
+ GCC_except_table4434
+ GCC_except_table4438
+ GCC_except_table4439
+ GCC_except_table4468
+ GCC_except_table4469
+ GCC_except_table4470
+ GCC_except_table4483
+ GCC_except_table4485
+ GCC_except_table4495
+ GCC_except_table4499
+ GCC_except_table4501
+ GCC_except_table4512
+ GCC_except_table4516
+ GCC_except_table4518
+ GCC_except_table4521
+ GCC_except_table4523
+ GCC_except_table4569
+ GCC_except_table4571
+ GCC_except_table459
+ GCC_except_table462
+ GCC_except_table4631
+ GCC_except_table4642
+ GCC_except_table4645
+ GCC_except_table4646
+ GCC_except_table4647
+ GCC_except_table4660
+ GCC_except_table4663
+ GCC_except_table4735
+ GCC_except_table4740
+ GCC_except_table4861
+ GCC_except_table4932
+ GCC_except_table498
+ GCC_except_table5093
+ GCC_except_table5103
+ GCC_except_table5108
+ GCC_except_table5178
+ GCC_except_table525
+ GCC_except_table5282
+ GCC_except_table5289
+ GCC_except_table5291
+ GCC_except_table5317
+ GCC_except_table5433
+ GCC_except_table5571
+ GCC_except_table5578
+ GCC_except_table5581
+ GCC_except_table5612
+ GCC_except_table5613
+ GCC_except_table5712
+ GCC_except_table585
+ GCC_except_table589
+ GCC_except_table601
+ GCC_except_table6205
+ GCC_except_table6238
+ GCC_except_table6241
+ GCC_except_table6242
+ GCC_except_table6247
+ GCC_except_table6269
+ GCC_except_table6363
+ GCC_except_table6459
+ GCC_except_table6499
+ GCC_except_table6501
+ GCC_except_table6535
+ GCC_except_table6536
+ GCC_except_table6570
+ GCC_except_table6572
+ GCC_except_table6622
+ GCC_except_table6682
+ GCC_except_table6707
+ GCC_except_table6714
+ GCC_except_table6725
+ GCC_except_table6730
+ GCC_except_table6733
+ GCC_except_table697
+ GCC_except_table703
+ GCC_except_table7063
+ GCC_except_table7069
+ GCC_except_table7073
+ GCC_except_table7077
+ GCC_except_table7089
+ GCC_except_table7109
+ GCC_except_table7120
+ GCC_except_table7131
+ GCC_except_table7176
+ GCC_except_table7228
+ GCC_except_table7259
+ GCC_except_table7566
+ GCC_except_table7621
+ GCC_except_table768
+ GCC_except_table775
+ GCC_except_table7772
+ GCC_except_table7779
+ GCC_except_table7836
+ GCC_except_table7853
+ GCC_except_table7871
+ GCC_except_table7882
+ GCC_except_table7888
+ GCC_except_table789
+ GCC_except_table7898
+ GCC_except_table7947
+ GCC_except_table7951
+ GCC_except_table7953
+ GCC_except_table7960
+ GCC_except_table7966
+ GCC_except_table7998
+ GCC_except_table8014
+ GCC_except_table8037
+ GCC_except_table8062
+ GCC_except_table8069
+ GCC_except_table807
+ GCC_except_table8074
+ GCC_except_table8077
+ GCC_except_table8078
+ GCC_except_table8090
+ GCC_except_table8093
+ GCC_except_table8151
+ GCC_except_table8219
+ GCC_except_table8245
+ GCC_except_table830
+ GCC_except_table8334
+ GCC_except_table8353
+ GCC_except_table8392
+ GCC_except_table8422
+ GCC_except_table8426
+ GCC_except_table8581
+ GCC_except_table8639
+ GCC_except_table8641
+ GCC_except_table8825
+ GCC_except_table8838
+ GCC_except_table8859
+ GCC_except_table8882
+ GCC_except_table8892
+ GCC_except_table8910
+ GCC_except_table8911
+ GCC_except_table8915
+ GCC_except_table8923
+ GCC_except_table8979
+ GCC_except_table9275
+ GCC_except_table9293
+ GCC_except_table9446
+ GCC_except_table9450
+ GCC_except_table9452
+ GCC_except_table9454
+ GCC_except_table9455
+ GCC_except_table9456
+ GCC_except_table9487
+ GCC_except_table9495
+ GCC_except_table9525
+ GCC_except_table954
+ GCC_except_table9551
+ GCC_except_table9569
+ GCC_except_table9573
+ GCC_except_table9577
+ GCC_except_table9579
+ GCC_except_table9651
+ GCC_except_table9674
+ GCC_except_table9702
+ GCC_except_table9714
+ GCC_except_table972
+ GCC_except_table9735
+ GCC_except_table9837
+ _MGCopyAnswer
+ _OBJC_CLASS_$_AVCaptureDeviceDescriptor
+ _OBJC_CLASS_$_AVCaptureDeviceDirectionCoordinator
+ _OBJC_CLASS_$_AVCaptureDeviceDirectionMap
+ _OBJC_CLASS_$_AVCaptureDeviceStateCoordinatorUtilities
+ _OBJC_IVAR_$_AVCaptureDeviceDescriptor._deviceType
+ _OBJC_IVAR_$_AVCaptureDeviceDescriptor._localizedName
+ _OBJC_IVAR_$_AVCaptureDeviceDescriptor._mediaTypes
+ _OBJC_IVAR_$_AVCaptureDeviceDescriptor._position
+ _OBJC_IVAR_$_AVCaptureDeviceDescriptor._uniqueID
+ _OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._changeHandler
+ _OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._currentMap
+ _OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._defaultMap
+ _OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._deviceTypes
+ _OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._hasPublishedInitialMap
+ _OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._lock
+ _OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._stateCoordinatorUtilities
+ _OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._utilitiesQueue
+ _OBJC_IVAR_$_AVCaptureDeviceDirectionCoordinator._view
+ _OBJC_IVAR_$_AVCaptureDeviceDirectionMap._backwardFacingDeviceDescriptors
+ _OBJC_IVAR_$_AVCaptureDeviceDirectionMap._forwardFacingDeviceDescriptors
+ _OBJC_IVAR_$_AVMobileGlassControlsStyleSheet._compactStatusBarHorizontalMargin
+ _OBJC_IVAR_$_AVMobileGlassControlsStyleSheet._contentTabSelectionAdditionalRightInset
+ _OBJC_IVAR_$_AVMobileGlassControlsView._effectivelyFullScreen
+ _OBJC_IVAR_$_AVMobileGlassControlsViewController._controlsViewArrangedAndWide
+ _OBJC_IVAR_$_AVMobileGlassControlsViewController._effectivelyFullScreen
+ _OBJC_IVAR_$_AVMobileGlassDisplayModeControlsView._effectivelyFullScreen
+ _OBJC_IVAR_$_AVMobileGlassVolumeControlsView._effectivelyFullScreen
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
+ ___54+[AVCaptureDeviceDirectionCoordinator _isLegacyDevice]_block_invoke
+ ___78-[AVCaptureDeviceDirectionCoordinator initWithView:deviceTypes:changeHandler:]_block_invoke
+ ___78-[AVCaptureDeviceDirectionCoordinator initWithView:deviceTypes:changeHandler:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ __isLegacyDevice.isLegacyDevice
+ __isLegacyDevice.onceToken
+ _objc_msgSend$_animateUsingSpringWithDuration:delay:options:mass:stiffness:damping:initialVelocity:animations:completion:
+ _objc_msgSend$_buildDefaultMapWithUtilities:
+ _objc_msgSend$_initWithForwardFacingDeviceDescriptors:backwardFacingDeviceDescriptors:
+ _objc_msgSend$_initWithStateDescriptor:
+ _objc_msgSend$_isLegacyDevice
+ _objc_msgSend$_updateCurrentMap
+ _objc_msgSend$avkit_defaultCompactStatusBarRightInset:isEffectivelyFullScreen:
+ _objc_msgSend$backwardFacingDeviceDescriptors
+ _objc_msgSend$contentTabSelectionAdditionalRightInset
+ _objc_msgSend$descriptorWithStateDescriptor:
+ _objc_msgSend$effectiveAutoHideInterval
+ _objc_msgSend$forwardFacingDeviceDescriptors
+ _objc_msgSend$initWithTypes:
+ _objc_msgSend$mapWithForwardFacingDeviceDescriptors:backwardFacingDeviceDescriptors:
+ _objc_msgSend$mediaTypes
+ _objc_msgSend$saveMostRecentLegibleLanguageCode:
+ _objc_msgSend$setCaptionAppearanceAlwaysOnIfNeededFor:
+ _objc_msgSend$setEffectivelyFullScreen:
+ _objc_msgSend$stateAForPosition:deviceAngle:
+ _objc_msgSend$stateBForPosition:deviceAngle:
+ _objc_msgSend$transitionWithView:duration:options:animations:completion:
+ _swift_conformsToProtocol2
+ _symbolic Ig_
+ _symbolic _____ So22AVMediaSelectionReasonV
- +[AVPlayerController keyPathsForValuesAffectingHasEnhancedDialogueEligibleAudio]
- GCC_except_table10122
- GCC_except_table10124
- GCC_except_table10138
- GCC_except_table10172
- GCC_except_table10182
- GCC_except_table10332
- GCC_except_table10338
- GCC_except_table10401
- GCC_except_table10617
- GCC_except_table10639
- GCC_except_table1111
- GCC_except_table1116
- GCC_except_table1125
- GCC_except_table1219
- GCC_except_table1319
- GCC_except_table1322
- GCC_except_table1325
- GCC_except_table1327
- GCC_except_table1438
- GCC_except_table1450
- GCC_except_table1476
- GCC_except_table1497
- GCC_except_table1511
- GCC_except_table1737
- GCC_except_table1738
- GCC_except_table1746
- GCC_except_table1778
- GCC_except_table1783
- GCC_except_table1798
- GCC_except_table1823
- GCC_except_table1833
- GCC_except_table1836
- GCC_except_table1837
- GCC_except_table1876
- GCC_except_table1877
- GCC_except_table1878
- GCC_except_table1882
- GCC_except_table1899
- GCC_except_table1928
- GCC_except_table1933
- GCC_except_table1936
- GCC_except_table2055
- GCC_except_table2165
- GCC_except_table2238
- GCC_except_table2293
- GCC_except_table2361
- GCC_except_table2400
- GCC_except_table2513
- GCC_except_table2536
- GCC_except_table2713
- GCC_except_table2789
- GCC_except_table2818
- GCC_except_table3017
- GCC_except_table3242
- GCC_except_table3251
- GCC_except_table3266
- GCC_except_table3283
- GCC_except_table3285
- GCC_except_table3296
- GCC_except_table3340
- GCC_except_table3389
- GCC_except_table3405
- GCC_except_table3630
- GCC_except_table3633
- GCC_except_table3638
- GCC_except_table3644
- GCC_except_table3669
- GCC_except_table3684
- GCC_except_table3697
- GCC_except_table3742
- GCC_except_table3751
- GCC_except_table3756
- GCC_except_table3787
- GCC_except_table3799
- GCC_except_table3827
- GCC_except_table3833
- GCC_except_table3847
- GCC_except_table3856
- GCC_except_table3928
- GCC_except_table3953
- GCC_except_table3962
- GCC_except_table3994
- GCC_except_table3995
- GCC_except_table4020
- GCC_except_table4078
- GCC_except_table4154
- GCC_except_table4155
- GCC_except_table4240
- GCC_except_table4280
- GCC_except_table4313
- GCC_except_table4367
- GCC_except_table4385
- GCC_except_table4395
- GCC_except_table4413
- GCC_except_table4426
- GCC_except_table4430
- GCC_except_table4431
- GCC_except_table4460
- GCC_except_table4461
- GCC_except_table4462
- GCC_except_table4475
- GCC_except_table4477
- GCC_except_table4487
- GCC_except_table4491
- GCC_except_table4493
- GCC_except_table4504
- GCC_except_table4508
- GCC_except_table4510
- GCC_except_table4513
- GCC_except_table4515
- GCC_except_table4552
- GCC_except_table4562
- GCC_except_table458
- GCC_except_table461
- GCC_except_table4622
- GCC_except_table4628
- GCC_except_table4633
- GCC_except_table4636
- GCC_except_table4638
- GCC_except_table4651
- GCC_except_table4654
- GCC_except_table4724
- GCC_except_table4729
- GCC_except_table4850
- GCC_except_table4921
- GCC_except_table497
- GCC_except_table5082
- GCC_except_table5092
- GCC_except_table5097
- GCC_except_table5167
- GCC_except_table524
- GCC_except_table5270
- GCC_except_table5277
- GCC_except_table5279
- GCC_except_table5305
- GCC_except_table5421
- GCC_except_table5559
- GCC_except_table5566
- GCC_except_table5569
- GCC_except_table5600
- GCC_except_table5601
- GCC_except_table5700
- GCC_except_table584
- GCC_except_table588
- GCC_except_table600
- GCC_except_table6193
- GCC_except_table6226
- GCC_except_table6229
- GCC_except_table6230
- GCC_except_table6235
- GCC_except_table6257
- GCC_except_table6351
- GCC_except_table6447
- GCC_except_table6487
- GCC_except_table6489
- GCC_except_table6523
- GCC_except_table6524
- GCC_except_table6558
- GCC_except_table6560
- GCC_except_table6609
- GCC_except_table6669
- GCC_except_table6694
- GCC_except_table6701
- GCC_except_table6704
- GCC_except_table6712
- GCC_except_table6720
- GCC_except_table695
- GCC_except_table702
- GCC_except_table7050
- GCC_except_table7056
- GCC_except_table7060
- GCC_except_table7064
- GCC_except_table7076
- GCC_except_table7096
- GCC_except_table7105
- GCC_except_table7107
- GCC_except_table7163
- GCC_except_table7215
- GCC_except_table7246
- GCC_except_table7552
- GCC_except_table7607
- GCC_except_table767
- GCC_except_table774
- GCC_except_table7758
- GCC_except_table7765
- GCC_except_table7822
- GCC_except_table7839
- GCC_except_table7857
- GCC_except_table7868
- GCC_except_table7874
- GCC_except_table788
- GCC_except_table7884
- GCC_except_table7933
- GCC_except_table7937
- GCC_except_table7939
- GCC_except_table7946
- GCC_except_table7952
- GCC_except_table7984
- GCC_except_table8000
- GCC_except_table8023
- GCC_except_table8048
- GCC_except_table8055
- GCC_except_table806
- GCC_except_table8060
- GCC_except_table8063
- GCC_except_table8064
- GCC_except_table8065
- GCC_except_table8076
- GCC_except_table8137
- GCC_except_table8204
- GCC_except_table8229
- GCC_except_table829
- GCC_except_table8318
- GCC_except_table8337
- GCC_except_table8376
- GCC_except_table8406
- GCC_except_table8410
- GCC_except_table8565
- GCC_except_table8623
- GCC_except_table8625
- GCC_except_table8809
- GCC_except_table8822
- GCC_except_table8843
- GCC_except_table8866
- GCC_except_table8876
- GCC_except_table8894
- GCC_except_table8895
- GCC_except_table8899
- GCC_except_table8907
- GCC_except_table8963
- GCC_except_table9259
- GCC_except_table9277
- GCC_except_table9430
- GCC_except_table9434
- GCC_except_table9436
- GCC_except_table9438
- GCC_except_table9439
- GCC_except_table9440
- GCC_except_table9471
- GCC_except_table9479
- GCC_except_table9509
- GCC_except_table953
- GCC_except_table9535
- GCC_except_table9553
- GCC_except_table9557
- GCC_except_table9561
- GCC_except_table9563
- GCC_except_table9635
- GCC_except_table9658
- GCC_except_table9686
- GCC_except_table9698
- GCC_except_table9703
- GCC_except_table971
- GCC_except_table9822
- GCC_except_table9987
- ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
- ___swift_closure_destructor.129Tm
CStrings:
+ "%s Initialized AVCaptureDeviceDirectionCoordinator for UIView: %@"
+ "%s Legacy device, published default map: %@."
+ "-[AVCaptureDeviceDirectionCoordinator _updateCurrentMap]"
+ "-[AVCaptureDeviceDirectionCoordinator initWithView:deviceTypes:changeHandler:]"
+ "AVMediaOptionsController: cannot store most recent selected legible - no extendedLanguageTag for selected MediaOptionSource"
+ "HWModelStr"
+ "Non-Legacy Device Detected. Returning self."
+ "V68"
+ "activePlayer.rate"
+ "com.apple.avkit.direction-coordinator"
+ "deviceType: %@, mediaTypes: %@, position: %ld, uniqueID: %@, localizedName: %@"
+ "forwardFacingDeviceDescriptors: %@, backwardFacingDeviceDescriptors: %@"
+ "\xf0\xf0\xf0\xf0\xf0\xf0a"
- "activePlayer"
- "interstitialController.interstitialPlayer.currentItem.hasEnabledAudio"
- "interstitialController.interstitialPlayer.currentItem.hasEnabledVideo"
- "interstitialController.interstitialPlayer.currentItem.isEligibleForDSPBasedEnhancedDialogue"
- "interstitialController.interstitialPlayer.rate"
- "player.currentItem.isEligibleForDSPBasedEnhancedDialogue"
- "player.reasonForWaitingToPlay"
- "\xeb"
- "\xf0\xf0\xf0\xf0\xf0\xf0Q"
```
