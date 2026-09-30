## MOVStreamIO

> `/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO`

```diff

-3.35.0.0.0
-  __TEXT.__text: 0x9f43c
-  __TEXT.__auth_stubs: 0x13c0
+3.36.0.0.0
+  __TEXT.__text: 0xa0334
+  __TEXT.__auth_stubs: 0x13e0
   __TEXT.__delay_stubs: 0x18c
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x6658
+  __TEXT.__objc_methlist: 0x6718
   __TEXT.__const: 0x4650
-  __TEXT.__cstring: 0x8985
+  __TEXT.__cstring: 0x8a80
   __TEXT.__oslogstring: 0x3580
   __TEXT.__gcc_except_tab: 0x10904
   __TEXT.__ustring: 0x64a
-  __TEXT.__unwind_info: 0x3618
-  __TEXT.__objc_classname: 0xf39
-  __TEXT.__objc_methname: 0xe9c0
-  __TEXT.__objc_methtype: 0x53d4
-  __TEXT.__objc_stubs: 0x9640
-  __DATA_CONST.__got: 0x7f8
-  __DATA_CONST.__const: 0x9b8
-  __DATA_CONST.__objc_classlist: 0x360
+  __TEXT.__unwind_info: 0x3648
+  __TEXT.__objc_classname: 0xf6b
+  __TEXT.__objc_methname: 0xee14
+  __TEXT.__objc_methtype: 0x5585
+  __TEXT.__objc_stubs: 0x9920
+  __DATA_CONST.__got: 0x810
+  __DATA_CONST.__const: 0x9e0
+  __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3098
+  __DATA_CONST.__objc_selrefs: 0x3170
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x2b8
-  __AUTH_CONST.__auth_got: 0xa40
+  __AUTH_CONST.__auth_got: 0xa50
   __AUTH_CONST.__const: 0xc18
-  __AUTH_CONST.__cfstring: 0x5c80
-  __AUTH_CONST.__objc_const: 0xeb18
+  __AUTH_CONST.__cfstring: 0x5e00
+  __AUTH_CONST.__objc_const: 0xec38
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x5a0
+  __AUTH.__objc_data: 0x640
   __DATA.__objc_ivar: 0x624
   __DATA.__data: 0xa24
   __DATA.__bss: 0x169

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D5B91EC4-1194-3CA5-B595-0A018EAC3B33
-  Functions: 2801
-  Symbols:   10956
-  CStrings:  4773
+  UUID: 3BA4401D-838C-3AC4-8BB2-B61B76E06B52
+  Functions: 2816
+  Symbols:   11024
+  CStrings:  4840
 
Symbols:
+ +[MIOPixelBufferFileReader detectPixelFormatFromFilePath:]
+ +[MIOPixelBufferFileReader parseFrameString:width:height:timestamp:]
+ +[MIOPixelBufferFileReader parseFrameStringWithIndex:width:height:index:]
+ +[MIOPixelBufferFileReader pixelBufferSizeFromFile:error:]
+ +[MIOPixelBufferFileReader readPlainPixelBufferFromFile:addAttchments:index:timestamp:attachmentsFound:error:]
+ +[MIOPixelBufferFileReader readPlainPixelBufferFromFile:addAttchments:timescale:index:timestamp:attachmentsFound:error:]
+ +[MIOPixelBufferFileWriter baseFileNameForPixelBuffer:filePrefix:fileSuffix:fileFormat:]
+ +[MIOPixelBufferFileWriter fileNameForPixelBuffer:filePrefix:index:fileFormat:]
+ +[MIOPixelBufferFileWriter fileNameForPixelBuffer:filePrefix:timestamp:fileFormat:]
+ +[MIOPixelBufferFileWriter pathExtensionForPixelBuffer:fileFormat:]
+ +[MIOPixelBufferFileWriter writePixelBuffer:toFile:attachments:fileFormat:error:]
+ +[MIOPixelBufferFileWriter writePlainPixelBuffer:toFile:error:]
+ +[MOVStreamTimestamps sampleTimelineForAssetTrack:shouldStartTimestampsAtZero:ptsHandler:]
+ +[MOVStreamTimestamps sampleTimelineForAssetTrack:shouldStartTimestampsAtZero:restrictedTimeRange:ptsHandler:]
+ _CMTimeConvertScale
+ _OBJC_CLASS_$_MIOPixelBufferFileReader
+ _OBJC_CLASS_$_MIOPixelBufferFileWriter
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_METACLASS_$_MIOPixelBufferFileReader
+ _OBJC_METACLASS_$_MIOPixelBufferFileWriter
+ __OBJC_$_CLASS_METHODS_MIOPixelBufferFileReader
+ __OBJC_$_CLASS_METHODS_MIOPixelBufferFileWriter
+ __OBJC_$_CLASS_METHODS_MOVStreamTimestamps
+ __OBJC_CLASS_RO_$_MIOPixelBufferFileReader
+ __OBJC_CLASS_RO_$_MIOPixelBufferFileWriter
+ __OBJC_METACLASS_RO_$_MIOPixelBufferFileReader
+ __OBJC_METACLASS_RO_$_MIOPixelBufferFileWriter
+ ___79-[MOVStreamTimestamps sampleTimelineForAssetTrack:shouldStartTimestampsAtZero:]_block_invoke
+ ___block_descriptor_40_e8_32s_e15_v32?0{?=qiIq}8ls32l8
+ _objc_msgSend$baseFileNameForPixelBuffer:filePrefix:fileSuffix:fileFormat:
+ _objc_msgSend$detectPixelFormatFromFilePath:
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$initWithContentsOfURL:error:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$numberOfRanges
+ _objc_msgSend$parseFrameString:width:height:timestamp:
+ _objc_msgSend$parseFrameStringWithIndex:width:height:index:
+ _objc_msgSend$pathExtensionForPixelBuffer:fileFormat:
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$readFrameFromFile:width:height:pixelFormat:
+ _objc_msgSend$readPlainPixelBufferFromFile:addAttchments:timescale:index:timestamp:attachmentsFound:error:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$sampleTimelineForAssetTrack:shouldStartTimestampsAtZero:restrictedTimeRange:ptsHandler:
+ _objc_msgSend$setMovieTimeScale:
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringWithCharacters:length:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$writeBuffer:toFile:
+ _objc_msgSend$writePlainPixelBuffer:toFile:error:
+ _objc_msgSend$writeToURL:error:
+ _objc_msgSend$writeToURL:options:error:
+ _strnlen
CStrings:
+ "%015.6f"
+ "%06llu"
+ "%@-%@-%@"
+ "%lux%lu"
+ ".*-(\\d+)x(\\d+)-(\\d{6})$"
+ ".*-(\\d+)x(\\d+)-(\\d{8}\\.\\d{6})$"
+ "3.36.0"
+ "@32@0:8^{__CVBuffer=}16q24"
+ "@48@0:8^{__CVBuffer=}16@24@32q40"
+ "@48@0:8^{__CVBuffer=}16@24Q32q40"
+ "@64@0:8^{__CVBuffer=}16@24{?=qiIq}32q56"
+ "B40@0:8^{__CVBuffer=}16@24^@32"
+ "B48@0:8@16^I24^I32^d40"
+ "B48@0:8@16^I24^I32^q40"
+ "B56@0:8^{__CVBuffer=}16@24@32q40^@48"
+ "Cannot read pixel buffer from file."
+ "Failure writing pixel buffer to file '%@'."
+ "File format not supported."
+ "Invalid file name format."
+ "MIOPixelBufferFileReader"
+ "MIOPixelBufferFileWriter"
+ "^{__CVBuffer=}60@0:8@16B24^q28^{?=qiIq}36^B44^@52"
+ "^{__CVBuffer=}64@0:8@16B24i28^q32^{?=qiIq}40^B48^@56"
+ "baseFileNameForPixelBuffer:filePrefix:fileSuffix:fileFormat:"
+ "detectPixelFormatFromFilePath:"
+ "fileNameForPixelBuffer:filePrefix:index:fileFormat:"
+ "fileNameForPixelBuffer:filePrefix:timestamp:fileFormat:"
+ "firstMatchInString:options:range:"
+ "initWithContentsOfURL:error:"
+ "lastPathComponent"
+ "meta"
+ "meta.plist"
+ "numberOfRanges"
+ "parseFrameString:width:height:timestamp:"
+ "parseFrameStringWithIndex:width:height:index:"
+ "pathExtensionForPixelBuffer:fileFormat:"
+ "pixelBufferSizeFromFile:error:"
+ "rangeAtIndex:"
+ "readPlainPixelBufferFromFile:addAttchments:index:timestamp:attachmentsFound:error:"
+ "readPlainPixelBufferFromFile:addAttchments:timescale:index:timestamp:attachmentsFound:error:"
+ "regularExpressionWithPattern:options:error:"
+ "sampleTimelineForAssetTrack:shouldStartTimestampsAtZero:ptsHandler:"
+ "sampleTimelineForAssetTrack:shouldStartTimestampsAtZero:restrictedTimeRange:ptsHandler:"
+ "setMovieTimeScale:"
+ "stringByAppendingPathExtension:"
+ "stringByDeletingPathExtension"
+ "stringWithCharacters:length:"
+ "substringWithRange:"
+ "v32@?0{?=qiIq}8"
+ "v36@0:8@16B24@?28"
+ "v84@0:8@16B24{?={?=qiIq}{?=qiIq}}28@?76"
+ "writePixelBuffer:toFile:attachments:fileFormat:error:"
+ "writePlainPixelBuffer:toFile:error:"
+ "writeToURL:error:"
+ "writeToURL:options:error:"
+ "{CGSize=dd}32@0:8@16^@24"
- "3.35.0"

```
