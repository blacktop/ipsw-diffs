## GeoAnalytics

> `/System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics`

```diff

-1986.33.11.14.4
-  __TEXT.__text: 0xa00f8
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x1a8c
-  __TEXT.__const: 0x620
-  __TEXT.__gcc_except_tab: 0x510
-  __TEXT.__cstring: 0xfd19
-  __TEXT.__oslogstring: 0xccc
+1986.34.9.12.31
+  __TEXT.__text: 0xa9b54
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_methlist: 0x1eac
+  __TEXT.__const: 0x628
   __TEXT.__dlopen_cstrs: 0x126
-  __TEXT.__unwind_info: 0xe80
-  __TEXT.__objc_classname: 0x34a
-  __TEXT.__objc_methname: 0x1161c
-  __TEXT.__objc_methtype: 0x1973
-  __TEXT.__objc_stubs: 0xd5a0
-  __DATA_CONST.__got: 0x640
-  __DATA_CONST.__const: 0x5020
-  __DATA_CONST.__objc_classlist: 0xb8
+  __TEXT.__gcc_except_tab: 0x50c
+  __TEXT.__cstring: 0x1034f
+  __TEXT.__oslogstring: 0xf29
+  __TEXT.__unwind_info: 0xe90
+  __TEXT.__objc_classname: 0x392
+  __TEXT.__objc_methname: 0x11a26
+  __TEXT.__objc_methtype: 0x19cb
+  __TEXT.__objc_stubs: 0xd860
+  __DATA_CONST.__got: 0x648
+  __DATA_CONST.__const: 0x51c8
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ba8
+  __DATA_CONST.__objc_selrefs: 0x3d18
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__objc_arraydata: 0x778
-  __AUTH_CONST.__auth_got: 0x430
-  __AUTH_CONST.__const: 0x3160
-  __AUTH_CONST.__cfstring: 0x12c00
-  __AUTH_CONST.__objc_const: 0x21a0
+  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_arraydata: 0x7c0
+  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__const: 0x3260
+  __AUTH_CONST.__cfstring: 0x13680
+  __AUTH_CONST.__objc_const: 0x1ec8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_intobj: 0x10f8
-  __AUTH_CONST.__objc_arrayobj: 0x270
+  __AUTH_CONST.__objc_intobj: 0x11a0
+  __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x398
-  __AUTH.__objc_data: 0x50
+  __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0xec
-  __DATA.__data: 0x15c0
+  __DATA.__data: 0x15f0
   __DATA.__bss: 0x18
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_ivar: 0x4c
+  __DATA_DIRTY.__objc_ivar: 0x54
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x3e0
+  __DATA_DIRTY.__bss: 0x400
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1451
-  Symbols:   2027
-  CStrings:  4871
+  Functions: 1418
+  Symbols:   2070
+  CStrings:  5018
 
Symbols:
+ _GEOConfigSetDouble
+ _GeoAnalyticsConfig_GetConfigStoreStringKeysForWatchSync
+ _GeoAnalyticsConfig_GetUserDefaultStringKeysForWatchSync
+ _GeoAnalyticsConfig_WebPlaceCardStates
+ _GeoAnalyticsConfig_WebPlaceCardUploadPolicy
+ _GeoAnalyticsUserActionConfig_MapViewEngagement_dropRate
+ _OBJC_CLASS_$_GEOAPWebPortal
+ _OBJC_CLASS_$_GEOUserAccountInfo
+ _OBJC_METACLASS_$_GEOAPWebPortal
+ _objc_setProperty_nonatomic_copy
CStrings:
+ "\x01\""
+ "\x02"
+ "'WebPlaceCardStates' has unexpected entry; must drop it"
+ "'WebPlaceCardUploadPolicy' value '%@' is invalid ; using GEOAPUploadPolicyType_UP_POLICY_00"
+ "(%@) state '%@' aborts on input pair"
+ "(%@) state '%@' fulfilled on input pair"
+ "(%@) state '%@' fulfilled wait time"
+ "(%@) state '%@' is holding"
+ "(%@) state '%@' is processing (%@, %@)"
+ "(%@) state '%@' timed out"
+ "(%@) state '%@' will excute fulfillment block"
+ "+[GEOAPPortal(UserActionCodeGen) captureMapViewEngagementWithAction:target:value:moduleType:moduleMetadata:richProviderId:additionalStates:providedDropRate:completionQueue:completionBlock:]"
+ "/System/AppleInternal/Library/Frameworks/CoreAnalytics.framework/CoreAnalytics"
+ "/System/AppleInternal/Library/Frameworks/GeoShifter.framework/GeoShifter"
+ "15MO"
+ "30s dwell"
+ "30s dwell achieved"
+ "30s wait"
+ "3s dwell achieved"
+ "3s engagement"
+ "3s wait"
+ "@28@0:8@16B24"
+ "@32@0:8@16i24i28"
+ "@?16@0:8"
+ "ACCOUNT"
+ "ACTION_BUTTON_DETAILS"
+ "APPLICATION_IDENTIFIER"
+ "Assertion failed: _completionBlock != ((void*)0)"
+ "Assertion failed: _historyVisitorBlock != ((void*)0)"
+ "Assertion failed: _inflightVisitorBlock != ((void*)0)"
+ "B24@0:8d16"
+ "BATCH_TRAFFIC"
+ "CAR_PLAY"
+ "COHORT"
+ "CURATED_COLLECTION"
+ "DAEMON_PARTY_MAP_VIEW"
+ "DETAIL_LOOK_AROUND_LOG"
+ "DEVICE_BASE"
+ "DEVICE_CONNECTION"
+ "DEVICE_IDENTIFIER"
+ "DEVICE_LOCALE"
+ "DEVICE_SETTINGS"
+ "DIRECTIONS_DETAIL"
+ "ELEMENT_IMPRESSION"
+ "EXPERIMENTS"
+ "EXTENSION"
+ "FIRST_PARTY_MAP_VIEW"
+ "FLEX_CARD_VERSION"
+ "FLYOVER"
+ "GEOAPSequenceActionTargetState"
+ "GEOAPSequenceManager"
+ "GEOAPSequenceWaitState"
+ "GEOAPWebPortal"
+ "GeoAnalyticsEvent_MapViewEngagement_dropRate"
+ "IMPRESSION_OBJECT"
+ "LOG_MSG_STATE_TYPE_UNKNOWN"
+ "LONG"
+ "LONG_APPID"
+ "MAPS_APP_DWELL_TIME_30_SEC"
+ "MAPS_APP_DWELL_TIME_3_SEC"
+ "MAPS_FEATURES"
+ "MAPS_LAUNCH"
+ "MAPS_PLACE_IDS"
+ "MAPS_SERVER"
+ "MAPS_USER"
+ "MAPS_USER_SETTINGS"
+ "MAP_RESTORE"
+ "MAP_SETTINGS"
+ "MAP_UI"
+ "MAP_UI_SHOWN"
+ "MAP_VIEW_LOCATION"
+ "MARKET"
+ "MUNIN_RESOURCE_LOG"
+ "NAVIGATION"
+ "NAV_TRACE"
+ "NEARBY_TRANSIT"
+ "NO"
+ "NO_WITH_TIME"
+ "OFFLINE_DOWNLOAD"
+ "PAIRED_DEVICE"
+ "PHOTO_SUBMISSION"
+ "PLACE_CARD"
+ "PLACE_CARD_RAP"
+ "PLACE_REQUEST"
+ "PLACE_SUMMARY_LAYOUT"
+ "POI_BUSYNESS"
+ "PREDEX_TRAINING"
+ "Q32@0:8i16i20d24"
+ "RATING_PHOTO_SUBMISSION"
+ "RATING_SUBMISSION"
+ "REALTIME_TRAFFIC"
+ "REPORT_AN_ISSUE"
+ "ROUTE"
+ "ROUTING_SETTINGS"
+ "ROUTING_WAYPOINTS"
+ "SEARCH_RESULTS"
+ "SECOND_PARTY_MAP_VIEW"
+ "SHORT"
+ "SHORT_NAV"
+ "STRN_HARVEST"
+ "SUMMARY_LOOK_AROUND_LOG"
+ "T@\"NSString\",R,N,V_name"
+ "T@?,C,N,V_fulfillmentBlock"
+ "TAP_EVENT"
+ "THIRD_PARTY_MAP_VIEW"
+ "TILE_SET"
+ "TRANSIT"
+ "TRANSIT_STEP"
+ "Td,N,V_startTime"
+ "Td,N,V_timeout"
+ "UGC_PHOTO"
+ "USER_SESSION"
+ "Unreachable reached: base class has no implementation"
+ "WIFI_PROBE"
+ "WebPlaceCardStates"
+ "WebPlaceCardUploadPolicy"
+ "WebPortal"
+ "_fulfillmentBlock"
+ "_serialQ"
+ "_waitTime"
+ "addAbortingUserAction:target:"
+ "addAdmissionUserAction:target:"
+ "await placecard interaction"
+ "await search results"
+ "await tap list item"
+ "captureDailyUseSummaryWithUseEvents:summaryPeriod:summaryDate:aggregationSummaryDate:firstEventDate:user_mapsUseLastDate:"
+ "captureDailyUseSummaryWithUseEvents:summaryPeriod:summaryDate:aggregationSummaryDate:firstEventDate:user_mapsUseLastDate:additionalStates:providedDropRate:completionQueue:completionBlock:"
+ "captureMapViewEngagementWithAction:target:value:moduleType:moduleMetadata:richProviderId:additionalStates:providedDropRate:completionQueue:completionBlock:"
+ "captureWebPlaceCardAnalyticEvent:analyticSessionType:"
+ "captureWebPlaceCardFeatureUseCount:usageString:usageBool:"
+ "com.apple.geoap.sequence"
+ "currentDailyAggregationRepresentativeString"
+ "dailyAggregationRepresentativeStringFromDate:"
+ "dailyAggregationTimestampFromDate:inAggTimestampFormat:"
+ "didTimeoutAt:"
+ "enter maps"
+ "event data from placecard could not be parsed : (%@)"
+ "fulfillmentBlock"
+ "indeterminant range"
+ "initWithName:"
+ "initWithName:admissionUserAction:target:"
+ "initWithName:waitTime:"
+ "isPaidAccount"
+ "mapsUserStartDate"
+ "name"
+ "not set"
+ "processUserAction:target:atTime:"
+ "received %lu bytes of event data with session type (%d : %@)"
+ "reset"
+ "search win"
+ "search win achieved"
+ "searchWinSequence"
+ "session state (%d : %@) could not be constructed"
+ "session type '%d : %@' is not supported"
+ "setAggregationSummaryDate:"
+ "setFulfillmentBlock:"
+ "setIsPaidAccount:"
+ "setMapsUserStartDate:"
+ "setTimeout:"
+ "startTime"
+ "state (%d : %@) could not be constructed"
+ "thirtySecondDurationEngagementSequence"
+ "threeSecondDurationEngagementSequence"
+ "timeZoneForSecondsFromGMT:"
+ "timeout"
+ "v28@0:8@16i24"
+ "v60@0:8@16i24@28@36@44@52"
+ "v92@0:8@16i24@28@36@44@52@60@68@76@?84"
- "Assertion failed: _completionBlock != ((void *)0)"
- "Assertion failed: _historyVisitorBlock != ((void *)0)"
- "Assertion failed: _inflightVisitorBlock != ((void *)0)"
- "C"
- "MAPS_INTERACTION_TYPE_POSITIVE_SEARCH_ENGAGEMENT"
- "MAPS_INTERACTION_TYPE_UNKNOWN"
- "_emitType"
- "_getMapsUserStartDate"
- "awaiting placecard interaction"
- "awaiting search results"
- "awaiting tap list item"
- "captureDailyUseSummaryWithUseEvents:summaryPeriod:summaryDate:firstEventDate:user_mapsUseLastDate:"
- "captureDailyUseSummaryWithUseEvents:summaryPeriod:summaryDate:firstEventDate:user_mapsUseLastDate:additionalStates:providedDropRate:completionQueue:completionBlock:"
- "search conversion"
- "state '%@' aborts on input pair"
- "state '%@' fulfilled on input pair"
- "state '%@' is processing (%@, %@)"
- "state '%@' timed out"
- "state '%@' will emit %@"
- "v52@0:8@16i24@28@36@44"
- "v84@0:8@16i24@28@36@44@52@60@68@?76"

```
