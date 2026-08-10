## OSEligibility

> `/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-446.0.2.0.0
-  __TEXT.__text: 0x1e6b0
+446.2.1.0.0
+  __TEXT.__text: 0x1e72c
   __TEXT.__objc_methlist: 0x17c
   __TEXT.__const: 0x5054
   __TEXT.__swift5_typeref: 0xe7e
-  __TEXT.__oslogstring: 0x1c0
+  __TEXT.__oslogstring: 0x1d0
   __TEXT.__cstring: 0x8f8
   __TEXT.__constg_swiftt: 0xb84
   __TEXT.__swift5_reflstr: 0x10f4

   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x138
+  __DATA_CONST.__objc_selrefs: 0x150
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x1728

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 931
-  Symbols:   544
+  Symbols:   547
   CStrings:  61
 
Symbols:
+ _objc_msgSend$betaTesterType
+ _objc_msgSend$distributorInfo
+ _objc_msgSend$iTunesMetadata
Functions:
~ sub_2953e1aa8 -> sub_294f79aa8 : 2888 -> 2932
~ sub_2953fbe70 -> sub_294f93e9c : 32 -> 112
CStrings:
+ "Not bypassing eligibility for %s:%s (isProfileValidated: %{bool}d isUPPValidated:%{bool}d isExternalBeta:%{bool}d)"
- "Not bypassing eligibility for %s:%s (isProfileValidated: %{bool}d isUPPValidated:%{bool}d isBeta:%{bool}d"
```
