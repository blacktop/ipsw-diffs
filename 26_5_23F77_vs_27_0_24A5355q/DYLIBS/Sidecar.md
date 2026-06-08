## Sidecar

> `/System/Library/AccessibilityBundles/Sidecar.axbundle/Sidecar`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x1b4
-  __TEXT.__auth_stubs: 0x90
+3036.2.0.0.0
+  __TEXT.__text: 0x1a4
   __TEXT.__objc_methlist: 0x14
   __TEXT.__cstring: 0x65
   __TEXT.__unwind_info: 0x70
-  __TEXT.__objc_classname: 0xe
-  __TEXT.__objc_methname: 0xf9
-  __TEXT.__objc_methtype: 0x8
-  __TEXT.__objc_stubs: 0xe0
-  __DATA_CONST.__got: 0x18
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x50
+  __DATA_CONST.__got: 0x18
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__common: 0x8
   __DATA.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3E29843F-E25F-3E16-B430-8969F9C1AC59
+  UUID: 56EA8CBD-C4E8-30FB-A753-A907A18CABF3
   Functions: 5
-  Symbols:   45
-  CStrings:  19
+  Symbols:   46
+  CStrings:  9
 
Symbols:
+ ___block_literal_global.351
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXSidecarGlue accessibilityInitializeBundle] : 152 -> 148
~ ___46+[AXSidecarGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ _accessibilityLocalizedString : 184 -> 176
CStrings:
- "AXSidecarGlue"
- "accessibilityInitializeBundle"
- "bundleForClass:"
- "init"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"

```
