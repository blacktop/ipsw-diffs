## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-471.0.0.0.0
-  __TEXT.__text: 0x159924
-  __TEXT.__auth_stubs: 0x2550
-  __TEXT.__objc_stubs: 0xb8c0
-  __TEXT.__objc_methlist: 0x49d4
-  __TEXT.__const: 0x2e94
-  __TEXT.__gcc_except_tab: 0x23dc
-  __TEXT.__cstring: 0x224f3
-  __TEXT.__objc_methname: 0x10d97
-  __TEXT.__objc_classname: 0x581
-  __TEXT.__objc_methtype: 0x2073
+14.16.2.0.0
+  __TEXT.__text: 0x15ca44
+  __TEXT.__auth_stubs: 0x25a0
+  __TEXT.__objc_stubs: 0xc100
+  __TEXT.__objc_methlist: 0x4d74
+  __TEXT.__const: 0x2ec4
+  __TEXT.__gcc_except_tab: 0x2508
+  __TEXT.__cstring: 0x23a53
+  __TEXT.__objc_methname: 0x11bb3
+  __TEXT.__objc_classname: 0x59b
+  __TEXT.__objc_methtype: 0x2098
   __TEXT.__oslogstring: 0x82ae
   __TEXT.__constg_swiftt: 0x12cc
   __TEXT.__swift5_typeref: 0x16ce

   __TEXT.__swift5_capture: 0x1b08
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x3820
-  __TEXT.__eh_frame: 0x18a8
-  __DATA_CONST.__auth_got: 0x12b8
-  __DATA_CONST.__got: 0x598
+  __TEXT.__unwind_info: 0x38e8
+  __TEXT.__eh_frame: 0x1870
+  __DATA_CONST.__auth_got: 0x12e0
+  __DATA_CONST.__got: 0x5a8
   __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0x9570
-  __DATA_CONST.__cfstring: 0x61c0
-  __DATA_CONST.__objc_classlist: 0x190
+  __DATA_CONST.__const: 0x96f8
+  __DATA_CONST.__cfstring: 0x6460
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x78
+  __DATA_CONST.__objc_classrefs: 0x520
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x2a8
   __DATA_CONST.__objc_dictobj: 0x488
   __DATA_CONST.__objc_intobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0xc980
-  __DATA.__objc_selrefs: 0x3a10
-  __DATA.__objc_protorefs: 0x78
-  __DATA.__objc_classrefs: 0x518
-  __DATA.__objc_superrefs: 0x90
-  __DATA.__objc_ivar: 0xac4
-  __DATA.__objc_data: 0x1648
-  __DATA.__data: 0x2c20
+  __DATA.__objc_const: 0xd110
+  __DATA.__objc_selrefs: 0x3c98
+  __DATA.__objc_ivar: 0xb64
+  __DATA.__objc_data: 0x1698
+  __DATA.__data: 0x2bf8
   __DATA.__bss: 0x56f0
-  __DATA.__common: 0x1f0
+  __DATA.__common: 0x1c0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5116
-  Symbols:   1033
-  CStrings:  7312
+  Functions: 5195
+  Symbols:   1041
+  CStrings:  7592
 
