## libCommCenterKCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib`

```diff

-12084.3.0.0.0
-  __TEXT.__text: 0x121fd4
-  __TEXT.__auth_stubs: 0x72c0
-  __TEXT.__gcc_except_tab: 0x13578
-  __TEXT.__const: 0x15e2f
-  __TEXT.__oslogstring: 0x13bc5
-  __TEXT.__cstring: 0x44a5
-  __TEXT.__unwind_info: 0x6b58
+12088.0.0.0.0
+  __TEXT.__text: 0x11dd78
+  __TEXT.__auth_stubs: 0x7200
+  __TEXT.__gcc_except_tab: 0x13348
+  __TEXT.__const: 0x15d7f
+  __TEXT.__oslogstring: 0x1277b
+  __TEXT.__cstring: 0x4380
+  __TEXT.__unwind_info: 0x6aa8
   __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0x9b0
-  __AUTH_CONST.__auth_got: 0x3968
-  __AUTH_CONST.__const: 0x10490
+  __AUTH_CONST.__auth_got: 0x3908
+  __AUTH_CONST.__const: 0x10408
   __AUTH_CONST.__cfstring: 0x120
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 5286
-  Symbols:   7559
-  CStrings:  2309
+  Functions: 5246
+  Symbols:   7510
+  CStrings:  2171
 
Symbols:
+ ___TUAssertTrigger
- __ZN3awd8asStringENS_11PayloadTypeE
- __ZN3awd8asStringENS_5AppIDE
- __ZN3ctu2cf6assignERNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKv
- __ZN6AriSdk28ARI_IBIStwDiagCommandReq_SDKC1Ev
- __ZN6AriSdk28ARI_IBIStwDiagCommandReq_SDKD1Ev
- __ZN6AriSdk30ARI_IBIStwDiagCommandIndCb_SDK6unpackEv
- __ZN6AriSdk30ARI_IBIStwDiagCommandIndCb_SDKC1EPKhj
- __ZN6AriSdk30ARI_IBIStwDiagCommandIndCb_SDKD1Ev
- __ZN6AriSdk30ARI_IBIStwDiagCommandRspCb_SDKC1EPKhj
- __ZN6AriSdk30ARI_IBIStwDiagCommandRspCb_SDKD1Ev
- __ZN9DataUtils26getPcscfAddressOverrideKeyEN10subscriber7SimSlotE
- __os_log_debug_impl
- _syslog
CStrings:
+ "/AppleInternal/Library/BuildRoots/69ce826a-553c-11ef-9150-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "totalNumOfSegments > 0"
- "#D %!s(MISSING) Cell ID: %!{(MISSING)private}llu"
- "#D %!s(MISSING) LAC Area code: %!{(MISSING)private}d"
- "#D %!s(MISSING) PLMN: %!d(MISSING)-%!(BADPREC)%!d(MISSING)"
- "#D %!s(MISSING) TAC Area code: %!{(MISSING)private}d"
- "#D %!s(MISSING) name length %!d(MISSING)"
- "#D %!s(MISSING) was already on!"
- "#D Adding %!s(MISSING)"
- "#D Adding LTE band %!d(MISSING)"
- "#D Adding inputs for 1x"
- "#D Adding inputs for EVDO"
- "#D Adding inputs for GSM"
- "#D Adding inputs for LTE"
- "#D Adding inputs for UMTS"
- "#D Adjusting SINR from %!f(MISSING) to %!d(MISSING)u"
- "#D All technologies: Going to determine if this call should go on"
- "#D Band %!z(MISSING)u not enabled"
- "#D Baseband dormancy request sent successfully due to %!s(MISSING): OK"
- "#D Bootstrapping"
- "#D Can send DTMF tones in a burst (CDMA)"
- "#D Cell info MCC (%!d(MISSING)) is the same as the registered PLMN MCC (%!d(MISSING))"
- "#D Cell info MNC (%!(BADPREC)%!d(MISSING)) is the same as the registered PLMN MNC (%!(BADPREC)%!d(MISSING))"
- "#D Configuring msimmode:%!d(MISSING) dataslot:%!d(MISSING)"
- "#D Converted EcIo threshold %!f(MISSING) to level threshold %!u(MISSING)"
- "#D Converted EcNo threshold %!f(MISSING) to level threshold %!u(MISSING)"
- "#D Converted RSCP threshold %!f(MISSING) to level threshold %!u(MISSING)"
- "#D Converted RSRP threshold %!f(MISSING) to level threshold %!u(MISSING)"
- "#D Converted RSRQ threshold %!f(MISSING) to level threshold %!u(MISSING)"
- "#D Converted RSSI threshold %!f(MISSING) to level threshold %!u(MISSING)"
- "#D Converted SINR threshold %!f(MISSING) to level threshold %!u(MISSING)"
- "#D Converted SNR threshold %!f(MISSING) to level threshold %!u(MISSING)"
- "#D Does not have line control information. So not telling call to go active"
- "#D Empty driver info"
- "#D Extracted MEID = %!s(MISSING)"
- "#D Found %!u(MISSING) 1x cells"
- "#D Found %!u(MISSING) EVDO cells"
- "#D Found %!u(MISSING) GSM cells"
- "#D Found %!u(MISSING) LTE Neighbor cells"
- "#D Found %!u(MISSING) TDS cells"
- "#D Found %!u(MISSING) UMTS cells"
- "#D Found %!u(MISSING) extended LTE cells"
- "#D Found CSG indicator"
- "#D Global switch %!s(MISSING)"
- "#D Got Remote Party Name (via CallerName) of %!s(MISSING)"
- "#D Got Remote Party Number of %!s(MISSING) with PI of %!d(MISSING)"
- "#D Got metric submission from BB"
- "#D Got trigger submission from BB"
- "#D IBI Incoming Indication: DISCONNECTED, on slot %!s(MISSING), for call %!u(MISSING), cause %!s(MISSING) (%!u(MISSING))"
- "#D IBICallCommandDriver::fillUpC2KCallCapabilities"
- "#D IBICallCommandDriver::fillUpDefaultCallCapabilities"
- "#D IBICallCommandDriver::fillUpGSMCallCapabilities"
- "#D IBICallCsVoimsANBRIndCb: nInstance_t1=%!d(MISSING)"
- "#D IBICallCsVoimsANBRProhibitTimerIndCb: nInstance_t1=%!d(MISSING)"
- "#D IBICallPsActivateStatusIndCb: nInstance_t1=%!d(MISSING)"
- "#D Ignore flow indication with empty payload"
- "#D Ignore flow indication without header or payload"
- "#D Looking at mask 0x%!l(MISSING)lx"
- "#D MEID not available"
- "#D Mapped level %!d(MISSING) to SNR value %!f(MISSING)"
- "#D Mapped level %!u(MISSING) to EcIo value %!f(MISSING)"
- "#D Mapped level %!u(MISSING) to EcNo value %!f(MISSING)"
- "#D Mapped level %!u(MISSING) to RSCP value %!f(MISSING)"
- "#D Mapped level %!u(MISSING) to RSRP value %!f(MISSING)"
- "#D Mapped level %!u(MISSING) to RSRQ value %!f(MISSING)"
- "#D Mapped level %!u(MISSING) to RSSI value %!f(MISSING)"
- "#D Mapped level %!u(MISSING) to SINR value %!f(MISSING)"
- "#D Metric submission for app: %!s(MISSING), triggerRef: %!d(MISSING), profileId: %!d(MISSING), metricId: %!d(MISSING), packetLength: %!d(MISSING), packetNumber: %!d(MISSING), isLastPacket: %!d(MISSING), isLastSegment: %!d(MISSING), piiUsed: %!d(MISSING), locationUsed: %!d(MISSING)"
- "#D Polarity is false. So not telling call to go active"
- "#D Preferred technology specified by BB: GSM"
- "#D Received Geo Plmn info indication"
- "#D Registering for V1"
- "#D Resetting call related state!"
- "#D SMS TPDU Length: %!z(MISSING)u, Phone Number: %!s(MISSING), Alpha: %!s(MISSING)"
- "#D Send tagged info not supported"
- "#D Sending Activation"
- "#D Sending CancelMessageTx"
- "#D Sending Deactivation"
- "#D Sending DiagCmd"
- "#D Sending GPSDataUpdate"
- "#D Sending GetCapabilities"
- "#D Sending GetServiceInfo"
- "#D Sending InitiateRegistration"
- "#D Sending MessageRXAck"
- "#D Sending MessageTX"
- "#D Sending Resume"
- "#D Sending SetBroadcastInfoBlob"
- "#D Sending SetConcurrencyConfig"
- "#D Sending SetSecurityConfig"
- "#D Sending Suspend"
- "#D Sending pdp statistics; PDP=%!u(MISSING) CID=%!u(MISSING) TX=%!u(MISSING) RX=%!u(MISSING)"
- "#D Setting emergency mode.."
- "#D Setting filters success for interface %!d(MISSING)"
- "#D Source does't not still exists. We will create one now."
- "#D Source still exists, so end it!"
- "#D Started"
- "#D Starting"
- "#D Stopped"
- "#D There is no caller name information"
- "#D Trigger submission for app: %!s(MISSING), triggerRef: 0x%!x(MISSING), triggerType: %!d(MISSING), triggerId: 0x%!x(MISSING), componentId: 0x%!x(MISSING), triggerTime: %!l(MISSING)ld"
- "#D Trimming SNR from %!f(MISSING) to %!f(MISSING) for LTE"
- "#D Turning it on now!"
- "#D Unhandled LQM bitmask: 0x%!x(MISSING)"
- "#D Unhandled LQM command type: %!s(MISSING) (%!u(MISSING))"
- "#D Waiting for IBIMSimConfigIndCb indication"
- "#D Waiting for IBIMapModemInstanceToSimIndCb indication"
- "#D Zero length %!s(MISSING) operator name"
- "#D [App %!h(MISSING)hu] Added configuration %!s(MISSING)"
- "#D [App %!h(MISSING)hu] Clear configuration %!s(MISSING)"
- "#D [App %!h(MISSING)hu] Metric query %!s(MISSING)"
- "#D [App %!h(MISSING)hu] Metric submission %!s(MISSING): %!s(MISSING)"
- "#D [App %!h(MISSING)hu] Querying metric, component: 0x%!x(MISSING), submissionId: 0x%!x(MISSING), triggerId: 0x%!x(MISSING)"
- "#D [App %!h(MISSING)hu] Querying metric, triggerRef: 0x%!x(MISSING), triggerType: %!d(MISSING), triggerId: 0x%!x(MISSING), profileId: 0x%!x(MISSING), metricId 0x%!x(MISSING)"
- "#D [App %!h(MISSING)hu] Requesting metric submission to be %!s(MISSING)"
- "#D [App %!h(MISSING)hu] Requesting to add configuration type: %!s(MISSING), payload size: %!l(MISSING)u"
- "#D [App %!h(MISSING)hu] Requesting to clear configuration for app: %!s(MISSING)"
- "#D [App %!h(MISSING)hu] Requesting to update properties"
- "#D [App %!h(MISSING)hu] Update properties %!s(MISSING)"
- "#D app %!d(MISSING) of type %!s(MISSING) is activated, chan %!d(MISSING)"
- "#D appInfo is null"
- "#D appInfoExt is null"
- "#D enable=%!s(MISSING) cid=%!d(MISSING), ip_type=%!d(MISSING), protocol = %!d(MISSING), num_ports=%!d(MISSING)"
- "#D isEmbedded: %!d(MISSING)"
- "#D sendPortFiltersRequest: enable=%!s(MISSING) cid=%!d(MISSING)"
- "#I DiagCmd succeeded"
- "#I Received DiagCmd indication"
- "/AppleInternal/Library/BuildRoots/a9331c2c-4f73-11ef-8db8-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Stewie/IBI/IBIStewieCommandDriver.cpp"
- "Assertion failure: ( %!s(MISSING) ), in file %!s(MISSING), line: %!d(MISSING)"
- "DiagCmd"
- "Failed to execute DiagCmd. Client is not ready"
- "Invalid data received for DiagCmd indication. Reported length: %!u(MISSING), available data length: %!z(MISSING)u"
- "Invalid data received for DiagCmd response. Reported length: %!u(MISSING), available data length: %!z(MISSING)u"
- "Received DiagCmd indication with error code:%!d(MISSING) (%!s(MISSING))"
- "error"
- "kDataTransferTimeEnabled"
- "kDownloadThroughput"
- "kLinkPowerCost"
- "kLinkQualityFingerprint"
- "kLinkState"
- "kNone"
- "kTrafficClass"

```
