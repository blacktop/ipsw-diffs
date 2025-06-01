## libSystem.B_asan.dylib

> `/usr/lib/libSystem.B_asan.dylib`

```diff

-1336.80.1.0.0
-  __TEXT.__text: 0x714
-  __TEXT.__auth_stubs: 0x430
+1345.100.2.0.0
+  __TEXT.__text: 0x758
+  __TEXT.__auth_stubs: 0x450
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x172
   __TEXT.__oslogstring: 0x35
   __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0x218
+  __DATA_CONST.__auth_got: 0x228
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xe0
   __DATA.__data: 0x8

   - /usr/lib/system/libsystem_darwin.dylib
   - /usr/lib/system/libsystem_darwindirectory.dylib
   - /usr/lib/system/libsystem_dnssd.dylib
+  - /usr/lib/system/libsystem_eligibility.dylib
   - /usr/lib/system/libsystem_featureflags.dylib
   - /usr/lib/system/libsystem_info.dylib
   - /usr/lib/system/libsystem_kernel.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
+  - /usr/lib/system/libsystem_sanitizers.dylib
   - /usr/lib/system/libsystem_symptoms.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
   - @rpath/libclang_rt.asan_ios_dynamic.dylib
-  UUID: 30E50C18-BE3B-3843-9FB4-0BEFF899B767
+  UUID: 4D156017-9D2B-3064-87D7-42DA9C739B56
   Functions: 9
-  Symbols:   97
+  Symbols:   99
   CStrings:  11
 
Symbols:
+ ___pthread_late_init
+ __sanitizers_init

```
