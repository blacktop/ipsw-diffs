## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary`

```diff

-4024.500.21.0.0
-  __TEXT.__text: 0x27d8b4
+4024.500.33.0.0
+  __TEXT.__text: 0x27e78c
   __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_methlist: 0xdea4
+  __TEXT.__objc_methlist: 0xe004
   __TEXT.__const: 0x260c0
   __TEXT.__dlopen_cstrs: 0x277
-  __TEXT.__gcc_except_tab: 0x13b08
-  __TEXT.__cstring: 0x686b6
-  __TEXT.__oslogstring: 0x1acfe
+  __TEXT.__gcc_except_tab: 0x13908
+  __TEXT.__cstring: 0x688f4
+  __TEXT.__oslogstring: 0x1ae82
   __TEXT.__ustring: 0x210
-  __TEXT.__unwind_info: 0x70f8
+  __TEXT.__unwind_info: 0x7140
   __TEXT.__eh_frame: 0x1cb0
-  __TEXT.__objc_classname: 0x1926
-  __TEXT.__objc_methname: 0x1e754
-  __TEXT.__objc_methtype: 0x5422
-  __TEXT.__objc_stubs: 0x14880
-  __DATA_CONST.__got: 0xb18
-  __DATA_CONST.__const: 0x91b8
-  __DATA_CONST.__objc_classlist: 0x6e0
+  __TEXT.__objc_classname: 0x1962
+  __TEXT.__objc_methname: 0x1ea67
+  __TEXT.__objc_methtype: 0x541e
+  __TEXT.__objc_stubs: 0x14b00
+  __DATA_CONST.__got: 0xb48
+  __DATA_CONST.__const: 0x9228
+  __DATA_CONST.__objc_classlist: 0x6f0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b28
+  __DATA_CONST.__objc_selrefs: 0x6bd0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x510
-  __DATA_CONST.__objc_arraydata: 0x10a8
+  __DATA_CONST.__objc_superrefs: 0x520
+  __DATA_CONST.__objc_arraydata: 0x10c8
   __AUTH_CONST.__auth_got: 0xff8
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x12428
-  __AUTH_CONST.__cfstring: 0x253e0
-  __AUTH_CONST.__objc_const: 0x14f30
-  __AUTH_CONST.__objc_arrayobj: 0x20d0
-  __AUTH_CONST.__objc_intobj: 0x1bd8
+  __AUTH_CONST.__cfstring: 0x25540
+  __AUTH_CONST.__objc_const: 0x151e0
+  __AUTH_CONST.__objc_arrayobj: 0x20e8
+  __AUTH_CONST.__objc_intobj: 0x1ba8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xe7c
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0xeac
   __DATA.__data: 0x1970
   __DATA.__bss: 0xc00
   __DATA.__common: 0xa54

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8045
-  Symbols:   9861
-  CStrings:  12551
+  Functions: 8093
+  Symbols:   9916
+  CStrings:  12598
 
Symbols:
+ _MDItemAppEntityInstanceId
+ _MDItemBundleID
+ _OBJC_CLASS_$_CSSearchQuery
+ _OBJC_CLASS_$_CSSearchQueryContext
+ _OBJC_CLASS_$_ML3AsyncDatabaseOperation
+ _OBJC_CLASS_$_ML3SpotlightBatchDonationObject
+ _OBJC_METACLASS_$_ML3AsyncDatabaseOperation
+ _OBJC_METACLASS_$_ML3SpotlightBatchDonationObject
- _ML3BundleIDVideos
CStrings:
+ "%@=\"com.apple.Music\" && %@ != \"*cloudID=*\""
+ "%{public}@ Failed to remove cached asset %{public}@ error %{public}@"
+ "@56@0:8q16q24@32@40@48"
+ "CREATE INDEX IF NOT EXISTS ArtworkRelativePath ON artwork (relative_path ASC)"
+ "CREATE INDEX IF NOT EXISTS BestArtworkTokenArtworkVariantType ON best_artwork_token (artwork_variant_type ASC)"
+ "CREATE INDEX IF NOT EXISTS ContainerAuthorPersonPID ON container_author (person_pid ASC)"
+ "ML3AsyncDatabaseOperation"
+ "ML3AsyncDatabaseOperation.m"
+ "ML3SpotlightBatchDonationObject"
+ "PRAGMA user_version = 2240031;"
+ "SELECT 1 FROM item JOIN item_store USING (item_pid) JOIN item_stats USING (item_pid) JOIN album ON (item.album_pid=album.album_pid) WHERE item.in_my_library AND item_store.cloud_status = 8 AND item_stats.liked_state != 2 AND album.liked_state != 2 LIMIT 1"
+ "Subclass %@ must implement -%@ defined in %@."
+ "[ML3AsyncDatabaseOperation class]"
+ "[ML3AsyncDatabaseOperation] Async operation %p failed in %.3f seconds"
+ "[ML3AsyncDatabaseOperation] Async operation %p finished successfully in %.3f seconds"
+ "[ML3UpdateSpotlightIndexOperation] Corrupt data found previously donated, wiping the index and re-indexing everything"
+ "[ML3UpdateSpotlightIndexOperation] Failed to fetch stale items from CSSearchQuery."
+ "[ML3UpdateSpotlightIndexOperation] Finished enumerating PIDs. Starting indexing in batches for %ld batch objects"
+ "[ML3UpdateSpotlightIndexOperation] Making CSSearchQuery to check for stale items with corrupt data."
+ "[Maintenance] %{public}@ Skipping maintenance because database is not validated, currentDatabaseVersion=%d, latestDatabaseVersion=%d "
+ "_batchIndexWithObject:completionBlock:"
+ "_batchIndicesWithObjects:completionBlock:"
+ "_cancelled"
+ "_checkIfPreviouslyDonatedStaleItemsWithCompletionBlock:"
+ "_currentRevision"
+ "_deleteAllAndReindexWithCompletionBlock:"
+ "_deleteAllIndexedItemsWithCompletionBlock:"
+ "_deleteIndexedItemsWithEntityStringIDs:completionBlock:"
+ "_entityStringsToDelete"
+ "_execute"
+ "_executing"
+ "_finished"
+ "_indexItemsFromLibrarySinceRevision:targetRevision:completionBlock:"
+ "_indexPlaylistsWithPersistentIDs:completionBlock:"
+ "_indexTracksWithPersistentIDs:completionBlock:"
+ "_indexTracksWithPersistentIDs:playlistsWithPersistentIDs:completionBlock:"
+ "_playlistsPersistentIDsToUpdate"
+ "_targetRevision"
+ "_trackPersistentIDsToUpdate"
+ "_updateIndexedItemsWithIdentifiers:completionBlock:"
+ "_verifyLibraryAndAttributesProperties:"
+ "contentType"
+ "didChangeValueForKey:"
+ "entityStringsToDelete"
+ "initWithCurrentRevision:targetRevision:trackPersistentIDsToUpdate:playlistsPersistentIDsToUpdate:entityStringsToDelete:"
+ "initWithQueryString:queryContext:"
+ "instanceMethodForSelector:"
+ "isAsynchronous"
+ "isConcurrent"
+ "isFinished"
+ "playlistsPersistentIDsToUpdate"
+ "setFetchAttributes:"
+ "setFoundItemsHandler:"
+ "trackPersistentIDsToUpdate"
+ "v40@0:8q16q24@?32"
+ "willChangeValueForKey:"
- "%{pubic}@ Failed to remove cached asset %{public}@ error %{public}@"
- "B40@0:8q16q24^@32"
- "B64@0:8@16@24@32@40@48^@56"
- "SELECT 1 FROM item JOIN item_store USING (item_pid) JOIN item_stats USING (item_pid) WHERE item.in_my_library AND item_store.cloud_status = 8 AND item_stats.liked_state != 2 LIMIT 1"
- "Videos"
- "[ML3UpdateSpotlightIndexOperation] Index update operation %p failed in %.3f seconds"
- "[ML3UpdateSpotlightIndexOperation] Index update operation %p finished successfully in %.3f seconds"
- "[Maintenance] %{public}@ Skipping maintenance because databaseis not validated, currentDatabaseVersion=%d, latestDatabaseVersion=%d "
- "_batchIndexWithTrackPersistentIDsToUpdate:playlistsPersistentIDsToUpdateSet:entityStringsToDelete:currentRevision:targetRevision:error:"
- "_deleteAllIndexedItemsWithError:"
- "_deleteIndexedItemsWithEntityStringIDs:error:"
- "_indexItemsFromLibrarySinceRevision:targetRevision:error:"
- "_indexTracksWithPersistentIDs:playlistsWithPersistentIDs:error:"
- "_updateIndexedItemsWithIdentifiers:error:"

```
