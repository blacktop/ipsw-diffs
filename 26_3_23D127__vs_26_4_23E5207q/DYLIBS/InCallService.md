## InCallService

> `/System/Library/AccessibilityBundles/InCallService.axbundle/InCallService`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x4c58
-  __TEXT.__auth_stubs: 0x430
+3005.16.0.0.0
+  __TEXT.__text: 0x4f04
+  __TEXT.__auth_stubs: 0x3d0
   __TEXT.__objc_methlist: 0x8b8
   __TEXT.__cstring: 0xf0a
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0xb8
   __TEXT.__oslogstring: 0x5f
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__unwind_info: 0x238
   __TEXT.__objc_classname: 0x6dd
   __TEXT.__objc_methname: 0x1120
   __TEXT.__objc_methtype: 0xc1

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x1f8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x14c0
   __AUTH_CONST.__objc_const: 0x1830

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 88187327-1038-3ECF-BAF2-7FA5CC7C9940
+  UUID: 445CC557-8C72-371D-958B-F0CE46A3E344
   Functions: 169
-  Symbols:   803
+  Symbols:   797
   CStrings:  570
 
Symbols:
+ _objc_retain_x20
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x27
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
- _objc_storeStrong
Functions:
~ +[AXInCallServiceGlue accessibilityInitializeBundle] : 100 -> 104
~ ___52+[AXInCallServiceGlue accessibilityInitializeBundle]_block_invoke : 268 -> 272
~ ___52+[AXInCallServiceGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___52+[AXInCallServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 472 -> 480
~ _accessibilityMobilePhoneLocalizedString : 212 -> 228
~ _accessibilityLocalizedString : 176 -> 184
~ _axStringForCallParticipantsView : 652 -> 696
~ +[PHCallParticipantsViewAccessibility _accessibilityPerformValidations:] : 308 -> 316
~ -[PHCallParticipantsViewAccessibility updateParticipantsAnimated:] : 280 -> 292
~ -[PHCallParticipantsViewAccessibility isAccessibilityElement] : 104 -> 108
~ -[PHCallParticipantsViewAccessibility _accessibilityIsDisplayedInBanner] : 76 -> 80
~ -[InCallServiceApplicationAccessibility accessibilityLabel] : 112 -> 120
~ -[InCallServiceApplicationAccessibility _axGetFirstCall] : 108 -> 120
~ +[PHActionSliderAccessibility _accessibilityPerformValidations:] : 264 -> 272
~ -[PHActionSliderAccessibility accessibilityPath] : 196 -> 212
~ -[PHActionSliderAccessibility accessibilityLabel] : 156 -> 168
~ -[PHAudioCallControlsViewAccessibility assignControlType:toButton:] : 144 -> 148
~ +[PHAudioCallViewControllerAccessibility _accessibilityPerformValidations:] : 532 -> 540
~ -[PHAudioCallViewControllerAccessibility _accessibilitySubscribeForBottomBarNotificationsIfNecessary] : 132 -> 136
~ -[PHAudioCallViewControllerAccessibility dealloc] : 116 -> 120
~ -[PHAudioCallViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 200 -> 204
~ -[PHAudioCallViewControllerAccessibility _accessibilityAnnounceIncomingCallUsingCurrentCallInfo:] : 980 -> 1056
~ -[PHAudioCallViewControllerAccessibility _axSetPhoneToMiddleState:totalTimeTried:] : 292 -> 304
~ ___82-[PHAudioCallViewControllerAccessibility _axSetPhoneToMiddleState:totalTimeTried:]_block_invoke : 384 -> 388
~ -[PHAudioCallViewControllerAccessibility setMiddleViewState:animated:completion:] : 356 -> 352
~ +[PHBottomBarAccessibility _accessibilityPerformValidations:] : 344 -> 352
~ -[PHBottomBarAccessibility _accessibilityLoadAccessibilityInformation] : 340 -> 364
~ -[PHBottomBarAccessibility setAnimating:] : 156 -> 160
~ -[PHBottomBarButtonAccessibility accessibilityLabel] : 328 -> 340
~ -[PHBottomBarButtonAccessibility accessibilityUserInputLabels] : 220 -> 232
~ +[PHCountdownViewAccessibility _accessibilityPerformValidations:] : 364 -> 376
~ -[PHCountdownViewAccessibility startCountdown] : 748 -> 772
~ ___46-[PHCountdownViewAccessibility startCountdown]_block_invoke : 264 -> 268
~ ___46-[PHCountdownViewAccessibility startCountdown]_block_invoke_2 : 80 -> 84
~ +[PHEmergencyDialerViewControllerAccessibility _accessibilityPerformValidations:] : 200 -> 208
~ -[PHEmergencyDialerViewControllerAccessibility viewDidDisappear:] : 232 -> 248
~ -[PHEmergencyDialerViewControllerAccessibility viewDidAppear:] : 320 -> 348
~ +[PHMobilePhoneRemoteViewControllerAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ ___64-[PHMobilePhoneRemoteViewControllerAccessibility viewDidAppear:]_block_invoke : 152 -> 160
~ +[PHSOSViewControllerAccessibility _accessibilityPerformValidations:] : 424 -> 432
~ -[PHSOSViewControllerAccessibility accessibilityPerformEscape] : 192 -> 204
~ -[PHSOSViewControllerAccessibility _axSpeakInfo] : 200 -> 212
~ -[PHSOSViewControllerAccessibility _axMoveToCancelButton] : 88 -> 92
~ -[PHSOSDialCountdownViewModelAccessibility _axAnnouncementString] : 192 -> 208
~ -[PHSOSNotifyCountdownViewModelAccessibility _axAnnouncementString] : 136 -> 144
~ +[PHSlidingViewAccessibility _accessibilityPerformValidations:] : 380 -> 388
~ -[PHSlidingViewAccessibility _accessibilityLoadAccessibilityInformation] : 320 -> 328
~ ___72-[PHSlidingViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 104 -> 112
~ -[PHSlidingViewAccessibility repeatingUpdateAnimatedSliderForCountdownNumber:forModel:] : 100 -> 104
~ -[PHSlidingViewAccessibility setSlidingViewState:] : 408 -> 428
~ -[PHSlidingViewAccessibility interactiveStartWithCountdownModel:] : 236 -> 240
~ -[PHSlidingViewAccessibility showSlidingViewModel:animatedSliderCompletion:medicalIDSliderCompletion:shouldMaxVolumeCompletion:] : 144 -> 152
~ +[PHVideoCallInterfaceOverlayViewAccessibility _accessibilityPerformValidations:] : 92 -> 100
~ -[PHVideoCallInterfaceOverlayViewAccessibility accessibilityViewIsModal] : 80 -> 84
~ -[MobilePhoneUILabelAccessibility accessibilityValue] : 252 -> 268
~ -[MobilePhoneUILabelAccessibility accessibilityLabel] : 212 -> 228
~ -[MobilePhoneUILabelAccessibility accessibilityTraits] : 160 -> 164
~ -[MobilePhoneUILabelAccessibility _accessibilityAlwaysOrderedFirst] : 120 -> 124
~ +[PHSingleCallParticipantLabelViewAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[PHSingleCallParticipantLabelViewAccessibility _accessibilityLoadAccessibilityInformation] : 420 -> 436
~ ___91-[PHSingleCallParticipantLabelViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 472 -> 500
~ -[PHSingleCallParticipantLabelViewAccessibility _axSetUpCallDetailsViewButton] : 84 -> 88

```
