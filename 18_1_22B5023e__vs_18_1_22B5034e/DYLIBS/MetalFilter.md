## MetalFilter

> `/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter`

```diff

-575.5.1.0.0
-  __TEXT.__text: 0x3b08
-  __TEXT.__auth_stubs: 0x2e0
+580.2.0.0.0
+  __TEXT.__text: 0x44dc
+  __TEXT.__auth_stubs: 0x320
   __TEXT.__objc_methlist: 0x214
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x384
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0xb47
+  __TEXT.__oslogstring: 0x1ac
   __TEXT.__unwind_info: 0xb8
   __TEXT.__objc_classname: 0x3e
   __TEXT.__objc_methname: 0xe6a

   __DATA_CONST.__objc_selrefs: 0x358
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x178
-  __AUTH_CONST.__cfstring: 0xc0
+  __AUTH_CONST.__auth_got: 0x198
+  __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x990
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x78
   __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0xc0
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
+  CStrings:  321
 
Symbols:
+ _FigSignalErrorAt3
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _os_log_type_enabled
+ __os_log_send_and_compose_impl
+ _fig_note_initialize_category_with_default_work_cf
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _fig_log_get_emitter
- _FigSignalErrorAt
CStrings:
+ "<<<< FigColorCube >>>> %!s(MISSING): Perform color Cube conversion for Background cube"
+ "<<<< FigColorCube >>>> %!s(MISSING): %!s(MISSING)"
+ "_colorCubePipelineState[useBgCube][manyFgCubes][colorSpace][mix] is NULL"
+ "outputTexUV is NULL"
+ "-1"
+ "commandBuffer is NULL"
+ "_colorCubePipelineStateY[useBgCube][manyFgCubes][colorSpace][mix] is NULL"
+ "-[FigColorCubeMetalFilter createPipelineStatesWithFragmentName:vertexFunction:]"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "_cubeConvert[i] is NULL"
+ "<<<< FigColorCube >>>>"
+ "FigColor failed allocateResources call"
+ "<<<< FigColorCube >>>> %!s(MISSING): FigColor doesn't implement resetState"
+ "matteTex is NULL"
+ "vertexFunc is NULL"
+ "<<<< FigColorCube >>>> %!s(MISSING): FigColor doesn't implement purgeResources"
+ "_colorCubePipelineStateUV[useBgCube][manyFgCubes][colorSpace][mix] is NULL"
+ "-[FigColorCubeMetalFilter runWithInputPixelBuffer:mattePixelBuffer:outputPixelBuffer:targetRectangle:]"
+ "<<<< FigColorCube >>>> %!s(MISSING): FigColor prewarms shaders"
+ "-[FigColorCubeMetalFilter createKernels]"
+ "textureDesc is NULL"
+ "com.apple.coremedia"
+ "fullRangeVertexBuf is NULL"
+ "-[FigColorCubeMetalFilter createPipelineStatesForCubeConversionWithVertexFunction:]"
+ "FigColor failed createKernels call"
+ "FigColorCubeMetalFilterStatusCompilationError"
+ "wrong-sized color cube"
+ "+[FigColorCubeMetalFilter createCubeTexture:ofSize:cubesCount:textureType:withDevice:]"
+ "-[FigColorCubeMetalFilter purgeResources]"
+ "inputTexUV is NULL"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "ccube_trace"
+ "FigColor uses Single-pass"
+ "inputTex is NULL"
+ "constantValues is NULL"
+ "<<<< FigColorCube >>>> %!s(MISSING): background cube is set to nil"
+ "Cube texture dimension mismatch"
+ "-[FigColorCubeMetalFilter prewarmWithTuningParameters:]"
+ "pd is NULL"
+ "device is NULL"
+ "FigColor uses Two-pass"
+ "-[FigColorCubeMetalFilter initWithCommandQueue:]"
+ "-[FigColorCubeMetalFilter prepareToProcess:]"
+ "-[FigColorCubeMetalFilter setBackgroundCubeWithName:data:]"
+ "pState is NULL"
+ "3D cubes support only one slice"
+ "-[FigColorCubeMetalFilter resetState]"
+ "outputTex is NULL"
+ "texture is NULL"
+ "<<<< FigColorCube >>>> %!s(MISSING): Perform color Cube conversion for Foreground cube"
+ "-[FigColorCubeMetalFilter createPipelineStateWithVertexFunction:fragmentName:isLuma:useBgCube:manyFgCubes:colorSpace:mixInGammaDomain:]"
+ "vd is NULL"
+ "-[FigColorCubeMetalFilter setForegroundCubesWithNames:data:]"
+ "FigColorCubeMetalFilterStatusAllocationError"
+ "_metal is NULL"
+ "+[FigColorCubeMetalFilter loadCube:ofSize:intoTexture:toSliceIndex:]"
+ "pd.fragmentFunction is NULL"
+ "kCMBaseObjectError_AllocationFailed"

```
