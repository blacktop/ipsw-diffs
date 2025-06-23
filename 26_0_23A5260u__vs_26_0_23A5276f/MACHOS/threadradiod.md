## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

-323.0.0.0.0
-  __TEXT.__text: 0x3e9690
-  __TEXT.__auth_stubs: 0x11230
+325.0.0.0.0
+  __TEXT.__text: 0x3e6788
+  __TEXT.__auth_stubs: 0x11240
   __TEXT.__objc_stubs: 0x98c0
   __TEXT.__init_offsets: 0xa4
-  __TEXT.__objc_methlist: 0x6580
+  __TEXT.__objc_methlist: 0x6588
   __TEXT.__objc_classname: 0x5f4
-  __TEXT.__cstring: 0x312e5
+  __TEXT.__cstring: 0x30f07
   __TEXT.__const: 0x946c
-  __TEXT.__gcc_except_tab: 0x2b634
-  __TEXT.__objc_methname: 0xeb57
-  __TEXT.__oslogstring: 0x222ce
+  __TEXT.__gcc_except_tab: 0x2b594
+  __TEXT.__objc_methname: 0xeb6c
+  __TEXT.__oslogstring: 0x2246c
   __TEXT.__objc_methtype: 0x3b20
-  __TEXT.__unwind_info: 0x7b20
+  __TEXT.__unwind_info: 0x7b30
   __TEXT.__eh_frame: 0x60
-  __DATA_CONST.__auth_got: 0x8930
+  __DATA_CONST.__auth_got: 0x8938
   __DATA_CONST.__got: 0x938
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0xd638
-  __DATA_CONST.__cfstring: 0x5f00
+  __DATA_CONST.__const: 0xd4d8
+  __DATA_CONST.__cfstring: 0x5f20
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA.__objc_const: 0x8518
-  __DATA.__objc_selrefs: 0x3648
+  __DATA.__objc_selrefs: 0x3650
   __DATA.__objc_ivar: 0x538
   __DATA.__objc_data: 0xe60
   __DATA.__data: 0x5a8
-  __DATA.__common: 0x3e320
+  __DATA.__common: 0x3e328
   __DATA.__bss: 0x1720c
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 56E5BB28-C7BC-34E7-824F-F5351A0BF4CF
-  Functions: 17155
-  Symbols:   89349
-  CStrings:  13382
+  UUID: 492F9224-C0E0-3F2A-A9BF-256B9DD0F5C6
+  Functions: 17130
+  Symbols:   89221
+  CStrings:  13357
 
