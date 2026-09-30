## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1526.70.0.0.0
-  __TEXT.__text: 0x2b4ce8
-  __TEXT.__auth_stubs: 0x2530
+1526.75.0.0.0
+  __TEXT.__text: 0x2b5b8c
+  __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x7fbfb
-  __TEXT.__const: 0x7ec70
-  __TEXT.__oslogstring: 0x1f52
-  __TEXT.__unwind_info: 0x5e18
+  __TEXT.__cstring: 0x80035
+  __TEXT.__const: 0x7ee40
+  __TEXT.__oslogstring: 0x1f3b
+  __TEXT.__unwind_info: 0x5e58
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x1298
+  __DATA_CONST.__auth_got: 0x12b0
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x20ab8
+  __DATA_CONST.__const: 0x20b58
   __DATA_CONST.__osclassinfo: 0x388
   __DATA.__data: 0x390
   __DATA.__bss: 0x958

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: EF5F7167-F6B3-399E-B838-F41F32301E51
-  Functions: 13126
-  Symbols:   16341
-  CStrings:  12866
+  UUID: C9B2528F-2A74-32E8-84D6-17D80D271022
+  Functions: 13148
+  Symbols:   16372
+  CStrings:  12883
 
Symbols:
+ _ZN16AppleBCMWLANCore8watchdogEP13CCFaultReport.cold.16
+ _ZN22AppleBCMWLANNetAdapter23configureAggressiveEDCAEb.cold.1
+ _ZN22AppleBCMWLANNetAdapter23configureAggressiveEDCAEb.cold.2
+ _ZN24AppleBCMWLANNANInterface21setNAN_VENDOR_PAYLOADEP29apple80211_nan_vendor_payload.cold.3
+ _ZN24AppleBCMWLANNANInterface22setNAN_ADDITIONAL_ATTREP29apple80211_nan_vendor_payload.cold.1
+ _ZN24AppleBCMWLANNANInterface22setNAN_ADDITIONAL_ATTREP29apple80211_nan_vendor_payload.cold.2
+ _ZN24AppleBCMWLANNANInterface22setNAN_ADDITIONAL_ATTREP29apple80211_nan_vendor_payload.cold.3
+ _ZN24AppleBCMWLANNANInterface22setNAN_ADDITIONAL_ATTREP29apple80211_nan_vendor_payload.cold.4
+ _ZN24AppleBCMWLANNANInterface22setNAN_ADDITIONAL_ATTREP29apple80211_nan_vendor_payload.cold.5
+ _ZN24AppleBCMWLANNANInterface29setNAN_VENDOR_PAYLOAD_COMPACTEP29apple80211_nan_vendor_payload.cold.1
+ _ZN24AppleBCMWLANNANInterface29setNAN_VENDOR_PAYLOAD_COMPACTEP29apple80211_nan_vendor_payload.cold.2
+ _ZN24AppleBCMWLANNANInterface29setNAN_VENDOR_PAYLOAD_COMPACTEP29apple80211_nan_vendor_payload.cold.3
+ _ZN24AppleBCMWLANNANInterface29setNAN_VENDOR_PAYLOAD_COMPACTEP29apple80211_nan_vendor_payload.cold.4
+ _ZN28AppleBCMWLANSkywalkInterface15flushFlowQueuesEP10ether_addr.cold.1
+ __ZL9bw40MHz6g
+ __ZN17IO80211Controller16configIOReporterEP15IODispatchQueue
+ __ZN17IO80211Controller23updateControllerMonitorEP6OSDatajPjPyS3_P18IOMemoryDescriptor
+ __ZN17IO80211Controller32configureControllerMonitorReportEP6OSDatajPj
+ __ZN23IO80211SkywalkInterface12syncDPSStatsEP26apple82011_postMessage_dps
+ __ZN23IO80211SkywalkInterface23getCompanionInterfaceIdEv
+ __ZN23IO80211VirtualInterface15flushFlowQueuesEP10ether_addr
+ __ZN24AppleBCMWLANNANInterface22setNAN_ADDITIONAL_ATTREP29apple80211_nan_vendor_payload
+ __ZN24AppleBCMWLANNANInterface29setNAN_VENDOR_PAYLOAD_COMPACTEP29apple80211_nan_vendor_payload
+ __ZN25AppleBCMWLANBGScanAdapter19isPnoScanConfiguredEv
+ __ZN28AppleBCMWLANSkywalkInterface15flushFlowQueuesEP10ether_addr
+ __ZN28AppleBCMWLANSkywalkInterface8findPeerER10ether_addr
+ __ZN30AppleBCMWLANProximityInterface15flushFlowQueuesEP10ether_addr
+ __ZThn112_N24AppleBCMWLANNANInterface22setNAN_ADDITIONAL_ATTREP29apple80211_nan_vendor_payload
+ __ZThn112_N24AppleBCMWLANNANInterface29setNAN_VENDOR_PAYLOAD_COMPACTEP29apple80211_nan_vendor_payload
+ __ZThn128_N24AppleBCMWLANNANInterface22setNAN_ADDITIONAL_ATTREP29apple80211_nan_vendor_payload
+ __ZThn128_N24AppleBCMWLANNANInterface29setNAN_VENDOR_PAYLOAD_COMPACTEP29apple80211_nan_vendor_payload
+ __ZThn48_N17IO80211Controller16configIOReporterEP15IODispatchQueue
+ __ZThn48_N17IO80211Controller23updateControllerMonitorEP6OSDatajPjPyS3_P18IOMemoryDescriptor
+ __ZThn48_N17IO80211Controller32configureControllerMonitorReportEP6OSDatajPj
+ __ZThn80_N23IO80211SkywalkInterface12syncDPSStatsEP26apple82011_postMessage_dps
+ __ZThn80_N28AppleBCMWLANSkywalkInterface8findPeerER10ether_addr
+ __ZThn96_N23IO80211VirtualInterface15flushFlowQueuesEP10ether_addr
+ __ZThn96_N30AppleBCMWLANProximityInterface15flushFlowQueuesEP10ether_addr
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2269
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2269.cold.1
+ __block_descriptor_tmp.1665
+ __block_descriptor_tmp.1970
+ __block_descriptor_tmp.2267
+ __block_descriptor_tmp.2289
+ __block_descriptor_tmp.2323
+ __block_descriptor_tmp.2652
+ __block_descriptor_tmp.2688
+ __block_descriptor_tmp.3152
+ __block_descriptor_tmp.3235
+ __block_descriptor_tmp.3251
+ __block_descriptor_tmp.3253
+ __block_descriptor_tmp.3256
+ __block_descriptor_tmp.3262
+ __block_descriptor_tmp.3300
+ __block_literal_global.2291
+ __block_literal_global.2325
- _ZN16AppleBCMWLANCore22updateWoWReasonToIoRegEjPcjjj.cold.1
- _ZN16AppleBCMWLANCore39parseEventLogRecordRoamTargetEvaluationEP6OSData.cold.5
- __ZN23IO80211SkywalkInterface12syncDPSStatsEv
- __ZN25AppleBCMWLANBGScanAdapter18isBGScanConfiguredEv
- __ZThn80_N23IO80211SkywalkInterface12syncDPSStatsEv
- __ZThn80_N23IO80211SkywalkInterface8findPeerER10ether_addr
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2273
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2273.cold.1
- __block_descriptor_tmp.1669
- __block_descriptor_tmp.1974
- __block_descriptor_tmp.2275
- __block_descriptor_tmp.2293
- __block_descriptor_tmp.2327
- __block_descriptor_tmp.2653
- __block_descriptor_tmp.2689
- __block_descriptor_tmp.3153
- __block_descriptor_tmp.3236
- __block_descriptor_tmp.3252
- __block_descriptor_tmp.3254
- __block_descriptor_tmp.3257
- __block_descriptor_tmp.3263
- __block_descriptor_tmp.3301
- __block_literal_global.2295
- __block_literal_global.2329
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1526.75\""
+ "/AppleInternal/Library/BuildRoots/4~B4R2ugDh2wfuAqJPfm1mN4BjmnXkR819EWIbUVE/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1526.75"
+ "Debug: WL_NAN_CMD_ADDITIONAL_ATTRIBUTES bytestream: "
+ "Jun 30 2025 22:01:18"
+ "LQM-WiFi-Roam: apTargetRSSIScore: mac=%8x%4x chanSpec=%{public}s rssi=%d rssiBoosted=%d rssiScore=%u loadAAC=%u chanFree=%u\n"
+ "LQM-WiFi-Roam: refScore=%u scoreDelta=%u numTargets=%u\n"
+ "LQM-WiFi-Roam: roamReason=%u roamType=%u home(bssid=%8x%4x chanSpec=%{public}s rssi=%d) prof[%d](flags=0x%x trigger=%d delta=%d) userOverride=%u\n"
+ "OS_LOG_DEFAULT, LQM-WiFi-Roam: apTargetLoadScore: mac=%8x%4x(%2s) chanSpec=%{public}s rssi=%d rssiBoosted=%d rate=%u bw=%u nss=%u chanFree=%u loadScore=%u\n"
+ "WL_NAN_CMD_ADDITIONAL_ATTRIBUTES"
+ "[dk] %s@%d: 'Bus low power' detected/available: APPLE80211_M_DRIVER_AVAILABLE, adjusting reason[0x%08x] -> [0x%08x], errorCode[0x%08x] isNonFatalFlag[0x%08x]\n"
+ "[dk] %s@%d: 'Bus low power' detected: APPLE80211_M_DRIVER_AVAILABLE, adjusting reason[0x%08x] -> [0x%08x], errorCode[0x%08x] isNonFatalFlag[0x%08x]\n"
+ "[dk] %s@%d: posting APPLE80211_M_DRIVER_AVAILABLE, available[%u] reason[0x%08x] sub_reason[0x%08x] minor_reason[0x%08x] flags[0x%08x]\n"
+ "[dk] %s@%d:%s:%d AllocationFailure\n"
+ "[dk] %s@%d:%s:%d ERROR: Mismatch: filled length %u, estimated length %u\n"
+ "[dk] %s@%d:%s:%d attrLen is 0\n"
+ "[dk] %s@%d:%s:%d estimated_len:%u payload->body_len:%u attr_count:%u\n"
+ "[dk] %s@%d:%s:%d invalid attr_count %u, out_offset:%u \n"
+ "[dk] %s@%d:%s:%d payloadLen + attrLen %u, exceeds body_len:%u \n"
+ "[dk] %s@%d:ALERT: Host pairing is not supported, ignoring compact payload"
+ "[dk] %s@%d:ALERT: Host pairing is supported, payload could be large to fit in a beacon, bailing out"
+ "[dk] %s@%d:Could not issue setIOVAR for vendor specific attribute; Invalid parameters\n"
+ "[dk] %s@%d:Driver avail message reason shouldn't be vendor specific - 0x%08x/%s\n"
+ "[dk] %s@%d:ERROR: Could not issue setNAN_VENDOR_PAYLOAD_COMPACT for vendor specific attribute; Invalid parameters"
+ "[dk] %s@%d:ERROR: Could not set additional attribute, issueSetIOVAR failed with retVal [ %d ]\n"
+ "[dk] %s@%d:Host pairing is not supported, ignoring additional attributes\n"
+ "[dk] %s@%d:Reason unknown, please add it reason<%d> type<%d> subtype<%d>\n"
+ "[dk] %s@%d:Removing Peer FLowQueue %02x:%02x:%02x:%02x:%02x:%02x\n"
+ "flushFlowQueues"
+ "setNAN_ADDITIONAL_ATTR"
+ "setNAN_VENDOR_PAYLOAD_COMPACT"
- "\"AppleBCMWLANV3_driverkit-1526.70\""
- "%c [dk] %s@%d: LQM-WiFi-Roam: apTargetLoadScore: mac=%8x%4x(%2s) chanSpec=%s, rssi=%d rssiBoosted=%d rate=%u bw=%u nss=%u chanFree=%u loadScore=%u\n"
- "%c [dk] %s@%d: LQM-WiFi-Roam: apTargetRSSIScore: mac=%8x%4x chanSpec=%s, rssi=%d rssiBoosted=%d rssiScore=%u loadAAC=%u chanFree=%u\n"
- "%c [dk] %s@%d: LQM-WiFi-Roam: refScore=%u scoreDelta=%u numTargets=%u\n"
- "%c [dk] %s@%d: LQM-WiFi-Roam: roamReason=%u roamType=%u home(bssid=%8x%4x chanSpec=%s, rssi=%d) prof[%d](flags=0x%x trigger=%d delta=%d) userOverride=%u\n"
- "/AppleInternal/Library/BuildRoots/4~B3ZcugBdhXEPfJRmC9dJ2kcvofhMZFDRYmWeLtk/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1526.70"
- "Jun 18 2025 21:17:18"
- "[dk] %s@%d:Driver avail message reason shouldn't be vendor specific - %s\n"
- "[dk] %s@%d:LQM-WiFi-Roam: apTargetLoadScore: mac=%8x%4x(%2s) chanSpec=%s, rssi=%d rssiBoosted=%d rate=%u bw=%u nss=%u chanFree=%u loadScore=%u\n"
- "[dk] %s@%d:LQM-WiFi-Roam: apTargetRSSIScore: mac=%8x%4x chanSpec=%s, rssi=%d rssiBoosted=%d rssiScore=%u loadAAC=%u chanFree=%u\n"
- "[dk] %s@%d:LQM-WiFi-Roam: refScore=%u scoreDelta=%u numTargets=%u\n"
- "[dk] %s@%d:LQM-WiFi-Roam: roamReason=%u roamType=%u home(bssid=%8x%4x chanSpec=%s, rssi=%d) prof[%d](flags=0x%x trigger=%d delta=%d) userOverride=%u\n"
- "[dk] %s@%d:Reason uknown, please add it <%d> \n"

```
