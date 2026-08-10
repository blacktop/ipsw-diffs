## AccessibilityDataMigration

> `/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-3237.1.0.0.0
-  __TEXT.__text: 0x2860
-  __TEXT.__auth_stubs: 0x2e0
+3240.3.0.0.0
+  __TEXT.__text: 0x291c
+  __TEXT.__auth_stubs: 0x2f0
   __TEXT.__objc_stubs: 0x10c0
   __TEXT.__objc_methlist: 0x188
-  __TEXT.__const: 0x38
+  __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x58
   __TEXT.__cstring: 0xa1c
-  __TEXT.__oslogstring: 0x12a
+  __TEXT.__oslogstring: 0x17d
   __TEXT.__objc_methname: 0xf6b
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methtype: 0x44

   __DATA_CONST.__cfstring: 0x860
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__auth_got: 0x188
   __DATA_CONST.__got: 0xf8
   __DATA.__objc_const: 0xd0
   __DATA.__objc_selrefs: 0x488

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 34
-  Symbols:   87
-  CStrings:  229
+  Symbols:   88
+  CStrings:  231
 
Symbols:
+ __AXSTripleClickCopyOptions
Functions:
~ sub_12a0 : 208 -> 396
CStrings:
+ "Triple click options after migration: %@"
+ "Triple click options before migration: %@"
```
