## photolibraryd

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/Support/photolibraryd`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x1da68
+751.0.104.0.0
+  __TEXT.__text: 0x1e36c
   __TEXT.__auth_stubs: 0xa10
   __TEXT.__objc_stubs: 0x4c00
-  __TEXT.__objc_methlist: 0xb90
-  __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x858
-  __TEXT.__objc_classname: 0x675
-  __TEXT.__objc_methname: 0x5778
-  __TEXT.__objc_methtype: 0xae1
-  __TEXT.__oslogstring: 0x391a
-  __TEXT.__cstring: 0x1a45
+  __TEXT.__objc_methlist: 0xf3c
   __TEXT.__dlopen_cstrs: 0x5e
+  __TEXT.__const: 0x148
+  __TEXT.__gcc_except_tab: 0x894
+  __TEXT.__objc_classname: 0x675
+  __TEXT.__objc_methname: 0x57ac
+  __TEXT.__objc_methtype: 0xac2
+  __TEXT.__oslogstring: 0x3ae5
+  __TEXT.__cstring: 0x1b80
   __TEXT.metaschema: 0xc000
-  __TEXT.__unwind_info: 0x610
+  __TEXT.__unwind_info: 0x5e0
   __DATA_CONST.__auth_got: 0x518
   __DATA_CONST.__got: 0x7a8
-  __DATA_CONST.__const: 0xc68
-  __DATA_CONST.__cfstring: 0xf00
+  __DATA_CONST.__const: 0x1048
+  __DATA_CONST.__cfstring: 0xee0
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0xa8
+  __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x3200
-  __DATA.__objc_selrefs: 0x13f0
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA.__objc_const: 0x2b38
+  __DATA.__objc_selrefs: 0x14f8
   __DATA.__objc_ivar: 0x98
   __DATA.__objc_data: 0xcd0
   __DATA.__data: 0x3c0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 410655E7-635B-334E-ACEF-26117EE38256
-  Functions: 407
+  UUID: D6F9C32A-8E8B-3BFE-AF1F-0D575BEB5B5A
+  Functions: 405
   Symbols:   420
-  CStrings:  1421
+  CStrings:  1428
 
Symbols:
+ _OBJC_CLASS_$_PLInitialSuggestionsManager
+ _PLLibraryServicesOperationNameCheckForAutoCreateWellKnownLibrary
+ _PLLibraryServicesOperationNameCrashRecoveryProcessAssetAlbumAssociativity
+ _PLPhotosBundleId
+ _PLTransactionScopeAlbumTrashCycle
- _NSCurrentLocaleDidChangeNotification
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_CLASS_$_PLAssetsdService
- _OBJC_CLASS_$_PLLibraryOpenerCreationOptions
- _PLMacPlatformLibraryServicesOperationNameCheckForAutoCreateSPL
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
+ "Generating global initial search suggestions..."
+ "Initial sync of shared albums on library open. RefreshResetSync: NO"
+ "PLSpotlightDaemonClientHandler failed to open system photo library"
+ "Photo library database at %@ cannot be opened: %@"
+ "Update asset album associativity because of outstanding transactions"
+ "[sync.spotlightReceiver] unable to signal background processing needed for library %td: %@"
+ "autoCreateWellKnownPhotoLibraryIfNeededWithURL:libraryServicesManager:wellKnownLibraryIdentifier:"
+ "availabilityComputer"
+ "didDropSearchIndexForPhotoLibrary:error:"
+ "generateInitialSuggestionsForPhotoLibrary:"
+ "operationWithName:libraryServicesManager:requiredState:parentProgress:executionBlock:"
+ "operations"
+ "runningLibraryServicesManagerForWellKnownPhotoLibraryIdentifier:error:"
+ "systemPhotoLibraryWithName:"
+ "updateAllAlbumAssociationIfNeededWithLibrary:"
+ "v16@?0@\"PLLibraryServicesManager\"8"
- "%{public}@: Failed to get store metadata in PLLibraryServicesOperationNameCreateSingletonAlbums"
- "@\"NSArray\"24@0:8q16"
- "@24@0:8q16"
- "Photo library database at %@ cannot be opened"
- "[sync.spotlightReceiver] unable to signal background processing needed for library %td"
- "addObserver:selector:name:object:"
- "autoCreateWellKnownPhotoLibraryIfNeededWithURL:wellKnownLibraryIdentifier:"
- "bundleController"
- "com.apple.Photos"
- "currentLocaleDidChangeNotification:"
- "defaultCenter"
- "initWithWellKnownLibraryIdentifier:"
- "libraryServicesManagerForLibraryURL:"
- "operationWithName:requiredState:parentProgress:execution:"
- "operationsForLibraryStateTransition:"
- "searchableItemsDidUpdate:"
- "setCreateMode:options:"

```
