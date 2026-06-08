## SIDInferenceProvider

> `/System/Library/ExtensionKit/Extensions/SIDInferenceProvider.appex/SIDInferenceProvider`

```diff

-1.37.0.0.0
-  __TEXT.__text: 0x112ac
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_stubs: 0x360
+1.53.0.0.0
+  __TEXT.__text: 0x1471c
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_stubs: 0x320
   __TEXT.__objc_methlist: 0x80
-  __TEXT.__const: 0x55a
-  __TEXT.__gcc_except_tab: 0x55c
-  __TEXT.__cstring: 0x70f
+  __TEXT.__const: 0x6de
+  __TEXT.__gcc_except_tab: 0x544
+  __TEXT.__cstring: 0x8f0
   __TEXT.__objc_classname: 0x81
   __TEXT.__objc_methtype: 0xa06
-  __TEXT.__swift5_typeref: 0x1b8
-  __TEXT.__oslogstring: 0x54c
+  __TEXT.__swift5_typeref: 0x293
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x140
-  __TEXT.__swift5_fieldmd: 0x8c
-  __TEXT.__objc_methname: 0x2cd
-  __TEXT.__swift5_reflstr: 0x54
+  __TEXT.__constg_swiftt: 0x190
+  __TEXT.__swift5_fieldmd: 0x100
+  __TEXT.__objc_methname: 0x2ad
+  __TEXT.__swift5_reflstr: 0x106
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_proto: 0x2c
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift_as_entry: 0x54
-  __TEXT.__swift_as_ret: 0x54
-  __TEXT.__unwind_info: 0x4a8
-  __TEXT.__eh_frame: 0xd30
-  __DATA_CONST.__auth_got: 0x770
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__auth_ptr: 0x1b8
-  __DATA_CONST.__const: 0x1a8
+  __TEXT.__oslogstring: 0xa48
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_mpenum: 0x14
+  __TEXT.__swift5_proto: 0x34
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x44
+  __TEXT.__swift_as_cont: 0x68
+  __TEXT.__unwind_info: 0x450
+  __TEXT.__eh_frame: 0xab8
+  __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x888
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__auth_ptr: 0x220
   __DATA.__objc_const: 0x1b0
-  __DATA.__objc_selrefs: 0xd8
+  __DATA.__objc_selrefs: 0xc8
   __DATA.__objc_data: 0x98
-  __DATA.__data: 0x318
-  __DATA.__bss: 0x580
+  __DATA.__data: 0x310
+  __DATA.__bss: 0x6c0
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E2E14954-423E-3889-874C-D6E78658BC14
-  Functions: 211
-  Symbols:   183
-  CStrings:  138
+  UUID: 93A65C42-34B0-38CF-A551-219C9E06FEBD
+  Functions: 227
+  Symbols:   199
+  CStrings:  163
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x3
+ _swift_bridgeObjectRetain_n
+ _swift_cvw_enumFn_getEnumTag
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x20
- _OBJC_CLASS_$_NSFileManager
- __swift_stdlib_bridgeErrorToNSError
- _objc_retain_x23
CStrings:
+ " out of Int32 range for feature "
+ " rows, expected batchSize "
+ " to Float16 for feature "
+ " to Float32 for feature "
+ " to Int32 for feature "
+ "' is not AssetBackedCoreMLRankingModelBundle"
+ "' requires assetDirectory but none was provided"
+ ". Asset not loaded."
+ "Cannot convert non-integer Float32 "
+ "Data size mismatch for Float16 array"
+ "Data size mismatch for Float32 array"
+ "Data size mismatch for Int32 array"
+ "Embedded model '"
+ "Failed to encode ModelManagerResponseData"
+ "Failed to fetch inference config for asset: "
+ "Failed to fetch mobileAsset for '"
+ "Inference execution failed: "
+ "Invalid input data format. Expecting ModelManagerRequestData JSON."
+ "Missing required feature: "
+ "No cached model for: "
+ "No resource bundle found for modelCatalogIdentifier: "
+ "No sideloaded resource found for assetIdentifier: "
+ "Resource bundle for '"
+ "Unknown asset source type: "
+ "Unsupported data type: "
+ "Unsupported load state transition: "
+ "Unsupported output type: "
+ "[SIDInferenceProvider][buildModelPath] Unhandled format: %s, using default path"
+ "[SIDInferenceProvider][compileESOP] Compiling model: %s at path: %s"
+ "[SIDInferenceProvider][compileESOP] E5RT compilation failed for %s: %s"
+ "[SIDInferenceProvider][compileESOP] Successfully compiled ESOP for: %s"
+ "[SIDInferenceProvider][convertDataToTaskValueFeatures] Output %s has %ld rows, expected batchSize %ld"
+ "[SIDInferenceProvider][convertToFloat32] Converting Double to Float32 for %s, potential precision loss"
+ "[SIDInferenceProvider][convertToFloat32] Converting Int64 to Float32 for %s, potential precision loss"
+ "[SIDInferenceProvider][loadAsset] Failed to fetch inference config for asset: %s"
+ "[SIDInferenceProvider][loadAsset] Failed to load asset: %s"
+ "[SIDInferenceProvider][loadAsset] Loading asset: %s, modelCatalogIdentifier: %s"
+ "[SIDInferenceProvider][loadAsset] Model already cached: %s"
+ "[SIDInferenceProvider][loadAsset] Resolved model path: %s"
+ "[SIDInferenceProvider][loadAsset] Successfully compiled and cached model: %s, assetVersion: %s"
+ "[SIDInferenceProvider][requestOneShot] No cached model for: %s. loadAsset should have been called first."
+ "[SIDInferenceProvider][requestOneShot] Using cached ESOP for model: %s"
+ "[SIDInferenceProvider][resolveAssetDirectory] Embedded model '%s' requires assetDirectory"
+ "[SIDInferenceProvider][resolveAssetDirectory] Failed to fetch mobileAsset: %s"
+ "[SIDInferenceProvider][resolveAssetDirectory] Fetching mobileAsset for catalogId: %s"
+ "[SIDInferenceProvider][resolveAssetDirectory] Fetching sideloaded asset: %s"
+ "[SIDInferenceProvider][resolveAssetDirectory] Invalid bundle type for: %s"
+ "[SIDInferenceProvider][resolveAssetDirectory] MobileAsset at: %s"
+ "[SIDInferenceProvider][resolveAssetDirectory] No resource bundle found for: %s"
+ "[SIDInferenceProvider][resolveAssetDirectory] No sideloaded resource found for: %s"
+ "[SIDInferenceProvider][resolveAssetDirectory] Sideloaded asset at: %s"
+ "[SIDInferenceProvider][resolveAssetDirectory] Unknown asset source type: %s"
+ "[SIDInferenceProvider][resolveAssetDirectory] Using embedded path: %s"
+ "[SIDInferenceProvider][unloadAsset] Error during unload for asset %s: %s"
+ "[SIDInferenceProvider][unloadAsset] No cached model found for asset: %s, model: %s"
+ "[SIDInferenceProvider][unloadAsset] No inference config found for asset: %s"
+ "[SIDInferenceProvider][unloadAsset] Successfully unloaded asset: %s, model: %s"
+ "[SIDInferenceProvider][unloadAsset] Unloading asset: %s"
+ "cachedModels"
+ "model.specialization.bundle"
- ". We support int32 and float32."
- "Data size is not a multiple of the expected row size. Data size: "
- "ESOP execution failed: "
- "Expected inference workflow for use case: "
- "Failed to encode response data"
- "Failed to fetch workflow."
- "Failed to get asset URL: "
- "Failure encoding output data"
- "Features do not match input definition"
- "Invalid input data format. Expecting EnhancedUseCaseRequest JSON."
- "Invalid model path: "
- "Model is unavailable for identifier: "
- "No workflow found for use case: "
- "Unhandled InferenceModelFormat: "
- "Unsupported feature data type: "
- "Unsupported load state transition."
- "[SIDInferenceProvider][compileESOP] Calling SIDE5Operations.compileAndRetrieveESOP"
- "[SIDInferenceProvider][compileESOP] Error details: %s"
- "[SIDInferenceProvider][compileESOP] Retrieved model path: %s"
- "[SIDInferenceProvider][compileESOP] SIDE5Operations.compileAndRetrieveESOP failed with error: %@"
- "[SIDInferenceProvider][compileESOP] Successfully compiled ESOP for model: %s"
- "[SIDInferenceProvider][getWorkflowAndESOP] Compiling ESOP for model: %s"
- "[SIDInferenceProvider][getWorkflowAndESOP] Successfully compiled and cached ESOP for model: %s"
- "[SIDInferenceProvider][getWorkflowAndESOP] Using cached ESOP for model: %s"
- "[SIDInferenceProvider][loadAsset] ESOP already cached for model: %s"
- "[SIDInferenceProvider][loadAsset] Fetching workflow for asset identifier %s"
- "[SIDInferenceProvider][loadAsset] Successfully compiled and cached ESOP for model: %s"
- "[SIDInferenceProvider][transitionAsset] Error during unload: %@"
- "[SIDInferenceProvider][transitionAsset] Fetching workflow for asset identifier %s"
- "[SIDInferenceProvider][transitionAsset] No cached ESOP found for asset: %s, model: %s"
- "[SIDInferenceProvider][transitionAsset] No workflow found for asset: %s"
- "[SIDInferenceProvider][transitionAsset] Successfully unloaded asset: %s, model: %s"
- "cachedESOPs"
- "defaultManager"
- "fileExistsAtPath:"

```
