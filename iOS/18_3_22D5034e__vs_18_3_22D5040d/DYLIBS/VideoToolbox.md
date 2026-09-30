## VideoToolbox

> `/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`

```diff

-3200.4.2.0.0
-  __TEXT.__text: 0x42eca4
+3200.5.1.11.1
+  __TEXT.__text: 0x42f544
   __TEXT.__auth_stubs: 0x3640
-  __TEXT.__cstring: 0x9743
-  __TEXT.__const: 0x40b8
-  __TEXT.__oslogstring: 0xcf0
+  __TEXT.__cstring: 0x97f1
+  __TEXT.__const: 0x40c8
+  __TEXT.__oslogstring: 0x1108
   __TEXT.__dlopen_cstrs: 0x4f
   __TEXT.__gcc_except_tab: 0x5c
   __TEXT.__unwind_info: 0x4dc0

   - /usr/lib/libobjc.A.dylib
   Functions: 6310
   Symbols:   8442
-  CStrings:  1584
+  CStrings:  1592
 
CStrings:
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %{public}@ decoderSession %p decompressionSession %{public}@ ) DecodeFrame failed with error %d, frame %p: sbuf PTS %1.3f, %zd bytes, decodeFlags 0x%x, frameOptions %@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %{public}@ tileDecoderSession %p tileDecompressionSession %{public}@) DecodeTile failed with error %d, tile %p: sbuf PTS %1.3f, %zd bytes, tileCropOffset [%d, %d], tileCropDimensions %d x %d, pixelBuffer %p, offsetWithinPixelBuffer [%d, %d] decodeFlags 0x%x"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %{public}@, encoderSession %p, compressionSession %{public}@) EncodeFrame failed with error %d, frame %p: pixelBuffer %p PTS %1.3f duration %1.3f frameProperties %{public}@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %{public}@, tileEncoderSession %p, tileCompressionSession %{public}@) EncodeTile failed with error %d, tile %lld pixelBuffer %p pixelBufferUUID %{public}@ tileOffset (%d, %d) tileAperture %d x %d tileProperties %{public}@ encodeFlags 0x%x -> %d"
+ "ParavirtualizedVideoDecoder_DecodeFrameWithOptions"
+ "ParavirtualizedVideoDecoder_DecodeTile"
+ "ParavirtualizedVideoEncoder_EncodeFrame"
+ "ParavirtualizedVideoEncoder_EncodeTile"
+ "description=CoreMedia_VideoToolbox-3200.5.1.11.1"
- "description=CoreMedia_VideoToolbox-3200.4.2"

```
