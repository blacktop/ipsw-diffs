## libGPUSupportMercury.dylib

> `/System/Library/PrivateFrameworks/GPUSupport.framework/libGPUSupportMercury.dylib`

```diff

-23.0.2.0.0
-  __TEXT.__text: 0x8590
+23.1.1.0.0
+  __TEXT.__text: 0x8528
   __TEXT.__auth_stubs: 0x490
-  __TEXT.__const: 0x60
+  __TEXT.__const: 0x70
   __TEXT.__cstring: 0x11
   __TEXT.__oslogstring: 0x32
-  __TEXT.__unwind_info: 0x260
+  __TEXT.__unwind_info: 0x268
   __DATA_CONST.__got: 0x18
   __AUTH_CONST.__auth_got: 0x248
   __DATA.__common: 0x4

   - /System/Library/PrivateFrameworks/IOAccelerator.framework/IOAccelerator
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: A0D65223-1CD6-3505-89C6-02563185CCE7
-  Functions: 173
+  UUID: 2295D315-2F25-3CC7-82D9-200378054F7E
+  Functions: 175
   Symbols:   274
   CStrings:  3
 
Functions:
~ _gpusGetKernelBufferResource : 312 -> 316
~ _gldClearFence : 92 -> 116
~ _gpulAllocFenceIndexOnQueue : 608 -> 600
~ _gldGetFenceStatus : 172 -> 176
~ _gpumChoosePixelFormat : 1792 -> 1716
+ sub_256799984
~ _gldLoadFramebuffer : 288 -> 284
~ _gldUpdateReadFramebuffer : 136 -> 124
~ _gpulCheckForFramebufferIOSurfaceChanges : 136 -> 132
~ _gldUpdateDrawFramebuffer : 212 -> 200
~ _gldSetInteger : 616 -> 600
~ _gpusPixelBytes : 788 -> 772
~ _gpumDeleteCachedProgram : 144 -> 136
~ _gpumGetCachedProgram : 260 -> 256
~ _gpusLoadCurrentSamplers : 388 -> 384
~ _gpumRestoreTextureData : 400 -> 392
~ _gpusLoadCurrentTextures : 864 -> 860
~ _gpusCreateZeroTexture : 908 -> 844
+ sub_25679dc04
~ _gpusGetKernelTextureIOSurface : 820 -> 840
~ _gpusLoadCurrentVertexArray : 756 -> 752

```
