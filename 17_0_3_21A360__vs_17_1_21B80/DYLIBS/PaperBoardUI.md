## PaperBoardUI

> `/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI`

```diff

-140.12.4.0.0
-  __TEXT.__text: 0x7a910
-  __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__objc_methlist: 0x8b20
-  __TEXT.__const: 0x810
-  __TEXT.__cstring: 0x64d0
-  __TEXT.__oslogstring: 0x3957
+140.26.102.0.0
+  __TEXT.__text: 0x7dbc4
+  __TEXT.__auth_stubs: 0x15d0
+  __TEXT.__objc_methlist: 0x8c88
+  __TEXT.__const: 0x820
+  __TEXT.__cstring: 0x6795
+  __TEXT.__oslogstring: 0x4111
   __TEXT.__gcc_except_tab: 0xa08
   __TEXT.__dlopen_cstrs: 0x252
-  __TEXT.__unwind_info: 0x2628
-  __TEXT.__objc_classname: 0x175d
-  __TEXT.__objc_methname: 0x161af
-  __TEXT.__objc_methtype: 0x425f
-  __TEXT.__objc_stubs: 0x114c0
-  __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x2460
-  __DATA_CONST.__objc_classlist: 0x400
-  __DATA_CONST.__objc_catlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x258
+  __TEXT.__unwind_info: 0x26b4
+  __TEXT.__objc_classname: 0x17b2
+  __TEXT.__objc_methname: 0x166c5
+  __TEXT.__objc_methtype: 0x42d9
+  __TEXT.__objc_stubs: 0x11980
+  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__const: 0x24c8
+  __DATA_CONST.__objc_classlist: 0x408
+  __DATA_CONST.__objc_catlist: 0x78
+  __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1c8f0
-  __DATA_CONST.__objc_selrefs: 0x4ed8
+  __DATA_CONST.__objc_const: 0x1cea0
+  __DATA_CONST.__objc_selrefs: 0x5020
   __DATA_CONST.__objc_arraydata: 0x1f8
-  __AUTH_CONST.__objc_const: 0x3240
-  __AUTH_CONST.__cfstring: 0x6c00
-  __AUTH_CONST.__const: 0xb78
+  __AUTH_CONST.__objc_const: 0x3310
+  __AUTH_CONST.__cfstring: 0x6e20
+  __AUTH_CONST.__const: 0xc58
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x210
-  __AUTH_CONST.__auth_got: 0xae8
-  __AUTH.__objc_data: 0x22b0
+  __AUTH_CONST.__auth_got: 0xaf8
+  __AUTH.__objc_data: 0x2300
   __AUTH.__data: 0x8
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x780
-  __DATA.__objc_superrefs: 0x358
-  __DATA.__objc_ivar: 0x9e4
-  __DATA.__data: 0x1e18
-  __DATA.__bss: 0x108
+  __DATA.__objc_classrefs: 0x7a8
+  __DATA.__objc_superrefs: 0x360
+  __DATA.__objc_ivar: 0xa04
+  __DATA.__data: 0x1e78
+  __DATA.__bss: 0x150
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x2c
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E6B6D88E-C245-3B02-BCF3-BE2F3AE14B92
-  Functions: 3725
-  Symbols:   13321
-  CStrings:  6428
+  UUID: 01165705-586F-3294-8EF2-C4297E80646F
+  Functions: 3781
+  Symbols:   13531
+  CStrings:  6560
 
Symbols:
+ +[PBUIMappedImageCacheManager cleanupOldCaches]
+ +[PBUIMappedImageCacheManager defaultCacheManager]
+ +[PBUIMappedImageCacheManager registerCacheManager:cacheManager:]
+ +[PBUIMappedImageCacheManager registerCacheManager:cacheManager:].cold.1
+ +[PBUIMappedImageCacheManager unregisterCacheManagerForURL:]
+ +[PBUIPosterVariantViewController defaultCacheManager]
+ -[BSUIMappedImageCache(PBUCacheManagerAdditions) pbui_cacheIdentifier]
+ -[BSUIMappedImageCache(PBUCacheManagerAdditions) setPbui_cacheIdentifier:]
+ -[PBUIMappedImageCacheManager .cxx_destruct]
+ -[PBUIMappedImageCacheManager _cacheLock_buildMappedImageCacheForKey:]
+ -[PBUIMappedImageCacheManager _cacheLock_bumpManifestForImageCacheKey:bumpDate:]
+ -[PBUIMappedImageCacheManager _cacheLock_checkoutImageCache:didCreateNew:bumpDate:]
+ -[PBUIMappedImageCacheManager _cacheLock_checkoutImageCache:didCreateNew:bumpDate:].cold.1
+ -[PBUIMappedImageCacheManager _cacheLock_onDiskCaches]
+ -[PBUIMappedImageCacheManager _cacheLock_onDiskCaches].cold.1
+ -[PBUIMappedImageCacheManager _cacheLock_removeCacheForKey:]
+ -[PBUIMappedImageCacheManager _cacheLock_teardownCacheForKey:]
+ -[PBUIMappedImageCacheManager _cacheLock_teardownCacheForKey:].cold.1
+ -[PBUIMappedImageCacheManager _cacheLock_truncateCaches:]
+ -[PBUIMappedImageCacheManager _cacheLock_writeManifest]
+ -[PBUIMappedImageCacheManager _cacheLock_writeManifest].cold.1
+ -[PBUIMappedImageCacheManager _cacheLock_writeManifest].cold.2
+ -[PBUIMappedImageCacheManager activeCaches]
+ -[PBUIMappedImageCacheManager checkoutImageCache:]
+ -[PBUIMappedImageCacheManager checkoutImageCache:date:]
+ -[PBUIMappedImageCacheManager checkoutImageCache:date:].cold.1
+ -[PBUIMappedImageCacheManager dealloc]
+ -[PBUIMappedImageCacheManager description]
+ -[PBUIMappedImageCacheManager initWithNumberOfManagedCaches:pathProvider:]
+ -[PBUIMappedImageCacheManager initWithNumberOfManagedCaches:pathProvider:].cold.1
+ -[PBUIMappedImageCacheManager initWithNumberOfManagedCaches:pathProvider:].cold.2
+ -[PBUIMappedImageCacheManager initWithNumberOfManagedCaches:pathProvider:].cold.3
+ -[PBUIMappedImageCacheManager invalidate]
+ -[PBUIMappedImageCacheManager knownCaches]
+ -[PBUIMappedImageCacheManager numberOfManagedCaches]
+ -[PBUIMappedImageCacheManager pathProvider]
+ -[PBUIMappedImageCacheManager removeImageCacheForKey:]
+ -[PBUIMappedImageCacheManager returnImageCache:]
+ -[PBUIMappedImageCacheManager returnImageCacheForKey:]
+ -[PBUIPosterHomeViewController evaluateSnapshotPreconditions:]
+ -[PBUIPosterVariantViewController _setupCachesIfNeeded]
+ -[PBUIPosterVariantViewController dealloc]
+ -[PBUIPosterVariantViewController evaluateSnapshotPreconditions:]
+ -[PBUIPosterVariantViewController initWithScene:counterpart:]
+ -[PBUIPosterVariantViewController initWithScene:counterpart:].cold.1
+ -[PBUIWallpaperDirectoryDataStore cleanup]
+ -[PBUIWallpaperUserDefaultsDataStore cleanup]
+ GCC_except_table10
+ GCC_except_table38
+ GCC_except_table46
+ _NSURLFileResourceTypeDirectory
+ _NSURLFileResourceTypeKey
+ _NSURLIsRegularFileKey
+ _OBJC_CLASS_$_BSMutableOrderedDictionary
+ _OBJC_CLASS_$_BSOrderedDictionaryKeyStrategy
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_PBUIMappedImageCacheManager
+ _OBJC_IVAR_$_PBUIMappedImageCacheManager._cacheLock
+ _OBJC_IVAR_$_PBUIMappedImageCacheManager._cacheLock_cacheKeyToCache
+ _OBJC_IVAR_$_PBUIMappedImageCacheManager._cacheLock_cacheKeys
+ _OBJC_IVAR_$_PBUIMappedImageCacheManager._cacheLock_manifest
+ _OBJC_IVAR_$_PBUIMappedImageCacheManager._cacheName
+ _OBJC_IVAR_$_PBUIMappedImageCacheManager._cacheURL
+ _OBJC_IVAR_$_PBUIMappedImageCacheManager._invalidationFlag
+ _OBJC_IVAR_$_PBUIMappedImageCacheManager._manifestURL
+ _OBJC_IVAR_$_PBUIMappedImageCacheManager._numberOfManagedCaches
+ _OBJC_IVAR_$_PBUIMappedImageCacheManager._pathProvider
+ _OBJC_METACLASS_$_PBUIMappedImageCacheManager
+ _PBUILogCaching
+ _PBUILogCaching.__logObj
+ _PBUILogCaching.onceToken
+ __OBJC_$_CATEGORY_BSUIMappedImageCache_$_PBUCacheManagerAdditions
+ __OBJC_$_CLASS_METHODS_PBUIMappedImageCacheManager
+ __OBJC_$_INSTANCE_METHODS_BSUIMappedImageCache(PBUCacheManagerAdditions)
+ __OBJC_$_INSTANCE_METHODS_PBUIMappedImageCacheManager
+ __OBJC_$_INSTANCE_VARIABLES_PBUIMappedImageCacheManager
+ __OBJC_$_PROP_LIST_PBUIManagedCacheIdentifying
+ __OBJC_$_PROP_LIST_PBUIMappedImageCacheManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PBUIManagedCacheIdentifying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PBUIManagedCacheIdentifying
+ __OBJC_$_PROTOCOL_REFS_PBUIManagedCacheIdentifying
+ __OBJC_CLASS_PROTOCOLS_$_BSUIMappedImageCache(PBUCacheManagerAdditions)
+ __OBJC_CLASS_PROTOCOLS_$_PBUIMappedImageCacheManager
+ __OBJC_CLASS_RO_$_PBUIMappedImageCacheManager
+ __OBJC_LABEL_PROTOCOL_$_PBUIManagedCacheIdentifying
+ __OBJC_METACLASS_RO_$_PBUIMappedImageCacheManager
+ __OBJC_PROTOCOL_$_PBUIManagedCacheIdentifying
+ ___42-[PBUIWallpaperDirectoryDataStore cleanup]_block_invoke
+ ___42-[PBUIWallpaperDirectoryDataStore cleanup]_block_invoke.cold.1
+ ___48-[PBUIPosterViewController updateConfiguration:]_block_invoke.27
+ ___50+[PBUIMappedImageCacheManager defaultCacheManager]_block_invoke
+ ___50+[PBUIMappedImageCacheManager defaultCacheManager]_block_invoke_2
+ ___57-[PBUIMappedImageCacheManager _cacheLock_truncateCaches:]_block_invoke
+ ___57-[PBUIMappedImageCacheManager _cacheLock_truncateCaches:]_block_invoke_2
+ ___61-[PBUIPosterVariantViewController initWithScene:counterpart:]_block_invoke
+ ___65+[PBUIMappedImageCacheManager registerCacheManager:cacheManager:]_block_invoke
+ ___69-[PBUIPosterViewController _updatePosterScenesForReasons:completion:]_block_invoke.39
+ ___PBUILogCaching_block_invoke
+ _____possibleWallpaperFileNames_block_invoke
+ ___block_descriptor_32_e27_B24?0"NSURL"8"NSError"16l
+ ___block_descriptor_32_e27_q24?0"NSDate"8"NSDate"16l
+ ___block_descriptor_40_e8_32s_e33_v32?0"NSString"8"NSDate"16^B24ls32l8
+ ___block_literal_global.10
+ ___block_literal_global.142
+ ___block_literal_global.352
+ ___block_literal_global.4
+ ___block_literal_global.56
+ ___knownCacheDirectories
+ ___possibleWallpaperFileNames
+ ___possibleWallpaperFileNames.onceToken
+ ___possibleWallpaperFileNames.possibleWallpaperFileNames
+ __knownCacheDirectoryLock
+ __unnamed_array_storage.80
+ _defaultCacheManager.defaultCacheManager
+ _defaultCacheManager.onceToken
+ _kPBUIMappedImageCacheManagerDefaultNumberOfManagedCaches
+ _objc_getAssociatedObject
+ _objc_msgSend$URLByStandardizingPath
+ _objc_msgSend$_cacheLock_buildMappedImageCacheForKey:
+ _objc_msgSend$_cacheLock_bumpManifestForImageCacheKey:bumpDate:
+ _objc_msgSend$_cacheLock_checkoutImageCache:didCreateNew:bumpDate:
+ _objc_msgSend$_cacheLock_onDiskCaches
+ _objc_msgSend$_cacheLock_removeCacheForKey:
+ _objc_msgSend$_cacheLock_teardownCacheForKey:
+ _objc_msgSend$_cacheLock_truncateCaches:
+ _objc_msgSend$_cacheLock_writeManifest
+ _objc_msgSend$_setupCachesIfNeeded
+ _objc_msgSend$activeCaches
+ _objc_msgSend$allKeys
+ _objc_msgSend$allValues
+ _objc_msgSend$appendString:
+ _objc_msgSend$checkoutImageCache:
+ _objc_msgSend$checkoutImageCache:date:
+ _objc_msgSend$cleanupOldCaches
+ _objc_msgSend$compare:
+ _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
+ _objc_msgSend$countForObject:
+ _objc_msgSend$date
+ _objc_msgSend$defaultCacheManager
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$evaluateSnapshotPreconditions:
+ _objc_msgSend$initWithCapacity:keyOrderingStrategy:
+ _objc_msgSend$initWithNumberOfManagedCaches:pathProvider:
+ _objc_msgSend$initWithScene:counterpart:
+ _objc_msgSend$isFileURL
+ _objc_msgSend$numberOfManagedCaches
+ _objc_msgSend$pbui_cacheIdentifier
+ _objc_msgSend$providerFromProvider:
+ _objc_msgSend$registerCacheManager:cacheManager:
+ _objc_msgSend$returnImageCache:
+ _objc_msgSend$returnImageCacheForKey:
+ _objc_msgSend$setPbui_cacheIdentifier:
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$stablePersistenceIdentifier
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$strongToWeakObjectsMapTable
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$unregisterCacheManagerForURL:
+ _objc_setAssociatedObject
+ _registerCacheManager:cacheManager:.onceToken
- -[PBUIPosterHomeViewController evaluateSnapshotPreconditions]
- -[PBUIPosterLockViewController initWithScene:cache:]
- -[PBUIPosterLockViewController initWithScene:cache:].cold.1
- -[PBUIPosterVariantViewController evaluateSnapshotPreconditions]
- -[PBUIPosterVariantViewController initWithCoder:]
- -[PBUIPosterVariantViewController initWithNibName:bundle:]
- -[PBUIPosterVariantViewController initWithScene:cache:]
- -[PBUIPosterVariantViewController initWithScene:cache:].cold.1
- -[PBUIPosterVariantViewController initWithScene:storagePath:]
- -[PBUIPosterViewController defaultStoragePath]
- -[PBUIPosterViewController makeImageCacheForVariant:]
- GCC_except_table11
- GCC_except_table40
- GCC_except_table43
- _OBJC_IVAR_$_PBUIPosterViewController._homeVCCache
- _OBJC_IVAR_$_PBUIPosterViewController._lockVCCache
- ___48-[PBUIPosterViewController updateConfiguration:]_block_invoke.33
- ___55-[PBUIPosterVariantViewController initWithScene:cache:]_block_invoke
- ___69-[PBUIPosterViewController _updatePosterScenesForReasons:completion:]_block_invoke.50
- ___block_literal_global.150
- ___block_literal_global.330
- __unnamed_array_storage.86
- _objc_msgSend$defaultStoragePath
- _objc_msgSend$evaluateSnapshotPreconditions
- _objc_msgSend$initWithScene:cache:
- _objc_msgSend$initWithScene:storagePath:
- _objc_msgSend$makeImageCacheForVariant:
CStrings:
+ "\x0ea"
+ "\x18"
+ ".CacheManagerManifest.plist"
+ "@\"BSUIMappedImageCache<PBUIManagedCacheIdentifying>\""
+ "@\"NSCountedSet\""
+ "@\"PBUIPathProvider\""
+ "@32@0:8Q16@24"
+ "@40@0:8@16o^B24@32"
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "Caching"
+ "Oct 11 2023 21:00:45"
+ "PBUCacheManagerAdditions"
+ "PBUIManagedCacheIdentifying"
+ "PBUIMappedImageCacheManager"
+ "PBUIMappedImageCacheManager-Default"
+ "PBUIMappedImageCacheManager.m"
+ "PosterViewController"
+ "Removed bad wallpaper data @ URL %{public}@"
+ "Snapshot attempt failed because preconditions failed: %{public}@"
+ "Snapshotting: %{public}@"
+ "T@\"<BSPathProviding>\",R,C,V_pathProvider"
+ "T@\"BSUIMappedImageCache<PBUIManagedCacheIdentifying>\",R,N,V_cache"
+ "T@\"NSSet\",R,C"
+ "T@\"NSString\",R,N"
+ "TQ,R,V_numberOfManagedCaches"
+ "URLByStandardizingPath"
+ "Unable to create directory %@: %{public}@"
+ "Unable to read resource type from directory URL %{public}@: %{public}@"
+ "Unable to read wallpaper directory URL %{public}@: %{public}@"
+ "Unable to remove bad wallpaper data @ URL %{public}@: %{public}@"
+ "Unable to remove old cache %@: %{public}@"
+ "["
+ "[%@] Poster scene is nil; cannot snapshot"
+ "[%@] Poster scene is not ready for snapshotting (mid-update)."
+ "[%@] Poster scene is not ready for snapshotting (not suspended)."
+ "[%p] failed to read manifest: %{public}@"
+ "[%{public}@/%p] building mapped image cache for key %@"
+ "[%{public}@/%p] bumpManifestForImageCacheKey %@ ; bumping to %{public}@"
+ "[%{public}@/%p] checkoutImageCache faulting in cache for %@"
+ "[%{public}@/%p] checkoutImageCache found cache for %@"
+ "[%{public}@/%p] checkoutImageCache:%@ bumpDate:%@"
+ "[%{public}@/%p] failed teardownCacheForKey key %@; cache is not currently active"
+ "[%{public}@/%p] onDiskCaches; failed to read on disk caches: %{public}@"
+ "[%{public}@/%p] onDiskCaches; failed to read resource type for URL %@: %{public}@"
+ "[%{public}@/%p] removeCacheForKey %@"
+ "[%{public}@/%p] removeCacheForKey %@ aborted; not currently in cacheKeys"
+ "[%{public}@/%p] removeCacheForKey %@ aborted; not currently in manifest"
+ "[%{public}@/%p] removeCacheForKey %@ completed; cache destroyed"
+ "[%{public}@/%p] teardownCacheForKey key %@"
+ "[%{public}@/%p] teardownCacheForKey key %@ aborted; cache still alive somewhere"
+ "[%{public}@/%p] teardownCacheForKey key %@ finished"
+ "[%{public}@/%p] truncateCaches bailing;  number of managed caches is NSNotFound"
+ "[%{public}@/%p] truncateCaches; did cleanup cache %{public}@"
+ "[%{public}@/%p] truncateCaches; failed to cleanup cache key %@: %{public}@"
+ "[%{public}@/%p] truncateCaches; known caches is less than max number of managed caches"
+ "[%{public}@/%p] truncateCaches; truncate on disk caches? %{BOOL}u"
+ "[%{public}@/%p] truncateCaches; truncating on disk cache %{public}@"
+ "[%{public}@/%p] truncateCaches; will attempt to cleanup %lu caches"
+ "[%{public}@/%p] truncateCaches; will not cleanup cache %{public}@ as it is still active"
+ "[%{public}@/%p] truncateCaches; will proceed"
+ "[%{public}@/%p] truncateCaches; will truncate on disk caches"
+ "[%{public}@/%p] truncateCaches; wrinting to manifest"
+ "[%{public}@/%p] truncateOnDiskCaches; failed to cleanup on disk cache key %@: %{public}@"
+ "[%{public}@/%p] writeManifest"
+ "[%{public}@/%p] writeManifest failed to write to url: %{public}@"
+ "[%{public}@/%p] writeManifest failed: %{public}@"
+ "[%{public}@/%p] writeManifest finished"
+ "[cacheURL isFileURL]"
+ "[imageCacheKey length] > 0"
+ "]-[%@]"
+ "_cacheLock"
+ "_cacheLock_buildMappedImageCacheForKey:"
+ "_cacheLock_bumpManifestForImageCacheKey:bumpDate:"
+ "_cacheLock_cacheKeyToCache"
+ "_cacheLock_cacheKeys"
+ "_cacheLock_checkoutImageCache:didCreateNew:bumpDate:"
+ "_cacheLock_manifest"
+ "_cacheLock_onDiskCaches"
+ "_cacheLock_removeCacheForKey:"
+ "_cacheLock_teardownCacheForKey:"
+ "_cacheLock_truncateCaches:"
+ "_cacheLock_writeManifest"
+ "_cacheName"
+ "_cacheURL"
+ "_invalidationFlag"
+ "_manifestURL"
+ "_numberOfManagedCaches"
+ "_pathProvider"
+ "_setupCachesIfNeeded"
+ "activeCaches"
+ "allKeys"
+ "allValues"
+ "appendString:"
+ "cacheKeys has entry that is not in cacheKeyToCache!"
+ "checkoutImageCache:"
+ "checkoutImageCache:date:"
+ "cleanup"
+ "cleanupOldCaches"
+ "compare:"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "countForObject:"
+ "date"
+ "defaultCacheManager"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
+ "evaluateSnapshotPreconditions:"
+ "initWithCapacity:keyOrderingStrategy:"
+ "initWithNumberOfManagedCaches:pathProvider:"
+ "initWithScene:counterpart:"
+ "isFileURL"
+ "knownCaches"
+ "numberOfManagedCaches"
+ "pathProvider"
+ "pbuiMappedImageCacheKey"
+ "pbui_cacheIdentifier"
+ "q24@?0@\"NSDate\"8@\"NSDate\"16"
+ "registerCacheManager:cacheManager:"
+ "removeImageCacheForKey:"
+ "returnImageCache:"
+ "returnImageCacheForKey:"
+ "setPbui_cacheIdentifier:"
+ "setWithSet:"
+ "sortUsingComparator:"
+ "stablePersistenceIdentifier"
+ "stringByAppendingFormat:"
+ "strongToWeakObjectsMapTable"
+ "subarrayWithRange:"
+ "unregisterCacheManagerForURL:"
+ "v32@?0@\"NSString\"8@\"NSDate\"16^B24"
+ "\xf0A"
- "\x0f\x01a"
- "Aug 22 2023 21:07:33"
- "PosterViewController-%p-%@"
- "Snapshot attempt failed because preconditions failed"
- "T@\"BSUIMappedImageCache\",R,N,V_cache"
- "T^{CGImage=},R,N"
- "Transient-%p"
- "Variant-%@"
- "[%@] Poster scene does not need color sampling (no scene)"
- "[%@] Poster scene is not ready for color sampling (mid-update)."
- "[%@] Poster scene is not ready for color sampling (not suspended)."
- "_homeVCCache"
- "_lockVCCache"
- "defaultStoragePath"
- "evaluateSnapshotPreconditions"
- "initWithScene:cache:"
- "initWithScene:storagePath:"
- "makeImageCacheForVariant:"

```
