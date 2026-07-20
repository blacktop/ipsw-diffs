## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

 59.160.7.0.0
-  __TEXT.__text: 0x59a30
+  __TEXT.__text: 0x599e8
   __TEXT.__auth_stubs: 0xf10
   __TEXT.__objc_methlist: 0x41e4
   __TEXT.__const: 0x1ba
   __TEXT.__gcc_except_tab: 0x10e4
   __TEXT.__cstring: 0x5707
-  __TEXT.__oslogstring: 0x71ad
+  __TEXT.__oslogstring: 0x717e
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x68

   - /usr/lib/swift/libswiftos.dylib
   Functions: 1664
   Symbols:   4847
-  CStrings:  3597
+  CStrings:  3596
 
Functions:
~ -[MDMServerCore migrateMDMWithContext:completion:] : 324 -> 252
CStrings:
- "Device is on seed build. Skip the random delay"
```
