## CoreOCModules

> `/System/Library/PrivateFrameworks/CoreOCModules.framework/CoreOCModules`

```diff

-11.3.2.0.0
-  __TEXT.__text: 0x737a8
-  __TEXT.__auth_stubs: 0x1120
+11.3.6.0.0
+  __TEXT.__text: 0x72fc8
   __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0x4d34
-  __TEXT.__gcc_except_tab: 0x336c
-  __TEXT.__cstring: 0x489e
+  __TEXT.__const: 0x4d54
+  __TEXT.__gcc_except_tab: 0x283c
+  __TEXT.__cstring: 0x48a4
   __TEXT.__oslogstring: 0x6db2
-  __TEXT.__unwind_info: 0x1048
-  __TEXT.__objc_classname: 0x56
-  __TEXT.__objc_methname: 0x1272
-  __TEXT.__objc_methtype: 0x1a7
-  __TEXT.__objc_stubs: 0x1500
-  __DATA_CONST.__got: 0x378
+  __TEXT.__unwind_info: 0xe48
+  __TEXT.__eh_frame: 0x48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x468
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x600
-  __AUTH_CONST.__auth_got: 0x8a8
+  __DATA_CONST.__objc_selrefs: 0x5f8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1088
   __AUTH_CONST.__cfstring: 0x1940
   __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__weak_auth_got: 0x48
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x50
+  __AUTH_CONST.__auth_got: 0x888
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x540
+  __DATA.__bss: 0x548
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
-  - /System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore
   - /System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto
   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
   - /System/Library/PrivateFrameworks/CoreAppleCVA.framework/CoreAppleCVA
   - /System/Library/PrivateFrameworks/H10ISPServices.framework/H10ISPServices
+  - /System/Library/SubFrameworks/ARKitCore.framework/ARKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF838804-9D96-312E-A775-583E4C9E8426
-  Functions: 843
-  Symbols:   619
-  CStrings:  1227
+  UUID: 3F07013A-84E8-3AEB-BA94-56F630156535
+  Functions: 861
+  Symbols:   624
+  CStrings:  994
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
- _objc_retain_x27
- _objc_retain_x28
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B48@0:8q16q24Q32@\"NSDictionary\"40"
- "B48@0:8q16q24Q32@40"
- "CMPhotoInPlaceHEIFEditorDelegate"
- "NSObject"
- "OCNonModularSPI_CMPhoto_InPlaceEditor"
- "Q16@0:8"
- "T#,R"
- "T@\"NSArray\",&,V_modifiedExtrinsicsPosition"
- "T@\"NSArray\",&,V_modifiedExtrinsicsRotation"
- "T@\"NSData\",&,V_modifiedXMP"
- "T@\"NSDictionary\",&,V_modifiedCustom"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_modifiedCustom"
- "_modifiedExtrinsicsPosition"
- "_modifiedExtrinsicsRotation"
- "_modifiedXMP"
- "addCompletedHandler:"
- "addEntriesFromDictionary:"
- "addObject:"
- "addScheduledHandler:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithObjects:count:"
- "attributes"
- "autorelease"
- "blitCommandEncoder"
- "boolValue"
- "bundleWithIdentifier:"
- "bytes"
- "cStringUsingEncoding:"
- "cameraCalibrationDataDictionary"
- "caseInsensitiveCompare:"
- "class"
- "colorAttachments"
- "commandBuffer"
- "commandBufferWithDescriptor:"
- "commit"
- "compare:"
- "compare:options:"
- "computeCommandEncoder"
- "conformsToProtocol:"
- "contents"
- "copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "dataBuffer"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithLength:"
- "debugDescription"
- "defaultDeviceWithDeviceType:mediaType:position:"
- "depthAttachment"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:"
- "dispatchThreads:threadsPerThreadgroup:"
- "dispatchThreadsPerTile:"
- "doubleValue"
- "drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:"
- "drawPrimitives:vertexStart:vertexCount:"
- "encodeToCommandBuffer:sourceTexture:destinationTexture:"
- "endEncoding"
- "error"
- "errorState"
- "extrinsicMatrixFromDevice:toDevice:"
- "extrinsics:forIndex:modifiedExtrinsics:"
- "floatValue"
- "formatDescription"
- "formats"
- "getBytes:bytesPerRow:fromRegion:mipmapLevel:"
- "getBytes:length:"
- "handleFailureInFunction:file:lineNumber:description:"
- "hash"
- "height"
- "i40@0:8@\"NSDictionary\"16q24^@32"
- "i40@0:8@16q24^@32"
- "i64@0:8@\"NSData\"16q24q32Q40@\"NSDictionary\"48^@56"
- "i64@0:8@16q24q32Q40@48^@56"
- "initWithCameraCalibrationDataDictionary:error:"
- "initWithData:encoding:"
- "initWithDataBuffer:"
- "initWithDevice:"
- "initWithDevice:kernelWidth:kernelHeight:weights:"
- "initWithDevice:sigma:"
- "intValue"
- "isEqual:"
- "isEqualToString:"
- "isFileURL"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isTimeOfFlightProjectorModeSupported:"
- "label"
- "layouts"
- "length"
- "localizedDescription"
- "longValue"
- "maxTotalThreadsPerThreadgroup"
- "metadataPayload:forImageIndex:payloadIndex:withType:customMetadataIdentifier:modifiedData:"
- "modifiedCustom"
- "modifiedExtrinsicsPosition"
- "modifiedExtrinsicsRotation"
- "modifiedXMP"
- "mutableBytes"
- "mutableCopy"
- "newBufferWithBytes:length:options:"
- "newBufferWithLength:options:"
- "newCommandQueue"
- "newComputePipelineStateWithFunction:error:"
- "newDefaultLibraryWithBundle:error:"
- "newDepthStencilStateWithDescriptor:"
- "newFunctionWithName:"
- "newFunctionWithName:constantValues:error:"
- "newRenderPipelineStateWithDescriptor:error:"
- "newRenderPipelineStateWithTileDescriptor:options:reflection:error:"
- "newTextureWithDescriptor:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithUnsignedLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "pathExtension"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "photoSettingsWithFormat:"
- "pixelFormat"
- "popDebugGroup"
- "prepareDataBuffer:forLength:"
- "pushDebugGroup:"
- "release"
- "renderCommandEncoderWithDescriptor:"
- "replacePointsInRange:withPointsFrom:range:"
- "requiredStorageBytesForLength:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setBuffer:offset:atIndex:"
- "setBufferIndex:"
- "setBytes:length:atIndex:"
- "setCaptureObject:"
- "setClearColor:"
- "setClearDepth:"
- "setComputePipelineState:"
- "setConstantValue:type:atIndex:"
- "setCullMode:"
- "setDepthAttachmentPixelFormat:"
- "setDepthCompareFunction:"
- "setDepthStencilState:"
- "setDepthWriteEnabled:"
- "setEdgeMode:"
- "setErrorOptions:"
- "setFormat:"
- "setFragmentBytes:length:atIndex:"
- "setFragmentFunction:"
- "setFragmentTexture:atIndex:"
- "setHeight:"
- "setHighResolutionPhotoEnabled:"
- "setLabel:"
- "setLoadAction:"
- "setModifiedCustom:"
- "setModifiedExtrinsicsPosition:"
- "setModifiedExtrinsicsRotation:"
- "setModifiedXMP:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setOffset:"
- "setPhotoQualityPrioritization:"
- "setPixelFormat:"
- "setRenderPipelineState:"
- "setShutterSound:"
- "setStepFunction:"
- "setStepRate:"
- "setStorageMode:"
- "setStoreAction:"
- "setStride:"
- "setTexture:"
- "setTexture:atIndex:"
- "setTextureType:"
- "setThreadgroupSizeMatchesTileSize:"
- "setTileBuffer:offset:atIndex:"
- "setTileBytes:length:atIndex:"
- "setTileFunction:"
- "setTileHeight:"
- "setTileWidth:"
- "setUsage:"
- "setVertexBuffer:offset:atIndex:"
- "setVertexBytes:length:atIndex:"
- "setVertexDescriptor:"
- "setVertexFunction:"
- "setViewport:"
- "setWidth:"
- "setWithObjects:"
- "sharedCaptureManager"
- "shouldModifyMetadataForImageIndex:payloadIndex:withType:customMetadataIdentifier:"
- "stringWithUTF8String:"
- "superclass"
- "supportsFamily:"
- "threadExecutionWidth"
- "unarchivedObjectOfClasses:fromData:error:"
- "unsignedLongValue"
- "updateModifiedCustom:"
- "updateModifiedExtrinsicsPosition:rotation:"
- "updateModifiedXMP:"
- "userInfo"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "waitUntilCompleted"
- "width"
- "zone"

```
