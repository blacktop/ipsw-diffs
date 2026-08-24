## UVCFrameProcessor

> `/System/Library/PrivateFrameworks/UVCFrameProcessor.framework/Versions/A/UVCFrameProcessor`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-520.0.0.0.0
-  __TEXT.__text: 0x9330
+520.21.1.0.0
+  __TEXT.__text: 0x9670
   __TEXT.__objc_methlist: 0x444
-  __TEXT.__const: 0xa0
-  __TEXT.__oslogstring: 0x1082
+  __TEXT.__const: 0xa8
+  __TEXT.__oslogstring: 0x1202
   __TEXT.__cstring: 0x57d
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__unwind_info: 0x228
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b0
+  __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__got: 0x128
   __AUTH_CONST.__const: 0x110
   __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__objc_const: 0xd58
+  __AUTH_CONST.__objc_const: 0xdb8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0xd8
+  __DATA.__objc_ivar: 0xe4
   __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia

   - /System/Library/PrivateFrameworks/UVCFamily.framework/Versions/A/UVCFamily
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 170
-  Symbols:   436
-  CStrings:  148
+  Functions: 172
+  Symbols:   448
+  CStrings:  151
 
Symbols:
+ -[UVCNativeFrame appendDataToBlockBuffer:bytesPerRowAllignment:compressed:error:]
+ OBJC_IVAR_$_UVCFrameProcessorNative._currentFrameReceivedBytes
+ OBJC_IVAR_$_UVCFrameProcessorNative._isCompressedBitstream
+ OBJC_IVAR_$_UVCFrameProcessorNative._sourceBytesPerRowFromUVCData
+ _CVPixelFormatDescriptionGetDescriptionWithPixelFormatType
+ _UVCFrameProcessorSourceBytesPerRowForFormat
+ _kCVPixelFormatBitsPerBlock
+ _kCVPixelFormatBlockWidth
+ _kCVPixelFormatPlanes
+ _kUVCStreamFormatGUIDH264
+ _kUVCStreamFormatGUIDH265
+ _kUVCStreamFormatGUIDMJPEG
+ _objc_msgSend$appendDataToBlockBuffer:bytesPerRowAllignment:compressed:error:
+ _objc_msgSend$formatGUID
+ _objc_msgSend$intValue
+ _objc_msgSend$isEqualToString:
- -[UVCNativeFrame appendDataToBlockBuffer:bytesPerRowAllignment:error:]
- _CVPixelBufferCreate
- _CVPixelBufferIsPlanar
- _objc_msgSend$appendDataToBlockBuffer:bytesPerRowAllignment:error:
CStrings:
+ "%@ Create Native Processor for Format %@ - alignedBytesPerRow: %lu sourceBytesPerRow: %lu compressed: %d"
+ "%@ Frame received total bytes: %lu (sourceBytesPerRow:%lu alignedBytesPerRow:%lu) previousFID:%u"
+ "%@ Plane stride mismatch: plane_0=%lu plane_%lu=%lu — non-aligned copy assumes uniform stride, failing frame"
+ "%@ non-aligned append overflow (dropping frame): usedDataSize:%lu space:%lu data.length:%lu totalDataSize:%lu expectedBytesPerRow:%lu actualBytesPerRow:%lu"
+ "Unable to determine base row bytes for format"
+ "\xf0r"
- "%@ Create Native Processor for Format %@ - alignedBytesPerRow: %lu"
- "Failed to create CVPixelBuffer to determine if it is planar: %d"
- "\xf0B"
```
