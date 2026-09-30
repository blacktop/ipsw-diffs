## mobilerepaird

> `/usr/libexec/mobilerepaird`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__objc_classname`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1307.0.26.502.1
-  __TEXT.__text: 0xe088
+1307.0.46.0.0
+  __TEXT.__text: 0xe1c8
   __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0x1c00
+  __TEXT.__objc_stubs: 0x1c20
   __TEXT.__objc_methlist: 0xcfc
   __TEXT.__const: 0xb2
-  __TEXT.__gcc_except_tab: 0x3d0
-  __TEXT.__objc_methname: 0x212c
-  __TEXT.__cstring: 0x23b9
-  __TEXT.__oslogstring: 0xb2c
+  __TEXT.__gcc_except_tab: 0x3e8
+  __TEXT.__objc_methname: 0x2140
+  __TEXT.__cstring: 0x242b
+  __TEXT.__oslogstring: 0xac6
   __TEXT.__objc_classname: 0x2e1
   __TEXT.__objc_methtype: 0x3da
   __TEXT.__unwind_info: 0x350
-  __DATA_CONST.__const: 0x478
-  __DATA_CONST.__cfstring: 0x2300
+  __DATA_CONST.__const: 0x458
+  __DATA_CONST.__cfstring: 0x2380
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x350
   __DATA_CONST.__got: 0x330
   __DATA.__objc_const: 0x1b08
-  __DATA.__objc_selrefs: 0x8d8
+  __DATA.__objc_selrefs: 0x8e0
   __DATA.__objc_ivar: 0xbc
   __DATA.__objc_data: 0x820
   __DATA.__data: 0x190

   - /usr/lib/libobjc.A.dylib
   Functions: 292
   Symbols:   201
-  CStrings:  821
+  CStrings:  824
 
CStrings:
+ "FINISH_TOUCHID_REPAIR_DESC"
+ "FINISH_VB_REPAIR_DESC_IPAD"
+ "Processing EIC strobe notification - posting DisplayTCON hardware failure status (%@)"
+ "Received EIC strobe daemon notification - marking DisplayTCON as failed (%@)"
+ "Successfully unregistered exclave notification listener(s)"
+ "com.apple.medina.1.hw.failure"
+ "com.apple.medina.1.hw.success"
+ "handleExclaveNotification:"
+ "supportHarvestMesa"
- "Exclave notification handler already registered"
- "Exclave notification handler not registered, nothing to unregister"
- "Processing EIC strobe notification - posting DisplayTCON hardware failure status"
- "Received EIC strobe daemon notification - marking DisplayTCON as failed"
- "Successfully unregistered exclave notification listener"
- "handleExclaveNotification"
```
