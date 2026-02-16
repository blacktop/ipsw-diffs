## heartratecoordinatord

> `/usr/libexec/heartratecoordinatord`

```diff

-26.0.0.0.0
-  __TEXT.__text: 0x25b30
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_stubs: 0x3a20
+31.0.0.0.0
+  __TEXT.__text: 0x27340
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__objc_stubs: 0x3be0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1794
-  __TEXT.__const: 0x37c
-  __TEXT.__oslogstring: 0x39ea
-  __TEXT.__cstring: 0x1f98
-  __TEXT.__gcc_except_tab: 0x4194
-  __TEXT.__objc_methname: 0x475a
-  __TEXT.__objc_classname: 0x3a4
-  __TEXT.__objc_methtype: 0x16ed
-  __TEXT.__unwind_info: 0x1128
-  __DATA_CONST.__auth_got: 0x400
+  __TEXT.__objc_methlist: 0x18ac
+  __TEXT.__const: 0x369
+  __TEXT.__oslogstring: 0x3946
+  __TEXT.__cstring: 0x2163
+  __TEXT.__gcc_except_tab: 0x428c
+  __TEXT.__objc_methname: 0x4be9
+  __TEXT.__objc_classname: 0x3d0
+  __TEXT.__objc_methtype: 0x1b68
+  __TEXT.__unwind_info: 0x12b0
+  __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0xbe8
-  __DATA_CONST.__cfstring: 0x1e20
+  __DATA_CONST.__const: 0xbe0
+  __DATA_CONST.__cfstring: 0x1d80
   __DATA_CONST.__objc_classlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__objc_intobj: 0x120
-  __DATA_CONST.__objc_arraydata: 0x4c0
+  __DATA_CONST.__objc_intobj: 0x150
+  __DATA_CONST.__objc_arraydata: 0x520
+  __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0xa8
-  __DATA.__objc_const: 0x29a0
-  __DATA.__objc_selrefs: 0x1070
-  __DATA.__objc_ivar: 0x254
+  __DATA.__objc_const: 0x2b10
+  __DATA.__objc_selrefs: 0x10e8
+  __DATA.__objc_ivar: 0x274
   __DATA.__objc_data: 0x640
-  __DATA.__data: 0x5a0
-  __DATA.__bss: 0xd8
+  __DATA.__data: 0x600
+  __DATA.__bss: 0xa8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B14B8355-9123-37A1-9679-8A32A86ED5FB
-  Functions: 855
-  Symbols:   205
-  CStrings:  1746
+  UUID: 3F5F8543-436B-3C78-856E-431F0A1B23FA
+  Functions: 892
+  Symbols:   200
+  CStrings:  1769
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDictionary
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ ___kCFBooleanFalse
+ _bzero
+ _objc_retainAutoreleasedReturnValue
- _IOPMAssertionCreateWithDescription
- _IOPMAssertionRelease
- _PPSCreateTelemetryIdentifier
- _PPSSendTelemetry
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHpYugBGXHjHyewPvGX2eM_uJ3gi5Kj3u5y0V8s/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "@\"<HRCAACPAnalyticsProcessorDelegate>\""
+ "@\"HRCAACPAnalyticsProcessor\""
+ "@24@0:8@\"HRCAnalyticsReporter\"16"
+ "@40@0:8q16@24@32"
+ "ATVRemote1,3"
+ "ATVRemote1,4"
+ "HRCAACPAnalyticsProcessor"
+ "HRCAACPAnalyticsProcessor init"
+ "HRCAACPAnalyticsProcessorDelegate"
+ "HRCClient init"
+ "Ignoring analytics for published heart rate, streaming session has not started"
+ "Saving host aacp analytics %{public}@"
+ "T@\"<HRCAACPAnalyticsProcessorDelegate>\",W,N,V_delegate"
+ "T@\"NSDictionary\",&,N,V_pendingAacpHostAnalytics"
+ "T{optional<std::chrono::time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>>=(?=c{time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>={duration<long long, std::ratio<1, 1000000000>>=q}})B},N,V_streamingModeStartTime"
+ "T{time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>={duration<long long, std::ratio<1, 1000000000>>=q}},R,N,V_creationTimestamp"
+ "_aaDeviceCreationTimestamp"
+ "_analytics"
+ "_analyticsProcessor"
+ "_analyticsQueue"
+ "_creationTimestamp"
+ "_firstConnectionSeen"
+ "_generateAnalyticsDictionary"
+ "_handleAacpAnalytics:"
+ "_handleHeartRateWithSteadyClockDurationCount:"
+ "_handleMatchedServiceWithProductId:aadNotificationTimestamp:serviceConnectedTimestamp:streamingRequestedTimestamp:isVirtual:"
+ "_hasMatchedService"
+ "_pendingAacpHostAnalytics"
+ "_recordAnalyticsForStreamingStart:"
+ "_reportAnalytics"
+ "_reportHostAacpAnalytics:"
+ "_saveHostAnalyticsAtTimestamp:streamingMode:"
+ "_setUUID:"
+ "added service with productId : %d, aadTimestamp : %lld, serviceTimestamp : %lld, streamingRequestedTimestamp : %lld, isVirtual : %d"
+ "com.apple.heartratecoordinator.aacpsource.analytics"
+ "com.apple.hrc.aacp_session.stats"
+ "computed analytics : %@"
+ "creationTimestamp"
+ "defaultHostAacpAnalytics"
+ "gated_hrs_in_pocket_percentage_left"
+ "gated_hrs_in_pocket_percentage_right"
+ "gated_hrs_low_mav_percentage_left"
+ "gated_hrs_low_mav_percentage_right"
+ "handleAacpAnalytics:"
+ "handleHeartRateWithSteadyClockDurationCount:"
+ "handleMatchedServiceWithProductId:aadNotificationTimestamp:serviceConnectedTimestamp:streamingRequestedTimestamp:isVirtual:"
+ "initMatching:withAnalyticsReporter:"
+ "initWithDictionary:"
+ "initWithStreamingModeStartTime:onQueue:delegate:"
+ "is_first_connection_of_streaming_session"
+ "is_virtual"
+ "latency_aad_notification_since_streaming_start_seconds"
+ "latency_first_hr_received_since_streaming_requested_seconds"
+ "latency_service_available_since_streaming_start_seconds"
+ "multiple matched services in HRCAACPAnalyticsProcessor"
+ "new"
+ "pendingAacpHostAnalytics"
+ "q"
+ "recorded first HR with timestamp : %lld"
+ "reportAnalytics"
+ "reportAnalytics:"
+ "serviceInfo present : %d"
+ "setPendingAacpHostAnalytics:"
+ "streamingRequestedSteadyClockDurationCount called with no matched service"
+ "streaming_mode"
+ "v24@0:8@\"NSDictionary\"16"
+ "v32@0:8{time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>={duration<long long, std::ratio<1, 1000000000>>=q}}16Q24"
+ "v48@0:8I16q20q28q36B44"
+ "{HRCAACPAnalytics=\"isVirtual\"B\"isFirstConnectionForStreamingSession\"B\"product_id\"I\"aadNotificationTime\"{time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>=\"__d_\"{duration<long long, std::ratio<1, 1000000000>>=\"__rep_\"q}}\"serviceConnectedTime\"{time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>=\"__d_\"{duration<long long, std::ratio<1, 1000000000>>=\"__rep_\"q}}\"streamingRequestedTime\"{time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>=\"__d_\"{duration<long long, std::ratio<1, 1000000000>>=\"__rep_\"q}}\"firstHrReceivedTime\"{optional<std::chrono::time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>>=\"\"(?=\"__null_state_\"c\"__val_\"{time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>=\"__d_\"{duration<long long, std::ratio<1, 1000000000>>=\"__rep_\"q}})\"__engaged_\"B}}"
- "@\"HRCPowerAssertion\""
- "HRCPowerAssertion"
- "HeartRateCoordinator"
- "Opportunistic mode not supported on BLE sources"
- "PreventUserIdleSystemSleep"
- "TimeoutActionTurnOff"
- "T{time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>={duration<long long, std::ratio<1, 1000000000>>=q}},N,V_streamingModeStartTime"
- "UUIDString"
- "Unsupported attempt to set opportunistic mode for AACP source"
- "_assertion"
- "_hrLoggingPreference"
- "_internalUIVariant"
- "_name"
- "_powerAssertion"
- "_saveHostAnalyticsAtTimestamp:"
- "activeSourceDidChange:"
- "bud_withheld_hrs_percentage_left"
- "bud_withheld_hrs_percentage_right"
- "clientConnection"
- "clientState"
- "collated streaming mode switched to : %lu"
- "collatedState"
- "com.apple.heartratecoordinator.streaming"
- "connection-identifier"
- "context"
- "copy"
- "creating a %{public}@ power assertion to prevent system sleep, reason : %{public}@"
- "failed to create power assertion: 0x%x"
- "hrLoggingPreference"
- "initMatching:"
- "initWithName:reason:"
- "opportunistic-mode"
- "power telemetry :: client connection with name : %{public}@ , uuid : %{public}@, process-connected : %{public}d"
- "power telemetry :: client snapshot with name : %{public}@ , uuid : %{public}@, streaming-mode : %{public}lu , opportunistic-mode : %{public}d"
- "power telemetry :: collated snapshot with streaming-mode : %{public}lu , opportunistic-mode : %{public}d"
- "process-connected"
- "process-name"
- "releasing %{public}@ power assertion"
- "streaming-mode"
- "successfully acquired power assertion %{public}@"
- "v24@0:8{time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>={duration<long long, std::ratio<1, 1000000000>>=q}}16"
- "\x81"

```
