## assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

-750.5.104.0.0
-  __TEXT.__text: 0x1604c
+750.11.101.0.0
+  __TEXT.__text: 0x165c4
   __TEXT.__auth_stubs: 0xb80
   __TEXT.__objc_stubs: 0x4180
-  __TEXT.__objc_methlist: 0xccc
+  __TEXT.__objc_methlist: 0xcd4
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x55c
+  __TEXT.__const: 0xf0
+  __TEXT.__gcc_except_tab: 0x590
   __TEXT.__objc_classname: 0x5ff
-  __TEXT.__objc_methname: 0x4bfe
-  __TEXT.__objc_methtype: 0x8cf
-  __TEXT.__oslogstring: 0x3a83
-  __TEXT.__cstring: 0x12df
-  __TEXT.__unwind_info: 0x500
+  __TEXT.__objc_methname: 0x4c47
+  __TEXT.__objc_methtype: 0x8b0
+  __TEXT.__oslogstring: 0x3bc1
+  __TEXT.__cstring: 0x142b
+  __TEXT.__unwind_info: 0x4e0
   __DATA_CONST.__auth_got: 0x5d0
-  __DATA_CONST.__got: 0x708
-  __DATA_CONST.__const: 0x8c0
+  __DATA_CONST.__got: 0x700
+  __DATA_CONST.__const: 0xd00
   __DATA_CONST.__cfstring: 0xa20
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__objc_arraydata: 0x30
+  __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x2798
   __DATA.__objc_selrefs: 0x1230
   __DATA.__objc_ivar: 0x6c

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 321
-  Symbols:   422
-  CStrings:  1121
+  Functions: 323
+  Symbols:   421
+  CStrings:  1130
 
Symbols:
+ _PLLibraryServicesOperationNameCheckForAutoCreateWellKnownLibrary
+ _PLMobileSlideshowBundleId
+ _objc_retain_x4
- _OBJC_CLASS_$_PLAssetsdService
- _OBJC_CLASS_$_PLLibraryOpenerCreationOptions
- _PLMacPlatformLibraryServicesOperationNameCheckForAutoCreateSPL
- _objc_retain_x9
CStrings:
+ "%s failed to process deletes for bundle ID %{public}@ error %@"
+ "%s unable to get running LSM: %@"
+ "%{public}@: Failed to get store metadata in %@"
+ "%{public}@: Short-lived PLPhotoLibrary is nil, returning early from %@"
+ "-[PLSpotlightDaemonClientHandler pathManager]"
+ "-[PLSpotlightDaemonClientHandler reindexAllItemsForBundleID:protectionClass:reason:acknowledgementHandler:]"
+ "-[PLSpotlightDaemonClientHandler systemPhotoLibraryWithName:]"
+ "-[PLSyndicationSpotlightReceiver deleteSearchableItemsWithIdentifiers:bundleID:]"
+ "Failed to update feature availability after Spotlight reindex request, error: %@"
+ "LSM is nil, unable to buildQuickActionItems"
+ "PLSpotlightDaemonClientHandler failed to open system photo library"
+ "Photo library database at %@ cannot be opened: %@"
+ "[sync.spotlightReceiver] unable to signal background processing needed for library %td: %@"
+ "autoCreateWellKnownPhotoLibraryIfNeededWithURL:libraryServicesManager:wellKnownLibraryIdentifier:"
+ "availabilityComputer"
+ "didDropSearchIndexForPhotoLibrary:error:"
+ "operationWithName:libraryServicesManager:requiredState:parentProgress:executionBlock:"
+ "operations"
+ "runningLibraryServicesManagerForWellKnownPhotoLibraryIdentifier:error:"
+ "systemPhotoLibraryWithName:"
+ "v16@?0@\"PLLibraryServicesManager\"8"
- "%{public}@: Failed to get store metadata in PLLibraryServicesOperationNameCreateSingletonAlbums"
- "@\"NSArray\"24@0:8q16"
- "@24@0:8q16"
- "Photo library database at %@ cannot be opened"
- "[sync.spotlightReceiver] unable to signal background processing needed for library %td"
- "autoCreateWellKnownPhotoLibraryIfNeededWithURL:wellKnownLibraryIdentifier:"
- "bundleController"
- "initWithWellKnownLibraryIdentifier:"
- "libraryServicesManagerForLibraryURL:"
- "operationWithName:requiredState:parentProgress:execution:"
- "operationsForLibraryStateTransition:"
- "setCreateMode:options:"

```
