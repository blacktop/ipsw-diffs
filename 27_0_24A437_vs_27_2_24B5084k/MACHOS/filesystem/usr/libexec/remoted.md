## remoted

> `/usr/libexec/remoted`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-245.0.7.0.0
-  __TEXT.__text: 0x3cc4c
+245.40.8.0.0
+  __TEXT.__text: 0x3cd14
   __TEXT.__auth_stubs: 0x1860
-  __TEXT.__objc_stubs: 0x24a0
-  __TEXT.__objc_methlist: 0x1560
+  __TEXT.__objc_stubs: 0x2520
+  __TEXT.__objc_methlist: 0x1590
   __TEXT.__const: 0x22a
-  __TEXT.__oslogstring: 0x8502
-  __TEXT.__cstring: 0x21d9
-  __TEXT.__objc_methname: 0x254c
+  __TEXT.__oslogstring: 0x85d2
+  __TEXT.__cstring: 0x2243
+  __TEXT.__objc_methname: 0x259a
   __TEXT.__objc_classname: 0x2c9
   __TEXT.__objc_methtype: 0x79b
-  __TEXT.__gcc_except_tab: 0x1120
-  __TEXT.__unwind_info: 0x1470
-  __DATA_CONST.__const: 0x12c8
-  __DATA_CONST.__cfstring: 0xea0
+  __TEXT.__gcc_except_tab: 0x1098
+  __TEXT.__unwind_info: 0x1480
+  __DATA_CONST.__const: 0x12b0
+  __DATA_CONST.__cfstring: 0xf00
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0xc40
   __DATA_CONST.__got: 0x250
-  __DATA.__objc_const: 0x2810
-  __DATA.__objc_selrefs: 0x980
-  __DATA.__objc_ivar: 0x21c
+  __DATA.__objc_const: 0x2850
+  __DATA.__objc_selrefs: 0x9a0
+  __DATA.__objc_ivar: 0x220
   __DATA.__objc_data: 0x870
   __DATA.__data: 0x6d4
   __DATA.__common: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1376
+  Functions: 1385
   Symbols:   492
-  CStrings:  1776
+  CStrings:  1786
 
Symbols:
+ _MGGetBoolAnswer
- _IORegistryEntryFromPath
CStrings:
+ "%{public}@> Device connection interrupted expectedly because of %{public}s; reattaching"
+ "%{public}@> Peer UUID changed across reconnect; reattaching so clients re-discover it"
+ "NLWYUp5icK9sRsPDI7XJtw"
+ "Not using public NCM interface due to the existence of private NCM interface"
+ "Not using public NCM interface on compute node"
+ "RvCUAjrf7O/zAzV1StnBlg"
+ "Using public NCM interface"
+ "XjG5q4m+sX+F9Prap4MBAQ"
+ "_needs_reattach"
+ "a reattach"
+ "a reset"
+ "beingReset"
+ "both controller and node device according to MobileGestalt"
+ "compute controller backend not initialized, cannot add device on %{public}s"
+ "connect_loopback_with_override"
+ "disconnect_loopback"
+ "needsReattach"
+ "override"
+ "reattach"
+ "shouldReattachForHandshake:"
- "%{public}@> Device connection interrupted. Proceed to reset"
- "IODeviceTree:/"
- "IODeviceTree:/%s"
- "IORegistryEntryCreateIterator: %d"
- "IORegistryEntryGetName: %d"
- "assertion failure: \"name\" -> %llu"
- "both manta-b and manta-c device found in device tree"
- "failed to find ioreg path: %{public}s"
- "manta-b"
- "manta-c"
```
