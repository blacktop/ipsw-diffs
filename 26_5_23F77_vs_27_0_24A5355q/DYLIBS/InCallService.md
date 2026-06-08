## InCallService

> `/System/Library/AccessibilityBundles/InCallService.axbundle/InCallService`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x4c1c
-  __TEXT.__auth_stubs: 0x3c0
+3036.2.0.0.0
+  __TEXT.__text: 0x4924
   __TEXT.__objc_methlist: 0x858
+  __TEXT.__const: 0x18
+  __TEXT.__gcc_except_tab: 0xa0
   __TEXT.__cstring: 0xe3a
-  __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0xb8
   __TEXT.__oslogstring: 0x5f
-  __TEXT.__unwind_info: 0x230
-  __TEXT.__objc_classname: 0x697
-  __TEXT.__objc_methname: 0x106a
-  __TEXT.__objc_methtype: 0xb6
-  __TEXT.__objc_stubs: 0xd60
-  __DATA_CONST.__got: 0x128
+  __TEXT.__unwind_info: 0x238
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4e8
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__got: 0x128
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x1360
   __AUTH_CONST.__objc_const: 0x1710
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xcd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 966CF76C-4741-3059-B6E0-4CDCCCF1CB4F
+  UUID: 4DE8ADF6-9BC1-323E-852C-54B383836D9A
   Functions: 163
-  Symbols:   768
-  CStrings:  541
+  Symbols:   773
+  CStrings:  326
 
