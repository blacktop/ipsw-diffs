## linkd

> `/usr/libexec/linkd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__oslogstring`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-301.1.16.0.0
-  __TEXT.__text: 0xc0024
+301.1.16.1.104
+  __TEXT.__text: 0xc009c
   __TEXT.__auth_stubs: 0x2a50
   __TEXT.__objc_stubs: 0x27e0
   __TEXT.__objc_methlist: 0xe0c

   __TEXT.__objc_methname: 0x3ffd
   __TEXT.__objc_methtype: 0x188b
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__cstring: 0x1c80
+  __TEXT.__cstring: 0x1cb0
   __TEXT.__swift5_capture: 0x2f30
   __TEXT.__swift_as_entry: 0x594
   __TEXT.__swift_as_cont: 0x758

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5615
+  Functions: 5616
   Symbols:   1202
-  CStrings:  1240
+  CStrings:  1241
 
CStrings:
+ "com.apple.frontboard.launchapplications"
```
