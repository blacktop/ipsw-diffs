## SceneKit

> `/System/Library/Frameworks/SceneKit.framework/Versions/A/SceneKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`

```diff

-608.600.0.0.0
-  __TEXT.__text: 0x4c1354
+608.901.0.0.0
+  __TEXT.__text: 0x4c1e80
   __TEXT.__auth_stubs: 0x3200
   __TEXT.__objc_methlist: 0x194b4
   __TEXT.__const: 0x26698
-  __TEXT.__cstring: 0x9db7f
-  __TEXT.__oslogstring: 0x197e8
-  __TEXT.__gcc_except_tab: 0x426c
+  __TEXT.__cstring: 0x9dcd2
+  __TEXT.__oslogstring: 0x1982f
+  __TEXT.__gcc_except_tab: 0x4270
   __TEXT.__ustring: 0x3c
   __TEXT.__dlopen_cstrs: 0x45
   __TEXT.__unwind_info: 0xb930

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 29193
-  Symbols:   42869
-  CStrings:  17787
+  Functions: 29197
+  Symbols:   42872
+  CStrings:  17797
 
Symbols:
+ _C3DShapeMeshCountsAccountForShape
+ _C3DShapeMeshCreationDestroy
+ _C3DShapeTriangulationMarkTriangles
+ __C3DMeshElementGetPrimitiveGroupBoundingBoxes_block_invoke
+ ___block_descriptor_116_e16_80r_e19_v32?0I8^I12I20^B24l
- _C3DShapeTriangulationTriangleMark
- ___block_descriptor_112_e16_80r_e19_v32?0I8^I12I20^B24l
CStrings:
+ "@68@0:8@16@24q32s40q44q52q60"
+ "C3DCreateTangentsWithGeometryOptimized"
+ "C3DMeshElementGetPrimitiveGroupBoundingBoxes"
+ "C3DMeshElementGetPrimitiveGroupBoundingBoxes_block_invoke"
+ "Error: %s - index (%d) out of bounds (%d)"
+ "Error: %s - index (%u) out of bounds (%u positions, %u uvs)"
+ "Error: %s - indices (%d/%d/%d) out of bounds (%d)"
+ "Error: Geometry source has invalid parameter"
+ "Welcome to SceneKit 608.901 (Aug  4 2026 22:18:23)"
+ "__ProcessPrimitiveRange_Generic_block_invoke"
+ "__ProcessPrimitiveRange_Mask_block_invoke"
+ "__ProcessSkinnedGeometryForJointIndex_block_invoke"
+ "__ProcessTriangleRange_Generic"
+ "__ProcessTriangleRange_Mask"
- "@68@0:8@16@24q32s40Q44q52q60"
- "Error: invalid geometry detected - skip C3DCreateTangentsWithGeometryOptimized"
- "Unreachable code: Unsupported index size (%zu)"
- "Welcome to SceneKit 608.600 (Jul 31 2026 22:37:07)"
```
