## itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

-4023.110.8.0.0
-  __TEXT.__text: 0x110d88
+4023.210.3.0.0
+  __TEXT.__text: 0x1148ec
   __TEXT.__auth_stubs: 0x11f0
-  __TEXT.__objc_stubs: 0x13100
-  __TEXT.__objc_methlist: 0x8b08
+  __TEXT.__objc_stubs: 0x13420
+  __TEXT.__objc_methlist: 0x8c78
   __TEXT.__const: 0x1d8
-  __TEXT.__gcc_except_tab: 0x2c38
-  __TEXT.__oslogstring: 0x22a50
-  __TEXT.__objc_classname: 0x2206
-  __TEXT.__objc_methname: 0x1cfd3
-  __TEXT.__objc_methtype: 0x3db2
-  __TEXT.__cstring: 0xdcea
+  __TEXT.__gcc_except_tab: 0x2d78
+  __TEXT.__oslogstring: 0x233d7
+  __TEXT.__objc_classname: 0x224a
+  __TEXT.__objc_methname: 0x1d4e9
+  __TEXT.__objc_methtype: 0x3e92
+  __TEXT.__cstring: 0xe05d
   __TEXT.__dlopen_cstrs: 0x662
-  __TEXT.__unwind_info: 0x3278
+  __TEXT.__unwind_info: 0x32f4
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__auth_got: 0x908
-  __DATA_CONST.__got: 0x968
-  __DATA_CONST.__const: 0x4f80
-  __DATA_CONST.__cfstring: 0xa940
-  __DATA_CONST.__objc_classlist: 0x750
+  __DATA_CONST.__got: 0x990
+  __DATA_CONST.__const: 0x5048
+  __DATA_CONST.__cfstring: 0xaba0
+  __DATA_CONST.__objc_classlist: 0x760
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0xd08
+  __DATA_CONST.__objc_intobj: 0xd50
   __DATA_CONST.__objc_arraydata: 0x268
   __DATA_CONST.__objc_arrayobj: 0x240
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x148d8
-  __DATA.__objc_selrefs: 0x5798
+  __DATA.__objc_const: 0x14cc0
+  __DATA.__objc_selrefs: 0x5868
   __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0xcc0
-  __DATA.__objc_superrefs: 0x510
-  __DATA.__objc_ivar: 0xb68
-  __DATA.__objc_data: 0x4920
+  __DATA.__objc_classrefs: 0xcd0
+  __DATA.__objc_superrefs: 0x518
+  __DATA.__objc_ivar: 0xb90
+  __DATA.__objc_data: 0x49c0
   __DATA.__data: 0xf70
   __DATA.__bss: 0x390
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4263
-  Symbols:   795
-  CStrings:  8114
+  Functions: 4308
+  Symbols:   800
+  CStrings:  8206
 
