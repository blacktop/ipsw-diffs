## SMS

> `/System/Library/Messages/PlugIns/SMS.imservice/SMS`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1491.200.73.0.0
-  __TEXT.__text: 0x108e0
+1491.200.95.0.0
+  __TEXT.__text: 0x10a50
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_stubs: 0x2b00
-  __TEXT.__objc_methlist: 0xdbc
+  __TEXT.__objc_stubs: 0x2b20
+  __TEXT.__objc_methlist: 0xdd4
   __TEXT.__const: 0x178
-  __TEXT.__gcc_except_tab: 0x1178
+  __TEXT.__gcc_except_tab: 0x1184
   __TEXT.__cstring: 0x650
-  __TEXT.__objc_methname: 0x48ea
-  __TEXT.__oslogstring: 0x1e4b
+  __TEXT.__objc_methname: 0x4932
+  __TEXT.__oslogstring: 0x1e7b
   __TEXT.__objc_classname: 0x247
   __TEXT.__objc_methtype: 0x1b2f
   __TEXT.__dlopen_cstrs: 0x5e

   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__auth_got: 0x468
-  __DATA_CONST.__got: 0x3e0
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x1180
-  __DATA.__objc_selrefs: 0x1038
+  __DATA.__objc_selrefs: 0x1040
   __DATA.__objc_ivar: 0x58
   __DATA.__objc_data: 0x3d0
   __DATA.__data: 0x418

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 222
+  Functions: 223
   Symbols:   307
-  CStrings:  1024
+  CStrings:  1026
 
Symbols:
+ _IMNormalizedPhoneNumberForPhoneNumber
- _IMCanonicalizeFormattedString
Functions:
~ sub_745c : 4036 -> 252
+ sub_7558
CStrings:
+ "Incoming recipient %@ is not the altPhoneNumber %@"
+ "_incomingRecipientHandle:matchesHiddenLocalNumber:receivingCountryCode:"
```