Symbols:
+ GCC_except_table139
+ GCC_except_table158
+ GCC_except_table45
+ GCC_except_table51
+ GCC_except_table87
+ ___block_literal_global.384
+ ___block_literal_global.393
+ ___block_literal_global.413
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_storeStrong
- GCC_except_table20
- GCC_except_table25
- GCC_except_table3
- GCC_except_table4
- GCC_except_table8
- ___block_literal_global.363
- ___block_literal_global.372
- _objc_retain_x20
- _objc_retain_x21
Functions:
~ +[AXInCallServiceGlue accessibilityInitializeBundle] : 104 -> 100
~ ___52+[AXInCallServiceGlue accessibilityInitializeBundle]_block_invoke : 272 -> 268
~ ___52+[AXInCallServiceGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ ___52+[AXInCallServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 460 -> 452
~ _accessibilityMobilePhoneLocalizedString : 228 -> 212
~ _accessibilityLocalizedString : 184 -> 176
~ _axStringForCallParticipantsView : 696 -> 664
~ +[PHCallParticipantsViewAccessibility _accessibilityPerformValidations:] : 316 -> 308
~ -[PHCallParticipantsViewAccessibility updateParticipantsAnimated:] : 292 -> 280
~ -[PHCallParticipantsViewAccessibility isAccessibilityElement] : 108 -> 104
~ -[PHCallParticipantsViewAccessibility _accessibilityIsDisplayedInBanner] : 80 -> 76
~ -[InCallServiceApplicationAccessibility accessibilityLabel] : 120 -> 112
~ -[InCallServiceApplicationAccessibility _axGetFirstCall] : 120 -> 108
~ +[PHActionSliderAccessibility _accessibilityPerformValidations:] : 272 -> 264
~ -[PHActionSliderAccessibility accessibilityPath] : 212 -> 196
~ -[PHActionSliderAccessibility accessibilityLabel] : 168 -> 156
~ -[PHAudioCallControlsViewAccessibility assignControlType:toButton:] : 148 -> 144
~ +[PHAudioCallViewControllerAccessibility _accessibilityPerformValidations:] : 540 -> 532
~ -[PHAudioCallViewControllerAccessibility _accessibilitySubscribeForBottomBarNotificationsIfNecessary] : 136 -> 128
~ -[PHAudioCallViewControllerAccessibility dealloc] : 120 -> 112
~ -[PHAudioCallViewControllerAccessibility _accessibilityAnnounceIncomingCallUsingCurrentCallInfo:] : 1056 -> 972
~ -[PHAudioCallViewControllerAccessibility _axSetPhoneToMiddleState:totalTimeTried:] : 304 -> 292
~ ___82-[PHAudioCallViewControllerAccessibility _axSetPhoneToMiddleState:totalTimeTried:]_block_invoke : 388 -> 384
~ -[PHAudioCallViewControllerAccessibility setMiddleViewState:animated:completion:] : 352 -> 356
~ +[PHBottomBarAccessibility _accessibilityPerformValidations:] : 352 -> 344
~ -[PHBottomBarAccessibility _accessibilityLoadAccessibilityInformation] : 364 -> 340
~ -[PHBottomBarAccessibility setAnimating:] : 160 -> 152
~ +[PHCountdownViewAccessibility _accessibilityPerformValidations:] : 360 -> 348
~ -[PHCountdownViewAccessibility startCountdown] : 772 -> 696
~ ___46-[PHCountdownViewAccessibility startCountdown]_block_invoke : 268 -> 264
~ ___46-[PHCountdownViewAccessibility startCountdown]_block_invoke_2 : 84 -> 80
~ +[PHEmergencyDialerViewControllerAccessibility _accessibilityPerformValidations:] : 208 -> 200
~ -[PHEmergencyDialerViewControllerAccessibility viewDidDisappear:] : 248 -> 232
~ -[PHEmergencyDialerViewControllerAccessibility viewDidAppear:] : 348 -> 320
~ +[PHMobilePhoneRemoteViewControllerAccessibility _accessibilityPerformValidations:] : 176 -> 168
~ ___64-[PHMobilePhoneRemoteViewControllerAccessibility viewDidAppear:]_block_invoke : 160 -> 152
~ +[PHSOSViewControllerAccessibility _accessibilityPerformValidations:] : 432 -> 424
~ -[PHSOSViewControllerAccessibility accessibilityPerformEscape] : 204 -> 192
~ -[PHSOSViewControllerAccessibility _axSpeakInfo] : 212 -> 200
~ -[PHSOSViewControllerAccessibility _axMoveToCancelButton] : 92 -> 88
~ -[PHSOSDialCountdownViewModelAccessibility _axAnnouncementString] : 208 -> 192
~ -[PHSOSNotifyCountdownViewModelAccessibility _axAnnouncementString] : 144 -> 136
~ +[PHSlidingViewAccessibility _accessibilityPerformValidations:] : 380 -> 372
~ -[PHSlidingViewAccessibility _accessibilityLoadAccessibilityInformation] : 328 -> 320
~ ___72-[PHSlidingViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 112 -> 104
~ -[PHSlidingViewAccessibility repeatingUpdateAnimatedSliderForCountdownNumber:forModel:] : 104 -> 100
~ -[PHSlidingViewAccessibility setSlidingViewState:] : 428 -> 364
~ -[PHSlidingViewAccessibility interactiveStartWithCountdownModel:] : 240 -> 236
~ -[PHSlidingViewAccessibility setMedicalIDSlidingButtonCompletionBlock:] : 152 -> 144
~ +[PHVideoCallInterfaceOverlayViewAccessibility _accessibilityPerformValidations:] : 100 -> 92
~ -[PHVideoCallInterfaceOverlayViewAccessibility accessibilityViewIsModal] : 84 -> 80
~ -[MobilePhoneUILabelAccessibility accessibilityValue] : 268 -> 248
~ -[MobilePhoneUILabelAccessibility accessibilityLabel] : 228 -> 208
~ -[MobilePhoneUILabelAccessibility accessibilityTraits] : 164 -> 160
~ -[MobilePhoneUILabelAccessibility _accessibilityAlwaysOrderedFirst] : 124 -> 120
~ +[PHSingleCallParticipantLabelViewAccessibility _accessibilityPerformValidations:] : 164 -> 156
~ -[PHSingleCallParticipantLabelViewAccessibility _accessibilityLoadAccessibilityInformation] : 340 -> 332
~ ___91-[PHSingleCallParticipantLabelViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 500 -> 472
~ -[PHSingleCallParticipantLabelViewAccessibility _axSetUpCallDetailsViewButton] : 88 -> 84
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXInCallServiceGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__ICSApplicationDelegateAccessibility_super"
- "__InCallServiceApplicationAccessibility_super"
- "__MobilePhoneUILabelAccessibility_super"
- "__PHActionSliderAccessibility_super"
- "__PHAudioCallControlsViewAccessibility_super"
- "__PHAudioCallViewControllerAccessibility_super"
- "__PHAudioControlsButtonAccessibility_super"
- "__PHBannerButtonsViewAccessibility_super"
- "__PHBottomBarAccessibility_super"
- "__PHCallParticipantsViewAccessibility_super"
- "__PHCountdownViewAccessibility_super"
- "__PHEmergencyDialerViewControllerAccessibility_super"
- "__PHInCallRemoteAlertShellViewControllerAccessibility_super"
- "__PHMobilePhoneRemoteViewControllerAccessibility_super"
- "__PHSOSDialCountdownViewModelAccessibility_super"
- "__PHSOSNotifyCountdownViewModelAccessibility_super"
- "__PHSOSViewControllerAccessibility_super"
- "__PHSingleCallParticipantLabelViewAccessibility_super"
- "__PHSlidingViewAccessibility_super"
- "__PHVideoCallInterfaceOverlayViewAccessibility_super"
- "_accessibilityAllowsSiblingsWhenOvergrown"
- "_accessibilityAlwaysOrderedFirst"
- "_accessibilityAnnounceIncomingCall"
- "_accessibilityAnnounceIncomingCallUsingCurrentCallInfo:"
- "_accessibilityBottomBarStoppedAnimating:"
- "_accessibilityDescendantOfType:"
- "_accessibilityDidAnnounceIncomingCall"
- "_accessibilityHasSubscribedForBottomBarNotifications"
- "_accessibilityHitTestShouldFallbackToNearestChild"
- "_accessibilityHitTestShouldUseWindowBounds"
- "_accessibilityIsDisplayedInBanner"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityMiddleViewStateDepth"
- "_accessibilityOnlyComparesByXAxis"
- "_accessibilityPerformValidations:"
- "_accessibilityScannerShouldUseActivateInPointMode"
- "_accessibilitySetAllowsNotificationsDuringSuspension:"
- "_accessibilitySetDidAnnounceIncomingCall:"
- "_accessibilitySetHasSubscribedToBottomBarNotifications:"
- "_accessibilitySetIsDictationListeningOverride:"
- "_accessibilitySetMiddleViewStateDepth:"
- "_accessibilitySetWantsToShowKeypad:"
- "_accessibilitySortPriority"
- "_accessibilitySubscribeForBottomBarNotificationsIfNecessary"
- "_accessibilityViewIsVisible"
- "_accessibilityWantsToShowKeypad"
- "_axAnnouncementTimer"
- "_axGetFirstCall"
- "_axMoveToCancelButton"
- "_axSetAnnouncementTimer:"
- "_axSetPhoneToMiddleState:totalTimeTried:"
- "_axSetUpCallDetailsViewButton"
- "_axSpeakInfo"
- "_setAccessibilityIsMainWindow:"
- "_setAccessibilityLabelBlock:"
- "accessibilityActivate"
- "accessibilityIdentifier"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityPath"
- "accessibilityPerformEscape"
- "accessibilityPerformMagicTap"
- "accessibilityRespondsToUserInteraction"
- "accessibilityTraits"
- "accessibilityValue"
- "accessibilityViewIsModal"
- "addObserver:selector:name:object:"
- "alpha"
- "assignControlType:toButton:"
- "assistiveTouchScannerSpeechEnabled"
- "attributedTitleForState:"
- "axArrayByIgnoringNilElementsWithCount:"
- "axAttributedStringWithString:"
- "bundleForClass:"
- "bundleWithPath:"
- "canonicalHandleForISOCountryCode:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentAudioAndVideoCalls"
- "currentCalls"
- "dealloc"
- "defaultCenter"
- "dictionaryWithObjects:forKeys:count:"
- "firstObject"
- "handle"
- "incomingCall"
- "initWithString:attributes:"
- "installSafeCategory:canInteractWithTargetClass:"
- "invalidate"
- "isAccessibilityElement"
- "isEqualToString:"
- "isRTT"
- "isTTY"
- "isoCountryCode"
- "length"
- "localizedName"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "matchesInString:options:range:"
- "numberWithBool:"
- "numberWithUnsignedInteger:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "postNotificationName:object:"
- "providerManager"
- "q16@0:8"
- "range"
- "regularExpressionWithPattern:options:error:"
- "removeObserver:name:object:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntForKey:"
- "safeIntegerForKey:"
- "safeTimeIntervalForKey:"
- "safeUIViewForKey:"
- "safeUnsignedIntegerForKey:"
- "safeValueForKey:"
- "safeValueForKeyPath:"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "senderIdentityForHandle:"
- "service"
- "setAccessibilityIgnoresInvertColors:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setAccessibilityViewIsModal:"
- "setAttribute:forKey:"
- "setAttributes:withRange:"
- "setCurrentState:animated:"
- "setCurrentState:animated:animationCompletionBlock:"
- "setIsAccessibilityElement:"
- "setMiddleViewState:animated:completion:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "shouldGroupAccessibilityChildren"
- "string"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "telephonyProvider"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8S16B20"
- "v24@0:8q16"
- "v28@0:8S16d20"
- "v32@0:8Q16@24"
- "v32@0:8S16B20@?24"
- "v36@0:8q16B24@?28"
- "validateClass:"
- "validateClass:conformsToProtocol:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:hasProperty:withType:"
- "validateClass:isKindOfClass:"
- "validateProtocol:hasRequiredInstanceMethod:"
- "value"
- "window"

```
