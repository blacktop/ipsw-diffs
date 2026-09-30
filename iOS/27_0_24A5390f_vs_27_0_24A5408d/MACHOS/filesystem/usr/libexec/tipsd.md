## tipsd

> `/usr/libexec/tipsd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-857.0.0.0.0
-  __TEXT.__text: 0x18a7c
+866.0.0.0.0
+  __TEXT.__text: 0x18b8c
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_stubs: 0x2e20
-  __TEXT.__objc_methlist: 0xd58
+  __TEXT.__objc_stubs: 0x2e40
+  __TEXT.__objc_methlist: 0xd60
   __TEXT.__const: 0x36c
   __TEXT.__gcc_except_tab: 0x4bc
-  __TEXT.__cstring: 0xe5c
-  __TEXT.__objc_methname: 0x379f
-  __TEXT.__oslogstring: 0x1706
+  __TEXT.__cstring: 0xe8c
+  __TEXT.__objc_methname: 0x37c0
+  __TEXT.__oslogstring: 0x172b
   __TEXT.__objc_classname: 0x225
   __TEXT.__objc_methtype: 0x1189
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0xac
-  __TEXT.__unwind_info: 0x700
+  __TEXT.__unwind_info: 0x708
   __TEXT.__eh_frame: 0xa28
-  __DATA_CONST.__const: 0xd90
+  __DATA_CONST.__const: 0xdb8
   __DATA_CONST.__cfstring: 0x880
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x98

   __DATA_CONST.__got: 0x400
   __DATA_CONST.__auth_ptr: 0xe8
   __DATA.__objc_const: 0xc60
-  __DATA.__objc_selrefs: 0xeb0
+  __DATA.__objc_selrefs: 0xeb8
   __DATA.__objc_ivar: 0x68
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x660

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 486
+  Functions: 489
   Symbols:   402
-  CStrings:  918
+  CStrings:  921
 
CStrings:
+ "XPC: fetchELabelURLsForCurrentDevice"
+ "fetchELabelURLsForCurrentDevice:"
+ "v32@?0@\"NSURL\"8@\"NSURL\"16@\"NSError\"24"
```
