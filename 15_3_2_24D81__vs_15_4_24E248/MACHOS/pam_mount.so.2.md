## pam_mount.so.2

> `/usr/lib/pam/pam_mount.so.2`

```diff

 213.0.0.0.0
-  __TEXT.__text: 0x1a68
+  __TEXT.__text: 0x1a74
   __TEXT.__auth_stubs: 0x310
   __TEXT.__cstring: 0x83b
   __TEXT.__const: 0x26
-  __TEXT.__unwind_info: 0xb0
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__auth_got: 0x188
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__cfstring: 0xe0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libpam.2.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 466722E5-24AA-30B4-A310-3200913BF71C
-  Functions: 21
+  UUID: 352A8969-2EAE-3EF1-B865-783A7581D6DC
+  Functions: 20
   Symbols:   87
   CStrings:  88
 
Functions:
~ _od_record_create_cstring : 248 -> 252
~ _od_record_check_pwpolicy : 244 -> 288
- sub_22c4
~ _pam_sm_close_session : 896 -> 884

```
