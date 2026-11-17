## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

```diff

-678.2.1.0.3
-  __TEXT.__text: 0x47ecec
-  __TEXT.__objc_methlist: 0x3902c
+678.2.6.0.2
+  __TEXT.__text: 0x481b3c
+  __TEXT.__objc_methlist: 0x3914c
   __TEXT.__const: 0x44fa
-  __TEXT.__cstring: 0x5ad12
-  __TEXT.__oslogstring: 0x3bea9
-  __TEXT.__gcc_except_tab: 0xf4d4
+  __TEXT.__cstring: 0x5b912
+  __TEXT.__oslogstring: 0x3c089
+  __TEXT.__gcc_except_tab: 0xf51c
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x14c6

   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x12948
+  __TEXT.__unwind_info: 0x12a08
   __TEXT.__eh_frame: 0x262c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc230
-  __DATA_CONST.__objc_classlist: 0x1f58
+  __DATA_CONST.__const: 0xc2b0
+  __DATA_CONST.__objc_classlist: 0x1f60
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x4d0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1c0c0
+  __DATA_CONST.__objc_selrefs: 0x1c158
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x14f8
-  __DATA_CONST.__objc_arraydata: 0x12f0
-  __DATA_CONST.__got: 0x39c8
-  __AUTH_CONST.__const: 0x8e70
-  __AUTH_CONST.__cfstring: 0x3bc80
-  __AUTH_CONST.__objc_const: 0x83d78
+  __DATA_CONST.__objc_superrefs: 0x1500
+  __DATA_CONST.__objc_arraydata: 0x1310
+  __DATA_CONST.__got: 0x39d0
+  __AUTH_CONST.__const: 0x8f70
+  __AUTH_CONST.__cfstring: 0x3bf80
+  __AUTH_CONST.__objc_const: 0x83ea8
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x3468
-  __AUTH_CONST.__objc_arrayobj: 0x1098
+  __AUTH_CONST.__objc_arrayobj: 0x10b0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x21f0
-  __AUTH.__objc_data: 0x4008
+  __AUTH_CONST.__auth_got: 0x21f8
+  __AUTH.__objc_data: 0x4058
   __AUTH.__data: 0x2178
-  __DATA.__objc_ivar: 0x4abc
+  __DATA.__objc_ivar: 0x4acc
   __DATA.__data: 0x3d18
   __DATA.__common: 0x128
   __DATA_DIRTY.__objc_data: 0x10088
   __DATA_DIRTY.__data: 0xd18
-  __DATA_DIRTY.__bss: 0xbb8
+  __DATA_DIRTY.__bss: 0xbc8
   __DATA_DIRTY.__common: 0xa0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 25767
-  Symbols:   36813
-  CStrings:  12517
+  Functions: 25815
+  Symbols:   36874
+  CStrings:  12569
 
Symbols:
+ +[ATXFaceGalleryLayoutGenerator descriptorsByPromotingCompactTimeDescriptorInDescriptors:toIndex:]
+ +[ATXNotificationCategorizationServer engagementMetricsJSONForTelemetry:error:]
+ +[ATXNotificationFeedbackContentStore isCollectionEnabled]
+ +[ATXNotificationFeedbackContentStore sharedInstance]
+ -[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationUUIDs:]
+ -[ATXNotificationAndSuggestionDatastore telemetryDataForNotificationUUIDs:]
+ -[ATXNotificationCategorizationServer collectEngagementMetricsForNotificationUUIDs:completion:]
+ -[ATXNotificationCategorizationServer collectNotificationFeedbackContentWithCompletion:]
+ -[ATXNotificationCategorizationServer deleteNotificationFeedbackContentWithCompletion:]
+ -[ATXNotificationFeedbackContentStore .cxx_destruct]
+ -[ATXNotificationFeedbackContentStore _queue_deleteAllIfPresent]
+ -[ATXNotificationFeedbackContentStore _queue_deleteAll]
+ -[ATXNotificationFeedbackContentStore _queue_openDatabase]
+ -[ATXNotificationFeedbackContentStore _queue_pruneWithDatabase:]
+ -[ATXNotificationFeedbackContentStore deleteAll]
+ -[ATXNotificationFeedbackContentStore initWithPath:isCollectionEnabled:]
+ -[ATXNotificationFeedbackContentStore pruneOrDeleteIfCollectionDisabled]
+ -[ATXNotificationFeedbackContentStore recentNotificationsJSONWithError:]
+ -[ATXNotificationFeedbackContentStore recordReceivedNotification:]
+ _ATXFaceGalleryFeaturedCompactTimeIndex
+ _ATXNotificationFeedbackDataCollectionEnabledKey
+ _OBJC_CLASS_$_ATXNotificationFeedbackContentStore
+ _OBJC_IVAR_$_ATXNotificationFeedbackContentStore._db
+ _OBJC_IVAR_$_ATXNotificationFeedbackContentStore._isCollectionEnabled
+ _OBJC_IVAR_$_ATXNotificationFeedbackContentStore._path
+ _OBJC_IVAR_$_ATXNotificationFeedbackContentStore._queue
+ _OBJC_METACLASS_$_ATXNotificationFeedbackContentStore
+ __OBJC_$_CLASS_METHODS_ATXNotificationFeedbackContentStore
+ __OBJC_$_INSTANCE_METHODS_ATXNotificationFeedbackContentStore
+ __OBJC_$_INSTANCE_VARIABLES_ATXNotificationFeedbackContentStore
+ __OBJC_CLASS_RO_$_ATXNotificationFeedbackContentStore
+ __OBJC_METACLASS_RO_$_ATXNotificationFeedbackContentStore
+ ___48-[ATXNotificationFeedbackContentStore deleteAll]_block_invoke
+ ___53+[ATXNotificationFeedbackContentStore sharedInstance]_block_invoke
+ ___53+[ATXNotificationFeedbackContentStore sharedInstance]_block_invoke_2
+ ___58-[ATXNotificationFeedbackContentStore _queue_openDatabase]_block_invoke
+ ___64-[ATXNotificationFeedbackContentStore _queue_pruneWithDatabase:]_block_invoke
+ ___64-[ATXNotificationFeedbackContentStore _queue_pruneWithDatabase:]_block_invoke_2
+ ___66-[ATXNotificationFeedbackContentStore recordReceivedNotification:]_block_invoke
+ ___66-[ATXNotificationFeedbackContentStore recordReceivedNotification:]_block_invoke_2
+ ___66-[ATXNotificationFeedbackContentStore recordReceivedNotification:]_block_invoke_3
+ ___66-[ATXNotificationFeedbackContentStore recordReceivedNotification:]_block_invoke_4
+ ___72-[ATXNotificationFeedbackContentStore pruneOrDeleteIfCollectionDisabled]_block_invoke
+ ___72-[ATXNotificationFeedbackContentStore recentNotificationsJSONWithError:]_block_invoke
+ ___72-[ATXNotificationFeedbackContentStore recentNotificationsJSONWithError:]_block_invoke_2
+ ___72-[ATXNotificationFeedbackContentStore recentNotificationsJSONWithError:]_block_invoke_3
+ ___74-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationUUIDs:]_block_invoke
+ ___74-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationUUIDs:]_block_invoke_2
+ ___74-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationUUIDs:]_block_invoke_3
+ ___74-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationUUIDs:]_block_invoke_4
+ ___74-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationUUIDs:]_block_invoke_5
+ ___95-[ATXNotificationCategorizationServer collectEngagementMetricsForNotificationUUIDs:completion:]_block_invoke
+ ___95-[ATXNotificationCategorizationServer collectEngagementMetricsForNotificationUUIDs:completion:]_block_invoke_2
+ ___98+[ATXFaceGalleryLayoutGenerator descriptorsByPromotingCompactTimeDescriptorInDescriptors:toIndex:]_block_invoke
+ ___block_descriptor_114_e8_32s40s48s56s64s72s80s88s_e29_v16?0"_PASSqliteStatement"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_122_e8_32s40s48s56s64s72s80s88s96s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_32_e36_B32?0"ATXPosterDescriptor"8Q16^B24l
+ _collectEngagementMetricsForNotificationUUIDs:completion:.engagementMetricsQueue
+ _collectEngagementMetricsForNotificationUUIDs:completion:.onceToken
+ _kATXNotificationTelemetryForNotificationUUIDsQuery
+ _swift_bridgeObjectRetain_n
CStrings:
+ "%s: could not delete %@: %@"
+ "%s: could not open the database: %@"
+ "%s: could not set up the database: %@"
+ "%s: deleted the notifications kept for Notification Feedback"
+ "%s: failed to keep a notification: %@"
+ "%s: failed to prune: %@"
+ "%s: failed to read notifications: %@"
+ "%s: found %lu deliveries of %lu notifications, error: %@"
+ "%s: promoting compact time descriptor from index %lu to %lu: %@ %@"
+ "+[ATXFaceGalleryLayoutGenerator descriptorsByPromotingCompactTimeDescriptorInDescriptors:toIndex:]"
+ "-[ATXNotificationCategorizationServer collectEngagementMetricsForNotificationUUIDs:completion:]"
+ "-[ATXNotificationCategorizationServer collectEngagementMetricsForNotificationUUIDs:completion:]_block_invoke"
+ "-[ATXNotificationFeedbackContentStore _queue_deleteAll]"
+ "-[ATXNotificationFeedbackContentStore _queue_openDatabase]"
+ "-[ATXNotificationFeedbackContentStore _queue_openDatabase]_block_invoke"
+ "-[ATXNotificationFeedbackContentStore _queue_pruneWithDatabase:]_block_invoke_2"
+ "-[ATXNotificationFeedbackContentStore recentNotificationsJSONWithError:]_block_invoke_3"
+ "-[ATXNotificationFeedbackContentStore recordReceivedNotification:]_block_invoke_4"
+ "-journal"
+ ":body"
+ ":contactIds"
+ ":requestId"
+ "ATXNotificationCategorizationServer.collectEngagementMetrics"
+ "ATXNotificationFeedbackDataCollectionEnabled"
+ "ATXNotificationFeedbackEnabled"
+ "B32@?0@\"ATXPosterDescriptor\"8Q16^B24"
+ "CREATE INDEX IF NOT EXISTS notification_receiveTimestamp ON notification (receiveTimestamp)"
+ "CREATE TABLE IF NOT EXISTS notification (uuid TEXT PRIMARY KEY, bundleId TEXT NOT NULL, requestId TEXT, receiveTimestamp REAL NOT NULL, title TEXT, subtitle TEXT, body TEXT, threadId TEXT, contactIds BLOB, isMessage INTEGER NOT NULL, isGroupMessage INTEGER NOT NULL, urgency INTEGER NOT NULL)"
+ "DELETE FROM notification WHERE receiveTimestamp < :cutoff"
+ "Engagement metrics are only available on internal builds"
+ "Engagement metrics aren't valid JSON"
+ "INSERT OR REPLACE INTO notification (uuid, bundleId, requestId, receiveTimestamp, title, subtitle, body, threadId, contactIds, isMessage, isGroupMessage, urgency) VALUES (:uuid, :bundleId, :requestId, :receiveTimestamp, :title, :subtitle, :body, :threadId, :contactIds, :isMessage, :isGroupMessage, :urgency)"
+ "Notification Feedback's data collection is off"
+ "NotificationFeedbackContent.db"
+ "PRAGMA journal_mode=DELETE"
+ "PRAGMA secure_delete=ON"
+ "SELECT     COALESCE(notificationUUID, uuid) AS uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     receivedMode,     firstUI,     mostRecentUI,     deliveryReason,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isDeliveredInPrioritySection,     isSummarized,     isPartOfStack,     isStackSummary,     numberOfNotificationsInStack,     notificationPriorityStatus,     notificationSummaryStatus,     isPriorityNotificationEnabled,     isNotificationSummaryEnabled,     nextAppLaunchTimestamp,     priorityFeedback,     resolutionUI FROM notifications WHERE     uuid IN _pas_nsarray(:notificationUUIDs) OR     notificationUUID IN _pas_nsarray(:notificationUUIDs) ORDER BY receiveTimestamp ASC "
+ "SELECT * FROM notification ORDER BY receiveTimestamp DESC"
+ "Starting %s for %lu notifications"
+ "body"
+ "bundleIdentifier"
+ "com.apple.duetexpertd.ATXNotificationCategorizationServer.engagementMetrics"
+ "com.apple.duetexpertd.ATXNotificationFeedbackContentStore"
+ "contactIdentifiers"
+ "contactIds"
+ "isCommunication"
+ "isCritical"
+ "isGroupThread"
+ "isTimeSensitive"
+ "requestId"
+ "requestIdentifier"
+ "threadIdentifier"
```
