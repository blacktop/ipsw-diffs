## securityd

> `/usr/libexec/securityd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`

```diff

-62460.0.38.0.1
-  __TEXT.__text: 0x26c4bc
+62460.0.55.0.1
+  __TEXT.__text: 0x26c590
   __TEXT.__auth_stubs: 0x4350
-  __TEXT.__objc_stubs: 0x1d8c0
+  __TEXT.__objc_stubs: 0x1d8e0
   __TEXT.__objc_methlist: 0x15e50
   __TEXT.__const: 0x910
   __TEXT.__cstring: 0x2273b
-  __TEXT.__objc_methname: 0x2e5af
+  __TEXT.__objc_methname: 0x2e5bf
   __TEXT.__oslogstring: 0x2fe5c
   __TEXT.__swift5_typeref: 0x372
   __TEXT.__swift5_fieldmd: 0x120

   __DATA_CONST.__got: 0x1528
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA.__objc_const: 0x23c40
-  __DATA.__objc_selrefs: 0x9850
+  __DATA.__objc_selrefs: 0x9858
   __DATA.__objc_ivar: 0x1ae8
   __DATA.__objc_data: 0x5d48
   __DATA.__data: 0x3150

   - /usr/lib/swift/libswiftos.dylib
   Functions: 9910
   Symbols:   1890
-  CStrings:  16391
+  CStrings:  16392
 
Symbols:
+ _kSecurityRTCEventNameJoinButDistrustEveryone
- _kSecurityRTCFieldDistrustEveryoneOnJoin
Functions:
~ sub_10012e48c : 932 -> 1048
~ sub_1001bbabc -> sub_1001bbb30 : 984 -> 996
~ sub_10020bf0c -> sub_10020bf8c : 1432 -> 1444
~ sub_10020c6c0 -> sub_10020c74c : 112 -> 184
CStrings:
+ "setPreventCylonUsage:"
```
