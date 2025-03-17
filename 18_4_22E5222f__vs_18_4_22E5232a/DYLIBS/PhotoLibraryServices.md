## PhotoLibraryServices

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices`

```diff

-750.17.102.0.0
-  __TEXT.__text: 0x697a14
-  __TEXT.__auth_stubs: 0x3f30
+752.0.105.0.0
+  __TEXT.__text: 0x69a3e0
+  __TEXT.__auth_stubs: 0x3f40
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x40cd4
+  __TEXT.__objc_methlist: 0x40f44
   __TEXT.__const: 0x5f40
   __TEXT.__dlopen_cstrs: 0xa03
-  __TEXT.__gcc_except_tab: 0x22a18
-  __TEXT.__oslogstring: 0x77704
-  __TEXT.__cstring: 0x611f5
+  __TEXT.__gcc_except_tab: 0x22a9c
+  __TEXT.__oslogstring: 0x77962
+  __TEXT.__cstring: 0x61243
   __TEXT.__ustring: 0x57c
-  __TEXT.__unwind_info: 0x14180
-  __TEXT.__objc_classname: 0x9c4f
-  __TEXT.__objc_methname: 0xbbc58
-  __TEXT.__objc_methtype: 0x12270
-  __TEXT.__objc_stubs: 0x77840
+  __TEXT.__unwind_info: 0x14268
+  __TEXT.__objc_classname: 0x9c7a
+  __TEXT.__objc_methname: 0xbc2b0
+  __TEXT.__objc_methtype: 0x12297
+  __TEXT.__objc_stubs: 0x77d00
   __DATA_CONST.__got: 0x4ae8
-  __DATA_CONST.__const: 0x14af0
+  __DATA_CONST.__const: 0x14b40
   __DATA_CONST.__objc_classlist: 0x20e0
   __DATA_CONST.__objc_catlist: 0xf0
-  __DATA_CONST.__objc_protolist: 0x688
+  __DATA_CONST.__objc_protolist: 0x690
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22d90
+  __DATA_CONST.__objc_selrefs: 0x22f50
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x1528
   __DATA_CONST.__objc_arraydata: 0x18f0
-  __AUTH_CONST.__auth_got: 0x1fb0
+  __AUTH_CONST.__auth_got: 0x1fb8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x5358
-  __AUTH_CONST.__cfstring: 0x4c940
-  __AUTH_CONST.__objc_const: 0x68098
+  __AUTH_CONST.__cfstring: 0x4c9a0
+  __AUTH_CONST.__objc_const: 0x680c0
   __AUTH_CONST.__objc_intobj: 0x4710
   __AUTH_CONST.__objc_arrayobj: 0x1200
   __AUTH_CONST.__objc_doubleobj: 0x110

   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH.__objc_data: 0x11490
   __DATA.__objc_ivar: 0x3c70
-  __DATA.__data: 0x5ec0
+  __DATA.__data: 0x5f20
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x2508
   __DATA.__common: 0xc

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 25625
-  Symbols:   31694
-  CStrings:  47119
+  Functions: 25682
+  Symbols:   31752
+  CStrings:  47190
 
