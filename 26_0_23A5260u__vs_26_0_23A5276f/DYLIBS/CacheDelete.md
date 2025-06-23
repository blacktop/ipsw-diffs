## CacheDelete

> `/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete`

```diff

-795.0.0.502.1
-  __TEXT.__text: 0x350d4
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x170c
+804.0.0.0.1
+  __TEXT.__text: 0x351e4
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__objc_methlist: 0x171c
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__const: 0x1e8
   __TEXT.__cstring: 0x23ec
-  __TEXT.__oslogstring: 0x5ca1
-  __TEXT.__gcc_except_tab: 0xe00
-  __TEXT.__unwind_info: 0x9d0
+  __TEXT.__oslogstring: 0x5cd3
+  __TEXT.__gcc_except_tab: 0xde4
+  __TEXT.__unwind_info: 0x9c0
   __TEXT.__objc_classname: 0x2a3
-  __TEXT.__objc_methname: 0x3a4d
+  __TEXT.__objc_methname: 0x3a5e
   __TEXT.__objc_methtype: 0xa5a
-  __TEXT.__objc_stubs: 0x35a0
+  __TEXT.__objc_stubs: 0x35c0
   __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0xd70
+  __DATA_CONST.__const: 0xd48
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1080
+  __DATA_CONST.__objc_selrefs: 0x1088
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x1c0
-  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__auth_got: 0x698
   __AUTH_CONST.__const: 0x580
   __AUTH_CONST.__cfstring: 0x2000
   __AUTH_CONST.__objc_const: 0x2158

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 54DF6882-D195-387F-A003-04F89D139EAD
+  UUID: 92A5FAD9-2561-386B-9F43-786E2B5E2393
   Functions: 772
-  Symbols:   2586
-  CStrings:  1978
+  Symbols:   2584
+  CStrings:  1980
 
Symbols:
+ -[AppCache setLastUsedTime:]
+ ___24-[AppCache clearCaches:]_block_invoke.30
+ _objc_msgSend$lastKnownTmpSize
+ _objc_msgSend$setLastUsed:
- GCC_except_table12
- ___24-[AppCache clearCaches:]_block_invoke.31
- ___26-[AppCache tmp:purge:all:]_block_invoke
- ___block_descriptor_50_e8_32s40r_e51_B24?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}B}16ls32l8r40l8
- _objc_msgSend$three_days_ago
- _unlinkat
Functions:
~ -[AppCache invalidate] -> -[AppCache setLastUsedTime:] : 64 -> 124
~ -[AppCache validate] -> -[AppCache invalidate] : 208 -> 64
~ -[AppCache three_days_ago] -> -[AppCache validate] : 216 -> 208
~ -[AppCache tmp:purge:all:] -> -[AppCache three_days_ago] : 316 -> 216
~ ___26-[AppCache tmp:purge:all:]_block_invoke -> -[AppCache tmp:purge:all:] : 152 -> 616
CStrings:
+ "%d %@ Unable to move aside tmp, clearing in place"
+ "setLastUsedTime:"

```
