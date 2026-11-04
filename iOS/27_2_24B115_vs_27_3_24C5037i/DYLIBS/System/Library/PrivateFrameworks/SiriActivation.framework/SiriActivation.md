## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3605.31.1.11.2
-  __TEXT.__text: 0x74b7c
-  __TEXT.__objc_methlist: 0x73f4
+3610.10.1.0.0
+  __TEXT.__text: 0x75d64
+  __TEXT.__objc_methlist: 0x75c4
   __TEXT.__const: 0x124c
-  __TEXT.__cstring: 0xd2a2
-  __TEXT.__oslogstring: 0x9bc3
-  __TEXT.__gcc_except_tab: 0xd00
+  __TEXT.__cstring: 0xd522
+  __TEXT.__oslogstring: 0x9e27
+  __TEXT.__gcc_except_tab: 0xd90
   __TEXT.__dlopen_cstrs: 0x1bc
   __TEXT.__swift5_typeref: 0x77a
   __TEXT.__constg_swiftt: 0x42c

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift_as_cont: 0x8c
-  __TEXT.__unwind_info: 0x2760
+  __TEXT.__unwind_info: 0x2808
   __TEXT.__eh_frame: 0xf58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1918
-  __DATA_CONST.__objc_classlist: 0x3a8
+  __DATA_CONST.__const: 0x1978
+  __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x36a0
+  __DATA_CONST.__objc_selrefs: 0x3790
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x2e8
+  __DATA_CONST.__objc_superrefs: 0x2f8
   __DATA_CONST.__objc_arraydata: 0x510
-  __DATA_CONST.__got: 0xaa8
-  __AUTH_CONST.__const: 0x14b0
-  __AUTH_CONST.__cfstring: 0x51c0
-  __AUTH_CONST.__objc_const: 0xb7c0
+  __DATA_CONST.__got: 0xac0
+  __AUTH_CONST.__const: 0x14f0
+  __AUTH_CONST.__cfstring: 0x52c0
+  __AUTH_CONST.__objc_const: 0xbbb0
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0xbf8
-  __AUTH.__objc_data: 0x2190
+  __AUTH_CONST.__auth_got: 0xc08
+  __AUTH.__objc_data: 0x2230
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x770
+  __DATA.__objc_ivar: 0x7a4
   __DATA.__data: 0x1710
   __DATA.__common: 0x270
   __DATA_DIRTY.__objc_data: 0x5f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3011
-  Symbols:   4796
-  CStrings:  1876
+  Functions: 3057
+  Symbols:   4876
+  CStrings:  1903
 
