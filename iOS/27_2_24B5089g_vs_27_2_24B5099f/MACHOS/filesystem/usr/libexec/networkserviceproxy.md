## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-990.0.0.0.0
-  __TEXT.__text: 0xc0544
+990.40.2.0.0
+  __TEXT.__text: 0xc0888
   __TEXT.__auth_stubs: 0x18e0
   __TEXT.__objc_stubs: 0xd260
   __TEXT.__objc_methlist: 0x5044
-  __TEXT.__const: 0x2a0
+  __TEXT.__const: 0x2a8
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x388c
-  __TEXT.__oslogstring: 0x1176c
-  __TEXT.__cstring: 0xdf5b
-  __TEXT.__objc_methname: 0x1043c
+  __TEXT.__gcc_except_tab: 0x3898
+  __TEXT.__oslogstring: 0x11846
+  __TEXT.__cstring: 0xdfe1
+  __TEXT.__objc_methname: 0x10474
   __TEXT.__objc_classname: 0xc2e
   __TEXT.__objc_methtype: 0x2a77
   __TEXT.__unwind_info: 0x1f30
   __DATA_CONST.__const: 0x22f8
-  __DATA_CONST.__cfstring: 0x8c40
+  __DATA_CONST.__cfstring: 0x8ce0
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__auth_got: 0xc80
   __DATA_CONST.__got: 0x848
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0xb178
+  __DATA.__objc_const: 0xb1b8
   __DATA.__objc_selrefs: 0x3b40
-  __DATA.__objc_ivar: 0xa00
+  __DATA.__objc_ivar: 0xa08
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0xb48
   __DATA.__common: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 2162
   Symbols:   645
-  CStrings:  6327
+  CStrings:  6336
 
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
+ "previously failed to fetch device identity with %{public}@ error %ld, allowing retry %u"
+ "unrecorded domain"
- "Device identity would be fetched on %@"
- "deferring fetching device identity until %@"
- "previously failed to fetch device identity, allowing retry %u"
```
