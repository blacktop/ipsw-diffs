## MMCS

> `/System/Library/PrivateFrameworks/MMCS.framework/MMCS`

```diff

-2300.118.0.0.0
-  __TEXT.__text: 0x83808
-  __TEXT.__auth_stubs: 0x1cc0
+2300.120.0.0.0
+  __TEXT.__text: 0x83864
+  __TEXT.__auth_stubs: 0x1cd0
   __TEXT.__objc_methlist: 0xc10
   __TEXT.__const: 0x99c
-  __TEXT.__oslogstring: 0x476c
+  __TEXT.__oslogstring: 0x47a8
   __TEXT.__cstring: 0x1791e
   __TEXT.__gcc_except_tab: 0x714
   __TEXT.__unwind_info: 0x1528

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8b8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xe70
+  __AUTH_CONST.__auth_got: 0xe78
   __AUTH_CONST.__const: 0x2d10
   __AUTH_CONST.__cfstring: 0xcf40
   __AUTH_CONST.__objc_const: 0x1240

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D05854C3-B052-304D-8721-FC86F3E883A5
+  UUID: 84B1BE0F-6B60-3BBF-9793-18FAC870231C
   Functions: 2388
-  Symbols:   6218
-  CStrings:  5162
+  Symbols:   6219
+  CStrings:  5163
 
Symbols:
+ _exit
Functions:
~ _mmcs_job_queue_sync_halt : 88 -> 180
CStrings:
+ "Timed out in mmcs_job_queue_sync_halt. Exiting the process."

```
