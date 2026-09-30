## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1937.1.0.0.0
-  __TEXT.__text: 0x1713d8
+1939.2.0.0.0
+  __TEXT.__text: 0x17171c
   __TEXT.__auth_stubs: 0x26f0
-  __TEXT.__objc_stubs: 0x21720
+  __TEXT.__objc_stubs: 0x21740
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0x11bf4
+  __TEXT.__objc_methlist: 0x11bfc
   __TEXT.__const: 0x11e08
   __TEXT.__gcc_except_tab: 0x6364
-  __TEXT.__cstring: 0x5a193
-  __TEXT.__objc_methname: 0x346a6
+  __TEXT.__cstring: 0x5a21d
+  __TEXT.__objc_methname: 0x346f4
   __TEXT.__objc_classname: 0x11e2
-  __TEXT.__objc_methtype: 0x8b16
+  __TEXT.__objc_methtype: 0x8b17
   __TEXT.__dlopen_cstrs: 0x43e
   __TEXT.__oslogstring: 0x109
-  __TEXT.__unwind_info: 0x50f0
+  __TEXT.__unwind_info: 0x50e8
   __DATA_CONST.__const: 0x5888
-  __DATA_CONST.__cfstring: 0x32f60
+  __DATA_CONST.__cfstring: 0x32f80
   __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__got: 0x8b0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x1cf78
-  __DATA.__objc_selrefs: 0xa038
+  __DATA.__objc_selrefs: 0xa040
   __DATA.__objc_ivar: 0x1e88
   __DATA.__objc_data: 0x3430
   __DATA.__data: 0x838
   __DATA.__bss: 0x7e0
-  __DATA.__common: 0x632
+  __DATA.__common: 0x63a
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7810
+  Functions: 7811
   Symbols:   874
-  CStrings:  16874
+  CStrings:  16876
 
CStrings:
+ "^{WRMMetricsCellTriggerDisconnect=d@@IIIIIIIIIIIIIIiBdBBd}16@0:8"
+ "handleStreamingStateChange skip stop detection, some apps are still active %@"
+ "handleVoIPStateChange skip stop detection, some apps are still active %@"
+ "handleVoIPStateChangeConference skip stop detection, some apps are still active %@"
+ "handleVoIPandStreamingStateChange skip stop detection, some apps are still active %@"
+ "hasAnyForegroundApps: VoIP (%lu), Streaming (%lu), VoIPAndStreaming (%lu), WebKit (%lu) apps are running in foreground"
+ "maybeNotifyStreamingStop: mStreamingConnectionReferenceCount: %llu, mWebkitStreamingActiveRefCnt: %d, mBBStateStreamingActive: %s"
+ "maybeTriggerCellularDisconnectForApp app running for %.2fs (<= %.2fs), skip cell disconnect for app: %@"
+ "maybeTriggerCellularDisconnectForApp:nwDeltaStatsIndex:minDataRateKbps:appRunningDuration:"
+ "startMonitoringAppSessions invalid NWStatsManager object"
+ "startMonitoringAppSessions suspicious txRate: %.2f for txBytes: %llu"
+ "startMonitoringAppSessions:interval:iRATHandler:"
+ "statsMonitorPeriodForApp:"
+ "stopMonitoringAppSessions"
+ "updateCellTriggerDisconnectMetric:genericCellScore:wifiScore:wrmWifiScore:statsMonitorPeriodicity:"
+ "v44@0:8@16C24d28d36"
+ "v48@0:8^{?=@QQQQQQQffB@Idd}16i24q28i36d40"
+ "{WRMMetricsCellTriggerDisconnect=\"timestamp\"d\"applicationId\"@\"NSString\"\"protocols\"@\"NSString\"\"txThroughputBefore\"I\"rxThroughputBefore\"I\"txThroughputAfter\"I\"rxThroughputAfter\"I\"rttMinBefore\"I\"rttMinAfter\"I\"rttAvgBefore\"I\"rttAvgAfter\"I\"cellScoreBefore\"I\"cellScoreAfter\"I\"wrmWifiScoreBefore\"I\"wrmWifiScoreAfter\"I\"wifiScoreBefore\"I\"wifiScoreAfter\"I\"dataLQM\"i\"didFallbackToWiFiOnCellDisconnect\"B\"postDisconnectMeasurementInterval\"d\"appRunsForeground\"B\"metricReportPending\"B\"metricSubmissionDeferInterval\"d}"
- "VoIP (%lu), Streaming (%lu), VoIPAndStreaming (%lu), WebKit (%lu) apps are running in foreground"
- "^{WRMMetricsCellTriggerDisconnect=d@@IIIIIIIIIIIIIIiBdBBC}16@0:8"
- "handleStreamingStateChange skip rxVoIPAppNotification %@"
- "handleVoIPStateChange skip rxVoIPAppNotification %@"
- "handleVoIPStateChangeConference skip rxVoIPAppNotification %@"
- "handleVoIPandStreamingStateChange skip, some apps are still active %@"
- "maybeNotifyStreamingStop: mStreamingConnectionReferenceCount: %llu, mWebkitStreamingActiveRefCnt: %d, mForegroundRunningVoipAndStreamingApps.count: %lu, mForegroundRunningStreamingApps.count: %lu"
- "maybeTriggerCellularDisconnectForApp:nwDeltaStatsIndex:minDataRateKbps:"
- "startStatsCollectionForApp invalid NWStatsManager object"
- "startStatsCollectionForApp suspicious txRate: %.2f for txBytes: %llu"
- "startStatsCollectionForApp:interval:iRATHandler:"
- "stopPeriodicTask"
- "updateCellTriggerDisconnectMetric:genericCellScore:wifiScore:wrmWifiScore:"
- "v36@0:8@16C24d28"
- "v40@0:8^{?=@QQQQQQQffB@Idd}16i24q28i36"
- "{WRMMetricsCellTriggerDisconnect=\"timestamp\"d\"applicationId\"@\"NSString\"\"protocols\"@\"NSString\"\"txThroughputBefore\"I\"rxThroughputBefore\"I\"txThroughputAfter\"I\"rxThroughputAfter\"I\"rttMinBefore\"I\"rttMinAfter\"I\"rttAvgBefore\"I\"rttAvgAfter\"I\"cellScoreBefore\"I\"cellScoreAfter\"I\"wrmWifiScoreBefore\"I\"wrmWifiScoreAfter\"I\"wifiScoreBefore\"I\"wifiScoreAfter\"I\"dataLQM\"i\"didFallbackToWiFiOnCellDisconnect\"B\"postDisconnectMeasurementInterval\"d\"appRunsForeground\"B\"metricReportPending\"B\"deferUntilAdditionalNwStatsReports\"C}"
```
