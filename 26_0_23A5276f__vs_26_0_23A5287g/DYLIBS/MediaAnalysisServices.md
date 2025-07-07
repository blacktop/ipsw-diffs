## MediaAnalysisServices

> `/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices`

```diff

-345.64.1.0.0
-  __TEXT.__text: 0x3a98c
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x4b54
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x3604
-  __TEXT.__gcc_except_tab: 0x4654
-  __TEXT.__oslogstring: 0x214a
-  __TEXT.__dlopen_cstrs: 0x3a5
-  __TEXT.__unwind_info: 0x1b08
-  __TEXT.__objc_classname: 0xe88
-  __TEXT.__objc_methname: 0x80a0
-  __TEXT.__objc_methtype: 0x2299
-  __TEXT.__objc_stubs: 0x2520
-  __DATA_CONST.__got: 0x480
-  __DATA_CONST.__const: 0x9e0
-  __DATA_CONST.__objc_classlist: 0x408
+345.67.3.0.0
+  __TEXT.__text: 0x3cdac
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_methlist: 0x4b34
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x36f0
+  __TEXT.__gcc_except_tab: 0x4814
+  __TEXT.__oslogstring: 0x2333
+  __TEXT.__dlopen_cstrs: 0x417
+  __TEXT.__unwind_info: 0x1b38
+  __TEXT.__objc_classname: 0xe70
+  __TEXT.__objc_methname: 0x82f3
+  __TEXT.__objc_methtype: 0x23f5
+  __TEXT.__objc_stubs: 0x26e0
+  __DATA_CONST.__got: 0x4d0
+  __DATA_CONST.__const: 0xa20
+  __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1768
-  __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x3d8
-  __AUTH_CONST.__auth_got: 0x480
+  __DATA_CONST.__objc_selrefs: 0x17c8
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x3c8
+  __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__const: 0x318
-  __AUTH_CONST.__cfstring: 0x4820
-  __AUTH_CONST.__objc_const: 0x99d8
+  __AUTH_CONST.__cfstring: 0x4860
+  __AUTH_CONST.__objc_const: 0x99f8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_ivar: 0x538
+  __AUTH.__objc_data: 0x1180
+  __DATA.__objc_ivar: 0x548
   __DATA.__data: 0x420
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x1680
   __DATA_DIRTY.__bss: 0x80
+  - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78A58CF1-E4E5-350E-9D2E-5AB4867DA4DD
-  Functions: 1607
-  Symbols:   5810
-  CStrings:  3033
+  UUID: 75397B6F-53AF-3CBA-93BF-BB5228EF8BE2
+  Functions: 1641
+  Symbols:   5930
+  CStrings:  3073
 
Symbols:
+ +[MADVideoSession isValidRegionOfInterest:frameWidth:frameHeight:]
+ +[MADVideoSessionFrameProperties supportsSecureCoding]
+ -[MADPixelBufferProcesser .cxx_construct]
+ -[MADPixelBufferProcesser .cxx_destruct]
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:]
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.1
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.10
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.11
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.12
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.13
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.14
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.15
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.16
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.17
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.18
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.19
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.2
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.20
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.21
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.22
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.23
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.24
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.25
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.26
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.3
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.4
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.5
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.6
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.7
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.8
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.9
+ -[MADPixelBufferProcesser _createPixelBuffer:width:height:format:]
+ -[MADPixelBufferProcesser _createPixelBuffer:width:height:format:].cold.1
+ -[MADPixelBufferProcesser _createPixelBuffer:width:height:format:].cold.2
+ -[MADPixelBufferProcesser processPixelBuffer:orientation:regionOfInterest:scaledWidth:scaledHeight:pixelFormat:output:]
+ -[MADPixelBufferProcesser processPixelBuffer:orientation:regionOfInterest:scaledWidth:scaledHeight:pixelFormat:output:].cold.1
+ -[MADPixelBufferProcesser processPixelBuffer:orientation:regionOfInterest:scaledWidth:scaledHeight:pixelFormat:output:].cold.2
+ -[MADPixelBufferProcesser processPixelBuffer:orientation:regionOfInterest:scaledWidth:scaledHeight:pixelFormat:output:].cold.3
+ -[MADPixelBufferProcesser processPixelBuffer:orientation:regionOfInterest:scaledWidth:scaledHeight:pixelFormat:output:].cold.4
+ -[MADRequest setError:].cold.1
+ -[MADTextInput addEntityUUID:].cold.1
+ -[MADVideoSession preprocessPixelBuffer:orientation:regionOfInterest:output:isProcessed:]
+ -[MADVideoSession preprocessPixelBuffer:orientation:regionOfInterest:output:isProcessed:].cold.1
+ -[MADVideoSession processPixelBuffer:frameProperties:resultHandler:]
+ -[MADVideoSession processPixelBuffer:frameProperties:resultHandler:].cold.1
+ -[MADVideoSession processPixelBuffer:frameProperties:resultHandler:].cold.2
+ -[MADVideoSession processPixelBuffer:frameProperties:resultHandler:].cold.3
+ -[MADVideoSessionFrameProperties description]
+ -[MADVideoSessionFrameProperties encodeWithCoder:]
+ -[MADVideoSessionFrameProperties initWithCoder:]
+ -[MADVideoSessionFrameProperties init]
+ -[MADVideoSessionFrameProperties orientation]
+ -[MADVideoSessionFrameProperties regionOfInterest]
+ -[MADVideoSessionFrameProperties setOrientation:]
+ -[MADVideoSessionFrameProperties setRegionOfInterest:]
+ -[MADVideoSessionFrameProperties setTimestamp:]
+ -[MADVideoSessionFrameProperties timestamp]
+ -[MADVideoSessionSafetyResult confidenceTypeN]
+ GCC_except_table107
+ GCC_except_table82
+ GCC_except_table86
+ GCC_except_table87
+ _CGRectCreateDictionaryRepresentation
+ _CGRectEqualToRect
+ _CGRectIntersection
+ _OBJC_CLASS_$_MADPixelBufferProcesser
+ _OBJC_CLASS_$_MADVideoSessionFrameProperties
+ _OBJC_IVAR_$_MADPixelBufferProcesser._bufferHeight
+ _OBJC_IVAR_$_MADPixelBufferProcesser._bufferWidth
+ _OBJC_IVAR_$_MADPixelBufferProcesser._pixelFormat
+ _OBJC_IVAR_$_MADPixelBufferProcesser._pool
+ _OBJC_IVAR_$_MADPixelBufferProcesser._rotationSession
+ _OBJC_IVAR_$_MADVideoSession._pixelBufferProcessor
+ _OBJC_IVAR_$_MADVideoSessionFrameProperties._orientation
+ _OBJC_IVAR_$_MADVideoSessionFrameProperties._regionOfInterest
+ _OBJC_IVAR_$_MADVideoSessionFrameProperties._timestamp
+ _OBJC_IVAR_$_MADVideoSessionSafetyResult._confidenceTypeN
+ _OBJC_METACLASS_$_MADPixelBufferProcesser
+ _OBJC_METACLASS_$_MADVideoSessionFrameProperties
+ _VTPixelRotationSessionCreate
+ _VTPixelRotationSessionRotateImage
+ __OBJC_$_CLASS_METHODS_MADVideoSessionFrameProperties
+ __OBJC_$_CLASS_PROP_LIST_MADVideoSessionFrameProperties
+ __OBJC_$_INSTANCE_METHODS_MADPixelBufferProcesser
+ __OBJC_$_INSTANCE_METHODS_MADVideoSessionFrameProperties
+ __OBJC_$_INSTANCE_VARIABLES_MADPixelBufferProcesser
+ __OBJC_$_INSTANCE_VARIABLES_MADVideoSessionFrameProperties
+ __OBJC_$_PROP_LIST_MADVideoSessionFrameProperties
+ __OBJC_CLASS_PROTOCOLS_$_MADVideoSessionFrameProperties
+ __OBJC_CLASS_RO_$_MADPixelBufferProcesser
+ __OBJC_CLASS_RO_$_MADVideoSessionFrameProperties
+ __OBJC_METACLASS_RO_$_MADPixelBufferProcesser
+ __OBJC_METACLASS_RO_$_MADVideoSessionFrameProperties
+ __OBJC_PROTOCOL_REFERENCE_$_NSSecureCoding
+ __ZL38audit_stringSensitiveContentAnalysisML
+ __ZN2CFIP28OpaqueVTPixelRotationSessionED2Ev
+ __ZN2CFIPK14__CFDictionaryED2Ev
+ __ZZL37SensitiveContentAnalysisMLLibraryCorePPcE16frameworkLibrary.0
+ __ZZL45getSCMLImageExplicitSensitivityScoreSymbolLocvE3ptr.0
+ ___23-[MADRequest setError:]_block_invoke
+ ___29-[MADVideoSession connection]_block_invoke.202
+ ___29-[MADVideoSession connection]_block_invoke.202.cold.1
+ ___29-[MADVideoSession connection]_block_invoke.203
+ ___33-[MADVideoSession removeRequest:]_block_invoke.217
+ ___36-[MADVideoSession addRequest:error:]_block_invoke.213
+ ___36-[MADVideoSession removeAllRequests]_block_invoke.225
+ ___52-[MADVideoSession _addBackRequestsAfterReconnection]_block_invoke.208
+ ___68-[MADVideoSession processPixelBuffer:frameProperties:resultHandler:]_block_invoke
+ ___68-[MADVideoSession processPixelBuffer:frameProperties:resultHandler:]_block_invoke.235
+ ___68-[MADVideoSession processPixelBuffer:frameProperties:resultHandler:]_block_invoke.cold.1
+ ___95-[MADVideoSession(UserSafety) requestTTRNotificationWithVideoFrames:options:completionHandler:]_block_invoke.281
+ ___Block_byref_object_copy_.232
+ ___Block_byref_object_dispose_.233
+ ____ZL37SensitiveContentAnalysisMLLibraryCorePPc_block_invoke
+ ____ZL45getSCMLImageExplicitSensitivityScoreSymbolLocv_block_invoke
+ ___block_descriptor_40_ea8_32s_e25_v32?0"NSString"816^B24ls32l8
+ ___block_descriptor_64_ea8_32s40s48bs56r_e17_v16?0"NSError"8lr56l8s32l8s48l8s40l8
+ ___block_descriptor_72_ea8_32s40s48bs56r_e39_v48?0"NSArray"8{?=qiIq}16"NSError"40lr56l8s32l8s40l8s48l8
+ _dlerror
+ _dlsym
+ _kCFBooleanFalse
+ _kCMTimeZero
+ _kVTPixelRotationPropertyKey_FlipHorizontalOrientation
+ _kVTPixelRotationPropertyKey_FlipVerticalOrientation
+ _kVTPixelRotationPropertyKey_Rotation
+ _kVTPixelRotationPropertyKey_SetGPUPriorityLow
+ _kVTPixelTransferPropertyKey_DestinationRectangle
+ _kVTPixelTransferPropertyKey_SetGPUPriorityLow
+ _kVTPixelTransferPropertyKey_SourceCropRectangle
+ _kVTRotation_0
+ _kVTRotation_180
+ _kVTRotation_CCW90
+ _kVTRotation_CW90
+ _objc_msgSend$_configurePixelRotationSessionWithOrientation:
+ _objc_msgSend$_createPixelBuffer:width:height:format:
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$decodeCMTimeForKey:
+ _objc_msgSend$domain
+ _objc_msgSend$encodeCMTime:forKey:
+ _objc_msgSend$isValidRegionOfInterest:frameWidth:frameHeight:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$orientation
+ _objc_msgSend$preprocessPixelBuffer:orientation:regionOfInterest:output:isProcessed:
+ _objc_msgSend$processFrameWithIOSurface:frameProperties:reply:
+ _objc_msgSend$processPixelBuffer:frameProperties:resultHandler:
+ _objc_msgSend$processPixelBuffer:orientation:regionOfInterest:scaledWidth:scaledHeight:pixelFormat:output:
+ _objc_msgSend$regionOfInterest
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$setOrientation:
+ _objc_msgSend$setRegionOfInterest:
+ _objc_msgSend$setTimestamp:
+ _objc_msgSend$timestamp
+ _objc_msgSend$userInfo
- +[MADMultiModalInputEntitySegment supportsSecureCoding]
- +[MADTextInputEntitySegment supportsSecureCoding]
- -[MADMultiModalInputEntitySegment .cxx_destruct]
- -[MADMultiModalInputEntitySegment description]
- -[MADMultiModalInputEntitySegment encodeWithCoder:]
- -[MADMultiModalInputEntitySegment entityUUID]
- -[MADMultiModalInputEntitySegment initWithCoder:]
- -[MADMultiModalInputEntitySegment initWithEntityUUID:seed:]
- -[MADMultiModalInputEntitySegment seed]
- -[MADMultiModalInputEntitySegment type]
- -[MADPixelBufferScaler .cxx_construct]
- -[MADPixelBufferScaler .cxx_destruct]
- -[MADPixelBufferScaler initWithTargetWidth:height:format:]
- -[MADPixelBufferScaler scalePixelBuffer:output:]
- -[MADPixelBufferScaler scalePixelBuffer:output:].cold.1
- -[MADPixelBufferScaler scalePixelBuffer:output:].cold.2
- -[MADTextInputEntitySegment .cxx_destruct]
- -[MADTextInputEntitySegment description]
- -[MADTextInputEntitySegment encodeWithCoder:]
- -[MADTextInputEntitySegment entityUUID]
- -[MADTextInputEntitySegment initWithCoder:]
- -[MADTextInputEntitySegment initWithEntityUUID:]
- -[MADTextInputEntitySegment type]
- -[MADVideoSession preprocessPixelBuffer:output:]
- -[MADVideoSession preprocessPixelBuffer:output:].cold.1
- -[MADVideoSession preprocessPixelBuffer:output:].cold.2
- -[MADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:].cold.1
- -[MADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:].cold.2
- GCC_except_table34
- GCC_except_table73
- GCC_except_table74
- _CVBufferPropagateAttachments
- _OBJC_CLASS_$_MADMultiModalInputEntitySegment
- _OBJC_CLASS_$_MADPixelBufferScaler
- _OBJC_CLASS_$_MADTextInputEntitySegment
- _OBJC_IVAR_$_MADMultiModalInputEntitySegment._entityUUID
- _OBJC_IVAR_$_MADMultiModalInputEntitySegment._seed
- _OBJC_IVAR_$_MADPixelBufferScaler._pool
- _OBJC_IVAR_$_MADPixelBufferScaler._transferSession
- _OBJC_IVAR_$_MADTextInputEntitySegment._entityUUID
- _OBJC_IVAR_$_MADVideoSession._scaler
- _OBJC_METACLASS_$_MADMultiModalInputEntitySegment
- _OBJC_METACLASS_$_MADPixelBufferScaler
- _OBJC_METACLASS_$_MADTextInputEntitySegment
- __OBJC_$_CLASS_METHODS_MADMultiModalInputEntitySegment
- __OBJC_$_CLASS_METHODS_MADTextInputEntitySegment
- __OBJC_$_INSTANCE_METHODS_MADMultiModalInputEntitySegment
- __OBJC_$_INSTANCE_METHODS_MADPixelBufferScaler
- __OBJC_$_INSTANCE_METHODS_MADTextInputEntitySegment
- __OBJC_$_INSTANCE_VARIABLES_MADMultiModalInputEntitySegment
- __OBJC_$_INSTANCE_VARIABLES_MADPixelBufferScaler
- __OBJC_$_INSTANCE_VARIABLES_MADTextInputEntitySegment
- __OBJC_$_PROP_LIST_MADMultiModalInputEntitySegment
- __OBJC_$_PROP_LIST_MADTextInputEntitySegment
- __OBJC_CLASS_RO_$_MADMultiModalInputEntitySegment
- __OBJC_CLASS_RO_$_MADPixelBufferScaler
- __OBJC_CLASS_RO_$_MADTextInputEntitySegment
- __OBJC_METACLASS_RO_$_MADMultiModalInputEntitySegment
- __OBJC_METACLASS_RO_$_MADPixelBufferScaler
- __OBJC_METACLASS_RO_$_MADTextInputEntitySegment
- ___29-[MADVideoSession connection]_block_invoke.183
- ___29-[MADVideoSession connection]_block_invoke.183.cold.1
- ___29-[MADVideoSession connection]_block_invoke.184
- ___33-[MADVideoSession removeRequest:]_block_invoke.198
- ___36-[MADVideoSession addRequest:error:]_block_invoke.194
- ___36-[MADVideoSession removeAllRequests]_block_invoke.206
- ___52-[MADVideoSession _addBackRequestsAfterReconnection]_block_invoke.189
- ___74-[MADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:]_block_invoke
- ___74-[MADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:]_block_invoke.216
- ___74-[MADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:]_block_invoke.cold.1
- ___95-[MADVideoSession(UserSafety) requestTTRNotificationWithVideoFrames:options:completionHandler:]_block_invoke.257
- ___Block_byref_object_copy_.213
- ___Block_byref_object_dispose_.214
- ___block_descriptor_80_ea8_32s40bs48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
- ___block_descriptor_92_ea8_32s40bs48r_e39_v48?0"NSArray"8{?=qiIq}16"NSError"40lr48l8s32l8s40l8
- _kVTPixelTransferPropertyKey_ScalingMode
- _objc_msgSend$initWithEntityUUID:
- _objc_msgSend$initWithEntityUUID:seed:
- _objc_msgSend$initWithFaceprint:
- _objc_msgSend$initWithTargetWidth:height:format:
- _objc_msgSend$preprocessPixelBuffer:output:
- _objc_msgSend$processFrameWithIOSurface:orientation:timestamp:reply:
- _objc_msgSend$scalePixelBuffer:output:
CStrings:
+ "%@ Failed configuring pixel rotation Session"
+ "%@ Failed creating pixel rotation Session"
+ "%@ Failed to rotate image"
+ "%@ Failed: CVPixelBuffer creation failure"
+ "%@ Failed: Invalid input region of interest"
+ "%@ Received input frame with orientation %u, timestamp %.4f, ROI [%.2f, %.2f, %.2f, %.2f]"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/Utilities/MADPixelBufferProcesser.mm"
+ "@\"MADPixelBufferProcesser\""
+ "Adding entity multi modal inputs are no longer supported"
+ "Adding entity segment as MADTextInput is no longer supported"
+ "Adding faceprint multi modal inputs are no longer supported"
+ "B40@0:8^{__CVBuffer=}16@24@?32"
+ "B56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16i48i52"
+ "ConfidenceTypeN"
+ "ConfidenceTypeN: %@, "
+ "Invalid orientation: %u"
+ "MADPixelBufferProcesser"
+ "MADPixelBufferProcesser_CreatePixelBuffer"
+ "MADPixelBufferProcesser_ScaleRotate"
+ "MADPixelBufferProcesser_processPixelBuffer"
+ "MADVideoSessionFrameProperties"
+ "NSError does not conform to NSSecureCoding; dropping some keys (%@)"
+ "RegionOfInterest"
+ "SCMLImageExplicitSensitivityScore"
+ "T@\"NSNumber\",R,N,V_confidenceTypeN"
+ "TI,N,V_orientation"
+ "Timestamp"
+ "T{?=qiIq},N,V_timestamp"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_regionOfInterest"
+ "[%@][processPixelBuffer]"
+ "_bufferHeight"
+ "_bufferWidth"
+ "_confidenceTypeN"
+ "_configurePixelRotationSessionWithOrientation:"
+ "_createPixelBuffer:width:height:format:"
+ "_pixelBufferProcessor"
+ "_regionOfInterest"
+ "_rotationSession"
+ "confidenceTypeN"
+ "conformsToProtocol:"
+ "decodeCMTimeForKey:"
+ "encodeCMTime:forKey:"
+ "i20@0:8I16"
+ "i44@0:8^^{__CVBuffer}16Q24Q32I40"
+ "i76@0:8^{__CVBuffer=}16I24{CGRect={CGPoint=dd}{CGSize=dd}}28^^{__CVBuffer}60^B68"
+ "i88@0:8^{__CVBuffer=}16I24{CGRect={CGPoint=dd}{CGSize=dd}}28Q60Q68I76^^{__CVBuffer}80"
+ "isValidRegionOfInterest:frameWidth:frameHeight:"
+ "mutableCopy"
+ "numberWithUnsignedLong:"
+ "orientation: %u"
+ "preprocessPixelBuffer:orientation:regionOfInterest:output:isProcessed:"
+ "processFrameWithIOSurface:frameProperties:reply:"
+ "processPixelBuffer:frameProperties:resultHandler:"
+ "processPixelBuffer:orientation:regionOfInterest:scaledWidth:scaledHeight:pixelFormat:output:"
+ "regionOfInterest"
+ "regionOfInterest: origin(%.4f, %.4f), size(%.4f, %.4f)>"
+ "removeObjectsForKeys:"
+ "setOrientation:"
+ "setRegionOfInterest:"
+ "setTimestamp:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML"
+ "userInfo"
+ "v20@0:8I16"
+ "v32@?0@\"NSString\"8@16^B24"
+ "v40@0:8@\"IOSurface\"16@\"MADVideoSessionFrameProperties\"24@?<v@?@\"NSArray\"{?=qiIq}@\"NSError\">32"
+ "{CF<OpaqueVTPixelRotationSession *>=\"value_\"^{OpaqueVTPixelRotationSession}}"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/Utilities/MADPixelBufferScaler.mm"
- "@\"MADPixelBufferScaler\""
- "@\"NSUUID\""
- "@28@0:8i16i20I24"
- "EntityUUID"
- "MADMultiModalInputEntitySegment"
- "MADPixelBufferScaler"
- "MADTextInputEntitySegment"
- "MADVideoSession_scalePixelBuffer"
- "T@\"NSUUID\",R,N,V_entityUUID"
- "TimestampEpoch"
- "TimestampFlags"
- "TimestampTimescale"
- "TimestampValue"
- "[%@] Failed to create pixelBuffer scaler"
- "_entityUUID"
- "_scaler"
- "entityUUID"
- "entityUUID: %@"
- "entityUUID: %@>"
- "initWithEntityUUID:"
- "initWithEntityUUID:seed:"
- "initWithTargetWidth:height:format:"
- "preprocessPixelBuffer:output:"
- "processFrameWithIOSurface:orientation:timestamp:reply:"
- "scalePixelBuffer:output:"
- "v60@0:8@\"IOSurface\"16I24{?=qiIq}28@?<v@?@\"NSArray\"{?=qiIq}@\"NSError\">52"
- "v60@0:8@16I24{?=qiIq}28@?52"

```
