## GameController

> `/System/Library/Frameworks/GameController.framework/GameController`

```diff

-13.3.1.0.0
-  __TEXT.__text: 0x107658
-  __TEXT.__auth_stubs: 0x1c30
+13.4.8.0.0
+  __TEXT.__text: 0x10a62c
+  __TEXT.__auth_stubs: 0x1bf0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xff2c
-  __TEXT.__const: 0x3d44
-  __TEXT.__cstring: 0xa419
-  __TEXT.__gcc_except_tab: 0x59ec
-  __TEXT.__oslogstring: 0x97d8
+  __TEXT.__objc_methlist: 0xfa7c
+  __TEXT.__const: 0x1c34
+  __TEXT.__gcc_except_tab: 0x58fc
+  __TEXT.__cstring: 0x9fe4
+  __TEXT.__oslogstring: 0x97b8
   __TEXT.__dlopen_cstrs: 0xfd
-  __TEXT.__swift5_typeref: 0x574
+  __TEXT.__swift5_typeref: 0x57c
   __TEXT.__swift5_reflstr: 0x22f
   __TEXT.__swift5_assocty: 0x2c8
   __TEXT.__constg_swiftt: 0x55c

   __TEXT.__swift5_types: 0x60
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0xc4
-  __TEXT.__unwind_info: 0x5400
-  __TEXT.__eh_frame: 0xf8
-  __TEXT.__objc_classname: 0x41b3
-  __TEXT.__objc_methname: 0x1920b
-  __TEXT.__objc_methtype: 0x7bdd
-  __TEXT.__objc_stubs: 0xf640
-  __DATA_CONST.__got: 0xba8
-  __DATA_CONST.__const: 0x2db0
-  __DATA_CONST.__objc_classlist: 0x990
-  __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x7e0
+  __TEXT.__unwind_info: 0x5550
+  __TEXT.__eh_frame: 0x40
+  __TEXT.__objc_classname: 0x4033
+  __TEXT.__objc_methname: 0x18f0c
+  __TEXT.__objc_methtype: 0x763d
+  __TEXT.__objc_stubs: 0xf560
+  __DATA_CONST.__got: 0xb88
+  __DATA_CONST.__const: 0x2db8
+  __DATA_CONST.__objc_classlist: 0x970
+  __DATA_CONST.__objc_catlist: 0xc0
+  __DATA_CONST.__objc_protolist: 0x778
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5358
-  __DATA_CONST.__objc_protorefs: 0x4f0
-  __DATA_CONST.__objc_superrefs: 0x8c8
+  __DATA_CONST.__objc_selrefs: 0x5268
+  __DATA_CONST.__objc_protorefs: 0x468
+  __DATA_CONST.__objc_superrefs: 0x8b0
   __DATA_CONST.__objc_arraydata: 0x570
-  __AUTH_CONST.__auth_got: 0xe30
-  __AUTH_CONST.__const: 0x1fb8
-  __AUTH_CONST.__cfstring: 0xb8c0
-  __AUTH_CONST.__objc_const: 0x49440
+  __AUTH_CONST.__auth_got: 0xe10
+  __AUTH_CONST.__const: 0x1f58
+  __AUTH_CONST.__cfstring: 0xb6a0
+  __AUTH_CONST.__objc_const: 0x48580
   __AUTH_CONST.__objc_intobj: 0x14a0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x5010
+  __AUTH.__objc_data: 0x4ed0
   __AUTH.__data: 0xe0
-  __DATA.__objc_ivar: 0x17bc
-  __DATA.__data: 0x5e10
+  __DATA.__objc_ivar: 0x1758
+  __DATA.__data: 0x58f0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1f20
+  __DATA.__bss: 0x1f40
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x228
+  __DATA_DIRTY.__bss: 0x220
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation
+  - /System/Library/PrivateFrameworks/GameControllerIO.framework/GameControllerIO
   - /System/Library/PrivateFrameworks/GameControllerSettings.framework/GameControllerSettings
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: AEE28012-76CB-3931-AF8D-FF15EBD56DC4
-  Functions: 7407
-  Symbols:   27513
-  CStrings:  9871
+  UUID: BA6EA3A9-9B5B-318E-BD92-F43BE9D88DA1
+  Functions: 7394
+  Symbols:   27537
+  CStrings:  9695
 
Symbols:
+ -[GCVirtualController initWithConfiguration:].cold.3
+ -[GCVirtualController initWithConfiguration:].cold.4
+ -[_GCDefaultLogicalDevice updateForNewActiveClient]
+ -[_GCGamepadEventImpl leftSideButton]
+ -[_GCGamepadEventImpl rightSideButton]
+ -[_GCGamepadEventImpl setLeftSideButton:]
+ -[_GCGamepadEventImpl setRightSideButton:]
+ -[_GCHapticEvent(Private) evaluateDeviceNoteParams:]
+ -[_GCHapticEvent(Private) initWithSyntheticCommand:]
+ -[_GCHapticEvent(Private) valueForNoteParam:inParameters:]
+ GCC_except_table80
+ _$s10Foundation4UUIDVSgMR
+ _$s10Foundation4UUIDVSgMd
+ _$s10Foundation4UUIDVSgWOb
+ _$s10Foundation4UUIDVSgWOhTm
+ _$s14GameController19GCButtonElementNameV14leftSideButtonACvau
+ _$s14GameController19GCButtonElementNameV14leftSideButtonACvgZ
+ _$s14GameController19GCButtonElementNameV14leftSideButtonACvpZ
+ _$s14GameController19GCButtonElementNameV14leftSideButtonACvpZMV
+ _$s14GameController19GCButtonElementNameV14leftSideButton_WZ
+ _$s14GameController19GCButtonElementNameV14leftSideButton_Wz
+ _$s14GameController19GCButtonElementNameV15rightSideButtonACvau
+ _$s14GameController19GCButtonElementNameV15rightSideButtonACvgZ
+ _$s14GameController19GCButtonElementNameV15rightSideButtonACvpZ
+ _$s14GameController19GCButtonElementNameV15rightSideButtonACvpZMV
+ _$s14GameController19GCButtonElementNameV15rightSideButton_WZ
+ _$s14GameController19GCButtonElementNameV15rightSideButton_Wz
+ _$sSD8_VariantV11removeValue6forKeyq_Sgx_tFSS_10Foundation4UUIDVTg5
+ _$ss10_HashTableV12previousHole6beforeAB6BucketVAF_tF
+ _$ss17_NativeDictionaryV7_delete2atys10_HashTableV6BucketV_tFSS_10Foundation4UUIDVTg5
+ _GCInputLeftSideButton
+ _GCInputProgrammableButton1
+ _GCInputProgrammableButton2
+ _GCInputProgrammableButton3
+ _GCInputProgrammableButton4
+ _GCInputProgrammableButton5
+ _GCInputRightSideButton
+ _OBJC_IVAR_$__GCDevicePhysicalInputComponent._cached_collectionEventBufferCount
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ __OBJC_$_CATEGORY_INSTANCE_METHODS__GCHapticEvent_$_Private
+ __OBJC_$_CATEGORY__GCHapticEvent_$_Private
+ __ZN18SharableMemoryBase14AllocNonSharedEm.cold.1
+ ___block_descriptor_48_e8_32w_e23_v16?0^{__IOHIDEvent=}8lw32l8
+ ___block_descriptor_56_e8_32s40w_e23_v16?0^{__IOHIDEvent=}8lw40l8s32l8
+ ___block_literal_global.252
+ ___block_literal_global.50
+ __swift_dead_method_stub
+ _block_copy_helper.16
+ _block_copy_helper.22
+ _block_copy_helper.31
+ _block_copy_helper.37
+ _block_copy_helper.43
+ _block_copy_helper.49
+ _block_copy_helper.55
+ _block_copy_helper.61
+ _block_copy_helper.67
+ _block_descriptor.18
+ _block_descriptor.24
+ _block_descriptor.33
+ _block_descriptor.39
+ _block_descriptor.45
+ _block_descriptor.51
+ _block_descriptor.57
+ _block_descriptor.63
+ _block_descriptor.69
+ _block_destroy_helper.17
+ _block_destroy_helper.23
+ _block_destroy_helper.32
+ _block_destroy_helper.38
+ _block_destroy_helper.44
+ _block_destroy_helper.50
+ _block_destroy_helper.56
+ _block_destroy_helper.62
+ _block_destroy_helper.68
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$changedElements
+ _objc_msgSend$controllerToProfileMappings
+ _objc_msgSend$current
+ _objc_msgSend$defaultIdentifier
+ _objc_msgSend$defaultProfile
+ _objc_msgSend$defaultProfileUUID
+ _objc_msgSend$gcsController_initWithController:
+ _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$initWithBundleIdentifier:title:controllerToProfileMappings:controllerToCompatibilityModeMappings:
+ _objc_msgSend$initWithJSONObject:
+ _objc_msgSend$jsonObject
+ _objc_msgSend$localizedNameWithPreferredLocalizations:
+ _objc_msgSend$setStartTime:
+ _objectdestroy.14Tm
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _symbolic _____Sg 10Foundation4UUIDV
- +[GCHapticMotor supportsSecureCoding]
- +[_GCHapticEvent(NSSecureCoding) supportsSecureCoding]
- +[_GCXRComponent componentWithPhysicalInputProfile:]
- -[GCControllerTouchpad setValueForXAxis:yAxis:touchDown:buttonValue:].cold.1
- -[GCHapticMotor .cxx_destruct]
- -[GCHapticMotor amplitude]
- -[GCHapticMotor applyValuesFrom:]
- -[GCHapticMotor copyWithZone:]
- -[GCHapticMotor description]
- -[GCHapticMotor drainQueuedTransients]
- -[GCHapticMotor encodeWithCoder:]
- -[GCHapticMotor enqueueHapticTransientEvent:]
- -[GCHapticMotor features]
- -[GCHapticMotor frequency]
- -[GCHapticMotor index]
- -[GCHapticMotor initWithCoder:]
- -[GCHapticMotor initWithIndex:]
- -[GCHapticMotor initWithIndex:name:]
- -[GCHapticMotor initWithIndex:name:features:]
- -[GCHapticMotor initWithIndex:name:features:frequency:amplitude:]
- -[GCHapticMotor init]
- -[GCHapticMotor name]
- -[GCHapticMotor queuedTransients]
- -[GCHapticMotor setAmplitude:]
- -[GCHapticMotor setFrequency:]
- -[GCHapticMotor setQueuedTransients:]
- -[GCPhysicalInputProfile capture].cold.1
- -[GCPhysicalInputProfile capture].cold.2
- -[GCPhysicalInputProfile setStateFromPhysicalInput:].cold.1
- -[_GCHandSkeleton .cxx_destruct]
- -[_GCHandSkeleton _boneDataWithMotionRange:curlAmts:]
- -[_GCHandSkeleton _boneDataWithMotionRangeDq:curlAmts:]
- -[_GCHandSkeleton _convertToModelSpaceUsingDQs:]
- -[_GCHandSkeleton _convertToModelSpaceUsingMatrices:]
- -[_GCHandSkeleton _setInterpolationMethod:]
- -[_GCHandSkeleton boneDataWithTransformSpace:motionRange:]
- -[_GCHandSkeleton boneDataWithTransformSpace:referencePose:]
- -[_GCHandSkeleton boneDataWithTransformSpace:referencePose:].cold.1
- -[_GCHandSkeleton fingerPositionsChangedForCurlAmts:]
- -[_GCHandSkeleton getFingerCurlAmt:boneType:]
- -[_GCHandSkeleton initWithBoneData:profile:handedness:]
- -[_GCHandSkeleton rightHand]
- -[_GCHapticEvent description]
- -[_GCHapticEvent evaluateDeviceNoteParams:]
- -[_GCHapticEvent identifier]
- -[_GCHapticEvent initWithSyntheticCommand:]
- -[_GCHapticEvent intensity]
- -[_GCHapticEvent setIdentifier:]
- -[_GCHapticEvent setIntensity:]
- -[_GCHapticEvent setSharpness:]
- -[_GCHapticEvent setStartTime:]
- -[_GCHapticEvent setStopped:]
- -[_GCHapticEvent setTransientBeganAsContinuousEvent:]
- -[_GCHapticEvent setType:]
- -[_GCHapticEvent sharpness]
- -[_GCHapticEvent startTime]
- -[_GCHapticEvent stopped]
- -[_GCHapticEvent transientBeganAsContinuousEvent]
- -[_GCHapticEvent type]
- -[_GCHapticEvent valueForNoteParam:inParameters:]
- -[_GCHapticEvent(NSSecureCoding) encodeWithCoder:]
- -[_GCHapticEvent(NSSecureCoding) initWithCoder:]
- -[_GCPhysicalInputFilteredElementCollection _filteredElements].cold.1
- -[_GCXRComponent .cxx_destruct]
- -[_GCXRComponent handSkeletons]
- -[_GCXRComponent identifier]
- -[_GCXRComponent initWithIdentifier:]
- -[_GCXRComponent setController:]
- -[_GCXRComponent setHandSkeletons:]
- -[_GCXRComponent setIdentifier:]
- -[_GCXRComponent updateSkeletons]
- _$s14GameController22GCOverlaySettingsStoreC8profilesSaySo10GCSProfileCGvpfiTm
- _$sSTsE8contains5whereS2b7ElementQzKXE_tKFSaySSG_Tg5
- _$sSTsSQ7ElementRpzrlE8containsySbABFSbABXEfU_SaySSG_TG5TA
- _$sSo26GCDevicePhysicalInputStateP14GameControllerE8elementsAC010GCPhysicalC17ElementCollectionVySo0hcI0_pGvgTm
- _$sSo7GCSGameC14GameControllerE13profileExists3for4withSbSo13GCSControllerC_AC22GCOverlaySettingsStoreCtFSbSo10GCSProfileCXEfU_TA
- _$sSo7GCSGameC14GameControllerE7profile3for4withSo10GCSProfileCSo13GCSControllerC_AC22GCOverlaySettingsStoreCtFSbAHXEfU_TA
- _$sSo7GCSGameC14GameControllerE7profile3for4withSo10GCSProfileCSo13GCSControllerC_AC22GCOverlaySettingsStoreCtFSbAHXEfU_Tm
- _$ss14_ArrayProtocolPsE6filterySay7ElementQzGSbAEKXEKFSaySo10GCSProfileCG_Tg5
- _$sypSgWOhTm
- _GCAdaptiveTriggersServiceClientInterface
- _GCAdaptiveTriggersServiceServerInterface
- _GCBatteryServiceClientInterface
- _GCBatteryServiceServerInterface
- _GCGameIntentServiceClientInterface
- _GCGameIntentServiceServerInterface
- _GCGenericDeviceDriverConfigurationServiceClientInterface
- _GCGenericDeviceDriverConfigurationServiceServerInterface
- _GCHandSkeletonAny
- _GCHandSkeletonLeft
- _GCHandSkeletonRight
- _GCIdleServiceClientInterface
- _GCIdleServiceServerInterface
- _GCLightServiceClientInterface
- _GCLightServiceServerInterface
- _GCMotionServiceClientInterface
- _GCMotionServiceServerInterface
- _GCNintendoJoyConFusionGestureServiceClientInterface
- _GCNintendoJoyConFusionGestureServiceServerInterface
- _GCPropertyValueHandedness
- _GCXRPropertyButtonFingerIndex
- _GCXRPropertyButtonFingerMiddle
- _GCXRPropertyButtonFingerPinky
- _GCXRPropertyButtonFingerRing
- _GCXRPropertyButtonFingerThumb
- _OBJC_CLASS_$_GCHapticMotor
- _OBJC_CLASS_$__GCHandSkeleton
- _OBJC_CLASS_$__GCXRComponent
- _OBJC_IVAR_$_GCHapticMotor._amplitude
- _OBJC_IVAR_$_GCHapticMotor._features
- _OBJC_IVAR_$_GCHapticMotor._frequency
- _OBJC_IVAR_$_GCHapticMotor._index
- _OBJC_IVAR_$_GCHapticMotor._name
- _OBJC_IVAR_$_GCHapticMotor._queuedTransients
- _OBJC_IVAR_$__GCHandSkeleton._boneData
- _OBJC_IVAR_$__GCHandSkeleton._handedness
- _OBJC_IVAR_$__GCHandSkeleton._interpolationMethod
- _OBJC_IVAR_$__GCHandSkeleton._lastFingerPositions
- _OBJC_IVAR_$__GCHandSkeleton._physicalInput
- _OBJC_IVAR_$__GCHandSkeleton.referenceDQs
- _OBJC_IVAR_$__GCHandSkeleton.referenceSkeletons
- _OBJC_IVAR_$__GCHapticEvent._identifier
- _OBJC_IVAR_$__GCHapticEvent._intensity
- _OBJC_IVAR_$__GCHapticEvent._sharpness
- _OBJC_IVAR_$__GCHapticEvent._startTime
- _OBJC_IVAR_$__GCHapticEvent._stopped
- _OBJC_IVAR_$__GCHapticEvent._transientBeganAsContinuousEvent
- _OBJC_IVAR_$__GCHapticEvent._type
- _OBJC_IVAR_$__GCXRComponent._controller
- _OBJC_IVAR_$__GCXRComponent._handSkeletons
- _OBJC_IVAR_$__GCXRComponent._identifier
- _OBJC_IVAR_$__GCXRComponent._leftHandSkeleton
- _OBJC_IVAR_$__GCXRComponent._physicalInput
- _OBJC_IVAR_$__GCXRComponent._rightHandSkeleton
- _OBJC_METACLASS_$_GCHapticMotor
- _OBJC_METACLASS_$__GCHandSkeleton
- _OBJC_METACLASS_$__GCHapticEvent
- _OBJC_METACLASS_$__GCXRComponent
- _SetupVirtualGameControllerIfForced
- _SetupVirtualGameControllerIfForced.cold.1
- _SetupVirtualGameControllerIfForced.onceToken
- _VirtualControllerBundle
- _VirtualControllerBundle.cold.1
- _VirtualControllerBundle.cold.2
- _VirtualControllerBundle.cold.3
- __OBJC_$_CLASS_METHODS_GCHapticMotor
- __OBJC_$_CLASS_METHODS__GCHapticEvent(NSSecureCoding)
- __OBJC_$_CLASS_METHODS__GCXRComponent
- __OBJC_$_CLASS_PROP_LIST_GCHapticMotor
- __OBJC_$_INSTANCE_METHODS_GCHapticMotor
- __OBJC_$_INSTANCE_METHODS__GCHandSkeleton
- __OBJC_$_INSTANCE_METHODS__GCHapticEvent(NSSecureCoding)
- __OBJC_$_INSTANCE_METHODS__GCXRComponent
- __OBJC_$_INSTANCE_VARIABLES_GCHapticMotor
- __OBJC_$_INSTANCE_VARIABLES__GCHandSkeleton
- __OBJC_$_INSTANCE_VARIABLES__GCHapticEvent
- __OBJC_$_INSTANCE_VARIABLES__GCXRComponent
- __OBJC_$_PROP_LIST_GCHapticMotor
- __OBJC_$_PROP_LIST_GCXRComponent
- __OBJC_$_PROP_LIST_GCXRComponentProvider
- __OBJC_$_PROP_LIST__GCHandSkeleton
- __OBJC_$_PROP_LIST__GCHapticEvent
- __OBJC_$_PROP_LIST__GCXRComponent
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCAdaptiveTriggersServiceServerInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCBatteryServiceServerInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCGameIntentServiceServerInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCLightServiceServerInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCMotionServiceServerInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCXRComponent
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCXRComponentProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCDriverClientInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCDriverServerInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_GCAdaptiveTriggersServiceServerInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_GCBatteryServiceServerInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_GCGameIntentServiceServerInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_GCLightServiceServerInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_GCMotionServiceServerInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_GCXRComponent
- __OBJC_$_PROTOCOL_METHOD_TYPES_GCXRComponentProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES__GCDriverClientInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES__GCDriverServerInterface
- __OBJC_$_PROTOCOL_REFS_GCXRComponent
- __OBJC_$_PROTOCOL_REFS_GCXRComponentProvider
- __OBJC_$_PROTOCOL_REFS__GCDriverClientInterface
- __OBJC_CLASS_PROTOCOLS_$_GCHapticMotor
- __OBJC_CLASS_PROTOCOLS_$__GCHapticEvent(NSSecureCoding)
- __OBJC_CLASS_PROTOCOLS_$__GCXRComponent
- __OBJC_CLASS_RO_$_GCHapticMotor
- __OBJC_CLASS_RO_$__GCHandSkeleton
- __OBJC_CLASS_RO_$__GCHapticEvent
- __OBJC_CLASS_RO_$__GCXRComponent
- __OBJC_LABEL_PROTOCOL_$_GCAdaptiveTriggersServiceServerInterface
- __OBJC_LABEL_PROTOCOL_$_GCBatteryServiceServerInterface
- __OBJC_LABEL_PROTOCOL_$_GCGameIntentServiceServerInterface
- __OBJC_LABEL_PROTOCOL_$_GCIdleServiceServerInterface
- __OBJC_LABEL_PROTOCOL_$_GCLightServiceClientInterface
- __OBJC_LABEL_PROTOCOL_$_GCLightServiceServerInterface
- __OBJC_LABEL_PROTOCOL_$_GCMotionServiceClientInterface
- __OBJC_LABEL_PROTOCOL_$_GCMotionServiceServerInterface
- __OBJC_LABEL_PROTOCOL_$_GCNintendoJoyConFusionGestureServiceServerInterface
- __OBJC_LABEL_PROTOCOL_$_GCXRComponent
- __OBJC_LABEL_PROTOCOL_$_GCXRComponentProvider
- __OBJC_LABEL_PROTOCOL_$__GCDriverClientInterface
- __OBJC_LABEL_PROTOCOL_$__GCDriverServerInterface
- __OBJC_METACLASS_RO_$_GCHapticMotor
- __OBJC_METACLASS_RO_$__GCHandSkeleton
- __OBJC_METACLASS_RO_$__GCHapticEvent
- __OBJC_METACLASS_RO_$__GCXRComponent
- __OBJC_PROTOCOL_$_GCAdaptiveTriggersServiceServerInterface
- __OBJC_PROTOCOL_$_GCBatteryServiceServerInterface
- __OBJC_PROTOCOL_$_GCGameIntentServiceServerInterface
- __OBJC_PROTOCOL_$_GCIdleServiceServerInterface
- __OBJC_PROTOCOL_$_GCLightServiceClientInterface
- __OBJC_PROTOCOL_$_GCLightServiceServerInterface
- __OBJC_PROTOCOL_$_GCMotionServiceClientInterface
- __OBJC_PROTOCOL_$_GCMotionServiceServerInterface
- __OBJC_PROTOCOL_$_GCNintendoJoyConFusionGestureServiceServerInterface
- __OBJC_PROTOCOL_$_GCXRComponent
- __OBJC_PROTOCOL_$_GCXRComponentProvider
- __OBJC_PROTOCOL_$__GCDriverClientInterface
- __OBJC_PROTOCOL_$__GCDriverServerInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCAdaptiveTriggersServiceClientInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCAdaptiveTriggersServiceServerInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCBatteryServiceClientInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCBatteryServiceServerInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCGameIntentServiceClientInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCGameIntentServiceServerInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCIdleServiceClientInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCIdleServiceServerInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCLightServiceClientInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCLightServiceServerInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCMotionServiceClientInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCMotionServiceServerInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCNintendoJoyConFusionGestureServiceClientInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCNintendoJoyConFusionGestureServiceServerInterface
- __OBJC_PROTOCOL_REFERENCE_$_GCXRComponentProvider
- __OBJC_PROTOCOL_REFERENCE_$__GCDriverClientInterface
- __OBJC_PROTOCOL_REFERENCE_$__GCDriverServerInterface
- __PromotedConst
- ___SetupVirtualGameControllerIfForced_block_invoke
- ___block_descriptor_56_e8_32s_e23_v16?0^{__IOHIDEvent=}8ls32l8u48l8
- ___block_literal_global.253
- ___block_literal_global.51
- ___block_literal_global.59
- ___getGCHIDLogger_block_invoke
- ___isPartnerSupportEnabled_block_invoke
- ___sincosf_stret
- __publishCustomController.cold.1
- __swift_FORCE_LOAD_$_swiftMetal_$_GameController
- __swift_FORCE_LOAD_$_swiftQuartzCore_$_GameController
- _acosf
- _block_copy_helper.21
- _block_copy_helper.27
- _block_copy_helper.33
- _block_copy_helper.39
- _block_copy_helper.45
- _block_copy_helper.51
- _block_copy_helper.57
- _block_copy_helper.63
- _block_copy_helper.69
- _block_descriptor.23
- _block_descriptor.29
- _block_descriptor.35
- _block_descriptor.41
- _block_descriptor.47
- _block_descriptor.53
- _block_descriptor.59
- _block_descriptor.65
- _block_descriptor.71
- _block_destroy_helper.22
- _block_destroy_helper.28
- _block_destroy_helper.34
- _block_destroy_helper.40
- _block_destroy_helper.46
- _block_destroy_helper.52
- _block_destroy_helper.58
- _block_destroy_helper.64
- _block_destroy_helper.70
- _dqAdd
- _dqConjugate
- _dqDLB
- _dqDLB.cold.1
- _dqGetMatrix
- _dqGetMatrix.cold.1
- _dqGetRotation
- _dqGetTranslation
- _dqIdentity
- _dqMakeDualQuaternion
- _dqMul
- _dqMulConst
- _dqNormalize
- _dqNormalize.cold.1
- _dqScLERP
- _gcHIDLogger
- _getGCHIDLogger
- _getGCHIDLogger.cold.1
- _getGCHIDLogger.onceToken
- _hexStringFromByteArray
- _isPartnerSupportEnabled
- _isPartnerSupportEnabled._partnerSupportEnabled
- _isPartnerSupportEnabled.cold.1
- _isPartnerSupportEnabled.onceToken
- _kBoneTypes
- _kGCBoneDataClosedFistBindingLeft
- _kGCBoneDataClosedFistBindingRight
- _kGCBoneDataClosedFistLeft
- _kGCBoneDataClosedFistRight
- _kGCBoneDataRestingBindLeft
- _kGCBoneDataRestingBindRight
- _kGCBoneDataRestingLeft
- _kGCBoneDataRestingRight
- _kLeftSkeletons
- _kRightSkeletons
- _malloc
- _matrix_identity_float4x4
- _objc_msgSend$_boneDataWithMotionRange:curlAmts:
- _objc_msgSend$_boneDataWithMotionRangeDq:curlAmts:
- _objc_msgSend$_convertToModelSpaceUsingDQs:
- _objc_msgSend$_stateTableForSlot:
- _objc_msgSend$amplitude
- _objc_msgSend$componentWithPhysicalInputProfile:
- _objc_msgSend$features
- _objc_msgSend$fingerPositionsChangedForCurlAmts:
- _objc_msgSend$forceVirtualController
- _objc_msgSend$getFingerCurlAmt:boneType:
- _objc_msgSend$handedness
- _objc_msgSend$initWithBoneData:profile:handedness:
- _objc_msgSend$initWithIndex:
- _objc_msgSend$initWithIndex:name:features:
- _objc_msgSend$initWithIndex:name:features:frequency:amplitude:
- _objc_msgSend$setAmplitude:
- _objc_msgSend$setFrequency:
- _objc_msgSend$stringWithCapacity:
- _objc_msgSend$stringWithString:
- _objc_msgSend$updateSkeletons
- _objc_msgSend$uppercaseString
- _objc_retain_x5
- _objc_retain_x9
- _objectdestroy.19Tm
- _parentIndices
- _setGCHIDLoggerCategory
- _sinf
CStrings:
+ "<%@ %p> {\n\t.DpadUp: %@\n\t.DpadDown: %@\n\t.DpadLeft: %@\n\t.DpadRight: %@\n\t.ButtonA: %@\n\t.ButtonB: %@\n\t.ButtonX: %@\n\t.ButtonY: %@\n\t.LeftShoulder: %@\n\t.RightShoulder: %@\n\t.LeftThumbstickUp: %@\n\t.LeftThumbstickDown: %@\n\t.LeftThumbstickLeft: %@\n\t.LeftThumbstickRight: %@\n\t.RightThumbstickUp: %@\n\t.RightThumbstickDown: %@\n\t.RightThumbstickLeft: %@\n\t.RightThumbstickRight: %@\n\t.LeftTrigger: %@\n\t.RightTrigger: %@\n\t.LeftThumbstickButton: %@\n\t.RightThumbstickButton: %@\n\t.LeftSideButton: %@\n\t.RightSideButton: %@\n\t.ButtonHome: %@\n\t.ButtonMenu: %@\n\t.ButtonOptions: %@\n\t.ButtonSpecial0: %@\n\t.ButtonSpecial1: %@\n\t.ButtonSpecial2: %@\n\t.ButtonSpecial3: %@\n\t.ButtonSpecial4: %@\n\t.ButtonSpecial5: %@\n\t.ButtonSpecial6: %@\n\t.ButtonSpecial7: %@\n\t.ButtonSpecial8: %@\n\t.ButtonSpecial9: %@\n\t.ButtonSpecial10: %@\n\t.ButtonSpecial11: %@\n\t.ButtonSpecial12: %@\n\t.ButtonSpecial13: %@\n\t.ButtonSpecial14: %@\n\t.ButtonShare: %@\n}"
+ "<%@ %p> {\n\t.DpadUp: %f\n\t.DpadDown: %f\n\t.DpadLeft: %f\n\t.DpadRight: %f\n\t.ButtonA: %f\n\t.ButtonB: %f\n\t.ButtonX: %f\n\t.ButtonY: %f\n\t.LeftShoulder: %f\n\t.RightShoulder: %f\n\t.LeftThumbstickUp: %f\n\t.LeftThumbstickDown: %f\n\t.LeftThumbstickLeft: %f\n\t.LeftThumbstickRight: %f\n\t.RightThumbstickUp: %f\n\t.RightThumbstickDown: %f\n\t.RightThumbstickLeft: %f\n\t.RightThumbstickRight: %f\n\t.LeftTrigger: %f\n\t.RightTrigger: %f\n\t.LeftThumbstickButton: %f\n\t.RightThumbstickButton: %f\n\t.LeftSideButton: %f\n\t.RightSideButton: %f\n\t.ButtonHome: %f\n\t.ButtonMenu: %f\n\t.ButtonOptions: %f\n\t.ButtonSpecial0: %f\n\t.ButtonSpecial1: %f\n\t.ButtonSpecial2: %f\n\t.ButtonSpecial3: %f\n\t.ButtonSpecial4: %f\n\t.ButtonSpecial5: %f\n\t.ButtonSpecial6: %f\n\t.ButtonSpecial7: %f\n\t.ButtonSpecial8: %f\n\t.ButtonSpecial9: %f\n\t.ButtonSpecial10: %f\n\t.ButtonSpecial11: %f\n\t.ButtonSpecial12: %f\n\t.ButtonSpecial13: %f\n\t.ButtonSearch: %f\n\t.ButtonShare: %f\n}"
+ "@40@0:8Q16[49f]24Q32"
+ "Left Side Button"
+ "Programmable Button 1"
+ "Programmable Button 2"
+ "Programmable Button 3"
+ "Programmable Button 4"
+ "Programmable Button 5"
+ "Right Side Button"
+ "[49@\"GCControllerElement\"]"
+ "[49{UsagePage_Usage_Pair=\"usagePage\"q\"usage\"q}]"
+ "^[49C]"
+ "_cached_collectionEventBufferCount"
+ "leftSideButton"
+ "rightSideButton"
+ "setLeftSideButton:"
+ "setRightSideButton:"
+ "{?=\"mask\"Q\"buttons\"[49f]}"
- "%02x%@"
- "(value > 0 && touched) || value == 0"
- "-[_GCHandSkeleton boneDataWithTransformSpace:referencePose:]"
- "0"
- "0 `"
- "<%@ %lu (%@), i=%f s=%f (started at %f)>"
- "<%@ %p> {\n\t.DpadUp: %@\n\t.DpadDown: %@\n\t.DpadLeft: %@\n\t.DpadRight: %@\n\t.ButtonA: %@\n\t.ButtonB: %@\n\t.ButtonX: %@\n\t.ButtonY: %@\n\t.LeftShoulder: %@\n\t.RightShoulder: %@\n\t.LeftThumbstickUp: %@\n\t.LeftThumbstickDown: %@\n\t.LeftThumbstickLeft: %@\n\t.LeftThumbstickRight: %@\n\t.RightThumbstickUp: %@\n\t.RightThumbstickDown: %@\n\t.RightThumbstickLeft: %@\n\t.RightThumbstickRight: %@\n\t.LeftTrigger: %@\n\t.RightTrigger: %@\n\t.LeftThumbstickButton: %@\n\t.RightThumbstickButton: %@\n\t.ButtonHome: %@\n\t.ButtonMenu: %@\n\t.ButtonOptions: %@\n\t.ButtonSpecial0: %@\n\t.ButtonSpecial1: %@\n\t.ButtonSpecial2: %@\n\t.ButtonSpecial3: %@\n\t.ButtonSpecial4: %@\n\t.ButtonSpecial5: %@\n\t.ButtonSpecial6: %@\n\t.ButtonSpecial7: %@\n\t.ButtonSpecial8: %@\n\t.ButtonSpecial9: %@\n\t.ButtonSpecial10: %@\n\t.ButtonSpecial11: %@\n\t.ButtonSpecial12: %@\n\t.ButtonSpecial13: %@\n\t.ButtonSpecial14: %@\n\t.ButtonShare: %@\n}"
- "<%@ %p> {\n\t.DpadUp: %f\n\t.DpadDown: %f\n\t.DpadLeft: %f\n\t.DpadRight: %f\n\t.ButtonA: %f\n\t.ButtonB: %f\n\t.ButtonX: %f\n\t.ButtonY: %f\n\t.LeftShoulder: %f\n\t.RightShoulder: %f\n\t.LeftThumbstickUp: %f\n\t.LeftThumbstickDown: %f\n\t.LeftThumbstickLeft: %f\n\t.LeftThumbstickRight: %f\n\t.RightThumbstickUp: %f\n\t.RightThumbstickDown: %f\n\t.RightThumbstickLeft: %f\n\t.RightThumbstickRight: %f\n\t.LeftTrigger: %f\n\t.RightTrigger: %f\n\t.LeftThumbstickButton: %f\n\t.RightThumbstickButton: %f\n\t.ButtonHome: %f\n\t.ButtonMenu: %f\n\t.ButtonOptions: %f\n\t.ButtonSpecial0: %f\n\t.ButtonSpecial1: %f\n\t.ButtonSpecial2: %f\n\t.ButtonSpecial3: %f\n\t.ButtonSpecial4: %f\n\t.ButtonSpecial5: %f\n\t.ButtonSpecial6: %f\n\t.ButtonSpecial7: %f\n\t.ButtonSpecial8: %f\n\t.ButtonSpecial9: %f\n\t.ButtonSpecial10: %f\n\t.ButtonSpecial11: %f\n\t.ButtonSpecial12: %f\n\t.ButtonSpecial13: %f\n\t.ButtonSearch: %f\n\t.ButtonShare: %f\n}"
- "@\"NSMutableDictionary\"16@0:8"
- "@\"_GCHandSkeleton\""
- "@1024@0:8{?=[31{?={?=}}]}16@1008q1016"
- "@20@0:8i16"
- "@24@0:8(SlotID=Q{?=Ib8b8S})16"
- "@28@0:8i16@20"
- "@36@0:8i16@20Q28"
- "@40@0:8Q16[47f]24Q32"
- "@44@0:8i16@20Q28f36f40"
- "B24@0:8r^{?=fffff}16"
- "GCAdaptiveTriggersServiceServerInterface"
- "GCBatteryServiceServerInterface"
- "GCControllerButtonInput_Private.h"
- "GCDualQuaternion.m"
- "GCForceVirtual"
- "GCGameIntentServiceServerInterface"
- "GCHandSkeletonAny"
- "GCHandSkeletonLeft"
- "GCHandSkeletonRight"
- "GCHapticMotor"
- "GCHapticMotor - %@(%d) f=%f a=%f"
- "GCIdleServiceServerInterface"
- "GCLightServiceClientInterface"
- "GCLightServiceServerInterface"
- "GCMotionServiceClientInterface"
- "GCMotionServiceServerInterface"
- "GCNintendoJoyConFusionGestureServiceServerInterface"
- "GCPartnersEnable"
- "GCPropertyValueHandedness"
- "GCXRComponent"
- "GCXRComponentProvider"
- "Partners mode enabled? %d"
- "T@\"<NSObject><NSCopying><NSSecureCoding>\",&,V_identifier"
- "T@\"NSMutableArray\",&,N,V_queuedTransients"
- "T@\"NSMutableDictionary\",&,N"
- "T@\"NSMutableDictionary\",&,N,V_handSkeletons"
- "T@\"NSString\",R,C,N,V_name"
- "TB,N,V_stopped"
- "TB,N,V_transientBeganAsContinuousEvent"
- "TQ,N,V_identifier"
- "TQ,R,N,V_features"
- "Td,N,V_intensity"
- "Td,N,V_sharpness"
- "Td,N,V_startTime"
- "Tf,N,V_amplitude"
- "Tf,N,V_frequency"
- "Ti,R,N,V_index"
- "XR Component: adding"
- "XRPropertyButtonFingerIndex"
- "XRPropertyButtonFingerLittle"
- "XRPropertyButtonFingerMiddle"
- "XRPropertyButtonFingerRing"
- "XRPropertyButtonFingerThumb"
- "[47@\"GCControllerElement\"]"
- "[47{UsagePage_Usage_Pair=\"usagePage\"q\"usage\"q}]"
- "[4[31{?=\"real\"{?=\"vector\"}\"dual\"{?=\"vector\"}}]]"
- "[5f]"
- "^[47C]"
- "_GCDriverClientInterface"
- "_GCDriverServerInterface"
- "_GCHandSkeleton"
- "_GCHapticEvent"
- "_GCXRComponent"
- "_GCXRComponent.m"
- "_amplitude"
- "_boneData"
- "_boneDataWithMotionRange:curlAmts:"
- "_boneDataWithMotionRangeDq:curlAmts:"
- "_convertToModelSpaceUsingDQs:"
- "_convertToModelSpaceUsingMatrices:"
- "_features"
- "_handSkeletons"
- "_handedness"
- "_intensity"
- "_interpolationMethod"
- "_lastFingerPositions"
- "_leftHandSkeleton"
- "_queuedTransients"
- "_rightHandSkeleton"
- "_setInterpolationMethod:"
- "_sharpness"
- "_startTime"
- "_stopped"
- "_transientBeganAsContinuousEvent"
- "amplitude"
- "applyValuesFrom:"
- "boneDataWithTransformSpace:motionRange:"
- "boneDataWithTransformSpace:referencePose:"
- "com.apple.GameController.HID"
- "componentWithPhysicalInputProfile:"
- "continuous"
- "dqNormalize"
- "drainQueuedTransients"
- "enqueueHapticTransientEvent:"
- "f32@0:8r^{?=fffff}16q24"
- "features"
- "fingerPositionsChangedForCurlAmts:"
- "forceVirtualController"
- "getFingerCurlAmt:boneType:"
- "handSkeletons"
- "handedness"
- "initWithBoneData:profile:handedness:"
- "initWithIndex:"
- "initWithIndex:name:"
- "initWithIndex:name:features:"
- "initWithIndex:name:features:frequency:amplitude:"
- "mag > 0.000001f"
- "queuedTransients"
- "r^^{?}"
- "referenceDQs"
- "referenceSkeletons"
- "rightHand"
- "setAmplitude:"
- "setButtonValueAndTouched"
- "setFrequency:"
- "setHandSkeletons:"
- "setHandedness:"
- "setQueuedTransients:"
- "stringWithCapacity:"
- "stringWithString:"
- "transient"
- "updateSkeletons"
- "uppercaseString"
- "v24@0:8@\"NSMutableDictionary\"16"
- "v24@0:8@?<v@?@\"NSNumber\"q>16"
- "v24@0:8@?<v@?CB>16"
- "v24@0:8@?<v@?CCCCCC>16"
- "v24@0:8@?<v@?fff>16"
- "v28@0:8@\"NSArray\"16i24"
- "v28@0:8f16f20i24"
- "v32@0:8@\"<GCAdaptiveTriggersServiceClientInterface>\"16@?<v@?@\"<GCAdaptiveTriggersServiceServerInterface>\"@\"NSError\">24"
- "v32@0:8@\"<GCBatteryServiceClientInterface>\"16@?<v@?@\"<GCBatteryServiceServerInterface>\"@\"NSError\">24"
- "v32@0:8@\"<GCGameIntentServiceClientInterface>\"16@?<v@?@\"<GCGameIntentServiceServerInterface>\"@\"NSError\">24"
- "v32@0:8@\"<GCGenericDeviceDriverConfigurationServiceClientInterface>\"16@?<v@?@\"<GCGenericDeviceDriverConfigurationServiceServerInterface>\"@\"NSError\">24"
- "v32@0:8@\"<GCIdleServiceClientInterface>\"16@?<v@?@\"<GCIdleServiceServerInterface>\"@\"NSError\">24"
- "v32@0:8@\"<GCLightServiceClientInterface>\"16@?<v@?@\"<GCLightServiceServerInterface>\"@\"NSError\">24"
- "v32@0:8@\"<GCMotionServiceClientInterface>\"16@?<v@?@\"<GCMotionServiceServerInterface>\"@\"NSError\">24"
- "v32@0:8@\"<GCNintendoJoyConFusionGestureServiceClientInterface>\"16@?<v@?@\"<GCNintendoJoyConFusionGestureServiceServerInterface>\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16f24i28"
- "v32@0:8@16f24i28"
- "v32@0:8f16f20f24i28"
- "v36@0:8f16f20f24f28i32"
- "{?=\"boneTransforms\"[31{?=\"position\"\"orientation\"{?=\"vector\"}}]}"
- "{?=\"mask\"Q\"buttons\"[47f]}"
- "{?=[31{?={?=}}]}24@0:8r^{?=[31{?={?=}}]}16"
- "{?=[31{?={?=}}]}32@0:8q16q24"
- "{?=[31{?={?=}}]}32@0:8q16r^{?=fffff}24"

```
