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
-  __TEXT.__text: 0x405bc
+245.40.8.0.0
+  __TEXT.__text: 0x406c8
   __TEXT.__auth_stubs: 0x1800
-  __TEXT.__objc_stubs: 0x2700
-  __TEXT.__objc_methlist: 0x1828
+  __TEXT.__objc_stubs: 0x2780
+  __TEXT.__objc_methlist: 0x1858
   __TEXT.__const: 0x222
-  __TEXT.__oslogstring: 0x89c5
-  __TEXT.__cstring: 0x245d
-  __TEXT.__objc_methname: 0x2976
+  __TEXT.__oslogstring: 0x8a95
+  __TEXT.__cstring: 0x24c7
+  __TEXT.__objc_methname: 0x29c4
   __TEXT.__objc_classname: 0x3c3
   __TEXT.__objc_methtype: 0x9e3
-  __TEXT.__gcc_except_tab: 0x1054
-  __TEXT.__unwind_info: 0x1550
-  __DATA_CONST.__const: 0x14e0
-  __DATA_CONST.__cfstring: 0xea0
+  __TEXT.__gcc_except_tab: 0xfcc
+  __TEXT.__unwind_info: 0x1558
+  __DATA_CONST.__const: 0x14d0
+  __DATA_CONST.__cfstring: 0xf00
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0xc10
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x2e38
-  __DATA.__objc_selrefs: 0xab0
-  __DATA.__objc_ivar: 0x244
+  __DATA.__objc_const: 0x2e78
+  __DATA.__objc_selrefs: 0xad0
+  __DATA.__objc_ivar: 0x248
   __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x8f0
   __DATA.__common: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1454
+  Functions: 1463
   Symbols:   489
-  CStrings:  1913
+  CStrings:  1923
 
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
