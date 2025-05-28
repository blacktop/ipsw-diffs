## ImageIOXPCService

> `/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService`

```diff

-2488.5.4.0.0
-  __TEXT.__text: 0x41cc6c
+2488.6.2.0.0
+  __TEXT.__text: 0x41dfec
   __TEXT.__auth_stubs: 0x4250
   __TEXT.__objc_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x310
-  __TEXT.__gcc_except_tab: 0x1f700
+  __TEXT.__gcc_except_tab: 0x1f710
   __TEXT.__const: 0x2a760
-  __TEXT.__cstring: 0x78ca2
+  __TEXT.__cstring: 0x79031
   __TEXT.__objc_methname: 0x1282
   __TEXT.__objc_classname: 0x3f
   __TEXT.__objc_methtype: 0x5f1

   __DATA_CONST.__auth_got: 0x2140
   __DATA_CONST.__got: 0x630
   __DATA_CONST.__auth_ptr: 0x90
-  __DATA_CONST.__const: 0x718c8
+  __DATA_CONST.__const: 0x706c8
   __DATA_CONST.__cfstring: 0xbee0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 16122
-  Symbols:   10803
-  CStrings:  12681
+  Functions: 16132
+  Symbols:   10804
+  CStrings:  12658
 
Symbols:
+ _TIFFOpenOptionsSetMaxCumulatedMemAlloc
+ __ZN13IIOReadPlugin14freeBlockArrayEv
+ __ZN13IIOReadPlugin18allocateBlockArrayEj
- __TIFFUInt64ToDouble
- __TIFFUInt64ToFloat
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
+ "Invalid row passed to TIFFReadRGBAStrip()."
+ "Invalid row/col passed to TIFFReadRGBATile()."
+ "JPEG horizontal or vertical sampling is zero"
+ "Requested memory size for StripArray of %llu is greater than filesize %llu. Memory not allocated"
+ "Requested memory size for StripByteCount and StripOffsets %llu is greater than filesize %llu. Memory not allocated"
+ "Requested memory size for StripByteCounts of %llu is greater than filesize %llu. Memory not allocated"
+ "Requested memory size for TIFF directory of %llu is greater than filesize %llu. Memory not allocated, TIFF directory not read"
+ "Requested memory size for tag %d (0x%x) %u is greater than filesize %llu. Memory not allocated, tag not read"
+ "RowsPerStrip is zero"
+ "SLONG8 not allowed for ClassicTIFF"
+ "TIFFCleanup"
+ "The value of field_readcount and field_writecount must be greater than or equal to -3 and not zero."
+ "Too few TransferFunctions provided. Tag not written to file"
+ "Too large IFD data size"
+ "Warning, unknown tag %s"
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
+ "tile_xsize or tile_ysize is zero"
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
- "Internal error, unknown tag %s"
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
