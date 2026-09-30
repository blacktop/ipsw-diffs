## geometry_builtin.dylib

> `/System/Library/PrivateFrameworks/CoreUSDEdit.framework/Versions/A/module/geometry_builtin.dylib`

```diff

-28.0.4.0.0
-  __TEXT.__text: 0x52c94
-  __TEXT.__gcc_except_tab: 0x23d4
-  __TEXT.__const: 0xaf2
-  __TEXT.__cstring: 0xdadf
-  __TEXT.__unwind_info: 0x850
+28.0.8.0.0
+  __TEXT.__text: 0x529ac
+  __TEXT.__gcc_except_tab: 0x2390
+  __TEXT.__const: 0xae5
+  __TEXT.__cstring: 0xdaab
+  __TEXT.__unwind_info: 0x7f8
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__weak_got: 0xf0
+  __DATA_CONST.__weak_got: 0xe0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1078
   __AUTH_CONST.__weak_auth_got: 0x30
-  __AUTH_CONST.__auth_got: 0x8f0
-  __DATA.__data: 0x1b0
+  __AUTH_CONST.__auth_got: 0x858
+  __DATA.__data: 0x1a0
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

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
-  Functions: 297
-  Symbols:   861
+  Functions: 278
+  Symbols:   821
   CStrings:  259
 
Symbols:
- __Z10_glColor4fffff
- __Z10_glEndListv
- __Z10_glNewListjj
- __Z11_glCallListj
- __Z11_glGenListsi
- __Z12_glPopMatrixv
- __Z13_glMatrixModej
- __Z13_glPushMatrixv
- __Z14_glDeleteListsji
- __Z14_glMultMatrixdPKd
- __Z9_glIsListj
- __ZGVZN14ModuleGeometry29RESOURCE_ID_GEOMETRY_DEFORMEDEvE30_RESOURCE_ID_GEOMETRY_DEFORMED
- __ZL34point_cloud_propagate_gl_dirtinessPv
- __ZN12GlUtilsGlCtx12delete_listsERKjS1_
- __ZN28_ModuleGeometryBoxCallbacks_12pre_paint_glER8OfObjectR10GlUtilsCtx
- __ZN28_ModuleGeometryBoxCallbacks_15destroy_gl_dataER8OfObjectR12GlUtilsGlCtx
- __ZN28_ModuleGeometryBoxCallbacks_18create_module_dataERK8OfObject
- __ZN28_ModuleGeometryBoxCallbacks_19destroy_module_dataERK8OfObjectPv
- __ZN28_ModuleGeometryBoxCallbacks_19on_attribute_changeER8OfObjectRK6OfAttrRiRKi
- __ZN28_ModuleGeometryBoxCallbacks_8paint_glER8OfObjectR10GlUtilsCtx
- __ZN31_ModuleGeometrySphereCallbacks_12pre_paint_glER8OfObjectR10GlUtilsCtx
- __ZN31_ModuleGeometrySphereCallbacks_15destroy_gl_dataER8OfObjectR12GlUtilsGlCtx
- __ZN31_ModuleGeometrySphereCallbacks_18create_module_dataERK8OfObject
- __ZN31_ModuleGeometrySphereCallbacks_19destroy_module_dataERK8OfObjectPv
- __ZN31_ModuleGeometrySphereCallbacks_19on_attribute_changeER8OfObjectRK6OfAttrRiRKi
- __ZN31_ModuleGeometrySphereCallbacks_8paint_glER8OfObjectR10GlUtilsCtx
- __ZN39_ModuleGeometrySceneItemCloudCallbacks_12pre_paint_glER8OfObjectR10GlUtilsCtx
- __ZN39_ModuleGeometrySceneItemCloudCallbacks_15destroy_gl_dataER8OfObjectR12GlUtilsGlCtx
- __ZN39_ModuleGeometrySceneItemCloudCallbacks_18create_module_dataERK8OfObject
- __ZN39_ModuleGeometrySceneItemCloudCallbacks_18on_resource_updateER8OfObjectRKiPK12ResourceData
- __ZN39_ModuleGeometrySceneItemCloudCallbacks_19destroy_module_dataERK8OfObjectPv
- __ZN39_ModuleGeometrySceneItemCloudCallbacks_8paint_glER8OfObjectR10GlUtilsCtx
- __ZN7GlUtils12draw_locatorER10GlUtilsCtxRK14GMathMatrix4x4IdLb1EERKd
- __ZN7GlUtils16draw_point_cloudER10GlUtilsCtxPK9GMathVec3IfERKj
- __ZN7GlUtils17draw_implicit_boxER10GlUtilsCtxRK14GMathMatrix4x4IdLb1EERK9GMathVec3IdE
- __ZN7GlUtils20draw_implicit_sphereER10GlUtilsCtxRK14GMathMatrix4x4IdLb1EERKd
- __ZN8OfObject19propagate_dirtinessERKiS1_P6OfAttr
- __ZNK12ModuleObject19get_shared_resourceERKi
- __ZNK12ModuleObject19is_resource_createdERKi
- __ZZN14ModuleGeometry29RESOURCE_ID_GEOMETRY_DEFORMEDEvE30_RESOURCE_ID_GEOMETRY_DEFORMED
CStrings:
+ "cull_back"
+ "left_handed"
- "geometry_deformed"
- "module.geometry.point_cloud: failed to create GL list.\n"
```
