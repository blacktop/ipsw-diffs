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
-  __TEXT.__text: 0x858
-  __TEXT.__auth_stubs: 0x240
+383.40.11.0.0
+  __TEXT.__text: 0x85c
+  __TEXT.__auth_stubs: 0x250
   __TEXT.__objc_stubs: 0x40
   __TEXT.__const: 0x42
   __TEXT.__cstring: 0x6f

   __TEXT.__unwind_info: 0x98
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__auth_got: 0x130
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_selrefs: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 11
-  Symbols:   54
+  Symbols:   55
   CStrings:  10
 
Symbols:
+ _$s8CipherML23DataProtectionMigrationO15migrateIfNeededyyFZ
Functions:
~ sub_100000c78 : 1160 -> 1164
```
