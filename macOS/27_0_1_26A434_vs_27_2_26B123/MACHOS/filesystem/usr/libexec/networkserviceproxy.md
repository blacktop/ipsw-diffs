## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__info_plist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-985.0.0.0.0
-  __TEXT.__text: 0xcdbc0
+990.40.2.0.0
+  __TEXT.__text: 0xce008
   __TEXT.__auth_stubs: 0x1740
   __TEXT.__objc_stubs: 0xd0e0
   __TEXT.__objc_methlist: 0x5044
-  __TEXT.__const: 0x288
+  __TEXT.__const: 0x290
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x3854
-  __TEXT.__oslogstring: 0x116e4
-  __TEXT.__cstring: 0xdf54
-  __TEXT.__objc_methname: 0x102bb
+  __TEXT.__gcc_except_tab: 0x3894
+  __TEXT.__oslogstring: 0x117be
+  __TEXT.__cstring: 0xe00b
+  __TEXT.__objc_methname: 0x102f3
   __TEXT.__objc_classname: 0xc2e
   __TEXT.__objc_methtype: 0x2a60
   __TEXT.__info_plist: 0x44b
   __TEXT.__unwind_info: 0x2058
   __DATA_CONST.__const: 0x25d8
-  __DATA_CONST.__cfstring: 0x8bc0
+  __DATA_CONST.__cfstring: 0x8c80
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0x108
-  __DATA_CONST.__objc_intobj: 0x6d8
+  __DATA_CONST.__objc_intobj: 0x6f0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0xbb0
   __DATA_CONST.__got: 0x840
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0xb158
+  __DATA.__objc_const: 0xb198
   __DATA.__objc_selrefs: 0x3ae0
-  __DATA.__objc_ivar: 0x9fc
+  __DATA.__objc_ivar: 0xa04
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0xb48
   __DATA.__bss: 0x218

   - /usr/lib/libobjc.A.dylib
   Functions: 2254
   Symbols:   618
-  CStrings:  6306
+  CStrings:  6316
 
Functions:
~ sub_10004e33c : 180 -> 236
~ sub_10004e3f0 -> sub_10004e428 : 116 -> 164
~ sub_10004e46c -> sub_10004e4d4 : 328 -> 432
~ sub_10004e5b4 -> sub_10004e684 : 140 -> 220
~ sub_10004ec94 -> sub_10004edb4 : 140 -> 220
~ sub_10004ed30 -> sub_10004eea0 : 1560 -> 1772
~ sub_10004f4c8 -> sub_10004f70c : 1200 -> 1344
~ sub_10004fa08 -> sub_10004fcdc : 56 -> 80
~ sub_10005306c -> sub_100053358 : 1860 -> 1916
~ sub_10008ffd0 -> sub_1000902f4 : 1536 -> 1660
~ sub_1000b587c -> sub_1000b5c1c : 5960 -> 6128
CStrings:
+ "$"
+ "%@ failed to create \"SafariTechnologyPreview PRIVATE UNENCRYPTED\" policies"
+ "Device Identity Failure Code"
+ "Device Identity Failure Domain"
+ "Device identity would be fetched on %@; deferral triggered by %{public}@ error %ld"
+ "DeviceIdentityFailureCode"
+ "DeviceIdentityFailureDomain"
+ "_deviceIdentityFailureCode"
+ "_deviceIdentityFailureDomain"
+ "deferring fetching device identity until %@, after %u failed retries; last recorded failure was %{public}@ error %ld"
+ "https://mask-api.icloud.com/v6_2/fetchConfigFile"
+ "previously failed to fetch device identity with %{public}@ error %ld, allowing retry %u"
+ "unrecorded domain"
- "Device identity would be fetched on %@"
- "deferring fetching device identity until %@"
- "previously failed to fetch device identity, allowing retry %u"
```
