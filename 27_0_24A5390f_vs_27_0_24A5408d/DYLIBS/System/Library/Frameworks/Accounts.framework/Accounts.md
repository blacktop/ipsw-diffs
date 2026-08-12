## Accounts

> `/System/Library/Frameworks/Accounts.framework/Accounts`

```diff

-1119.0.0.0.0
-  __TEXT.__text: 0x59198
-  __TEXT.__objc_methlist: 0x417c
+1122.0.0.0.0
+  __TEXT.__text: 0x590ec
+  __TEXT.__objc_methlist: 0x4174
   __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0x3660
   __TEXT.__cstring: 0x3e29
   __TEXT.__oslogstring: 0x4f74
-  __TEXT.__unwind_info: 0x1ac0
+  __TEXT.__unwind_info: 0x1ab8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22b8
+  __DATA_CONST.__objc_selrefs: 0x22b0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x38

   __AUTH_CONST.__objc_const: 0x5c38
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x558
-  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__auth_got: 0x660
   __AUTH.__objc_data: 0x960
   __DATA.__objc_ivar: 0x3d0
   __DATA.__data: 0x4d0

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1948
-  Symbols:   4210
+  Functions: 1947
+  Symbols:   4209
   CStrings:  1122
 
Symbols:
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ _dispatch_suspend
- -[ACTimedExpirer _unsafeCancelTimer]
- ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
- _objc_msgSend$_unsafeCancelTimer
Functions:
~ ___37-[ACTimedExpirer scheduleExpiration:]_block_invoke : 360 -> 324
~ ___29-[ACTimedExpirer cancelTimer]_block_invoke : 8 -> 32
~ ___37-[ACTimedExpirer scheduleExpiration:]_block_invoke_2 : 96 -> 16
- -[ACTimedExpirer _unsafeCancelTimer]
```
