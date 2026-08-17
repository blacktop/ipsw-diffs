## AccessorySensorManagerDarwin_Private

> `/System/Library/PrivateFrameworks/AccessorySensorManagerDarwin_Private.framework/Versions/A/AccessorySensorManagerDarwin_Private`

```diff

 11.28.0.0.0
-  __TEXT.__text: 0x494
-  __TEXT.__auth_stubs: 0xd0
-  __TEXT.__objc_methlist: 0xd4
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x6e
-  __TEXT.__unwind_info: 0x90
-  __TEXT.__objc_classname: 0x44
-  __TEXT.__objc_methname: 0x1e5
-  __TEXT.__objc_methtype: 0x7b
-  __TEXT.__objc_stubs: 0x40
-  __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x20
+  __TEXT.__text: 0x1754
+  __TEXT.__auth_stubs: 0x230
+  __TEXT.__objc_methlist: 0x17c
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x255
+  __TEXT.__gcc_except_tab: 0x40
+  __TEXT.__oslogstring: 0x3ac
+  __TEXT.__unwind_info: 0xd0
+  __TEXT.__objc_classname: 0x45
+  __TEXT.__objc_methname: 0x4d1
+  __TEXT.__objc_methtype: 0x101
+  __TEXT.__objc_stubs: 0x280
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68
+  __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x70
-  __AUTH_CONST.__const: 0x70
+  __AUTH_CONST.__auth_got: 0x128
+  __AUTH_CONST.__const: 0xb0
   __AUTH_CONST.__objc_const: 0x2d8
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x18
+  __DATA.__data: 0xe0
+  - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
+  - /System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage
+  - /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AccessorySensorManagerDefines_Private.framework/Versions/A/AccessorySensorManagerDefines_Private
   - /System/Library/PrivateFrameworks/AccessorySensorManagerServices.framework/Versions/A/AccessorySensorManagerServices
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 22
-  Symbols:   77
-  CStrings:  39
+  Functions: 42
+  Symbols:   155
+  CStrings:  108
 
Symbols:
+ +[ASMImageProcessingHelper createPixelBufferFromRawImageData:withSensorInfo:error:]
+ +[ASMImageProcessingHelper getPNGDataFromRawImageData:error:]
+ +[ASMImageProcessingHelper getPNGDataFromRawImageData:withSensorInfo:error:]
+ -[ASMPolarisResourceProvider publishResourcesForKinoSensor:completion:]
+ -[ASMPolarisResourceProvider setAvailabilityForKinoSensor:availability:]
+ -[ASMSignpost beginActiveFirstSliceSignposts]
+ -[ASMSignpost beginCaptureSignpostForConfig:]
+ -[ASMSignpost beginGATTSignalingSignpost]
+ -[ASMSignpost endActiveEndToEndSignpostOnError]
+ -[ASMSignpost endActiveFirstSliceSignpostsOnError]
+ -[ASMSignpost endGATTSignalingSignpost]
+ -[ASMSignpost endPassiveEndToEndSignpost]
+ -[ASMSignpost handleImageSliceSignpostForSDU:]
+ GCC_except_table1
+ _ASMErrorF
+ _ASMKinoSensorIdentifierActive1024_WRR
+ _ASMKinoSensorIdentifierAmbient320_BU
+ _ASMKinoSensorIdentifierAmbient320_BWRRC
+ _ASMKinoSensorIdentifierAmbient320_BWRRD
+ _ASMKinoSensorIdentifierAmbient512_BWRR
+ _CGColorSpaceCreateWithName
+ _CGColorSpaceGetGray
+ _CVPixelBufferCreate
+ _CVPixelBufferCreateWithPlanarBytes
+ _CVPixelBufferGetBaseAddress
+ _CVPixelBufferGetDataSize
+ _CVPixelBufferLockBaseAddress
+ _CVPixelBufferRelease
+ _CVPixelBufferUnlockBaseAddress
+ _LogPrintF
+ _OBJC_CLASS_$_ASMKinoSensorInfo
+ _OBJC_CLASS_$_CIContext
+ _OBJC_CLASS_$_CIImage
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSMutableSet
+ _OUTLINED_FUNCTION_0
+ __LogCategory_Initialize
+ __OBJC_$_CLASS_METHODS_ASMImageProcessingHelper
+ __Unwind_Resume
+ ___71-[ASMPolarisResourceProvider publishResourcesForKinoSensor:completion:]_block_invoke
+ ___72-[ASMPolarisResourceProvider setAvailabilityForKinoSensor:availability:]_block_invoke
+ ___76+[ASMImageProcessingHelper getPNGDataFromRawImageData:withSensorInfo:error:]_block_invoke
+ ___NSDictionary0__struct
+ ___block_descriptor_40_e5_v8?0l
+ ___objc_personality_v0
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_signpost_emit_with_name_impl
+ _gLogCategory_ASMImageProcessingHelper
+ _gLogCategory_ASMSignpost
+ _kCGColorSpaceExtendedSRGB
+ _kCIFormatL8
+ _kCIFormatRGB16
+ _memcpy
+ _objc_autorelease
+ _objc_enumerationMutation
+ _objc_msgSend$PNGRepresentationOfImage:format:colorSpace:options:
+ _objc_msgSend$addObject:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$asmLogInstance
+ _objc_msgSend$bytes
+ _objc_msgSend$bytesPerPixel
+ _objc_msgSend$context
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createPixelBufferFromRawImageData:withSensorInfo:error:
+ _objc_msgSend$getPNGDataFromRawImageData:withSensorInfo:error:
+ _objc_msgSend$imageWithCVPixelBuffer:
+ _objc_msgSend$kinoCaptureMode
+ _objc_msgSend$kinoSensorInfoWithIdentifier:
+ _objc_msgSend$length
+ _objc_msgSend$outputPixelHeight
+ _objc_msgSend$outputPixelWidth
+ _objc_msgSend$pixelFormat
+ _objc_msgSend$sharedInstance
+ _objc_retainAutorelease
+ _objc_retainBlock
+ _objc_terminate
+ _os_signpost_enabled
CStrings:
+ "+[ASMImageProcessingHelper createPixelBufferFromRawImageData:withSensorInfo:error:]"
+ "-[ASMSignpost beginCaptureSignpostForConfig:]"
+ "0_SignpostActiveE2E"
+ "0_SignpostPassiveE2E"
+ "1_SignpostGATTSignaling"
+ "2_SignpostActiveFirstSliceLeft"
+ "3_SignpostActiveFirstSliceRight"
+ "4_SignpostActiveLastSliceLeft"
+ "5_SignpostActiveLastSliceRight"
+ "6_SignpostActiveInfiltration"
+ "@32@0:8@16^@24"
+ "@40@0:8@16@24^@32"
+ "CVPixelBuffer size %lu less than expected size %lu"
+ "Ignoring extra %lu bytes, assuming it is the footer"
+ "PNGRepresentationOfImage:format:colorSpace:options:"
+ "Raw image data size %lu is less than expected size %u"
+ "Sensor info is not specified"
+ "Starting active capture"
+ "Starting passive capture"
+ "Unable to create CVPixelBuffer"
+ "Unable to find best match format"
+ "^{__CVBuffer=}40@0:8@16@24^@32"
+ "addObject:"
+ "arrayWithObjects:count:"
+ "asmd: B790 GATT confirmation received"
+ "asmd: B790 Start kino request"
+ "asmd: B790 awaiting final slice from left bud"
+ "asmd: B790 awaiting final slice from right bud"
+ "asmd: B790 begin asmd active e2e check"
+ "asmd: B790 begin asmd passive e2e check"
+ "asmd: B790 final slice received from left bud"
+ "asmd: B790 final slice received from right bud"
+ "asmd: B790 first slice from left bud received"
+ "asmd: B790 first slice from right bud received"
+ "asmd: B790 passive e2e complete"
+ "asmd: B790 start image stream failed for left bud"
+ "asmd: B790 start image stream failed for right bud"
+ "asmd: B790 waiting for first left slice"
+ "asmd: B790 waiting for first right slice"
+ "asmd: awaiting Infiltration to begin"
+ "asmd: e2e failed while starting image stream"
+ "beginActiveFirstSliceSignposts"
+ "beginCaptureSignpostForConfig:"
+ "beginGATTSignalingSignpost"
+ "bytes"
+ "bytesPerPixel"
+ "com.apple.AccessorySensorManager"
+ "context"
+ "countByEnumeratingWithState:objects:count:"
+ "createPixelBufferFromRawImageData:withSensorInfo:error:"
+ "endActiveEndToEndSignpostOnError"
+ "endActiveFirstSliceSignpostsOnError"
+ "endGATTSignalingSignpost"
+ "endPassiveEndToEndSignpost"
+ "getPNGDataFromRawImageData:error:"
+ "getPNGDataFromRawImageData:withSensorInfo:error:"
+ "handleImageSliceSignpostForSDU:"
+ "imageWithCVPixelBuffer:"
+ "kinoCaptureMode"
+ "kinoSensorInfoWithIdentifier:"
+ "length"
+ "outputPixelHeight"
+ "outputPixelWidth"
+ "pixelFormat"
+ "publishResourcesForKinoSensor:completion:"
+ "setAvailabilityForKinoSensor:availability:"
+ "v24@0:8^{?={?=C(?=I{?=b1b31})b15b1S}@}16"
+ "v28@0:8@16B24"
+ "v32@0:8@16@?24"
```
