## libsystem_darwin.dylib

> `/usr/lib/system/libsystem_darwin.dylib`

```diff

-  __TEXT.__text: 0x65c4
-  __TEXT.__const: 0x90
+  __TEXT.__text: 0x65d8
+  __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x1ebc
   __TEXT.__oslogstring: 0x8d4
   __TEXT.__unwind_info: 0x1d8
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _os_mach_msg_get_trailer -> _os_mach_msg_get_audit_trailer : 24 -> 48
~ _os_mach_msg_get_audit_trailer -> _os_mach_msg_get_trailer : 48 -> 24
~ _os_variant_check : 140 -> 160

```
