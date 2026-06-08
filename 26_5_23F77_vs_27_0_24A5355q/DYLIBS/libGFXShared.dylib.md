## libGFXShared.dylib

> `/System/Library/Frameworks/OpenGLES.framework/libGFXShared.dylib`

```diff

-23.1.1.0.0
-  __TEXT.__text: 0x64a0
-  __TEXT.__auth_stubs: 0x390
+24.0.1.0.0
+  __TEXT.__text: 0x6518
   __TEXT.__cstring: 0x1b8a
   __TEXT.__const: 0x40
-  __TEXT.__unwind_info: 0x158
-  __DATA_CONST.__got: 0x30
+  __TEXT.__unwind_info: 0x178
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x4a0
-  __AUTH_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x380
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__common: 0xac
   __DATA.__bss: 0x8
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: B80922DE-5362-3FB5-AFBF-B51EFA3E9E7C
+  UUID: 680BFA3A-7B6B-3BED-B3FB-9A669F5F6F96
   Functions: 104
   Symbols:   203
   CStrings:  415
Functions:
~ _gfxWaitPluginBuffer : 108 -> 112
~ _gfxWaitBufferOnDevices : 128 -> 132
~ _gfxDestroyPluginBuffer : 108 -> 120
~ _gfxUploadPluginBufferData : 80 -> 84
~ _gfxInitializeLibrary : 2140 -> 2164
~ _gfxCreateSharedState : 468 -> 472
~ _gfxCompareSharedState : 92 -> 96
~ _gfxInitializeGLTexture : 920 -> 928
~ _gfxUploadPluginTextureLevel : 208 -> 212
~ _gfxWaitPluginTexture : 108 -> 112
~ _gfxWaitTextureOnDevices : 128 -> 132
~ _gfxSynchronizeTexLevelStorage : 316 -> 320
~ _gfxModifyPluginTextureLevel : 140 -> 144
~ _gfxEvaluateTextureForParameterChange : 1136 -> 1148
~ _gfxUpdateTextureForParameterChange : 368 -> 380
~ _gfxEvaluateTextureForGeometryChange : 2036 -> 2052
~ _gfxUpdateTextureForGeometryChange : 668 -> 636
~ _gfxUpdatePluginTextureLevelGeometry : 208 -> 212
~ _gfxAnnotateTexture : 332 -> 340
~ _gfxAnnotateBuffer : 296 -> 304
~ _gfxClearSyncObjectsInHash : 224 -> 228
~ _gfxCreateGLSyncFromCLEvent : 536 -> 540

```
