## SpringBoardUIServices

> `/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices`

```diff

-4416.41.0.0.0
-  __TEXT.__text: 0x84e2c
-  __TEXT.__auth_stubs: 0x1480
-  __TEXT.__objc_methlist: 0x9704
+4416.132.102.0.0
+  __TEXT.__text: 0x85f68
+  __TEXT.__auth_stubs: 0x14a0
+  __TEXT.__objc_methlist: 0x989c
   __TEXT.__const: 0x778
-  __TEXT.__gcc_except_tab: 0x71c
-  __TEXT.__cstring: 0x8a0a
+  __TEXT.__gcc_except_tab: 0x734
+  __TEXT.__cstring: 0x8ab4
   __TEXT.__dlopen_cstrs: 0x2b8
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x36df
-  __TEXT.__unwind_info: 0x2698
-  __TEXT.__objc_classname: 0x2a09
-  __TEXT.__objc_methname: 0x1df01
-  __TEXT.__objc_methtype: 0x4d6f
-  __TEXT.__objc_stubs: 0x13460
+  __TEXT.__unwind_info: 0x2714
+  __TEXT.__objc_classname: 0x2b29
+  __TEXT.__objc_methname: 0x1e45f
+  __TEXT.__objc_methtype: 0x4e19
+  __TEXT.__objc_stubs: 0x13680
   __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x2470
-  __DATA_CONST.__objc_classlist: 0x650
+  __DATA_CONST.__const: 0x2518
+  __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x350
+  __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ee78
-  __DATA_CONST.__objc_selrefs: 0x64e0
+  __DATA_CONST.__objc_const: 0x1f538
+  __DATA_CONST.__objc_selrefs: 0x65b0
+  __DATA_CONST.__objc_protorefs: 0xb0
+  __DATA_CONST.__objc_classrefs: 0xa38
+  __DATA_CONST.__objc_superrefs: 0x490
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__cfstring: 0x88a0
-  __AUTH_CONST.__objc_const: 0x4820
-  __AUTH_CONST.__const: 0x660
-  __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__cfstring: 0x8940
+  __AUTH_CONST.__objc_const: 0x4a18
+  __AUTH_CONST.__const: 0x6c0
+  __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0xa50
-  __AUTH.__objc_data: 0x3430
-  __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0xa18
-  __DATA.__objc_superrefs: 0x478
-  __DATA.__objc_ivar: 0xae4
-  __DATA.__data: 0x28f0
-  __DATA.__bss: 0x1a8
+  __AUTH_CONST.__auth_got: 0xa60
+  __AUTH.__objc_data: 0x3660
+  __DATA.__objc_ivar: 0xaec
+  __DATA.__data: 0x2988
+  __DATA.__bss: 0x180
   __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3727
-  Symbols:   13864
-  CStrings:  6914
+  Functions: 3766
+  Symbols:   14025
+  CStrings:  6977
 
Symbols:
+ +[SBSUIFeaturePolicyClientSettingsExtension protocol]
+ +[SBSUIProximityReaderSceneExtension clientSettingsExtensions]
+ +[SBSUIProximityReaderSceneExtension hostComponents]
+ +[SBUILegibilityContainerView legibilityImageDisposalQueue]
+ -[SBSUIFeaturePolicyHostComponent .cxx_destruct]
+ -[SBSUIFeaturePolicyHostComponent allowsMenuButtonDismissal]
+ -[SBSUIFeaturePolicyHostComponent delegate]
+ -[SBSUIFeaturePolicyHostComponent desiredBackgroundActivities]
+ -[SBSUIFeaturePolicyHostComponent desiredHardwareButtonEvents]
+ -[SBSUIFeaturePolicyHostComponent scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]
+ -[SBSUIFeaturePolicyHostComponent sendActions:]
+ -[SBSUIFeaturePolicyHostComponent setDelegate:]
+ -[SBSUIFeaturePolicyHostComponent shouldDisableAlertItems]
+ -[SBSUIFeaturePolicyHostComponent shouldDisableBanners]
+ -[SBSUIFeaturePolicyHostComponent shouldDisableControlCenter]
+ -[SBSUIFeaturePolicyHostComponent shouldDisableInteractiveScreenshotGesture]
+ -[SBSUIFeaturePolicyHostComponent shouldDisableReachability]
+ -[SBSUIFeaturePolicyHostComponent shouldDisableSiri]
+ -[SBSUIIdleTimerSceneHostComponent .cxx_destruct]
+ -[SBSUIIdleTimerSceneHostComponent delegate]
+ -[SBSUIIdleTimerSceneHostComponent scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]
+ -[SBSUIIdleTimerSceneHostComponent setDelegate:]
+ -[SBSUIProximityReaderSceneRequestBuilder _specification]
+ -[SBSUIProximityReaderSceneSpecification defaultExtensions]
+ -[SBSUIProximityReaderSceneSpecification uiSceneSessionRole]
+ -[SBUIBackgroundActivityAction backgroundActivityIdentifier]
+ -[SBUIBackgroundActivityAction initWithBackgroundActivityIdentifier:handler:]
+ -[SBUIBackgroundActivityAction keyDescriptionForSetting:]
+ -[SBUIBackgroundActivityAction setProceed:]
+ -[SBUIButtonAction buttonEvents]
+ -[SBUIButtonAction initWithButtonEvents:]
+ -[SBUIButtonAction initWithButtonEvents:withHandler:]
+ -[SBUIButtonAction sendResponse:withCompletion:]
+ -[SBUIButtonAction sendResponseWithUnHandledButtonEvents:]
+ -[SBUIButtonAction settings:keyDescriptionForSetting:]
+ -[SBUIButtonAction settings:valueDescriptionForFlag:object:ofSetting:]
+ -[SBUIButtonActionResponse initWithUnHandledButtonEvents:]
+ -[SBUIButtonActionResponse settings:keyDescriptionForSetting:]
+ -[SBUIButtonActionResponse settings:valueDescriptionForFlag:object:ofSetting:]
+ -[SBUIButtonActionResponse unHandledButtonEvents]
+ -[SBUILegibilityContainerView _resetImages]
+ -[SBUILegibilityContainerView dealloc]
+ -[SBUIProudLockContainerViewController orientation]
+ -[SBUISystemApertureElementSource requestAlertingAssertionWithOptions:]
+ -[SBUISystemApertureElementUnassociatedContext requestAlertingAssertionWithOptions:]
+ -[UIView(ControlCenterInvocationHint) SBSUI_sourceRectForControlCenterInvocationHint]
+ GCC_except_table158
+ GCC_except_table160
+ _BSDispatchQueueCreateWithQualityOfService
+ _OBJC_CLASS_$_SBSUIFeaturePolicyClientSettingsExtension
+ _OBJC_CLASS_$_SBSUIFeaturePolicyHostComponent
+ _OBJC_CLASS_$_SBSUIIdleTimerSceneHostComponent
+ _OBJC_CLASS_$_SBSUIProximityReaderSceneExtension
+ _OBJC_CLASS_$_SBSUIProximityReaderSceneRequestBuilder
+ _OBJC_CLASS_$_SBSUIProximityReaderSceneSpecification
+ _OBJC_CLASS_$_SBUIBackgroundActivityAction
+ _OBJC_CLASS_$_SBUIButtonAction
+ _OBJC_CLASS_$_SBUIButtonActionResponse
+ _OBJC_IVAR_$_SBSUIFeaturePolicyHostComponent._delegate
+ _OBJC_IVAR_$_SBSUIIdleTimerSceneHostComponent._delegate
+ _OBJC_METACLASS_$_SBSUIFeaturePolicyClientSettingsExtension
+ _OBJC_METACLASS_$_SBSUIFeaturePolicyHostComponent
+ _OBJC_METACLASS_$_SBSUIIdleTimerSceneHostComponent
+ _OBJC_METACLASS_$_SBSUIProximityReaderSceneExtension
+ _OBJC_METACLASS_$_SBSUIProximityReaderSceneRequestBuilder
+ _OBJC_METACLASS_$_SBSUIProximityReaderSceneSpecification
+ _OBJC_METACLASS_$_SBUIBackgroundActivityAction
+ _OBJC_METACLASS_$_SBUIButtonAction
+ _OBJC_METACLASS_$_SBUIButtonActionResponse
+ _SBSUIWindowSceneSessionRoleProximityReader
+ _SBUIServiceButtonEventDescription
+ __OBJC_$_CLASS_METHODS_SBSUIFeaturePolicyClientSettingsExtension
+ __OBJC_$_CLASS_METHODS_SBSUIProximityReaderSceneExtension
+ __OBJC_$_CLASS_METHODS_SBUILegibilityContainerView
+ __OBJC_$_CLASS_METHODS_UIView(SBUISystemApertureStyling|ControlCenterInvocationHint|SBUtilities|SBUISystemAperturePrivate|SBUISystemAperture|SBUISystemApertureDynamicLayoutSupport|SBUISystemApertureStaticLayoutSupport|SBUISystemApertureAnimationParameters|SBUISystemApertureElementContextProviding)
+ __OBJC_$_INSTANCE_METHODS_SBSUIFeaturePolicyHostComponent
+ __OBJC_$_INSTANCE_METHODS_SBSUIIdleTimerSceneHostComponent
+ __OBJC_$_INSTANCE_METHODS_SBSUIProximityReaderSceneRequestBuilder
+ __OBJC_$_INSTANCE_METHODS_SBSUIProximityReaderSceneSpecification
+ __OBJC_$_INSTANCE_METHODS_SBUIBackgroundActivityAction
+ __OBJC_$_INSTANCE_METHODS_SBUIButtonAction
+ __OBJC_$_INSTANCE_METHODS_SBUIButtonActionResponse
+ __OBJC_$_INSTANCE_METHODS_UIView(SBUISystemApertureStyling|ControlCenterInvocationHint|SBUtilities|SBUISystemAperturePrivate|SBUISystemAperture|SBUISystemApertureDynamicLayoutSupport|SBUISystemApertureStaticLayoutSupport|SBUISystemApertureAnimationParameters|SBUISystemApertureElementContextProviding)
+ __OBJC_$_INSTANCE_VARIABLES_SBSUIFeaturePolicyHostComponent
+ __OBJC_$_INSTANCE_VARIABLES_SBSUIIdleTimerSceneHostComponent
+ __OBJC_$_PROP_LIST_SBSUIFeaturePolicyClientSettings
+ __OBJC_$_PROP_LIST_SBSUIFeaturePolicyHostComponent
+ __OBJC_$_PROP_LIST_SBSUIIdleTimerSceneHostComponent
+ __OBJC_$_PROP_LIST_SBSUILoginUISceneClientSettings.78
+ __OBJC_$_PROP_LIST_SBSUIStarkNotificationsSceneClientSettings.54
+ __OBJC_$_PROP_LIST_SBSUIStarkNotificationsSceneSettings.83
+ __OBJC_$_PROP_LIST_SBUIBackgroundActivityAction
+ __OBJC_$_PROP_LIST_SBUIBiometricResource.336
+ __OBJC_$_PROP_LIST_SBUIButtonAction
+ __OBJC_$_PROP_LIST_SBUIButtonActionResponse
+ __OBJC_$_PROP_LIST_SBUILegibilitySettings.175
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSUIFeaturePolicyClientSettings
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSUIFeaturePolicyClientSettings
+ __OBJC_$_PROTOCOL_REFS_SBSUIFeaturePolicyClientSettings
+ __OBJC_CLASS_RO_$_SBSUIFeaturePolicyClientSettingsExtension
+ __OBJC_CLASS_RO_$_SBSUIFeaturePolicyHostComponent
+ __OBJC_CLASS_RO_$_SBSUIIdleTimerSceneHostComponent
+ __OBJC_CLASS_RO_$_SBSUIProximityReaderSceneExtension
+ __OBJC_CLASS_RO_$_SBSUIProximityReaderSceneRequestBuilder
+ __OBJC_CLASS_RO_$_SBSUIProximityReaderSceneSpecification
+ __OBJC_CLASS_RO_$_SBUIBackgroundActivityAction
+ __OBJC_CLASS_RO_$_SBUIButtonAction
+ __OBJC_CLASS_RO_$_SBUIButtonActionResponse
+ __OBJC_LABEL_PROTOCOL_$_SBSUIFeaturePolicyClientSettings
+ __OBJC_METACLASS_RO_$_SBSUIFeaturePolicyClientSettingsExtension
+ __OBJC_METACLASS_RO_$_SBSUIFeaturePolicyHostComponent
+ __OBJC_METACLASS_RO_$_SBSUIIdleTimerSceneHostComponent
+ __OBJC_METACLASS_RO_$_SBSUIProximityReaderSceneExtension
+ __OBJC_METACLASS_RO_$_SBSUIProximityReaderSceneRequestBuilder
+ __OBJC_METACLASS_RO_$_SBSUIProximityReaderSceneSpecification
+ __OBJC_METACLASS_RO_$_SBUIBackgroundActivityAction
+ __OBJC_METACLASS_RO_$_SBUIButtonAction
+ __OBJC_METACLASS_RO_$_SBUIButtonActionResponse
+ __OBJC_PROTOCOL_$_SBSUIFeaturePolicyClientSettings
+ __OBJC_PROTOCOL_REFERENCE_$_SBSUIFeaturePolicyClientSettings
+ ___124+[UIButtonConfiguration(SBUISystemApertureStyling) sbui_systemApertureTextButtonConfigurationCompatibleWithTraitCollection:]_block_invoke
+ ___41-[SBUIButtonAction initWithButtonEvents:]_block_invoke
+ ___43-[SBUILegibilityContainerView _resetImages]_block_invoke
+ ___47-[SBSUIFeaturePolicyHostComponent sendActions:]_block_invoke
+ ___53-[SBUIButtonAction initWithButtonEvents:withHandler:]_block_invoke
+ ___59+[SBUILegibilityContainerView legibilityImageDisposalQueue]_block_invoke
+ ___60-[SBSUIProximityReaderSceneSpecification uiSceneSessionRole]_block_invoke
+ ___71-[SBUISystemApertureElementSource requestAlertingAssertionWithOptions:]_block_invoke
+ ___77-[SBUIBackgroundActivityAction initWithBackgroundActivityIdentifier:handler:]_block_invoke
+ ___96+[UIButtonConfiguration(SBUISystemApertureStyling) sbui_systemApertureSymbolButtonConfiguration]_block_invoke
+ ___block_descriptor_32_e26_"UIColor"16?0"UIColor"8l
+ ___block_descriptor_32_e34_v16?0"SBUIButtonActionResponse"8l
+ ___block_descriptor_40_e8_32bs_e34_v16?0"SBUIButtonActionResponse"8ls32l8
+ ___block_descriptor_49_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
+ ___block_literal_global.16
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _legibilityImageDisposalQueue.disposalQueue
+ _legibilityImageDisposalQueue.onceToken
+ _objc_msgSend$_resetImages
+ _objc_msgSend$animateWithSpringDuration:bounce:initialSpringVelocity:delay:options:animations:completion:
+ _objc_msgSend$background
+ _objc_msgSend$buttonEvents
+ _objc_msgSend$desiredBackgroundActivities
+ _objc_msgSend$featurePolicyHostComponentDidChangeAllowsMenuButtonDismissal:
+ _objc_msgSend$featurePolicyHostComponentDidChangeDesiredBackgroundActivities:
+ _objc_msgSend$featurePolicyHostComponentDidChangeDesiredHardwareButtonEvents:
+ _objc_msgSend$featurePolicyHostComponentDidChangeShouldDisableAlertItems:
+ _objc_msgSend$featurePolicyHostComponentDidChangeShouldDisableBanners:
+ _objc_msgSend$featurePolicyHostComponentDidChangeShouldDisableControlCenter:
+ _objc_msgSend$featurePolicyHostComponentDidChangeShouldDisableInteractiveScreenshotGesture:
+ _objc_msgSend$featurePolicyHostComponentDidChangeShouldDisableReachability:
+ _objc_msgSend$featurePolicyHostComponentDidChangeShouldDisableSiri:
+ _objc_msgSend$idleTimerDisabled
+ _objc_msgSend$idleTimerSceneHostComponentDidChangeShouldDisableIdleTimer:
+ _objc_msgSend$initWithButtonEvents:withHandler:
+ _objc_msgSend$initWithUnHandledButtonEvents:
+ _objc_msgSend$legibilityImageDisposalQueue
+ _objc_msgSend$orientation
+ _objc_msgSend$requestAlertingAssertionWithOptions:
+ _objc_msgSend$setBackgroundColorTransformer:
+ _objc_msgSend$unHandledButtonEvents
- +[SBSUIProxReaderSceneExtension hostComponents]
- -[SBSUIProxReaderSceneRequestBuilder _specification]
- -[SBSUIProxReaderSceneSpecification defaultExtensions]
- -[SBSUIProxReaderSceneSpecification uiSceneSessionRole]
- -[SBSUIRemoteAlertSceneHostComponent allowsMenuButtonDismissal]
- -[SBSUIRemoteAlertSceneHostComponent desiredHardwareButtonEvents]
- -[SBSUIRemoteAlertSceneHostComponent shouldDisableAlertItems]
- -[SBSUIRemoteAlertSceneHostComponent shouldDisableBanners]
- -[SBSUIRemoteAlertSceneHostComponent shouldDisableControlCenter]
- -[SBSUIRemoteAlertSceneHostComponent shouldDisableInteractiveScreenshotGesture]
- -[SBSUIRemoteAlertSceneHostComponent shouldDisableReachability]
- -[SBSUIRemoteAlertSceneHostComponent shouldDisableSiri]
- -[SBUIRemoteAlertButtonAction sendResponse:withCompletion:]
- -[SBUIRemoteAlertButtonAction settings:keyDescriptionForSetting:]
- -[SBUIRemoteAlertButtonAction settings:valueDescriptionForFlag:object:ofSetting:]
- -[SBUIRemoteAlertButtonActionResponse settings:keyDescriptionForSetting:]
- -[SBUIRemoteAlertButtonActionResponse settings:valueDescriptionForFlag:object:ofSetting:]
- GCC_except_table157
- GCC_except_table159
- _OBJC_CLASS_$_SBSUIProxReaderSceneExtension
- _OBJC_CLASS_$_SBSUIProxReaderSceneRequestBuilder
- _OBJC_METACLASS_$_SBSUIProxReaderSceneExtension
- _OBJC_METACLASS_$_SBSUIProxReaderSceneRequestBuilder
- _SBSUIWindowSceneSessionRoleProxReader
- __OBJC_$_CLASS_METHODS_SBSUIProxReaderSceneExtension
- __OBJC_$_CLASS_METHODS_UIView(SBUISystemApertureStyling|SBUtilities|SBUISystemAperturePrivate|SBUISystemAperture|SBUISystemApertureDynamicLayoutSupport|SBUISystemApertureStaticLayoutSupport|SBUISystemApertureAnimationParameters|SBUISystemApertureElementContextProviding)
- __OBJC_$_INSTANCE_METHODS_SBSUIProxReaderSceneRequestBuilder
- __OBJC_$_INSTANCE_METHODS_SBSUIProxReaderSceneSpecification
- __OBJC_$_INSTANCE_METHODS_UIView(SBUISystemApertureStyling|SBUtilities|SBUISystemAperturePrivate|SBUISystemAperture|SBUISystemApertureDynamicLayoutSupport|SBUISystemApertureStaticLayoutSupport|SBUISystemApertureAnimationParameters|SBUISystemApertureElementContextProviding)
- __OBJC_$_PROP_LIST_SBSUILoginUISceneClientSettings.77
- __OBJC_$_PROP_LIST_SBSUIStarkNotificationsSceneClientSettings.53
- __OBJC_$_PROP_LIST_SBSUIStarkNotificationsSceneSettings.82
- __OBJC_$_PROP_LIST_SBUIBiometricResource.335
- __OBJC_$_PROP_LIST_SBUILegibilitySettings.174
- __OBJC_CLASS_RO_$_SBSUIProxReaderSceneExtension
- __OBJC_CLASS_RO_$_SBSUIProxReaderSceneRequestBuilder
- __OBJC_METACLASS_RO_$_SBSUIProxReaderSceneExtension
- __OBJC_METACLASS_RO_$_SBSUIProxReaderSceneRequestBuilder
- ___46-[SBUIRemoteAlertButtonAction initWithEvents:]_block_invoke
- ___55-[SBSUIProxReaderSceneSpecification uiSceneSessionRole]_block_invoke
- ___59-[SBUISystemApertureElementSource requestAlertingAssertion]_block_invoke
- ___block_descriptor_32_e45_v16?0"SBUIRemoteAlertButtonActionResponse"8l
- _objc_msgSend$initWithEvents:withHandler:
- _objc_msgSend$initWithUnHandledEvents:
- _objc_msgSend$remoteAlertSceneHostComponentDidChangeAllowsMenuButtonDismissal:
- _objc_msgSend$remoteAlertSceneHostComponentDidChangeDesiredHardwareButtonEvents:
- _objc_msgSend$remoteAlertSceneHostComponentDidChangeFeaturePolicy:
- _objc_msgSend$unHandledEvents
CStrings:
+ "@\"<SBSUIFeaturePolicyHostComponentDelegate>\""
+ "@\"<SBSUIIdleTimerSceneHostComponentDelegate>\""
+ "@\"<SBUISystemApertureAutomaticallyInvalidatable>\"24@0:8Q16"
+ "@\"UIColor\"16@?0@\"UIColor\"8"
+ "BKMatchFailReasonESDFailure"
+ "ControlCenterInvocationHint"
+ "SBSUIFeaturePolicyClientSettings"
+ "SBSUIFeaturePolicyClientSettingsExtension"
+ "SBSUIFeaturePolicyHostComponent"
+ "SBSUIIdleTimerSceneHostComponent"
+ "SBSUIProximityReaderSceneExtension"
+ "SBSUIProximityReaderSceneRequestBuilder"
+ "SBSUIProximityReaderSceneSpecification"
+ "SBSUIWindowSceneSessionRoleProximityReader"
+ "SBSUI_sourceRectForControlCenterInvocationHint"
+ "SBUIBackgroundActivityAction"
+ "SBUIBackgroundActivityAction.m"
+ "SBUIButtonAction"
+ "SBUIButtonAction responses must be SBUIButtonActionResponse instances"
+ "SBUIButtonAction.m"
+ "SBUIButtonActionResponse"
+ "T@\"<SBSUIFeaturePolicyHostComponentDelegate>\",W,N,V_delegate"
+ "T@\"<SBSUIIdleTimerSceneHostComponentDelegate>\",W,N,V_delegate"
+ "T@\"BSAction\",?,R,N"
+ "T@\"NSDate\",?,R,C,N"
+ "T@\"NSDate\",?,R,C,N,V_creationDate"
+ "T@\"NSSet\",?,R,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSURL\",?,R,C,N"
+ "T@\"UIColor\",?,R,C,N"
+ "T@\"UIView<SBUISystemApertureAccessoryView>\",?,R,N"
+ "T@\"UIWindow\",?,&,N"
+ "T@\"_UILegibilitySettings\",?,&,N"
+ "TB,?,N"
+ "TB,?,R,N"
+ "TQ,?,N"
+ "TQ,?,R,N"
+ "Td,?,N"
+ "Td,?,N,V_backgroundAlpha"
+ "Td,?,R,N"
+ "Tq,?,R,N"
+ "T{CGSize=dd},?,R,N"
+ "_resetImages"
+ "animateWithSpringDuration:bounce:initialSpringVelocity:delay:options:animations:completion:"
+ "background"
+ "backgroundActivityIdentifier"
+ "buttonEvents"
+ "com.apple.SpringBoard.legibilityImageDisposalQueue"
+ "desiredBackgroundActivities"
+ "featurePolicyHostComponentDidChangeAllowsMenuButtonDismissal:"
+ "featurePolicyHostComponentDidChangeDesiredBackgroundActivities:"
+ "featurePolicyHostComponentDidChangeDesiredHardwareButtonEvents:"
+ "featurePolicyHostComponentDidChangeShouldDisableAlertItems:"
+ "featurePolicyHostComponentDidChangeShouldDisableBanners:"
+ "featurePolicyHostComponentDidChangeShouldDisableControlCenter:"
+ "featurePolicyHostComponentDidChangeShouldDisableInteractiveScreenshotGesture:"
+ "featurePolicyHostComponentDidChangeShouldDisableReachability:"
+ "featurePolicyHostComponentDidChangeShouldDisableSiri:"
+ "idleTimerSceneHostComponentDidChangeShouldDisableIdleTimer:"
+ "initWithBackgroundActivityIdentifier:handler:"
+ "initWithButtonEvents:"
+ "initWithButtonEvents:withHandler:"
+ "initWithUnHandledButtonEvents:"
+ "legibilityImageDisposalQueue"
+ "orientation"
+ "proceed"
+ "requestAlertingAssertionWithOptions:"
+ "requestImplicitlyDismissableAlertingAssertion"
+ "sendResponseWithUnHandledButtonEvents:"
+ "setBackgroundColorTransformer:"
+ "setDesiredBackgroundActivities:"
+ "setProceed:"
+ "unHandledButtonEvents"
+ "updateBackgroundMaterial:"
+ "v16@?0@\"SBUIButtonActionResponse\"8"
+ "v24@0:8@\"NSArray\"16"
- "SBSUIProxReaderSceneExtension"
- "SBSUIProxReaderSceneRequestBuilder"
- "SBSUIWindowSceneSessionRoleProxReader"
- "SBUIRemoteAlertButtonAction responses must be SBUIRemoteAlertButtonActionResponse instances"
- "SBUIRemoteAlertButtonAction.m"
- "T@\"NSDate\",R,C,N"
- "T@\"NSDate\",R,C,N,V_creationDate"
- "T@\"UIColor\",R,C,N"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",R,N"
- "T@\"UIWindow\",&,N"
- "Td,N,V_backgroundAlpha"
- "remoteAlertSceneHostComponentDidChangeAllowsMenuButtonDismissal:"
- "remoteAlertSceneHostComponentDidChangeDesiredHardwareButtonEvents:"
- "remoteAlertSceneHostComponentDidChangeFeaturePolicy:"
- "v16@?0@\"SBUIRemoteAlertButtonActionResponse\"8"

```
