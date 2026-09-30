## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2639.0.0.0.0
-  __TEXT.__text: 0x3f8300
-  __TEXT.__auth_stubs: 0x3f80
-  __TEXT.__objc_methlist: 0x928
-  __TEXT.__gcc_except_tab: 0x1eee4
-  __TEXT.__const: 0x31418
-  __TEXT.__cstring: 0x79386
+2644.0.0.0.0
+  __TEXT.__text: 0x3fb6e8
+  __TEXT.__auth_stubs: 0x3fd0
+  __TEXT.__objc_methlist: 0x938
+  __TEXT.__const: 0x314b8
+  __TEXT.__gcc_except_tab: 0x1f178
+  __TEXT.__cstring: 0x79ace
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xd158
+  __TEXT.__unwind_info: 0xd200
   __TEXT.__eh_frame: 0x390
   __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x290a
-  __TEXT.__objc_methtype: 0x1c6f
-  __TEXT.__objc_stubs: 0x21e0
-  __DATA_CONST.__got: 0x5b8
+  __TEXT.__objc_methname: 0x29f2
+  __TEXT.__objc_methtype: 0x1eec
+  __TEXT.__objc_stubs: 0x2260
+  __DATA_CONST.__got: 0x5c8
   __DATA_CONST.__const: 0xf4b0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x918
+  __DATA_CONST.__objc_selrefs: 0x938
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x1fd8
+  __AUTH_CONST.__auth_got: 0x2000
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x3c978
-  __AUTH_CONST.__cfstring: 0xd920
+  __AUTH_CONST.__const: 0x3caf8
+  __AUTH_CONST.__cfstring: 0xd9e0
   __AUTH_CONST.__objc_const: 0x1248
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x10

   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x2bb8
   __DATA.__bss: 0x5340
-  __DATA.__common: 0x1ee8
+  __DATA.__common: 0x1f00
   __DATA_DIRTY.__data: 0x170
   __DATA_DIRTY.__crash_info: 0x40
   __DATA_DIRTY.__common: 0xd03

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13069
-  Symbols:   15437
-  CStrings:  12490
+  Functions: 13097
+  Symbols:   15472
+  CStrings:  12533
 
