## bluetoothd

> `/usr/sbin/bluetoothd`

```diff

-190.47.3.0.0
-  __TEXT.__text: 0x84ae1c
-  __TEXT.__auth_stubs: 0x4780
-  __TEXT.__objc_stubs: 0x16c20
+190.50.0.0.0
+  __TEXT.__text: 0x84b064
+  __TEXT.__auth_stubs: 0x4790
+  __TEXT.__objc_stubs: 0x16c60
   __TEXT.__init_offsets: 0x54
   __TEXT.__objc_methlist: 0x8964
-  __TEXT.__const: 0x24f8c
-  __TEXT.__gcc_except_tab: 0x6b344
-  __TEXT.__cstring: 0xae658
+  __TEXT.__const: 0x24fbc
+  __TEXT.__gcc_except_tab: 0x6b300
+  __TEXT.__cstring: 0xae898
   __TEXT.__objc_classname: 0x9e1
-  __TEXT.__objc_methname: 0x1b464
-  __TEXT.__objc_methtype: 0x494f
-  __TEXT.__oslogstring: 0xab34d
+  __TEXT.__objc_methname: 0x1b48d
+  __TEXT.__objc_methtype: 0x4954
+  __TEXT.__oslogstring: 0xab242
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x227f0
+  __TEXT.__unwind_info: 0x227c8
   __TEXT.__eh_frame: 0x60
-  __DATA_CONST.__auth_got: 0x23d8
-  __DATA_CONST.__got: 0xd68
+  __DATA_CONST.__auth_got: 0x23e0
+  __DATA_CONST.__got: 0xd70
   __DATA_CONST.__auth_ptr: 0x1f8
-  __DATA_CONST.__const: 0x2f5a0
-  __DATA_CONST.__cfstring: 0x228e0
+  __DATA_CONST.__const: 0x2f4a8
+  __DATA_CONST.__cfstring: 0x229e0
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd0

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_intobj: 0x9f0
-  __DATA_CONST.__objc_arraydata: 0x418
-  __DATA_CONST.__objc_dictobj: 0x2a8
+  __DATA_CONST.__objc_arraydata: 0x438
+  __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_arrayobj: 0x1f8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xed98
-  __DATA.__objc_selrefs: 0x6948
+  __DATA.__objc_selrefs: 0x6958
   __DATA.__objc_ivar: 0xfe4
   __DATA.__objc_data: 0x1a40
   __DATA.__data: 0x47e8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x71c6a
+  __DATA.__bss: 0x7264a
   __DATA.__common: 0x6fb0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A0720DD2-A347-370D-8298-0271024C62A8
-  Functions: 32725
-  Symbols:   1595
-  CStrings:  43076
+  UUID: 261A24E8-4E1A-3E22-9E3E-C0D4FACE4B85
+  Functions: 32732
+  Symbols:   1597
+  CStrings:  43097
 
Symbols:
+ _IOObjectRetain
+ _kSymptomDiagnosticKeyPayloadDEParameters
CStrings:
+ "18:55:18"
+ "3901a8a835488761bd84e6b02b76b962d8972a43e1bc591ba5b55a39f4900c30"
+ "8f5051e6a0a3a1e1b8123d16db1c2e9c39e77806cf7fcbf9799d10339b3cd189"
+ "BTBandSwitchesDailyStats"
+ "BandSwitchManager: Allowed channels array -  raw 0x%x unii1 %d, unii3 %d, unii4 %d, unii5a %d, unii5b %d, unii5c %d, unii5d %d"
+ "BluetoothDiagnosticsManager: Skipping ABC trigger, we are in Recovery/NeRD mode"
+ "Do not set ConnScanTimeoutExtendPercent %f percent - invalid"
+ "Domain"
+ "Ethernet device became invalid while waiting for interface name"
+ "Extended feature complete timed out!"
+ "HAoS read failed %u"
+ "Jul 27 2025"
+ "Override %s Coex 0x%x connection  scan timeout %d extended by %f percent"
+ "Override %s Coex None connection  scan timeout %d extended by %f percent"
+ "Overwaited HAL %u(%u) seq %d+%d, %zu->%zu"
+ "Read extended feature completed, resume suspended policy enforcement"
+ "SendThread fShouldRunOverwaitDetection false"
+ "SendThread fShouldRunOverwaitDetection true"
+ "Set ConnScanTimeoutExtendPercent %f percent"
+ "Suspend enforcement due to missing extended feature"
+ "T^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSB{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})},N,V_connectionHandle"
+ "Timer late %u,%zu"
+ "^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSB{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}"
+ "^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSB{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}16@0:8"
+ "c58867b175427b870c1cc87cfe4b5ad03ab477d4e1ca693a70071caf9eac96e8"
+ "com.apple.DiagnosticExtensions.ConnectivityDE"
+ "convertFromWHBEvent:"
+ "convertToWHBEvent:"
+ "d69e862df0a18b0bae5b917cfa16022637a7e8aebf59af1751ed89dc19f8f7d0"
+ "fADVBufferWatchdogTimer %llu ms Armed!"
+ "fADVBufferWatchdogTimer Timer expired! screenState:%d"
+ "fADVBufferWatchdogTimer destroyed!"
+ "percentToDrop >= 0 && percentToDrop <= 100"
+ "registerCustomDataCallback: Registering client type %u (0x%X)"
+ "stepDataLength[i] > MAX_STEP_DATA_LENGTH, aborting"
+ "v24@0:8^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSB{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}16"
+ "v32@0:8^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSB{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}16i24c28"
+ "v36@0:8I16i20^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSB{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}24c32"
- "22:22:57"
- "BSMDailyStats"
- "Clearing KeepAudioInHeadphones A2DP mitigation timer due to AVRCP disconnection"
- "Do not set ConnScanTimeoutExtendPercent %d percent - invalid"
- "Engaging KeepAudioInHeadphones A2DP mitigation: time since start of mitigation window is %d seconds"
- "Engaging KeepAudioInHeadphones hfp mitigation: time since start of mitigation window is %d seconds"
- "Extending KeepAudioInHeadphones A2DP mitigation timer due to call ending"
- "Extending KeepAudioInHeadphones HFP mitigation timer due to call starting"
- "First read failed"
- "Jul 15 2025"
- "KeepAudioInHeadphones starting HFP mitigation timer due to HFP connection"
- "Override %s Coex 0x%x connection  scan timeout %d extended by %d percent"
- "Override %s Coex None connection  scan timeout %d extended by %d percent"
- "Overwait detected %d currentSequenceNumber %d incrementing sequenceNumber by %d"
- "Set ConnScanTimeoutExtendPercent %d percent"
- "Starting KeepAudioInHeadphones A2DP mitigation timer due to AVRCP connection"
- "T^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSB{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})},N,V_connectionHandle"
- "Using override A2DP timeout value %d on device %{public}s for KeepAudioInHeadphones"
- "Using override HFP timeout value %d on device %{public}s for KeepAudioInHeadphones"
- "^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSB{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}"
- "^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSB{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}16@0:8"
- "registerCustomDataCallback: Registering client type %d"
- "v24@0:8^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSB{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}16"
- "v32@0:8^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSB{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}16i24c28"
- "v36@0:8I16i20^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSB{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}24c32"

```
