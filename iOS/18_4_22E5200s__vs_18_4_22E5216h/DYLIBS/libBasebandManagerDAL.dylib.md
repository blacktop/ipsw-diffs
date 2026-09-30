## libBasebandManagerDAL.dylib

> `/usr/lib/libBasebandManagerDAL.dylib`

```diff

-1245.0.0.0.0
-  __TEXT.__text: 0x112ad4
-  __TEXT.__auth_stubs: 0x2350
-  __TEXT.__init_offsets: 0xb4
+1248.0.0.0.0
+  __TEXT.__text: 0x11aa18
+  __TEXT.__auth_stubs: 0x23c0
+  __TEXT.__init_offsets: 0xc4
   __TEXT.__objc_methlist: 0x274
-  __TEXT.__const: 0x64d7
-  __TEXT.__gcc_except_tab: 0x1a730
-  __TEXT.__oslogstring: 0x534e
-  __TEXT.__cstring: 0x2f41
-  __TEXT.__unwind_info: 0x5470
+  __TEXT.__const: 0x6677
+  __TEXT.__gcc_except_tab: 0x1b758
+  __TEXT.__oslogstring: 0x576c
+  __TEXT.__cstring: 0x30c4
+  __TEXT.__unwind_info: 0x55d8
   __TEXT.__objc_classname: 0x68
   __TEXT.__objc_methname: 0x626
   __TEXT.__objc_methtype: 0x1289
   __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x1178
-  __DATA_CONST.__const: 0xf30
+  __DATA_CONST.__got: 0x1210
+  __DATA_CONST.__const: 0x1030
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x218
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x11b8
-  __AUTH_CONST.__const: 0x8a28
+  __AUTH_CONST.__auth_got: 0x11f0
+  __AUTH_CONST.__const: 0x8c28
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x418
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x740
   __DATA.__common: 0x28
-  __DATA.__bss: 0x1d8
+  __DATA.__bss: 0x1f8
   __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3108
-  Symbols:   4632
-  CStrings:  1170
+  Functions: 3172
+  Symbols:   4730
+  CStrings:  1210
 
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
+ _xpc_double_create
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
+ "Resetting baseband after pushing files (due to kCarrierBundleChange)"
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
