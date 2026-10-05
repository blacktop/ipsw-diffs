## ImmersiveMediaSupport

> `/System/Library/Frameworks/ImmersiveMediaSupport.framework/ImmersiveMediaSupport`

```diff

-124.0.4.0.0
-  __TEXT.__text: 0x17469c
-  __TEXT.__objc_methlist: 0x2b1c
-  __TEXT.__const: 0x1c628
-  __TEXT.__gcc_except_tab: 0x1d34
-  __TEXT.__cstring: 0xa64a
-  __TEXT.__oslogstring: 0x36fc
+124.40.1.0.0
+  __TEXT.__text: 0x17ad6c
+  __TEXT.__objc_methlist: 0x2cf4
+  __TEXT.__const: 0x1c7c8
+  __TEXT.__gcc_except_tab: 0x1da4
+  __TEXT.__cstring: 0xa75a
+  __TEXT.__oslogstring: 0x3a1c
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x333e
-  __TEXT.__swift5_reflstr: 0x4e8e
+  __TEXT.__swift5_typeref: 0x33c0
+  __TEXT.__swift5_reflstr: 0x4f0e
   __TEXT.__swift5_assocty: 0xea0
-  __TEXT.__constg_swiftt: 0x6d3c
-  __TEXT.__swift5_fieldmd: 0x56b0
+  __TEXT.__constg_swiftt: 0x6d9c
+  __TEXT.__swift5_fieldmd: 0x56e0
   __TEXT.__swift5_builtin: 0x230
   __TEXT.__swift5_proto: 0xe44
   __TEXT.__swift5_types: 0x470
-  __TEXT.__swift5_capture: 0xa9c
-  __TEXT.__swift_as_entry: 0x20c
-  __TEXT.__swift_as_ret: 0x1e4
-  __TEXT.__swift_as_cont: 0x680
-  __TEXT.__swift5_mpenum: 0xa8
+  __TEXT.__swift5_capture: 0xac4
+  __TEXT.__swift_as_entry: 0x214
+  __TEXT.__swift_as_ret: 0x1f0
+  __TEXT.__swift_as_cont: 0x6a0
+  __TEXT.__swift5_mpenum: 0xa0
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x77f8
-  __TEXT.__eh_frame: 0xa2cc
+  __TEXT.__unwind_info: 0x7958
+  __TEXT.__eh_frame: 0xa4fc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8d0
-  __DATA_CONST.__objc_classlist: 0x2a0
+  __DATA_CONST.__const: 0x920
+  __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x1f30
+  __DATA_CONST.__objc_selrefs: 0x2068
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__got: 0xbf8
-  __AUTH_CONST.__const: 0xbf50
-  __AUTH_CONST.__cfstring: 0xf00
-  __AUTH_CONST.__objc_const: 0x233d8
+  __DATA_CONST.__objc_arraydata: 0x3a8
+  __DATA_CONST.__got: 0xc28
+  __AUTH_CONST.__const: 0xbff0
+  __AUTH_CONST.__cfstring: 0x1100
+  __AUTH_CONST.__objc_const: 0x24e48
   __AUTH_CONST.__weak_auth_got: 0x50
-  __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x1ae8
-  __AUTH.__objc_data: 0x1390
-  __AUTH.__data: 0x8c28
+  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_dictobj: 0x258
+  __AUTH_CONST.__auth_got: 0x1b10
+  __AUTH.__objc_data: 0x1520
+  __AUTH.__data: 0x8ca8
   __DATA.__objc_ivar: 0x224
-  __DATA.__data: 0x3dd8
+  __DATA.__data: 0x3de8
   __DATA.__common: 0x9e0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8328
-  Symbols:   4305
-  CStrings:  1327
+  Functions: 8414
+  Symbols:   4390
+  CStrings:  1351
 
Symbols:
+ +[IMSMathHelper almostEqualForTolerance:firstVector:secondVector:]
+ +[IMSMathHelper makeArrayFromVector:]
+ +[IMSMathHelper makeQuaternionFromEulerXYZ:]
+ +[IMSMathHelper radiansFromDegrees:]
+ +[IMSMathHelper rotationMatrixFromArray:]
+ +[IMSMathHelper rotationMatrixFromVector:]
+ +[IMSMathHelper scaleMatrixFromArray:]
+ +[IMSMathHelper scaleMatrixFromVector:]
+ +[IMSMathHelper timeFromTimecodeString:]
+ +[IMSMathHelper translationMatrixFromArray:]
+ +[IMSMathHelper translationMatrixFromVector:]
+ +[IMSMeshHelper getCalibrationTypeForGeometryType:]
+ +[IMSMeshHelper getMeshGeometryType:]
+ +[IMSMeshHelper getMeshGeometryTypeForCameraId:]
+ +[IMSMeshHelper getSideloadedMaskForCameraId:]
+ +[IMSMeshHelper getSideloadedMeshForCameraId:]
+ +[IMSMeshHelper getUSDZNameFromCalibrationType:]
+ +[IMSMeshHelper isValidBuiltinMeshCalibrationType:]
+ +[IMSMeshHelper isValidMeshCalibrationType:]
+ +[IMSMeshHelper isValidMeshCamId:]
+ +[IMSMeshHelper isValidSideLoadedMask:]
+ +[IMSMeshHelper isValidSideLoadedMesh:]
+ +[IMSMeshLoader isValidBuiltinMeshCalibrationType:]
+ +[IMSMeshLoader tryLoadPreLoadRectilinearMesh:withCompletionHandler:]
+ +[IMSMeshLoader tryLoadRectilinearMesh:width:height:depth:withCompletionHandler:]
+ +[IMSMeshLoader tryLoadSphericalMesh:originalGeometryType:fov:withCompletionHandler:]
+ +[IMSMeshLoader tryLoadSphericalMesh:withCompletionHandler:]
+ +[IMSRectilinear generateMesh:]
+ +[IMSRectilinear generateMesh:height:depth:withCompletionHandler:]
+ +[IMSRectilinear generateMesh:withCompletionHandler:]
+ +[IMSRuntimeMaskRenderer minimumControlPointsForInterpolation:]
+ +[IMSSphericalEquirect generateMeshDome:originalGeometryType:fov:horizontalSegments:verticalSegments:withCompletionHandler:]
+ +[IMSSphericalEquirect generateMeshsphere:fov:horizontalSegments:verticalSegments:withCompletionHandler:]
+ +[NSError(IMSMeshLoadingErrors) ims_mesh_loading_errorWithCode:errorDescription:]
+ _IMSMeshCalibrationTypeMap
+ _IMSMeshCameraIdToGeometryTypeMap
+ _IMSMeshCameraIdToSideloadedMask
+ _IMSMeshCameraIdToSideloadedMesh
+ _IMSMeshDefaultCamIds
+ _IMSMeshLoadingErrorDomain
+ _IMSSideLoadedMaskList
+ _IMSSideLoadedMeshList
+ _OBJC_CLASS_$_IMSMathHelper
+ _OBJC_CLASS_$_IMSMeshHelper
+ _OBJC_CLASS_$_IMSMeshLoader
+ _OBJC_CLASS_$_IMSRectilinear
+ _OBJC_CLASS_$_IMSSphericalEquirect
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSSet
+ _OBJC_METACLASS_$_IMSMathHelper
+ _OBJC_METACLASS_$_IMSMeshHelper
+ _OBJC_METACLASS_$_IMSMeshLoader
+ _OBJC_METACLASS_$_IMSRectilinear
+ _OBJC_METACLASS_$_IMSSphericalEquirect
+ __OBJC_$_CATEGORY_NSError_$_IMSMeshLoadingErrors
+ __OBJC_$_CLASS_METHODS_IMSMathHelper
+ __OBJC_$_CLASS_METHODS_IMSMeshHelper
+ __OBJC_$_CLASS_METHODS_IMSMeshLoader
+ __OBJC_$_CLASS_METHODS_IMSRectilinear
+ __OBJC_$_CLASS_METHODS_IMSRuntimeMaskRenderer
+ __OBJC_$_CLASS_METHODS_IMSSphericalEquirect
+ __OBJC_$_CLASS_METHODS_NSError(IMSMeshLoadingErrors|IMSArchiveReadErrors|IMSLoadIconErrors|IMSCustomTextureLoadingErrors)
+ __OBJC_CLASS_RO_$_IMSMathHelper
+ __OBJC_CLASS_RO_$_IMSMeshHelper
+ __OBJC_CLASS_RO_$_IMSMeshLoader
+ __OBJC_CLASS_RO_$_IMSRectilinear
+ __OBJC_CLASS_RO_$_IMSSphericalEquirect
+ __OBJC_METACLASS_RO_$_IMSMathHelper
+ __OBJC_METACLASS_RO_$_IMSMeshHelper
+ __OBJC_METACLASS_RO_$_IMSMeshLoader
+ __OBJC_METACLASS_RO_$_IMSRectilinear
+ __OBJC_METACLASS_RO_$_IMSSphericalEquirect
+ ___69+[IMSMeshLoader tryLoadPreLoadRectilinearMesh:withCompletionHandler:]_block_invoke
+ ___81+[IMSMeshLoader tryLoadRectilinearMesh:width:height:depth:withCompletionHandler:]_block_invoke
+ ___85+[IMSMeshLoader tryLoadSphericalMesh:originalGeometryType:fov:withCompletionHandler:]_block_invoke
+ ___85+[IMSMeshLoader tryLoadSphericalMesh:originalGeometryType:fov:withCompletionHandler:]_block_invoke_2
+ ___85+[IMSMeshLoader tryLoadSphericalMesh:originalGeometryType:fov:withCompletionHandler:]_block_invoke_3
+ ___block_descriptor_40_e8_32bs_e49_v64?0{IMSMeshGeometryData=II*^I^^^}8"NSError"56ls32l8
+ ___sincos_stret
+ ___swift_memcpy225_8
+ ___swift_memcpy337_16
+ _fmod
+ _malloc_type_malloc
+ _objc_retain_x4
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _symbolic SS8cameraID______Sg14lensDefinition_____Sg8maskDatat 21ImmersiveMediaSupport0A20CameraLensDefinitionV AA0A11DynamicMaskV
+ _symbolic So7MDLMeshC8leftMesh_AB05rightC0tSg
+ _symbolic So7MDLMeshC8leftMesh_AB05rightC0tSgz_Xx
- __OBJC_$_CATEGORY_NSError_$_IMSArchiveReadErrors
- __OBJC_$_CLASS_METHODS_NSError(IMSArchiveReadErrors|IMSLoadIconErrors|IMSCustomTextureLoadingErrors)
- ___swift_memcpy224_8
- ___swift_memcpy321_16
CStrings:
+ ".usdz"
+ ":"
+ "Builtin mesh generation failed for %s: %@"
+ "Builtin mesh generation produced empty geometry"
+ "Builtin mesh generation produced geometry without texture coordinates"
+ "Could not register preload camera %s - geometry or mask failed to load."
+ "Failed to create the empty mask texture"
+ "Failed to generate builtin geometry for preload camera %s"
+ "Generated builtin geometry for preload camera %s"
+ "IMSMeshLoadingErrorDomain"
+ "Invalid Geometry - Unsupported mesh type"
+ "No builtin geometry type mapped for preload camera %s"
+ "Preload camera %s is not declared in the venue descriptor, registering it dynamically"
+ "Sideloaded calibration asset %s is missing from the ImmersiveMediaSupport bundle"
+ "Unsupported builtin geometry type %u for preload camera %s"
+ "[Mask] Mask Data is invalid, return full mask: interpolation %ld requires >= %lu control points (left %lu, right %lu)"
+ "_default_preroll_cg_lens_01.png"
+ "_default_preroll_cg_s45_01.png"
+ "_default_preroll_cg_s45_01.usdz"
+ "_default_preroll_rect_lens_01.png"
+ "customEquirectMesh"
+ "hemisphericalEquirectMesh"
+ "nexcalivrMesh"
+ "rectilinearMesh"
+ "sphericalEquirectMesh"
+ "v64@?0{IMSMeshGeometryData=II*^I^^^}8@\"NSError\"56"
- "Override params present but no lens definition"
- "[Mask] Mask Data is invalid, return full mask: left %d, right %d"
```
