## libSystem_debug.dylib

> `/System/DriverKit/usr/lib/libSystem_debug.dylib`

```diff

-1351.0.0.0.0
-  __TEXT.__text: 0x488
-  __TEXT.__auth_stubs: 0x270
+1354.0.0.0.2
+  __TEXT.__text: 0x4f4
+  __TEXT.__auth_stubs: 0x2b0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x11
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0x27
   __TEXT.__unwind_info: 0x70
   __DATA_CONST.__got: 0x48
-  __AUTH_CONST.__auth_got: 0x138
+  __AUTH_CONST.__auth_got: 0x158
   __AUTH_CONST.__const: 0xe0
   __AUTH.__data: 0x8
   __DATA.__common: 0x8

   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
   - /System/DriverKit/usr/lib/system/libsystem_trace.dylib
-  UUID: FDDE4673-CCA7-3F46-ACFB-78AC93CE8975
+  UUID: 1E2F4E40-FE25-3124-B87F-DBCA523BF6EB
   Functions: 18
-  Symbols:   84
-  CStrings:  1
+  Symbols:   88
+  CStrings:  2
 
Symbols:
+ ___libkernel_init_late
+ _dyld_program_sdk_at_least
+ _getenv
+ _strtol
Functions:
~ _libSystem_initializer : 452 -> 560
CStrings:
+ "SYSTEM_VERSION_COMPAT"

```
