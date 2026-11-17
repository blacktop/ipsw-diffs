## ProactiveSummarization

> `/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization`

```diff

-1354.3.8.0.0
-  __TEXT.__text: 0x18d888
-  __TEXT.__objc_methlist: 0x714
-  __TEXT.__const: 0x12e58
-  __TEXT.__dlopen_cstrs: 0xaa
-  __TEXT.__cstring: 0xaac3
-  __TEXT.__swift5_typeref: 0x4960
-  __TEXT.__swift5_reflstr: 0x432d
+1354.3.14.0.0
+  __TEXT.__text: 0x18f488
+  __TEXT.__objc_methlist: 0x86c
+  __TEXT.__const: 0x12bd8
+  __TEXT.__dlopen_cstrs: 0xf9
+  __TEXT.__cstring: 0xc53e
+  __TEXT.__swift5_typeref: 0x4954
+  __TEXT.__swift5_reflstr: 0x42cd
   __TEXT.__swift5_assocty: 0x480
-  __TEXT.__constg_swiftt: 0x3c64
-  __TEXT.__swift5_fieldmd: 0x4910
-  __TEXT.__swift5_proto: 0xd64
-  __TEXT.__swift5_types: 0x588
+  __TEXT.__constg_swiftt: 0x3b74
+  __TEXT.__swift5_fieldmd: 0x481c
+  __TEXT.__swift5_proto: 0xd28
+  __TEXT.__swift5_types: 0x58c
   __TEXT.__swift5_protos: 0x4c
-  __TEXT.__swift5_capture: 0x34ec
-  __TEXT.__oslogstring: 0x74a8
-  __TEXT.__swift_as_entry: 0x5c4
-  __TEXT.__swift_as_ret: 0x808
-  __TEXT.__swift_as_cont: 0xc18
-  __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__gcc_except_tab: 0xfc
-  __TEXT.__unwind_info: 0x7f50
-  __TEXT.__eh_frame: 0x11148
+  __TEXT.__swift5_capture: 0x3cb8
+  __TEXT.__oslogstring: 0x77bc
+  __TEXT.__swift_as_entry: 0x598
+  __TEXT.__swift_as_ret: 0x7dc
+  __TEXT.__swift_as_cont: 0xbd0
+  __TEXT.__swift5_builtin: 0x118
+  __TEXT.__swift5_mpenum: 0x60
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__unwind_info: 0x7e58
+  __TEXT.__eh_frame: 0x10a40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x428
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__const: 0x508
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xe0
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf88
+  __DATA_CONST.__objc_selrefs: 0x1128
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__got: 0x1230
-  __AUTH_CONST.__const: 0x10720
-  __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0x3e08
-  __AUTH_CONST.__auth_got: 0x2060
+  __AUTH_CONST.__const: 0x12210
+  __AUTH_CONST.__cfstring: 0x320
+  __AUTH_CONST.__objc_const: 0x3f98
+  __AUTH_CONST.__auth_got: 0x2088
   __AUTH.__objc_data: 0x398
-  __AUTH.__data: 0xe58
-  __DATA.__objc_ivar: 0x24
+  __AUTH.__data: 0xdb8
+  __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x1b18
-  __DATA.__common: 0xc0
+  __DATA.__common: 0xb8
   __DATA_DIRTY.__objc_data: 0x388
-  __DATA_DIRTY.__data: 0x2930
-  __DATA_DIRTY.__bss: 0x1620
-  __DATA_DIRTY.__common: 0x310
+  __DATA_DIRTY.__data: 0x2940
+  __DATA_DIRTY.__bss: 0x1570
+  __DATA_DIRTY.__common: 0x308
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11241
-  Symbols:   3343
-  CStrings:  1404
+  Functions: 11452
+  Symbols:   3390
+  CStrings:  1526
 
Symbols:
+ +[PSULocationProvider stopMonitoringIfRegistered]
+ -[PSULocationProvider locationManager:didFailWithError:]
+ -[PSULocationProvider locationManager:didUpdateLocations:]
+ -[PSULocationProvider locationManager:didVisit:]
+ -[PSULocationProvider locationManagerDidChangeAuthorization:]
+ -[PSULocationProvider makeRoutineManager]
+ -[PSULocationProvider report:place:]
+ -[PSULocationProvider reportCurrentPlace]
+ -[PSULocationProvider reportPlaceAtLocation:event:arrival:]
+ -[PSULocationProvider requestFixIfAllowed]
+ -[PSULocationProvider startMonitoringPlaceWithHandler:]
+ -[PSULocationProvider stopMonitoringPlace]
+ GCC_except_table18
+ GCC_except_table46
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table72
+ GCC_except_table74
+ GCC_except_table76
+ GCC_except_table8
+ _CoreLocationLibraryCore
+ _CoreLocationLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_IVAR_$_PSULocationProvider._generation
+ _OBJC_IVAR_$_PSULocationProvider._handler
+ _OBJC_IVAR_$_PSULocationProvider._locationManager
+ _OBJC_IVAR_$_PSULocationProvider._queue
+ _OUTLINED_FUNCTION_520
+ __DATA__TtC22ProactiveSummarization18ContextSignalStore
+ __DATA__TtC22ProactiveSummarization30NotificationPipelineEventStore
+ __IVARS__TtC22ProactiveSummarization18ContextSignalStore
+ __IVARS__TtC22ProactiveSummarization30NotificationPipelineEventStore
+ __METACLASS_DATA__TtC22ProactiveSummarization18ContextSignalStore
+ __METACLASS_DATA__TtC22ProactiveSummarization30NotificationPipelineEventStore
+ __OBJC_$_CLASS_METHODS_PSULocationProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CLLocationManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CLLocationManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_CLLocationManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PSULocationProvider
+ __OBJC_LABEL_PROTOCOL_$_CLLocationManagerDelegate
+ __OBJC_PROTOCOL_$_CLLocationManagerDelegate
+ ___41-[PSULocationProvider reportCurrentPlace]_block_invoke
+ ___41-[PSULocationProvider reportCurrentPlace]_block_invoke_2
+ ___42-[PSULocationProvider stopMonitoringPlace]_block_invoke
+ ___49+[PSULocationProvider stopMonitoringIfRegistered]_block_invoke
+ ___55-[PSULocationProvider startMonitoringPlaceWithHandler:]_block_invoke
+ ___59-[PSULocationProvider reportPlaceAtLocation:event:arrival:]_block_invoke
+ ___59-[PSULocationProvider reportPlaceAtLocation:event:arrival:]_block_invoke_2
+ ___CoreLocationLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0lu40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s_e42_v24?0"RTLocationOfInterest"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___getCLLocationClass_block_invoke
+ ___getCLLocationManagerClass_block_invoke
+ ___swift_closure_destructor.28Tm
+ ___swift_closure_destructor.558Tm
+ ___swift_closure_destructor.662Tm
+ ___swift_closure_destructor.79Tm
+ ___swift_closure_destructor.88Tm
+ ___swift_memcpy145_8
+ ___unnamed_24
+ _audit_stringCoreLocation
+ _dispatch_async
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _getCLLocationClass.softClass
+ _getCLLocationManagerClass
+ _getCLLocationManagerClass.softClass
+ _get_enum_tag_for_layout_string 10Foundation4DataV15_RepresentationO
+ _get_enum_tag_for_layout_string 10Foundation4DataVSg
+ _objc_release_x1
+ _objc_retainBlock
+ _objc_retain_x3
+ _swift_isUniquelyReferenced_nonNull
+ _symbolic Ig_
+ _symbolic SDySSSay_____GG 10Foundation4DataV
+ _symbolic SDySSypGSg
+ _symbolic SaySay_____GG 22ProactiveSummarization19ContextSignalLoggerC10UsageEventV
+ _symbolic Say_____G 10Foundation4DataV
+ _symbolic Say_____G 22ProactiveSummarization24ContextSignalDeliveryRowV
+ _symbolic ScCySDySSSay_____GG_____G 10Foundation4DataV s5NeverO
+ _symbolic ScSy_____G 22ProactiveSummarization16PlaceObservationV
+ _symbolic So24PSUSummarizationPipelineCXDXMT
+ _symbolic So9TRIClientC
+ _symbolic _____ 22ProactiveSummarization12AssetManagerC14ConstantsCache025_A9C24845A2E6CB3ACCF47514J6E7FB6DLLV
+ _symbolic _____ 22ProactiveSummarization18ContextSignalStoreC
+ _symbolic _____ 22ProactiveSummarization19VisitLocationSourceV
+ _symbolic _____ 22ProactiveSummarization24ContextSignalDeliveryRowV
+ _symbolic _____ 22ProactiveSummarization30NotificationPipelineEventStoreC
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic _____Sg 22ProactiveSummarization19ContextSignalLoggerC
+ _symbolic _____Sg 22ProactiveSummarization24ContextSignalDeliveryRowV
+ _symbolic _____Sg 22ProactiveSummarization30NotificationPipelineEventStoreC
+ _symbolic _____XDXMT 22ProactiveSummarization30NotificationPipelineEventStoreC
+ _symbolic _____ySSSay_____GG s17_NativeDictionaryV 10Foundation4DataV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation4DataV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 22ProactiveSummarization24ContextSignalDeliveryRowV
+ _symbolic _____y_____Sg_____G s13ManagedBufferCsRi__rlE 22ProactiveSummarization30NotificationPipelineEventStoreC So16os_unfair_lock_sV
+ _symbolic _____y______G ScS12ContinuationV 22ProactiveSummarization16PlaceObservationV
+ _symbolic _____y______G ScS8IteratorV 22ProactiveSummarization16PlaceObservationV
+ _symbolic _____y_______G ScS12ContinuationV11YieldResultO 22ProactiveSummarization16PlaceObservationV
+ _symbolic _____y_______G ScS12ContinuationV15BufferingPolicyO 22ProactiveSummarization16PlaceObservationV
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 22ProactiveSummarization12AssetManagerC14ConstantsCache025_A9C24845A2E6CB3ACCF47514L6E7FB6DLLV So16os_unfair_lock_sV
+ _symbolic xIgr_
+ _type_layout_string 22ProactiveSummarization12AssetManagerC14ConstantsCache025_A9C24845A2E6CB3ACCF47514J6E7FB6DLLV
+ _type_layout_string 22ProactiveSummarization19VisitLocationSourceV
+ _type_layout_string 22ProactiveSummarization24ContextSignalDeliveryRowV
- -[PSULocationProvider fetchCurrentPlaceWithinWindow:completion:]
- -[PSULocationProvider isAvailable]
- -[PSULocationProvider routineManager]
- -[PSULocationProvider startMonitoringSettledStateWithHandler:]
- -[PSULocationProvider stopMonitoringSettledState]
- GCC_except_table12
- GCC_except_table44
- GCC_except_table45
- GCC_except_table55
- GCC_except_table57
- GCC_except_table59
- _OUTLINED_FUNCTION_516
- _OUTLINED_FUNCTION_626
- ___62-[PSULocationProvider startMonitoringSettledStateWithHandler:]_block_invoke
- ___64-[PSULocationProvider fetchCurrentPlaceWithinWindow:completion:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e39_v24?0"RTScenarioTrigger"8"NSError"16ls32l8s40l8
- ___swift_closure_destructor.111Tm
- ___swift_closure_destructor.26Tm
- ___swift_closure_destructor.556Tm
- ___swift_closure_destructor.660Tm
- ___swift_closure_destructor.77Tm
- ___swift_closure_destructor.86Tm
- ___swift_closure_destructor.95Tm
- ___unnamed_34
- __os_log_debug_impl
- _associated conformance 22ProactiveSummarization18ContextSignalStoreV10CodingKeys33_5D9C3894D823D7FE9D90BDD1F5A72004LLOSHAASQ
- _associated conformance 22ProactiveSummarization18ContextSignalStoreV10CodingKeys33_5D9C3894D823D7FE9D90BDD1F5A72004LLOs0F3KeyAAs23CustomStringConvertible
- _associated conformance 22ProactiveSummarization18ContextSignalStoreV10CodingKeys33_5D9C3894D823D7FE9D90BDD1F5A72004LLOs0F3KeyAAs28CustomDebugStringConvertible
- _associated conformance 22ProactiveSummarization21DeliveredNotificationV10CodingKeys33_5D9C3894D823D7FE9D90BDD1F5A72004LLOSHAASQ
- _associated conformance 22ProactiveSummarization21DeliveredNotificationV10CodingKeys33_5D9C3894D823D7FE9D90BDD1F5A72004LLOs0E3KeyAAs23CustomStringConvertible
- _associated conformance 22ProactiveSummarization21DeliveredNotificationV10CodingKeys33_5D9C3894D823D7FE9D90BDD1F5A72004LLOs0E3KeyAAs28CustomDebugStringConvertible
- _get_enum_tag_for_layout_string 22ProactiveSummarization24ContextSignalPersistenceV10LoadResultO
- _swift_release_x10
- _symbolic SDySSSdG
- _symbolic ScCySo15PSUPlaceContextCSg_____G s5NeverO
- _symbolic ScCy_____SgSg_____G 22ProactiveSummarization16PlaceObservationV s5NeverO
- _symbolic ScCy_____SgSg_____GSg 22ProactiveSummarization16PlaceObservationV s5NeverO
- _symbolic ScSySbG
- _symbolic So15PSUPlaceContextCSg
- _symbolic _____ 10Foundation3URLV
- _symbolic _____ 22ProactiveSummarization18ContextSignalStoreV
- _symbolic _____ 22ProactiveSummarization18ContextSignalStoreV10CodingKeys33_5D9C3894D823D7FE9D90BDD1F5A72004LLO
- _symbolic _____ 22ProactiveSummarization21DeliveredNotificationV10CodingKeys33_5D9C3894D823D7FE9D90BDD1F5A72004LLO
- _symbolic _____ 22ProactiveSummarization24ContextSignalPersistenceV
- _symbolic _____ 22ProactiveSummarization24ContextSignalPersistenceV10LoadResultO
- _symbolic _____ 22ProactiveSummarization25CoreRoutineLocationSourceV
- _symbolic _____SgIeghHr_ 22ProactiveSummarization16PlaceObservationV
- _symbolic _____SgSg 22ProactiveSummarization16PlaceObservationV
- _symbolic _____ySSSdG s17_NativeDictionaryV
- _symbolic _____ySSSdG s18_DictionaryStorageC
- _symbolic _____ySb_G ScS12ContinuationV
- _symbolic _____ySb_G ScS8IteratorV
- _symbolic _____ySb__G ScS12ContinuationV11YieldResultO
- _symbolic _____ySb__G ScS12ContinuationV15BufferingPolicyO
- _symbolic _____ySdSgG s23_ContiguousArrayStorageC
- _symbolic _____y_____G s22KeyedDecodingContainerV 22ProactiveSummarization18ContextSignalStoreV10CodingKeys33_5D9C3894D823D7FE9D90BDD1F5A72004LLO
- _symbolic _____y_____G s22KeyedDecodingContainerV 22ProactiveSummarization21DeliveredNotificationV10CodingKeys33_5D9C3894D823D7FE9D90BDD1F5A72004LLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 22ProactiveSummarization18ContextSignalStoreV10CodingKeys33_5D9C3894D823D7FE9D90BDD1F5A72004LLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 22ProactiveSummarization21DeliveredNotificationV10CodingKeys33_5D9C3894D823D7FE9D90BDD1F5A72004LLO
- _symbolic _____y_____SgSgG 22ProactiveSummarization12DeadlineGate33_3F73588C3A92FB599084710CA662C71CLLC AA16PlaceObservationV
- _type_layout_string 22ProactiveSummarization18ContextSignalStoreV
- _type_layout_string 22ProactiveSummarization24ContextSignalPersistenceV10LoadResultO
- _type_layout_string 22ProactiveSummarization25CoreRoutineLocationSourceV
CStrings:
+ " AND deliveryMode IS NOT :deliveryMode))"
+ " ORDER BY deliveredAt DESC, rowid DESC LIMIT 1"
+ " THEN :deliveryMode ELSE deliveryMode END WHERE id = :id AND (biomeNotificationId IS NOT :biomeNotificationId OR receivedAt IS NULL OR receivedAt > :receivedAt OR ("
+ "/System/Library/PrivateFrameworks/CoreParsec.framework"
+ "0`"
+ ":biomeNotificationId"
+ ":cursor"
+ ":deliveredAt"
+ ":deliveryMode"
+ ":deliveryMode IS NOT NULL AND (deliveryMode IS NULL OR deliveryMode = :replaceableMode)"
+ ":event"
+ ":high"
+ ":id"
+ ":ids"
+ ":key"
+ ":low"
+ ":notificationDate"
+ ":outcome"
+ ":receivedAt"
+ ":replaceableMode"
+ ":signals"
+ ":spotlightIdentifier"
+ ":spotlightIdentifiers"
+ ":time"
+ "AND biomeNotificationId IS NULL"
+ "CLLocation"
+ "CLLocationManager"
+ "CREATE INDEX IF NOT EXISTS contextSignalDelivery_biomeNotificationId ON contextSignalDelivery(biomeNotificationId)"
+ "CREATE INDEX IF NOT EXISTS contextSignalDelivery_bundleId_notificationDate ON contextSignalDelivery(bundleId, notificationDate)"
+ "CREATE INDEX IF NOT EXISTS contextSignalDelivery_deliveredAt ON contextSignalDelivery(deliveredAt)"
+ "CREATE INDEX IF NOT EXISTS contextSignalGestureStart_time ON contextSignalGestureStart(time)"
+ "CREATE INDEX IF NOT EXISTS contextSignalLoggedEvent_time ON contextSignalLoggedEvent(time)"
+ "CREATE INDEX IF NOT EXISTS notificationPipelineEvent_spotlightIdentifier ON notificationPipelineEvent(spotlightIdentifier)"
+ "CREATE INDEX IF NOT EXISTS notificationPipelineEvent_timestamp ON notificationPipelineEvent(timestamp)"
+ "CREATE TABLE IF NOT EXISTS contextSignalCursor (pk INTEGER PRIMARY KEY CHECK (pk = 1), cursor REAL NOT NULL)"
+ "CREATE TABLE IF NOT EXISTS contextSignalDelivery (id TEXT PRIMARY KEY, bundleId TEXT NOT NULL, threadId TEXT, notificationDate REAL NOT NULL, deliveredAt REAL NOT NULL, signals BLOB NOT NULL, biomeNotificationId TEXT, receivedAt REAL, deliveryMode TEXT, outcome BLOB, outcomeLogged INTEGER NOT NULL DEFAULT 0)"
+ "CREATE TABLE IF NOT EXISTS contextSignalGestureStart (biomeNotificationId TEXT PRIMARY KEY, time REAL NOT NULL)"
+ "CREATE TABLE IF NOT EXISTS contextSignalLoggedEvent (key TEXT PRIMARY KEY, time REAL NOT NULL)"
+ "CREATE TABLE IF NOT EXISTS notificationPipelineEvent (pk INTEGER PRIMARY KEY AUTOINCREMENT, spotlightIdentifier TEXT NOT NULL, timestamp REAL NOT NULL, event BLOB NOT NULL)"
+ "Context signal %{public}s not decoded: %{public}@"
+ "Context signal %{public}s not encoded: %{public}@"
+ "Context signals off: the pipeline database has no context signal tables"
+ "ContextSignalsLastLocationRequest"
+ "ContextSignalsLastPlace"
+ "ContextSignalsVisitMonitoringRegistered"
+ "Creating the notification pipeline event table, which migration 15 didn't create"
+ "DELETE FROM contextSignalDelivery WHERE id IN _pas_nsarray(:ids)"
+ "DELETE FROM contextSignalGestureStart WHERE time < :threshold"
+ "DELETE FROM contextSignalLoggedEvent WHERE time < :threshold"
+ "DELETE FROM notificationPipelineEvent ORDER BY timestamp DESC, pk DESC LIMIT -1 OFFSET :offset"
+ "DELETE FROM notificationPipelineEvent WHERE timestamp < :threshold"
+ "INSERT INTO notificationPipelineEvent (spotlightIdentifier, timestamp, event) VALUES (:spotlightIdentifier, :timestamp, :event)"
+ "INSERT OR IGNORE INTO contextSignalDelivery (id, bundleId, threadId, notificationDate, deliveredAt, biomeNotificationId, signals) VALUES (:id, :bundleId, :threadId, :notificationDate, :deliveredAt, :biomeNotificationId, :signals)"
+ "INSERT OR REPLACE INTO contextSignalCursor (pk, cursor) VALUES (1, :cursor)"
+ "INSERT OR REPLACE INTO contextSignalGestureStart (biomeNotificationId, time) VALUES (:biomeNotificationId, :time)"
+ "INSERT OR REPLACE INTO contextSignalLoggedEvent (key, time) VALUES (:key, :time)"
+ "NotificationOutcome"
+ "NotificationSignals"
+ "PSULocationProvider: %{public}s at %{private}@ (looked up in %.2fs)"
+ "PSULocationProvider: CoreLocation or CoreRoutine unavailable"
+ "PSULocationProvider: arrival %.0fs ago, accuracy %.0fm"
+ "PSULocationProvider: authorization %d"
+ "PSULocationProvider: departed (%.0fs ago)"
+ "PSULocationProvider: location failed: %{public}@ %ld"
+ "PSULocationProvider: monitoring visits, authorization %d"
+ "PSULocationProvider: moved since the saved place (error %ld)"
+ "PSULocationProvider: no fix, last requested %.0fs ago; waiting for a visit"
+ "PSULocationProvider: no location manager"
+ "PSULocationProvider: place lookup failed: %{public}ld"
+ "PSULocationProvider: place lookup overtaken by a later visit; dropped"
+ "PSULocationProvider: requesting a location fix"
+ "PSULocationProvider: restored %{private}@, no departure in %.0fs"
+ "PSULocationProvider: restored away, reported %.0fs ago"
+ "PSULocationProvider: stopped visit monitoring left from an earlier run"
+ "Place monitoring ended; place cleared, retrying later"
+ "Place now %{private}s visits=%{private}ld"
+ "ProactiveSummarization Trial namespace updated; refreshing assets"
+ "SELECT * FROM contextSignalDelivery WHERE deliveredAt < :threshold ORDER BY deliveredAt ASC, rowid ASC"
+ "SELECT * FROM contextSignalDelivery WHERE deliveredAt >= :threshold ORDER BY deliveredAt DESC, rowid DESC LIMIT -1 OFFSET :offset"
+ "SELECT * FROM contextSignalDelivery WHERE id = :id"
+ "SELECT 1 FROM contextSignalDelivery WHERE id = :id LIMIT 1"
+ "SELECT 1 FROM contextSignalLoggedEvent WHERE key = :key LIMIT 1"
+ "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'notificationPipelineEvent' LIMIT 1"
+ "SELECT cursor FROM contextSignalCursor WHERE pk = 1"
+ "SELECT id FROM contextSignalDelivery WHERE biomeNotificationId = :biomeNotificationId ORDER BY deliveredAt DESC, rowid DESC LIMIT 1"
+ "SELECT id FROM contextSignalDelivery WHERE bundleId = :bundleId AND notificationDate > :low AND notificationDate < :high AND (threadId IS NULL OR :threadId IS NULL OR threadId = :threadId) "
+ "SELECT signals FROM contextSignalDelivery WHERE id = :id"
+ "SELECT spotlightIdentifier, event FROM notificationPipelineEvent WHERE spotlightIdentifier IN _pas_nsarray(:spotlightIdentifiers) AND timestamp >= :threshold ORDER BY timestamp ASC, pk ASC"
+ "SELECT time FROM contextSignalGestureStart WHERE biomeNotificationId = :biomeNotificationId"
+ "UPDATE contextSignalDelivery SET biomeNotificationId = :biomeNotificationId, receivedAt = MIN(COALESCE(receivedAt, :receivedAt), :receivedAt), deliveryMode = CASE WHEN "
+ "UPDATE contextSignalDelivery SET biomeNotificationId = COALESCE(biomeNotificationId, :biomeNotificationId), outcome = :outcome WHERE id = :id"
+ "UPDATE contextSignalDelivery SET outcomeLogged = 1 WHERE id = :id"
+ "[NotificationPipelineEventStore] Not keeping an event that isn't valid JSON"
+ "arrived"
+ "attachContextSignalReceipt(id:biomeNotificationId:receivedAt:deliveryMode:replaceableMode:)"
+ "bundleId"
+ "com.apple.suggestions.NotificationPipelineEventStore"
+ "com.apple.suggestions.PSULocationProvider"
+ "contextSignalCursor()"
+ "contextSignalDelivery(id:)"
+ "contextSignalDeliveryExists(id:)"
+ "contextSignalDeliveryId(biomeNotificationId:)"
+ "contextSignalDeliveryId(bundleId:notificationDate:threadId:unattachedOnly:)"
+ "contextSignalEventIsLogged(key:)"
+ "contextSignalGestureStart(biomeNotificationId:)"
+ "contextSignalSignals(id:)"
+ "contextSignalWriteTransaction: body did not run"
+ "currently"
+ "cursor"
+ "deliveredAt"
+ "deliveryMode"
+ "ensureNotificationPipelineEventTable()"
+ "event"
+ "events(forSpotlightIdentifiers:now:)"
+ "hasNotificationPipelineEventTable"
+ "id"
+ "insertContextSignalDelivery(id:bundleId:threadId:notificationDate:deliveredAt:biomeNotificationId:signals:)"
+ "insertNotificationPipelineEvent(spotlightIdentifier:event:timestamp:)"
+ "kind"
+ "known"
+ "markContextSignalEventLogged(key:time:)"
+ "markContextSignalOutcomeLogged(id:)"
+ "no learned place"
+ "notificationPipelineEvents endpoint unavailable"
+ "notificationPipelineEvents(spotlightIdentifiers:since:)"
+ "outcome"
+ "outcomeLogged"
+ "pruneContextSignalDeliveries(olderThan:maxRowCount:)"
+ "pruneContextSignalEvents(olderThan:)"
+ "pruneNotificationPipelineEvents(olderThan:maxRowCount:)"
+ "receivedAt"
+ "setContextSignalCursor(_:)"
+ "setContextSignalGestureStart(biomeNotificationId:time:)"
+ "signals"
+ "softlink:o:path:/System/Library/Frameworks/CoreLocation.framework/CoreLocation"
+ "spotlightIdentifier"
+ "threadId"
+ "time"
+ "updateContextSignalOutcome(id:biomeNotificationId:outcome:)"
+ "v24@?0@\"RTLocationOfInterest\"8@\"NSError\"16"
+ "visitCount"
- "%.0fs ago"
- "Context signal store not readable yet: %{public}@"
- "Context signal store not saved: %{public}@"
- "Context signal store unreadable, starting over: %{public}@"
- "CoreRoutine unavailable"
- "Device %{public}s; refreshing place"
- "No place: nothing visited in either window, or no reply within %{public}s"
- "PSULocationProvider"
- "PSULocationProvider: LOI visit fetch failed: %{public}ld"
- "PSULocationProvider: RTRoutineManager has no +defaultManager"
- "PSULocationProvider: failed to soft-link CoreRoutine"
- "PSULocationProvider: latest visit type=%{private}ld entered=%{private}.0fs ago exited=%{private}@"
- "PSULocationProvider: settled-state monitoring error: %{public}@"
- "Place pull finished after a settled-state change; discarded"
- "Settled-state monitoring ended; retrying later"
- "completion != nil"
- "currentPlace(withinWindow:)"
- "open"
- "v24@?0@\"RTScenarioTrigger\"8@\"NSError\"16"
```
