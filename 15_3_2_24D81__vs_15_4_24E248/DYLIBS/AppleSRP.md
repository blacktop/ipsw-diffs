## AppleSRP

> `/System/Library/PrivateFrameworks/AppleSRP.framework/Versions/A/AppleSRP`

```diff

 37.0.0.0.0
-  __TEXT.__text: 0x49ac
+  __TEXT.__text: 0x494c
   __TEXT.__auth_stubs: 0x260
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0xba

   __DATA.__data: 0x49
   __DATA.__bss: 0x5
   - /usr/lib/libSystem.B.dylib
-  UUID: D659CDEE-5ED1-3971-A295-01C4083CBBC7
+  UUID: B68FD912-CF7A-329F-9CBD-F05A25C0619D
   Functions: 135
   Symbols:   191
   CStrings:  9
Functions:
~ _t_serveropenraw : 528 -> 500
~ _t_servergetkey : 748 -> 732
~ _t_serververify : 312 -> 308
~ _cstr_clear_free : 104 -> 96
~ _cstr_free : 96 -> 88
~ _cstr_alloc : 188 -> 192
~ _SRP_finalize_library : 48 -> 52
~ _srp6_client_finish : 76 -> 80
~ _srp6_server_finish : 108 -> 112
~ _t_sessionkey : 460 -> 468
~ _t_fromhex : 316 -> 248
~ _t_fromb64 : 488 -> 464
~ _t_tob64 : 272 -> 300
~ _srp2945_client_finish : 76 -> 80
~ _srp2945_server_finish : 108 -> 112

```
