## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness`

```diff

-2300.1.2.0.0
-  __TEXT.__text: 0x1634fc
-  __TEXT.__objc_methlist: 0xd31c
-  __TEXT.__const: 0x127a0
-  __TEXT.__oslogstring: 0x185dd
-  __TEXT.__cstring: 0xcdc5
-  __TEXT.__gcc_except_tab: 0x1fc8
+2300.41.8.0.0
+  __TEXT.__text: 0x16bb80
+  __TEXT.__objc_methlist: 0xd888
+  __TEXT.__cstring: 0xd12a
+  __TEXT.__const: 0x129e8
+  __TEXT.__gcc_except_tab: 0x210c
+  __TEXT.__oslogstring: 0x18ffd
   __TEXT.__dlopen_cstrs: 0x10d
-  __TEXT.__swift5_typeref: 0xeaf
-  __TEXT.__constg_swiftt: 0xc34
-  __TEXT.__swift5_reflstr: 0xa4e
+  __TEXT.__swift5_typeref: 0xf36
+  __TEXT.__constg_swiftt: 0xd80
+  __TEXT.__swift5_reflstr: 0xbf4
   __TEXT.__swift5_assocty: 0x288
-  __TEXT.__swift5_fieldmd: 0x100c
-  __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_capture: 0x3d0
+  __TEXT.__swift5_fieldmd: 0x1240
+  __TEXT.__swift5_builtin: 0x168
+  __TEXT.__swift5_capture: 0x41c
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x308
-  __TEXT.__swift5_types: 0x120
+  __TEXT.__swift5_types: 0x144
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x5348
-  __TEXT.__eh_frame: 0xb88
+  __TEXT.__unwind_info: 0x5568
+  __TEXT.__eh_frame: 0xbc8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11d8
-  __DATA_CONST.__objc_classlist: 0x6f0
-  __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x338
+  __DATA_CONST.__const: 0x1210
+  __DATA_CONST.__objc_classlist: 0x720
+  __DATA_CONST.__objc_catlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x350
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x56c8
-  __DATA_CONST.__objc_protorefs: 0x130
-  __DATA_CONST.__objc_superrefs: 0x5b8
-  __DATA_CONST.__objc_arraydata: 0xb90
-  __DATA_CONST.__got: 0x760
-  __AUTH_CONST.__const: 0x5860
-  __AUTH_CONST.__cfstring: 0xe5c0
-  __AUTH_CONST.__objc_const: 0x34b28
+  __DATA_CONST.__objc_selrefs: 0x5938
+  __DATA_CONST.__objc_protorefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0x5c8
+  __DATA_CONST.__objc_arraydata: 0xc40
+  __DATA_CONST.__got: 0x7b8
+  __AUTH_CONST.__const: 0x5f88
+  __AUTH_CONST.__cfstring: 0xe8e0
+  __AUTH_CONST.__objc_const: 0x36758
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__objc_intobj: 0xcd8
-  __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__objc_dictobj: 0x5f0
+  __AUTH_CONST.__objc_intobj: 0xd08
   __AUTH_CONST.__objc_floatobj: 0x180
-  __AUTH_CONST.__objc_arrayobj: 0x2a0
-  __AUTH_CONST.__auth_got: 0x1288
-  __AUTH_CONST.__auth_ptr: 0x480
-  __AUTH.__objc_data: 0x2680
-  __AUTH.__data: 0x630
-  __DATA.__objc_ivar: 0x1768
-  __DATA.__data: 0x66f50
-  __DATA.__bss: 0x63e0
+  __AUTH_CONST.__objc_arrayobj: 0x2d0
+  __AUTH_CONST.__objc_dictobj: 0x690
+  __AUTH_CONST.__objc_doubleobj: 0x40
+  __AUTH_CONST.__auth_got: 0x1300
+  __AUTH_CONST.__auth_ptr: 0x4a0
+  __AUTH.__objc_data: 0x2940
+  __AUTH.__data: 0x6c0
+  __DATA.__objc_ivar: 0x17ec
+  __DATA.__data: 0x670c8
+  __DATA.__bss: 0x6440
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x21e8
   __DATA_DIRTY.__data: 0x510
-  __DATA_DIRTY.__bss: 0x168
+  __DATA_DIRTY.__bss: 0x160
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreDisplay.framework/Versions/A/CoreDisplay
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8200
-  Symbols:   12859
-  CStrings:  4652
+  Functions: 8418
+  Symbols:   13170
+  CStrings:  4738
 
Symbols:
+ +[CBDisplayBrightnessClient copyNSNumberForKey:client:handle:andError:]
+ +[CBRampProfileSpring defaultSpringProfile]
+ -[BLControl callBlockWithProperty:value:origin:]
+ -[BLControl clearKeyboardSet]
+ -[BLControl clearPILSet]
+ -[BLControl setFrameInfoProviderForProxy:]
+ -[BacklightDriverPWM _noteLevelWriteForFrequencySettle:]
+ -[BacklightDriverPWM _scheduleFrequencySettleAfter:]
+ -[BacklightDriverPWM _setNits:withFadeSpeed:minPWMPercentage:completion:]
+ -[BacklightDriverPWM dutyKey]
+ -[BacklightDriverPWM initWithBacklightService:configuration:]
+ -[BacklightDriverPWM initWithConfiguration:]
+ -[BacklightDriverPWM nitsUpdateLogType]
+ -[BacklightDriverPWM setDutyKey:]
+ -[BacklightDriverPWM setNits:withFadeSpeed:minPWMPercentage:]
+ -[BacklightDriverPWM setUseDynamicFrequency:]
+ -[BacklightDriverPWM useDynamicFrequency]
+ -[BrightnessSystemClient observerSlug:]
+ -[BrightnessSystemClient refreshKeys]
+ -[CBCEModule copyCachedInferenceForEvent:]
+ -[CBCEModule invalidateInferenceCache]
+ -[CBCEModule shouldRunInferenceAtTime:]
+ -[CBColorModuleShared CEModulePropertyHandler:key:]
+ -[CBColorPolicyFilter colorAdaptationActive]
+ -[CBColorPolicyFilter setColorAdaptationActive:]
+ -[CBDarwinStateNotifier dealloc]
+ -[CBDarwinStateNotifier initWithNotificationName:logCategory:]
+ -[CBDarwinStateNotifier publishState:]
+ -[CBDisplayBrightnessClient currentSDRNitsWithError:]
+ -[CBDisplayBrightnessClient description]
+ -[CBDisplayBrightnessClient maxSDRDisplayNitsWithError:]
+ -[CBDisplayClient description]
+ -[CBDisplayContainerSKL clearCachedALSEvents]
+ -[CBDisplayContainerSKL handleDisplayBrightnessFactorUpdate:]
+ -[CBDisplayContainerSKL handleDisplayPowerStateEvent:]
+ -[CBDisplayContainerSKL shouldDiscardALSEvent:]
+ -[CBDisplayStatusBroadcaster activate]
+ -[CBDisplayStatusBroadcaster cancel]
+ -[CBDisplayStatusBroadcaster dealloc]
+ -[CBDisplayStatusBroadcaster displayModeProvidersUpdate:]
+ -[CBDisplayStatusBroadcaster initWithDisplayManager:]
+ -[CBDisplayStatusBroadcaster reevaluateAndNotify]
+ -[CBDisplayStatusBroadcaster sendNotificationForKey:value:origin:]
+ -[CBHIDEventManager addUnfilteredClient:]
+ -[CBIndicatorBrightnessModule currentTimeUs]
+ -[CBIndicatorBrightnessModule registerForThermalPressureNotifications]
+ -[CBIndicatorBrightnessModule shouldHintSILOnForEventTimestampUs:]
+ -[CBIndicatorBrightnessModule thermalPressureNotificationHandler:]
+ -[CBPreset alwaysRequestMaxHeadroom]
+ -[CBPreset maxPotentialEDRHeadroom]
+ -[CBPresetsParser alwaysRequestMaxHeadroom:]
+ -[CBPresetsParser maxPotentialEDRHeadroomForDisplay:]
+ -[CBRampManager insertNewRampOrigin:target:length:frequency:identifier:profile:]
+ -[CBRampManager insertNewRampOrigin:target:length:frequency:startRamp:identifier:profile:]
+ -[CBRampProfileLinear normalizedOutputForProgress:]
+ -[CBRampProfileSpring _cacheNormalizer]
+ -[CBRampProfileSpring _springValAtT:]
+ -[CBRampProfileSpring damping]
+ -[CBRampProfileSpring init]
+ -[CBRampProfileSpring initialVelocity]
+ -[CBRampProfileSpring mass]
+ -[CBRampProfileSpring normalizedOutputForProgress:]
+ -[CBRampProfileSpring setDamping:]
+ -[CBRampProfileSpring setInitialVelocity:]
+ -[CBRampProfileSpring setMass:]
+ -[CBRampProfileSpring setStiffness:]
+ -[CBRampProfileSpring stiffness]
+ -[CBRingLight resetUserAdjustmentState]
+ -[CBRingLight statusInfo]
+ -[CBSystemContext frameInfoProvider]
+ -[CBSystemContext setFrameInfoProvider:]
+ -[NSArray(PrimitiveDataProvider) copyFloatVector]
+ -[NSSet(PrettyDescription) prettyDescription]
+ -[NightModeControl stop]
+ -[PWMCalibrationManager convertNitsToPWMPercentage:minPWMPercentage:]
+ -[PWMDeviceController _reportDuty:]
+ -[PWMDeviceController dutyKey]
+ -[PWMDeviceController setDutyCycle:dynamicFrequency:]
+ -[PWMDeviceController setDutyKey:]
+ -[PWMDeviceController setEnabled:commit:applyEnablePulse:]
+ -[VMBLControl addDisplayModuleForBrightnessControlProxy:]
+ -[VMBLControl sendBrightnessTransactionRequestForDisplayUUID:builtIn:]
+ -[VMBLControl sendBrightnessTransactionRequestOnQueueForDisplayUUID:builtIn:]
+ -[VMBLControl sendHeadroomRequestOnQueue:forDisplayUUID:builtIn:]
+ -[VMDisplayModule setPropertyOnQueue:forKey:]
+ CBU_IsDisplayStatusAggregationEnabled
+ CBU_IsDisplayStatusAggregationEnabled.once
+ CBU_IsDisplayStatusAggregationEnabled.result
+ GCC_except_table100
+ GCC_except_table125
+ GCC_except_table150
+ GCC_except_table153
+ GCC_except_table154
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table162
+ GCC_except_table163
+ GCC_except_table167
+ GCC_except_table168
+ GCC_except_table177
+ GCC_except_table182
+ GCC_except_table183
+ GCC_except_table211
+ GCC_except_table46
+ GCC_except_table69
+ GCC_except_table72
+ GCC_except_table77
+ OBJC_IVAR_$_BacklightDriverPWM._frequencySettlePending
+ OBJC_IVAR_$_BacklightDriverPWM._lastLevelWriteTime
+ OBJC_IVAR_$_BacklightDriverPWM._lastLevelWritten
+ OBJC_IVAR_$_BacklightDriverPWM._useDynamicFrequency
+ OBJC_IVAR_$_BrightnessSystemClient._observedKeys
+ OBJC_IVAR_$_BrightnessSystemClient._observersCount
+ OBJC_IVAR_$_CBCEModule._cachedResult
+ OBJC_IVAR_$_CBCEModule._cadenceSeconds
+ OBJC_IVAR_$_CBCEModule._lastInferenceTime
+ OBJC_IVAR_$_CBCPMSModule._currentHDRNits
+ OBJC_IVAR_$_CBColorPolicyFilter._ceModelID
+ OBJC_IVAR_$_CBColorPolicyFilter._colorAdaptationActive
+ OBJC_IVAR_$_CBDarwinStateNotifier._logHandle
+ OBJC_IVAR_$_CBDarwinStateNotifier._name
+ OBJC_IVAR_$_CBDarwinStateNotifier._token
+ OBJC_IVAR_$_CBDisplayContainerSKL._alsNodes
+ OBJC_IVAR_$_CBDisplayContainerSKL._coexTracker
+ OBJC_IVAR_$_CBDisplayContainerSKL._lastEventByServiceID
+ OBJC_IVAR_$_CBDisplayContainerSKL._sensitivityFilter
+ OBJC_IVAR_$_CBDisplayStatusBroadcaster._displayOnByDisplay
+ OBJC_IVAR_$_CBDisplayStatusBroadcaster._hasPublished
+ OBJC_IVAR_$_CBDisplayStatusBroadcaster._lastPublishedState
+ OBJC_IVAR_$_CBDisplayStatusBroadcaster._logHandle
+ OBJC_IVAR_$_CBDisplayStatusBroadcaster._manager
+ OBJC_IVAR_$_CBDisplayStatusBroadcaster._notifier
+ OBJC_IVAR_$_CBHIDEventManager._unfilteredClients
+ OBJC_IVAR_$_CBIndicatorBrightnessModule._thermalPressure
+ OBJC_IVAR_$_CBIndicatorBrightnessModule._thermalPressureNotificationToken
+ OBJC_IVAR_$_CBRampProfileSpring._damping
+ OBJC_IVAR_$_CBRampProfileSpring._initialVelocity
+ OBJC_IVAR_$_CBRampProfileSpring._mass
+ OBJC_IVAR_$_CBRampProfileSpring._normalizer
+ OBJC_IVAR_$_CBRampProfileSpring._stiffness
+ OBJC_IVAR_$_CBRingLight._overriddenByUser
+ OBJC_IVAR_$_CBSystemContext._frameInfoProvider
+ OBJC_IVAR_$_PWMDeviceController._clock
+ OBJC_IVAR_$_PWMDeviceController._dutyKey
+ _CBU_DeviceEnclosureColor
+ _CBU_IsDisplayStatusAggregationEnabled
+ _CFStringGetIntValue
+ _DisplayGetBrightnessAfterForcedDynamicSliderRestriction
+ _OBJC_CLASS_$_ALSSensitivityFilter
+ _OBJC_CLASS_$_CBDarwinStateNotifier
+ _OBJC_CLASS_$_CBDisplayStatusBroadcaster
+ _OBJC_CLASS_$_CBRampProfileLinear
+ _OBJC_CLASS_$_CBRampProfileSpring
+ _OBJC_CLASS_$_CBSMCLib
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_METACLASS_$_ALSSensitivityFilter
+ _OBJC_METACLASS_$_CBDarwinStateNotifier
+ _OBJC_METACLASS_$_CBDisplayStatusBroadcaster
+ _OBJC_METACLASS_$_CBRampProfileLinear
+ _OBJC_METACLASS_$_CBRampProfileSpring
+ _OBJC_METACLASS_$_CBSMCLib
+ _OBJC_METACLASS_$__TtC14CoreBrightnessP33_6B340E709F1569E35356F761E538365910SMCKeyImpl
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _PROTOCOLS__TtC14CoreBrightnessP33_6B340E709F1569E35356F761E538365910SMCKeyImpl
+ _SMCGetKeyInfo
+ _SMCOpenConnectionWithDefaultService
+ _SMCWriteKeyWithKnownSize
+ __45-[CBIndicatorBrightnessModule setSilEnabled:]_block_invoke
+ __52-[CBHIDEventManager hidEventCallbackWithEvent:from:]_block_invoke
+ __73-[BacklightDriverPWM _setNits:withFadeSpeed:minPWMPercentage:completion:]_block_invoke
+ __CLASS_METHODS_CBCoexTracker
+ __DATA_ALSSensitivityFilter
+ __DATA_CBSMCLib
+ __DATA__TtC14CoreBrightnessP33_6B340E709F1569E35356F761E538365910SMCKeyImpl
+ __INSTANCE_METHODS_ALSSensitivityFilter
+ __INSTANCE_METHODS_CBSMCLib
+ __INSTANCE_METHODS__TtC14CoreBrightnessP33_6B340E709F1569E35356F761E538365910SMCKeyImpl
+ __IVARS_ALSSensitivityFilter
+ __IVARS_CBSMCLib
+ __IVARS__TtC14CoreBrightnessP33_6B340E709F1569E35356F761E538365910SMCKeyImpl
+ __METACLASS_DATA_ALSSensitivityFilter
+ __METACLASS_DATA_CBSMCLib
+ __METACLASS_DATA__TtC14CoreBrightnessP33_6B340E709F1569E35356F761E538365910SMCKeyImpl
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSSet_$_PrettyDescription
+ __OBJC_$_CATEGORY_NSSet_$_PrettyDescription
+ __OBJC_$_CLASS_METHODS_CBRampProfileSpring
+ __OBJC_$_INSTANCE_METHODS_CBDarwinStateNotifier
+ __OBJC_$_INSTANCE_METHODS_CBDisplayStatusBroadcaster
+ __OBJC_$_INSTANCE_METHODS_CBRampProfileLinear
+ __OBJC_$_INSTANCE_METHODS_CBRampProfileSpring
+ __OBJC_$_INSTANCE_VARIABLES_CBDarwinStateNotifier
+ __OBJC_$_INSTANCE_VARIABLES_CBDisplayStatusBroadcaster
+ __OBJC_$_INSTANCE_VARIABLES_CBRampProfileSpring
+ __OBJC_$_PROP_LIST_CBDarwinStateNotifier
+ __OBJC_$_PROP_LIST_CBDisplayStatusBroadcaster
+ __OBJC_$_PROP_LIST_CBRampProfileLinear
+ __OBJC_$_PROP_LIST_CBRampProfileSpring
+ __OBJC_$_PROP_LIST_NSSet_$_PrettyDescription
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBRampProfile
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBSMCKey
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBStateNotifier
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBRampProfile
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBSMCKey
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBStateNotifier
+ __OBJC_$_PROTOCOL_REFS_CBRampProfile
+ __OBJC_$_PROTOCOL_REFS_CBSMCKey
+ __OBJC_$_PROTOCOL_REFS_CBStateNotifier
+ __OBJC_CLASS_PROTOCOLS_$_CBDarwinStateNotifier
+ __OBJC_CLASS_PROTOCOLS_$_CBDisplayStatusBroadcaster
+ __OBJC_CLASS_PROTOCOLS_$_CBRampProfileLinear
+ __OBJC_CLASS_PROTOCOLS_$_CBRampProfileSpring
+ __OBJC_CLASS_RO_$_CBDarwinStateNotifier
+ __OBJC_CLASS_RO_$_CBDisplayStatusBroadcaster
+ __OBJC_CLASS_RO_$_CBRampProfileLinear
+ __OBJC_CLASS_RO_$_CBRampProfileSpring
+ __OBJC_LABEL_PROTOCOL_$_CBRampProfile
+ __OBJC_LABEL_PROTOCOL_$_CBSMCKey
+ __OBJC_LABEL_PROTOCOL_$_CBStateNotifier
+ __OBJC_METACLASS_RO_$_CBDarwinStateNotifier
+ __OBJC_METACLASS_RO_$_CBDisplayStatusBroadcaster
+ __OBJC_METACLASS_RO_$_CBRampProfileLinear
+ __OBJC_METACLASS_RO_$_CBRampProfileSpring
+ __OBJC_PROTOCOL_$_CBRampProfile
+ __OBJC_PROTOCOL_$_CBSMCKey
+ __OBJC_PROTOCOL_$_CBStateNotifier
+ __PROPERTIES_ALSSensitivityFilter
+ __PROTOCOLS__TtC14CoreBrightnessP33_6B340E709F1569E35356F761E538365910SMCKeyImpl
+ __ZN14CoreBrightness19lookupValueWithAxisIfEET_NSt3__16vectorIS1_NS2_9allocatorIS1_EEEES6_S1_
+ __ZN4AABC13setTrustedALSEPNS_3ALSE
+ __ZN4AABC20logTrustedALSSummaryEPNS_3ALSE
+ __ZN4AABC22BrightnessRestrictionsD2Ev
+ __ZN4AABC39BrightnessRestrictionMultiPointValues_saSERKS0_
+ ___24-[BLControl clearPILSet]_block_invoke
+ ___29-[BLControl clearKeyboardSet]_block_invoke
+ ___29-[VMDisplayModule invalidate]_block_invoke
+ ___35-[CBHIDEventManager addHIDService:]_block_invoke_2
+ ___38-[CBHIDEventManager removeHIDService:]_block_invoke_2
+ ___41-[CBHIDEventManager addUnfilteredClient:]_block_invoke
+ ___45-[VMDisplayModule setPropertyOnQueue:forKey:]_block_invoke
+ ___52-[BacklightDriverPWM _scheduleFrequencySettleAfter:]_block_invoke
+ ___58-[VMBLControl sendHeadroomRequest:forDisplayUUID:builtIn:]_block_invoke
+ ___70-[CBIndicatorBrightnessModule registerForThermalPressureNotifications]_block_invoke
+ ___70-[VMBLControl sendBrightnessTransactionRequestForDisplayUUID:builtIn:]_block_invoke
+ ___73-[BacklightDriverPWM _setNits:withFadeSpeed:minPWMPercentage:completion:]_block_invoke
+ ___90-[CBRampManager insertNewRampOrigin:target:length:frequency:startRamp:identifier:profile:]_block_invoke
+ ___CBU_IsDisplayStatusAggregationEnabled_block_invoke
+ ___DisplayApplyDynamicSliderRestriction
+ ____ZN4AABC20logTrustedALSSummaryEPNS_3ALSE_block_invoke
+ ___block_descriptor_40_e8_32b_e33_v16?0r^{?=IIQQQQIBBBfffQIBQQfB}8l
+ ___block_descriptor_40_e8_32o_e36_v24?0"<CBHIDServiceProtocol>"8^B16l
+ ___block_descriptor_40_e8_32o_e45_v32?08"CBKeyboardBacklightContainer"16^B24l
+ ___block_descriptor_40_e8_32o_e71_v32?08"CBContainer<CBContainerProtocol><CBHIDServiceProtocol>"16^B24l
+ ___block_descriptor_40_e8_32r_e8_v12?0i8l
+ ___block_descriptor_40_e8_32w_e5_v8?0l
+ ___block_descriptor_49_e8_32o40o_e15_v32?08Q16^B24l
+ ___block_descriptor_49_e8_32o40o_e5_v8?0l
+ ___block_descriptor_56_e8_32o_e35_v24?0^{__IOHIDServiceClient=}8^v16l
+ ___block_descriptor_57_e8_32o40o48o_e5_v8?0l
+ ___block_descriptor_58_e8_32s40bs_e5_v8?0l
+ ___copy_helper_block_e8_32w
+ ___destroy_helper_block_e8_32w
+ ___sincosf_stret
+ ___swift_memcpy512_8
+ ___swift_memcpy56_8
+ ___swift_memcpy5_4
+ ___swift_memcpy8_8
+ _interpolate_value_in_table
+ _kCBSPIBrightnessCommitUpdate
+ _kCBSPIBrightnessCommitUpdateNitsFinal
+ _kCBSPIBrightnessCommitUpdateNitsInitial
+ _kOSThermalNotificationPressureLevelName
+ _load_mapping_table_from_defaults
+ _mapping_table_is_valid
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_msgSend$CEModulePropertyHandler:key:
+ _objc_msgSend$_cacheNormalizer
+ _objc_msgSend$_noteLevelWriteForFrequencySettle:
+ _objc_msgSend$_reportDuty:
+ _objc_msgSend$_scheduleFrequencySettleAfter:
+ _objc_msgSend$_setNits:withFadeSpeed:minPWMPercentage:completion:
+ _objc_msgSend$_springValAtT:
+ _objc_msgSend$addUnfilteredClient:
+ _objc_msgSend$alwaysRequestMaxHeadroom
+ _objc_msgSend$alwaysRequestMaxHeadroom:
+ _objc_msgSend$arrayForKey:
+ _objc_msgSend$bootNits
+ _objc_msgSend$brightnessCommitUpdate:
+ _objc_msgSend$callBlockWithProperty:value:origin:
+ _objc_msgSend$clearCachedALSEvents
+ _objc_msgSend$clearKeyboardSet
+ _objc_msgSend$clearPILSet
+ _objc_msgSend$coexDescription:
+ _objc_msgSend$colorSensitivity
+ _objc_msgSend$convertNitsToPWMPercentage:minPWMPercentage:
+ _objc_msgSend$copyCachedInferenceForEvent:
+ _objc_msgSend$copyFloatVector
+ _objc_msgSend$copyNSNumberForKey:client:handle:andError:
+ _objc_msgSend$crossedColorThreshold::
+ _objc_msgSend$crossedLuxThreshold::
+ _objc_msgSend$currentTimeUs
+ _objc_msgSend$dutyKey
+ _objc_msgSend$getBrightnessCapabilities
+ _objc_msgSend$handleDisplayBrightnessFactorUpdate:
+ _objc_msgSend$handleDisplayPowerStateEvent:
+ _objc_msgSend$hasAnyCoexForALS:type:
+ _objc_msgSend$initWithFrameInfoProvider:
+ _objc_msgSend$initWithIdentifier:configuration:
+ _objc_msgSend$initWithNotificationName:logCategory:
+ _objc_msgSend$initWithOptions:capacity:
+ _objc_msgSend$insertNewRampOrigin:target:length:frequency:startRamp:identifier:profile:
+ _objc_msgSend$invalidateInferenceCache
+ _objc_msgSend$isEventOverThreshold:comparedTo:
+ _objc_msgSend$luxAbsoluteSensitivity
+ _objc_msgSend$luxRelativeSensitivity
+ _objc_msgSend$maxPotentialEDRHeadroom
+ _objc_msgSend$maxPotentialEDRHeadroomForDisplay:
+ _objc_msgSend$nitsUpdateLogType
+ _objc_msgSend$normalizedOutputForProgress:
+ _objc_msgSend$observerSlug:
+ _objc_msgSend$prettyDescription
+ _objc_msgSend$refreshKeys
+ _objc_msgSend$registerForThermalPressureNotifications
+ _objc_msgSend$resetUserAdjustmentState
+ _objc_msgSend$sendBrightnessTransactionRequestOnQueueForDisplayUUID:builtIn:
+ _objc_msgSend$sendHeadroomRequestOnQueue:forDisplayUUID:builtIn:
+ _objc_msgSend$setColorAdaptationActive:
+ _objc_msgSend$setColorSensitivity:
+ _objc_msgSend$setDutyCycle:dynamicFrequency:
+ _objc_msgSend$setDutyKey:
+ _objc_msgSend$setEnabled:commit:applyEnablePulse:
+ _objc_msgSend$setFrameInfoProvider:
+ _objc_msgSend$setFrameInfoProviderForProxy:
+ _objc_msgSend$setLuxAbsoluteSensitivity:
+ _objc_msgSend$setLuxRelativeSensitivity:
+ _objc_msgSend$setPropertyOnQueue:forKey:
+ _objc_msgSend$shouldDiscardALSEvent:
+ _objc_msgSend$shouldHintSILOnForEventTimestampUs:
+ _objc_msgSend$shouldRunInferenceAtTime:
+ _objc_msgSend$string
+ _objc_msgSend$thermalPressureNotificationHandler:
+ _objc_msgSend$writeFloat:
+ _objc_msgSend$writeFloat:throttled:
+ _save_mapping_table_to_defaults
+ _swift_isaMask
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic So8CBSMCLibC
+ _symbolic Spy_____G So13smc_connect_ta
+ _symbolic _____ 14CoreBrightness10SMCKeyImpl33_6B340E709F1569E35356F761E5383659LLC
+ _symbolic _____ 14CoreBrightness10SMCKeyImpl33_6B340E709F1569E35356F761E5383659LLC7PendingO
+ _symbolic _____ So10SMCKeyAttra
+ _symbolic _____ So10SMCKeyInfoa
+ _symbolic _____ So10SMCKeyInfoa20__Unnamed_union_infoV
+ _symbolic _____ So13smc_connect_ta
+ _symbolic _____ So16SMCNumericOutputa
+ _symbolic _____ So24SMCProgrammableAccumDataa
+ _symbolic _____ So25SMCProgrammableAccumParama
+ _symbolic _____ s5UInt8V
+ _symbolic _____Sg 8Dispatch0A4TimeV
+ _symbolic _____Sg s13OpaquePointerV
+ _symbolic ______A3At So24SMCProgrammableAccumDataa
+ _symbolic ______A3At s6UInt32V
+ _type_layout_string So10SMCKeyAttra
+ _type_layout_string So10SMCKeyInfoa
+ _type_layout_string So13smc_connect_ta
+ _type_layout_string So24SMCProgrammableAccumDataa
+ _type_layout_string So25SMCProgrammableAccumParama
- -[BLControl callBlockWithProperty:value:]
- -[CBColorModuleShared CEOverridePropertyHandler:key:]
- -[CBDarwinBrightnessLevelNotifier dealloc]
- -[CBDarwinBrightnessLevelNotifier init]
- -[CBDarwinBrightnessLevelNotifier publishState:]
- -[CBRingLight getStatusInfo]
- -[VMBLControl requestBrightnessTransactionForDisplayUUID:builtIn:]
- GCC_except_table138
- GCC_except_table140
- GCC_except_table144
- GCC_except_table152
- GCC_except_table156
- GCC_except_table157
- GCC_except_table160
- GCC_except_table161
- GCC_except_table165
- GCC_except_table166
- GCC_except_table174
- GCC_except_table175
- GCC_except_table180
- GCC_except_table181
- GCC_except_table210
- GCC_except_table40
- GCC_except_table54
- GCC_except_table59
- GCC_except_table61
- GCC_except_table62
- GCC_except_table65
- GCC_except_table70
- GCC_except_table71
- GCC_except_table98
- OBJC_IVAR_$_CBCPMSModule._currentSDRNits
- OBJC_IVAR_$_CBDarwinBrightnessLevelNotifier._logHandle
- OBJC_IVAR_$_CBDarwinBrightnessLevelNotifier._token
- OBJC_IVAR_$_CBRingLight._overridenByUser
- _OBJC_CLASS_$_CBDarwinBrightnessLevelNotifier
- _OBJC_METACLASS_$_CBDarwinBrightnessLevelNotifier
- __55-[BacklightDriverPWM setNits:withFadeSpeed:completion:]_block_invoke
- __DisplayGetDeviceBrightnessAfterDynamicSliderAdjustment
- __OBJC_$_INSTANCE_METHODS_CBDarwinBrightnessLevelNotifier
- __OBJC_$_INSTANCE_VARIABLES_CBDarwinBrightnessLevelNotifier
- __OBJC_$_PROP_LIST_CBDarwinBrightnessLevelNotifier
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBBrightnessLevelNotifier
- __OBJC_$_PROTOCOL_METHOD_TYPES_CBBrightnessLevelNotifier
- __OBJC_$_PROTOCOL_REFS_CBBrightnessLevelNotifier
- __OBJC_CLASS_PROTOCOLS_$_CBDarwinBrightnessLevelNotifier
- __OBJC_CLASS_RO_$_CBDarwinBrightnessLevelNotifier
- __OBJC_LABEL_PROTOCOL_$_CBBrightnessLevelNotifier
- __OBJC_METACLASS_RO_$_CBDarwinBrightnessLevelNotifier
- __OBJC_PROTOCOL_$_CBBrightnessLevelNotifier
- ___55-[BacklightDriverPWM setNits:withFadeSpeed:completion:]_block_invoke
- ___block_descriptor_40_e8_32b_e32_v16?0r^{?=IIQQQQIBBBfffQIBQQf}8l
- ___block_descriptor_54_e8_32s40bs_e5_v8?0l
- _objc_msgSend$CEOverridePropertyHandler:key:
- _objc_msgSend$callBlockWithProperty:value:
- _objc_msgSend$requestBrightnessTransactionForDisplayUUID:builtIn:
- _objc_msgSend$setWithSet:
- _objc_msgSend$terminateConnection:
CStrings:
+ "%@<%@>"
+ "%@@%@ with %@"
+ "-[BrightnessSystemClient unregisterObserver:]"
+ "4"
+ "Add unfiltered client %@"
+ "Brightness factor = %f, clear cached ALS events"
+ "BrightnessCommitUpdate"
+ "BrightnessLevelNotifier"
+ "BrightnessRestrictionsFromPreferences"
+ "CECadence"
+ "CPMSCurrentHDRNits"
+ "CoreBrightness.SMCKeyImpl"
+ "CoreBrightness_Internal.CBSMCLib"
+ "Display on seeded by handoff — skipping snap to own curve"
+ "Display will wake, clear cached ALS events"
+ "DisplayIntegrated"
+ "DisplayStatusNotifier"
+ "EXBrightSILStateTrusted"
+ "Enabling device without enable pulse"
+ "Failed to write %f to SMC key %s (%hhd)"
+ "Harmony supported?? %d"
+ "HarmonyShiftA"
+ "HarmonyShiftB"
+ "HarmonyStrength"
+ "Ignoring %{public}@: expected %zu levels, got %lu"
+ "Ignoring %{public}@: not ascending: %{public}@"
+ "Ignoring negative CE cadence %f"
+ "Initial thermal pressure level: %llu"
+ "Loaded Restriction Dictionary (Dynamic Slider Configuration) from defaults (StoreDemoMode = %d): %@"
+ "OverriddenByUser"
+ "Overriding Boot-nits: %.2f -> %.2f nits"
+ "PresetHostAlwaysRequestMaxHeadroom"
+ "PresetHostMaxPotentialEDRHeadroom"
+ "Presets(%lu): always request max headroom = %d"
+ "Presets(%lu): maxPotentialEDRHeadroom: %@"
+ "SIL OFF @ %llu us (was ON for %llu us)"
+ "SIL ON @ %llu us"
+ "SMC key %s unavailable on this platform (%hhd)"
+ "SMC key name %s is not four characters"
+ "Semantic ambient lux levels: %{public}@"
+ "Setting CE inference cadence to %f s"
+ "Setting PWM duty cycle to: %llu at %llu Hz"
+ "Thermal Pressure Critical! Snapping to target indicator brightness %f"
+ "Thermal pressure level changed: %llu -> %llu"
+ "TrueTone: shift-a = %f, shift-b = %f"
+ "Trusted ALS updated: %{public}@"
+ "Unable to open an SMC connection; missing the entitlement?"
+ "Wrote %f to SMC key %s"
+ "[%@]"
+ "[%@]cached strength: %.2f, confidence: %f"
+ "[BRT update: %s]: Begin slider drag"
+ "[BRT update: %s]: begin ramp L: %0.2f -> %0.2f P: %0.2f -> %0.2f (hwMax-perceptual) t: %f rate: %0.2f nits/s %0.2fhz"
+ "[CPMS] Current HDR brightness updated: %f -> %f"
+ "[CPMS] Sending nits cap ramp to display: target=%f duration=%fs start=%f"
+ "[CPMS] Using current HDR nits (%f) instead of cap (%f) for ramp duration calculation"
+ "[Color Mitigation] lux=%.1f nits=%.1f mitigated=%d ceEnabled=%d ttActive=%d ceAttempted=%d source=%s confidence=%.3f threshold=%.3f crossedThreshold=%d strength=%.3f"
+ "[Display] CPMS cap ramp: seeding origin %f -> %f (target %f, headroom %f)"
+ "[Display] CPMS ramp request: target=%f duration=%f start=%f"
+ "[Dynamic Slider] MAX - failed to convert thresholds or factors to a float vector"
+ "[Dynamic Slider] MAX - missing thresholds or factors"
+ "[Dynamic Slider] MAX - thresholds and factors differ in size (%zu vs %zu)"
+ "[Dynamic Slider] MAX - thresholds and factors need at least 1 entry"
+ "[Dynamic Slider] MAX - thresholds or factors are not arrays"
+ "[Dynamic Slider] MAX - thresholds or factors not sorted in ascending order"
+ "[Dynamic Slider] MIN - failed to convert thresholds or factors to a float vector"
+ "[Dynamic Slider] MIN - missing thresholds or factors"
+ "[Dynamic Slider] MIN - thresholds and factors differ in size (%zu vs %zu)"
+ "[Dynamic Slider] MIN - thresholds and factors need at least 1 entry"
+ "[Dynamic Slider] MIN - thresholds or factors are not arrays"
+ "[Dynamic Slider] MIN - thresholds or factors not sorted in ascending order"
+ "[Observer] Adding %@"
+ "[Observer] Not adding %@ - no observable properties"
+ "[Observer] Observed keys 🔑: %@ - %@ + %@ = %@"
+ "[Observer] Refreshing %@"
+ "[Observer] Removing %@ since the set of properties become empty."
+ "[Observer] Unregistering %@"
+ "[SIL Hint] Received MIB while SIL OFF, turning SIL ON... (mibTs=%llu, lastSILOffTs=%llu)"
+ "[dcpRoleID=%d] [ReadBack] Couldn't fetch SIL state!"
+ "[dcpRoleID=%d] [ReadBack] SIL=%d"
+ "[dcpRoleID=%d] [ReadBack] SIL=%d, sessionID=%u"
+ "[dcpRoleID=%d] [WillSend] SIL=%d"
+ "[dcpRoleID=%d] [WillSend] SIL=%d failed!"
+ "_S=%f"
+ "cleared"
+ "com.apple.CoreBrightness.BacklightDriverPWM"
+ "com.apple.CoreBrightness.CBSMCLib"
+ "com.apple.CoreBrightness.DisplayStatusBroadcaster"
+ "com.apple.iokit.hid.displayStatus"
+ "crgb lookup: found=%d parsed=%d value=%d"
+ "dropping departed display %{public}@"
+ "frame info provider %s"
+ "no valid token for %@; dropping state=%llu"
+ "notify_get_state failed with %d for token %d"
+ "notify_post failed for %@ (status=%u)"
+ "notify_register_dispatch failed with %d for %s"
+ "notify_set_state failed for %@ (status=%u)"
+ "orient=%d lux=%.2f coex=%@"
+ "override-boot-brightness-nits"
+ "published"
+ "publishing display status state=%llu"
+ "seeding displayID=%lu on=%d"
+ "semantic-lux-levels"
+ "startNits"
+ "truetone-shift-a"
+ "truetone-shift-b"
+ "trusted={%@} "
+ "v16@?0r^{?=IIQQQQIBBBfffQIBQQfB}8"
+ "v24@?0@\"<CBHIDServiceProtocol>\"8^B16"
+ "v32@?0@8@\"CBContainer<CBContainerProtocol><CBHIDServiceProtocol>\"16^B24"
+ "v32@?0@8@\"CBKeyboardBacklightContainer\"16^B24"
+ "{%@} "
- "CPMSCurrentSDRNits"
- "Can't talk to PWM driver. Return code = %d"
- "OverridenByUser"
- "Registered observer %@ with handle %@, properties %@. Subscribing to the following new keys: %@"
- "Removing observer %@ with handle %@. Unregistering the following keys: %@"
- "SIL OFF @ %f us (was ON for %f us)"
- "SIL ON @ %f us"
- "Setting PWM duty cycle to: %llu"
- "[%x]: _S=%f"
- "[CPMS] Current SDR brightness updated: %f -> %f"
- "[CPMS] Sending nits cap ramp to display: target=%f duration=%fs"
- "[CPMS] Using current SDR nits (%f) instead of cap (%f) for ramp duration calculation"
- "[Color Mitigation] lux=%.1f nits=%.1f mitigated=%d ceEnabled=%d ceAttempted=%d source=%s confidence=%.3f threshold=%.3f crossedThreshold=%d strength=%.3f"
- "[Display] CPMS ramp request: target=%f duration=%f"
- "[SIL Hint] Received MIB while SIL OFF, turning SIL ON..."
- "[SIL Hint] now=%f motMet=%d shouldUseHint=%d"
- "[dcpRoleID=%d] SIL=%d, monotonicTimeUS=%llu. Sending to EXBright: %@."
- "com.apple.CoreBrightness.BrightnessLevelNotifier"
- "error: unknown notification type (%@)"
- "failed to terminate SKL client (%@)"
- "harmony HW not supported"
- "harmony HW supported"
- "key=%@ (type=%tu) value=%@  block=%p queue=%p"
- "key=%@ property=%@ queue=%p clientBlock=%p"
- "v16@?0r^{?=IIQQQQIBBBfffQIBQQf}8"
```
