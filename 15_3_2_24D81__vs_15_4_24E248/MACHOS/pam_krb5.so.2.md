## pam_krb5.so.2

> `/usr/lib/pam/pam_krb5.so.2`

```diff

 213.0.0.0.0
-  __TEXT.__text: 0x2f60
+  __TEXT.__text: 0x2f78
   __TEXT.__auth_stubs: 0x610
   __TEXT.__cstring: 0xe35
   __TEXT.__const: 0x1c
-  __TEXT.__unwind_info: 0xb0
+  __TEXT.__unwind_info: 0xa8
   __DATA_CONST.__auth_got: 0x308
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__cfstring: 0xe0

   - /System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libpam.2.dylib
-  UUID: 5DD9F628-DDA0-3A46-8E90-965C2527E49C
-  Functions: 22
+  UUID: CA2E5619-0E90-3E93-8213-FDDD7B32FEF5
+  Functions: 21
   Symbols:   134
   CStrings:  170
 
Functions:
~ _pam_sm_authenticate : 2496 -> 2492
~ _pam_sm_acct_mgmt : 508 -> 512
~ _od_record_create_cstring : 248 -> 252
~ _od_record_check_pwpolicy : 244 -> 288
- sub_61ec

```