Symbols:
+ _CGImageGetHDRPixelBufferHeadroom
+ _kCGRWTMSourceReferenceWhite
+ _CGImageProviderSetContentHeadroom
+ _CGColorSpaceCreateCopyWithStandardRange
+ _CGColorSpaceCreateExtended
+ _CGContextSetEDRTargetHeadroom
+ _kCGRWTMSourcePeak
+ _cbrtf
CStrings:
+ "imageSourceCanBeUsedForJPEGResize"
+ "setHeight:"
+ "r^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}16@0:8"
+ "cubeSize"
+ "B72@0:8^i16^@24^32^@40^S48^B56^{__CVBuffer=}64"
+ "Tr^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}},R,N"
+ "getInputPixelRange:forPixelType:componentRange:bitDepth:isFloat:"
+ "getOutputPixelRange:forPixelType:componentRange:bitDepth:isFloat:"
+ "Already have post color transform TRC stage!"
+ "addICNSInfo"
+ "ContentColorVolume"
+ "RGBA32Float"
+ "Tr^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}},R,N"
+ "HDRImageConverter_SIMD.mm"
+ "3D-LUT (grid=%!f(MISSING))"
+ "*** 12-bit JPEG --> switching to HEIC decoder\n"
+ "convertBlockSetToSDR"
+ "B48@0:8^{__CVBuffer=}16r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}}24^{__CVBuffer=}32r^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}40"
+ "B32@0:8^f16^{CGImageMetadata=}24"
+ "B28@0:8^{?=I{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}}{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}}16f24"
+ "*** ERROR: CGImagePixelDataProviderCreate is called with NULL-image\n"
+ " MAT(pre):%!@(MISSING)"
+ "f24@0:8f16f20"
+ "☀️  %!s(MISSING) - updating image headroom: %!g(MISSING)\n"
+ "❌  failed to load 'kCVImageBufferTransferFunction_SMPTE_ST_2084_PQ' "
+ "☀️ Requested headroom (%!f(MISSING)) is less than FlexGTC headroom (%!f(MISSING)), dropping FlexGTC info"
+ "B96@0:8^{__CVBuffer=}16r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}}24r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}}32^{__CVBuffer=}40r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}48r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}56^{__CVBuffer=}64r^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}72^{__CVBuffer=}80r^{?={?={?=i{?=}}{?={?=[3]}B}B}{?=i{?=}{?=[3]}}}88"
+ "☀️  %!s(MISSING) - headroom from makerNote: _meteorHeadroom: %!g(MISSING)   _meteorPlusHeadroom:%!g(MISSING)\n"
+ "B28@0:8^{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}16f24"
+ "*** ERROR: read error requested %!l(MISSING)d bytes - got %!d(MISSING)\n"
+ "*** 🔄 ImageIO: plugin changed from '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)' to '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)'    '%!s(MISSING)%!s(MISSING)'\n"
+ "B28@0:8^{?=I{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}{?={?={?=i{?=}}{?={?=[3]}B}B}{?=i{?=}{?=[3]}}}}16f24"
+ "kCVImageBufferTransferFunction_SMPTE_ST_2084_PQ"
+ "HDRImageConverter_Metal.mm"
+ "❌  failed to load 'kCVImageBufferAmbientViewingEnvironmentKey' "
+ "⭕️ ImageIO: saving HEIF (%!d(MISSING)x%!d(MISSING)) with '%!s(MISSING)'\n"
+ "B60@0:8^{?=i{?=ffffffff}^v}16^{?={?=[3]}B}24^{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}32^{CGColorSpace=}40f48f52i56"
+ "B64@0:8^{__CVBuffer=}16r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}}24^{__CVBuffer=}32r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}40^{__CVBuffer=}48r^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}56"
+ "*** NOTE: '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)' requested pixelformat: '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)' -- got: '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)'\n"
+ "B28@0:8^{?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?=i{?=ffffffff}^v}}16f24"
+ "☀️  %!s(MISSING) - using image with headroom: %!g(MISSING)\n"
+ "B52@0:8^{?=i{?=ffffffff}^v}16^{?={?=[3]}B}24^{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}32f40^{CGColorSpace=}44"
+ "☀️  %!s(MISSING) - not setting image headroom: %!g(MISSING) for SDR [colorspace: '%!s(MISSING)']\n"
+ "B28@0:8^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}16f24"
+ "^{?=I{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}}{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}}16@0:8"
+ "Tf,N,V_headroom"
+ "☀️  %!s(MISSING) - updating image headroom: %!g(MISSING) [colorspace: '%!s(MISSING)']\n"
+ "+[HDRImage getPixelType:YCCMatrixString:chromaSubsampling:componentRange:bitDepth:isFloat:forBuffer:]"
+ "kCVImageBufferTransferFunction_ITU_R_2100_HLG"
+ "Invalid grid size: %!l(MISSING)u for cube data size: %!l(MISSING)u"
+ "r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}}16@0:8"
+ "☀️  %!s(MISSING) - adding image with headroom: %!g(MISSING)\n"
+ "☀️  %!s(MISSING) - _gainMapHeadroom: %!g(MISSING)\n"
+ "HDR"
+ "B32@0:8^f16@24"
+ "{?=\"flags\"I\"image\"{?=\"color\"{?=\"rgb\"{?=\"matrix\"{?=\"columns\"[3]}\"identity\"B}\"tm\"{?=\"type\"i\"params\"{?=\"a\"f\"b\"f\"c\"f\"d\"f\"e\"f\"f\"f\"g\"f\"gamma\"f\"luma\"}\"lut\"^v\"mat\"{?=\"matrix\"{?=\"columns\"[3]}\"identity\"B}\"trc\"{?=\"type\"i\"params\"{?=\"a\"f\"b\"f\"c\"f\"d\"f\"e\"f\"f\"f\"g\"f\"gamma\"f\"luma\"}\"lut\"^v}}\"trc\"{?=\"type\"i\"params\"{?=\"a\"f\"b\"f\"c\"f\"d\"f\"e\"f\"f\"f\"g\"f\"gamma\"f\"luma\"}\"lut\"^v}}\"pixel\"{?=\"type\"i\"range\"{?=\"scale\"\"offset\"}\"yccMatrix\"{?=\"columns\"[3]}\"subsampling\"}}\"gainMap\"{?=\"gain\"{?=\"gm\"{?=\"type\"i\"params\"{?=\"gamma\"\"a\"\"b\"\"c\"\"d\"\"scale\"}}\"color\"{?=\"matrix\"{?=\"columns\"[3]}\"identity\"B}\"clip\"\"luma\"\"isLuma\"B}\"pixel\"{?=\"type\"i\"range\"{?=\"scale\"\"offset\"}\"yccMatrix\"{?=\"columns\"[3]}\"subsampling\"}}}"
+ "v64@0:8r^{?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?=i{?=ffffffff}^v}}16@24Q32@40@48Q56"
+ "B64@0:8^{?=[32[32I]]}1624^{__CVBuffer=}32r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}}40^{__CVBuffer=}48r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}56"
+ "T^{?=I{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}{?={?={?=i{?=}}{?={?=[3]}B}B}{?=i{?=}{?=[3]}}}},R,N"
+ "*** ERROR: IIOImageSource::updateThumbnailInfo '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)' did not get image dimensions (%!d(MISSING) x %!d(MISSING))\n"
+ "getPixelType:YCCMatrixString:chromaSubsampling:componentRange:bitDepth:isFloat:forBuffer:"
+ "❌  failed to load 'kCVImageBufferTransferFunction_ITU_R_2100_HLG' "
+ "ImageIO: imageSourceCanBeUsedForJPEGResize: <CGImageSourceRef:%!p(MISSING)> <CGImageReadRef:%!p(MISSING)>\n"
+ "^{?=I{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}{?={?={?=i{?=}}{?={?=[3]}B}B}{?=i{?=}{?=[3]}}}}16@0:8"
+ "B72@0:8^{__CVBuffer=}16r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}}24r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}}32^{__CVBuffer=}40r^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}48^{__CVBuffer=}56r^{?={?={?=i{?=}}{?={?=[3]}B}B}{?=i{?=}{?=[3]}}}64"
+ "{?=\"flags\"I\"image\"{?=\"pixel\"{?=\"type\"i\"range\"{?=\"scale\"\"offset\"}\"yccMatrix\"{?=\"columns\"[3]}\"affineTransform\"{?=\"columns\"[3]}}\"color\"{?=\"trc\"{?=\"type\"i\"params\"{?=\"a\"f\"b\"f\"c\"f\"d\"f\"e\"f\"f\"f\"g\"f\"gamma\"f\"luma\"}\"lut\"^v}\"tm\"{?=\"type\"i\"params\"{?=\"a\"f\"b\"f\"c\"f\"d\"f\"e\"f\"f\"f\"g\"f\"gamma\"f\"luma\"}\"lut\"^v\"mat\"{?=\"matrix\"{?=\"columns\"[3]}\"identity\"B}\"trc\"{?=\"type\"i\"params\"{?=\"a\"f\"b\"f\"c\"f\"d\"f\"e\"f\"f\"f\"g\"f\"gamma\"f\"luma\"}\"lut\"^v}}\"rgb\"{?=\"matrix\"{?=\"columns\"[3]}\"identity\"B}}}\"gainMap\"{?=\"pixel\"{?=\"type\"i\"range\"{?=\"scale\"\"offset\"}\"yccMatrix\"{?=\"columns\"[3]}\"affineTransform\"{?=\"columns\"[3]}}\"gain\"{?=\"gm\"{?=\"type\"i\"params\"{?=\"gamma\"\"a\"\"b\"\"c\"\"d\"\"scale\"}}\"color\"{?=\"matrix\"{?=\"columns\"[3]}\"identity\"B}}}}"
+ "replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:"
+ "*** ERROR: unexpected bitdepth: %!d(MISSING)\n"
+ "kCVImageBufferAmbientViewingEnvironmentKey"
+ "☀️  %!s(MISSING) - updating thumbnail headroom: %!g(MISSING)\n"
+ "^{CGImageMetadata=}20@0:8f16"
+ "B28@0:8^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}}16f24"
+ "B44@0:8^{?=}16i24@28S36B40"
+ "*** ERROR: CopyImageBlockSetWithOptions '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)' returned NULL\n"
+ "*** ERROR: CGImagePixelDataProviderCreate is called with NULL-dstFormat-colorspace\n"
+ "*** ERROR: invalid image source: <CGImageSourceRef:%!p(MISSING)>  <CGImageReadRef:%!p(MISSING)>"
+ "*** ERROR: duplicate icnsOSType? '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)' already exists\n"
+ "T^{?=I{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}}{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}},R,N"
+ "@28@0:8f16@20"
+ "getColorTRC:matrix:toneMapping:fromSourceSpace:headroom:toEDR:toneMappingMode:"
+ "setDepth:"
+ "B64@0:8^{?=i{?=ffffffff}^v}16^{?={?=[3]}B}24^{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}32^{CGColorSpace=}40^{CGColorSpace=}48@56"
+ "*** ERROR: unhandled componentType '%!d(MISSING)'\n"
+ "☀️  %!s(MISSING) - failed to update image headroom: %!g(MISSING)  [colorspace: '%!s(MISSING)']\n"
+ "SDR"
+ " TRC(post):%!@(MISSING)"
+ "metalTextureFromCubeData:"
+ "⭕️ ImageIO: loading HEIF (%!d(MISSING)x%!d(MISSING)) with '%!s(MISSING)'\n"
+ "☀️ HDR input headroom: %!f(MISSING), destination: %!f(MISSING), output headroom: %!f(MISSING)"
+ "stringByAppendingFormat:"
+ "v64@0:8r^{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}{?=i{?=ffffffff}^v}}{?={?=[3]}B}}16@24Q32@40@48Q56"
+ "N * N * N == count"
- "{?=\"flags\"I\"image\"{?=\"color\"{?=\"rgb\"{?=\"matrix\"{?=\"columns\"[3]}\"identity\"B}\"tm\"{?=\"type\"i\"params\"{?=\"a\"f\"b\"f\"c\"f\"d\"f\"e\"f\"f\"f\"g\"f\"gamma\"f\"luma\"}\"lut\"^v\"mat\"{?=\"matrix\"{?=\"columns\"[3]}\"identity\"B}}\"trc\"{?=\"type\"i\"params\"{?=\"a\"f\"b\"f\"c\"f\"d\"f\"e\"f\"f\"f\"g\"f\"gamma\"f\"luma\"}\"lut\"^v}}\"pixel\"{?=\"type\"i\"range\"{?=\"scale\"\"offset\"}\"yccMatrix\"{?=\"columns\"[3]}\"subsampling\"}}\"gainMap\"{?=\"gain\"{?=\"gm\"{?=\"type\"i\"params\"{?=\"gamma\"\"a\"\"b\"\"c\"\"d\"\"scale\"}}\"color\"{?=\"matrix\"{?=\"columns\"[3]}\"identity\"B}\"clip\"\"luma\"\"isLuma\"B}\"pixel\"{?=\"type\"i\"range\"{?=\"scale\"\"offset\"}\"yccMatrix\"{?=\"columns\"[3]}\"subsampling\"}}}"
- "r^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}16@0:8"
- "B64@0:8^{__CVBuffer=}16r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}}24^{__CVBuffer=}32r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}40^{__CVBuffer=}48r^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}56"
- "*** ERROR: CGImageSetHeadroom: %!f(MISSING) failed for image with %!s(MISSING) color space\n"
- "T^{?=I{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}}{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}},R,N"
- "B56@0:8^{?=i{?=ffffffff}^v}16^{?={?=[3]}B}24^{?=i{?=ffffffff}^v{?={?=[3]}B}}32^{CGColorSpace=}40f48i52"
- "v24@0:8d16"
- "@32@0:8d16@24"
- "B28@0:8^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}16f24"
- "\x82"
- "B48@0:8^{__CVBuffer=}16r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}}24^{__CVBuffer=}32r^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}40"
- "Td,N,V_headroom"
- "B64@0:8^{?=[32[32I]]}1624^{__CVBuffer=}32r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}}40^{__CVBuffer=}48r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}56"
- "B72@0:8^{__CVBuffer=}16r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}}24r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}}32^{__CVBuffer=}40r^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}48^{__CVBuffer=}56r^{?={?={?=i{?=}}{?={?=[3]}B}B}{?=i{?=}{?=[3]}}}64"
- "B28@0:8^{?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?=i{?=ffffffff}^v}}16f24"
- "B32@0:8^d16@24"
- "B32@0:8^d16^{CGImageMetadata=}24"
- "^{?=I{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}{?={?={?=i{?=}}{?={?=[3]}B}B}{?=i{?=}{?=[3]}}}}16@0:8"
- "☀️ Requested headroom (%!f(MISSING)) is less than native headroom (%!f(MISSING)), dropping FlexGTC info"
- "getOutputPixelRange:forPixelType:componentRange:bitDepth:"
- "d"
- "d32@0:8d16d24"
- "Tr^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}},R,N"
- "B64@0:8^i16^@24^32^@40^S48^{__CVBuffer=}56"
- "+[HDRImage getPixelType:YCCMatrixString:chromaSubsampling:componentRange:bitDepth:forBuffer:]"
- "r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}}16@0:8"
- "v64@0:8r^{?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?=i{?=ffffffff}^v}}16@24Q32@40@48Q56"
- "getPixelType:YCCMatrixString:chromaSubsampling:componentRange:bitDepth:forBuffer:"
- "☀️  %!s(MISSING) - updating CGImage<%!p(MISSING)>  headroom: %!g(MISSING)\n"
- "numberWithDouble:"
- "getInputPixelRange:forPixelType:componentRange:bitDepth:"
- "*** NOTE: requested pixelformat: '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)' -- got: '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)'\n"
- "d16@0:8"
- "B52@0:8^{?=i{?=ffffffff}^v}16^{?={?=[3]}B}24^{?=i{?=ffffffff}^v{?={?=[3]}B}}32f40^{CGColorSpace=}44"
- "B40@0:8^{?=}16i24@28S36"
- "^{?=I{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}}{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}}16@0:8"
- "Tr^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}},R,N"
- "B64@0:8^{?=i{?=ffffffff}^v}16^{?={?=[3]}B}24^{?=i{?=ffffffff}^v{?={?=[3]}B}}32^{CGColorSpace=}40^{CGColorSpace=}48@56"
- "B28@0:8^{?=I{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}}{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}}16f24"
- "^{CGImageMetadata=}24@0:8d16"
- "v64@0:8r^{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}16@24Q32@40@48Q56"
- "B28@0:8^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}}16f24"
- "{?=\"flags\"I\"image\"{?=\"pixel\"{?=\"type\"i\"range\"{?=\"scale\"\"offset\"}\"yccMatrix\"{?=\"columns\"[3]}\"affineTransform\"{?=\"columns\"[3]}}\"color\"{?=\"trc\"{?=\"type\"i\"params\"{?=\"a\"f\"b\"f\"c\"f\"d\"f\"e\"f\"f\"f\"g\"f\"gamma\"f\"luma\"}\"lut\"^v}\"tm\"{?=\"type\"i\"params\"{?=\"a\"f\"b\"f\"c\"f\"d\"f\"e\"f\"f\"f\"g\"f\"gamma\"f\"luma\"}\"lut\"^v\"mat\"{?=\"matrix\"{?=\"columns\"[3]}\"identity\"B}}\"rgb\"{?=\"matrix\"{?=\"columns\"[3]}\"identity\"B}}}\"gainMap\"{?=\"pixel\"{?=\"type\"i\"range\"{?=\"scale\"\"offset\"}\"yccMatrix\"{?=\"columns\"[3]}\"affineTransform\"{?=\"columns\"[3]}}\"gain\"{?=\"gm\"{?=\"type\"i\"params\"{?=\"gamma\"\"a\"\"b\"\"c\"\"d\"\"scale\"}}\"color\"{?=\"matrix\"{?=\"columns\"[3]}\"identity\"B}}}}"
- "B28@0:8^{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}16f24"
- "*** ERROR: CGImageSetHeadroom: %!f(MISSING) failed for image with unnamed color space\n"
- "*** ERROR: IIOImageSource::updateThumbnailInfo did not get image dimensions (%!d(MISSING) x %!d(MISSING))\n"
- "getColorTRC:matrix:toneMapping:fromSourceSpace:toEDR:toneMappingMode:"
- "T^{?=I{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}{?={?={?=i{?=}}{?={?=[3]}B}B}{?=i{?=}{?=[3]}}}},R,N"
- "B96@0:8^{__CVBuffer=}16r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}}24r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=ffffffff}^v}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?={?=[3]}B}}}32^{__CVBuffer=}40r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}48r^{?={?=i{?=}{?=[3]}{?=[3]}}{?={?=i{?=}}{?={?=[3]}B}}}56^{__CVBuffer=}64r^{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}72^{__CVBuffer=}80r^{?={?={?=i{?=}}{?={?=[3]}B}B}{?=i{?=}{?=[3]}}}88"
- "B28@0:8^{?=I{?={?={?={?=[3]}B}{?=i{?=ffffffff}^v{?={?=[3]}B}}{?=i{?=ffffffff}^v}}{?=i{?=}{?=[3]}}}{?={?={?=i{?=}}{?={?=[3]}B}B}{?=i{?=}{?=[3]}}}}16f24"

```
