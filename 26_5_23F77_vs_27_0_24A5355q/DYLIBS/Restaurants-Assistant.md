## Restaurants-Assistant

> `/System/Library/AccessibilityBundles/Restaurants-Assistant.axbundle/Restaurants-Assistant`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x12b8
-  __TEXT.__auth_stubs: 0x1f0
+3036.2.0.0.0
+  __TEXT.__text: 0x11a0
   __TEXT.__objc_methlist: 0x16c
-  __TEXT.__cstring: 0x429
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x40
+  __TEXT.__cstring: 0x429
   __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0x20b
-  __TEXT.__objc_methname: 0x400
-  __TEXT.__objc_methtype: 0x39
-  __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x48
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x4e0
   __AUTH_CONST.__objc_const: 0x630
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x370
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 61B06EFC-3366-331B-996C-0602A4299663
-  Functions: 33
-  Symbols:   212
-  CStrings:  143
+  UUID: B16DB4B6-4A49-3206-8DB3-8E961D1C110A
+  Functions: 32
+  Symbols:   213
+  CStrings:  88
 
Symbols:
+ GCC_except_table16
+ GCC_except_table6
+ ___block_literal_global.15
+ ___block_literal_global.360
+ ___block_literal_global.406
+ ___block_literal_global.415
+ ___block_literal_global.77
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- +[AXRestaurantsAssistantGlue accessibilityInitializeBundle].cold.1
- GCC_except_table2
- GCC_except_table4
- ___block_literal_global.339
- ___block_literal_global.385
- ___block_literal_global.394
- _objc_retainAutoreleasedReturnValue
Functions:
~ _restaurantAccessibilityLocalizedString : 184 -> 176
~ +[AXRestaurantsAssistantGlue accessibilityInitializeBundle] : 44 -> 40
~ ___59+[AXRestaurantsAssistantGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___59+[AXRestaurantsAssistantGlue accessibilityInitializeBundle]_block_invoke_2 : 384 -> 380
~ ___59+[AXRestaurantsAssistantGlue accessibilityInitializeBundle]_block_invoke_3 : 88 -> 84
~ ___59+[AXRestaurantsAssistantGlue accessibilityInitializeBundle]_block_invoke_4 : 160 -> 152
~ -[SiriRestaurantsDetailDescriptionCellAccessibility _setPriceInfoWithRestaurant:] : 568 -> 540
~ -[SiriRestaurantsDetailViewControllerAccessibility _configurePhoneCell:forItem:] : 196 -> 184
~ -[SiriRestaurantsDetailViewControllerAccessibility _configureURLCell:forItem:] : 196 -> 184
~ -[SiriRestaurantsDetailViewControllerAccessibility _configureReviewsCell:forItem:] : 292 -> 268
~ +[SiriRestaurantsListItemCellAccessibility _accessibilityPerformValidations:] : 280 -> 272
~ -[SiriRestaurantsListItemCellAccessibility accessibilityLabel] : 880 -> 804
~ -[SiriRestaurantsOpenHoursCellAccessibility configureWithParsedOpenHoursInfo:] : 288 -> 280
~ ___78-[SiriRestaurantsOpenHoursCellAccessibility configureWithParsedOpenHoursInfo:]_block_invoke_2 : 392 -> 356
~ +[SiriRestaurantsLogoButtonAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[SiriRestaurantsLogoButtonAccessibility accessibilityLabel] : 172 -> 160
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXRestaurantsAssistantGlue"
- "B16@0:8"
- "SafeCategory"
- "__SiriRestaurantsDetailDescriptionCellAccessibility_super"
- "__SiriRestaurantsDetailViewControllerAccessibility_super"
- "__SiriRestaurantsListItemCellAccessibility_super"
- "__SiriRestaurantsLogoButtonAccessibility_super"
- "__SiriRestaurantsOpenHoursCellAccessibility_super"
- "_accessibilityFindSubviewDescendant:"
- "_accessibilityPerformValidations:"
- "_configurePhoneCell:forItem:"
- "_configureReviewsCell:forItem:"
- "_configureURLCell:forItem:"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "bundleForClass:"
- "count"
- "enumerateAttribute:inRange:options:usingBlock:"
- "enumerateObjectsUsingBlock:"
- "firstObject"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "lastObject"
- "length"
- "localizedStringForKey:value:table:"
- "objectAtIndex:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "string"
- "stringByReplacingCharactersInRange:withString:"
- "stringWithFormat:"
- "substringWithRange:"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16q24"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"

```
