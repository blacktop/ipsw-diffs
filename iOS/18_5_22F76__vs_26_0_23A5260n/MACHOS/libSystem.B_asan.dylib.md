## libSystem.B_asan.dylib

> `/usr/lib/libSystem.B_asan.dylib`

```diff

-1351.0.0.0.0
-  __TEXT.__text: 0x6d0
-  __TEXT.__auth_stubs: 0x450
+1354.0.0.0.2
+  __TEXT.__text: 0x748
+  __TEXT.__auth_stubs: 0x480
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x172
+  __TEXT.__cstring: 0x188
   __TEXT.__oslogstring: 0x35
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x228
+  __DATA_CONST.__auth_got: 0x240
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xe0
+  __DATA.__data: 0x8
   __DATA.__common: 0x408
-  __DATA_DIRTY.__data: 0x8
   - /usr/lib/system/libcache.dylib
   - /usr/lib/system/libcommonCrypto.dylib
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_sanitizers.dylib
   - /usr/lib/system/libsystem_symptoms.dylib
   - /usr/lib/system/libsystem_trace.dylib
+  - /usr/lib/system/libsystem_trial.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
   - @rpath/libclang_rt.asan_ios_dynamic.dylib
-  UUID: 5215D35D-38AF-31C7-B323-C2670470EBCF
+  UUID: AC03C527-903F-3B2B-A534-CD3B8D02F879
   Functions: 23
-  Symbols:   114
-  CStrings:  11
+  Symbols:   117
+  CStrings:  12
 
Symbols:
+ _dyld_program_sdk_at_least
+ _getenv
+ _strtol
Functions:
~ _libSystem_initializer : 868 -> 988
CStrings:
+ "SYSTEM_VERSION_COMPAT"

```
