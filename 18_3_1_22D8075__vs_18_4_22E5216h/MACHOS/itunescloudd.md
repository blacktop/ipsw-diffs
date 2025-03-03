## itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

-4024.410.1.0.0
-  __TEXT.__text: 0x12d610
-  __TEXT.__auth_stubs: 0x12e0
-  __TEXT.__objc_stubs: 0x14c40
-  __TEXT.__objc_methlist: 0x98e8
+4024.500.33.0.0
+  __TEXT.__text: 0x12cea0
+  __TEXT.__auth_stubs: 0x1250
+  __TEXT.__objc_stubs: 0x14da0
+  __TEXT.__objc_methlist: 0xa8f4
+  __TEXT.__dlopen_cstrs: 0x6b8
   __TEXT.__const: 0x330
-  __TEXT.__gcc_except_tab: 0x4ec8
-  __TEXT.__oslogstring: 0x27089
+  __TEXT.__gcc_except_tab: 0x4ed4
+  __TEXT.__oslogstring: 0x26e19
   __TEXT.__objc_classname: 0x252e
-  __TEXT.__objc_methname: 0x1fc02
-  __TEXT.__objc_methtype: 0x41ba
-  __TEXT.__cstring: 0xf5cc
-  __TEXT.__dlopen_cstrs: 0x6b8
-  __TEXT.__unwind_info: 0x3698
+  __TEXT.__objc_methname: 0x20018
+  __TEXT.__objc_methtype: 0x421e
+  __TEXT.__cstring: 0xf5de
+  __TEXT.__unwind_info: 0x3628
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x980
-  __DATA_CONST.__got: 0x1060
+  __DATA_CONST.__auth_got: 0x938
+  __DATA_CONST.__got: 0x1008
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x58e8
-  __DATA_CONST.__cfstring: 0xb8e0
+  __DATA_CONST.__const: 0x5930
+  __DATA_CONST.__cfstring: 0xb960
   __DATA_CONST.__objc_classlist: 0x7e0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x590
+  __DATA_CONST.__objc_superrefs: 0x598
   __DATA_CONST.__objc_intobj: 0xe40
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__objc_arrayobj: 0x240
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x16a78
-  __DATA.__objc_selrefs: 0x5fa8
+  __DATA.__objc_const: 0x14dd0
+  __DATA.__objc_selrefs: 0x6238
   __DATA.__objc_ivar: 0xd2c
   __DATA.__objc_data: 0x4ec0
   __DATA.__data: 0x1150

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4664
-  Symbols:   851
-  CStrings:  8938
+  Functions: 4624
+  Symbols:   830
+  CStrings:  8948
 
