## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3600.55.37.11.4
-  __TEXT.__text: 0x719bc
-  __TEXT.__objc_methlist: 0x6fa4
-  __TEXT.__const: 0x11dc
-  __TEXT.__cstring: 0xcc42
-  __TEXT.__oslogstring: 0x934c
-  __TEXT.__gcc_except_tab: 0xc8c
+3605.22.2.0.0
+  __TEXT.__text: 0x7385c
+  __TEXT.__objc_methlist: 0x7254
+  __TEXT.__const: 0x124c
+  __TEXT.__cstring: 0xcf62
+  __TEXT.__oslogstring: 0x9ae4
+  __TEXT.__gcc_except_tab: 0xcec
   __TEXT.__dlopen_cstrs: 0x1bc
   __TEXT.__swift5_typeref: 0x77a
   __TEXT.__constg_swiftt: 0x42c

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift_as_cont: 0x8c
-  __TEXT.__unwind_info: 0x2638
+  __TEXT.__unwind_info: 0x26f0
   __TEXT.__eh_frame: 0xf58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1808
-  __DATA_CONST.__objc_classlist: 0x390
+  __DATA_CONST.__const: 0x18c0
+  __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x1d8
+  __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3528
+  __DATA_CONST.__objc_selrefs: 0x35f8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_superrefs: 0x2d8
   __DATA_CONST.__objc_arraydata: 0x510
-  __DATA_CONST.__got: 0xa80
+  __DATA_CONST.__got: 0xaa8
   __AUTH_CONST.__const: 0x14b0
-  __AUTH_CONST.__cfstring: 0x5000
-  __AUTH_CONST.__objc_const: 0xb188
+  __AUTH_CONST.__cfstring: 0x50a0
+  __AUTH_CONST.__objc_const: 0xb5f8
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xbd8
-  __AUTH.__objc_data: 0x20a0
+  __AUTH_CONST.__auth_got: 0xbe8
+  __AUTH.__objc_data: 0x2190
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x720
-  __DATA.__data: 0x16a0
+  __DATA.__objc_ivar: 0x748
+  __DATA.__data: 0x1700
   __DATA.__common: 0x270
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/IAP.framework/IAP
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
+  - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2906
-  Symbols:   6020
-  CStrings:  1806
+  Functions: 2971
+  Symbols:   6136
+  CStrings:  1856
 
