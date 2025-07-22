## CacheDelete

> `/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete`

```diff

-806.0.0.0.1
-  __TEXT.__text: 0x3520c
-  __TEXT.__auth_stubs: 0xd10
+810.0.0.0.0
+  __TEXT.__text: 0x35300
+  __TEXT.__auth_stubs: 0xd20
   __TEXT.__objc_methlist: 0x171c
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__const: 0x1e8
-  __TEXT.__cstring: 0x2411
-  __TEXT.__oslogstring: 0x5cd3
-  __TEXT.__gcc_except_tab: 0xde4
+  __TEXT.__cstring: 0x2423
+  __TEXT.__oslogstring: 0x5d31
+  __TEXT.__gcc_except_tab: 0xde8
   __TEXT.__unwind_info: 0x9f8
   __TEXT.__objc_classname: 0x2a3
   __TEXT.__objc_methname: 0x3a5e

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x1c0
-  __AUTH_CONST.__auth_got: 0x698
+  __AUTH_CONST.__auth_got: 0x6a0
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x2020
+  __AUTH_CONST.__cfstring: 0x2040
   __AUTH_CONST.__objc_const: 0x2158
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x1b0

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F51985F-C8D4-3CE6-853C-FF28A29C39EA
+  UUID: AEB7C4C2-BEE9-3A88-B440-AE0A46320F90
   Functions: 772
-  Symbols:   2584
-  CStrings:  1982
+  Symbols:   2585
+  CStrings:  1986
 
Symbols:
+ _removefile_state_get
Functions:
~ _CacheDeleteCopyAvailableSpaceForVolume : 3344 -> 3372
~ _removefile_error_callback : 548 -> 764
CStrings:
+ "CACHE_DELETE_SUR_"
+ "removefile_error_callback for %s : %s (%d)\n"
+ "removefile_error_callback for %s : unknown error\n"

```
