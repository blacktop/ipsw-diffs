## GESS

> `/System/Library/PrivateFrameworks/GESS.framework/GESS`

```diff

-1.5.23.0.0
-  __TEXT.__text: 0x32f6f8
-  __TEXT.__auth_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0x1714
-  __TEXT.__const: 0x3b000
-  __TEXT.__gcc_except_tab: 0x49de8
-  __TEXT.__cstring: 0x8be72
-  __TEXT.__oslogstring: 0x28d
-  __TEXT.__unwind_info: 0x124d0
+1.5.24.0.0
+  __TEXT.__text: 0x3371e4
+  __TEXT.__auth_stubs: 0x1720
+  __TEXT.__objc_methlist: 0x1904
+  __TEXT.__const: 0x3bf50
+  __TEXT.__gcc_except_tab: 0x4a670
+  __TEXT.__cstring: 0x8bec5
+  __TEXT.__oslogstring: 0x2e1
+  __TEXT.__unwind_info: 0x12938
   __TEXT.__eh_frame: 0x5b0
-  __TEXT.__objc_classname: 0x5b4
-  __TEXT.__objc_methname: 0x30df
-  __TEXT.__objc_methtype: 0xc7b
-  __TEXT.__objc_stubs: 0x2b20
-  __DATA_CONST.__got: 0x388
+  __TEXT.__objc_classname: 0x67d
+  __TEXT.__objc_methname: 0x33bc
+  __TEXT.__objc_methtype: 0xdbf
+  __TEXT.__objc_stubs: 0x2ca0
+  __DATA_CONST.__got: 0x3b8
   __DATA_CONST.__const: 0x1178
-  __DATA_CONST.__objc_classlist: 0x198
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe78
-  __DATA_CONST.__objc_superrefs: 0x130
-  __AUTH_CONST.__auth_got: 0xb80
-  __AUTH_CONST.__const: 0xd610
+  __DATA_CONST.__objc_selrefs: 0xf08
+  __DATA_CONST.__objc_superrefs: 0x148
+  __AUTH_CONST.__auth_got: 0xba0
+  __AUTH_CONST.__const: 0xdc60
   __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0x3a10
-  __AUTH.__objc_data: 0xff0
+  __AUTH_CONST.__objc_const: 0x4128
+  __AUTH.__objc_data: 0x11d0
   __AUTH.__data: 0x8
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_data: 0x8
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x260
+  __DATA.__objc_ivar: 0x2b8
   __DATA.__data: 0x1f0
   __DATA.__bss: 0x6558
   __DATA.__common: 0x8

   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders
   - /System/Library/Frameworks/ModelIO.framework/ModelIO
+  - /System/Library/Frameworks/OSLog.framework/OSLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D2FFFEA-81AB-3418-B749-C06E5A4D634E
-  Functions: 11012
-  Symbols:   2170
-  CStrings:  4258
+  UUID: DB575542-9D90-35E0-B20B-BCF23F9E248B
+  Functions: 11244
+  Symbols:   2186
+  CStrings:  4314
 
Symbols:
+ _OBJC_CLASS_$_GESSAlgAdaptiveCubeInferenceExtended
+ _OBJC_CLASS_$_GESSAlgAdaptiveCubeInferenceReport
+ _OBJC_CLASS_$_GESSAlgInverseRenderExtended
+ _OBJC_CLASS_$_GESSAlgInverseRenderReport
+ _OBJC_CLASS_$_GESSAlgSplitMeshByComponentsExtended
+ _OBJC_CLASS_$_GESSAlgSplitMeshByComponentsOptions
+ _OBJC_METACLASS_$_GESSAlgAdaptiveCubeInferenceExtended
+ _OBJC_METACLASS_$_GESSAlgAdaptiveCubeInferenceReport
+ _OBJC_METACLASS_$_GESSAlgInverseRenderExtended
+ _OBJC_METACLASS_$_GESSAlgInverseRenderReport
+ _OBJC_METACLASS_$_GESSAlgSplitMeshByComponentsExtended
+ _OBJC_METACLASS_$_GESSAlgSplitMeshByComponentsOptions
+ __os_signpost_emit_with_name_impl
+ _os_log_create
+ _os_signpost_enabled
+ _os_signpost_id_generate
CStrings:
+ "1.5.24"
+ "@\"GESSAlgAdaptiveCubeInferenceOptions\""
+ "@\"GESSAlgInverseRenderOptions\""
+ "@\"GESSAlgSplitMeshByComponentsOptions\""
+ "B48@0:8@16@24@32@40"
+ "DataConversion"
+ "Extraction"
+ "GESSAlgAdaptiveCubeInferenceExtended"
+ "GESSAlgAdaptiveCubeInferenceReport"
+ "GESSAlgInverseRenderExtended"
+ "GESSAlgInverseRenderReport"
+ "GESSAlgSplitMeshByComponentsExtended"
+ "GESSAlgSplitMeshByComponentsOptions"
+ "Optimization"
+ "Parameterization"
+ "PostProcessing"
+ "Preparation"
+ "TI,VmaxSplitCount"
+ "T^{CGImage=},VmraImage"
+ "Td,VbuildMaterialMapsTime"
+ "Td,VconstructMeshTime"
+ "Td,VconstructVerticesAndFacesTime"
+ "Td,VdataConvertTime"
+ "Td,VparameterizeTime"
+ "Td,VtextureOptimizationPreparationTime"
+ "Td,VtextureOptimizationTime"
+ "buildMaterialMapsTime"
+ "constructMeshTime"
+ "constructMeshTime_"
+ "constructVerticesAndFacesTime"
+ "dataConvertTime"
+ "dataConvertTime_"
+ "maxSplitCount"
+ "options_"
+ "parameterizeTime"
+ "parameterizeTime_"
+ "report_"
+ "run:deform:weight:outputMesh:"
+ "run:mvps:imageSets:outputMesh:"
+ "setBuildMaterialMapsTime:"
+ "setConstructMeshTime:"
+ "setConstructVerticesAndFacesTime:"
+ "setDataConvertTime:"
+ "setMaxSplitCount:"
+ "setParameterizeTime:"
+ "setTextureOptimizationPreparationTime:"
+ "setTextureOptimizationTime:"
+ "success_"
+ "textureOptimizationPreparationTime"
+ "textureOptimizationTime"
+ "totalTime_"
+ "{AdaptiveCubeFWDReport=\"time_data_convert\"d\"time_construct_vertices_faces\"d}"
+ "{InverseRenderReport=\"time_texture_optimization_preparation\"d\"time_texture_optimization\"d\"time_build_material_maps\"d}"
- "1.5.23"
- "T^{CGImage=},V_mraImage"
- "_mraImage"

```
