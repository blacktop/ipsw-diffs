## MediaAnalysisServices

> `/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices`

```diff

-315.3.1.0.0
-  __TEXT.__text: 0x32180
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x42a8
-  __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x2e39
-  __TEXT.__gcc_except_tab: 0x3abc
-  __TEXT.__oslogstring: 0x18cd
-  __TEXT.__dlopen_cstrs: 0x33e
-  __TEXT.__unwind_info: 0x1720
-  __TEXT.__objc_classname: 0xcce
-  __TEXT.__objc_methname: 0x730a
-  __TEXT.__objc_methtype: 0x1e02
-  __TEXT.__objc_stubs: 0x2080
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x800
-  __DATA_CONST.__objc_classlist: 0x390
-  __DATA_CONST.__objc_protolist: 0x48
+345.58.3.0.0
+  __TEXT.__text: 0x3a9b4
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_methlist: 0x4b54
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x3619
+  __TEXT.__gcc_except_tab: 0x4654
+  __TEXT.__oslogstring: 0x214a
+  __TEXT.__dlopen_cstrs: 0x3a5
+  __TEXT.__unwind_info: 0x1b08
+  __TEXT.__objc_classname: 0xe83
+  __TEXT.__objc_methname: 0x80a0
+  __TEXT.__objc_methtype: 0x2299
+  __TEXT.__objc_stubs: 0x2520
+  __DATA_CONST.__got: 0x480
+  __DATA_CONST.__const: 0x9e0
+  __DATA_CONST.__objc_classlist: 0x408
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14b0
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x360
-  __AUTH_CONST.__auth_got: 0x408
-  __AUTH_CONST.__const: 0x2f8
-  __AUTH_CONST.__cfstring: 0x4000
-  __AUTH_CONST.__objc_const: 0x8760
+  __DATA_CONST.__objc_selrefs: 0x1768
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x3d8
+  __AUTH_CONST.__auth_got: 0x480
+  __AUTH_CONST.__const: 0x318
+  __AUTH_CONST.__cfstring: 0x4820
+  __AUTH_CONST.__objc_const: 0x99d8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x480
-  __DATA.__data: 0x360
-  __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_data: 0x1cc0
+  __AUTH.__objc_data: 0x11d0
+  __DATA.__objc_ivar: 0x538
+  __DATA.__data: 0x420
+  __DATA.__bss: 0x80
+  __DATA_DIRTY.__objc_data: 0x1680
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/Frameworks/Vision.framework/Vision
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C540CCB4-B0CD-327D-9AEB-18E8222A6472
-  Functions: 1393
-  Symbols:   5052
-  CStrings:  2657
+  UUID: F769D391-13AA-3D06-93E2-D9B4921D30BE
+  Functions: 1607
+  Symbols:   5810
+  CStrings:  3033
 
Symbols:
+ +[MADRichLabelClassificationRequest supportsSecureCoding]
+ +[MADRichLabelClassificationRequest targetResolution]
+ +[MADRichLabelClassificationResult supportsSecureCoding]
+ +[MADRichLabelClassificationResultItem supportsSecureCoding]
+ +[MADTimer timerWithInterval:unit:oneShot:andBlock:]
+ +[MADTimer timerWithIntervalSeconds:isOneShot:andBlock:]
+ +[MADUserSafetyPolicy supportsSecureCoding]
+ +[MADVideoSession allowedRequestTTRNotificationClasses]
+ +[MADVideoSession allowedResultClasses]
+ +[MADVideoSession configureServerInterface:]
+ +[MADVideoSession enabledQRCodeDetection]
+ +[MADVideoSession enabledVideoSessionXPC]
+ +[MADVideoSession serverProtocol]
+ +[MADVideoSession serviceName]
+ +[MADVideoSession session]
+ +[MADVideoSession session].cold.1
+ +[MADVideoSessionRequest supportsSecureCoding]
+ +[MADVideoSessionResult supportsSecureCoding]
+ +[MADVideoSessionSafetyRequest supportsSecureCoding]
+ +[MADVideoSessionSafetyResult supportsSecureCoding]
+ +[MADVideoSessionTTRFrame supportsSecureCoding]
+ +[MADVideoSessionTTROptions supportsSecureCoding]
+ -[MADCoreMLResult initWithVisionResults:].cold.1
+ -[MADImageEmbeddingRequest embeddingRequestType]
+ -[MADImageEmbeddingRequest setEmbeddingRequestType:]
+ -[MADImageEmbeddingResult initWithVersion:data:type:shape:]
+ -[MADImageSafetyClassificationRequest enableGoreViolenceDetection]
+ -[MADImageSafetyClassificationRequest enableNudityDetection]
+ -[MADImageSafetyClassificationRequest init]
+ -[MADImageSafetyClassificationRequest setEnableGoreViolenceDetection:]
+ -[MADImageSafetyClassificationRequest setEnableNudityDetection:]
+ -[MADImageSafetyClassificationResult initWithIsSensitiveNudity:isSensitiveGoreViolence:]
+ -[MADImageSafetyClassificationResult isSensitiveGoreViolence]
+ -[MADImageSafetyClassificationResult isSensitiveNudity]
+ -[MADPersonIdentificationRequest includePets]
+ -[MADPersonIdentificationRequest setIncludePets:]
+ -[MADPersonIdentificationRequest setUseVIPModel:]
+ -[MADPersonIdentificationRequest useVIPModel]
+ -[MADPersonIdentificationResultItem detectionType]
+ -[MADPersonIdentificationResultItem initWithPersonIdentifier:personName:mdID:detectionType:verified:boundingBox:andConfidence:]
+ -[MADPixelBufferScaler .cxx_construct]
+ -[MADPixelBufferScaler .cxx_destruct]
+ -[MADPixelBufferScaler initWithTargetWidth:height:format:]
+ -[MADPixelBufferScaler scalePixelBuffer:output:]
+ -[MADPixelBufferScaler scalePixelBuffer:output:].cold.1
+ -[MADPixelBufferScaler scalePixelBuffer:output:].cold.2
+ -[MADRichLabelClassificationRequest .cxx_destruct]
+ -[MADRichLabelClassificationRequest description]
+ -[MADRichLabelClassificationRequest domains]
+ -[MADRichLabelClassificationRequest encodeWithCoder:]
+ -[MADRichLabelClassificationRequest initWithCoder:]
+ -[MADRichLabelClassificationRequest richLabelResult]
+ -[MADRichLabelClassificationRequest setDomains:]
+ -[MADRichLabelClassificationResult .cxx_destruct]
+ -[MADRichLabelClassificationResult description]
+ -[MADRichLabelClassificationResult encodeWithCoder:]
+ -[MADRichLabelClassificationResult initWithCoder:]
+ -[MADRichLabelClassificationResult initWithResultItems:]
+ -[MADRichLabelClassificationResult resultItems]
+ -[MADRichLabelClassificationResultItem .cxx_destruct]
+ -[MADRichLabelClassificationResultItem description]
+ -[MADRichLabelClassificationResultItem displayLabel]
+ -[MADRichLabelClassificationResultItem domain]
+ -[MADRichLabelClassificationResultItem encodeWithCoder:]
+ -[MADRichLabelClassificationResultItem initWithCoder:]
+ -[MADRichLabelClassificationResultItem initWithDomain:displayLabel:]
+ -[MADService performRequests:onCGImage:withOrientation:andIdentifier:error:]
+ -[MADService performRequests:onCGImage:withOrientation:andIdentifier:error:].cold.1
+ -[MADService reportMADUserSafetyPolicy:error:]
+ -[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:]
+ -[MADService(Photos) performRequests:onAssetWithLocalIdentifier:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:]
+ -[MADService(UserSafety) registerUserSafetyPolicyUpdateHandler:error:]
+ -[MADService(UserSafety) registerUserSafetyPolicyUpdateHandler:error:].cold.1
+ -[MADService(UserSafety) registerUserSafetyPolicyUpdateHandler:error:].cold.2
+ -[MADServiceProxy reportMADUserSafetyPolicy:error:]
+ -[MADTimer .cxx_destruct]
+ -[MADTimer dealloc]
+ -[MADTimer destroy]
+ -[MADTimer handleTimerEvent]
+ -[MADTimer initWithIntervalNanoseconds:isOneShot:andBlock:]
+ -[MADUserSafetyPolicy description]
+ -[MADUserSafetyPolicy encodeWithCoder:]
+ -[MADUserSafetyPolicy initWithCoder:]
+ -[MADUserSafetyPolicy initWithPolicyType:]
+ -[MADUserSafetyPolicy policyType]
+ -[MADVideoSafetyClassificationRequest enableGoreViolenceDetection]
+ -[MADVideoSafetyClassificationRequest enableNudityDetection]
+ -[MADVideoSafetyClassificationRequest setEnableGoreViolenceDetection:]
+ -[MADVideoSafetyClassificationRequest setEnableNudityDetection:]
+ -[MADVideoSafetyClassificationResult initWithIsSensitiveNudity:isSensitiveGoreViolence:scoresForLabels:]
+ -[MADVideoSafetyClassificationResult isSensitiveGoreViolence]
+ -[MADVideoSafetyClassificationResult isSensitiveNudity]
+ -[MADVideoSession .cxx_destruct]
+ -[MADVideoSession _addBackRequestsAfterReconnection]
+ -[MADVideoSession _removeLocalRequest:]
+ -[MADVideoSession addRequest:error:]
+ -[MADVideoSession addRequest:error:].cold.1
+ -[MADVideoSession connection]
+ -[MADVideoSession dealloc]
+ -[MADVideoSession hasOnlyOneSafetyRquest]
+ -[MADVideoSession initInternal]
+ -[MADVideoSession init]
+ -[MADVideoSession init].cold.1
+ -[MADVideoSession preprocessPixelBuffer:output:]
+ -[MADVideoSession preprocessPixelBuffer:output:].cold.1
+ -[MADVideoSession preprocessPixelBuffer:output:].cold.2
+ -[MADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:]
+ -[MADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:].cold.1
+ -[MADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:].cold.2
+ -[MADVideoSession removeAllRequests]
+ -[MADVideoSession removeAllRequests].cold.1
+ -[MADVideoSession removeRequest:]
+ -[MADVideoSession removeRequest:].cold.1
+ -[MADVideoSession(UserSafety) requestTTRNotificationWithVideoFrames:options:completionHandler:]
+ -[MADVideoSessionPixelBufferPool .cxx_construct]
+ -[MADVideoSessionPixelBufferPool .cxx_destruct]
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:]
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.1
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.2
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.3
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.4
+ -[MADVideoSessionPixelBufferPool init]
+ -[MADVideoSessionProxy .cxx_destruct]
+ -[MADVideoSessionProxy initWithSession:]
+ -[MADVideoSessionRequest .cxx_destruct]
+ -[MADVideoSessionRequest description]
+ -[MADVideoSessionRequest encodeWithCoder:]
+ -[MADVideoSessionRequest initWithCoder:]
+ -[MADVideoSessionRequest init]
+ -[MADVideoSessionRequest requestID]
+ -[MADVideoSessionResult .cxx_destruct]
+ -[MADVideoSessionResult description]
+ -[MADVideoSessionResult encodeWithCoder:]
+ -[MADVideoSessionResult initWithCoder:]
+ -[MADVideoSessionResult initWithRequestID:]
+ -[MADVideoSessionResult requestID]
+ -[MADVideoSessionSafetyRequest description]
+ -[MADVideoSessionSafetyRequest enableDetectionTypeGV]
+ -[MADVideoSessionSafetyRequest enableDetectionTypeN]
+ -[MADVideoSessionSafetyRequest encodeWithCoder:]
+ -[MADVideoSessionSafetyRequest initWithCoder:]
+ -[MADVideoSessionSafetyRequest init]
+ -[MADVideoSessionSafetyRequest setEnableDetectionTypeGV:]
+ -[MADVideoSessionSafetyRequest setEnableDetectionTypeN:]
+ -[MADVideoSessionSafetyResult .cxx_destruct]
+ -[MADVideoSessionSafetyResult analysisResult]
+ -[MADVideoSessionSafetyResult description]
+ -[MADVideoSessionSafetyResult encodeWithCoder:]
+ -[MADVideoSessionSafetyResult initWithCoder:]
+ -[MADVideoSessionSafetyResult initWithSensitivityAttributes:requestID:]
+ -[MADVideoSessionSafetyResult initWithSensitivityAttributes:requestID:].cold.1
+ -[MADVideoSessionTTRFrame .cxx_construct]
+ -[MADVideoSessionTTRFrame .cxx_destruct]
+ -[MADVideoSessionTTRFrame description]
+ -[MADVideoSessionTTRFrame encodeWithCoder:]
+ -[MADVideoSessionTTRFrame initWithCoder:]
+ -[MADVideoSessionTTRFrame initWithPixelBuffer:timestamp:orientation:]
+ -[MADVideoSessionTTRFrame initWithPixelBuffer:timestamp:orientation:].cold.1
+ -[MADVideoSessionTTRFrame orientation]
+ -[MADVideoSessionTTRFrame pixelBuffer]
+ -[MADVideoSessionTTRFrame pixelBuffer].cold.1
+ -[MADVideoSessionTTRFrame timestamp]
+ -[MADVideoSessionTTROptions .cxx_destruct]
+ -[MADVideoSessionTTROptions description]
+ -[MADVideoSessionTTROptions encodeWithCoder:]
+ -[MADVideoSessionTTROptions eventDate]
+ -[MADVideoSessionTTROptions initWithCoder:]
+ -[MADVideoSessionTTROptions setEventDate:]
+ -[MADVideoSessionTTROptions setStartDate:]
+ -[MADVideoSessionTTROptions setStreamID:]
+ -[MADVideoSessionTTROptions startDate]
+ -[MADVideoSessionTTROptions streamID]
+ GCC_except_table101
+ GCC_except_table110
+ GCC_except_table116
+ GCC_except_table125
+ GCC_except_table127
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table130
+ GCC_except_table131
+ GCC_except_table134
+ GCC_except_table144
+ GCC_except_table146
+ GCC_except_table168
+ GCC_except_table170
+ GCC_except_table171
+ GCC_except_table173
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table186
+ GCC_except_table187
+ GCC_except_table44
+ GCC_except_table50
+ GCC_except_table64
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table74
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table99
+ _CVBufferPropagateAttachments
+ _CVPixelBufferGetPixelFormatType
+ _CVPixelBufferPoolCreate
+ _CVPixelBufferPoolCreatePixelBuffer
+ _MADSafetyClassificationGoreViolenceResultKey
+ _MADSafetyClassificationNudityResultKey
+ _OBJC_CLASS_$_MADPixelBufferScaler
+ _OBJC_CLASS_$_MADRichLabelClassificationRequest
+ _OBJC_CLASS_$_MADRichLabelClassificationResult
+ _OBJC_CLASS_$_MADRichLabelClassificationResultItem
+ _OBJC_CLASS_$_MADTimer
+ _OBJC_CLASS_$_MADUserSafetyPolicy
+ _OBJC_CLASS_$_MADVideoSession
+ _OBJC_CLASS_$_MADVideoSessionPixelBufferPool
+ _OBJC_CLASS_$_MADVideoSessionProxy
+ _OBJC_CLASS_$_MADVideoSessionRequest
+ _OBJC_CLASS_$_MADVideoSessionResult
+ _OBJC_CLASS_$_MADVideoSessionSafetyRequest
+ _OBJC_CLASS_$_MADVideoSessionSafetyResult
+ _OBJC_CLASS_$_MADVideoSessionTTRFrame
+ _OBJC_CLASS_$_MADVideoSessionTTROptions
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_MADImageEmbeddingRequest._embeddingRequestType
+ _OBJC_IVAR_$_MADImageSafetyClassificationRequest._enableGoreViolenceDetection
+ _OBJC_IVAR_$_MADImageSafetyClassificationRequest._enableNudityDetection
+ _OBJC_IVAR_$_MADImageSafetyClassificationResult._isSensitiveGoreViolence
+ _OBJC_IVAR_$_MADImageSafetyClassificationResult._isSensitiveNudity
+ _OBJC_IVAR_$_MADPersonIdentificationRequest._includePets
+ _OBJC_IVAR_$_MADPersonIdentificationRequest._useVIPModel
+ _OBJC_IVAR_$_MADPersonIdentificationResultItem._detectionType
+ _OBJC_IVAR_$_MADPixelBufferScaler._pool
+ _OBJC_IVAR_$_MADPixelBufferScaler._transferSession
+ _OBJC_IVAR_$_MADRichLabelClassificationRequest._domains
+ _OBJC_IVAR_$_MADRichLabelClassificationResult._resultItems
+ _OBJC_IVAR_$_MADRichLabelClassificationResultItem._displayLabel
+ _OBJC_IVAR_$_MADRichLabelClassificationResultItem._domain
+ _OBJC_IVAR_$_MADService._userSafetyHandler
+ _OBJC_IVAR_$_MADTimer._active
+ _OBJC_IVAR_$_MADTimer._block
+ _OBJC_IVAR_$_MADTimer._isOneShot
+ _OBJC_IVAR_$_MADTimer._queue
+ _OBJC_IVAR_$_MADTimer._source
+ _OBJC_IVAR_$_MADUserSafetyPolicy._policyType
+ _OBJC_IVAR_$_MADVideoSafetyClassificationRequest._enableGoreViolenceDetection
+ _OBJC_IVAR_$_MADVideoSafetyClassificationRequest._enableNudityDetection
+ _OBJC_IVAR_$_MADVideoSafetyClassificationResult._isSensitiveGoreViolence
+ _OBJC_IVAR_$_MADVideoSafetyClassificationResult._isSensitiveNudity
+ _OBJC_IVAR_$_MADVideoSession._connection
+ _OBJC_IVAR_$_MADVideoSession._connectionQueue
+ _OBJC_IVAR_$_MADVideoSession._pool
+ _OBJC_IVAR_$_MADVideoSession._requests
+ _OBJC_IVAR_$_MADVideoSession._requestsManagementQueue
+ _OBJC_IVAR_$_MADVideoSession._scaler
+ _OBJC_IVAR_$_MADVideoSessionPixelBufferPool._height
+ _OBJC_IVAR_$_MADVideoSessionPixelBufferPool._pixelBufferPool
+ _OBJC_IVAR_$_MADVideoSessionPixelBufferPool._pixelFormat
+ _OBJC_IVAR_$_MADVideoSessionPixelBufferPool._transferSession
+ _OBJC_IVAR_$_MADVideoSessionPixelBufferPool._width
+ _OBJC_IVAR_$_MADVideoSessionProxy._session
+ _OBJC_IVAR_$_MADVideoSessionRequest._requestID
+ _OBJC_IVAR_$_MADVideoSessionResult._requestID
+ _OBJC_IVAR_$_MADVideoSessionSafetyRequest._enableDetectionTypeGV
+ _OBJC_IVAR_$_MADVideoSessionSafetyRequest._enableDetectionTypeN
+ _OBJC_IVAR_$_MADVideoSessionSafetyResult._analysisResult
+ _OBJC_IVAR_$_MADVideoSessionTTRFrame._orientation
+ _OBJC_IVAR_$_MADVideoSessionTTRFrame._pixelBuffer
+ _OBJC_IVAR_$_MADVideoSessionTTRFrame._surface
+ _OBJC_IVAR_$_MADVideoSessionTTRFrame._timestamp
+ _OBJC_IVAR_$_MADVideoSessionTTROptions._eventDate
+ _OBJC_IVAR_$_MADVideoSessionTTROptions._startDate
+ _OBJC_IVAR_$_MADVideoSessionTTROptions._streamID
+ _OBJC_METACLASS_$_MADPixelBufferScaler
+ _OBJC_METACLASS_$_MADRichLabelClassificationRequest
+ _OBJC_METACLASS_$_MADRichLabelClassificationResult
+ _OBJC_METACLASS_$_MADRichLabelClassificationResultItem
+ _OBJC_METACLASS_$_MADTimer
+ _OBJC_METACLASS_$_MADUserSafetyPolicy
+ _OBJC_METACLASS_$_MADVideoSession
+ _OBJC_METACLASS_$_MADVideoSessionPixelBufferPool
+ _OBJC_METACLASS_$_MADVideoSessionProxy
+ _OBJC_METACLASS_$_MADVideoSessionRequest
+ _OBJC_METACLASS_$_MADVideoSessionResult
+ _OBJC_METACLASS_$_MADVideoSessionSafetyRequest
+ _OBJC_METACLASS_$_MADVideoSessionSafetyResult
+ _OBJC_METACLASS_$_MADVideoSessionTTRFrame
+ _OBJC_METACLASS_$_MADVideoSessionTTROptions
+ _OUTLINED_FUNCTION_8
+ _VTPixelTransferSessionCreate
+ _VTPixelTransferSessionTransferImage
+ _VTSessionSetProperty
+ __OBJC_$_CLASS_METHODS_MADRichLabelClassificationRequest
+ __OBJC_$_CLASS_METHODS_MADRichLabelClassificationResult
+ __OBJC_$_CLASS_METHODS_MADRichLabelClassificationResultItem
+ __OBJC_$_CLASS_METHODS_MADTimer
+ __OBJC_$_CLASS_METHODS_MADUserSafetyPolicy
+ __OBJC_$_CLASS_METHODS_MADVideoSession
+ __OBJC_$_CLASS_METHODS_MADVideoSessionRequest
+ __OBJC_$_CLASS_METHODS_MADVideoSessionResult
+ __OBJC_$_CLASS_METHODS_MADVideoSessionSafetyRequest
+ __OBJC_$_CLASS_METHODS_MADVideoSessionSafetyResult
+ __OBJC_$_CLASS_METHODS_MADVideoSessionTTRFrame
+ __OBJC_$_CLASS_METHODS_MADVideoSessionTTROptions
+ __OBJC_$_CLASS_PROP_LIST_MADRichLabelClassificationResultItem
+ __OBJC_$_CLASS_PROP_LIST_MADUserSafetyPolicy
+ __OBJC_$_CLASS_PROP_LIST_MADVideoSessionRequest
+ __OBJC_$_CLASS_PROP_LIST_MADVideoSessionResult
+ __OBJC_$_CLASS_PROP_LIST_MADVideoSessionTTRFrame
+ __OBJC_$_CLASS_PROP_LIST_MADVideoSessionTTROptions
+ __OBJC_$_INSTANCE_METHODS_MADPixelBufferScaler
+ __OBJC_$_INSTANCE_METHODS_MADRichLabelClassificationRequest
+ __OBJC_$_INSTANCE_METHODS_MADRichLabelClassificationResult
+ __OBJC_$_INSTANCE_METHODS_MADRichLabelClassificationResultItem
+ __OBJC_$_INSTANCE_METHODS_MADTimer
+ __OBJC_$_INSTANCE_METHODS_MADUserSafetyPolicy
+ __OBJC_$_INSTANCE_METHODS_MADVideoSession(UserSafety)
+ __OBJC_$_INSTANCE_METHODS_MADVideoSessionPixelBufferPool
+ __OBJC_$_INSTANCE_METHODS_MADVideoSessionProxy
+ __OBJC_$_INSTANCE_METHODS_MADVideoSessionRequest
+ __OBJC_$_INSTANCE_METHODS_MADVideoSessionResult
+ __OBJC_$_INSTANCE_METHODS_MADVideoSessionSafetyRequest
+ __OBJC_$_INSTANCE_METHODS_MADVideoSessionSafetyResult
+ __OBJC_$_INSTANCE_METHODS_MADVideoSessionTTRFrame
+ __OBJC_$_INSTANCE_METHODS_MADVideoSessionTTROptions
+ __OBJC_$_INSTANCE_VARIABLES_MADPixelBufferScaler
+ __OBJC_$_INSTANCE_VARIABLES_MADRichLabelClassificationRequest
+ __OBJC_$_INSTANCE_VARIABLES_MADRichLabelClassificationResult
+ __OBJC_$_INSTANCE_VARIABLES_MADRichLabelClassificationResultItem
+ __OBJC_$_INSTANCE_VARIABLES_MADTimer
+ __OBJC_$_INSTANCE_VARIABLES_MADUserSafetyPolicy
+ __OBJC_$_INSTANCE_VARIABLES_MADVideoSession
+ __OBJC_$_INSTANCE_VARIABLES_MADVideoSessionPixelBufferPool
+ __OBJC_$_INSTANCE_VARIABLES_MADVideoSessionProxy
+ __OBJC_$_INSTANCE_VARIABLES_MADVideoSessionRequest
+ __OBJC_$_INSTANCE_VARIABLES_MADVideoSessionResult
+ __OBJC_$_INSTANCE_VARIABLES_MADVideoSessionSafetyRequest
+ __OBJC_$_INSTANCE_VARIABLES_MADVideoSessionSafetyResult
+ __OBJC_$_INSTANCE_VARIABLES_MADVideoSessionTTRFrame
+ __OBJC_$_INSTANCE_VARIABLES_MADVideoSessionTTROptions
+ __OBJC_$_PROP_LIST_MADRichLabelClassificationRequest
+ __OBJC_$_PROP_LIST_MADRichLabelClassificationResult
+ __OBJC_$_PROP_LIST_MADRichLabelClassificationResultItem
+ __OBJC_$_PROP_LIST_MADUserSafetyPolicy
+ __OBJC_$_PROP_LIST_MADVideoSessionRequest
+ __OBJC_$_PROP_LIST_MADVideoSessionResult
+ __OBJC_$_PROP_LIST_MADVideoSessionSafetyRequest
+ __OBJC_$_PROP_LIST_MADVideoSessionSafetyResult
+ __OBJC_$_PROP_LIST_MADVideoSessionTTRFrame
+ __OBJC_$_PROP_LIST_MADVideoSessionTTROptions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MADVideoSessionServerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VCPMediaAnalysisClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MADVideoSessionServerProtocol
+ __OBJC_CLASS_PROTOCOLS_$_MADRichLabelClassificationResultItem
+ __OBJC_CLASS_PROTOCOLS_$_MADUserSafetyPolicy
+ __OBJC_CLASS_PROTOCOLS_$_MADVideoSession
+ __OBJC_CLASS_PROTOCOLS_$_MADVideoSessionProxy
+ __OBJC_CLASS_PROTOCOLS_$_MADVideoSessionRequest
+ __OBJC_CLASS_PROTOCOLS_$_MADVideoSessionResult
+ __OBJC_CLASS_PROTOCOLS_$_MADVideoSessionTTRFrame
+ __OBJC_CLASS_PROTOCOLS_$_MADVideoSessionTTROptions
+ __OBJC_CLASS_RO_$_MADPixelBufferScaler
+ __OBJC_CLASS_RO_$_MADRichLabelClassificationRequest
+ __OBJC_CLASS_RO_$_MADRichLabelClassificationResult
+ __OBJC_CLASS_RO_$_MADRichLabelClassificationResultItem
+ __OBJC_CLASS_RO_$_MADTimer
+ __OBJC_CLASS_RO_$_MADUserSafetyPolicy
+ __OBJC_CLASS_RO_$_MADVideoSession
+ __OBJC_CLASS_RO_$_MADVideoSessionPixelBufferPool
+ __OBJC_CLASS_RO_$_MADVideoSessionProxy
+ __OBJC_CLASS_RO_$_MADVideoSessionRequest
+ __OBJC_CLASS_RO_$_MADVideoSessionResult
+ __OBJC_CLASS_RO_$_MADVideoSessionSafetyRequest
+ __OBJC_CLASS_RO_$_MADVideoSessionSafetyResult
+ __OBJC_CLASS_RO_$_MADVideoSessionTTRFrame
+ __OBJC_CLASS_RO_$_MADVideoSessionTTROptions
+ __OBJC_LABEL_PROTOCOL_$_MADVideoSessionClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_MADVideoSessionServerProtocol
+ __OBJC_METACLASS_RO_$_MADPixelBufferScaler
+ __OBJC_METACLASS_RO_$_MADRichLabelClassificationRequest
+ __OBJC_METACLASS_RO_$_MADRichLabelClassificationResult
+ __OBJC_METACLASS_RO_$_MADRichLabelClassificationResultItem
+ __OBJC_METACLASS_RO_$_MADTimer
+ __OBJC_METACLASS_RO_$_MADUserSafetyPolicy
+ __OBJC_METACLASS_RO_$_MADVideoSession
+ __OBJC_METACLASS_RO_$_MADVideoSessionPixelBufferPool
+ __OBJC_METACLASS_RO_$_MADVideoSessionProxy
+ __OBJC_METACLASS_RO_$_MADVideoSessionRequest
+ __OBJC_METACLASS_RO_$_MADVideoSessionResult
+ __OBJC_METACLASS_RO_$_MADVideoSessionSafetyRequest
+ __OBJC_METACLASS_RO_$_MADVideoSessionSafetyResult
+ __OBJC_METACLASS_RO_$_MADVideoSessionTTRFrame
+ __OBJC_METACLASS_RO_$_MADVideoSessionTTROptions
+ __OBJC_PROTOCOL_$_MADVideoSessionClientProtocol
+ __OBJC_PROTOCOL_$_MADVideoSessionServerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_MADVideoSessionClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_MADVideoSessionServerProtocol
+ __ZL17MADQoSDescription11qos_class_t
+ __ZL29getSCSensitivityAnalysisClassv
+ __ZL36audit_stringSensitiveContentAnalysis
+ __ZL40CGImage_CreateCVPixelBufferWithTransformP7CGImagePP10__CVBufferj26CGImagePropertyOrientationd.cold.6
+ __ZL40CGImage_CreateCVPixelBufferWithTransformP7CGImagePP10__CVBufferj26CGImagePropertyOrientationd.cold.7
+ __ZN17CVPixelBufferLockD2Ev
+ __ZN17CVPixelBufferLockD2Ev.cold.1
+ __ZN2CFIP10__CVBufferEaSEOS2_
+ __ZN2CFIP19__CVPixelBufferPoolED2Ev
+ __ZN2CFIP28OpaqueVTPixelTransferSessionED2Ev
+ __ZZ52+[MADTimer timerWithInterval:unit:oneShot:andBlock:]E11kTimeScaler
+ __ZZL29getSCSensitivityAnalysisClassvE9softClass.0
+ __ZZL35SensitiveContentAnalysisLibraryCorePPcE16frameworkLibrary.0
+ ___100-[MADService performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:completionHandler:]_block_invoke.101
+ ___100-[MADService(Photos) requestApplicationDataFolderIdentifierVisionServiceWithPhotosLibraryURL:error:]_block_invoke.228
+ ___100-[MADService(Photos) requestApplicationDataFolderIdentifierVisionServiceWithPhotosLibraryURL:error:]_block_invoke.228.cold.1
+ ___101-[MADService(Spotlight) submitSpotlightAssetURL:uniqueIdentifier:bundleIdentifier:completionHandler:]_block_invoke.350
+ ___105-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:error:]_block_invoke.185
+ ___105-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:error:]_block_invoke.185.cold.1
+ ___109-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:completionHandler:]_block_invoke.198
+ ___122-[MADService(Photos) _performRequests:onIOSurface:withOrientation:assetLocalIdentifier:photoLibraryURL:completionHandler:]_block_invoke.186
+ ___123-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:resultHandler:completionHandler:]_block_invoke.199
+ ___123-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:resultHandler:completionHandler:]_block_invoke.199.cold.1
+ ___123-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:resultHandler:completionHandler:]_block_invoke.200
+ ___133-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:]_block_invoke
+ ___133-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:]_block_invoke.183
+ ___133-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:]_block_invoke.183.cold.1
+ ___133-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:]_block_invoke.184
+ ___133-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:]_block_invoke.cold.1
+ ___24-[MADService connection]_block_invoke.63
+ ___24-[MADService connection]_block_invoke.63.cold.1
+ ___24-[MADService connection]_block_invoke.64
+ ___29-[MADVideoSession connection]_block_invoke
+ ___29-[MADVideoSession connection]_block_invoke.183
+ ___29-[MADVideoSession connection]_block_invoke.183.cold.1
+ ___29-[MADVideoSession connection]_block_invoke.184
+ ___29-[MADVideoSession connection]_block_invoke_2
+ ___33-[MADVideoSession removeRequest:]_block_invoke
+ ___33-[MADVideoSession removeRequest:]_block_invoke.198
+ ___33-[MADVideoSession removeRequest:]_block_invoke.cold.1
+ ___36-[MADVideoSession addRequest:error:]_block_invoke
+ ___36-[MADVideoSession addRequest:error:]_block_invoke.194
+ ___36-[MADVideoSession addRequest:error:]_block_invoke.cold.1
+ ___36-[MADVideoSession addRequest:error:]_block_invoke_2
+ ___36-[MADVideoSession removeAllRequests]_block_invoke
+ ___36-[MADVideoSession removeAllRequests]_block_invoke.206
+ ___36-[MADVideoSession removeAllRequests]_block_invoke.cold.1
+ ___37-[MADService currentOutstandingTasks]_block_invoke.110
+ ___39-[MADVideoSession _removeLocalRequest:]_block_invoke
+ ___41-[MADVideoSession hasOnlyOneSafetyRquest]_block_invoke
+ ___44-[MADService(UserSafety) userSafetyEnabled:]_block_invoke.305
+ ___52-[MADVideoSession _addBackRequestsAfterReconnection]_block_invoke
+ ___52-[MADVideoSession _addBackRequestsAfterReconnection]_block_invoke.189
+ ___52-[MADVideoSession _addBackRequestsAfterReconnection]_block_invoke_2
+ ___52-[MADVideoSession _addBackRequestsAfterReconnection]_block_invoke_2.cold.1
+ ___55-[MADService(Performance) queryPerformanceMeasurements]_block_invoke.269
+ ___59-[MADTimer initWithIntervalNanoseconds:isOneShot:andBlock:]_block_invoke
+ ___62-[MADService performRequests:onImageURL:withIdentifier:error:]_block_invoke.100
+ ___62-[MADService performRequests:onImageURL:withIdentifier:error:]_block_invoke.100.cold.1
+ ___63-[MADService(Spotlight) prewarmTextRequests:completionHandler:]_block_invoke.338
+ ___64-[MADService(Photos) requestVUIndexURLForPhotoLibraryURL:error:]_block_invoke.209
+ ___64-[MADService(Photos) requestVUIndexURLForPhotoLibraryURL:error:]_block_invoke.209.cold.1
+ ___64-[MADService(Photos) requestVUIndexURLForPhotoLibraryURL:error:]_block_invoke.209.cold.2
+ ___70-[MADService(MultiModal) prewarmMultiModalRequests:completionHandler:]_block_invoke.359
+ ___70-[MADService(Spotlight) performRequests:textInputs:completionHandler:]_block_invoke.342
+ ___70-[MADService(UserSafety) registerUserSafetyPolicyUpdateHandler:error:]_block_invoke
+ ___70-[MADService(UserSafety) registerUserSafetyPolicyUpdateHandler:error:]_block_invoke.307
+ ___70-[MADService(UserSafety) registerUserSafetyPolicyUpdateHandler:error:]_block_invoke.cold.1
+ ___74-[MADService performRequests:onImageURL:withIdentifier:completionHandler:]_block_invoke.99
+ ___74-[MADService(Photos) queryVUIndexAssetCountForType:photoLibraryURL:error:]_block_invoke.221
+ ___74-[MADService(Photos) queryVUIndexAssetCountForType:photoLibraryURL:error:]_block_invoke.221.cold.1
+ ___74-[MADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:]_block_invoke
+ ___74-[MADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:]_block_invoke.216
+ ___74-[MADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:]_block_invoke.cold.1
+ ___76-[MADService performRequests:onCGImage:withOrientation:andIdentifier:error:]_block_invoke
+ ___76-[MADService performRequests:onCGImage:withOrientation:andIdentifier:error:]_block_invoke.90
+ ___76-[MADService performRequests:onCGImage:withOrientation:andIdentifier:error:]_block_invoke.90.cold.1
+ ___76-[MADService performRequests:onCGImage:withOrientation:andIdentifier:error:]_block_invoke.cold.1
+ ___76-[MADService(Photos) performRequestsWithCloudIdentifiers:completionHandler:]_block_invoke.191
+ ___76-[MADService(Photos) performRequestsWithCloudIdentifiers:completionHandler:]_block_invoke.192
+ ___76-[MADService(Photos) queryImagePriority1MCEnableDate:photoLibraryURL:error:]_block_invoke.227
+ ___76-[MADService(Photos) queryImagePriority1MCEnableDate:photoLibraryURL:error:]_block_invoke.227.cold.1
+ ___77-[MADService(MultiModal) performRequests:multiModalInputs:completionHandler:]_block_invoke.360
+ ___80-[MADService(Photos) queryVUIndexLastFullModeClusterDate:photoLibraryURL:error:]_block_invoke.224
+ ___80-[MADService(Photos) queryVUIndexLastFullModeClusterDate:photoLibraryURL:error:]_block_invoke.224.cold.1
+ ___83-[MADService(Photos) performRequests:onAssetWithCloudIdentifier:completionHandler:]_block_invoke.190
+ ___84-[MADService performRequests:videoURL:identifier:progressHandler:completionHandler:]_block_invoke.103
+ ___86-[MADService(Photos) queryVUIndexAssetCountForType:photoLibraryURL:completionHandler:]_block_invoke.223
+ ___88-[MADService performRequests:onCGImage:withOrientation:andIdentifier:completionHandler:]_block_invoke.83
+ ___88-[MADService performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:error:]_block_invoke.102
+ ___88-[MADService performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:error:]_block_invoke.102.cold.1
+ ___92-[MADService performRequests:onPixelBuffer:withOrientation:andIdentifier:completionHandler:]_block_invoke.81
+ ___95-[MADService(Photos) queryVUIndexLastFullModeClusterDateWithPhotoLibraryURL:completionHandler:]_block_invoke.226
+ ___95-[MADVideoSession(UserSafety) requestTTRNotificationWithVideoFrames:options:completionHandler:]_block_invoke
+ ___95-[MADVideoSession(UserSafety) requestTTRNotificationWithVideoFrames:options:completionHandler:]_block_invoke.257
+ ___95-[MADVideoSession(UserSafety) requestTTRNotificationWithVideoFrames:options:completionHandler:]_block_invoke.cold.1
+ ___Block_byref_object_copy_.213
+ ___Block_byref_object_copy_.72
+ ___Block_byref_object_dispose_.214
+ ___Block_byref_object_dispose_.73
+ ____ZL29getSCSensitivityAnalysisClassv_block_invoke
+ ____ZL29getSCSensitivityAnalysisClassv_block_invoke.cold.1
+ ____ZL35SensitiveContentAnalysisLibraryCorePPc_block_invoke
+ ___block_descriptor_40_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_44_ea8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_ea8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_52_ea8_32bs40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_56_ea8_32s40bs48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40bs48r_e20_v20?0B8"NSError"12lr48l8s32l8s40l8
+ ___block_descriptor_76_ea8_32s40s48bs56r_e29_v24?0"NSArray"8"NSError"16lr56l8s32l8s40l8s48l8
+ ___block_descriptor_80_ea8_32s40bs48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
+ ___block_descriptor_92_ea8_32s40bs48r_e39_v48?0"NSArray"8{?=qiIq}16"NSError"40lr48l8s32l8s40l8
+ ___block_literal_global.105
+ ___block_literal_global.107
+ ___block_literal_global.109
+ ___block_literal_global.202
+ ___block_literal_global.268
+ ___block_literal_global.272
+ ___block_literal_global.304
+ ___block_literal_global.317
+ ___block_literal_global.319
+ ___block_literal_global.321
+ ___block_literal_global.323
+ ___block_literal_global.325
+ ___block_literal_global.62
+ ___block_literal_global.67
+ ___block_literal_global.71
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_time
+ _kCVPixelBufferExtendedPixelsBottomKey
+ _kCVPixelBufferExtendedPixelsRightKey
+ _kCVPixelBufferHeightKey
+ _kCVPixelBufferPixelFormatTypeKey
+ _kCVPixelBufferWidthKey
+ _kVTPixelTransferPropertyKey_ScalingMode
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_addBackRequestsAfterReconnection
+ _objc_msgSend$_removeLocalRequest:
+ _objc_msgSend$addRequest:reply:
+ _objc_msgSend$allowedRequestTTRNotificationClasses
+ _objc_msgSend$allowedResultClasses
+ _objc_msgSend$boolValue
+ _objc_msgSend$copyPixelBuffer:toPixelBuffer:
+ _objc_msgSend$date
+ _objc_msgSend$destroy
+ _objc_msgSend$enabledQRCodeDetection
+ _objc_msgSend$enabledVideoSessionXPC
+ _objc_msgSend$handleTimerEvent
+ _objc_msgSend$hasOnlyOneSafetyRquest
+ _objc_msgSend$initWithIntervalNanoseconds:isOneShot:andBlock:
+ _objc_msgSend$initWithPixelBufferClassificationDictionary:error:
+ _objc_msgSend$initWithSession:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithTargetWidth:height:format:
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:
+ _objc_msgSend$preprocessPixelBuffer:output:
+ _objc_msgSend$processFrameWithIOSurface:orientation:timestamp:reply:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeAllRequests
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$removeRequest:reply:
+ _objc_msgSend$reportMADUserSafetyPolicy:error:
+ _objc_msgSend$requestID
+ _objc_msgSend$requestTTRNotificationWithVideoFrames:options:reply:
+ _objc_msgSend$scalePixelBuffer:output:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$subscribeUserSafety:
+ _objc_msgSend$timerWithInterval:unit:oneShot:andBlock:
+ _objc_retain_x9
+ _qos_class_self
- -[MADImageSafetyClassificationResult attributes]
- -[MADImageSafetyClassificationResult initWithIsSensitive:andAttributes:]
- -[MADPersonIdentificationResultItem initWithPersonIdentifier:personName:mdID:verified:boundingBox:andConfidence:]
- -[MADVideoSafetyClassificationResult initWithIsSensitive:scoresForLabels:]
- GCC_except_table107
- GCC_except_table109
- GCC_except_table118
- GCC_except_table136
- GCC_except_table137
- GCC_except_table138
- GCC_except_table141
- GCC_except_table143
- GCC_except_table147
- GCC_except_table151
- GCC_except_table153
- GCC_except_table155
- GCC_except_table157
- GCC_except_table159
- GCC_except_table161
- GCC_except_table164
- GCC_except_table49
- GCC_except_table71
- GCC_except_table75
- GCC_except_table80
- GCC_except_table81
- GCC_except_table82
- GCC_except_table86
- GCC_except_table87
- _OBJC_IVAR_$_MADImageSafetyClassificationResult._attributes
- _OBJC_IVAR_$_MADImageSafetyClassificationResult._isSensitive
- _OBJC_IVAR_$_MADVideoSafetyClassificationResult._isSensitive
- __ZN17CVPixelBufferLockD1Ev
- __ZN17CVPixelBufferLockD1Ev.cold.1
- ___100-[MADService performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:completionHandler:]_block_invoke.94
- ___100-[MADService(Photos) requestApplicationDataFolderIdentifierVisionServiceWithPhotosLibraryURL:error:]_block_invoke.211
- ___100-[MADService(Photos) requestApplicationDataFolderIdentifierVisionServiceWithPhotosLibraryURL:error:]_block_invoke.211.cold.1
- ___101-[MADService(Spotlight) submitSpotlightAssetURL:uniqueIdentifier:bundleIdentifier:completionHandler:]_block_invoke.322
- ___105-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:error:]_block_invoke.168
- ___105-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:error:]_block_invoke.168.cold.1
- ___109-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:completionHandler:]_block_invoke.181
- ___117-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:completionHandler:]_block_invoke
- ___117-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:completionHandler:]_block_invoke.167
- ___117-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:completionHandler:]_block_invoke.cold.1
- ___122-[MADService(Photos) _performRequests:onIOSurface:withOrientation:assetLocalIdentifier:photoLibraryURL:completionHandler:]_block_invoke.169
- ___123-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:resultHandler:completionHandler:]_block_invoke.182
- ___123-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:resultHandler:completionHandler:]_block_invoke.182.cold.1
- ___123-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:resultHandler:completionHandler:]_block_invoke.183
- ___24-[MADService connection]_block_invoke.60
- ___24-[MADService connection]_block_invoke.60.cold.1
- ___24-[MADService connection]_block_invoke.61
- ___37-[MADService currentOutstandingTasks]_block_invoke.103
- ___44-[MADService(UserSafety) userSafetyEnabled:]_block_invoke.284
- ___55-[MADService(Performance) queryPerformanceMeasurements]_block_invoke.248
- ___62-[MADService performRequests:onImageURL:withIdentifier:error:]_block_invoke.93
- ___62-[MADService performRequests:onImageURL:withIdentifier:error:]_block_invoke.93.cold.1
- ___63-[MADService(Spotlight) prewarmTextRequests:completionHandler:]_block_invoke.310
- ___64-[MADService(Photos) requestVUIndexURLForPhotoLibraryURL:error:]_block_invoke.192
- ___64-[MADService(Photos) requestVUIndexURLForPhotoLibraryURL:error:]_block_invoke.192.cold.1
- ___64-[MADService(Photos) requestVUIndexURLForPhotoLibraryURL:error:]_block_invoke.192.cold.2
- ___70-[MADService(MultiModal) prewarmMultiModalRequests:completionHandler:]_block_invoke.331
- ___70-[MADService(Spotlight) performRequests:textInputs:completionHandler:]_block_invoke.314
- ___74-[MADService performRequests:onImageURL:withIdentifier:completionHandler:]_block_invoke.92
- ___74-[MADService(Photos) queryVUIndexAssetCountForType:photoLibraryURL:error:]_block_invoke.204
- ___74-[MADService(Photos) queryVUIndexAssetCountForType:photoLibraryURL:error:]_block_invoke.204.cold.1
- ___76-[MADService(Photos) performRequestsWithCloudIdentifiers:completionHandler:]_block_invoke.174
- ___76-[MADService(Photos) performRequestsWithCloudIdentifiers:completionHandler:]_block_invoke.175
- ___76-[MADService(Photos) queryImagePriority1MCEnableDate:photoLibraryURL:error:]_block_invoke.210
- ___76-[MADService(Photos) queryImagePriority1MCEnableDate:photoLibraryURL:error:]_block_invoke.210.cold.1
- ___77-[MADService(MultiModal) performRequests:multiModalInputs:completionHandler:]_block_invoke.332
- ___80-[MADService(Photos) queryVUIndexLastFullModeClusterDate:photoLibraryURL:error:]_block_invoke.207
- ___80-[MADService(Photos) queryVUIndexLastFullModeClusterDate:photoLibraryURL:error:]_block_invoke.207.cold.1
- ___83-[MADService(Photos) performRequests:onAssetWithCloudIdentifier:completionHandler:]_block_invoke.173
- ___84-[MADService performRequests:videoURL:identifier:progressHandler:completionHandler:]_block_invoke.96
- ___86-[MADService(Photos) queryVUIndexAssetCountForType:photoLibraryURL:completionHandler:]_block_invoke.206
- ___88-[MADService performRequests:onCGImage:withOrientation:andIdentifier:completionHandler:]_block_invoke.80
- ___88-[MADService performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:error:]_block_invoke.95
- ___88-[MADService performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:error:]_block_invoke.95.cold.1
- ___92-[MADService performRequests:onPixelBuffer:withOrientation:andIdentifier:completionHandler:]_block_invoke.78
- ___95-[MADService(Photos) queryVUIndexLastFullModeClusterDateWithPhotoLibraryURL:completionHandler:]_block_invoke.209
- ___Block_byref_object_copy_.69
- ___Block_byref_object_dispose_.70
- ___block_descriptor_56_ea8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_literal_global.100
- ___block_literal_global.102
- ___block_literal_global.185
- ___block_literal_global.247
- ___block_literal_global.251
- ___block_literal_global.283
- ___block_literal_global.289
- ___block_literal_global.291
- ___block_literal_global.293
- ___block_literal_global.295
- ___block_literal_global.297
- ___block_literal_global.59
- ___block_literal_global.64
- ___block_literal_global.68
- ___block_literal_global.98
- _objc_msgSend$performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:completionHandler:
CStrings:
+ "%@ Error connecting to video session - %@"
+ "%@ Error connecting to video session, error: %@"
+ "%@ Failed adding request with requestID: %@, error: %@"
+ "%@ Failed preprocessing input pixel buffer"
+ "%@ Failed removing all requests, error: %@"
+ "%@ Failed removing request with requestID: %@, error: %@"
+ "%@ Failed the removing local request, requestID: %@"
+ "%@ Failed to get IOSurface for pixel buffer"
+ "%@ Finish adding request, requestID: %@ ..."
+ "%@ Finish processing pixel buffer ..."
+ "%@ Finish removeAllRequests ..."
+ "%@ Finish removing request, requestID: %@ ..."
+ "%@ Finish request tap to radar notification..."
+ "%@ Start adding request, requestID: %@ ..."
+ "%@ Start processing pixel buffer ..."
+ "%@ Start removing all requests ..."
+ "%@ Start removing request, requestID: %@ ..."
+ ", enableGoreViolenceDetection: %@"
+ ", enableNudityDetection: %@"
+ ", isSensitiveGoreViolence: %@"
+ ", isSensitiveNudity: %@"
+ ", scoresForLabels: %@"
+ "./Utilities/CGUtilities.h"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysisServices/ComputeService/MADCoreMLResult.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/MADVideoSession.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/Utilities/MADPixelBufferScaler.mm"
+ "@\"MADPixelBufferScaler\""
+ "@\"MADVideoSession\""
+ "@\"MADVideoSessionPixelBufferPool\""
+ "@\"NSDate\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@\"SCSensitivityAnalysis\""
+ "@24@0:8q16"
+ "@28@0:8i16i20I24"
+ "@32@0:8Q16@24"
+ "@36@0:8Q16B24@?28"
+ "@44@0:8Q16Q24B32@?36"
+ "@52@0:8^{__CVBuffer=}16{?=qiIq}24I48"
+ "@84@0:8@16@24@32s40B44{CGRect={CGPoint=dd}{CGSize=dd}}48f80"
+ "@?"
+ "AB"
+ "AnalysisResult"
+ "AnalysisResult: %@, "
+ "B24@0:8@16"
+ "B32@0:8@?16^@24"
+ "B52@0:8@16^{CGImage=}24I32@36^@44"
+ "B60@0:8^{__CVBuffer=}16{?=qiIq}24I48@?52"
+ "Background"
+ "Default"
+ "DetectionType"
+ "Embedding shape %@ inconsistent with embedding data size:%lu"
+ "EnableDetectionTypeGV"
+ "EnableDetectionTypeGV: %@, "
+ "EnableDetectionTypeN"
+ "EnableDetectionTypeN: %@, "
+ "EnableGoreViolenceDetection"
+ "EnableNudityDetection"
+ "Error creating CVPixelBuffer from non-IOSurface-backed CGImage"
+ "EventDate"
+ "Failed to get IOSurface from CVPixelBuffer"
+ "I"
+ "I16@0:8"
+ "IncludePets"
+ "IsSensitiveGoreViolence"
+ "IsSensitiveNudity"
+ "MADPixelBufferScaler"
+ "MADRichLabelClassificationRequest"
+ "MADRichLabelClassificationResult"
+ "MADRichLabelClassificationResultItem"
+ "MADTimer"
+ "MADUserSafetyPolicy"
+ "MADVideoSession"
+ "MADVideoSession.connectionQueue"
+ "MADVideoSession.requestsManagemenQueue"
+ "MADVideoSessionClientProtocol"
+ "MADVideoSessionPixelBufferPool"
+ "MADVideoSessionProxy"
+ "MADVideoSessionRequest"
+ "MADVideoSessionResult"
+ "MADVideoSessionSafetyRequest"
+ "MADVideoSessionSafetyResult"
+ "MADVideoSessionServerProtocol"
+ "MADVideoSessionTTRFrame"
+ "MADVideoSessionTTROptions"
+ "MADVideoSession_processPixelBuffer"
+ "MADVideoSession_requestTTRNotification"
+ "MADVideoSession_scalePixelBuffer"
+ "MD5TextCalibrationV3"
+ "Orientation"
+ "PolicyType"
+ "RequestID"
+ "RequestID: %@>"
+ "SCSensitivityAnalysis"
+ "SearchUnifiedEmbeddingMD6"
+ "SensitiveContentAnalysisTestMode"
+ "StartDate"
+ "StreamID"
+ "T@\"MADRichLabelClassificationResult\",R,N"
+ "T@\"NSDate\",&,N,V_eventDate"
+ "T@\"NSDate\",&,N,V_startDate"
+ "T@\"NSIndexSet\",&,N,V_domains"
+ "T@\"NSNumber\",R,N,V_isSensitiveGoreViolence"
+ "T@\"NSNumber\",R,N,V_isSensitiveNudity"
+ "T@\"NSString\",&,N,V_streamID"
+ "T@\"NSString\",R,N,V_requestID"
+ "T@\"SCSensitivityAnalysis\",R,N,V_analysisResult"
+ "TB,N,V_enableDetectionTypeGV"
+ "TB,N,V_enableDetectionTypeN"
+ "TB,N,V_enableGoreViolenceDetection"
+ "TB,N,V_enableNudityDetection"
+ "TB,N,V_includePets"
+ "TB,N,V_useVIPModel"
+ "TI,R,N,V_orientation"
+ "TQ,R,N,V_domain"
+ "TimestampEpoch"
+ "TimestampFlags"
+ "TimestampTimescale"
+ "TimestampValue"
+ "Tq,N,V_embeddingRequestType"
+ "Tq,R,N,V_policyType"
+ "Ts,R,N,V_detectionType"
+ "T{?=qiIq},R,N,V_timestamp"
+ "UUIDString"
+ "Unknown(%d)"
+ "Unspecified"
+ "UseVIPModel"
+ "UserInitiated"
+ "UserInteractive"
+ "Utility"
+ "VideoSessionXPC"
+ "[%@] Failed to create SCSensitivityAnalysis error:%@"
+ "[%@] Failed to create pixelBuffer pool"
+ "[%@] Failed to create pixelBuffer scaler"
+ "[%@][addBackRequestsAfterReconnection]"
+ "[%@][addRequest]"
+ "[%@][processPixelBuffer:]"
+ "[%@][removeAllRequest]"
+ "[%@][removeRequest]"
+ "[%@][requestTTRNotification:]"
+ "[LOG_ERROR] %s[%d]: code %d\n"
+ "[MADService] A handler has been registered, do not re-register another one"
+ "[MADService] Attempting to re-register the handler"
+ "[MADService] Completed subscribeUserSafety"
+ "[MADService] Error creating CVPixelBuffer from non-IOSurface-backed CGImage with downscaling factor %f (synchronous)"
+ "[MADService] Failed subscribeUserSafety, error: %@"
+ "[MADService] Proactive timeout triggered"
+ "[MADService] Receive request from %@"
+ "[MADService] Setup proactive timeout of %.3f seconds"
+ "[MADService] Starting subscribeUserSafety"
+ "[MADService] Submitting text pre-warming request [ID: %d QoS: %@]"
+ "[MADService] Submitting text processing request [ID: %d QoS: %@]"
+ "[MADService] Text pre-warming request completed [ID: %d]"
+ "[MADService] Text pre-warming request failed [ID: %d] (%@)"
+ "[MADService] Text processing request completed [ID: %d]"
+ "[MADService] Text processing request failed [ID: %d] (%@)"
+ "[MADVideoSession init] unavialable; please call [MADVideoSession session]"
+ "[MADVideoSession] Client XPC connection interrupted"
+ "[MADVideoSession] Client XPC connection invalidated"
+ "[MADVideoSession] Failed; please turn on the VideoSessionXPC feature flag."
+ "_active"
+ "_addBackRequestsAfterReconnection"
+ "_analysisResult"
+ "_block"
+ "_detectionType"
+ "_embeddingRequestType"
+ "_enableDetectionTypeGV"
+ "_enableDetectionTypeN"
+ "_enableGoreViolenceDetection"
+ "_enableNudityDetection"
+ "_eventDate"
+ "_includePets"
+ "_isOneShot"
+ "_isSensitiveGoreViolence"
+ "_isSensitiveNudity"
+ "_orientation"
+ "_pixelBufferPool"
+ "_pixelFormat"
+ "_policyType"
+ "_pool"
+ "_queue"
+ "_removeLocalRequest:"
+ "_requests"
+ "_requestsManagementQueue"
+ "_scaler"
+ "_session"
+ "_source"
+ "_startDate"
+ "_streamID"
+ "_timestamp"
+ "_transferSession"
+ "_useVIPModel"
+ "_userSafetyHandler"
+ "addRequest:error:"
+ "addRequest:reply:"
+ "allowedRequestTTRNotificationClasses"
+ "allowedResultClasses"
+ "analysisResult"
+ "boolValue"
+ "com.apple.mediaanalysisd.videosession.public"
+ "com.apple.mediaanalysisservices.timer"
+ "com.apple.sensitivecontentanalysis.testing"
+ "copyPixelBuffer:toPixelBuffer:"
+ "date"
+ "destroy"
+ "detection-type: %hd, "
+ "detectionType"
+ "displayLabel: %@>"
+ "domain: %lu, "
+ "embeddingRequestType"
+ "enableDetectionTypeGV"
+ "enableDetectionTypeN"
+ "enableGoreViolenceDetection"
+ "enableGoreViolenceDetection: %@, "
+ "enableNudityDetection"
+ "enableNudityDetection: %@, "
+ "enabledQRCodeDetection"
+ "enabledVideoSessionXPC"
+ "eventDate"
+ "eventDate: %@>"
+ "goreViolenceResult"
+ "handleTimerEvent"
+ "hasOnlyOneSafetyRquest"
+ "i32@0:8^{__CVBuffer=}16^^{__CVBuffer}24"
+ "i56@0:8@16@24@32d40@?48"
+ "i64@0:8@16@24Q32@40d48@?56"
+ "includePets"
+ "includePets: %@, "
+ "initWithDomain:displayLabel:"
+ "initWithIntervalNanoseconds:isOneShot:andBlock:"
+ "initWithIsSensitiveNudity:isSensitiveGoreViolence:"
+ "initWithIsSensitiveNudity:isSensitiveGoreViolence:scoresForLabels:"
+ "initWithPersonIdentifier:personName:mdID:detectionType:verified:boundingBox:andConfidence:"
+ "initWithPixelBuffer:timestamp:orientation:"
+ "initWithPixelBufferClassificationDictionary:error:"
+ "initWithPolicyType:"
+ "initWithRequestID:"
+ "initWithResultItems:"
+ "initWithSensitivityAttributes:requestID:"
+ "initWithSession:"
+ "initWithSuiteName:"
+ "initWithTargetWidth:height:format:"
+ "isMemberOfClass:"
+ "isSensitiveGoreViolence"
+ "isSensitiveGoreViolence: %@>"
+ "isSensitiveNudity"
+ "isSensitiveNudity : %@,"
+ "nudityResult"
+ "numberWithUnsignedInt:"
+ "objectForKey:"
+ "orientation"
+ "orientation: %u>"
+ "performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:"
+ "performRequests:onAssetWithLocalIdentifier:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:"
+ "performRequests:onCGImage:withOrientation:andIdentifier:error:"
+ "policyType"
+ "policyType: %d>"
+ "preprocessPixelBuffer:output:"
+ "processFrameWithIOSurface:orientation:timestamp:reply:"
+ "processPixelBuffer timestamp: %.2f, orientation %d"
+ "processPixelBuffer:timestamp:orientation:resultHandler:"
+ "registerUserSafetyPolicyUpdateHandler:error:"
+ "removeAllObjects"
+ "removeAllRequests"
+ "removeObjectAtIndex:"
+ "removeRequest:"
+ "removeRequest:reply:"
+ "reportMADUserSafetyPolicy:error:"
+ "requestAnalysisXPCStoreListenerEndpointWithPhotoLibraryURL:reply:"
+ "requestCollectionTheme:forLocalIdentifiers:fromPhotoLibraryWithURL:withOptions:andReply:"
+ "requestCollectionThemeVersion:withOptions:andReply:"
+ "requestID"
+ "requestPhotosDeferredProcessing:reply:"
+ "requestProgressReport:reply:"
+ "requestResetProcessingStatus:taskID:photoLibraryURL:options:reply:"
+ "requestSystemXPCStoreListenerEndpoint:"
+ "requestTTRNotificationWithVideoFrames:options:completionHandler:"
+ "requestTTRNotificationWithVideoFrames:options:reply:"
+ "requestedEmbeddingType: %d, "
+ "resultItems: %@ >"
+ "richLabelResult"
+ "s"
+ "s16@0:8"
+ "scalePixelBuffer:output:"
+ "session"
+ "setDateFormat:"
+ "setEmbeddingRequestType:"
+ "setEnableDetectionTypeGV:"
+ "setEnableDetectionTypeN:"
+ "setEnableGoreViolenceDetection:"
+ "setEnableNudityDetection:"
+ "setEventDate:"
+ "setIncludePets:"
+ "setStartDate:"
+ "setStreamID:"
+ "setUseVIPModel:"
+ "softlink:r:path:/System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis"
+ "startDate"
+ "startDate: %@"
+ "streamID"
+ "streamID: %@"
+ "stringFromDate:"
+ "subscribeUserSafety:"
+ "timerWithInterval:unit:oneShot:andBlock:"
+ "timerWithIntervalSeconds:isOneShot:andBlock:"
+ "timestamp"
+ "timestamp: %.4f"
+ "useVIPModel"
+ "useVIPModel: %@, "
+ "v24@0:8@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v32@0:8@\"MADUserSafetyPolicy\"16@\"NSError\"24"
+ "v32@0:8@\"MADVideoSessionRequest\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">24"
+ "v36@0:8i16@\"NSDictionary\"20@?<v@?@\"NSNumber\"@\"NSError\">28"
+ "v40@0:8@\"NSArray\"16@\"MADVideoSessionTTROptions\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "v48@?0@\"NSArray\"8{?=qiIq}16@\"NSError\"40"
+ "v52@0:8i16@\"NSArray\"20@\"NSURL\"28@\"NSDictionary\"36@?<v@?@\"NSDictionary\"@\"NSError\">44"
+ "v60@0:8@\"IOSurface\"16I24{?=qiIq}28@?<v@?@\"NSArray\"{?=qiIq}@\"NSError\">52"
+ "v60@0:8@16I24{?=qiIq}28@?52"
+ "yyyy-MM-dd_HH:mm:ss"
+ "{CF<OpaqueVTPixelTransferSession *>=\"value_\"^{OpaqueVTPixelTransferSession}}"
+ "{CF<__CVPixelBufferPool *>=\"value_\"^{__CVPixelBufferPool}}"
- ", ScoresForLabels: %@"
- ", isSensitive: %@"
- "@28@0:8B16@20"
- "@80@0:8@16@24@32B40{CGRect={CGPoint=dd}{CGSize=dd}}44f76"
- "IsSensitive"
- "MD5TextCalibrationV2"
- "SearchUnifiedEmbeddingMD5"
- "TB,R,N,V_isSensitive"
- "_isSensitive"
- "attributes: %@>"
- "initWithIsSensitive:andAttributes:"
- "initWithIsSensitive:scoresForLabels:"
- "initWithPersonIdentifier:personName:mdID:verified:boundingBox:andConfidence:"
- "isSensitive: %d,"
- "requestMediaAnalysisDatabaseBackup:photoLibraryURL:options:reply:"

```
