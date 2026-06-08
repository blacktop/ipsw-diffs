## TipsApp

> `/System/Library/AccessibilityBundles/TipsApp.axbundle/TipsApp`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x10c4
-  __TEXT.__auth_stubs: 0x190
+3036.2.0.0.0
+  __TEXT.__text: 0xfe0
   __TEXT.__objc_methlist: 0x1cc
   __TEXT.__cstring: 0x39d
   __TEXT.__unwind_info: 0xc0
-  __TEXT.__objc_classname: 0x198
-  __TEXT.__objc_methname: 0x554
-  __TEXT.__objc_methtype: 0x6e
-  __TEXT.__objc_stubs: 0x4e0
-  __DATA_CONST.__got: 0x88
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1a0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x6c0
   __AUTH_CONST.__objc_const: 0x630
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 838BF828-C87E-3804-920E-7ED9443D3A0A
+  UUID: B3DE5A14-EC33-384A-8ADA-7EDCAFD11D1E
   Functions: 32
-  Symbols:   213
-  CStrings:  185
+  Symbols:   215
+  CStrings:  113
 
Symbols:
+ ___block_literal_global.351
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_retain_x19
Functions:
~ +[AXTipsGlue accessibilityInitializeBundle] : 152 -> 148
~ ___43+[AXTipsGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ ___43+[AXTipsGlue accessibilityInitializeBundle]_block_invoke_3 : 160 -> 152
~ _accessibilityLocalizedString : 184 -> 176
~ -[TPSPageControlAccessibility accessibilityValue] : 240 -> 228
~ +[TPSTipCollectionViewCellAccessibility _accessibilityPerformValidations:] : 316 -> 308
~ -[TPSTipCollectionViewCellAccessibility _accessibilityScannerGroupElements] : 360 -> 336
~ -[TPSTipCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 696 -> 644
~ +[TPSUICollectionViewAccessibility _accessibilityPerformValidations:] : 276 -> 264
~ -[TPSUICollectionViewAccessibility _axIsTipsCollectionView] : 88 -> 84
~ -[TPSUICollectionViewAccessibility _accessibilityFirstVisibleItem] : 196 -> 176
~ -[TPSUICollectionViewAccessibility _accessibilityScrollStatus] : 436 -> 400
~ +[TPSViewControllerAccessibility _accessibilityPerformValidations:] : 140 -> 132
~ +[UIBarButtonItemAccessibility__Tips__UIKit _accessibilityPerformValidations:] : 172 -> 160
~ -[UIBarButtonItemAccessibility__Tips__UIKit accessibilityLabel] : 252 -> 236
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "AXTipsGlue"
- "B16@0:8"
- "SafeCategory"
- "__TPSPageControlAccessibility_super"
- "__TPSTipCollectionViewCellAccessibility_super"
- "__TPSUICollectionViewAccessibility_super"
- "__TPSViewControllerAccessibility_super"
- "__UIBarButtonItemAccessibility__Tips__UIKit_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityProvidesScannerGroupElements"
- "_accessibilityScannerGroupElements"
- "_accessibilitySetRoleDescription:"
- "_axIsTipsCollectionView"
- "accessibilityCollectionViewBehavesLikeUIViewAccessibility"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "accessibilityValue"
- "arrayWithObjects:count:"
- "axAttributedStringWithString:"
- "bundleForClass:"
- "count"
- "currentPage"
- "dictionaryWithObjects:forKeys:count:"
- "firstObject"
- "init"
- "initWithFrame:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isEqualToString:"
- "localizedStringForKey:value:table:"
- "numberOfPages"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeArrayForKey:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeStringForKey:"
- "safeUIViewForKey:"
- "safeValueForKey:"
- "safeValueForKeyPath:"
- "setAccessibilityHint:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setAttribute:forKey:"
- "setIsAccessibilityElement:"
- "setIsAccessibilityScrollAncestor:"
- "setOverrideProcessName:"
- "setTip:withCellAppearance:"
- "setValidationTargetName:"
- "sharedInstance"
- "stringWithFormat:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"

```
