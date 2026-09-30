## mount

> `/sbin/mount`

```diff

-751.0.0.0.0
-  __TEXT.__text: 0x4bc0
-  __TEXT.__auth_stubs: 0x810
+751.40.1.0.1
+  __TEXT.__text: 0x4c1c
+  __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_stubs: 0x6a0
   __TEXT.__const: 0x3c
-  __TEXT.__gcc_except_tab: 0x248
-  __TEXT.__cstring: 0x1223
+  __TEXT.__gcc_except_tab: 0x254
+  __TEXT.__cstring: 0x122c
   __TEXT.__oslogstring: 0xc
   __TEXT.__objc_methname: 0x4ff
   __TEXT.__unwind_info: 0x108
-  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x450

   - /System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84A0AFA2-7981-3418-97F4-498C5CB0621E
+  UUID: A9924904-1F25-38CD-9387-C37B95344A41
   Functions: 51
-  Symbols:   164
-  CStrings:  276
+  Symbols:   168
+  CStrings:  277
 
Symbols:
+ _getenv
+ _getuid
+ _setreuid
+ _strtoul
Functions:
~ sub_100000bc0 : 5132 -> 5224
CStrings:
+ "SUDO_UID"

```
