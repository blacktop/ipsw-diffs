## MediaAnalysisServices

> `/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices`

```diff

-380.2.1.0.0
-  __TEXT.__text: 0x3b64c
-  __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_methlist: 0x4b34
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x35c4
-  __TEXT.__gcc_except_tab: 0x4820
-  __TEXT.__oslogstring: 0x2349
+395.17.2.0.0
+  __TEXT.__text: 0x3e208
+  __TEXT.__auth_stubs: 0x8e0
+  __TEXT.__objc_methlist: 0x4c9c
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x389b
+  __TEXT.__gcc_except_tab: 0x4844
+  __TEXT.__oslogstring: 0x2366
   __TEXT.__dlopen_cstrs: 0x417
-  __TEXT.__unwind_info: 0x1b38
-  __TEXT.__objc_classname: 0xe70
-  __TEXT.__objc_methname: 0x82f3
-  __TEXT.__objc_methtype: 0x23f5
-  __TEXT.__objc_stubs: 0x2700
-  __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0xa70
-  __DATA_CONST.__objc_classlist: 0x400
+  __TEXT.__unwind_info: 0x1c08
+  __TEXT.__objc_classname: 0xea5
+  __TEXT.__objc_methname: 0x8416
+  __TEXT.__objc_methtype: 0x2404
+  __TEXT.__objc_stubs: 0x2720
+  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__const: 0xae0
+  __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17c8
+  __DATA_CONST.__objc_selrefs: 0x1818
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x3c8
-  __AUTH_CONST.__auth_got: 0x4b0
+  __DATA_CONST.__objc_superrefs: 0x3d8
+  __AUTH_CONST.__auth_got: 0x488
   __AUTH_CONST.__const: 0x318
-  __AUTH_CONST.__cfstring: 0x49c0
-  __AUTH_CONST.__objc_const: 0x99f8
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1270
-  __DATA.__objc_ivar: 0x548
+  __AUTH_CONST.__cfstring: 0x4b40
+  __AUTH_CONST.__objc_const: 0x9c98
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH.__objc_data: 0x12c0
+  __DATA.__objc_ivar: 0x564
   __DATA.__data: 0x420
   __DATA.__bss: 0x90
-  __DATA_DIRTY.__objc_data: 0x1590
+  __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C9C6BBF-F223-30EF-A62F-BBA14FA1B302
-  Functions: 1606
-  Symbols:   5854
-  CStrings:  3091
+  UUID: 17FBC4CE-D6E1-3EE7-99E3-0A51A4B8B533
+  Functions: 1687
+  Symbols:   6034
+  CStrings:  3139
 
Symbols:
+ +[MADTextTokenizationRequest maxTokenSizeForVersion:error:]
+ +[MADTextTokenizationRequest maxTokenSize]
+ +[MADTextTokenizationRequest supportsSecureCoding]
+ +[MADTextTokenizationResult supportsSecureCoding]
+ -[MADCoreMLResult initWithVisionResults:].cold.1
+ -[MADImageEmbeddingRequest computeUnits]
+ -[MADImageEmbeddingRequest setComputeUnits:]
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
+ -[MADPixelBufferProcesser _createPixelBuffer:width:height:format:].cold.1
+ -[MADPixelBufferProcesser _createPixelBuffer:width:height:format:].cold.2
+ -[MADTextEmbeddingRequest allowTruncation]
+ -[MADTextEmbeddingRequest computeUnits]
+ -[MADTextEmbeddingRequest setAllowTruncation:]
+ -[MADTextEmbeddingRequest setComputeUnits:]
+ -[MADTextEmbeddingResult setTruncated:]
+ -[MADTextEmbeddingResult truncated]
+ -[MADTextTokenizationRequest description]
+ -[MADTextTokenizationRequest encodeWithCoder:]
+ -[MADTextTokenizationRequest initWithCoder:]
+ -[MADTextTokenizationRequest init]
+ -[MADTextTokenizationRequest setVersion:]
+ -[MADTextTokenizationRequest tokenizationResults]
+ -[MADTextTokenizationRequest version]
+ -[MADTextTokenizationResult .cxx_destruct]
+ -[MADTextTokenizationResult description]
+ -[MADTextTokenizationResult encodeWithCoder:]
+ -[MADTextTokenizationResult error]
+ -[MADTextTokenizationResult initWithCoder:]
+ -[MADTextTokenizationResult initWithTokenIDs:error:]
+ -[MADTextTokenizationResult tokenIDs]
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.1
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.2
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.3
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.4
+ GCC_except_table107
+ _MADComputeUnitsToString
+ _OBJC_CLASS_$_MADTextTokenizationRequest
+ _OBJC_CLASS_$_MADTextTokenizationResult
+ _OBJC_IVAR_$_MADImageEmbeddingRequest._computeUnits
+ _OBJC_IVAR_$_MADTextEmbeddingRequest._allowTruncation
+ _OBJC_IVAR_$_MADTextEmbeddingRequest._computeUnits
+ _OBJC_IVAR_$_MADTextEmbeddingResult._truncated
+ _OBJC_IVAR_$_MADTextTokenizationRequest._version
+ _OBJC_IVAR_$_MADTextTokenizationResult._error
+ _OBJC_IVAR_$_MADTextTokenizationResult._tokenIDs
+ _OBJC_METACLASS_$_MADTextTokenizationRequest
+ _OBJC_METACLASS_$_MADTextTokenizationResult
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_CLASS_METHODS_MADTextTokenizationRequest
+ __OBJC_$_CLASS_METHODS_MADTextTokenizationResult
+ __OBJC_$_INSTANCE_METHODS_MADTextTokenizationRequest
+ __OBJC_$_INSTANCE_METHODS_MADTextTokenizationResult
+ __OBJC_$_INSTANCE_VARIABLES_MADTextTokenizationRequest
+ __OBJC_$_INSTANCE_VARIABLES_MADTextTokenizationResult
+ __OBJC_$_PROP_LIST_MADTextTokenizationRequest
+ __OBJC_$_PROP_LIST_MADTextTokenizationResult
+ __OBJC_CLASS_RO_$_MADTextTokenizationRequest
+ __OBJC_CLASS_RO_$_MADTextTokenizationResult
+ __OBJC_METACLASS_RO_$_MADTextTokenizationRequest
+ __OBJC_METACLASS_RO_$_MADTextTokenizationResult
+ __ZL40CGImage_CreateCVPixelBufferWithTransformP7CGImagePP10__CVBufferj26CGImagePropertyOrientationd.cold.6
+ __ZL40CGImage_CreateCVPixelBufferWithTransformP7CGImagePP10__CVBufferj26CGImagePropertyOrientationd.cold.7
+ ___29-[MADVideoSession connection]_block_invoke.202.cold.1
+ ___29-[MADVideoSession connection]_block_invoke.203
+ ___33-[MADVideoSession removeRequest:]_block_invoke.217
+ ___36-[MADVideoSession addRequest:error:]_block_invoke.213
+ ___36-[MADVideoSession removeAllRequests]_block_invoke.225
+ ___52-[MADVideoSession _addBackRequestsAfterReconnection]_block_invoke.208
+ ___68-[MADVideoSession processPixelBuffer:frameProperties:resultHandler:]_block_invoke.235
+ ___95-[MADVideoSession(UserSafety) requestTTRNotificationWithVideoFrames:options:completionHandler:]_block_invoke.281
+ ___Block_byref_object_copy_.232
+ ___Block_byref_object_dispose_.233
+ _objc_msgSend$maxTokenSizeForVersion:error:
+ _objc_retainAutoreleasedReturnValue
- ___29-[MADVideoSession connection]_block_invoke.201
- ___29-[MADVideoSession connection]_block_invoke.201.cold.1
- ___33-[MADVideoSession removeRequest:]_block_invoke.216
- ___36-[MADVideoSession addRequest:error:]_block_invoke.212
- ___36-[MADVideoSession removeAllRequests]_block_invoke.224
- ___52-[MADVideoSession _addBackRequestsAfterReconnection]_block_invoke.207
- ___68-[MADVideoSession processPixelBuffer:frameProperties:resultHandler:]_block_invoke.234
- ___95-[MADVideoSession(UserSafety) requestTTRNotificationWithVideoFrames:options:completionHandler:]_block_invoke.280
- ___Block_byref_object_copy_.231
- ___Block_byref_object_dispose_.232
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "\n"
+ ", truncated: %@"
+ "./Utilities/CGUtilities.h"
+ "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysisServices/ComputeService/MADCoreMLResult.mm"
+ "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/MADVideoSession.mm"
+ "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/Utilities/MADPixelBufferProcesser.mm"
+ "@32@0:8Q16^@24"
+ "ANE"
+ "AllowTruncation"
+ "CPU"
+ "ComputeUnits"
+ "GPU"
+ "MADTextTokenizationRequest"
+ "MADTextTokenizationResult"
+ "Specified version (%d) not supported"
+ "T@\"NSNumber\",R,N,V_truncated"
+ "TB,N,V_allowTruncation"
+ "TQ,N,V_computeUnits"
+ "Truncated"
+ "[LOG_ERROR] %s[%d]: code %d\n"
+ "_allowTruncation"
+ "_computeUnits"
+ "_truncated"
+ "allowTruncation"
+ "allowTruncation: %d, "
+ "computeUnits"
+ "computeUnits: %u, "
+ "error: %@"
+ "initWithTokenIDs:error:"
+ "maxTokenSize"
+ "maxTokenSizeForVersion:error:"
+ "setAllowTruncation:"
+ "setComputeUnits:"
+ "setTruncated:"
+ "tokenIDs: %@"
+ "tokenizationResults"
+ "truncated"
- "\t"

```
