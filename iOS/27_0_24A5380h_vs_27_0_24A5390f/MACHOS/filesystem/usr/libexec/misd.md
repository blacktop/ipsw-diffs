## misd

> `/usr/libexec/misd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-398.0.0.0.0
-  __TEXT.__text: 0x21d24
+399.0.0.0.0
+  __TEXT.__text: 0x21e14
   __TEXT.__auth_stubs: 0x1250
   __TEXT.__objc_stubs: 0x4e0
   __TEXT.__objc_methlist: 0x39c
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0xb6ba
+  __TEXT.__cstring: 0xb718
   __TEXT.__oslogstring: 0x1e
   __TEXT.__objc_methname: 0x915
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methtype: 0x6b7
   __TEXT.__unwind_info: 0x500
   __DATA_CONST.__const: 0xa18
-  __DATA_CONST.__cfstring: 0xb40
+  __DATA_CONST.__cfstring: 0xba0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 456
   Symbols:   393
-  CStrings:  1754
+  CStrings:  1758
 
Functions:
~ sub_100008d58 : 852 -> 972
~ sub_1000191c0 -> sub_100019238 : 2324 -> 2444
CStrings:
+ "DisableHostModeAllSubnetsLocal %s"
+ "HostModeAllSubnetsLocal"
+ "all_subnets_local"
+ "use_server_config"
```