Symbols:
+ _$sSayxGSlsMc
+ _$sSw10copyMemory4fromySW_tF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss6UInt64VN
+ _$ss6UInt64Vs7CVarArgsWP
+ _malloc
+ _memset
CStrings:
+ "\x01!!\x11R\x11\x11%#2\x11\x111!\x11\x11\x12\x13\x126\x13\x13\x11\x12\xb1\x81\x111\x12$1!!H\x12\x12\x13#\x11\x13\x18"
+ "-[BTSmartRoutingDaemon _activate]_block_invoke_7"
+ "-[BTSmartRoutingDaemon _cancelInUseBannerForCallTimer]"
+ "-[BTSmartRoutingDaemon _evaluatorRunInUseBanner:]"
+ "-[BTSmartRoutingDaemon _getIDSDeviceFromBtAddress:]"
+ "-[BTSmartRoutingDaemon _isPhoneCall:]"
+ "-[BTSmartRoutingDaemon _resetInUserBannerShown]"
+ "-[BTSmartRoutingDaemon _resetInUserBannerShown]_block_invoke"
+ "-[BTSmartRoutingDaemon _startInUseBannerTimer]"
+ "-[BTSmartRoutingDaemon _startInUseBannerTimer]_block_invoke"
+ "-[BTSmartRoutingDaemon _updateSRDiscoveredDeviceForCBDeviceChanged:connectionStatus:]"
+ "-[BTSmartRoutingDaemon _updateSRDiscoveredDeviceForNearbyWxChanged:isNearby:]"
+ "-[BTSmartRoutingSourceDevice _setBuiltInMicAudioDeviceID:]"
+ "-[BTSmartRoutingSourceDevice _setBuiltInSpeakerAudioDeviceID:]"
+ "-[BTSmartRoutingSourceDevice _setHijackedByPhoneCall:]"
+ "-[BTSmartRoutingSourceDevice _setShouldStayOnVirtual:]"
+ "-[BTSmartRoutingWxDevice _setOtherTipiDeviceBuildVersion:andMinorBuildVersion:]"
+ "-[SRDiscoveredDevice _setBtAddress:]"
+ "-[SRDiscoveredDevice _setConnectionState:]"
+ "-[SRDiscoveredDevice _setInUseBannerBackoffReason:]"
+ "-[SRDiscoveredDevice _setInUseBannerBackoffTick:]"
+ "-[SRDiscoveredDevice _setInUseBannerShown:]"
+ "-[SRDiscoveredDevice _setIsNearby:]"
+ "-[SRDiscoveredDevice _setMutedSpeakerForRemotePhoneCall:]"
+ "-[SRDiscoveredDevice _setNearbyConnectedSourceCount:]"
+ "-[SRDiscoveredDevice _setNearbyInEar:]"
+ "-[SRDiscoveredDevice _setNearbyLastRouteHost:]"
+ "-[SRDiscoveredDevice _setNearbyName:]"
+ "-[SRDiscoveredDevice _setNearbyOutOfCaseTime:]"
+ "-[SRDiscoveredDevice _setNearbyPaired:]"
+ "-[SRDiscoveredDevice _setNearbyPrevInEar:]"
+ "-[SRDiscoveredDevice _setNearbyProductID:]"
+ "-[SRDiscoveredDevice _setNearbyStreamState:]"
+ "-[SRDiscoveredDevice _setNearbyiCloudSignIn:]"
+ "-[SRDiscoveredDevice _setRouteToWxAfterUnhide:]"
+ "1\x13\x11"
+ "3rdPartyHeadset-PhoneCall"
+ "3rdPartyHeadset-Unlock"
+ "@\"NSSet\""
+ "Assistant not enabled"
+ "BannerAction"
+ "BannerTrigger"
+ "Call State, incoming unconnected: %d, incoming connected: %d, outgoing unconnected: %d, outgoing connected: %d activeCall %d"
+ "Can't construct Array with count < 0"
+ "Cancel InUseBanner timer"
+ "CloudSync: Skip fetch operation for unchanged zone ID: %@ with existing token"
+ "Device1,8229"
+ "Division by zero"
+ "Division results in an overflow"
+ "Evaluator: Evaluating Tipi2.0 eligibility: address %@, identifier %@, fwVersion %@, tipiScore1 %s, tipiScore2 %s, inScore %s, first connection after SR enable %@, connectForCallA2DP %s, wx streaming state %s"
+ "Evaluator: InUseBanner, wx %@ shouldShow %s trigger %@ inEarSt %s prevInEarSt %s streamState %s isLastHost3rdParty %s isLastHostPaired %s name %@ productID %u iCloudSignedIn %s outOfCaseTime %s timeout %d W3 %s callStart %.2fs"
+ "Evaluator: headset %@ sources %d inEar %s connectForCallA2DP %s callConnected %s playbackStart %s audioState %s"
+ "Failed to connect to Wx %@. Nearby Wx not found"
+ "Failed to get IDS device from address %@"
+ "I\x11R\x1a\x1b"
+ "In Use by Other Device"
+ "In-Use banner timeout: %d -> %d"
+ "In-Use banner: %s -> %s"
+ "InUse"
+ "InUseBanner"
+ "InUseBanner: Evaluate it in %ds"
+ "InUseBanner: Getting active nearby Wx %@"
+ "InUseBanner: ResetInUserBannerShown"
+ "InUseBanner: Resetting Wx %@ nearby %s inEar %s connection %s"
+ "InUseBanner: Skip, Missing Wx address"
+ "InUseBanner: Skip, Wx connecting/connected"
+ "InUseBanner: Skip, banner shown already"
+ "InUseBanner: Skip, connected source count is 0"
+ "InUseBanner: Skip, headset not supports SR"
+ "InUseBanner: Skip, not enabled"
+ "InUseBanner: Skip, reason %@"
+ "InUseBanner: Skip, screen locked"
+ "InUseBanner: Timeout. Checking if we should show in-use banner"
+ "InUseBanner: secondsSinceDismiss %.2fs"
+ "Index out of range"
+ "New call is null"
+ "New call uuid is null"
+ "PriortizedCall muteMac: %s -> %s"
+ "PriortizedCall: %s -> %s"
+ "Range requires lowerBound <= upperBound"
+ "ReceivedOwnershipLost: Hijackv2 localScore %@ remoteHijackScore %@"
+ "S$1\x13"
+ "SRDiscoveredDevice"
+ "SRDiscoveredDevice: Clearing Wx %@ state for disconnection"
+ "SRDiscoveredDevice: Nearby Wx changed addr %@ name %@ found %s streamState %s productID %u paired %s iCloudSignedIn %s lastConnect %@"
+ "ScreenLocked"
+ "Setting btaddress %@ -> %@"
+ "Setting builtInMic audio device ID %u -> %u"
+ "Setting builtInSpeaker audio device ID %u -> %u"
+ "Setting connectionState %s -> %s"
+ "Setting hijacked by phone %s -> %s"
+ "Setting inUseBannerBackoff %@ %@ -> %@"
+ "Setting inUseBannerBackoffTick %@ %u -> %u"
+ "Setting inUseBannerShown %@ %s -> %s"
+ "Setting isNearby %@ %s -> %s"
+ "Setting muted speaker for remote phone call %s -> %s"
+ "Setting nearbyConnectedSourceCount %@ %d -> %d"
+ "Setting nearbyInEar %@ %s -> %s"
+ "Setting nearbyLastRouteHost %@ %@ -> %@"
+ "Setting nearbyName %@ %@ -> %@"
+ "Setting nearbyPaired %@ %s -> %s"
+ "Setting nearbyPrevInEar %@ %s -> %s"
+ "Setting nearbyProductID %@ %u -> %u"
+ "Setting nearbyStreamState %@ %s -> %s"
+ "Setting nearbyiCloudSignIn %@ %s -> %s"
+ "Setting otherTipi build version for Wx %@ %d.%d -> %d.%d"
+ "Setting outOfCaseTime %@ %d -> %d"
+ "Setting routeToWxAfterUnhide %@ %s -> %s"
+ "Setting shouldStayOnVirtual %s -> %s"
+ "Skip conferencing call"
+ "Smart Routing Screen On. Existing banner %@"
+ "Smart Routing sending srCapable state : %s"
+ "SmartRouting banner action: %s, type %s %{error}"
+ "Swift/Array.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Range.swift"
+ "Swift/UnsafePointer.swift"
+ "T@\"NSData\",R,N,V_nearbyLastRouteHost"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_routeCheckInUseBannerTimer"
+ "T@\"NSSet\",&,N,V_conferencingCallSets"
+ "T@\"NSString\",&,N,V_bannerAction"
+ "T@\"NSString\",&,N,V_bannerTrigger"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C,N,V_btAddress"
+ "T@\"NSString\",R,C,N,V_nearbyName"
+ "T@\"NSString\",R,N,V_inUseBannerBackoffReason"
+ "T@\"SFDevice\",R,C,N,V_nearbyWxDevice"
+ "TB,N,V_builtInMicRegistered"
+ "TB,N,V_builtInSpeakerRegistered"
+ "TB,R,N,V_inUseBannerShown"
+ "TB,R,N,V_isNearby"
+ "TB,R,N,V_mutedSpeakerForRemotePhoneCall"
+ "TB,R,N,V_nearbyPaired"
+ "TB,R,N,V_nearbyiCloudSignIn"
+ "TB,R,N,V_routeToWxAfterUnhide"
+ "TB,R,N,VhijackedByPhoneCall"
+ "TB,R,N,VshouldStayOnVirtual"
+ "TC,R,N,V_connectionState"
+ "TC,R,N,V_nearbyConnectedSourceCount"
+ "TC,R,N,V_nearbyOutOfCaseTime"
+ "TI,N,VbuiltInMicAudioDeviceID"
+ "TI,N,VbuiltInSpeakerAudioDeviceID"
+ "TI,R,N,V_nearbyProductID"
+ "TQ,N,V_callStartTicks"
+ "TQ,R,N,V_inUseBannerBackoffTick"
+ "TUNotification: %@"
+ "TUNotification: Call state changed incoming %s outgoing %s status %s endpoint %s uuid %@ providerID %@ providerName %@ bundleID %@ isSys %s"
+ "TUNotification: New Call is conferencing call %@"
+ "TUNotification: Outgoing call active"
+ "TUNotification: Outgoing call ended"
+ "TUNotification: Outgoing call sending"
+ "Ti,R,N,V_nearbyInEar"
+ "Ti,R,N,V_nearbyPrevInEar"
+ "TipiTableEvent: Tipi healing attempt succeeded! Booyaaa!!! update the other tipi address %@, model %@ build %d.%d"
+ "Tq,R,N,V_nearbyStreamState"
+ "Tq,R,N,VotherTipiDeviceMajorBuildVersion"
+ "Tq,R,N,VotherTipiDeviceMinorBuildVersion"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "Update case (major) version from %u to %u"
+ "Update case (minor) version from %u.%u to %u.%u"
+ "Update case (revision) version from %u.%u.%u to %u.%u.%u"
+ "UserDismiss"
+ "Webex"
+ "Wx disconnecting"
+ "Zoom"
+ "[Hijackv2] Wx stream state not matches remote score, fallback to legacy hijack"
+ "[Hijackv2] loacl %u vs remote %u isPhoneCallHijack %s CallCount %d otherTipi %@ %d.%d"
+ "_bannerAction"
+ "_bannerTrigger"
+ "_btAddress"
+ "_builtInMicRegistered"
+ "_builtInSpeakerRegistered"
+ "_callStartTicks"
+ "_cancelInUseBannerForCallTimer"
+ "_clearCallSession"
+ "_conferencingCallSets"
+ "_connectionState"
+ "_evaluatorRunInUseBanner:"
+ "_getActiveNearbyWxAdress"
+ "_getIDSDeviceFromBtAddress:"
+ "_getJsonStringFromDictionary:"
+ "_inUseBannerBackoffReason"
+ "_inUseBannerBackoffTick"
+ "_inUseBannerShown"
+ "_inUseBannerTimer"
+ "_isMuteStateChangedBlock"
+ "_isNearby"
+ "_isPhoneCall:"
+ "_mutedSpeakerForRemotePhoneCall"
+ "_nearbyConnectedSourceCount"
+ "_nearbyInEar"
+ "_nearbyLastRouteHost"
+ "_nearbyName"
+ "_nearbyOutOfCaseTime"
+ "_nearbyPaired"
+ "_nearbyPrevInEar"
+ "_nearbyProductID"
+ "_nearbyStreamState"
+ "_nearbyWxDevice"
+ "_nearbyiCloudSignIn"
+ "_notifyOtherTipiCallState:"
+ "_prefSmartRoutingInUseBanner"
+ "_prefSmartRoutingInUseBannerTimeout"
+ "_prefSmartRoutingPrioritizedCall"
+ "_prefSmartRoutingPrioritizedCallMuteMac"
+ "_resetInUserBannerShown"
+ "_routeCheckInUseBannerTimer"
+ "_routeToWxAfterUnhide"
+ "_setBtAddress:"
+ "_setBuiltInMicAudioDeviceID:"
+ "_setBuiltInSpeakerAudioDeviceID:"
+ "_setConnectionState:"
+ "_setHijackedByPhoneCall:"
+ "_setInUseBannerBackoffReason:"
+ "_setInUseBannerBackoffTick:"
+ "_setInUseBannerShown:"
+ "_setIsNearby:"
+ "_setMutedSpeakerForRemotePhoneCall:"
+ "_setNearbyConnectedSourceCount:"
+ "_setNearbyInEar:"
+ "_setNearbyLastRouteHost:"
+ "_setNearbyName:"
+ "_setNearbyOutOfCaseTime:"
+ "_setNearbyPaired:"
+ "_setNearbyPrevInEar:"
+ "_setNearbyProductID:"
+ "_setNearbyStreamState:"
+ "_setNearbyWxDevice:"
+ "_setNearbyiCloudSignIn:"
+ "_setOtherTipiDeviceBuildVersion:andMinorBuildVersion:"
+ "_setShouldStayOnVirtual:"
+ "_srDiscoveredDeviceMap"
+ "_startInUseBannerTimer"
+ "_tuCallCenter"
+ "_updateOtherTipiBuildVersion:"
+ "_updateSRDiscoveredDeviceForCBDeviceChanged:connectionStatus:"
+ "_updateSRDiscoveredDeviceForNearbyWxChanged:isNearby:"
+ "a\x12\"\x16\x14"
+ "assistantIsEnabled"
+ "bannerTrigger"
+ "builtInMicAudioDeviceID"
+ "builtInMicRegistered"
+ "builtInSpeakerAudioDeviceID"
+ "builtInSpeakerRegistered"
+ "callCenterWithQueue:"
+ "callStartTicks"
+ "callState"
+ "conferencingCallSets"
+ "connectionState"
+ "google.Tachyon"
+ "google.meetings"
+ "hijackedByPhoneCall"
+ "inUseBannerBackoffReason"
+ "inUseBannerBackoffTick"
+ "inUseBannerShown"
+ "initWithData:encoding:"
+ "isNearby"
+ "isSystemProvider"
+ "mutedSpeakerForRemotePhoneCall"
+ "nearbyConnectedSourceCount"
+ "nearbyInEar"
+ "nearbyLastRouteHost"
+ "nearbyName"
+ "nearbyOutOfCaseTime"
+ "nearbyPaired"
+ "nearbyPrevInEar"
+ "nearbyProductID"
+ "nearbyStreamState"
+ "nearbyWxDevice"
+ "nearbyiCloudSignIn"
+ "otherTipiDeviceMajorBuildVersion"
+ "otherTipiDeviceMinorBuildVersion"
+ "provider"
+ "routeCheckInUseBannerTimer"
+ "setBannerAction:"
+ "setBannerTrigger:"
+ "setBuiltInMicAudioDeviceID:"
+ "setBuiltInMicRegistered:"
+ "setBuiltInSpeakerAudioDeviceID:"
+ "setBuiltInSpeakerRegistered:"
+ "setCallStartTicks:"
+ "setConferencingCallSets:"
+ "setRouteCheckInUseBannerTimer:"
+ "setWithObjects:"
+ "shouldStayOnVirtual"
+ "srInUseBanner"
+ "srInUseBannerTimeout"
+ "srPriortizedCall"
+ "srPriortizedCallMuteMac"
+ "v28@0:8@16C24"
+ "v32@0:8q16q24"
+ "v32@?0@\"NSString\"8@\"SRDiscoveredDevice\"16^B24"
- "\x01!!\x11R\x12%#2\x11\x111!\x11\x11\x13\x126\x13\x13\x11\x12\xb1a\x111\x12$1!!H\x11\x12\x13\"\x11\x13\x18"
- "-[BTSmartRoutingSourceDevice _setRouteToWxAfterUnhide:]"
- "3\x131\x13"
- "Call State, incoming unconnected: %d, incoming connected: %d, outgoing unconnected: %d, outgoing connected: %d"
- "Evaluator: Evaluating Tipi2.0 eligibility: address %@, identifier %@, fwVersion %@, tipiScore1 %s, tipiScore2 %s, inScore %s, first connection after SR enable %@, onDemandConnect %s, wx streaming state %s"
- "Evaluator: headset %@ sources %d inEar %s OnDemandConnect %s callConnected %s playbackStart %s audioState %s"
- "G\x11R\x1a\x1a"
- "Setting routeToWxAfterUnhide %s -> %s"
- "Smart Routing Screen On"
- "SmartRouting banner action: %s, %{error}"
- "TB,N,VrouteToWxAfterUnhide"
- "TUNotification: Call state changed incoming %s outgoing %s status %s endpoint %s uuid %@"
- "TUNotification: New call is null"
- "TUNotification: New call uuid is null"
- "TipiTableEvent: Tipi healing attempt succeeded! Booyaaa!!! update the other tipi address %@, model %@"
- "a\x14\x16\x14"
- "setRouteToWxAfterUnhide:"

```
