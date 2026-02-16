## CoreDynamicUIPlugin

> `/System/Library/AccessibilityBundles/CoreDynamicUIPlugin.axbundle/CoreDynamicUIPlugin`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x31c
+3005.16.0.0.0
+  __TEXT.__text: 0x33c
   __TEXT.__auth_stubs: 0xd0
   __TEXT.__objc_methlist: 0xb8
   __TEXT.__cstring: 0x126

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7F94E503-40D3-3E7F-AAF3-DB2160737204
+  UUID: 530AE9D7-469C-3F95-AF13-8DD48A8C4898
   Functions: 15
   Symbols:   96
   CStrings:  52
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
Functions:
~ -[TextComponentAccessibility accessibilityLabel] : 104 -> 112
~ +[AXCoreDynamicUIPluginGlue accessibilityInitializeBundle] : 148 -> 152
~ ___58+[AXCoreDynamicUIPluginGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___58+[AXCoreDynamicUIPluginGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityLocalizedString : 176 -> 184

```
