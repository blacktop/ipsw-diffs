## libWrapGL.dylib

> `/System/Library/Frameworks/CoreImage.framework/Versions/A/Frameworks/libWrapGL.dylib`

```diff

-1510.80.3.0.0
-  __TEXT.__text: 0x2798
+1510.100.3.0.0
+  __TEXT.__text: 0x27e0
   __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_stubs: 0x120
   __TEXT.__const: 0x50

   __TEXT.__oslogstring: 0x1ad
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x9c
-  __TEXT.__unwind_info: 0xf8
+  __TEXT.__unwind_info: 0x110
   __DATA_CONST.__auth_got: 0x1a8
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x1a0

   - /System/Library/Frameworks/OpenGL.framework/Versions/A/OpenGL
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4857A118-AB61-364F-B41E-4E703535A642
-  Functions: 132
-  Symbols:   228
+  UUID: 633F141B-A2AB-3A40-A6CE-B5C1055C512E
+  Functions: 139
+  Symbols:   235
   CStrings:  28
 
Symbols:
+ ci_logger_api.cold.1
+ ci_logger_performance.cold.1
+ ci_logger_render.cold.1
+ mux_app_checkfix.cold.1
+ wrapCGLContextCreate.cold.1
+ wrapGLIsAccelerated.cold.1
+ wrapGLIsUsable.cold.1
Functions:
~ _wrapGLIsUsable : 68 -> 56
~ _wrapGLIsAccelerated : 68 -> 56
~ _wrapCGLContextCreate : 680 -> 664
~ __CGLContextCreateWithSharing : 960 -> 972
~ _wrapCGLContextIterateRegistryIDs : 356 -> 352
~ _wrapEAGLContextTexImageIOSurface : 616 -> 628
~ _ci_logger_api : 68 -> 56
~ _ci_logger_render : 68 -> 56
~ _ci_logger_performance : 68 -> 56
~ _mux_app_checkfix : 76 -> 64
+ wrapGLIsUsable.cold.1
+ wrapGLIsAccelerated.cold.1
+ wrapCGLContextCreate.cold.1

```
