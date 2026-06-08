## com.apple.DocumentManager.Service-AppExtension

> `/System/Library/AccessibilityBundles/com.apple.DocumentManager.Service-AppExtension.axbundle/com.apple.DocumentManager.Service-AppExtension`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x1d4
-  __TEXT.__auth_stubs: 0x90
+3036.2.0.0.0
+  __TEXT.__text: 0x1ac
   __TEXT.__objc_methlist: 0x14
   __TEXT.__cstring: 0xbd
   __TEXT.__unwind_info: 0x70
-  __TEXT.__objc_classname: 0x1d
-  __TEXT.__objc_methname: 0x103
-  __TEXT.__objc_methtype: 0x8
-  __TEXT.__objc_stubs: 0xe0
-  __DATA_CONST.__got: 0x18
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x50
+  __DATA_CONST.__got: 0x18
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C91FD217-2404-368F-A0E0-71D0DC70DEEE
-  Functions: 7
-  Symbols:   50
-  CStrings:  22
+  UUID: 206DEC23-37D5-38AD-97EA-A8986CA0B4BA
+  Functions: 6
+  Symbols:   49
+  CStrings:  12
 
Symbols:
+ ___block_literal_global.352
+ ___block_literal_global.357
+ ___block_literal_global.366
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
- +[AXDocumentManagerServiceGlue accessibilityInitializeBundle].cold.1
- ___block_literal_global.331
- ___block_literal_global.336
- ___block_literal_global.345
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXDocumentManagerServiceGlue accessibilityInitializeBundle] : 44 -> 40
~ ___61+[AXDocumentManagerServiceGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___61+[AXDocumentManagerServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 88 -> 84
~ _accessibilityLocalizedString : 168 -> 160
CStrings:
- "AXDocumentManagerServiceGlue"
- "accessibilityInitializeBundle"
- "bundleForClass:"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "validateClass:"

```
