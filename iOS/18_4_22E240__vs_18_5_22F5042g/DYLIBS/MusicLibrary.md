## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary`

```diff

-4024.500.35.0.0
-  __TEXT.__text: 0x27ea2c
+4024.600.4.0.0
+  __TEXT.__text: 0x2804b4
   __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_methlist: 0xe004
+  __TEXT.__objc_methlist: 0xe064
   __TEXT.__const: 0x260a0
   __TEXT.__dlopen_cstrs: 0x277
-  __TEXT.__gcc_except_tab: 0x13908
-  __TEXT.__cstring: 0x68930
-  __TEXT.__oslogstring: 0x1ae82
+  __TEXT.__gcc_except_tab: 0x13984
+  __TEXT.__cstring: 0x689b1
+  __TEXT.__oslogstring: 0x1afec
   __TEXT.__ustring: 0x210
-  __TEXT.__unwind_info: 0x7150
+  __TEXT.__unwind_info: 0x7120
   __TEXT.__eh_frame: 0x1cb8
   __TEXT.__objc_classname: 0x1962
-  __TEXT.__objc_methname: 0x1ea67
-  __TEXT.__objc_methtype: 0x541e
-  __TEXT.__objc_stubs: 0x14b00
-  __DATA_CONST.__got: 0xb40
-  __DATA_CONST.__const: 0x9230
+  __TEXT.__objc_methname: 0x1ec93
+  __TEXT.__objc_methtype: 0x541c
+  __TEXT.__objc_stubs: 0x14c40
+  __DATA_CONST.__got: 0xb50
+  __DATA_CONST.__const: 0x92a8
   __DATA_CONST.__objc_classlist: 0x6f0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6bd0
+  __DATA_CONST.__objc_selrefs: 0x6c20
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x520
   __DATA_CONST.__objc_arraydata: 0x10c8
   __AUTH_CONST.__auth_got: 0xff8
   __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__const: 0x123f0
-  __AUTH_CONST.__cfstring: 0x25580
-  __AUTH_CONST.__objc_const: 0x151e0
+  __AUTH_CONST.__cfstring: 0x255a0
+  __AUTH_CONST.__objc_const: 0x15220
   __AUTH_CONST.__objc_arrayobj: 0x20e8
   __AUTH_CONST.__objc_intobj: 0x1ba8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xeac
+  __DATA.__objc_ivar: 0xeb4
   __DATA.__data: 0x1968
   __DATA.__bss: 0xc00
   __DATA.__common: 0xa5c

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8095
-  Symbols:   9917
-  CStrings:  12600
+  Functions: 8114
+  Symbols:   9938
+  CStrings:  12620
 
Symbols:
+ _MDItemContentType
+ _UTTypeContent
CStrings:
+ "%@=\"com.apple.Music\" && %@ != \"*cloudID=*\" && %@ != \"*.content\""
+ "%p dealloc"
+ "%{public}@ - Creating new connection pool=%{public}@ with path: %{public}@"
+ "%{public}@ - _closeAndLockCurrentDatabaseConnections, _connectionPoolsPendingClose.count=%d, connectionPool=%{public}@ "
+ "%{public}@ - not removing connection pool=%{public}@ as it has active connections"
+ "%{public}@ - removing connection pool=%{public}@"
+ "%{public}@ Closing all connections and wait for busy connection=%{BOOL}u, owningPoolClosed=%{BOOL}u"
+ "%{public}@ checking in available connection=%{public}@"
+ "@72@0:8q16q24@32@40@48@56@64"
+ "AvailableConnectionCount"
+ "AvailableConnectionDesc"
+ "BusyConnectionDesc"
+ "DatabaseConnectionPoolDesc"
+ "Failed to create CSSearchable albums from the library."
+ "ML3DatabaseConnectionPool=%p, maxReaders=%d, maxWriters=%d, journalingMode=%d, closed=%d, useDistantWriterConnections=%d, closed=%d"
+ "ML3DatabaseConnectionSubPool=%p closeConnectionsAndWaitForBusyConnections owningPoolClosed=%{BOOL}u, waitForBusyConnections=%{BOOL}u,_availableConnections(count)=%{public}@, _busyConnections=%{public}@"
+ "ML3DatabaseConnectionSubPool=%p, maxConcurrentConnections=%lu, useReadOnlyConnections=%d, useDistantConnections=%d, busyConnections=%p, availableConnections=%p"
+ "MusicAlbumsArtistsSpotlightDonation"
+ "[ML3UpdateSpotlightIndexOperation]  ┃  Creating searchable items for artists"
+ "[ML3UpdateSpotlightIndexOperation]  ┃  Failed to index spotlight albums"
+ "[ML3UpdateSpotlightIndexOperation]  ┃  Failed to index spotlight artists"
+ "[ML3UpdateSpotlightIndexOperation]  ┃  Started to index albums"
+ "[ML3UpdateSpotlightIndexOperation]  ┃  Started to index artists"
+ "[ML3UpdateSpotlightIndexOperation]  ┃  Updated %lu albums in spotlight index with bundle ID:%@"
+ "[ML3UpdateSpotlightIndexOperation]  ┃  Updated %lu artists in spotlight index with bundle ID:%@"
+ "[ML3UpdateSpotlightIndexOperation] No corrupt data found that was previously donated"
+ "[ML3UpdateSpotlightIndexOperation] Operation 2.0 %p started for bundleID %{public}@"
+ "_albumPersistentIDsToUpdate"
+ "_artistPersistentIDsToUpdate"
+ "_closeConnectionsForOwningPoolClosed:andWaitForBusyConnections:"
+ "_createSearchableItemsForAlbumsWithQuery:error:"
+ "_createSearchableItemsForArtistsWithQuery:error:"
+ "_enumerateSearchableItemsWithPersistentIDs:entityType:completionBlock:"
+ "_indexAlbumsWithPersistentIDs:completionBlock:"
+ "_indexArtistsWithPersistentIDs:completionBlock:"
+ "_indexTracksWithPersistentIDs:playlistsWithPersistentIDs:albumsWithPersistentIDs:artistsWithPersistentIDs:completionBlock:"
+ "_playlistPersistentIDsToUpdate"
+ "albumPersistentIDsToUpdate"
+ "artistPersistentIDsToUpdate"
+ "attributeSet"
+ "closeConnectionsForOwningPoolClosed:andWaitForBusyConnections:"
+ "initWithCurrentRevision:targetRevision:trackPersistentIDsToUpdate:playlistPersistentIDsToUpdate:albumPersistentIDsToUpdate:artistPersistentIDsToUpdate:entityStringsToDelete:"
+ "playlistPersistentIDsToUpdate"
+ "v24@0:8B16B20"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
- "%@=\"com.apple.Music\" && %@ != \"*cloudID=*\""
- "%{public}@ - Creating connection pool with path: %{public}@"
- "%{public}@ - _closeAndLockCurrentDatabaseConnections"
- "%{public}@ - connection pool %{public}@ has pending or active connections"
- "%{public}@ Closing all connections and wait for busy connection=%{BOOL}u."
- "%{public}@ closeConnectionsAndWaitForBusyConnections _availableConnections (count) = %d, _busyConnections (count) = %d"
- "@56@0:8q16q24@32@40@48"
- "Attempted to return connection %@ not owned by connection pool %@. (Connections in this pool: %@)"
- "B48@0:8@16q24^@32@?40"
- "DatabaseConnectionPool"
- "ML3DatabaseConnectionPool=%p, maxReaders=%d, maxWriters=%d, journalingMode=%d, useDistantWriterConnections=%d, closed=%d"
- "ML3DatabaseConnectionSubPool=%p, maxConcurrentConnections=%lu, useReadOnlyConnections=%d, useDistantConnections=%d"
- "[ML3UpdateSpotlightIndexOperation]  ┃  Attempted to enumerate searchable items without block, returning"
- "[ML3UpdateSpotlightIndexOperation]  ┃  Created searchable items batch with library fetch batching"
- "[ML3UpdateSpotlightIndexOperation]  ┃  Evaluating the need of batching for database fetch"
- "[ML3UpdateSpotlightIndexOperation]  ┃  Failed to create searchable items batch with library fetch batching"
- "[ML3UpdateSpotlightIndexOperation]  ┃  Library fetch batching is needed, fetching from the DB in chuncks of %lu"
- "[ML3UpdateSpotlightIndexOperation]  ┃  Searchable item creation is done"
- "[ML3UpdateSpotlightIndexOperation] Operation %p started for bundleID %{public}@"
- "_enumerateSearchableItemsWithPersistentIDs:entityType:error:usingBlock:"
- "_indexTracksWithPersistentIDs:playlistsWithPersistentIDs:completionBlock:"
- "_playlistsPersistentIDsToUpdate"
- "availableConnections=%@"
- "busyConnections=%@"
- "initWithCurrentRevision:targetRevision:trackPersistentIDsToUpdate:playlistsPersistentIDsToUpdate:entityStringsToDelete:"
- "playlistsPersistentIDsToUpdate"

```
