## libAppleTconUARPUpdater.dylib

> `/usr/lib/updaters/libAppleTconUARPUpdater.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-1587.0.21.0.0
-  __TEXT.__text: 0x45944
-  __TEXT.__objc_methlist: 0x47cc
-  __TEXT.__cstring: 0x40f2
+1587.0.27.0.0
+  __TEXT.__text: 0x45c50
+  __TEXT.__objc_methlist: 0x47d4
+  __TEXT.__cstring: 0x4109
   __TEXT.__const: 0xa0
-  __TEXT.__oslogstring: 0x13a8
+  __TEXT.__oslogstring: 0x13ff
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x13d0
+  __TEXT.__unwind_info: 0x13e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa00
+  __DATA_CONST.__const: 0xa10
   __DATA_CONST.__objc_classlist: 0x518
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1160
+  __DATA_CONST.__objc_selrefs: 0x1168
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__got: 0x5e8
   __AUTH_CONST.__const: 0xb0
-  __AUTH_CONST.__cfstring: 0x3560
+  __AUTH_CONST.__cfstring: 0x35c0
   __AUTH_CONST.__objc_const: 0x9ee8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x32f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1942
-  Symbols:   3944
-  CStrings:  743
+  Functions: 1947
+  Symbols:   3951
+  CStrings:  747
 
Symbols:
+ -[UARPSuperBinaryLayer3 processSuperBinaryPropertyList:]
+ _UARPLayer3DateAsString
+ _UARPLayer3DateTimeAsString
+ _UARPLayer3TimestampAsString
+ _kUARPCommonPayloadPLST
+ _kUARPCommonPayloadPMAP
+ _objc_msgSend$processSuperBinaryPropertyList:
CStrings:
+ "%02ld-%02ld-%02ld"
+ "%04ld-%02ld-%02ld"
+ "%s: Failed to instantiate UARPSuperBinaryPayloadLayer3 at index %lu for %@"
+ "%s: processSuperBinaryPropertyList: failed to process"
+ "-"
+ "PLST"
- "%s: Failed to create payload at index %lu"
- "yyyy-MM-dd-HH-mm-ss"
```
