## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1740.3.8.0.0
-  __TEXT.__text: 0x1315dc
-  __TEXT.__auth_stubs: 0x2140
-  __TEXT.__objc_stubs: 0x1bc20
+1740.3.9.0.0
+  __TEXT.__text: 0x1355b8
+  __TEXT.__auth_stubs: 0x22e0
+  __TEXT.__objc_stubs: 0x1bc80
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xe99c
-  __TEXT.__objc_methname: 0x2b487
-  __TEXT.__cstring: 0x478c6
+  __TEXT.__objc_methname: 0x2b483
+  __TEXT.__cstring: 0x48213
   __TEXT.__objc_classname: 0xddf
   __TEXT.__objc_methtype: 0x754a
-  __TEXT.__gcc_except_tab: 0x4460
+  __TEXT.__gcc_except_tab: 0x4740
   __TEXT.__const: 0x1b028
   __TEXT.__dlopen_cstrs: 0x376
   __TEXT.__oslogstring: 0x90
-  __TEXT.__unwind_info: 0x3f30
-  __DATA_CONST.__auth_got: 0x10b8
+  __TEXT.__unwind_info: 0x4060
+  __DATA_CONST.__auth_got: 0x1188
   __DATA_CONST.__got: 0x6f8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4810
-  __DATA_CONST.__cfstring: 0x28720
+  __DATA_CONST.__const: 0x49e0
+  __DATA_CONST.__cfstring: 0x28ce0
   __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x430
-  __DATA_CONST.__objc_intobj: 0x3378
-  __DATA_CONST.__objc_arraydata: 0xf438
-  __DATA_CONST.__objc_arrayobj: 0x6a38
+  __DATA_CONST.__objc_intobj: 0x3390
+  __DATA_CONST.__objc_arraydata: 0xf778
+  __DATA_CONST.__objc_arrayobj: 0x6be8
   __DATA_CONST.__objc_dictobj: 0x2a8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x17680

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6445
-  Symbols:   759
-  CStrings:  13952
+  Functions: 6473
+  Symbols:   785
+  CStrings:  13998
 
