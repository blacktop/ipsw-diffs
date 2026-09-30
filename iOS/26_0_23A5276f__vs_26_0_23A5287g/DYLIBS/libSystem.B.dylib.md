## libSystem.B.dylib

> `/usr/lib/libSystem.B.dylib`

```diff

 1356.0.0.0.0
-  __TEXT.__text: 0x6ac
-  __TEXT.__auth_stubs: 0x440
+  __TEXT.__text: 0x634
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x80
+  __TEXT.__cstring: 0x6a
   __TEXT.__oslogstring: 0x35
   __TEXT.__unwind_info: 0x80
   __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0x220
+  __AUTH_CONST.__auth_got: 0x208
   __AUTH_CONST.__const: 0xe0
   __DATA.__common: 0x8
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/system/libsystem_trial.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: ACF121D4-5343-38DD-A41A-E286C4A2B38C
+  UUID: CD68ACFE-9318-31B2-9193-0FB588B4A429
   Functions: 22
-  Symbols:   133
-  CStrings:  8
+  Symbols:   130
+  CStrings:  7
 
Symbols:
- _dyld_program_sdk_at_least
- _getenv
- _strtol
Functions:
~ _libSystem_initializer : 964 -> 844
~ _libSystem_initializer.cold.16 -> _libSystem_initializer.cold.7 : 48 -> 16
~ _libSystem_atfork_prepare -> _libSystem_initializer.cold.16 : 88 -> 48
~ _libSystem_atfork_child -> _libSystem_atfork_prepare : 120 -> 88
~ _OUTLINED_FUNCTION_0 -> _libSystem_atfork_child : 16 -> 120
CStrings:
- "SYSTEM_VERSION_COMPAT"

```
