## Translate

> `/System/Library/AccessibilityBundles/Translate.axbundle/Translate`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x16bc
-  __TEXT.__auth_stubs: 0x210
+3036.2.0.0.0
+  __TEXT.__text: 0x1590
   __TEXT.__objc_methlist: 0x2fc
+  __TEXT.__const: 0x10
   __TEXT.__cstring: 0x5b0
   __TEXT.__ustring: 0x16
   __TEXT.__oslogstring: 0xbe
-  __TEXT.__const: 0x10
   __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0x2cb
-  __TEXT.__objc_methname: 0x56d
-  __TEXT.__objc_methtype: 0x41
-  __TEXT.__objc_stubs: 0x420
-  __DATA_CONST.__got: 0x98
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x190
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0xab0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C2DB7DE1-697F-3709-A345-F1887E74BB45
-  Functions: 59
-  Symbols:   315
-  CStrings:  198
+  UUID: 8F1DF343-8CF5-3924-B5D8-966222CB045A
+  Functions: 58
+  Symbols:   313
+  CStrings:  121
 
Symbols:
+ ___block_literal_global.160
+ ___block_literal_global.351
+ ___block_literal_global.360
+ ___block_literal_global.428
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
- -[LanguageAwareTextViewAccessibility accessibilityLanguage].cold.1
- ___block_literal_global.330
- ___block_literal_global.339
- ___block_literal_global.407
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
Functions:
~ +[AXTranslateGlue accessibilityInitializeBundle] : 152 -> 148
~ ___48+[AXTranslateGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___48+[AXTranslateGlue accessibilityInitializeBundle]_block_invoke_3 : 240 -> 232
~ _accessibilityLocalizedString : 184 -> 176
~ -[UIButtonAccessibility__Translate__UIKit accessibilityTraits] : 144 -> 140
~ +[RecordingHelperAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[RecordingHelperAccessibility _accessibilityDidStartListening] : 132 -> 128
~ -[RecordingHelperAccessibility _accessibilityDidStopListening] : 128 -> 124
~ -[LanguageAwareTextViewAccessibility accessibilityLanguage] : 236 -> 268
~ -[AccessibilityNodeAccessibility__Translate__SwiftUI accessibilityLabel] : 192 -> 188
~ -[AccessibilityNodeAccessibility__Translate__SwiftUI accessibilityAttributedLabel] : 132 -> 124
~ +[SenseRowAccessibility _accessibilityPerformValidations:] : 168 -> 156
~ -[SenseRowAccessibility accessibilityLabel] : 372 -> 344
~ -[SenseRowAccessibility accessibilityTraits] : 216 -> 208
~ +[TranslationCardAccessibility _accessibilityPerformValidations:] : 416 -> 408
~ -[TranslationCardAccessibility accessibilityLabel] : 472 -> 432
~ -[TranslationCardAccessibility accessibilityCustomActions] : 568 -> 556
~ -[TranslationCardAccessibility _accessibilitySupplementaryFooterViews] : 208 -> 196
~ -[TranslationCardAccessibility senseTapped:] : 208 -> 196
~ -[TextViewWithPlaceHolderAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 104
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXTranslateGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__AccessibilityNodeAccessibility__Translate__SwiftUI_super"
- "__ConversationManagerAccessibility_super"
- "__HighlightTextViewAccessibility_super"
- "__LanguageAwareTextViewAccessibility_super"
- "__RecordingHelperAccessibility_super"
- "__SenseRowAccessibility_super"
- "__TextViewWithPlaceHolderAccessibility_super"
- "__TranslationCardAccessibility_super"
- "__UIButtonAccessibility__Translate__UIKit_super"
- "_accessibilityCanDrag"
- "_accessibilityFindSubviewDescendantsPassingTest:"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilitySetIsDictationListeningOverride:"
- "_accessibilitySupplementaryFooterViews"
- "_accessibilityViewIsVisible"
- "accessibilityAttributedLabel"
- "accessibilityCustomActions"
- "accessibilityIdentifier"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityLanguage"
- "accessibilityPlaceholderValue"
- "accessibilityTraits"
- "addObject:"
- "addObjectsFromArray:"
- "attributedString"
- "axAttributedStringWithString:"
- "bundleForClass:"
- "init"
- "initWithName:actionHandler:"
- "initWithStringOrAttributedString:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isEqualToString:"
- "localeIdentifier"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeStringForKey:"
- "safeSwiftValueForKey:"
- "safeUIViewForKey:"
- "safeValueForKey:"
- "setAccessibilityElementsHidden:"
- "setAttribute:forKey:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "validateClass:hasInstanceMethod:withFullSignature:"

```
