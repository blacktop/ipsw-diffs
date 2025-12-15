## callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

-1576.300.31.0.0
-  __TEXT.__text: 0x4802f0
-  __TEXT.__auth_stubs: 0x4be0
-  __TEXT.__objc_stubs: 0x35300
-  __TEXT.__objc_methlist: 0x26ee8
-  __TEXT.__objc_classname: 0x2db6
-  __TEXT.__objc_methname: 0x61a19
-  __TEXT.__objc_methtype: 0x109ab
-  __TEXT.__cstring: 0x2598d
-  __TEXT.__const: 0xe9e0
-  __TEXT.__oslogstring: 0x4c133
-  __TEXT.__gcc_except_tab: 0x29ec
+1576.400.4.0.0
+  __TEXT.__text: 0x48277c
+  __TEXT.__auth_stubs: 0x4c10
+  __TEXT.__objc_stubs: 0x35420
+  __TEXT.__objc_methlist: 0x26ff8
+  __TEXT.__objc_classname: 0x2dcd
+  __TEXT.__objc_methname: 0x61d80
+  __TEXT.__objc_methtype: 0x109f3
+  __TEXT.__cstring: 0x25a2d
+  __TEXT.__const: 0xe9f0
+  __TEXT.__oslogstring: 0x4cb43
+  __TEXT.__gcc_except_tab: 0x2a34
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x86fc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x9168
+  __TEXT.__constg_swiftt: 0x9178
   __TEXT.__swift5_builtin: 0x6cc
   __TEXT.__swift5_reflstr: 0x7ce3
   __TEXT.__swift5_fieldmd: 0x657c

   __TEXT.__swift_as_entry: 0x214
   __TEXT.__swift_as_ret: 0x250
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0xd7f0
+  __TEXT.__unwind_info: 0xd830
   __TEXT.__eh_frame: 0x8ad8
-  __DATA_CONST.__auth_got: 0x2600
+  __DATA_CONST.__auth_got: 0x2618
   __DATA_CONST.__got: 0x2418
-  __DATA_CONST.__auth_ptr: 0x1320
-  __DATA_CONST.__const: 0x182c0
-  __DATA_CONST.__cfstring: 0xae00
-  __DATA_CONST.__objc_classlist: 0xc18
+  __DATA_CONST.__auth_ptr: 0x1330
+  __DATA_CONST.__const: 0x18330
+  __DATA_CONST.__cfstring: 0xae60
+  __DATA_CONST.__objc_classlist: 0xc20
   __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0xac8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x3bd18
-  __DATA.__objc_selrefs: 0x12648
-  __DATA.__objc_ivar: 0x1de0
-  __DATA.__objc_data: 0xd7c0
-  __DATA.__data: 0xf708
-  __DATA.__bss: 0xd600
+  __DATA.__objc_const: 0x3bec0
+  __DATA.__objc_selrefs: 0x126c0
+  __DATA.__objc_ivar: 0x1df0
+  __DATA.__objc_data: 0xd820
+  __DATA.__data: 0xf738
+  __DATA.__bss: 0xd610
   __DATA.__common: 0x9e8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FA008ED8-2394-3204-AED4-AB699D367CDA
-  Functions: 24069
-  Symbols:   2607
-  CStrings:  25179
+  UUID: 0C44F0CE-E029-349A-B3E5-07A583A6BEBD
+  Functions: 24095
+  Symbols:   2610
+  CStrings:  25249
 
