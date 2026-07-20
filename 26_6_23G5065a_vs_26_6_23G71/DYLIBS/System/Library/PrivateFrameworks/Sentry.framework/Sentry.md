## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Sentry`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

 3.0.0.0.0
-  __TEXT.__text: 0x10b8c
+  __TEXT.__text: 0x10c8c
   __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_methlist: 0xd50
   __TEXT.__const: 0xe4
-  __TEXT.__cstring: 0x140f
-  __TEXT.__oslogstring: 0x1beb
-  __TEXT.__gcc_except_tab: 0x42c
+  __TEXT.__cstring: 0x1431
+  __TEXT.__oslogstring: 0x1c09
+  __TEXT.__gcc_except_tab: 0x444
   __TEXT.__unwind_info: 0x490
   __TEXT.__objc_classname: 0x1b1
   __TEXT.__objc_methname: 0x2e56

   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x11a0
+  __AUTH_CONST.__cfstring: 0x11c0
   __AUTH_CONST.__objc_const: 0x19b0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xf0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 447
+  Functions: 448
   Symbols:   1123
-  CStrings:  835
+  CStrings:  837
 
Symbols:
+ GCC_except_table220
- GCC_except_table219
Functions:
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:] : 2256 -> 2460
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.3 : 120 -> 52
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.4 : 52 -> 120
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.8 : 100 -> 52
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.9
CStrings:
+ "App launch threshold enforced"
+ "ApplicationFirstFramePresentation"
```
