## photolibraryd

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/Support/photolibraryd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__data`

```diff

-910.34.101.0.0
-  __TEXT.__text: 0x1eed0
-  __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_stubs: 0x55a0
-  __TEXT.__objc_methlist: 0x107c
+911.0.134.0.0
+  __TEXT.__text: 0x1fc60
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__objc_stubs: 0x57a0
+  __TEXT.__objc_methlist: 0x10dc
   __TEXT.__dlopen_cstrs: 0xc5
-  __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x828
-  __TEXT.__objc_classname: 0x757
-  __TEXT.__objc_methname: 0x618e
+  __TEXT.__const: 0x168
+  __TEXT.__gcc_except_tab: 0x8f8
+  __TEXT.__objc_classname: 0x781
+  __TEXT.__objc_methname: 0x63ae
   __TEXT.__objc_methtype: 0xb9f
-  __TEXT.__oslogstring: 0x3f1b
-  __TEXT.__cstring: 0x1f8a
+  __TEXT.__oslogstring: 0x4188
+  __TEXT.__cstring: 0x1fa2
   __TEXT.metaschema: 0xc000
-  __TEXT.__unwind_info: 0x648
+  __TEXT.__unwind_info: 0x668
   __DATA_CONST.__const: 0x1270
-  __DATA_CONST.__cfstring: 0x1020
-  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__cfstring: 0x1040
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x50
+  __DATA_CONST.__objc_intobj: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x4f0
-  __DATA_CONST.__got: 0x790
-  __DATA.__objc_const: 0x3078
-  __DATA.__objc_selrefs: 0x1770
+  __DATA_CONST.__auth_got: 0x4f8
+  __DATA_CONST.__got: 0x7a8
+  __DATA.__objc_const: 0x3168
+  __DATA.__objc_selrefs: 0x17f0
   __DATA.__objc_ivar: 0xa8
-  __DATA.__objc_data: 0xe60
+  __DATA.__objc_data: 0xeb0
   __DATA.__data: 0x420
   __DATA.__bss: 0x51
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 441
-  Symbols:   411
-  CStrings:  1445
+  Functions: 450
+  Symbols:   415
+  CStrings:  1472
 
Symbols:
+ _NSURLIsSymbolicLinkKey
+ _OBJC_CLASS_$_PLAssetsdMigrationService
+ _OBJC_CLASS_$_PLPhotoLibrarySearchCriteria
+ _PLIsErrorOrUnderlyingErrorFileNotFound
CStrings:
+ "Cannot stat File Provider cache file %@, error: %d"
+ "Failed to create enumerator for File Provider cache directory: %@"
+ "Failed to enumerate File Provider cache entry at URL: %@, error: %@"
+ "File Provider Storage"
+ "File Provider cache cleanup complete: removed %tu of %tu entries"
+ "File Provider cache cleanup: Failed to cleanup path %@. Error: %@"
+ "File Provider cache cleanup: Skipping file path cleanup %@"
+ "PLFileProviderCacheCleanupMaintenanceTask"
+ "Refusing to run File Provider cache cleanup, unexpected document storage URL: %@"
+ "Skipping File Provider cache cleanup, unable to resolve document storage URL: %@"
+ "URLByDeletingLastPathComponent"
+ "Unable to determine relationship of File Provider cache URL %@ to its parent %@: %@"
+ "_allKnownLibraryURLs"
+ "_cleanUpFileProviderCacheAtURL:transaction:"
+ "_isSaneFileProviderCacheRootURL:"
+ "_registeredCriticalMaintenanceTaskClasses"
+ "_shouldRemoveFileProviderCacheFileAtURL:"
+ "addObjectsFromArray:"
+ "allObjects"
+ "allWellKnownAppDomainLibraryContainerIdentifiers"
+ "dateWithTimeIntervalSince1970:"
+ "deactivateFromOperationWithInvalidationError:asyncNodeCleanupBlock:"
+ "enabledFeatureDataclasses"
+ "findPhotoLibraryIdentifiersMatchingSearchCriteria:error:"
+ "getRelationship:ofDirectoryAtURL:toItemAtURL:error:"
+ "orderedSet"
+ "photosFileProviderManagerDocumentStorageURL:"
+ "setContainerIdentifier:"
+ "setDomain:"
- "_registeredCriticalMaintenaceTaskClasses"
- "deactivateWithInvalidationError:"
```
