## MediaAnalysisServices

> `/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices`

```diff

-375.10.1.0.0
-  __TEXT.__text: 0x3b64c
+380.1.1.0.0
+  __TEXT.__text: 0x3cea8
   __TEXT.__auth_stubs: 0x930
   __TEXT.__objc_methlist: 0x4b34
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x35c4
-  __TEXT.__gcc_except_tab: 0x4820
-  __TEXT.__oslogstring: 0x2349
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x3736
+  __TEXT.__gcc_except_tab: 0x4830
+  __TEXT.__oslogstring: 0x2366
   __TEXT.__dlopen_cstrs: 0x417
   __TEXT.__unwind_info: 0x1b38
   __TEXT.__objc_classname: 0xe70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4F0F4327-FED8-3DCB-B92C-A4075FE2D34E
-  Functions: 1606
-  Symbols:   5854
-  CStrings:  3091
+  UUID: ED737411-ADD8-39E9-9247-927AA648C85A
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
+ "[LOG_ERROR] %s[%d]: code %d\n"

```
