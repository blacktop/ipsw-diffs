## CMImaging

> `/System/Library/PrivateFrameworks/CMImaging.framework/Versions/A/CMImaging`

```diff

-764.21.3.0.0
-  __TEXT.__text: 0x1e23e0
-  __TEXT.__objc_methlist: 0x110f4
-  __TEXT.__cstring: 0x1df10
+764.41.11.0.0
+  __TEXT.__text: 0x1e4a80
+  __TEXT.__objc_methlist: 0x111ac
+  __TEXT.__cstring: 0x1e029
   __TEXT.__const: 0x5400
   __TEXT.__oslogstring: 0x4c3d
   __TEXT.__gcc_except_tab: 0x149c
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x3760
+  __TEXT.__unwind_info: 0x3788
   __TEXT.__eh_frame: 0x608
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x13e8
-  __DATA_CONST.__objc_classlist: 0x760
+  __DATA_CONST.__const: 0x1420
+  __DATA_CONST.__objc_classlist: 0x768
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x77e0
+  __DATA_CONST.__objc_selrefs: 0x7838
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x5c0
+  __DATA_CONST.__objc_superrefs: 0x5c8
   __DATA_CONST.__objc_arraydata: 0x618
-  __DATA_CONST.__got: 0xe18
-  __AUTH_CONST.__const: 0x14e0
-  __AUTH_CONST.__cfstring: 0x8b20
-  __AUTH_CONST.__objc_const: 0x27bc0
+  __DATA_CONST.__got: 0xe68
+  __AUTH_CONST.__const: 0x1510
+  __AUTH_CONST.__cfstring: 0x8d00
+  __AUTH_CONST.__objc_const: 0x27d48
   __AUTH_CONST.__objc_intobj: 0xf00
   __AUTH_CONST.__objc_arrayobj: 0x138
-  __AUTH_CONST.__objc_floatobj: 0xe0
-  __AUTH_CONST.__objc_doubleobj: 0x1300
+  __AUTH_CONST.__objc_floatobj: 0xd0
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0xb38
+  __AUTH_CONST.__objc_doubleobj: 0x1300
+  __AUTH_CONST.__auth_got: 0xb48
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0xcd0
-  __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x2008
-  __DATA.__data: 0x12f90
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x2020
+  __DATA.__data: 0x11948
   __DATA.__common: 0x180
-  __DATA.__bss: 0xc8
-  __DATA_DIRTY.__objc_data: 0x3cf0
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x200
+  __DATA.__bss: 0xb8
+  __DATA_DIRTY.__objc_data: 0x49c0
+  __DATA_DIRTY.__data: 0x1658
+  __DATA_DIRTY.__bss: 0x210
   __DATA_DIRTY.__common: 0x100
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8862
-  Symbols:   13333
-  CStrings:  3730
+  Functions: 8885
+  Symbols:   13391
+  CStrings:  3749
 
Symbols:
+ +[CMIStylesMetadataInterpolator initialize]
+ -[CMILCBDatabase databaseVersion]
+ -[CMILCBDatabase distortion]
+ -[CMILCBDatabase updateDistortion:]
+ -[CMILCBEntry blemishType]
+ -[CMILCBEntry correctionPatch]
+ -[CMILCBEntry decodeCommonFieldsWithCoder:]
+ -[CMILCBEntry decodeCorrectionFeaturesWithCoder:]
+ -[CMILCBEntry decodeV4FieldsWithCoder:]
+ -[CMILCBEntry decodeV5FieldsWithCoder:]
+ -[CMILCBEntry initWithKey:position:radius:defocusRadius:particleDistance:apertureRatio:focusLensPosition:oisShift:opticalCenter:detectionCount:blemishType:lastDetectionGravityVector:lastDetectionTimeStamp:shouldCorrect:correctionFeatures:correctionPatch:]
+ -[CMIStylesMetadataInterpolator .cxx_destruct]
+ -[CMIStylesMetadataInterpolator _smartStyleUtilitiesForFloat16Coefficients:]
+ -[CMIStylesMetadataInterpolator initWithOptionalMetalCommandQueue:]
+ -[CMIStylesMetadataInterpolator init]
+ -[CMIStylesMetadataInterpolator interpolateStylesMetadataFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:]
+ OBJC_IVAR_$_CMILCBDatabase._databaseVersion
+ OBJC_IVAR_$_CMILCBDatabase._distortion
+ OBJC_IVAR_$_CMILCBEntry._blemishType
+ OBJC_IVAR_$_CMILCBEntry._correctionPatch
+ OBJC_IVAR_$_CMIStylesMetadataInterpolator._commandQueue
+ OBJC_IVAR_$_CMIStylesMetadataInterpolator._smartStyleUtilities
+ OBJC_IVAR_$_CMIStylesMetadataInterpolator._smartStyleUtilitiesCreationAttempted
+ _CMIStylesMetadataKey_FaceROIs
+ _CMIStylesMetadataKey_SmartStyleMetadata
+ _CMIStylesMetadataKey_TextureStyleMetadata
+ _CMTimeCompare
+ _OBJC_CLASS_$_CMIStylesMetadataInterpolator
+ _OBJC_METACLASS_$_CMIStylesMetadataInterpolator
+ __OBJC_$_CLASS_METHODS_CMIStylesMetadataInterpolator
+ __OBJC_$_INSTANCE_METHODS_CMIStylesMetadataInterpolator
+ __OBJC_$_INSTANCE_VARIABLES_CMIStylesMetadataInterpolator
+ __OBJC_CLASS_RO_$_CMIStylesMetadataInterpolator
+ __OBJC_METACLASS_RO_$_CMIStylesMetadataInterpolator
+ ___158-[CMIStylesMetadataInterpolator interpolateStylesMetadataFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:]_block_invoke
+ ___158-[CMIStylesMetadataInterpolator interpolateStylesMetadataFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:]_block_invoke_2
+ ___block_descriptor_36_e53_"NSDictionary"24?0"NSDictionary"8"NSDictionary"16l
+ ___block_descriptor_52_e8_32s40s_e28_"NSNumber"16?0"NSString"8l
+ ___smi_interpolateFaceROI_block_invoke
+ _fmodf
+ _kFigCaptureSampleBufferAttachedMediaKey_TextureStyleFaceAttitudeMetadata
+ _kFigCaptureSampleBufferAttachedMediaKey_TextureStyleImageStatistics
+ _kFigCaptureStreamLCBKey_OpticalCenterForLensX
+ _kFigCaptureStreamLCBKey_OpticalCenterForLensY
+ _kFigCaptureStreamLCBKey_RadialDistortionEnabled
+ _kFigCaptureStreamLCBKey_RadialDistortionK1
+ _kFigCaptureStreamLCBKey_RadialDistortionK2
+ _kFigCaptureStreamLCBKey_RadialDistortionK3
+ _kFigCaptureStreamLCBKey_RadialDistortionMaxR
+ _kFigCaptureStreamLCBKey_RadialDistortionRPeak
+ _objc_msgSend$_smartStyleUtilitiesForFloat16Coefficients:
+ _objc_msgSend$blemishType
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$correctionPatch
+ _objc_msgSend$decodeCommonFieldsWithCoder:
+ _objc_msgSend$decodeCorrectionFeaturesWithCoder:
+ _objc_msgSend$decodeV4FieldsWithCoder:
+ _objc_msgSend$decodeV5FieldsWithCoder:
+ _objc_msgSend$initWithKey:position:radius:defocusRadius:particleDistance:apertureRatio:focusLensPosition:oisShift:opticalCenter:detectionCount:blemishType:lastDetectionGravityVector:lastDetectionTimeStamp:shouldCorrect:correctionFeatures:correctionPatch:
+ _objc_msgSend$initWithOptionalMetalCommandQueue:useCase:
+ _objc_msgSend$interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:
+ _objc_msgSend$setCoefficientsPixelBufferPixelFormat:
+ _smi_interpolatePeopleByFaceID
- -[CMILCBEntry initWithKey:position:radius:defocusRadius:particleDistance:apertureRatio:focusLensPosition:oisShift:opticalCenter:detectionCount:relativeToLens:lastDetectionGravityVector:lastDetectionTimeStamp:shouldCorrect:correctionFeatures:]
- -[CMILCBEntry relativeToLens]
- OBJC_IVAR_$_CMILCBEntry._relativeToLens
- _objc_msgSend$initWithKey:position:radius:defocusRadius:particleDistance:apertureRatio:focusLensPosition:oisShift:opticalCenter:detectionCount:relativeToLens:lastDetectionGravityVector:lastDetectionTimeStamp:shouldCorrect:correctionFeatures:
- _objc_msgSend$relativeToLens
CStrings:
+ "@\"NSDictionary\"24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "@\"NSNumber\"16@?0@\"NSString\"8"
+ "BT"
+ "CP"
+ "EV"
+ "[self decodeV4FieldsWithCoder:coder]"
+ "[self decodeV5FieldsWithCoder:coder]"
+ "blemishType"
+ "correctionPatchBytes"
+ "dcx"
+ "dcy"
+ "de"
+ "dk1"
+ "dk2"
+ "dk3"
+ "dmr"
+ "drp"
+ "faceROIs"
+ "smartStyleMetadata"
+ "textureStyleMetadata"
+ "version >= 4 && version <= 6"
+ "\xf0aA"
- "relativeToLens"
- "version == 4"
- "\xf0a"
```
