## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

```diff

-621.2.1.10.3
-  __TEXT.__text: 0xa69430
-  __TEXT.__auth_stubs: 0x1490
+621.2.3.10.3
+  __TEXT.__text: 0xa6aa0c
+  __TEXT.__auth_stubs: 0x1560
   __TEXT.__objc_methlist: 0x14e4
   __TEXT.__const: 0xb3a98
-  __TEXT.__cstring: 0x4b952
-  __TEXT.__gcc_except_tab: 0x181c
-  __TEXT.__unwind_info: 0x35c0
+  __TEXT.__cstring: 0x4bca1
+  __TEXT.__gcc_except_tab: 0x1864
+  __TEXT.__unwind_info: 0x35f8
   __TEXT.__eh_frame: 0x1118
   __TEXT.__objc_classname: 0x45a
   __TEXT.__objc_methname: 0x27ee
   __TEXT.__objc_methtype: 0x41fe
   __TEXT.__objc_stubs: 0x19e0
-  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__const: 0x15f20
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x890
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0xa58
+  __AUTH_CONST.__auth_got: 0xac0
   __AUTH_CONST.__auth_ptr: 0x368
-  __AUTH_CONST.__const: 0x1f9e0
-  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__const: 0x1fb80
+  __AUTH_CONST.__cfstring: 0x380
   __AUTH_CONST.__objc_const: 0x35d8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 17993
-  Symbols:   18666
-  CStrings:  9524
+  Functions: 18021
+  Symbols:   18712
+  CStrings:  9538
 
Symbols:
+ _CFArrayAppendValue
+ _CFArrayCreateMutable
+ _CFDataGetTypeID
+ _CFDictionaryGetTypeID
+ _CFGetTypeID
+ _CMBaseObjectGetDerivedStorage
+ _CMDerivedObjectCreate
+ _CMFormatDescriptionGetExtensions
+ _VTDecoderSessionEmitDecodedFrame
+ _VTDecoderSessionGetPixelBufferPool
+ _VTDecoderSessionSetPixelBufferAttributes
+ _VTRegisterVideoDecoder
+ _VTVideoDecoderGetClassID
+ __ZN6webrtc24registerWebKitVP9DecoderEv
+ _kCFTypeArrayCallBacks
+ _kCVPixelBufferExtendedPixelsBottomKey
+ _kCVPixelBufferExtendedPixelsLeftKey
+ _kCVPixelBufferExtendedPixelsRightKey
+ _kCVPixelBufferExtendedPixelsTopKey
CStrings:
+ ", vtError "
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/webkit_sdk/WebKit/WebKitDecoderReceiver.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/webkit_sdk/WebKit/WebKitVP9Decoder.cpp"
+ "Failed to allocate cpi->cyclic_refresh->map"
+ "VP9 decoder creation failed, CMDerivedObjectCreate failed with error "
+ "VP9 decoder creation failed, no decoder output"
+ "VP9 decoder: CMBlockBufferGetDataPointer failed with error "
+ "VP9 decoder: decoder failed with error "
+ "VP9 decoder: failed to create contiguous block buffer with error "
+ "VP9 decoder: failed to get data buffer"
+ "VP9 decoder: failed to get decoder from instance while decoding"
+ "VP9 decoder: failed to get decoder from instance while starting"
+ "VP9 decoder: invalidation failed as instance has no decoder"
+ "WebKit VP9 decoder"

```
