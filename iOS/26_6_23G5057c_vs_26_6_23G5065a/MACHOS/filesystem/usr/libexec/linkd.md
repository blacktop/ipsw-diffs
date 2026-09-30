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

-  __TEXT.__text: 0x1675ec
+  __TEXT.__text: 0x167784
   __TEXT.__auth_stubs: 0x3310
   __TEXT.__objc_stubs: 0x2ac0
   __TEXT.__objc_methlist: 0x1404

   __TEXT.__objc_methname: 0x499d
   __TEXT.__objc_methtype: 0x1a2b
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__oslogstring: 0x419f
+  __TEXT.__oslogstring: 0x41df
   __TEXT.__swift5_protos: 0xa0
   __TEXT.__swift_as_entry: 0x8e8
   __TEXT.__swift_as_ret: 0x8cc

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8832
+  Functions: 8834
   Symbols:   1544
-  CStrings:  1476
+  CStrings:  1477
 
CStrings:
+ "Client is missing entitlement. Failed to delete all records."
+ "LinkProgrammaticInterface-300.6.3"
- "LinkProgrammaticInterface-300.6.2"
```
