## PaperBoardUI

> `/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI`

```diff

-140.26.102.0.0
-  __TEXT.__text: 0x7dbc4
+140.39.0.0.0
+  __TEXT.__text: 0x7e018
   __TEXT.__auth_stubs: 0x15d0
-  __TEXT.__objc_methlist: 0x8c88
+  __TEXT.__objc_methlist: 0x8cd8
   __TEXT.__const: 0x820
-  __TEXT.__cstring: 0x6795
-  __TEXT.__oslogstring: 0x4111
+  __TEXT.__cstring: 0x677c
+  __TEXT.__oslogstring: 0x4187
   __TEXT.__gcc_except_tab: 0xa08
   __TEXT.__dlopen_cstrs: 0x252
-  __TEXT.__unwind_info: 0x26b4
-  __TEXT.__objc_classname: 0x17b2
-  __TEXT.__objc_methname: 0x166c5
-  __TEXT.__objc_methtype: 0x42d9
-  __TEXT.__objc_stubs: 0x11980
+  __TEXT.__unwind_info: 0x26c8
+  __TEXT.__objc_classname: 0x17ca
+  __TEXT.__objc_methname: 0x16727
+  __TEXT.__objc_methtype: 0x42f6
+  __TEXT.__objc_stubs: 0x119e0
   __DATA_CONST.__got: 0x358
   __DATA_CONST.__const: 0x24c8
-  __DATA_CONST.__objc_classlist: 0x408
+  __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1cea0
-  __DATA_CONST.__objc_selrefs: 0x5020
+  __DATA_CONST.__objc_const: 0x1cf30
+  __DATA_CONST.__objc_selrefs: 0x5038
   __DATA_CONST.__objc_arraydata: 0x1f8
-  __AUTH_CONST.__objc_const: 0x3310
+  __AUTH_CONST.__objc_const: 0x3358
   __AUTH_CONST.__cfstring: 0x6e20
   __AUTH_CONST.__const: 0xc58
   __AUTH_CONST.__objc_intobj: 0x150

   __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0xaf8
-  __AUTH.__objc_data: 0x2300
+  __AUTH.__objc_data: 0x2350
   __AUTH.__data: 0x8
   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x7a8
-  __DATA.__objc_superrefs: 0x360
-  __DATA.__objc_ivar: 0xa04
+  __DATA.__objc_superrefs: 0x368
+  __DATA.__objc_ivar: 0xa0c
   __DATA.__data: 0x1e78
   __DATA.__bss: 0x150
   __DATA_DIRTY.__objc_data: 0x550

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3781
-  Symbols:   13531
-  CStrings:  5679
+  Functions: 3787
+  Symbols:   13552
+  CStrings:  5685
 
Symbols:
+ -[BSUIMappedImageCache(PBUCacheManagerAdditions) pbui_setCacheManager:cacheIdentifier:]
+ -[PBUICachedSnapshotEffectProvider cacheIdentifier]
+ -[PBUICachedSnapshotEffectProvider setCacheIdentifier:]
+ -[PBUIMappedImageCacheManager _cacheLock_activeCaches]
+ -[PBUIMappedImageCacheManager _cacheLock_deleteCacheDirectoryForKey:error:]
+ -[PBUIPosterHomeViewController configureForZOrder]
+ -[PBUIPosterHomeViewController setActiveStyle:]
+ -[_BSUIMappedImageCacheCanary .cxx_destruct]
+ -[_BSUIMappedImageCacheCanary dealloc]
+ -[_BSUIMappedImageCacheCanary initWithCacheManager:key:]
+ OBJC_IVAR_$_PBUIPosterVariantViewController._snapshotView
+ _OBJC_CLASS_$__BSUIMappedImageCacheCanary
+ _OBJC_IVAR_$_PBUICachedSnapshotEffectProvider._cacheIdentifier
+ _OBJC_IVAR_$_PBUIMappedImageCacheManager._cacheLock_cacheKeyToWeakCache
+ _OBJC_IVAR_$__BSUIMappedImageCacheCanary._cacheManager
+ _OBJC_IVAR_$__BSUIMappedImageCacheCanary._key
+ _OBJC_METACLASS_$__BSUIMappedImageCacheCanary
+ _PBUIWallpaperSharedDirectoryDataStoreSharedDirectoryURL
+ __OBJC_$_INSTANCE_METHODS__BSUIMappedImageCacheCanary
+ __OBJC_$_INSTANCE_VARIABLES__BSUIMappedImageCacheCanary
+ __OBJC_CLASS_RO_$__BSUIMappedImageCacheCanary
+ __OBJC_METACLASS_RO_$__BSUIMappedImageCacheCanary
+ ___38-[_BSUIMappedImageCacheCanary dealloc]_block_invoke
+ ___76-[PBUICachedSnapshotEffectProvider initForSnapshotProvider:cacheIdentifier:]_block_invoke
+ ___block_literal_global.53
+ _objc_msgSend$_cacheLock_activeCaches
+ _objc_msgSend$_cacheLock_deleteCacheDirectoryForKey:error:
+ _objc_msgSend$configureForZOrder
+ _objc_msgSend$initForSnapshotProvider:cacheIdentifier:
+ _objc_msgSend$initWithCacheManager:key:
+ _objc_msgSend$insertSubview:aboveSubview:
+ _objc_msgSend$keyEnumerator
+ _objc_msgSend$nextObject
+ _objc_msgSend$pbui_setCacheManager:cacheIdentifier:
- -[BSUIMappedImageCache(PBUCacheManagerAdditions) setPbui_cacheIdentifier:]
- -[PBUICachedSnapshotEffectProvider initForSnapshotProvider:cache:]
- -[PBUIMappedImageCacheManager _cacheLock_checkoutImageCache:didCreateNew:bumpDate:].cold.1
- -[PBUIMappedImageCacheManager _cacheLock_teardownCacheForKey:].cold.1
- _OBJC_CLASS_$_NSCountedSet
- _OBJC_IVAR_$_PBUIMappedImageCacheManager._cacheLock_cacheKeyToCache
- _OBJC_IVAR_$_PBUIMappedImageCacheManager._cacheLock_cacheKeys
- _OBJC_IVAR_$_PBUIPosterVariantViewController._snapshotView
- ___66-[PBUICachedSnapshotEffectProvider initForSnapshotProvider:cache:]_block_invoke
- ___block_literal_global.56
- _objc_msgSend$countForObject:
- _objc_msgSend$initForSnapshotProvider:cache:
- _objc_msgSend$initWithUniqueIdentifier:
- _objc_msgSend$returnImageCache:
- _objc_msgSend$setPbui_cacheIdentifier:
- _objc_msgSend$setWithSet:
CStrings:
+ "\x04\x14\x12\x13\x111"
+ "@\"NSMapTable\""
+ "@\"PBUIMappedImageCacheManager\""
+ "Nov 14 2023 21:00:53"
+ "[%{public}@/%p] removeCacheForKey %@ aborted; cache is live"
+ "[%{public}@/%p] removeCacheForKey; failed to cleanup cache key %@: %{public}@"
+ "[%{public}@/%p] teardownCacheForKey key %@ ignored - already cleaned up"
+ "[%{public}@/%p] truncateCaches; will cleanup cache %{public}@"
+ "_BSUIMappedImageCacheCanary"
+ "_cacheLock_activeCaches"
+ "_cacheLock_cacheKeyToWeakCache"
+ "_cacheLock_deleteCacheDirectoryForKey:error:"
+ "_cacheManager"
+ "_key"
+ "configureForZOrder"
+ "initWithCacheManager:key:"
+ "insertSubview:aboveSubview:"
+ "keyEnumerator"
+ "nextObject"
+ "pbuiMappedImageCacheCanary"
+ "pbui_setCacheManager:cacheIdentifier:"
- "\x04\x13\x12\x13\x121"
- "\a"
- "\x18"
- "@\"NSCountedSet\""
- "Oct 11 2023 21:00:45"
- "[%{public}@/%p] failed teardownCacheForKey key %@; cache is not currently active"
- "[%{public}@/%p] removeCacheForKey %@ aborted; not currently in cacheKeys"
- "_cacheLock_cacheKeyToCache"
- "_cacheLock_cacheKeys"
- "cacheKeys has entry that is not in cacheKeyToCache!"
- "countForObject:"
- "initForSnapshotProvider:cache:"
- "initWithUniqueIdentifier:"
- "setPbui_cacheIdentifier:"
- "setWithSet:"

```
