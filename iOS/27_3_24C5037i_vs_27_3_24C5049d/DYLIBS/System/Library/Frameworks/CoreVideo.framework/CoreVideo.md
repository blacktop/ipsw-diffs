## CoreVideo

> `/System/Library/Frameworks/CoreVideo.framework/CoreVideo`

```diff

-780.2.0.0.0
-  __TEXT.__text: 0x6d374
+780.2.11.1.0
+  __TEXT.__text: 0x6d994
   __TEXT.__const: 0x5ca8
-  __TEXT.__cstring: 0xcc2c
+  __TEXT.__cstring: 0xd02c
   __TEXT.__oslogstring: 0x2e3
   __TEXT.__objc_databytes: 0x493
   __TEXT.__gcc_except_tab: 0x64

   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 3635
   Symbols:   8152
-  CStrings:  1074
+  CStrings:  1080
 
Functions:
~ _CVPixelBufferCreateWithBytes : 1468 -> 1792
~ _CVPixelBufferCreateWithPlanarBytes : 1984 -> 2900
~ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtF9CoreVideo33CVImageStereoDisplayMaskRectangleV9EdgePointV_Tg5 : 248 -> 272
~ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFs6UInt16V_Tg5 : 244 -> 256
~ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtF9CoreVideo24CVPixelFormatDescriptionV_Tg5 : 284 -> 316
~ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtF9CoreVideo24CVPixelFormatDescriptionV11PixelLayoutV_Tg5 : 284 -> 316
~ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtF9CoreVideo17TypedCFDictionaryV_Tg5 : 256 -> 280
~ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtF9CoreVideo07CVPixelC15PlanePropertiesV10properties_Sw5bytest_Tg5 : 264 -> 300
~ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFs6UInt32V_Tg5 : 248 -> 272
~ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtF9CoreVideo17CVPixelFormatTypeV_Tg5 : 248 -> 272
~ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFSS_Tg5 : 256 -> 280
~ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFSS_9CoreVideo20CVAttachmentRawValueVt_Tg5 : 296 -> 320
~ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtF9CoreVideo07CVPixelC15PlanePropertiesV_Tg5 : 264 -> 300
~ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtF9CoreVideo07CVPixelC15PlanePropertiesV10properties_SW5bytest_Tg5 : 264 -> 300
CStrings:
+ "CVPixelBufferCreateWithPlanarBytes returning err %d because the planes span %u bytes which does not fit inside dataSize %u. Width %u, Height %u, planeWidth[0] %u, planeHeight[0] %u, planeBytesPerRow[0] %u, planeWidth[1] %u, planeHeight[1] %u, planeBytesPerRow[1] %u, pixel format %c%c%c%c"
+ "WARNING: CVPixelBufferCreateWithBytes bytesPerRow %u is too small for width %u (bytesPerElement %u, elementsPerBlock %u)."
+ "WARNING: CVPixelBufferCreateWithBytes pixel format %c%c%c%c is planar (%ld planes); use CVPixelBufferCreateWithPlanarBytes()."
+ "WARNING: CVPixelBufferCreateWithPlanarBytes planeBaseAddress %p + plane size %d overflows the address space for planeIndex %d."
+ "WARNING: CVPixelBufferCreateWithPlanarBytes planeHeight %d * planeBytesPerRow %d overflows for planeIndex %d."
+ "WARNING: CVPixelBufferCreateWithPlanarBytes planes %u do not fit inside dataPtr %p, dataPtr+dataSize (%u bytes)."
+ "WARNING: CVPixelBufferCreateWithPlanarBytes planes span %u bytes which does not fit inside dataSize %u. Width %u, Height %u, planeWidth[0] %u, planeHeight[0] %u, planeBytesPerRow[0] %u, planeWidth[1] %u, planeHeight[1] %u, planeBytesPerRow[1] %u, pixel format %c%c%c%c"
- "CVPixelBufferCreateWithPlanarBytes returning err %d because the planes span %d bytes which does not fit inside dataSize %d"
```
