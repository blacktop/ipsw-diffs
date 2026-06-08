## SIMSetupUIService

> `/System/Library/AccessibilityBundles/SIMSetupUIService.axbundle/SIMSetupUIService`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x618
-  __TEXT.__auth_stubs: 0xf0
+3036.2.0.0.0
+  __TEXT.__text: 0x5e4
   __TEXT.__objc_methlist: 0xdc
   __TEXT.__cstring: 0x16b
   __TEXT.__unwind_info: 0x90
-  __TEXT.__objc_classname: 0xbf
-  __TEXT.__objc_methname: 0x2e7
-  __TEXT.__objc_methtype: 0x39
-  __TEXT.__objc_stubs: 0x220
-  __DATA_CONST.__got: 0x30
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x80
+  __DATA_CONST.__got: 0x30
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C0803FE9-3C8D-3C94-A731-8BAE87F9FDB4
+  UUID: 03FD956A-D361-30BF-A166-7EC512421B2A
   Functions: 18
-  Symbols:   111
-  CStrings:  70
+  Symbols:   113
+  CStrings:  34
 
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
~ +[AXSIMSetupUIServiceGlue accessibilityInitializeBundle] : 152 -> 148
~ ___56+[AXSIMSetupUIServiceGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___56+[AXSIMSetupUIServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 92
~ _accessibilityLocalizedString : 184 -> 176
~ +[TSSIMUnlockDetailViewAccessibility _accessibilityPerformValidations:] : 148 -> 140
~ -[TSSIMUnlockDetailViewAccessibility _accessibilityLoadAccessibilityInformation] : 116 -> 112
~ -[TSSIMUnlockDetailViewAccessibility initWithActionType:actionSubtype:] : 92 -> 96
~ +[TSSIMUnlockEntryViewAccessibility _accessibilityPerformValidations:] : 208 -> 200
~ -[TSSIMUnlockEntryViewAccessibility _accessibilityLoadAccessibilityInformation] : 140 -> 132
~ -[TSSIMUnlockEntryViewAccessibility initWithActionType:actionSubtype:] : 92 -> 96
~ -[TSSIMUnlockEntryViewAccessibility _configureDetailLabelText] : 152 -> 144
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@32@0:8q16q24"
- "AXSIMSetupUIServiceGlue"
- "SafeCategory"
- "__TSSIMUnlockDetailViewAccessibility_super"
- "__TSSIMUnlockEntryViewAccessibility_super"
- "_accessibilityAddTrait:"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityStringForLabelKeyValues:"
- "accessibilityContainerType"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "bundleForClass:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "q16@0:8"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "setAccessibilityLabel:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"

```
