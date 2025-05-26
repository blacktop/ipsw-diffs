## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2488.5.4.0.0
-  __TEXT.__text: 0x3bd0c4
+2488.6.2.0.0
+  __TEXT.__text: 0x3be29c
   __TEXT.__auth_stubs: 0x3bc0
   __TEXT.__objc_methlist: 0x310
-  __TEXT.__gcc_except_tab: 0x1bd98
+  __TEXT.__gcc_except_tab: 0x1bda8
   __TEXT.__const: 0x28968
-  __TEXT.__cstring: 0x6e0ff
+  __TEXT.__cstring: 0x6e396
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xce20
+  __TEXT.__unwind_info: 0xce38
   __TEXT.__eh_frame: 0x460
   __TEXT.__objc_classname: 0x3c
   __TEXT.__objc_methname: 0x1270
   __TEXT.__objc_methtype: 0x5f1
   __TEXT.__objc_stubs: 0xfa0
   __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0x10e10
+  __DATA_CONST.__const: 0xfc10
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12983
-  Symbols:   32572
-  CStrings:  11327
+  Functions: 12994
+  Symbols:   32594
+  CStrings:  11299
 
Symbols:
+ _CalcFinalIFDdatasizeReading
+ _EvaluateIFDdatasizeReading
+ _TIFFRewriteDirectorySec
+ _TIFFRewriteDirectorySec.module
+ _TIFFWriteDirectoryTagAscii
+ _TIFFWriteDirectoryTagByteArray
+ _TIFFWriteDirectoryTagCheckedSlong8Array
+ _TIFFWriteDirectoryTagCheckedSlong8Array.cold.1
+ _TIFFWriteDirectoryTagSbyteArray
+ _TIFFWriteDirectoryTagUndefinedArray
+ __TIFFfreeExt.cold.1
+ __TIFFreallocExt.cold.1
+ __ZN13IIOReadPlugin14freeBlockArrayEv
+ __ZN13IIOReadPlugin18allocateBlockArrayEj
+ ___block_descriptor_tmp.163
+ ___block_descriptor_tmp.167
+ ___block_descriptor_tmp.172
+ ___block_descriptor_tmp.175
+ ___block_descriptor_tmp.179
+ ___block_literal_global.177
+ _cmpTIFFEntryOffsetAndLength
- _TIFFReadDirEntryCheckedRationalDirect
- _TIFFReadDirectoryCheckOrder
- _TIFFRewriteDirectory.module
- _TIFFWriteDirectorySec.cold.15
- ___block_descriptor_tmp.170
- ___block_descriptor_tmp.173
- ___block_literal_global.175
CStrings:
+ "%s: Invalid InkNames value; no null at given buffer end location %u, after %hu ink"
+ "%s: Memory allocation of %llu bytes is beyond the %llu cumulated byte limit defined in open options"
+ "%s:%d: %s: Error fetching directory count"
+ "*** ERROR: corrupt logLUV / CIE Log2(L)(u',v') image\n"
+ "*** ERROR: invalid compression: %d\n"
+ "*** ERROR: rowBytes <= 0 - skipping layer decoding\n"
+ "*** ERROR: unexpected TIFFTAG_PHOTOMETRIC [%d]\n"
+ "/Library/Caches/com.apple.xbs/Sources/ImageIO/FileFormats/libTIFF/tif_dir.c"
+ "ASCII value for ASCII array tag \"%s\" does not end in null byte. Forcing it to be null"
+ "Cumulated memory allocation of %llu + %llu bytes is beyond the %llu cumulated byte limit defined in open options"
+ "EvaluateIFDdatasizeReading"
+ "Failed to allocate memory for counting IFD data size at reading"
+ "JPEG horizontal or vertical sampling is zero"
+ "Requested memory size for StripArray of %llu is greater than filesize %llu. Memory not allocated"
+ "Requested memory size for StripByteCount and StripOffsets %llu is greater than filesize %llu. Memory not allocated"
+ "Requested memory size for StripByteCounts of %llu is greater than filesize %llu. Memory not allocated"
+ "Requested memory size for TIFF directory of %llu is greater than filesize %llu. Memory not allocated, TIFF directory not read"
+ "Requested memory size for tag %d (0x%x) %u is greater than filesize %llu. Memory not allocated, tag not read"
+ "RowsPerStrip is zero"
+ "SLONG8 not allowed for ClassicTIFF"
+ "TIFFCleanup"
+ "Too few TransferFunctions provided. Tag not written to file"
+ "Too large IFD data size"
+ "Warning, unknown tag 0x%x"
+ "ZIPDecode: Scanline %u cannot be read due to previous error"
+ "Zero tilewidth"
+ "_TIFFfreeExt"
+ "allocChoppedUpStripArrays"
+ "oldSize <= tif->tif_cur_cumulated_mem_alloc"
+ "rowsperstrip is zero"
+ "tif_cur_cumulated_mem_alloc = %llu whereas it should be 0"
+ "tif_open.c"
+ "tile width or height is zero"
+ "🔸  '%c%c%c%c' - decoded IOSurface: <IOSurface: %p> %ldx%ld  '%c%c%c%c'\n"
- "%s: Error fetching directory count"
- "%s: Invalid InkNames value; no NUL at given buffer end location %u, after %hu ink"
- "ASCII value for tag \"%s\" does not end in null byte"
- "CalibrationIlluminant3"
- "CameraCalibration3"
- "ColorMatrix3"
- "DepthFar"
- "DepthFormat"
- "DepthMeasureType"
- "DepthNear"
- "DepthUnits"
- "EP ApertureValue"
- "EP BatteryLevel"
- "EP BrightnessValue"
- "EP CompressedBitsPerPixel"
- "EP DateTimeOriginal"
- "EP ExposureBiasValue"
- "EP ExposureIndex"
- "EP ExposureProgram"
- "EP ExposureTime"
- "EP FNumber"
- "EP Flash"
- "EP FlashEnergy"
- "EP FocalLength"
- "EP FocalPlaneResolutionUnit"
- "EP FocalPlaneXResolution"
- "EP FocalPlaneYResolution"
- "EP ISOSpeedRatings"
- "EP ImageHistory"
- "EP ImageNumber"
- "EP Interlace"
- "EP LightSource"
- "EP MaxApertureValue"
- "EP MeteringMode"
- "EP Noise"
- "EP OptoelectricConversionFactor"
- "EP SecurityClassification"
- "EP SelfTimerMode"
- "EP SensingMethod"
- "EP ShutterSpeedValue"
- "EP SpatialFrequencyResponse"
- "EP SpectralSensitivity"
- "EP StandardId"
- "EP SubjectDistance"
- "EP SubjectLocation"
- "EP TimeZoneOffset"
- "EnhanceParams"
- "ForwardMatrix3"
- "IlluminantData1"
- "IlluminantData2"
- "IlluminantData3"
- "Internal error, unknown tag 0x%x"
- "Invalid data type for tag %s. ASCII or RATIONAL expected"
- "MaskSubArea"
- "OpcodeList2"
- "OpcodeList3"
- "ProfileGainTableMap"
- "ProfileHueSatMapData3"
- "RGBTables"
- "ReductionMatrix3"
- "SemanticInstanceID"
- "SemanticName"

```
