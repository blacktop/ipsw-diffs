## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

 2851.1.8.0.0
-  __TEXT.__text: 0x4fbc84
+  __TEXT.__text: 0x4fbfa0
   __TEXT.__objc_methlist: 0xd68
   __TEXT.__const: 0x4a070
-  __TEXT.__gcc_except_tab: 0x22bd4
-  __TEXT.__cstring: 0xa740d
+  __TEXT.__gcc_except_tab: 0x22bec
+  __TEXT.__cstring: 0xa777d
   __TEXT.__oslogstring: 0x17
   __TEXT.__constg_swiftt: 0x26a4
   __TEXT.__swift5_typeref: 0x3d88

   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x18370
+  __TEXT.__unwind_info: 0x18378
   __TEXT.__eh_frame: 0x9324
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
-  Functions: 23237
+  Functions: 23239
   Symbols:   24492
-  CStrings:  18300
+  CStrings:  18318
 
Functions:
~ __ZN13IIOReadPlugin10willDecodeEPK14__CFDictionary : 1728 -> 1736
~ _OUTLINED_FUNCTION_1 : 20 -> 24
~ _OUTLINED_FUNCTION_1 : 16 -> 20
~ _OUTLINED_FUNCTION_1 : 72 -> 16
~ _OUTLINED_FUNCTION_1 : 16 -> 72
~ _OUTLINED_FUNCTION_1 : 28 -> 16
~ _OUTLINED_FUNCTION_1 : 20 -> 28
~ _OUTLINED_FUNCTION_1 : 16 -> 20
~ _OUTLINED_FUNCTION_1 : 12 -> 16
~ _OUTLINED_FUNCTION_1 : 16 -> 12
~ _OUTLINED_FUNCTION_1 : 32 -> 16
~ _OUTLINED_FUNCTION_1 : 24 -> 32
~ _OUTLINED_FUNCTION_1 : 20 -> 24
~ _OUTLINED_FUNCTION_1 : 48 -> 20
~ _OUTLINED_FUNCTION_1 : 20 -> 48
~ _OUTLINED_FUNCTION_1 : 32 -> 20
~ _OUTLINED_FUNCTION_1 : 16 -> 32
~ _OUTLINED_FUNCTION_1 : 20 -> 16
~ _OUTLINED_FUNCTION_1 : 16 -> 20
~ _OUTLINED_FUNCTION_1 : 20 -> 16
~ _OUTLINED_FUNCTION_1 : 16 -> 20
~ _OUTLINED_FUNCTION_1 : 36 -> 16
~ _OUTLINED_FUNCTION_1 : 16 -> 36
~ _OUTLINED_FUNCTION_1 : 32 -> 16
~ _OUTLINED_FUNCTION_1 : 20 -> 32
~ _OUTLINED_FUNCTION_1 : 32 -> 20
+ _OUTLINED_FUNCTION_1
~ _OUTLINED_FUNCTION_2 : 32 -> 20
~ _OUTLINED_FUNCTION_2 : 24 -> 32
~ _OUTLINED_FUNCTION_2 : 28 -> 24
~ _OUTLINED_FUNCTION_2 : 12 -> 28
~ _OUTLINED_FUNCTION_2 : 24 -> 12
~ _OUTLINED_FUNCTION_2 : 16 -> 24
~ _OUTLINED_FUNCTION_2 : 20 -> 16
~ _OUTLINED_FUNCTION_2 : 32 -> 20
~ _OUTLINED_FUNCTION_2 : 12 -> 32
~ _OUTLINED_FUNCTION_2 : 20 -> 12
~ _OUTLINED_FUNCTION_2 : 32 -> 20
~ _OUTLINED_FUNCTION_2 : 16 -> 32
~ _OUTLINED_FUNCTION_2 : 12 -> 16
~ _OUTLINED_FUNCTION_2 : 40 -> 12
~ _OUTLINED_FUNCTION_2 : 20 -> 40
~ _OUTLINED_FUNCTION_2 : 16 -> 20
~ _OUTLINED_FUNCTION_2 : 20 -> 16
~ _OUTLINED_FUNCTION_2 : 24 -> 20
+ _OUTLINED_FUNCTION_2
~ __ZN15IIO_Reader_HEIF16extractImageInfoENSt3__110shared_ptrI14GlobalHEIFInfoEEP19IIOImageReadSessionP13IIODictionary : 2580 -> 2656
~ __ZN14TIFFReadPlugin17decodeStripChunkyEP4tiff13IIODecodeInfo : 1260 -> 1304
~ _TIFFReadDirEntryShortArray : 732 -> 748
~ _TIFFReadDirEntryLong8ArrayWithLimit : 736 -> 752
~ __ZN9_JPEGFile11processDataEv : 1812 -> 1728
~ __ZN5_APP111processAPP1Emb : 1556 -> 1664
~ __ZN18IIO_Reader_LibJPEG13initThumbnailEP13CGImagePluginmm : 1720 -> 1764
~ _TIFFReadDirEntrySshortArray : 724 -> 740
~ _TIFFReadDirEntryLongArray : 736 -> 752
~ _TIFFReadDirEntrySlongArray : 720 -> 736
~ _TIFFReadDirEntrySlong8Array : 672 -> 688
~ _TIFFReadDirEntryFloatArray : 1016 -> 1032
~ _TIFFReadDirEntryIfd8Array : 348 -> 364
~ _CGImagePluginInitThumbJPEGAtOffsetWithOptions : 1888 -> 1996
~ __Z15ReadUserCommentP15CGImageMetadataP19IIOImageReadSessionPK10__CFStringS5_S5_P21CGImageMetadataTagKeyP9tag_entrymb : 656 -> 712
~ __ZN13JP2ReadPlugin19saveDataToXPCObjectEPv : 324 -> 320
~ __ZN20IIO_Reader_AppleJPEG13initThumbnailEP13CGImagePluginmm : 1664 -> 1700
~ __ZN5_APPx13writeToStreamEP15__CFWriteStream : 72 -> 152
~ ____ZN18IIOMetadataUpdater17updatePNGExifDataEP8__CFDataP13IIODictionarybb_block_invoke : 1020 -> 1032
~ __ZN14TIFFReadPlugin17decodeStripPlanarEP4tiff13IIODecodeInfo : 956 -> 1060
~ __ZN14TIFFReadPlugin16decodeTilePlanarEP4tiff13IIODecodeInfo : 1080 -> 1116
CStrings:
+ "*** ERROR: CGImagePluginInitThumbJPEGAtOffsetWithOptions offset (%ld) + size (%ld) out of range (%zu)\n"
+ "*** ERROR: decodeStripPlanar destination row is %u bytes, the scatter needs %llu\n"
+ "*** ERROR: decodeTilePlanar destination row is %u bytes, the scatter needs %llu\n"
+ "*** ERROR: extractImageInfo: thumbnail offset (%llu) + length (%llu) out of range (%zu)\n"
+ "*** ERROR: initThumbnail: thumbnail offset (%zu) + length (%zu) out of range (%zu)\n"
+ "*** ERROR: marker 0x%04X is out of bounds (offset %llu, length %u, size %zd) - skipping\n"
+ "*** ERROR: markerLength too big: %u  max: %zd\n"
+ "*** ERROR: short read for tag %d, count: %d\n"
+ "*** TIFFReadEncodedStrip(%d) failed - strip %d is zero-filled\n"
+ "TIFFReadDirEntryFloatArray"
+ "TIFFReadDirEntryIfd8Array"
+ "TIFFReadDirEntryLong8ArrayWithLimit"
+ "TIFFReadDirEntryLongArray"
+ "TIFFReadDirEntryShortArray"
+ "TIFFReadDirEntrySlong8Array"
+ "TIFFReadDirEntrySlongArray"
+ "TIFFReadDirEntrySshortArray"
+ "decodeStripChunky"
+ "decodeStripPlanar"
- "*** WARNING: check markerLength: %d - expected max: %zd\n"
```
