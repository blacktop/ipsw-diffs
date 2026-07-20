## tzd

> `/usr/libexec/tzd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-89.0.0.0.0
-  __TEXT.__text: 0x15c58
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_stubs: 0xc40
-  __TEXT.__objc_methlist: 0x44c
+90.0.0.0.0
+  __TEXT.__text: 0x15d18
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_stubs: 0xca0
+  __TEXT.__objc_methlist: 0x464
   __TEXT.__const: 0x8b0
-  __TEXT.__cstring: 0x17a4
-  __TEXT.__objc_methname: 0x139f
-  __TEXT.__objc_classname: 0x103
-  __TEXT.__objc_methtype: 0xb9a
+  __TEXT.__cstring: 0x17c4
+  __TEXT.__objc_methname: 0x13df
+  __TEXT.__objc_classname: 0x113
+  __TEXT.__objc_methtype: 0xb8a
   __TEXT.__swift5_typeref: 0x476
   __TEXT.__swift5_capture: 0x25c
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_proto: 0x58
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__unwind_info: 0x460
   __TEXT.__eh_frame: 0x320
   __DATA_CONST.__const: 0xc28
   __DATA_CONST.__cfstring: 0xa0
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x40

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x7b0
-  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__auth_got: 0x7b8
+  __DATA_CONST.__got: 0x280
   __DATA_CONST.__auth_ptr: 0x1e0
-  __DATA.__objc_const: 0x968
-  __DATA.__objc_selrefs: 0x4f8
+  __DATA.__objc_const: 0x9f8
+  __DATA.__objc_selrefs: 0x510
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x2b0
+  __DATA.__objc_data: 0x300
   __DATA.__data: 0x848
   __DATA.__bss: 0xb10
   __DATA.__common: 0xc8

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 424
-  Symbols:   403
-  CStrings:  384
+  Functions: 425
+  Symbols:   405
+  CStrings:  389
 
Symbols:
+ _OBJC_CLASS_$_UNNotificationIcon
+ _objc_retain_x3
CStrings:
+ "TZNotificationIcon"
+ "com.apple.Preferences"
+ "iconForApplicationIdentifier:"
+ "setIcon:"
+ "setIconForApplicationIdentifier:onContent:"
```
