## trustd

> `/usr/libexec/trustd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-62460.2.2.0.0
-  __TEXT.__text: 0x59b58
+62460.2.3.0.0
+  __TEXT.__text: 0x59ce0
   __TEXT.__auth_stubs: 0x23d0
-  __TEXT.__objc_stubs: 0x3360
+  __TEXT.__objc_stubs: 0x3380
   __TEXT.__objc_methlist: 0xe14
   __TEXT.__const: 0xde40
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__objc_classname: 0x1b4
-  __TEXT.__objc_methname: 0x2fbe
+  __TEXT.__objc_methname: 0x2fd4
   __TEXT.__objc_methtype: 0xc6b
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x17

   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xae0
-  __TEXT.__cstring: 0x60c3
+  __TEXT.__cstring: 0x6115
   __TEXT.__oslogstring: 0x5d96
-  __TEXT.__unwind_info: 0x1018
-  __DATA_CONST.__const: 0x3dc8
-  __DATA_CONST.__cfstring: 0x5d40
+  __TEXT.__unwind_info: 0x1020
+  __DATA_CONST.__const: 0x3de0
+  __DATA_CONST.__cfstring: 0x5da0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__got: 0x930
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x1750
-  __DATA.__objc_selrefs: 0xe58
+  __DATA.__objc_selrefs: 0xe60
   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x5b8
-  __DATA.__data: 0x3f8
+  __DATA.__data: 0x400
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1202
+  Functions: 1204
   Symbols:   889
-  CStrings:  2210
+  CStrings:  2214
 
CStrings:
+ "PhotoRevocationCheck"
+ "com.apple.private.trustd.prl-access"
+ "isPhotoRevoked:error:"
+ "photoID must be 32 bytes"
```
