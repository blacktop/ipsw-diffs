## pam_opendirectory.so.2

> `/usr/lib/pam/pam_opendirectory.so.2`

```diff

 213.0.0.0.0
-  __TEXT.__text: 0x1e4c
+  __TEXT.__text: 0x1e70
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_stubs: 0xa0
   __TEXT.__cstring: 0xa7c
   __TEXT.__const: 0x4e
   __TEXT.__objc_methname: 0x4b
-  __TEXT.__unwind_info: 0xb8
+  __TEXT.__unwind_info: 0xa8
   __DATA_CONST.__auth_got: 0x170
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__cfstring: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpam.2.dylib
-  UUID: E6CC5C9F-B07E-3A19-8045-DBC925F74995
-  Functions: 24
+  UUID: 3DFBF76E-D01D-3699-96BD-AA8C51338029
+  Functions: 21
   Symbols:   94
   CStrings:  109
 
Functions:
~ _od_record_create_cstring : 248 -> 252
~ _od_record_check_pwpolicy : 244 -> 288
- sub_1bb4
~ _pam_sm_authenticate : 1288 -> 1324
- sub_2d2c
~ _pam_sm_chauthtok : 848 -> 868

```
