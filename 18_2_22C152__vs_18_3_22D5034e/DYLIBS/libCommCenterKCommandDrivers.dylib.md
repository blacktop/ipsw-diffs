## libCommCenterKCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib`

```diff

-12214.4.0.0.0
-  __TEXT.__text: 0x121814
-  __TEXT.__auth_stubs: 0x73b0
-  __TEXT.__gcc_except_tab: 0x136fc
-  __TEXT.__const: 0x15f0f
-  __TEXT.__oslogstring: 0x12b89
-  __TEXT.__cstring: 0x4705
-  __TEXT.__unwind_info: 0x6bc0
-  __DATA_CONST.__got: 0x418
+12225.1.0.0.0
+  __TEXT.__text: 0x125930
+  __TEXT.__auth_stubs: 0x7430
+  __TEXT.__gcc_except_tab: 0x13930
+  __TEXT.__const: 0x15fcf
+  __TEXT.__oslogstring: 0x140ec
+  __TEXT.__cstring: 0x4805
+  __TEXT.__unwind_info: 0x6c68
+  __DATA_CONST.__got: 0x420
   __DATA_CONST.__const: 0xa00
-  __AUTH_CONST.__auth_got: 0x39e0
-  __AUTH_CONST.__const: 0x10610
-  __AUTH_CONST.__cfstring: 0x120
+  __AUTH_CONST.__auth_got: 0x3a20
+  __AUTH_CONST.__const: 0x10658
+  __AUTH_CONST.__cfstring: 0x100
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 5295
-  Symbols:   7587
-  CStrings:  2240
+  Functions: 5334
+  Symbols:   7635
+  CStrings:  2382
 
Symbols:
+ __ZN23SetupEventNotificationsD1Ev
+ __ZN3awd8asStringENS_11PayloadTypeE
+ __ZN3awd8asStringENS_5AppIDE
+ __ZN3ctu2cf6assignERNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKv
+ __ZN6AriSdk28ARI_IBIStwDiagCommandReq_SDKC1Ev
+ __ZN6AriSdk28ARI_IBIStwDiagCommandReq_SDKD1Ev
+ __ZN6AriSdk30ARI_IBIStwDiagCommandIndCb_SDK6unpackEv
+ __ZN6AriSdk30ARI_IBIStwDiagCommandIndCb_SDKC1EPKhj
+ __ZN6AriSdk30ARI_IBIStwDiagCommandIndCb_SDKD1Ev
+ __ZN6AriSdk30ARI_IBIStwDiagCommandRspCb_SDKC1EPKhj
+ __ZN6AriSdk30ARI_IBIStwDiagCommandRspCb_SDKD1Ev
+ __ZN9DataUtils26getPcscfAddressOverrideKeyEN10subscriber7SimSlotE
+ __ZTV23SetupEventNotifications
+ __os_log_debug_impl
+ _syslog
- __ZN12capabilities2ct26supportsSTKSendIMSRegEventEv
- __ZN22SetupEventIMSRegNotifyD1Ev
- __ZN22SetupEventUserActivityD1Ev
- __ZN26SetupEventIdleScreenNotifyD1Ev
- __ZN30SetupEventLanguageSelectNotifyD1Ev
- ___TUAssertTrigger
CStrings:
+ "#D %s Cell ID: %{private}llu"
+ "#D %s LAC Area code: %{private}d"
+ "#D %s PLMN: %03d-%0.*d"
+ "#D %s TAC Area code: %{private}d"
+ "#D %s name length %d"
+ "#D %s was already on!"
+ "#D Adding %s"
+ "#D Adding LTE band %d"
+ "#D Adding inputs for 1x"
+ "#D Adding inputs for EVDO"
+ "#D Adding inputs for GSM"
+ "#D Adding inputs for LTE"
+ "#D Adding inputs for UMTS"
+ "#D Adjusting SINR from %.2f to %du"
+ "#D All technologies: Going to determine if this call should go on"
+ "#D Band %zu not enabled"
+ "#D Baseband dormancy request sent successfully due to %s: OK"
+ "#D Bootstrapping"
+ "#D Can send DTMF tones in a burst (CDMA)"
+ "#D Cell info MCC (%03d) is the same as the registered PLMN MCC (%03d)"
+ "#D Cell info MNC (%0.*d) is the same as the registered PLMN MNC (%0.*d)"
+ "#D Configuring msimmode:%d dataslot:%d"
+ "#D Converted EcIo threshold %.2f to level threshold %u"
+ "#D Converted EcNo threshold %.2f to level threshold %u"
+ "#D Converted RSCP threshold %.2f to level threshold %u"
+ "#D Converted RSRP threshold %.2f to level threshold %u"
+ "#D Converted RSRQ threshold %.2f to level threshold %u"
+ "#D Converted RSSI threshold %.2f to level threshold %u"
+ "#D Converted SINR threshold %.2f to level threshold %u"
+ "#D Converted SNR threshold %.2f to level threshold %u"
+ "#D Does not have line control information. So not telling call to go active"
+ "#D Empty driver info"
+ "#D Extracted MEID = %s"
+ "#D Found %u 1x cells"
+ "#D Found %u EVDO cells"
+ "#D Found %u GSM cells"
+ "#D Found %u LTE Neighbor cells"
+ "#D Found %u TDS cells"
+ "#D Found %u UMTS cells"
+ "#D Found %u extended LTE cells"
+ "#D Found CSG indicator"
+ "#D Global switch %s"
+ "#D Got Remote Party Name (via CallerName) of %s"
+ "#D Got Remote Party Number of %s with PI of %d"
+ "#D Got metric submission from BB"
+ "#D Got trigger submission from BB"
+ "#D IBI Incoming Indication: DISCONNECTED, on slot %s, for call %u, cause %s (%u)"
+ "#D IBICallCommandDriver::fillUpC2KCallCapabilities"
+ "#D IBICallCommandDriver::fillUpDefaultCallCapabilities"
+ "#D IBICallCommandDriver::fillUpGSMCallCapabilities"
+ "#D IBICallCsVoimsANBRIndCb: nInstance_t1=%d"
+ "#D IBICallCsVoimsANBRProhibitTimerIndCb: nInstance_t1=%d"
+ "#D IBICallPsActivateStatusIndCb: nInstance_t1=%d"
+ "#D IBINetCellularSwitchStatusReq VoWiFiProv %s reported successfully"
+ "#D Ignore flow indication with empty payload"
+ "#D Ignore flow indication without header or payload"
+ "#D Looking at mask 0x%llx"
+ "#D MEID not available"
+ "#D Mapped level %d to SNR value %.2f"
+ "#D Mapped level %u to EcIo value %.2f"
+ "#D Mapped level %u to EcNo value %.2f"
+ "#D Mapped level %u to RSCP value %.2f"
+ "#D Mapped level %u to RSRP value %.2f"
+ "#D Mapped level %u to RSRQ value %.2f"
+ "#D Mapped level %u to RSSI value %.2f"
+ "#D Mapped level %u to SINR value %.2f"
+ "#D Metric submission for app: %s, triggerRef: %d, profileId: %d, metricId: %d, packetLength: %d, packetNumber: %d, isLastPacket: %d, isLastSegment: %d, piiUsed: %d, locationUsed: %d"
+ "#D Polarity is false. So not telling call to go active"
+ "#D Preferred technology specified by BB: GSM"
+ "#D Received Geo Plmn info indication"
+ "#D Received audio statistics indication"
+ "#D Received distortion indication."
+ "#D Registering for V1"
+ "#D Resetting call related state!"
+ "#D SMS TPDU Length: %zu, Phone Number: %s, Alpha: %s"
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
+ "#D Sending pdp statistics; PDP=%u CID=%u TX=%u RX=%u"
+ "#D Setting emergency mode.."
+ "#D Setting filters success for interface %d"
+ "#D Source does't not still exists. We will create one now."
+ "#D Source still exists, so end it!"
+ "#D Started"
+ "#D Starting"
+ "#D Stopped"
+ "#D Successfully sent IBINetTransitInformationReq with in metro status: %s"
+ "#D There is no caller name information"
+ "#D Trigger submission for app: %s, triggerRef: 0x%x, triggerType: %d, triggerId: 0x%x, componentId: 0x%x, triggerTime: %lld"
+ "#D Trimming SNR from %.2f to %.2f for LTE"
+ "#D Turning it on now!"
+ "#D Unhandled LQM bitmask: 0x%0x"
+ "#D Unhandled LQM command type: %s (%u)"
+ "#D Waiting for IBIMSimConfigIndCb indication"
+ "#D Waiting for IBIMapModemInstanceToSimIndCb indication"
+ "#D Zero length %s operator name"
+ "#D [App %hhu] Added configuration %s"
+ "#D [App %hhu] Clear configuration %s"
+ "#D [App %hhu] Metric query %s"
+ "#D [App %hhu] Metric submission %s: %s"
+ "#D [App %hhu] Querying metric, component: 0x%x, submissionId: 0x%x, triggerId: 0x%x"
+ "#D [App %hhu] Querying metric, triggerRef: 0x%x, triggerType: %d, triggerId: 0x%x, profileId: 0x%x, metricId 0x%x"
+ "#D [App %hhu] Requesting metric submission to be %s"
+ "#D [App %hhu] Requesting to add configuration type: %s, payload size: %lu"
+ "#D [App %hhu] Requesting to clear configuration for app: %s"
+ "#D [App %hhu] Requesting to update properties"
+ "#D [App %hhu] Update properties %s"
+ "#D app %d of type %s is activated, chan %d"
+ "#D appInfo is null"
+ "#D appInfoExt is null"
+ "#D enable=%s cid=%d, ip_type=%d, protocol = %d, num_ports=%d"
+ "#D isEmbedded: %d"
+ "#D s_nssai_t31 not present , set fNetworkAssignedSnssai = NULL"
+ "#D sendPortFiltersRequest: enable=%s cid=%d"
+ "#I DiagCmd succeeded"
+ "#I Received DiagCmd indication"
+ "/AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Stewie/IBI/IBIStewieCommandDriver.cpp"
+ "Assertion failure: ( %s ), in file %s, line: %d"
+ "DiagCmd"
+ "Failed to execute DiagCmd. Client is not ready"
+ "Invalid data received for DiagCmd indication. Reported length: %u, available data length: %zu"
+ "Invalid data received for DiagCmd response. Reported length: %u, available data length: %zu"
+ "Received DiagCmd indication with error code:%d (%s)"
+ "error"
+ "kDataTransferTimeEnabled"
+ "kDownloadThroughput"
+ "kLinkPowerCost"
+ "kLinkQualityFingerprint"
+ "kLinkState"
+ "kNone"
+ "kTrafficClass"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "SupportSimToolkitIMSRegNotifications"
- "totalNumOfSegments > 0"

```
