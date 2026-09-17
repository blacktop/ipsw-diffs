## ciphermld

> `/usr/libexec/ciphermld`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-383.0.24.0.0
-  __TEXT.__text: 0x2870
-  __TEXT.__auth_stubs: 0x510
+383.40.11.0.0
+  __TEXT.__text: 0x2874
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0x40
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x1ed

   __TEXT.__unwind_info: 0x110
   __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x38
   __DATA.__objc_selrefs: 0x10

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 39
-  Symbols:   117
+  Symbols:   118
   CStrings:  20
 
Symbols:
+ _$s8CipherML23DataProtectionMigrationO15migrateIfNeededyyFZ
Functions:
~ sub_100000d30 : 1220 -> 1224
```
