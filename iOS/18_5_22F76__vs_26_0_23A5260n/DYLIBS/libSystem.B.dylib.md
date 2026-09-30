## libSystem.B.dylib

> `/usr/lib/libSystem.B.dylib`

```diff

-1351.0.0.0.0
-  __TEXT.__text: 0x634
-  __TEXT.__auth_stubs: 0x410
+1354.0.0.0.2
+  __TEXT.__text: 0x6ac
+  __TEXT.__auth_stubs: 0x440
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x6a
+  __TEXT.__cstring: 0x80
   __TEXT.__oslogstring: 0x35
   __TEXT.__unwind_info: 0x80
   __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0x208
+  __AUTH_CONST.__auth_got: 0x220
   __AUTH_CONST.__const: 0xe0
   __DATA.__common: 0x8
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/system/libsystem_sanitizers.dylib
   - /usr/lib/system/libsystem_symptoms.dylib
   - /usr/lib/system/libsystem_trace.dylib
+  - /usr/lib/system/libsystem_trial.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: EA5C2FDF-8B24-312D-B515-6C137A02396E
+  UUID: DE619FB4-391E-3A5A-8EB5-7AB03D167720
   Functions: 22
-  Symbols:   130
-  CStrings:  7
+  Symbols:   133
+  CStrings:  8
 
Symbols:
+ _dyld_program_sdk_at_least
+ _getenv
+ _strtol
Functions:
~ _libSystem_initializer : 844 -> 964
CStrings:
+ "SYSTEM_VERSION_COMPAT"

```
