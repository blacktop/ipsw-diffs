## AVKit

> `/System/Library/Frameworks/AVKit.framework/AVKit`

```diff

-1385.7.1.0.0
-  __TEXT.__text: 0x255d24
-  __TEXT.__objc_methlist: 0x1eedc
+1385.12.1.0.0
+  __TEXT.__text: 0x258138
+  __TEXT.__objc_methlist: 0x1f0c4
   __TEXT.__const: 0x84b8
   __TEXT.__constg_swiftt: 0x2cdc
   __TEXT.__swift5_typeref: 0x831c

   __TEXT.__swift5_fieldmd: 0x1e58
   __TEXT.__swift5_assocty: 0x870
   __TEXT.__swift5_capture: 0x192c
-  __TEXT.__cstring: 0x131b9
+  __TEXT.__cstring: 0x133c2
   __TEXT.__swift5_proto: 0x2d4
   __TEXT.__swift5_types: 0x250
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift_as_entry: 0x2e8
   __TEXT.__swift_as_ret: 0x444
   __TEXT.__swift_as_cont: 0x86c
-  __TEXT.__oslogstring: 0xc1db
+  __TEXT.__oslogstring: 0xc32a
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__gcc_except_tab: 0x4284
-  __TEXT.__dlopen_cstrs: 0x1ef
+  __TEXT.__gcc_except_tab: 0x43c4
+  __TEXT.__dlopen_cstrs: 0x289
   __TEXT.__ustring: 0x10c
-  __TEXT.__unwind_info: 0xcaa0
+  __TEXT.__unwind_info: 0xcb18
   __TEXT.__eh_frame: 0x7a34
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x33b0
-  __DATA_CONST.__objc_classlist: 0xaf8
+  __DATA_CONST.__const: 0x33e0
+  __DATA_CONST.__objc_classlist: 0xb10
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x4e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd4d8
-  __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x808
+  __DATA_CONST.__objc_selrefs: 0xd598
+  __DATA_CONST.__objc_protorefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x820
   __DATA_CONST.__objc_arraydata: 0x6c0
-  __DATA_CONST.__got: 0x18a8
-  __AUTH_CONST.__const: 0x8a58
-  __AUTH_CONST.__cfstring: 0x9940
-  __AUTH_CONST.__objc_const: 0x38688
+  __DATA_CONST.__got: 0x18d0
+  __AUTH_CONST.__const: 0x8a78
+  __AUTH_CONST.__cfstring: 0x99e0
+  __AUTH_CONST.__objc_const: 0x38b90
   __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_doubleobj: 0x280
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x1fb0
-  __AUTH.__objc_data: 0x68d8
-  __AUTH.__data: 0x2148
-  __DATA.__objc_ivar: 0x306c
-  __DATA.__data: 0x5ca8
-  __DATA.__common: 0x1c8
-  __DATA_DIRTY.__objc_data: 0x12e0
-  __DATA_DIRTY.__data: 0x50
+  __AUTH_CONST.__auth_got: 0x1fb8
+  __AUTH.__objc_data: 0x60f8
+  __AUTH.__data: 0x20d0
+  __DATA.__objc_ivar: 0x30bc
+  __DATA.__data: 0x5ce8
+  __DATA.__common: 0x1d0
+  __DATA_DIRTY.__objc_data: 0x1bb0
+  __DATA_DIRTY.__data: 0xd0
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14913
-  Symbols:   20186
-  CStrings:  2999
+  Functions: 14958
+  Symbols:   20282
+  CStrings:  3015
 
Symbols:
+ +[AVCaptureDeviceDescriptor descriptorWithStateDescriptor:]
+ +[AVCaptureDeviceDirectionCoordinator _buildDefaultMapWithUtilities:]
+ +[AVCaptureDeviceDirectionCoordinator _isLegacyDevice]
+ +[AVCaptureDeviceDirectionMap mapWithForwardFacingDeviceDescriptors:backwardFacingDeviceDescriptors:]
+ +[AVKitGlobalSettings _determineEnablePlayerGeneration]
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
+ -[AVMenuButton _contextMenu]
+ -[AVMobileGlassDisplayModeControlsView rightBarInsetReservedByOwner]
+ -[AVMobileGlassDisplayModeControlsView setRightBarInsetReservedByOwner:]
+ -[AVMobileGlassVolumeControlsView rightBarInsetReservedByOwner]
+ -[AVMobileGlassVolumeControlsView setRightBarInsetReservedByOwner:]
+ -[AVPlayerViewController controlsViewControllerWillEvaluateContentTabPresentationInfo:]
+ -[AVRoutePickerView _updateRoutePickingControlsSourceView]
+ -[UIView(AVAdditions) avkit_horizontalEdgeInsetsForBarOnEdge:extent:reservedRightInset:]
+ -[UIView(AVAdditions) avkit_reservedRightInsetForBarWithExtent:controlsViewLayoutPlane:isEffectivelyFullScreen:]
+ GCC_except_table10047
+ GCC_except_table10183
+ GCC_except_table10185
+ GCC_except_table10199
+ GCC_except_table10233
+ GCC_except_table10243
+ GCC_except_table10393
+ GCC_except_table10399
+ GCC_except_table10440
+ GCC_except_table10462
+ GCC_except_table10682
+ GCC_except_table10704
+ GCC_except_table1116
+ GCC_except_table1121
+ GCC_except_table1130
+ GCC_except_table1224
+ GCC_except_table1324
+ GCC_except_table1327
+ GCC_except_table1330
+ GCC_except_table1332
+ GCC_except_table1443
+ GCC_except_table1444
+ GCC_except_table1445
+ GCC_except_table1455
+ GCC_except_table1481
+ GCC_except_table1502
+ GCC_except_table1516
+ GCC_except_table1743
+ GCC_except_table1744
+ GCC_except_table1752
+ GCC_except_table1781
+ GCC_except_table1788
+ GCC_except_table1793
+ GCC_except_table1808
+ GCC_except_table1833
+ GCC_except_table1843
+ GCC_except_table1846
+ GCC_except_table1847
+ GCC_except_table1887
+ GCC_except_table1888
+ GCC_except_table1889
+ GCC_except_table1893
+ GCC_except_table1910
+ GCC_except_table1945
+ GCC_except_table1948
+ GCC_except_table199
+ GCC_except_table2067
+ GCC_except_table2177
+ GCC_except_table2250
+ GCC_except_table2305
+ GCC_except_table2373
+ GCC_except_table2414
+ GCC_except_table2527
+ GCC_except_table2550
+ GCC_except_table2727
+ GCC_except_table2804
+ GCC_except_table2833
+ GCC_except_table3035
+ GCC_except_table3260
+ GCC_except_table3269
+ GCC_except_table3284
+ GCC_except_table3301
+ GCC_except_table3303
+ GCC_except_table3314
+ GCC_except_table3358
+ GCC_except_table3407
+ GCC_except_table3423
+ GCC_except_table3651
+ GCC_except_table3656
+ GCC_except_table3658
+ GCC_except_table3662
+ GCC_except_table3687
+ GCC_except_table3702
+ GCC_except_table3715
+ GCC_except_table3761
+ GCC_except_table3770
+ GCC_except_table3775
+ GCC_except_table3806
+ GCC_except_table3818
+ GCC_except_table3846
+ GCC_except_table3852
+ GCC_except_table3866
+ GCC_except_table3873
+ GCC_except_table3875
+ GCC_except_table3947
+ GCC_except_table3972
+ GCC_except_table3981
+ GCC_except_table4013
+ GCC_except_table4014
+ GCC_except_table4039
+ GCC_except_table4097
+ GCC_except_table4173
+ GCC_except_table4174
+ GCC_except_table4259
+ GCC_except_table4299
+ GCC_except_table4332
+ GCC_except_table4387
+ GCC_except_table4405
+ GCC_except_table4415
+ GCC_except_table4423
+ GCC_except_table4433
+ GCC_except_table4445
+ GCC_except_table4449
+ GCC_except_table4450
+ GCC_except_table4479
+ GCC_except_table4480
+ GCC_except_table4481
+ GCC_except_table4494
+ GCC_except_table4506
+ GCC_except_table4510
+ GCC_except_table4512
+ GCC_except_table4523
+ GCC_except_table4527
+ GCC_except_table4529
+ GCC_except_table4532
+ GCC_except_table4534
+ GCC_except_table4571
+ GCC_except_table4580
+ GCC_except_table4582
+ GCC_except_table4642
+ GCC_except_table465
+ GCC_except_table4653
+ GCC_except_table4656
+ GCC_except_table4657
+ GCC_except_table4658
+ GCC_except_table4671
+ GCC_except_table4674
+ GCC_except_table4746
+ GCC_except_table4751
+ GCC_except_table4872
+ GCC_except_table4943
+ GCC_except_table501
+ GCC_except_table5114
+ GCC_except_table5119
+ GCC_except_table5189
+ GCC_except_table528
+ GCC_except_table5293
+ GCC_except_table5300
+ GCC_except_table5302
+ GCC_except_table5328
+ GCC_except_table5444
+ GCC_except_table5589
+ GCC_except_table5592
+ GCC_except_table5623
+ GCC_except_table5624
+ GCC_except_table5723
+ GCC_except_table593
+ GCC_except_table605
+ GCC_except_table6216
+ GCC_except_table6249
+ GCC_except_table6252
+ GCC_except_table6253
+ GCC_except_table6258
+ GCC_except_table6280
+ GCC_except_table6374
+ GCC_except_table6470
+ GCC_except_table65
+ GCC_except_table6510
+ GCC_except_table6512
+ GCC_except_table6546
+ GCC_except_table6547
+ GCC_except_table6581
+ GCC_except_table6583
+ GCC_except_table6633
+ GCC_except_table6693
+ GCC_except_table6725
+ GCC_except_table6728
+ GCC_except_table6736
+ GCC_except_table6742
+ GCC_except_table6745
+ GCC_except_table700
+ GCC_except_table701
+ GCC_except_table707
+ GCC_except_table7075
+ GCC_except_table7081
+ GCC_except_table7085
+ GCC_except_table7089
+ GCC_except_table7101
+ GCC_except_table7130
+ GCC_except_table7143
+ GCC_except_table7188
+ GCC_except_table7240
+ GCC_except_table7271
+ GCC_except_table7578
+ GCC_except_table7633
+ GCC_except_table772
+ GCC_except_table7784
+ GCC_except_table779
+ GCC_except_table7791
+ GCC_except_table7848
+ GCC_except_table7865
+ GCC_except_table7894
+ GCC_except_table7900
+ GCC_except_table7910
+ GCC_except_table793
+ GCC_except_table7959
+ GCC_except_table7963
+ GCC_except_table7965
+ GCC_except_table7972
+ GCC_except_table7978
+ GCC_except_table8010
+ GCC_except_table8026
+ GCC_except_table8049
+ GCC_except_table8074
+ GCC_except_table8081
+ GCC_except_table8086
+ GCC_except_table8089
+ GCC_except_table8090
+ GCC_except_table8102
+ GCC_except_table8105
+ GCC_except_table811
+ GCC_except_table8163
+ GCC_except_table8232
+ GCC_except_table8259
+ GCC_except_table834
+ GCC_except_table8348
+ GCC_except_table8367
+ GCC_except_table8406
+ GCC_except_table8436
+ GCC_except_table8440
+ GCC_except_table8595
+ GCC_except_table86
+ GCC_except_table8653
+ GCC_except_table8655
+ GCC_except_table8852
+ GCC_except_table8873
+ GCC_except_table8896
+ GCC_except_table8906
+ GCC_except_table8925
+ GCC_except_table8929
+ GCC_except_table8937
+ GCC_except_table8993
+ GCC_except_table9289
+ GCC_except_table9307
+ GCC_except_table9460
+ GCC_except_table9464
+ GCC_except_table9466
+ GCC_except_table9468
+ GCC_except_table9469
+ GCC_except_table9470
+ GCC_except_table9501
+ GCC_except_table9509
+ GCC_except_table9539
+ GCC_except_table9565
+ GCC_except_table958
+ GCC_except_table9583
+ GCC_except_table9587
+ GCC_except_table9591
+ GCC_except_table9593
+ GCC_except_table9665
+ GCC_except_table9688
+ GCC_except_table9716
+ GCC_except_table9728
+ GCC_except_table9733
+ GCC_except_table9749
+ GCC_except_table976
+ GCC_except_table9851
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
+ _OBJC_IVAR_$_AVControlItem._menu
+ _OBJC_IVAR_$_AVMobileGlassControlsView._topControlsRightInsetReserve
+ _OBJC_IVAR_$_AVMobileGlassDisplayModeControlsView._rightBarInsetReservedByOwner
+ _OBJC_IVAR_$_AVMobileGlassVolumeControlsView._rightBarInsetReservedByOwner
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
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___getMPBaseAppEntityIdentifierClass_block_invoke
+ ___getMPNowPlayingInfoCenterClass_block_invoke
+ ___getMPNowPlayingInfoPropertyAppEntityIdentifiersSymbolLoc_block_invoke
+ __isLegacyDevice.isLegacyDevice
+ __isLegacyDevice.onceToken
+ _getMPBaseAppEntityIdentifierClass.softClass
+ _getMPNowPlayingInfoCenterClass.softClass
+ _getMPNowPlayingInfoPropertyAppEntityIdentifiersSymbolLoc.ptr
+ _kMRMediaRemoteNowPlayingInfoAppEntityPaths
- -[AVMobileGlassControlsViewController _prefersVolumeSliderIncluded]
- GCC_except_table10004
- GCC_except_table10140
- GCC_except_table10142
- GCC_except_table10156
- GCC_except_table10190
- GCC_except_table10200
- GCC_except_table10350
- GCC_except_table10356
- GCC_except_table10397
- GCC_except_table10419
- GCC_except_table10637
- GCC_except_table10659
- GCC_except_table1112
- GCC_except_table1117
- GCC_except_table1126
- GCC_except_table1220
- GCC_except_table1320
- GCC_except_table1323
- GCC_except_table1326
- GCC_except_table1328
- GCC_except_table1439
- GCC_except_table1440
- GCC_except_table1441
- GCC_except_table1451
- GCC_except_table1477
- GCC_except_table1498
- GCC_except_table1512
- GCC_except_table1739
- GCC_except_table1740
- GCC_except_table1748
- GCC_except_table1780
- GCC_except_table1785
- GCC_except_table1800
- GCC_except_table1825
- GCC_except_table1835
- GCC_except_table1838
- GCC_except_table1839
- GCC_except_table1879
- GCC_except_table1880
- GCC_except_table1881
- GCC_except_table1885
- GCC_except_table1902
- GCC_except_table1932
- GCC_except_table1937
- GCC_except_table196
- GCC_except_table2059
- GCC_except_table2169
- GCC_except_table2242
- GCC_except_table2297
- GCC_except_table2365
- GCC_except_table2406
- GCC_except_table2519
- GCC_except_table2542
- GCC_except_table2719
- GCC_except_table2796
- GCC_except_table2825
- GCC_except_table3025
- GCC_except_table3250
- GCC_except_table3259
- GCC_except_table3274
- GCC_except_table3291
- GCC_except_table3293
- GCC_except_table3304
- GCC_except_table3348
- GCC_except_table3397
- GCC_except_table3413
- GCC_except_table3638
- GCC_except_table3641
- GCC_except_table3646
- GCC_except_table3652
- GCC_except_table3677
- GCC_except_table3692
- GCC_except_table3705
- GCC_except_table3750
- GCC_except_table3759
- GCC_except_table3764
- GCC_except_table3795
- GCC_except_table3807
- GCC_except_table3835
- GCC_except_table3841
- GCC_except_table3855
- GCC_except_table3862
- GCC_except_table3864
- GCC_except_table3936
- GCC_except_table3961
- GCC_except_table3970
- GCC_except_table4002
- GCC_except_table4003
- GCC_except_table4028
- GCC_except_table4086
- GCC_except_table4162
- GCC_except_table4163
- GCC_except_table4248
- GCC_except_table4288
- GCC_except_table4321
- GCC_except_table4376
- GCC_except_table4394
- GCC_except_table4404
- GCC_except_table4412
- GCC_except_table4422
- GCC_except_table4435
- GCC_except_table4439
- GCC_except_table4440
- GCC_except_table4469
- GCC_except_table4470
- GCC_except_table4471
- GCC_except_table4484
- GCC_except_table4486
- GCC_except_table4500
- GCC_except_table4502
- GCC_except_table4513
- GCC_except_table4517
- GCC_except_table4519
- GCC_except_table4522
- GCC_except_table4524
- GCC_except_table4561
- GCC_except_table4570
- GCC_except_table4572
- GCC_except_table459
- GCC_except_table4632
- GCC_except_table4638
- GCC_except_table4643
- GCC_except_table4646
- GCC_except_table4647
- GCC_except_table4661
- GCC_except_table4664
- GCC_except_table4736
- GCC_except_table4741
- GCC_except_table4862
- GCC_except_table4933
- GCC_except_table498
- GCC_except_table5094
- GCC_except_table5109
- GCC_except_table5179
- GCC_except_table525
- GCC_except_table5283
- GCC_except_table5290
- GCC_except_table5292
- GCC_except_table5318
- GCC_except_table5434
- GCC_except_table5572
- GCC_except_table5579
- GCC_except_table5613
- GCC_except_table5614
- GCC_except_table5713
- GCC_except_table585
- GCC_except_table601
- GCC_except_table6206
- GCC_except_table6239
- GCC_except_table6242
- GCC_except_table6243
- GCC_except_table6248
- GCC_except_table6270
- GCC_except_table63
- GCC_except_table6364
- GCC_except_table6460
- GCC_except_table6500
- GCC_except_table6502
- GCC_except_table6536
- GCC_except_table6537
- GCC_except_table6571
- GCC_except_table6573
- GCC_except_table6623
- GCC_except_table6683
- GCC_except_table6708
- GCC_except_table6715
- GCC_except_table6726
- GCC_except_table6731
- GCC_except_table6734
- GCC_except_table696
- GCC_except_table697
- GCC_except_table703
- GCC_except_table7064
- GCC_except_table7070
- GCC_except_table7074
- GCC_except_table7078
- GCC_except_table7090
- GCC_except_table7110
- GCC_except_table7119
- GCC_except_table7177
- GCC_except_table7229
- GCC_except_table7260
- GCC_except_table7567
- GCC_except_table7622
- GCC_except_table768
- GCC_except_table775
- GCC_except_table7773
- GCC_except_table7780
- GCC_except_table7837
- GCC_except_table7854
- GCC_except_table7872
- GCC_except_table7889
- GCC_except_table789
- GCC_except_table7899
- GCC_except_table7948
- GCC_except_table7952
- GCC_except_table7954
- GCC_except_table7961
- GCC_except_table7967
- GCC_except_table7999
- GCC_except_table8015
- GCC_except_table8038
- GCC_except_table8063
- GCC_except_table807
- GCC_except_table8070
- GCC_except_table8075
- GCC_except_table8078
- GCC_except_table8079
- GCC_except_table8080
- GCC_except_table8094
- GCC_except_table8152
- GCC_except_table8220
- GCC_except_table8246
- GCC_except_table830
- GCC_except_table8335
- GCC_except_table8354
- GCC_except_table8393
- GCC_except_table84
- GCC_except_table8423
- GCC_except_table8427
- GCC_except_table8582
- GCC_except_table8640
- GCC_except_table8642
- GCC_except_table8826
- GCC_except_table8860
- GCC_except_table8883
- GCC_except_table8893
- GCC_except_table8911
- GCC_except_table8912
- GCC_except_table8916
- GCC_except_table8980
- GCC_except_table9276
- GCC_except_table9294
- GCC_except_table9447
- GCC_except_table9451
- GCC_except_table9453
- GCC_except_table9455
- GCC_except_table9456
- GCC_except_table9457
- GCC_except_table9488
- GCC_except_table9496
- GCC_except_table9526
- GCC_except_table954
- GCC_except_table9552
- GCC_except_table9570
- GCC_except_table9574
- GCC_except_table9578
- GCC_except_table9580
- GCC_except_table9652
- GCC_except_table9675
- GCC_except_table9703
- GCC_except_table9715
- GCC_except_table972
- GCC_except_table9720
- GCC_except_table9736
- GCC_except_table9838
- ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
CStrings:
+ "%s Initialized AVCaptureDeviceDirectionCoordinator for UIView: %@"
+ "%s Legacy device, published default map: %@."
+ "%s reserve: %f (statusBarCompact: %d, statusBarOrientationDefault: %d, layoutPlane: %ld, effectivelyFullScreen: %d)"
+ "-[AVCaptureDeviceDirectionCoordinator _updateCurrentMap]"
+ "-[AVCaptureDeviceDirectionCoordinator initWithView:deviceTypes:changeHandler:]"
+ "-[AVMobileGlassControlsView _rightInsetReserveForTopControls]"
+ "Error: setAllowInfoMetadataSubpanel is only available on the TV app, the Artemis app and the Fitness app."
+ "HWModelStr"
+ "MPBaseAppEntityIdentifier"
+ "MPNowPlayingInfoCenter"
+ "MPNowPlayingInfoPropertyAppEntityIdentifiers"
+ "Non-Legacy Device Detected. Returning self."
+ "Transferring %lu app entity path(s) from MPNowPlayingInfoCenter"
+ "V68"
+ "com.apple.avkit.direction-coordinator"
+ "deviceType: %@, mediaTypes: %@, position: %ld, uniqueID: %@, localizedName: %@"
+ "forwardFacingDeviceDescriptors: %@, backwardFacingDeviceDescriptors: %@"
+ "\xf0Q"
- "Error: setAllowInfoMetadataSubpanel is only available on the TV app and the Artemis app."
- "\xf0A"
```
