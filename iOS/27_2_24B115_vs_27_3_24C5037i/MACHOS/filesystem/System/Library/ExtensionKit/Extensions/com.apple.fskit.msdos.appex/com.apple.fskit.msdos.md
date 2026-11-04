## com.apple.fskit.msdos

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__objc_classname`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-845.40.3.0.0
-  __TEXT.__text: 0x154fc
-  __TEXT.__auth_stubs: 0x7f0
+845.60.2.0.0
+  __TEXT.__text: 0x15894
+  __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_stubs: 0x1f80
+  __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xd04
   __TEXT.__const: 0x4e26
-  __TEXT.__cstring: 0x286d
-  __TEXT.__oslogstring: 0xf6d
+  __TEXT.__cstring: 0x2889
   __TEXT.__objc_classname: 0x154
   __TEXT.__objc_methname: 0x229e
   __TEXT.__objc_methtype: 0xad9
-  __TEXT.__gcc_except_tab: 0x464
+  __TEXT.__oslogstring: 0xf6d
+  __TEXT.__gcc_except_tab: 0x4ec
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_typeref: 0x80

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x5e0
+  __TEXT.__unwind_info: 0x5d8
   __DATA_CONST.__const: 0x3c0
   __DATA_CONST.__cfstring: 0x4e0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__auth_got: 0x408
-  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x68
   __DATA.__objc_const: 0x16d0
   __DATA.__objc_selrefs: 0xac0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 457
-  Symbols:   323
-  CStrings:  1021
+  Functions: 458
+  Symbols:   324
+  CStrings:  1022
 
Symbols:
+ _fat_std_log
+ _fat_std_log_set_subsystem
- __os_log_default
CStrings:
+ "com.apple.filesystems.msdos"
```
