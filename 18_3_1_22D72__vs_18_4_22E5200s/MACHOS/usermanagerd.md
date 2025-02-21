## usermanagerd

> `/usr/libexec/usermanagerd`

```diff

-417.0.0.0.0
-  __TEXT.__text: 0xacd08
-  __TEXT.__auth_stubs: 0x1820
+417.100.1.0.0
+  __TEXT.__text: 0xa45dc
+  __TEXT.__auth_stubs: 0x1830
   __TEXT.__objc_stubs: 0x2220
-  __TEXT.__objc_methlist: 0x1064
-  __TEXT.__const: 0x10f4
-  __TEXT.__gcc_except_tab: 0xe08
-  __TEXT.__cstring: 0x66fe
+  __TEXT.__objc_methlist: 0x18dc
+  __TEXT.__const: 0x1124
+  __TEXT.__gcc_except_tab: 0xdf4
+  __TEXT.__cstring: 0x6790
   __TEXT.__objc_classname: 0x39a
   __TEXT.__objc_methname: 0x346d
   __TEXT.__objc_methtype: 0x12c2
   __TEXT.__oslogstring: 0x107da
-  __TEXT.__unwind_info: 0x1298
-  __DATA_CONST.__auth_got: 0xc20
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__auth_ptr: 0x28
+  __TEXT.__unwind_info: 0x1360
+  __DATA_CONST.__auth_got: 0xc28
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__auth_ptr: 0x50
   __DATA_CONST.__const: 0x2660
   __DATA_CONST.__cfstring: 0x1c00
   __DATA_CONST.__objc_classlist: 0x100

   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x5600
-  __DATA.__objc_selrefs: 0xbe8
+  __DATA.__objc_const: 0x45e8
+  __DATA.__objc_selrefs: 0xc70
   __DATA.__objc_ivar: 0x1d8
   __DATA.__objc_data: 0xa00
-  __DATA.__data: 0x11d8
+  __DATA.__data: 0x11e8
   __DATA.__bss: 0x319
   __DATA.__common: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 1528
-  Symbols:   455
-  CStrings:  3182
+  Functions: 2040
+  Symbols:   456
+  CStrings:  3184
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "UserManagement early boot task failed assertion: loginwindowSession != ((void*)0)"
+ "UserManagement early boot task failed assertion: mobileSession != ((void*)0)"
+ "UserManagement user switch failed assertion: oldSession != ((void*)0)"
- "UserManagement early boot task failed assertion: loginwindowSession != ((void *)0)"
- "UserManagement early boot task failed assertion: mobileSession != ((void *)0)"
- "UserManagement user switch failed assertion: oldSession != ((void *)0)"

```
