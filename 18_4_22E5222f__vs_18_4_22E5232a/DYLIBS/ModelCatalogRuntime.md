## ModelCatalogRuntime

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime`

```diff

-162.749.5.1.0
-  __TEXT.__text: 0x59e5c
-  __TEXT.__auth_stubs: 0x1f60
+162.749.7.0.0
+  __TEXT.__text: 0x623a8
+  __TEXT.__auth_stubs: 0x1fa0
   __TEXT.__objc_methlist: 0x4c8
   __TEXT.__const: 0x1408
-  __TEXT.__swift5_typeref: 0x11a7
-  __TEXT.__swift5_fieldmd: 0x714
-  __TEXT.__constg_swiftt: 0xc28
-  __TEXT.__cstring: 0x1823
+  __TEXT.__swift5_typeref: 0x11e7
+  __TEXT.__swift5_fieldmd: 0x720
+  __TEXT.__constg_swiftt: 0xc58
+  __TEXT.__cstring: 0x19c3
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x640
+  __TEXT.__swift5_reflstr: 0x660
   __TEXT.__swift5_assocty: 0x118
-  __TEXT.__oslogstring: 0x2e0a
+  __TEXT.__oslogstring: 0x2e8a
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_proto: 0xa0
   __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_capture: 0x548
-  __TEXT.__swift_as_entry: 0xfc
-  __TEXT.__swift_as_ret: 0x11c
-  __TEXT.__unwind_info: 0x1410
-  __TEXT.__eh_frame: 0x371c
+  __TEXT.__swift_as_entry: 0x114
+  __TEXT.__swift_as_ret: 0x14c
+  __TEXT.__unwind_info: 0x1530
+  __TEXT.__eh_frame: 0x3bd4
   __TEXT.__objc_classname: 0x45
-  __TEXT.__objc_methname: 0x971
+  __TEXT.__objc_methname: 0x9b9
   __TEXT.__objc_methtype: 0x127
-  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x338
+  __DATA_CONST.__objc_selrefs: 0x358
   __DATA_CONST.__objc_protorefs: 0x38
-  __AUTH_CONST.__auth_got: 0xfb0
-  __AUTH_CONST.__auth_ptr: 0x798
+  __AUTH_CONST.__auth_got: 0xfd0
+  __AUTH_CONST.__auth_ptr: 0x7a8
   __AUTH_CONST.__const: 0x16d0
-  __AUTH_CONST.__objc_const: 0xf30
-  __AUTH.__objc_data: 0x328
-  __AUTH.__data: 0x878
-  __DATA.__data: 0xaa8
+  __AUTH_CONST.__objc_const: 0xf50
+  __AUTH.__objc_data: 0x338
+  __AUTH.__data: 0x898
+  __DATA.__data: 0xae0
   __DATA.__bss: 0xd10
-  __DATA.__common: 0x1c8
-  __DATA_DIRTY.__objc_data: 0xf8
-  __DATA_DIRTY.__data: 0x690
+  __DATA.__common: 0x1e8
+  __DATA_DIRTY.__objc_data: 0x100
+  __DATA_DIRTY.__data: 0x698
   __DATA_DIRTY.__common: 0x98
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1867
-  Symbols:   211
-  CStrings:  454
+  Functions: 2106
+  Symbols:   212
+  CStrings:  468
 
Symbols:
+ _OBJC_CLASS_$_UAFAssetSet
CStrings:
+ " - no asset found"
+ " - no asset set found"
+ " - no asset sets"
+ "Asset %s does not have a location. Metadata: %s"
+ "Could not inflate asset set "
+ "Could not inflate asset sets as the store is not initialized"
+ "assetNamed:"
+ "attemptToInvalidatePendingAssetSets failed to update token: %@"
+ "availableUseCases got nil results, this should only be seen during unit testing"
+ "availableUseCases: Could not fetch usageAgnosticCoherentAssetSets for assetSetName: %s usages: %s"
+ "availableUseCases: resource %s is NOT ready: %@"
+ "availableUseCases: resource %s is ready"
+ "com.apple.if.planner."
+ "location"
+ "metadata"
+ "resourceReadinessProvider"
+ "retrieveAssetSet:usages:consistencyToken:"
+ "triggerInvalidationOfAssetSet failed to update token: %@"
+ "usageAgnosticCoherentAssetSet called on a non-initialized coherence store"
+ "usageAgnosticCoherentAssetSets called on a non-initialized coherence store"
+ "useCaseResourceAvailability: could not fetch usageAgnosticCoherentAssetSets for assetSetName: %s usages: %s"
- "All resources unavailable due to failure to lock: %@"
- "availableUseCases: ALL resources for use case %s are NOT ready due to failure to lock coherent asset lock: %@"
- "availableUseCases: Could not obtain coherent lock for use case %s due to error: %@"
- "availableUseCases: resource %s/%s is NOT ready: %@"
- "availableUseCases: resource %s/%s is ready"
- "resource %s is NOT ready: %@"
- "resource %s is ready"

```