Symbols:
+ __ZN6AriSdk29ARI_IBICallPsWrmSAInfoReq_SDKC1Ev
+ __ZN6AriSdk29ARI_IBICallPsWrmSAInfoReq_SDKD1Ev
+ __ZN6AriSdk29ARI_IBICallPsWrmSAInfoRsp_SDK6unpackEv
+ __ZN6AriSdk29ARI_IBICallPsWrmSAInfoRsp_SDKC1EPKhj
+ __ZN6AriSdk29ARI_IBICallPsWrmSAInfoRsp_SDKD1Ev
+ __ZN6AriSdk33ARI_IBICallPsWrmSdmInfoReq_V2_SDKC1Ev
+ __ZN6AriSdk33ARI_IBICallPsWrmSdmInfoReq_V2_SDKD1Ev
+ __ZN6AriSdk33ARI_IBICallPsWrmSdmInfoRsp_V2_SDK6unpackEv
+ __ZN6AriSdk33ARI_IBICallPsWrmSdmInfoRsp_V2_SDKC1EPKhj
+ __ZN6AriSdk33ARI_IBICallPsWrmSdmInfoRsp_V2_SDKD1Ev
+ __ZN6AriSdk40ARI_IBICallPsWrmSdmLocationDBInfoReq_SDKC1Ev
+ __ZN6AriSdk40ARI_IBICallPsWrmSdmLocationDBInfoReq_SDKD1Ev
+ __ZN6AriSdk40ARI_IBICallPsWrmSdmLocationDBInfoRsp_SDK6unpackEv
+ __ZN6AriSdk40ARI_IBICallPsWrmSdmLocationDBInfoRsp_SDKC1EPKhj
+ __ZN6AriSdk40ARI_IBICallPsWrmSdmLocationDBInfoRsp_SDKD1Ev
+ __ZN6AriSdk43ARI_IBICallPsWrmSdmLocationDBInfoRegReq_SDKC1Ev
+ __ZN6AriSdk43ARI_IBICallPsWrmSdmLocationDBInfoRegReq_SDKD1Ev
+ __ZN6AriSdk43ARI_IBICallPsWrmSdmLocationDBInfoRegRsp_SDK6unpackEv
+ __ZN6AriSdk43ARI_IBICallPsWrmSdmLocationDBInfoRegRsp_SDKC1EPKhj
+ __ZN6AriSdk43ARI_IBICallPsWrmSdmLocationDBInfoRegRsp_SDKD1Ev
+ __ZN6AriSdk45ARI_IBICallPsWrmSdmLocationDBInfoRegIndCb_SDK6unpackEv
+ __ZN6AriSdk45ARI_IBICallPsWrmSdmLocationDBInfoRegIndCb_SDKC1EPKhj
+ __ZN6AriSdk45ARI_IBICallPsWrmSdmLocationDBInfoRegIndCb_SDKD1Ev
+ __ZN6AriSdk47ARI_IBICallPsWrmSdmLocationDBFetchInfoIndCb_SDK6unpackEv
+ __ZN6AriSdk47ARI_IBICallPsWrmSdmLocationDBFetchInfoIndCb_SDKC1EPKhj
+ __ZN6AriSdk47ARI_IBICallPsWrmSdmLocationDBFetchInfoIndCb_SDKD1Ev
CStrings:
+ "BB25A AntMapping_1:Updating antenna map params to cellular modem"
+ "BB25A: platformID not defined to configure CellTxAntIdx over the bus"
+ "CoEx-Table-AntBlockPwrLmt-Coex001"
+ "CoEx-Table-CellCoex027_V7WiFiEnh"
+ "Failed to unpack IBICallPsWrmSdmLocationDBFetchInfoIndCb: %s (%u)"
+ "Failed to unpack IBICallPsWrmSdmLocationDBInfoRegIndCb: %s (%u)"
+ "HFAFHDebug_ Coex Issue array count 5G: %lu"
+ "HPCellular (handleBTPowerStateChange): HPCellularActive = (%d), set BT AFH map to (%@)."
+ "HPCellular (handleCellularNetworkUpdate): HPCellularActive = (%d), set BT AFH map to (%@)."
+ "HPCellular (handleHPCellularStateUpdate): HPCellularActive = (%d), set BT AFH map to (%@)."
+ "HPCellular (updateGPSRadioActiveState): HPCellularActive = (%d), set BT AFH map to (%@)."
+ "HPCellular: Calling queryHPCellularInitialState after BB power on"
+ "HPCellular: Error - unexpected null pointer in stateChanged delegate callback!"
+ "HPCellular: HPCellularActive=%d, state unchanged. Skip sending indication to BT host."
+ "HPCellular: In initial state query, HPCellularActive = (%d)"
+ "HPCellular: WCM_HPCellularStateMonitor start failed."
+ "HPCellular: WCM_HPCellularStateMonitor started."
+ "HPCellular: start HPCellularStateMonitor ..."
+ "HPCellular: stateChanged : %@"
+ "HPCellular: stateChanged, set BT AFH map for HPCellular = (%d)"
+ "IBI simSlot %d: setLocationDbInfoPushOneEntryForCellType ERROR: invalid CellType, has to be CellTypeLTE, CellType5GSA, or CellType5GNSA"
+ "IBI simSlot %d: setWrmSdmLocationDbPushOneEntryForCellType LTE entry exceeds max limit"
+ "IBI simSlot %d: setWrmSdmLocationDbPushOneEntryForCellType LTENSA entry exceeds max limit"
+ "IBI simSlot %d: setWrmSdmLocationDbPushOneEntryForCellType SA entry exceeds max limit"
+ "IBI simSlot %d: setWrmSdmLocationDbPushOneEntryForCellType SADC entry exceeds max limit"
+ "IBICallPsWrmSdmLocationDBInfoRegReq on sim %s"
+ "ICE Client NOT querySdmLocationDBInfoReg as SIS not supported."
+ "ICE Client querySdmLocationDBInfoReg"
+ "ICE ERROR: Invalid IBICallPsWrmSAInfoRsp in setBBSAState"
+ "ICE ERROR: Invalid IBICallPsWrmSdmInfoRsp_V2 in notifyAVStatus"
+ "ICE ERROR: Invalid IBICallPsWrmSdmInfoRsp_V2 in notifyBBCallState"
+ "ICE ERROR: Invalid IBICallPsWrmSdmInfoRsp_V2 in notifyBBLockState"
+ "ICE ERROR: Invalid IBICallPsWrmSdmInfoRsp_V2 in notifyFTDupelicationState"
+ "ICE ERROR: Invalid IBICallPsWrmSdmInfoRsp_V2 in notifyStreamingEBHState"
+ "ICE ERROR: Invalid IBICallPsWrmSdmLocationDBFetchInfoIndCb received"
+ "ICE ERROR: Invalid IBICallPsWrmSdmLocationDBInfoRegIndCb received"
+ "ICE ERROR: Invalid IBICallPsWrmSdmLocationDBInfoRegRsp"
+ "ICE ERROR: Invalid IBICallPsWrmSdmLocationDBInfoRsp in sendWrmSdmLocationDbInfo"
+ "ICE ERROR: Unpack IBICallPsWrmSAInfoRsp in setBBSAState:  %s (%u)"
+ "ICE ERROR: Unpack IBICallPsWrmSdmInfoRsp_V2 in notifyAVStatus:  %s (%u)"
+ "ICE ERROR: Unpack IBICallPsWrmSdmInfoRsp_V2 in notifyBBCallState:  %s (%u)"
+ "ICE ERROR: Unpack IBICallPsWrmSdmInfoRsp_V2 in notifyBBLockState:  %s (%u)"
+ "ICE ERROR: Unpack IBICallPsWrmSdmInfoRsp_V2 in notifyFTDupelicationState:  %s (%u)"
+ "ICE ERROR: Unpack IBICallPsWrmSdmInfoRsp_V2 in notifyStreamingEBHState:  %s (%u)"
+ "ICE ERROR: Unpack IBICallPsWrmSdmLocationDBInfoRegRsp"
+ "ICE ERROR: Unpack IBICallPsWrmSdmLocationDBInfoRsp in sendWrmSdmLocationDbInfo:  %s (%u)"
+ "ICE IBICallPsWrmSdmLocationDBFetchInfoIndCb received"
+ "ICE IBICallPsWrmSdmLocationDBFetchInfoIndCbHandle  nInstance=%s mcc=%u, mnc=%u, cell_id=%llu"
+ "ICE IBICallPsWrmSdmLocationDBInfoRegIndCb received"
+ "ICE IBICallPsWrmSdmLocationDBInfoRegIndCbHandle  locationDbRequired=%d"
+ "ICE Rsp OK: IBICallPsWrmSAInfoRsp in setBBSAState:  %s (%u)"
+ "ICE Rsp OK: IBICallPsWrmSdmInfoRsp_V2 in notifyAVStatus:  %s (%u)"
+ "ICE Rsp OK: IBICallPsWrmSdmInfoRsp_V2 in notifyBBCallState:  %s (%u)"
+ "ICE Rsp OK: IBICallPsWrmSdmInfoRsp_V2 in notifyBBLockState:  %s (%u)"
+ "ICE Rsp OK: IBICallPsWrmSdmInfoRsp_V2 in notifyFTDupelicationState:  %s (%u)"
+ "ICE Rsp OK: IBICallPsWrmSdmInfoRsp_V2 in notifyStreamingEBHState:  %s (%u)"
+ "ICE Rsp OK: IBICallPsWrmSdmLocationDBInfoRegRsp:: locationDbRequired = %d"
+ "ICE Rsp OK: IBICallPsWrmSdmLocationDBInfoRsp in sendWrmSdmLocationDbInfo:  %s (%u)"
+ "ICE send IBICallPsWrmSdmLocationDBInfoReq on sim %s sendWrmSdmLocationDbInfo locationDB available %d, cellID %llu, mcc %u, mnc %u"
+ "ICE send wrmSDMInformation on sim %s VoIP app: %d, Call State: %d, CallType: %d, telephonyCall: %d"
+ "ICE send wrmSDMInformation on sim %s notifyAVStatus state: %d, BW: %d"
+ "ICE send wrmSDMInformation on sim %s notifyFTDupelicationState state: %d"
+ "ICE send wrmSDMInformation on sim %s notifyStreamingEBHState state: %d"
+ "ICE send wrmSDMInformation on sim %s screen lock status %d"
+ "ICE send wrmSDMSAInformation on sim %s setBBSAState disable: %d, CallSimSlot %d"
+ "initWiFiStatetoBT"
+ "setBBSAState SaAllowedOnWiFiAssociation on sim %s"
- "BT Crashed or init - resending WiFi states"
- "HPCellular (handleBTPowerStateChange): Bool flag self.hpCellNeed2SetBTAFH = (%d), Fixed AFH self.btPreferredChannelMapHPCellularActive = (%@)."
- "HPCellular (handleCellularNetworkUpdate): Bool flag self.hpCellNeed2SetBTAFH = (%d), Fixed AFH self.btPreferredChannelMapHPCellularActive = (%@)."
- "HPCellular (handleHPCellularStateUpdate): Bool flag self.hpCellNeed2SetBTAFH = (%d), Fixed AFH self.btPreferredChannelMapHPCellularActive = (%@)."
- "HPCellular (updateGPSRadioActiveState): Bool flag self.hpCellNeed2SetBTAFH = (%d), Fixed AFH self.btPreferredChannelMapHPCellularActive = (%@)."
- "HPCellular: Accessing WCM_HPCellularStateMonitor intance self.hpCellularMonitor in WCM_PolicyManager.m is successful."
- "HPCellular: Calling [self queryHPCellularInitialState] from handleCellularNetworkUpdate."
- "HPCellular: Duplicated indications: self.hpCellNeed2SetBTAFH=%d is equal to hpCellularStateActive=%d. Skip sending indication to BT host."
- "HPCellular: In initial state query, HPCellular Status is active and Bool flag bHPCellSetBTAFH of WCM_HPCellularStateMonitor class has been set to: (%d)"
- "HPCellular: In initial state query, HPCellular Status is not active and Bool flag bHPCellSetBTAFH of WCM_HPCellularStateMonitor class has been set to: (%d)"
- "HPCellular: Initial queryHPCellularInitialState is success. HPCellular status printed"
- "HPCellular: in initial state query, creating [WCM_PolicyManager singleton] is successful in WCM_HPCellularStateMonitor.m."
- "HPCellular: in stateChanged method, HPCellular Status is active and Bool flag bHPCellSetBTAFH of WCM_HPCellularStateMonitor class has been set to: (%d)"
- "HPCellular: in stateChanged method, HPCellular Status is not active and Bool flag bHPCellSetBTAFH of WCM_HPCellularStateMonitor class has been set to: (%d)"
- "HPCellular: in stateChanged method, [WCM_PolicyManager singleton] is successful in WCM_HPCellularStateMonitor.m."
- "HPCellular: in stateChanged method, unexpected CTHPCellState null pointer in delegate callback"
- "HPCellular: queryHPCellularInitialState getting called."
- "HPCellular: start method in WCM_HPCellularStateMonitor is called."
- "HPCellular: stateChanged method is called in delegate callback."
- "HPCellular: stateChanged method, HPCellular state changed to: %@"
- "initControllerPolicy:"

```
