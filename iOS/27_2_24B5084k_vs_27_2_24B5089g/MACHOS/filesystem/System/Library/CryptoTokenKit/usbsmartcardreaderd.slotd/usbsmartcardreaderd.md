## usbsmartcardreaderd

> `/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/usbsmartcardreaderd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-878.40.2.0.0
-  __TEXT.__text: 0x16dd4
+878.40.4.0.0
+  __TEXT.__text: 0x16f68
   __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0x3660
-  __TEXT.__objc_methlist: 0x1a94
+  __TEXT.__objc_stubs: 0x36a0
+  __TEXT.__objc_methlist: 0x1abc
   __TEXT.__const: 0x2a0
   __TEXT.__objc_classname: 0x2fc
   __TEXT.__objc_methtype: 0xaf3
-  __TEXT.__objc_methname: 0x2a06
-  __TEXT.__oslogstring: 0x1a69
+  __TEXT.__objc_methname: 0x2a38
+  __TEXT.__oslogstring: 0x1aac
   __TEXT.__cstring: 0x16ea
   __TEXT.__gcc_except_tab: 0x2e8
-  __TEXT.__unwind_info: 0xac0
+  __TEXT.__unwind_info: 0xac8
   __DATA_CONST.__const: 0x898
   __DATA_CONST.__cfstring: 0x21a0
   __DATA_CONST.__objc_classlist: 0x128

   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__auth_got: 0x350
   __DATA_CONST.__got: 0x168
-  __DATA.__objc_const: 0x3348
-  __DATA.__objc_selrefs: 0xf40
+  __DATA.__objc_const: 0x3370
+  __DATA.__objc_selrefs: 0xf50
   __DATA.__objc_ivar: 0x144
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x370

   - /System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 740
+  Functions: 743
   Symbols:   151
-  CStrings:  1281
+  CStrings:  1284
 
CStrings:
+ "Ignoring RFU bChainParameter=0x%02x from non-extended-level reader"
+ "chainableTransmitter"
+ "supportsExtendedAPDUExchange"
```
