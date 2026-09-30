## QuickTime Plugin

> `/System/Library/AccessibilityBundles/QuickTime Plugin.axbundle/QuickTime Plugin`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x370
-  __TEXT.__auth_stubs: 0xd0
+3005.16.0.0.0
+  __TEXT.__text: 0x390
+  __TEXT.__auth_stubs: 0xc0
   __TEXT.__objc_methlist: 0x78
   __TEXT.__cstring: 0x124
   __TEXT.__unwind_info: 0x70

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x70
+  __AUTH_CONST.__auth_got: 0x68
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7CBBEC9C-3BEE-344B-8680-6CFE4A13DC97
+  UUID: 1BDFCDD2-DF12-3D03-8E71-B35AC03457CE
   Functions: 12
-  Symbols:   85
+  Symbols:   84
   CStrings:  59
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ _accessibilityLocalizedString : 156 -> 164
~ +[AXQuicktimePluginGlue accessibilityInitializeBundle] : 148 -> 152
~ ___54+[AXQuicktimePluginGlue accessibilityInitializeBundle]_block_invoke : 168 -> 172
~ ___54+[AXQuicktimePluginGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ -[FigPluginViewAccessibility setAllowPlayback:] : 132 -> 140
~ -[FigPluginViewAccessibility webPlugInStart] : 116 -> 120

```
