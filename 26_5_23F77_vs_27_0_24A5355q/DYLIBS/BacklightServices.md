## BacklightServices

> `/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`

```diff

-5.4.2.0.0
-  __TEXT.__text: 0x28f3c
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x334c
+6.0.33.0.0
+  __TEXT.__text: 0x29974
+  __TEXT.__objc_methlist: 0x37bc
   __TEXT.__const: 0x138
-  __TEXT.__oslogstring: 0x27ef
-  __TEXT.__cstring: 0x19e1
-  __TEXT.__ustring: 0xf4
-  __TEXT.__gcc_except_tab: 0xde8
-  __TEXT.__unwind_info: 0x1000
-  __TEXT.__objc_classname: 0x108e
-  __TEXT.__objc_methname: 0x5fa4
-  __TEXT.__objc_methtype: 0x1249
-  __TEXT.__objc_stubs: 0x3e00
-  __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0xd80
-  __DATA_CONST.__objc_classlist: 0x338
+  __TEXT.__oslogstring: 0x2943
+  __TEXT.__cstring: 0x1b86
+  __TEXT.__ustring: 0xfe
+  __TEXT.__gcc_except_tab: 0xcb4
+  __TEXT.__unwind_info: 0x1058
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xdd0
+  __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0xf8
+  __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14c0
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__objc_selrefs: 0x1658
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x1a8
-  __AUTH_CONST.__auth_got: 0x4b8
-  __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x2200
-  __AUTH_CONST.__objc_const: 0x7958
-  __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0x2a8
-  __DATA.__data: 0xba8
-  __DATA.__bss: 0x109
-  __DATA_DIRTY.__objc_data: 0x1860
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_CONST.__objc_superrefs: 0x1b8
+  __DATA_CONST.__got: 0x400
+  __AUTH_CONST.__const: 0x5c0
+  __AUTH_CONST.__cfstring: 0x23e0
+  __AUTH_CONST.__objc_const: 0x8148
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x870
+  __DATA.__objc_ivar: 0x2e0
+  __DATA.__data: 0xc68
+  __DATA.__bss: 0xd9
+  __DATA_DIRTY.__objc_data: 0x1900
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
+  - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99EBF0A2-9CB6-308C-9E09-20163E0A9CCD
-  Functions: 1239
-  Symbols:   4548
-  CStrings:  2079
+  UUID: 6448F87B-7106-3887-B025-B4DC5014CF47
+  Functions: 1327
+  Symbols:   4789
+  CStrings:  795
 
Symbols:
+ +[BLSAssertionDescriptor highLuminanceSupportedByCoreBrightness]
+ +[BLSAssertionDescriptor setHighLuminanceSupportedByCoreBrightness:]
+ +[BLSBacklight backlightProxyForDisplay:]
+ +[BLSBacklight createBacklightProxyForDisplay:]
+ +[BLSBacklight createBacklightProxyForDisplay:].cold.1
+ +[BLSBacklight setBacklightProxy:forDisplay:]
+ +[BLSBacklight setBacklightProxy:forDisplay:].cold.1
+ +[BLSBacklight sharedBacklightForDisplay:]
+ +[BLSDisableLowPowerRenderingAttribute disableLowPowerRendering]
+ +[BLSDisplayAttribute attributeForDisplay:]
+ +[BLSDisplayAttribute supportsSecureCoding]
+ +[BLSDisplayReference displays]
+ +[BLSDisplayReference displays].cold.1
+ +[BLSDisplayReference referenceForAggregateDisplay]
+ +[BLSDisplayReference referenceForCADisplay:]
+ +[BLSDisplayReference referenceIdForCADisplay:]
+ +[BLSDisplayReference setDisplays:]
+ +[BLSDisplayReference supportsSecureCoding]
+ +[BLSLowPowerRenderingAttribute lowPowerRenderingForFBSScene:]
+ -[BLSAlwaysOnDateSpecifier initWithDate:fidelity:userObject:lowPowerRenderingPresentationTime:]
+ -[BLSAlwaysOnDateSpecifier lowPowerRenderingPresentationTime]
+ -[BLSAlwaysOnFrameSpecifier isLowPowerRendering]
+ -[BLSAlwaysOnFrameSpecifier lowPowerRenderingPresentationDate]
+ -[BLSAlwaysOnFrameSpecifier lowPowerRenderingPresentationTime]
+ -[BLSAlwaysOnFrameSpecifier setLowPowerRendering:]
+ -[BLSAlwaysOnFrameSpecifier setLowPowerRenderingPresentationTime:]
+ -[BLSAssertionDescriptor canAcquireForDisplay:]
+ -[BLSBacklight display]
+ -[BLSBacklight initForDisplay:]
+ -[BLSBacklightChangeEvent display]
+ -[BLSBacklightChangeEvent initWithEventID:state:previousState:wasTransitioning:changeRequest:display:]
+ -[BLSBacklightChangeEvent initWithXPCDictionary:].cold.2
+ -[BLSBacklightFBSSceneEnvironment lowPowerRenderingPresentationTime]
+ -[BLSBacklightFBSSceneEnvironment needsFlipbookStateUpdates]
+ -[BLSBacklightFBSSceneEnvironment needsLowPowerRenderingStateUpdates]
+ -[BLSBacklightFBSSceneEnvironment setNeedsFlipbookStateUpdates:]
+ -[BLSBacklightFBSSceneEnvironment setNeedsFlipbookStateUpdates:].cold.1
+ -[BLSBacklightFBSSceneEnvironment setNeedsLowPowerRenderingStateUpdates:]
+ -[BLSBacklightFBSSceneEnvironment setNeedsLowPowerRenderingStateUpdates:].cold.1
+ -[BLSBacklightSceneVisualState initWithActiveAppearance:updateFidelity:adjustedLuminance:dimmed:flipbook:]
+ -[BLSBacklightSceneVisualState initWithActiveAppearance:updateFidelity:adjustedLuminance:dimmed:flipbook:lowPowerRendering:]
+ -[BLSBacklightSceneVisualState isEqualToVisualStateIgnoringFlipbook:]
+ -[BLSBacklightSceneVisualState isEqualToVisualStateIgnoringFlipbookAndLowPowerRendering:]
+ -[BLSBacklightSceneVisualState isFlipbook]
+ -[BLSBacklightSceneVisualState isLowPowerRendering]
+ -[BLSBacklightSceneVisualState newVisualStateWithUpdateFidelity:flipbook:lowPowerRendering:]
+ -[BLSDiagnosticFlipbookFrame initWithPresentationTime:frameId:apl:aplDimming:memoryUsage:rawSurfaceFrameRect:inverted:specifier:uuid:lowPowerRendering:lowPowerRenderingPresentationTime:]
+ -[BLSDiagnosticFlipbookFrame lowPowerRenderingPresentationTime]
+ -[BLSDiagnosticFlipbookFrame lowPowerRendering]
+ -[BLSDisableLowPowerRenderingAttribute checkEntitlementSourceForRequiredEntitlements:error:]
+ -[BLSDisplayAttribute .cxx_destruct]
+ -[BLSDisplayAttribute copyWithZone:]
+ -[BLSDisplayAttribute description]
+ -[BLSDisplayAttribute display]
+ -[BLSDisplayAttribute encodeWithCoder:]
+ -[BLSDisplayAttribute encodeWithXPCDictionary:]
+ -[BLSDisplayAttribute hash]
+ -[BLSDisplayAttribute initForDisplay:]
+ -[BLSDisplayAttribute initWithCoder:]
+ -[BLSDisplayAttribute initWithXPCDictionary:]
+ -[BLSDisplayAttribute isEqual:]
+ -[BLSDisplayReference .cxx_destruct]
+ -[BLSDisplayReference copyWithZone:]
+ -[BLSDisplayReference description]
+ -[BLSDisplayReference doesMatchCADisplay:]
+ -[BLSDisplayReference encodeWithCoder:]
+ -[BLSDisplayReference encodeWithXPCDictionary:]
+ -[BLSDisplayReference hash]
+ -[BLSDisplayReference initWithBLSDisplay:]
+ -[BLSDisplayReference initWithCADisplay:]
+ -[BLSDisplayReference initWithCoder:]
+ -[BLSDisplayReference initWithReferenceId:loggingName:]
+ -[BLSDisplayReference initWithXPCDictionary:]
+ -[BLSDisplayReference init]
+ -[BLSDisplayReference isEqual:]
+ -[BLSDisplayReference loggingName]
+ -[BLSDisplayReference referenceId]
+ -[BLSPendingBacklightProxy display]
+ -[BLSXPCAssertionService displays]
+ -[BLSXPCBacklightProxy display]
+ -[BLSXPCBacklightProxy initForDisplay:]
+ -[BLSXPCBacklightProxy initWithEndpoint:display:]
+ -[BLSXPCBacklightProxy initWithEndpoint:display:].cold.1
+ -[BLSXPCBacklightProxy initWithEndpoint:display:].cold.2
+ -[FBSMutableSceneClientSettings(BacklightServices) bls_setNeedsFlipbookStateUpdates:]
+ -[FBSMutableSceneClientSettings(BacklightServices) bls_setNeedsLowPowerRenderingStateUpdates:]
+ -[FBSMutableSceneSettings(BacklightServicesInternal) bls_setLowPowerRenderingPresentationTime:]
+ -[FBSSceneClientSettings(BacklightServices) bls_needsFlipbookStateUpdates]
+ -[FBSSceneClientSettings(BacklightServices) bls_needsLowPowerRenderingStateUpdates]
+ -[FBSSceneSettings(BacklightServices) bls_lowPowerRenderingPresentationTime]
+ GCC_except_table12
+ GCC_except_table16
+ GCC_except_table55
+ _BLSDisableLowPowerRenderingAssertionEntitlement
+ _OBJC_CLASS_$_BLSDisableLowPowerRenderingAttribute
+ _OBJC_CLASS_$_BLSDisplayAttribute
+ _OBJC_CLASS_$_BLSDisplayReference
+ _OBJC_CLASS_$_BLSLowPowerRenderingAttribute
+ _OBJC_CLASS_$_BSServiceDispatchQueue
+ _OBJC_CLASS_$_BSServiceInitiatingConnection
+ _OBJC_CLASS_$_BSServiceInitiatingConnectionMultiplexer
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_IVAR_$_BLSAlwaysOnDateSpecifier._lowPowerRenderingPresentationTime
+ _OBJC_IVAR_$_BLSAlwaysOnFrameSpecifier._lowPowerRendering
+ _OBJC_IVAR_$_BLSAlwaysOnFrameSpecifier._lowPowerRenderingPresentationTime
+ _OBJC_IVAR_$_BLSAssertionDescriptor._lock
+ _OBJC_IVAR_$_BLSAssertionDescriptor._lock_displays
+ _OBJC_IVAR_$_BLSBacklight._display
+ _OBJC_IVAR_$_BLSBacklightChangeEvent._display
+ _OBJC_IVAR_$_BLSBacklightSceneVisualState._flipbook
+ _OBJC_IVAR_$_BLSBacklightSceneVisualState._lowPowerRendering
+ _OBJC_IVAR_$_BLSDiagnosticFlipbookFrame._lowPowerRendering
+ _OBJC_IVAR_$_BLSDiagnosticFlipbookFrame._lowPowerRenderingPresentationTime
+ _OBJC_IVAR_$_BLSDisplayAttribute._display
+ _OBJC_IVAR_$_BLSDisplayReference._loggingName
+ _OBJC_IVAR_$_BLSDisplayReference._referenceId
+ _OBJC_IVAR_$_BLSXPCBacklightProxy._display
+ _OBJC_METACLASS_$_BLSDisableLowPowerRenderingAttribute
+ _OBJC_METACLASS_$_BLSDisplayAttribute
+ _OBJC_METACLASS_$_BLSDisplayReference
+ _OBJC_METACLASS_$_BLSLowPowerRenderingAttribute
+ __OBJC_$_CLASS_METHODS_BLSDisableLowPowerRenderingAttribute
+ __OBJC_$_CLASS_METHODS_BLSDisplayAttribute
+ __OBJC_$_CLASS_METHODS_BLSDisplayReference
+ __OBJC_$_CLASS_METHODS_BLSLowPowerRenderingAttribute
+ __OBJC_$_CLASS_PROP_LIST_BLSDisplayReference
+ __OBJC_$_INSTANCE_METHODS_BLSDisableLowPowerRenderingAttribute
+ __OBJC_$_INSTANCE_METHODS_BLSDisplayAttribute
+ __OBJC_$_INSTANCE_METHODS_BLSDisplayReference
+ __OBJC_$_INSTANCE_VARIABLES_BLSDisplayAttribute
+ __OBJC_$_INSTANCE_VARIABLES_BLSDisplayReference
+ __OBJC_$_PROP_LIST_BLSDisplay
+ __OBJC_$_PROP_LIST_BLSDisplayAttribute
+ __OBJC_$_PROP_LIST_BLSDisplayReference
+ __OBJC_$_PROP_LIST_BLSDisplaySpecifying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSDisplay
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSDisplaySpecifying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSDisplay
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSDisplaySpecifying
+ __OBJC_$_PROTOCOL_REFS_BLSDisplay
+ __OBJC_$_PROTOCOL_REFS_BLSDisplaySpecifying
+ __OBJC_CLASS_PROTOCOLS_$_BLSDisplayAttribute
+ __OBJC_CLASS_PROTOCOLS_$_BLSDisplayReference
+ __OBJC_CLASS_RO_$_BLSDisableLowPowerRenderingAttribute
+ __OBJC_CLASS_RO_$_BLSDisplayAttribute
+ __OBJC_CLASS_RO_$_BLSDisplayReference
+ __OBJC_CLASS_RO_$_BLSLowPowerRenderingAttribute
+ __OBJC_LABEL_PROTOCOL_$_BLSDisplay
+ __OBJC_LABEL_PROTOCOL_$_BLSDisplaySpecifying
+ __OBJC_METACLASS_RO_$_BLSDisableLowPowerRenderingAttribute
+ __OBJC_METACLASS_RO_$_BLSDisplayAttribute
+ __OBJC_METACLASS_RO_$_BLSDisplayReference
+ __OBJC_METACLASS_RO_$_BLSLowPowerRenderingAttribute
+ __OBJC_PROTOCOL_$_BLSDisplay
+ __OBJC_PROTOCOL_$_BLSDisplaySpecifying
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEEPS2_EclB9fqe220100Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI26BLSTimelineEntryBookkeeperEEPS2_EclB9fqe220100Ev
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt3__114__split_bufferI24BLSTimelineEntryIteratorRNS_9allocatorIS1_EEE5clearB9fqe220100Ev
+ __ZNSt3__114__split_bufferI26BLSTimelineEntryBookkeeperRNS_9allocatorIS1_EEE17__destruct_at_endB9fqe220100EPS1_
+ __ZNSt3__116allocator_traitsINS_9allocatorI26BLSTimelineEntryBookkeeperEEE7destroyB9fqe220100IS2_Li0EEEvRS3_PT_
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEEPS3_EEED2B9fqe220100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI26BLSTimelineEntryBookkeeperEEPS3_EEED2B9fqe220100Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB9fqe220100INS_9allocatorI24BLSTimelineEntryIteratorEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB9fqe220100INS_9allocatorI26BLSTimelineEntryBookkeeperEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE16__destroy_vectorclB9fqe220100Ev
+ __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE16__destroy_vectorclB9fqe220100Ev
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE22__base_destruct_at_endB9fqe220100EPS1_
+ __ZNSt3__19allocatorI24BLSTimelineEntryIteratorE17allocate_at_leastB9fqe220100Em
+ __ZNSt3__19allocatorI26BLSTimelineEntryBookkeeperE17allocate_at_leastB9fqe220100Em
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ ___34-[BLSDisplayAttribute description]_block_invoke
+ ___34-[BLSDisplayReference description]_block_invoke
+ ___35-[BLSDiagnostics initWithEndpoint:]_block_invoke_4
+ ___40-[BLSBacklightSceneVisualState isEqual:]_block_invoke_5
+ ___40-[BLSBacklightSceneVisualState isEqual:]_block_invoke_6
+ ___43-[BLSXPCAssertionService initWithEndpoint:]_block_invoke_4
+ ___49-[BLSXPCBacklightProxy initWithEndpoint:display:]_block_invoke
+ ___49-[BLSXPCBacklightProxy initWithEndpoint:display:]_block_invoke_2
+ ___49-[BLSXPCBacklightProxy initWithEndpoint:display:]_block_invoke_3
+ ___49-[BLSXPCBacklightProxy initWithEndpoint:display:]_block_invoke_4
+ ___49-[BLSXPCBacklightProxy initWithEndpoint:display:]_block_invoke_5
+ ___64-[BLSBacklightFBSSceneEnvironment setNeedsFlipbookStateUpdates:]_block_invoke
+ ___73-[BLSBacklightFBSSceneEnvironment setNeedsLowPowerRenderingStateUpdates:]_block_invoke
+ ___90-[BLSAlwaysOnFrequencyPerMinuteTimeline unconfiguredEntriesForDateInterval:previousEntry:]_block_invoke.58
+ ___NSStringFromBLSBacklightChangeEvents_block_invoke.67
+ ___NSStringFromBLSBacklightChangeEvents_block_invoke_2.68
+ ___block_descriptor_32_e48_v16?0"<BSServiceConnectionInitiatingOptions>"8l
+ ___block_descriptor_32_e67_v16?0"BSServiceInitiatingConnection<BSServiceConnectionContext>"8l
+ ___block_descriptor_40_e8_32s_e25_v16?0"<BSXPCEncoding>"8ls32l8
+ ___block_descriptor_40_e8_32s_e48_v16?0"<BSServiceConnectionInitiatingOptions>"8ls32l8
+ ___block_descriptor_40_e8_32s_e52_v16?0"<BSServiceInitiatingConnectionConfiguring>"8ls32l8
+ ___block_descriptor_40_e8_32w_e67_v16?0"BSServiceInitiatingConnection<BSServiceConnectionContext>"8lw32l8
+ ___block_descriptor_48_e8_32s40w_e52_v16?0"<BSServiceInitiatingConnectionConfiguring>"8ls32l8w40l8
+ ___block_descriptor_56_e8_32s40s48w_e52_v16?0"<BSServiceInitiatingConnectionConfiguring>"8ls32l8s40l8w48l8
+ ___block_literal_global.103
+ ___block_literal_global.207
+ ___block_literal_global.30
+ ___block_literal_global.48
+ ___block_literal_global.50
+ ___block_literal_global.78
+ ___block_literal_global.92
+ __class_displays
+ __highLuminanceSupportedByCB
+ __lock_backlightsByDisplayId
+ __lock_proxiesByDisplayId
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$assertBarrierOnQueue
+ _objc_msgSend$bls_lowPowerRenderingPresentationTime
+ _objc_msgSend$bls_needsFlipbookStateUpdates
+ _objc_msgSend$bls_needsLowPowerRenderingStateUpdates
+ _objc_msgSend$bls_setNeedsFlipbookStateUpdates:
+ _objc_msgSend$bls_setNeedsLowPowerRenderingStateUpdates:
+ _objc_msgSend$configure:
+ _objc_msgSend$connectionSeed
+ _objc_msgSend$defaultMultiplexer
+ _objc_msgSend$dictionary
+ _objc_msgSend$display
+ _objc_msgSend$displayId
+ _objc_msgSend$displays
+ _objc_msgSend$encodeContext:
+ _objc_msgSend$initForDisplay:
+ _objc_msgSend$initWithActiveAppearance:updateFidelity:adjustedLuminance:dimmed:flipbook:
+ _objc_msgSend$initWithActiveAppearance:updateFidelity:adjustedLuminance:dimmed:flipbook:lowPowerRendering:
+ _objc_msgSend$initWithBLSDisplay:
+ _objc_msgSend$initWithCADisplay:
+ _objc_msgSend$initWithDate:fidelity:userObject:lowPowerRenderingPresentationTime:
+ _objc_msgSend$initWithEndpoint:options:
+ _objc_msgSend$initWithEventID:state:previousState:wasTransitioning:changeRequest:display:
+ _objc_msgSend$initWithPresentationTime:frameId:apl:aplDimming:memoryUsage:rawSurfaceFrameRect:inverted:specifier:uuid:lowPowerRendering:lowPowerRenderingPresentationTime:
+ _objc_msgSend$initWithReferenceId:loggingName:
+ _objc_msgSend$isFlipbook
+ _objc_msgSend$isLowPowerRendering
+ _objc_msgSend$loggingName
+ _objc_msgSend$lowPowerRendering
+ _objc_msgSend$lowPowerRenderingPresentationTime
+ _objc_msgSend$name
+ _objc_msgSend$performAsync:
+ _objc_msgSend$queueWithName:serviceQuality:
+ _objc_msgSend$referenceForAggregateDisplay
+ _objc_msgSend$referenceId
+ _objc_msgSend$referenceIdForCADisplay:
+ _objc_msgSend$setMultiplexer:
+ _objc_msgSend$sharedBacklight
+ _objc_msgSend$sharedBacklightForDisplay:
+ _objc_msgSend$userInteractiveMultiplexer
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x8
- +[BLSBacklight defaultBacklightProxy]
- +[BLSBacklight setDefaultBacklightProxy:]
- +[BLSBacklight setDefaultBacklightProxy:].cold.1
- -[BLSDiagnosticFlipbookFrame initWithPresentationTime:frameId:apl:aplDimming:memoryUsage:rawSurfaceFrameRect:inverted:specifier:uuid:]
- -[BLSXPCBacklightProxy initWithEndpoint:]
- -[BLSXPCBacklightProxy initWithEndpoint:].cold.1
- -[BLSXPCBacklightProxy initWithEndpoint:].cold.2
- -[BLSXPCBacklightProxy init]
- GCC_except_table31
- GCC_except_table54
- GCC_except_table58
- GCC_except_table59
- GCC_except_table60
- _BSDispatchQueueCreate
- _OBJC_CLASS_$_BSDispatchQueueAttributes
- _OBJC_CLASS_$_BSServiceConnection
- _OBJC_IVAR_$_BLSXPCBacklightProxy._callbackQueue
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEEPS2_EclB9nqe210106Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI26BLSTimelineEntryBookkeeperEEPS2_EclB9nqe210106Ev
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__114__split_bufferI24BLSTimelineEntryIteratorRNS_9allocatorIS1_EEE5clearB9nqe210106Ev
- __ZNSt3__114__split_bufferI26BLSTimelineEntryBookkeeperRNS_9allocatorIS1_EEE17__destruct_at_endB9nqe210106EPS1_
- __ZNSt3__116allocator_traitsINS_9allocatorI26BLSTimelineEntryBookkeeperEEE7destroyB9nqe210106IS2_Li0EEEvRS3_PT_
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEEPS3_EEED2B9nqe210106Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI26BLSTimelineEntryBookkeeperEEPS3_EEED2B9nqe210106Ev
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorI24BLSTimelineEntryIteratorEEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorI26BLSTimelineEntryBookkeeperEEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE22__base_destruct_at_endB9nqe210106EPS1_
- __ZNSt3__19allocatorI24BLSTimelineEntryIteratorE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI26BLSTimelineEntryBookkeeperE17allocate_at_leastB9nqe210106Em
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- ___31+[BLSBacklight sharedBacklight]_block_invoke
- ___41-[BLSXPCBacklightProxy initWithEndpoint:]_block_invoke
- ___41-[BLSXPCBacklightProxy initWithEndpoint:]_block_invoke_2
- ___41-[BLSXPCBacklightProxy initWithEndpoint:]_block_invoke_3
- ___90-[BLSAlwaysOnFrequencyPerMinuteTimeline unconfiguredEntriesForDateInterval:previousEntry:]_block_invoke.59
- ___NSStringFromBLSBacklightChangeEvents_block_invoke.70
- ___NSStringFromBLSBacklightChangeEvents_block_invoke_2.71
- ___block_descriptor_32_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8l
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32w_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8lw32l8
- ___block_descriptor_48_e8_32s40s_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48w_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8s40l8w48l8
- ___block_descriptor_64_e8_32s40s48s56w_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8s40l8s48l8w56l8
- ___block_literal_global.104
- ___block_literal_global.187
- ___block_literal_global.25
- ___block_literal_global.39
- ___block_literal_global.41
- ___block_literal_global.79
- ___block_literal_global.93
- __defaultBacklightProxy
- _dispatch_assert_queue$V2
- _objc_msgSend$configureConnection:
- _objc_msgSend$connectionWithEndpoint:
- _objc_msgSend$initWithPresentationTime:frameId:apl:aplDimming:memoryUsage:rawSurfaceFrameRect:inverted:specifier:uuid:
- _objc_msgSend$relativePriority
- _objc_msgSend$serial
- _objc_msgSend$serviceClass
- _objc_msgSend$serviceClass:relativePriority:
- _objc_msgSend$setServiceQuality:
- _objc_msgSend$setTargetQueue:
- _objc_retain_x28
- _sharedBacklight.__sharedBacklight
- _sharedBacklight.onceToken
CStrings:
+ "%@ is not a BLSDisplayReference"
+ "%p did activate connection:%{public}@ for endpoint:%{public}@ display:%{public}@"
+ "%p setNeedsFlipbookStateUpdates:%{BOOL}u for environment:%{public}@"
+ "%p setNeedsLowPowerRenderingStateUpdates:%{BOOL}u for environment:%{public}@"
+ "2"
+ "BLSBacklight.m"
+ "BLSBacklightProxy backlightProxy reset for display %{public}@ - should only occur during unit testing"
+ "BLSBacklightProxy setBacklightProxy:forDisplay: replacing nil for display %{public}@ - no backlight instances created prior to server bringup - yay"
+ "LCD∅"
+ "LPR"
+ "attempting to replace backlightProxy:%@ which is not a BLSPendingBacklightProxy"
+ "com.apple.BacklightServices.Diagnostics"
+ "com.apple.BacklightServices.XPCAssertionService"
+ "com.apple.BacklightServices.XPCProxy"
+ "com.apple.backlight.disable_low_power_rendering_assertion"
+ "display"
+ "displays method prior to service start"
+ "dspl"
+ "dspl missing from encoding: %@"
+ "flp"
+ "lowPowerRendering"
+ "lowPowerRenderingPresentationTime"
+ "lpr"
+ "lprTime"
+ "name"
+ "v16@?0@\"<BSServiceConnectionInitiatingOptions>\"8"
+ "v16@?0@\"<BSServiceInitiatingConnectionConfiguring>\"8"
+ "v16@?0@\"<BSXPCEncoding>\"8"
+ "v16@?0@\"BSServiceInitiatingConnection<BSServiceConnectionContext>\"8"
+ "\x81"
+ "∅LCD∅"
+ "∑LCD"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<BLSAssertionService>\""
- "@\"<BLSBacklightFBSSceneEnvironmentDiffActionDelegate>\""
- "@\"<BLSBacklightProxy>\""
- "@\"<BLSBacklightSceneEnvironment>\""
- "@\"<BLSBacklightSceneEnvironmentDelegate>\""
- "@\"<BLSBacklightSceneEnvironmentDelegate>\"16@0:8"
- "@\"<BLSBacklightSceneEnvironmentUpdating>\""
- "@\"<BLSBacklightSceneEnvironmentUpdating>\"16@0:8"
- "@\"<BLSBacklightSceneEnvironment_Private>\""
- "@\"<BLSDiagnosticFlipbookFrameSurfaceProvider>\""
- "@\"<BLSPresentationDateSpecifying>\"16@0:8"
- "@\"<NSObject>\""
- "@\"<NSObject><NSCopying>\""
- "@\"BLSAlwaysOnDateSpecifier\""
- "@\"BLSAlwaysOnDateSpecifier\"16@0:8"
- "@\"BLSAlwaysOnFrameSpecifier\""
- "@\"BLSAlwaysOnFrameSpecifier\"16@0:8"
- "@\"BLSAlwaysOnSession\""
- "@\"BLSAlwaysOnSession\"16@0:8"
- "@\"BLSAlwaysOnTimelineEntry\""
- "@\"BLSAssertionAcquisitionObserver\""
- "@\"BLSAssertionDescriptor\""
- "@\"BLSAssertionDescriptor\"16@0:8"
- "@\"BLSAssertionIdentifier\""
- "@\"BLSAssertionIdentifier\"16@0:8"
- "@\"BLSAssertionIdentifier\"32@0:8@\"BLSAssertionDescriptor\"16o^@24"
- "@\"BLSBacklightChangeEvent\""
- "@\"BLSBacklightChangeRequest\""
- "@\"BLSBacklightChangeSourceEventMetadata\""
- "@\"BLSBacklightSceneSettingsDiffInspector\""
- "@\"BLSBacklightSceneUpdateContext\""
- "@\"BLSBacklightSceneVisualState\""
- "@\"BLSBacklightSceneVisualState\"16@0:8"
- "@\"BLSDiagnosticFlipbookFrame\"16@0:8"
- "@\"BLSDiagnosticFlipbookFrame\"24@0:8@\"NSUUID\"16"
- "@\"BLSDiagnosticPresentationDateSpecifier\""
- "@\"BLSFrameSpecifierModel\""
- "@\"BSServiceConnection\""
- "@\"FBSScene\""
- "@\"FBSSceneIdentityToken\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray<__BLSDiagnosticFlipbookFrame__>\"16@0:8"
- "@\"NSCalendar\""
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSDateInterval\""
- "@\"NSEnumerator\""
- "@\"NSError\"24@0:8@\"BLSBacklightChangeRequest\"16"
- "@\"NSHashTable\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableSet\""
- "@\"NSNumber\"16@0:8"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSUUID\"16@0:8"
- "@100@0:8Q16Q24f32f36Q40{CGRect={CGPoint=dd}{CGSize=dd}}48B80@84@92"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8#16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSObject<OS_xpc_object>\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8B16B20"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@24@0:8q16"
- "@28@0:8I16r*20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16o^@24"
- "@32@0:8@16q24"
- "@32@0:8Q16Q24"
- "@32@0:8i16i20Q24"
- "@32@0:8q16@?24"
- "@32@0:8{CGPoint=dd}16"
- "@36@0:8@16B24@28"
- "@36@0:8d16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16q24@32"
- "@40@0:8B16B20B24B28B32B36"
- "@40@0:8q16@24@?32"
- "@40@0:8q16q24q32"
- "@44@0:8@16@24B32@?36"
- "@44@0:8@16B24B28B32@?36"
- "@44@0:8@16d24@32B40"
- "@44@0:8@16q24B32@36"
- "@44@0:8q16q24q32B40"
- "@48@0:8Q16q24q32@40"
- "@48@0:8d16@24@32@?40"
- "@52@0:8@16@24B32d36@44"
- "@52@0:8Q16q24q32B40@44"
- "@56@0:8@16@24@32B40@44B52"
- "@56@0:8q16@24Q32q40@48"
- "@60@0:8@16q24B32d36@44@52"
- "@92@0:8@16@24@32@40B48@52B60B64@?68@?76@?84"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B32@0:8@16d24"
- "B32@0:8@16o^@24"
- "B40@0:8@16@24d32"
- "B40@0:8@16@24o^@32"
- "B40@0:8@16d24^d32"
- "BLS1HzFlipbookAttribute"
- "BLSAlwaysFillFlipbookAttribute"
- "BLSAlwaysOnDateSpecifier"
- "BLSAlwaysOnExplicitEntriesTimeline"
- "BLSAlwaysOnFrameSpecifier"
- "BLSAlwaysOnFrequencyPerMinuteTimeline"
- "BLSAlwaysOnPeriodicTimeline"
- "BLSAlwaysOnSession"
- "BLSAlwaysOnTimeline"
- "BLSAlwaysOnTimelineEntry"
- "BLSAlwaysOnTimelineEntrySpecifier"
- "BLSAlwaysOnTimelineUnconfiguredEntry"
- "BLSAsserting"
- "BLSAssertion"
- "BLSAssertionAcquisitionObserver"
- "BLSAssertionDescriptor"
- "BLSAssertionIdentifier"
- "BLSAssertionObserving"
- "BLSAssertionService"
- "BLSAssertionServiceResponding"
- "BLSAttribute"
- "BLSBacklight"
- "BLSBacklightChangeEvent"
- "BLSBacklightChangeRequest"
- "BLSBacklightChangeRequestable"
- "BLSBacklightChangeSourceEventDisplayLongPressMetadata"
- "BLSBacklightChangeSourceEventDisplaySwipeMetadata"
- "BLSBacklightChangeSourceEventDisplayTapMetadata"
- "BLSBacklightChangeSourceEventMetadata"
- "BLSBacklightChangeSourceEventSuppressionMetadata"
- "BLSBacklightFBSSceneEnvironment"
- "BLSBacklightFBSSceneEnvironmentActionHandler"
- "BLSBacklightFBSSceneEnvironmentDiffAction"
- "BLSBacklightFBSSceneEnvironmentDiffActionDelegate"
- "BLSBacklightFBSSceneEnvironmentDiffActionNullDelegate"
- "BLSBacklightProxy"
- "BLSBacklightProxy defaultBacklightProxy reset - should only occur during unit testing"
- "BLSBacklightProxy setDefaultBacklightProxy replacing nil - no backlight instances created prior to server bringup - yay"
- "BLSBacklightSceneClientSettings"
- "BLSBacklightSceneEnvironment"
- "BLSBacklightSceneEnvironmentUpdater"
- "BLSBacklightSceneEnvironmentUpdating"
- "BLSBacklightSceneEnvironment_Private"
- "BLSBacklightSceneSettings"
- "BLSBacklightSceneSettingsDiffInspector"
- "BLSBacklightSceneUpdate"
- "BLSBacklightSceneUpdateAction"
- "BLSBacklightSceneUpdateAnimationCompleteAction"
- "BLSBacklightSceneUpdateBacklightRampAction"
- "BLSBacklightSceneUpdateBacklightRampResponse"
- "BLSBacklightSceneUpdateContext"
- "BLSBacklightSceneVisualState"
- "BLSBacklightStateObservable"
- "BLSCacheFlipbookOnDisplayWakeAttribute"
- "BLSCancelWhenBacklightInactivatesAttribute"
- "BLSDesiredFidelityAction"
- "BLSDesiredFidelityRequest"
- "BLSDesiredFidelityResponse"
- "BLSDiagnosticEnvironmentDateSpecifier"
- "BLSDiagnosticFlipbookFrame"
- "BLSDiagnosticFlipbookFrameSurfaceProvider"
- "BLSDiagnosticPresentationDateSpecifier"
- "BLSDiagnostics"
- "BLSDiagnosticsXPCHostInterface"
- "BLSDiagnosticsXPCServiceSpecification"
- "BLSDisableAlwaysOnAttribute"
- "BLSDisableAlwaysOnHoldGestureAttribute"
- "BLSDisableAlwaysOnHoldThroughAttribute"
- "BLSDisableAlwaysOnSwipeGestureAttribute"
- "BLSDisableAlwaysOnSwipeThroughAttribute"
- "BLSDisableAlwaysOnTapThroughAttribute"
- "BLSDisableBacklightWatchdogsAttribute"
- "BLSDisableCommitOnWakeMeasurementAttribute"
- "BLSDisableCrownRotateToWakeAttribute"
- "BLSDisableFlipbookAttribute"
- "BLSDisableInactiveTapGestureAttribute"
- "BLSDisableLongCoverGestureAttribute"
- "BLSDisableLowerGestureAttribute"
- "BLSDisableRaiseGestureAttribute"
- "BLSDurationAttribute"
- "BLSEnableCoverGestureAttribute"
- "BLSEnvironmentDateSpecifying"
- "BLSFidelityThreshold"
- "BLSFlipbookDiagnosticsProviding"
- "BLSForceActiveAttribute"
- "BLSFrameSpecifiersRequest"
- "BLSFrameSpecifiersRequestAction"
- "BLSFrameSpecifiersRequestResponse"
- "BLSGlobal1HzFlipbookAttribute"
- "BLSGlobalCacheFlipbookOnDisplayWakeAttribute"
- "BLSGlobalHighLuminanceAlwaysOnAttribute"
- "BLSHighLuminanceAlwaysOnAttribute"
- "BLSIgnoreCoverGestureAttribute"
- "BLSIgnoreWhenBacklightInactivatesAttribute"
- "BLSInvalidOnSystemSleepAttribute"
- "BLSInvalidateFrameSpecifiersAction"
- "BLSInvalidationDurationAttribute"
- "BLSMemoryByteCountFormatter"
- "BLSPauseOnSystemSleepAttribute"
- "BLSPauseWhenSceneBackgroundAttribute"
- "BLSPeeking"
- "BLSPeekingEnumerator"
- "BLSPendingAssertionService"
- "BLSPendingBacklightProxy"
- "BLSPresentationDateSpecifying"
- "BLSPreventBacklightIdleAttribute"
- "BLSPseudoFlipbookAttribute"
- "BLSRenderedFlipbookFrame"
- "BLSRequestGlobalUnrestrictedFramerateAttribute"
- "BLSRequestLiveUpdatingAttribute"
- "BLSRequestUnrestrictedFramerateAttribute"
- "BLSRuntime"
- "BLSSceneAttribute"
- "BLSTimeoutDurationAttribute"
- "BLSTouchLockAttribute"
- "BLSTransparentFlipbookAttribute"
- "BLSValidWhenBacklightInactiveAttribute"
- "BLSWarningDurationAttribute"
- "BLSXPCAssertionService"
- "BLSXPCAssertionService.requestQueue"
- "BLSXPCAssertionServiceClientInterface"
- "BLSXPCAssertionServiceHostInterface"
- "BLSXPCAssertionServiceSpecification"
- "BLSXPCBacklightProxy"
- "BLSXPCBacklightProxyClientInterface"
- "BLSXPCBacklightProxyHostInterface"
- "BLSXPCBacklightProxyObserverMask"
- "BLSXPCBacklightProxySpecification"
- "BSCancellable"
- "BSInvalidatable"
- "BSXPCCoding"
- "BacklightServices"
- "BacklightServicesInternal"
- "BacklightServices_Internal"
- "NSCoding"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "NSSecureCoding"
- "Off—Cached"
- "Q16@0:8"
- "T#,R"
- "T@\"<BLSAssertionService>\",&,V_service"
- "T@\"<BLSBacklightFBSSceneEnvironmentDiffActionDelegate>\",W,V_delegate"
- "T@\"<BLSBacklightSceneEnvironment>\",R,W,V_environment"
- "T@\"<BLSBacklightSceneEnvironmentDelegate>\",&"
- "T@\"<BLSBacklightSceneEnvironmentUpdating>\",&"
- "T@\"<BLSBacklightSceneEnvironmentUpdating>\",&,V_updater"
- "T@\"<BLSBacklightSceneEnvironment_Private>\",R,W,N,V_environment"
- "T@\"<BLSDiagnosticFlipbookFrameSurfaceProvider>\",W,V_surfaceProvider"
- "T@\"<BLSPresentationDateSpecifying>\",R,N"
- "T@\"<NSObject>\",&,D,N"
- "T@\"<NSObject>\",&,N,V_userObject"
- "T@\"<NSObject><NSCopying>\",&,D,N"
- "T@\"<NSObject><NSCopying>\",&,N,V_timelineIdentifier"
- "T@\"<NSObject><NSCopying>\",R,N,V_identifier"
- "T@\"BLSAlwaysOnDateSpecifier\",R,N"
- "T@\"BLSAlwaysOnDateSpecifier\",R,N,V_dateSpecifier"
- "T@\"BLSAlwaysOnFrameSpecifier\",R"
- "T@\"BLSAlwaysOnFrameSpecifier\",R,N,V_frameSpecifier"
- "T@\"BLSAlwaysOnSession\",&"
- "T@\"BLSAlwaysOnSession\",&,V_alwaysOnSession"
- "T@\"BLSAlwaysOnSession\",R"
- "T@\"BLSAlwaysOnTimelineEntry\",R,V_previousTimelineEntry"
- "T@\"BLSAlwaysOnTimelineEntry\",R,V_timelineEntry"
- "T@\"BLSAssertionDescriptor\",R,N"
- "T@\"BLSAssertionDescriptor\",R,N,V_descriptor"
- "T@\"BLSAssertionIdentifier\",&,N"
- "T@\"BLSBacklightChangeEvent\",R,N"
- "T@\"BLSBacklightChangeEvent\",R,N,V_triggerEvent"
- "T@\"BLSBacklightChangeRequest\",R,N,V_changeRequest"
- "T@\"BLSBacklightChangeSourceEventMetadata\",R,N,V_sourceEventMetadata"
- "T@\"BLSBacklightSceneUpdateContext\",R,N,V_context"
- "T@\"BLSBacklightSceneVisualState\",&,D,N,Sbls_setVisualState:"
- "T@\"BLSBacklightSceneVisualState\",R"
- "T@\"BLSBacklightSceneVisualState\",R,N"
- "T@\"BLSBacklightSceneVisualState\",R,N,V_previousVisualState"
- "T@\"BLSBacklightSceneVisualState\",R,N,V_visualState"
- "T@\"BLSFrameSpecifierModel\",&,V_model"
- "T@\"BSServiceInterface\",R,C,N"
- "T@\"BSServiceQuality\",R,C,N"
- "T@\"FBSScene\",W,G_FBSScene,S_setFBSScene:,V_fbsScene"
- "T@\"FBSSceneIdentityToken\",R,N,V_sceneIdentityToken"
- "T@\"NSArray\",R"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,C,N,V_attributes"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,V_entrySpecifiers"
- "T@\"NSDate\",&,D,N,Sbls_setPresentationDate:"
- "T@\"NSDate\",R"
- "T@\"NSDate\",R,N"
- "T@\"NSDate\",R,N,V_date"
- "T@\"NSDate\",R,N,V_presentationDate"
- "T@\"NSDate\",R,N,V_presentationTime"
- "T@\"NSDate\",R,N,V_previousPresentationDate"
- "T@\"NSDateInterval\",R,N"
- "T@\"NSDateInterval\",R,N,V_dateInterval"
- "T@\"NSDateInterval\",R,V_presentationInterval"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_environmentIdentifier"
- "T@\"NSString\",R,C,N,V_explanation"
- "T@\"NSString\",R,N"
- "T@\"NSUUID\",R,N"
- "T@\"NSUUID\",R,N,V_uuid"
- "T@,R,N,V_userObject"
- "TB"
- "TB,D,N,Gbls_hasDelegate,Sbls_setHasDelegate:"
- "TB,D,N,Gbls_isAlwaysOnEnabledForEnvironment,Sbls_setAlwaysOnEnabledForEnvironment:"
- "TB,D,N,Gbls_isDelegateActive,Sbls_setDelegateActive:"
- "TB,D,N,GisAnimated"
- "TB,D,N,Sbls_setOptsOutOfProcessAssertions:"
- "TB,D,N,Sbls_setSupportsAlwaysOn:"
- "TB,GisAnimatingVisualState"
- "TB,GisAnimatingVisualState,V_animatingVisualState"
- "TB,N"
- "TB,N,Gbls_hasUnrestrictedFramerateUpdates,Sbls_setUnrestrictedFramerateUpdates:"
- "TB,N,Gbls_isLiveUpdating,Sbls_setLiveUpdating:"
- "TB,N,GisAnimated,V_animated"
- "TB,N,Sbls_setAlwaysOnContentIs1hz:"
- "TB,R"
- "TB,R,GhasUnrestrictedFramerateUpdates"
- "TB,R,GisAnimatingVisualState"
- "TB,R,GisDelegateActive"
- "TB,R,GisLiveUpdating"
- "TB,R,N"
- "TB,R,N,GareSceneContentsUpdated"
- "TB,R,N,Gbls_hasUnrestrictedFramerateUpdates"
- "TB,R,N,Gbls_isAlwaysOnEnabledForEnvironment"
- "TB,R,N,Gbls_isDelegateActive"
- "TB,R,N,Gbls_isLiveUpdating"
- "TB,R,N,GisAcquired"
- "TB,R,N,GisActive"
- "TB,R,N,GisAlwaysOnEnabled"
- "TB,R,N,GisAnimated"
- "TB,R,N,GisAnimated,V_animated"
- "TB,R,N,GisAnimationComplete"
- "TB,R,N,GisDimmed,V_dimmed"
- "TB,R,N,GisEnvironmentTransitionAnimated,V_environmentTransitionAnimated"
- "TB,R,N,GisInverted"
- "TB,R,N,GisInverted,V_inverted"
- "TB,R,N,GisObserving"
- "TB,R,N,GisObservingActivatingWithEvent,V_observingActivatingWithEvent"
- "TB,R,N,GisObservingDeactivatingWithEvent,V_observingDeactivatingWithEvent"
- "TB,R,N,GisObservingDidChangeAlwaysOnEnabled,V_observingDidChangeAlwaysOnEnabled"
- "TB,R,N,GisObservingDidCompleteUpdateToState,V_observingDidCompleteUpdateToState"
- "TB,R,N,GisObservingEventsArray,V_observingEventsArray"
- "TB,R,N,GisObservingPerformingEvent,V_observingPerformingEvent"
- "TB,R,N,GisPaused"
- "TB,R,N,GisTouchTargetable"
- "TB,R,N,GisTouchTargetable,V_touchTargetable"
- "TB,R,N,GisTransitionForcedUnanimated,V_transitionForcedUnanimated"
- "TB,R,N,GisTransitioning"
- "TB,R,N,GwasTransitioning,V_transitioning"
- "TB,R,N,V_clearUserInteraction"
- "TB,R,N,V_isUpdateToDateSpecifier"
- "TB,R,N,V_restartTimerOnInvalidation"
- "TB,R,N,V_shouldReset"
- "TB,R,N,V_userInitiated"
- "TB,V_didChange"
- "TQ,N,Sbls_setRenderSeed:"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_count"
- "TQ,R,N,V_eventID"
- "TQ,R,N,V_frameId"
- "TQ,R,N,V_memoryUsage"
- "TQ,R,N,V_presentationTime"
- "TQ,R,N,V_reason"
- "TQ,R,N,V_timestamp"
- "TQ,R,N,V_type"
- "T^{__IOSurface=},R,N"
- "Td,D,N"
- "Td,N,V_duration"
- "Td,R,N"
- "Td,R,N,V_duration"
- "Td,R,V_percentComplete"
- "Tf,R,N"
- "Tf,R,N,V_apl"
- "Tf,R,N,V_aplDimming"
- "Ti,R,N,V_clientPid"
- "Ti,R,N,V_hostPid"
- "Tq"
- "Tq,D,N"
- "Tq,N,V_requestedFidelity"
- "Tq,R"
- "Tq,R,N"
- "Tq,R,N,V_activeAppearance"
- "Tq,R,N,V_adjustedLuminance"
- "Tq,R,N,V_direction"
- "Tq,R,N,V_fidelity"
- "Tq,R,N,V_previousState"
- "Tq,R,N,V_requestedActivityState"
- "Tq,R,N,V_sourceEvent"
- "Tq,R,N,V_state"
- "Tq,R,N,V_updateFidelity"
- "Tq,V_grantedFidelity"
- "T{CGPoint=dd},R,N,V_position"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_rawSurfaceFrame"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "Vv24@0:8@\"<BLSAssertionServiceResponding>\"16"
- "Vv24@0:8@\"BLSAssertionIdentifier\"16"
- "Vv24@0:8@\"BLSBacklightChangeEvent\"16"
- "Vv24@0:8@\"NSError\"16"
- "Vv24@0:8@\"NSNumber\"16"
- "Vv24@0:8@16"
- "Vv32@0:8@\"<BLSAssertionServiceResponding>\"16@\"NSError\"24"
- "Vv32@0:8@\"BLSAssertionIdentifier\"16@\"NSError\"24"
- "Vv32@0:8@\"BLSXPCBacklightProxyObserverMask\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@16@24"
- "Vv32@0:8@16@?24"
- "Vv40@0:8@\"NSNumber\"16@\"NSArray<__BLSBacklightChangeEvent__>\"24@\"NSArray<__BLSBacklightChangeEvent__>\"32"
- "Vv40@0:8@16@24@32"
- "^{_NSZone=}16@0:8"
- "^{__IOSurface=}16@0:8"
- "^{__IOSurface=}24@0:8@\"BLSDiagnosticFlipbookFrame\"16"
- "^{__IOSurface=}24@0:8@16"
- "_FBSScene"
- "_acquisitionObserver"
- "_activeAppearance"
- "_adjustedLuminance"
- "_alwaysOnSession"
- "_animated"
- "_animatingVisualState"
- "_apl"
- "_aplDimming"
- "_assertionsToAcquire"
- "_attributes"
- "_backlightProxy"
- "_backlightState"
- "_calendar"
- "_callbackQueue"
- "_changeRequest"
- "_clearUserInteraction"
- "_clientPid"
- "_completion"
- "_configureEntryBlock"
- "_connection"
- "_context"
- "_count"
- "_date"
- "_dateInterval"
- "_dateSpecifier"
- "_delegate"
- "_descriptor"
- "_didChange"
- "_diffInspector"
- "_dimmed"
- "_direction"
- "_duration"
- "_entrySpecifiers"
- "_enumerator"
- "_environment"
- "_environmentIdentifier"
- "_environmentTransitionAnimated"
- "_eventID"
- "_expectsResponse"
- "_explanation"
- "_explicitEntries"
- "_fbsScene"
- "_fidelity"
- "_frameId"
- "_frameSpecifier"
- "_frequencyPerMinute"
- "_grantedFidelity"
- "_hostPid"
- "_identifier"
- "_inverted"
- "_isUpdateToDateSpecifier"
- "_lock"
- "_lock_accumulatedUnpausedDuration"
- "_lock_acquired"
- "_lock_acquiredMachContinuousTime"
- "_lock_animationComplete"
- "_lock_backlightState"
- "_lock_canceledMachContinuousTime"
- "_lock_completed"
- "_lock_completion"
- "_lock_deviceSupportsAlwaysOn"
- "_lock_deviceSupportsAlwaysOnCached"
- "_lock_didStartBacklightRamp"
- "_lock_everPaused"
- "_lock_isAlwaysOnEnabled"
- "_lock_isAlwaysOnEnabledCached"
- "_lock_isBacklightStateCached"
- "_lock_localState"
- "_lock_observers"
- "_lock_observingActivatingWithEventCount"
- "_lock_observingDeactivatingWithEventCount"
- "_lock_observingDidChangeAlwaysOnEnabledCount"
- "_lock_observingDidCompleteUpdateToStateCount"
- "_lock_observingEventsArrayCount"
- "_lock_observingPerformingEventCount"
- "_lock_paused"
- "_lock_requestedMachContinuousTime"
- "_lock_sceneContentsUpdated"
- "_lock_unpauseMachContinuousTime"
- "_memoryUsage"
- "_model"
- "_observers"
- "_observingActivatingWithEvent"
- "_observingDeactivatingWithEvent"
- "_observingDidChangeAlwaysOnEnabled"
- "_observingDidCompleteUpdateToState"
- "_observingEventsArray"
- "_observingPerformingEvent"
- "_peekedObject"
- "_percentComplete"
- "_performBacklightRampBlock"
- "_periodicInterval"
- "_periodicStart"
- "_position"
- "_presentationDate"
- "_presentationInterval"
- "_presentationTime"
- "_previousPresentationDate"
- "_previousState"
- "_previousTimelineEntry"
- "_previousVisualState"
- "_queue_assertions"
- "_queue_assertionsToReacquire"
- "_rawSurfaceFrame"
- "_reason"
- "_replacementBacklightProxy"
- "_replacementService"
- "_requestQueue"
- "_requestedActivityState"
- "_requestedFidelity"
- "_requests"
- "_restartTimerOnInvalidation"
- "_sceneContentsAnimationCompleteBlock"
- "_sceneContentsUpdatedBlock"
- "_sceneIdentityToken"
- "_service"
- "_setFBSScene:"
- "_shouldReset"
- "_sourceEvent"
- "_sourceEventMetadata"
- "_specifier"
- "_specifiers"
- "_state"
- "_stateHandler"
- "_surfaceProvider"
- "_timelineEntry"
- "_timelineIdentifier"
- "_timestamp"
- "_touchTargetable"
- "_transitionForcedUnanimated"
- "_transitioning"
- "_triggerEvent"
- "_type"
- "_updateFidelity"
- "_updater"
- "_userInitiated"
- "_userObject"
- "_uuid"
- "_visualState"
- "acquireAssertion:"
- "acquireAssertionForDescriptor:error:"
- "acquireWithCompletion:"
- "acquireWithExplanation:observer:attributes:"
- "acquireWithObserver:"
- "acquisitionState"
- "actions"
- "activate"
- "activeAppearance"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:"
- "addSpecifiers:"
- "allFlipbookFrames"
- "allObjects"
- "alwaysFillFlipbook"
- "alwaysOnContentIs1hz"
- "alwaysOnSession"
- "animationCoalesceThreshold"
- "aplDimming"
- "appendArraySection:withName:skipIfEmpty:"
- "appendArraySection:withName:skipIfEmpty:objectTransformer:"
- "appendBodySectionWithName:openDelimiter:closeDelimiter:block:"
- "appendBodySectionWithOpenDelimiter:closeDelimiter:block:"
- "appendBool:"
- "appendBool:counterpart:"
- "appendBool:withName:"
- "appendBool:withName:ifEqualTo:"
- "appendCGPoint:"
- "appendCGRect:"
- "appendCGRect:counterpart:"
- "appendCollection:withName:itemBlock:"
- "appendCustomFormatWithName:block:"
- "appendDouble:"
- "appendDouble:withName:decimalPrecision:"
- "appendFidelityToTarget:"
- "appendFloat:"
- "appendFloat:counterpart:"
- "appendFloat:withName:decimalPrecision:"
- "appendFormat:"
- "appendInt64:"
- "appendInt64:counterpart:"
- "appendInt:withName:"
- "appendInteger:"
- "appendInteger:counterpart:"
- "appendInteger:withName:"
- "appendObject:"
- "appendObject:counterpart:"
- "appendObject:withName:"
- "appendObject:withName:skipIfNil:"
- "appendPoint:withName:"
- "appendPointer:"
- "appendPointer:withName:"
- "appendProem:block:"
- "appendRect:withName:"
- "appendString:"
- "appendString:counterpart:"
- "appendString:withName:"
- "appendString:withName:skipIfEmpty:"
- "appendTimeInterval:withName:decomposeUnits:"
- "appendUInt64:withName:"
- "appendUInt64:withName:format:"
- "appendUnsignedInteger:"
- "appendUnsignedInteger:counterpart:"
- "appendUnsignedInteger:withName:"
- "areSceneContentsUpdated"
- "array"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "assertion:didCancelWithError:"
- "assertion:didFailToAcquireWithError:"
- "assertion:failedToAcquireWithError:"
- "assertionAcquired:"
- "assertionDidCancel:withError:"
- "assertionDidPause:"
- "assertionDidResume:"
- "assertionPaused:"
- "assertionResumed:"
- "assertionWasAcquired:"
- "assertionWillCancel:"
- "attempting to replace backlightProxy:%@ which does not respond to replaceWithBacklightProxy:"
- "attributeOfClass:"
- "attributesOfClasses:"
- "autorelease"
- "autoupdatingCurrentCalendar"
- "backlight:activatingWithEvent:"
- "backlight:deactivatingWithEvent:"
- "backlight:didChangeAlwaysOnEnabled:"
- "backlight:didCompleteUpdateToState:forEvent:"
- "backlight:didCompleteUpdateToState:forEvents:abortedEvents:"
- "backlight:performingEvent:"
- "backlightSceneEnvironment"
- "backlightSceneEnvironmentWithCreationBlock:"
- "backlightState"
- "bls_alwaysOnContentIs1hz"
- "bls_alwaysOnEnabledForEnvironment"
- "bls_appendBoundedCollection:withName:maximumItems:itemBlock:"
- "bls_appendTimeInterval:withName:decomposeUnits:"
- "bls_boundedDescription"
- "bls_boundedDescriptionWithMax:"
- "bls_boundedDescriptionWithMax:transformer:"
- "bls_boundedDescriptionWithTransformer:"
- "bls_compare:withEpsilon:"
- "bls_containsDate:withEpsilon:"
- "bls_containsDate:withEpsilon:outDelta:"
- "bls_delegateActive"
- "bls_fileNameString"
- "bls_hasDelegate"
- "bls_hasUnrestrictedFramerateUpdates"
- "bls_initWithBSContinuousMachTime:"
- "bls_initWithMachContinuousTime:"
- "bls_initWithStartMachContinuousTime:endMachContinuousTime:"
- "bls_isAlwaysOnEnabledForEnvironment"
- "bls_isDelegateActive"
- "bls_isLiveUpdating"
- "bls_isOnOrAfter:"
- "bls_isOnOrAfter:andOnOrBefore:"
- "bls_isOnOrAfter:andOnOrBefore:withEpsilon:"
- "bls_isOnOrBefore:"
- "bls_isValidDate"
- "bls_liveUpdating"
- "bls_loggingString"
- "bls_machContinuousEndTime"
- "bls_machContinuousStartTime"
- "bls_machContinuousTime"
- "bls_machDuration"
- "bls_optsOutOfProcessAssertions"
- "bls_presentationDate"
- "bls_renderSeed"
- "bls_setAlwaysOnContentIs1hz:"
- "bls_setAlwaysOnEnabledForEnvironment:"
- "bls_setDelegateActive:"
- "bls_setHasDelegate:"
- "bls_setLiveUpdating:"
- "bls_setOptsOutOfProcessAssertions:"
- "bls_setPresentationDate:"
- "bls_setRenderSeed:"
- "bls_setSupportsAlwaysOn:"
- "bls_setUnrestrictedFramerateUpdates:"
- "bls_setVisualState:"
- "bls_shortLoggingString"
- "bls_specifier"
- "bls_supportsAlwaysOn"
- "bls_unrestrictedFramerateUpdates"
- "bls_uuid"
- "bls_visualState"
- "boolForSetting:"
- "boolValue"
- "bs_CGRectValue"
- "bs_filter:"
- "bs_map:"
- "bs_mapNoNulls:"
- "bs_valueWithCGRect:"
- "build"
- "builder"
- "builderWithObject:"
- "builderWithObject:ofExpectedClass:"
- "bytes"
- "cacheFlipbook"
- "cacheFlipbookForFBSScene:"
- "cacheFlipbookForFBSSceneIdentityToken:"
- "canBePaused"
- "canSendResponse"
- "cancel"
- "cancelAfterInterval:"
- "cancelAssertion:withError:"
- "cancelWhenBacklightInactivates"
- "changeRequest"
- "checkEntitlementSource:forSingleEntitlement:error:"
- "checkEntitlementSourceForRequiredEntitlements:error:"
- "class"
- "clearUserInteraction"
- "clientSettings"
- "code"
- "compare:"
- "completeWithDateSpecifiers:"
- "completeWithDesiredFidelity:"
- "components:fromDate:"
- "componentsJoinedByString:"
- "configureConnection:"
- "configureEntries:previousEntry:"
- "configureEntry:previousEntry:"
- "conformsToProtocol:"
- "connectionWithEndpoint:"
- "constructFrameSpecifiersForTimelines:dateInterval:shouldConstructStartSpecifier:framesPerSecond:previousSpecifier:"
- "containsObject:"
- "context"
- "copy"
- "copyWithZone:"
- "correctedSpecifierWithNextSpecifier:"
- "countByEnumeratingWithState:objects:count:"
- "createEnvironmentForFBSScene:"
- "createWithFrame:"
- "createWithSpecifier:"
- "d"
- "d16@0:8"
- "dataWithPropertyList:format:options:error:"
- "dateByAddingTimeInterval:"
- "dateByAddingUnit:value:toDate:options:"
- "dateInterval"
- "dateSpecifier"
- "dateSpecifiers"
- "dateWithTimeIntervalSinceNow:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeFloatForKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodePointForKey:"
- "defaultEndpoint"
- "defaultShellMachName"
- "delegate"
- "delegateActive"
- "description"
- "desiredFidelity"
- "desiredFidelityForDateInterval:timelines:withCompletion:"
- "desiredFidelityRequestFromAction:"
- "destroyAssertion:"
- "deviceSupportsAlwaysOn"
- "dictionaryWithObjects:forKeys:count:"
- "didChangeAlwaysOnEnabled:"
- "didCompleteUpdateToState:forEvents:abortedEvents:"
- "disableAlwaysOn"
- "disableCrownRotateToWake"
- "disableFlipbook"
- "disableHoldGesture"
- "disableHoldThrough"
- "disableLongCoverGesture"
- "disableLowerGesture"
- "disableMeasurement"
- "disableRaiseGesture"
- "disableSwipeGesture"
- "disableSwipeThrough"
- "disableTapGesture"
- "disableTapThrough"
- "disableWatchdogs"
- "dispatchWithQOSClass:block:"
- "distantFuture"
- "distantPast"
- "domain"
- "doubleValue"
- "emptyTimelineWithIdentifier:"
- "enableCoverGesture"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeFloat:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodePoint:forKey:"
- "encodeWithCoder:"
- "encodeWithXPCDictionary:"
- "endDate"
- "endpointForMachName:service:instance:"
- "entryForPresentationTime:"
- "entryForPresentationTime:animated:userObject:"
- "entryForPresentationTime:withRequestedFidelity:"
- "entryForPresentationTime:withRequestedFidelity:animated:userObject:"
- "entrySpecifierForTimelineIdentifier:"
- "entrySpecifiers"
- "enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:"
- "enumerateObjectsUsingBlock:"
- "environment:performBacklightSceneUpdate:"
- "environment:timelinesForDateInterval:previousSpecifier:completion:"
- "environmentIdentifier"
- "environmentTransitionAnimated"
- "errorForMissingEntitlement:inSource:"
- "errorWithDomain:code:userInfo:"
- "estimatedFidelityForPresentationTime:nextPresentationTime:"
- "event"
- "eventID"
- "everyMinuteTimelineWithIdentifier:configure:"
- "expectedFidelity"
- "f"
- "f16@0:8"
- "fallbackXPCEncodableClass"
- "fbsScene"
- "fidelityForUpdateInterval:"
- "firstObject"
- "flagForSetting:"
- "flipbookState"
- "forceActive"
- "forceActiveUserInitiated:"
- "frameOnGlassNow"
- "frameOnGlassWhenFlipbookLastCancelled"
- "frameSpecifiersRequestFromAction:"
- "frameWithUUID:"
- "getBacklightState"
- "getFlipbookState"
- "getUUIDBytes:"
- "hasEntitlement:"
- "hasUnrestrictedFramerateUpdates"
- "hash"
- "highLuminanceWhileInAlwaysOn"
- "highLuminanceWhileInAlwaysOnForFBSScene:"
- "highLuminanceWhileInAlwaysOnForFBSSceneIdentityToken:"
- "i"
- "i16@0:8"
- "ignoreCoverGesture"
- "ignoreWhenBacklightInactivates"
- "indexOfObjectPassingTest:"
- "indexOfObjectWithOptions:passingTest:"
- "indexesOfObjectsPassingTest:"
- "info"
- "init"
- "initForEnvironment:visualState:previousVisualState:frameSpecifier:animated:triggerEvent:touchTargetable:isUpdateToDateSpecifier:sceneContentsUpdated:performBacklightRamp:sceneContentsAnimationComplete:"
- "initWithActiveAppearance:updateFidelity:adjustedLuminance:"
- "initWithActiveAppearance:updateFidelity:adjustedLuminance:dimmed:"
- "initWithArray:copyItems:"
- "initWithBacklightChangeEvent:animated:touchTargetable:isUpdateToDateSpecifier:completion:"
- "initWithCapacity:"
- "initWithClientPid:hostPid:count:"
- "initWithCoder:"
- "initWithCompletion:"
- "initWithDate:fidelity:"
- "initWithDate:fidelity:userObject:"
- "initWithDateInterval:previousPresentationDate:shouldReset:completion:"
- "initWithDateSpecifier:environmentIdentifier:"
- "initWithDateSpecifiers:"
- "initWithDesiredFidelity:"
- "initWithDirection:"
- "initWithDuration:"
- "initWithEndpoint:"
- "initWithEntries:identifier:configure:"
- "initWithEnvironment:"
- "initWithEventID:state:previousState:changeRequest:"
- "initWithEventID:state:previousState:wasTransitioning:changeRequest:"
- "initWithExplanation:attributes:"
- "initWithFBSScene:"
- "initWithFrame:"
- "initWithIdentifier:configure:"
- "initWithInfo:error:"
- "initWithInfo:responder:"
- "initWithLocaleIdentifier:"
- "initWithObserver:"
- "initWithObservingDidCompleteUpdateToState:observingEventsArray:didChangeAlwaysOnEnabled:activatingWithEvent:deactivatingWithEvent:performingEvent:"
- "initWithOptions:capacity:"
- "initWithPerMinuteUpdateFrequency:identifier:configure:"
- "initWithPosition:"
- "initWithPresentationDate:specifiers:"
- "initWithPresentationTime:frameId:apl:aplDimming:memoryUsage:rawSurfaceFrameRect:inverted:specifier:uuid:"
- "initWithPresentationTime:requestedFidelity:animated:duration:timelineIdentifier:userObject:"
- "initWithRampDuration:"
- "initWithReason:"
- "initWithRequestedActivityState:explanation:timestamp:sourceEvent:sourceEventMetadata:"
- "initWithRestartTimerOnInvalidation:clearUserInteraction:"
- "initWithSceneIdentityToken:"
- "initWithStartDate:duration:"
- "initWithStartDate:endDate:"
- "initWithTimeIntervalSinceNow:"
- "initWithTimelineEntry:percentComplete:previousTimelineEntry:didChange:"
- "initWithTimelineEntrySpecifiers:presentationInterval:"
- "initWithType:reason:"
- "initWithUUIDBytes:"
- "initWithUpdateInterval:startDate:identifier:configure:"
- "initWithUserInitiated:"
- "initWithVisualState:previousVisualState:frameSpecifier:animated:triggerEvent:touchTargetable:"
- "initWithXPCDictionary:"
- "inspectDiff:"
- "inspectDiff:withContext:"
- "integerValue"
- "interface"
- "interfaceWithIdentifier:"
- "invalidate"
- "invalidateAllTimelinesForReason:"
- "invalidateOnSystemSleep"
- "isActive"
- "isAfterDate:"
- "isAlwaysOnEnabled"
- "isAnimated"
- "isAnimatingVisualState"
- "isAnimationComplete"
- "isBSServiceConnectionError"
- "isBeforeDate:"
- "isDelegateActive"
- "isDimmed"
- "isEnvironmentTransitionAnimated"
- "isEqual"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToDate:"
- "isEssentiallyEqualToVisualState:"
- "isHostProcess"
- "isInverted"
- "isKindOfClass:"
- "isLiveUpdating"
- "isMemberOfClass:"
- "isObserving"
- "isObservingActivatingWithEvent"
- "isObservingDeactivatingWithEvent"
- "isObservingDidChangeAlwaysOnEnabled"
- "isObservingDidCompleteUpdateToState"
- "isObservingEventsArray"
- "isObservingPerformingEvent"
- "isProxy"
- "isTouchTargetable"
- "isTransitionForcedUnanimated"
- "isTransitioning"
- "lastObject"
- "laterDate:"
- "length"
- "localizedDescription"
- "localizedFailureReason"
- "loggingStringForPresentationInterval:"
- "loggingStringForPresentationTime:"
- "maskForObserver:"
- "maskForObservingDidCompleteUpdateToState:observingEventsArray:didChangeAlwaysOnEnabled:activatingWithEvent:deactivatingWithEvent:performingEvent:"
- "mutableCopyWithZone:"
- "nanosecond"
- "newSpecifierWithMaxFidelity:"
- "newVisualStateWithUpdateFidelity:"
- "nextCount"
- "nextDateAfterDate:matchingComponents:options:"
- "nextObject"
- "now"
- "nowObservingWithMask:completion:"
- "nullEndpointForService:instance:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "objectForSetting:"
- "objectsAtIndexes:"
- "observeOtherSetting:withBlock:"
- "observerWithCompletion:"
- "observing"
- "observingActivatingWithEvent"
- "observingDeactivatingWithEvent"
- "observingDidChangeAlwaysOnEnabled"
- "observingDidCompleteUpdateToState"
- "observingEventsArray"
- "observingPerformingEvent"
- "otherSettings"
- "pauseOnSystemSleep"
- "pauseWhenBackgroundFBSScene:"
- "pauseWhenBackgroundForFBSSceneIdentityToken:"
- "paused"
- "peekNextObject"
- "peekingEnumerator"
- "peekingEnumeratorWithEnumerator:"
- "performActionsForUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:"
- "performBacklightRampWithDuration:"
- "performChangeRequest:"
- "performChangesWithTransitionContext:environmentDelta:performActionsBlock:"
- "performDesiredFidelityRequest:"
- "performFrameSpecifiersRequest:"
- "performFrameSpecifiersRequest:timelines:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performingEvent:"
- "presentationInterval"
- "preventIdle"
- "preventIdleAndRestartTimerOnInvalidation"
- "preventIdleClearUserInteractionAndRestartTimerOnInvalidation"
- "previousPresentationDate"
- "previousTimelineEntry"
- "previousVisualState"
- "propertyList:isValidForFormat:"
- "protocolForProtocol:"
- "purgeAllButOneSpecifiersBeforeDate:"
- "purgeAllSpecifiersOnOrAfterDate:"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "q24@0:8d16"
- "q32@0:8@16@24"
- "q32@0:8@16d24"
- "raise:format:"
- "rampDuration"
- "rangeOfEntries:forDateInterval:shouldIncludePrevious:"
- "rawSurface"
- "rawSurfaceForFrame:"
- "rawSurfaceForFrameUUID:reply:"
- "relativePriority"
- "release"
- "remoteTarget"
- "removeAllObjects"
- "removeLastObject"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectsInRange:"
- "removeObserver:"
- "replaceWithBacklightProxy:"
- "replaceWithService:"
- "requestLiveUpdatingForFBSScene:"
- "requestLiveUpdatingForFBSSceneIdentityToken:"
- "requestUnrestrictedFramerate"
- "requestUnrestrictedFramerateForFBSScene:"
- "requestUnrestrictedFramerateForFBSSceneIdentityToken:"
- "requestedActivityState"
- "requestedFidelityForStartEntryInDateInterval:withPreviousEntry:"
- "requestedFidelityForTimelines:inDateInterval:"
- "respondToActions:forFBSScene:fromTransitionContext:"
- "responderWithHandler:"
- "respondsToSelector:"
- "response"
- "restartAssertionTimeoutTimer:"
- "restartTimeoutTimer"
- "restartTimerOnInvalidation"
- "retain"
- "retainCount"
- "reverseObjectEnumerator"
- "sceneContentsAnimationDidComplete"
- "sceneContentsDidUpdate"
- "sceneIdentityToken"
- "second"
- "secondsFidelityThreshold"
- "self"
- "sendActions:"
- "sendResponse:"
- "serial"
- "serialQueueWithQOSClass:label:"
- "serviceClass"
- "serviceClass:relativePriority:"
- "serviceDidAcquire"
- "serviceDidCancelWithError:"
- "serviceDidPause"
- "serviceDidResume"
- "serviceFailedToAcquireWithError:"
- "serviceQuality"
- "serviceWillCancel"
- "set"
- "set1HzFlipbooForFBSSceneIdentityToken:"
- "set1HzFlipbook"
- "set1HzFlipbookForFBSScene:"
- "setAllowedUnits:"
- "setAlwaysOnContentIs1hz:"
- "setAlwaysOnSession:"
- "setAnimated:"
- "setAnimatingVisualState:"
- "setClient:"
- "setCountStyle:"
- "setDateFormat:"
- "setDefaultBacklightProxy:"
- "setDefaultService:"
- "setDelegate:"
- "setDidChange:"
- "setDuration:"
- "setFlag:forSetting:"
- "setGrantedFidelity:"
- "setIdentifier:"
- "setInterface:"
- "setInterfaceTarget:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsHostProcess:"
- "setLocale:"
- "setModel:"
- "setObject:forKey:"
- "setObject:forSetting:"
- "setOptsOutOfProcessAssertions:"
- "setQueue:"
- "setReplacedSceneUpdate:"
- "setRequestedFidelity:"
- "setSecond:"
- "setServer:"
- "setService:"
- "setServiceQuality:"
- "setSupportsAlwaysOn:"
- "setSurfaceProvider:"
- "setTargetQueue:"
- "setTimelineIdentifier:"
- "setTimeout:"
- "setTransitionForcedUnanimated:environmentTransitionAnimated:"
- "setUnitsStyle:"
- "setUpdater:"
- "setUserObject:"
- "setWithArray:"
- "setWithObject:"
- "settings"
- "sharedBacklight"
- "sharedFormatter"
- "shortLoggingStringForPresentationInterval:"
- "shortLoggingStringForPresentationTime:"
- "shouldReset"
- "sortKeys"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingSelector:"
- "sourceEvent"
- "sourceEventMetadata"
- "specifierAtPresentationDate:"
- "specifierCount"
- "specifierForPresentationDate:"
- "startDate"
- "stringFromByteCount:"
- "stringFromDate:"
- "stringFromTimeInterval:"
- "stringRepresentation"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "strongToWeakObjectsMapTable"
- "subarrayWithRange:"
- "superclass"
- "supportsAlwaysOn"
- "supportsSecureCoding"
- "surface"
- "surfaceForFrame:"
- "surfaceForFrameUUID:reply:"
- "surfaceProvider"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeIntervalSinceReferenceDate"
- "timelineEntry"
- "timelineIdentifier"
- "timelineWithEntries:identifier:configure:"
- "timelineWithPerMinuteUpdateFrequency:identifier:configure:"
- "timelineWithUpdateInterval:startDate:identifier:configure:"
- "timeoutAfterInterval:"
- "touchLock"
- "touchTargetable"
- "transitionForcedUnanimated"
- "transitioning"
- "transparentFlipbook"
- "triggerEvent"
- "unconfiguredEntriesForDateInterval:previousEntry:"
- "unrestrictedFramerateUpdates"
- "unsignedLongLongValue"
- "updateClientSettingsWithBlock:"
- "updateFidelity"
- "updatedEnvironmentWithDelta:backlightSceneUpdate:"
- "updater"
- "usePseudoFlipbook"
- "userInteractive"
- "utility"
- "v16@0:8"
- "v16@?0@\"<BSServiceConnectionConfiguring>\"8"
- "v16@?0@\"BSServiceConnection<BSServiceConnectionContext>\"8"
- "v20@0:8B16"
- "v24@0:8@\"<BLSAssertionService>\"16"
- "v24@0:8@\"<BLSBacklightSceneEnvironmentDelegate>\"16"
- "v24@0:8@\"<BLSBacklightSceneEnvironmentUpdating>\"16"
- "v24@0:8@\"<BLSBacklightStateObserving>\"16"
- "v24@0:8@\"BLSAlwaysOnSession\"16"
- "v24@0:8@\"BLSAssertion\"16"
- "v24@0:8@\"BLSAssertionIdentifier\"16"
- "v24@0:8@\"BLSDesiredFidelityRequest\"16"
- "v24@0:8@\"BLSFrameSpecifiersRequest\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSObject<OS_xpc_object>\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v25@0:8{?=b1b1b1b1b1}16@\"BLSBacklightSceneUpdate\"17"
- "v25@0:8{?=b1b1b1b1b1}16@17"
- "v28@0:8I16@?20"
- "v32@0:8@\"BLSAssertion\"16@\"NSError\"24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSObject<OS_xpc_object>\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v33@0:8@\"FBSSceneTransitionContext\"16{?=b1b1b1b1b1}24@?<v@?@\"FBSSceneTransitionContext\"{?=b1b1b1b1b1}>25"
- "v33@0:8@16{?=b1b1b1b1b1}24@?25"
- "v40@0:8@16@24@?32"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24q32@?40"
- "warnAfterInterval:"
- "wasTransitioning"
- "weakToStrongObjectsMapTable"
- "workloop"
- "zone"
- "{?=b1b1b1b1b1}24@0:8@16"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{_NSRange=QQ}36@0:8@16@24B32"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
