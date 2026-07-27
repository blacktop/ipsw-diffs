## linkd

> `/usr/libexec/linkd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__cstring`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-300.6.2.0.0
-  __TEXT.__text: 0x15ad50
+300.6.3.0.0
+  __TEXT.__text: 0x15aedc
   __TEXT.__auth_stubs: 0x2fe0
   __TEXT.__objc_stubs: 0x2a40
   __TEXT.__objc_methlist: 0x141c

   __TEXT.__objc_methname: 0x493d
   __TEXT.__objc_methtype: 0x1a9b
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__oslogstring: 0x3bcf
+  __TEXT.__oslogstring: 0x3c0f
   __TEXT.__swift5_protos: 0xa0
   __TEXT.__swift_as_entry: 0x8dc
   __TEXT.__swift_as_ret: 0x8c0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8581
+  Functions: 8583
   Symbols:   1464
-  CStrings:  1435
+  CStrings:  1436
 
CStrings:
+ "Client is missing entitlement. Failed to delete all records."
+ "LinkProgrammaticInterface-300.6.3"
- "LinkProgrammaticInterface-300.6.2"
```