Symbols:
+ -[ThreadNetworkManagerInstance isRegulatoryCertMode]
+ -[ThreadNetworkManagerInstance isRegulatoryCertMode].cold.1
+ -[ThreadNetworkManagerInstance(RCP2CAMetrics_extension) getBTWifiLoadInfoEvent:].cold.3
+ GCC_except_table1105
+ GCC_except_table180
+ GCC_except_table227
+ GCC_except_table232
+ GCC_except_table260
+ GCC_except_table306
+ GCC_except_table373
+ GCC_except_table374
+ GCC_except_table378
+ GCC_except_table410
+ GCC_except_table411
+ _Z28persist_host_reset_dueto_rcpbPKc.cold.1
+ _Z28persist_host_reset_dueto_rcpbPKc.cold.2
+ _Z28persist_host_reset_dueto_rcpbPKc.cold.3
+ _ZN15HostInterpreter14ProcessRcpInitEhPPcPv.cold.12
+ _ZN15HostInterpreter14ProcessRcpInitEhPPcPv.cold.13
+ _ZN15HostInterpreter14ProcessRcpInitEhPPcPv.cold.14
+ _ZN15HostInterpreter14ProcessRcpInitEhPPcPv.cold.15
+ _ZN15HostInterpreter14ProcessRcpInitEhPPcPv.cold.16
+ _ZN15HostInterpreter14ProcessRcpInitEhPPcPv.cold.17
+ __Z28persist_host_reset_dueto_rcpbPKc
+ __ZN14RcpHostContext20isRegulatoryCertModeEv
+ __ZN14RcpHostContext26iscoreDumpTXFailureEnabledEv
+ __ZN15HostInterpreter18CAStabilityMetricsENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN15HostInterpreter20isRegulatoryCertModeEv
+ __ZN2ot17WakeupTxScheduler6WakeUpERKNS_3Mac10ExtAddressEjh
+ __ZN2ot3Mle3Mle11setWasChildEb
+ __ZN2ot3Mle3Mle19AttachCslPeripheralERKNS_3Mac10ExtAddressEjhbh
+ __ZN2ot3Mle3Mle29isThreadRegulatoryCertEnabledEv
+ __ZN2ot5Radio22SetWakeupConfigurationEjh
+ __ZN2ot6Spinel11RadioSpinel22SetWakeupConfigurationEjh
+ __ZN2ot6Spinel11RadioSpinel27GetCoreDumpTXFailureEnabledEv
+ __ZN2ot6Spinel11RadioSpinel27SetCoreDumpTXFailureEnabledEb
+ __ZZN2ot3Mle3Mle19AttachCslPeripheralERKNS_3Mac10ExtAddressEjhbhE11mNumRetries
+ ___ZN15HostInterpreter18CAStabilityMetricsENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_block_invoke.cold.1
+ ___ZN15HostInterpreter18CAStabilityMetricsENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_block_invoke.cold.2
+ ___ZN15HostInterpreter18CAStabilityMetricsENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_block_invoke.cold.3
+ ___ZN15HostInterpreter18CAStabilityMetricsENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_block_invoke.cold.4
+ ____ZN15HostInterpreter18CAStabilityMetricsENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_block_invoke
+ ___copy_helper_block_e8_40c66_ZTSNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ ___destroy_helper_block_e8_40c66_ZTSNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __block_descriptor_tmp.569
+ __block_descriptor_tmp.95
+ _otPlatRadioGetCoreDumpTXFailureEnabled
+ _otPlatRadioSetCoreDumpTXFailureEnabled
+ _otThreadResolve
+ _otThreadSetWasChild
- GCC_except_table1091
- GCC_except_table186
- GCC_except_table210
- GCC_except_table222
- GCC_except_table245
- GCC_except_table303
- GCC_except_table304
- GCC_except_table322
- GCC_except_table350
- GCC_except_table381
- GCC_except_table391
- GCC_except_table414
- GCC_except_table415
- GCC_except_table499
- GCC_except_table525
- GCC_except_table526
- _Z28persist_host_reset_dueto_rcpb.cold.1
- __Z28persist_host_reset_dueto_rcpb
- __ZN15HostInterpreter31GetTriggerBasedCountersAsValMapEPK25otMleTriggerBasedCountersPK24otIpTriggerBasedCountersP19otVendorCoexMetrics
- __ZN2ot17WakeupTxScheduler6WakeUpERKNS_3Mac10ExtAddressEth
- __ZN2ot3Cli6Vendor25ProcessGetVendorCsmaMaxBeEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor25ProcessGetVendorCsmaMinBeEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor25ProcessSetVendorCsmaMaxBeEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor25ProcessSetVendorCsmaMinBeEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor26ProcessGetVendorFemEnabledEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor26ProcessSetVendorFemEnabledEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor27ProcessGetVendorCoexEnabledEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor27ProcessSetVendorCoexEnabledEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor28ProcessSetVendorCoexCountersEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor30ProcessGetVendorCoexHistogramsEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor30ProcessSetVendorCoexHistogramsEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor31ProcessGetVendorCsmaMaxBackOffsEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor31ProcessSetVendorCsmaMaxBackOffsEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor32ProcessGetVendorCoexGrantTimeoutEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor32ProcessSetVendorCoexGrantTimeoutEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor32ProcessSetVendorPmuWakeTestStartEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor33ProcessGetVendorPmuWakeTestResultEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor35ProcessGetVendorCoexCslReqAheadTimeEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor35ProcessGetVendorCsmaCcaIdleAttemptsEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor35ProcessSetVendorCoexCslReqAheadTimeEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor35ProcessSetVendorCsmaCcaIdleAttemptsEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor36ProcessGetVendorCsmaBackoffHistogramEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor36ProcessSetVendorCsmaBackoffHistogramEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor37ProcessGetVendorCoexRxThrottleTimeoutEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor37ProcessSetVendorCoexRxThrottleTimeoutEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor38ProcessGetVendorCoexCslReqAheadTimeMinEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor40ProcessGetVendorCsmaSlidingWindowEnabledEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor40ProcessSetVendorCsmaSlidingWindowEnabledEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor42ProcessGetVendorCcaEnergyDetectedHistogramEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor42ProcessSetVendorCcaEnergyDetectedHistogramEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor43ProcessGetVendorCslTxSchedulerFrameReqAheadEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor43ProcessSetVendorCslTxSchedulerFrameReqAheadEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor45ProcessGetVendorCoexRxThrottleMaxAttemptsNoneEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor45ProcessSetVendorCoexRxThrottleMaxAttemptsNoneEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor47ProcessGetVendorCoexRxThrottleMaxAttemptsRxOnlyEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor47ProcessGetVendorCoexRxThrottleMaxAttemptsTxOnlyEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor47ProcessSetVendorCoexRxThrottleMaxAttemptsRxOnlyEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Cli6Vendor47ProcessSetVendorCoexRxThrottleMaxAttemptsTxOnlyEPNS_5Utils13CmdLineParser3ArgE
- __ZN2ot3Mle3Mle19AttachCslPeripheralERKNS_3Mac10ExtAddressEthbh
- __ZN2ot5Radio22SetWakeupConfigurationEth
- __ZN2ot6Spinel11RadioSpinel21GetVendorCoexCountersER19otVendorCoexMetrics
- __ZN2ot6Spinel11RadioSpinel22SetWakeupConfigurationEth
- __ZN2ot6Spinel11RadioSpinel23GetVendorCoexHistogramsER22otVendorCoexHistograms
- __ZN2ot6Spinel11RadioSpinel28GetVendorCsmaCcaIdleAttemptsEPh
- __ZN2ot6Spinel11RadioSpinel28SetVendorCsmaCcaIdleAttemptsEh
- __ZN2ot6Spinel11RadioSpinel35GetVendorCcaEnergyDetectedHistogramEP34otVendorCcaEneryDetectedHistograms
- __ZZN15HostInterpreter31GetTriggerBasedCountersAsValMapEPK25otMleTriggerBasedCountersPK24otIpTriggerBasedCountersP19otVendorCoexMetricsE14ipCounterNames
- __ZZN15HostInterpreter31GetTriggerBasedCountersAsValMapEPK25otMleTriggerBasedCountersPK24otIpTriggerBasedCountersP19otVendorCoexMetricsE15mleCounterNames
- __ZZN15HostInterpreter31GetTriggerBasedCountersAsValMapEPK25otMleTriggerBasedCountersPK24otIpTriggerBasedCountersP19otVendorCoexMetricsE16coexCounterNames
- __ZZN2ot3Mle3Mle19AttachCslPeripheralERKNS_3Mac10ExtAddressEthbhE11mNumRetries
- __block_descriptor_tmp.585
- _otPlatVendorGetCcaEnergyDetectedHistogram
- _otPlatVendorGetCoexHistograms
- _otPlatVendorGetCsmaCcaIdleAttempts
- _otPlatVendorSetCsmaCcaIdleAttempts
CStrings:
+ " Morty_Version: V0.325"
+ "%s : %d : Can not form preferred network keychain item with insufficient information "
+ "%s:%d: Feature flag: threadAlwaysOnFeatureEnabled = [%d], stateMachineEnabled = [%d], audioNoThreadFeatureEnabled = [%d], RegulatoryCertMode = [%d]"
+ "%sFailed to get thread channel"
+ "... wasChild:%s"
+ "1.4.0"
+ "EnableCoreDumpTXFailure"
+ "HI:Couldn't get RCP vendor version"
+ "HI:Couldn't parse prior FirmwareCrash reason"
+ "HI:Host restarted after a prior FW crash. Triggering ABC"
+ "HI:Prior FW Crash:Couln't trigger CAStabilityMetrics,len=[%d]"
+ "HI:Prior FW Crash:kAWDStabilityCounters_Crash_Type invalid"
+ "HI:Prior FW Crash:len=[%d],reason %s "
+ "HI:Prior FW Crash:triggering stability"
+ "HI:timeline_log_level is [%d]"
+ "Overriding Device Stat,set wasChild:[True]"
+ "Persisting crash reason %s"
+ "RCP2_TX_RX_ABORT"
+ "RegulatoryCertMode"
+ "Threadradiod startup: Feature flag: Init Complete: threadAlwaysOnFeatureEnabled = [%d], stateMachineEnabled = [%d], audioNoThreadFeatureEnabled = [%d], threadCertEnabled = [%d], threadGeoEnabled = [%d], coexLoadSimulationEnabled = [%d], coreDumpTXFailureEnabled = [%d], regulatoryCertMode = [%d]"
+ "Triggered flagstoneStabilityMetrics"
+ "isRegulatoryCertMode"
+ "thread_channel"
+ "trapReason ="
+ "wifi_channel"
- " Morty_Version: V0.323"
- "%s : %d : Can not form preferred netowk keychain item with insufficient information "
- "%s:%d: Feature flag: threadAlwaysOnFeatureEnabled = [%d], stateMachineEnabled = [%d], audioNoThreadFeatureEnabled = [%d]"
- "%s:%d: Finding Thread network Broder Routers around"
- ", %u"
- "1.4"
- "CCA Idle Attempts=%u"
- "CSMABackoffHistogram[%d]=%u"
- "CcaHistogram[%d]=%u"
- "CcaIdleAttempts=%u"
- "Coex RxThrottle Timeout=%u"
- "CoexUnsolicatedTxGrantHistogram=[%u"
- "CslReqAheadTime=%u"
- "CslReqAheadTimeMin=%u"
- "Enabled=%u"
- "Fem Enabled=%u"
- "FrameReqAhead=%u"
- "Get VendorCcaEnergyDetectedHistogram failed"
- "Get VendorCoexCounters failed"
- "Get VendorCoexHistograms failed"
- "Get VendorCsmaCcaIdleAttempts failed"
- "Host restarted after a prior FW crash. Triggering ABC"
- "MaxAttempts=%u"
- "MaxAttemptsNone=%u"
- "MaxAttemptsRxOnly=%u"
- "MaxAttemptsTxOnly=%u"
- "MaxBE=%u"
- "MaxBackoffs=%u"
- "MinBE=%u"
- "PmuWakeTestResult=%u"
- "PmuWakeTestStart=%u"
- "Reset CSMABackoffHistogram"
- "Reset CcaHistogram"
- "Reset Coex Histogram"
- "Reset CoexMetrics"
- "Set VendorCsmaCcaIdleAttempts failed"
- "Threadradiod startup: Feature flag: Init Complete: threadAlwaysOnFeatureEnabled = [%d], stateMachineEnabled = [%d], audioNoThreadFeatureEnabled = [%d], threadCertEnabled = [%d], threadGeoEnabled = [%d], coexLoadSimulationEnabled = [%d]"
- "Timeout=%u"
- "Timeout=%u is greater than max supported value:208440 "
- "]\nCoexAbortsDueToGrantRevokesHistogram=[%u"
- "]\nCoexTotalGrantTimeHistogram=[%u"
- "]\nCoexTotalRxGrantHistogram=[%u"
- "]\nCoexTotalTxGrantHistogram=[%u"
- "]\nCoexUnsolicatedRxGrantHistogram=[%u"
- "coex_denied_requests"
- "coex_granted_requests"
- "coex_requests"
- "t(LLLLLLLLLLLL)"
- "t(LLLLLLLLLLLLLLL)t(LLLLLLLLLLLLLL)t(LLLLLLLLLLLLLLL)t(LLLL)"
- "t(LLLLLLLLLLLLLLLLLLLL)t(LLLLLLLLLLLLLLLLLLLL)t(LLLLLLLLLLLLLLLLLLLL)t(LLLLLLLLLLLLLLLLLLLL)t(LLLLLLLLLLLLLLLL)t(LLLLLLLLLLL)"
- "timeline_log_level is [%d]"

```
