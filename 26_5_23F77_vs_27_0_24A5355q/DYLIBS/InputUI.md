## InputUI

> `/System/Library/AccessibilityBundles/InputUI.axbundle/InputUI`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x80c
-  __TEXT.__auth_stubs: 0x180
+3036.2.0.0.0
+  __TEXT.__text: 0x7c4
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__cstring: 0x1d9
   __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x1d9
   __TEXT.__oslogstring: 0x19
   __TEXT.__unwind_info: 0x90
-  __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methname: 0x375
-  __TEXT.__objc_methtype: 0x23
-  __TEXT.__objc_stubs: 0x320
-  __DATA_CONST.__got: 0x70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x70
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x2e0
   __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7A9DCF87-569B-3CC1-AC74-4439852E4F73
+  UUID: F4A8D8D5-F188-3426-95B6-0AC8B10BF260
   Functions: 14
-  Symbols:   123
-  CStrings:  92
+  Symbols:   124
+  CStrings:  53
 
Symbols:
+ ___block_literal_global.3
+ ___block_literal_global.379
+ ___block_literal_global.388
+ ___block_literal_global.388.6
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___block_literal_global.358
- ___block_literal_global.367
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXInputUIGlue accessibilityInitializeBundle] : 152 -> 148
~ ___46+[AXInputUIGlue accessibilityInitializeBundle]_block_invoke : 220 -> 216
~ ___46+[AXInputUIGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ _accessibilityLocalizedString : 184 -> 176
~ +[InputUIWindowAccessibility _accessibilityPerformValidations:] : 212 -> 204
~ -[InputUIWindowAccessibility _accessibilityLoadAccessibilityInformation] : 544 -> 532
~ ___72-[InputUIWindowAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 132 -> 120
~ ___72-[InputUIWindowAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_3 : 244 -> 224
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXInputUIGlue"
- "SafeCategory"
- "__InputUIWindowAccessibility_super"
- "_accessibilityAllWindowsOnlyVisibleWindows:"
- "_accessibilityBoolValueForKey:"
- "_accessibilityContextId"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilitySetBoolValue:forKey:"
- "accessibilityInitializeBundle"
- "ax_filteredArrayUsingBlock:"
- "bundleForClass:"
- "dictionaryWithObjects:forKeys:count:"
- "firstObject"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "localizedStringForKey:value:table:"
- "numberWithUnsignedInt:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "processId"
- "registerRemoteElement:remotePort:"
- "rootViewController"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:isKindOfClass:"

```