Symbols:
+ _ICStoreHTTPHeaderKeyXDAAPClientDebugFeatures
+ _ICStoreHTTPHeaderKeyXDAAPClientFeaturesVersion
+ _ICStoreHTTPHeaderKeyXDAAPSupportedFeatures
+ _ML3TrackPropertyAlbumLikedStateChangedDate
+ _MSVAutoBugCaptureDomainMusicLibrary
CStrings:
+ "%{public}@ %{public}@ is not subscribed to Cloud Music Library. Not running content taste operation for artist with storeID %lld "
+ "%{public}@ - Clearing TroveID, CUID, client feature versions and setting merge preference to %{BOOL}u"
+ "%{public}@ - Clearing flag to perform a reset sync."
+ "%{public}@ - Defaults to use DAAP debug feature is set."
+ "%{public}@ - Got update reponse databaseRevision=%u, updateResponseContainsAddToPlaylistBehavior=%{BOOL}u, updateResponseContainsNeedsResetSync=%{BOOL}u, updateResponseContainsClientFeaturesVersion=%{BOOL}u, addToPlaylistBehaviorDAAPValue=%d, updateResponseContainsNeedsResetSync=%d, clientFeaturesVersionDAAPValue=%{public}@"
+ "%{public}@ - Will perform a sync from version=1, onDiskDatabaseRevision=%d, needs full update (client=%{BOOL}u, server=%{BOOL}u)"
+ "%{public}@ - performing initial saga update, sagaDatabaseVersion=%d, sagaNeedsFullUpdate=%{BOOL}u, shouldForceServerToUseDAAPDebugFeature=%{BOOL}u"
+ "%{public}@ Adding content taste item=%{public}@. actionTimestampMillis=%lld"
+ "%{public}@ Cannot run operation as iCloud Music Library is not enabled"
+ "%{public}@ Cannot run operation as user is not subscribed to Cloud Music Library"
+ "%{public}@ Cannot update content taste for album with storeID %lld@, configuration=%{public}@"
+ "%{public}@ Cannot update content taste for artist with storeID %lld, configuration=%{public}@"
+ "%{public}@ Could not get properties for %{public}@, error=%{public}@"
+ "%{public}@ Could not get subscription status for %{public}@, error=%{public}@. Not running request"
+ "%{public}@ Error %{public}@ getting bag for identity %{public}@"
+ "%{public}@ Error getting sync url"
+ "%{public}@ Finished request to edit collaboration"
+ "%{public}@ Finished request to edit collaboration error=%{public}@"
+ "%{public}@ Got request to %{public}@ album with persistentID=%lld, storeID=%lld and the locker bit is set for the account"
+ "%{public}@ Got request to %{public}@ item with storeID=%lld and the locker bit is set for the account"
+ "%{public}@ Got request to %{public}@ playlist with globalID=%{public}@ and the locker bit is set for the account"
+ "%{public}@ Music app is not installed - not running content taste update operation for album with storeID %lld"
+ "%{public}@ Music app is not installed - not running content taste update operation for artist with storeID %lld"
+ "%{public}@ Not running operation"
+ "%{public}@ Sending favorite entity request <%{public}@: %p method=%{public}@ action=%{public}@>"
+ "%{public}@ Skip setting tasteType for content taste item=%{public}@"
+ "%{public}@ Subscription status request completed with response: %{public}@"
+ "%{public}@ Subscription status request completed with response: %{public}@ error=%{public}@"
+ "%{public}@ Unsupported content taste value=%d to send to library APIs"
+ "%{public}@ finished with response=%{public}@, error=%{public}@, responseErrorCode %ld"
+ "%{public}@ loading account properties for %{public}@ failed with error: %{public}@"
+ "<ICDMusicUserSocialProfileProvider: %p> Short-circuiting with cached response: %{private}@."
+ "<ICDMusicUserSocialProfileProvider: %p> Subscription status request completed with response: %{public}@"
+ "<ICDMusicUserSocialProfileProvider: %p> Subscription status request completed with response: %{public}@ error=%{public}@"
+ "<SagaFavoriteEntityOperation=%p, adamID=%lld, globalPlaylistID=%@, albumCloudLibraryID=%@, artistCloudLibraryID=%@, entityType=%@, _persistentID=%lld, timeStamp=%@>"
+ "DeleteFromLibraryResponseParserDelegate"
+ "FavoriteChangeOperation"
+ "ICRemoveFromLibraryResponse"
+ "MLCloudDatabaseClientFeaturesVersion"
+ "Making albums request with pagination token: %{public}@"
+ "Making artist request with pagination token: %{public}@"
+ "Migrating to version 520000"
+ "Migrating to version 520010"
+ "Migrating to version 520020"
+ "OFT-FavoriteEntityForUnsupportedSubscription"
+ "OFT-FavoriteEntityWithCloudLibraryOff"
+ "SELECT cloud_library_id FROM album WHERE album_pid=?"
+ "SELECT cloud_universal_library_id FROM album_artist WHERE album_artist_pid=?"
+ "SELECT reaction FROM container_item_reaction JOIN container_item WHERE uui = ?"
+ "SELECT store_cloud_id FROM CONTAINER WHERE cloud_global_id=?"
+ "SELECT store_saga_id FROM item_store WHERE item_pid=?"
+ "Setting debugFeaturesValue=%d for header DAAP-debug-features"
+ "Setting options for Vision."
+ "SubscriptionStatus"
+ "T@\"NSString\",&,N,V_clientFeaturesVersion"
+ "TB,N,V_hasClientFeaturesVersion"
+ "TB,N,V_hasNeedsResetSync"
+ "TB,N,V_includeCloudLibraryDAAPDebugFeature"
+ "TC,N,V_needsResetSync"
+ "UPDATE container SET date_modified=? WHERE distinguished_kind=?"
+ "UPDATE item SET in_my_library=?, date_added=? WHERE item_pid=?"
+ "UPDATE item_store SET store_saga_id=?, cloud_in_my_library=? WHERE item_pid=?"
+ "Unsupported API call"
+ "_adjustedContentTasteForLibraryEndpoint:"
+ "_canRunOperationWithCompletionHandler:"
+ "_clientFeaturesVersion"
+ "_getStoreAdamIDLikedState:playlistGlobalIDLikedState:artistStoreAdamIDLikedState:"
+ "_hasClientFeaturesVersion"
+ "_hasNeedsResetSync"
+ "_includeCloudLibraryDAAPDebugFeature"
+ "_needsResetSync"
+ "album-liked-status"
+ "album-liked-status-last-updated-date"
+ "clearSagaClientFeaturesVersion"
+ "clearShouldForceServerToUseDAAPDebugFeatures"
+ "clientFeaturesVersion"
+ "dmap.paginationtoken"
+ "el_camino_cover"
+ "hasClientFeaturesVersion"
+ "hasNeedsResetSync"
+ "includeCloudLibraryDAAPDebugFeature"
+ "is-collaborative"
+ "isCollaborativePlaylist"
+ "isROSDevice"
+ "item_stats.liked_state"
+ "item_stats.liked_state_changed_date"
+ "liked-status"
+ "liked-status-last-updated-date"
+ "liked_state"
+ "liked_state_changed_date"
+ "needsResetSync"
+ "objectForFirstRowAndColumn"
+ "performReadOnlyDatabaseTransactionWithBlock:"
+ "sagaClientFeaturesVersion"
+ "sagaNeedsFullUpdate"
+ "setClientFeaturesVersion:"
+ "setContentTaste:forAlbumStoreID:persistentID:timeStamp:configuration:withCompletionHandler:"
+ "setContentTaste:forArtistStoreID:persistentID:timeStamp:configuration:withCompletionHandler:"
+ "setContentTaste:forMediaItem:storeIdentifier:persistentID:timeStamp:configuration:withCompletionHandler:"
+ "setContentTaste:forPlaylistGlobalID:persistentID:timeStamp:configuration:withCompletionHandler:"
+ "setHasClientFeaturesVersion:"
+ "setHasNeedsResetSync:"
+ "setIncludeCloudLibraryDAAPDebugFeature:"
+ "setNeedsResetSync:"
+ "setReactionString:"
+ "setSagaClientFeaturesVersion:"
+ "setSagaNeedsFullUpdate:"
+ "shouldForceServerToUseDAAPDebugFeature"
+ "shouldForceServerToUseDAAPDebugFeatureAlwaysBackoff"
+ "shouldForceServerToUseDAAPDebugFeatureAlwaysPerformResetSync"
+ "v64@0:8q16@\"NSString\"24q32@\"NSDate\"40@\"ICConnectionConfiguration\"48@?<v@?@\"NSError\">56"
+ "v64@0:8q16@24q32@40@48@?56"
+ "v72@0:8q16q24q32q40@\"NSDate\"48@\"ICConnectionConfiguration\"56@?<v@?@\"NSError\">64"
+ "v72@0:8q16q24q32q40@48@56@?64"
+ "{\"version\":\"0.1\"}"
- "%{public}@ - Clearing TroveID and CUID, setting merge preference to %{BOOL}u"
- "%{public}@ - Enqueuing cloud library reset update."
- "%{public}@ - performing initial saga update, sagaDatabaseVersion=%d, sagaNeedsFullUpdateAfterNextUpdate=%{BOOL}u"
- "%{public}@ Could not set cloud_library_id for artist with adamID=%lld, persistentID=%lld as cloudid=%{public}@ is not a string"
- "%{public}@ set cloud_universal_library_id=%{public}@ for album_artist with persistentID=%lld with error=%{public}@"
- "%{public}@] Adding content taste item=%{public}@. actionTimestampMillis=%lld"
- "<ICDMusicUserSocialProfileProvider: %p> Short-circuiting with cached userProfile."
- "Sending favorite entity request <%{public}@: %p method=%{public}@ action=%{public}@> for entityType=%{public}@, item storeID:%lld, globalPlaylistID:%{public}@, albumLibraryID=%{public}@, artistLibraryID=%{public}@ timestamp:%{public}@"
- "UPDATE album_artist SET cloud_universal_library_id=? WHERE album_artist_pid=?"
- "UPDATE item_store SET store_saga_id=? WHERE item_pid=?"
- "[%{public}@] Error %{public}@ getting bag for identity %{public}@"
- "[%{public}@] Error getting sync url"
- "[%{public}@] finished with response=%{public}@, error=%{public}@, responseErrorCode %ld"
- "_bodyDataForAlbumsRequestWithPaginationToken:"
- "_bodyDataForArtistsRequestWithPaginationToken:"
- "_getStoreAdamIDLikedState:playlistGlobalIDLikedState:artistGlobalIDLikedState:"
- "album.liked_state"
- "album.liked_state_changed_date"
- "album_artist.liked_state"
- "album_artist.liked_state_changed_date"
- "sagaNeedsFullUpdateAfterNextUpdate"
- "setSagaNeedsFullUpdateAfterNextUpdate:"
- "supportedFeatures"

```
