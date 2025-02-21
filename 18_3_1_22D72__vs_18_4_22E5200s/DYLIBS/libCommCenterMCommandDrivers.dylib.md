## libCommCenterMCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib`

```diff

-12227.1.1.0.0
-  __TEXT.__text: 0x222ec4
-  __TEXT.__auth_stubs: 0x2a90
+12317.2.0.0.0
+  __TEXT.__text: 0x226fd8
+  __TEXT.__auth_stubs: 0x2b00
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0xb18f
-  __TEXT.__gcc_except_tab: 0x1d890
-  __TEXT.__const: 0x25578
-  __TEXT.__oslogstring: 0x16e96
-  __TEXT.__unwind_info: 0xe720
-  __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0xb218
-  __AUTH_CONST.__auth_got: 0x1550
-  __AUTH_CONST.__const: 0x21088
-  __AUTH_CONST.__cfstring: 0x200
+  __TEXT.__const: 0x258b0
+  __TEXT.__cstring: 0xb9c4
+  __TEXT.__gcc_except_tab: 0x1ea34
+  __TEXT.__oslogstring: 0x193db
+  __TEXT.__unwind_info: 0xe928
+  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__const: 0xb340
+  __AUTH_CONST.__auth_got: 0x1588
+  __AUTH_CONST.__const: 0x21298
+  __AUTH_CONST.__cfstring: 0x220
   __DATA.__data: 0x58
   __DATA.__bss: 0x1
   __DATA_DIRTY.__common: 0x4

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 12172
-  Symbols:   14607
-  CStrings:  3910
+  Functions: 12141
+  Symbols:   14689
+  CStrings:  4169
 
Symbols:
+ _CFPreferencesCopyValue
+ __Z8asString18DataConnectionType
+ __Z8asString19DataConnectionState
+ __ZN23SetupEventNotificationsD1Ev
+ __ZN3awd8asStringENS_11PayloadTypeE
+ __ZN3ctu2cf6assignERNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKv
+ __ZN9DataUtils26getPcscfAddressOverrideKeyEN10subscriber7SimSlotE
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ __os_log_debug_impl
+ _syslog
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- ___TUAssertTrigger
CStrings:
+ "#D %s client started, but some clients are still not ready"
+ "#D %s client stopped, but some clients are still active"
+ "#D %s system status reporting"
+ "#D %s was already on!"
+ "#D %s, len %zu (0x%lX), %s"
+ "#D %s: received segment #%d (of %d total segments)"
+ "#D %s: sending segment #%d (of %zu total segments)"
+ "#D 1x is enabled in RAT selection"
+ "#D <%p> deregistered"
+ "#D <%p> registered"
+ "#D AKA response success; reporting result"
+ "#D ANBRDeregisterFilter was successful"
+ "#D ANBRQueryBitrate was successful"
+ "#D ANBRRegisterFilter was successful"
+ "#D Adding %s active band %lu"
+ "#D Adding %s band mask 0x%016llx"
+ "#D All technologies: Going to determine if this call should go on"
+ "#D Audio logging enabled succeeded"
+ "#D Audio stat disabled succeeded"
+ "#D BB returned UTF 16 characters data. Taking this data."
+ "#D BB returned UTF 16 characters data. Taking this value as the data."
+ "#D BB returned simple (non UTF 16/extended characters) data"
+ "#D BB returned simple (non-extended chars) data"
+ "#D BSP QMI Client is entering low power"
+ "#D BSP QMI Client is exiting low power"
+ "#D Band %zu not enabled"
+ "#D Binding"
+ "#D Binding NAS subscription succeeded"
+ "#D Binding USSD subscription succeeded"
+ "#D Binding subscription not supported by the device"
+ "#D Binding subscription succeeded"
+ "#D Bootstrapping"
+ "#D Bulk hints request succeeded"
+ "#D CS-PS Attach preference request succeeded"
+ "#D Call preference update successfully completed"
+ "#D Can send DTMF tones in a burst"
+ "#D Cancelling ongoing USSD Session"
+ "#D Cannot send DTMF tones in a burst, so send 1 at a time"
+ "#D Cell Monitor IndicationRegister succeeded"
+ "#D Clear configuration %s"
+ "#D Client started"
+ "#D Client stopped"
+ "#D Coding scheme for USSD Ind is UCS2, converting"
+ "#D Command Driver is trying to send end call audio for call: %s"
+ "#D CongestionInd simSlot %s"
+ "#D Decoding %d to %hhu"
+ "#D Do not send VoLTE call type to baseband."
+ "#D Does not have LineControl TLV or polarity is false. So not telling call to go active"
+ "#D EAP-AKA response success; reporting result"
+ "#D EAP-SIM response success; reporting result"
+ "#D EVDO is enabled in RAT selection"
+ "#D Enabling band %zu at bands[%zu] = 0x%lx"
+ "#D End indication is parsed. RadioCallId we will look up in map is: %d"
+ "#D Enter E911 state successful"
+ "#D EurekaCallCommandDriver::fillUpC2KCallCapabilities"
+ "#D EurekaCallCommandDriver::fillUpDefaultCallCapabilities"
+ "#D EurekaCallCommandDriver::fillUpGSMCallCapabilities"
+ "#D Failed to set profile because profiles were locked"
+ "#D Formatter needs to be set."
+ "#D GBA-BS response success; reporting result"
+ "#D GSM is enabled in RAT selection"
+ "#D Get Cell Info request succeeded"
+ "#D Get NR disable status succeeded"
+ "#D Get PLMN Name succeeded"
+ "#D Get System Selection succeeded"
+ "#D GetANBRProhibitTimerInfo was successful"
+ "#D Getting current data system status"
+ "#D Got PII/Location used message from BB: appid= 0x%x, cid=0x%x, trid=0x%x, sid=0x%x, profid=0x%x, pa:%d la:%d pu:%d lu:%d"
+ "#D Got PII/Location used message from BB: cid=0x%x, trid=0x%x, sid=0x%x, profid=0x%x, pa:%d la:%d pu:%d lu:%d"
+ "#D Got Remote Party Name (via CallerName) of %s"
+ "#D Got Remote Party Name (via DisplayBuffer) of %s"
+ "#D Got Remote Party Number of %s with PI of %d"
+ "#D Got a call status notif. Is there a settings call going on? %s"
+ "#D Got configuration success message from BB: profid=0x%x, %d"
+ "#D Got finish submission from BB: appid=0x%x, cid=0x%x, trid=0x%x, profid=0x%x, sid=0x%x"
+ "#D Got finish submission from BB: cid=0x%x, trid=0x%x, profid=0x%x, sid=0x%x"
+ "#D Got metric submission from BB: appid=0x%x, cid=0x%x, trid=0x%x, profid=0x%x, metricid=0x%x, sid=0x%x, %d, %d bytes"
+ "#D Got metric submission from BB: cid=0x%x, trid=0x%x, profid=0x%x, sid=0x%x, %d, %d bytes"
+ "#D Got trigger submission from BB: appid= 0x%x, cid=0x%x, trid=0x%x, sid=0x%x, profid=0x%x, %lld"
+ "#D Got trigger submission from BB: cid=0x%x, trid=0x%x, sid=0x%x, profid=0x%x, %lld"
+ "#D I2S Clock Rate: 0x%x"
+ "#D IMS call status update successfully completed"
+ "#D IMS-GBA-NAF response success; reporting result"
+ "#D Ignoring camped indication, because of rat %s"
+ "#D Ignoring enhanced voice LQM TLV due to presence of legacy voice LQM TLV"
+ "#D Ignoring legacy OTASP value"
+ "#D Indication reports handover for call id: %d"
+ "#D Informing AWD location was used by BB"
+ "#D Init"
+ "#D Invalidate cache request succeeded"
+ "#D LTE is enabled in RAT selection"
+ "#D LinkStats request success for pdp %d"
+ "#D Metric query %s"
+ "#D Metric submission %s %s"
+ "#D NAS end call reason TLV not supported"
+ "#D NR Cell ID lsb: 0x%08x"
+ "#D NR Cell ID msb: 0x%08x"
+ "#D NR NonStandAlone is enabled in RAT selection"
+ "#D NR StandAlone is enabled in RAT selection"
+ "#D NR is enabled in RAT selection"
+ "#D No handover related items in indication"
+ "#D Number of active calls ended now are: %d"
+ "#D Number of active calls ended so far are: %d"
+ "#D PDC client not ready yet"
+ "#D PDC client not stopped yet"
+ "#D PhsStatusInfo %d request: success"
+ "#D ProceedWithSubscriptionChange request successful"
+ "#D QMI BSP Send AP Status for screen was successful"
+ "#D QMI BSP Send AP Status for sleep was successful"
+ "#D QMI BSP Send AP Status for tethering status was successful"
+ "#D QMI client has started"
+ "#D QMI client has stopped"
+ "#D QMI clients created"
+ "#D QMI clients started"
+ "#D QMI clients stopped"
+ "#D Query for bandwidth info"
+ "#D Querying metric, component: 0x%x, submissionId: 0x%x, triggerId: 0x%x"
+ "#D Received Geo MCC fetch indication"
+ "#D Received Geo Plmn info indication"
+ "#D Received NR disable status indication"
+ "#D Received audio statistics indication"
+ "#D Received current sys info from baseband"
+ "#D Received distortion indication."
+ "#D Received frequency report indication"
+ "#D Received frequency report response"
+ "#D Received vocoder info indication"
+ "#D Received vocoder info response"
+ "#D Register for NAS indications succeeded"
+ "#D Register for indications succeeded"
+ "#D Register request %s"
+ "#D Registering for UI info indication"
+ "#D Removing vinyl transaction %s"
+ "#D Requesting metric submission to be %s"
+ "#D Requesting to add configuration type: %s, payload size: %lu"
+ "#D Requesting to clear configuration"
+ "#D Requesting to update properties"
+ "#D Send VoLTE call status info was successful"
+ "#D Send tagged info not supported"
+ "#D Send wds::notifyCellularDataSwitchingAllowed::Request allowed = %d"
+ "#D Sending Activation"
+ "#D Sending CancelMessageTX"
+ "#D Sending DTMF tones in a burst"
+ "#D Sending Deactivation"
+ "#D Sending DiagCmd"
+ "#D Sending GPSDataUpdate"
+ "#D Sending GetCapabilities"
+ "#D Sending GetCellularTxDeferTime"
+ "#D Sending GetServiceInfo"
+ "#D Sending InitiateRegistration"
+ "#D Sending MessageRXAck"
+ "#D Sending MessageTX"
+ "#D Sending Resume"
+ "#D Sending SetBroadcastInfoBlob"
+ "#D Sending SetCellularDataStatusInfo %s request"
+ "#D Sending SetConcurrencyConfig"
+ "#D Sending SetGPSVisibility - areGPSSatsVisible: %s"
+ "#D Sending SetSecurityConfig"
+ "#D Sending Suspend"
+ "#D Sending cell avoidance request successful"
+ "#D Sending pdp statistics; PDP=%u TX=%u RX=%u"
+ "#D Sending read record for id: %d in %s file 0x%04x"
+ "#D Sending reportPhsClients %d request"
+ "#D Sending stop DTMF? Burst? %d, DtmfType: %d"
+ "#D Sending user response to USSD Request/Indication. Response: %s"
+ "#D Set 2G %s succeeded"
+ "#D Set 3G enable succeeded"
+ "#D Set 5G %s mode succeeded"
+ "#D Set 5G Standalone %s succeeded"
+ "#D Set LTE enable succeeded"
+ "#D Set System Selection succeeded"
+ "#D Set emergency mode succeeded"
+ "#D Set%s(%s, %s)"
+ "#D SetAntennaPreference succeeded"
+ "#D SetCellularDataStatusInfo %s request: success"
+ "#D SetCoalescing was successful"
+ "#D Source does't not still exists. We will create one now."
+ "#D Source still exists, so end it!"
+ "#D Starting client"
+ "#D Successful Response to NotifyDataService"
+ "#D Successfully activated turbo mode: sent ActivateTurboMode Activate: true"
+ "#D Successfully sent InMetroStatus TransitClassiferInfo to: %s"
+ "#D Successfully set battery saver mode to: %s"
+ "#D SystemStatusChange response received successfully"
+ "#D SystemStatusReport indication received"
+ "#D TDSCDMA is enabled in RAT selection"
+ "#D There is no caller name information"
+ "#D Transaction[txid=%d] no longer exists, cannot cancel."
+ "#D Transaction[txid=%d] no longer exists, cannot finish"
+ "#D Transaction[txid=%d] no longer exists, cannot finish data."
+ "#D Transaction[txid=%d] no longer exists, cannot finish with firmware update data"
+ "#D Transaction[txid=%d] no longer exists, cannot finish with profileId %s"
+ "#D Transaction[txid=%d] no longer exists, cannot finish with result %d"
+ "#D Turning it on now!"
+ "#D UMTS is enabled in RAT selection"
+ "#D Update IMS Status succeeded"
+ "#D Update SA Info succeeded"
+ "#D Update properties %s"
+ "#D VinylQMICommandDriver: QMI client started"
+ "#D VinylQMICommandDriver: manager signals ready=%d"
+ "#D VinylQMICommandDriver::init_sync: creating QMI client"
+ "#D Voice call status indication"
+ "#D VoiceStatus indication has RemotePartyNumber, parsing"
+ "#D We already sent one request to end active/accept waiting so ignoring the request to send another"
+ "#D Write security attributes: Attribute %d, Mask %d"
+ "#D [App %hhu] Metric submission %s %s"
+ "#D [App %hhu] Requesting metric submission to be %s"
+ "#D get UI info"
+ "#D handleQMIClientStarted_sync()"
+ "#D isBootstrap: %d"
+ "#D isEmbedded: %d"
+ "#D query card status"
+ "#D query eos status"
+ "#D sending wds::NotifyDataService::Request %s %s"
+ "#D setGPSVisibility successful"
+ "#D start"
+ "#D transientCamping=%s, status=%s, domainValid=%d, domain=%s, rat=%s"
+ "#D vocoder info: %x, %x"
+ "#I %s: PCSCF address substituted with %s"
+ "#I %s: Received UL Congestion Indication: Ifconfig congestion bottleneck %d"
+ "#I Activating Turbo Mode: Sending Activate: true"
+ "#I DiagCmd succeeded"
+ "#I Received DiagCmd indication"
+ "#I UL Ifconfig Congestion Bottleneck state change from %d to %d"
+ "#N Turbo Mode Activation: ActivateTurboMode::Request returned error: %s"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CSI/Modules/CallModule/EurekaC2KCallFormatter.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/AQM/QMIAQMCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Activation/QMIActivationCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Awd/QMIAwdCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/DataSubscription/QMIDataSubscriptionCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Dormancy/QMIDormancyCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/MavCommandDriversFactory.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/QMIClientPool.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/QMIClientPool.h"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/STK/QMI_STK_Helper.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/SignalStrength/QMISignalStrengthCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/EURSubscriberSimCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Stewie/QMI/QMIStewieCommandDriver.cpp"
+ "Assertion failure: ( %s ), in file %s, line: %d"
+ "Failed to execute DiagCmd. Client is not ready"
+ "Failed to execute DiagCmd. Error code:0x%x (%s)"
+ "LTE"
+ "NR"
+ "Received DiagCmd indication with error code:0x%x (%s)"
+ "com.apple.commcenter"
+ "disable"
+ "enable"
+ "error"
+ "failed"
+ "handleUlHealthIfconfigCongestionBottleneck_sync"
+ "kLimited"
+ "kLimitedRegional"
+ "kPowerSave"
+ "kService"
+ "kSysServiceDomainCSOnly"
+ "kSysServiceDomainCSPS"
+ "kSysServiceDomainCamped"
+ "kSysServiceDomainNoService"
+ "kSysServiceDomainPSOnly"
+ "kUnauthorized"
+ "setGPSVisibility failed: %d (%s)"
+ "succeeded"
+ "uim::sendSimApdu, block"
+ "uim::sendSimApdu, single cmnd"
- "#I %s: Received UL Congestion Indication: tcp bottleneck %d"
- "#I Turbo mode not supported on this platform."
- "handleUlHealthTCPBottleneck_sync"
- "totalNumOfSegments > 0"

```
