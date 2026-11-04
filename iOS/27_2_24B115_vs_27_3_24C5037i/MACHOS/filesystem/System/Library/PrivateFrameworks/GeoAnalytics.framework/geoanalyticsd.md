## geoanalyticsd

> `/System/Library/PrivateFrameworks/GeoAnalytics.framework/geoanalyticsd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protorefs`

```diff

-2076.31.9.18.8
-  __TEXT.__text: 0x21d74
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_stubs: 0x3680
-  __TEXT.__objc_methlist: 0xe9c
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x4f4
-  __TEXT.__cstring: 0xdbe1
-  __TEXT.__objc_methname: 0x3085
-  __TEXT.__objc_classname: 0x2c3
-  __TEXT.__objc_methtype: 0xc16
-  __TEXT.__oslogstring: 0x1241
-  __TEXT.__unwind_info: 0x7b0
-  __DATA_CONST.__const: 0x1108
-  __DATA_CONST.__cfstring: 0x128e0
-  __DATA_CONST.__objc_classlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x50
+2076.32.9.18.5
+  __TEXT.__text: 0x2a23c
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_stubs: 0x41a0
+  __TEXT.__objc_methlist: 0x1624
+  __TEXT.__const: 0x168
+  __TEXT.__gcc_except_tab: 0x690
+  __TEXT.__cstring: 0xe825
+  __TEXT.__objc_methname: 0x3c09
+  __TEXT.__objc_classname: 0x642
+  __TEXT.__objc_methtype: 0x1097
+  __TEXT.__oslogstring: 0x1f5e
+  __TEXT.__unwind_info: 0xa78
+  __DATA_CONST.__const: 0x1518
+  __DATA_CONST.__cfstring: 0x12dc0
+  __DATA_CONST.__objc_classlist: 0x130
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__auth_got: 0x438
-  __DATA_CONST.__got: 0x2d0
-  __DATA.__objc_const: 0x1c38
-  __DATA.__objc_selrefs: 0xf28
-  __DATA.__objc_ivar: 0xf8
-  __DATA.__objc_data: 0x690
-  __DATA.__data: 0x3c0
+  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x378
+  __DATA.__objc_const: 0x33c8
+  __DATA.__objc_selrefs: 0x1208
+  __DATA.__objc_ivar: 0x184
+  __DATA.__objc_data: 0xbe0
+  __DATA.__data: 0x6c0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 402
-  Symbols:   244
-  CStrings:  3356
+  Functions: 561
+  Symbols:   272
+  CStrings:  3683
 
Symbols:
+ _GEOConfigGetArray
+ _GEOErrorDomain
+ _GeoAnalyticsConfig_AllowedAggregatorMetrics
+ _GeoAnalyticsConfig_DailySettingsAggregationInterval
+ _GeoAnalyticsConfig_DailySettingsAggregationLastRunTime
+ _GeoAnalyticsConfig_ShortSessionCountsDisabled
+ _GeoAnalyticsConfig_ShortSessionHarvestMaxAge
+ _GeoAnalyticsConfig_ShortSessionHarvestMinAge
+ _GeoAnalyticsConfig_ShortSessionHarvestRetryDelay
+ _GeoAnalyticsConfig_ShortSessionOSVersionDenyList
+ _GeoAnalyticsConfig_ShortSessionSignalAggregationInterval
+ _GeoAnalyticsConfig_ShortSessionSignalAggregationLastRunTime
+ _GeoAnalyticsConfig__debug_DisableSessionHarvestJitter
+ _NSPOSIXErrorDomain
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_GEODynamicDailyCountsFetchReply
+ _OBJC_CLASS_$_GEODynamicDailyCountsFetchRequest
+ _OBJC_CLASS_$_GEODynamicDailyCountsRequest
+ _OBJC_CLASS_$_GEODynamicDailyCountsResponse
+ _OBJC_CLASS_$_GEODynamicDailyUseSummaryUseEvent
+ _OBJC_CLASS_$_GEOUserSession
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSSet
+ _arc4random
+ _dispatch_source_cancel
+ _log2
+ _objc_opt_respondsToSelector
+ _objc_retain_x7
CStrings:
+ "-[GEOAPDaemonManagerBridge flushShortSessionDataWithCompletion:]"
+ "-[GEOAPDaemonManagerBridge reportLogMsg:uploadBatchId:sessionId:logMessageType:applicationID:completion:]"
+ "-[GEOAPDaemonManagerBridge reportSessionSeen:logMessageType:applicationID:createTime:readyTime:completion:]"
+ "-[GEOAPDaemonManagerBridge runAggregationTasks:lastAggregationDate:]"
+ "-[GEOAPServiceLocal reportLogMsg:uploadBatchId:sessionId:logMessageType:applicationID:completion:]"
+ "@\"<GEOAPDailySettingsAggregatorConfigProviding>\""
+ "@\"<GEOAPDynamicCountsAggregatorConfigProviding>\""
+ "@\"<GEOAPDynamicDailyUseSummaryCapturing>\""
+ "@\"<GEOAPPeriodicSettingsCapturing>\""
+ "@\"<GEOAPSessionSignalResolving>\""
+ "@\"<GEOAPSessionSignalsHarvesting>\""
+ "@\"<GEOAPShortSessionHarvestConfigProviding>\""
+ "@\"<GEOAPUserSessionProviding>\""
+ "@\"GEOAPDB\""
+ "@\"NSArray\"16@0:8"
+ "@\"NSMutableDictionary\""
+ "@\"NSUUID\""
+ "@48@0:8@16@24@32@40"
+ "@48@0:8q16@24@32@40"
+ "@52@0:8@16i24@28@36@44"
+ "@56@0:8@16@24@32@40@48"
+ "@applicationid"
+ "@logmessagetype"
+ "@readytime"
+ "@servercountsdata"
+ "@sessioncreatetime"
+ "@sessionid"
+ "ACSN_FINDER_USAGE"
+ "AllowedAggregatorMetrics has %lu entries; truncating to 16"
+ "B16@?0@\"GEOAPShortSessionSignalQueueElem\"8"
+ "B16@?0Q8"
+ "B24@0:8@?16"
+ "B24@0:8^@16"
+ "B32@0:8I16I20@24"
+ "B32@?0@\"NSUUID\"8@\"NSDate\"16^B24"
+ "B40@?0q8@\"NSUUID\"16Q24@\"NSData\"32"
+ "B44@?0@\"NSUUID\"8Q16Q24i32@\"NSString\"36"
+ "B52@0:8@16@24@32i40@44"
+ "BATCH_TRAFFIC_PROBE"
+ "COHORTS_SESSION_USAGE"
+ "CREATE TABLE IF NOT EXISTS SessionsSeen (    sessionid BLOB NOT NULL,    createtime INT NOT NULL,    readytime INT NOT NULL,    logmessagetype INT NOT NULL,    applicationid TEXT,    UNIQUE(sessionid)    ON CONFLICT IGNORE    );"
+ "CREATE TABLE IF NOT EXISTS ShortSessionSignals (    rowid INTEGER PRIMARY KEY NOT NULL,    sessionid BLOB NOT NULL,    sessioncreatetime INT NOT NULL,    servercountsdata BLOB NOT NULL    );"
+ "CURATED_COLLECTION_SESSION"
+ "CountSessionsSeen"
+ "CountSessionsSeen: %@"
+ "CountShortSessionSignals"
+ "DEBUGLOG"
+ "DELETE FROM SessionsSeen    WHERE sessionid = @sessionid;"
+ "DELETE FROM SessionsSeen;"
+ "DELETE FROM ShortSessionSignals    WHERE rowid = @rowid;"
+ "DELETE FROM ShortSessionSignals;"
+ "DYNAMIC_DAILY_USE_SUMMARY"
+ "DeleteAllSessionsSeen"
+ "DeleteAllSessionsSeen: %@"
+ "DeleteAllShortSessionSignals"
+ "DeleteAllShortSessionSignals: %@"
+ "DeleteOneShortSessionSignal"
+ "DeleteOneShortSessionSignal: %@"
+ "DeleteSessionSeen"
+ "DeleteSessionSeen: %@"
+ "EQ_DATA_SESSSION"
+ "FIFTEEN_MONTH_SESSION"
+ "FIFTEEN_MONTH_USER_SESSION"
+ "GEOAPDailySettingsAggregator"
+ "GEOAPDailySettingsAggregatorConfigProvider"
+ "GEOAPDailySettingsAggregatorConfigProviding"
+ "GEOAPDailySettingsAggregatorTimeProvider"
+ "GEOAPDynamicCountsAggregator"
+ "GEOAPDynamicCountsAggregatorConfigProvider"
+ "GEOAPDynamicCountsAggregatorConfigProviding"
+ "GEOAPDynamicCountsAggregatorEvalConfigProvider"
+ "GEOAPDynamicCountsAggregatorTimeProvider"
+ "GEOAPDynamicDailyUseSummaryCapturing"
+ "GEOAPPeriodicSettingsCapturing"
+ "GEOAPPortalPeriodicSettingsCapturer"
+ "GEOAPSessionCountPrivacyHandler"
+ "GEOAPSessionSignalResolving"
+ "GEOAPSessionSignalResolvingErrorDomain"
+ "GEOAPSessionSignalsHarvester"
+ "GEOAPSessionSignalsHarvesterConfigProvider"
+ "GEOAPSessionSignalsHarvesterServiceResolver"
+ "GEOAPSessionSignalsHarvesterTimeProvider"
+ "GEOAPSessionSignalsHarvesting"
+ "GEOAPShortSessionHarvestConfigProviding"
+ "GEOAPShortSessionQueueElem"
+ "GEOAPShortSessionSignalCapturer"
+ "GEOAPShortSessionSignalQueueElem"
+ "GEOAPUserSessionProvider"
+ "GEOAPUserSessionProviding"
+ "INSERT INTO SessionsSeen    (sessionid, createtime, readytime, logmessagetype, applicationid)    VALUES (@sessionid, @createtime, @readytime, @logmessagetype, @applicationid);"
+ "INSERT OR REPLACE INTO ShortSessionSignals    (sessionid, sessioncreatetime, servercountsdata)    VALUES (@sessionid, @sessioncreatetime, @servercountsdata);"
+ "InsertShortSessionSignal"
+ "InsertShortSessionSignal: %@"
+ "LOG_DISCARD_EVENT"
+ "LOG_MESSAGE_TYPE_UNKNOWN"
+ "LONG_SESSION_LOG_FRAMEWORK_USAGE"
+ "LONG_SESSION_USAGE"
+ "MADSession"
+ "MEDIUM_SESSION_USAGE"
+ "NAVIGATION_TRACE"
+ "NETWORK_SELECTION_HARVEST_SESSION"
+ "OS version %{public}@ is denylisted; skipping session signal aggregation"
+ "OS version %{public}@ is denylisted; skipping session signal harvesting"
+ "PERFORMANCE"
+ "POI_BUSYNESS_DATA_SESSION"
+ "PRESSURE_DATA_SESSION"
+ "REALTIME_TRAFFIC_PROBE"
+ "RecordSessionSeen"
+ "RecordSessionSeen: %@"
+ "SELECT COUNT(*)    FROM SessionsSeen;"
+ "SELECT COUNT(*)    FROM ShortSessionSignals;"
+ "SELECT createtime    FROM SessionsSeen    ORDER BY createtime ASC    LIMIT 1;"
+ "SELECT rowid, sessionid, sessioncreatetime, servercountsdata    FROM ShortSessionSignals    ORDER BY sessioncreatetime ASC;"
+ "SELECT sessionid, createtime, readytime, logmessagetype, applicationid    FROM SessionsSeen    ORDER BY readytime ASC    LIMIT 1;"
+ "SESSIONLESS_USAGE"
+ "SHORT_SESSION_USAGE"
+ "SelectOldestSessionSeen"
+ "SelectOldestSessionSeen: %@"
+ "SelectOldestSessionSeenCreateTime"
+ "SelectOldestSessionSeenCreateTime: %@"
+ "SelectShortSessionSignals"
+ "SelectShortSessionSignals: %@"
+ "SessionCountPrivacyHandler"
+ "SessionSignalsHarvester"
+ "SignalAggregation"
+ "SignalAggregator"
+ "T@\"NSArray\",R,N"
+ "T@\"NSData\",R,N,V_serverCountsResponseData"
+ "T@\"NSDate\",&,N"
+ "T@\"NSDate\",R,N,V_readyTime"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_applicationID"
+ "T@\"NSUUID\",R,N,V_sessionID"
+ "TELEMETRY"
+ "Ti,R,N,V_logMessageType"
+ "Tq,R,N,V_rowid"
+ "UPDATE SessionsSeen    SET readytime = @readytime    WHERE sessionid = @sessionid;"
+ "USAGE"
+ "UUIDForColumn:inStatment:"
+ "UpdateSessionSeenReadyTime"
+ "UpdateSessionSeenReadyTime: %@"
+ "WIFI_CONNECTION_QUALITY_PROBE_COLLECTION"
+ "_aggregateWindowAfterDate:"
+ "_aggregationInterval"
+ "_allShortSessionsHarvestedBefore:"
+ "_applicationID"
+ "_capturer"
+ "_countsByMetric"
+ "_finalized"
+ "_harvestKicker"
+ "_harvestNextOnQueue"
+ "_harvestRunning"
+ "_isFirstSightingOfSession:"
+ "_lastAggTime"
+ "_logMessageType"
+ "_loggedSessionIDs"
+ "_loggedSessionIDsLastPurge"
+ "_loggedSessionIDsLock"
+ "_maxAge"
+ "_nextAggregationTimeAfterDate:"
+ "_privacyConformant"
+ "_processSessionID:createTime:readyTime:logMessageType:applicationID:"
+ "_queue"
+ "_readyTime"
+ "_reportFrom:until:"
+ "_reportSessionID:createTime:logMessageType:applicationID:"
+ "_resolver"
+ "_retryTimer"
+ "_rowid"
+ "_scheduleRetryAfter:"
+ "_serverCountsResponseData"
+ "_sessionID"
+ "_taintedMetrics"
+ "_treatmentsByMetric"
+ "_userSessionProvider"
+ "_writeShortSessionElem:"
+ "addMetric:count:treatments:"
+ "aggregateShortSessionSignalsAndReportFrom:until:"
+ "aggregation not ready; waiting on other session's signals"
+ "aggregation successful; processed %u signals; dropped %u"
+ "aggregationInterval"
+ "allKeys"
+ "allObjects"
+ "allowedMetrics"
+ "applicationID"
+ "applying bit max of %u"
+ "attempting signal harvest"
+ "bindUUIDParameter:toValue:inStatement:error:"
+ "bit usage %u exceeds bit max of %u"
+ "captureDynamicDailyUseSummaryWithUseEvents:summaryDate:aggregationSummaryDate:user_mapsUseLastDate:"
+ "com.apple.geo.analytics.loggedsessionids"
+ "com.apple.geo.analytics.sessionharvester"
+ "containsObject:"
+ "countsDisabled"
+ "current 15mo session is excluded from server counts; skipping dynamic daily use summary capture"
+ "daily settings aggregation already running; done"
+ "deleteSessionSeen:"
+ "deleteSessionSeenOnQueue:"
+ "dropping metric %u; differing treatments received"
+ "dropping metric %u; not in the allowed set"
+ "dynamic daily use summary will not be captured"
+ "empty signal set for today; dynamic daily use summary will not be captured"
+ "enumerateMetricsWithVisitorBlock:"
+ "error"
+ "exclude15MoSessionFromServerCounts"
+ "finalize"
+ "finished daily settings aggregation"
+ "finished eval mode daily settings aggregation"
+ "finished short session signal aggregation"
+ "flushShortSessionData:"
+ "flushShortSessionDataWithCompletion:"
+ "getUUIDBytes:"
+ "hardwareIdentifier"
+ "harvest already running; done"
+ "harvestNext"
+ "hasMaxValue"
+ "hasMinValue"
+ "initWithConfigProvider:db:timeProvider:capturer:"
+ "initWithConfigProvider:userSessionProvider:db:timeProvider:capturer:"
+ "initWithDBFilePath:harvestKicker:"
+ "initWithLastAggTime:"
+ "initWithResolver:"
+ "initWithResolver:db:timeProvider:configProvider:"
+ "initWithRowid:sessionID:createTime:serverCountsResponseData:"
+ "initWithSessionID:logMessageType:applicationID:createTime:readyTime:"
+ "initWithTraits:auditToken:throttleToken:"
+ "isEqualToArray:"
+ "isSessionCountsDisabledInCountry:"
+ "jitterDisabled"
+ "keysOfEntriesPassingTest:"
+ "lastAggregationTime"
+ "maxAge"
+ "maxValue"
+ "metric"
+ "metric %u applying MAX of %u"
+ "metric %u applying MIN of %u"
+ "metric %u applying privacy treatments"
+ "metric %u applying subtractive noise w/ probability %05.4f"
+ "metric %u count is now %u"
+ "metric %u dropped; count %u is below min %u"
+ "metric %u dropping; min %u exceeds max %u"
+ "metric %u final count %u; used %u bits"
+ "metric %u max set to %u"
+ "metric %u min set to %u"
+ "metric %u subtractive noise probability set to %f"
+ "metric %u subtractive noise removed %u of %u counts"
+ "metricCount"
+ "metricTreatments"
+ "metrics"
+ "minValue"
+ "missing required entitlement"
+ "no more short sessions to harvest"
+ "oldestSessionSeenCreateTime"
+ "osVersion"
+ "osVersionDenyList"
+ "privacy compliant"
+ "processing session signals was unsuccessful"
+ "readyTime"
+ "recordShortSessionSignals:forSessionID:sessionCreateTime:"
+ "removeObjectsForKeys:"
+ "reportLogMsg:uploadBatchId:sessionId:logMessageType:applicationID:completion:"
+ "reportSessionSeen:date:logMessageType:applicationID:completion:"
+ "reportSessionSeen:logMessageType:applicationID:createTime:readyTime:completion:"
+ "response"
+ "retryDelay"
+ "runAggregationTasks:lastAggregationDate:"
+ "runEvalAggregationWithLastAggregationDate:"
+ "running eval aggregation"
+ "selectOldestSessionSeenWithVisitorBlock:"
+ "selectShortSessionSignalsWithVisitorBlock:completionBlock:"
+ "send:withReply:handler:"
+ "serverCountsResponseData"
+ "session %{public}@ aggregating signals"
+ "session %{public}@ check if ready (age %.0fs, readyTime %{public}@)"
+ "session %{public}@ current 15mo session has opted out of dynamic counts; not recording signals"
+ "session %{public}@ dropping; retry delay would exceed max age"
+ "session %{public}@ dropping; server has no data and none is forthcoming"
+ "session %{public}@ entered MAD processing (type %{public}@, readyTime %{public}@)"
+ "session %{public}@ expired; age %.0fs exceeds max %.0fs"
+ "session %{public}@ not ready; retrying in %.0fs"
+ "session %{public}@ ready; will request svc for metrics"
+ "session %{public}@ received empty signal list"
+ "session %{public}@ received exception: %{public}@"
+ "session %{public}@ received signal list"
+ "session %{public}@ requesting signals"
+ "session %{public}@ storing signals"
+ "session %{public}@ will retry in %.0fs, at %{public}@"
+ "session signal aggregation is disabled by config; skipping"
+ "session signal aggregation is disabled in country %{private}@; skipping"
+ "session signal harvesting is disabled by config; skipping"
+ "session signal harvesting is disabled in country %{private}@; skipping"
+ "sessionID"
+ "sessionsSeenCount"
+ "set"
+ "setDate:"
+ "setHwModel:"
+ "setIsInternalInstall:"
+ "setLastAggregationTime:"
+ "setOsVersion:"
+ "setRequest:"
+ "setRequestUUID:"
+ "setSessionId:"
+ "setSessionType:"
+ "setWithArray:"
+ "sharedHarvester"
+ "starting Daily Settings report from %{private}@ until %{private}@"
+ "starting daily settings aggregation"
+ "starting eval mode daily settings aggregation"
+ "starting session signal aggregation from %{private}@ until %{private}@"
+ "starting short session signal aggregation"
+ "subarrayWithRange:"
+ "subtractiveNoiseP"
+ "tainting metric %u; treatments changed since it was last seen"
+ "treatmentType"
+ "updateSessionSeen:readyTime:"
+ "v16@?0I8I12"
+ "v24@0:8@\"NSDate\"16"
+ "v24@?0@\"<GEOXPCReply>\"8@\"NSError\"16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v32@0:8Q16@\"NSDate\"24"
+ "v32@0:8Q16@24"
+ "v44@0:8@16@24i32@36"
+ "v44@?0@\"NSUUID\"8@\"NSDate\"16@\"NSDate\"24i32@\"NSString\"36"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSNumber\"40"
+ "v48@0:8@16@24@32@40"
+ "v52@0:8@\"NSUUID\"16@\"NSDate\"24i32@\"NSString\"36@?<v@?@\"NSData\"@\"NSError\">44"
+ "v52@0:8@16@24i32@36@?44"
+ "v60@0:8@\"NSData\"16Q24@\"NSUUID\"32i40@\"NSString\"44@?<v@?>52"
+ "v60@0:8@\"NSUUID\"16i24@\"NSString\"28@\"NSDate\"36@\"NSDate\"44@?<v@?@\"NSError\">52"
+ "v60@0:8@16Q24@32i40@44@?52"
+ "v60@0:8@16i24@28@36@44@?52"
+ "v64@0:8@\"GEOLogMsgStateMapSettings\"16@\"GEOLogMsgStateMapUIShown\"24@\"GEOLogMsgStateMapsFeatures\"32@\"GEOLogMsgStateMapsUserSettings\"40@\"GEOLogMsgStateRoutingSettings\"48@\"GEOLogMsgStateWidgetConfiguration\"56"
+ "v64@0:8@16@24@32@40@48@56"
+ "will process session %{public}@"
+ "window ending %{private}@ not ready; a short session from that window (or earlier) is still pending harvest"
- "-[GEOAPDaemonManagerBridge reportLogMsg:uploadBatchId:completion:]"
- "-[GEOAPDaemonManagerBridge runAggregationTasks]"
- "-[GEOAPServiceLocal reportLogMsg:uploadBatchId:completion:]"
- "reportDailySettingsFrom:until:"
- "reportLogMsg:uploadBatchId:completion:"
- "starting Daily Settings report"
- "v40@0:8@\"NSData\"16Q24@?<v@?>32"
- "v40@0:8@16Q24@?32"
```
