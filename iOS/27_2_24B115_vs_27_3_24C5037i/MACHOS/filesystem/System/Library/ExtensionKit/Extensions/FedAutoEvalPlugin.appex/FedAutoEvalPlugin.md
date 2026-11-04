## FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-47.0.0.0.0
-  __TEXT.__text: 0x1007c
-  __TEXT.__auth_stubs: 0xf40
+51.0.0.0.0
+  __TEXT.__text: 0x10ac0
+  __TEXT.__auth_stubs: 0xf60
   __TEXT.__objc_stubs: 0x60
   __TEXT.__const: 0x8c0
-  __TEXT.__cstring: 0x142
+  __TEXT.__cstring: 0x162
   __TEXT.__swift5_typeref: 0x1f1
   __TEXT.__swift5_reflstr: 0x3e5
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x1a0
   __TEXT.__swift5_fieldmd: 0x214
-  __TEXT.__oslogstring: 0x2fa
+  __TEXT.__oslogstring: 0x30a
   __TEXT.__objc_methtype: 0x15
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift_as_entry: 0x68
-  __TEXT.__swift_as_ret: 0x74
-  __TEXT.__swift_as_cont: 0x88
+  __TEXT.__swift_as_ret: 0x78
+  __TEXT.__swift_as_cont: 0x90
   __TEXT.__objc_classname: 0x71
   __TEXT.__objc_methname: 0xb7
-  __TEXT.__unwind_info: 0x4b0
-  __TEXT.__eh_frame: 0xcc0
+  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__eh_frame: 0xd58
   __DATA_CONST.__const: 0x3c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x7a8
+  __DATA_CONST.__auth_got: 0x7b8
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x2b8
   __DATA.__objc_const: 0x208

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 229
+  Functions: 232
   Symbols:   129
-  CStrings:  39
+  CStrings:  40
 
Symbols:
+ _swift_retain_x24
- _swift_release_x21
CStrings:
+ "Returning a vector of %ld floats from plugin, metadata=%s"
+ "morpheusProgramFileName"
- "Returning from plugin metadata=%s, vector=%s"
```
