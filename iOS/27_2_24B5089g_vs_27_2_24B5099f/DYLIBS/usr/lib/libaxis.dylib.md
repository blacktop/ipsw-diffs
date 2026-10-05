## libaxis.dylib

> `/usr/lib/libaxis.dylib`

```diff

-8.1.13.0.0
-  __TEXT.__text: 0x53cf68
-  __TEXT.__const: 0xf874
-  __TEXT.__gcc_except_tab: 0x47194
-  __TEXT.__cstring: 0x16b08
-  __TEXT.__unwind_info: 0x12300
+8.1.15.0.0
+  __TEXT.__text: 0x54f480
+  __TEXT.__const: 0xf8a4
+  __TEXT.__gcc_except_tab: 0x48268
+  __TEXT.__cstring: 0x17928
+  __TEXT.__unwind_info: 0x12598
   __TEXT.__eh_frame: 0x88
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xc0

   __DATA.__common: 0x8
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 9906
+  Functions: 9983
   Symbols:   2776
-  CStrings:  1961
+  CStrings:  2079
 
Symbols:
+ __ZN5terra13GeoTIFFReader11read_memoryEPKhm
- __ZN5terra13GeoTIFFReader11read_memoryEPKh
CStrings:
+ " SHORT values, but holds only "
+ " and StripByteCounts holds "
+ " and a full strip holds "
+ " available"
+ " bytes"
+ " bytes available for that tag"
+ " bytes exceeds the "
+ " bytes from file: "
+ " bytes needed, "
+ " bytes remain"
+ " bytes remaining"
+ " bytes the raster needs"
+ " bytes where the "
+ " coordinates but only "
+ " declares "
+ " exceed the supported maximum"
+ " float raster cannot fit in "
+ " for a "
+ " has type "
+ " hex chars, have "
+ " input bytes"
+ " is out of range for this API"
+ " is supported"
+ " keys, which need "
+ " leaves no room for a coordinate delta"
+ " lies outside the input: offset "
+ " of the "
+ " origin "
+ " points but decoded "
+ " precision cannot be encoded, got "
+ " precision is not usable for decoding, got "
+ " raster"
+ " raster by pixel"
+ " row(s) it covers need "
+ " strips but StripOffsets holds "
+ " value(s)"
+ " value(s) at index "
+ " values, only a single sample per pixel is supported"
+ " where BYTE, SHORT or LONG is required"
+ " x "
+ " x ImageHeight "
+ ") has no value at index "
+ ") is missing"
+ ") value "
+ ", only "
+ ", only 32 is supported"
+ ", which holds only "
+ "-bit target type"
+ "-byte header: "
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AxisGeometry/src/axis/algorithm/AxisCompressionDecoder.hpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AxisGeometry/src/axis/algorithm/AxisCompressionEncoder.hpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AxisGeometry/src/axis/misc/BinaryConverters.hpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AxisGeometry/src/terra/algorithm/MeshCompression.cpp"
+ "; "
+ "ACF "
+ "BitsPerSample"
+ "Compression"
+ "GCL TriangleMeshDecoder: triangle count "
+ "GCL TriangleMeshDecoder: vertex count "
+ "GCL payload is shorter than its "
+ "GCL run declared "
+ "GeoAsciiParams"
+ "GeoDoubleParams"
+ "GeoKeyDirectory"
+ "GeoPixelScale"
+ "GeoTIFFReader: "
+ "GeoTIFFReader: BitsPerSample(258) holds "
+ "GeoTIFFReader: GeoKeyDirectory declares "
+ "GeoTIFFReader: GeoKeyDirectory must hold at least 4 SHORT values, got "
+ "GeoTIFFReader: RowsPerStrip(278) is 0, which describes no strip at all"
+ "GeoTIFFReader: a "
+ "GeoTIFFReader: cannot determine the size of file: "
+ "GeoTIFFReader: cannot open file: "
+ "GeoTIFFReader: empty raster: ImageWidth "
+ "GeoTIFFReader: geo key references "
+ "GeoTIFFReader: null input"
+ "GeoTIFFReader: raster dimensions "
+ "GeoTIFFReader: raster needs "
+ "GeoTIFFReader: read "
+ "GeoTIFFReader: required TIFF tag "
+ "GeoTIFFReader: strip "
+ "GeoTIFFReader: strips cover "
+ "GeoTIFFReader: tag "
+ "GeoTIFFReader: the tie point and pixel scale give a degenerate bounding box, extent "
+ "GeoTIFFReader: the tie point and pixel scale give an extent too large to address a "
+ "GeoTIFFReader: tiled GeoTIFF is not supported (TileWidth(322) is present); only strip layouts are read"
+ "GeoTIFFReader: unsupported "
+ "GeoTIFFReader: unsupported BitsPerSample(258) value "
+ "GeoTiePoints"
+ "ImageHeight"
+ "ImageWidth"
+ "IndexedGeometry::get_de9im()"
+ "PlanarConfiguration"
+ "RowsPerStrip"
+ "SampleFormat"
+ "SamplesPerPixel"
+ "StripByteCounts"
+ "StripOffsets"
+ "TIFF directory"
+ "TIFF directory entry"
+ "TIFF header"
+ "Truncated bytestream: "
+ "Truncated bytestream: ACF header is empty"
+ "Truncated bytestream: ACF header needs 3 bytes, found "
+ "Truncated bytestream: declared payload of "
+ "Truncated bytestream: payload declares "
+ "Truncated bytestream: varint continues past the end of the input"
+ "Unsupported number of tie points values (expected 6 DOUBLEs): "
+ "Unsupported pixel scale values (expect at least 2 DOUBLEs): "
+ "Unsupported pixel scale values (expect finite and positive): "
+ "Unsupported tie points values (expect a finite origin): "
+ "Varint is longer than its "
+ "Varint value does not fit its "
+ "WKBReader: truncated hex WKB, need "
+ "X"
+ "XY"
+ "Y"
+ "Z"
+ "data of strip "
+ "value of tag "
- "Truncated bytestream"
- "Unsupported number of tie points values (expected 6): "
```
