## VideoToolbox

> `/System/Library/Frameworks/VideoToolbox.framework/Versions/A/VideoToolbox`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3350.67.2.0.0
-  __TEXT.__text: 0x732e4c
+3350.71.2.0.0
+  __TEXT.__text: 0x732f64
   __TEXT.__objc_methlist: 0x1574
   __TEXT.__cstring: 0x4397d
   __TEXT.__const: 0xddfc
-  __TEXT.__oslogstring: 0x2b38c
+  __TEXT.__oslogstring: 0x2b3a4
   __TEXT.__gcc_except_tab: 0x390
   __TEXT.__dlopen_cstrs: 0x9b
   __TEXT.__constg_swiftt: 0x4d8

   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcb0
+  __DATA_CONST.__objc_selrefs: 0xcb8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x20

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 10629
-  Symbols:   11807
+  Symbols:   11808
   CStrings:  10665
 
Symbols:
+ _objc_msgSend$bundleIdentifier
Functions:
~ _vtCompressionSessionCompressionWork : 11292 -> 11396
~ _vtDecompressionDuctEmitDecodedFrame : 4056 -> 4068
~ _RemoteVideoDecoder_Finalize : 1032 -> 1048
~ ___vtRemoteDecoderClient_validateAndRebuildIfNeeded_block_invoke_2 : 7976 -> 8068
~ _vtRemoteDecoderClientInstance_handleServerCallback : 4916 -> 4956
~ _forgetPixelBufferRecipient : 1112 -> 1128
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Can't guess what this image's colourspace is"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: GetConversionRoutine: unrecognised source colourspace"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: JPEG GetConversionRoutine can only take RGB to 32ARGB.  Preflight must have lied!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: JPEG GetConversionRoutine can only take RGBA to 32ARGB.  Preflight must have lied!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: 8-grey -> ?"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCr 411 -> ?"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCr 422 -> ?"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCr with funny sampling -> ?"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCrA 4114 -> ?"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCrA non4114 -> ?"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Warning in GetConversionRoutine: unhandled number of components"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Warning: JPEG is doing nothing."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_blockdecode.c %s: Decode Error in DecodeBlocks"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Exif marker is too large to fit!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: JPEG SOF marker has a bad quantization table selector"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: JPEG SOF marker has a bad sampling factor"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: JPEG SOF marker has too many components for us"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Progressive JPEG scan SOS has Se > 63"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Progressive JPEG scan SOS has Ss > Se"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Progressive JPEG scan trying to use undefined AC huffman table"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Progressive JPEG scan trying to use undefined DC huffman table"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Sequential JPEG trying to use undefined huffman table"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_progressive.c %s: Bad data: attempted to place a value outside this scan's coefficient range."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_prototypeDecode.c %s: Mismatch between the height allocated and what is read from the bitstream."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_prototypeDecode.c %s: Mismatch between the width allocated and what is read from the bitstream."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s:  Calculated dataSize + HeaderSize %d is larger than allocated size %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s:  height %d is not multiple of tileHeight %d, we can only fill whole tile CVPixelBuffer will not be black filled."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s:  width %d is not multiple of tileWidth %d, we can only fill whole tile CVPixelBuffer will not be black filled."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: BlackBlock is more than %d bytes -- need to increase limit in VT to accommodate this pixel format: '%.4s'"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatBlockHeight"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatBlockHeight for pixelformat '%.4s' (%d)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatBlockWidth for pixelformat '%.4s' (%d)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatHorizontalSubsampling for pixelformat '%.4s' (%d)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatVerticalSubsampling for pixelformat '%.4s' (%d)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: blackfillHeightInTiles %d is greater than planeHeightInTiles %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: blackfillWidthInTiles %d is greater than planeWidthInTiles %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: dataPattern is NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: destination address is NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: didn't find kCVPixelFormatPlane dictionary for index %zu for pixelformat '%.4s' (%d) in pixel format description dictionary"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: didn't find kCVPixelFormatPlanes for pixelformat '%.4s' (%d) in pixel format description dictionary"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: kCVPixelFormatBitsPerBlock not set for pixelformat '%.4s' (%d) in pixel format description dictionary"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: left offset %d is not tileWidth %d aligned, we can only black fill whole tile"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: planeIndex out of range"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: top offset %d is not tileHeight %d aligned, we can only black fill whole tile"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds read plane 0. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds read plane 1. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds read plane 2. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds read. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds write plane 0. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds write plane 1. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds write plane 2. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds write rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds write. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: Buffer %p not IOsurface backed. VTFrameProcessorFrame requires IOsurface backing"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: Fail to initialize"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: Input buffer cannot be nil in VTFrameProcessorFrame"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: backwardFlow %p is not IOSurface backed"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: backwardFlow cannot be nil in VTFrameProcessorOpticalFlow"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: forwardFlow %p is not IOSurface backed"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: forwardFlow cannot be nil in VTFrameProcessorOpticalFlow"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTTestMotionEstimationProcessor.c %s: unrecognised property key %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oqqSuL/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTXPCSupport.c %s: CFURLCreateBookmarkData reported error: %@"
+ "<<<< RemoteDecode - client >>>> %s: [%p:%{public}s] Created pixelBufferRecipient %p for extension decoder %@ (%@)"
+ "<<<< RemoteDecode - client >>>> %s: [%p:%{public}s] MemoryOrigin ID entry created for %@ (%@)"
+ "<<<< VT-DS >>>> %s: [%p:%{public}s] Output frame for sourceFrameRefCon: %p frame: %p imageBuffer: %p infoFlags: %x status: %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Can't guess what this image's colourspace is"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: GetConversionRoutine: unrecognised source colourspace"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: JPEG GetConversionRoutine can only take RGB to 32ARGB.  Preflight must have lied!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: JPEG GetConversionRoutine can only take RGBA to 32ARGB.  Preflight must have lied!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: 8-grey -> ?"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCr 411 -> ?"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCr 422 -> ?"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCr with funny sampling -> ?"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCrA 4114 -> ?"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCrA non4114 -> ?"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Warning in GetConversionRoutine: unhandled number of components"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Warning: JPEG is doing nothing."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_blockdecode.c %s: Decode Error in DecodeBlocks"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Exif marker is too large to fit!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: JPEG SOF marker has a bad quantization table selector"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: JPEG SOF marker has a bad sampling factor"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: JPEG SOF marker has too many components for us"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Progressive JPEG scan SOS has Se > 63"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Progressive JPEG scan SOS has Ss > Se"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Progressive JPEG scan trying to use undefined AC huffman table"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Progressive JPEG scan trying to use undefined DC huffman table"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Sequential JPEG trying to use undefined huffman table"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_progressive.c %s: Bad data: attempted to place a value outside this scan's coefficient range."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_prototypeDecode.c %s: Mismatch between the height allocated and what is read from the bitstream."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_prototypeDecode.c %s: Mismatch between the width allocated and what is read from the bitstream."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s:  Calculated dataSize + HeaderSize %d is larger than allocated size %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s:  height %d is not multiple of tileHeight %d, we can only fill whole tile CVPixelBuffer will not be black filled."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s:  width %d is not multiple of tileWidth %d, we can only fill whole tile CVPixelBuffer will not be black filled."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: BlackBlock is more than %d bytes -- need to increase limit in VT to accommodate this pixel format: '%.4s'"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatBlockHeight"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatBlockHeight for pixelformat '%.4s' (%d)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatBlockWidth for pixelformat '%.4s' (%d)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatHorizontalSubsampling for pixelformat '%.4s' (%d)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatVerticalSubsampling for pixelformat '%.4s' (%d)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: blackfillHeightInTiles %d is greater than planeHeightInTiles %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: blackfillWidthInTiles %d is greater than planeWidthInTiles %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: dataPattern is NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: destination address is NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: didn't find kCVPixelFormatPlane dictionary for index %zu for pixelformat '%.4s' (%d) in pixel format description dictionary"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: didn't find kCVPixelFormatPlanes for pixelformat '%.4s' (%d) in pixel format description dictionary"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: kCVPixelFormatBitsPerBlock not set for pixelformat '%.4s' (%d) in pixel format description dictionary"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: left offset %d is not tileWidth %d aligned, we can only black fill whole tile"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: planeIndex out of range"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: top offset %d is not tileHeight %d aligned, we can only black fill whole tile"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds read plane 0. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds read plane 1. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds read plane 2. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds read. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds write plane 0. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds write plane 1. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds write plane 2. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds write rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlitterTemplate_ColorHandling_Optimized.c %s: out of bounds write. rowBytes %zu  left %zu  top %zu  width %zu  height %zu  planeSize %zu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: Buffer %p not IOsurface backed. VTFrameProcessorFrame requires IOsurface backing"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: Fail to initialize"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: Input buffer cannot be nil in VTFrameProcessorFrame"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: backwardFlow %p is not IOSurface backed"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: backwardFlow cannot be nil in VTFrameProcessorOpticalFlow"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: forwardFlow %p is not IOSurface backed"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: forwardFlow cannot be nil in VTFrameProcessorOpticalFlow"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTTestMotionEstimationProcessor.c %s: unrecognised property key %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KPHXfB/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTXPCSupport.c %s: CFURLCreateBookmarkData reported error: %@"
- "<<<< RemoteDecode - client >>>> %s: [%p:%{public}s] Created pixelBufferRecipient %p for extension decoder %@"
- "<<<< RemoteDecode - client >>>> %s: [%p:%{public}s] MemoryOrigin ID entry created for %@"
- "<<<< VT-DS >>>> %s: [%p:%{public}s] Output frame for sourceFrameRefCon: %p frame: %p imageBuffer: %p status: %d"
```
