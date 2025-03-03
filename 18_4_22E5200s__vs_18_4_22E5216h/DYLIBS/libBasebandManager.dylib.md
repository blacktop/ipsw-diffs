## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

-1245.0.0.0.0
-  __TEXT.__text: 0x1f8c70
-  __TEXT.__auth_stubs: 0x32a0
-  __TEXT.__init_offsets: 0x134
+1248.0.0.0.0
+  __TEXT.__text: 0x200d18
+  __TEXT.__auth_stubs: 0x3300
+  __TEXT.__init_offsets: 0x144
   __TEXT.__objc_methlist: 0x46c
-  __TEXT.__const: 0xcc8b
-  __TEXT.__gcc_except_tab: 0x31c78
-  __TEXT.__cstring: 0x6f9f
-  __TEXT.__oslogstring: 0xb090
-  __TEXT.__unwind_info: 0x99b8
+  __TEXT.__const: 0xcdeb
+  __TEXT.__gcc_except_tab: 0x32cb8
+  __TEXT.__cstring: 0x7139
+  __TEXT.__oslogstring: 0xb4ae
+  __TEXT.__unwind_info: 0x9b20
   __TEXT.__objc_classname: 0x109
   __TEXT.__objc_methname: 0x1187
   __TEXT.__objc_methtype: 0x1753
   __TEXT.__objc_stubs: 0xfa0
-  __DATA_CONST.__got: 0x20a8
-  __DATA_CONST.__const: 0x1e10
+  __DATA_CONST.__got: 0x2140
+  __DATA_CONST.__const: 0x1f10
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x568
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1960
-  __AUTH_CONST.__const: 0xff28
+  __AUTH_CONST.__auth_got: 0x1990
+  __AUTH_CONST.__const: 0x10128
   __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0x918
   __AUTH_CONST.__objc_intobj: 0x18

   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x550
   __DATA_DIRTY.__common: 0xc8
-  __DATA_DIRTY.__bss: 0x21a
+  __DATA_DIRTY.__bss: 0x23a
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5893
-  Symbols:   8644
-  CStrings:  2481
+  Functions: 5957
+  Symbols:   8741
+  CStrings:  2523
 