Symbols:
+ _$sSS10lowercasedSSyF
+ _TUIsSameWiFiNetworkPingCheckEnabled
+ _TUMinimumSupportedSharePlayProtocolVersion
CStrings:
+ "(IDSMessaging Host->Client) send ping to devices: %@, destinations: %@, for UPI: %@, account: %@, call: %@"
+ "... but we were told to ignore didReceiveLocalNetworkHandshake"
+ "... so we are going to handle the session's didReceiveLocalNetworkHandshake message"
+ "At least one participant in conversation %@ does not support SharePlay. Invalidating session %@"
+ "CSDRelayPingIDSService"
+ "Creating call to screen for request: %@"
+ "Handle incoming %@ message: %@ relayMessageResponse: %ld, device: %@"
+ "HandleDeclineCallInvite: Ignoring %@ message because no call exists for %@ or screening mode: %@"
+ "HandleReceivedCallInvite: Ignoring %@ message because no call exists for %@ or screening mode: %@"
+ "Not adding activity session, as not all participants are on the latest SharePlay version"
+ "Not enforcing shareplay version check due to server over-ride"
+ "Phone app installation check - isInstalled: %d"
+ "SameWiFiPing"
+ "Setting callScreening to %@ self.screening: %@"
+ "T@\"NSMutableSet\",&,N,V_pingDeclinedUniqueProxyIdentifierCache"
+ "T@\"NSMutableSet\",&,N,V_pingSucceededUniqueProxyIdentifierCache"
+ "TB,N,GcanAnswerCall,V_mockCanAnswerCall"
+ "TB,R,N,GisSameWiFiNetworkPingDisabled"
+ "TUIsSameWiFiNetworkPingCheck is not enabled, don't send ping request"
+ "TUIsSameWiFiNetworkPingCheck is not enabled, return"
+ "We already have a call for this %@ message: %@. Updating it with canAnswer property to NO"
+ "We already have a call for this %@ message: %@. Updating it with canAnswer property to YES"
+ "[WARN] All active participants in the call are not on minimum supported shareplay version"
+ "[WARN] One or more participant on %@ is on an older share play protocol %@ version %@"
+ "_canAnswerCallForMessage:fromDevice:"
+ "_mockCanAnswerCall"
+ "_pingDeclinedUniqueProxyIdentifierCache"
+ "_pingSucceededUniqueProxyIdentifierCache"
+ "answerFromScreening set to YES"
+ "beginLocalNetworkHandshakeFromAccount:destinations:options:"
+ "beginLocalNetworkHandshakeFromAccount:destinations:options: not available on IDSService"
+ "caching %@ to pingDeclinedUniqueProxyIdentifierCache because it is screening"
+ "caching %@ to pingSucceededUniqueProxyIdentifierCache because it is screening"
+ "canAnswer is already NO for %@, dont update"
+ "canAnswerCall"
+ "com.apple.private.alloy.phonecontinuity.ping"
+ "didReceiveLocalNetworkHandshake fromID: %@, handshakeSucceeded: %@ message: %@, self.currentSession: %p, context: %@"
+ "handleDeclinedMessageSentToHost message: %@"
+ "handleSameWiFiPingFromHost: Ignoring %@ isHandshakeSuccess: %@ because no call exists for %@ or screening mode: %@"
+ "handleSameWiFiPingFromHost:fromPairedDevice:isHandshakeSuccess:"
+ "handleScreeningChangedFromHost:fromDevice:"
+ "isConnecting: %@, answerRequest: %@"
+ "isPhoneAppInstalled"
+ "isSameWiFiNetworkPingCheckEnabled"
+ "isSameWiFiNetworkPingDisabled"
+ "local-handshake-context-key"
+ "messenger:handledMessage:fromDestination:device:messageResponse:"
+ "mockCanAnswerCall"
+ "notification: %@, call: %@"
+ "pingDeclinedUniqueProxyIdentifierCache"
+ "pingSucceededUniqueProxyIdentifierCache"
+ "remote %@ doesn't have IDSPing service"
+ "remote %@ has IDSPing service"
+ "removing upi %@ from pingDeclinedUniqueProxyIdentifierCache: %@, pingSucceededUniqueProxyIdentifierCache: %@"
+ "same-wifi-network-ping-disabled"
+ "sameWiFiNetworkPingDisabled"
+ "send ping for call"
+ "sendAnswerCallMessageToHostForCall: isEndpointOnCurrentDevice: %@, rs: %lu, cs: %@, status: %lu, answerFromScreening: %@, canAnswerFromReceptionist: %@"
+ "sendPingForCall:"
+ "sendPingWithDestinations: %@, account: %@, options: %@, service: %@"
+ "sendPingWithDestinations:data:"
+ "setCanAnswerCall:"
+ "setCanAnswerCall: %@, self.canAnswerCall: %@"
+ "setMockCanAnswerCall:"
+ "setPingDeclinedUniqueProxyIdentifierCache:"
+ "setPingSucceededUniqueProxyIdentifierCache:"
+ "setting canAnswerCall to NO because it gets ping decline message"
+ "setting canAnswerCall to NO because the device doesn't get invite or decline from host"
+ "setting canAnswerCall to YES because it gets ping succeed message"
+ "telephonyDeviceExists: %d, relayCapableDeviceExists: %d, defaultPairedDeviceExists: %d, phoneAppCoupledRelayCheck: %d"
+ "v32@0:8@\"CSDMessagingRelayMessage\"16B24B28"
+ "v32@0:8@\"NSSet\"16@\"NSData\"24"
+ "v56@0:8@\"CSDRelayIDSMessenger\"16@\"CSDMessagingRelayMessage\"24@\"IDSDestination\"32@\"IDSDevice\"40q48"
- "Creating call to screen"
- "Handle incoming %@ message: %@"
- "handleScreeningChangedFromHost:"
- "messenger:handledMessage:fromDestination:device:isMessageDeclined:"
- "sendAnswerCallMessageToHostForCall: rs: %lu, cs: %@, status: %lu, answerFromScreening: %@, canAnswerFromReceptionist: %@"
- "telephonyDeviceExists: %d, relayCapableDeviceExists: %d, defaultPairedDeviceExists: %d"
- "v52@0:8@\"CSDRelayIDSMessenger\"16@\"CSDMessagingRelayMessage\"24@\"IDSDestination\"32@\"IDSDevice\"40B48"

```
