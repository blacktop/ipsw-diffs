## Siri

> `/System/Library/AccessibilityBundles/Siri.axbundle/Siri`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x1280
+3005.16.0.0.0
+  __TEXT.__text: 0x1338
   __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_methlist: 0x350
   __TEXT.__cstring: 0x573

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4B0FCE7-7A9C-3D6A-B505-F5B26DDE7BB8
+  UUID: 8F132C18-229D-3537-9396-CAD334F6A6B5
   Functions: 63
   Symbols:   303
   CStrings:  181
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXSiriGlue accessibilityInitializeBundle] : 108 -> 112
~ ___43+[AXSiriGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___43+[AXSiriGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 104
~ ___43+[AXSiriGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ ___43+[AXSiriGlue accessibilityInitializeBundle]_block_invoke_4 : 232 -> 240
~ _accessibilityLocalizedString : 176 -> 184
~ -[SRCompactTextRequestViewControllerAccessibility viewWillAppear:] : 152 -> 160
~ +[SRGuideDetailSectionHeaderCollectionViewCellAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[SRGuideDetailSectionHeaderCollectionViewCellAccessibility accessibilityLabel] : 184 -> 196
~ +[SRGuideViewCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[SRGuideViewCellAccessibility accessibilityLabel] : 84 -> 92
~ -[SRGuideViewCellAccessibility accessibilityValue] : 84 -> 92
~ -[SRGuideViewHeaderAccessibility accessibilityLabel] : 84 -> 92
~ +[SRSiriViewControllerAccessibility _accessibilityPerformValidations:] : 248 -> 256
~ +[SRSpeechAlternativeTapToEditCellViewAccessibility _accessibilityPerformValidations:] : 124 -> 136
~ -[SRSpeechAlternativeTapToEditCellViewAccessibility _axAnnotateTapToEditLabel] : 84 -> 88
~ +[SystemAssistantPromptEntryViewAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[SystemAssistantPromptEntryViewAccessibility _accessibilityLoadAccessibilityInformation] : 520 -> 544
~ ___89-[SystemAssistantPromptEntryViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 220 -> 232
~ +[SRSystemAssistantExperienceViewControllerAccessibility _accessibilityPerformValidations:] : 160 -> 172
~ -[SRSystemAssistantExperienceViewControllerAccessibility setupTextFieldForTextInput] : 252 -> 264

```
