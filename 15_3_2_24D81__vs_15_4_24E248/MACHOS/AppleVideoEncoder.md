## AppleVideoEncoder

> `/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/Contents/MacOS/AppleVideoEncoder`

```diff

-803.54.2.0.0
-  __TEXT.__text: 0xe2eb4
-  __TEXT.__auth_stubs: 0xf20
+803.63.1.0.0
+  __TEXT.__text: 0xe20b4
+  __TEXT.__auth_stubs: 0xf50
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x5a893
-  __TEXT.__const: 0x15e18
-  __TEXT.__gcc_except_tab: 0x5cc
+  __TEXT.__cstring: 0x5abad
+  __TEXT.__const: 0x15de8
+  __TEXT.__gcc_except_tab: 0x604
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x7a8
-  __DATA_CONST.__auth_got: 0x7a0
-  __DATA_CONST.__got: 0x8f8
+  __TEXT.__unwind_info: 0x738
+  __DATA_CONST.__auth_got: 0x7b8
+  __DATA_CONST.__got: 0x900
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x2eb8
-  __DATA_CONST.__cfstring: 0x2580
+  __DATA_CONST.__cfstring: 0x2560
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0xb8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5FD2B4B0-3DBE-3A97-BF14-18F1D238F17F
-  Functions: 694
-  Symbols:   544
-  CStrings:  6033
+  UUID: 807AA43C-6933-3646-909F-56817DB2DED9
+  Functions: 669
+  Symbols:   548
+  CStrings:  6047
 
Symbols:
+ _VTPixelTransferSessionCreate
+ _VTPixelTransferSessionInvalidate
+ _VTPixelTransferSessionTransferImage
+ _kVTCompressionPropertyKey_NumberOfTemporalLayers
CStrings:
+ "%lld %d AVE %s: %s:%d %s | Failed to create image transfer session, err = %d"
+ "%lld %d AVE %s: %s:%d %s | Failed to create image transfer session, err = %d\n"
+ "%lld %d AVE %s: %s:%d %s | Failed to transfer image, err = %d"
+ "%lld %d AVE %s: %s:%d %s | Failed to transfer image, err = %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d %d"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to transfer a pixel buffer to another format %p (0x%X -> 0x%X) %d."
+ "%lld %d AVE %s: %s:%d %s | failed to transfer a pixel buffer to another format %p (0x%X -> 0x%X) %d.\n"
+ "%lld %d AVE %s: %s:%d %s | pixelBufferIn is NULL"
+ "%lld %d AVE %s: %s:%d %s | pixelBufferIn is NULL\n"
+ "%lld %d AVE %s: %s:%d %s | pixelBufferOut is NULL"
+ "%lld %d AVE %s: %s:%d %s | pixelBufferOut is NULL\n"
+ "%lld %d AVE %s: FIG: asked for kVTCompressionPropertyKey_NumberOfTemporalLayers return %d"
+ "%lld %d AVE %s: FIG: asked for kVTCompressionPropertyKey_NumberOfTemporalLayers return %d\n"
+ "%lld %d AVE %s: FIG: asked for kVTCompressionPropertyKey_NumberOfTemporalLayers return %u"
+ "%lld %d AVE %s: FIG: asked for kVTCompressionPropertyKey_NumberOfTemporalLayers return %u\n"
+ "%lld %d AVE %s: FIG: received kVTCompressionPropertyKey_NumberOfTemporalLayers"
+ "%lld %d AVE %s: FIG: received kVTCompressionPropertyKey_NumberOfTemporalLayers\n"
+ "21:25:21"
+ "21:25:23"
+ "803.63.1"
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Number, kVTCompressionPropertyKey_NumberOfTemporalLayers, false)"
+ "AVE_ImageBuf_Transfer"
+ "AVE_ImageTransfer"
+ "Mar 19 2025"
+ "err == kCVReturnSuccess"
+ "pixelBufferIn != __null"
+ "pixelBufferOut != __null"
+ "psList != ((void*)0)"
+ "psList->psNext != ((void*)0)"
+ "psList->psPrev != ((void*)0)"
+ "psNewNode != ((void*)0)"
+ "psNode != ((void*)0)"
+ "psNode->psNext != ((void*)0)"
+ "psNode->psPrev != ((void*)0)"
- "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d %d%d"
- "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d %d%d\n"
- "%lld %d AVE %s: FIG: asked for AVE_kVTCompressionPropertyKey_NumberOfTemporalLayers return %d"
- "%lld %d AVE %s: FIG: asked for AVE_kVTCompressionPropertyKey_NumberOfTemporalLayers return %d\n"
- "%lld %d AVE %s: FIG: asked for AVE_kVTCompressionPropertyKey_NumberOfTemporalLayers return %u"
- "%lld %d AVE %s: FIG: asked for AVE_kVTCompressionPropertyKey_NumberOfTemporalLayers return %u\n"
- "%lld %d AVE %s: FIG: received ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"NumberOfTemporalLayers\" \"\"))"
- "%lld %d AVE %s: FIG: received ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"NumberOfTemporalLayers\" \"\"))\n"
- "20:50:10"
- "20:50:13"
- "803.54.2"
- "Jan  2 2025"
- "NumberOfTemporalLayers"
- "psList != ((void *)0)"
- "psList->psNext != ((void *)0)"
- "psList->psPrev != ((void *)0)"
- "psNewNode != ((void *)0)"
- "psNode != ((void *)0)"
- "psNode->psNext != ((void *)0)"
- "psNode->psPrev != ((void *)0)"

```
