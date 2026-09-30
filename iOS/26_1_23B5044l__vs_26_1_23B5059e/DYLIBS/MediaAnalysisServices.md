## MediaAnalysisServices

> `/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices`

```diff

-375.6.1.0.0
-  __TEXT.__text: 0x3b550
+375.8.1.11.1
+  __TEXT.__text: 0x3cea8
   __TEXT.__auth_stubs: 0x930
   __TEXT.__objc_methlist: 0x4b34
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x357e
-  __TEXT.__gcc_except_tab: 0x4804
-  __TEXT.__oslogstring: 0x2316
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x3736
+  __TEXT.__gcc_except_tab: 0x4830
+  __TEXT.__oslogstring: 0x2366
   __TEXT.__dlopen_cstrs: 0x417
   __TEXT.__unwind_info: 0x1b38
   __TEXT.__objc_classname: 0xe70
   __TEXT.__objc_methname: 0x82f3
   __TEXT.__objc_methtype: 0x23f5
-  __TEXT.__objc_stubs: 0x26e0
+  __TEXT.__objc_stubs: 0x2700
   __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0xa20
+  __DATA_CONST.__const: 0xa70
   __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x3c8
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__const: 0x318
-  __AUTH_CONST.__cfstring: 0x4860
+  __AUTH_CONST.__cfstring: 0x49c0
   __AUTH_CONST.__objc_const: 0x99f8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x1270

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 328657C9-39AF-3843-A2AC-93C6A593C8C0
-  Functions: 1605
-  Symbols:   5852
-  CStrings:  3068
+  UUID: ABBDA01E-259D-38BD-A6E0-AC1909009068
+  Functions: 1642
+  Symbols:   5932
+  CStrings:  3096
 
Symbols:
+ -[MADCoreMLResult initWithVisionResults:].cold.1
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
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.1
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.2
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.3
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.4
+ GCC_except_table107
+ _MADUnifiedEmbeddingVersionToString
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
+ _objc_msgSend$policyType
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
CStrings:
+ "./Utilities/CGUtilities.h"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysisServices/ComputeService/MADCoreMLResult.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/MADVideoSession.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/Utilities/MADPixelBufferProcesser.mm"
+ "MD1"
+ "MD2"
+ "MD3"
+ "MD4"
+ "MD5"
+ "MD6"
+ "MD6'"
+ "MD7"
+ "MD7v2"
+ "Unexpected value (%lu)"
+ "Unknown"
+ "[LOG_ERROR] %s[%d]: code %d\n"
+ "[MADService] Report userSafetyPolicy: %d to client"

```
