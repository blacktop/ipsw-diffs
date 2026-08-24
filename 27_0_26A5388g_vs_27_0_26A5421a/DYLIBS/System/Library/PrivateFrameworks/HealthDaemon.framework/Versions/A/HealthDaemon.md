## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/Versions/A/HealthDaemon`

```diff

-7027.0.67.1.1
-  __TEXT.__text: 0x968068
-  __TEXT.__objc_methlist: 0x459fc
-  __TEXT.__const: 0x253c0
-  __TEXT.__constg_swiftt: 0x3ba0
-  __TEXT.__swift5_typeref: 0x3ff9
+7027.0.72.1.1
+  __TEXT.__text: 0x96b1ac
+  __TEXT.__objc_methlist: 0x45a2c
+  __TEXT.__const: 0x253f0
+  __TEXT.__constg_swiftt: 0x3be4
+  __TEXT.__swift5_typeref: 0x3fff
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0x29d8
-  __TEXT.__swift5_fieldmd: 0x2bb0
+  __TEXT.__swift5_reflstr: 0x2a18
+  __TEXT.__swift5_fieldmd: 0x2be4
   __TEXT.__swift5_assocty: 0x9b8
   __TEXT.__swift5_proto: 0x4e4
-  __TEXT.__swift5_types: 0x318
-  __TEXT.__cstring: 0x8350e
+  __TEXT.__swift5_types: 0x31c
+  __TEXT.__cstring: 0x83892
   __TEXT.__swift5_capture: 0x1bb8
-  __TEXT.__oslogstring: 0x44a0a
+  __TEXT.__oslogstring: 0x44b69
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_protos: 0xac
   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift_as_cont: 0x2c
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x391ec
+  __TEXT.__gcc_except_tab: 0x392d8
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x206f0
-  __TEXT.__eh_frame: 0x6030
+  __TEXT.__unwind_info: 0x20738
+  __TEXT.__eh_frame: 0x6060
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc420
-  __DATA_CONST.__objc_classlist: 0x2b50
+  __DATA_CONST.__objc_classlist: 0x2b58
   __DATA_CONST.__objc_catlist: 0x490
   __DATA_CONST.__objc_protolist: 0xb18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x1ac00
+  __DATA_CONST.__objc_selrefs: 0x1ac18
   __DATA_CONST.__objc_protorefs: 0x2e8
   __DATA_CONST.__objc_superrefs: 0x1d40
-  __DATA_CONST.__objc_arraydata: 0x89a0
+  __DATA_CONST.__objc_arraydata: 0x89e8
   __DATA_CONST.__got: 0x58a0
-  __AUTH_CONST.__const: 0x29890
-  __AUTH_CONST.__cfstring: 0x3fc80
-  __AUTH_CONST.__objc_const: 0x81580
+  __AUTH_CONST.__const: 0x29898
+  __AUTH_CONST.__cfstring: 0x3fde0
+  __AUTH_CONST.__objc_const: 0x81688
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x3eb8
-  __AUTH_CONST.__objc_arrayobj: 0x2148
+  __AUTH_CONST.__objc_arrayobj: 0x2178
   __AUTH_CONST.__objc_doubleobj: 0x3c0
-  __AUTH_CONST.__auth_got: 0x3758
+  __AUTH_CONST.__auth_got: 0x3768
   __AUTH.__objc_data: 0x8b40
-  __AUTH.__data: 0x1a98
-  __DATA.__objc_ivar: 0x44c4
-  __DATA.__data: 0x94f8
+  __AUTH.__data: 0x1b40
+  __DATA.__objc_ivar: 0x44cc
+  __DATA.__data: 0x9518
   __DATA.__bss: 0x75e0
   __DATA.__common: 0x198
   __DATA_DIRTY.__objc_ivar: 0xe30
   __DATA_DIRTY.__objc_data: 0x13d28
-  __DATA_DIRTY.__data: 0x3658
+  __DATA_DIRTY.__data: 0x3648
   __DATA_DIRTY.__bss: 0x1790
   __DATA_DIRTY.__common: 0x130
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 40086
-  Symbols:   70212
-  CStrings:  13842
+  Functions: 40113
+  Symbols:   70241
+  CStrings:  13861
 
Symbols:
+ +[HDFitnessFriendActivitySnapshotEntity shouldInsertObject:sourceID:profile:transaction:objectToReplace:objectID:error:]
+ -[HDLocationDataCollector flushBufferedLocationsThroughDate:completion:]
+ -[HDLocationDataCollector shouldFlushBufferedLocationTail]
+ -[HDLocationManager flushBufferedLocationsThroughDate:timeout:completion:]
+ OBJC_IVAR_$_HDLocationDataCollector._usesBufferedSensorBehavior
+ OBJC_IVAR_$_HDLocationManager._observerDeliveryQueue
+ _HDLocationDataCollectorStateToString
+ __72-[HDLocationDataCollector flushBufferedLocationsThroughDate:completion:]_block_invoke
+ __87-[HDWorkoutRouteDataSource workoutDataDestination:requestsFinalDataFrom:to:completion:]_block_invoke
+ __87-[HDWorkoutRouteDataSource workoutDataDestination:requestsFinalDataFrom:to:completion:]_block_invoke_2
+ __DATA__TtCC12HealthDaemon16HDDataCacheStoreP33_947F840B8844D71EAB3AFA884CB8010626AnchorAfterDatabaseScanBox
+ __HDCreateNMTable
+ __HDDeleteOrphanedFitnessFriendActivitySnapshots
+ __HDDropRedundantTrainingLoadCachePlainIndexes
+ __HKWorkoutExtendedModeTypeForPowerMode
+ __IVARS__TtCC12HealthDaemon16HDDataCacheStoreP33_947F840B8844D71EAB3AFA884CB8010626AnchorAfterDatabaseScanBox
+ __METACLASS_DATA__TtCC12HealthDaemon16HDDataCacheStoreP33_947F840B8844D71EAB3AFA884CB8010626AnchorAfterDatabaseScanBox
+ ___120+[HDFitnessFriendActivitySnapshotEntity shouldInsertObject:sourceID:profile:transaction:objectToReplace:objectID:error:]_block_invoke
+ ___72-[HDLocationDataCollector flushBufferedLocationsThroughDate:completion:]_block_invoke
+ ___72-[HDLocationDataCollector flushBufferedLocationsThroughDate:completion:]_block_invoke_2
+ ___74-[HDLocationManager flushBufferedLocationsThroughDate:timeout:completion:]_block_invoke
+ ___74-[HDLocationManager flushBufferedLocationsThroughDate:timeout:completion:]_block_invoke_2
+ ___78-[HDWorkoutRouteDataSource workoutDataDestination:didChangeFromState:toState:]_block_invoke
+ ___87-[HDWorkoutRouteDataSource workoutDataDestination:requestsFinalDataFrom:to:completion:]_block_invoke_4
+ ___87-[HDWorkoutRouteDataSource workoutDataDestination:requestsFinalDataFrom:to:completion:]_block_invoke_5
+ ___swift_memcpy120_8
+ ___swift_memcpy168_8
+ _objc_msgSend$flushBufferedLocationsThroughDate:completion:
+ _objc_msgSend$flushBufferedLocationsThroughDate:timeout:completion:
+ _objc_msgSend$shouldFlushBufferedLocationTail
+ _symbolic _____ 12HealthDaemon16HDDataCacheStoreC26AnchorAfterDatabaseScanBox33_947F840B8844D71EAB3AFA884CB80106LLC
- ___swift_memcpy112_8
- ___swift_memcpy160_8
CStrings:
+ "CREATE TEMPORARY TABLE temp_orphaned_ffas_ids AS             SELECT data_id FROM samples              WHERE data_type = 77                AND data_id NOT IN (SELECT data_id FROM fitness_friend_activity_snapshots)"
+ "DELETE FROM objects WHERE data_id IN (SELECT data_id FROM temp_orphaned_ffas_ids)"
+ "DELETE FROM samples WHERE data_id IN (SELECT data_id FROM temp_orphaned_ffas_ids)"
+ "DROP INDEX IF EXISTS training_load_statistics_cache_training_load_stats_idx"
+ "DROP INDEX IF EXISTS training_load_statistics_cache_training_load_stats_type_idx"
+ "DROP TABLE IF EXISTS temp_orphaned_ffas_ids"
+ "DROP TABLE temp_orphaned_ffas_ids"
+ "MANUALLY_ENTERED_TYPES_COUNT"
+ "No active transaction for %{public}@; forwarding presentation failure to fail the pending request"
+ "SELECT ROWID AS device_id FROM source_devices WHERE name IS NOT ?"
+ "SELECT p.source_id AS source_id,\n       p.device_id AS device_id,\n       COUNT(*) AS cnt\nFROM samples AS s\nINNER JOIN objects AS o ON o.data_id = s.data_id\nINNER JOIN data_provenances AS p ON o.provenance = p.ROWID\nWHERE s.data_type = ?\nGROUP BY p.source_id, p.device_id"
+ "Saving cached manually-entered types count"
+ "Unauthorized access to feature availability requirement evaluation"
+ "[Recovery] No accumulator snapshot for activity %s; creating fresh zone accumulators"
+ "[routes] %{public}@ Buffered-location flush skipped; no active location session."
+ "[routes] %{public}@ Deferring GPS teardown to final-data request to flush buffered route tail."
+ "[routes] %{public}@ Flushing buffered route tail through %@."
+ "[routes] %{public}@ Skipping buffered-location flush; collector is %{public}@."
+ "com.appleinternal."
+ "countFirstPartyInternalBundleIdentifier"
+ "health-location-manager-delivery"
+ "skipping prompt for drained request group %@; finishing it"
+ "sourceID deviceID count "
- "%{public}@: Failed to read associated builder configuration while finishing session: %{public}@"
- "%{public}@: Not finishing associated builder %{public}@: client is present and builder is actively saving (isEnding=YES)."
- "SELECT p.source_id AS source_id,\n       p.origin_product_type AS origin_product_type,\n       COUNT(*) AS cnt\nFROM samples AS s\nINNER JOIN objects AS o ON o.data_id = s.data_id\nINNER JOIN data_provenances AS p ON o.provenance = p.ROWID\nWHERE s.data_type = ?\nGROUP BY p.source_id, p.origin_product_type"
- "sourceID productType count "
```
