## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Sentry`

```diff

 12.0.0.0.0
-  __TEXT.__text: 0xfdc8
+  __TEXT.__text: 0xfecc
   __TEXT.__objc_methlist: 0xd60
   __TEXT.__const: 0xec
-  __TEXT.__cstring: 0x14ec
-  __TEXT.__oslogstring: 0x1d9e
-  __TEXT.__gcc_except_tab: 0x3a0
-  __TEXT.__unwind_info: 0x598
+  __TEXT.__cstring: 0x150e
+  __TEXT.__oslogstring: 0x1dbc
+  __TEXT.__gcc_except_tab: 0x3b8
+  __TEXT.__unwind_info: 0x5a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x278
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x1220
+  __AUTH_CONST.__cfstring: 0x1240
   __AUTH_CONST.__objc_const: 0x19f0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 459
+  Functions: 460
   Symbols:   898
-  CStrings:  302
+  CStrings:  304
 
Functions:
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:] : 2656 -> 2864
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.5 : 96 -> 52
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.6 : 52 -> 96
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.10 : 100 -> 52
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.11
CStrings:
+ "App launch threshold enforced"
+ "ApplicationFirstFramePresentation"
```
