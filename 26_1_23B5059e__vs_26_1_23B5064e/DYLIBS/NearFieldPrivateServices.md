## NearFieldPrivateServices

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/NearFieldPrivateServices`

```diff

-361.5.0.0.0
-  __TEXT.__text: 0x77dc
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x45c
+361.6.0.0.0
+  __TEXT.__text: 0x7bd0
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0x47c
   __TEXT.__const: 0x98
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__cstring: 0x10e9
-  __TEXT.__oslogstring: 0x74d
-  __TEXT.__unwind_info: 0x170
+  __TEXT.__cstring: 0x1156
+  __TEXT.__oslogstring: 0x786
+  __TEXT.__unwind_info: 0x180
   __TEXT.__objc_classname: 0x10f
-  __TEXT.__objc_methname: 0x9a3
-  __TEXT.__objc_methtype: 0x263
-  __TEXT.__objc_stubs: 0x7a0
+  __TEXT.__objc_methname: 0x9d8
+  __TEXT.__objc_methtype: 0x29f
+  __TEXT.__objc_stubs: 0x7c0
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x4c0
+  __DATA_CONST.__const: 0x510
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x360
+  __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x228
-  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__auth_got: 0x230
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x580
-  __AUTH_CONST.__objc_const: 0x6d8
+  __AUTH_CONST.__objc_const: 0x6f8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x180
   __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF83069E-B988-366D-9E52-02746608050C
-  Functions: 85
-  Symbols:   105
-  CStrings:  418
+  UUID: EEEA0B47-C26C-3DD1-AB7B-EB6CCAB6ABFC
+  Functions: 93
+  Symbols:   106
+  CStrings:  426
 
Symbols:
+ _objc_retain_x8
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _objc_sync_enter
- _objc_sync_exit
CStrings:
+ "%s:%i NFPrivateService xpcConnection invalidated"
+ "%{public}s:%i NFPrivateService xpcConnection invalidated"
+ "-[NFPrivateService connectToService:outError:]_block_invoke"
+ "@32@0:8@16^@24"
+ "_iVarLock"
+ "_sync_disconnect"
+ "connectToService:outError:"
+ "executeWithLock:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "connectToService:"

```
