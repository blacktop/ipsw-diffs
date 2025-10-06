## AXSpringBoardServerInstance

> `/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance`

```diff

-3093.2.4.4.11
-  __TEXT.__text: 0x3eb40
-  __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_methlist: 0x2394
+3093.23.0.0.0
+  __TEXT.__text: 0x3d19c
+  __TEXT.__auth_stubs: 0x1730
+  __TEXT.__objc_methlist: 0x249c
   __TEXT.__const: 0x674
-  __TEXT.__cstring: 0x65db
-  __TEXT.__gcc_except_tab: 0x960
-  __TEXT.__oslogstring: 0x1236
+  __TEXT.__cstring: 0x60fb
+  __TEXT.__gcc_except_tab: 0x968
+  __TEXT.__oslogstring: 0x1374
   __TEXT.__dlopen_cstrs: 0x1d0
   __TEXT.__swift5_typeref: 0x202
   __TEXT.__swift5_capture: 0xd8

   __TEXT.__swift5_fieldmd: 0xa4
   __TEXT.__swift5_proto: 0x34
   __TEXT.__swift5_types: 0x20
-  __TEXT.__unwind_info: 0x1144
-  __TEXT.__eh_frame: 0x220
-  __TEXT.__objc_classname: 0x980
-  __TEXT.__objc_methname: 0x8e0f
-  __TEXT.__objc_methtype: 0x118e
-  __TEXT.__objc_stubs: 0x7200
-  __DATA_CONST.__got: 0x408
+  __TEXT.__unwind_info: 0x1130
+  __TEXT.__eh_frame: 0x1a8
+  __TEXT.__objc_classname: 0x9b2
+  __TEXT.__objc_methname: 0x910e
+  __TEXT.__objc_methtype: 0x11d3
+  __TEXT.__objc_stubs: 0x74c0
+  __DATA_CONST.__got: 0x410
   __DATA_CONST.__const: 0xf28
-  __DATA_CONST.__objc_classlist: 0x1e0
+  __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x34f8
-  __DATA_CONST.__objc_selrefs: 0x23e0
+  __DATA_CONST.__objc_const: 0x3768
+  __DATA_CONST.__objc_selrefs: 0x24a8
+  __DATA_CONST.__objc_classrefs: 0x4a0
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__cfstring: 0x6080
+  __AUTH_CONST.__cfstring: 0x6180
   __AUTH_CONST.__const: 0xdc8
-  __AUTH_CONST.__objc_const: 0x1128
+  __AUTH_CONST.__objc_const: 0x11b8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0xbd0
-  __AUTH.__objc_data: 0x390
+  __AUTH_CONST.__auth_got: 0xba8
+  __AUTH.__objc_data: 0x3e0
   __AUTH.__data: 0x250
-  __DATA.__objc_classrefs: 0x498
-  __DATA.__objc_superrefs: 0xf0
-  __DATA.__objc_ivar: 0xcc
-  __DATA.__data: 0x680
+  __DATA.__objc_ivar: 0xec
+  __DATA.__data: 0x740
   __DATA.__bss: 0x880
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xf00

   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/HearingCore.framework/HearingCore
   - /System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 15113025-D4B4-3AD4-8889-3C9C9FA01203
-  Functions: 1361
-  Symbols:   4708
-  CStrings:  3307
+  UUID: 9FE4A44A-E24C-3B3B-A9B8-942D1AEDE764
+  Functions: 1381
+  Symbols:   4812
+  CStrings:  3348
 
Symbols:
+ +[AccessibilityFeatureCache supportsSecureCoding]
+ -[AXSpringBoardServerHelper _restoreAccessibilityFeatureFromSecurePayCache:]
+ -[AXSpringBoardServerHelper _restoreSecurePayFeaturesIfNeeded]
+ -[AXSpringBoardServerHelper _restoreSecurePayFeaturesIfNeeded].cold.1
+ -[AXSpringBoardServerHelper setSecurePayAccessibilityFeaturesDisabled:withServerInstance:]
+ -[AXSpringBoardServerHelper setSecurePayAccessibilityFeaturesDisabled:withServerInstance:].cold.1
+ -[AccessibilityFeatureCache assistiveTouch]
+ -[AccessibilityFeatureCache backTap]
+ -[AccessibilityFeatureCache encodeWithCoder:]
+ -[AccessibilityFeatureCache initWithCoder:]
+ -[AccessibilityFeatureCache liveCaptions]
+ -[AccessibilityFeatureCache liveSpeech]
+ -[AccessibilityFeatureCache setAssistiveTouch:]
+ -[AccessibilityFeatureCache setBackTap:]
+ -[AccessibilityFeatureCache setLiveCaptions:]
+ -[AccessibilityFeatureCache setLiveSpeech:]
+ -[AccessibilityFeatureCache setSpeakScreen:]
+ -[AccessibilityFeatureCache setVoiceControl:]
+ -[AccessibilityFeatureCache setZoom:]
+ -[AccessibilityFeatureCache speakScreen]
+ -[AccessibilityFeatureCache voiceControl]
+ -[AccessibilityFeatureCache zoom]
+ -[_AXSpringBoardServerInstance _setSecurePayAccessibilityFeaturesDisabled:]
+ GCC_except_table113
+ GCC_except_table115
+ GCC_except_table120
+ GCC_except_table122
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table154
+ GCC_except_table165
+ GCC_except_table169
+ GCC_except_table171
+ GCC_except_table174
+ GCC_except_table176
+ GCC_except_table181
+ GCC_except_table183
+ GCC_except_table185
+ GCC_except_table189
+ GCC_except_table198
+ GCC_except_table201
+ GCC_except_table203
+ GCC_except_table205
+ GCC_except_table207
+ GCC_except_table210
+ GCC_except_table212
+ GCC_except_table217
+ GCC_except_table227
+ GCC_except_table230
+ GCC_except_table232
+ GCC_except_table234
+ GCC_except_table241
+ GCC_except_table258
+ GCC_except_table259
+ GCC_except_table263
+ GCC_except_table264
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table269
+ GCC_except_table270
+ GCC_except_table272
+ GCC_except_table276
+ GCC_except_table301
+ GCC_except_table311
+ GCC_except_table320
+ GCC_except_table323
+ GCC_except_table324
+ GCC_except_table343
+ GCC_except_table369
+ GCC_except_table373
+ GCC_except_table375
+ GCC_except_table377
+ GCC_except_table380
+ GCC_except_table382
+ GCC_except_table384
+ GCC_except_table386
+ GCC_except_table392
+ GCC_except_table409
+ GCC_except_table77
+ _AXAssertionTypeDisableSecurePayAccessibilityFeatures
+ _OBJC_CLASS_$_AccessibilityFeatureCache
+ _OBJC_IVAR_$_AXSpringBoardServerHelper._axFeatureCache
+ _OBJC_IVAR_$_AccessibilityFeatureCache._assistiveTouch
+ _OBJC_IVAR_$_AccessibilityFeatureCache._backTap
+ _OBJC_IVAR_$_AccessibilityFeatureCache._liveCaptions
+ _OBJC_IVAR_$_AccessibilityFeatureCache._liveSpeech
+ _OBJC_IVAR_$_AccessibilityFeatureCache._speakScreen
+ _OBJC_IVAR_$_AccessibilityFeatureCache._voiceControl
+ _OBJC_IVAR_$_AccessibilityFeatureCache._zoom
+ _OBJC_METACLASS_$_AccessibilityFeatureCache
+ __AXSBackTapEnabled
+ __AXSBackTapSetEnabled
+ __OBJC_$_CLASS_METHODS_AccessibilityFeatureCache
+ __OBJC_$_CLASS_PROP_LIST_AccessibilityFeatureCache
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_AccessibilityFeatureCache
+ __OBJC_$_INSTANCE_VARIABLES_AccessibilityFeatureCache
+ __OBJC_$_PROP_LIST_AccessibilityFeatureCache
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_AccessibilityFeatureCache
+ __OBJC_CLASS_RO_$_AccessibilityFeatureCache
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_AccessibilityFeatureCache
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ ___33-[AXSpringBoardServerHelper init]_block_invoke.1582
+ ___33-[AXSpringBoardServerHelper init]_block_invoke.1596
+ ___33-[AXSpringBoardServerHelper init]_block_invoke_2.1585
+ ___33-[AXSpringBoardServerHelper init]_block_invoke_3.1588
+ ___35-[AXSpringBoardSettingsLoader init]_block_invoke.452
+ ___35-[AXSpringBoardSettingsLoader init]_block_invoke.458
+ ___46-[AXSpringBoardServerHelper _sortVisibleItems]_block_invoke.1911
+ ___47-[AXSpringBoardServerHelper _unlockWithIntent:]_block_invoke.1769
+ ___54-[AXSpringBoardServerHelper _toggleTripleClickDisplay]_block_invoke.1923
+ ___54-[AXSpringBoardServerHelper _toggleTripleClickDisplay]_block_invoke.1927
+ ___59+[AXSpringBoardSettingsLoader _checkForHomeButtonBreakage:]_block_invoke.427
+ ___60-[AXSpringBoardServerHelper accessibilityShowControlCenter:]_block_invoke.1897
+ ___60-[AXSpringBoardServerHelper accessibilityShowControlCenter:]_block_invoke.1898
+ ___61-[AXSpringBoardServerHelper hasActiveCallWithServerInstance:]_block_invoke.1799
+ ___63-[AXSpringBoardServerHelper openAppSwitcherWithServerInstance:]_block_invoke.1659
+ ___63-[AXSpringBoardServerHelper openAppSwitcherWithServerInstance:]_block_invoke_2.1660
+ ___65+[AXSpringBoardSettingsLoader _gracefulRebootForBrokenHomeButton]_block_invoke.394
+ ___67-[AXSpringBoardServerHelper _displayViewController:withCompletion:]_block_invoke.1932
+ ___67-[AXSpringBoardServerHelper _displayViewController:withCompletion:]_block_invoke.1940
+ ___68+[AXSpringBoardSettingsLoader _initializeDelayedSpringBoardSettings]_block_invoke.308
+ ___68+[AXSpringBoardSettingsLoader _initializeDelayedSpringBoardSettings]_block_invoke_2.314
+ ___68+[AXSpringBoardSettingsLoader _initializeDelayedSpringBoardSettings]_block_invoke_3.315
+ ___73-[_AXSpringBoardServerInstance _setCallRoute:ifCurrentlyRoutedTo:rampUp:]_block_invoke.284
+ ___81-[AXSpringBoardServerHelper _accessibilityShowNotificationCenter:serverInstance:]_block_invoke.1881
+ ___81-[AXSpringBoardServerHelper _accessibilityShowNotificationCenter:serverInstance:]_block_invoke.1888
+ ___84-[AXSpringBoardServerHelper _accessibilityShowCoverSheet:serverInstance:completion:]_block_invoke.1869
+ ___84-[AXSpringBoardServerHelper _accessibilityShowCoverSheet:serverInstance:completion:]_block_invoke.1870
+ ___84-[AXSpringBoardServerHelper _accessibilityShowCoverSheet:serverInstance:completion:]_block_invoke.1871
+ ___84-[AXSpringBoardServerHelper _accessibilityShowCoverSheet:serverInstance:completion:]_block_invoke_2.1872
+ ___92-[_AXSpringBoardServerInstance _rampUpCallVolumeFromVolume:toVolume:totalDuration:progress:]_block_invoke.328
+ ___block_literal_global.1017
+ ___block_literal_global.1088
+ ___block_literal_global.1090
+ ___block_literal_global.1174
+ ___block_literal_global.1392
+ ___block_literal_global.1480
+ ___block_literal_global.1486
+ ___block_literal_global.1558
+ ___block_literal_global.1560
+ ___block_literal_global.1562
+ ___block_literal_global.1564
+ ___block_literal_global.1569
+ ___block_literal_global.1584
+ ___block_literal_global.1587
+ ___block_literal_global.1622
+ ___block_literal_global.1624
+ ___block_literal_global.1652
+ ___block_literal_global.1662
+ ___block_literal_global.1664
+ ___block_literal_global.1667
+ ___block_literal_global.1669
+ ___block_literal_global.1694
+ ___block_literal_global.1696
+ ___block_literal_global.1698
+ ___block_literal_global.1700
+ ___block_literal_global.1703
+ ___block_literal_global.1706
+ ___block_literal_global.1772
+ ___block_literal_global.1828
+ ___block_literal_global.1854
+ ___block_literal_global.1890
+ ___block_literal_global.1913
+ ___block_literal_global.1945
+ ___block_literal_global.2516
+ ___block_literal_global.2574
+ ___block_literal_global.2576
+ ___block_literal_global.2578
+ ___block_literal_global.293
+ ___block_literal_global.295
+ ___block_literal_global.310
+ ___block_literal_global.321
+ ___block_literal_global.323
+ ___block_literal_global.331
+ ___block_literal_global.337
+ ___block_literal_global.354
+ ___block_literal_global.384
+ ___block_literal_global.390
+ ___block_literal_global.401
+ ___block_literal_global.420
+ ___block_literal_global.429
+ ___block_literal_global.450
+ ___block_literal_global.486
+ ___block_literal_global.495
+ ___block_literal_global.500
+ ___block_literal_global.501
+ ___block_literal_global.567
+ ___block_literal_global.577
+ ___block_literal_global.579
+ ___block_literal_global.590
+ ___block_literal_global.592
+ ___block_literal_global.594
+ ___block_literal_global.596
+ ___block_literal_global.598
+ ___block_literal_global.600
+ ___block_literal_global.665
+ ___block_literal_global.668
+ ___block_literal_global.670
+ ___block_literal_global.798
+ ___incomingCallStateChanged_block_invoke.1396
+ __unnamed_array_storage.1025
+ __unnamed_array_storage.1098
+ __unnamed_array_storage.1099
+ __unnamed_array_storage.1111
+ __unnamed_array_storage.1112
+ __unnamed_array_storage.2502
+ __unnamed_array_storage.2506
+ __unnamed_array_storage.2507
+ __unnamed_array_storage.375
+ __unnamed_array_storage.379
+ __unnamed_array_storage.380
+ __unnamed_array_storage.385
+ __unnamed_array_storage.386
+ __unnamed_array_storage.388
+ __unnamed_array_storage.391
+ __unnamed_array_storage.392
+ __unnamed_array_storage.517
+ __unnamed_array_storage.785
+ __unnamed_array_storage.786
+ _objc_msgSend$_restoreAccessibilityFeatureFromSecurePayCache:
+ _objc_msgSend$_restoreSecurePayFeaturesIfNeeded
+ _objc_msgSend$_setSecurePayAccessibilityFeaturesDisabled:
+ _objc_msgSend$assistiveTouch
+ _objc_msgSend$backTap
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$liveCaptions
+ _objc_msgSend$liveSpeech
+ _objc_msgSend$securePayAssertionActive
+ _objc_msgSend$setAssistiveTouch:
+ _objc_msgSend$setBackTap:
+ _objc_msgSend$setLiveCaptions:
+ _objc_msgSend$setLiveSpeech:
+ _objc_msgSend$setSecurePayAccessibilityFeaturesDisabled:withServerInstance:
+ _objc_msgSend$setSecurePayAssertionActive:
+ _objc_msgSend$setSpeakScreen:
+ _objc_msgSend$setVoiceControl:
+ _objc_msgSend$setZoom:
+ _objc_msgSend$speakScreen
+ _objc_msgSend$voiceControl
+ _objc_msgSend$zoom
+ _swift_initStackObject
- GCC_except_table101
- GCC_except_table103
- GCC_except_table123
- GCC_except_table125
- GCC_except_table135
- GCC_except_table146
- GCC_except_table151
- GCC_except_table152
- GCC_except_table155
- GCC_except_table157
- GCC_except_table162
- GCC_except_table164
- GCC_except_table166
- GCC_except_table168
- GCC_except_table172
- GCC_except_table179
- GCC_except_table182
- GCC_except_table184
- GCC_except_table186
- GCC_except_table188
- GCC_except_table193
- GCC_except_table194
- GCC_except_table197
- GCC_except_table208
- GCC_except_table211
- GCC_except_table213
- GCC_except_table220
- GCC_except_table222
- GCC_except_table240
- GCC_except_table244
- GCC_except_table245
- GCC_except_table247
- GCC_except_table248
- GCC_except_table250
- GCC_except_table251
- GCC_except_table253
- GCC_except_table257
- GCC_except_table282
- GCC_except_table290
- GCC_except_table299
- GCC_except_table302
- GCC_except_table303
- GCC_except_table322
- GCC_except_table329
- GCC_except_table340
- GCC_except_table344
- GCC_except_table346
- GCC_except_table348
- GCC_except_table352
- GCC_except_table354
- GCC_except_table356
- GCC_except_table359
- GCC_except_table363
- GCC_except_table94
- GCC_except_table96
- ___33-[AXSpringBoardServerHelper init]_block_invoke.1487
- ___33-[AXSpringBoardServerHelper init]_block_invoke_2.1490
- ___33-[AXSpringBoardServerHelper init]_block_invoke_3.1493
- ___35-[AXSpringBoardSettingsLoader init]_block_invoke.428
- ___35-[AXSpringBoardSettingsLoader init]_block_invoke.434
- ___46-[AXSpringBoardServerHelper _sortVisibleItems]_block_invoke.1812
- ___47-[AXSpringBoardServerHelper _unlockWithIntent:]_block_invoke.1668
- ___54-[AXSpringBoardServerHelper _toggleTripleClickDisplay]_block_invoke.1824
- ___54-[AXSpringBoardServerHelper _toggleTripleClickDisplay]_block_invoke.1828
- ___59+[AXSpringBoardSettingsLoader _checkForHomeButtonBreakage:]_block_invoke.403
- ___60-[AXSpringBoardServerHelper accessibilityShowControlCenter:]_block_invoke.1797
- ___60-[AXSpringBoardServerHelper accessibilityShowControlCenter:]_block_invoke.1798
- ___61-[AXSpringBoardServerHelper hasActiveCallWithServerInstance:]_block_invoke.1698
- ___63-[AXSpringBoardServerHelper openAppSwitcherWithServerInstance:]_block_invoke.1558
- ___63-[AXSpringBoardServerHelper openAppSwitcherWithServerInstance:]_block_invoke_2.1559
- ___65+[AXSpringBoardSettingsLoader _gracefulRebootForBrokenHomeButton]_block_invoke.370
- ___67-[AXSpringBoardServerHelper _displayViewController:withCompletion:]_block_invoke.1833
- ___67-[AXSpringBoardServerHelper _displayViewController:withCompletion:]_block_invoke.1841
- ___68+[AXSpringBoardSettingsLoader _initializeDelayedSpringBoardSettings]_block_invoke.284
- ___68+[AXSpringBoardSettingsLoader _initializeDelayedSpringBoardSettings]_block_invoke_2.290
- ___68+[AXSpringBoardSettingsLoader _initializeDelayedSpringBoardSettings]_block_invoke_3.291
- ___73-[_AXSpringBoardServerInstance _setCallRoute:ifCurrentlyRoutedTo:rampUp:]_block_invoke.260
- ___81-[AXSpringBoardServerHelper _accessibilityShowNotificationCenter:serverInstance:]_block_invoke.1781
- ___81-[AXSpringBoardServerHelper _accessibilityShowNotificationCenter:serverInstance:]_block_invoke.1788
- ___84-[AXSpringBoardServerHelper _accessibilityShowCoverSheet:serverInstance:completion:]_block_invoke.1769
- ___84-[AXSpringBoardServerHelper _accessibilityShowCoverSheet:serverInstance:completion:]_block_invoke.1770
- ___84-[AXSpringBoardServerHelper _accessibilityShowCoverSheet:serverInstance:completion:]_block_invoke.1771
- ___84-[AXSpringBoardServerHelper _accessibilityShowCoverSheet:serverInstance:completion:]_block_invoke_2.1772
- ___92-[_AXSpringBoardServerInstance _rampUpCallVolumeFromVolume:toVolume:totalDuration:progress:]_block_invoke.304
- ___block_literal_global.1061
- ___block_literal_global.1063
- ___block_literal_global.1147
- ___block_literal_global.1363
- ___block_literal_global.1383
- ___block_literal_global.1389
- ___block_literal_global.1463
- ___block_literal_global.1465
- ___block_literal_global.1467
- ___block_literal_global.1469
- ___block_literal_global.1474
- ___block_literal_global.1489
- ___block_literal_global.1492
- ___block_literal_global.1521
- ___block_literal_global.1523
- ___block_literal_global.1551
- ___block_literal_global.1561
- ___block_literal_global.1563
- ___block_literal_global.1566
- ___block_literal_global.1568
- ___block_literal_global.1593
- ___block_literal_global.1595
- ___block_literal_global.1597
- ___block_literal_global.1599
- ___block_literal_global.1602
- ___block_literal_global.1605
- ___block_literal_global.1671
- ___block_literal_global.1728
- ___block_literal_global.1754
- ___block_literal_global.1790
- ___block_literal_global.1814
- ___block_literal_global.1846
- ___block_literal_global.2413
- ___block_literal_global.245
- ___block_literal_global.2471
- ___block_literal_global.2473
- ___block_literal_global.2475
- ___block_literal_global.271
- ___block_literal_global.273
- ___block_literal_global.286
- ___block_literal_global.299
- ___block_literal_global.307
- ___block_literal_global.313
- ___block_literal_global.330
- ___block_literal_global.360
- ___block_literal_global.366
- ___block_literal_global.372
- ___block_literal_global.377
- ___block_literal_global.405
- ___block_literal_global.426
- ___block_literal_global.462
- ___block_literal_global.471
- ___block_literal_global.476
- ___block_literal_global.477
- ___block_literal_global.543
- ___block_literal_global.546
- ___block_literal_global.553
- ___block_literal_global.555
- ___block_literal_global.566
- ___block_literal_global.568
- ___block_literal_global.570
- ___block_literal_global.572
- ___block_literal_global.574
- ___block_literal_global.576
- ___block_literal_global.640
- ___block_literal_global.645
- ___block_literal_global.771
- ___block_literal_global.990
- ___incomingCallStateChanged_block_invoke.1367
- __unnamed_array_storage.1071
- __unnamed_array_storage.1072
- __unnamed_array_storage.1084
- __unnamed_array_storage.1085
- __unnamed_array_storage.2399
- __unnamed_array_storage.2403
- __unnamed_array_storage.2404
- __unnamed_array_storage.351
- __unnamed_array_storage.355
- __unnamed_array_storage.356
- __unnamed_array_storage.361
- __unnamed_array_storage.362
- __unnamed_array_storage.364
- __unnamed_array_storage.367
- __unnamed_array_storage.368
- __unnamed_array_storage.493
- __unnamed_array_storage.758
- __unnamed_array_storage.759
- __unnamed_array_storage.998
CStrings:
+ "\x02\x17"
+ "@\"AccessibilityFeatureCache\""
+ "@24@0:8@\"NSCoder\"16"
+ "AXSecurePayFeatureCache"
+ "AccessibilityFeatureCache"
+ "Acquiring assertion for ax secure pay feature disablement"
+ "Error unarchiving data blob for secure pay: %@"
+ "NSCoding"
+ "NSSecureCoding"
+ "Processing secure pay ax features: %@"
+ "Release assertion for ax secure pay feature disablement"
+ "Secure pay ax feature assertion was held during SB startup - restoring features"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_assistiveTouch"
+ "TB,N,V_backTap"
+ "TB,N,V_liveCaptions"
+ "TB,N,V_liveSpeech"
+ "TB,N,V_speakScreen"
+ "TB,N,V_voiceControl"
+ "TB,N,V_zoom"
+ "TB,R"
+ "Unable to encode feature cache map: %@"
+ "_assistiveTouch"
+ "_axFeatureCache"
+ "_backTap"
+ "_liveCaptions"
+ "_liveSpeech"
+ "_restoreAccessibilityFeatureFromSecurePayCache:"
+ "_restoreSecurePayFeaturesIfNeeded"
+ "_setSecurePayAccessibilityFeaturesDisabled:"
+ "_speakScreen"
+ "_voiceControl"
+ "_zoom"
+ "assistiveTouch"
+ "backTap"
+ "com.apple.accessibility.feature.securepay"
+ "decodeBoolForKey:"
+ "encodeBool:forKey:"
+ "encodeWithCoder:"
+ "initWithCoder:"
+ "liveCaptions"
+ "liveSpeech"
+ "securePayAssertionActive"
+ "setAssistiveTouch:"
+ "setBackTap:"
+ "setLiveCaptions:"
+ "setLiveSpeech:"
+ "setSecurePayAccessibilityFeaturesDisabled:withServerInstance:"
+ "setSecurePayAssertionActive:"
+ "setSpeakScreen:"
+ "setVoiceControl:"
+ "setZoom:"
+ "speakScreen"
+ "supportsSecureCoding"
+ "v24@0:8@\"NSCoder\"16"
+ "voiceControl"
+ "zoom"
- "\x02\x16"
- "Attempt to copy contents into nil buffer pointer"
- "Can't unsafeBitCast between types of different sizes"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Insufficient space allocated to copy array contents"
- "Insufficient space allocated to copy string contents"
- "String index is out of bounds"
- "Swift/Array.swift"
- "Swift/Builtin.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "UnsafeRawBufferPointer with negative count"
- "invalid Collection: less than 'count' elements in collection"
- "invalid Collection: more than 'count' elements in collection"
- "newElements.underestimatedCount was an overestimate"

```
