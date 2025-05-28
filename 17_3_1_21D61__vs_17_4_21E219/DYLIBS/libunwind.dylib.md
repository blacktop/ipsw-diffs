## libunwind.dylib

> `/usr/lib/system/libunwind.dylib`

```diff

-1600.136.0.0.0
-  __TEXT.__text: 0x5fe4
-  __TEXT.__auth_stubs: 0x100
-  __TEXT.__cstring: 0x9e4
-  __TEXT.__unwind_info: 0x15c
+1700.242.0.0.0
+  __TEXT.__text: 0x6810
+  __TEXT.__auth_stubs: 0x110
+  __TEXT.__cstring: 0xa61
+  __TEXT.__unwind_info: 0x160
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x310
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x80
+  __AUTH_CONST.__auth_got: 0x88
   __DATA.__data: 0x1b0
-  __DATA.__bss: 0x851
+  __DATA.__bss: 0x859
   __DATA_DIRTY.__const: 0x88
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  Functions: 82
-  Symbols:   138
-  CStrings:  123
+  Functions: 83
+  Symbols:   141
+  CStrings:  127
 
Symbols:
+ __ZZ29__unw_is_pointer_auth_enabledE4mode
+ ___unw_is_pointer_auth_enabled
+ _sysctlbyname
CStrings:
+ "Inconsistent invalid authentication state"
+ "Invalid authentication state"
+ "__unw_is_pointer_auth_enabled"
+ "machdep.ptrauth_enabled"

```
