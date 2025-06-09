## geoanalyticsd

> `/System/Library/PrivateFrameworks/GeoAnalytics.framework/geoanalyticsd`

```diff

-1986.35.3.6.3
-  __TEXT.__text: 0x18214
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_stubs: 0x3220
-  __TEXT.__objc_methlist: 0xc14
-  __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0x438
-  __TEXT.__cstring: 0x3a20
-  __TEXT.__oslogstring: 0x11f1
-  __TEXT.__objc_classname: 0x22d
-  __TEXT.__objc_methname: 0x2d33
-  __TEXT.__objc_methtype: 0xabc
-  __TEXT.__unwind_info: 0x658
-  __DATA_CONST.__auth_got: 0x408
+2018.30.5.20.2
+  __TEXT.__text: 0x163e8
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_stubs: 0x3160
+  __TEXT.__objc_methlist: 0xc4c
+  __TEXT.__const: 0x10c
+  __TEXT.__gcc_except_tab: 0x82c
+  __TEXT.__cstring: 0x35bc
+  __TEXT.__oslogstring: 0xf86
+  __TEXT.__objc_classname: 0x26d
+  __TEXT.__objc_methname: 0x2c7a
+  __TEXT.__objc_methtype: 0xb29
+  __TEXT.__unwind_info: 0x5f8
+  __DATA_CONST.__auth_got: 0x430
   __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x10c0
-  __DATA_CONST.__cfstring: 0x30a0
-  __DATA_CONST.__objc_classlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__const: 0x1030
+  __DATA_CONST.__cfstring: 0x2fc0
+  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x20f0
-  __DATA.__objc_selrefs: 0xdf8
-  __DATA.__objc_ivar: 0xc4
-  __DATA.__objc_data: 0x500
-  __DATA.__data: 0x300
-  __DATA.__bss: 0x138
+  __DATA.__objc_const: 0x17f8
+  __DATA.__objc_selrefs: 0xdd0
+  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_data: 0x550
+  __DATA.__data: 0x3c0
+  __DATA.__bss: 0x120
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 89682DA5-DAA7-32D7-82FA-E5606AC9B309
-  Functions: 435
-  Symbols:   234
-  CStrings:  1678
+  UUID: D68E6718-1044-3096-925C-3FECFC68D74E
+  Functions: 334
+  Symbols:   233
+  CStrings:  1660
 
Symbols:
+ _GEOBatchDescription
+ _GEOConfigGetUint64
+ _GEOConfigSetUInteger
+ _GEOConfigSetUint64
+ _GEOGetApproximateTapewormIterations
+ _GEOInsertTapewormOnDispatchTimer
+ _GeoAnalyticsConfig_B74FC90_enabled
+ _GeoAnalyticsConfig_LocIntActiveBatchID
+ _GeoAnalyticsConfig_LocIntSeqNo
+ _GeoAnalyticsConfig__debug_simulateNoURLs
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_15MO_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_BATCH_TRAFFIC_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_LOC_INTEL_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_LOG_DISCARD_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_LONG_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_NAV_TRACE_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_NO_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_POI_BUSYNESS_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_PREDEX_TRAINING_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_PRESSURE_DATA_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_REALTIME_TRAFFIC_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_SHORT_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_STRN_HARVEST_holddownDurationInSec
+ _GeoAnalyticsSessionConfig_GEOAPAnalyticSessionType_WIFI_PROBE_holddownDurationInSec
+ _GeoServicesConfig_GeoanalyticsdTapewormEnabled
+ _GeoServicesConfig_GeoanalyticsdTapewormInstructionCount
+ _GeoServicesConfig_GeoanalyticsdTapewormTimerIntervalMs
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ _arc4random_uniform
+ _nw_context_copy_implicit_context
+ _nw_context_set_privacy_level
+ _objc_retain_x27
- OBJC_IVAR_$_GEOAPQueueElem._createTime
- OBJC_IVAR_$_GEOAPQueueElem._dirty
- _GEOBatchLogMessageType
- _GEOBatchOpaqueAppID
- _GEOMakeGEOAPBatchIDForReqRespMetadata
- _GEOMightHaveCorrespondingReqRespMetadata
- _GeoAnalyticsConfig_AnalyticsPipelineUploadHolddownTimeInSeconds
- _GeoAnalyticsConfig_MonthlyCountsAggregationLastRunTime
- _OBJC_CLASS_$_GEOAPDailyCountsQueueElem
- _OBJC_CLASS_$_GEOAPDailySettingsQueueElem
- _OBJC_CLASS_$_GEOAPDebugPersistence
- _OBJC_CLASS_$_GEOAPLogMsgQueueElem
- _OBJC_CLASS_$_GEOAPMonthlyCountsQueueElem
- _OBJC_CLASS_$_GEOAPPersistence
- _OBJC_CLASS_$_GEOAPQueueElem
- _OBJC_CLASS_$_GEOAPRRLogQueueElem
- _OBJC_CLASS_$_GEOAPStateFactory
- _OBJC_CLASS_$_GEOLogMsgEvent
- _OBJC_CLASS_$_GEOLogMsgState
- _OBJC_CLASS_$_GEORequestResponseMetadata
- _OBJC_CLASS_$_GEORequestResponseMetadataFile
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_METACLASS_$_GEOAPDailyCountsQueueElem
- _OBJC_METACLASS_$_GEOAPDailySettingsQueueElem
- _OBJC_METACLASS_$_GEOAPDebugPersistence
- _OBJC_METACLASS_$_GEOAPLogMsgQueueElem
- _OBJC_METACLASS_$_GEOAPMonthlyCountsQueueElem
- _OBJC_METACLASS_$_GEOAPPersistence
- _OBJC_METACLASS_$_GEOAPQueueElem
- _OBJC_METACLASS_$_GEOAPRRLogQueueElem
- ___NSArray0__struct
- _geo_userActionAndMetadataUploadType
- _objc_retain_x10
CStrings:
+ "%@ has nothing to upload now"
+ "%@ won't be ready for upload for %llu more seconds"
+ "%lu types are ready"
+ "(%@) %@ -- upload stage %lu:%@ for %@ ended in error"
+ "(%@) %@ had %llu expired records"
+ "(%@) %@ is using uploading policy type '%@' : %lu messages of size %lu with TTL %ld"
+ "(%@) URL task complete for %@"
+ "(%@) nothing to upload for %@"
+ "(%@) unable to create upload file writer for %@; unable to upload right now"
+ "(%@) unable to finalize and close upload file for %@; will try upload later"
+ "(%@) unable to write upload record for %@; stopping here"
+ "(%@) upload requested for %@"
+ "(%@) upload stage %lu:%@ %@ exhausted the remaining TTL"
+ "@\"<GEOAPConfigProviding>\""
+ "@\"<GEOAPTimeProviding>\""
+ "@\"GEOAPUploadHolddown\""
+ "@\"NSDate\"16@0:8"
+ "@32@0:8Q16@24"
+ "@appid"
+ "@rowid"
+ "@settings"
+ "@usagebool"
+ "@usagestring"
+ "AP.db-wal"
+ "APDB.db"
+ "B24@?0Q8Q16"
+ "B32@?0q8@\"NSData\"16Q24"
+ "B40@?0d8Q16Q24@\"NSData\"32"
+ "B48@?0q8Q16Q24Q32@\"NSData\"40"
+ "B52@?0q8i16@\"NSString\"20@\"NSString\"28@\"NSString\"36Q44"
+ "B56@0:8@16@24i32i36d40d48"
+ "CREATE TABLE IF NOT EXISTS Analytics (    rowid INTEGER PRIMARY KEY NOT NULL,    expiretime INT NOT NULL,    createtime INT NOT NULL,    batchid INT NOT NULL,    analytic BLOB NOT NULL    );"
+ "CREATE TABLE IF NOT EXISTS DailyCounts (    rowid INTEGER PRIMARY KEY NOT NULL,    type INT NOT NULL,    createtime INT NOT NULL,    appid TEXT,    usagestring TEXT,    usagebool TEXT    );"
+ "CREATE TABLE IF NOT EXISTS DailySettings (    rowid INTEGER PRIMARY KEY NOT NULL,    settings BLOB NOT NULL,    createtime INT NOT NULL    );"
+ "CREATE TABLE IF NOT EXISTS Shadow (    createtime REAL NOT NULL,    type INT NOT NULL,    batchid INT NOT NULL,    analytic BLOB NOT NULL    );"
+ "CountAnalytics"
+ "CountAnalytics: %@"
+ "DB"
+ "DELETE FROM Analytics    WHERE expiretime <= @expiretime;"
+ "DELETE FROM Analytics    WHERE rowid = @rowid;"
+ "DELETE FROM DailyCounts    WHERE rowid = @rowid;"
+ "DELETE FROM DailyCounts;"
+ "DELETE FROM DailySettings    WHERE rowid = @rowid;"
+ "DELETE FROM DailySettings;"
+ "DELETE FROM Shadow;"
+ "DeleteAllDailyCount"
+ "DeleteAllDailySettings"
+ "DeleteAllExpiredAnalytics"
+ "DeleteOneAnalytic"
+ "DeleteOneAnalytic: %@"
+ "DeleteOneDailyCount"
+ "DeleteOneDailyCount: %@"
+ "DeleteOneDailySettings"
+ "DeleteOneDailySettings: %@"
+ "DeleteShadowAnalytics"
+ "DepInjection"
+ "GEOAPConfigProviding"
+ "GEOAPDB"
+ "GEOAPTimeProviding"
+ "GEOAPUploadConfigProvider"
+ "GEOAPUploadHolddown"
+ "GEOAPUploadTimeProvider"
+ "INSERT OR REPLACE INTO Analytics    (expiretime, createtime, batchid, analytic)    VALUES (@expiretime, @createtime, @batchid, @analytic);"
+ "INSERT OR REPLACE INTO DailyCounts    (type, createtime, appid, usagestring, usagebool)    VALUES (@type, @createtime, @appid, @usagestring, @usagebool);"
+ "INSERT OR REPLACE INTO DailySettings    (settings, createtime)    VALUES (@settings, @createtime);"
+ "INSERT OR REPLACE INTO Shadow    (createtime, type, batchid, analytic)    VALUES (@createtime, @type, @batchid, @analytic);"
+ "InsertAnalytic"
+ "InsertAnalytic : %@"
+ "InsertDailyCount"
+ "InsertDailyCount: %@"
+ "InsertDailySetting"
+ "InsertDailySetting: %@"
+ "InsertShadow : %@"
+ "InsertShadowAnalytic"
+ "LOC_INTEL"
+ "MAPS_CARPLAY_DWELL_TIME_30_SEC"
+ "MAPS_CARPLAY_DWELL_TIME_3_SEC"
+ "MAP_EXPLORED_HZ"
+ "MAP_EXPLORED_LZ"
+ "N"
+ "NEARBY_SUGGESTION_SHARE"
+ "NEARBY_SUGGESTION_WRONG_LOCATION"
+ "No URL for %@; unable to upload right now"
+ "PUNCH_IN_WIDGET"
+ "Q20@0:8i16"
+ "RAND_DELAY"
+ "SELECT COUNT(*)    FROM Analytics;"
+ "SELECT batchUUID, strftime('%s',createTime),sessionType,eventCount,uploadSize,uploadPolicy,stageNum FROM uploadInflight;"
+ "SELECT batchid,    MIN(createtime) AS minCreateTime    FROM Analytics    GROUP BY batchid;"
+ "SELECT createtime, type, batchid, analytic    FROM Shadow    ORDER BY createtime ASC;"
+ "SELECT rowid, expiretime, createtime, batchid, analytic    FROM Analytics    WHERE batchid = @batchid;"
+ "SELECT rowid, settings, createtime    FROM DailySettings    ORDER BY createtime ASC;"
+ "SELECT rowid, type, appid, usagestring, usagebool, createtime    FROM DailyCounts    ORDER BY createtime ASC;"
+ "SelectAllShadowAnalytics"
+ "SelectAnalytic: %@"
+ "SelectAnalyticBatchIdsForUpload"
+ "SelectAnalyticBatchIdsForUpload : %@"
+ "SelectAnalyticWithBatchId"
+ "SelectDailyCounts"
+ "SelectDailyCounts: %@"
+ "SelectDailySettings"
+ "SelectDailySettingsInRange: %@"
+ "T@\"NSDate\",R,N"
+ "TEST"
+ "TQ,R,N"
+ "Td,R,N"
+ "Td,R,N,G_mustWait"
+ "VISITED_PLACES_INTERACTION"
+ "VISITED_PLACES_REVEAL"
+ "VISITED_PLACES_SHARE"
+ "VISITED_PLACES_WRONG_LOCATION"
+ "WATCH_GET_DIRECTIONS"
+ "Y"
+ "_activeLocIntelBatchID"
+ "_backoffExpireTime"
+ "_backoffIdx"
+ "_configProvider"
+ "_currentLocIntelSeqNo"
+ "_geo_setTLSMinimumSupportedProtocolVersion"
+ "_holddown"
+ "_mustWait"
+ "_sessionHolddownDurationForSessionType:"
+ "_setAllowsUCA:"
+ "_setLocIntSequenceNumberForBatch:inLogMsg:"
+ "_setup:"
+ "_startTaskForFile:taskDescription:analyticSessionType:apURLsessionConfigType:ttl:startDelay:"
+ "_startUploadTimerForDuration:"
+ "_timeProvider"
+ "analyticsCount"
+ "batchReadyInSeconds"
+ "bestReferenceTime"
+ "conditionMet"
+ "conditionUnmet"
+ "d24@0:8Q16"
+ "dateNow"
+ "dropAllTables"
+ "earliestBeginDate"
+ "holdDownDurationForBatch:"
+ "initWithQueueName:log:databaseFileURL:sqliteFlags:pragmas:setupBlock:"
+ "initWithTimeIntervalSinceNow:"
+ "initWithTimeProvider:configProvider:"
+ "internalInstall"
+ "isolationQueue"
+ "logMessageType"
+ "logMsgEvents"
+ "logMsgStates"
+ "maxDelay"
+ "mustWait"
+ "no URL for uploadTask '%@'"
+ "not now; holddown in effect"
+ "nothing available"
+ "pendingBatchesReadyForUpload"
+ "ready in %lld seconds"
+ "ready now"
+ "reportSQLiteErrorCode:method:error:"
+ "setEarliestBeginDate:"
+ "setSequenceNumber:"
+ "simulateNoURLs"
+ "step"
+ "timeNow"
+ "timer fired"
+ "timer set for %lld seconds"
+ "timer was cleared"
+ "unable to write %lu elements; over size limit"
+ "upload requested"
+ "uploadTask '%@' will not start before %@"
+ "usageBoolNumber:"
+ "usageBoolString:"
+ "userSession"
+ "v24@0:8d16"
- "%lu analytic types ready for upload"
- "(%@) URL task complete for batchId:%llu -- %@ / %@ / %u"
- "(%@) batchId %llu had %llu expired records"
- "(%@) batchId:%llu -- upload stage %lu:%@ for %@ ended in error"
- "(%@) nothing to upload for batchId %llu"
- "(%@) unable to create upload file writer for batch id %llu; unable to upload right now"
- "(%@) unable to finalize and close upload file for batchId %llu; will try upload later"
- "(%@) unable to write upload record for batch id %llu; stopping here"
- "(%@) upload batchId %llu is using uploading policy type '%@' : %lu messages of size %lu with TTL %ld"
- "(%@) upload requested for batch id %llu / message Type : %@, upload policy : %@, opaqueId : %u"
- "(%@) upload stage %lu:%@ for batchId %llu exhausted the remaining TTL"
- "-[GEOAPPersistence selectCountsWithQueryStmtKey:deleteStmtKey:visitorBlock:completionBlock:]"
- "-[GEOAPPersistence(Eval) showEvalDataWithVisitorBlock:]"
- "@app_id"
- "@count_type"
- "@fk_msgid"
- "@msgid"
- "@settings_data"
- "@usage_bool"
- "@usage_string"
- "Assertion failed: [db prepareStatement:FlushShadowSQL forKey:FlushShadowStmtKey]"
- "Assertion failed: [db prepareStatement:InsertShadowSQL forKey:InsertShadowStmtKey]"
- "Assertion failed: [db prepareStatement:ShowShadowSQL forKey:ShowShadowStmtKey]"
- "B16@?0@\"GEOAPMonthlyCountsQueueElem\"8"
- "B48@0:8@16@24i32i36d40"
- "BATCH_TRAFFIC_PROBE"
- "BGNonRepeatingSystemTaskRequest"
- "BGRepeatingSystemTaskRequest"
- "COHORTS_SESSION_USAGE"
- "CREATE TABLE IF NOT EXISTS analytics (msgid INTEGER PRIMARY KEY AUTOINCREMENT, createtime DATETIME DEFAULT CURRENT_TIMESTAMP, expiretime DATETIME, batchid INTEGER NOT NULL, analytic BLOB NOT NULL);"
- "CREATE TABLE IF NOT EXISTS dailycounts (msgid INTEGER PRIMARY KEY AUTOINCREMENT, count_type INT NOT NULL, app_id TEXT, usage_string TEXT, usage_bool BOOLEAN, createtime DATETIME );"
- "CREATE TABLE IF NOT EXISTS dailysettings (msgid INTEGER PRIMARY KEY AUTOINCREMENT, settings_data BLOB NOT NULL, createtime DATETIME NOT NULL );"
- "CREATE TABLE IF NOT EXISTS inflight (fk_msgid INTEGER PRIMARY KEY, up_time DATETIME DEFAULT CURRENT_TIMESTAMP );"
- "CREATE TABLE IF NOT EXISTS monthlycounts (msgid INTEGER PRIMARY KEY AUTOINCREMENT, count_type INT NOT NULL, app_id TEXT, usage_string TEXT, usage_bool BOOLEAN, createtime DATETIME );"
- "CREATE TABLE IF NOT EXISTS shadow (analytic BLOB NOT NULL, COL_TYPE INT NOT NULL, createtime DATETIME DEFAULT CURRENT_TIMESTAMP );"
- "CURATED_COLLECTION_SESSION"
- "DEBUGLOG"
- "DELETE FROM analytics WHERE batchid = @batchid AND msgid IN (SELECT fk_msgid FROM inflight);"
- "DELETE FROM analytics WHERE expiretime <=  DATETIME( @expiretime, 'UNIXEPOCH')  AND batchid = @batchid;"
- "DELETE FROM analytics;"
- "DELETE FROM dailycounts WHERE msgid <= @msgid;"
- "DELETE FROM dailysettings WHERE msgid <= @msgid;"
- "DELETE FROM inflight WHERE fk_msgid NOT IN (SELECT msgid FROM analytics);"
- "DELETE FROM monthlycounts WHERE msgid <= @msgid;"
- "DELETE FROM shadow;"
- "DROP TABLE analytics;"
- "DROP TABLE dailycounts;"
- "DROP TABLE dailysettings;"
- "DROP TABLE inflight;"
- "DROP TABLE monthlycounts;"
- "DROP TABLE shadow;"
- "FIFTEEN_MONTH_SESSION"
- "FIFTEEN_MONTH_USER_SESSION"
- "GEOAPMonthlyCountsQueueElem"
- "GEOAPPersistence"
- "GEOAPRRLogQueueElem"
- "INSERT INTO analytics (batchid,expiretime,analytic)VALUES (@batchid, DATETIME( @expiretime, 'UNIXEPOCH') ,@analytic);"
- "INSERT INTO dailycounts (count_type,app_id,createtime,usage_string,usage_bool) VALUES (@count_type,@app_id, DATETIME( @createtime, 'UNIXEPOCH'), @usage_string,@usage_bool );"
- "INSERT INTO dailysettings (settings_data, createtime) VALUES (@settings_data, DATETIME( @createtime, 'UNIXEPOCH') );"
- "INSERT INTO inflight (fk_msgid) VALUES (@fk_msgid);"
- "INSERT INTO monthlycounts (count_type,app_id,createtime,usage_string,usage_bool) VALUES (@count_type,@app_id, DATETIME( @createtime, 'UNIXEPOCH'), @usage_string,@usage_bool );"
- "INSERT INTO shadow (analytic,COL_TYPE,createtime) VALUES ( @analytic,@type, DATETIME( @createtime, 'UNIXEPOCH', 'SUBSEC'))"
- "LOG_DISCARD_EVENT"
- "LOG_MESSAGE_TYPE_UNKNOWN"
- "LONG_SESSION_LOG_FRAMEWORK_USAGE"
- "LONG_SESSION_USAGE"
- "MonthlyAggregation"
- "NAVIGATION_TRACE"
- "NETWORK_SELECTION_HARVEST_SESSION"
- "No URL for batch id %llu; unable to upload right now"
- "PERFORMANCE"
- "POI_BUSYNESS_DATA_SESSION"
- "PRESSURE_DATA_SESSION"
- "Persistence"
- "REALTIME_TRAFFIC_PROBE"
- "SELECT COUNT(1) FROM analytics;"
- "SELECT DISTINCT batchid FROM analytics;"
- "SELECT analytic,COL_TYPE, strftime('%s',createtime, 'SUBSEC' ) FROM shadow;"
- "SELECT batchUUID,createTime,sessionType,eventCount,uploadSize,uploadPolicy,stageNum FROM uploadInflight;"
- "SELECT batchid FROM analytics WHERE batchid NOT IN ( SELECT batchid FROM analytics,inflight WHERE msgid = fk_msgid GROUP BY batchid)GROUP BY batchid;"
- "SELECT changes();"
- "SELECT msgid, settings_data, strftime('%s',createtime) FROM dailysettings;"
- "SELECT msgid,batchid,analytic, strftime('%s',expiretime), strftime('%s',createtime) FROM analytics WHERE msgid NOT IN ( SELECT fk_msgid FROM inflight)  AND batchid = @batchid;"
- "SELECT msgid,count_type, app_id, usage_string, usage_bool, strftime('%s',createtime) FROM dailycounts;"
- "SELECT msgid,count_type, app_id, usage_string, usage_bool, strftime('%s',createtime) FROM monthlycounts;"
- "SESSIONLESS_USAGE"
- "SHORT_SESSION_USAGE"
- "T@\"NSData\",R,N,V_rrLogData"
- "TELEMETRY"
- "USAGE"
- "WIFI_CONNECTION_QUALITY_PROBE_COLLECTION"
- "_initiateCollationAndUpload"
- "_lastMonthlyAggregation"
- "_rrLogData"
- "_setupEvalStmtsOnDb:"
- "_startTaskForFile:taskDescription:analyticSessionType:apURLsessionConfigType:ttl:"
- "_startUploadTimer"
- "_writeDailyCountElem:withStmtKey:"
- "_writeMonthlyCountElem:"
- "_writeRRLogElem:"
- "addLogMsgEvent:"
- "addLogMsgState:"
- "aggregateMonthlyCountsAndReportFrom:until:"
- "aggregateMonthlyUsageCountsAndReportFrom:until:"
- "analytics upload timer fired"
- "availB"
- "batch id %llu has nothing to upload now"
- "bindNullParameter:inStatement:error:"
- "chng"
- "cleanB"
- "clearAllData"
- "clearPendingLogMsgElemsForBatchUploadWithBatchId:"
- "collectionTime"
- "completed monthly"
- "data type %lld"
- "date"
- "dateWithTimeIntervalSince1970:"
- "delBP"
- "delDC"
- "delDS"
- "delMC"
- "delX"
- "eventMetadata"
- "executeSync"
- "executeTransaction"
- "finished monthly aggregation from %{private}@ until %{private}@"
- "first class upgrade; batchId %{private}llu is now %{private}llu"
- "flush"
- "fuzzMonthlyCount:forDailyUsageType:"
- "initWithData:createTime:"
- "insA"
- "insDC"
- "insDS"
- "insI"
- "insMC"
- "insS"
- "next agg at %@"
- "nextBP"
- "nothing available for upload"
- "nuke"
- "numberWithLongLong:"
- "populateCommonEventValues:"
- "processed %u Monthly Usage counts; dropped %u counts"
- "q16@0:8"
- "qryDC"
- "qryDS"
- "qryMC"
- "requestResponseMetadataFileDescriptorForBatchID:"
- "retrieveLastMonthlyAggregationTime"
- "rrLogData"
- "saveLastMonthlyAggregationTime:"
- "select elem with create time %@"
- "selectBatchIdsForBatchUpload"
- "selectCountsWithQueryStmtKey:deleteStmtKey:visitorBlock:completionBlock:"
- "selectMonthlyCountsWithVisitorBlock:completionBlock:"
- "setLogMessageType:"
- "setOffline:"
- "setServiceMetadata:"
- "setStateType:"
- "setUserSession:"
- "sfd"
- "sharedFactory"
- "show"
- "showEvalDataWithVisitorBlock: done"
- "startMonthlyAggregationFromTime:"
- "started monthly at %@"
- "starting monthly aggregation from %{private}@ until %{private}@"
- "starting monthly usage counts aggregation up until %{private}@"
- "stateForType:"
- "stateOffline"
- "stateUserSession"
- "stmtforkey %p"
- "storing Monthly Usage action '%@'"
- "storing analytic of type %@ (%{private}u)"
- "unsafe_readReqRespMetadataWithVisitorBlock:"
- "upload holddown timer set to fire in %lld seconds"
- "upload holddown timer was cleared"
- "v48@0:8@16@24@?32@?40"
- "writing monthly elem : %@"

```
