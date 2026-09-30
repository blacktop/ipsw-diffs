## AppleSRP

> `/System/Library/PrivateFrameworks/AppleSRP.framework/AppleSRP`

```diff

 37.0.0.0.0
-  __TEXT.__text: 0x494c
+  __TEXT.__text: 0x4938
   __TEXT.__auth_stubs: 0x260
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0xba

   __DATA.__data: 0x49
   __DATA.__bss: 0x5
   - /usr/lib/libSystem.B.dylib
-  UUID: 09C19857-288C-3695-877E-820EB102F450
+  UUID: D27C4B5F-2A95-3573-BB06-5FDD249654F2
   Functions: 135
   Symbols:   255
   CStrings:  9
Functions:
~ _t_servergetkey : 732 -> 724
~ _srp6a_client_key : 912 -> 908
~ _srp6_server_key : 864 -> 860
~ _BigIntegerToString : 344 -> 340
~ _t_sessionkey : 468 -> 472
~ _t_fromb64 : 464 -> 460

```
