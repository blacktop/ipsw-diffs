## libsystem_symptoms.dylib

> `/usr/lib/system/libsystem_symptoms.dylib`

```diff

-2158.80.11.0.0
-  __TEXT.__text: 0x5c0c
+2169.100.28.0.0
+  __TEXT.__text: 0x5bdc
   __TEXT.__auth_stubs: 0x310
   __TEXT.__cstring: 0x18b3
   __TEXT.__const: 0x30

   __DATA_CONST.__const: 0x1c0
   __AUTH_CONST.__auth_got: 0x188
   __AUTH_CONST.__const: 0xa0
-  __DATA.__data: 0x8
+  __DATA.__data: 0x4
   __DATA.__bss: 0x28
+  __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x20
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 746CDFD1-6321-3CD1-BC1E-5D02410DFB8E
+  UUID: A19B026D-7E87-3C9C-964B-7263E9BD952E
   Functions: 69
   Symbols:   220
   CStrings:  195
Functions:
~ _handle_symptom : 2004 -> 2012
~ _read_current_status : 312 -> 304
~ ___symptom_transport_connect_block_invoke : 1716 -> 1708
~ _read_symptoms : 940 -> 920
~ _sym_ctrl_dequeue : 224 -> 220
~ ___obtain_symptom_framework_block_invoke : 644 -> 636
~ _fill_sender_id : 76 -> 68

```
