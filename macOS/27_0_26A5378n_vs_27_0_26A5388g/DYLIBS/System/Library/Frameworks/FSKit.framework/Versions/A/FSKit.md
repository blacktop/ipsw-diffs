## FSKit

> `/System/Library/Frameworks/FSKit.framework/Versions/A/FSKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-974.0.7.0.0
-  __TEXT.__text: 0x58d8c
-  __TEXT.__objc_methlist: 0x6278
+974.0.11.0.0
+  __TEXT.__text: 0x58dac
+  __TEXT.__objc_methlist: 0x6288
   __TEXT.__const: 0x4a8
   __TEXT.__gcc_except_tab: 0xe7c
-  __TEXT.__oslogstring: 0x3fb6
+  __TEXT.__oslogstring: 0x3fc6
   __TEXT.__cstring: 0x636f
   __TEXT.__swift5_typeref: 0x264
   __TEXT.__swift5_capture: 0xec

   __TEXT.__constg_swiftt: 0x210
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1858
+  __TEXT.__unwind_info: 0x1860
   __TEXT.__eh_frame: 0x400
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c10
+  __DATA_CONST.__objc_selrefs: 0x2c18
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x488
   __DATA_CONST.__got: 0x488
-  __AUTH_CONST.__const: 0x1e90
+  __AUTH_CONST.__const: 0x1ec0
   __AUTH_CONST.__cfstring: 0x2b20
   __AUTH_CONST.__objc_const: 0xb258
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2738
-  Symbols:   5201
+  Functions: 2739
+  Symbols:   5204
   CStrings:  1089
 
Symbols:
+ -[FSFreeSpace(Project) isNoUpdate]
+ ___block_descriptor_48_e8_32bs40bs_e17_v16?0"NSError"8l
+ _objc_msgSend$isNoUpdate
CStrings:
+ "%s: freeSpaceData called on the \"no update\" sentinel"
- "%s: free space was not populated!"
```
