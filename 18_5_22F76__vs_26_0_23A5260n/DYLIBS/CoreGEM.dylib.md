## CoreGEM.dylib

> `/System/Library/PrivateFrameworks/CoreGEM.framework/CoreGEM.dylib`

```diff

-10.0.4.0.0
-  __TEXT.__text: 0xd75f0
-  __TEXT.__auth_stubs: 0xaf0
+23.0.0.0.0
+  __TEXT.__text: 0xeeda0
+  __TEXT.__auth_stubs: 0xb00
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0xae30
-  __TEXT.__gcc_except_tab: 0x3a08
-  __TEXT.__cstring: 0x5e10
-  __TEXT.__oslogstring: 0x7e14
-  __TEXT.__unwind_info: 0x38f0
+  __TEXT.__const: 0xb870
+  __TEXT.__gcc_except_tab: 0x4464
+  __TEXT.__cstring: 0x675b
+  __TEXT.__oslogstring: 0x8f04
+  __TEXT.__unwind_info: 0x3f28
   __TEXT.__objc_classname: 0x1a
-  __TEXT.__objc_methname: 0xd4
-  __TEXT.__objc_methtype: 0x37
+  __TEXT.__objc_methname: 0xc6
+  __TEXT.__objc_methtype: 0x34
   __TEXT.__objc_stubs: 0x80
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x495b8
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__const: 0x49690
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x588
-  __AUTH_CONST.__const: 0x80f0
+  __AUTH_CONST.__auth_got: 0x590
+  __AUTH_CONST.__const: 0x8ea0
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x90
   __DATA.__data: 0x10
-  __DATA.__common: 0x10f8
-  __DATA.__bss: 0xf0
+  __DATA.__common: 0x1051
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0x5f8
-  __DATA_DIRTY.__common: 0x140
+  __DATA_DIRTY.__bss: 0x700
+  __DATA_DIRTY.__common: 0x280
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 93F31C24-AAB5-3851-BD4C-BD099F1469A2
-  Functions: 3603
-  Symbols:   226
-  CStrings:  1265
+  UUID: 4864688C-6532-3C31-A974-097DB2BC8362
+  Functions: 4013
+  Symbols:   229
+  CStrings:  1405
 
Symbols:
+ _TelephonyRadiosGetRadioVendor
+ __DefaultRuneLocale
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__16localeC1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ ___toupper
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __Znwm
- _malloc_type_malloc
CStrings:
+ "#cplane,nmeas,%d"
+ "#cplane,scell,num_of_ssb_Index,%d,sfn,%d,pci,%d,cell_id,%d,mcc,%d,mnc,%d,rsrp,%d,rsrq,%d"
+ "#gem,#cplane, ratType,%d"
+ "#gem,#lpp,#cplane,handleDlLppMsg"
+ "#gem,#lpp,#cplane,handleEmergencyPositionReport"
+ "#gem,#lpp,#cplane,lpp msg received"
+ "#gem,#lpp,#cplane,sendEcidMeasError, no response from BB for ECID request"
+ "#gem,#lpp,#cplane,sending lpp msg"
+ "#gem,#lpp,#cplane,startPosRequest"
+ "#gpsd,#cplane,#out,Invalid posProtocol in Pos Response"
+ "#gpsd,#cplane,#posp calling injectNavModel"
+ "#gpsd,#cplane,#posp calling injectRefLocation"
+ "#gpsd,#cplane,#posp calling injectRefTime"
+ "#gpsd,#cplane,#posp calling startPosRequest"
+ "#gpsd,#posp,#lpp,config,gps_support,%{private}d,gps_mode,%{private}d,ecall_ongoing,%{private}d,cplane_support,%{private}d,cp_lr,%{private}d,lte_ecid_support,%{private}d,nr_ecid_support,%{private}d,active_rat,%{private}d"
+ "#gpsd,#supl,#posp calling injectNavModel"
+ "#gpsd,#supl,#posp calling injectRefLocation"
+ "#gpsd,#supl,#posp calling injectRefTime"
+ "#gpsd,#supl,#posp calling startPosRequest"
+ "#input,#nilr,injectReflocationToGnssDevice,refLat,%{private}u,refLon,%{private}u,original uncertainties, %{private}f,semiMinor,%{private}f,%{private}u"
+ "#lpp, Packet to be acked. LPP message not sent"
+ "#lpp, setting RAT to LTE"
+ "#lpp, setting RAT to NR"
+ "#lpp,#cplane,#ecid, Invalid RAT"
+ "#lpp,#cplane,#ecid, LTE Meas error"
+ "#lpp,#cplane,#ecid, LTE neighbouring cell meas,%d"
+ "#lpp,#cplane,#ecid, LTE serving cell meas,rsrp,%{private}lu,rsrq,%{private}lu,ue_tx_rx,%{private}lu,pci,%{private}lu,sfn,%{private}lu,cellId,%{private}lu,mcc,%{private}lu,mnc,%{private}lu"
+ "#lpp,#cplane,#ecid, NR Meas failure"
+ "#lpp,#cplane,#ecid, NR Meas of serving cell"
+ "#lpp,#cplane,#ecid, NR Meas received"
+ "#lpp,#cplane,#ecid, NR Meas success, no of meas,%d"
+ "#lpp,#cplane,#ecid, NR neighbouring cell meas,%d"
+ "#lpp,#cplane,#ecid, Received LTE meas response"
+ "#lpp,#cplane,#ecid, Received LTE meas success, number of meas,%d"
+ "#lpp,#cplane,#ecid, Received meas response"
+ "#lpp,#cplane,#ecid, Received meas response for LTE"
+ "#lpp,#cplane,#ecid, Received meas response for NR"
+ "#lpp,#cplane,#ecid, Received meas response, cancelling timer"
+ "#lpp,#cplane,#ecid, Serving cell meas, pci,%d,,rsrp,%d, rsrq,%d"
+ "#lpp,#cplane,#ecid, sending LTE Meas error, no response for ECID req"
+ "#lpp,#cplane,#ecid, sending NR Meas error, no response for ECID req"
+ "#lpp,#cplane,#pdu,%{private}zu,of,%{private}zu,%{private}s,%{private}s"
+ "#nilr,#cplane, Invalid RAT type received"
+ "#nilr,#cplane, handleEcidResponse,result,%d,lteMeasPresent,%d, %d"
+ "#nilr,#cplane,LTE Meas error present"
+ "#nilr,#cplane,LTE Meas error,cause,%d,detailedCause,%d"
+ "#nilr,#cplane,LTE Meas present"
+ "#nilr,#cplane,NR Meas error,cause,%d,detailedCause,%d"
+ "#nilr,#cplane,NR Meas present"
+ "#nilr,#cplane,copyLteMeasData,received,rsrp,%{private}lu,rsrq,%{private}lu,txrxtime,%{private}lu,pci,%{private}u,mcc,%{private}u,mnc,%{private}u"
+ "#nilr,#cplane,handleCPlaneDlLppMsg"
+ "#nilr,#cplane,handleCPlaneUlLppMsg"
+ "#nilr,#cplane,handleConformanceMode"
+ "#nilr,#cplane,handleConformanceMode,mode,%d"
+ "#nilr,#cplane,handleCplanePosResponse"
+ "#nilr,#cplane,handleEcidResponse"
+ "#nilr,#cplane,ratType LTE"
+ "#nilr,#cplane,ratType NR"
+ "#nilr,#cplane,ratType received"
+ "#nilr,handleEcidReq, indication to CL"
+ "#nilr,sendEphemerisIndicationToCl, indication to CL"
+ "#nilr,sendNilrEndIndication"
+ "#nilr,sendNilrEndIndication, GNSS not running"
+ "#nilr,sendNilrEndIndication, indication to CL"
+ "#nilr,sendNilrStartIndication"
+ "#nilr,sendNilrStartIndication, GNSS already running"
+ "#nilr,sendNilrStartIndication, indication to CL"
+ "#nilr,sendRefLocationIndicationCl, indication to CL"
+ "#nilr,sendRefTimeIndicationToCl, indication to CL"
+ "#nilr,sendRequestLocation, indication to CL"
+ "#supl,#posp,#lpp, Calling lpp_t_supl_pos_trigger"
+ "/AppleInternal/Library/BuildRoots/4~B1cEugClRbzVg2tLurbm7ChWfNtV7QNuFPkwRTY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Emergency/CplaneBridge.mm"
+ "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Protobuf/Generated/CLPGemProtocolGpsd.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Protobuf/Generated/CLPGnssEmergencyLppTypes.pb.cc"
+ "0471001123"
+ "::CoreGem::CLP::LogEntry::Gem::Gpsd::Request_Type_IsValid(value)"
+ "::CoreGem::proto::gnss::Emergency::DiscardReason_IsValid(value)"
+ "::CoreGem::proto::gnss::Emergency::DiscardedMsgType_IsValid(value)"
+ "::CoreGem::proto::gnss::Emergency::MeasResult_IsValid(value)"
+ "::CoreGem::proto::gnss::Emergency::PosMethod_IsValid(value)"
+ "::CoreGem::proto::gnss::Emergency::PosMode_IsValid(value)"
+ "::CoreGem::proto::gnss::Emergency::RatType_IsValid(value)"
+ "@40@0:8@?16@?24@32"
+ "CLPGemProtocolGpsd.pb.h"
+ "CLPGnssEmergencyLppTypes.pb.h"
+ "CoreGem.CLP.LogEntry.Gem.Gpsd.Indication"
+ "CoreGem.CLP.LogEntry.Gem.Gpsd.Request"
+ "CoreGem.CLP.LogEntry.Gem.Gpsd.Response"
+ "CoreGem.proto.gnss.Emergency.ConformanceMode"
+ "CoreGem.proto.gnss.Emergency.DiscardedSessionInfo"
+ "CoreGem.proto.gnss.Emergency.EcidMeasRequest"
+ "CoreGem.proto.gnss.Emergency.EcidMeasResponse"
+ "CoreGem.proto.gnss.Emergency.LppMsg"
+ "CoreGem.proto.gnss.Emergency.LteEcidError"
+ "CoreGem.proto.gnss.Emergency.LteEcidMeasInfo"
+ "CoreGem.proto.gnss.Emergency.LteMeasRequestType"
+ "CoreGem.proto.gnss.Emergency.NilrIndication"
+ "CoreGem.proto.gnss.Emergency.NrEcidError"
+ "CoreGem.proto.gnss.Emergency.NrEcidMeasInfo"
+ "CoreGem.proto.gnss.Emergency.NrMeasRequestType"
+ "CoreGem.proto.gnss.Emergency.NrQuantityResultSsbCellMeas"
+ "CoreGem.proto.gnss.Emergency.NrResultsPerSsbIndex"
+ "CoreGem.proto.gnss.Emergency.SetRatType"
+ "CoreGem.proto.gpsd.InjectRavenOrbitFile"
+ "CplaneBridge.mm"
+ "CplaneLppExecutePosRsp"
+ "DiscardReason:CapabilityMisMatch,"
+ "DiscardReason:NotInEmergency,"
+ "DiscardReason:Unknown, "
+ "DiscardedMsgType:AssistanceData,"
+ "DiscardedMsgType:CapabilityReq,"
+ "DiscardedMsgType:LocationReq,"
+ "DiscardedMsgType:Unknown,"
+ "GEM handleGemRequest,%{public}d"
+ "GEM_PROTOCOL_INDICATION"
+ "GEM_PROTOCOL_REQUEST"
+ "HeloEstimator,GemHeloEstimator::getBestHorizontal, GNSS HUNC after scaling,%f"
+ "HeloEstimator,GemHeloEstimator::getBestHorizontal, GNSS HUNC before scaling,%f"
+ "INJECT_RAVEN_ORBIT_FILE"
+ "LppSessionActiveTimer,#input,cancel the ongoing timer"
+ "LppSessionActiveTimer,#input,created timer,starting timer for,%d,milli seconds"
+ "LppSessionActiveTimer,fTimer NULL"
+ "LppTimer,#input,cancel the ongoing timer"
+ "LppTimer,#input,created timer,starting timer for,%d,milli seconds"
+ "LppTimer,#input,created timer,starting timer for,%d,milli seconds for ECID request"
+ "LppTimer,ECID Req timer expired"
+ "LppTimer,fTimer NULL"
+ "Memory allocation failure,%s"
+ "PosMethod:GNSS,"
+ "PosMethod:LTE_ECID,"
+ "PosMethod:NR_ECID,"
+ "PosMode:MSA,"
+ "PosMode:MSB,"
+ "PosMode:Standalone,"
+ "PosMode:Unknown, "
+ "com.gnss.cplaneq"
+ "com.gnss.gem.timerq"
+ "false && \"Memory allocation failure,%s\""
+ "fill_lpp_data"
+ "handleCPlaneDlLppMsg,pduSize invalid"
+ "handleCPlaneDlLppMsg,pduSize,%d"
+ "handleCPlaneDlLppMsg,sn,%d,pdusize,%d"
+ "handleDiscardedSessionInfo,%s"
+ "initForComm:sendIndicationToRemoteCallback:dispatch_queue_t:"
+ "setModemVendor,modemVendor,%{public}d"
+ "set_discard_reason"
+ "set_discarded_msg_type"
+ "set_meas_result"
+ "set_pos_mode"
+ "set_rat_type"
- "#lpp,#pdu,%{sensitive}zu,of,%{sensitive}zu,%{sensitive}s"
- "#posp,#lpp, Calling lpp_t_supl_pos_trigger"
- "/AppleInternal/Library/BuildRoots/24f0c819-1ca3-11f0-bc1f-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "::CoreGem::proto::gpsd::CntinStatus_IsValid(value)"
- "@44@0:8@?16@?24@32i40"
- "CNTIN_CLOCK_CONTROL"
- "CNTIN_STATUS_UPDATE"
- "CoreGem.proto.gpsd.CntinClockControl"
- "CoreGem.proto.gpsd.CntinStatusMessage"
- "initForComm:sendIndicationToRemoteCallback:dispatch_queue_t:GemDeviceType:"
- "setDeviceType,deviceType,%d"

```
