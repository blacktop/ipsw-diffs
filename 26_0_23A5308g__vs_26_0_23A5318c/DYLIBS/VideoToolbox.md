## VideoToolbox

> `/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`

```diff

-3255.77.2.11.2
-  __TEXT.__text: 0x4f52a8
+3255.79.1.5.0
+  __TEXT.__text: 0x4f584c
   __TEXT.__auth_stubs: 0x38e0
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0xe54
   __TEXT.__const: 0x4140
-  __TEXT.__cstring: 0xd72d
-  __TEXT.__oslogstring: 0x4e2f
+  __TEXT.__cstring: 0xd72a
+  __TEXT.__oslogstring: 0x4e93
   __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__dlopen_cstrs: 0x9b
   __TEXT.__unwind_info: 0x5880

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4031ED74-4E4A-30D0-84FB-C83F909530FD
-  Functions: 8417
-  Symbols:   20336
+  UUID: 4997D53A-9CC3-3ECC-9364-61876EDAF6BC
+  Functions: 8422
+  Symbols:   20348
   CStrings:  3845
 
CStrings:
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %{public}@ decoderSession %p decompressionSession %{public}@ ) DecodeFrame failed with error %d, frame %p: codecType %c%c%c%c, sbuf PTS %1.3f, %zd bytes, decodeFlags 0x%x, frameOptions %{public}@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %{public}@, encoderSession %p, compressionSession %{public}@) EncodeFrame for codecType %c%c%c%c failed with error %d, frame %d: pixelBuffer %p PTS %1.3f duration %1.3f frameProperties %{public}@"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) codecType %c%c%c%c VTVideoDecoderDecodeFrame or VTVideoDecoderDecodeFrameWithOptions failed with error %d, frame %d, flags 0x%x"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: codecType %c%c%c%c guestProtocolVersion %u hostProtocolVersion %u, guestInfo %{public}@, hostBuildVersion %{public}@"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: codecType %c%c%c%c guestProtocolVersion %u hostProtocolVersion %u, guestInfo %{public}@, hostBuildVersion %{public}@"
+ "description=CoreMedia_VideoToolbox-3255.79.1.5"
- "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %{public}@ decoderSession %p decompressionSession %{public}@ ) DecodeFrame failed with error %d, frame %p: sbuf PTS %1.3f, %zd bytes, decodeFlags 0x%x, frameOptions %{public}@"
- "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %{public}@, encoderSession %p, compressionSession %{public}@) EncodeFrame failed with error %d, frame %d: pixelBuffer %p PTS %1.3f duration %1.3f frameProperties %{public}@"
- "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderDecodeFrame or VTVideoDecoderDecodeFrameWithOptions failed with error %d, frame %d, flags 0x%x"
- "<<<< VTParavirtualizationHostDecoder >>>> %s: guestProtocolVersion %u hostProtocolVersion %u, guestInfo %{public}@, hostBuildVersion %{public}@"
- "<<<< VTParavirtualizationHostEncoder >>>> %s: guestProtocolVersion %u hostProtocolVersion %u, guestInfo %{public}@, hostBuildVersion %{public}@"
- "description=CoreMedia_VideoToolbox-3255.77.2.11.2"

```
