## libGPUSupportMercury.dylib

> `/System/Library/PrivateFrameworks/GPUSupport.framework/libGPUSupportMercury.dylib`

```diff

-23.1.1.0.0
-  __TEXT.__text: 0x8528
-  __TEXT.__auth_stubs: 0x490
+24.0.1.0.0
+  __TEXT.__text: 0x8614
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x11
   __TEXT.__oslogstring: 0x32
   __TEXT.__unwind_info: 0x268
-  __DATA_CONST.__got: 0x18
-  __AUTH_CONST.__auth_got: 0x248
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__common: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/IOAccelerator.framework/IOAccelerator
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: E189E21A-9495-3E91-8C4D-25CF0D01E8C0
+  UUID: A99C861E-8DB5-30C8-B8F7-9CC592B1C22A
   Functions: 175
   Symbols:   274
   CStrings:  3
Functions:
~ _gpusLoadTransformFeedbackBuffers : 196 -> 200
~ _gpumUpdateUniformBuffers : 300 -> 308
~ _gpumCompCreateFence : 236 -> 240
~ _gpumCompDestroyFence : 48 -> 52
~ _gpusComputeGetDataBuffer : 208 -> 212
~ _gpusQueueGetDataBuffer : 208 -> 212
~ _gpumCreateDevice : 204 -> 208
~ _gldClearFence : 116 -> 124
~ _gpulAllocFenceIndexOnQueue : 600 -> 604
~ _gldSetFenceOnContext : 348 -> 352
~ _gpumChoosePixelFormat : 1716 -> 1720
~ _gpumInitializeIOData : 540 -> 592
~ _gpumTerminateIOData : 140 -> 144
~ _gpumCreateQuery : 776 -> 780
~ _gpumDestroyQuery : 148 -> 152
~ _gpusLoadCurrentSamplers : 384 -> 412
~ _gpulDeleteKernelTexture : 180 -> 184
~ _gpumGetTextureLevelInfo : 816 -> 820
~ _gpumRestoreTextureData : 392 -> 404
~ _gpusLoadCurrentTextures : 860 -> 892
~ _gpusCreateZeroTexture : 844 -> 856
~ _gldGetTextureAllocationIdentifiers : 304 -> 308
~ _gpusGetKernelTextureIOSurface : 840 -> 860
~ _gpusLoadCurrentVertexArray : 752 -> 756

```