Symbols:
+ __ZN10BootModule25stopNetworkCampTimer_syncEv
+ __ZN10BootModule26startNetworkCampTimer_syncEv
+ __ZN10BootModule28updateNetworkCampStatus_syncEb
+ __ZN12HealthModule51prepareAnalyticsDataForCommCenterBootupLatency_syncEN3xpc4dictE
+ __ZN12capabilities5radio7initiumEv
+ __ZN15DeviceHistoryDB16getDeviceHistoryERNSt3__16vectorI18_DeviceHistoryItemNS0_9allocatorIS2_EEEE
+ __ZN3abm10kNumBootupE
+ __ZN3abm11kBuildAfterE
+ __ZN3abm11kIsSwUpdateE
+ __ZN3abm12kBuildBeforeE
+ __ZN3abm13kIsSuccessfulE
+ __ZN3abm16kLatencyBBBootupE
+ __ZN3abm16kLatencyCCBootupE
+ __ZN3abm20kBootupFailureReasonE
+ __ZN3abm20kLatencyRegistrationE
+ __ZN3abm21kKeyCACCBootupLatencyE
+ __ZN3abm22kKeyRegistrationStatusE
+ __ZN3abm24kKeyCommandGetPersParamsE
+ __ZN3abm24kKeyStatsBootIsReadyTimeE
+ __ZN3abm24kLatencyBBBootupCompleteE
+ __ZN3abm25kKeyStatsBootFailedReasonE
+ __ZN3abm28kKeyNetworkRegistrationStateE
+ __ZN3abm30kKeyAirplaneModeUserPreferenceE
+ __ZN3abm32kKeyStatsNetworkRegistrationTimeE
+ __ZN3abm33kCommandSubmitHealthDBBootMetricsE
+ __ZN3abm46kKeyStatsCommCenterRegistrationMetricSubmittedE
+ __ZN3sys17getDeviceBootTimeEv
+ __ZN4util8to_lowerERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN5trace22kKeyTraceErrorHandlingE
+ __ZN6config2hw6iPhoneEv
+ __ZN7support4misc10safe_timer10start_syncEv
+ __ZN7support4misc10safe_timer4initEv
+ __ZN7support4misc10safe_timer4stopEv
+ __ZN7support4misc10safe_timer5startEv
+ __ZN7support4misc10safe_timer6createENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS2_6chrono8durationIxNS2_5ratioILl1ELl1000EEEEENS2_8functionIFvvEEE11qos_class_t
+ __ZN7support4misc10safe_timer6createENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS2_6chrono8durationIxNS2_5ratioILl1ELl1000EEEEESD_NS2_8functionIFvvEEE11qos_class_t
+ __ZN7support4misc10safe_timer7restartEv
+ __ZN7support4misc10safe_timer9stop_syncEv
+ __ZN7support4misc10safe_timerC1ENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS2_6chrono8durationIxNS2_5ratioILl1ELl1000EEEEESD_NS2_8functionIFvvEEE11qos_class_t
+ __ZN7support4misc10safe_timerC2ENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS2_6chrono8durationIxNS2_5ratioILl1ELl1000EEEEESD_NS2_8functionIFvvEEE11qos_class_t
+ __ZN7support4misc10safe_timerD0Ev
+ __ZN7support4misc10safe_timerD1Ev
+ __ZN7support4misc10safe_timerD2Ev
+ __ZNK15DeviceHistoryDB22isFirstBootAfterUpdateEv
+ __ZNK7support4misc10safe_timer12getLogClientEv
+ __ZNK7support4misc10safe_timer9has_firedEv
+ __ZNSt13runtime_errorC1ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZTIN7support4misc10safe_timerE
+ __ZTSN7support4misc10safe_timerE
+ __ZTVN7support4misc10safe_timerE
+ _dispatch_assert_queue$V2
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _sysctl
CStrings:
+ "#I Metric has been submitted, skipping submission to Core Analytics"
+ "#I Registration state is %s"
+ "#I Sending out AWD metric: %s"
+ "#I Start network registration timer for metric submission"
+ "#I Stop network registration timer for metric submission"
+ "#I Timeout for network camping metrics capture, sending out existing metrics to Core Analytics"
+ "#I Updating metric with registration state [%s]"
+ "#I User preference airplane mode is %s"
+ "#I burning config will map to Burnin_INT"
+ "#I initializing baseband crash reason patterns and masks from factory file"
+ "' already active"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1248"
+ "AppleBasebandServices_Manager-1248"
+ "Burnin_INT"
+ "CommandSubmitHealthDBBootMetrics"
+ "CurrentQueue"
+ "Failed to allocate xpc dictionary for stats"
+ "Failed to prepare xpc dictionary to update CommCenter stats"
+ "Failed to query health DB for baseband boot related information"
+ "Failed to send command %s to update"
+ "Failed to submit metric %s to Core Analytics"
+ "Failed to update health DB"
+ "Got empty baseband statistics; something is wrong in HealthDB. Please file a radar"
+ "Information not available after a clean restore"
+ "LiveOn_INT"
+ "QMI Timeout"
+ "Resetting baseband after pushing files (due to kCarrierBundleChange)"
+ "[Timeout] "
+ "com.apple.telephony.baseband."
+ "com.apple.telephony.basebandservices.support"
+ "error: '%s' already active"
+ "error: failed to create dispatch queue"
+ "error: failed to create dispatch safe_timer object"
+ "error: failed to init safe_timer object"
+ "error: invalid timeout callback"
+ "error: invalid timeout value"
+ "file size cannot be 0"
+ "fired"
+ "kKeyStatsCommCenterRegistrationMetricSubmitted"
+ "not set"
+ "registration-wait"
+ "safe-timer"
+ "safe-timer."
+ "starting..."
+ "stopping..."
+ "timeout"
- "AppleBasebandManager-AppleBasebandServices_Manager-1245"
- "AppleBasebandServices_Manager-1245"
- "Failed to create xpc dictionary to reset Baseband stats"
- "Failed to create xpc dictionary to reset CommCenter stats"

```
