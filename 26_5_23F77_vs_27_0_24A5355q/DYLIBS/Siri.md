## Siri

> `/System/Library/AccessibilityBundles/Siri.axbundle/Siri`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x1338
-  __TEXT.__auth_stubs: 0x1a0
+3036.2.0.0.0
+  __TEXT.__text: 0x1274
   __TEXT.__objc_methlist: 0x350
-  __TEXT.__cstring: 0x573
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x14
+  __TEXT.__cstring: 0x573
   __TEXT.__unwind_info: 0x100
-  __TEXT.__objc_classname: 0x35c
-  __TEXT.__objc_methname: 0x4c3
-  __TEXT.__objc_methtype: 0x6c
-  __TEXT.__objc_stubs: 0x320
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x600
   __AUTH_CONST.__objc_const: 0xab0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x4b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DA764119-D264-3048-95E1-77F43B14C9F3
-  Functions: 63
-  Symbols:   303
-  CStrings:  181
+  UUID: 789AB040-12BC-34AE-8919-04412AF2748D
+  Functions: 62
+  Symbols:   301
+  CStrings:  109
 
Symbols:
+ GCC_except_table45
+ ___block_literal_global.364
+ ___block_literal_global.373
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXSiriGlue accessibilityInitializeBundle].cold.1
- GCC_except_table3
- ___block_literal_global.331
- ___block_literal_global.343
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
Functions:
~ +[AXSiriGlue accessibilityInitializeBundle] : 112 -> 124
~ ___43+[AXSiriGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___43+[AXSiriGlue accessibilityInitializeBundle]_block_invoke_2 : 104 -> 100
~ ___43+[AXSiriGlue accessibilityInitializeBundle]_block_invoke_3 : 88 -> 84
~ ___43+[AXSiriGlue accessibilityInitializeBundle]_block_invoke_4 : 240 -> 232
~ _accessibilityLocalizedString : 184 -> 176
~ -[SRCompactTextRequestViewControllerAccessibility viewWillAppear:] : 160 -> 152
~ +[SRGuideDetailSectionHeaderCollectionViewCellAccessibility _accessibilityPerformValidations:] : 128 -> 120
~ -[SRGuideDetailSectionHeaderCollectionViewCellAccessibility accessibilityLabel] : 196 -> 184
~ +[SRGuideViewCellAccessibility _accessibilityPerformValidations:] : 132 -> 124
~ -[SRGuideViewCellAccessibility accessibilityLabel] : 92 -> 84
~ -[SRGuideViewCellAccessibility accessibilityValue] : 92 -> 84
~ -[SRGuideViewHeaderAccessibility accessibilityLabel] : 92 -> 84
~ +[SRSiriViewControllerAccessibility _accessibilityPerformValidations:] : 256 -> 248
~ +[SRSpeechAlternativeTapToEditCellViewAccessibility _accessibilityPerformValidations:] : 136 -> 124
~ -[SRSpeechAlternativeTapToEditCellViewAccessibility _axAnnotateTapToEditLabel] : 88 -> 84
~ -[SRSpeechAlternativeTapToEditCellViewAccessibility init] : 84 -> 80
~ +[SystemAssistantPromptEntryViewAccessibility _accessibilityPerformValidations:] : 144 -> 136
~ -[SystemAssistantPromptEntryViewAccessibility _accessibilityLoadAccessibilityInformation] : 544 -> 520
~ ___89-[SystemAssistantPromptEntryViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 232 -> 216
~ +[SRSystemAssistantExperienceViewControllerAccessibility _accessibilityPerformValidations:] : 172 -> 160
~ -[SRSystemAssistantExperienceViewControllerAccessibility setupTextFieldForTextInput] : 264 -> 252
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXSiriGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__SRCompactTextRequestViewControllerAccessibility_super"
- "__SRGuideDetailSectionHeaderCollectionViewCellAccessibility_super"
- "__SRGuideViewCellAccessibility_super"
- "__SRGuideViewHeaderAccessibility_super"
- "__SRSiriViewControllerAccessibility_super"
- "__SRSpeechAlternativeTapToEditCellViewAccessibility_super"
- "__SRSystemAssistantExperienceViewControllerAccessibility_super"
- "__SRUserUtteranceViewAccessibility_super"
- "__SystemAssistantPromptEntryViewAccessibility_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityStringForLabelKeyValues:"
- "_axAnnotateTapToEditLabel"
- "accessibilityHint"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "accessibilityValue"
- "bundleForClass:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isFirstResponder"
- "length"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "registerSiriViewServicePID:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeSwiftValueForKey:"
- "safeValueForKey:"
- "server"
- "setAccessibilityLabel:"
- "setAccessibilityLabelBlock:"
- "setAccessibilityTraits:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v28@0:8@16B24"
- "v48@0:8q16q24q32d40"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:hasSwiftField:withSwiftType:"
- "viewWillAppear:"

```
