## libBasebandManagerDAL.dylib

> `/usr/lib/libBasebandManagerDAL.dylib`

```diff

-1220.0.0.0.0
-  __TEXT.__text: 0x119660
-  __TEXT.__auth_stubs: 0x22a0
-  __TEXT.__init_offsets: 0xa8
-  __TEXT.__objc_methlist: 0x140
-  __TEXT.__const: 0x640f
-  __TEXT.__gcc_except_tab: 0x1a3a4
-  __TEXT.__oslogstring: 0x5243
-  __TEXT.__cstring: 0x2e1a
-  __TEXT.__unwind_info: 0x51c8
+1248.0.0.0.0
+  __TEXT.__text: 0x11aa18
+  __TEXT.__auth_stubs: 0x23c0
+  __TEXT.__init_offsets: 0xc4
+  __TEXT.__objc_methlist: 0x274
+  __TEXT.__const: 0x6677
+  __TEXT.__gcc_except_tab: 0x1b758
+  __TEXT.__oslogstring: 0x576c
+  __TEXT.__cstring: 0x30c4
+  __TEXT.__unwind_info: 0x55d8
   __TEXT.__objc_classname: 0x68
   __TEXT.__objc_methname: 0x626
-  __TEXT.__objc_methtype: 0x1389
+  __TEXT.__objc_methtype: 0x1289
   __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x1140
-  __DATA_CONST.__const: 0xf10
+  __DATA_CONST.__got: 0x1210
+  __DATA_CONST.__const: 0x1030
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x168
+  __DATA_CONST.__objc_selrefs: 0x218
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1160
-  __AUTH_CONST.__const: 0x8a58
-  __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0x658
+  __AUTH_CONST.__auth_got: 0x11f0
+  __AUTH_CONST.__const: 0x8c28
+  __AUTH_CONST.__cfstring: 0x300
+  __AUTH_CONST.__objc_const: 0x418
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x6a8
-  __DATA.__common: 0x20
-  __DATA.__bss: 0x1a8
-  __DATA_DIRTY.__data: 0x78
+  __DATA.__data: 0x740
+  __DATA.__common: 0x28
+  __DATA.__bss: 0x1f8
+  __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3067
-  Symbols:   4438
-  CStrings:  1152
+  Functions: 3172
+  Symbols:   4730
+  CStrings:  1210
 
Symbols:
+ _CFUserNotificationCreate
+ _CFUserNotificationDisplayNotice
+ _CFUserNotificationReceiveResponse
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyUtilTriggerNMI
+ _TelephonyUtilWriteStackshot
+ __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN10BootModule25stopNetworkCampTimer_syncEv
+ __ZN10BootModule26startNetworkCampTimer_syncEv
+ __ZN10BootModule28updateNetworkCampStatus_syncEb
+ __ZN12HealthModule51prepareAnalyticsDataForCommCenterBootupLatency_syncEN3xpc4dictE
+ __ZN12capabilities3abs17shouldBlockResetsEv
+ __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
+ __ZN12capabilities3abs39shouldTriggerStackshotOnShutdownTimeoutEv
+ __ZN12capabilities4diag12supportsQDSSEv
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
+ __ZN3abm24kKeyStatsBootIsReadyTimeE
+ __ZN3abm24kLatencyBBBootupCompleteE
+ __ZN3abm25kKeyStatsBootFailedReasonE
+ __ZN3abm28kKeyNetworkRegistrationStateE
+ __ZN3abm30kKeyAirplaneModeUserPreferenceE
+ __ZN3abm32kKeyStatsNetworkRegistrationTimeE
+ __ZN3abm33kCommandSubmitHealthDBBootMetricsE
+ __ZN3abm46kKeyStatsCommCenterRegistrationMetricSubmittedE
+ __ZN3ctu5power7manager20simulateNotificationEjb
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN3sys17getDeviceBootTimeEv
+ __ZN4util8to_lowerERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
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
+ __ZNSt3__117bad_function_callD0Ev
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTIN7support4misc10safe_timerE
+ __ZTINSt3__117bad_function_callE
+ __ZTSN7support4misc10safe_timerE
+ __ZTVN7support4misc10safe_timerE
+ __ZTVNSt3__117bad_function_callE
+ _dispatch_assert_queue$V2
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationDefaultButtonTitleKey
+ _sysctl
+ _xpc_double_create
- __ZNSt9exceptionD2Ev
CStrings:
+ "#D     %s"
+ "#D Enumerating HealthEvents to be written to disk:"
+ "#D HealthEvents dictionary representation to be written to disk: %@"
+ "#I Metric has been submitted, skipping submission to Core Analytics"
+ "#I Registration state is %s"
+ "#I Sending out AWD metric: %s"
+ "#I Simulated notification: %s"
+ "#I Start network registration timer for metric submission"
+ "#I Stop network registration timer for metric submission"
+ "#I Timeout for network camping metrics capture, sending out existing metrics to Core Analytics"
+ "#I Triggering stackshot"
+ "#I Triggering stackshot  -- done"
+ "#I Updating metric with registration state [%s]"
+ "#I User preference airplane mode is %s"
+ "#I blocking reset until user signals"
+ "' already active"
+ ", reason "
+ "@40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1248"
+ "AppleBasebandServices_Manager-1248"
+ "B136@0:8{NotificationInfo={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}16@88{CallBackData=@?{queue={object=^{dispatch_object_s}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}96"
+ "Baseband Hard-Reset: "
+ "Capability %s returning overridden value"
+ "CommandSubmitHealthDBBootMetrics"
+ "CurrentQueue"
+ "Failed to allocate xpc dictionary for stats"
+ "Failed to prepare xpc dictionary to update CommCenter stats"
+ "Failed to query health DB for baseband boot related information"
+ "Failed to send command %s to update"
+ "Failed to submit metric %s to Core Analytics"
+ "Failed to update health DB"
+ "Got empty baseband statistics; something is wrong in HealthDB. Please file a radar"
+ "Incompatible Baseband firmware."
+ "Information not available after a clean restore"
+ "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
+ "OK"
+ "PANIC: %s"
+ "ResetInfoReasonRegexPattern"
+ "ResetInfoReasonRegexPatternMask"
+ "ResetInfoRegexPatterns"
+ "Resetting baseband after pushing files (due to kCarrierBundleChange)"
+ "ServiceManager sleep timeout"
+ "ServiceManager wake timeout"
+ "Triggering stackshot, goes with "
+ "Unexpected behavior may occur. Please upgrade to a newer firmware."
+ "Unsupported ABM profile, check your plist!"
+ "baseband crash"
+ "com.apple.telephony.baseband."
+ "com.apple.telephony.basebandservices.support"
+ "com.apple.telephony.capabilities"
+ "error: '%s' already active"
+ "error: failed to create dispatch queue"
+ "error: failed to create dispatch safe_timer object"
+ "error: failed to init safe_timer object"
+ "error: invalid timeout callback"
+ "error: invalid timeout value"
+ "fired"
+ "kKeyStatsCommCenterRegistrationMetricSubmitted"
+ "not set"
+ "registration-wait"
+ "safe-timer"
+ "safe-timer."
+ "starting..."
+ "stopping..."
+ "timeout"
+ "v116@0:8i16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}20{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}44{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}68{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}92"
+ "v128@0:8{NotificationInfo={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}16{CallBackData=@?{queue={object=^{dispatch_object_s}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}88"
+ "v32@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}8"
+ "v36@?0i8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}12"
+ "v44@0:8i16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}20"
+ "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40"
+ "v48@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}8{CFSharedRef<const __CFDictionary>=^{__CFDictionary}}32{block<void (^)()>=@?}40"
+ "{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}64@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}40"
- "@40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}16"
- "AppleBasebandManager-AppleBasebandServices_Manager-1220"
- "AppleBasebandServices_Manager-1220"
- "B136@0:8{NotificationInfo={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}16@88{CallBackData=@?{queue={object=^{dispatch_object_s}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}96"
- "Default pattern masks will be used"
- "Failed to create xpc dictionary to reset Baseband stats"
- "Failed to create xpc dictionary to reset CommCenter stats"
- "v116@0:8i16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}20{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}44{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}68{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}92"
- "v128@0:8{NotificationInfo={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}16{CallBackData=@?{queue={object=^{dispatch_object_s}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}88"
- "v32@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}8"
- "v36@?0i8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}12"
- "v44@0:8i16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}20"
- "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}8{dict={object=^v}}40"
- "v48@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}8{CFSharedRef<const __CFDictionary>=^{__CFDictionary}}32{block<void (^)()>=@?}40"
- "{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}64@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}40"

```
