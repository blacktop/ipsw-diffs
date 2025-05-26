## libSystem.B.dylib

> `/usr/lib/libSystem.B.dylib`

```diff

-1336.80.1.0.0
-  __TEXT.__text: 0x678
-  __TEXT.__auth_stubs: 0x3f0
+1345.100.2.0.0
+  __TEXT.__text: 0x6bc
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x6a
   __TEXT.__oslogstring: 0x35
   __TEXT.__unwind_info: 0x64
   __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0x1f8
+  __AUTH_CONST.__auth_got: 0x208
   __DATA.__common: 0x8
   __DATA_DIRTY.__const: 0xe0
   __DATA_DIRTY.__data: 0x8

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
   Functions: 8
-  Symbols:   98
+  Symbols:   100
   CStrings:  7
 
Symbols:
+ ___pthread_late_init
+ __sanitizers_init

```
