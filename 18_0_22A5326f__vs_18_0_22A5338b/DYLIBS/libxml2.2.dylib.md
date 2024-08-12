## libxml2.2.dylib

> `/usr/lib/libxml2.2.dylib`

```diff

-38.0.0.0.0
-  __TEXT.__text: 0xc9464
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0x19864
-  __TEXT.__const: 0x38b0
-  __TEXT.__oslogstring: 0x77
-  __TEXT.__unwind_info: 0x1d30
+38.1.0.0.0
+  __TEXT.__text: 0xc955c
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__cstring: 0x19863
+  __TEXT.__const: 0x38c0
+  __TEXT.__oslogstring: 0xa2
+  __TEXT.__unwind_info: 0x1d38
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x7a78
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__const: 0xaa0
   __AUTH.__data: 0x130

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2726
-  Symbols:   2734
-  CStrings:  3979
+  Functions: 2727
+  Symbols:   2736
+  CStrings:  3980
 
Symbols:
+ __os_log_error_impl
CStrings:
+ "growing buffer past INT_MAX"
+ "xmlBufferLength() int overflow: %!{(MISSING)public}u"
- "growing buffer past UINT_MAX"

```
