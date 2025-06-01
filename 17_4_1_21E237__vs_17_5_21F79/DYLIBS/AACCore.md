## AACCore

> `/System/Library/PrivateFrameworks/AACCore.framework/AACCore`

```diff

-13.4.3.0.0
-  __TEXT.__text: 0xbae4
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0xf30
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xa9a
-  __TEXT.__oslogstring: 0x21e
-  __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__unwind_info: 0x4b4
-  __TEXT.__objc_classname: 0x760
-  __TEXT.__objc_methname: 0x21ab
-  __TEXT.__objc_methtype: 0x6b1
-  __TEXT.__objc_stubs: 0x13c0
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x520
-  __DATA_CONST.__objc_classlist: 0x178
+13.5.10.0.0
+  __TEXT.__text: 0xd6f4
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_methlist: 0x11b8
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0xc0a
+  __TEXT.__oslogstring: 0x248
+  __TEXT.__gcc_except_tab: 0xd4
+  __TEXT.__unwind_info: 0x59c
+  __TEXT.__objc_classname: 0x860
+  __TEXT.__objc_methname: 0x27a5
+  __TEXT.__objc_methtype: 0x7fb
+  __TEXT.__objc_stubs: 0x1740
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0x5b0
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2ea0
-  __DATA_CONST.__objc_selrefs: 0x700
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_classrefs: 0x1e0
-  __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__cfstring: 0xa40
-  __AUTH_CONST.__objc_const: 0x10f8
+  __DATA_CONST.__objc_const: 0x3588
+  __DATA_CONST.__objc_selrefs: 0x838
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x1f8
+  __DATA_CONST.__objc_superrefs: 0x110
+  __AUTH_CONST.__cfstring: 0xb80
+  __AUTH_CONST.__objc_const: 0x12a8
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__auth_got: 0x2a0
-  __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_ivar: 0x178
-  __DATA.__data: 0x860
+  __AUTH_CONST.__auth_got: 0x2d0
+  __AUTH.__objc_data: 0x1040
+  __DATA.__objc_ivar: 0x194
+  __DATA.__data: 0x9e0
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DBE734CA-E79B-3488-96CA-13416BED22D7
-  Functions: 412
-  Symbols:   1692
-  CStrings:  734
+  UUID: FE54E5FA-F292-3E82-89CB-001CD688B4B4
+  Functions: 489
+  Symbols:   1947
+  CStrings:  833
 
Symbols:
+ +[AEAssessmentAgentService registerRestrictionEnforcer:machServiceName:]
+ +[AESystemNotificationObservation observationWithNotificationName:queue:notificationHandler:]
+ -[AEAssessmentModeRestrictionEnforcementSession .cxx_destruct]
+ -[AEAssessmentModeRestrictionEnforcementSession dealloc]
+ -[AEAssessmentModeRestrictionEnforcementSession initWithRestrictionEnforcer:machServiceName:]
+ -[AEAssessmentModeRestrictionEnforcementSession invalidate]
+ -[AEAssessmentModeRestrictionEnforcementSession listener:shouldAcceptNewConnection:]
+ -[AEAssessmentModeRestrictionEnforcerProxy .cxx_destruct]
+ -[AEAssessmentModeRestrictionEnforcerProxy dealloc]
+ -[AEAssessmentModeRestrictionEnforcerProxy initWithMachServiceName:queue:]
+ -[AEAssessmentModeRestrictionEnforcerProxy invalidate]
+ -[AEAssessmentModeRestrictionEnforcerProxy proxy]
+ -[AEAssessmentModeRestrictionEnforcerProxy shouldBeginRestrictingForAssessmentModeWithCompletion:]
+ -[AEAssessmentModeRestrictionEnforcerProxy shouldEndRestrictingForAssessmentModeWithCompletion:]
+ -[AEConcreteDevicePrimitives deviceType]
+ -[AEConcreteDevicePrimitives init]
+ -[AEConcretePreferencePrimitives numberForKey:]
+ -[AEConcretePreferencePrimitives objectForKey:ofClass:]
+ -[AEConcretePreferencePrimitives setNumber:forKey:]
+ -[AEConcretePreferences assessmentNumberForKey:]
+ -[AEConcretePreferences expirationTime]
+ -[AEConcretePreferences setAllowRemotelyKillingAgent:]
+ -[AEConcretePreferences setEnforceSingleAppMode:]
+ -[AEConcretePreferences setExpirationTime:]
+ -[AEConcretePreferences setForceScreenMirroring:]
+ -[AEConcretePreferences setShowPromptsAndBanners:]
+ -[AEConcretePreferences shouldAllowRemotelyKillingAgent]
+ -[AEConcretePreferences shouldEnforceSingleAppMode]
+ -[AEConcretePreferences shouldForceScreenMirroring]
+ -[AEConcretePreferences shouldShowPromptsAndBanners]
+ -[AEDevicePrimitivesProvider makePrimitives]
+ -[AEEmptyPreferences expirationTime]
+ -[AEEmptyPreferences setAllowRemotelyKillingAgent:]
+ -[AEEmptyPreferences setEnforceSingleAppMode:]
+ -[AEEmptyPreferences setExpirationTime:]
+ -[AEEmptyPreferences setForceScreenMirroring:]
+ -[AEEmptyPreferences setShowPromptsAndBanners:]
+ -[AEEmptyPreferences shouldAllowRemotelyKillingAgent]
+ -[AEEmptyPreferences shouldEnforceSingleAppMode]
+ -[AEEmptyPreferences shouldForceScreenMirroring]
+ -[AEEmptyPreferences shouldShowPromptsAndBanners]
+ -[AELifecycleEventHandlingProxy _handleEventWantsBeginSingleAppModeWithCompletion:]
+ -[AELifecycleEventHandlingProxy _handleEventWantsEndSingleAppModeWithCompletion:]
+ -[AELifecycleEventHandlingProxy _handleEventWantsPresentBannerWithTitle:duration:completion:]
+ -[AELifecycleEventHandlingProxy _handleEventWantsPresentChoicePromptWithTitle:message:confirmTitle:cancelTitle:completion:]
+ -[AELifecycleEventHandlingProxy handleEventWantsBeginSingleAppModeWithCompletion:]
+ -[AELifecycleEventHandlingProxy handleEventWantsEndSingleAppModeWithCompletion:]
+ -[AELifecycleEventHandlingProxy handleEventWantsPresentBannerWithTitle:duration:completion:]
+ -[AELifecycleEventHandlingProxy handleEventWantsPresentChoicePromptWithTitle:message:confirmTitle:cancelTitle:completion:]
+ -[AESystemNotificationObservation .cxx_destruct]
+ -[AESystemNotificationObservation beginObserving]
+ -[AESystemNotificationObservation fire]
+ -[AESystemNotificationObservation initWithNotificationName:queue:notificationHandler:]
+ -[AESystemNotificationObservation invalidate]
+ -[AESystemNotificationObservation notificationHandler]
+ -[AESystemNotificationObservation notificationName]
+ -[AESystemNotificationObservation queue]
+ -[AESystemNotificationObservation setNotificationHandler:]
+ -[NSProcessInfo(AEAdditions) ae_hasEntitlement:withValue:]
+ _AEAssessmentModeEntitlement
+ _AEAssessmentModeLegacyEntitlement
+ _AEAssessmentSessionExpirationTimeInSeconds
+ _AEIsAssessmentModeAvailableForDeviceType
+ _AEIsMultiAppAvailableForDeviceType
+ _AEIsProcessEntitledForAssessmentMode
+ _AEIsProcessEntitledForMultiApp
+ _AEKillAssessmentAgentNotificationName
+ _MGGetSInt32Answer
+ _NSMultipleUnderlyingErrorsKey
+ _OBJC_CLASS_$_AEAssessmentAgentService
+ _OBJC_CLASS_$_AEAssessmentModeRestrictionEnforcementSession
+ _OBJC_CLASS_$_AEAssessmentModeRestrictionEnforcerProxy
+ _OBJC_CLASS_$_AEConcreteDevicePrimitives
+ _OBJC_CLASS_$_AEDevicePrimitivesProvider
+ _OBJC_CLASS_$_AESystemNotificationObservation
+ _OBJC_CLASS_$_NSXPCListener
+ _OBJC_IVAR_$_AEAssessmentModeRestrictionEnforcementSession._enforcer
+ _OBJC_IVAR_$_AEAssessmentModeRestrictionEnforcementSession._machServiceName
+ _OBJC_IVAR_$_AEAssessmentModeRestrictionEnforcementSession._xpcListener
+ _OBJC_IVAR_$_AEAssessmentModeRestrictionEnforcerProxy._machServiceName
+ _OBJC_IVAR_$_AEAssessmentModeRestrictionEnforcerProxy._proxy
+ _OBJC_IVAR_$_AEAssessmentModeRestrictionEnforcerProxy._queue
+ _OBJC_IVAR_$_AEConcreteDevicePrimitives._deviceTypeInternal
+ _OBJC_IVAR_$_AESystemNotificationObservation._notificationHandler
+ _OBJC_IVAR_$_AESystemNotificationObservation._notificationName
+ _OBJC_IVAR_$_AESystemNotificationObservation._queue
+ _OBJC_METACLASS_$_AEAssessmentAgentService
+ _OBJC_METACLASS_$_AEAssessmentModeRestrictionEnforcementSession
+ _OBJC_METACLASS_$_AEAssessmentModeRestrictionEnforcerProxy
+ _OBJC_METACLASS_$_AEConcreteDevicePrimitives
+ _OBJC_METACLASS_$_AEDevicePrimitivesProvider
+ _OBJC_METACLASS_$_AESystemNotificationObservation
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ __OBJC_$_CLASS_METHODS_AEAssessmentAgentService
+ __OBJC_$_CLASS_METHODS_AESystemNotificationObservation
+ __OBJC_$_INSTANCE_METHODS_AEAssessmentModeRestrictionEnforcementSession
+ __OBJC_$_INSTANCE_METHODS_AEAssessmentModeRestrictionEnforcerProxy
+ __OBJC_$_INSTANCE_METHODS_AEConcreteDevicePrimitives
+ __OBJC_$_INSTANCE_METHODS_AEDevicePrimitivesProvider
+ __OBJC_$_INSTANCE_METHODS_AESystemNotificationObservation
+ __OBJC_$_INSTANCE_VARIABLES_AEAssessmentModeRestrictionEnforcementSession
+ __OBJC_$_INSTANCE_VARIABLES_AEAssessmentModeRestrictionEnforcerProxy
+ __OBJC_$_INSTANCE_VARIABLES_AEConcreteDevicePrimitives
+ __OBJC_$_INSTANCE_VARIABLES_AESystemNotificationObservation
+ __OBJC_$_PROP_LIST_AEAssessmentModeRestrictionEnforcementSession
+ __OBJC_$_PROP_LIST_AEConcreteDevicePrimitives
+ __OBJC_$_PROP_LIST_AEDevicePrimitives
+ __OBJC_$_PROP_LIST_AESystemNotificationObservation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AEAssessmentModeRestrictionEnforcer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AEDevicePrimitives
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AEInvalidatable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AEAssessmentModeRestrictionEnforcer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AEDevicePrimitives
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AEInvalidatable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AEAssessmentModeRestrictionEnforcementSession
+ __OBJC_CLASS_PROTOCOLS_$_AEAssessmentModeRestrictionEnforcerProxy
+ __OBJC_CLASS_PROTOCOLS_$_AEConcreteDevicePrimitives
+ __OBJC_CLASS_PROTOCOLS_$_AESystemNotificationObservation
+ __OBJC_CLASS_RO_$_AEAssessmentAgentService
+ __OBJC_CLASS_RO_$_AEAssessmentModeRestrictionEnforcementSession
+ __OBJC_CLASS_RO_$_AEAssessmentModeRestrictionEnforcerProxy
+ __OBJC_CLASS_RO_$_AEConcreteDevicePrimitives
+ __OBJC_CLASS_RO_$_AEDevicePrimitivesProvider
+ __OBJC_CLASS_RO_$_AESystemNotificationObservation
+ __OBJC_LABEL_PROTOCOL_$_AEAssessmentModeRestrictionEnforcer
+ __OBJC_LABEL_PROTOCOL_$_AEDevicePrimitives
+ __OBJC_LABEL_PROTOCOL_$_AEInvalidatable
+ __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_METACLASS_RO_$_AEAssessmentAgentService
+ __OBJC_METACLASS_RO_$_AEAssessmentModeRestrictionEnforcementSession
+ __OBJC_METACLASS_RO_$_AEAssessmentModeRestrictionEnforcerProxy
+ __OBJC_METACLASS_RO_$_AEConcreteDevicePrimitives
+ __OBJC_METACLASS_RO_$_AEDevicePrimitivesProvider
+ __OBJC_METACLASS_RO_$_AESystemNotificationObservation
+ __OBJC_PROTOCOL_$_AEAssessmentModeRestrictionEnforcer
+ __OBJC_PROTOCOL_$_AEDevicePrimitives
+ __OBJC_PROTOCOL_$_AEInvalidatable
+ __OBJC_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_AEAssessmentModeRestrictionEnforcer
+ ___122-[AELifecycleEventHandlingProxy handleEventWantsPresentChoicePromptWithTitle:message:confirmTitle:cancelTitle:completion:]_block_invoke
+ ___122-[AELifecycleEventHandlingProxy handleEventWantsPresentChoicePromptWithTitle:message:confirmTitle:cancelTitle:completion:]_block_invoke_2
+ ___123-[AELifecycleEventHandlingProxy _handleEventWantsPresentChoicePromptWithTitle:message:confirmTitle:cancelTitle:completion:]_block_invoke
+ ___39-[AESystemNotificationObservation fire]_block_invoke
+ ___80-[AELifecycleEventHandlingProxy handleEventWantsEndSingleAppModeWithCompletion:]_block_invoke
+ ___80-[AELifecycleEventHandlingProxy handleEventWantsEndSingleAppModeWithCompletion:]_block_invoke_2
+ ___81-[AELifecycleEventHandlingProxy _handleEventWantsEndSingleAppModeWithCompletion:]_block_invoke
+ ___82-[AELifecycleEventHandlingProxy handleEventWantsBeginSingleAppModeWithCompletion:]_block_invoke
+ ___82-[AELifecycleEventHandlingProxy handleEventWantsBeginSingleAppModeWithCompletion:]_block_invoke_2
+ ___83-[AELifecycleEventHandlingProxy _handleEventWantsBeginSingleAppModeWithCompletion:]_block_invoke
+ ___84-[AEAssessmentModeRestrictionEnforcementSession listener:shouldAcceptNewConnection:]_block_invoke
+ ___84-[AEAssessmentModeRestrictionEnforcementSession listener:shouldAcceptNewConnection:]_block_invoke.cold.1
+ ___92-[AELifecycleEventHandlingProxy handleEventWantsPresentBannerWithTitle:duration:completion:]_block_invoke
+ ___92-[AELifecycleEventHandlingProxy handleEventWantsPresentBannerWithTitle:duration:completion:]_block_invoke_2
+ ___93-[AELifecycleEventHandlingProxy _handleEventWantsPresentBannerWithTitle:duration:completion:]_block_invoke
+ ___96-[AEAssessmentModeRestrictionEnforcerProxy shouldEndRestrictingForAssessmentModeWithCompletion:]_block_invoke
+ ___96-[AEAssessmentModeRestrictionEnforcerProxy shouldEndRestrictingForAssessmentModeWithCompletion:]_block_invoke_2
+ ___96-[AEAssessmentModeRestrictionEnforcerProxy shouldEndRestrictingForAssessmentModeWithCompletion:]_block_invoke_3
+ ___98-[AEAssessmentModeRestrictionEnforcerProxy shouldBeginRestrictingForAssessmentModeWithCompletion:]_block_invoke
+ ___98-[AEAssessmentModeRestrictionEnforcerProxy shouldBeginRestrictingForAssessmentModeWithCompletion:]_block_invoke_2
+ ___98-[AEAssessmentModeRestrictionEnforcerProxy shouldBeginRestrictingForAssessmentModeWithCompletion:]_block_invoke_3
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
+ _objc_msgSend$activate
+ _objc_msgSend$ae_hasEntitlement:withValue:
+ _objc_msgSend$allowsKeyboardShortcuts
+ _objc_msgSend$beginObserving
+ _objc_msgSend$deviceType
+ _objc_msgSend$doubleValue
+ _objc_msgSend$fire
+ _objc_msgSend$handleEventWantsBeginSingleAppModeWithCompletion:
+ _objc_msgSend$handleEventWantsEndSingleAppModeWithCompletion:
+ _objc_msgSend$handleEventWantsPresentBannerWithTitle:duration:completion:
+ _objc_msgSend$handleEventWantsPresentChoicePromptWithTitle:message:confirmTitle:cancelTitle:completion:
+ _objc_msgSend$initWithMachServiceName:
+ _objc_msgSend$initWithNotificationName:queue:notificationHandler:
+ _objc_msgSend$notificationHandler
+ _objc_msgSend$notificationName
+ _objc_msgSend$numberForKey:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$observationWithNotificationName:queue:notificationHandler:
+ _objc_msgSend$queue
+ _objc_msgSend$setAllowsKeyboardShortcuts:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setNotificationHandler:
+ _objc_msgSend$setNumber:forKey:
+ _objc_msgSend$shouldBeginRestrictingForAssessmentModeWithCompletion:
+ _objc_msgSend$shouldEndRestrictingForAssessmentModeWithCompletion:
+ _objc_msgSend$valueForEntitlement:
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
- +[AEConcreteSystemNotificationObservation observationWithNotificationName:queue:notificationHandler:]
- -[AEConcreteSystemNotificationObservation .cxx_destruct]
- -[AEConcreteSystemNotificationObservation beginObserving]
- -[AEConcreteSystemNotificationObservation fire]
- -[AEConcreteSystemNotificationObservation initWithNotificationName:queue:notificationHandler:]
- -[AEConcreteSystemNotificationObservation invalidate]
- _OBJC_CLASS_$_AEConcreteSystemNotificationObservation
- _OBJC_IVAR_$_AEConcreteSystemNotificationObservation._notificationHandler
- _OBJC_IVAR_$_AEConcreteSystemNotificationObservation._notificationName
- _OBJC_IVAR_$_AEConcreteSystemNotificationObservation._queue
- _OBJC_METACLASS_$_AEConcreteSystemNotificationObservation
- __OBJC_$_INSTANCE_METHODS_AEConcreteSystemNotificationObservation
- __OBJC_$_INSTANCE_VARIABLES_AEConcreteSystemNotificationObservation
- __OBJC_CLASS_PROTOCOLS_$_AEConcreteSystemNotificationObservation
- __OBJC_CLASS_RO_$_AEConcreteSystemNotificationObservation
- __OBJC_METACLASS_RO_$_AEConcreteSystemNotificationObservation
- ___47-[AEConcreteSystemNotificationObservation fire]_block_invoke
CStrings:
+ "\x01\x11"
+ "\x11"
+ "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilitySpeech = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@}>"
+ "@\"<AEAssessmentModeRestrictionEnforcer>\""
+ "@\"NSXPCListener\""
+ "@40@0:8@16@24@?32"
+ "AEAssessmentAgentService"
+ "AEAssessmentModeRestrictionEnforcementSession"
+ "AEAssessmentModeRestrictionEnforcer"
+ "AEAssessmentModeRestrictionEnforcerProxy"
+ "AEConcreteDevicePrimitives"
+ "AEDevicePrimitives"
+ "AEDevicePrimitivesProvider"
+ "AEInvalidatable"
+ "AESystemNotificationObservation"
+ "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
+ "B32@0:8@16@24"
+ "DeviceClassNumber"
+ "EnforcementSession connection interrupted"
+ "ExpirationTime"
+ "IgnoreEnforceSingleAppMode"
+ "IgnoreForceScreenMirroring"
+ "IgnoreShowPromptsAndBanners"
+ "KillAssessmentAgent"
+ "NSXPCListenerDelegate"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSString\",R,C,N,V_notificationName"
+ "T@?,C,N,V_notificationHandler"
+ "TB,N,GshouldAllowRemotelyKillingAgent"
+ "TB,N,GshouldEnforceSingleAppMode"
+ "TB,N,GshouldForceScreenMirroring"
+ "TB,N,GshouldShowPromptsAndBanners"
+ "Td,N"
+ "_deviceTypeInternal"
+ "_enforcer"
+ "_proxy"
+ "_xpcListener"
+ "activate"
+ "ae_hasEntitlement:withValue:"
+ "allowRemotelyKillingAgent"
+ "beginObserving"
+ "com.apple.developer.automatic-assessment-configuration"
+ "com.apple.developer.edu-assessment-mode"
+ "com.apple.private.automatic-assessment-configuration.restrictor"
+ "d16@0:8"
+ "deviceType"
+ "doubleValue"
+ "enforceSingleAppMode"
+ "expirationTime"
+ "fire"
+ "forceScreenMirroring"
+ "handleEventWantsBeginSingleAppModeWithCompletion:"
+ "handleEventWantsEndSingleAppModeWithCompletion:"
+ "handleEventWantsPresentBannerWithTitle:duration:completion:"
+ "handleEventWantsPresentChoicePromptWithTitle:message:confirmTitle:cancelTitle:completion:"
+ "initWithMachServiceName:"
+ "initWithMachServiceName:queue:"
+ "initWithNotificationName:queue:notificationHandler:"
+ "listener:shouldAcceptNewConnection:"
+ "notificationHandler"
+ "notificationName"
+ "numberForKey:"
+ "numberWithDouble:"
+ "observationWithNotificationName:queue:notificationHandler:"
+ "queue"
+ "registerRestrictionEnforcer:machServiceName:"
+ "setAllowRemotelyKillingAgent:"
+ "setDelegate:"
+ "setEnforceSingleAppMode:"
+ "setExpirationTime:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setForceScreenMirroring:"
+ "setNotificationHandler:"
+ "setNumber:forKey:"
+ "setShowPromptsAndBanners:"
+ "shouldAllowRemotelyKillingAgent"
+ "shouldBeginRestrictingForAssessmentModeWithCompletion:"
+ "shouldEndRestrictingForAssessmentModeWithCompletion:"
+ "shouldEnforceSingleAppMode"
+ "shouldForceScreenMirroring"
+ "shouldShowPromptsAndBanners"
+ "showPromptsAndBanners"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8d16"
+ "v40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?B@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
+ "valueForEntitlement:"
- "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilitySpeech = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@ }>"
- "AEConcreteSystemNotificationObservation"

```
