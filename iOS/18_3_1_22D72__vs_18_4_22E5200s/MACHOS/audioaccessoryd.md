## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-23.1.1.2.0
-  __TEXT.__text: 0x1b6b50
-  __TEXT.__auth_stubs: 0x27b0
-  __TEXT.__objc_stubs: 0xe0e0
-  __TEXT.__objc_methlist: 0x5d18
-  __TEXT.__const: 0x3a70
-  __TEXT.__gcc_except_tab: 0x352c
-  __TEXT.__cstring: 0x2a963
-  __TEXT.__objc_methname: 0x1503e
-  __TEXT.__objc_classname: 0x689
-  __TEXT.__objc_methtype: 0x23e0
+24.21.0.0.0
+  __TEXT.__text: 0x1abec4
+  __TEXT.__auth_stubs: 0x2760
+  __TEXT.__objc_stubs: 0xe440
+  __TEXT.__objc_methlist: 0x6990
+  __TEXT.__const: 0x3a60
+  __TEXT.__gcc_except_tab: 0x35e4
+  __TEXT.__cstring: 0x2b4c3
+  __TEXT.__objc_methname: 0x15898
+  __TEXT.__objc_classname: 0x693
+  __TEXT.__objc_methtype: 0x2465
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x83ca
   __TEXT.__constg_swiftt: 0x18ec
-  __TEXT.__swift5_typeref: 0x19cc
+  __TEXT.__swift5_typeref: 0x19c4
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_reflstr: 0x16fb
   __TEXT.__swift5_fieldmd: 0x161c

   __TEXT.__swift5_capture: 0x25e8
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x3930
-  __TEXT.__eh_frame: 0x21d8
-  __DATA_CONST.__auth_got: 0x13e8
-  __DATA_CONST.__got: 0xae0
-  __DATA_CONST.__auth_ptr: 0x6f8
-  __DATA_CONST.__const: 0xad68
-  __DATA_CONST.__cfstring: 0x68e0
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __TEXT.__unwind_info: 0x3e88
+  __TEXT.__eh_frame: 0x2208
+  __DATA_CONST.__auth_got: 0x13c0
+  __DATA_CONST.__got: 0xae8
+  __DATA_CONST.__auth_ptr: 0x6e8
+  __DATA_CONST.__const: 0xad78
+  __DATA_CONST.__cfstring: 0x69e0
+  __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x2c8
   __DATA_CONST.__objc_dictobj: 0x4b0
   __DATA_CONST.__objc_intobj: 0x180
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x114b8
-  __DATA.__objc_selrefs: 0x4910
-  __DATA.__objc_ivar: 0xcc0
-  __DATA.__objc_data: 0x20e8
-  __DATA.__data: 0x32c8
+  __DATA.__objc_const: 0x10b10
+  __DATA.__objc_selrefs: 0x4bd0
+  __DATA.__objc_ivar: 0xd34
+  __DATA.__objc_data: 0x1f38
+  __DATA.__data: 0x32b8
   __DATA.__bss: 0x6c90
   __DATA.__common: 0x358
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5868
-  Symbols:   1131
-  CStrings:  8772
+  Functions: 6712
+  Symbols:   1133
+  CStrings:  8930
 
