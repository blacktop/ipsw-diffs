## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2661.5.2.0.0
-  __TEXT.__text: 0x465390
+2661.6.2.0.0
+  __TEXT.__text: 0x465700
   __TEXT.__auth_stubs: 0x4120
   __TEXT.__objc_methlist: 0xb58
   __TEXT.__const: 0xb8a08
-  __TEXT.__gcc_except_tab: 0x1fa84
-  __TEXT.__cstring: 0x7c0de
+  __TEXT.__gcc_except_tab: 0x1fa8c
+  __TEXT.__cstring: 0x7c2d5
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x20
   __TEXT.__unwind_info: 0xd840

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 10CC4CB3-264C-3269-B6A2-DC7A2D7B2179
-  Functions: 13887
-  Symbols:   36723
-  CStrings:  14474
+  UUID: 8002DCD6-C871-3D74-81DF-DC9FB800922A
+  Functions: 13888
+  Symbols:   36725
+  CStrings:  14485
 
Symbols:
+ __ZN19AppleJPEGReadPlugin10initializeEP13IIODictionary.cold.10
+ ___block_descriptor_tmp.157
+ ___block_descriptor_tmp.161
+ ___block_descriptor_tmp.168
+ ___block_descriptor_tmp.169
+ ___block_descriptor_tmp.173
+ ___block_descriptor_tmp.180
+ ___block_literal_global.171
+ ___block_literal_global.182
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.159
- ___block_descriptor_tmp.164
- ___block_descriptor_tmp.167
- ___block_descriptor_tmp.171
- ___block_descriptor_tmp.178
- ___block_literal_global.169
- ___block_literal_global.180
Functions:
~ __ZN19IIOImageReadSession8getBytesEPvm : 96 -> 172
~ __ZN12IIOImageRead16getBytesAtOffsetEPvmm : 472 -> 464
~ __ZN19AppleJPEGReadPlugin10initializeEP13IIODictionary : 5924 -> 6072
~ __ZN13IIOReadPlugin19imageBlockSetCreateEP15CGImageProvider6CGSize6CGRectmPKP12CGImageBlockPv : 484 -> 572
~ __ZN19AppleJPEGReadPlugin20copyImageBlockSetImpEP7InfoRecP15CGImageProvider6CGRect6CGSizePK14__CFDictionary : 3944 -> 4012
~ __ZN14TIFFReadPlugin10initializeEP13IIODictionary : 2836 -> 2904
~ __ZN14IIO_Reader_PVR13getImageCountEP19IIOImageReadSessionP13IIODictionaryP19CGImageSourceStatusPj : 676 -> 728
~ __ZN13JP2ReadPlugin27checkContinousCodestreamBoxEP10IIOScannery : 224 -> 216
~ _IIOCreateMemoryString : 1108 -> 1112
~ __Z10AlphaBlendItElPK13vImage_BufferS2_S2_j : 176 -> 252
~ __Z10AlphaBlendIjElPK13vImage_BufferS2_S2_j : 152 -> 228
~ __ZN13PSDReadPlugin21decodeBlockSubsampledER20IIODecodeFrameParamsjj : 2352 -> 2388
~ _gtTileContig : 928 -> 996
~ _gtStripContig : 800 -> 796
~ _gtTileSeparate : 1344 -> 1420
~ __ZN19AppleJPEGReadPlugin10initializeEP13IIODictionary.cold.1 : 44 -> 64
~ __ZN19AppleJPEGReadPlugin10initializeEP13IIODictionary.cold.2 : 24 -> 44
~ __ZN19AppleJPEGReadPlugin10initializeEP13IIODictionary.cold.3 : 144 -> 24
+ __ZN19AppleJPEGReadPlugin10initializeEP13IIODictionary.cold.4
CStrings:
+ "%s %lld"
+ "*** ERROR: IIOImageReadSession::getBytes: count:%ld   offset:%ld   imgSize:%ld\n"
+ "*** ERROR: combination of samplesPerPixel(%d) and extraSamples(%d) is not supported\n"
+ "*** ERROR: failed to read %d bytes at offset %ld\n"
+ "*** ERROR: invalid rowBytes[%d] < width[%d]*bpc[%d]*4\n"
+ "*** ERROR: rect:{%g,%g,%g,%g} - invalid height\n"
+ "*** ERROR: rect:{%g,%g,%g,%g} - invalid width\n"
+ "*** ERROR: unexpected data '%02X%02X %02X%02X' at offset %ld\n"
+ "*** ERROR: unsupported bitsPerComponent[%d] for PHOTOMETRIC_YCBCR\n"
+ "*** invalid PVR file: Bits Per Pixel: %d\n"
+ "AlphaBlend"
+ "Invalid skew"
- "*** ERROR: samplesPerPixel(%d) and extraSamples(%d) don't match\n"

```
