## bluetoothd

> `/usr/sbin/bluetoothd`

```diff

-191.10.0.0.0
-  __TEXT.__text: 0x879f10
+192.5.2.0.0
+  __TEXT.__text: 0x87bbb8
   __TEXT.__auth_stubs: 0x4990
   __TEXT.__objc_stubs: 0x173a0
   __TEXT.__init_offsets: 0x58
   __TEXT.__objc_methlist: 0x8b3c
-  __TEXT.__const: 0x2503c
-  __TEXT.__gcc_except_tab: 0x6c610
-  __TEXT.__cstring: 0xb4c61
+  __TEXT.__const: 0x2504c
+  __TEXT.__gcc_except_tab: 0x6c760
+  __TEXT.__cstring: 0xb4eaa
   __TEXT.__objc_classname: 0xa07
-  __TEXT.__objc_methname: 0x1be72
-  __TEXT.__objc_methtype: 0x496f
-  __TEXT.__oslogstring: 0xadcf4
+  __TEXT.__objc_methname: 0x1be76
+  __TEXT.__objc_methtype: 0x49af
+  __TEXT.__oslogstring: 0xadf58
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0xd4
-  __TEXT.__unwind_info: 0x22f30
+  __TEXT.__unwind_info: 0x22fb8
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0x24e0
   __DATA_CONST.__got: 0xdc8
   __DATA_CONST.__auth_ptr: 0x210
-  __DATA_CONST.__const: 0x303c8
-  __DATA_CONST.__cfstring: 0x23600
+  __DATA_CONST.__const: 0x304d0
+  __DATA_CONST.__cfstring: 0x236a0
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 1EDFE4A3-D0A2-359B-AB94-F3C0486AF129
-  Functions: 33381
+  UUID: C6FCA5F2-62FA-3D3E-A416-61178950D419
+  Functions: 33417
   Symbols:   1640
-  CStrings:  44091
+  CStrings:  44119
 
CStrings:
+ "(connect:%d disconnect:%d notify:%d delay:%ld wantsObjectDiscoverData:%d transportBridging:%d disableLeGATT:%d ancsRequired:%d hideFromBTSettings:%d initPHYs:%ld PHYoptions:%ld enableControllerBTClockUpdates:%d enableLESynchronizationEvent:%d connectionUseCase:%ld _minRSSILevelForConnection:%ld _waitForConnectionPoll:%d ctkdChosenTransport:%lu) connectingBundles:%@ opportunistic:%d requiresLowLatency:%@"
+ "056A7EBE-02C0-499D-A96A-5F5998C71B38"
+ "20:25:01"
+ "Error, maxPduSize too small : %d"
+ "Error, maxPduSize too small: %d"
+ "FCS enabled but dataLen (%d) is less than 2 bytes, dropping packet"
+ "First packet dataSize (%d) is less than 2 bytes, cannot read SDU length header"
+ "LEConnectionTimeoutSharingHomePodSetup"
+ "Oct 30 2025"
+ "ProximityPairingToken"
+ "Received a START frame while another reassembly is in progress. Discarding."
+ "SystemActivityHelper actionBlk is NULL!"
+ "SystemActivityHelper failed to init due to queue"
+ "SystemActivityHelper isn't initalized!"
+ "SystemActivityHelper setting up fSystemActivityCoalser"
+ "SystemActivityHelper timeout timer exists for 0X%lx"
+ "SystemActivityHelper timeout timer fired. %s removing 0X%lx"
+ "SystemActivityHelper timeout timer starting for %llu ms"
+ "SystemActivityHelper timeout timer stop: 0x%lx"
+ "SystemActivityHelper timer doesn't exist for 0X%lx"
+ "This link is already encrypted, ignoring this request"
+ "T{CallList={vector<BT::CallInfo, std::allocator<BT::CallInfo>>=^{CallInfo}^{CallInfo}{?=^{CallInfo}}}},N,V_calls"
+ "Updated fSystemActivityBitmap 0x%lx"
+ "^v40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}}16"
+ "connectDeviceForApp called for enabling LE Synchronization Events for device \"%{public}@\". Saving new connection options before returning."
+ "dea6c3f2e9003e884bcde070807c8e941ee17dad2458692a47387c4c62a9d994"
+ "i40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}}16"
+ "i48@0:8r^v16{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}}24"
+ "isValidProximityPairingPayload: Received companyID : %@"
+ "kCBMsgArgLocalLTKType"
+ "kCBMsgArgRemoteLTKType"
+ "systemActivityChanged systemActivityBitMap:0x%lx"
+ "v40@0:8{CallList={vector<BT::CallInfo, std::allocator<BT::CallInfo>>=^{CallInfo}^{CallInfo}{?=^{CallInfo}}}}16"
+ "v48@0:8^v16{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}}24"
+ "v52@0:8i16^v20{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}}28"
+ "v60@0:8i16^v20{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}}28^v52"
+ "v60@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}}8Q32Q40Q48i56"
+ "{CallList=\"fCalls\"{vector<BT::CallInfo, std::allocator<BT::CallInfo>>=\"__begin_\"^{CallInfo}\"__end_\"^{CallInfo}\"\"{?=\"__cap_\"^{CallInfo}}}}"
+ "{CallList={vector<BT::CallInfo, std::allocator<BT::CallInfo>>=^{CallInfo}^{CallInfo}{?=^{CallInfo}}}}16@0:8"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}}16@0:8"
+ "{map<std::string, BT::XpcAudioPluginDevice *, std::less<std::string>, std::allocator<std::pair<const std::string, BT::XpcAudioPluginDevice *>>>=\"__tree_\"{__tree<std::__value_type<std::string, BT::XpcAudioPluginDevice *>, std::__map_value_compare<std::string, std::__value_type<std::string, BT::XpcAudioPluginDevice *>, std::less<std::string>>, std::allocator<std::__value_type<std::string, BT::XpcAudioPluginDevice *>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{vector<BT::XpcAudioPluginClient *, std::allocator<BT::XpcAudioPluginClient *>>=\"__begin_\"^^{XpcAudioPluginClient}\"__end_\"^^{XpcAudioPluginClient}\"\"{?=\"__cap_\"^^{XpcAudioPluginClient}}}"
+ "{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}}24@0:8@16"
- "(connect:%d disconnect:%d notify:%d delay:%ld wantsObjectDiscoverData:%d transportBridging:%d disableLeGATT:%d ancsRequired:%d hideFromBTSettings:%d initPHYs:%ld PHYoptions:%ld enableControllerBTClockUpdates:%d connectionUseCase:%ld _minRSSILevelForConnection:%ld _waitForConnectionPoll:%d ctkdChosenTransport:%lu) connectingBundles:%@ opportunistic:%d requiresLowLatency:%@"
- "06:55:44"
- "Device is already connected & LE Synchronization is not enabled. Sending leEnableSynchronization VSC."
- "Oct 23 2025"
- "Sync Event =%x"
- "T{CallList={vector<BT::CallInfo, std::allocator<BT::CallInfo>>=^{CallInfo}^{CallInfo}^{CallInfo}}},N,V_calls"
- "^v40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}16"
- "i40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}16"
- "i48@0:8r^v16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}24"
- "v40@0:8{CallList={vector<BT::CallInfo, std::allocator<BT::CallInfo>>=^{CallInfo}^{CallInfo}^{CallInfo}}}16"
- "v48@0:8^v16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}24"
- "v52@0:8i16^v20{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}28"
- "v60@0:8i16^v20{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}28^v52"
- "v60@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}8Q32Q40Q48i56"
- "{CallList=\"fCalls\"{vector<BT::CallInfo, std::allocator<BT::CallInfo>>=\"__begin_\"^{CallInfo}\"__end_\"^{CallInfo}\"__cap_\"^{CallInfo}}}"
- "{CallList={vector<BT::CallInfo, std::allocator<BT::CallInfo>>=^{CallInfo}^{CallInfo}^{CallInfo}}}16@0:8"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23C]b7b1}{__long=*Qb63b1})}16@0:8"
- "{map<std::string, BT::XpcAudioPluginDevice *, std::less<std::string>, std::allocator<std::pair<const std::string, BT::XpcAudioPluginDevice *>>>=\"__tree_\"{__tree<std::__value_type<std::string, BT::XpcAudioPluginDevice *>, std::__map_value_compare<std::string, std::__value_type<std::string, BT::XpcAudioPluginDevice *>, std::less<std::string>>, std::allocator<std::__value_type<std::string, BT::XpcAudioPluginDevice *>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{vector<BT::XpcAudioPluginClient *, std::allocator<BT::XpcAudioPluginClient *>>=\"__begin_\"^^{XpcAudioPluginClient}\"__end_\"^^{XpcAudioPluginClient}\"__cap_\"^^{XpcAudioPluginClient}}"
- "{vector<std::string, std::allocator<std::string>>=^v^v^v}24@0:8@16"

```
