## AppleCVA

> `/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA`

```diff

-1002.101.0.0.0
-  __TEXT.__text: 0xb3b5c
-  __TEXT.__auth_stubs: 0x19f0
+1003.0.2.0.0
+  __TEXT.__text: 0xb3cdc
   __TEXT.__objc_methlist: 0xb4
-  __TEXT.__const: 0x939
-  __TEXT.__gcc_except_tab: 0x49e4
-  __TEXT.__cstring: 0x5c54
-  __TEXT.__oslogstring: 0x9537
-  __TEXT.__unwind_info: 0x1338
-  __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0xd69
-  __TEXT.__objc_methtype: 0x1e6
-  __TEXT.__objc_stubs: 0x1220
-  __DATA_CONST.__got: 0x218
+  __TEXT.__const: 0x950
+  __TEXT.__gcc_except_tab: 0x416c
+  __TEXT.__cstring: 0x5cc7
+  __TEXT.__oslogstring: 0x95a0
+  __TEXT.__unwind_info: 0x12f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1588
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x498
+  __DATA_CONST.__objc_selrefs: 0x4a8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0xd08
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1f58
   __AUTH_CONST.__cfstring: 0x3980
   __AUTH_CONST.__objc_const: 0x348
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__weak_auth_got: 0xf8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0xf0
-  __AUTH.__objc_data: 0x50
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0xc40
   __DATA.__objc_ivar: 0x1c
-  __DATA.__bss: 0x290
-  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA.__bss: 0x288
+  __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x2a8
+  __DATA_DIRTY.__bss: 0x298
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D6561AD1-F66E-395C-9E6D-DC0EBC347FE8
-  Functions: 1179
-  Symbols:   960
-  CStrings:  2353
+  UUID: 48E71E20-8DD6-3C19-89EE-DADDA6DC5A4C
+  Functions: 1197
+  Symbols:   968
+  CStrings:  2182
 
Symbols:
+ _OBJC_CLASS_$_VNSequenceRequestHandler
+ _OBJC_CLASS_$_VNSession
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x9
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "Color pixel format type: 0x%x ('%s')"
+ "FaceKitRecognitionProcessor initialization failed: could not create a faceprinter thread."
+ "FaceKitRecognitionProcessor initialization failed: null faceprinter object."
+ "Faceprinter warmup failure: unable to create pixel buffer"
+ "Faceprinter warmup request failed"
+ "Failed to perform faceprint request (%s)."
+ "faceprint request failed"
+ "faceprinter initialization failed"
+ "make_exception_ptr was called in -fno-exceptions mode"
- ".cxx_destruct"
- "@\"<MTLDevice>\""
- "@\"<MTLRenderPipelineState>\""
- "@\"MTLRenderPassDescriptor\""
- "@\"MTLRenderPipelineDescriptor\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16^@24"
- "@40@0:8@16@24@32"
- "AppleCVABundleFinder"
- "B32@0:8f16f20Q24"
- "CVABilinearSampler"
- "CVAMotionTrackingExpressionConfiguration_Exclave"
- "FaceKitRecognitionProcessor initialization failed: could not create a recognition thread."
- "FaceKitRecognitionProcessor initialization failed: null recognition object."
- "Recognition initialization failure: unable to create pixel buffer"
- "T{?=QQQQQQQQQ},N,V_previousExpressions"
- "URLForResource:withExtension:"
- "UTF8String"
- "VPCMetalLib"
- "[4{?=\"position\"}]"
- "_device"
- "_emptyAccessibilityExpressions"
- "_facialExpressionToActivationToValueMapping"
- "_initWithDevice:pipelineLabel:fragmentFunction:"
- "_jawOpenStartingWithValue:mouthClose:forActivation:"
- "_minConfidenceExpressionStarted:forActivation:"
- "_perspectiveWarpFragmentData"
- "_previousExpressions"
- "_renderPassDescriptor"
- "_renderPipelineDescriptor"
- "_renderPipelineState"
- "_vertexData"
- "addObject:"
- "allocationSize"
- "arrayWithObjects:count:"
- "attributes"
- "baseAddress"
- "beginScope"
- "blitCommandEncoder"
- "boundingBox"
- "bundleForClass:"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "bytes"
- "bytesPerElement"
- "bytesPerRow"
- "cStringUsingEncoding:"
- "code"
- "colorAttachments"
- "commandBuffer"
- "commit"
- "commitAndWaitUntilSubmitted"
- "computeCommandEncoder"
- "contents"
- "copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "defaultANEDevice"
- "description"
- "descriptorData"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "dispatchThreads:threadsPerThreadgroup:"
- "drawPrimitives:vertexStart:vertexCount:"
- "encodeToCommandBuffer:sourceTexture:transform:destinationTexture:destinationBoundingBox:"
- "endEncoding"
- "endScope"
- "errorWithDomain:code:userInfo:"
- "f32@0:8Q16Q24"
- "faceObservationWithRequestRevision:boundingBox:roll:yaw:pitch:"
- "faceprint"
- "floatValue"
- "init"
- "initWithCVPixelBuffer:options:"
- "initWithDevice:"
- "initWithProperties:"
- "intValue"
- "isEqualToDictionary:"
- "layouts"
- "length"
- "localizedDescription"
- "lockWithOptions:seed:"
- "maxTotalThreadsPerThreadgroup"
- "metalLibraryWithDevice:error:"
- "mipmapLevelCount"
- "mutableBytes"
- "mutableCopy"
- "newBufferWithLength:options:"
- "newCaptureScopeWithCommandQueue:"
- "newCommandQueueWithDescriptor:"
- "newComputePipelineStateWithFunction:error:"
- "newFunctionWithName:"
- "newFunctionWithName:constantValues:error:"
- "newLibraryWithURL:error:"
- "newRenderPipelineStateWithDescriptor:error:"
- "newTextureWithDescriptor:"
- "newTextureWithDescriptor:iosurface:plane:"
- "numberWithBool:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performRequests:error:"
- "pixelFormat"
- "planeCount"
- "previousExpressions"
- "processIncomingExpressions:"
- "renderCommandEncoderWithDescriptor:"
- "renderPassDescriptor"
- "resourcePath"
- "results"
- "roll"
- "setBuffer:offset:atIndex:"
- "setBufferIndex:"
- "setCommitSynchronously:"
- "setCompletionQueue:"
- "setComputePipelineState:"
- "setConstantValue:type:atIndex:"
- "setCullMode:"
- "setDepthAttachmentPixelFormat:"
- "setDetectionLevel:"
- "setFormat:"
- "setFragmentBytes:length:atIndex:"
- "setFragmentFunction:"
- "setFragmentTexture:atIndex:"
- "setInputFaceObservations:"
- "setLabel:"
- "setLength:"
- "setLoadAction:"
- "setObject:forKeyedSubscript:"
- "setOffset:"
- "setPixelFormat:"
- "setPreviousExpressions:"
- "setProcessingDevice:"
- "setRasterSampleCount:"
- "setRenderPipelineState:"
- "setRevision:error:"
- "setStencilAttachmentPixelFormat:"
- "setStepFunction:"
- "setStepRate:"
- "setStorageMode:"
- "setStoreAction:"
- "setStride:"
- "setTexture:"
- "setTexture:atIndex:"
- "setUsage:"
- "setValue:forKey:"
- "setVertexBytes:length:atIndex:"
- "setVertexDescriptor:"
- "setVertexFunction:"
- "sharedCaptureManager"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "texture2DDescriptorWithPixelFormat:width:height:mipmapped:"
- "threadExecutionWidth"
- "unlockWithOptions:seed:"
- "unsignedIntegerValue"
- "usage"
- "v16@0:8"
- "v88@0:8{?=QQQQQQQQQ}16"
- "v96@0:8@16@24{?=[3]}32@80r^v88"
- "vertexDescriptor"
- "waitUntilCompleted"
- "waitUntilScheduled"
- "yaw"
- "{?=\"raiseEyebrows\"Q\"openMouth\"Q\"smile\"Q\"tongueOut\"Q\"eyeBlink\"Q\"noseSneer\"Q\"mouthPuckerCenter\"Q\"puckerLipsLeft\"Q\"puckerLipsRight\"Q}"
- "{?=\"transform\"{?=\"columns\"[3]}}"
- "{?=QQQQQQQQQ}16@0:8"
- "{?=QQQQQQQQQ}72@0:8{?=ffffffffffffff}16"

```
