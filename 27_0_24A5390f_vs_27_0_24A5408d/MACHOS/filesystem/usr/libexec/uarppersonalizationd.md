## uarppersonalizationd

> `/usr/libexec/uarppersonalizationd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA.__objc_const`
- `__DATA.__data`

```diff

-1587.0.27.0.0
+1587.2.2.0.0
   __TEXT.__text: 0x4b4c
   __TEXT.__auth_stubs: 0x4c0
   __TEXT.__objc_stubs: 0xaa0

   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0xa8
   __TEXT.__objc_methname: 0x939
-  __TEXT.__cstring: 0xdae
+  __TEXT.__cstring: 0xe23
   __TEXT.__oslogstring: 0x8f4
   __TEXT.__objc_classname: 0x94
   __TEXT.__objc_methtype: 0x1d7
   __TEXT.__unwind_info: 0x1b8
-  __DATA_CONST.__const: 0x520
-  __DATA_CONST.__cfstring: 0xfa0
+  __DATA_CONST.__const: 0x548
+  __DATA_CONST.__cfstring: 0x1020
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 126
   Symbols:   120
-  CStrings:  352
+  CStrings:  356
 
CStrings:
+ "com.apple.uarp.endpoint.assetavailable"
+ "com.apple.uarp.endpoint.assetavailable.subscriber"
+ "metrics"
+ "uarpTransportDomain"
```
