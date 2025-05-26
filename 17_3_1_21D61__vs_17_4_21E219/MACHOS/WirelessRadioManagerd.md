## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1630.3.1.0.0
-  __TEXT.__text: 0x12a57c
+1630.4.8.0.0
+  __TEXT.__text: 0x12fcc8
   __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_stubs: 0x1a2e0
-  __TEXT.__objc_methlist: 0xd26c
-  __TEXT.__objc_methname: 0x2860c
-  __TEXT.__cstring: 0x433a8
+  __TEXT.__objc_stubs: 0x1a5c0
+  __TEXT.__objc_methlist: 0xd3ac
+  __TEXT.__objc_methname: 0x28afe
+  __TEXT.__cstring: 0x43d23
   __TEXT.__objc_classname: 0xcf6
-  __TEXT.__objc_methtype: 0x6ad9
+  __TEXT.__objc_methtype: 0x6af4
   __TEXT.__const: 0x21098
-  __TEXT.__gcc_except_tab: 0x35f8
+  __TEXT.__gcc_except_tab: 0x3698
   __TEXT.__dlopen_cstrs: 0x2b4
   __TEXT.__oslogstring: 0x85
-  __TEXT.__unwind_info: 0x3fe0
+  __TEXT.__unwind_info: 0x4064
   __TEXT.__eh_frame: 0x88
   __DATA_CONST.__auth_got: 0xff8
   __DATA_CONST.__got: 0x478
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4570
-  __DATA_CONST.__cfstring: 0x25b20
+  __DATA_CONST.__const: 0x45b8
+  __DATA_CONST.__cfstring: 0x26160
   __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0xc278
-  __DATA_CONST.__objc_arrayobj: 0x55f8
-  __DATA_CONST.__objc_intobj: 0x2bf8
+  __DATA_CONST.__objc_classrefs: 0x520
+  __DATA_CONST.__objc_superrefs: 0x400
+  __DATA_CONST.__objc_arraydata: 0xd890
+  __DATA_CONST.__objc_arrayobj: 0x5e20
+  __DATA_CONST.__objc_intobj: 0x30d8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x170a8
-  __DATA.__objc_selrefs: 0x78d0
-  __DATA.__objc_classrefs: 0x520
-  __DATA.__objc_superrefs: 0x400
-  __DATA.__objc_ivar: 0x1790
+  __DATA.__objc_const: 0x171e8
+  __DATA.__objc_selrefs: 0x79a0
+  __DATA.__objc_ivar: 0x17ac
   __DATA.__objc_data: 0x2670
   __DATA.__data: 0x5b8
-  __DATA.__common: 0x13a
+  __DATA.__common: 0x142
   __DATA.__bss: 0x3f0
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6588
+  Functions: 6624
   Symbols:   732
-  CStrings:  13103
+  CStrings:  13193
 