Symbols:
+ _ICArtworkInfoKeyArtworkDictionaryFullURL3x4
+ _ML3ContainerPropertyEditSessionID
+ _OBJC_CLASS_$_ICBackgroundTaskScheduler
- _XPC_ACTIVITY_ALLOW_BATTERY
- _XPC_ACTIVITY_CHECK_IN
- _XPC_ACTIVITY_DELAY
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_INTERVAL
- _XPC_ACTIVITY_INTERVAL_15_MIN
- _XPC_ACTIVITY_INTERVAL_1_DAY
- _XPC_ACTIVITY_INTERVAL_1_HOUR
- _XPC_ACTIVITY_INTERVAL_1_MIN
- _XPC_ACTIVITY_INTERVAL_30_MIN
- _XPC_ACTIVITY_INTERVAL_7_DAYS
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _XPC_ACTIVITY_REPEATING
- _XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP
- __os_feature_enabled_impl
- _xpc_activity_copy_criteria
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_activity_set_criteria
- _xpc_activity_set_state
- _xpc_activity_unregister
- _xpc_dictionary_get_double
- _xpc_dictionary_set_string
CStrings:
+ "\x02\x11\x112"
+ "!\""
+ "%{public}@ - Disabling cloud library and removing tracks"
+ "%{public}@ - Removing sources from all tracks: %{public}@"
+ "%{public}@ - ignoring importContainerArtworkForSagaID for sagaID %lld as we don't have a valid SagaRequestHandler"
+ "%{public}@ Adding 3x4 variant entry for artwork token '%{public}@"
+ "%{public}@ Artwork info does not contain any variants - skipping adding to db"
+ "%{public}@ Failed to load properties for identity %{public}@ error=%{public}@"
+ "%{public}@ Failed to load the bag - will use default frequency"
+ "%{public}@ Failed to remove playback intents error=%{public}@"
+ "%{public}@ Importing tracks up to revision %u. onDiskRevision=%u"
+ "%{public}@ No existing entries for token '%{public}@' - not adding variants"
+ "%{public}@ No pending events - canceling any previously scheduled task"
+ "%{public}@ Not performing sync because privacy acknowledgement needed for a media application to proceed"
+ "%{public}@ Not scheduling a flush because one is already scheduled"
+ "%{public}@ Retrieved flush frequency from bag value: %f"
+ "%{public}@ skip lookup of adamID=%{public}@, likedStateInfo=%{public}@"
+ "%{public}@ skip lookup of album artist adamID=%{public}@, likedStateInfo=%{public}@"
+ "%{public}@ skip lookup of global playlist=%{public}@, likedStateInfo=%{public}@"
+ "%{public}@ starting operation to flush play activity events"
+ "@\"NSDictionary\"32@0:8@\"AMSPushPayload\"16@\"NSString\"24"
+ "@80@0:8@16@24Q32@40q48q56q64@72"
+ "Album Artist Import [Count:(%lu) - Ids:(%@)]"
+ "ICDBackgroundTaskManager %p - startPeriodicPolling - Setting timer to perform periodic poll for %llds"
+ "No cloud_artwork_token for playlist saga id = %llu, variantType = %ld"
+ "Privacy acknowledgement required"
+ "SELECT entity_pid, entity_type, artwork_variant_type from artwork_token WHERE artwork_token = ? AND artwork_source_type = ? AND artwork_type = ?"
+ "T@\"NSDictionary\",C,N,V_assetInfoDictionary"
+ "Tq,N,V_artworkVariantType"
+ "Tq,R,N,V_variantType"
+ "[Updating HTTP Cookies] Current cookie values: itre=%{public}@, itrv=%{public}@, itst=%{public}@"
+ "_artworkVariantType"
+ "_assetInfoDictionary"
+ "_clearDatabaseWithCompletion:"
+ "_disableCloudLibraryAndRemoveTracksWithCompletion:"
+ "_disableCloudLibraryWithCompletion:"
+ "_performRemoveCloudSourcesWithCompletion:"
+ "_populateAvailableVariantsIfNeeded"
+ "_scheduleNextPlayActivityFlushOperationReplacingExisting:"
+ "_variantType"
+ "artworkRelativePathFromToken:variantType:"
+ "artworkVariantType"
+ "assetInfoDictionary"
+ "authenticationProvider"
+ "cancelTask:"
+ "com.apple.itunescloud.ICMusicLibraryRecommendationController.refresh"
+ "com.apple.itunescloud.ICPlayActivityServer.flush_task"
+ "hasScheduledTask:"
+ "importArtworkForCloudID:artworkType:token:mediaType:variantType:allowsCellularData:clientIdentity:completionHandler:"
+ "importArtworkTokenForEntityPersistentID:entityType:artworkToken:artworkType:sourceType:variantType:usingConnection:"
+ "importContainerArtworkForSagaID requires icml to be enabled"
+ "importContainerArtworkForSagaID:artworkVariantType:clientIdentity:completionHandler:"
+ "importContainerArtworkForSagaID:artworkVariantType:configuration:completion:"
+ "importContainerArtworkForSagaID:variantType:clientIdentity:completionHandler:"
+ "importExistingOriginalArtworkWithArtworkToken:artworkType:sourceType:mediaType:variantType:"
+ "importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:"
+ "importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:"
+ "initWithEntity:artworkType:artworkVariantType:"
+ "initWithURLSession:configuration:cloudID:artworkToken:artworkType:sourceType:variantType:clientIdentity:"
+ "processing cloud add/favorite operation with response=%{public}@"
+ "pushPayload:metricsOverlayForType:"
+ "registerForTask:handler:"
+ "sagaPushNotificationTimes"
+ "scheduleRecurringTask:withInterval:afterDelay:withUserData:"
+ "scheduleTask:afterDelay:withUserData:"
+ "setArtworkVariantType:"
+ "setAssetInfoDictionary:"
+ "setSagaPushNotificationTimes:"
+ "sharedTaskScheduler"
+ "updateBestArtworkTokenForEntityPersistentID:entityType:artworkType:variantType:retrievalTime:preserveExistingAvailableToken:usingConnection:"
+ "v24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "v48@0:8Q16q24@\"ICConnectionConfiguration\"32@?<v@?@\"NSError\">40"
+ "v72@0:8Q16q24@32I40q44B52@56@?64"
+ "variantType"
- "\x02\x11\x11!"
- "\x132"
- "%{public}@  criteria to fire next content taste operation is unchanged"
- "%{public}@  setting criteria to fire next content taste operation"
- "%{public}@  updating criteria to fire next content taste operation at %{public}@"
- "%{public}@ - Finished running maintenance task with error=%{public}@"
- "%{public}@ - ignoring setCloudFavoriteSongAddToLibraryBehavior as %{public}@ feature is not enabled"
- "%{public}@ Cannot import artwork on the watch while its not plugged in"
- "%{public}@ Creating new criteria to fire on %{public}@ with grace period till %{public}@"
- "%{public}@ Did not find postFrequency from bag using default value (%f)"
- "%{public}@ Found existing activity to flush play activity events on %{public}@"
- "%{public}@ Found postFrequency %f from bag"
- "%{public}@ Have pending play activity events to flush"
- "%{public}@ Importing tracks up to revision %u. onDiskRevision=%u, supportsPagination=%{BOOL}u"
- "%{public}@ Loading default nextFlushPlayActivityFireSyncInterval to %f"
- "%{public}@ Loading next play activity flush event to fire on %{public}@"
- "%{public}@ No active user identity - using default value (%f) to update the criteria to flush play activity events"
- "%{public}@ Not creating a new criteria for flush play activity events nextFlushPlayActivityFireSyncInterval (%f), testNextFlushPlayActivityFireSyncInterval (%f)"
- "%{public}@ Setting criteria to fire the next play activity event on %{public}@"
- "%{public}@ Unknown state"
- "%{public}@ starting operation for flush play activity events pendingOperationCount %lld, nextFlushPlayActivityFireSyncInterval %f, _testNextFlushPlayActivityFireSyncInterval %f "
- "%{public}@ starting xpc activity to flush play activity events"
- "%{public}@ updating current criteria to flush the next play activity event from %{public}@ to %{public}@"
- "@24@0:8d16"
- "@32@0:8q16q24"
- "@40@0:8@16q24q32"
- "@72@0:8@16@24Q32@40q48q56@64"
- "AddToLibraryWhenFavoriting"
- "B24@0:8d16"
- "CloudPlayActivityListenerNextFlushPlayActivityFireDateKey"
- "FavoritesPlaylist"
- "Favoriting"
- "ICDBackgroundTaskManager %p - periodicPolling - Ignoring activity [State != Run]"
- "ICDBackgroundTaskManager %p - scheduleTask - Unable to force task termination [%{public}@]"
- "ICDBackgroundTaskManager %p - scheduleTask - Unable to perform asynchrounous work [%{public}@]"
- "ICDBackgroundTaskManager %p - startPeriodicPolling - Setting timer to perform periodic poll for %llds (+/- %llds)"
- "Invalid CloudLibraryStateReasonType (%d)"
- "JaliscoPagination"
- "MediaContentTasteResponseExpirationTimeKey"
- "NanoMusicSync"
- "No cloud_artwork_token for playlist saga id = %llu"
- "Not performing artwork info operation because power is required"
- "OffPuckDownloads"
- "_cellularDataAllowed"
- "_criteriaDictionaryWithPostFrequency:"
- "_deferredPushActivityCriteriaForTask:startTime:gracePeriod:"
- "_flushOperationCount"
- "_isValidTimeInterval:"
- "_nextFlushPlayActivityFireSyncInterval"
- "_periodicPollingActivityCriteriaWithRefreshInterval:gracePeriod:"
- "_pollingGracePeriodSecondsForRefreshInterval:"
- "_scheduleNextPlayActivityFlushOperationWithCriteria:"
- "_testNextFlushPlayActivityFireSyncInterval"
- "_timeIntervalForNextFlushOperationWithReplyBlock:"
- "activityCriteriaForTask:startTimeInSeconds:"
- "com.apple.itunescloud.library_recommendations_refresh"
- "com.apple.itunescloudd.flushPlayactivityEventsBackgroundTask"
- "importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:shouldPerformColorAnalysis:completion:"
- "importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:shouldPerformColorAnalysis:completion:"
- "initWithURLSession:configuration:cloudID:artworkToken:artworkType:sourceType:clientIdentity:"
- "performMaintenanceTasksForDatabaseAtPath:withCompletionHandler:"
- "task.configuration.userIdentity.accountDSID != nil"
- "v16@?0d8"
- "watchNotCharging"

```
