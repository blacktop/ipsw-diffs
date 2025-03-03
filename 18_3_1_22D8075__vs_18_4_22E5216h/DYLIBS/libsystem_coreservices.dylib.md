## libsystem_coreservices.dylib

> `/usr/lib/system/libsystem_coreservices.dylib`

```diff

-171.1.0.0.0
-  __TEXT.__text: 0x1b0c
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x315
-  __TEXT.__oslogstring: 0x24a
-  __TEXT.__unwind_info: 0xb8
+178.0.0.0.0
+  __TEXT.__text: 0x1848
+  __TEXT.__auth_stubs: 0x280
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x30a
+  __TEXT.__oslogstring: 0x1fe
+  __TEXT.__unwind_info: 0xc0
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x928
-  __AUTH_CONST.__auth_got: 0x148
+  __AUTH_CONST.__auth_got: 0x140
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x80
   __DATA.__bss: 0x820

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  Functions: 33
-  Symbols:   78
-  CStrings:  60
+  Functions: 40
+  Symbols:   91
+  CStrings:  58
 
Symbols:
+ _statfs_ext
- _getattrlist
- _statfs
CStrings:
- "%s: getattrlist result=%d, error=%{errno}d, calling statfs for '%{public}s'"
- "ministatfs"

```
