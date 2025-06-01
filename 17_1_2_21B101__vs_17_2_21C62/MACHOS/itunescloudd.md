## itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

-4023.210.3.0.0
-  __TEXT.__text: 0x1148ec
-  __TEXT.__auth_stubs: 0x11f0
-  __TEXT.__objc_stubs: 0x13420
-  __TEXT.__objc_methlist: 0x8c78
-  __TEXT.__const: 0x1d8
-  __TEXT.__gcc_except_tab: 0x2d78
-  __TEXT.__oslogstring: 0x233d7
-  __TEXT.__objc_classname: 0x224a
-  __TEXT.__objc_methname: 0x1d4e9
-  __TEXT.__objc_methtype: 0x3e92
-  __TEXT.__cstring: 0xe05d
+4023.310.5.0.0
+  __TEXT.__text: 0x116898
+  __TEXT.__auth_stubs: 0x1200
+  __TEXT.__objc_stubs: 0x13680
+  __TEXT.__objc_methlist: 0x8dd0
+  __TEXT.__const: 0x1e8
+  __TEXT.__gcc_except_tab: 0x2e28
+  __TEXT.__oslogstring: 0x23835
+  __TEXT.__objc_classname: 0x22a9
+  __TEXT.__objc_methname: 0x1d905
+  __TEXT.__objc_methtype: 0x3e38
+  __TEXT.__cstring: 0xe30d
   __TEXT.__dlopen_cstrs: 0x662
-  __TEXT.__unwind_info: 0x32f4
+  __TEXT.__unwind_info: 0x3344
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x908
-  __DATA_CONST.__got: 0x990
-  __DATA_CONST.__const: 0x5048
-  __DATA_CONST.__cfstring: 0xaba0
-  __DATA_CONST.__objc_classlist: 0x760
+  __DATA_CONST.__auth_got: 0x910
+  __DATA_CONST.__got: 0x998
+  __DATA_CONST.__const: 0x5098
+  __DATA_CONST.__cfstring: 0xad80
+  __DATA_CONST.__objc_classlist: 0x770
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x268
   __DATA_CONST.__objc_arrayobj: 0x240
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x14cc0
-  __DATA.__objc_selrefs: 0x5868
+  __DATA.__objc_const: 0x14f58
+  __DATA.__objc_selrefs: 0x5908
   __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0xcd0
-  __DATA.__objc_superrefs: 0x518
-  __DATA.__objc_ivar: 0xb90
-  __DATA.__objc_data: 0x49c0
+  __DATA.__objc_classrefs: 0xce8
+  __DATA.__objc_superrefs: 0x528
+  __DATA.__objc_ivar: 0xbb0
+  __DATA.__objc_data: 0x4a60
   __DATA.__data: 0xf70
   __DATA.__bss: 0x390
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
+  - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9E740CCD-1622-393D-A279-EF98B1552904
-  Functions: 4308
-  Symbols:   800
-  CStrings:  9579
+  UUID: 3838C088-7BAF-3300-B36F-B4FBF631A75D
+  Functions: 4338
+  Symbols:   803
+  CStrings:  9657
 
