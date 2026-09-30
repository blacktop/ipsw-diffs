## Translate

> `/System/Library/AccessibilityBundles/Translate.axbundle/Translate`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x15e0
-  __TEXT.__auth_stubs: 0x230
+3005.16.0.0.0
+  __TEXT.__text: 0x16bc
+  __TEXT.__auth_stubs: 0x210
   __TEXT.__objc_methlist: 0x2fc
   __TEXT.__cstring: 0x5b0
   __TEXT.__ustring: 0x16

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x190
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x120
+  __AUTH_CONST.__auth_got: 0x110
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0xab0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20171CE2-2BEC-3D85-895B-1FA9CADD74B6
+  UUID: 2AED17EF-EB5B-3377-8AF3-268A8C6DDEA0
   Functions: 59
-  Symbols:   317
+  Symbols:   315
   CStrings:  198
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
Functions:
~ +[AXTranslateGlue accessibilityInitializeBundle] : 148 -> 152
~ ___48+[AXTranslateGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___48+[AXTranslateGlue accessibilityInitializeBundle]_block_invoke_3 : 232 -> 240
~ _accessibilityLocalizedString : 176 -> 184
~ -[UIButtonAccessibility__Translate__UIKit accessibilityTraits] : 140 -> 144
~ +[RecordingHelperAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[RecordingHelperAccessibility _accessibilityDidStartListening] : 128 -> 132
~ -[RecordingHelperAccessibility _accessibilityDidStopListening] : 124 -> 128
~ -[LanguageAwareTextViewAccessibility accessibilityLanguage] : 220 -> 236
~ -[AccessibilityNodeAccessibility__Translate__SwiftUI accessibilityLabel] : 180 -> 192
~ -[AccessibilityNodeAccessibility__Translate__SwiftUI accessibilityAttributedLabel] : 124 -> 132
~ +[SenseRowAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[SenseRowAccessibility accessibilityLabel] : 344 -> 372
~ -[SenseRowAccessibility accessibilityTraits] : 208 -> 216
~ +[TranslationCardAccessibility _accessibilityPerformValidations:] : 408 -> 416
~ -[TranslationCardAccessibility accessibilityLabel] : 432 -> 472
~ -[TranslationCardAccessibility accessibilityCustomActions] : 556 -> 568
~ -[TranslationCardAccessibility _accessibilitySupplementaryFooterViews] : 196 -> 208
~ -[TranslationCardAccessibility senseTapped:] : 196 -> 208
~ -[TextViewWithPlaceHolderAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108

```