Symbols:
+ _PLVoidResultFromResultAndError
CStrings:
+ "/Application/"
+ "@\"PLResult\"24@0:8q16"
+ "Bound to %@"
+ "CloudInternalService"
+ "CloudService"
+ "Created missing identifier for library bundle %@: %{public}@"
+ "Creating missing identifier for library bundle %@"
+ "DebugService"
+ "DemoService"
+ "DiagnosticsService"
+ "Error writing tombstone for photo library at %@ : %@"
+ "Failed to create photo library bundle with default name matching identifier UUID %{public}@: %{public}@, renamed %@ as %{public}@.%{public}@"
+ "Library identifier is already persisted for this URL, existing '%@' vs. requested '%@'"
+ "LibraryInternalService"
+ "LibraryManagementService"
+ "LibraryService"
+ "MigrationService"
+ "Need to bind to URL: %@"
+ "NonBindingDebugService"
+ "NotificationService"
+ "PLAssetsdNonBindingPhotoKitServiceProtocol"
+ "PhotoKitAddService"
+ "PhotoKitAddService_applyChangesRequest:libraryToken:reply:"
+ "PhotoKitService"
+ "PhotoKitService_applyChangesRequest:libraryToken:reply:"
+ "PrivacySupportService"
+ "ResourceAvailabilityService"
+ "ResourceInternalService"
+ "ResourceService"
+ "ResourceWriteOnlyService"
+ "Skipping tombstoned library bundle %{public}@ with library URL %@"
+ "SyncService"
+ "SystemLibraryURLReadOnlyService"
+ "Updating library identifier path %@ to match real path %@"
+ "Wrote tombstone for photo library at %@"
+ "_addWellKnownIdentifierFromIdentifierMap:updateLibraryURL:"
+ "_awaitForRequiredLibraryStateWithContext:"
+ "_checkLibraryDeletionTombstoneForLibraryURL:"
+ "_createPhotoLibraryDatabaseWithOptions:error:"
+ "_deleteLibraryFromFilesystemAtURL:shouldWriteTombstone:error:"
+ "_prepareLibraryForDeletionWithTombstone:libraryURL:error:"
+ "_removeAppPhotoLibrariesForApplication: Adding default GP library URL, failed to find library identifier"
+ "_removeAppPhotoLibrariesForApplication: Error preparing library for deletion %@: %@"
+ "_removeAppPhotoLibrariesForApplication: Missing library URL found for identifier %@"
+ "_removeAppPhotoLibrariesForApplication: No bundle found for libraryURL: %@"
+ "_validateWithContext:"
+ "awaitLibraryState:"
+ "bindToPhotoLibraryURL:sandboxExtension:clientOptions:"
+ "bindWithToken:"
+ "bundle exists"
+ "clientOptions"
+ "defaultLibraryURLForLibraryDomain:container:uuid:"
+ "deleteLibraryFromFilesystemAtURL:shouldWriteTombstone:error:"
+ "found tombstone"
+ "innerServiceWithContext:forceValidation:"
+ "makeInnerCloudInternalService"
+ "makeInnerCloudService"
+ "makeInnerDebugService"
+ "makeInnerDemoService"
+ "makeInnerDiagnosticsService"
+ "makeInnerLibraryInternalService"
+ "makeInnerLibraryManagementService"
+ "makeInnerLibraryService"
+ "makeInnerMigrationService"
+ "makeInnerNonBindingDebugService"
+ "makeInnerNotificationService"
+ "makeInnerPhotoKitAddService"
+ "makeInnerPhotoKitService"
+ "makeInnerPrivacySupportService"
+ "makeInnerResourceAvailabilityService"
+ "makeInnerResourceInternalService"
+ "makeInnerResourceService"
+ "makeInnerResourceWriteOnlyService"
+ "makeInnerSyncService"
+ "makeInnerSystemLibraryURLReadOnlyService"
+ "performAtomicLibraryIdentifierAccessBlock:"
+ "photosLibrariesDataVaultPath"
+ "photosLibraryTombstoneExtension"
+ "prepareLibraryForDeletionWithTombstone:libraryURL:error:"
+ "sandboxExtension"
+ "v40@0:8@\"PLXPCObject\"16@\"PLXPCLibraryToken\"24@?<v@?B@\"NSError\">32"
- "Failed to create photo library bundle with name matching identifier UUID %{public}@, renamed as %{public}@.%{public}@"
- "Library identifier is already persisted for this url"
- "Library identifier path %@ does not match real path %@"
- "_addWellKnownIdentifierFromIdentifierMap:libraryURL:"
- "_awaitForRequiredLibraryStateWithContext:completionHandler:"
- "_removeAppPhotoLibrariesForApplication: No bundle found for libraryURL %@"
- "bindToPhotoLibraryURL:sandboxExtension:withReply:"
- "deleteLibraryFromFilesystemAtURL:error:"
- "instantiateInnerService"
- "v40@0:8@\"NSURL\"16@\"NSData\"24@?<v@?@\"NSError\">32"

```