Symbols:
+ _ICCloudClientCloudFavoriteSongAddToLibraryBehaviorDidChangeNotification
+ _ICCloudClientGetStringForAddToLibraryBehavior
+ _ML3ContainerPropertyCollaboratorStatus
+ _OBJC_CLASS_$_NLTokenizer
- _ML3AlbumArtistPropertyPersistentID
CStrings:
+ "%{public}@  No pending changes to process."
+ "%{public}@ %lu pending changes failed again, persisting for another time."
+ "%{public}@ - Got update reponse databaseRevision=%u, addToPlaylistBehavior=%{BOOL}u, favoriteSongAddToLibraryBehavior=%{BOOL}u, needsResetSync=%{BOOL}u, clientFeaturesVersion=%{BOOL}u, addToPlaylistBehaviorDAAPValue=%d, addToLibraryWhenFavoritingBehaviorDAAPValue=%d, needsResetSyncDAAPValue=%d, clientFeaturesVersionDAAPValue=%{public}@"
+ "%{public}@ - Server response indicates the limit on active collaborators has been reached"
+ "%{public}@ - Server response indicates the limit on pending collaborators has been reached"
+ "%{public}@ - Setting album properties %{public}@ with album persistent ID: %lld"
+ "%{public}@ - Setting cloud add to library behavior to: %{public}@"
+ "%{public}@ - Update response contained add to library behavior: %{public}@"
+ "%{public}@ - ignoring setCloudFavoriteSongAddToLibraryBehavior as %{public}@ feature is not enabled"
+ "%{public}@ - ignoring setCloudFavoriteSongAddToLibraryBehavior as %{public}@ is not a valid behavior"
+ "%{public}@ - ignoring setCloudFavoriteSongAddToLibraryBehavior as we don't have a valid SagaRequestHandler"
+ "%{public}@ - processPendingChangesUsingLibrary - path=%@ - libraryIdentifier=%@"
+ "%{public}@ Couldn't validate the reaction \"%{public}@\" with params: %{public}@"
+ "%{public}@ Enqueueing pending change operation %{public}@"
+ "%{public}@ Processing %lu pending changes: %{public}@"
+ "%{public}@ SagaCloudSDKAddOperation ID cannot be nil!"
+ "Active collaborator limit exceeded"
+ "AddToLibraryWhenFavoriting"
+ "AddToLibraryWhenFavoriting is enabled, but addToLibraryBehavior=%d, setting to %d"
+ "Album Artist with persistentID=%lld does not have a cloud library id. Not setting properties=%{public}@"
+ "Album Artist with pid = %lld, cloudLibraryID = %{public}@ does not exist locally"
+ "Album with pid = %lld, cloudLibraryID = %{public}@ does not exist locally"
+ "CloudService %p - setCloudFavoriteSongAddToLibraryBehavior (%d) - Unable to service request - error=%{public}@"
+ "CloudSetFavoriteSongAddToLibraryBehaviorOperation"
+ "CloudSetFavoriteSongAddToLibraryBehaviorOperation - (add to library behavior = %@)"
+ "CloudSetFavoriteSongAddToLibraryBehaviorOperationIDKey"
+ "FavoritesPlaylist"
+ "ICSetFavoriteSongAddToLibraryBehaviorRequest"
+ "ID cannot be nil"
+ "MLCloudAccountFavoriteSongAddToLibraryBehavior"
+ "Migrating to version 530000"
+ "Migrating to version 530010"
+ "Migrating to version 530020"
+ "Missing cloud IDs"
+ "Pending collaborator limit exceeded"
+ "Response: (HTTP %lu) - Bad Request/No Found"
+ "Response: (HTTP 403, DMAP %lu) - Collaboration limit exceeded."
+ "SELECT 1 FROM container WHERE is_collaborative = 1"
+ "SagaCloudSDKAddOperation passed nil ID"
+ "SagaCollaborationEndOperationCollaborationCloudLibraryIDKey"
+ "SagaCollaborationEndOperationCollaborationGlobalPlaylistIDKey"
+ "Sending request %p to set add to library behavior to %{public}@"
+ "TB,N,V_hasAddToLibraryWhenFavoritingBehavior"
+ "TC,N,V_addToLibraryWhenFavoritingBehavior"
+ "Tq,N,Sicd_setSagaCloudFavoriteSongAddToLibraryBehavior:"
+ "_addToLibraryBehavior"
+ "_addToLibraryWhenFavoritingBehavior"
+ "_albumArtistCloudLibraryID"
+ "_bodyDataForDatabaseRevision:addToLibraryBehavior:"
+ "_cloudLibraryID"
+ "_hasAddToLibraryWhenFavoritingBehavior"
+ "addToLibraryWhenFavoritingBehavior"
+ "clearSagaCloudFavoriteSongAddToLibraryBehavior"
+ "cloud_library_id"
+ "cloud_universal_library_id"
+ "com.apple.itunescloudd.CloudPendingChangesCoordinator.operationQueue"
+ "com.apple.itunescloudd.SagaRequestHandler.setAddToLibraryBehaviorOperation"
+ "enumerateTokensInRange:usingBlock:"
+ "executeQuery:"
+ "hasAddToLibraryWhenFavoritingBehavior"
+ "hasAtLeastOneRow"
+ "icd_sagaCloudFavoriteSongAddToLibraryBehavior"
+ "icd_setSagaCloudFavoriteSongAddToLibraryBehavior:"
+ "initWithConfiguration:clientIdentity:addToLibraryBehavior:"
+ "initWithConfiguration:clientIdentity:albumPersistentID:properties:"
+ "initWithDatabaseID:databaseRevision:addToLibraryBehavior:"
+ "initWithUnit:"
+ "isReactionValid:"
+ "itemPositionUUID"
+ "requestWithDatabaseID:databaseRevision:addToLibraryBehavior:"
+ "setAddToLibraryWhenFavoritingBehavior:"
+ "setAlbumArtistProperties:withArtistPersistentID:clientIdentity:completionHandler:"
+ "setAlbumEntityProperties:forAlbumPersistentID:configuration:completion:"
+ "setAlbumEntityProperties:withAlbumPersistentID:clientIdentity:completionHandler:"
+ "setCloudFavoriteSongAddToLibraryBehavior:clientIdentity:completionHandler:"
+ "setCloudFavoriteSongAddToLibraryBehavior:forConfiguration:completion:"
+ "setHasAddToLibraryWhenFavoritingBehavior:"
+ "setSagaCloudFavoriteSongAddToLibraryBehavior:"
+ "setString:"
+ "v40@?0{_NSRange=QQ}8Q24^B32"
- "%lu pending changes failed again, persisting for another time."
- "%{public}@ - Got update reponse databaseRevision=%u, updateResponseContainsAddToPlaylistBehavior=%{BOOL}u, updateResponseContainsNeedsResetSync=%{BOOL}u, updateResponseContainsClientFeaturesVersion=%{BOOL}u, addToPlaylistBehaviorDAAPValue=%d, updateResponseContainsNeedsResetSync=%d, clientFeaturesVersionDAAPValue=%{public}@"
- "%{public}@ - Setting album properties %{public}@ with album persistent ID: %lld, cloudLibraryID: %{public}@"
- "%{public}@ Finished request to join collaboration. sagaID=%u error=%{public}@"
- "Album Artist with pid = %lld does not have a cloud library id, skipping updates to cloud library."
- "Album Artist with pid = %lld is not in the database, skipping updates to cloud library."
- "CloudPendingChangesCoordinator %p - processPendingChangesUsingLibrary - path=%@ - libraryIdentifier=%@"
- "CloudService %p - setAlbumProperties: (albumID=%llu, cloudLibraryID=%{public}@, properties=%{public}@) - Unable to service request - error=%{public}@"
- "No pending changes to process."
- "Processing %lu pending changes..."
- "SELECT reaction FROM container_item_reaction JOIN container_item WHERE uui = ?"
- "el_camino_cover"
- "initWithConfiguration:clientIdentity:albumPersistentID:cloudLibraryID:properties:"
- "setAlbumArtistProperties:forItemsWithAlbumArtistPersistentID:clientIdentity:completionHandler:"
- "setAlbumProperties:forAlbumPersistentID:cloudLibraryID:configuration:completion:"
- "setAlbumProperties:withAlbumPersistentID:cloudLibraryID:clientIdentity:completionHandler:"
- "setReactionString:"
- "v56@0:8@\"NSDictionary\"16q24@\"NSString\"32@\"ICConnectionConfiguration\"40@?<v@?@\"NSError\">48"

```
