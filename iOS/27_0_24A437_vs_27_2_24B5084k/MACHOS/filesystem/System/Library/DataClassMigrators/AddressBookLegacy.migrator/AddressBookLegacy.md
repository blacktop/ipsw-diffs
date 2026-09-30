## AddressBookLegacy

> `/System/Library/DataClassMigrators/AddressBookLegacy.migrator/AddressBookLegacy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-12877.100.1.0.0
-  __TEXT.__text: 0x24e8
-  __TEXT.__auth_stubs: 0x490
+12880.200.11.0.0
+  __TEXT.__text: 0x254c
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_stubs: 0x540
   __TEXT.__objc_methlist: 0x11c
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x94
+  __TEXT.__gcc_except_tab: 0xbc
   __TEXT.__objc_methname: 0x554
-  __TEXT.__cstring: 0x30f
+  __TEXT.__cstring: 0x319
   __TEXT.__oslogstring: 0x71a
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methtype: 0xad
   __TEXT.__dlopen_cstrs: 0xa3
   __TEXT.__unwind_info: 0x140
   __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__auth_got: 0x290
   __DATA_CONST.__got: 0x50
   __DATA.__objc_const: 0x130
   __DATA.__objc_selrefs: 0x180

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 43
-  Symbols:   93
-  CStrings:  127
+  Functions: 44
+  Symbols:   100
+  CStrings:  128
 
Symbols:
+ _ABMigrationGateBegin
+ _ABMigrationGateEnd
+ _ABMigrationGateRenew
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_terminate
CStrings:
+ "no errors"
```
