## libramrod.dylib

> `/usr/lib/libramrod.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-3696.0.7.0.0
-  __TEXT.__text: 0xeec34
-  __TEXT.__objc_methlist: 0x1194
-  __TEXT.__cstring: 0x2bb6f
-  __TEXT.__const: 0x79100
+3696.0.12.0.3
+  __TEXT.__text: 0xeedb4
+  __TEXT.__objc_methlist: 0x119c
+  __TEXT.__cstring: 0x2bbc5
+  __TEXT.__const: 0x79110
   __TEXT.__gcc_except_tab: 0xb2c
   __TEXT.__oslogstring: 0xac8
   __TEXT.__unwind_info: 0x1e88

   __TEXT.__objc_stubs: 0x2900
   __TEXT.__auth_stubs: 0x2af0
   __TEXT.__objc_classname: 0x18b
-  __TEXT.__objc_methname: 0x29d3
+  __TEXT.__objc_methname: 0x29f1
   __TEXT.__objc_methtype: 0xb58
   __DATA_CONST.__const: 0x1f88
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcc8
+  __DATA_CONST.__objc_selrefs: 0xcd0
   __DATA_CONST.__got: 0x2c0
   __AUTH_CONST.__const: 0x2068
-  __AUTH_CONST.__cfstring: 0xc3a0
+  __AUTH_CONST.__cfstring: 0xc3c0
   __AUTH_CONST.__objc_const: 0x1ad0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x30

   __DATA.__objc_classrefs: 0x128
   __DATA.__objc_superrefs: 0x80
   __DATA.__objc_ivar: 0x138
-  __DATA.__data: 0x2598
-  __DATA.__bss: 0x888
+  __DATA.__data: 0x2590
+  __DATA.__bss: 0x8a0
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib
   - /usr/lib/updaters/libBMCMCUUpdater.dylib
-  Functions: 2860
-  Symbols:   1885
-  CStrings:  6356
+  Functions: 2862
+  Symbols:   1886
+  CStrings:  6360
 
Symbols:
+ _Img4EncodeItemCopyAndTransferBuffer
CStrings:
+ "Will use display %s (ctx %d)\n"
+ "aux image path set: %s\n"
+ "ctx[%d] rotation: %d\n"
+ "display-boot-rotation (MG) = %d\n"
+ "hasExclusiveUSBHostDeviceMode"
+ "usb-host-device-exclusive"
- "Will use display %s\n"
- "display-boot-rotation = %d\n"
```
