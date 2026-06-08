## WritingToolsUIService

> `/System/Library/AccessibilityBundles/WritingToolsUIService.axbundle/WritingToolsUIService`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x298
-  __TEXT.__auth_stubs: 0xd0
+3036.2.0.0.0
+  __TEXT.__text: 0x284
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__cstring: 0xc1
   __TEXT.__unwind_info: 0x78
-  __TEXT.__objc_classname: 0x9d
-  __TEXT.__objc_methname: 0x1d8
-  __TEXT.__objc_methtype: 0x3a
-  __TEXT.__objc_stubs: 0x160
-  __DATA_CONST.__got: 0x28
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x70
+  __DATA_CONST.__got: 0x28
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8AEA79F1-A52F-3FA0-BB90-F3DB936FC522
+  UUID: E1C4A8E4-81C0-373F-BCCE-24B9B263D13B
   Functions: 10
-  Symbols:   78
-  CStrings:  39
+  Symbols:   80
+  CStrings:  14
 
Symbols:
+ ___block_literal_global.351
+ ___block_literal_global.360
+ ___block_literal_global.6
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x21
+ _objc_retain
+ _objc_retain_x1
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ -[UITextViewAccessibility__WritingToolsUIService__UIKit _accessibilitySetSelectedTextRange:] : 156 -> 152
~ +[AXWritingToolsUIServiceGlue accessibilityInitializeBundle] : 152 -> 148
~ ___60+[AXWritingToolsUIServiceGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ _accessibilityLocalizedString : 184 -> 176
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXWritingToolsUIServiceGlue"
- "SafeCategory"
- "__UITextViewAccessibility__WritingToolsUIService__UIKit_super"
- "_accessibilityPerformValidations:"
- "_accessibilitySelectedTextRange"
- "_accessibilitySetSelectedTextRange:"
- "accessibilityInitializeBundle"
- "bundleForClass:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "select:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8{_NSRange=QQ}16"

```
