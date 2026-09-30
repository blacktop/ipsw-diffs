## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.3.3.0.0
-  __TEXT.__text: 0x4669c0
+2784.3.4.1.0
+  __TEXT.__text: 0x46611c
   __TEXT.__auth_stubs: 0x4250
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x31330
-  __TEXT.__gcc_except_tab: 0x2679c
-  __TEXT.__cstring: 0x9d2a7
+  __TEXT.__gcc_except_tab: 0x26758
+  __TEXT.__cstring: 0x9d27a
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xebf0
+  __TEXT.__unwind_info: 0xebb8
   __TEXT.__eh_frame: 0x358
   __TEXT.__objc_classname: 0xe0
   __TEXT.__objc_methname: 0x2e13

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: BDE1A628-AF8F-371F-9FEB-25F141F18F1C
-  Functions: 14921
-  Symbols:   45271
-  CStrings:  24865
+  UUID: 3D835956-CDBA-321C-AD2D-8E4D4892224B
+  Functions: 14910
+  Symbols:   45246
+  CStrings:  24863
 
Symbols:
+ __ZN14WebPReadPlugin18decodeAnimatedWebPEP8WebPDataPhm
- _WebPAnimDecoderRestoreCanvas
- _WebPAnimDecoderSkipFrame
- __ZL21releaseGlobalWebPInfoPv
- __ZN14GlobalWebPInfo14setFrameBufferEPhmjjj
- __ZN14GlobalWebPInfo15copyFrameBufferEPPhPmPj
- __ZN14GlobalWebPInfo16clearFrameBufferEv
- __ZN14GlobalWebPInfo19hasValidFrameBufferEj
- __ZN14GlobalWebPInfoD2Ev
- __ZN14WebPReadPlugin24copyDecodedFrameToBufferEPhS0_jjji
- __ZN14WebPReadPlugin27decodeAnimatedWebPOptimizedEP8WebPDataPhm
- __ZNK14GlobalWebPInfo19getCachedFrameIndexEv
CStrings:
+ "*** Error: MergeLayers was called with %d frame channels\n"
+ "decodeAnimatedWebP"
- "*** ERROR: invalid canvas size %dx%d\n"
- "*** ERROR: setFrameBuffer - bailing out\n"
- "decodeAnimatedWebPOptimized"
- "setFrameBuffer"

```
