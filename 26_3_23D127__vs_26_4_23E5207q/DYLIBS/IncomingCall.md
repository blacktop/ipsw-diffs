## IncomingCall

> `/System/Library/AccessibilityBundles/IncomingCall.axbundle/IncomingCall`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xf4
+3005.16.0.0.0
+  __TEXT.__text: 0xfc
   __TEXT.__auth_stubs: 0x60
   __TEXT.__objc_methlist: 0x14
   __TEXT.__cstring: 0x60

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 14D3B9BF-3BC2-39CF-B7C9-BDD891677AC1
+  UUID: 3DE5E43A-D1BF-3A17-80B1-B5D966CE7018
   Functions: 4
   Symbols:   37
   CStrings:  14
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
Functions:
~ +[AXIncomingCallGlue accessibilityInitializeBundle] : 148 -> 152
~ ___51+[AXIncomingCallGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88

```
