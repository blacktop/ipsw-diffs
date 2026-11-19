## ImmersiveMediaSupport

> `/System/Library/Frameworks/ImmersiveMediaSupport.framework/Versions/A/ImmersiveMediaSupport`

```diff

-124.0.4.0.0
-  __TEXT.__text: 0x219b50
-  __TEXT.__objc_methlist: 0x2d9c
-  __TEXT.__const: 0x1f868
-  __TEXT.__gcc_except_tab: 0x1d3c
-  __TEXT.__cstring: 0xafaa
-  __TEXT.__oslogstring: 0x60ec
+124.40.1.0.0
+  __TEXT.__text: 0x220900
+  __TEXT.__objc_methlist: 0x2f74
+  __TEXT.__const: 0x1f9b8
+  __TEXT.__gcc_except_tab: 0x1dac
+  __TEXT.__cstring: 0xb0ba
+  __TEXT.__oslogstring: 0x640c
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x3c6c
-  __TEXT.__swift5_reflstr: 0x5c2e
+  __TEXT.__swift5_typeref: 0x3cee
+  __TEXT.__swift5_reflstr: 0x5cae
   __TEXT.__swift5_assocty: 0xf50
-  __TEXT.__constg_swiftt: 0x8e7c
-  __TEXT.__swift5_fieldmd: 0x62c4
+  __TEXT.__constg_swiftt: 0x8edc
+  __TEXT.__swift5_fieldmd: 0x62f4
   __TEXT.__swift5_builtin: 0x2bc
   __TEXT.__swift5_proto: 0xf1c
   __TEXT.__swift5_types: 0x500
-  __TEXT.__swift5_capture: 0x11b0
-  __TEXT.__swift_as_entry: 0x3e4
-  __TEXT.__swift_as_ret: 0x3ac
-  __TEXT.__swift_as_cont: 0xa5c
-  __TEXT.__swift5_mpenum: 0xa8
+  __TEXT.__swift5_capture: 0x11d8
+  __TEXT.__swift_as_entry: 0x3ec
+  __TEXT.__swift_as_ret: 0x3b8
+  __TEXT.__swift_as_cont: 0xa7c
+  __TEXT.__swift5_mpenum: 0xa0
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x81f0
-  __TEXT.__eh_frame: 0xf980
+  __TEXT.__unwind_info: 0x8318
+  __TEXT.__eh_frame: 0xfba0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x998
-  __DATA_CONST.__objc_classlist: 0x310
+  __DATA_CONST.__const: 0x9c0
+  __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x21c8
+  __DATA_CONST.__objc_selrefs: 0x2300
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__got: 0xe68
-  __AUTH_CONST.__const: 0xda90
-  __AUTH_CONST.__cfstring: 0xf00
-  __AUTH_CONST.__objc_const: 0x294f8
+  __DATA_CONST.__objc_arraydata: 0x3a8
+  __DATA_CONST.__got: 0xe98
+  __AUTH_CONST.__const: 0xdb60
+  __AUTH_CONST.__cfstring: 0x1100
+  __AUTH_CONST.__objc_const: 0x2b0d8
   __AUTH_CONST.__weak_auth_got: 0x50
-  __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x1f18
-  __AUTH_CONST.__auth_ptr: 0xed0
-  __AUTH.__objc_data: 0x2270
-  __AUTH.__data: 0xaa48
+  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_dictobj: 0x258
+  __AUTH_CONST.__auth_got: 0x1f38
+  __AUTH_CONST.__auth_ptr: 0xed8
+  __AUTH.__objc_data: 0x2400
+  __AUTH.__data: 0xaac8
   __DATA.__objc_ivar: 0x224
-  __DATA.__data: 0x4688
+  __DATA.__data: 0x46b8
   __DATA.__common: 0xa08
-  __DATA.__bss: 0x1e908
+  __DATA.__bss: 0x1e928
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10230
-  Symbols:   5338
-  CStrings:  1576
+  Functions: 10318
+  Symbols:   5449
+  CStrings:  1600
 
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
+ __85+[IMSMeshLoader tryLoadSphericalMesh:originalGeometryType:fov:withCompletionHandler:]_block_invoke
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
+ ___block_descriptor_40_e8_32bs_e49_v64?0{IMSMeshGeometryData=II*^I^^^}8"NSError"56l
+ ___copy_helper_block_e8_32b
+ ___sincos_stret
+ ___swift_memcpy225_8
+ ___swift_memcpy337_16
+ _fmod
+ _malloc_type_malloc
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$generateMesh:
+ _objc_msgSend$generateMesh:height:depth:withCompletionHandler:
+ _objc_msgSend$generateMeshDome:originalGeometryType:fov:horizontalSegments:verticalSegments:withCompletionHandler:
+ _objc_msgSend$generateMeshsphere:fov:horizontalSegments:verticalSegments:withCompletionHandler:
+ _objc_msgSend$getMeshGeometryTypeForCameraId:
+ _objc_msgSend$getSideloadedMeshForCameraId:
+ _objc_msgSend$ims_mesh_loading_errorWithCode:errorDescription:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$intValue
+ _objc_msgSend$isValidBuiltinMeshCalibrationType:
+ _objc_msgSend$isValidMeshCamId:
+ _objc_msgSend$isValidSideLoadedMask:
+ _objc_msgSend$isValidSideLoadedMesh:
+ _objc_msgSend$makeQuaternionFromEulerXYZ:
+ _objc_msgSend$minimumControlPointsForInterpolation:
+ _objc_msgSend$radiansFromDegrees:
+ _objc_msgSend$rotationMatrixFromVector:
+ _objc_msgSend$scaleMatrixFromVector:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$translationMatrixFromVector:
+ _objc_msgSend$tryLoadPreLoadRectilinearMesh:withCompletionHandler:
+ _objc_msgSend$tryLoadSphericalMesh:originalGeometryType:fov:withCompletionHandler:
+ _objc_msgSend$tryLoadSphericalMesh:withCompletionHandler:
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
