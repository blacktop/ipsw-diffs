## AVKit

> `/System/iOSSupport/System/Library/Frameworks/AVKit.framework/Versions/A/AVKit`

```diff

-1235.3.1.0.0
-  __TEXT.__text: 0xd7598
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x10060
-  __TEXT.__cstring: 0x9a21
-  __TEXT.__const: 0x670
+1240.20.1.0.0
+  __TEXT.__text: 0xd8068
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_methlist: 0x11cf4
+  __TEXT.__dlopen_cstrs: 0x58
+  __TEXT.__cstring: 0x9b1d
+  __TEXT.__const: 0x690
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x1ea0
-  __TEXT.__oslogstring: 0x41ed
-  __TEXT.__dlopen_cstrs: 0x58
+  __TEXT.__gcc_except_tab: 0x1f0c
+  __TEXT.__oslogstring: 0x4171
   __TEXT.__ustring: 0x3c
-  __TEXT.__unwind_info: 0x3958
-  __TEXT.__objc_classname: 0x26f4
-  __TEXT.__objc_methname: 0x3424d
-  __TEXT.__objc_methtype: 0x6b40
-  __TEXT.__objc_stubs: 0x1df60
-  __DATA_CONST.__got: 0xbc8
-  __DATA_CONST.__const: 0x1fd8
+  __TEXT.__unwind_info: 0x3938
+  __TEXT.__objc_classname: 0x26f6
+  __TEXT.__objc_methname: 0x34692
+  __TEXT.__objc_methtype: 0x6b8f
+  __TEXT.__objc_stubs: 0x1e1c0
+  __DATA_CONST.__got: 0xbf0
+  __DATA_CONST.__const: 0x1fd0
   __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8f08
+  __DATA_CONST.__objc_selrefs: 0x9260
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x500
   __DATA_CONST.__objc_arraydata: 0x1a8
-  __AUTH_CONST.__auth_got: 0x708
-  __AUTH_CONST.__const: 0x1ae0
-  __AUTH_CONST.__cfstring: 0x5080
-  __AUTH_CONST.__objc_const: 0x22ca8
+  __AUTH_CONST.__auth_got: 0x718
+  __AUTH_CONST.__const: 0x1b00
+  __AUTH_CONST.__cfstring: 0x5240
+  __AUTH_CONST.__objc_const: 0x1fe48
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH.__objc_data: 0x3020
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x1b10
+  __DATA.__objc_ivar: 0x1b54
   __DATA.__data: 0x26b0
-  __DATA.__bss: 0x1f8
+  __DATA.__bss: 0x1e8
   __DATA_DIRTY.__objc_data: 0xe10
   __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 17726AFE-019F-3D71-A2CA-1D3ED3BDA3DB
-  Functions: 6033
-  Symbols:   15045
-  CStrings:  10408
+  UUID: 552CEE25-9195-3F7D-8B25-723081358AAC
+  Functions: 6042
+  Symbols:   15115
+  CStrings:  10488
 
Symbols:
+ -[AVControlItem setTip:]
+ -[AVControlItem tip]
+ -[AVEditBehaviorContext _createAssetImageGenerator]
+ -[AVMobileChromelessControlsViewController auxiliaryControlsView:didOverflowControls:]
+ -[AVMobileChromelessPlaybackControlButton _glyphForCurrentSkipInterval]
+ -[AVMobileChromelessPlaybackControlButton _setupMicaPackageIfNeeded]
+ -[AVMobileChromelessPlaybackControlButton _updateEnabledState]
+ -[AVMobileChromelessPlaybackControlButton _updateGlyphSkipInterval]
+ -[AVMobileChromelessPlaybackControlButton _updateImageViewHiddenState]
+ -[AVMobileChromelessPlaybackControlButton _updateTintColor]
+ -[AVMobileChromelessPlaybackControlButton buttonMicaPackageContainerView]
+ -[AVMobileChromelessPlaybackControlButton buttonMicaPackage]
+ -[AVMobileChromelessPlaybackControlButton setButtonMicaPackage:]
+ -[AVMobileChromelessPlaybackControlButton setButtonMicaPackageContainerView:]
+ -[AVMobileChromelessPlaybackControlButton setEnabled:]
+ -[AVMobileChromelessPlaybackControlButton setImageName:]
+ -[AVMobileChromelessPlaybackControlButton setSkipInterval:]
+ -[AVMobileChromelessPlaybackControlButton skipInterval]
+ -[AVMobileChromelessPlaybackControlButton tintColorDidChange]
+ -[AVMobileChromelessPlaybackControlsView backwardSecondaryControlSkipInterval]
+ -[AVMobileChromelessPlaybackControlsView forwardSecondaryControlSkipInterval]
+ -[AVMobileChromelessPlaybackControlsView setBackwardSecondaryControlSkipInterval:]
+ -[AVMobileChromelessPlaybackControlsView setForwardSecondaryControlSkipInterval:]
+ -[AVMobileChromelessPlaybackControlsView triggerBackwardSecondaryControlIconAnimation]
+ -[AVMobileChromelessPlaybackControlsView triggerForwardSecondaryControlIconAnimation]
+ -[AVPlayerItem(AVKitAdditionsPrivate) disableAVKitIntegratedTimeline]
+ -[AVPlayerItem(AVKitAdditionsPrivate) isAVKitIntegratedTimelineDisabled]
+ -[AVPlayerViewController _updateVideoGravityPinchGestureEnablementState]
+ -[AVPlayerViewController playerViewControllerContentViewDidMoveToSuperview:]
+ -[AVPlayerViewController scheduleTips]
+ -[AVPlayerViewControllerConfiguration .cxx_destruct]
+ -[AVPlayerViewControllerConfiguration setTips:]
+ -[AVPlayerViewControllerConfiguration tips]
+ -[AVPlayerViewControllerContentView isInAScrollView]
+ AVDefaultHitRectInsets.12674
+ GCC_except_table1000
+ GCC_except_table1079
+ GCC_except_table1080
+ GCC_except_table1088
+ GCC_except_table1115
+ GCC_except_table1128
+ GCC_except_table1187
+ GCC_except_table1297
+ GCC_except_table130
+ GCC_except_table145
+ GCC_except_table1456
+ GCC_except_table1463
+ GCC_except_table1466
+ GCC_except_table1497
+ GCC_except_table1498
+ GCC_except_table1616
+ GCC_except_table165
+ GCC_except_table1738
+ GCC_except_table187
+ GCC_except_table1930
+ GCC_except_table194
+ GCC_except_table199
+ GCC_except_table203
+ GCC_except_table204
+ GCC_except_table2096
+ GCC_except_table2099
+ GCC_except_table2104
+ GCC_except_table2106
+ GCC_except_table2110
+ GCC_except_table2131
+ GCC_except_table2135
+ GCC_except_table2139
+ GCC_except_table2140
+ GCC_except_table2141
+ GCC_except_table2145
+ GCC_except_table2152
+ GCC_except_table216
+ GCC_except_table2165
+ GCC_except_table2177
+ GCC_except_table2205
+ GCC_except_table2216
+ GCC_except_table2250
+ GCC_except_table2262
+ GCC_except_table2289
+ GCC_except_table2295
+ GCC_except_table2308
+ GCC_except_table2368
+ GCC_except_table2391
+ GCC_except_table2460
+ GCC_except_table2512
+ GCC_except_table2580
+ GCC_except_table2581
+ GCC_except_table2664
+ GCC_except_table2783
+ GCC_except_table2803
+ GCC_except_table2931
+ GCC_except_table3492
+ GCC_except_table3498
+ GCC_except_table3505
+ GCC_except_table3513
+ GCC_except_table3537
+ GCC_except_table3546
+ GCC_except_table3548
+ GCC_except_table3606
+ GCC_except_table3658
+ GCC_except_table382
+ GCC_except_table3867
+ GCC_except_table3868
+ GCC_except_table3869
+ GCC_except_table3879
+ GCC_except_table3980
+ GCC_except_table4020
+ GCC_except_table4025
+ GCC_except_table4062
+ GCC_except_table4141
+ GCC_except_table4277
+ GCC_except_table4297
+ GCC_except_table4322
+ GCC_except_table4432
+ GCC_except_table4438
+ GCC_except_table4545
+ GCC_except_table4566
+ GCC_except_table4568
+ GCC_except_table457
+ GCC_except_table4752
+ GCC_except_table4864
+ GCC_except_table4868
+ GCC_except_table4880
+ GCC_except_table4976
+ GCC_except_table4979
+ GCC_except_table5108
+ GCC_except_table5169
+ GCC_except_table5239
+ GCC_except_table5362
+ GCC_except_table5364
+ GCC_except_table5378
+ GCC_except_table5535
+ GCC_except_table5538
+ GCC_except_table5668
+ GCC_except_table5690
+ GCC_except_table587
+ GCC_except_table5908
+ GCC_except_table5939
+ GCC_except_table5961
+ GCC_except_table6013
+ GCC_except_table611
+ GCC_except_table706
+ GCC_except_table735
+ GCC_except_table745
+ GCC_except_table748
+ OBJC_IVAR_$_AVControlItem._tip
+ OBJC_IVAR_$_AVMobileChromelessControlsViewController._controlsInOverflowMenu
+ OBJC_IVAR_$_AVMobileChromelessControlsViewController._temporarilyVisible
+ OBJC_IVAR_$_AVMobileChromelessControlsViewController._volumeSliderTemporarilyVisibleInFullscreen
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._buttonMicaPackage
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._buttonMicaPackageContainerView
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._prefersMicaPackage
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._skipInterval
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._skipInterval10
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._skipInterval15
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._skipInterval30
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._skipInterval45
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._skipInterval5
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._skipInterval60
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._skipInterval75
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._skipInterval90
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlsView._backwardIntervalSkipGlyphState
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlsView._backwardSecondaryControlSkipInterval
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlsView._forwardIntervalSkipGlyphState
+ OBJC_IVAR_$_AVMobileChromelessPlaybackControlsView._forwardSecondaryControlSkipInterval
+ OBJC_IVAR_$_AVPlayerViewControllerConfiguration._tips
+ _AVIntervalSkipGlyphStateNameState1
+ _AVIntervalSkipGlyphStateNameState2
+ _AVMicaPackageNameIntervalSkipGlyph
+ _AVMobileAccessibilityLabelMute
+ _AVMobileAccessibilityLabelUnmute
+ _CATransform3DMakeRotation
+ _CGColorCreateCopyWithAlpha
+ _CommonInit.17890
+ _OBJC_CLASS_$_CAShapeLayer
+ __118-[AVPlayerViewController pictureInPictureController:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:]_block_invoke.750
+ __Block_byref_object_copy_.18403
+ __Block_byref_object_copy_.6214
+ __Block_byref_object_dispose_.18404
+ __Block_byref_object_dispose_.6215
+ ___39-[AVPlayerViewController _addObservers]_block_invoke_18
+ ___47-[AVMobileAuxiliaryControlsView layoutSubviews]_block_invoke
+ ___58-[AVMobileChromelessPlaybackControlButton setHighlighted:]_block_invoke_2
+ ___61-[AVMobileChromelessControlsViewController _observationSetup]_block_invoke_26
+ __block_literal_global.10.3266
+ __block_literal_global.1053
+ __block_literal_global.112.7351
+ __block_literal_global.112.9415
+ __block_literal_global.114.9416
+ __block_literal_global.11449
+ __block_literal_global.11588
+ __block_literal_global.119
+ __block_literal_global.1204
+ __block_literal_global.121
+ __block_literal_global.12379
+ __block_literal_global.12669
+ __block_literal_global.128
+ __block_literal_global.13.18654
+ __block_literal_global.13.3267
+ __block_literal_global.133.13637
+ __block_literal_global.135
+ __block_literal_global.13640
+ __block_literal_global.14.17570
+ __block_literal_global.14036
+ __block_literal_global.141.2836
+ __block_literal_global.14159
+ __block_literal_global.143.13615
+ __block_literal_global.146.13610
+ __block_literal_global.14922
+ __block_literal_global.151
+ __block_literal_global.15308
+ __block_literal_global.156
+ __block_literal_global.15774
+ __block_literal_global.15959
+ __block_literal_global.16.11447
+ __block_literal_global.16.16402
+ __block_literal_global.16.3268
+ __block_literal_global.161
+ __block_literal_global.16137
+ __block_literal_global.16417
+ __block_literal_global.166
+ __block_literal_global.16839
+ __block_literal_global.171
+ __block_literal_global.17209
+ __block_literal_global.17315
+ __block_literal_global.17568
+ __block_literal_global.176
+ __block_literal_global.18089
+ __block_literal_global.181
+ __block_literal_global.183
+ __block_literal_global.18405
+ __block_literal_global.18642
+ __block_literal_global.188.14082
+ __block_literal_global.19.3269
+ __block_literal_global.19.8983
+ __block_literal_global.193
+ __block_literal_global.19671
+ __block_literal_global.198
+ __block_literal_global.19920
+ __block_literal_global.203
+ __block_literal_global.208
+ __block_literal_global.2112
+ __block_literal_global.213
+ __block_literal_global.218
+ __block_literal_global.226
+ __block_literal_global.231
+ __block_literal_global.2323
+ __block_literal_global.236
+ __block_literal_global.238
+ __block_literal_global.24.11440
+ __block_literal_global.24.3270
+ __block_literal_global.24.8984
+ __block_literal_global.248
+ __block_literal_global.253.9856
+ __block_literal_global.255
+ __block_literal_global.269
+ __block_literal_global.27.16405
+ __block_literal_global.27.3271
+ __block_literal_global.274
+ __block_literal_global.279
+ __block_literal_global.2839
+ __block_literal_global.284
+ __block_literal_global.2905
+ __block_literal_global.3091
+ __block_literal_global.3265
+ __block_literal_global.34.8968
+ __block_literal_global.3445
+ __block_literal_global.3783
+ __block_literal_global.39.4114
+ __block_literal_global.4113
+ __block_literal_global.412
+ __block_literal_global.4228
+ __block_literal_global.45.14038
+ __block_literal_global.45.16841
+ __block_literal_global.487
+ __block_literal_global.50.11398
+ __block_literal_global.50.14040
+ __block_literal_global.50.6539
+ __block_literal_global.500
+ __block_literal_global.507
+ __block_literal_global.511
+ __block_literal_global.513
+ __block_literal_global.5146
+ __block_literal_global.515
+ __block_literal_global.517
+ __block_literal_global.519
+ __block_literal_global.519.6218
+ __block_literal_global.521
+ __block_literal_global.523
+ __block_literal_global.5234
+ __block_literal_global.55.9490
+ __block_literal_global.573
+ __block_literal_global.609
+ __block_literal_global.63.6519
+ __block_literal_global.6305
+ __block_literal_global.638
+ __block_literal_global.6533
+ __block_literal_global.66
+ __block_literal_global.668
+ __block_literal_global.695
+ __block_literal_global.7026
+ __block_literal_global.716
+ __block_literal_global.718
+ __block_literal_global.7341
+ __block_literal_global.7424
+ __block_literal_global.747
+ __block_literal_global.759
+ __block_literal_global.7593
+ __block_literal_global.762
+ __block_literal_global.8980
+ __block_literal_global.9155
+ __block_literal_global.9488
+ __block_literal_global.9950
+ _imageNameForMicaPackageState.imageNamesForStates.16138
+ _imageNameForMicaPackageState.onceToken.16136
+ _objc_msgSend$addAnimations:delayFactor:
+ _objc_msgSend$animatedSkipButtonsEnabled
+ _objc_msgSend$auxiliaryControlsView:didOverflowControls:
+ _objc_msgSend$backwardSecondaryControlSkipInterval
+ _objc_msgSend$buttonMicaPackage
+ _objc_msgSend$buttonMicaPackageContainerView
+ _objc_msgSend$forwardSecondaryControlSkipInterval
+ _objc_msgSend$getWhite:alpha:
+ _objc_msgSend$interstice
+ _objc_msgSend$isCollapsedInTimeLine
+ _objc_msgSend$isInAScrollView
+ _objc_msgSend$playerTipsEnabled
+ _objc_msgSend$playerViewControllerContentViewDidMoveToSuperview:
+ _objc_msgSend$prefersTintColorForPlaybackControlsView
+ _objc_msgSend$setBackwardSecondaryControlSkipInterval:
+ _objc_msgSend$setButtonMicaPackage:
+ _objc_msgSend$setFillColor:
+ _objc_msgSend$setForwardSecondaryControlSkipInterval:
+ _objc_msgSend$setInterruptible:
+ _objc_msgSend$setSkipInterval:
+ _objc_msgSend$setStrokeColor:
+ _objc_msgSend$sublayerWithName:
+ _objc_msgSend$timeline
+ _objc_msgSend$triggerBackwardSecondaryControlIconAnimation
+ _objc_msgSend$triggerForwardSecondaryControlIconAnimation
- -[AVEditBehaviorContext _generateThumbnails]
- -[AVMobileChromelessFluidSlider _normalizeSliderMarkValue:]
- -[AVMobileChromelessPlaybackControlButton _imageNameForMicaPackageState]
- -[AVMobileChromelessPlaybackControlButton playPauseButtonMicaPackageContainerView]
- -[AVMobileChromelessPlaybackControlButton playPauseButtonMicaPackage]
- -[AVMobileChromelessPlaybackControlButton setPlayPauseButtonMicaPackage:]
- -[AVMobileChromelessPlaybackControlButton setPlayPauseButtonMicaPackageContainerView:]
- AVDefaultHitRectInsets.12494
- GCC_except_table1056
- GCC_except_table1057
- GCC_except_table1065
- GCC_except_table1092
- GCC_except_table1105
- GCC_except_table1164
- GCC_except_table1274
- GCC_except_table129
- GCC_except_table1433
- GCC_except_table144
- GCC_except_table1440
- GCC_except_table1443
- GCC_except_table1474
- GCC_except_table1475
- GCC_except_table1593
- GCC_except_table164
- GCC_except_table1715
- GCC_except_table185
- GCC_except_table1886
- GCC_except_table192
- GCC_except_table197
- GCC_except_table200
- GCC_except_table201
- GCC_except_table2074
- GCC_except_table2077
- GCC_except_table2082
- GCC_except_table2084
- GCC_except_table2088
- GCC_except_table2109
- GCC_except_table2113
- GCC_except_table2117
- GCC_except_table2118
- GCC_except_table2119
- GCC_except_table2123
- GCC_except_table2130
- GCC_except_table214
- GCC_except_table2143
- GCC_except_table2155
- GCC_except_table2180
- GCC_except_table2191
- GCC_except_table2225
- GCC_except_table2237
- GCC_except_table2265
- GCC_except_table2271
- GCC_except_table2284
- GCC_except_table2343
- GCC_except_table2366
- GCC_except_table2434
- GCC_except_table2486
- GCC_except_table2554
- GCC_except_table2555
- GCC_except_table2639
- GCC_except_table2757
- GCC_except_table2777
- GCC_except_table2905
- GCC_except_table3466
- GCC_except_table3472
- GCC_except_table3479
- GCC_except_table3487
- GCC_except_table3511
- GCC_except_table3520
- GCC_except_table3522
- GCC_except_table3580
- GCC_except_table3632
- GCC_except_table377
- GCC_except_table3839
- GCC_except_table3840
- GCC_except_table3841
- GCC_except_table3851
- GCC_except_table3952
- GCC_except_table3992
- GCC_except_table3997
- GCC_except_table4034
- GCC_except_table4113
- GCC_except_table4249
- GCC_except_table4269
- GCC_except_table4294
- GCC_except_table4404
- GCC_except_table4410
- GCC_except_table4517
- GCC_except_table452
- GCC_except_table4538
- GCC_except_table4540
- GCC_except_table4724
- GCC_except_table4836
- GCC_except_table4840
- GCC_except_table4852
- GCC_except_table4948
- GCC_except_table4951
- GCC_except_table5080
- GCC_except_table5141
- GCC_except_table5333
- GCC_except_table5335
- GCC_except_table5349
- GCC_except_table5506
- GCC_except_table5509
- GCC_except_table5639
- GCC_except_table5661
- GCC_except_table582
- GCC_except_table5879
- GCC_except_table5910
- GCC_except_table5932
- GCC_except_table606
- GCC_except_table699
- GCC_except_table726
- GCC_except_table731
- GCC_except_table733
- GCC_except_table981
- OBJC_IVAR_$_AVMobileChromelessControlsViewController._temporarilyVisibile
- OBJC_IVAR_$_AVMobileChromelessControlsViewController._volumeSliderTemporarilyVisibileInFullscreen
- OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._playPauseButtonMicaPackage
- OBJC_IVAR_$_AVMobileChromelessPlaybackControlButton._playPauseButtonMicaPackageContainerView
- _AVMobileImageNameSkipBack10
- _AVMobileImageNameStartPreviousContentTransition
- _CommonInit.17703
- __118-[AVPlayerViewController pictureInPictureController:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:]_block_invoke.745
- __Block_byref_object_copy_.18216
- __Block_byref_object_copy_.6089
- __Block_byref_object_dispose_.18217
- __Block_byref_object_dispose_.6090
- ___72-[AVMobileChromelessPlaybackControlButton _imageNameForMicaPackageState]_block_invoke
- __block_literal_global.10.3156
- __block_literal_global.1003
- __block_literal_global.112.7215
- __block_literal_global.112.9256
- __block_literal_global.11269
- __block_literal_global.114.9257
- __block_literal_global.11408
- __block_literal_global.1150
- __block_literal_global.118
- __block_literal_global.120
- __block_literal_global.12199
- __block_literal_global.12489
- __block_literal_global.127.13455
- __block_literal_global.13.18469
- __block_literal_global.13.3157
- __block_literal_global.1318
- __block_literal_global.132
- __block_literal_global.134
- __block_literal_global.13458
- __block_literal_global.13854
- __block_literal_global.13974
- __block_literal_global.14.17383
- __block_literal_global.140.19484
- __block_literal_global.143.13433
- __block_literal_global.145
- __block_literal_global.14737
- __block_literal_global.150
- __block_literal_global.15122
- __block_literal_global.155
- __block_literal_global.15588
- __block_literal_global.15773
- __block_literal_global.15951
- __block_literal_global.16.11267
- __block_literal_global.16.16216
- __block_literal_global.16.3158
- __block_literal_global.160
- __block_literal_global.16231
- __block_literal_global.165
- __block_literal_global.16651
- __block_literal_global.170
- __block_literal_global.17022
- __block_literal_global.17128
- __block_literal_global.17381
- __block_literal_global.175
- __block_literal_global.17902
- __block_literal_global.180
- __block_literal_global.182
- __block_literal_global.18218
- __block_literal_global.18457
- __block_literal_global.187
- __block_literal_global.19.3159
- __block_literal_global.19.8823
- __block_literal_global.192
- __block_literal_global.19483
- __block_literal_global.197
- __block_literal_global.19738
- __block_literal_global.202
- __block_literal_global.2027
- __block_literal_global.207
- __block_literal_global.212.9748
- __block_literal_global.217
- __block_literal_global.2237
- __block_literal_global.225
- __block_literal_global.230
- __block_literal_global.235
- __block_literal_global.24.11260
- __block_literal_global.24.3160
- __block_literal_global.24.8824
- __block_literal_global.245
- __block_literal_global.250
- __block_literal_global.252
- __block_literal_global.266
- __block_literal_global.27.16219
- __block_literal_global.27.3161
- __block_literal_global.271
- __block_literal_global.2730
- __block_literal_global.276.6091
- __block_literal_global.2797
- __block_literal_global.281
- __block_literal_global.2983
- __block_literal_global.3155
- __block_literal_global.3332
- __block_literal_global.34.8808
- __block_literal_global.3667
- __block_literal_global.39.3996
- __block_literal_global.3995
- __block_literal_global.402
- __block_literal_global.4110
- __block_literal_global.45.13856
- __block_literal_global.45.16653
- __block_literal_global.490
- __block_literal_global.497
- __block_literal_global.50.11218
- __block_literal_global.50.13858
- __block_literal_global.5018
- __block_literal_global.506
- __block_literal_global.508
- __block_literal_global.508.6095
- __block_literal_global.51
- __block_literal_global.510
- __block_literal_global.5107
- __block_literal_global.512
- __block_literal_global.514
- __block_literal_global.516
- __block_literal_global.518
- __block_literal_global.55.9331
- __block_literal_global.568
- __block_literal_global.588
- __block_literal_global.6181
- __block_literal_global.633
- __block_literal_global.64
- __block_literal_global.6410
- __block_literal_global.658
- __block_literal_global.67
- __block_literal_global.6894
- __block_literal_global.690
- __block_literal_global.711
- __block_literal_global.713
- __block_literal_global.7205
- __block_literal_global.7283
- __block_literal_global.742
- __block_literal_global.7443
- __block_literal_global.754
- __block_literal_global.757
- __block_literal_global.8820
- __block_literal_global.8994
- __block_literal_global.9329
- __block_literal_global.9776
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_AVKit
- _imageNameForMicaPackageState.imageNamesForStates
- _imageNameForMicaPackageState.imageNamesForStates.15952
- _imageNameForMicaPackageState.onceToken
- _imageNameForMicaPackageState.onceToken.15950
- _kMRMediaRemoteOptionSkipInterval
- _objc_msgSend$_generateThumbnails
- _objc_msgSend$_makeBarButtonItems
- _objc_msgSend$_updateMicaPackage
- _objc_msgSend$playPauseButtonMicaPackage
- _objc_msgSend$playPauseButtonMicaPackageContainerView
- _objc_msgSend$setPlayPauseButtonMicaPackage:
CStrings:
+ "%dfill"
+ "-[AVPlayerItem(AVKitAdditionsPrivate) disableAVKitIntegratedTimeline]"
+ "@\"NSSet\""
+ "Can not seek chapter backward; skipping backward instead"
+ "Can not seek chapter forward; skipping forward instead"
+ "Overflow Menu"
+ "T@\"AVMicaPackage\",&,N,V_buttonMicaPackage"
+ "T@\"NSDictionary\",C,N,V_tips"
+ "T@\"UIView\",&,N,V_buttonMicaPackageContainerView"
+ "T@,&,N,V_tip"
+ "T{?=qiIq},N,V_backwardSecondaryControlSkipInterval"
+ "T{?=qiIq},N,V_forwardSecondaryControlSkipInterval"
+ "T{?=qiIq},N,V_skipInterval"
+ "_backwardIntervalSkipGlyphState"
+ "_backwardSecondaryControlSkipInterval"
+ "_buttonMicaPackage"
+ "_buttonMicaPackageContainerView"
+ "_controlsInOverflowMenu"
+ "_forwardIntervalSkipGlyphState"
+ "_forwardSecondaryControlSkipInterval"
+ "_prefersMicaPackage"
+ "_skipInterval"
+ "_skipInterval10"
+ "_skipInterval15"
+ "_skipInterval30"
+ "_skipInterval45"
+ "_skipInterval5"
+ "_skipInterval60"
+ "_skipInterval75"
+ "_skipInterval90"
+ "_temporarilyVisible"
+ "_tip"
+ "_tips"
+ "_volumeSliderTemporarilyVisibleInFullscreen"
+ "addAnimations:delayFactor:"
+ "animatedSkipButtonsEnabled"
+ "arab"
+ "auxiliaryControlsView:didOverflowControls:"
+ "backwardSecondaryControlSkipInterval"
+ "buttonMicaPackage"
+ "buttonMicaPackageContainerView"
+ "contentView.bounds"
+ "deva"
+ "disableAVKitIntegratedTimeline"
+ "flip"
+ "forwardSecondaryControlSkipInterval"
+ "getWhite:alpha:"
+ "glyphs"
+ "glyphs-mask"
+ "interstice"
+ "isAVKitIntegratedTimelineDisabled"
+ "isCollapsedInTimeLine"
+ "isInAScrollView"
+ "origin"
+ "path-pause-tint-shape"
+ "path-play-tint-shape"
+ "playerTipsEnabled"
+ "playerViewControllerContentViewDidMoveToSuperview:"
+ "prefersTintColorForPlaybackControlsView"
+ "ringstroke"
+ "scheduleTips"
+ "setBackwardSecondaryControlSkipInterval:"
+ "setButtonMicaPackage:"
+ "setButtonMicaPackageContainerView:"
+ "setFillColor:"
+ "setForwardSecondaryControlSkipInterval:"
+ "setInterruptible:"
+ "setSkipInterval:"
+ "setStrokeColor:"
+ "setTip:"
+ "setTips:"
+ "skipInterval"
+ "sublayerWithName:"
+ "timeline"
+ "tip"
+ "tips"
+ "trianglefill"
+ "triggerBackwardSecondaryControlIconAnimation"
+ "triggerForwardSecondaryControlIconAnimation"
+ "v32@0:8@\"AVMobileAuxiliaryControlsView\"16@\"NSSet\"24"
+ "v40@0:8{?=qiIq}16"
- "Both the imageView and the micaPackage rootLayer are visible in the hierarchy at the same time."
- "Can not seek chapter backward; skipping backward %.2f seconds instead."
- "Can not seek chapter forward; skipping forward %.2f seconds instead."
- "T@\"AVMicaPackage\",&,N,V_playPauseButtonMicaPackage"
- "T@\"UIView\",&,N,V_playPauseButtonMicaPackageContainerView"
- "_generateThumbnails"
- "_makeBarButtonItems"
- "_playPauseButtonMicaPackage"
- "_playPauseButtonMicaPackageContainerView"
- "_temporarilyVisibile"
- "_updateMicaPackage"
- "_volumeSliderTemporarilyVisibileInFullscreen"
- "playPauseButtonMicaPackage"
- "playPauseButtonMicaPackageContainerView"
- "setPlayPauseButtonMicaPackage:"
- "setPlayPauseButtonMicaPackageContainerView:"

```
