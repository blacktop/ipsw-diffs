## HybridSearch

> `/System/Library/PrivateFrameworks/HybridSearch.framework/HybridSearch`

```diff

-67.0.0.0.0
-  __TEXT.__text: 0x470a04
-  __TEXT.__objc_methlist: 0x404
-  __TEXT.__cstring: 0x7003
-  __TEXT.__swift5_typeref: 0x1106c
-  __TEXT.__const: 0x520d0
-  __TEXT.__constg_swiftt: 0xc638
-  __TEXT.__swift5_builtin: 0x334
-  __TEXT.__swift5_reflstr: 0x13924
-  __TEXT.__swift5_fieldmd: 0x17620
-  __TEXT.__swift5_assocty: 0x5c70
-  __TEXT.__swift5_proto: 0x4964
-  __TEXT.__swift5_types: 0x13f0
-  __TEXT.__oslogstring: 0x1e5e
-  __TEXT.__swift_as_entry: 0x84c
-  __TEXT.__swift_as_ret: 0x804
-  __TEXT.__swift_as_cont: 0xd74
-  __TEXT.__swift5_protos: 0x74
-  __TEXT.__swift5_mpenum: 0x24c
-  __TEXT.__swift5_capture: 0x47b4
+73.2.0.0.0
+  __TEXT.__text: 0x62bcec
+  __TEXT.__objc_methlist: 0x234
+  __TEXT.__cstring: 0x96b3
+  __TEXT.__swift5_typeref: 0x146c4
+  __TEXT.__const: 0x649c0
+  __TEXT.__constg_swiftt: 0xe1c0
+  __TEXT.__swift5_builtin: 0x384
+  __TEXT.__swift5_reflstr: 0x19c6d
+  __TEXT.__swift5_assocty: 0x7780
+  __TEXT.__swift5_fieldmd: 0x1cc2c
+  __TEXT.__swift5_proto: 0x5928
+  __TEXT.__swift5_types: 0x16cc
+  __TEXT.__oslogstring: 0x214e
+  __TEXT.__swift_as_entry: 0xfa8
+  __TEXT.__swift_as_ret: 0xfa4
+  __TEXT.__swift_as_cont: 0x14e8
+  __TEXT.__swift5_protos: 0x98
+  __TEXT.__swift5_mpenum: 0x29c
+  __TEXT.__swift5_capture: 0x4044
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x18810
-  __TEXT.__eh_frame: 0x1c76c
+  __TEXT.__swift5_acfuncs: 0x5a0
+  __TEXT.__unwind_info: 0x1ee50
+  __TEXT.__eh_frame: 0x2a714
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x170
-  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__const: 0x1b8
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x550
-  __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__got: 0x690
-  __AUTH_CONST.__const: 0x40578
-  __AUTH_CONST.__objc_const: 0x1d48
-  __AUTH_CONST.__auth_got: 0x1608
-  __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0xc700
-  __DATA.__data: 0xff68
-  __DATA.__common: 0x170
+  __DATA_CONST.__objc_selrefs: 0x440
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__got: 0x740
+  __AUTH_CONST.__const: 0x4d750
+  __AUTH_CONST.__objc_const: 0x1be8
+  __AUTH_CONST.__auth_got: 0x19e0
+  __AUTH.__objc_data: 0x230
+  __AUTH.__data: 0xf9d0
+  __DATA.__data: 0x12888
+  __DATA.__common: 0x198
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/IntelligencePlatformQuery.framework/IntelligencePlatformQuery
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
-  - /System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport
+  - /System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftDistributed.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftSynchronization.dylib
+  - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 34545
-  Symbols:   280
-  CStrings:  1121
+  Functions: 41777
+  Symbols:   297
+  CStrings:  1529
 
Symbols:
+ _CCSetErrorDomain
+ _OBJC_CLASS_$_OS_dispatch_queue_serial
+ _SecTaskCreateWithAuditToken
+ _dispatch_semaphore_create
+ _dispatch_sync
+ _object_getClass
+ _os_transaction_create
+ _pthread_mach_thread_np
+ _pthread_self
+ _qos_class_self
+ _swift_distributedActor_remote_initialize
+ _swift_distributed_actor_is_remote
+ _swift_getExistentialTypeMetadata
+ _swift_isEscapingClosureAtFileLocation
+ _swift_release_x14
+ _swift_task_immediate
+ _swift_task_isCurrentExecutorWithFlags
+ _swift_willThrowTypedImpl
+ _thread_info
+ _xpc_fd_create
+ _xpc_fd_dup
+ _xpc_get_type
- _OBJC_CLASS_$_NSFileHandle
- _objc_retain_x25
- _swift_deletedAsyncMethodErrorTu
- _swift_release_x15
- _swift_unknownObjectRetain_n
CStrings:
+ " AND activityType IN ("
+ " AND locationType IN ("
+ " AND startDate <= '"
+ " AND startDate >= '"
+ " FROM FitnessWorkoutRecord WHERE 1=1"
+ " Important dates: "
+ " degrees Celsius"
+ " seconds per minute"
+ "%{public}s cancelling request after %{public}s"
+ "%{public}s escalating priority %s→%s after %{public}s"
+ "%{public}s failed after %{public}s with error %{public}@"
+ "%{public}s received response after %{public}s"
+ "%{public}s request cancelled after %{public}s"
+ "%{public}s sending request"
+ "(CASE WHEN strftime('%w', start, 'unixepoch') IN ('0', '6') THEN 'Weekend' ELSE 'Weekday' END)"
+ "(CASE WHEN strftime('%w', startDate, 'unixepoch') IN ('0', '6') THEN 'Weekend' ELSE 'Weekday' END)"
+ ", AVG(average) AS avg"
+ ", COUNT(*) AS workoutCount"
+ ", MAX(maximum) AS max"
+ ", MAX(startDate)"
+ ", MIN(minimum) AS min"
+ ", SUM(sum) AS sum"
+ ", unit, COUNT(*) AS recordCount FROM HealthStatisticsRecord WHERE measurementIdentifier = '"
+ "Activity Move Mode: "
+ "Activity paused: "
+ "Ambiguous reverse mapping: both .provenance_stableIdentifier and .itemInstanceUUID map to this record attribute"
+ "Average heart rate: "
+ "Awake: %.1f minutes."
+ "Biological sex: "
+ "Blood oxygen: %.1f%%."
+ "Calories burned: "
+ "Core sleep: %.1f hours."
+ "Deep sleep: %.1f hours."
+ "DocumentCacheRetriever: Cache miss — CachedDocument set does not exist for this bundle. Reason: %@"
+ "Elevation gain: "
+ "Exercise minutes: "
+ "Failed to get remote invocation origin audit token"
+ "Failed to initialize SecTask from audit token"
+ "Final heart rate: "
+ "Fitness Activity Rings"
+ "Fitness Mindful Session"
+ "Fitness Mindful Session on "
+ "Fitness Workout on "
+ "Fitness activity rings on "
+ "FitnessActivityRings"
+ "FitnessMindfulSession"
+ "Flights of stairs climbed: "
+ "Health Measurement"
+ "Health category sample of "
+ "Health characteristics"
+ "Health classification of "
+ "Health statistics of "
+ "HealthCategorySample"
+ "HealthCharacteristics"
+ "HealthClassification"
+ "HealthKit Kind: "
+ "HealthOvernightVitalsSummary"
+ "HealthSleepDaySummary"
+ "HealthStateOfMindSample"
+ "HealthStatistics"
+ "HealthSummaryInsight"
+ "Heart rate variability: %.0f ms."
+ "HybridSearch.IndexingClient"
+ "HybridSearch.SearchClient"
+ "HybridSearch/BarrierInsightEntityAttributeMappers.swift"
+ "HybridSearch/MotivatorInsightEntityAttributeMappers.swift"
+ "HybridSearch/ResourceInsightEntityAttributeMappers.swift"
+ "HybridSearch/SearchServiceProtocol.swift"
+ "HybridSearchProvider.scanSync"
+ "Int could not be created from String key"
+ "Internal error: "
+ "Kickoff Fitness Activity Rings donation"
+ "Kickoff Fitness Mindful Session donation"
+ "Kickoff Fitness Workout donation"
+ "Kickoff Health Measurement donation"
+ "Last data entry timestamp: "
+ "LiveCountQuery [%{public}s] awaiting next trigger"
+ "LiveCountQuery [%{public}s] count changed %{public}ld -> %{public}ld"
+ "LiveCountQuery [%{public}s] count unchanged at %{public}ld, waiting"
+ "LiveCountQuery [%{public}s] initial count is %{public}ld"
+ "LiveCountQuery [%{public}s] starting initial count"
+ "LiveCountQuery [%{public}s] trigger stream ended, finishing count stream"
+ "LiveCountQuery.start"
+ "LiveQuery [%{public}s] awaiting next trigger"
+ "LiveQuery [%{public}s] diff complete: %ld additions, %ld removals"
+ "LiveQuery [%{public}s] initial retrieval returned %ld results"
+ "LiveQuery [%{public}s] initializing differ (%ld results)"
+ "LiveQuery [%{public}s] starting initial retrieval"
+ "LiveQuery [%{public}s] trigger fired, performing retrieval"
+ "LiveQuery [%{public}s] trigger stream ended, finishing delta stream"
+ "Meditation type: "
+ "MessageIndexing"
+ "Momentary Emotion"
+ "Most recent data entry: "
+ "MotivatorInsight"
+ "Neither 'categoryKey' nor its 'category' fallback spelling was present"
+ "Not authorized: "
+ "Overnight heart rate: %.0f bpm."
+ "Overnight vitals summary for "
+ "REM sleep: %.1f hours."
+ "Request cancelled"
+ "Respiratory rate: %.1f breaths/min."
+ "Scoring parameter documentLengthNormalization must be finite and in [0, 1], got "
+ "Scoring parameter termFrequencySaturation must be finite and >= 0, got "
+ "Scoring parameters must carry at least one tuned parameter"
+ "Session data source: "
+ "Session duration: "
+ "Session identifier: "
+ "Sleep day summary for "
+ "Time asleep: %.1f hours."
+ "Total data points: "
+ "Total distance: "
+ "Total sleep: %.1f hours."
+ "Unable to determine remote invocation origin"
+ "Unknown IndexReadiness identifier '"
+ "Unknown distinctBy attribute '"
+ "Unknown entity type: "
+ "Uses wheelchair: "
+ "Valence: %.2f (Classification: "
+ "Wheelchair use: "
+ "Workout data source: "
+ "Workout duration: "
+ "Workout identifier: "
+ "WorkoutPlaceInsight"
+ "Wrist temperature deviation: %.2f°C."
+ "XPC call did not complete"
+ "activeEnergy"
+ "activityMoveMode"
+ "addDynamicStartupTask"
+ "addDynamicStartupTask(task:context:)"
+ "allDay"
+ "americanFootball"
+ "appleMoveTime"
+ "archery"
+ "associations"
+ "attendees"
+ "attendeesText"
+ "attributeName"
+ "australianFootball"
+ "availability"
+ "average"
+ "averageHeartRate"
+ "averagePace"
+ "badminton"
+ "barre"
+ "barrierInsight"
+ "baseball"
+ "baselineMedialRangeMaximum"
+ "baselineMedialRangeMinimum"
+ "basketball"
+ "biologicalSex"
+ "birthDate"
+ "bloodOxygen"
+ "bloodType"
+ "bowling"
+ "boxing"
+ "cacheIndex"
+ "caloriesBurned"
+ "caloriesBurnedGoal"
+ "cardioDance"
+ "categoryKey"
+ "chatStyle"
+ "checkEmbeddingModelEnabled(context:)"
+ "climbing"
+ "content"
+ "conversation"
+ "cooldown"
+ "cooldown(context:)"
+ "coreSleepDuration"
+ "coreTraining"
+ "countAll"
+ "countAllDomain(payload:context:)"
+ "countByDisplayIdentifier"
+ "countByDisplayIdentifier(context:)"
+ "countDomain"
+ "countDomain(payload:context:)"
+ "countEmbeddingsDomain"
+ "countEmbeddingsDomain(payload:context:)"
+ "countEmbeddingsGlobal"
+ "countEmbeddingsGlobal(payload:context:)"
+ "countGlobal"
+ "countGlobal(payload:context:)"
+ "createEmbeddings"
+ "createEmbeddings(payload:context:)"
+ "cricket"
+ "crossCountrySkiing"
+ "crossTraining"
+ "curling"
+ "cycling"
+ "dance"
+ "danceInspiredTraining"
+ "date(start, 'unixepoch')"
+ "date(start, 'unixepoch', '+1 day', 'weekday 0', '-7 days')"
+ "date(startDate, 'unixepoch')"
+ "date(startDate, 'unixepoch', '+1 day', 'weekday 0', '-7 days')"
+ "dayComponent"
+ "deepSleepDuration"
+ "deleteEmbeddings"
+ "deleteEmbeddings(payload:context:)"
+ "discSports"
+ "distance"
+ "distinctByAttributeName"
+ "documentLengthNormalization"
+ "downhillSkiing"
+ "dueDate"
+ "dump"
+ "dumpDomain(payload:context:outputFileHandle:)"
+ "duration"
+ "elevationGain"
+ "elliptical"
+ "end"
+ "entityTypeName"
+ "equestrianSports"
+ "ethnicity"
+ "eventStatus"
+ "evidence"
+ "exerciseMinutes"
+ "exerciseMinutesGoal"
+ "failure"
+ "fencing"
+ "finalHeartRate"
+ "fishing"
+ "fitnessActivityRings"
+ "fitnessGaming"
+ "fitnessMindfulSession"
+ "fitnessPlusSessionMetadata"
+ "fitnessWorkout"
+ "fitzpatrickSkinType"
+ "flexibility"
+ "flightsClimbed"
+ "folder"
+ "forceBackfill"
+ "forceBackfill(storeName:context:)"
+ "functionalStrengthTraining"
+ "generationVersion(context:)"
+ "getDynamicStartupTaskRecord"
+ "getDynamicStartupTaskRecord(taskId:context:)"
+ "getDynamicStartupTaskRecords"
+ "getDynamicStartupTaskRecords(context:)"
+ "golf"
+ "groupName"
+ "gymnastics"
+ "handCycling"
+ "handball"
+ "healthCategorySample"
+ "healthCharacteristics"
+ "healthClassification"
+ "healthKitKindType"
+ "healthMeasurement"
+ "healthOvernightVitalsSummary"
+ "healthSleepDaySummary"
+ "healthStateOfMindSample"
+ "healthStatistics"
+ "healthSummaryInsight"
+ "heartRate"
+ "heartRateVariability"
+ "highIntensityIntervalTraining"
+ "hiking"
+ "hockey"
+ "hourOfDay"
+ "hunting"
+ "identifierType"
+ "indexItems"
+ "indexItems(items:context:)"
+ "indexReadiness"
+ "indexReadiness(context:)"
+ "indexSize"
+ "indexSize(context:)"
+ "indoor"
+ "ingestionDate"
+ "integrationTestOnly_reportABC"
+ "integrationTestOnly_reportABC(source:context:)"
+ "integrationTestOnly_reportTapToRadar"
+ "integrationTestOnly_reportTapToRadar(source:context:)"
+ "isCompleted"
+ "isFromMe"
+ "isHoliday"
+ "isPaused"
+ "isRecurring"
+ "isSensitive"
+ "isVacation"
+ "isWheelchairUser"
+ "jumpRope"
+ "kickboxing"
+ "labels"
+ "lacrosse"
+ "latitude"
+ "levelID"
+ "lexicalScore"
+ "lexicalTermMatches"
+ "listID"
+ "listStores"
+ "listStores(context:)"
+ "location"
+ "locationName"
+ "locationText"
+ "locationType"
+ "longitude"
+ "lookbackPeriodEndAtPlace"
+ "lookbackPeriodStartAtPlace"
+ "martialArts"
+ "maximum"
+ "measurementIdentifier"
+ "medianWorkoutDuration"
+ "meditationType"
+ "messageID"
+ "mindAndBody"
+ "minimum"
+ "mixedCardio"
+ "mixedMetabolicCardioTraining"
+ "modificationDate"
+ "monthComponent"
+ "monthOfYear"
+ "mostRecent"
+ "motivatorBarrierResource"
+ "motivatorInsight"
+ "moveMinutes"
+ "moveMinutesGoal"
+ "numWorkoutsAtPlace"
+ "openWater"
+ "organizers"
+ "organizersText"
+ "other"
+ "outdoor"
+ "outputFileHandle"
+ "paddleSports"
+ "payload"
+ "peopleGroup"
+ "performCount: predicate: %{public}s | distinctBy: %{public}s | sensitive: %{sensitive}s"
+ "pickleball"
+ "pilates"
+ "play"
+ "pool"
+ "preparationAndRecovery"
+ "prewarm"
+ "prewarm(context:)"
+ "primaryAwakeDuration"
+ "primaryCoreSleepDuration"
+ "primaryDeepSleepDuration"
+ "primaryInBedDuration"
+ "primaryRemSleepDuration"
+ "primarySleepDuration"
+ "primarySleepEndTime"
+ "primarySleepStartTime"
+ "primaryTimeZone"
+ "privacy"
+ "processingStatus"
+ "processingStatus(context:)"
+ "quantity"
+ "racquetball"
+ "rationale"
+ "rawValue"
+ "remSleepDuration"
+ "resourceInsight"
+ "respiratoryRate"
+ "restartForDynamicStartupTask"
+ "restartForDynamicStartupTask(taskId:context:)"
+ "retrieveDomain(payload:context:)"
+ "rowing"
+ "rugby"
+ "runDataMigration"
+ "runDataMigration(readiness:context:)"
+ "running"
+ "sailing"
+ "scaleLevelID"
+ "scan(payload:context:)"
+ "scheduledBedTimeHour"
+ "scheduledBedTimeMinute"
+ "scheduledWakeTimeHour"
+ "scheduledWakeTimeMinute"
+ "scoreAwakeDurationPoints"
+ "scoreAwakeInterruptionPoints"
+ "scoreAwakePoints"
+ "scoreDeepSleepDurationPoints"
+ "scoreRemSleepDurationPoints"
+ "scoreSleepDurationPoints"
+ "scoreSleepStartPunctualityPoints"
+ "scoreTotalPoints"
+ "scoringParameters"
+ "searchDomain(payload:context:)"
+ "searchGlobal(payload:context:)"
+ "semanticContext"
+ "senderText"
+ "sessionCount"
+ "sessionIdentifier"
+ "sessions"
+ "skatingSports"
+ "snowSports"
+ "snowboarding"
+ "soccer"
+ "socialDance"
+ "softball"
+ "sourceDevice"
+ "sourceItemUUID"
+ "squash"
+ "stairClimbing"
+ "stairs"
+ "standHour"
+ "standHourGoal"
+ "start"
+ "stepTraining"
+ "strftime('%Y-%m', start, 'unixepoch')"
+ "strftime('%Y-%m', startDate, 'unixepoch')"
+ "strftime('%Y-%m-%d %H:00:00', start, 'unixepoch')"
+ "strftime('%Y-%m-%d %H:00:00', startDate, 'unixepoch')"
+ "strftime('%w', startDate, 'unixepoch')"
+ "surfingSports"
+ "swimBikeRun"
+ "swimming"
+ "tableTennis"
+ "tags"
+ "taiChi"
+ "tearDown"
+ "tearDown(context:)"
+ "temporalWindow"
+ "tennis"
+ "termFrequencySaturation"
+ "termScores"
+ "termTypeRaw"
+ "threadIdentifier"
+ "timeAsleep"
+ "timestamp"
+ "titleText"
+ "totalSteps"
+ "trackAndField"
+ "traditionalStrengthTraining"
+ "trainerFullNames"
+ "trainerIdentifiers"
+ "trainerInformalNames"
+ "triggerCorruptionHandler"
+ "triggerCorruptionHandler(context:)"
+ "underwaterDiving"
+ "unit"
+ "unspecifiedSleepDuration"
+ "updateEmbeddingsByReference"
+ "updateEmbeddingsByReference(payload:context:)"
+ "vacuumStart"
+ "vacuumStart(config:context:)"
+ "vacuumStatus"
+ "vacuumStatus(context:)"
+ "valence"
+ "valenceClassification"
+ "variant"
+ "vectorScores"
+ "volleyball"
+ "walking"
+ "walkingRunningDistance"
+ "waterFitness"
+ "waterPolo"
+ "waterSports"
+ "weakAnd matchMode requires weakAndThreshold on the wire"
+ "weakAnd threshold must be in the open interval (0, 1), got "
+ "weatherTemperature"
+ "wheelchairRunPace"
+ "wheelchairUse"
+ "wheelchairWalkPace"
+ "workdayType"
+ "workoutDescription"
+ "workoutIdentifier"
+ "workoutPlace"
+ "workoutPlaceInsight"
+ "workoutPlaceRank"
+ "workoutPlaceRole"
+ "wrestling"
+ "wristTemperature"
+ "writesUnavailable"
+ "yearComponent"
+ "yoga"
- " Relationships: "
- " Scheduled for: "
- "%{public}s cancelling request %{public}s"
- "%{public}s sending request %{public}s"
- "AdminClient.dropIndex(reason:)"
- "AdminClient.indexSize()"
- "AdminClient.taskRecords"
- "AdminClient.triggerCorruptionHandler()"
- "Down-casted Array element failed to match the target type\nExpected "
- "EmbeddingClient.createEmbeddings(for:)"
- "EmbeddingClient.deleteEmbeddingsWithResults(for:)"
- "EmbeddingClient.prewarm()"
- "EmbeddingClient.tearDown()"
- "EmbeddingClient.updateEmbeddings(byReference:)"
- "EmbeddingClient.updateEmbeddingsWithResults(_:)"
- "HybridSearch/CalendarContent.swift"
- "IndexingClient.index(items:)"
- "IndexingClient.prewarm()"
- "IndexingClient.sendCancelRequest"
- "IndexingClient.sendCancelRequest. Error: %{public}@"
- "IndexingClient.tearDown()"
- "InternalSearchClient.checkEmbeddingModelEnabled"
- "InternalSearchClient.cooldown"
- "InternalSearchClient.dump(ofType:)"
- "InternalSearchClient.prewarm"
- "InternalSearchClient.scan(ofType:)"
- "InternalSearchClient.scanSync(ofType:)"
- "InternalSearchClient.sendCancelRequest. Error: %{public}@"
- "LiveQuery awaiting next trigger"
- "LiveQuery diff complete: %ld additions, %ld removals"
- "LiveQuery initial retrieval returned %ld results"
- "LiveQuery initializing differ (%ld results)"
- "LiveQuery starting initial retrieval"
- "LiveQuery trigger fired, performing retrieval"
- "LiveQuery trigger stream ended, finishing delta stream"
- "SearchClient.count(ofType:predicate:)"
- "SearchClient.count(predicate:)"
- "SearchClient.countAll(ofType:predicate:)"
- "SearchClient.countEmbeddings(ofType:predicate:)"
- "SearchClient.countEmbeddings(predicate:)"
- "SearchClient.retrieve(ofType:searchTerms:predicate:)"
- "SearchClient.search(ofType:query:searchTerms:predicate:limit:orderBy:)"
- "SearchClient.search(query:predicate:limit:orderBy:)"
- "SearchClient.sendCancelRequest"
- "SearchIngestionClient.countByDisplayIdentifier()"
- "SearchIngestionClient.forceBackfill"
- "SearchIngestionClient.generationVersion"
- "SearchIngestionClient.listStores"
- "SearchIngestionClient.processingStatus"
- "SearchIngestionClient.sendCancelRequest"
- "SearchIngestionClient.vacuum"
- "SearchIngestionClient.vacuumStatus"
- "Swift.CancellationError"
- "_kMDItemAppEntityTypeIdentifier"
- "_kMDItemAppEntityTypeIdentifier == NoteEntity"
- "embeddingResults"
- "isSelf"
- "kMDItemTextContent"
- "kMDItemTextContent == \"*"
- "performCount: predicate: %{public}s | sensitive: %{sensitive}s"
```
