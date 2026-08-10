## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1303.0.3.0.0
-  __TEXT.__text: 0x6ddc8
+1303.0.6.0.0
+  __TEXT.__text: 0x6ddec
   __TEXT.__objc_methlist: 0x2028
   __TEXT.__const: 0x3c8
   __TEXT.__cstring: 0xe0b4
-  __TEXT.__oslogstring: 0x4024
+  __TEXT.__oslogstring: 0x4089
   __TEXT.__gcc_except_tab: 0x3630
   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__unwind_info: 0x18d0

   - /usr/lib/libsqlite3.dylib
   Functions: 2125
   Symbols:   4209
-  CStrings:  3795
+  CStrings:  3796
 
Functions:
~ ___42-[PCSCKKSSyncViewOperation checkTLKStatus]_block_invoke : 520 -> 556
CStrings:
+ "CKKS response for active views: not in circle"
+ "CKKS response for active views: wait for Octagon. This should resolve, proceeding with CKKS sync anyway"
- "CKKS response for active views: wait for Octagon"
```
