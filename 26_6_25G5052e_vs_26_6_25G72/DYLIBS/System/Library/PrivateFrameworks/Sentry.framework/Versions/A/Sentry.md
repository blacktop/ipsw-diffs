## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Versions/A/Sentry`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

 3.0.0.0.0
-  __TEXT.__text: 0x1d758
+  __TEXT.__text: 0x1d85c
   __TEXT.__auth_stubs: 0x710
   __TEXT.__objc_methlist: 0x1768
   __TEXT.__const: 0x174
-  __TEXT.__cstring: 0x1e7e
-  __TEXT.__oslogstring: 0x2f8f
-  __TEXT.__gcc_except_tab: 0x4dc
+  __TEXT.__cstring: 0x1ea0
+  __TEXT.__oslogstring: 0x2fad
+  __TEXT.__gcc_except_tab: 0x4f4
   __TEXT.__unwind_info: 0x760
   __TEXT.__objc_classname: 0x386
   __TEXT.__objc_methname: 0x4951

   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0xb60
-  __AUTH_CONST.__cfstring: 0x1e60
+  __AUTH_CONST.__cfstring: 0x1e80
   __AUTH_CONST.__objc_const: 0x31f0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 771
+  Functions: 772
   Symbols:   1809
-  CStrings:  1448
+  CStrings:  1450
 
Symbols:
+ GCC_except_table238
- GCC_except_table237
Functions:
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:] : 2428 -> 2636
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.3 : 120 -> 52
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.4 : 52 -> 120
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.8 : 108 -> 52
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.9
CStrings:
+ "App launch threshold enforced"
+ "ApplicationFirstFramePresentation"
```
