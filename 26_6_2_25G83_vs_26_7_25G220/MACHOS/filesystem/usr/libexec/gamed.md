## gamed

> `usr/libexec/gamed`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-820.6.10.1.1
-  __TEXT.__text: 0x3956d0
-  __TEXT.__auth_stubs: 0x4840
+820.6.10.1.2
+  __TEXT.__text: 0x395790
+  __TEXT.__auth_stubs: 0x4850
   __TEXT.__objc_stubs: 0x1baa0
   __TEXT.__objc_methlist: 0xe1fc
   __TEXT.__const: 0x6fd30
   __TEXT.__objc_classname: 0x2b67
-  __TEXT.__oslogstring: 0x18659
+  __TEXT.__oslogstring: 0x18699
   __TEXT.__cstring: 0x19f01
   __TEXT.__objc_methname: 0x23d97
   __TEXT.__objc_methtype: 0x731d

   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__unwind_info: 0x9c50
   __TEXT.__eh_frame: 0xc930
-  __DATA_CONST.__auth_got: 0x2438
+  __DATA_CONST.__auth_got: 0x2440
   __DATA_CONST.__got: 0x1f78
   __DATA_CONST.__auth_ptr: 0xff8
   __DATA_CONST.__const: 0x1c858

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13322
-  Symbols:   2578
-  CStrings:  10584
+  Functions: 13323
+  Symbols:   2579
+  CStrings:  10585
 
Symbols:
+ _GKPathInsideImageCache
CStrings:
+ "Refusing to cache image at path outside the image cache: %@"
```
