## libCommCenterKCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib`

```diff

-12317.2.0.0.0
-  __TEXT.__text: 0x123188
-  __TEXT.__auth_stubs: 0x7420
-  __TEXT.__const: 0x15f57
-  __TEXT.__gcc_except_tab: 0x13b60
-  __TEXT.__oslogstring: 0x14061
-  __TEXT.__cstring: 0x47ec
-  __TEXT.__unwind_info: 0x6c18
+12320.0.0.0.0
+  __TEXT.__text: 0x1335cc
+  __TEXT.__auth_stubs: 0x7930
+  __TEXT.__const: 0x17659
+  __TEXT.__gcc_except_tab: 0x14d68
+  __TEXT.__oslogstring: 0x15214
+  __TEXT.__cstring: 0x486f
+  __TEXT.__unwind_info: 0x71b8
   __DATA_CONST.__got: 0x438
   __DATA_CONST.__const: 0x988
-  __AUTH_CONST.__auth_got: 0x3a18
-  __AUTH_CONST.__const: 0x10620
+  __AUTH_CONST.__auth_got: 0x3ca0
+  __AUTH_CONST.__const: 0x11458
   __AUTH_CONST.__cfstring: 0x100
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 5280
-  Symbols:   7642
-  CStrings:  2374
+  Functions: 5568
+  Symbols:   8025
+  CStrings:  2484
 
Symbols:
+ __Z8asString13CallIMSStatus
+ __Z8asString18FileTransferStatus
+ __ZN12capabilities2ct20supportsHiSpeedFilerEv
+ __ZN12capabilities2ct20supportsNewPhonebookEv
+ __ZN12capabilities2ct29getProvisioningProfileSupportEv
+ __ZN12capabilities2ct30supportsCachedNetworkTimeQueryEv
+ __ZN12capabilities5radio7initiumEv
+ __ZN14HSFilerManager13sendFile_syncERKNSt3__110shared_ptrIK8RegistryEEN10subscriber7SimSlotE8FileTypeRKNS1_INS0_13basic_istreamIcNS0_11char_traitsIcEEEEEERKNS0_12basic_stringIcSC_NS0_9allocatorIcEEEE
+ __ZN14HSFilerManager19getFilerSegmentSizeEv
+ __ZN14HSFilerManager20handleRadioDown_syncEv
+ __ZN14HSFilerManager31reportHSFileTransferStatus_syncEN10subscriber7SimSlotE18FileTransferStatus8FileTypeb
+ __ZN14HSFilerManagerC2ERKN8dispatch5queueE
+ __ZN14HSFilerManagerD2Ev
+ __ZN3ctu6hex_spEPKvm
+ __ZN6AriSdk25ARI_IBIPriWriteReq_V3_SDKC1Ev
+ __ZN6AriSdk25ARI_IBIPriWriteReq_V3_SDKD1Ev
+ __ZN6AriSdk26ARI_IBISimPbReadRecReq_SDKC1Ev
+ __ZN6AriSdk26ARI_IBISimPbReadRecReq_SDKD1Ev
+ __ZN6AriSdk27ARI_IBIPriWriteRspCb_V3_SDK6unpackEv
+ __ZN6AriSdk27ARI_IBIPriWriteRspCb_V3_SDKC1EPKhj
+ __ZN6AriSdk27ARI_IBIPriWriteRspCb_V3_SDKD1Ev
+ __ZN6AriSdk27ARI_IBISimPbWriteRecReq_SDKC1Ev
+ __ZN6AriSdk27ARI_IBISimPbWriteRecReq_SDKD1Ev
+ __ZN6AriSdk28ARI_IBICpsSetCmasModeReq_SDKC1Ev
+ __ZN6AriSdk28ARI_IBICpsSetCmasModeReq_SDKD1Ev
+ __ZN6AriSdk28ARI_IBILapsFetchIndCb_V2_SDK6unpackEv
+ __ZN6AriSdk28ARI_IBILapsFetchIndCb_V2_SDKC1EPKhj
+ __ZN6AriSdk28ARI_IBILapsFetchIndCb_V2_SDKD1Ev
+ __ZN6AriSdk28ARI_IBINetGetNitzInfoReq_SDKC1Ev
+ __ZN6AriSdk28ARI_IBINetGetNitzInfoReq_SDKD1Ev
+ __ZN6AriSdk28ARI_IBINetRatNRStatusReq_SDKC1Ev
+ __ZN6AriSdk28ARI_IBINetRatNRStatusReq_SDKD1Ev
+ __ZN6AriSdk28ARI_IBISimPbReadRecRspCb_SDK6unpackEv
+ __ZN6AriSdk28ARI_IBISimPbReadRecRspCb_SDKC1EPKhj
+ __ZN6AriSdk28ARI_IBISimPbReadRecRspCb_SDKD1Ev
+ __ZN6AriSdk29ARI_IBISimPbWriteRecRspCb_SDK6unpackEv
+ __ZN6AriSdk29ARI_IBISimPbWriteRecRspCb_SDKC1EPKhj
+ __ZN6AriSdk29ARI_IBISimPbWriteRecRspCb_SDKD1Ev
+ __ZN6AriSdk30ARI_IBICpsSetCmasModeRspCb_SDK6unpackEv
+ __ZN6AriSdk30ARI_IBICpsSetCmasModeRspCb_SDKC1EPKhj
+ __ZN6AriSdk30ARI_IBICpsSetCmasModeRspCb_SDKD1Ev
+ __ZN6AriSdk30ARI_IBINetGetNitzInfoRspCb_SDK6unpackEv
+ __ZN6AriSdk30ARI_IBINetGetNitzInfoRspCb_SDKC1EPKhj
+ __ZN6AriSdk30ARI_IBINetGetNitzInfoRspCb_SDKD1Ev
+ __ZN6AriSdk30ARI_IBINetRatNRStatusRspCb_SDK6unpackEv
+ __ZN6AriSdk30ARI_IBINetRatNRStatusRspCb_SDKC1EPKhj
+ __ZN6AriSdk30ARI_IBINetRatNRStatusRspCb_SDKD1Ev
+ __ZN6AriSdk30ARI_IBISendApacsDataReq_V2_SDKC1Ev
+ __ZN6AriSdk30ARI_IBISendApacsDataReq_V2_SDKD1Ev
+ __ZN6AriSdk30ARI_IBISimPbGetMetaInfoReq_SDKC1Ev
+ __ZN6AriSdk30ARI_IBISimPbGetMetaInfoReq_SDKD1Ev
+ __ZN6AriSdk32ARI_IBISimPbGetMetaInfoIndCb_SDK6unpackEv
+ __ZN6AriSdk32ARI_IBISimPbGetMetaInfoIndCb_SDKC1EPKhj
+ __ZN6AriSdk32ARI_IBISimPbGetMetaInfoIndCb_SDKD1Ev
+ __ZN6AriSdk32ARI_IBISimPbGetMetaInfoRspCb_SDK6unpackEv
+ __ZN6AriSdk32ARI_IBISimPbGetMetaInfoRspCb_SDKC1EPKhj
+ __ZN6AriSdk32ARI_IBISimPbGetMetaInfoRspCb_SDKD1Ev
+ __ZN6AriSdk33ARI_IBIPriWriteStatusIndCb_V2_SDK6unpackEv
+ __ZN6AriSdk33ARI_IBIPriWriteStatusIndCb_V2_SDKC1EPKhj
+ __ZN6AriSdk33ARI_IBIPriWriteStatusIndCb_V2_SDKD1Ev
+ __ZN6AriSdk36ARI_IBICallPsTrafficClassInfo_V2_SDKC1Ev
+ __ZN6AriSdk36ARI_IBICallPsTrafficClassInfo_V2_SDKD1Ev
+ __ZN6AriSdk41ARI_IBICallCsEmergencyNumberListIndCb_SDK6unpackEv
+ __ZN6AriSdk41ARI_IBICallCsEmergencyNumberListIndCb_SDKC1EPKhj
+ __ZN6AriSdk41ARI_IBICallCsEmergencyNumberListIndCb_SDKD1Ev
+ __ZN6AriSdk41ARI_IBICallPsTrafficClassInfoRspCb_V2_SDK6unpackEv
+ __ZN6AriSdk41ARI_IBICallPsTrafficClassInfoRspCb_V2_SDKC1EPKhj
+ __ZN6AriSdk41ARI_IBICallPsTrafficClassInfoRspCb_V2_SDKD1Ev
+ __ZN6AriSdk41ARI_IBINetEmergencyApacsScanFailIndCb_SDK6unpackEv
+ __ZN6AriSdk41ARI_IBINetEmergencyApacsScanFailIndCb_SDKC1EPKhj
+ __ZN6AriSdk41ARI_IBINetEmergencyApacsScanFailIndCb_SDKD1Ev
+ __ZN6AriSdk47ARI_IBINetNetworkFeatureSupportInfoIndCb_V2_SDK6unpackEv
+ __ZN6AriSdk47ARI_IBINetNetworkFeatureSupportInfoIndCb_V2_SDKC1EPKhj
+ __ZN6AriSdk47ARI_IBINetNetworkFeatureSupportInfoIndCb_V2_SDKD1Ev
+ __ZN6AriSdk52ARI_IBIMsCallCsVoimsProvideMMTelSessionStatusReq_SDKC1Ev
+ __ZN6AriSdk52ARI_IBIMsCallCsVoimsProvideMMTelSessionStatusReq_SDKD1Ev
+ __ZN6AriSdk54ARI_IBIMsCallCsVoimsProvideMMTelSessionStatusRspCb_SDK6unpackEv
+ __ZN6AriSdk54ARI_IBIMsCallCsVoimsProvideMMTelSessionStatusRspCb_SDKC1EPKhj
+ __ZN6AriSdk54ARI_IBIMsCallCsVoimsProvideMMTelSessionStatusRspCb_SDKD1Ev
+ __ZNK14HSFilerManager14dumpState_syncEv
+ __ZNK14HSFilerManager22isTransferPending_syncEv
+ __ZTI14HSFilerManager
CStrings:
+ "  Missing cell id."
+ "  Missing tac."
+ "#D *** IMS call state notification to BB: Dropping the request for %s as legacy devices do not need them."
+ "#D Adding inputs for NR"
+ "#D Found %u LTE R15 cells"
+ "#D Found %u NR neighbor cells"
+ "#D Found %u NR serving cells"
+ "#D Found %u R15 LTE cells"
+ "#D Found %u R15-V2 LTE cells"
+ "#D Found %u V2 LTE Neighbor cells"
+ "#D Found %u V2 NR neighbor cells"
+ "#D Found %u V2 NR serving cell"
+ "#D Found %u V3 NR serving cell"
+ "#D Found NR serving cell"
+ "#D IMS call status update successfully completed"
+ "#D Invalidate cache request succeeded"
+ "#D Registering for V2"
+ "#D Trimming SNR from %.2f to %.2f for Nr"
+ "#D bootstrapVersion: %s"
+ "#D isBootstrap: %d"
+ "#I %s"
+ "#I %s phone number written to record number 1"
+ "#I %s smart data mode succeeded"
+ "#I %sable 5G standalone succeeded"
+ "#I %sable nr roaming succeeded"
+ "#I *** IMS call state notification to BB because of %s."
+ "#I Could not copy signature data for bundle %s"
+ "#I Could not unpack IBILapsFetchIndCb_V2: %s (%d)"
+ "#I Dropping acccess data in %s"
+ "#I E911 scan completed (failed)"
+ "#I Enable 5G result from %s succeeded"
+ "#I Enabling NR band%s: %s"
+ "#I Failed to set band %u"
+ "#I Found PLMN %03d-%0.*d from LTE R15 cell"
+ "#I Found PLMN %03d-%0.*d from NR cell"
+ "#I Informing baseband to %sable 5G standalone because %s"
+ "#I Informing baseband to %sable nr roaming"
+ "#I NR has been enabled in RAT selection"
+ "#I PB Types present:"
+ "#I Processing IBICallCsEmergencyNumberListIndCb for types: Local[%lu]"
+ "#I Processing IBICallCsEmergencyNumberListIndCb for types: Network[%lu]"
+ "#I RAT mode status: GSM=%s, UMTS=%s, LTE=%s, NR=%s"
+ "#I Read entry (%d) pbType (%s) number (%s) result=%s"
+ "#I Received indication from baseband file: %s (%s) result: %s"
+ "#I Received phonebook meta information for %s"
+ "#I Register new PBK indications"
+ "#I Setting acquisition order to NR"
+ "#N %s smart data mode failed"
+ "#N %sable 5G standalone failed"
+ "#N %sable nr roaming failed"
+ "#N *** IMS call state notification to BB: Dropping the request for %s as it is handled by IPT on device that supports 5G."
+ "#N *** IMS call state notification to BB: Dropping the request for %s as it is not supported."
+ "#N BDN phonebook was not requested"
+ "#N CPHS INFNUM phonebook was not requested"
+ "#N Could not unpack AriACK for %s smart data mode: %s (%d)"
+ "#N Could not unpack AriACK for allow enabling 5G standalone: %s (%d)"
+ "#N Could not unpack AriACK for allow nr roaming request: %s (%d)"
+ "#N Could not unpack AriACK for getting nr status request: %s (%d)"
+ "#N Could not unpack IBICallCsEmergencyNumberListIndCb: %s (%d)"
+ "#N Could not unpack IBICpsSetCmasModeRspCb: %s (%d)"
+ "#N Could not unpack IBINetGetNitzInfoRspCb: %s (%d)"
+ "#N Could not unpack IBISimPbGetMetaInfoIndCb: %s (%d)"
+ "#N Could not unpack IBISimPbGetMetaInfoRspCb: %s (%d)"
+ "#N Could not unpack IBISimPbReadRecRspCb: %s (%d)"
+ "#N Did not find UMTS, GSM, LTE, NR, or CDMA serving cell"
+ "#N Dropping GSM ARFCN entries starting at index %d of %zu"
+ "#N Dropping LTE EARFCN entries starting at index %d of %zu"
+ "#N Dropping NR entries starting at index %d of %zu"
+ "#N Dropping UMTS UARFCN entries starting at index %d of %zu"
+ "#N ECC phonebook was not requested"
+ "#N Empty data modes in IBINetNetworkFeatureSupportInfoIndCb_V2"
+ "#N Enable 5G from %s failed"
+ "#N Invalid response to IBICpsSetCmasModeReq with camp only mode"
+ "#N Invalidate cache request failed with invalid response"
+ "#N Invalidate cache request failed: Error in response with result %d (%s)"
+ "#N LND phonebook was not requested"
+ "#N Location mismatch for 2G ADN phonebook TLV for %s"
+ "#N Location mismatch for global phonebook TLV for %s"
+ "#N Location mismatch for local USIM phonebook TLV for %s"
+ "#N Missing FR2 recommendation TLV"
+ "#N Missing NR serving cell TLV"
+ "#N Network Feature Support indication V2 is not valid %s (%d) "
+ "#N No valid disablement status"
+ "#N Unrecognized phonebook location was returned"
+ "#N getting nr status failed"
+ "%s is not supported"
+ "%s smart data mode failed. Result: %d"
+ "%sable 5G standalone failed: %d"
+ "%sable nr roaming failed: %d"
+ "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "Could not unpack IBIPriWriteRspCb_V3: %s (%d)"
+ "Device does not support 5G"
+ "EmergencyNumbersList with empty numbers array - bailing"
+ "EmergencyNumbersList with zero length - bailing"
+ "ExtEmergencyNumbersList with empty numbers array - bailing"
+ "ExtEmergencyNumbersList with zero length - bailing"
+ "File transfer is not allowed due to pending session"
+ "IMS call status update failed"
+ "Incoming payload for Traffic Class Request V2 invalid"
+ "Invalid message.%{public}s%{public}s"
+ "Missing band settings TLV 0x11"
+ "NetEmergencyApacsScanFailIndCb is not valid %s (%d) "
+ "Nr cell %d of %d MCC (%d) is invalid"
+ "Preparing for file transfer failed: %d"
+ "Received IBINetNRCellInfoList with size %u (max %zu)"
+ "Receiving Write status for %u files. Expecting only %u"
+ "Response is not IBIPriWriteRspCb_V3"
+ "kHighThroughput"
+ "kNRServingCellType"
+ "set.bb.ibi.hs"
+ "set.bb.ibi.hs.1"
+ "set.bb.ibi.hs.2"
+ "set.bb.ibi.hs.?"
- "#N Did not find UMTS, GSM, LTE, or CDMA serving cell"
- "#N Send Smart data mode not supported"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"

```
