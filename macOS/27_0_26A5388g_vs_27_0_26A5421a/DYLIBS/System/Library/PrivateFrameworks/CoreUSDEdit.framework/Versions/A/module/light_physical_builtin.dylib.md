## light_physical_builtin.dylib

> `/System/Library/PrivateFrameworks/CoreUSDEdit.framework/Versions/A/module/light_physical_builtin.dylib`

```diff

-28.0.4.0.0
-  __TEXT.__text: 0x2ee28
+28.0.8.0.0
+  __TEXT.__text: 0x2d50c
   __TEXT.__init_offsets: 0xc
-  __TEXT.__gcc_except_tab: 0xa14
-  __TEXT.__const: 0x785
-  __TEXT.__cstring: 0x182c6
-  __TEXT.__unwind_info: 0x718
+  __TEXT.__gcc_except_tab: 0x908
+  __TEXT.__const: 0x755
+  __TEXT.__cstring: 0x181ac
+  __TEXT.__unwind_info: 0x6b0
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__weak_got: 0x20
+  __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xdd0
+  __AUTH_CONST.__const: 0xdb8
   __AUTH_CONST.__weak_auth_got: 0x148
-  __AUTH_CONST.__auth_got: 0x538
-  __DATA.__data: 0x108
+  __AUTH_CONST.__auth_got: 0x468
+  __DATA.__data: 0xd0
   __DATA.__bss: 0xc8
   __DATA.__common: 0xa8
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /System/Library/Frameworks/Metal.framework/Versions/A/Metal
   - /System/Library/Frameworks/MetalKit.framework/Versions/A/MetalKit
   - /System/Library/Frameworks/Network.framework/Versions/A/Network
-  - /System/Library/Frameworks/OpenGL.framework/Versions/A/OpenGL
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/USDKit.framework/Versions/A/USDKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/usd/libusd_ms.dylib
-  Functions: 307
-  Symbols:   757
-  CStrings:  124
+  Functions: 296
+  Symbols:   714
+  CStrings:  119
 
Symbols:
+ GCC_except_table21
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table41
+ GCC_except_table42
+ GCC_except_table47
+ GCC_except_table50
+ GCC_except_table61
- GCC_except_table10
- GCC_except_table20
- GCC_except_table28
- GCC_except_table32
- GCC_except_table36
- GCC_except_table44
- GCC_except_table49
- GCC_except_table52
- GCC_except_table65
- _ZN34_ModuleLightPhysicalAreaCallbacks_11get_gl_bboxER8OfObjectR10GlUtilsCtx
- _ZN36_ModuleLightPhysicalLinearCallbacks_11get_gl_bboxER8OfObjectR10GlUtilsCtx
- __Z10_glColor3dddd
- __Z10_glColor4fffff
- __Z10_glDisablej
- __Z11_glVertex2fff
- __Z12_glIsEnabledj
- __Z12_glPopMatrixv
- __Z13_glMatrixModej
- __Z13_glPushMatrixv
- __Z14_glMultMatrixdPKd
- __Z6_glEndv
- __Z8_glBeginj
- __Z9_glEnablej
- __Z9_glScaledddd
- __Z9_glScaleffff
- __ZGVZN10GMathBbox3IdE9empty_boxEvE11s_empty_box
- __ZN23_ModulePortalCallbacks_8paint_glER8OfObjectR10GlUtilsCtx
- __ZN34_ModuleLightPhysicalAreaCallbacks_11get_gl_bboxER8OfObjectR10GlUtilsCtx
- __ZN34_ModuleLightPhysicalAreaCallbacks_8paint_glER8OfObjectR10GlUtilsCtx
- __ZN34_ModuleLightPhysicalSpotCallbacks_8paint_glER8OfObjectR10GlUtilsCtx
- __ZN35_ModuleLightPhysicalPointCallbacks_8paint_glER8OfObjectR10GlUtilsCtx
- __ZN36_ModuleLightPhysicalLinearCallbacks_11get_gl_bboxER8OfObjectR10GlUtilsCtx
- __ZN36_ModuleLightPhysicalLinearCallbacks_8paint_glER8OfObjectR10GlUtilsCtx
- __ZN37_ModuleLightPhysicalDistantCallbacks_8paint_glER8OfObjectR10GlUtilsCtx
- __ZN41_ModuleLightPhysicalEnvironmentCallbacks_8paint_glER8OfObjectR10GlUtilsCtx
- __ZN7GlUtils10draw_arrowEddRK9GMathVec3IdE
- __ZN7GlUtils10draw_flakeEd
- __ZN7GlUtils11draw_circleERKdS1_jbb
- __ZN7GlUtils12draw_frustumER10GlUtilsCtxRK14GMathMatrix4x4IdLb1EERKbRKdS9_S9_S9_
- __ZN7GlUtils13draw_3d_arrowERK9GMathVec3IdES3_RKdRKb
- __ZN7GlUtils14draw_appertureEjd
- __ZN7GlUtils15draw_area_lightER10GlUtilsCtxRK14GMathMatrix4x4IdLb1EERKbRKdS9_S9_
- __ZN7GlUtils15draw_cylinder_xEjffb
- __ZN7GlUtils15draw_dome_lightER10GlUtilsCtxRK14GMathMatrix4x4IdLb1EE
- __ZN7GlUtils16draw_point_lightER10GlUtilsCtxRK14GMathMatrix4x4IdLb1EE
- __ZN7GlUtils18draw_distant_lightER10GlUtilsCtxRK14GMathMatrix4x4IdLb1EE
- __ZN7GlUtils24draw_physical_spot_lightER10GlUtilsCtxRK14GMathMatrix4x4IdLb1EERKdS7_S7_S7_S7_
- __ZTI23ModuleGlObjectCallbacks
- __ZTS23ModuleGlObjectCallbacks
- __ZZN10GMathBbox3IdE9empty_boxEvE11s_empty_box
- __ZZN25LightPhysicalPointBuiltin18on_register_moduleER5OfAppR10CoreVectorIP7OfClassEEN3$_08__invokeER8OfObjectR10GlUtilsCtx
CStrings:
- "Light.Physical.Area.paint_gl:Implementation is null.\n"
- "Light.Physical.Distant.paint_gl:Implementation is null.\n"
- "Light.Physical.Environment.paint_gl:Implementation is null.\n"
- "Light.Physical.Linear.paint_gl:Implementation is null.\n"
- "Light.Physical.Spot.paint_gl:Implementation is null.\n"
```
