## trustdFileHelper

> `/usr/libexec/trustdFileHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-62460.0.55.0.1
-  __TEXT.__text: 0x1dac
+62460.2.1.0.0
+  __TEXT.__text: 0x1e00
   __TEXT.__auth_stubs: 0x390
   __TEXT.__objc_stubs: 0x620
   __TEXT.__objc_methlist: 0x1dc
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x481
+  __TEXT.__cstring: 0x4fd
   __TEXT.__oslogstring: 0x116
   __TEXT.__objc_classname: 0x6a
   __TEXT.__objc_methname: 0x5d4

   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__unwind_info: 0xf0
   __DATA_CONST.__const: 0x2e8
-  __DATA_CONST.__cfstring: 0x540
+  __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   - /usr/lib/libobjc.A.dylib
   Functions: 44
   Symbols:   90
-  CStrings:  162
+  CStrings:  166
 
Symbols:
+ _objc_retain_x25
- _objc_retain_x24
Functions:
~ sub_100001918 : 1276 -> 1360
CStrings:
+ "private/TrustStore.sqlite3"
+ "private/TrustStore.sqlite3-journal"
+ "private/TrustStore.sqlite3-shm"
+ "private/TrustStore.sqlite3-wal"
```
