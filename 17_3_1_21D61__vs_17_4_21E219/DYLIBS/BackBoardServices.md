## BackBoardServices

> `/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`

```diff

-598.50.0.0.0
-  __TEXT.__text: 0x61ff4
-  __TEXT.__auth_stubs: 0xdc0
-  __TEXT.__objc_methlist: 0x55e8
-  __TEXT.__const: 0x428
-  __TEXT.__gcc_except_tab: 0x2e4
-  __TEXT.__cstring: 0x8fc1
-  __TEXT.__oslogstring: 0x1c3b
-  __TEXT.__dlopen_cstrs: 0x143
+599.124.0.0.0
+  __TEXT.__text: 0x64fc0
+  __TEXT.__auth_stubs: 0xdf0
+  __TEXT.__objc_methlist: 0x57d0
+  __TEXT.__const: 0x438
+  __TEXT.__gcc_except_tab: 0x368
+  __TEXT.__cstring: 0x97a3
+  __TEXT.__oslogstring: 0x1c77
+  __TEXT.__dlopen_cstrs: 0x18e
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x1750
-  __TEXT.__objc_classname: 0x1337
-  __TEXT.__objc_methname: 0xac60
-  __TEXT.__objc_methtype: 0x1940
-  __TEXT.__objc_stubs: 0x5d00
+  __TEXT.__unwind_info: 0x1800
+  __TEXT.__objc_classname: 0x1400
+  __TEXT.__objc_methname: 0xafbc
+  __TEXT.__objc_methtype: 0x19dc
+  __TEXT.__objc_stubs: 0x6020
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x1310
-  __DATA_CONST.__objc_classlist: 0x400
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__const: 0x1460
+  __DATA_CONST.__objc_classlist: 0x420
+  __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9108
-  __DATA_CONST.__objc_selrefs: 0x2438
+  __DATA_CONST.__objc_const: 0x9498
+  __DATA_CONST.__objc_selrefs: 0x2508
+  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_classrefs: 0x520
+  __DATA_CONST.__objc_superrefs: 0x2d8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__const: 0xee8
-  __AUTH_CONST.__cfstring: 0x81e0
-  __AUTH_CONST.__objc_const: 0x3a38
+  __AUTH_CONST.__const: 0xfe8
+  __AUTH_CONST.__cfstring: 0x83c0
+  __AUTH_CONST.__objc_const: 0x3c30
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__auth_got: 0x6f0
-  __AUTH.__objc_data: 0x1a90
-  __DATA.__objc_protorefs: 0x80
-  __DATA.__objc_classrefs: 0x4f8
-  __DATA.__objc_superrefs: 0x2c0
-  __DATA.__objc_ivar: 0x608
-  __DATA.__data: 0xfa8
-  __DATA.__bss: 0x208
+  __AUTH_CONST.__auth_got: 0x708
+  __AUTH.__objc_data: 0x1bd0
+  __DATA.__objc_ivar: 0x628
+  __DATA.__data: 0x10d8
+  __DATA.__bss: 0x2a8
   __DATA_DIRTY.__objc_data: 0xd70
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0xf8
+  __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2417
-  Symbols:   7555
-  CStrings:  3781
+  Functions: 2492
+  Symbols:   7821
+  CStrings:  3868
 
Symbols:
+ +[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]
+ +[BKSHIDEventSenderDescriptor stylusOpaqueTouchDigitizer]
+ +[BKSHIDEventSmartCoverAttributes protobufSchema]
+ +[BKSProximityDetectionMaskChangeEvent build:]
+ +[BKSProximityDetectionMaskChangeEvent new]
+ +[BKSProximityDetectionMaskChangeEvent supportsSecureCoding]
+ +[BKSProximitySensorService sharedInstance]
+ +[BKSWindowServerHitTestSecurityAnalysis securityAnalysisFromCAHitTestDictionary:errorString:]
+ -[BKSHIDEventKeyCommand _appendKeyWithoutModifiersToDescriptionTarget:keyCodeString:]
+ -[BKSHIDEventKeyCommand appendDescriptionToStream:]
+ -[BKSHIDEventSmartCoverAttributes appendDescriptionToFormatter:]
+ -[BKSHIDEventSmartCoverAttributes copyWithZone:]
+ -[BKSHIDEventSmartCoverAttributes isEqual:]
+ -[BKSHIDEventSmartCoverAttributes setSmartCoverState:]
+ -[BKSHIDEventSmartCoverAttributes smartCoverState]
+ -[BKSMutableProximityEvent copyWithZone:]
+ -[BKSMutableProximityEvent setDetectionMask:]
+ -[BKSMutableProximityEvent setMode:]
+ -[BKSMutableProximityEvent setTimestamp:]
+ -[BKSProximityDetectionMaskChangeEvent _initWithCopyOf:]
+ -[BKSProximityDetectionMaskChangeEvent _init]
+ -[BKSProximityDetectionMaskChangeEvent appendDescriptionToFormatter:]
+ -[BKSProximityDetectionMaskChangeEvent copyWithZone:]
+ -[BKSProximityDetectionMaskChangeEvent description]
+ -[BKSProximityDetectionMaskChangeEvent detectionMask]
+ -[BKSProximityDetectionMaskChangeEvent encodeWithCoder:]
+ -[BKSProximityDetectionMaskChangeEvent hash]
+ -[BKSProximityDetectionMaskChangeEvent initWithCoder:]
+ -[BKSProximityDetectionMaskChangeEvent init]
+ -[BKSProximityDetectionMaskChangeEvent isEqual:]
+ -[BKSProximityDetectionMaskChangeEvent mode]
+ -[BKSProximityDetectionMaskChangeEvent mutableCopyWithZone:]
+ -[BKSProximityDetectionMaskChangeEvent timestamp]
+ -[BKSProximitySensorService .cxx_destruct]
+ -[BKSProximitySensorService _connectToRemoteServiceIfNeeded]
+ -[BKSProximitySensorService _init]
+ -[BKSProximitySensorService addObserver:forReason:]
+ -[BKSProximitySensorService proximityDetectionMaskDidChange:]
+ GCC_except_table1005
+ GCC_except_table1152
+ GCC_except_table1258
+ GCC_except_table1349
+ GCC_except_table1358
+ GCC_except_table1458
+ GCC_except_table1550
+ GCC_except_table1552
+ GCC_except_table1599
+ GCC_except_table1656
+ GCC_except_table1775
+ GCC_except_table1870
+ GCC_except_table1877
+ GCC_except_table2068
+ GCC_except_table2079
+ GCC_except_table2324
+ GCC_except_table265
+ GCC_except_table738
+ GCC_except_table739
+ GCC_except_table849
+ GCC_except_table869
+ GCC_except_table890
+ GCC_except_table991
+ GCC_except_table995
+ _BKLogHapticFeedback
+ _BKLogHapticFeedback.__logObj
+ _BKLogHapticFeedback.onceToken
+ _BKNSStringFromIOHIDGenericGestureType
+ _BKSDisplayServicesNotifyDisplayBlanked
+ _BKSHIDEventGetSmartCoverAttributes
+ _BKSHIDEventSetSmartCoverAttributes
+ _BKSHIDEventSetSmartCoverInfo
+ _BKSHIDServicesNotifyBacklightFactorWithFadeDurationAsync
+ _BKSProximitySensorBSServiceName
+ _OBJC_CLASS_$_BKSHIDEventSmartCoverAttributes
+ _OBJC_CLASS_$_BKSMutableProximityEvent
+ _OBJC_CLASS_$_BKSProximityDetectionMaskChangeEvent
+ _OBJC_CLASS_$_BKSProximitySensorService
+ _OBJC_CLASS_$_BSDescriptionStyle
+ _OBJC_IVAR_$_BKSHIDEventSmartCoverAttributes._smartCoverState
+ _OBJC_IVAR_$_BKSProximityDetectionMaskChangeEvent._detectionMask
+ _OBJC_IVAR_$_BKSProximityDetectionMaskChangeEvent._mode
+ _OBJC_IVAR_$_BKSProximityDetectionMaskChangeEvent._timestamp
+ _OBJC_IVAR_$_BKSProximitySensorService._calloutQueue
+ _OBJC_IVAR_$_BKSProximitySensorService._connection
+ _OBJC_IVAR_$_BKSProximitySensorService._lock_observingDetectionMaskChanges
+ _OBJC_IVAR_$_BKSProximitySensorService._observers
+ _OBJC_METACLASS_$_BKSHIDEventSmartCoverAttributes
+ _OBJC_METACLASS_$_BKSMutableProximityEvent
+ _OBJC_METACLASS_$_BKSProximityDetectionMaskChangeEvent
+ _OBJC_METACLASS_$_BKSProximitySensorService
+ _QuartzCoreLibrary.8560
+ _QuartzCoreLibraryCore.frameworkLibrary.5486
+ _QuartzCoreLibraryCore.frameworkLibrary.6048
+ _QuartzCoreLibraryCore.frameworkLibrary.8572
+ __BKSDisplayNotifySetDisplayBlanked
+ __BKSDisplayServicesNotifySetDisplayBlanked
+ __BKSHIDNotifySetBacklightFactorWithFadeDurationAsync
+ __BKSHIDRequestHapticFeedback
+ __OBJC_$_CLASS_METHODS_BKSHIDEventSmartCoverAttributes
+ __OBJC_$_CLASS_METHODS_BKSProximityDetectionMaskChangeEvent
+ __OBJC_$_CLASS_METHODS_BKSProximitySensorService
+ __OBJC_$_CLASS_PROP_LIST_BKSProximityDetectionMaskChangeEvent
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventSmartCoverAttributes
+ __OBJC_$_INSTANCE_METHODS_BKSMutableProximityEvent
+ __OBJC_$_INSTANCE_METHODS_BKSProximityDetectionMaskChangeEvent
+ __OBJC_$_INSTANCE_METHODS_BKSProximitySensorService
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventSmartCoverAttributes
+ __OBJC_$_INSTANCE_VARIABLES_BKSProximityDetectionMaskChangeEvent
+ __OBJC_$_INSTANCE_VARIABLES_BKSProximitySensorService
+ __OBJC_$_PROP_LIST_BKSHIDEventSmartCoverAttributes
+ __OBJC_$_PROP_LIST_BKSMutableProximityEvent
+ __OBJC_$_PROP_LIST_BKSProximityDetectionMaskChangeEvent
+ __OBJC_$_PROP_LIST_BKSProximitySensorService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSProximitySensorClient_IPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSProximitySensorServer_IPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSDescriptionStreaming
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSProximitySensorClient_IPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSProximitySensorServer_IPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSDescriptionStreaming
+ __OBJC_$_PROTOCOL_REFS_BKSProximitySensorClient_IPC
+ __OBJC_$_PROTOCOL_REFS_BKSProximitySensorServer_IPC
+ __OBJC_$_PROTOCOL_REFS_BSDescriptionStreaming
+ __OBJC_CLASS_PROTOCOLS_$_BKSProximityDetectionMaskChangeEvent
+ __OBJC_CLASS_PROTOCOLS_$_BKSProximitySensorService
+ __OBJC_CLASS_RO_$_BKSHIDEventSmartCoverAttributes
+ __OBJC_CLASS_RO_$_BKSMutableProximityEvent
+ __OBJC_CLASS_RO_$_BKSProximityDetectionMaskChangeEvent
+ __OBJC_CLASS_RO_$_BKSProximitySensorService
+ __OBJC_LABEL_PROTOCOL_$_BKSProximitySensorClient_IPC
+ __OBJC_LABEL_PROTOCOL_$_BKSProximitySensorServer_IPC
+ __OBJC_LABEL_PROTOCOL_$_BSDescriptionStreaming
+ __OBJC_METACLASS_RO_$_BKSHIDEventSmartCoverAttributes
+ __OBJC_METACLASS_RO_$_BKSMutableProximityEvent
+ __OBJC_METACLASS_RO_$_BKSProximityDetectionMaskChangeEvent
+ __OBJC_METACLASS_RO_$_BKSProximitySensorService
+ __OBJC_PROTOCOL_$_BKSProximitySensorClient_IPC
+ __OBJC_PROTOCOL_$_BKSProximitySensorServer_IPC
+ __OBJC_PROTOCOL_$_BSDescriptionStreaming
+ __OBJC_PROTOCOL_REFERENCE_$_BKSProximitySensorClient_IPC
+ __OBJC_PROTOCOL_REFERENCE_$_BKSProximitySensorServer_IPC
+ ___34-[BKSProximitySensorService _init]_block_invoke
+ ___34-[BKSProximitySensorService _init]_block_invoke_2
+ ___41-[BKSTouchEventService _connectToService]_block_invoke.88
+ ___41-[BKSTouchEventService _connectToService]_block_invoke.90
+ ___49+[BKSHIDEventSmartCoverAttributes protobufSchema]_block_invoke
+ ___49+[BKSHIDEventSmartCoverAttributes protobufSchema]_block_invoke_2
+ ___49-[BKSHIDEventKeyCommand _appendPropertiesCommon:]_block_invoke
+ ___57+[BKSHIDEventSenderDescriptor stylusOpaqueTouchDigitizer]_block_invoke
+ ___57+[BKSHIDEventSenderDescriptor stylusOpaqueTouchDigitizer]_block_invoke_2
+ ___57-[BKSSystemShellControlService _activateServerConnection]_block_invoke.51
+ ___57-[BKSSystemShellControlService _activateServerConnection]_block_invoke.55
+ ___60-[BKSProximitySensorService _connectToRemoteServiceIfNeeded]_block_invoke
+ ___60-[BKSProximitySensorService _connectToRemoteServiceIfNeeded]_block_invoke.58
+ ___60-[BKSProximitySensorService _connectToRemoteServiceIfNeeded]_block_invoke.60
+ ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke
+ ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke_2
+ ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke_3
+ ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke_4
+ ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke_5
+ ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke_6
+ ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke_7
+ ___62-[BKSMutableHIDEventDiscreteDispatchingPredicate setDisplays:]_block_invoke.152
+ ___65-[BKSMutableHIDEventKeyCommandsDispatchingPredicate setDisplays:]_block_invoke.123
+ ___68-[BKSTouchDeliveryObservationService _connectToTouchDeliveryService]_block_invoke.72
+ ___72-[BKSSystemShellService _activateServerConnectionWithIdleSleepInterval:]_block_invoke.70
+ ___72-[BKSSystemShellService _activateServerConnectionWithIdleSleepInterval:]_block_invoke.72
+ ___72-[BKSTouchDeliveryObservationService observeTouchEventDeliveryDidOccur:]_block_invoke.84
+ ___94+[BKSWindowServerHitTestSecurityAnalysis securityAnalysisFromCAHitTestDictionary:errorString:]_block_invoke
+ ___BKLogHapticFeedback_block_invoke
+ ___Block_byref_object_copy_.3217
+ ___Block_byref_object_copy_.3331
+ ___Block_byref_object_copy_.7004
+ ___Block_byref_object_copy_.9668
+ ___Block_byref_object_dispose_.3218
+ ___Block_byref_object_dispose_.3332
+ ___Block_byref_object_dispose_.7005
+ ___Block_byref_object_dispose_.9669
+ ___QuartzCoreLibraryCore_block_invoke.5487
+ ___QuartzCoreLibraryCore_block_invoke.6049
+ ___QuartzCoreLibraryCore_block_invoke.8573
+ ___block_descriptor_32_e35_v16?0"BSMutableDescriptionStyle"8l
+ ___block_descriptor_32_e44_"<NSCopying>"16?0"BKSHIDEventKeyCommand"8l
+ ___block_descriptor_40_e8_32s_e43_v16?0"<BSDescriptionStringAppendTarget>"8ls32l8
+ ___block_descriptor_40_e8_32s_e8_v16?08ls32l8
+ ___block_descriptor_48_e8_32s40s_e21_v24?0"NSNumber"816ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e43_v16?0"<BSDescriptionStringAppendTarget>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e43_v16?0"<BSDescriptionStringAppendTarget>"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s_e55_v16?0"BKSMutableWindowServerHitTestSecurityAnalysis"8ls32l8
+ ___block_literal_global.10103
+ ___block_literal_global.10236
+ ___block_literal_global.10455
+ ___block_literal_global.110
+ ___block_literal_global.11047
+ ___block_literal_global.1114
+ ___block_literal_global.112
+ ___block_literal_global.119
+ ___block_literal_global.123
+ ___block_literal_global.126
+ ___block_literal_global.1296
+ ___block_literal_global.133.3667
+ ___block_literal_global.1430
+ ___block_literal_global.148
+ ___block_literal_global.155
+ ___block_literal_global.16.5405
+ ___block_literal_global.165
+ ___block_literal_global.171
+ ___block_literal_global.175
+ ___block_literal_global.1761
+ ___block_literal_global.18.6226
+ ___block_literal_global.180
+ ___block_literal_global.186
+ ___block_literal_global.1888
+ ___block_literal_global.2.5790
+ ___block_literal_global.2.9187
+ ___block_literal_global.2125
+ ___block_literal_global.22.7208
+ ___block_literal_global.2334
+ ___block_literal_global.2494
+ ___block_literal_global.273
+ ___block_literal_global.2775
+ ___block_literal_global.283
+ ___block_literal_global.2855
+ ___block_literal_global.3055
+ ___block_literal_global.31.5418
+ ___block_literal_global.3215
+ ___block_literal_global.3359
+ ___block_literal_global.3498
+ ___block_literal_global.3734
+ ___block_literal_global.3917
+ ___block_literal_global.395
+ ___block_literal_global.405
+ ___block_literal_global.4210
+ ___block_literal_global.4571
+ ___block_literal_global.4585
+ ___block_literal_global.509
+ ___block_literal_global.52
+ ___block_literal_global.5307
+ ___block_literal_global.5390
+ ___block_literal_global.5396
+ ___block_literal_global.54
+ ___block_literal_global.57
+ ___block_literal_global.5703
+ ___block_literal_global.5787
+ ___block_literal_global.615
+ ___block_literal_global.62
+ ___block_literal_global.62.2335
+ ___block_literal_global.6239
+ ___block_literal_global.633
+ ___block_literal_global.6476
+ ___block_literal_global.651
+ ___block_literal_global.6767
+ ___block_literal_global.68
+ ___block_literal_global.6885
+ ___block_literal_global.69
+ ___block_literal_global.703
+ ___block_literal_global.7061
+ ___block_literal_global.7227
+ ___block_literal_global.7433
+ ___block_literal_global.75
+ ___block_literal_global.7669
+ ___block_literal_global.8369
+ ___block_literal_global.8551
+ ___block_literal_global.8640
+ ___block_literal_global.8961
+ ___block_literal_global.9.10460
+ ___block_literal_global.9190
+ ___block_literal_global.92
+ ___block_literal_global.9454
+ ___block_literal_global.9701
+ ___block_literal_global.99.9656
+ ___block_literal_global.9928
+ ___getCADisplayClass_block_invoke.6047
+ ___getkCAWindowServerHitTestSecurityAnalysisCumulativeLayerTransformSymbolLoc_block_invoke
+ ___getkCAWindowServerHitTestSecurityAnalysisCumulativeOpacitySymbolLoc_block_invoke
+ ___getkCAWindowServerHitTestSecurityAnalysisIsInsecureFilteredSymbolLoc_block_invoke
+ ___getkCAWindowServerHitTestSecurityAnalysisOcclusionPercentSymbolLoc_block_invoke
+ ___getkCAWindowServerHitTestSecurityAnalysisOcclusionTypeSymbolLoc_block_invoke
+ ___getkCAWindowServerHitTestSecurityAnalysisParentsHaveInsecureLayerPropertiesSymbolLoc_block_invoke
+ ___getkCAWindowServerOcclusionTypeBorderSymbolLoc_block_invoke
+ ___getkCAWindowServerOcclusionTypeClippedSymbolLoc_block_invoke
+ ___getkCAWindowServerOcclusionTypeLayerSymbolLoc_block_invoke
+ _audit_stringQuartzCore.5498
+ _audit_stringQuartzCore.6061
+ _audit_stringQuartzCore.8576
+ _dispatch_queue_create
+ _dlerror
+ _dlsym
+ _getCADisplayClass.6045
+ _getCADisplayClass.softClass.6046
+ _getkCAWindowServerHitTestSecurityAnalysisCumulativeLayerTransformSymbolLoc.ptr
+ _getkCAWindowServerHitTestSecurityAnalysisCumulativeOpacitySymbolLoc.ptr
+ _getkCAWindowServerHitTestSecurityAnalysisIsInsecureFilteredSymbolLoc.ptr
+ _getkCAWindowServerHitTestSecurityAnalysisOcclusionPercentSymbolLoc.ptr
+ _getkCAWindowServerHitTestSecurityAnalysisOcclusionTypeSymbolLoc.ptr
+ _getkCAWindowServerHitTestSecurityAnalysisParentsHaveInsecureLayerPropertiesSymbolLoc.ptr
+ _getkCAWindowServerOcclusionTypeBorderSymbolLoc.ptr
+ _getkCAWindowServerOcclusionTypeClippedSymbolLoc.ptr
+ _getkCAWindowServerOcclusionTypeLayerSymbolLoc.ptr
+ _objc_msgSend$CATransform3DValue
+ _objc_msgSend$_appendKeyWithoutModifiersToDescriptionTarget:keyCodeString:
+ _objc_msgSend$_connectToRemoteServiceIfNeeded
+ _objc_msgSend$appendCustomFormatForValue:withCustomFormatForName:
+ _objc_msgSend$appendDictionary:withName:itemBlock:
+ _objc_msgSend$appendInt64:withName:
+ _objc_msgSend$bs_dictionaryByPartitioning:
+ _objc_msgSend$clientInformation
+ _objc_msgSend$floatValue
+ _objc_msgSend$initWithString:
+ _objc_msgSend$overlayStyle:block:
+ _objc_msgSend$proximityDetectionMaskDidChange:
+ _objc_msgSend$proximitySensorDetectionMaskDidChange:
+ _objc_msgSend$setClientInformation:
+ _objc_msgSend$setCollectionLineBreak:
+ _objc_msgSend$setCumulativeLayerTransform:
+ _objc_msgSend$setCumulativeOpacity:
+ _objc_msgSend$setHasInsecureFilter:
+ _objc_msgSend$setObservesProximitySensorDetectionMaskChanges:
+ _objc_msgSend$setOcclusionMask:
+ _objc_msgSend$setOcclusionPercentage:
+ _objc_msgSend$setOcclusionType:
+ _objc_msgSend$setParentsHaveInsecureLayerProperties:
+ _objc_msgSend$setSmartCoverState:
+ _objc_msgSend$smartCoverState
+ _protobufSchema.onceToken.10233
+ _protobufSchema.onceToken.1111
+ _protobufSchema.onceToken.184
+ _protobufSchema.onceToken.1882
+ _protobufSchema.onceToken.2123
+ _protobufSchema.onceToken.2491
+ _protobufSchema.onceToken.271
+ _protobufSchema.onceToken.281
+ _protobufSchema.onceToken.3495
+ _protobufSchema.onceToken.393
+ _protobufSchema.onceToken.507
+ _protobufSchema.onceToken.5700
+ _protobufSchema.onceToken.613
+ _protobufSchema.onceToken.631
+ _protobufSchema.onceToken.6474
+ _protobufSchema.onceToken.649
+ _protobufSchema.onceToken.6882
+ _protobufSchema.onceToken.9445
+ _protobufSchema.schema.10234
+ _protobufSchema.schema.1112
+ _protobufSchema.schema.183
+ _protobufSchema.schema.1883
+ _protobufSchema.schema.2124
+ _protobufSchema.schema.2492
+ _protobufSchema.schema.270
+ _protobufSchema.schema.280
+ _protobufSchema.schema.3496
+ _protobufSchema.schema.392
+ _protobufSchema.schema.506
+ _protobufSchema.schema.5701
+ _protobufSchema.schema.612
+ _protobufSchema.schema.630
+ _protobufSchema.schema.6475
+ _protobufSchema.schema.648
+ _protobufSchema.schema.6883
+ _protobufSchema.schema.9446
+ _sharedInstance.__shared.9702
+ _sharedInstance.__sharedInstance.8370
+ _sharedInstance.controller.4586
+ _sharedInstance.onceToken.10102
+ _sharedInstance.onceToken.2774
+ _sharedInstance.onceToken.3358
+ _sharedInstance.onceToken.3733
+ _sharedInstance.onceToken.4570
+ _sharedInstance.onceToken.4584
+ _sharedInstance.onceToken.702
+ _sharedInstance.onceToken.7060
+ _sharedInstance.onceToken.8368
+ _sharedInstance.onceToken.9700
+ _sharedInstance.service.10104
+ _sharedInstance.service.3735
+ _sharedInstance.service.704
+ _stylusOpaqueTouchDigitizer.descriptor
+ _stylusOpaqueTouchDigitizer.onceToken
- -[BKSHIDEventKeyCommand appendDescriptionToFormatter:]
- GCC_except_table1120
- GCC_except_table1226
- GCC_except_table1315
- GCC_except_table1324
- GCC_except_table1424
- GCC_except_table1516
- GCC_except_table1518
- GCC_except_table1565
- GCC_except_table1622
- GCC_except_table1741
- GCC_except_table1997
- GCC_except_table2008
- GCC_except_table2250
- GCC_except_table255
- GCC_except_table708
- GCC_except_table709
- GCC_except_table819
- GCC_except_table837
- GCC_except_table858
- GCC_except_table959
- GCC_except_table963
- GCC_except_table973
- _BKSHIDEventSetSmartCoverState
- _QuartzCoreLibraryCore.frameworkLibrary.5341
- _QuartzCoreLibraryCore.frameworkLibrary.5910
- __BKSDisplaySetDisplayBlanked
- __BKSHIDSetBacklightFactorWithFadeDurationAsync
- ___41-[BKSTouchEventService _connectToService]_block_invoke.87
- ___41-[BKSTouchEventService _connectToService]_block_invoke.89
- ___57-[BKSSystemShellControlService _activateServerConnection]_block_invoke.50
- ___57-[BKSSystemShellControlService _activateServerConnection]_block_invoke.54
- ___62-[BKSMutableHIDEventDiscreteDispatchingPredicate setDisplays:]_block_invoke.151
- ___65-[BKSMutableHIDEventKeyCommandsDispatchingPredicate setDisplays:]_block_invoke.122
- ___68-[BKSTouchDeliveryObservationService _connectToTouchDeliveryService]_block_invoke.70
- ___72-[BKSSystemShellService _activateServerConnectionWithIdleSleepInterval:]_block_invoke.69
- ___72-[BKSSystemShellService _activateServerConnectionWithIdleSleepInterval:]_block_invoke.71
- ___72-[BKSTouchDeliveryObservationService observeTouchEventDeliveryDidOccur:]_block_invoke.83
- ___Block_byref_object_copy_.3131
- ___Block_byref_object_copy_.3242
- ___Block_byref_object_copy_.6856
- ___Block_byref_object_copy_.9365
- ___Block_byref_object_dispose_.3132
- ___Block_byref_object_dispose_.3243
- ___Block_byref_object_dispose_.6857
- ___Block_byref_object_dispose_.9366
- ___QuartzCoreLibraryCore_block_invoke.5342
- ___QuartzCoreLibraryCore_block_invoke.5911
- ___block_literal_global.10152
- ___block_literal_global.107
- ___block_literal_global.10738
- ___block_literal_global.109
- ___block_literal_global.1173
- ___block_literal_global.118
- ___block_literal_global.124.8566
- ___block_literal_global.125
- ___block_literal_global.133.3574
- ___block_literal_global.1352
- ___block_literal_global.147
- ___block_literal_global.1485
- ___block_literal_global.154
- ___block_literal_global.16.5262
- ___block_literal_global.164
- ___block_literal_global.170
- ___block_literal_global.174
- ___block_literal_global.18.6083
- ___block_literal_global.1805
- ___block_literal_global.185
- ___block_literal_global.1930
- ___block_literal_global.2.5645
- ___block_literal_global.2.8889
- ___block_literal_global.2148
- ___block_literal_global.22.7070
- ___block_literal_global.2416
- ___block_literal_global.2694
- ___block_literal_global.272
- ___block_literal_global.2772
- ___block_literal_global.282
- ___block_literal_global.2968
- ___block_literal_global.31.5275
- ___block_literal_global.3129
- ___block_literal_global.3270
- ___block_literal_global.3408
- ___block_literal_global.3638
- ___block_literal_global.3813
- ___block_literal_global.394
- ___block_literal_global.398
- ___block_literal_global.4095
- ___block_literal_global.4454
- ___block_literal_global.4468
- ___block_literal_global.508
- ___block_literal_global.5164
- ___block_literal_global.5247
- ___block_literal_global.5253
- ___block_literal_global.53
- ___block_literal_global.5558
- ___block_literal_global.56
- ___block_literal_global.5642
- ___block_literal_global.6096
- ___block_literal_global.614
- ___block_literal_global.632
- ___block_literal_global.6329
- ___block_literal_global.6621
- ___block_literal_global.6738
- ___block_literal_global.6915
- ___block_literal_global.7089
- ___block_literal_global.7297
- ___block_literal_global.73
- ___block_literal_global.7536
- ___block_literal_global.760
- ___block_literal_global.8097
- ___block_literal_global.8275
- ___block_literal_global.8346
- ___block_literal_global.8667
- ___block_literal_global.8892
- ___block_literal_global.9.10157
- ___block_literal_global.91
- ___block_literal_global.9154
- ___block_literal_global.9400
- ___block_literal_global.9626
- ___block_literal_global.98.9353
- ___block_literal_global.9801
- ___block_literal_global.9933
- ___getCADisplayClass_block_invoke.5909
- _audit_stringQuartzCore.5354
- _audit_stringQuartzCore.5920
- _getCADisplayClass.5907
- _getCADisplayClass.softClass.5908
- _protobufSchema.onceToken.1170
- _protobufSchema.onceToken.183
- _protobufSchema.onceToken.1924
- _protobufSchema.onceToken.2146
- _protobufSchema.onceToken.2413
- _protobufSchema.onceToken.270
- _protobufSchema.onceToken.280
- _protobufSchema.onceToken.3405
- _protobufSchema.onceToken.392
- _protobufSchema.onceToken.506
- _protobufSchema.onceToken.5555
- _protobufSchema.onceToken.612
- _protobufSchema.onceToken.630
- _protobufSchema.onceToken.6327
- _protobufSchema.onceToken.6735
- _protobufSchema.onceToken.9144
- _protobufSchema.onceToken.9930
- _protobufSchema.schema.1171
- _protobufSchema.schema.182
- _protobufSchema.schema.1925
- _protobufSchema.schema.2147
- _protobufSchema.schema.2414
- _protobufSchema.schema.269
- _protobufSchema.schema.279
- _protobufSchema.schema.3406
- _protobufSchema.schema.391
- _protobufSchema.schema.505
- _protobufSchema.schema.5556
- _protobufSchema.schema.611
- _protobufSchema.schema.629
- _protobufSchema.schema.6328
- _protobufSchema.schema.6736
- _protobufSchema.schema.9145
- _protobufSchema.schema.9931
- _sharedInstance.__shared.9401
- _sharedInstance.__sharedInstance.8098
- _sharedInstance.controller.4469
- _sharedInstance.onceToken.2693
- _sharedInstance.onceToken.3269
- _sharedInstance.onceToken.3637
- _sharedInstance.onceToken.4453
- _sharedInstance.onceToken.4467
- _sharedInstance.onceToken.6914
- _sharedInstance.onceToken.759
- _sharedInstance.onceToken.8096
- _sharedInstance.onceToken.9399
- _sharedInstance.onceToken.9800
- _sharedInstance.service.3639
- _sharedInstance.service.761
- _sharedInstance.service.9802
CStrings:
+ "%@ count:%d phase:%@"
+ "%@ progress:%g phase:%@"
+ "+[BKSProximityDetectionMaskChangeEvent new]"
+ "-[BKSProximityDetectionMaskChangeEvent init]"
+ "@\"<NSCopying>\"16@?0@\"BKSHIDEventKeyCommand\"8"
+ "@\"BKSProximityDetectionMaskChangeEvent\"24@0:8@\"NSNumber\"16"
+ "@32@0:8@16^@24"
+ "BKProximitySensor"
+ "BKSHIDEventSmartCoverAttributes"
+ "BKSMutableProximityEvent"
+ "BKSProximityDetectionMaskChangeEvent"
+ "BKSProximityDetectionMaskChangeEvent cannot be subclassed"
+ "BKSProximityDetectionMaskChangeEvent.m"
+ "BKSProximitySensorClient_IPC"
+ "BKSProximitySensorServer_IPC"
+ "BKSProximitySensorService"
+ "BKSProximitySensorService observers"
+ "BKSProximitySensorService.m"
+ "BSDescriptionStreaming"
+ "CATransform3DValue"
+ "HapticFeedback"
+ "NSString *getkCAWindowServerHitTestSecurityAnalysisCumulativeLayerTransform(void)"
+ "NSString *getkCAWindowServerHitTestSecurityAnalysisCumulativeOpacity(void)"
+ "NSString *getkCAWindowServerHitTestSecurityAnalysisIsInsecureFiltered(void)"
+ "NSString *getkCAWindowServerHitTestSecurityAnalysisOcclusionPercent(void)"
+ "NSString *getkCAWindowServerHitTestSecurityAnalysisOcclusionType(void)"
+ "NSString *getkCAWindowServerHitTestSecurityAnalysisParentsHaveInsecureLayerProperties(void)"
+ "NSString *getkCAWindowServerOcclusionTypeBorder(void)"
+ "NSString *getkCAWindowServerOcclusionTypeClipped(void)"
+ "NSString *getkCAWindowServerOcclusionTypeLayer(void)"
+ "T@\"NSString\",?,R,C"
+ "Ti,N,V_smartCoverState"
+ "Vv24@0:8@\"BKSProximityDetectionMaskChangeEvent\"16"
+ "_appendKeyWithoutModifiersToDescriptionTarget:keyCodeString:"
+ "_connectToRemoteServiceIfNeeded"
+ "_descriptionForKeyCommandCollection:"
+ "_detectionMask"
+ "_lock_observingDetectionMaskChanges"
+ "_observers"
+ "_smartCoverState"
+ "addObserver:forReason:"
+ "appendCustomFormatForValue:withCustomFormatForName:"
+ "appendDescriptionToStream:"
+ "appendDictionary:withName:itemBlock:"
+ "appendInt64:withName:"
+ "backboardd must be going down, sounds like fun"
+ "backboardd-attr-cache-15000309"
+ "bs_dictionaryByPartitioning:"
+ "cannot directly allocate BKSProximityDetectionMaskChangeEvent"
+ "clientInformation"
+ "collection must be an NSSet, NSArray, or NSOrderedSet"
+ "com.apple.backboardd.BKSProximitySensorService"
+ "detectionMask"
+ "floatValue"
+ "initWithString:"
+ "kCAWindowServerHitTestSecurityAnalysisCumulativeLayerTransform"
+ "kCAWindowServerHitTestSecurityAnalysisCumulativeOpacity"
+ "kCAWindowServerHitTestSecurityAnalysisIsInsecureFiltered"
+ "kCAWindowServerHitTestSecurityAnalysisOcclusionPercent"
+ "kCAWindowServerHitTestSecurityAnalysisOcclusionType"
+ "kCAWindowServerHitTestSecurityAnalysisParentsHaveInsecureLayerProperties"
+ "kCAWindowServerOcclusionTypeBorder"
+ "kCAWindowServerOcclusionTypeClipped"
+ "kCAWindowServerOcclusionTypeLayer"
+ "no classes other than BKSHIDEventSmartCoverAttributes allowed, not even %@"
+ "occlusionType is unexpected class:%@"
+ "occlusionTypeMask is %X, but there is no percentage"
+ "overlayStyle:block:"
+ "proximityDetectionMaskDidChange:"
+ "proximitySensorDetectionMaskDidChange:"
+ "securityAnalysisFromCAHitTestDictionary:errorString:"
+ "service interruption -- attempting to reactivate"
+ "setClientInformation:"
+ "setCollectionLineBreak:"
+ "setDetectionMask:"
+ "setObservesProximitySensorDetectionMaskChanges:"
+ "setSmartCoverState:"
+ "setTimestamp:"
+ "skipModifiers"
+ "smartCoverState"
+ "stylusOpaqueTouchDigitizer"
+ "swipe"
+ "v16@?0@\"BKSMutableWindowServerHitTestSecurityAnalysis\"8"
+ "v16@?0@\"BSMutableDescriptionStyle\"8"
+ "v24@0:8@\"BSDescriptionStream\"16"
+ "v24@?0@\"NSNumber\"8@16"
+ "void BKSHIDEventSetSmartCoverAttributes(IOHIDEventRef, BKSHIDEventSmartCoverAttributes *__strong)"
- "Error: unknown smart cover state %X"
- "SmartCoverState: %d"
- "backboardd-attr-cache-15000100"
- "swipe progress:%g phase:%@"
- "tap count:%d phase:%@"

```
