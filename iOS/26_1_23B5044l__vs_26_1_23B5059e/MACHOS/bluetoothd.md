## bluetoothd

> `/usr/sbin/bluetoothd`

```diff

-191.5.1.1.0
-  __TEXT.__text: 0x877554
+191.8.0.0.0
+  __TEXT.__text: 0x879c90
   __TEXT.__auth_stubs: 0x4990
   __TEXT.__objc_stubs: 0x173a0
   __TEXT.__init_offsets: 0x58
   __TEXT.__objc_methlist: 0x8b3c
   __TEXT.__const: 0x24fac
-  __TEXT.__gcc_except_tab: 0x6c484
-  __TEXT.__cstring: 0xb4772
+  __TEXT.__gcc_except_tab: 0x6c604
+  __TEXT.__cstring: 0xb4c20
   __TEXT.__objc_classname: 0xa07
-  __TEXT.__objc_methname: 0x1be71
-  __TEXT.__objc_methtype: 0x496a
-  __TEXT.__oslogstring: 0xadb3d
+  __TEXT.__objc_methname: 0x1be72
+  __TEXT.__objc_methtype: 0x496f
+  __TEXT.__oslogstring: 0xadccc
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0xd4
-  __TEXT.__unwind_info: 0x22eb8
+  __TEXT.__unwind_info: 0x22f28
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0x24e0
   __DATA_CONST.__got: 0xdc8
   __DATA_CONST.__auth_ptr: 0x210
-  __DATA_CONST.__const: 0x30320
-  __DATA_CONST.__cfstring: 0x23500
+  __DATA_CONST.__const: 0x303c8
+  __DATA_CONST.__cfstring: 0x235e0
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd0

   __DATA.__objc_data: 0x1a90
   __DATA.__data: 0x4a78
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x72b12
+  __DATA.__bss: 0x72b4a
   __DATA.__common: 0x6fb8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A327CA66-256C-3E89-B33C-070ADFEE9003
-  Functions: 33346
+  UUID: CE2382D1-223E-335B-9EF8-2FE28E3AC5EA
+  Functions: 33380
   Symbols:   1640
-  CStrings:  44049
+  CStrings:  44088
 
CStrings:
+ "%s:%06u Got an XPC error: %s\n"
+ "%s:%06u No change in profile configuration\n"
+ "%s:%06u Received NULL reply\n"
+ "%s:%06u XPC connection error: %s\n"
+ "%s:%06u XPC connection interrupted - will auto-reconnect\n"
+ "%s:%06u XPC connection invalidated\n"
+ "%s:%06u cannot create xpc connection"
+ "%s:%06u cannot create xpc message"
+ "%s:%06u cannot get property value"
+ "%s:%06u debug profile present -> %d"
+ "%s:%06u failed to create MACH service\n"
+ "%s:%06u invalid xml data\n"
+ "%s:%06u invalid xml data length\n"
+ "%s:%06u invalid xml data ptr\n"
+ "%s:%06u unable to build ccconfig dictionary\n"
+ "%s:%06u unable to build result dictionary\n"
+ "%s:%06u unable to check if profile is installed"
+ "%s:%06u unable to create XPC dictionary\n"
+ "%s:%06u unable to create ccpipe dict"
+ "%s:%06u unable to create ccstream dict"
+ "%s:%06u unable to create intermediate directory for logging plist"
+ "%s:%06u unable to create policy CFNumber"
+ "%s:%06u unable to create property list data\n"
+ "%s:%06u unable to write bt profile plist. error code: %d\n"
+ "%s:%06u value is of incorrect type"
+ "%s:%06u xpc message is not valid"
+ "-[CBDaemonServer _updateUserControllerCloudDevices]_block_invoke"
+ "22:00:10"
+ "3a137a2c8d573eb9b62a53a98afad8d67bcdd7eb1b06cb7e4021f52651ae260b"
+ "5c8aa8293f8342d68f85b2db2087f1ece2b2a7c674cfca4b811cb75cd42aff63"
+ "6a9767980952356b19c6d1817163d9d8f858652babc2047a461da73a26ab1ad5"
+ "Advanced Create Connection failed for %:, sending dummy Connection Complete Event"
+ "BTConnectionStalls"
+ "BTPreferencesGetAppBooleanValue"
+ "Duplicate request so set max interval to min interval"
+ "FrequentAPWakeup"
+ "HostwakeReport: reset counter %d"
+ "Invalid handle to send session stats metric"
+ "Magic Pairing key malloc failed"
+ "Notify AAoS is %s"
+ "Oct  1 2025"
+ "ReportConnectionRequestStallStats connectionRequestFail sending metrics: successCount %d, VID %d, PID %d"
+ "ReportConnectionRequestStallStats successCount: %d"
+ "SuccessCount"
+ "T^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSBBC{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})},N,V_connectionHandle"
+ "TccCheckComplete for %{public}@"
+ "Transitioning to HandsfreeAoS - device:%{public}s isInAdvancedSniff:%d pendingAoSExit:%d"
+ "Unexpected frequent VSE caused AP wakeup counter %d reasonCode %d"
+ "User Controller missing, Error saving this device's controller info"
+ "User Controller missing, Unable to report biome device event for %s"
+ "User Controller missing, Unable to report biome usecase event for %s"
+ "User Controller missing, unable to fetch cloud paired device metadata"
+ "WakePacketTypeVSE"
+ "^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSBBC{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}"
+ "^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSBBC{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}16@0:8"
+ "af1c6ec62137d81cf873e8c8cb495d93ee035f68519eff202b84ee30b63afd58"
+ "cc_xpc_create_connection"
+ "cc_xpc_create_connection_block_invoke"
+ "cc_xpc_send_message"
+ "createCCConfigDict"
+ "createPolicyDict"
+ "eb9cd9a1910a8c502dba984f2c99067fe8385aba266fa6a60490b821cc86a40a"
+ "getProfileDictionary"
+ "handleReply"
+ "v24@0:8^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSBBC{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}16"
+ "v24@?0@\"CBUserController\"8@\"NSError\"16"
+ "v32@0:8^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSBBC{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}16i24c28"
+ "v36@0:8I16i20^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSBBC{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}24c32"
- "%s:%06u: invalid xml data\n"
- "%s:%06u: invalid xml data length\n"
- "%s:%06u: invalid xml data ptr\n"
- "%s:%06u: unable to check if profile is installed"
- "%s:%06u: unable to create XPC dictionary\n"
- "%s:%06u: unable to create intermediate directory for logging plist"
- "%s:%06u: unable to write bt profile plist. error code: %d\n"
- "20:56:28"
- "Checking for installed profiles\n"
- "Got an XPC error (handleReply): %s\n"
- "No change in profile configuration\n"
- "Received NULL reply\n"
- "Sep 16 2025"
- "T^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSBBC{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})},N,V_connectionHandle"
- "Transitioning to HandsfreeAoS - device:%{public}s isInAdvancedSniff:%d"
- "XPC Service is %s\n"
- "XPC connection error: %s\n"
- "XPC connection interrupted - will auto-reconnect\n"
- "XPC connection invalidated\n"
- "^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSBBC{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}"
- "^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSBBC{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}16@0:8"
- "cannot create xpc connection"
- "cannot create xpc message"
- "cannot get property value"
- "failed to create MACH service\n"
- "unable to build ccconfig dictionary\n"
- "unable to build result dictionary\n"
- "unable to create ccpipe dict"
- "unable to create ccstream dict"
- "unable to create policy CFNumber"
- "unable to create property list data\n"
- "v24@0:8^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSBBC{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}16"
- "v32@0:8^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSBBC{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}16i24c28"
- "v36@0:8I16i20^{_OI_HCI_CONNECTION={?=SCI^?SsSSCBBSBCB^{_OI_HCI_CONNECTION}}(?={?={?=[6C]}CI^{_OI_HCI_CONNECTION}I^{?}^{?}^v^{_ESCO_SETUP_PARAMS}^{?}^{?}^{?}SSSSCiCCC^{_L2CAP_RECV_DATA}^{_L2CAP_RECV_DATA}I{?=iSSSS}BBBBBBBBB{?=is}BB^vBBBCB[4C][8C]IIIBB{?=[8C]}{?=[8C]}SCCBIICCBC{?=ICCCCSS}B^viSBBBB}{?=^{_OI_HCI_CONNECTION}CCCCCC}{LE_CONNECTION_RECORD={LE_Address=C{?=[6C]}}B{LE_Address=C{?=[6C]}}{LE_Address=C{?=[6C]}}C^{_OI_HCI_CONNECTION}SSSSSSSSSSSSSSSSSSSC[5C]CBBBBBiiiiiBBB{?=SSSSSS}CCCC{?=[8C]}{?=[32C]}II^{_L2CAP_RECV_DATA}IiBIIB^{s_linkedListHolder}BBi^v{?=CIIS}BBBQBSSSSBBC{?=CSCCCCCCCSSCSSSSSCC}BBC{?=is}I}{LE_CIS_RECORD=^{_OI_HCI_CONNECTION}CCCC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}{LE_CIS_EST_DATA=SIIIICCCCCCCSSS}i}{LE_BIS_RECORD=CC{LE_ISO_DATA=SSII{LE_ISO_RECV_DATA=*SS}}i}{OTHER_CONNECTION_RECORD=^{_OI_HCI_CONNECTION}IC^{_L2CAP_RECV_DATA}})}24c32"
- "value is of incorrect type"
- "xpc message is not valid"

```