Symbols:
+ __ZN3ctu5iokit10Controller20setAccessoryCallbackEN8dispatch8callbackIU13block_pointerFvNS0_32TelephonyIOKitAccessoryParameterEEEE
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
CStrings:
+ "7"
+ "AccessoryStateEvent"
+ "Already set 2G antennaSelection %@"
+ "Already set 5G antennaSelection %@"
+ "Already set 6G antennaSelection %@"
+ "CoEx-Table-CellCoex035_V7WiFiEnh"
+ "CoEx-Table-CellCoex036_V7WiFiEnh"
+ "CoEx-Table-CellCoex039_V7WiFiEnh"
+ "CoEx-Table-CellCoex040_V7WiFiEnh"
+ "ConstructAntennaMapXpcMsg:AntPhyIdxDict:AntSpmiIdxDict:"
+ "IOKit State registration: Failed to create WCM_IOKitEventNotifier object"
+ "IOKit state registration: Start WCM_IOKitEventNotifier result: 0x%x"
+ "IOKit state registration: register WCM_IOKitEventNotifier callback result: 0x%x"
+ "PencilCoex"
+ "PencilCoexSupport"
+ "Received handleAppStateChange changeInfo: %@"
+ "Setting TDD profile for 2.4GHz -pencilCoexActive || threadActive is (%d || %d)"
+ "T@\"NSArray\",&,N,V_antennaSelectionEnh2G"
+ "T@\"NSArray\",&,N,V_antennaSelectionEnh5G"
+ "T@\"NSArray\",&,N,V_antennaSelectionEnh6G"
+ "T@\"NSString\",?,R,C"
+ "TB,R,N,V_pencilCoexActive"
+ "TDD_PENCIL"
+ "TDD_THREAD"
+ "TI,N,V_pencilState"
+ "Ti,R,N,V_coexProfile2GTDDReason"
+ "Try to set 2G antennaSelection %@"
+ "Try to set 5G antennaSelection %@"
+ "Try to set 6G antennaSelection %@"
+ "VoIP Delta: TX rate: %f, RX Rate: %f, Diff: %f"
+ "VoIP Delta: TX rate: %f, RX Rate: %f, VoIP active Diff: %f"
+ "WiFiEnh_: with WiFi State (%s), calculated bmWiFiBand %d bitmaps 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x"
+ "YYDebug_ BT OFF not setting antenna selection policy for pencil coex"
+ "YYDebug_ Cannot determine pencil state. This should never happen."
+ "YYDebug_ Carrier %d, UL (%f, %f)"
+ "YYDebug_ ENABLED_UL_CA"
+ "YYDebug_ IOKIT callback pencil state [state = %d]"
+ "YYDebug_ Need to update pencil coex activation condition to %d"
+ "YYDebug_ No need to update pencil coex activation condition. Current condition is %d"
+ "YYDebug_ Pencil Coex is not supported"
+ "YYDebug_ Pencil Coex is supported 3"
+ "YYDebug_ Pencil state attached"
+ "YYDebug_ Pencil state detached"
+ "YYDebug_ Pencil state unknown"
+ "YYDebug_ PolicyManager handle pencil state indication, new pencil state = %d"
+ "YYDebug_ Received BT Antenna PreferenceB Response"
+ "YYDebug_ Setting BT Antenna Policy for pencil coex BT blocking bitmap: %d Thread blocking bitmap: %d"
+ "YYDebug_ Unknown WiFi band for WiFi antenna selection"
+ "YYDebug_ WiFi antenna selection is not supported"
+ "YYDebug_ antennaAction(%u) status(%llu) currentAnt(%llu) previousAnt(%llu)"
+ "YYDebug_ check pencil coex activation condition"
+ "YYDebug_ configure wifi antenna selection with ul freq = (%f, %f) and dl freq = (%f, %f) "
+ "YYDebug_ configureAntennaForCoex: with WiFi State (%s), Pencil coex antenna selection for band 2G, bitmaps 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x"
+ "YYDebug_ configureBTAntennaSelection: BT power state = %d, "
+ "YYDebug_ configureWifiAntennaSelectionForCoex: wifi state = %d, "
+ "YYDebug_ disable BT pencil coex mitigation config"
+ "YYDebug_ enable BT pencil coex mitigation config"
+ "YYDebug_ evaluateULCARestrictions Carrier %d, UL (%f, %f)"
+ "YYDebug_ executing v1/v2 wifi antenna selection in WiFiEnh platforms"
+ "YYDebug_ pencil coex Error: No ULCA config"
+ "YYDebug_ unhandled antenna selection case in Enh antenna selection"
+ "YYDebug_ updating wifi antenna selection for Enh without WiFiEnhCoexSupport"
+ "_antennaSelectionEnh2G"
+ "_antennaSelectionEnh5G"
+ "_antennaSelectionEnh6G"
+ "_coexProfile2GTDDReason"
+ "_pencilCoexActive"
+ "_pencilState"
+ "antennaSelectionEnh2G"
+ "antennaSelectionEnh5G"
+ "antennaSelectionEnh6G"
+ "app category %@, genreID: %llu"
+ "bb_CoEx-Table-CellCoex035_V7WiFiEnh"
+ "bb_CoEx-Table-CellCoex036_V7WiFiEnh"
+ "bb_CoEx-Table-CellCoex039_V7WiFiEnh"
+ "bb_CoEx-Table-CellCoex040_V7WiFiEnh"
+ "coexProfile2GTDDReason"
+ "com.linkedin.LinkedIn"
+ "configureBTAntennaSelection"
+ "configureWifiAntennaSelectionForCoex"
+ "dataConnectionStatusInfo %@"
+ "deviceIsMacBookAir"
+ "evaluateCbrsInDualSimMode Force Recommend dataSlotQuality=%d, anyCallState=%d"
+ "evaluateCbrsInDualSimMode Recommend data on nonPrivateNw SIM %d anyCallState %d"
+ "evaluateCbrsInDualSimMode Recommend data on privateNwSlot %d, dataSlotQuality %llu, anyCallState %d"
+ "getBtBlockedAntennaForPencilCoexByPlatform"
+ "getDeltaIPStats internetInterfaceName=%@"
+ "getInitialIPStats internetInterfaceName=%@"
+ "getInternetInterfaceName"
+ "getUpdatedWifiAntennaSelectionEnhConfigsWithbmWifiEnhAntTx000:bmWiFiEnhAntTx001:bmWiFiEnhAntTx010:bmWiFiEnhAntTx011:bmWiFiEnhAntTx100:bmWiFiEnhAntTx101:bmWiFiEnhAntTx110:bmWiFiEnhAntTx111:bmWiFiBand:"
+ "getWifiAntennaBitmapForPencilCoexByPlatform"
+ "handlePencilStateIndication"
+ "handleStreamingStateChange skip rxVoIPAppNotification %@"
+ "handleStreamingStateChange state=%d appId=%@"
+ "handleStreamingStateChange:appId:"
+ "handleVoIPStateChange skip rxVoIPAppNotification %@"
+ "handleVoIPStateChange state= %d, appId=%@"
+ "handleVoIPStateChange:appId:"
+ "handleVoIPStateChangeConference state=%d appId=%@"
+ "handleVoIPStateChangeConference:appId:"
+ "interfaceName"
+ "invalid applicationBundleId or appState"
+ "isPencilIndicationSupported"
+ "mInternetInterfaceName"
+ "mInternetInterfaceName = %@"
+ "pencilCoexActive"
+ "pencilState"
+ "registerIOkitStateEvent"
+ "setAntennaSelectionEnh2G:"
+ "setAntennaSelectionEnh5G:"
+ "setAntennaSelectionEnh6G:"
+ "setPencilState:"
+ "streaming Delta: TX rate: %f, RX Rate: %f"
+ "threadActive is %d"
+ "updateAntennaSelectionWiFiEnh2G:"
+ "updateAntennaSelectionWiFiEnh5G:"
+ "updateAntennaSelectionWiFiEnh6G:"
+ "updateCellTxPowerLimit"
+ "updatePencilCoexActivationCondition"
+ "updatePencilCoexAntennaSelectionPolicy:param1:param2:"
+ "updateWifiAntennaSelectionV1V2Configs"
+ "v20@?0{TelephonyIOKitAccessoryParameter=III}8"
+ "v88@0:8^S16^S24^S32^S40^S48^S56^S64^S72^S80"
- " Streaming AP Delta TX : %llu, RX: %llu"
- "Ari Camera State registration: Failed to create WCM_IOKitEventNotifier object"
- "Ari Camera State registration: Start WCM_IOKitEventNotifier result: 0x%x"
- "Ari Camera State registration: register WCM_IOKitEventNotifier callback result: 0x%x"
- "BT OFF not setting antenna selection policy antennaConfig(%d)"
- "Calling rxVoIPAppNotification:%d"
- "CoEx-Table-CellCoex035_V6WiFiEnh"
- "CoEx-Table-CellCoex036_V6WiFiEnh"
- "Configure WCI2 Antenna Policy: Param1(%d) Param2(%d)"
- "Delta: TX rate: %f, RX Rate: %f"
- "Delta: TX rate: %f, RX Rate: %f, Diff: %f"
- "Delta: TX rate: %f, RX Rate: %f, VoIP active Diff: %f"
- "Received BT Antenna PreferenceB Response"
- "Received handleAppStateChange dsiplay id: %@"
- "Received handleAppStateChange event, app state: %d , id: %@"
- "Setting BT Antenna Policy: %d"
- "WiFiEnh_: with WiFi State (%s), trying to update antenna selection V2 bitmaps 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x"
- "antennaAction(%u) status(%llu) currentAnt(%llu) previousAnt(%llu)"
- "app category %@, appID: %u"
- "com.apple.WRM.AppMonitor"
- "configureAntennaForCoex"
- "evaluateCbrsInDualSimMode Force Recommend dataSlotQuality=%d, callState=%d"
- "evaluateCbrsInDualSimMode Recommend data on nonPrivateNw SIM %d"
- "evaluateCbrsInDualSimMode Recommend data on privateNwSlot %d, dataSlotQuality %llu"
- "handleStreamingStateChange:"
- "handleVoIPStateChange:"
- "handleVoIPStateChange:%d"
- "handleVoIPStateChangeConference:"
- "handleVoIPStateChangeConference:%d"
- "registerCameraStateEvent"
- "updateAntennaSelectionPolicy:param1:param2:"
- "updateAntennaSelectionWiFiEnh:"
- "v28@0:8i16i20i24"

```
