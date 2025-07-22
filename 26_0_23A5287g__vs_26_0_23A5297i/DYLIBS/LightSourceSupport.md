## LightSourceSupport

> `/System/Library/PrivateFrameworks/LightSourceSupport.framework/LightSourceSupport`

```diff

-7.0.75.1.0
-  __TEXT.__text: 0xda08
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0x9ec
-  __TEXT.__const: 0xdc
-  __TEXT.__cstring: 0xb22
-  __TEXT.__oslogstring: 0x68e
-  __TEXT.__gcc_except_tab: 0x460
-  __TEXT.__unwind_info: 0x558
-  __TEXT.__objc_classname: 0x298
-  __TEXT.__objc_methname: 0x1253
-  __TEXT.__objc_methtype: 0xa91
-  __TEXT.__objc_stubs: 0xd00
+7.0.79.1.102
+  __TEXT.__text: 0xdbb8
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__objc_methlist: 0xa7c
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0xa73
+  __TEXT.__oslogstring: 0x700
+  __TEXT.__gcc_except_tab: 0x45c
+  __TEXT.__unwind_info: 0x560
+  __TEXT.__objc_classname: 0x2a9
+  __TEXT.__objc_methname: 0x12ca
+  __TEXT.__objc_methtype: 0x7a3
+  __TEXT.__objc_stubs: 0xd80
   __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x418
-  __DATA_CONST.__objc_classlist: 0xd0
+  __DATA_CONST.__const: 0x3b8
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x490
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __AUTH_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__objc_selrefs: 0x4c0
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_arraydata: 0x20
+  __AUTH_CONST.__auth_got: 0x3c8
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x5a0
-  __AUTH_CONST.__objc_const: 0x2978
+  __AUTH_CONST.__cfstring: 0x600
+  __AUTH_CONST.__objc_const: 0x2af8
+  __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x100
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x220
-  __DATA.__data: 0x308
+  __AUTH.__objc_data: 0x2d0
+  __AUTH.__thread_vars: 0x30
+  __AUTH.__thread_bss: 0x38
+  __DATA.__objc_ivar: 0x21c
+  __DATA.__data: 0x2a8
   __DATA_DIRTY.__objc_data: 0x5f0
-  __DATA_DIRTY.__bss: 0x158
+  __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 06049D9B-CDF1-3A44-9ECD-321B10736A04
-  Functions: 349
-  Symbols:   1565
-  CStrings:  664
+  UUID: 70CA4932-C3C7-3968-A84E-82D1087C27BD
+  Functions: 368
+  Symbols:   1599
+  CStrings:  670
 
Symbols:
+ +[LSSInvalidatableSet addAssertionsForOptions:reason:to:]
+ -[LSSCAService _setExtendedDisplayLighting]
+ -[LSSCAService initWithTargetQueue:subscriber:]
+ -[LSSCAService initWithTargetQueue:subscriber:].cold.1
+ -[LSSCAService initWithTargetQueue:subscriber:].cold.2
+ -[LSSCAService initWithTargetQueue:subscriber:].cold.3
+ -[LSSCAService setSubscriber:]
+ -[LSSCAService subscriber]
+ -[LSSController _start]
+ -[LSSController _start].cold.1
+ -[LSSController _start].cold.2
+ -[LSSController _start].cold.3
+ -[LSSController _start].cold.4
+ -[LSSController _start].cold.5
+ -[LSSController _start].cold.6
+ -[LSSController _start].cold.7
+ -[LSSController addAssertion:reason:]
+ -[LSSInvalidatableSet .cxx_destruct]
+ -[LSSInvalidatableSet dealloc]
+ -[LSSInvalidatableSet invalidatables]
+ -[LSSInvalidatableSet invalidate]
+ -[LSSInvalidatableSet setInvalidatables:]
+ -[LSSMotionBasedProvider invalidate]
+ -[LSSNullProvider invalidate]
+ -[LSSPerformanceTestProvider invalidate]
+ -[LSSResampler invalidate]
+ -[LSSSettings boolForKey:].cold.1
+ -[LSSSettings doubleForKey:].cold.1
+ -[LSSSettings floatForKey:].cold.1
+ -[LSSSettings logDebugInfo]
+ -[LSSStationaryProvider invalidate]
+ -[LSSSubscriber subscribeOnQueue:options:activityLevelChangeHandler:]
+ -[LSSSubscriber subscribeOnQueue:options:activityLevelChangeHandler:].cold.1
+ -[LSSTestProvider _updateAngle:forTime:]
+ -[LSSTestProvider _updateRealtime:forTime:]
+ -[LSSTestProvider invalidate]
+ -[LSSTimeBasedProvider invalidate]
+ -[LSSXPCClient setOptions:]
+ -[LSSXPCService initWithTargetQueue:subscriber:]
+ -[_LSSCAParamsDictionary count]
+ -[_LSSCAParamsDictionary initWithObjects:forKeys:count:]
+ -[_LSSCAParamsDictionary keyEnumerator]
+ -[_LSSCAParamsDictionary objectForKey:]
+ -[_LSSCAParamsDictionary params]
+ -[_LSSCAParamsDictionary setParams:]
+ -[_LSSSubscription options]
+ -[_LSSSubscription setOptions:]
+ GCC_except_table16
+ GCC_except_table4
+ _LSSMessageKeyLightState
+ _LSSMessageKeyOptions
+ _LSSPowerLog
+ _LSSPowerLog.cold.1
+ _LSSPowerLog.cold.2
+ _OBJC_CLASS_$_LSSInvalidatableSet
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$__LSSCAParamsDictionary
+ _OBJC_IVAR_$_LSSCAService._alignmentRange
+ _OBJC_IVAR_$_LSSCAService._extendedParams
+ _OBJC_IVAR_$_LSSCAService._params
+ _OBJC_IVAR_$_LSSCAService._subscriber
+ _OBJC_IVAR_$_LSSController._needsLight
+ _OBJC_IVAR_$_LSSController._needsOrientation
+ _OBJC_IVAR_$_LSSInvalidatableSet._invalidatables
+ _OBJC_IVAR_$_LSSMotionBasedLightSource._cosLargeAngle
+ _OBJC_IVAR_$_LSSMotionBasedLightSource._cosSmallAngle
+ _OBJC_IVAR_$_LSSXPCClient._options
+ _OBJC_IVAR_$_LSSXPCService._subscriber
+ _OBJC_IVAR_$__LSSCAParamsDictionary._params
+ _OBJC_IVAR_$__LSSSubscription._options
+ _OBJC_METACLASS_$_LSSInvalidatableSet
+ _OBJC_METACLASS_$_NSDictionary
+ _OBJC_METACLASS_$__LSSCAParamsDictionary
+ _OUTLINED_FUNCTION_4
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
+ __OBJC_$_CLASS_METHODS_LSSInvalidatableSet
+ __OBJC_$_INSTANCE_METHODS_LSSInvalidatableSet
+ __OBJC_$_INSTANCE_METHODS__LSSCAParamsDictionary
+ __OBJC_$_INSTANCE_VARIABLES_LSSInvalidatableSet
+ __OBJC_$_INSTANCE_VARIABLES__LSSCAParamsDictionary
+ __OBJC_$_PROP_LIST_LSSInvalidatableSet
+ __OBJC_$_PROP_LIST__LSSCAParamsDictionary
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSSSubscriptionProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSSSubscriptionProvider
+ __OBJC_$_PROTOCOL_REFS_LSSSubscriptionProvider
+ __OBJC_CLASS_PROTOCOLS_$_LSSInvalidatableSet
+ __OBJC_CLASS_RO_$_LSSInvalidatableSet
+ __OBJC_CLASS_RO_$__LSSCAParamsDictionary
+ __OBJC_LABEL_PROTOCOL_$_LSSSubscriptionProvider
+ __OBJC_METACLASS_RO_$_LSSInvalidatableSet
+ __OBJC_METACLASS_RO_$__LSSCAParamsDictionary
+ __OBJC_PROTOCOL_$_LSSSubscriptionProvider
+ __ZL6_cache
+ __ZL6_cache$tlv$init
+ __ZN3lss11SimpleCacheIP11objc_objectyED1Ev
+ __ZNSt3__16vectorIP11objc_objectNS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIP11objc_objectNS_9allocatorIS3_EEE9push_backB8nn200100ERKS2_
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE9push_backB8nn200100ERKy
+ ___23-[LSSController _start]_block_invoke
+ ___23-[LSSController _start]_block_invoke_2
+ ___23-[LSSXPCService _start]_block_invoke.1.cold.8
+ ___30+[LSSSettings currentSettings]_block_invoke.cold.1
+ ___30+[LSSSettings currentSettings]_block_invoke.cold.2
+ ___33-[LSSXPCClient initWithDelegate:]_block_invoke.cold.8
+ ___33-[LSSXPCClient initWithDelegate:]_block_invoke.cold.9
+ ___47-[LSSCAService initWithTargetQueue:subscriber:]_block_invoke
+ ___47-[LSSCAService initWithTargetQueue:subscriber:]_block_invoke_2
+ ___48-[LSSStationaryProvider initWithQueue:delegate:]_block_invoke
+ ___57+[LSSInvalidatableSet addAssertionsForOptions:reason:to:]_block_invoke
+ ___63-[LSSCAService observeValueForKeyPath:ofObject:change:context:]_block_invoke.34
+ ___66-[LSSTestProvider observeValueForKeyPath:ofObject:change:context:]_block_invoke.2
+ ___69-[LSSSubscriber subscribeOnQueue:options:activityLevelChangeHandler:]_block_invoke
+ ___72-[LSSStationaryProvider observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ____ActiveStreamId_block_invoke
+ ____ZL14LSSLogSettingsv_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e8_v12?0I8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_60_e8_32s40s48w_e33_v16?0"NSObject<OS_xpc_object>"8lw48l8s32l8s40l8
+ ___block_literal_global.109
+ ___block_literal_global.131
+ ___block_literal_global.143
+ ___block_literal_global.147
+ ___block_literal_global.152
+ ___block_literal_global.159
+ ___tls_guard
+ ___tls_guard$tlv$init
+ __tlv_atexit
+ __tlv_bootstrap
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$addAssertion:reason:
+ _objc_msgSend$addAssertionsForOptions:reason:to:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$firstObject
+ _objc_msgSend$initWithTargetQueue:subscriber:
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$objectEnumerator
+ _objc_msgSend$options
+ _objc_msgSend$params
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$removeObserver:forKeyPath:
+ _objc_msgSend$setInvalidatables:
+ _objc_msgSend$setOptions:
+ _objc_msgSend$setParams:
+ _objc_msgSend$subscribeOnQueue:options:activityLevelChangeHandler:
+ _xpc_dictionary_get_data
+ _xpc_dictionary_set_data
- +[LSSCAService needsBasedCallbackAvailable]
- -[LSSCAService _requestGlobalFrom:enabled:].cold.1
- -[LSSCAService _requestGlobalFrom:enabled:].cold.2
- -[LSSCAService _setExtendedDisplayLightingTo:]
- -[LSSCAService _updateDisplays].cold.1
- -[LSSCAService _updateDisplays].cold.2
- -[LSSCAService delegate]
- -[LSSCAService initWithTargetQueue:delegate:]
- -[LSSCAService initWithTargetQueue:delegate:].cold.1
- -[LSSCAService initWithTargetQueue:delegate:].cold.2
- -[LSSCAService initWithTargetQueue:delegate:].cold.3
- -[LSSCAService initWithTargetQueue:delegate:].cold.4
- -[LSSCAService setDelegate:]
- -[LSSController caServiceNeedsUpdates:]
- -[LSSController init].cold.1
- -[LSSController init].cold.2
- -[LSSController init].cold.3
- -[LSSController init].cold.4
- -[LSSController init].cold.5
- -[LSSController init].cold.6
- -[LSSController init].cold.7
- -[LSSController init].cold.8
- -[LSSController init].cold.9
- -[LSSController xpcService:addedAssertion:reason:]
- -[LSSController xpcService:addedAssertion:reason:].cold.1
- -[LSSController xpcServiceNeedsUpdates:]
- -[LSSMotionBasedLightSource observeValueForKeyPath:ofObject:change:context:]
- -[LSSMotionBasedProvider dealloc]
- -[LSSPerformanceTestProvider dealloc]
- -[LSSResampler dealloc]
- -[LSSSettings .cxx_construct]
- -[LSSStationaryProvider refresh]
- -[LSSSubscriber subscribeOnQueue:activityLevelChangeHandler:].cold.1
- -[LSSTestProvider observeValueForKeyPath:ofObject:change:context:].cold.5
- -[LSSTestProvider observeValueForKeyPath:ofObject:change:context:].cold.6
- -[LSSTestProvider observeValueForKeyPath:ofObject:change:context:].cold.7
- -[LSSXPCService initWithTargetQueue:]
- -[LSSXPCService setDelegate:]
- GCC_except_table10
- GCC_except_table15
- GCC_except_table39
- _LSSLogTestProvider
- _LSSLogTestProvider.cold.1
- _LSSMessageKeyDirectionX
- _LSSMessageKeyDirectionY
- _LSSMessageKeyDirectionZ
- _LSSMessageKeyIntensity
- _LSSMessageKeyReferenceOrientationW
- _LSSMessageKeyReferenceOrientationX
- _LSSMessageKeyReferenceOrientationY
- _LSSMessageKeyReferenceOrientationZ
- _LSSMessageKeyStartPause
- _LSSMessageKeyTimestamp
- _LSSShouldRun.cold.3
- _OBJC_CLASS_$_CAWindowServerDisplay
- _OBJC_IVAR_$_LSSCAService._alwaysOnFallback
- _OBJC_IVAR_$_LSSCAService._delegate
- _OBJC_IVAR_$_LSSCAService._deviceAlignmentMax
- _OBJC_IVAR_$_LSSCAService._extendedParamsCache
- _OBJC_IVAR_$_LSSCAService._hasExtendedParams
- _OBJC_IVAR_$_LSSCAService._paramsCache
- _OBJC_IVAR_$_LSSCAService._paramsDictionary
- _OBJC_IVAR_$_LSSController._caNeedsUpdates
- _OBJC_IVAR_$_LSSController._xpcNeedsUpdates
- _OBJC_IVAR_$_LSSSettings._boolCache
- _OBJC_IVAR_$_LSSSettings._doubleCache
- _OBJC_IVAR_$_LSSSettings._floatCache
- _OBJC_IVAR_$_LSSSettings._integerCache
- _OBJC_IVAR_$_LSSXPCService._delegate
- __LSSCAParamsFillDictionary
- __LSSCAParamsFillDictionary.cold.1
- __OBJC_$_CLASS_METHODS_LSSCAService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSSCAServiceDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSSXPCAssertionDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_LSSCAServiceDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_LSSXPCAssertionDelegate
- __OBJC_$_PROTOCOL_REFS_LSSCAServiceDelegate
- __OBJC_$_PROTOCOL_REFS_LSSXPCAssertionDelegate
- __OBJC_LABEL_PROTOCOL_$_LSSCAServiceDelegate
- __OBJC_LABEL_PROTOCOL_$_LSSXPCAssertionDelegate
- __OBJC_PROTOCOL_$_LSSCAServiceDelegate
- __OBJC_PROTOCOL_$_LSSXPCAssertionDelegate
- __ZN3lss11SimpleCacheIbE3getEP8NSString
- __ZN3lss11SimpleCacheIbE3putEP8NSStringb
- __ZN3lss11SimpleCacheIdE3getEP8NSString
- __ZN3lss11SimpleCacheIfE3getEP8NSString
- __ZN3lss14_cached_lookupIbEET_P8NSStringRNS_11SimpleCacheIS1_EEP14NSUserDefaults
- __ZN3lss14_cached_lookupIdEET_P8NSStringRNS_11SimpleCacheIS1_EEP14NSUserDefaults
- __ZN3lss14_cached_lookupIfEET_P8NSStringRNS_11SimpleCacheIS1_EEP14NSUserDefaults
- __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRU8__strongKS2_EEEPS3_DpOT_
- __ZNSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__16vectorIbNS_9allocatorIbEEE7reserveEm
- __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__16vectorIdNS_9allocatorIdEEE9push_backB8nn200100ERKd
- __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB8nn200100ERKf
- ___21-[LSSController init]_block_invoke.23
- ___21-[LSSController init]_block_invoke_2
- ___32-[LSSStationaryProvider refresh]_block_invoke
- ___43-[LSSCAService setLightForDynamicDisplays:]_block_invoke_2
- ___45-[LSSCAService initWithTargetQueue:delegate:]_block_invoke
- ___45-[LSSCAService initWithTargetQueue:delegate:]_block_invoke_2
- ___61-[LSSSubscriber subscribeOnQueue:activityLevelChangeHandler:]_block_invoke
- ___66-[LSSTestProvider observeValueForKeyPath:ofObject:change:context:]_block_invoke.3
- ____ZL30_LSSIsMotionBasedPhotosEnabledv_block_invoke
- ___block_descriptor_144_e16_128s136s_e5_v8?0ls128l8s136l8
- ___block_descriptor_32_e31_B16?0"CAWindowServerDisplay"8l
- ___block_descriptor_48_e8_32s40w_e33_v16?0"NSObject<OS_xpc_object>"8lw40l8s32l8
- ___block_descriptor_68_e8_32s40s48s56w_e33_v16?0"NSObject<OS_xpc_object>"8lw56l8s32l8s40l8s48l8
- ___block_literal_global.120
- ___block_literal_global.123
- ___block_literal_global.153
- ___block_literal_global.162
- ___block_literal_global.168
- ___block_literal_global.173
- ___block_literal_global.68
- _objc_msgSend$caServiceNeedsUpdates:
- _objc_msgSend$initWithTargetQueue:delegate:
- _objc_msgSend$instancesRespondToSelector:
- _objc_msgSend$needsBasedCallbackAvailable
- _objc_msgSend$numberWithDouble:
- _objc_msgSend$refresh
- _objc_msgSend$setGlobalLightAngle:
- _objc_msgSend$setValue:forKey:
- _objc_msgSend$valueForKey:
- _objc_msgSend$xpcService:addedAssertion:reason:
- _objc_msgSend$xpcServiceNeedsUpdates:
- _objc_opt_respondsToSelector
- _objc_release_x28
- _objc_retain
- _pow
- _xpc_dictionary_get_bool
- _xpc_dictionary_get_double
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_double
CStrings:
+ "--ACTIVE-"
+ "--IDLE--"
+ "-[LSSController _start]"
+ "-[LSSSubscriber subscribeOnQueue:options:activityLevelChangeHandler:]"
+ "@\"<BSInvalidatable>\"28@0:8I16@\"NSString\"20"
+ "@\"<LSSSubscriptionProvider>\""
+ "@\"NSArray\""
+ "@\"_LSSCAParamsDictionary\""
+ "@28@0:8I16@20"
+ "@36@0:8@16I24@?28"
+ "@36@0:8I16@20@28"
+ "@40@0:8r^@16r^@24Q32"
+ "CoreAnimation"
+ "I"
+ "I16@0:8"
+ "LSSInvalidatableSet"
+ "LSSPowerLog"
+ "LSSPowerLogging.m"
+ "LSSSubscriptionProvider"
+ "LightSourceSupport"
+ "RenderData"
+ "Settings"
+ "T@\"<LSSSubscriptionProvider>\",W,N,V_subscriber"
+ "T@\"NSArray\",&,N,V_invalidatables"
+ "TI,N,V_options"
+ "T{?=ffff},N,V_params"
+ "_LSSCAParamsDictionary"
+ "_alignmentRange"
+ "_client != nil"
+ "_cosLargeAngle"
+ "_cosSmallAngle"
+ "_extendedParams"
+ "_invalidatables"
+ "_needsLight"
+ "_needsOrientation"
+ "_options"
+ "_params"
+ "addAssertion:reason:"
+ "addAssertionsForOptions:reason:to:"
+ "adding subscription. options: %u"
+ "arrayWithObjects:count:"
+ "cached keys: %lu"
+ "configure assertion"
+ "configure subscription"
+ "dynamic settings"
+ "firstObject"
+ "initWithObjects:forKeys:count:"
+ "initWithTargetQueue:subscriber:"
+ "invalidatables"
+ "keyEnumerator"
+ "needsLight"
+ "needsOrientation"
+ "numberWithFloat:"
+ "objectEnumerator"
+ "options"
+ "params"
+ "removeObserver:"
+ "removeObserver:forKeyPath:"
+ "s"
+ "setInvalidatables:"
+ "setOptions:"
+ "setParams:"
+ "static settings"
+ "subscribeOnQueue:options:activityLevelChangeHandler:"
+ "unexpected light state size: %lu"
+ "update options: %u"
+ "v12@?0I8"
+ "v20@0:8I16"
+ "v32@0:8{?=ffff}16"
+ "xpc client"
+ "{?=\"angle\"f\"opacity\"f\"spread\"f\"height\"f}"
+ "{?=ffff}16@0:8"
+ "\x81"
+ "\xd1"
- "+1"
- "-[LSSCAService _requestGlobalFrom:enabled:]"
- "-[LSSCAService _updateDisplays]"
- "-[LSSController init]"
- "-[LSSController xpcService:addedAssertion:reason:]"
- "-[LSSSubscriber subscribeOnQueue:activityLevelChangeHandler:]"
- ".cxx_construct"
- "@\"<BSInvalidatable>\""
- "@\"<BSInvalidatable>\"24@0:8@\"LSSCAService\"16"
- "@\"<BSInvalidatable>\"24@0:8@\"LSSXPCService\"16"
- "@\"<BSInvalidatable>\"40@0:8@\"LSSXPCService\"16Q24@\"NSString\"32"
- "@\"<LSSCAServiceDelegate>\""
- "@\"<LSSXPCAssertionDelegate>\""
- "@40@0:8@16Q24@32"
- "Gyro1Up"
- "GyroPoster"
- "GyroWidget"
- "LSSCAService.m"
- "LSSCAServiceDelegate"
- "LSSXPCAssertionDelegate"
- "Photos"
- "T@\"<LSSCAServiceDelegate>\",W,N,V_delegate"
- "W"
- "X"
- "Y"
- "Z"
- "_LSSCAParamsFillDictionary"
- "_alwaysOnFallback"
- "_alwaysOnFallback == nil"
- "_boolCache"
- "_caNeedsUpdates"
- "_deviceAlignmentMax"
- "_doubleCache"
- "_extendedParamsCache"
- "_floatCache"
- "_hasExtendedParams"
- "_integerCache"
- "_paramsCache"
- "_paramsDictionary"
- "_xpcNeedsUpdates"
- "adding subscription"
- "always on"
- "caNeedsUpdates"
- "caServiceNeedsUpdates:"
- "dictionary != nil"
- "has clients"
- "has updating displays"
- "initWithTargetQueue:delegate:"
- "instancesRespondToSelector:"
- "message"
- "needsBasedCallbackAvailable"
- "numberWithDouble:"
- "p"
- "refresh"
- "setGlobalLightAngle:"
- "setValue:forKey:"
- "t"
- "typeNumber != 0"
- "using dynamic settings"
- "using static settings"
- "valueForKey:"
- "x"
- "xpcNeedsUpdates"
- "xpcService:addedAssertion:reason:"
- "xpcServiceNeedsUpdates:"
- "y"
- "z"
- "{?=\"angle\"d\"opacity\"d\"spread\"d\"height\"d}"
- "{SimpleCache<bool>=\"keys\"{vector<NSString *, std::allocator<NSString *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}\"vals\"{vector<bool, std::allocator<bool>>=\"__begin_\"^Q\"__size_\"Q\"__cap_\"Q}}"
- "{SimpleCache<double>=\"keys\"{vector<NSString *, std::allocator<NSString *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}\"vals\"{vector<double, std::allocator<double>>=\"__begin_\"^d\"__end_\"^d\"__cap_\"^d}}"
- "{SimpleCache<float>=\"keys\"{vector<NSString *, std::allocator<NSString *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}\"vals\"{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__cap_\"^f}}"
- "{SimpleCache<long>=\"keys\"{vector<NSString *, std::allocator<NSString *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}\"vals\"{vector<long, std::allocator<long>>=\"__begin_\"^q\"__end_\"^q\"__cap_\"^q}}"
- "\xf0!"

```
