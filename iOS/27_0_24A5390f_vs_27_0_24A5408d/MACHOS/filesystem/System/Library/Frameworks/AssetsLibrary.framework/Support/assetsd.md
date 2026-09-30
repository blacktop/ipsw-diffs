## assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__data`

```diff

-910.33.102.0.0
-  __TEXT.__text: 0x1827c
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_stubs: 0x4ac0
-  __TEXT.__objc_methlist: 0xe14
+912.0.111.0.0
+  __TEXT.__text: 0x18ecc
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_stubs: 0x4ca0
+  __TEXT.__objc_methlist: 0xe74
   __TEXT.__dlopen_cstrs: 0x11b
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x554
-  __TEXT.__objc_classname: 0x6e1
-  __TEXT.__objc_methname: 0x563c
+  __TEXT.__const: 0x120
+  __TEXT.__gcc_except_tab: 0x624
+  __TEXT.__objc_classname: 0x70b
+  __TEXT.__objc_methname: 0x5851
   __TEXT.__objc_methtype: 0x98d
-  __TEXT.__oslogstring: 0x3ff7
-  __TEXT.__cstring: 0x175e
-  __TEXT.__unwind_info: 0x548
-  __DATA_CONST.__const: 0xf10
-  __DATA_CONST.__cfstring: 0xb60
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__oslogstring: 0x4264
+  __TEXT.__cstring: 0x1776
+  __TEXT.__unwind_info: 0x568
+  __DATA_CONST.__const: 0xf38
+  __DATA_CONST.__cfstring: 0xb80
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x5b0
-  __DATA_CONST.__got: 0x700
-  __DATA.__objc_const: 0x2cd8
-  __DATA.__objc_selrefs: 0x1490
+  __DATA_CONST.__objc_intobj: 0xa8
+  __DATA_CONST.__objc_arraydata: 0x40
+  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__auth_got: 0x5b8
+  __DATA_CONST.__got: 0x720
+  __DATA.__objc_const: 0x2dc8
+  __DATA.__objc_selrefs: 0x1508
   __DATA.__objc_ivar: 0x7c
-  __DATA.__objc_data: 0xdc0
+  __DATA.__objc_data: 0xe10
   __DATA.__data: 0x360
   __DATA.__bss: 0x58
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 358
-  Symbols:   416
-  CStrings:  1257
+  Functions: 366
+  Symbols:   421
+  CStrings:  1283
 
Symbols:
+ _NSURLIsSymbolicLinkKey
+ _OBJC_CLASS_$_PLAssetsdMigrationService
+ _OBJC_CLASS_$_PLPhotoLibraryPathManagerCore
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
