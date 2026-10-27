## vImage

> `/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/vImage`

```diff

-650.0.1.0.0
-  __TEXT.__text: 0x39abc8
+650.40.4.0.0
+  __TEXT.__text: 0x39b128
   __TEXT.__delay_stubs: 0x780
   __TEXT.__delay_helper: 0x5a4
   __TEXT.__const: 0x9a9b0
-  __TEXT.__cstring: 0x6be6
+  __TEXT.__cstring: 0x6cdb
   __TEXT.__unwind_info: 0x2748
   __TEXT.__eh_frame: 0x412c
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libcompression.dylib
   Functions: 3468
   Symbols:   4416
-  CStrings:  404
+  CStrings:  406
 
Functions:
~ _ReduceToCoreFormats : 1468 -> 1564
~ _Deepmap2DecodeDefaultScratchBufferSize : 136 -> 196
~ _Deepmap2DecodeDefault : 1232 -> 1196
~ _Deepmap2DecodePalette : 672 -> 676
~ _DecodeImageDefaultScratchBufferSize : 80 -> 136
~ _vImageDeepmapDecodeStreamProcess : 1596 -> 1632
~ _DecodeImageLossless : 264 -> 332
~ _DecodeImageDefault : 1096 -> 1184
~ _DecodeImagePalette : 304 -> 328
~ ___vOverwriteChannelsWithScalar_ARGB8888_block_invoke : 636 -> 640
~ _ImagePaletteCreate : 1064 -> 1112
~ _vImageDeepmapEncodeCreateBuffer : 484 -> 516
~ _EncodeImageLossless : 280 -> 332
~ _EncodeImagePalette : 424 -> 448
~ _EncodeImageDefault : 1068 -> 1140
~ _EncodeImageWithMehtod : 684 -> 720
~ _vImageDeepmap2EncodeCreateBuffer : 484 -> 516
~ _vImageDeepmap2DecodeStreamProcess : 1476 -> 1508
~ _Deepmap2EncodeLossless : 388 -> 416
~ _Deepmap2DecodeDefaultRawBufferSize : 68 -> 136
~ _Deepmap2DecodeDefaultMaxRawBufferSize : 28 -> 100
~ _Deepmap2EncodeDefault : 1080 -> 1148
~ _Deepmap2BuildPalette : 1756 -> 1800
~ _Deepmap2EncodePalette : 616 -> 660
~ _ConvertIndexedToDirect : 1308 -> 1632
CStrings:
+ "650.40.4"
+ "kvImagePrintDiagnosticsToConsole: vImageConverter: indexed color table has more entries than srcFormat->bitsPerComponent can address."
+ "kvImagePrintDiagnosticsToConsole: vImageConverter: indexed destination color table has more than 256 entries."
- "650.0.1"
```
