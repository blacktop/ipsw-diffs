## libAppleTconUARPUpdater.dylib

> `/usr/lib/updaters/libAppleTconUARPUpdater.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-1587.0.27.0.0
-  __TEXT.__text: 0x70778
-  __TEXT.__objc_methlist: 0x6804
-  __TEXT.__cstring: 0x76ff
+1587.2.2.0.0
+  __TEXT.__text: 0x71424
+  __TEXT.__objc_methlist: 0x6894
+  __TEXT.__cstring: 0x7763
   __TEXT.__const: 0x110
-  __TEXT.__oslogstring: 0x3847
+  __TEXT.__oslogstring: 0x388a
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x1a70
+  __TEXT.__unwind_info: 0x1aa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xdc8
+  __DATA_CONST.__const: 0xdd0
   __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f70
+  __DATA_CONST.__objc_selrefs: 0x1fb0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0xd8
   __DATA_CONST.__got: 0x680
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x5520
-  __AUTH_CONST.__objc_const: 0xd1f8
+  __AUTH_CONST.__cfstring: 0x5580
+  __AUTH_CONST.__objc_const: 0xd2b8
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__auth_got: 0x3d8
   __AUTH.__objc_data: 0x36b0
-  __DATA.__objc_ivar: 0x8a4
+  __DATA.__objc_ivar: 0x8b4
   __DATA.__data: 0x305
   __DATA.__bss: 0x1180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2928
-  Symbols:   5688
-  CStrings:  1300
+  Functions: 2948
+  Symbols:   5718
+  CStrings:  1305
 
Symbols:
+ -[UARPComponentConfiguration productGroup]
+ -[UARPComponentConfiguration productNumber]
+ -[UARPComponentConfiguration setProductGroup:]
+ -[UARPComponentConfiguration setProductNumber:]
+ -[UARPEndpointConfiguration productGroup]
+ -[UARPEndpointConfiguration productNumber]
+ -[UARPEndpointConfiguration setProductGroup:]
+ -[UARPEndpointConfiguration setProductNumber:]
+ -[UARPEndpointLayer3 clearMatchingLayer2Context:]
+ -[UARPEndpointLayer3 configureEndpointLayer2Tags]
+ -[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackRequestAssetBuffer:]
+ -[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackReturnAssetBuffer:]
+ _OBJC_IVAR_$_UARPComponentConfiguration._productGroup
+ _OBJC_IVAR_$_UARPComponentConfiguration._productNumber
+ _OBJC_IVAR_$_UARPEndpointConfiguration._productGroup
+ _OBJC_IVAR_$_UARPEndpointConfiguration._productNumber
+ _UARPEndpointLayer3RequestAssetBuffer
+ _UARPEndpointLayer3ReturnAssetBuffer
+ _UARPLayer2RequestAssetBuffer
+ _UARPLayer2ReturnAssetBuffer
+ _dispatch_assert_queue$V2
+ _kUARPLayer3StringMetricsSubfolder
+ _objc_msgSend$clearMatchingLayer2Context:
+ _objc_msgSend$configureEndpointLayer2Tags
+ _objc_msgSend$layer2CallbackRequestAssetBuffer:
+ _objc_msgSend$layer2CallbackReturnAssetBuffer:
+ _objc_msgSend$productGroup
+ _objc_msgSend$productNumber
+ _objc_msgSend$setProductGroup:
+ _objc_msgSend$setProductNumber:
CStrings:
+ "%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@"
+ "%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@"
+ "%s: uncompressedLength (%u) exceeds decompressionBuffer size (%lu)"
+ "-[UARPEndpointLayer3 configureEndpointLayer2Tags]"
+ "Product Group"
+ "Product Number"
+ "metrics"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa31"
- "%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@"
- "%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x831"
```
