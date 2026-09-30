## libAppleTconUARPUpdater.dylib

> `/usr/lib/updaters/libAppleTconUARPUpdater.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-1587.0.21.0.0
-  __TEXT.__text: 0x702e4
-  __TEXT.__objc_methlist: 0x67fc
-  __TEXT.__cstring: 0x7675
+1587.0.27.0.0
+  __TEXT.__text: 0x70778
+  __TEXT.__objc_methlist: 0x6804
+  __TEXT.__cstring: 0x76ff
   __TEXT.__const: 0x110
-  __TEXT.__oslogstring: 0x377b
+  __TEXT.__oslogstring: 0x3847
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x1a50
+  __TEXT.__unwind_info: 0x1a70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xdb8
+  __DATA_CONST.__const: 0xdc8
   __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xd8
   __DATA_CONST.__got: 0x680
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x54c0
+  __AUTH_CONST.__cfstring: 0x5520
   __AUTH_CONST.__objc_const: 0xd1f8
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2921
-  Symbols:   5682
-  CStrings:  1294
+  Functions: 2928
+  Symbols:   5688
+  CStrings:  1300
 
Symbols:
+ -[UARPSuperBinaryLayer3 processSuperBinaryPropertyList:]
+ _UARPLayer3DateAsString
+ _UARPLayer3DateTimeAsString
+ _UARPLayer3TimestampAsString
+ _kUARPCommonPayloadPLST
+ _kUARPCommonPayloadPMAP
+ _objc_msgSend$processSuperBinaryPropertyList:
- _objc_msgSend$date
CStrings:
+ "%02ld-%02ld-%02ld"
+ "%04ld-%02ld-%02ld"
+ "%s: Failed to instantiate UARPSuperBinaryPayloadLayer3 at index %lu for %@"
+ "%s: could not instantiate UARPSuperBinaryLayer3 for tag %@ on endpoint %@"
+ "%s: could not instantiate UARPSuperBinaryPayloadLayer3 for asset %@ on endpoint %@"
+ "%s: processSuperBinaryPropertyList: failed to process"
+ "-"
+ "-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackUnsolicitedDynamicAssetOffered:assetTag:]_block_invoke"
+ "PLST"
- "%s: Error creating payload at index %lu"
- "%s: Failed to create payload at index %lu"
- "yyyy-MM-dd-HH-mm-ss"
```
