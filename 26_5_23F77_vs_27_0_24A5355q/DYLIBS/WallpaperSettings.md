## WallpaperSettings

> `/System/Library/AccessibilityBundles/WallpaperSettings.axbundle/WallpaperSettings`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x1a78
-  __TEXT.__auth_stubs: 0x210
+3036.2.0.0.0
+  __TEXT.__text: 0x18d8
   __TEXT.__objc_methlist: 0x150
   __TEXT.__const: 0x20
+  __TEXT.__gcc_except_tab: 0x18
   __TEXT.__cstring: 0xaa1
   __TEXT.__oslogstring: 0x3e
-  __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0xe0
-  __TEXT.__objc_classname: 0x13b
-  __TEXT.__objc_methname: 0x43e
-  __TEXT.__objc_methtype: 0x46
-  __TEXT.__objc_stubs: 0x420
-  __DATA_CONST.__got: 0x68
+  __TEXT.__unwind_info: 0xd8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x68
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x1940
   __AUTH_CONST.__objc_const: 0x3f0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
   __DATA.__common: 0x8
   __DATA.__bss: 0x18

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 05095902-1E83-3AF1-BA4F-0AADF46B3DCC
-  Functions: 33
+  UUID: C2CD6088-4BD0-3FC4-95CD-F1D371E5DEC2
+  Functions: 32
   Symbols:   200
-  CStrings:  470
+  CStrings:  413
 
Symbols:
+ GCC_except_table15
+ ___block_literal_global.880
+ ___block_literal_global.882
+ ___block_literal_global.891
+ ___block_literal_global.894
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- GCC_except_table6
- _AXWallpaperLabel.cold.1
- ___block_literal_global.859
- ___block_literal_global.861
- ___block_literal_global.870
- ___block_literal_global.873
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x24
Functions:
~ _AXWallpaperLabel : 948 -> 848
~ _accessibilityLocalizedString : 184 -> 176
~ +[AXWallpaperSettingsGlue accessibilityInitializeBundle] : 156 -> 152
~ ___56+[AXWallpaperSettingsGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___56+[AXWallpaperSettingsGlue accessibilityInitializeBundle]_block_invoke_4 : 120 -> 112
~ +[WSBundleCollectionOptionViewAccessibility _accessibilityPerformValidations:] : 132 -> 120
~ -[WSBundleCollectionOptionViewAccessibility accessibilityLabel] : 200 -> 180
~ -[WSBundleCollectionOptionViewAccessibility accessibilityUserInputLabels] : 268 -> 248
~ +[WallpaperPhotoCellAccessibility _accessibilityPerformValidations:] : 236 -> 228
~ -[WallpaperPhotoCellAccessibility accessibilityLabel] : 176 -> 160
~ -[WallpaperPhotoCellAccessibility _axWallpaperBundle] : 496 -> 468
~ ___53-[WallpaperPhotoCellAccessibility _axWallpaperBundle]_block_invoke : 92 -> 88
~ -[SwiftUIAccessibilityNode__WallpaperSettings__SwiftUI _axWallpaperDescription] : 608 -> 524
~ -[SwiftUIAccessibilityNode__WallpaperSettings__SwiftUI accessibilityTraits] : 136 -> 132
~ -[SwiftUIAccessibilityNode__WallpaperSettings__SwiftUI _accessibilityMediaAnalysisOptions] : 116 -> 112
~ -[SwiftUIAccessibilityNode__WallpaperSettings__SwiftUI _iosAccessibilityAttributeValue:] : 188 -> 176
~ -[SwiftUIAccessibilityNode__WallpaperSettings__SwiftUI accessibilityLabel] : 392 -> 332
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@24@0:8q16"
- "AXWallpaperSettingsGlue"
- "B16@0:8"
- "I16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__SwiftUIAccessibilityNode__WallpaperSettings__SwiftUI_super"
- "__WSBundleCollectionOptionViewAccessibility_super"
- "__WallpaperPhotoCellAccessibility_super"
- "_accessibilityAncestorIsKindOf:"
- "_accessibilityIndexPath"
- "_accessibilityMediaAnalysisOptions"
- "_accessibilityPerformValidations:"
- "_axWallpaperBundle"
- "_axWallpaperDescription"
- "_iosAccessibilityAttributeValue:"
- "accessibilityIdentifier"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "accessibilityUserInputLabels"
- "arrayWithObjects:count:"
- "bundleForClass:"
- "hasPrefix:"
- "init"
- "initWithObjectsAndKeys:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isEqualToString:"
- "item"
- "length"
- "localizedStringForKey:value:table:"
- "numberWithUnsignedInt:"
- "objectForKey:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntegerForKey:"
- "safeStringForKey:"
- "safeUnsignedIntegerForKey:"
- "safeValueForKey:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByReplacingOccurrencesOfString:withString:options:range:"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"

```
