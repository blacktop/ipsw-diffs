## pam_ntlm.so.2

> `/usr/lib/pam/pam_ntlm.so.2`

```diff

 213.0.0.0.0
-  __TEXT.__text: 0x1754
+  __TEXT.__text: 0x1764
   __TEXT.__auth_stubs: 0x290
   __TEXT.__cstring: 0x670
   __TEXT.__const: 0x1c
-  __TEXT.__unwind_info: 0xa8
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__cfstring: 0x100

   - /System/Library/Frameworks/OpenDirectory.framework/Versions/A/OpenDirectory
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libpam.2.dylib
-  UUID: D9C08BFF-5973-30FA-8083-81742AFE6DF7
-  Functions: 22
+  UUID: 54EE9789-9548-3BD4-B8EC-764E04ED4032
+  Functions: 21
   Symbols:   79
   CStrings:  71
 
Functions:
~ _od_record_create_cstring : 248 -> 252
~ _od_record_check_pwpolicy : 244 -> 288
- sub_2838
~ _pam_sm_setcred : 1032 -> 1024

```
