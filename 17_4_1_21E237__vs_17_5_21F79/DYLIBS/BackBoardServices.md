## BackBoardServices

> `/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`

```diff

-599.124.0.0.0
-  __TEXT.__text: 0x64fc0
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x57d0
+599.328.0.0.0
+  __TEXT.__text: 0x665dc
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_methlist: 0x5980
   __TEXT.__const: 0x438
   __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__cstring: 0x97a3
-  __TEXT.__oslogstring: 0x1c77
+  __TEXT.__cstring: 0x9a45
+  __TEXT.__oslogstring: 0x1cd6
   __TEXT.__dlopen_cstrs: 0x18e
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x1800
-  __TEXT.__objc_classname: 0x1400
-  __TEXT.__objc_methname: 0xafbc
+  __TEXT.__unwind_info: 0x1858
+  __TEXT.__objc_classname: 0x1442
+  __TEXT.__objc_methname: 0xb20a
   __TEXT.__objc_methtype: 0x19dc
-  __TEXT.__objc_stubs: 0x6020
+  __TEXT.__objc_stubs: 0x6060
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x1460
-  __DATA_CONST.__objc_classlist: 0x420
+  __DATA_CONST.__const: 0x1490
+  __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9498
-  __DATA_CONST.__objc_selrefs: 0x2508
+  __DATA_CONST.__objc_const: 0x9798
+  __DATA_CONST.__objc_selrefs: 0x2578
   __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_classrefs: 0x520
-  __DATA_CONST.__objc_superrefs: 0x2d8
+  __DATA_CONST.__objc_classrefs: 0x530
+  __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__const: 0xfe8
-  __AUTH_CONST.__cfstring: 0x83c0
-  __AUTH_CONST.__objc_const: 0x3c30
+  __AUTH_CONST.__const: 0x1008
+  __AUTH_CONST.__cfstring: 0x85e0
+  __AUTH_CONST.__objc_const: 0x3d08
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x708
-  __AUTH.__objc_data: 0x1bd0
-  __DATA.__objc_ivar: 0x628
-  __DATA.__data: 0x10d8
-  __DATA.__bss: 0x2a8
+  __AUTH_CONST.__auth_got: 0x710
+  __AUTH.__objc_data: 0x1c70
+  __DATA.__objc_ivar: 0x64c
+  __DATA.__data: 0x10d0
+  __DATA.__bss: 0x250
   __DATA_DIRTY.__objc_data: 0xd70
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA_DIRTY.__bss: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 247549A6-F127-33CE-8487-1DBF8139A670
-  Functions: 2492
-  Symbols:   7821
-  CStrings:  4922
+  UUID: B48186A9-938B-3933-85AF-A8EA732A61E3
+  Functions: 2534
+  Symbols:   7929
+  CStrings:  5001
 
Symbols:
+ +[BKSHIDHapticFeedbackRequest build:]
+ +[BKSHIDHapticFeedbackRequest new]
+ +[BKSHIDHapticFeedbackRequest protobufSchema]
+ +[BKSHIDHapticFeedbackRequest supportsSecureCoding]
+ -[BKSHIDEventSmartCoverAttributes setWakeAnimationStyle:]
+ -[BKSHIDEventSmartCoverAttributes wakeAnimationStyle]
+ -[BKSHIDHapticFeedbackRequest .cxx_destruct]
+ -[BKSHIDHapticFeedbackRequest _initWithCopyOf:]
+ -[BKSHIDHapticFeedbackRequest _init]
+ -[BKSHIDHapticFeedbackRequest appendDescriptionToFormatter:]
+ -[BKSHIDHapticFeedbackRequest copyWithZone:]
+ -[BKSHIDHapticFeedbackRequest description]
+ -[BKSHIDHapticFeedbackRequest deviceType]
+ -[BKSHIDHapticFeedbackRequest encodeWithCoder:]
+ -[BKSHIDHapticFeedbackRequest hash]
+ -[BKSHIDHapticFeedbackRequest initForProtobufDecoding]
+ -[BKSHIDHapticFeedbackRequest initWithCoder:]
+ -[BKSHIDHapticFeedbackRequest init]
+ -[BKSHIDHapticFeedbackRequest isEqual:]
+ -[BKSHIDHapticFeedbackRequest mutableCopyWithZone:]
+ -[BKSHIDHapticFeedbackRequest pattern]
+ -[BKSHIDHapticFeedbackRequest powerSourceID]
+ -[BKSHIDHapticFeedbackRequest senderID]
+ -[BKSHIDHapticFeedbackRequest timestamp]
+ -[BKSMousePointerDevice setSupportsLightClick:]
+ -[BKSMousePointerDevice setSupportsSystemHaptics:]
+ -[BKSMousePointerDevice supportsLightClick]
+ -[BKSMousePointerDevice supportsSystemHaptics]
+ -[BKSMousePointerDevicePreferences clickHapticStrength]
+ -[BKSMousePointerDevicePreferences setClickHapticStrength:]
+ -[BKSMutableHIDHapticFeedbackRequest copyWithZone:]
+ -[BKSMutableHIDHapticFeedbackRequest setDeviceType:]
+ -[BKSMutableHIDHapticFeedbackRequest setPattern:]
+ -[BKSMutableHIDHapticFeedbackRequest setPowerSourceID:]
+ -[BKSMutableHIDHapticFeedbackRequest setSenderID:]
+ -[BKSMutableHIDHapticFeedbackRequest setTimestamp:]
+ GCC_except_table1002
+ GCC_except_table1012
+ GCC_except_table1159
+ GCC_except_table1265
+ GCC_except_table1356
+ GCC_except_table1365
+ GCC_except_table1468
+ GCC_except_table1560
+ GCC_except_table1562
+ GCC_except_table1609
+ GCC_except_table1666
+ GCC_except_table1785
+ GCC_except_table1880
+ GCC_except_table1887
+ GCC_except_table2108
+ GCC_except_table2119
+ GCC_except_table2364
+ GCC_except_table745
+ GCC_except_table746
+ GCC_except_table856
+ GCC_except_table876
+ GCC_except_table897
+ GCC_except_table998
+ _BKSHIDServicesRequestHapticFeedback
+ _IOHIDEventGetVendorDefinedData
+ _NSStringFromBKSHIDForceStageTransition
+ _NSStringFromBKSHIDHapticFeedbackRequestDeviceType
+ _NSStringFromBKSMousePointerDeviceClickHapticStrength
+ _OBJC_CLASS_$_BKSHIDHapticFeedbackRequest
+ _OBJC_CLASS_$_BKSMutableHIDHapticFeedbackRequest
+ _OBJC_IVAR_$_BKSHIDEventSmartCoverAttributes._wakeAnimationStyle
+ _OBJC_IVAR_$_BKSHIDHapticFeedbackRequest._deviceType
+ _OBJC_IVAR_$_BKSHIDHapticFeedbackRequest._pattern
+ _OBJC_IVAR_$_BKSHIDHapticFeedbackRequest._powerSourceID
+ _OBJC_IVAR_$_BKSHIDHapticFeedbackRequest._senderID
+ _OBJC_IVAR_$_BKSHIDHapticFeedbackRequest._timestamp
+ _OBJC_IVAR_$_BKSMousePointerDevice._supportsLightClick
+ _OBJC_IVAR_$_BKSMousePointerDevice._supportsSystemHaptics
+ _OBJC_IVAR_$_BKSMousePointerDevicePreferences._clickHapticStrength
+ _OBJC_METACLASS_$_BKSHIDHapticFeedbackRequest
+ _OBJC_METACLASS_$_BKSMutableHIDHapticFeedbackRequest
+ _QuartzCoreLibrary.8606
+ _QuartzCoreLibraryCore.frameworkLibrary.5474
+ _QuartzCoreLibraryCore.frameworkLibrary.6071
+ _QuartzCoreLibraryCore.frameworkLibrary.8620
+ __BKSHIDEventGetConciseDescriptionVendorDefinedForceStageEvent
+ __OBJC_$_CLASS_METHODS_BKSHIDHapticFeedbackRequest
+ __OBJC_$_CLASS_PROP_LIST_BKSHIDHapticFeedbackRequest
+ __OBJC_$_INSTANCE_METHODS_BKSHIDHapticFeedbackRequest
+ __OBJC_$_INSTANCE_METHODS_BKSMutableHIDHapticFeedbackRequest
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDHapticFeedbackRequest
+ __OBJC_$_PROP_LIST_BKSHIDHapticFeedbackRequest
+ __OBJC_$_PROP_LIST_BKSMutableHIDHapticFeedbackRequest
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDHapticFeedbackRequest
+ __OBJC_CLASS_RO_$_BKSHIDHapticFeedbackRequest
+ __OBJC_CLASS_RO_$_BKSMutableHIDHapticFeedbackRequest
+ __OBJC_METACLASS_RO_$_BKSHIDHapticFeedbackRequest
+ __OBJC_METACLASS_RO_$_BKSMutableHIDHapticFeedbackRequest
+ ___45+[BKSHIDHapticFeedbackRequest protobufSchema]_block_invoke
+ ___Block_byref_object_copy_.3221
+ ___Block_byref_object_copy_.3336
+ ___Block_byref_object_copy_.7035
+ ___Block_byref_object_copy_.9919
+ ___Block_byref_object_dispose_.3222
+ ___Block_byref_object_dispose_.3337
+ ___Block_byref_object_dispose_.7036
+ ___Block_byref_object_dispose_.9920
+ ___QuartzCoreLibraryCore_block_invoke.5475
+ ___QuartzCoreLibraryCore_block_invoke.6072
+ ___QuartzCoreLibraryCore_block_invoke.8621
+ ___block_literal_global.10180
+ ___block_literal_global.10355
+ ___block_literal_global.10488
+ ___block_literal_global.10707
+ ___block_literal_global.1120
+ ___block_literal_global.11295
+ ___block_literal_global.1302
+ ___block_literal_global.133.3669
+ ___block_literal_global.1434
+ ___block_literal_global.16.5393
+ ___block_literal_global.1758
+ ___block_literal_global.18.6246
+ ___block_literal_global.1885
+ ___block_literal_global.2.5804
+ ___block_literal_global.2.9434
+ ___block_literal_global.2127
+ ___block_literal_global.22.7242
+ ___block_literal_global.2336
+ ___block_literal_global.2776
+ ___block_literal_global.2856
+ ___block_literal_global.31.5406
+ ___block_literal_global.3219
+ ___block_literal_global.3364
+ ___block_literal_global.3502
+ ___block_literal_global.3735
+ ___block_literal_global.3913
+ ___block_literal_global.420
+ ___block_literal_global.4207
+ ___block_literal_global.4568
+ ___block_literal_global.4582
+ ___block_literal_global.5295
+ ___block_literal_global.5378
+ ___block_literal_global.5384
+ ___block_literal_global.5704
+ ___block_literal_global.5801
+ ___block_literal_global.62.2337
+ ___block_literal_global.6259
+ ___block_literal_global.6499
+ ___block_literal_global.6798
+ ___block_literal_global.6916
+ ___block_literal_global.709
+ ___block_literal_global.7092
+ ___block_literal_global.7261
+ ___block_literal_global.7471
+ ___block_literal_global.7708
+ ___block_literal_global.8415
+ ___block_literal_global.8597
+ ___block_literal_global.8688
+ ___block_literal_global.8816
+ ___block_literal_global.9.10712
+ ___block_literal_global.9208
+ ___block_literal_global.9437
+ ___block_literal_global.9704
+ ___block_literal_global.99.9907
+ ___block_literal_global.9953
+ ___getCADisplayClass_block_invoke.6070
+ _audit_stringQuartzCore.5490
+ _audit_stringQuartzCore.6084
+ _audit_stringQuartzCore.8624
+ _getCADisplayClass.6068
+ _getCADisplayClass.softClass.6069
+ _objc_msgSend$setClickHapticStrength:
+ _objc_msgSend$setWakeAnimationStyle:
+ _protobufSchema.onceToken.10485
+ _protobufSchema.onceToken.1117
+ _protobufSchema.onceToken.1879
+ _protobufSchema.onceToken.2125
+ _protobufSchema.onceToken.2492
+ _protobufSchema.onceToken.3499
+ _protobufSchema.onceToken.5702
+ _protobufSchema.onceToken.6497
+ _protobufSchema.onceToken.6913
+ _protobufSchema.onceToken.9695
+ _protobufSchema.schema.10486
+ _protobufSchema.schema.1118
+ _protobufSchema.schema.1880
+ _protobufSchema.schema.2126
+ _protobufSchema.schema.2493
+ _protobufSchema.schema.3500
+ _protobufSchema.schema.5703
+ _protobufSchema.schema.6498
+ _protobufSchema.schema.6914
+ _protobufSchema.schema.9696
+ _sharedInstance.__shared.9954
+ _sharedInstance.__sharedInstance.8416
+ _sharedInstance.controller.4583
+ _sharedInstance.onceToken.10354
+ _sharedInstance.onceToken.2775
+ _sharedInstance.onceToken.3363
+ _sharedInstance.onceToken.3734
+ _sharedInstance.onceToken.4567
+ _sharedInstance.onceToken.4581
+ _sharedInstance.onceToken.708
+ _sharedInstance.onceToken.7091
+ _sharedInstance.onceToken.8414
+ _sharedInstance.onceToken.9952
+ _sharedInstance.service.10356
+ _sharedInstance.service.3736
+ _sharedInstance.service.710
- GCC_except_table1005
- GCC_except_table1152
- GCC_except_table1258
- GCC_except_table1349
- GCC_except_table1358
- GCC_except_table1458
- GCC_except_table1550
- GCC_except_table1552
- GCC_except_table1599
- GCC_except_table1656
- GCC_except_table1775
- GCC_except_table1870
- GCC_except_table1877
- GCC_except_table2068
- GCC_except_table2079
- GCC_except_table2324
- GCC_except_table738
- GCC_except_table739
- GCC_except_table849
- GCC_except_table869
- GCC_except_table890
- GCC_except_table991
- GCC_except_table995
- _QuartzCoreLibrary.8560
- _QuartzCoreLibraryCore.frameworkLibrary.5486
- _QuartzCoreLibraryCore.frameworkLibrary.6048
- _QuartzCoreLibraryCore.frameworkLibrary.8572
- ___Block_byref_object_copy_.3217
- ___Block_byref_object_copy_.3331
- ___Block_byref_object_copy_.7004
- ___Block_byref_object_copy_.9668
- ___Block_byref_object_dispose_.3218
- ___Block_byref_object_dispose_.3332
- ___Block_byref_object_dispose_.7005
- ___Block_byref_object_dispose_.9669
- ___QuartzCoreLibraryCore_block_invoke.5487
- ___QuartzCoreLibraryCore_block_invoke.6049
- ___QuartzCoreLibraryCore_block_invoke.8573
- ___block_literal_global.10103
- ___block_literal_global.10236
- ___block_literal_global.10455
- ___block_literal_global.11047
- ___block_literal_global.1114
- ___block_literal_global.1296
- ___block_literal_global.133.3667
- ___block_literal_global.1430
- ___block_literal_global.16.5405
- ___block_literal_global.1761
- ___block_literal_global.18.6226
- ___block_literal_global.1888
- ___block_literal_global.2.5790
- ___block_literal_global.2.9187
- ___block_literal_global.2125
- ___block_literal_global.22.7208
- ___block_literal_global.2334
- ___block_literal_global.2775
- ___block_literal_global.2855
- ___block_literal_global.31.5418
- ___block_literal_global.3215
- ___block_literal_global.3359
- ___block_literal_global.3498
- ___block_literal_global.3734
- ___block_literal_global.3917
- ___block_literal_global.405
- ___block_literal_global.4210
- ___block_literal_global.4571
- ___block_literal_global.4585
- ___block_literal_global.5307
- ___block_literal_global.5390
- ___block_literal_global.5396
- ___block_literal_global.5703
- ___block_literal_global.5787
- ___block_literal_global.62.2335
- ___block_literal_global.6239
- ___block_literal_global.6476
- ___block_literal_global.6767
- ___block_literal_global.6885
- ___block_literal_global.703
- ___block_literal_global.7061
- ___block_literal_global.7227
- ___block_literal_global.7433
- ___block_literal_global.7669
- ___block_literal_global.8369
- ___block_literal_global.8551
- ___block_literal_global.8640
- ___block_literal_global.8961
- ___block_literal_global.9.10460
- ___block_literal_global.9190
- ___block_literal_global.9454
- ___block_literal_global.9701
- ___block_literal_global.99.9656
- ___block_literal_global.9928
- ___getCADisplayClass_block_invoke.6047
- _audit_stringQuartzCore.5498
- _audit_stringQuartzCore.6061
- _audit_stringQuartzCore.8576
- _getCADisplayClass.6045
- _getCADisplayClass.softClass.6046
- _protobufSchema.onceToken.10233
- _protobufSchema.onceToken.1111
- _protobufSchema.onceToken.1882
- _protobufSchema.onceToken.2123
- _protobufSchema.onceToken.2491
- _protobufSchema.onceToken.3495
- _protobufSchema.onceToken.5700
- _protobufSchema.onceToken.6474
- _protobufSchema.onceToken.6882
- _protobufSchema.onceToken.9445
- _protobufSchema.schema.10234
- _protobufSchema.schema.1112
- _protobufSchema.schema.1883
- _protobufSchema.schema.2124
- _protobufSchema.schema.2492
- _protobufSchema.schema.3496
- _protobufSchema.schema.5701
- _protobufSchema.schema.6475
- _protobufSchema.schema.6883
- _protobufSchema.schema.9446
- _sharedInstance.__shared.9702
- _sharedInstance.__sharedInstance.8370
- _sharedInstance.controller.4586
- _sharedInstance.onceToken.10102
- _sharedInstance.onceToken.2774
- _sharedInstance.onceToken.3358
- _sharedInstance.onceToken.3733
- _sharedInstance.onceToken.4570
- _sharedInstance.onceToken.4584
- _sharedInstance.onceToken.702
- _sharedInstance.onceToken.7060
- _sharedInstance.onceToken.8368
- _sharedInstance.onceToken.9700
- _sharedInstance.service.10104
- _sharedInstance.service.3735
- _sharedInstance.service.704
CStrings:
+ "\x01!"
+ " clickHapticStrength:%d"
+ " supportsLightClick:%d supportsSystemHaptics:%d"
+ "%@ phase:%@"
+ "+[BKSHIDHapticFeedbackRequest new]"
+ "-[BKSHIDHapticFeedbackRequest init]"
+ "<corrupt data>"
+ "BKSHIDHapticFeedbackRequest"
+ "BKSHIDHapticFeedbackRequest cannot be subclassed"
+ "BKSHIDHapticFeedbackRequest.m"
+ "BKSMutableHIDHapticFeedbackRequest"
+ "BKSqueezeForSystemShortcutEnabled"
+ "Error encoding haptic feedback request: %{public}@"
+ "Error sending haptic feedback request: 0x%x"
+ "Force:%f stage:%u"
+ "T@\"NSNumber\",&,D,N"
+ "T@\"NSNumber\",R,N"
+ "TB,D,N,GisSqueezeForSystemShortcutEnabled"
+ "TB,N,V_supportsLightClick"
+ "TB,N,V_supportsSystemHaptics"
+ "Ti,N,V_wakeAnimationStyle"
+ "Tq,N,V_clickHapticStrength"
+ "_clickHapticStrength"
+ "_deviceType"
+ "_pattern"
+ "_powerSourceID"
+ "_supportsLightClick"
+ "_supportsSystemHaptics"
+ "_wakeAnimationStyle"
+ "cannot directly allocate BKSHIDHapticFeedbackRequest"
+ "clickHapticStrength"
+ "deviceType"
+ "pattern"
+ "pencil"
+ "powerSourceID"
+ "request"
+ "setClickHapticStrength:"
+ "setDeviceType:"
+ "setPattern:"
+ "setPowerSourceID:"
+ "setSupportsLightClick:"
+ "setSupportsSystemHaptics:"
+ "setWakeAnimationStyle:"
+ "squeeze"
+ "squeezeForSystemShortcutEnabled"
+ "supportsLightClick"
+ "supportsSystemHaptics"
+ "t:9"
+ "void BKSHIDServicesRequestHapticFeedback(BKSHIDHapticFeedbackRequest *__strong _Nonnull)"
+ "wakeAnimationStyle"

```
