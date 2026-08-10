## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
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
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-154.0.0.0.0
-  __TEXT.__text: 0x69b78
+156.0.0.0.0
+  __TEXT.__text: 0x69c58
   __TEXT.__objc_methlist: 0x6c4
   __TEXT.__const: 0x4550
-  __TEXT.__cstring: 0x651e
+  __TEXT.__cstring: 0x659e
   __TEXT.__oslogstring: 0x386a
   __TEXT.__gcc_except_tab: 0x724
   __TEXT.__swift5_typeref: 0xb06

   __AUTH_CONST.__objc_const: 0x1938
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0xbe8
+  __AUTH_CONST.__auth_got: 0xbf0
   __AUTH.__objc_data: 0x3b8
   __AUTH.__data: 0x2e0
   __DATA.__objc_ivar: 0x40

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1489
   Symbols:   1344
-  CStrings:  826
+  CStrings:  829
 
Functions:
~ sub_22c4e2670 -> sub_22bd0e670 : 8796 -> 8800
~ sub_22c4e53d8 -> sub_22bd113dc : 564 -> 784
CStrings:
+ "AppAttest (%@-156) - %@"
+ "Not fetching CD hash."
+ "Should fetch CD hash. { source=default }"
+ "Should fetch CD hash. { source=entitlement }"
- "AppAttest (%@-154) - %@"
```
