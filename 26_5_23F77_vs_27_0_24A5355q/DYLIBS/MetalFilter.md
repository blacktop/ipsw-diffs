## MetalFilter

> `/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter`

```diff

-665.120.8.0.0
-  __TEXT.__text: 0x396c
-  __TEXT.__auth_stubs: 0x2c0
+748.0.0.122.2
+  __TEXT.__text: 0x3f04
   __TEXT.__objc_methlist: 0x41c
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x3a7
-  __TEXT.__unwind_info: 0x100
-  __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methname: 0xf1d
-  __TEXT.__objc_methtype: 0x490
-  __TEXT.__objc_stubs: 0x8e0
-  __DATA_CONST.__got: 0x90
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0xaf9
+  __TEXT.__oslogstring: 0x1ac
+  __TEXT.__unwind_info: 0x110
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0x3e8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x168
-  __AUTH_CONST.__cfstring: 0xc0
+  __DATA_CONST.__got: 0x90
+  __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x710
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__common: 0x10
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6398628-DE5C-3CAA-B8E3-CBC1BBCB0155
-  Functions: 98
-  Symbols:   70
-  CStrings:  274
+  UUID: CD52911D-1882-34D1-BB20-727828C91EBC
+  Functions: 115
+  Symbols:   76
+  CStrings:  99
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x6
+ _objc_retain_x8
+ _os_log_type_enabled
- _FigSignalErrorAtGM
- _fig_log_get_emitter
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x26
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "+[FigColorCubeMetalFilter createCubeTexture:ofSize:cubesCount:textureType:withDevice:]"
+ "+[FigColorCubeMetalFilter loadCube:ofSize:intoTexture:toSliceIndex:]"
+ "-[FigColorCubeMetalFilter _prewarmWithTuningParameters:]"
+ "-[FigColorCubeMetalFilter createPipelineStateWithVertexFunctionName:fragmentName:isLuma:useBgCube:manyFgCubes:colorSpace:mixInGammaDomain:]"
+ "-[FigColorCubeMetalFilter createPipelineStatesForCubeConversionWithVertexFunctionName:]"
+ "-[FigColorCubeMetalFilter createPipelineStatesWithFragmentName:vertexFunctionName:]"
+ "-[FigColorCubeMetalFilter initWithCommandQueue:]"
+ "-[FigColorCubeMetalFilter prepareToProcess:]"
+ "-[FigColorCubeMetalFilter purgeResources]"
+ "-[FigColorCubeMetalFilter resetState]"
+ "-[FigColorCubeMetalFilter runWithInputPixelBuffer:mattePixelBuffer:outputPixelBuffer:targetRectangle:]"
+ "-[FigColorCubeMetalFilter setBackgroundCubeWithName:data:]"
+ "-[FigColorCubeMetalFilter setForegroundCubesWithNames:data:]"
+ "3D cubes support only one slice"
+ "<<<< FigColorCube >>>> %s: %s"
+ "<<<< FigColorCube >>>> %s: FigColor doesn't implement purgeResources"
+ "<<<< FigColorCube >>>> %s: FigColor doesn't implement resetState"
+ "<<<< FigColorCube >>>> %s: FigColor prewarms shaders"
+ "<<<< FigColorCube >>>> %s: Perform color Cube conversion for Background cube"
+ "<<<< FigColorCube >>>> %s: Perform color Cube conversion for Foreground cube"
+ "<<<< FigColorCube >>>> %s: background cube is set to nil"
+ "Cube texture dimension mismatch"
+ "FigColor failed allocateResources call"
+ "FigColor failed createKernels call"
+ "FigColor uses Single-pass"
+ "FigColor uses Two-pass"
+ "FigColorCubeMetalFilterStatusAllocationError"
+ "FigColorCubeMetalFilterStatusCompilationError"
+ "_colorCubePipelineStateUV[useBgCube][manyFgCubes][colorSpace][mix] is NULL"
+ "_colorCubePipelineStateY[useBgCube][manyFgCubes][colorSpace][mix] is NULL"
+ "_colorCubePipelineState[useBgCube][manyFgCubes][colorSpace][mix] is NULL"
+ "_metal is NULL"
+ "ccube_trace"
+ "com.apple.coremedia"
+ "commandBuffer is NULL"
+ "constantValues is NULL"
+ "device is NULL"
+ "fullRangeVertexBuf is NULL"
+ "inputTex is NULL"
+ "inputTexUV is NULL"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "matteTex is NULL"
+ "outputTex is NULL"
+ "outputTexUV is NULL"
+ "renderPipelineColorAttachmentDescriptor is NULL"
+ "texture is NULL"
+ "textureDesc is NULL"
+ "vd is NULL"
+ "wrong-sized color cube"
- "#16@0:8"
- "%s signalled err=%d at <>:%d"
- ".cxx_destruct"
- "@\"<MTLCommandQueue>\""
- "@\"<MTLCommandQueue>\"16@0:8"
- "@\"CMIExternalMemoryDescriptor\"24@0:8@\"CMIExternalMemoryConfiguration\"16"
- "@\"CMIExternalMemoryResource\"16@0:8"
- "@\"FigMetalContext\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@52@0:8@16@24B32B36B40i44B48"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "C"
- "ImageBufferProcessor"
- "MetalImageBufferProcessor"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<MTLCommandQueue>\",&,N"
- "T@\"<MTLCommandQueue>\",&,N,V_metalCommandQueue"
- "T@\"CMIExternalMemoryResource\",?,&,N"
- "T@\"NSDictionary\",&,N"
- "T@\"NSDictionary\",&,N,V_cameraInfoByPortType"
- "T@\"NSDictionary\",&,N,V_tuningParameters"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,?,R,N"
- "TQ,R"
- "T^{?=iiBiB},N,V_filterDescriptor"
- "T^{__CVBuffer=},N,V_inputPixelBuffer"
- "T^{__CVBuffer=},N,V_mattePixelbuffer"
- "T^{__CVBuffer=},N,V_outputPixelBuffer"
- "Ti,N,V_matteToInputPixelBufferRotationDegrees"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_targetRectangle"
- "Vv16@0:8"
- "[2@\"<MTLRenderPipelineState>\"]"
- "[2@\"<MTLTexture>\"]"
- "[2[2[2[2@\"<MTLRenderPipelineState>\"]]]]"
- "^{?=iiBiB}"
- "^{?=iiBiB}16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CVBuffer=}"
- "^{__CVBuffer=}16@0:8"
- "_bgCubeTexture"
- "_bgCubeTextureTemp"
- "_bgCubeToUseIndex"
- "_bgCubesHaveBeenUpdated"
- "_bgCubesHaveBeenUpdatedLock"
- "_cameraInfoByPortType"
- "_colorCubePipelineState"
- "_colorCubePipelineStateUV"
- "_colorCubePipelineStateY"
- "_cubeConvert"
- "_fgCubeToUseIndex"
- "_fgCubesHaveBeenUpdated"
- "_fgCubesHaveBeenUpdatedLock"
- "_fgCubesTexture"
- "_fgCubesTextureTemp"
- "_filterDescriptor"
- "_inputPixelBuffer"
- "_isSingleFgCube"
- "_mattePixelbuffer"
- "_matteToInputPixelBufferRotationDegrees"
- "_metalCommandQueue"
- "_outputPixelBuffer"
- "_prewarmWithTuningParameters:"
- "_targetRectangle"
- "_tuningParameters"
- "_useBgCube"
- "_yuvFormat"
- "allocateResources"
- "arrayWithObjects:count:"
- "attributes"
- "autorelease"
- "bindPixelBufferToMTL2DTexture:pixelFormat:usage:plane:"
- "bundleForClass:"
- "bytes"
- "cameraInfoByPortType"
- "class"
- "colorAttachments"
- "commandQueue"
- "commit"
- "conformsToProtocol:"
- "convertCubeWithSrcTexture:dstTexture:isP3Cube:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createCubeTexture:ofSize:cubesCount:textureType:withDevice:"
- "createKernels"
- "createPipelineStateWithVertexFunctionName:fragmentName:isLuma:useBgCube:manyFgCubes:colorSpace:mixInGammaDomain:"
- "createPipelineStatesForCubeConversionWithVertexFunctionName:"
- "createPipelineStatesWithFragmentName:vertexFunctionName:"
- "cubeColorSpaceName"
- "dataWithLength:"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "drawPrimitives:vertexStart:vertexCount:"
- "endEncoding"
- "externalMemoryDescriptorForConfiguration:"
- "externalMemoryResource"
- "filterDescriptor"
- "filterWithName:"
- "finishProcessing"
- "hash"
- "height"
- "i"
- "i16@0:8"
- "i20@0:8I16"
- "i24@0:8@\"NSDictionary\"16"
- "i24@0:8@16"
- "i32@0:8@16@24"
- "i40@0:8@16i24@28i36"
- "i48@0:8^@16i24i28Q32@40"
- "i72@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32{CGRect={CGPoint=dd}{CGSize=dd}}40"
- "init"
- "initWithCommandQueue:"
- "initWithbundle:andOptionalCommandQueue:"
- "inputPixelBuffer"
- "intValue"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "layouts"
- "length"
- "loadCube:ofSize:intoTexture:toSliceIndex:"
- "mattePixelbuffer"
- "matteToInputPixelBufferRotationDegrees"
- "metalCommandQueue"
- "mutableBytes"
- "newBufferWithBytes:length:options:"
- "newTextureWithDescriptor:"
- "newTextureWithDescriptor:iosurface:plane:"
- "objectAtIndexedSubscript:"
- "outputPixelBuffer"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "prepareToProcess:"
- "prewarm"
- "prewarmInternalMetalShadersForFormatsList:"
- "prewarmMetalInternalShader"
- "prewarmWithTuningParameters:"
- "process"
- "purgeResources"
- "release"
- "releaseResources"
- "renderCommandEncoderWithDescriptor:"
- "renderPassDescriptor"
- "renderPipelineStateForVertexFunction:vertexDescriptor:fragmentFunction:constants:colorAttachmentDescriptorArrray:"
- "replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:"
- "resetState"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "runWithInputPixelBuffer:mattePixelBuffer:outputPixelBuffer:targetRectangle:"
- "self"
- "setArrayLength:"
- "setBackgroundCubeWithName:data:"
- "setBufferIndex:"
- "setCameraInfoByPortType:"
- "setConstantValue:type:atIndex:"
- "setDepth:"
- "setExternalMemoryResource:"
- "setFilterDescriptor:"
- "setForegroundCubesWithNames:data:"
- "setFormat:"
- "setFragmentBytes:length:atIndex:"
- "setFragmentTexture:atIndex:"
- "setHeight:"
- "setInputPixelBuffer:"
- "setLabel:"
- "setLoadAction:"
- "setMattePixelbuffer:"
- "setMatteToInputPixelBufferRotationDegrees:"
- "setMetalCommandQueue:"
- "setOffset:"
- "setOutputPixelBuffer:"
- "setPixelFormat:"
- "setRenderPipelineState:"
- "setStoreAction:"
- "setStride:"
- "setTargetRectangle:"
- "setTexture:"
- "setTextureType:"
- "setTuningParameters:"
- "setUsage:"
- "setVertexBuffer:offset:atIndex:"
- "setWidth:"
- "setup"
- "superclass"
- "supportsExternalMemoryResource"
- "targetRectangle"
- "textureType"
- "tuningParameters"
- "v16@0:8"
- "v20@0:8i16"
- "v24@0:8@\"<MTLCommandQueue>\"16"
- "v24@0:8@\"CMIExternalMemoryResource\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@16"
- "v24@0:8^{?=iiBiB}16"
- "v24@0:8^{__CVBuffer=}16"
- "v36@0:8@16@24B32"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "waitForIdle"
- "width"
- "zone"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
