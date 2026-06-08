## Movies-Assistant

> `/System/Library/AccessibilityBundles/Movies-Assistant.axbundle/Movies-Assistant`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x2024
-  __TEXT.__auth_stubs: 0x210
+3036.2.0.0.0
+  __TEXT.__text: 0x1e40
   __TEXT.__objc_methlist: 0x368
-  __TEXT.__cstring: 0x654
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x10
+  __TEXT.__cstring: 0x654
   __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0x335
-  __TEXT.__objc_methname: 0x571
-  __TEXT.__objc_methtype: 0x6b
-  __TEXT.__objc_stubs: 0x5c0
-  __DATA_CONST.__got: 0x80
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1c0
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x80
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x920
   __AUTH_CONST.__objc_const: 0xab0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x5f0
   __DATA.__bss: 0x12
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 689B63C9-1151-3E03-836E-6BC5AC342FD7
-  Functions: 68
-  Symbols:   348
-  CStrings:  240
+  UUID: 87C67564-B6BB-3B4F-B173-1173314A81B5
+  Functions: 67
+  Symbols:   351
+  CStrings:  156
 
Symbols:
+ GCC_except_table22
+ ___block_literal_global.360
+ ___block_literal_global.39
+ ___block_literal_global.434
+ ___block_literal_global.443
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
+ _objc_storeStrong
- +[AXMoviesAssistantGlue accessibilityInitializeBundle].cold.1
- GCC_except_table3
- ___block_literal_global.339
- ___block_literal_global.413
- ___block_literal_global.422
Functions:
~ _accessibilityLocalizedString : 184 -> 176
~ +[AXMoviesAssistantGlue accessibilityInitializeBundle] : 44 -> 40
~ ___54+[AXMoviesAssistantGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___54+[AXMoviesAssistantGlue accessibilityInitializeBundle]_block_invoke_2 : 508 -> 504
~ ___54+[AXMoviesAssistantGlue accessibilityInitializeBundle]_block_invoke_3 : 88 -> 84
~ ___54+[AXMoviesAssistantGlue accessibilityInitializeBundle]_block_invoke_4 : 240 -> 232
~ -[SiriMoviesAttributionCellAccessibility isBuyTicketsCell] : 132 -> 120
~ -[SiriMoviesAttributionCellAccessibility accessibilityLabel] : 124 -> 116
~ -[SiriUIBorderedLabelViewAccessibility accessibilityLabel] : 196 -> 180
~ +[SiriMoviesChevronButtonAccessibility _accessibilityPerformValidations:] : 292 -> 280
~ ___72-[SiriMoviesChevronButtonAccessibility _accessibilityProxyChevronButton]_block_invoke : 144 -> 140
~ -[SiriMoviesChevronButtonAccessibility isAccessibilityElement] : 160 -> 148
~ -[SiriMoviesChevronButtonAccessibility accessibilityLabel] : 420 -> 388
~ -[SiriMoviesChevronButtonAccessibility accessibilityValue] : 504 -> 472
~ ___58-[SiriMoviesChevronButtonAccessibility accessibilityValue]_block_invoke_2 : 352 -> 332
~ ___58-[SiriMoviesChevronButtonAccessibility accessibilityValue]_block_invoke_3 : 252 -> 236
~ -[SiriMoviesChevronCellAccessibility chevronButtonIsDimmed] : 104 -> 96
~ -[SiriMoviesChevronCellAccessibility accessibilityLabel] : 160 -> 144
~ -[SiriMoviesChevronCellAccessibility accessibilityValue] : 160 -> 144
~ -[SiriMoviesChevronCellAccessibility accessibilityHint] : 124 -> 116
~ +[SiriMoviesDetailViewAccessibility _accessibilityPerformValidations:] : 232 -> 220
~ -[SiriMoviesDetailViewAccessibility _accessibilityLoadAccessibilityInformation] : 772 -> 692
~ +[SiriMoviesIndividualShowtimeViewAccessibility _accessibilityPerformValidations:] : 212 -> 204
~ -[SiriMoviesIndividualShowtimeViewAccessibility accessibilityLabel] : 208 -> 188
~ -[SiriMoviesMovieListCellViewAccessibility accessibilityLabel] : 504 -> 456
~ +[SiriMoviesRottenTomatoesRatingViewAccessibility _accessibilityPerformValidations:] : 136 -> 124
~ -[SiriMoviesRottenTomatoesRatingViewAccessibility accessibilityLabel] : 328 -> 304
~ +[SiriMoviesMovieCreditsViewAccessibility _accessibilityPerformValidations:] : 176 -> 168
~ -[SiriMoviesMovieCreditsViewAccessibility initWithFrame:movieDetailSnippet:] : 180 -> 172
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "AXMoviesAssistantGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__SiriMoviesAttributionCellAccessibility_super"
- "__SiriMoviesChevronButtonAccessibility_super"
- "__SiriMoviesChevronCellAccessibility_super"
- "__SiriMoviesDetailViewAccessibility_super"
- "__SiriMoviesIndividualShowtimeViewAccessibility_super"
- "__SiriMoviesMovieCreditsViewAccessibility_super"
- "__SiriMoviesMovieListCellViewAccessibility_super"
- "__SiriMoviesRottenTomatoesRatingViewAccessibility_super"
- "__SiriUIBorderedLabelViewAccessibility_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityProxyChevronButton"
- "accessibilityHint"
- "accessibilityInitializeBundle"
- "accessibilityIsShowtimeHighlighted"
- "accessibilityIsShowtimeSelected"
- "accessibilityLabel"
- "accessibilityTraits"
- "accessibilityValue"
- "addObject:"
- "array"
- "axAttributedStringWithString:"
- "boolValue"
- "bundleForClass:"
- "chevronButtonIsDimmed"
- "compare:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "count"
- "enumerateObjectsUsingBlock:"
- "initWithFrame:movieDetailSnippet:"
- "installSafeCategory:canInteractWithTargetClass:"
- "integerValue"
- "isAccessibilityElement"
- "isBuyTicketsCell"
- "isEqualToString:"
- "length"
- "letterCharacterSet"
- "localizedStringForKey:value:table:"
- "objectAtIndex:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "scanInteger:"
- "scannerWithString:"
- "setAccessibilityHint:"
- "setAccessibilityLabel:"
- "setAccessibilityShowtimeHighlighted:"
- "setAccessibilityShowtimeSelected:"
- "setAccessibilityTraits:"
- "setAttribute:forKey:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "sortedArrayUsingComparator:"
- "stringByTrimmingCharactersInSet:"
- "stringWithFormat:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "whitespaceCharacterSet"

```