Symbols:
+ +[SASActivationDecision shouldContinueActivationForCondition:errorNotification:activationDeclinedHandler:]
+ +[SASDeviceSelectionController _resetSignalObserverSetupForTesting]
+ +[SASDeviceSelectionController setupSignalObservers]
+ +[SRUIFIntelligenceFlowFeatureFlag(SWEFeatureFlags) isCampoEnabled]
+ +[SRUIFIntelligenceFlowFeatureFlag(SWEFeatureFlags) isCrossSessionContinuityEnabled]
+ +[SRUIFIntelligenceFlowFeatureFlag(SWEFeatureFlags) isDashboardCampoEnabled]
+ +[SRUIFIntelligenceFlowFeatureFlag(SWEFeatureFlags) isLinwoodEnabled]
+ +[SRUIFIntelligenceFlowFeatureFlag(SWEFeatureFlags) isThirdPartyAppModelsEnabled]
+ +[SRUIFSiriFeatureFlag(SWEFeatureFlags) isContinuousConversationHomepodEnabled]
+ -[SASActivationCondition setUserNotificationPresenter:]
+ -[SASActivationCondition userNotificationPresenter]
+ -[SASDeviceSelectionController .cxx_destruct]
+ -[SASDeviceSelectionController _selectDeviceWithSignals:completion:]
+ -[SASDeviceSelectionController _triggerSignalForActivationRequest:isSiriDisplayed:isSiriSpeaking:]
+ -[SASDeviceSelectionController _triggerTypeForActivationRequest:]
+ -[SASDeviceSelectionController activateForInTaskRequest:isVisible:]
+ -[SASDeviceSelectionController activateForRequest:visible:]
+ -[SASDeviceSelectionController activateForRequest:withTimeout:visible:]
+ -[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:]
+ -[SASDeviceSelectionController canceledByMyriad]
+ -[SASDeviceSelectionController initWithDelegate:]
+ -[SASMyriadController activateForRequest:withTimeout:visible:idleAndQuiet:]
+ -[SASMyriadWatchController activateForRequest:withTimeout:visible:idleAndQuiet:]
+ -[SASPresentationManager _presentationsLock_cancelPrewarmCancellationTimer]
+ -[SASPresentationManager _presentationsLock_startPrewarmCancellationTimer]
+ -[SASPresentationManager prewarmCancellationBlock]
+ -[SASPresentationManager setPrewarmCancellationBlock:]
+ -[SASPresentationManager unregisterSiriPresentation:withIdentifier:]
+ -[SASSignalServer registerActivationOutcomeListenerWithIdentifier:]
+ -[SASSignalServer unregisterActivationOutcomeListenerWithIdentifier:]
+ -[SASSystemState _demoModeIsSupported]
+ -[SASSystemState _inPressDemoMode]
+ -[SASSystemState _inSecureDemoModeWithError:]
+ -[SASSystemState _inStoreDemoMode]
+ -[SASSystemState _shouldShowDemoSiriAI]
+ -[SASSystemState isInDemoMode]
+ -[SiriActivationOutcomeListener .cxx_destruct]
+ -[SiriActivationOutcomeListener activationSourceDidReceiveDeclinedActivation]
+ -[SiriActivationOutcomeListener dealloc]
+ -[SiriActivationOutcomeListener delegate]
+ -[SiriActivationOutcomeListener dispatchDelegateCallbacksOnMainQueue]
+ -[SiriActivationOutcomeListener initWithDelegate:dispatchCallbacksOnMainQueue:]
+ -[SiriActivationOutcomeListener invalidate]
+ -[SiriActivationOutcomeListener setDelegate:]
+ -[SiriActivationOutcomeListener setDispatchDelegateCallbacksOnMainQueue:]
+ -[SiriActivationOutcomeListener setSource:]
+ -[SiriActivationOutcomeListener source]
+ -[SiriActivationService _notifyListenersOfDeclinedActivation]
+ -[SiriActivationService activationOutcomeListeners]
+ -[SiriActivationService registerActivationOutcomeListenerServer:identifier:]
+ -[SiriActivationService setActivationOutcomeListeners:]
+ -[SiriActivationService unregisterActivationOutcomeListenerWithIdentifier:]
+ -[SiriActivationService unregisterSiriPresentation:withIdentifier:]
+ -[SiriActivationSource siriActivationDeclined]
+ -[SiriSimpleActivationSource .cxx_destruct]
+ -[SiriSimpleActivationSource initAsOutcomeReceiverWithDelegate:]
+ -[SiriSimpleActivationSource siriActivationDeclined]
+ -[SiriTVLongPressButtonContext SAFLongPressButtonContext]
+ GCC_except_table10
+ GCC_except_table110
+ GCC_except_table111
+ GCC_except_table16
+ GCC_except_table162
+ GCC_except_table41
+ GCC_except_table48
+ GCC_except_table71
+ GCC_except_table82
+ GCC_except_table83
+ _CFPreferencesGetAppBooleanValue
+ _NSStringFromAFSiriUnavailabilityReasons
+ _OBJC_CLASS_$_DeviceSelectionSiriSessionSignal
+ _OBJC_CLASS_$_DeviceSelectionTriggerSignal
+ _OBJC_CLASS_$_MSDKDemoState
+ _OBJC_CLASS_$_SAFTVLongPressButtonContext
+ _OBJC_CLASS_$_SASDeviceSelectionController
+ _OBJC_CLASS_$_SRUIFIntelligenceFlowFeatureFlag
+ _OBJC_CLASS_$_SiriActivationOutcomeListener
+ _OBJC_IVAR_$_SASActivationCondition._userNotificationPresenter
+ _OBJC_IVAR_$_SASDeviceSelectionController._canceledByMyriad
+ _OBJC_IVAR_$_SASDeviceSelectionController._delegate
+ _OBJC_IVAR_$_SASPresentationManager._prewarmCancellationBlock
+ _OBJC_IVAR_$_SiriActivationOutcomeListener._delegate
+ _OBJC_IVAR_$_SiriActivationOutcomeListener._dispatchDelegateCallbacksOnMainQueue
+ _OBJC_IVAR_$_SiriActivationOutcomeListener._source
+ _OBJC_IVAR_$_SiriActivationService._activationOutcomeListeners
+ _OBJC_IVAR_$_SiriSimpleActivationSource._isOutcomeReceiver
+ _OBJC_IVAR_$_SiriSimpleActivationSource._outcomeDelegate
+ _OBJC_METACLASS_$_SASDeviceSelectionController
+ _OBJC_METACLASS_$_SRUIFIntelligenceFlowFeatureFlag
+ _OBJC_METACLASS_$_SiriActivationOutcomeListener
+ _SAFTVRemoteTypeFromSiriTVRemoteType
+ _SASDeviceSelectionSignalObserverLock
+ _SASDeviceSelectionSignalObserversAreSetUp
+ __OBJC_$_CLASS_METHODS_SASDeviceSelectionController
+ __OBJC_$_CLASS_METHODS_SRUIFIntelligenceFlowFeatureFlag(SWEFeatureFlags)
+ __OBJC_$_INSTANCE_METHODS_SASDeviceSelectionController
+ __OBJC_$_INSTANCE_METHODS_SiriActivationOutcomeListener
+ __OBJC_$_INSTANCE_VARIABLES_SASDeviceSelectionController
+ __OBJC_$_INSTANCE_VARIABLES_SiriActivationOutcomeListener
+ __OBJC_$_INSTANCE_VARIABLES_SiriSimpleActivationSource
+ __OBJC_$_PROP_LIST_SASDeviceSelectionController
+ __OBJC_$_PROP_LIST_SiriActivationOutcomeListener
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SiriSimpleActivationSourceOutcomeDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SiriSimpleActivationSourceOutcomeDelegate
+ __OBJC_$_PROTOCOL_REFS_SiriSimpleActivationSourceOutcomeDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SASDeviceSelectionController
+ __OBJC_CLASS_PROTOCOLS_$_SiriActivationOutcomeListener
+ __OBJC_CLASS_RO_$_SASDeviceSelectionController
+ __OBJC_CLASS_RO_$_SRUIFIntelligenceFlowFeatureFlag
+ __OBJC_CLASS_RO_$_SiriActivationOutcomeListener
+ __OBJC_LABEL_PROTOCOL_$_SiriSimpleActivationSourceOutcomeDelegate
+ __OBJC_METACLASS_RO_$_SASDeviceSelectionController
+ __OBJC_METACLASS_RO_$_SRUIFIntelligenceFlowFeatureFlag
+ __OBJC_METACLASS_RO_$_SiriActivationOutcomeListener
+ __OBJC_PROTOCOL_$_SiriSimpleActivationSourceOutcomeDelegate
+ ___106+[SASActivationDecision shouldContinueActivationForCondition:errorNotification:activationDeclinedHandler:]_block_invoke
+ ___47+[SASPresentationServer _unregisterConnection:]_block_invoke
+ ___52+[SASDeviceSelectionController setupSignalObservers]_block_invoke
+ ___61-[SiriActivationService _notifyListenersOfDeclinedActivation]_block_invoke
+ ___61-[SiriActivationService handleActivationRequest:systemState:]_block_invoke_2
+ ___75-[SASMyriadController activateForRequest:withTimeout:visible:idleAndQuiet:]_block_invoke
+ ___77-[SiriActivationOutcomeListener activationSourceDidReceiveDeclinedActivation]_block_invoke
+ ___84-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:]_block_invoke
+ ___84-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:]_block_invoke_2
+ ___block_descriptor_32_e42_v32?0"NSString"8"SASSignalServer"16^B24l
+ ___block_descriptor_40_e8_32w_e43_v24?0"DeviceSelectionDevice"8"NSError"16lw32l8
+ ___block_descriptor_41_e8_32s_e29_v16?0"BSServiceConnection"8ls32l8
+ ___block_descriptor_41_e8_32w_e42_v16?0"<BSServiceConnectionConfiguring>"8lw32l8
+ ___block_descriptor_49_e8_32s40w_e29_v16?0"BSServiceConnection"8lw40l8s32l8
+ _activationOutcomeListenerLock
+ _objc_msgSend$_demoModeIsSupported
+ _objc_msgSend$_inPressDemoMode
+ _objc_msgSend$_inSecureDemoModeWithError:
+ _objc_msgSend$_inStoreDemoMode
+ _objc_msgSend$_notifyListenersOfDeclinedActivation
+ _objc_msgSend$_presentationsLock_cancelPrewarmCancellationTimer
+ _objc_msgSend$_presentationsLock_startPrewarmCancellationTimer
+ _objc_msgSend$_selectDeviceWithSignals:completion:
+ _objc_msgSend$_shouldShowDemoSiriAI
+ _objc_msgSend$_triggerSignalForActivationRequest:isSiriDisplayed:isSiriSpeaking:
+ _objc_msgSend$_triggerTypeForActivationRequest:
+ _objc_msgSend$activateForRequest:withTimeout:visible:idleAndQuiet:
+ _objc_msgSend$activationDeclinedBecauseSiriIsUnavailable
+ _objc_msgSend$activationOutcomeListeners
+ _objc_msgSend$activationSourceDidReceiveDeclinedActivation
+ _objc_msgSend$initAsOutcomeReceiverWithDelegate:
+ _objc_msgSend$initWithState:timestamp:
+ _objc_msgSend$initWithType:context:
+ _objc_msgSend$isDashboardCampoEnabled
+ _objc_msgSend$isSecureDemoModeEnabled:
+ _objc_msgSend$registerActivationOutcomeListenerServer:identifier:
+ _objc_msgSend$registerActivationOutcomeListenerWithIdentifier:
+ _objc_msgSend$selectDeviceForRole:withSignals:completion:
+ _objc_msgSend$setActivationOutcomeListeners:
+ _objc_msgSend$setupSignalObservers
+ _objc_msgSend$shouldContinueActivationForCondition:errorNotification:activationDeclinedHandler:
+ _objc_msgSend$siriActivationDeclined
+ _objc_msgSend$unavailabilityReasons
+ _objc_msgSend$unregisterActivationOutcomeListenerWithIdentifier:
+ _objc_msgSend$unregisterSiriPresentation:withIdentifier:
+ _objc_msgSend$willAttemptFallback
+ _shouldContinueActivationForCondition:errorNotification:activationDeclinedHandler:.log
+ _shouldContinueActivationForCondition:errorNotification:activationDeclinedHandler:.once
- +[SASActivationDecision shouldContinueActivationForCondition:errorNotification:]
- -[SASMyriadController activateForRequest:withTimeout:visible:quiet:]
- -[SASMyriadWatchController activateForRequest:withTimeout:visible:quiet:]
- -[SASPresentationManager unregisterSiriPresentationWithIdentifier:]
- -[SiriActivationService _performDeviceSelectionWithActivation:withSystemState:withOptions:]
- -[SiriActivationService _performLegacyDeviceSelectionActivation:withSystemState:presentationIdentifier:]
- -[SiriActivationService _sendActivationTriggerToDeviceSelection:withSystemState:]
- -[SiriActivationService _setupDeviceSelectionSignalObservers]
- -[SiriActivationService unregisterSiriPresentationIdentifier:]
- GCC_except_table100
- GCC_except_table106
- GCC_except_table15
- GCC_except_table164
- GCC_except_table37
- GCC_except_table44
- GCC_except_table67
- GCC_except_table76
- GCC_except_table79
- _OBJC_CLASS_$_DeviceSelectionContext
- _OBJC_CLASS_$_DeviceSelectionTriggerSource
- _OBJC_CLASS_$_NSConstantDoubleNumber
- ___32-[SASRemoteRequestManager _init]_block_invoke_6
- ___32-[SASRemoteRequestManager _init]_block_invoke_7
- ___32-[SASRemoteRequestManager _init]_block_invoke_8
- ___32-[SASRemoteRequestManager _init]_block_invoke_9
- ___61-[SiriActivationService _setupDeviceSelectionSignalObservers]_block_invoke
- ___68-[SASMyriadController activateForRequest:withTimeout:visible:quiet:]_block_invoke
- ___80+[SASActivationDecision shouldContinueActivationForCondition:errorNotification:]_block_invoke
- ___81-[SiriActivationService _sendActivationTriggerToDeviceSelection:withSystemState:]_block_invoke
- ___91-[SiriActivationService _performDeviceSelectionWithActivation:withSystemState:withOptions:]_block_invoke
- ___block_descriptor_40_e8_32s_e43_v24?0"DeviceSelectionDevice"8"NSError"16ls32l8
- _objc_msgSend$_performDeviceSelectionWithActivation:withSystemState:withOptions:
- _objc_msgSend$_performLegacyDeviceSelectionActivation:withSystemState:presentationIdentifier:
- _objc_msgSend$_sendActivationTriggerToDeviceSelection:withSystemState:
- _objc_msgSend$_setupDeviceSelectionSignalObservers
- _objc_msgSend$activateForRequest:visible:
- _objc_msgSend$activateForRequest:withTimeout:visible:quiet:
- _objc_msgSend$donateTriggerSource:withCompletion:
- _objc_msgSend$initWithSessionId:
- _objc_msgSend$initWithTriggerType:context:
- _objc_msgSend$selectDeviceForRole:context:completion:
- _objc_msgSend$shouldContinueActivationForCondition:errorNotification:
- _objc_msgSend$turnIdentifier
- _objc_msgSend$unregisterSiriPresentationIdentifier:
- _objc_msgSend$unregisterSiriPresentationWithIdentifier:
- _shouldContinueActivationForCondition:errorNotification:.log
- _shouldContinueActivationForCondition:errorNotification:.once
CStrings:
+ "%s #Availability #activation NO: Siri is unavailable and nothing will serve the request { reasons: %@, source: %@ }"
+ "%s #activation #locks #noisy activationOutcomeListenerLock about to lock with qos: %zd"
+ "%s #activation #locks #noisy activationOutcomeListenerLock successfully locked"
+ "%s #activation #locks #noisy activationOutcomeListenerLock unlocked"
+ "%s #activation #staleUnregister Ignoring unregister of '%@' from a presentation server that no longer owns it."
+ "%s #activation Allowing the lock button press to fall through to SpringBoard for an announce call"
+ "%s #activation Registering activation outcome listener with Id - '%@'"
+ "%s #activation Registration of '%@' outcome listener when it is already present. Removing"
+ "%s #activation Relaying declined activation from '%@'"
+ "%s #activation Unregister outcome listener for '%@' when it is not registered."
+ "%s #activation Unregistering activation outcome listener '%@'"
+ "%s #activation activateFromSource: on a source created as an outcome receiver. Ignoring."
+ "%s #activation registerActivationOutcomeListenerWithIdentifier:%@"
+ "%s #activation unregisterActivationOutcomeListenerWithIdentifier:%@"
+ "%s #deviceSelection Creating trigger signal with type(%@), isConnectedToCarPlay %d, isSiriDisplayed %d, isSiriSpeaking %d"
+ "%s #deviceSelection Device does not support device selection, skipping arbitration"
+ "%s #deviceSelection Donating signals: session start and trigger"
+ "%s #deviceSelection Error: %@"
+ "%s #deviceSelection Ignoring legacy Myriad timeout of %@ ms"
+ "%s #deviceSelection In-task activation is not donated to device selection - isVoiceTrigger: %d, isVisible: %d"
+ "%s #deviceSelection Signal observers already set up, ignoring duplicate request"
+ "%s #deviceSelection Unexpected activation type %ld, defaulting to Button Press"
+ "%s #settings #demomode Checking for demo mode"
+ "%s #settings #demomode Demo mode isn't supported on this platform"
+ "%s #settings #demomode Either not in Store demo mode, or we don't have the Carousel default set"
+ "%s #settings #demomode Failed to check for secure demo mode: %@"
+ "%s #settings #demomode Not in Press demo mode"
+ "%s #settings #demomode Not in secure demo mode"
+ "%s #settings #demomode Press demo mode detected"
+ "%s #settings #demomode Secure Store demo mode detected and Carousel's ShowDemoSiriAI=true. Using demo mode."
+ "+[SASActivationDecision shouldContinueActivationForCondition:errorNotification:activationDeclinedHandler:]"
+ "+[SASDeviceSelectionController setupSignalObservers]"
+ "+[SASDeviceSelectionController setupSignalObservers]_block_invoke"
+ "-[SASDeviceSelectionController _triggerSignalForActivationRequest:isSiriDisplayed:isSiriSpeaking:]"
+ "-[SASDeviceSelectionController _triggerTypeForActivationRequest:]"
+ "-[SASDeviceSelectionController activateForInTaskRequest:isVisible:]"
+ "-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:]"
+ "-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:]_block_invoke"
+ "-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:]_block_invoke_2"
+ "-[SASMyriadController activateForRequest:withTimeout:visible:idleAndQuiet:]"
+ "-[SASMyriadController activateForRequest:withTimeout:visible:idleAndQuiet:]_block_invoke"
+ "-[SASMyriadWatchController activateForRequest:withTimeout:visible:idleAndQuiet:]"
+ "-[SASPresentationManager unregisterSiriPresentation:withIdentifier:]"
+ "-[SASRemoteRequestManager _init]_block_invoke_5"
+ "-[SASSignalServer registerActivationOutcomeListenerWithIdentifier:]"
+ "-[SASSignalServer unregisterActivationOutcomeListenerWithIdentifier:]"
+ "-[SASSystemState isInDemoMode]"
+ "-[SiriActivationService _notifyListenersOfDeclinedActivation]"
+ "-[SiriActivationService registerActivationOutcomeListenerServer:identifier:]"
+ "-[SiriActivationService unregisterActivationOutcomeListenerWithIdentifier:]"
+ "-[SiriSimpleActivationSource activateFromSource:]"
+ "-[SiriSimpleActivationSource siriActivationDeclined]"
+ "ButtonDown"
+ "ButtonLongPress"
+ "ButtonUp"
+ "CrossSessionContinuity"
+ "DashboardCampo"
+ "Linwood"
+ "PressDemoMode"
+ "RemoteRequestManagerReceivedActivation"
+ "RemoteRequestManagerReceivedDismissal"
+ "RemoteRequestManagerReceivedPrewarm"
+ "ShowDemoSiriAI"
+ "StoreDemoMode"
+ "ThirdPartyAppModels"
+ "com.apple.Carousel"
+ "com.apple.demo-settings"
+ "continuous_conversation_homepod"
- "%s #activation Voice request on CarPlay, delaying Myriad decision by %@ ms"
- "%s #deviceSelection Donating activation with type(%@), isConnectedToCarPlay %d, isSiriDisplayed %d, isSiriSpeaking %d"
- "%s #deviceSelection Failed to donate Siri activation trigger source: %@"
- "%s #deviceSelection Successfully donated Siri activation trigger source."
- "%s #deviceSelection trigger selectDevice not using turn identifier - new session ID generated."
- "%s #deviceSelection trigger selectDevice using request info turn identifier: %@"
- "+[SASActivationDecision shouldContinueActivationForCondition:errorNotification:]"
- "-[SASMyriadController activateForRequest:withTimeout:visible:quiet:]"
- "-[SASMyriadController activateForRequest:withTimeout:visible:quiet:]_block_invoke"
- "-[SASMyriadWatchController activateForRequest:withTimeout:visible:quiet:]"
- "-[SASPresentationManager unregisterSiriPresentationWithIdentifier:]"
- "-[SASRemoteRequestManager _init]_block_invoke_9"
- "-[SiriActivationService _performDeviceSelectionWithActivation:withSystemState:withOptions:]"
- "-[SiriActivationService _performDeviceSelectionWithActivation:withSystemState:withOptions:]_block_invoke"
- "-[SiriActivationService _performLegacyDeviceSelectionActivation:withSystemState:presentationIdentifier:]"
- "-[SiriActivationService _sendActivationTriggerToDeviceSelection:withSystemState:]"
- "-[SiriActivationService _sendActivationTriggerToDeviceSelection:withSystemState:]_block_invoke"
- "-[SiriActivationService _setupDeviceSelectionSignalObservers]_block_invoke"
```
