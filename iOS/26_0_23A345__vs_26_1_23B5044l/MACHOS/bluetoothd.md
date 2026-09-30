## bluetoothd

> `/usr/sbin/bluetoothd`

```diff

-190.51.1.6.0
-  __TEXT.__text: 0x874108
+191.5.1.1.0
+  __TEXT.__text: 0x877554
   __TEXT.__auth_stubs: 0x4990
-  __TEXT.__objc_stubs: 0x17280
-  __TEXT.__init_offsets: 0x54
-  __TEXT.__objc_methlist: 0x8b34
-  __TEXT.__const: 0x24f7c
-  __TEXT.__gcc_except_tab: 0x6c260
-  __TEXT.__cstring: 0xb3ee7
+  __TEXT.__objc_stubs: 0x173a0
+  __TEXT.__init_offsets: 0x58
+  __TEXT.__objc_methlist: 0x8b3c
+  __TEXT.__const: 0x24fac
+  __TEXT.__gcc_except_tab: 0x6c484
+  __TEXT.__cstring: 0xb4772
   __TEXT.__objc_classname: 0xa07
-  __TEXT.__objc_methname: 0x1bdba
+  __TEXT.__objc_methname: 0x1be71
   __TEXT.__objc_methtype: 0x496a
-  __TEXT.__oslogstring: 0xada7a
+  __TEXT.__oslogstring: 0xadb3d
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0xd4
-  __TEXT.__unwind_info: 0x22e58
+  __TEXT.__unwind_info: 0x22eb8
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0x24e0
-  __DATA_CONST.__got: 0xdc0
+  __DATA_CONST.__got: 0xdc8
   __DATA_CONST.__auth_ptr: 0x210
-  __DATA_CONST.__const: 0x30160
-  __DATA_CONST.__cfstring: 0x233c0
+  __DATA_CONST.__const: 0x30320
+  __DATA_CONST.__cfstring: 0x23500
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd0

   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_arrayobj: 0x1f8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xf078
-  __DATA.__objc_selrefs: 0x6b00
-  __DATA.__objc_ivar: 0x1014
+  __DATA.__objc_const: 0xf0a8
+  __DATA.__objc_selrefs: 0x6b48
+  __DATA.__objc_ivar: 0x1018
   __DATA.__objc_data: 0x1a90
   __DATA.__data: 0x4a78
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x72aaa
+  __DATA.__bss: 0x72b12
   __DATA.__common: 0x6fb8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0E9CADCD-E121-34B0-B639-C1714C7DD2A6
-  Functions: 33322
-  Symbols:   1639
-  CStrings:  43985
+  UUID: A327CA66-256C-3E89-B33C-070ADFEE9003
+  Functions: 33346
+  Symbols:   1640
+  CStrings:  44049
 
Symbols:
+ _OBJC_CLASS_$_CBServer
CStrings:
+ "    HostAwakeVSC          Trigger Host Awake VSC for BD_VSC_REMOTE_AP_WRITE_LOCAL_STATE.\n"
+ "    HostSleptVSC          Trigger Host Slept VSC for BD_VSC_REMOTE_AP_WRITE_LOCAL_STATE.\n"
+ "    restart               Trigger bluetoothd restart manually.\n"
+ "### Failed to publish with error %@"
+ "### Invalid PSM expected: %d, received: %d"
+ "### Invalid device identifier"
+ "### Invalid socket %d"
+ "### Invalid xpc publisher token %llu"
+ "### Server activate failed: %@\n"
+ "-[CBDaemonServer _xpcPublisherConnectionsAddToken:info:]_block_invoke"
+ "-[CBDaemonServer _xpcPublisherConnectionsAddToken:info:]_block_invoke_2"
+ "-[CBDaemonServer _xpcPublisherConnectionsAddToken:info:]_block_invoke_3"
+ "056b468ef4a7246bf08d91d27fb80d6641211385e46c49231344c556b726d338"
+ "20:56:28"
+ "2974cb2f2c08e11b8e5d536ab9c8ec5e519d9149adf767f522a371a2a57889eb"
+ "5781d21efafa3958b73feb2132b454fb069ee116bb771fb7f6581a14bbc551a4"
+ "7891978d09c0fa40ff072eb974e776f3f431d6a018dd3b50d087f279b9dfb02d"
+ "Antenna Desense Info Event: Desense State: %s, Antenna Config: %d, NF Old Antenna: %d, NF New Antenna: %d"
+ "BD_VSC_ENABLE_BT_CORE_DIVERSITY"
+ "BT_VSC_EnableBTCoreDiversity"
+ "Bluetooth FLR Transport hard reset done"
+ "Device %{public}@ is receiving a Rssi Detection Rssi [Avg|Max|median|min] var = %d:%d:%d:%d %d unreliable due to COEX(27) or saturation CoreMotion=%x:%x:%x %{public}s"
+ "Error: Bluetooth FLR Transport hard reset failed"
+ "Found FW file: %s"
+ "HF Sendthread stopped & destoryed before start"
+ "HostAwakeVSC"
+ "HostSleptVSC"
+ "OI_STATUS _ACI_EnableBTCoreDiversity(uint8_t, int8_t, uint8_t, int8_t, uint8_t, BT_VSC_COMPLETE_CB)"
+ "OI_STATUS _BCM_SetLpmEnable(BT_VSC_COMPLETE_CB)"
+ "OI_STATUS _BCM_SetLpmHostWakeScanParameter(LPM_SET_HOSTWAKE_OFFLOAD_SCAN_PARAMS_T *, BT_VSC_COMPLETE_CB)"
+ "PSM"
+ "Sep 16 2025"
+ "Stack halted, %s cmd opcode 0x%4x"
+ "Stream state changed : Media type %d , Active: %d"
+ "TB,N,V_requiresUrgentAssertion"
+ "Unable to send setSleepMode, result: %d"
+ "Warning: BTWake: LPM: DeviceID length truncated to max supported: %d"
+ "XPC subscriber PSM connected: token %llu, %@, %@, 0x%x, 0x%x, %d"
+ "_requiresUrgentAssertion"
+ "c6f6ecfedcc9004f2a083b1c187e68e7d3159fee8be3377c8f08b41adaab6bf9"
+ "com.apple.driver.AppleCentauriManager"
+ "createCCPipeCentauriManagerDict"
+ "createCCStreamCentauriManagerDict"
+ "d84ce3142fa61cd22beef74189754af4c0e56f9a98fa18ff2d9c84610585c349"
+ "df9a4ebeed75ee796aa09fc2a011436ecdb0ad20a3b3391f10dc279bfe16dfcd"
+ "disconnectTimeoutCb - connection is already gone"
+ "feff0aa949da2316fad76d3431dd87a1c59b13b8ce55f3a122251a1eb95e9b2b"
+ "l2capChannel"
+ "peer"
+ "post disconnect timeout when connection is already gone"
+ "psm"
+ "requiresUrgentAssertion"
+ "restart"
+ "setAcceptHandler:"
+ "setBleListenPSM:"
+ "setRequiresUrgentAssertion:"
+ "setServer:"
+ "socketFD"
+ "stringWithCapacity:"
+ "supportsLpmHostWakeOffloadScan supported = %d"
+ "trace exit: handle_CommandComplete DEBUG events in halted mode"
+ "v24@?0@\"CBConnection\"8@?<v@?@\"NSError\">16"
+ "virtual void CBStackDeviceMonitorCPP::streamStateChanged(BTAddress, bool, AudioMediaType, bool)"
- "20:37:38"
- "Aug 26 2025"
- "BTWake: LMP: entering LPM_SET_SCAN_OFFLOAD_PARAMS %p"
- "BTWake: LMP: entering Set_LPM_HostWake_ScanParameters with deviceID %p"
- "BTWake: LMP: entering Set_LPM_HostWake_TxAdvDiagParameters %p"
- "BTWake: LPM: data %@"
- "BTWake: LPM: fScanOffloadParams is nil"
- "BTWake: LPM: mask %@"
- "LPM: test params reason %d, %@"
- "isPrivilegedBundleID:"

```
