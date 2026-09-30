## ARKit

> `/System/iOSSupport/System/Library/Frameworks/ARKit.framework/Versions/A/ARKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__oslogstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__objc_ivar`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-781.0.2.0.1
-  __TEXT.__text: 0x3a8d8
-  __TEXT.__objc_methlist: 0x425c
-  __TEXT.__const: 0x3660
+781.0.4.0.0
+  __TEXT.__text: 0x3abbc
+  __TEXT.__objc_methlist: 0x42c4
+  __TEXT.__const: 0x3690
   __TEXT.__cstring: 0x5194
   __TEXT.__gcc_except_tab: 0x1de8
   __TEXT.__oslogstring: 0x458a
   __TEXT.__ustring: 0xde
-  __TEXT.__unwind_info: 0x1218
+  __TEXT.__unwind_info: 0x1220
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x2008
+  __DATA_CONST.__objc_selrefs: 0x2048
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x2d0
   __DATA_CONST.__got: 0x440
   __AUTH_CONST.__const: 0xaa0
   __AUTH_CONST.__cfstring: 0x4b80
-  __AUTH_CONST.__objc_const: 0xce40
+  __AUTH_CONST.__objc_const: 0xce60
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x198

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1949
-  Symbols:   4569
+  Functions: 1963
+  Symbols:   4583
   CStrings:  1027
 
Symbols:
+ -[ARCamera projectPoint:viewRotationAngle:viewportSize:]
+ -[ARCamera projectionMatrixForViewRotationAngle:viewportSize:zNear:zFar:]
+ -[ARCamera unprojectPoint:ontoPlaneWithTransform:viewRotationAngle:viewportSize:]
+ -[ARCamera viewMatrixForViewRotationAngle:]
+ -[ARFrame displayTransformForViewRotationAngle:viewportSize:]
+ -[ARSession setViewLayer:]
+ -[ARSession viewLayer]
+ -[ARSession viewRotationAngle]
+ _ARCameraImageToViewTransformWithAngle
+ _ARCorrectedViewRotationAngleForRotation
+ _ARDisplayRotationFromViewRotationAngle
+ _ARInterfaceOrientationFromViewRotationAngle
+ _ARViewRotationAngleFromInterfaceOrientation
+ _ARViewToCameraImageTransformWithAngle
```
