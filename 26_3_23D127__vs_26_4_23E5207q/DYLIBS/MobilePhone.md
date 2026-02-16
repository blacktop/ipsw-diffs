## MobilePhone

> `/System/Library/AccessibilityBundles/MobilePhone.axbundle/MobilePhone`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x4ae8
-  __TEXT.__auth_stubs: 0x380
+3005.16.0.0.0
+  __TEXT.__text: 0x4e1c
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_methlist: 0x89c
   __TEXT.__cstring: 0x118b
   __TEXT.__const: 0x18

   __DATA_CONST.__objc_selrefs: 0x518
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x1d0
+  __AUTH_CONST.__auth_got: 0x1c0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x18c0
   __AUTH_CONST.__objc_const: 0x1988

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B52FAC5A-EF9D-3BC1-8FE2-E1BAE7A4B347
+  UUID: 9035CB55-864D-3049-A219-8165FD225DEA
   Functions: 148
-  Symbols:   757
+  Symbols:   755
   CStrings:  648
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x9
Functions:
~ +[AXMobilePhoneGlue accessibilityInitializeBundle] : 148 -> 152
~ ___50+[AXMobilePhoneGlue accessibilityInitializeBundle]_block_invoke : 860 -> 864
~ ___50+[AXMobilePhoneGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___50+[AXMobilePhoneGlue accessibilityInitializeBundle]_block_invoke_3 : 492 -> 500
~ +[VMMessageTranscriptViewAccessibility _accessibilityPerformValidations:] : 164 -> 172
~ -[VMMessageTranscriptViewAccessibility _accessibilityActivateTextViewLink:] : 436 -> 472
~ ___75-[VMMessageTranscriptViewAccessibility _accessibilityActivateTextViewLink:]_block_invoke : 84 -> 88
~ +[MPVoicemailTableViewControllerAccessibility _accessibilityPerformValidations:] : 236 -> 248
~ -[MPVoicemailTableViewControllerAccessibility voicemailMessageViewModelForVoicemail:isExpanded:] : 932 -> 956
~ ___96-[MPVoicemailTableViewControllerAccessibility voicemailMessageViewModelForVoicemail:isExpanded:]_block_invoke : 76 -> 80
~ ___96-[MPVoicemailTableViewControllerAccessibility voicemailMessageViewModelForVoicemail:isExpanded:]_block_invoke_2 : 76 -> 80
~ +[MPRecentsTableViewControllerAccessibility _accessibilityPerformValidations:] : 420 -> 428
~ -[MPRecentsTableViewControllerAccessibility tableView:cellForRowAtIndexPath:] : 1856 -> 1988
~ ___77-[MPRecentsTableViewControllerAccessibility tableView:cellForRowAtIndexPath:]_block_invoke : 88 -> 92
~ -[UITextViewAccessibility__MobilePhone__UIKit _accessibilityActivateTextViewLink:] : 88 -> 92
~ +[MPLegacyRecentsTableViewCellAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[MPLegacyRecentsTableViewCellAccessibility accessibilityCustomActions] : 420 -> 436
~ ___71-[MPLegacyRecentsTableViewCellAccessibility accessibilityCustomActions]_block_invoke : 132 -> 140
~ _accessibilityLocalizedString : 212 -> 228
~ -[MobilePhoneUIButtonAccessibility _accessibilityKeyboardKeyAllowsTouchTyping] : 120 -> 124
~ +[PHRecentCallDetailsItemViewAccessibility _accessibilityPerformValidations:] : 212 -> 224
~ -[PHRecentCallDetailsItemViewAccessibility _axIsTTYCall] : 60 -> 64
~ -[PHRecentCallDetailsItemViewAccessibility accessibilityHint] : 68 -> 72
~ -[PHRecentCallDetailsItemViewAccessibility accessibilityLabel] : 376 -> 416
~ +[PHVoicemailGreetingViewControllerAccessibility _accessibilityPerformValidations:] : 196 -> 208
~ -[PHVoicemailGreetingViewControllerAccessibility viewDidLoad] : 228 -> 244
~ +[PHVoicemailInboxListViewControllerAccessibility _accessibilityPerformValidations:] : 152 -> 164
~ +[PHVoicemailMessageTableViewCellAccessibility _accessibilityPerformValidations:] : 476 -> 484
~ -[PHVoicemailMessageTableViewCellAccessibility accessibilityElements] : 148 -> 156
~ -[PHVoicemailMessageTableViewCellAccessibility isAccessibilityElement] : 112 -> 116
~ -[PHVoicemailMessageTableViewCellAccessibility accessibilityLabel] : 84 -> 92
~ -[PHVoicemailMessageTableViewCellAccessibility accessibilityTraits] : 168 -> 172
~ -[PHVoicemailMessageTableViewCellAccessibility accessibilityCustomActions] : 252 -> 264
~ ___61-[PHVoicemailMessageTableViewCellAccessibility _axInfoAction]_block_invoke : 84 -> 88
~ ___62-[PHVoicemailMessageTableViewCellAccessibility _axShareAction]_block_invoke : 84 -> 88
~ -[PHVoicemailMessageTableViewCellAccessibility setExpanded:animated:] : 288 -> 292
~ -[PHVoicemailMessageTableViewCellScrollViewAccessibility accessibilityElements] : 84 -> 92
~ +[PhoneApplicationAccesssibility _accessibilityPerformValidations:] : 652 -> 660
~ -[PhoneApplicationAccesssibility _accessibilitySoftwareMimicKeyboard] : 500 -> 540
~ -[PhoneApplicationAccesssibility accessibilityStartStopToggle] : 872 -> 928
~ ___83-[PhoneApplicationAccesssibility _accessibilityAllowsNotificationsDuringSuspension]_block_invoke : 104 -> 108
~ -[MobilePhoneUILabelAccessibility accessibilityValue] : 252 -> 268
~ -[MobilePhoneUILabelAccessibility accessibilityLabel] : 212 -> 228
~ -[MobilePhoneUILabelAccessibility accessibilityTraits] : 160 -> 164
~ -[MobilePhoneUILabelAccessibility _accessibilityAlwaysOrderedFirst] : 120 -> 124
~ +[VMMessageMetadataViewAccessibility _accessibilityPerformValidations:] : 332 -> 344
~ -[VMMessageMetadataViewAccessibility _accessibilityExpandedStatus] : 96 -> 100
~ -[VMMessageMetadataViewAccessibility accessibilityLabel] : 628 -> 692
~ -[VMMessageMetadataViewAccessibility _axIsVoiceMailUnread] : 116 -> 124
~ -[VMPlayerControlButtonAccessibility accessibilityLabel] : 96 -> 100
~ +[VMRoundButtonAccessibility _accessibilityPerformValidations:] : 220 -> 228
~ -[VMRoundButtonAccessibility accessibilityLabel] : 88 -> 92
~ -[VMRoundButtonAccessibility configureButtonUsingAudioRoute:] : 136 -> 140
~ -[VMPlayerTimelineSliderAccessibility _axUpdateSliderValue] : 380 -> 388
~ +[VMPlayerTimelineSliderAccessibility _accessibilityPerformValidations:] : 232 -> 240
~ -[VMPlayerTimelineSliderAccessibility accessibilityLabel] : 148 -> 160
~ -[VMPlayerTimelineSliderAccessibility accessibilityValue] : 388 -> 424
~ -[VMPlayerTimelineSliderAccessibility accessibilityTraits] : 176 -> 184
~ -[VMPlayerTimelineSliderAccessibility accessibilityIncrement] : 144 -> 152
~ -[VMPlayerTimelineSliderAccessibility accessibilityDecrement] : 144 -> 152

```