Symbols:
+ +[SASActivationDecision missingAssetsNotificationForCondition:handler:]
+ +[SRUIFIntelligenceFlowFeatureFlag(SWEFeatureFlags) isAnnounceCampoEnabled]
+ +[SRUIFSiriUIFeatureFlag(SWEFeatureFlags) isDisplayTransitionCallEnabled]
+ +[SiriActivationService _shouldReportAvailability]
+ -[SASDeviceSelectionShadowController .cxx_destruct]
+ -[SASDeviceSelectionShadowController _beginActivation]
+ -[SASDeviceSelectionShadowController _deviceSelectionObserverForTesting]
+ -[SASDeviceSelectionShadowController _donateRecencyForActivationDate:]
+ -[SASDeviceSelectionShadowController _myriadObserverForTesting]
+ -[SASDeviceSelectionShadowController _recordDeviceSelectionOutcome:]
+ -[SASDeviceSelectionShadowController _recordMyriadOutcome:]
+ -[SASDeviceSelectionShadowController _relayMyriadOutcome:]
+ -[SASDeviceSelectionShadowController _setNowForTesting:]
+ -[SASDeviceSelectionShadowController activateForInTaskRequest:isVisible:]
+ -[SASDeviceSelectionShadowController activateForRequest:visible:]
+ -[SASDeviceSelectionShadowController activateForRequest:withTimeout:visible:]
+ -[SASDeviceSelectionShadowController activateForRequest:withTimeout:visible:idleAndQuiet:]
+ -[SASDeviceSelectionShadowController canceledByMyriad]
+ -[SASDeviceSelectionShadowController initWithDelegate:]
+ -[SASDeviceSelectionShadowController initWithDelegate:myriadChild:deviceSelectionChild:]
+ -[SASRequestOptions carOwnsCommunication]
+ -[SASRequestOptions setCarOwnsCommunication:]
+ -[SASShadowChildObserver .cxx_destruct]
+ -[SASShadowChildObserver handler]
+ -[SASShadowChildObserver initWithHandler:]
+ -[SASShadowChildObserver scdaShouldAbort:]
+ -[SASShadowChildObserver scdaShouldContinue:]
+ -[SASSystemState _updateCarOwnsCommunication]
+ -[SASSystemState _vehicleHandlesMessagesChanged:]
+ -[SASSystemState carOwnsCommunicationOverrideDefaults]
+ -[SASSystemState carOwnsCommunication]
+ -[SASSystemState isOnMainDisplay]
+ -[SASSystemState isV68]
+ -[SASSystemState onMainDisplay]
+ -[SASSystemState setCarOwnsCommunication:]
+ -[SASSystemState setCarOwnsCommunicationOverrideDefaults:]
+ -[SASSystemState setOnMainDisplay:]
+ -[SiriTVActivationSource speechInteractionActivityWithTimestamp:]
+ GCC_except_table107
+ GCC_except_table113
+ GCC_except_table164
+ GCC_except_table24
+ GCC_except_table29
+ GCC_except_table85
+ GCC_except_table87
+ _AFDeviceSelectionParticipating
+ _CARSessionVehicleHandlesMessagesChangedNotification
+ _MGGetProductType
+ _OBJC_CLASS_$_SASDeviceSelectionShadowController
+ _OBJC_CLASS_$_SASShadowChildObserver
+ _OBJC_IVAR_$_SASDeviceSelectionShadowController._delegate
+ _OBJC_IVAR_$_SASDeviceSelectionShadowController._deviceSelection
+ _OBJC_IVAR_$_SASDeviceSelectionShadowController._deviceSelectionObserver
+ _OBJC_IVAR_$_SASDeviceSelectionShadowController._lastDeviceSelectionOutcome
+ _OBJC_IVAR_$_SASDeviceSelectionShadowController._myriad
+ _OBJC_IVAR_$_SASDeviceSelectionShadowController._myriadObserver
+ _OBJC_IVAR_$_SASDeviceSelectionShadowController._now
+ _OBJC_IVAR_$_SASDeviceSelectionShadowController._pendingActivationDate
+ _OBJC_IVAR_$_SASRequestOptions._carOwnsCommunication
+ _OBJC_IVAR_$_SASShadowChildObserver._handler
+ _OBJC_IVAR_$_SASSystemState._carOwnsCommunication
+ _OBJC_IVAR_$_SASSystemState._carOwnsCommunicationOverrideDefaults
+ _OBJC_IVAR_$_SASSystemState._onMainDisplay
+ _OBJC_METACLASS_$_SASDeviceSelectionShadowController
+ _OBJC_METACLASS_$_SASShadowChildObserver
+ __OBJC_$_INSTANCE_METHODS_SASDeviceSelectionShadowController
+ __OBJC_$_INSTANCE_METHODS_SASShadowChildObserver
+ __OBJC_$_INSTANCE_VARIABLES_SASDeviceSelectionShadowController
+ __OBJC_$_INSTANCE_VARIABLES_SASShadowChildObserver
+ __OBJC_$_PROP_LIST_SASDeviceSelectionShadowController
+ __OBJC_$_PROP_LIST_SASShadowChildObserver
+ __OBJC_CLASS_PROTOCOLS_$_SASDeviceSelectionShadowController
+ __OBJC_CLASS_PROTOCOLS_$_SASShadowChildObserver
+ __OBJC_CLASS_RO_$_SASDeviceSelectionShadowController
+ __OBJC_CLASS_RO_$_SASShadowChildObserver
+ __OBJC_METACLASS_RO_$_SASDeviceSelectionShadowController
+ __OBJC_METACLASS_RO_$_SASShadowChildObserver
+ ___54-[SASDeviceSelectionShadowController _beginActivation]_block_invoke
+ ___70-[SASDeviceSelectionShadowController _donateRecencyForActivationDate:]_block_invoke
+ ___88-[SASDeviceSelectionShadowController initWithDelegate:myriadChild:deviceSelectionChild:]_block_invoke
+ ___88-[SASDeviceSelectionShadowController initWithDelegate:myriadChild:deviceSelectionChild:]_block_invoke_2
+ ___88-[SASDeviceSelectionShadowController initWithDelegate:myriadChild:deviceSelectionChild:]_block_invoke_3
+ ___88-[SASDeviceSelectionShadowController initWithDelegate:myriadChild:deviceSelectionChild:]_block_invoke_4
+ ___88-[SASDeviceSelectionShadowController initWithDelegate:myriadChild:deviceSelectionChild:]_block_invoke_5
+ ___block_descriptor_32_e13_"NSDate"8?0l
+ ___block_descriptor_40_e8_32w_e8_v16?0Q8lw32l8
- GCC_except_table106
- GCC_except_table111
- GCC_except_table163
- GCC_except_table42
- GCC_except_table82
- GCC_except_table84
CStrings:
+ "%s #CarPlay Car owns communication: %@"
+ "%s #CarPlay Vehicle handles messages changed"
+ "%s #activation: Smart Cover is closed, but it isn't covering the display in use, so ignoring Smart Cover state"
+ "%s #deviceSelection #shadow Device Selection reported %{public}@."
+ "%s #deviceSelection #shadow Myriad %{public}@, Device Selection %{public}@."
+ "%s #deviceSelection #shadow Recency donation failed: %{public}@"
+ "%s #deviceSelection #shadow Shadow controller installed. Myriad decides; Device Selection is recorded."
+ "%s #deviceSelection Device selection not participating, skipping arbitration"
+ "%s #modes Device is not on main display setOnMainDisplay:NO"
+ "%s #modes Device on main display setOnMainDisplay:YES"
+ "-[SASDeviceSelectionShadowController _donateRecencyForActivationDate:]_block_invoke"
+ "-[SASDeviceSelectionShadowController _recordDeviceSelectionOutcome:]"
+ "-[SASDeviceSelectionShadowController _recordMyriadOutcome:]"
+ "-[SASDeviceSelectionShadowController initWithDelegate:myriadChild:deviceSelectionChild:]"
+ "-[SASSystemState _updateCarOwnsCommunication]"
+ "-[SASSystemState _vehicleHandlesMessagesChanged:]"
+ ";is(speech=%i; textInput=%i;stark=%i;CPconnected=%i;dnd=%i;rightHandDrive=%i;isForBluetoothCar=%i);carDNDStatus=%@;remotePresentationBringUp=%i;supportsCarPlayVehicleData=%i;carOwnsMainAudio=%i;carOwnsCommunication=%i"
+ "@\"NSDate\"8@?0"
+ "AnnounceCampo"
+ "CarOwnsCommunicationOverride"
+ "SASRequestOptionsCarOwnsCommunicationCodingKey"
+ "abort"
+ "carOwnsCommunication"
+ "com.apple.siri.systemstate"
+ "continue"
+ "display_transition_call"
+ "none"
+ "unknown"
+ "v16@?0Q8"
- "%s #deviceSelection Device does not support device selection, skipping arbitration"
- ";is(speech=%i; textInput=%i;stark=%i;CPconnected=%i;dnd=%i;rightHandDrive=%i;isForBluetoothCar=%i);carDNDStatus=%@;remotePresentationBringUp=%i;supportsCarPlayVehicleData=%i;carOwnsMainAudio=%i"
```
