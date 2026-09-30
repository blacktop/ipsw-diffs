## MetalFilter

> `/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter`

```diff

-580.14.5.0.0
-  __TEXT.__text: 0x3b50
-  __TEXT.__auth_stubs: 0x2e0
+587.60.6.0.0
+  __TEXT.__text: 0x456c
+  __TEXT.__auth_stubs: 0x320
   __TEXT.__objc_methlist: 0x214
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x384
-  __TEXT.__unwind_info: 0xb8
-  __TEXT.__objc_classname: 0x3e
-  __TEXT.__objc_methname: 0xe6a
-  __TEXT.__objc_methtype: 0x3c6
-  __TEXT.__objc_stubs: 0x9c0
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0xb63
+  __TEXT.__oslogstring: 0x1ac
+  __TEXT.__unwind_info: 0xc0
+  __TEXT.__objc_classname: 0x58
+  __TEXT.__objc_methname: 0xf7c
+  __TEXT.__objc_methtype: 0x490
+  __TEXT.__objc_stubs: 0x9e0
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x358
+  __DATA_CONST.__objc_selrefs: 0x368
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x178
-  __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__objc_const: 0x990
+  __AUTH_CONST.__auth_got: 0x198
+  __AUTH_CONST.__cfstring: 0x100
+  __AUTH_CONST.__objc_const: 0xad0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x78
   __DATA.__objc_ivar: 0x6c
-  __DATA.__data: 0xc0
+  __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__common: 0x10
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 44
-  Symbols:   72
-  CStrings:  263
+  Symbols:   76
+  CStrings:  337
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _os_log_type_enabled
- _FigSignalErrorAt
- _fig_log_get_emitter
CStrings:
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "+[FigColorCubeMetalFilter createCubeTexture:ofSize:cubesCount:textureType:withDevice:]"
+ "+[FigColorCubeMetalFilter loadCube:ofSize:intoTexture:toSliceIndex:]"
+ "-[FigColorCubeMetalFilter _prewarmWithTuningParameters:]"
+ "-[FigColorCubeMetalFilter createKernels]"
+ "-[FigColorCubeMetalFilter createPipelineStateWithVertexFunction:fragmentName:isLuma:useBgCube:manyFgCubes:colorSpace:mixInGammaDomain:]"
+ "-[FigColorCubeMetalFilter createPipelineStatesForCubeConversionWithVertexFunction:]"
+ "-[FigColorCubeMetalFilter createPipelineStatesWithFragmentName:vertexFunction:]"
+ "-[FigColorCubeMetalFilter initWithCommandQueue:]"
+ "-[FigColorCubeMetalFilter prepareToProcess:]"
+ "-[FigColorCubeMetalFilter purgeResources]"
+ "-[FigColorCubeMetalFilter resetState]"
+ "-[FigColorCubeMetalFilter runWithInputPixelBuffer:mattePixelBuffer:outputPixelBuffer:targetRectangle:]"
+ "-[FigColorCubeMetalFilter setBackgroundCubeWithName:data:]"
+ "-[FigColorCubeMetalFilter setForegroundCubesWithNames:data:]"
+ "3D cubes support only one slice"
+ "<<<< FigColorCube >>>>"
+ "<<<< FigColorCube >>>> %!s(MISSING): %!s(MISSING)"
+ "<<<< FigColorCube >>>> %!s(MISSING): FigColor doesn't implement purgeResources"
+ "<<<< FigColorCube >>>> %!s(MISSING): FigColor doesn't implement resetState"
+ "<<<< FigColorCube >>>> %!s(MISSING): FigColor prewarms shaders"
+ "<<<< FigColorCube >>>> %!s(MISSING): Perform color Cube conversion for Background cube"
+ "<<<< FigColorCube >>>> %!s(MISSING): Perform color Cube conversion for Foreground cube"
+ "<<<< FigColorCube >>>> %!s(MISSING): background cube is set to nil"
+ "@\"<MTLCommandQueue>\"16@0:8"
+ "@\"CMIExternalMemoryDescriptor\"24@0:8@\"CMIExternalMemoryConfiguration\"16"
+ "@\"CMIExternalMemoryResource\"16@0:8"
+ "Cube texture dimension mismatch"
+ "FIGMETALCONTEXT_CHECK_ERRCODE"
+ "FigColor failed allocateResources call"
+ "FigColor failed createKernels call"
+ "FigColor uses Single-pass"
+ "FigColor uses Two-pass"
+ "FigColorCubeMetalFilterStatusAllocationError"
+ "FigColorCubeMetalFilterStatusCompilationError"
+ "MetalImageBufferProcessor"
+ "T@\"<MTLCommandQueue>\",&,N"
+ "T@\"<MTLCommandQueue>\",&,N,V_metalCommandQueue"
+ "T@\"CMIExternalMemoryResource\",?,&,N"
+ "TB,?,R,N"
+ "_colorCubePipelineStateUV[useBgCube][manyFgCubes][colorSpace][mix] is NULL"
+ "_colorCubePipelineStateY[useBgCube][manyFgCubes][colorSpace][mix] is NULL"
+ "_colorCubePipelineState[useBgCube][manyFgCubes][colorSpace][mix] is NULL"
+ "_cubeConvert[i] is NULL"
+ "_metal is NULL"
+ "_metalCommandQueue"
+ "_prewarmWithTuningParameters:"
+ "ccube_trace"
+ "com.apple.coremedia"
+ "commandBuffer is NULL"
+ "constantValues is NULL"
+ "device is NULL"
+ "externalMemoryDescriptorForConfiguration:"
+ "externalMemoryResource"
+ "fullRangeVertexBuf is NULL"
+ "inputTex is NULL"
+ "inputTexUV is NULL"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "matteTex is NULL"
+ "metalCommandQueue"
+ "outputTex is NULL"
+ "outputTexUV is NULL"
+ "pState is NULL"
+ "pd is NULL"
+ "pd.fragmentFunction is NULL"
+ "setExternalMemoryResource:"
+ "setMetalCommandQueue:"
+ "supportsExternalMemoryResource"
+ "texture is NULL"
+ "textureDesc is NULL"
+ "v24@0:8@\"<MTLCommandQueue>\"16"
+ "v24@0:8@\"CMIExternalMemoryResource\"16"
+ "vd is NULL"
+ "vertexFunc is NULL"
+ "wrong-sized color cube"
- "T@\"<MTLCommandQueue>\",R,N,V_commandQueue"
- "_commandQueue"

```
