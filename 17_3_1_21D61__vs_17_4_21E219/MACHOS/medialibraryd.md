## medialibraryd

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd`

```diff

-4023.410.1.0.0
-  __TEXT.__text: 0x127e8
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_stubs: 0x2ca0
-  __TEXT.__objc_methlist: 0xb78
+4023.510.4.0.0
+  __TEXT.__text: 0x13eac
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_stubs: 0x2fa0
+  __TEXT.__objc_methlist: 0xbc0
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x4f8
-  __TEXT.__cstring: 0x138f
+  __TEXT.__gcc_except_tab: 0x504
+  __TEXT.__cstring: 0x1521
   __TEXT.__objc_classname: 0x2b0
-  __TEXT.__objc_methname: 0x392c
+  __TEXT.__objc_methname: 0x3cda
   __TEXT.__objc_methtype: 0xc10
-  __TEXT.__oslogstring: 0x2111
-  __TEXT.__unwind_info: 0x52c
-  __DATA_CONST.__auth_got: 0x3d0
+  __TEXT.__oslogstring: 0x258e
+  __TEXT.__unwind_info: 0x55c
+  __DATA_CONST.__auth_got: 0x400
   __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x960
-  __DATA_CONST.__cfstring: 0x1100
+  __DATA_CONST.__const: 0xa50
+  __DATA_CONST.__cfstring: 0x11c0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x1f0
+  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_arraydata: 0x80
+  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x21d8
-  __DATA.__objc_selrefs: 0xd58
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x1f0
-  __DATA.__objc_superrefs: 0x50
-  __DATA.__objc_ivar: 0x130
+  __DATA.__objc_const: 0x21f8
+  __DATA.__objc_selrefs: 0xe18
+  __DATA.__objc_ivar: 0x134
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x30

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 367
-  Symbols:   222
-  CStrings:  1046
+  Functions: 384
+  Symbols:   228
+  CStrings:  1100
 
Symbols:
+ _CacheDeleteEnumerateRemovedFilesInDirectories
+ _CacheDeleteInitPurgeMarker
+ _CacheDeleteRegisterPurgeNotification
+ _CacheDeleteSyncDone
+ _bzero
+ _statfs
CStrings:
+ "\x03Q"
+ "%{public}@ Checking path %{public}@ for purged artwork"
+ "%{public}@ EnumerateRemovedFilesInDirectories events=%{public}@"
+ "%{public}@ Error clearing artwork.relative_path for artwork relativePath=%{public}@."
+ "%{public}@ Reconciling %lu paths of purged original artwork."
+ "%{public}@ Reconciling all original artwork for library %{public}@."
+ "%{public}@ Registered CacheDelete handlers."
+ "%{public}@ Updated best artwork token for purged artwork with relativePath %{public}@."
+ "%{public}@ _reconcilePurgeNotification - Ignoring unrecognized path %{public}@"
+ "/private"
+ "CacheManagement_Oversize"
+ "Failed to fetch mount stats for path %{public}@"
+ "Ignoring purge request with urgency %u for volume '%{public}@'"
+ "Ignoring purgeable request with urgency %u for volume '%{public}@'"
+ "Received CacheDelete notification: %{public}@"
+ "Received purge request with urgency %u for volume '%{public}@'"
+ "Received purgeable request with urgency %u for volume '%{public}@'"
+ "SELECT entity_pid, entity_type, artwork_token.artwork_type FROM artwork JOIN artwork_token USING(artwork_token) WHERE relative_path = ?"
+ "Skipping artwork reconciliation for %lu paths. No file exists at path '%{public}@'"
+ "Skipping artwork reconciliation. No file exists at path '%{public}@'"
+ "Skipping usage calculation for library at path '%{public}@' because db file is not present or invalid (db version=%d)"
+ "T@\"NSString\",?,R,C"
+ "UPDATE artwork SET relative_path = '' WHERE relative_path = ?"
+ "[Maintenance] Artwork reconciliation complete."
+ "[Maintenance] Maintenance activity triggered."
+ "[Maintenance] Maintenance operation complete. Performing artwork reconciliation."
+ "_artworkOperationQueue"
+ "_isMediaVolume:"
+ "_reconcileAllOriginalArtworkForLibrary:withCompletion:"
+ "_reconcileOrginalArtworkWitRelativePaths:forLibrary:withCompletion:"
+ "_reconcilePurgeNotification"
+ "_updatePurgedOriginalWithRelativePath:forLibrary:usingConnection:"
+ "addOperationWithBlock:"
+ "arrayWithObjects:count:"
+ "cleanupArtworkWithOptions:"
+ "currentDatabaseVersion"
+ "databaseConnectionAllowingWrites:withBlock:"
+ "enumerateArtworkRelativePathsWithConnection:matchingRelativePathContainer:block:"
+ "enumerateRowsWithBlock:"
+ "executeQuery:withParameters:"
+ "executeUpdate:withParameters:error:"
+ "historyDone"
+ "int64ForColumnIndex:"
+ "intForColumnIndex:"
+ "originalArtworkDirectory"
+ "rangeOfString:"
+ "reconcilePurgeableArtworkForLibrary:withCompletion:"
+ "rescan"
+ "rootArtworkCacheDirectory"
+ "set"
+ "stringByAppendingString:"
+ "substringFromIndex:"
+ "updateBestArtworkTokenForEntityPersistentID:entityType:artworkType:retrievalTime:preserveExistingAvailableToken:usingConnection:"
+ "v16@?0@\"ML3DatabaseConnection\"8"
+ "v16@?0^{__CFArray=}8"
+ "v24@?0@\"NSString\"8@\"NSSet\"16"
+ "v24@?0@\"NSString\"8^B16"
+ "v32@?0@\"ML3DatabaseRow\"8@\"NSError\"16^B24"
- "\x02Q"
- "Maintenance activity triggered."
- "Received purge request with urgency %u for volume '%@'"
- "Received purgeable request with urgency %u for volume '%@'"
- "received CacheDelete notification: %{public}@"

```