Symbols:
+ _$sSaMa
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initStructMetadataWithLayoutString
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _OBJC_CLASS_$_CUBluetoothClient
- _memset
- _swift_initStructMetadata
CStrings:
+ "\x03!!\x11R\x11\x11%$2\x12\x111!\x12\x11\x12\x13\x126\x14\x13\x13\x12\xb1\x81\x111\x12$1!!H\x12\x12\x13$\x11\x13\x18"
+ "\x04\x12\x13\x11C\x121\x11\x13"
+ "### SystemState Monitor Activate failed: %{error}"
+ "$"
+ "-[AAServicesDaemon _processFirstPartyBannerRequestWithCompletion:]_block_invoke_3"
+ "-[AAServicesXPCConnection _entitledForSystemStateMonitorAndReturnError:]"
+ "-[AAServicesXPCConnection systemStateMonitorActivate:completion:]"
+ "-[AAServicesXPCConnection systemStateMonitorActivate:completion:]_block_invoke"
+ "-[BTServicesDaemon _shareAudioConnectedDiscoveryEnsureStarted]"
+ "-[BTServicesDaemon _shareAudioConnectedDiscoveryEnsureStarted]_block_invoke_3"
+ "-[BTServicesDaemon _shareAudioConnectedDiscoveryEnsureStopped]"
+ "-[BTServicesDaemon _shareAudioSessionStartWithDarwinDevice:cbDevice:]"
+ "-[BTSmartRoutingDaemon _connectToHeadphoneWithAddress:]"
+ "-[BTSmartRoutingDaemon _connectToHeadphoneWithAddress:]_block_invoke"
+ "-[BTSmartRoutingDaemon _getIDSDeviceFromWxLastConnectedHost:]"
+ "-[BTSmartRoutingDaemon _handleMediaPauseStateChanged]_block_invoke"
+ "-[BTSmartRoutingDaemon _isUSBPluggedIn:]"
+ "-[BTSmartRoutingDaemon _mediaRouteMonitorActiveAudioRouteChanged:]_block_invoke_5"
+ "-[BTSmartRoutingDaemon _setTipiAndRoutedStateFlags:forAddress:]"
+ "-[BTSmartRoutingDaemon _startEffectiveUnlockedAfterBootTimer:]"
+ "-[BTSmartRoutingDaemon _startEffectiveUnlockedAfterBootTimer:]_block_invoke"
+ "-[BTSmartRoutingDaemon _updateSRDiscoveredDeviceForPairStateChange:isPaired:]_block_invoke"
+ "-[SRDiscoveredDevice _setRouted:]"
+ "-[SRDiscoveredDevice setAirplaneMode:]"
+ "-[SRDiscoveredDevice setIsPaired:]"
+ "-[SRDiscoveredDevice setIsPairingInProgress:]"
+ "-[SRDiscoveredDevice setIsUSBPlugIn:]"
+ "-[SRDiscoveredDevice setNearbyIsMeLastRoute:]"
+ "-[SRDiscoveredDevice setNearbyUSBPluggedIn:]"
+ "-[SRDiscoveredDevice setNearbyUSBPluggedInTick:]"
+ "-[SRDiscoveredDevice setNearbyUpdateTick:]"
+ "-[SRDiscoveredDevice setPairingBannerClickTick:]"
+ "-[SRDiscoveredDevice setUsbColorCode:]"
+ "-[SRDiscoveredDevice setUsbName:]"
+ "-[SRDiscoveredDevice setUsbProductID:]"
+ "B515cUSBConnected-call"
+ "BT route, make Wx %@ Routed, currently routed %s"
+ "CBIDSManager not ready, skip updating CBDaemon"
+ "ConnectToHeadphoneWithAddress: Failed to connect. Null address"
+ "Connected discovery start"
+ "Connected discovery stop"
+ "Effective unlocked after boot"
+ "EffectiveUnlockedAfterBootTimer: Start timer with delay %us"
+ "Evaluator: InUseBanner, wx %@ addr %@ shouldShow %s trigger %@ inEarSt %s prevInEarSt %s streamState %s isLastHost3rdParty %s isLastHostPaired %s name %@ productID %u iCloudSignedIn %s outOfCaseTime %s timeout %d callStart %.2fs secondsSinceNearbyUSBPlugInUpdate %llu nbUSBConnected %s call %s"
+ "Evaluator: connect complete with address %@ result %@"
+ "Evaluator: connect start with address %@"
+ "Evaluator: headset %@ sources %d inEar %s connectForCallA2DP %s callConnected %s playbackStart %s audioState %s TipiScore1 %s TipiScore2 %s wxUSBPluggedIn %s wxUSBPluggedInLastConnectedToMe %s"
+ "Evaluator: skip, headset %@ is USB plugged in but last connected to another source"
+ "Failed to update SRDisDevice for pair state change. Reason %@"
+ "GetIDSDeviceFromWxLastConnectedHost: comparing, Wx: %@, IDS: %@, Model: %u, name: %@"
+ "Headset is USB plugged in but last connected to another source"
+ "InUseBanner: Skip, USB plug-in to myself"
+ "InUseBanner: Skip, last routed to myself, assume Wx is already connecting"
+ "No discovered device for address %@"
+ "Pairing"
+ "R\x131\x11"
+ "RealityDevice"
+ "Rejected, Remote Category %u > Local Category %u, audio streaming state %d"
+ "Rejected, Remote Category %u >= Local Category %u"
+ "SRCall"
+ "SRDiscoveredDevice: Nearby Wx changed addr %@ name %@ found %s streamState %s productID %u paired %s iCloudSignedIn %s lastConnect %@ usb %s"
+ "SendTipiScoreToWx: %@ score %s srMode %s USB %s byte %@ result %{error}\n"
+ "Session start: Darwin %@, CB %@"
+ "Setting airplaneMode %@ %s -> %s"
+ "Setting colorCode %@ %u -> %u"
+ "Setting isPaired %@ %s -> %s"
+ "Setting isPairingInProgress %@ %s -> %s"
+ "Setting isUSBPlugIn %@ %s -> %s"
+ "Setting nearbyIsMeLastRoute %@ %s -> %s"
+ "Setting nearbyUSBPluggedIn %@ %s -> %s"
+ "Setting nearbyUSBPluggedInTick %@ %llu -> %llu"
+ "Setting nearbyUpdateTick %@ %llu -> %llu"
+ "Setting pairingBannerClickTick %@ %llu -> %llu"
+ "Setting routed for %@ %s -> %s"
+ "Setting usbName %@ %@ -> %@"
+ "Setting usbProductID %@ %u -> %u"
+ "T31\x13"
+ "T@\"CBDevice\",&,N,V_cbDevice"
+ "T@\"NSMutableDictionary\",&,N,V_callMap"
+ "T@\"NSString\",C,N,V_usbName"
+ "T@\"NSString\",R,C,N,V_callUUID"
+ "T@\"NSString\",R,C,N,V_providerBundleIdentifier"
+ "T@\"NSString\",R,C,N,V_providerIdentifier"
+ "T@\"NSString\",R,C,N,V_providerLocalizedName"
+ "TB,N,V_airplaneMode"
+ "TB,N,V_isPaired"
+ "TB,N,V_isPairingInProgress"
+ "TB,N,V_isUSBPlugIn"
+ "TB,N,V_nearbyIsMeLastRoute"
+ "TB,N,V_routed"
+ "TB,R,N"
+ "TB,R,N,V_connected"
+ "TB,R,N,V_connecting"
+ "TB,R,N,V_endpointOnCurrentDevice"
+ "TB,R,N,V_incoming"
+ "TB,R,N,V_outgoing"
+ "TB,R,N,V_providerSystemProvider"
+ "TI,N,V_usbProductID"
+ "TI,N,V_usbcColorCode"
+ "TQ,N,V_nearbyUSBPluggedInTick"
+ "TQ,N,V_nearbyUpdateTick"
+ "TQ,N,V_pairingBannerClickTick"
+ "Tc,N,V_nearbyUSBPluggedIn"
+ "Ti,R,N,V_status"
+ "TipiTableEvent: Wx %@ TipiDevice %@ Conn %s model %@ Flag %u IsMe %s LastPlay %s Ownership %s TipiState %s usb %s"
+ "Tq,N,V_bluetoothStatePrev"
+ "TriangleRecovery: Received companion connect message. wxAddress %@"
+ "TriangleRecovery: Skip, phone has USB plug-in"
+ "TriangleRecovery: SrDeviceNearby %s magnet %s inAnyTipi %s timeout %d isAnyUSBPluggedIn %s"
+ "TriangleRecovery: connect via %@"
+ "USB-C unified audio device: %s -> %s"
+ "USBAudioDevice"
+ "USBCUnifiedDevice"
+ "Updating case version from  %@ -> %@ for device %@"
+ "Wx Device found/updated: %@, headphone Status 0x%0X, bud is %@/%@, source device count: %u audio state: %s lastConnect: %@, tipiScore1: %s, tipiScore2: %s, idle time: %d, outofCaseTime %s, icloud Signed in %@ usb %s"
+ "Wx device is USB plugged in!!! BACK OFF!"
+ "_airplaneMode"
+ "_bluetoothStatePrev"
+ "_callMap"
+ "_callUUID"
+ "_cbDevice"
+ "_connectToHeadphoneWithAddress:"
+ "_connecting"
+ "_effectiveUnlockedAfterBoot"
+ "_effectiveUnlockedAfterBootTimer"
+ "_endpointOnCurrentDevice"
+ "_entitledForSystemStateMonitorAndReturnError:"
+ "_getIDSDeviceFromWxLastConnectedHost:"
+ "_incoming"
+ "_isAnyUSBAudioDevicePluggedIn"
+ "_isPaired"
+ "_isPairingInProgress"
+ "_isUSBPlugIn"
+ "_isUSBPluggedIn:"
+ "_isWxPaired:"
+ "_localDeviceAudioCatogory check failed, _localDeviceAudioCatogory : %d"
+ "_nearbyIsMeLastRoute"
+ "_nearbyUSBPluggedIn"
+ "_nearbyUSBPluggedInTick"
+ "_nearbyUpdateTick"
+ "_outgoing"
+ "_pairingBannerClickTick"
+ "_pairingTimer"
+ "_prefSmartRoutingUSBAudioDevice"
+ "_providerBundleIdentifier"
+ "_providerIdentifier"
+ "_providerLocalizedName"
+ "_providerSystemProvider"
+ "_routed"
+ "_sendAudioCategoryViaWx:"
+ "_setRouted:"
+ "_setTipiAndRoutedStateFlags:forAddress:"
+ "_shareAudioConnectedDeviceDiscovery"
+ "_shareAudioConnectedDiscoveryEnsureStarted"
+ "_shareAudioConnectedDiscoveryEnsureStopped"
+ "_shareAudioSessionStartWithDarwinDevice:cbDevice:"
+ "_sourceModelNameFromModelIdentifier:"
+ "_startEffectiveUnlockedAfterBootTimer:"
+ "_status"
+ "_submitUSBAudioDeviceMetric:"
+ "_triangleRecoveryInitiatedAddress"
+ "_updateSRDiscoveredDeviceForPairStateChange:isPaired:"
+ "_usbName"
+ "_usbProductID"
+ "_usbcColorCode"
+ "address is null"
+ "airplaneMode"
+ "bluetoothStatePrev"
+ "btAddress is null"
+ "callMap"
+ "cbDevice"
+ "com.apple.AudioAccessorySystemStateService"
+ "com.apple.HeadphoneProxService"
+ "com.apple.bluetooth.SmartRouting.usbConnection"
+ "conferenceCall"
+ "connecting"
+ "disconnectionReason"
+ "endpointOnCurrentDevice"
+ "incoming"
+ "initWithCall:"
+ "isConnecting"
+ "isPaired"
+ "isPairingInProgress"
+ "isUSBPlugIn"
+ "nearbyIsMeLastRoute"
+ "nearbyUSBPluggedIn"
+ "nearbyUSBPluggedInTick"
+ "nearbyUpdateTick"
+ "nearbyWx"
+ "outgoing"
+ "pairingBannerClickTick"
+ "providerBundleIdentifier"
+ "providerIdentifier"
+ "providerLocalizedName"
+ "providerSystemProvider"
+ "proxCardUserActionOnHeadphone:btAddress:withAction:completion:"
+ "queue"
+ "setAirplaneMode:"
+ "setBluetoothStatePrev:"
+ "setCallMap:"
+ "setCbDevice:"
+ "setIsPaired:"
+ "setIsPairingInProgress:"
+ "setIsUSBPlugIn:"
+ "setNearbyIsMeLastRoute:"
+ "setNearbyUSBPluggedIn:"
+ "setNearbyUSBPluggedInTick:"
+ "setNearbyUpdateTick:"
+ "setPairingBannerClickTick:"
+ "setRouted:"
+ "setUsbColorCode:"
+ "setUsbName:"
+ "setUsbProductID:"
+ "setUsbcColorCode:"
+ "shouldUpdateCaseVersion - false. cacheMajorVersion: %u > newMajorVersion:  %u"
+ "shouldUpdateCaseVersion - false. cacheMinorVersion: %u.%u > newMinorVersion: %u.%u"
+ "shouldUpdateCaseVersion - false. cacheRevisionVersion: %u.%u.%u > newRevisionVersion: %u.%u.%u"
+ "shouldUpdateCaseVersion - false. cacheVersion: %d == newVersion: %d"
+ "sourceBluetoothState"
+ "sourceCurrentActiveRoute"
+ "sourceScreenState"
+ "stringValue"
+ "systemStateMonitorActivate:completion:"
+ "usbAudioConnected"
+ "usbName"
+ "usbProductID"
+ "usbState"
+ "usbcColorCode"
+ "v32@0:8@\"AASystemStateMonitor\"16@?<v@?@\"NSError\">24"
+ "v44@0:8@\"AAUSBSupportedDeviceManager\"16@\"NSString\"24C32@?<v@?@\"NSDictionary\"@\"NSError\">36"
+ "v44@0:8@16@24C32@?36"
+ "wxConnectionState"
+ "wxPairState"
- "\x03!!\x11R\x11\x11%$2\x11\x111!\x12\x11\x12\x13\x126\x14\x13\x12\x12\xb1\x81\x111\x12$1!!H\x12\x12\x13#\x11\x13\x18"
- "\x04\x12\x13\x11C\x122\x11\x13"
- "-[AAServicesDaemon _processFirstPartyBannerRequestWithCompletion:]_block_invoke_2"
- "-[BTServicesDaemon _audioQualityShowBanner:title:deviceAddressString:messageKey:messageArgs:timeoutSeconds:]_block_invoke"
- "-[BTServicesDaemon _shareAudioConnectedMonitorEnsureStarted]"
- "-[BTServicesDaemon _shareAudioConnectedMonitorEnsureStopped]"
- "-[BTServicesDaemon _shareAudioSessionStartWithDarwinDevice:wxDevice:]"
- "-[BTServicesDaemon openRadarforAudioQuality]"
- "-[BTSmartRoutingDaemon _handleMediaPauseStateChanged]"
- "-[BTSmartRoutingDaemon _mediaRouteMonitorActiveAudioRouteChanged:]_block_invoke_2"
- "1\x13\x11"
- "1551854"
- "815886"
- "@\"CUBluetoothDevice\""
- "@\"NSSet\""
- "Bluetooth Audio Quality Feedback"
- "Can't construct Array with count < 0"
- "Connected monitor start"
- "CoreBluetooth - HFP Audio | iOS"
- "Division by zero"
- "Division results in an overflow"
- "Evaluator: InUseBanner, wx %@ addr %@ shouldShow %s trigger %@ inEarSt %s prevInEarSt %s streamState %s isLastHost3rdParty %s isLastHostPaired %s name %@ productID %u iCloudSignedIn %s outOfCaseTime %s timeout %d callStart %.2fs"
- "Evaluator: headset %@ sources %d inEar %s connectForCallA2DP %s callConnected %s playbackStart %s audioState %s TipiScore1 %s TipiScore2 %s"
- "In Use by Other Device"
- "Keywords"
- "New call is null"
- "Performance"
- "Rejected, Remote Category %d > Local Category %d, audio streaming state %d"
- "Rejected, Remote Category %d >= Local Category %d"
- "SRDiscoveredDevice: Nearby Wx changed addr %@ name %@ found %s streamState %s productID %u paired %s iCloudSignedIn %s lastConnect %@"
- "SendTipiScoreToWx: %@ score %s srMode %s byte %@ result %{error}\n"
- "Session start: Darwin %@, Wx %@"
- "Swift/Array.swift"
- "Swift/IntegerTypes.swift"
- "Swift/UnsafePointer.swift"
- "T$1\x13"
- "T@\"CUBluetoothDevice\",&,N,V_wxDevice"
- "T@\"NSMutableDictionary\",&,N,V_TUCallMap"
- "T@\"NSSet\",&,N,V_conferencingCallSets"
- "TUCallMap"
- "TipiTableEvent: Wx %@ TipiDevice %@ Conn %s model %@ Flag %u IsMe %s LastPlay %s Ownership %s TipiState %s"
- "Triangle recovery: wxAddress %@"
- "TriangleRecovery: SrDeviceNearby %s magnet %s inAnyTipi %s timeout %d"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "Wx Device found/updated: %@, headphone Status 0x%0X, bud is %@/%@, source device count: %u audio state: %s lastConnect: %@, tipiScore1: %s, tipiScore2: %s, idle time: %d, outofCaseTime %s, icloud Signed in %@"
- "_TUCallMap"
- "_conferencingCallSets"
- "_localDeviceAudioCatogory check failed, _localDeviceAudioCatogory : %u"
- "_shareAudioConnectedDeviceMonitor"
- "_shareAudioConnectedMonitorEnsureStarted"
- "_shareAudioConnectedMonitorEnsureStopped"
- "_shareAudioSessionStartWithDarwinDevice:wxDevice:"
- "_tuBargeCallCenter"
- "_wxDevice"
- "addressString"
- "audioQuality - File Radar"
- "audioQuality banner timeout"
- "audioQuality user click, openradar"
- "audioQuality user dismiss"
- "audioQuality: banner action: %s, %{error}"
- "audioQuality: banner error for device %@"
- "callCenterWithQueue:"
- "com.apple.SharingViewService"
- "conferencingCallSets"
- "productIdentifier"
- "setConferencingCallSets:"
- "setDeviceConnectedHandler:"
- "setDeviceDisconnectedHandler:"
- "setTUCallMap:"
- "setWxDevice:"
- "statusFlags"
- "v16@?0@\"CUBluetoothDevice\"8"
- "wxDevice"

```
