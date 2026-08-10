## eventkitsyncd

> `/usr/libexec/eventkitsyncd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-430.0.0.0.0
-  __TEXT.__text: 0x75ec0
+431.0.0.0.0
+  __TEXT.__text: 0x761dc
   __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_stubs: 0xcbc0
+  __TEXT.__objc_stubs: 0xcc20
   __TEXT.__objc_methlist: 0x7510
-  __TEXT.__cstring: 0x5b50
-  __TEXT.__objc_methname: 0xfc6c
+  __TEXT.__cstring: 0x5b5a
+  __TEXT.__objc_methname: 0xfcc5
   __TEXT.__objc_classname: 0x8ae
   __TEXT.__objc_methtype: 0x2576
   __TEXT.__const: 0x278
-  __TEXT.__oslogstring: 0xbc30
+  __TEXT.__oslogstring: 0xbc8e
   __TEXT.__gcc_except_tab: 0x844
   __TEXT.__unwind_info: 0x1660
   __DATA_CONST.__const: 0x1870
-  __DATA_CONST.__cfstring: 0x5080
+  __DATA_CONST.__cfstring: 0x50c0
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA_CONST.__auth_got: 0x6d8
-  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__got: 0x4d8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xefb0
-  __DATA.__objc_selrefs: 0x3f60
+  __DATA.__objc_selrefs: 0x3f78
   __DATA.__objc_ivar: 0x998
   __DATA.__objc_data: 0x1e50
   __DATA.__data: 0x800

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
   Functions: 2865
-  Symbols:   369
-  CStrings:  4634
+  Symbols:   371
+  CStrings:  4641
 
Symbols:
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
+ _NSFileProtectionKey
Functions:
~ sub_100007ad8 : 176 -> 972
CStrings:
+ "-shm"
+ "-wal"
+ "== Started EventKitSync-431"
+ "Failed to set protection level of file %@ with error: %@"
+ "Updating protection level of file %@"
+ "attributesOfItemAtPath:error:"
+ "setAttributes:ofItemAtPath:error:"
+ "stringByAppendingString:"
- "== Started EventKitSync-430"
```
