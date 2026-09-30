## securityuploadd

> `/usr/libexec/securityuploadd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.2.2.0.0
-  __TEXT.__text: 0x13210
+62460.2.3.0.0
+  __TEXT.__text: 0x13224
   __TEXT.__auth_stubs: 0xf50
   __TEXT.__objc_stubs: 0x1f80
   __TEXT.__objc_methlist: 0x8fc

   __TEXT.__swift5_fieldmd: 0xfc
   __TEXT.__oslogstring: 0xe38
   __TEXT.__swift5_capture: 0xf0
-  __TEXT.__cstring: 0x107e
+  __TEXT.__cstring: 0x1086
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
   __TEXT.__gcc_except_tab: 0x290
Functions:
~ sub_100002a60 : 1172 -> 1188
~ sub_1000132dc -> sub_1000132ec : 1196 -> 1200
CStrings:
+ "62460.2.3"
+ "DevicePercentageCustomer"
+ "SecondsBetweenUploadsCustomer"
- "62460.2.2"
- "DevicePercentageSeed"
- "SecondsBetweenUploadsSeed"
```
