## libCommCenterKCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib`

```diff

-12109.5.0.0.0
-  __TEXT.__text: 0x11dd78
-  __TEXT.__auth_stubs: 0x7200
-  __TEXT.__gcc_except_tab: 0x13348
-  __TEXT.__const: 0x15d7f
-  __TEXT.__oslogstring: 0x1277b
-  __TEXT.__cstring: 0x4380
-  __TEXT.__unwind_info: 0x6aa8
+12209.3.0.0.0
+  __TEXT.__text: 0x125a6c
+  __TEXT.__auth_stubs: 0x7470
+  __TEXT.__gcc_except_tab: 0x13910
+  __TEXT.__const: 0x15fbf
+  __TEXT.__oslogstring: 0x14087
+  __TEXT.__cstring: 0x482a
+  __TEXT.__unwind_info: 0x6c78
   __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x9b0
-  __AUTH_CONST.__auth_got: 0x3908
-  __AUTH_CONST.__const: 0x10408
+  __DATA_CONST.__const: 0xa00
+  __AUTH_CONST.__auth_got: 0x3a40
+  __AUTH_CONST.__const: 0x10698
   __AUTH_CONST.__cfstring: 0x120
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 5246
-  Symbols:   7510
-  CStrings:  2171
+  Functions: 5335
+  Symbols:   7636
+  CStrings:  2381
 
Symbols:
+ __ZN10subscriber16makeSimSlotRangeENS_7SimSlotE
+ __ZN3awd8asStringENS_11PayloadTypeE
+ __ZN3awd8asStringENS_5AppIDE
+ __ZN3ctu2cf6assignERNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKv
+ __ZN6AriSdk28ARI_IBINetBBTurboModeReq_SDKC1Ev
+ __ZN6AriSdk28ARI_IBINetBBTurboModeReq_SDKD1Ev
+ __ZN6AriSdk28ARI_IBIStwDiagCommandReq_SDKC1Ev
+ __ZN6AriSdk28ARI_IBIStwDiagCommandReq_SDKD1Ev
+ __ZN6AriSdk29ARI_IBICallPsWrmSAInfoReq_SDKC1Ev
+ __ZN6AriSdk29ARI_IBICallPsWrmSAInfoReq_SDKD1Ev
+ __ZN6AriSdk29ARI_IBICallPsWrmSAInfoRsp_SDK6unpackEv
+ __ZN6AriSdk29ARI_IBICallPsWrmSAInfoRsp_SDKC1EPKhj
+ __ZN6AriSdk29ARI_IBICallPsWrmSAInfoRsp_SDKD1Ev
+ __ZN6AriSdk30ARI_IBINetBBTurboModeRspCb_SDK6unpackEv
+ __ZN6AriSdk30ARI_IBINetBBTurboModeRspCb_SDKC1EPKhj
+ __ZN6AriSdk30ARI_IBINetBBTurboModeRspCb_SDKD1Ev
+ __ZN6AriSdk30ARI_IBIStwDiagCommandIndCb_SDK6unpackEv
+ __ZN6AriSdk30ARI_IBIStwDiagCommandIndCb_SDKC1EPKhj
+ __ZN6AriSdk30ARI_IBIStwDiagCommandIndCb_SDKD1Ev
+ __ZN6AriSdk30ARI_IBIStwDiagCommandRspCb_SDKC1EPKhj
+ __ZN6AriSdk30ARI_IBIStwDiagCommandRspCb_SDKD1Ev
+ __ZN6AriSdk31ARI_CsiIceAudStatsInfoIndCb_SDK6unpackEv
+ __ZN6AriSdk31ARI_CsiIceAudStatsInfoIndCb_SDKC1EPKhj
+ __ZN6AriSdk31ARI_CsiIceAudStatsInfoIndCb_SDKD1Ev
+ __ZN6AriSdk35ARI_IBINetTransitInformationReq_SDKC1Ev
+ __ZN6AriSdk35ARI_IBINetTransitInformationReq_SDKD1Ev
+ __ZN6AriSdk36ARI_CsiIceAudDistortionInfoIndCb_SDK6unpackEv
+ __ZN6AriSdk36ARI_CsiIceAudDistortionInfoIndCb_SDKC1EPKhj
+ __ZN6AriSdk36ARI_CsiIceAudDistortionInfoIndCb_SDKD1Ev
+ __ZN6AriSdk37ARI_IBICallPsServiceTypeUpdateReq_SDKC1Ev
+ __ZN6AriSdk37ARI_IBICallPsServiceTypeUpdateReq_SDKD1Ev
+ __ZN6AriSdk37ARI_IBINetTransitInformationRspCb_SDK6unpackEv
+ __ZN6AriSdk37ARI_IBINetTransitInformationRspCb_SDKC1EPKhj
+ __ZN6AriSdk37ARI_IBINetTransitInformationRspCb_SDKD1Ev
+ __ZN6AriSdk39ARI_IBICallPsServiceTypeUpdateRspCb_SDK6unpackEv
+ __ZN6AriSdk39ARI_IBICallPsServiceTypeUpdateRspCb_SDKC1EPKhj
+ __ZN6AriSdk39ARI_IBICallPsServiceTypeUpdateRspCb_SDKD1Ev
+ __ZN9DataUtils26getPcscfAddressOverrideKeyEN10subscriber7SimSlotE
+ __os_log_debug_impl
+ _syslog
- ___TUAssertTrigger
CStrings:
+ "#D %!s(MISSING) Cell ID: %!{(MISSING)private}llu"
+ "#D %!s(MISSING) LAC Area code: %!{(MISSING)private}d"
+ "#D %!s(MISSING) PLMN: %!d(MISSING)-%!(BADPREC)%!d(MISSING)"
+ "#D %!s(MISSING) TAC Area code: %!{(MISSING)private}d"
+ "#D %!s(MISSING) name length %!d(MISSING)"
+ "#D %!s(MISSING) was already on!"
+ "#D Adding %!s(MISSING)"
+ "#D Adding LTE band %!d(MISSING)"
+ "#D Adding inputs for 1x"
+ "#D Adding inputs for EVDO"
+ "#D Adding inputs for GSM"
+ "#D Adding inputs for LTE"
+ "#D Adding inputs for UMTS"
+ "#D Adjusting SINR from %!f(MISSING) to %!d(MISSING)u"
+ "#D All technologies: Going to determine if this call should go on"
+ "#D Band %!z(MISSING)u not enabled"
+ "#D Baseband dormancy request sent successfully due to %!s(MISSING): OK"
+ "#D Bootstrapping"
+ "#D Can send DTMF tones in a burst (CDMA)"
+ "#D Cell info MCC (%!d(MISSING)) is the same as the registered PLMN MCC (%!d(MISSING))"
+ "#D Cell info MNC (%!(BADPREC)%!d(MISSING)) is the same as the registered PLMN MNC (%!(BADPREC)%!d(MISSING))"
+ "#D Configuring msimmode:%!d(MISSING) dataslot:%!d(MISSING)"
+ "#D Converted EcIo threshold %!f(MISSING) to level threshold %!u(MISSING)"
+ "#D Converted EcNo threshold %!f(MISSING) to level threshold %!u(MISSING)"
+ "#D Converted RSCP threshold %!f(MISSING) to level threshold %!u(MISSING)"
+ "#D Converted RSRP threshold %!f(MISSING) to level threshold %!u(MISSING)"
+ "#D Converted RSRQ threshold %!f(MISSING) to level threshold %!u(MISSING)"
+ "#D Converted RSSI threshold %!f(MISSING) to level threshold %!u(MISSING)"
+ "#D Converted SINR threshold %!f(MISSING) to level threshold %!u(MISSING)"
+ "#D Converted SNR threshold %!f(MISSING) to level threshold %!u(MISSING)"
+ "#D Does not have line control information. So not telling call to go active"
+ "#D Empty driver info"
+ "#D Extracted MEID = %!s(MISSING)"
+ "#D Found %!u(MISSING) 1x cells"
+ "#D Found %!u(MISSING) EVDO cells"
+ "#D Found %!u(MISSING) GSM cells"
+ "#D Found %!u(MISSING) LTE Neighbor cells"
+ "#D Found %!u(MISSING) TDS cells"
+ "#D Found %!u(MISSING) UMTS cells"
+ "#D Found %!u(MISSING) extended LTE cells"
+ "#D Found CSG indicator"
+ "#D Global switch %!s(MISSING)"
+ "#D Got Remote Party Name (via CallerName) of %!s(MISSING)"
+ "#D Got Remote Party Number of %!s(MISSING) with PI of %!d(MISSING)"
+ "#D Got metric submission from BB"
+ "#D Got trigger submission from BB"
+ "#D IBI Incoming Indication: DISCONNECTED, on slot %!s(MISSING), for call %!u(MISSING), cause %!s(MISSING) (%!u(MISSING))"
+ "#D IBICallCommandDriver::fillUpC2KCallCapabilities"
+ "#D IBICallCommandDriver::fillUpDefaultCallCapabilities"
+ "#D IBICallCommandDriver::fillUpGSMCallCapabilities"
+ "#D IBICallCsVoimsANBRIndCb: nInstance_t1=%!d(MISSING)"
+ "#D IBICallCsVoimsANBRProhibitTimerIndCb: nInstance_t1=%!d(MISSING)"
+ "#D IBICallPsActivateStatusIndCb: nInstance_t1=%!d(MISSING)"
+ "#D IBINetCellularSwitchStatusReq VoWiFiProv %!s(MISSING) reported successfully"
+ "#D Ignore flow indication with empty payload"
+ "#D Ignore flow indication without header or payload"
+ "#D Looking at mask 0x%!l(MISSING)lx"
+ "#D MEID not available"
+ "#D Mapped level %!d(MISSING) to SNR value %!f(MISSING)"
+ "#D Mapped level %!u(MISSING) to EcIo value %!f(MISSING)"
+ "#D Mapped level %!u(MISSING) to EcNo value %!f(MISSING)"
+ "#D Mapped level %!u(MISSING) to RSCP value %!f(MISSING)"
+ "#D Mapped level %!u(MISSING) to RSRP value %!f(MISSING)"
+ "#D Mapped level %!u(MISSING) to RSRQ value %!f(MISSING)"
+ "#D Mapped level %!u(MISSING) to RSSI value %!f(MISSING)"
+ "#D Mapped level %!u(MISSING) to SINR value %!f(MISSING)"
+ "#D Metric submission for app: %!s(MISSING), triggerRef: %!d(MISSING), profileId: %!d(MISSING), metricId: %!d(MISSING), packetLength: %!d(MISSING), packetNumber: %!d(MISSING), isLastPacket: %!d(MISSING), isLastSegment: %!d(MISSING), piiUsed: %!d(MISSING), locationUsed: %!d(MISSING)"
+ "#D Polarity is false. So not telling call to go active"
+ "#D Preferred technology specified by BB: GSM"
+ "#D Received Geo Plmn info indication"
+ "#D Received audio statistics indication"
+ "#D Received distortion indication."
+ "#D Registering for V1"
+ "#D Resetting call related state!"
+ "#D SMS TPDU Length: %!z(MISSING)u, Phone Number: %!s(MISSING), Alpha: %!s(MISSING)"
+ "#D Send tagged info not supported"
+ "#D Sending Activation"
+ "#D Sending CancelMessageTx"
+ "#D Sending Deactivation"
+ "#D Sending DiagCmd"
+ "#D Sending GPSDataUpdate"
+ "#D Sending GetCapabilities"
+ "#D Sending GetServiceInfo"
+ "#D Sending InitiateRegistration"
+ "#D Sending MessageRXAck"
+ "#D Sending MessageTX"
+ "#D Sending Resume"
+ "#D Sending SetBroadcastInfoBlob"
+ "#D Sending SetConcurrencyConfig"
+ "#D Sending SetSecurityConfig"
+ "#D Sending Suspend"
+ "#D Sending pdp statistics; PDP=%!u(MISSING) CID=%!u(MISSING) TX=%!u(MISSING) RX=%!u(MISSING)"
+ "#D Setting emergency mode.."
+ "#D Setting filters success for interface %!d(MISSING)"
+ "#D Source does't not still exists. We will create one now."
+ "#D Source still exists, so end it!"
+ "#D Started"
+ "#D Starting"
+ "#D Stopped"
+ "#D Successfully sent IBINetTransitInformationReq with in metro status: %!s(MISSING)"
+ "#D There is no caller name information"
+ "#D Trigger submission for app: %!s(MISSING), triggerRef: 0x%!x(MISSING), triggerType: %!d(MISSING), triggerId: 0x%!x(MISSING), componentId: 0x%!x(MISSING), triggerTime: %!l(MISSING)ld"
+ "#D Trimming SNR from %!f(MISSING) to %!f(MISSING) for LTE"
+ "#D Turning it on now!"
+ "#D Unhandled LQM bitmask: 0x%!x(MISSING)"
+ "#D Unhandled LQM command type: %!s(MISSING) (%!u(MISSING))"
+ "#D Waiting for IBIMSimConfigIndCb indication"
+ "#D Waiting for IBIMapModemInstanceToSimIndCb indication"
+ "#D Zero length %!s(MISSING) operator name"
+ "#D [App %!h(MISSING)hu] Added configuration %!s(MISSING)"
+ "#D [App %!h(MISSING)hu] Clear configuration %!s(MISSING)"
+ "#D [App %!h(MISSING)hu] Metric query %!s(MISSING)"
+ "#D [App %!h(MISSING)hu] Metric submission %!s(MISSING): %!s(MISSING)"
+ "#D [App %!h(MISSING)hu] Querying metric, component: 0x%!x(MISSING), submissionId: 0x%!x(MISSING), triggerId: 0x%!x(MISSING)"
+ "#D [App %!h(MISSING)hu] Querying metric, triggerRef: 0x%!x(MISSING), triggerType: %!d(MISSING), triggerId: 0x%!x(MISSING), profileId: 0x%!x(MISSING), metricId 0x%!x(MISSING)"
+ "#D [App %!h(MISSING)hu] Requesting metric submission to be %!s(MISSING)"
+ "#D [App %!h(MISSING)hu] Requesting to add configuration type: %!s(MISSING), payload size: %!l(MISSING)u"
+ "#D [App %!h(MISSING)hu] Requesting to clear configuration for app: %!s(MISSING)"
+ "#D [App %!h(MISSING)hu] Requesting to update properties"
+ "#D [App %!h(MISSING)hu] Update properties %!s(MISSING)"
+ "#D app %!d(MISSING) of type %!s(MISSING) is activated, chan %!d(MISSING)"
+ "#D appInfo is null"
+ "#D appInfoExt is null"
+ "#D enable=%!s(MISSING) cid=%!d(MISSING), ip_type=%!d(MISSING), protocol = %!d(MISSING), num_ports=%!d(MISSING)"
+ "#D isEmbedded: %!d(MISSING)"
+ "#D sendPortFiltersRequest: enable=%!s(MISSING) cid=%!d(MISSING)"
+ "#E Cannot unpack IBICallPsServiceTypeUpdateRspCb"
+ "#E IBICallPsServiceTypeUpdateRspCb failed, result: %!d(MISSING)"
+ "#E IBICallPsServiceTypeUpdateRspCb: NACK"
+ "#I %!s(MISSING): Mapping MAX ATTEMPTS TIMED OUT error to 3GPP error type"
+ "#I Activating turbo mode: sending request to bb"
+ "#I DiagCmd succeeded"
+ "#I Received DiagCmd indication"
+ "#I Sending InMetroStatus: %!s(MISSING)"
+ "#I Successfully activated turbo mode in bb."
+ "#I connMask = 0x%!l(MISSING)lx, serviceMask = 0x%!x(MISSING)"
+ "#N Could not unpack CsiIceAudDistortionInfoIndCb: %!s(MISSING) (%!d(MISSING))"
+ "#N Could not unpack CsiIceAudStatsInfoIndCb: %!s(MISSING) (%!d(MISSING))"
+ "#N Could not unpack IBICallPsWrmSAInfoRsp: %!s(MISSING) (%!d(MISSING))"
+ "#N Could not unpack IBINetBBTurboModeRspCb response: %!s(MISSING) (%!d(MISSING))"
+ "#N Could not unpack IBINetTransitInformationRspCb response: %!s(MISSING) (%!d(MISSING))"
+ "#N IBINetBBTurboModeRspCb::Request returned error:"
+ "#N IBINetTransitInformationRspCb::Request returned error:"
+ "/AppleInternal/Library/BuildRoots/e20a253b-8c72-11ef-890e-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Stewie/IBI/IBIStewieCommandDriver.cpp"
+ "AMR-NB 10.2"
+ "AMR-NB 12.2"
+ "AMR-NB 4.75"
+ "AMR-NB 5.15"
+ "AMR-NB 5.9"
+ "AMR-NB 6.7"
+ "AMR-NB 7.4"
+ "AMR-NB 7.95"
+ "AMR-WB 12.65"
+ "AMR-WB 14.25"
+ "AMR-WB 15.85"
+ "AMR-WB 18.25"
+ "AMR-WB 19.85"
+ "AMR-WB 23.05"
+ "AMR-WB 23.85"
+ "AMR-WB 6.6"
+ "AMR-WB 8.85"
+ "Assertion failure: ( %!s(MISSING) ), in file %!s(MISSING), line: %!d(MISSING)"
+ "AudioDistortionAverageSpeechLoss"
+ "AudioDistortionContinuousSpeechLoss"
+ "AudioDistortionRxHighNoise"
+ "AudioDistortionRxLinkBroken"
+ "AudioDistortionRxLowEnergy"
+ "AudioDistortionRxZeros"
+ "AudioDistortionTxHighNoise"
+ "AudioDistortionTxLowEnergy"
+ "AudioDistortionTxZeros"
+ "Could not unpack IBINetCellularSwitchStatusRsp VoWiFiProv %!s(MISSING): %!s(MISSING) (%!d(MISSING))"
+ "DiagCmd"
+ "Failed to activate turbo mode in bb."
+ "Failed to execute DiagCmd. Client is not ready"
+ "IBINetCellularSwitchStatusReq VoWiFiProv %!s(MISSING) failed"
+ "IBINetCellularSwitchStatusReq VoWiFiProv %!s(MISSING) reporting failed. Result: %!d(MISSING)"
+ "IBI_CALL_PS_RESULT_CODE_MAX_ATTEMPTS_TIMED_OUT"
+ "Invalid data received for DiagCmd indication. Reported length: %!u(MISSING), available data length: %!z(MISSING)u"
+ "Invalid data received for DiagCmd response. Reported length: %!u(MISSING), available data length: %!z(MISSING)u"
+ "No Distortion"
+ "Off"
+ "On"
+ "Received DiagCmd indication with error code:%!d(MISSING) (%!s(MISSING))"
+ "error"
+ "kAudioVocoder4GVNB"
+ "kAudioVocoder4GVNW"
+ "kAudioVocoder4GVWB"
+ "kAudioVocoderAMR"
+ "kAudioVocoderAMRWithBWE"
+ "kAudioVocoderEAMR"
+ "kAudioVocoderEFR"
+ "kAudioVocoderEFRWithBWE"
+ "kAudioVocoderEVRC"
+ "kAudioVocoderEVRCB"
+ "kAudioVocoderEVRCBWithBWE"
+ "kAudioVocoderEVS"
+ "kAudioVocoderFR"
+ "kAudioVocoderFRWithBWE"
+ "kAudioVocoderHR"
+ "kAudioVocoderHRWithBWE"
+ "kAudioVocoderQCELP13"
+ "kAudioVocoderUnknown"
+ "kAudioVocoderWAMR"
+ "kDataTransferTimeEnabled"
+ "kDownloadThroughput"
+ "kLinkPowerCost"
+ "kLinkQualityFingerprint"
+ "kLinkState"
+ "kNone"
+ "kTrafficClass"
- "/AppleInternal/Library/BuildRoots/ab5caff2-8bcd-11ef-a07c-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "totalNumOfSegments > 0"

```
