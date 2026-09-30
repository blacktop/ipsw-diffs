## TVStorageExtension

> `/System/Applications/TV.app/Contents/PlugIns/TVStorageExtension.appex/Contents/MacOS/TVStorageExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1.7.0.146.0
-  __TEXT.__text: 0x1f9c8
-  __TEXT.__auth_stubs: 0xd30
+1.7.0.161.2
+  __TEXT.__text: 0x1f98c
+  __TEXT.__auth_stubs: 0xd20
   __TEXT.__objc_stubs: 0xf40
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x298

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x6b0
+  __DATA_CONST.__auth_got: 0x6a8
   __DATA_CONST.__got: 0x1c8
   __DATA.__objc_const: 0x280
   __DATA.__objc_selrefs: 0x4d8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 783
-  Symbols:   286
+  Functions: 782
+  Symbols:   285
   CStrings:  567
 
Symbols:
- _pthread_kill
Functions:
~ sub_100008dd4 : 60 -> 4
- sub_100008e10
+ sub_100017d1c
- sub_100017ffc
CStrings:
+ "1.7.0.161"
- "1.7.0.146"
```
