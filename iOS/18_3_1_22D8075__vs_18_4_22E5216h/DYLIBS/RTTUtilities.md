## RTTUtilities

> `/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities`

```diff

-456.6.3.0.0
-  __TEXT.__text: 0x21b08
+456.8.6.0.0
+  __TEXT.__text: 0x22770
   __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x168c
+  __TEXT.__objc_methlist: 0x1a58
   __TEXT.__const: 0xe0
   __TEXT.__gcc_except_tab: 0xce8
-  __TEXT.__cstring: 0x15d2
-  __TEXT.__oslogstring: 0x27d6
+  __TEXT.__cstring: 0x165a
+  __TEXT.__oslogstring: 0x2a8e
   __TEXT.__dlopen_cstrs: 0x1c2
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x898
+  __TEXT.__unwind_info: 0x910
   __TEXT.__objc_classname: 0x254
-  __TEXT.__objc_methname: 0x5170
-  __TEXT.__objc_methtype: 0x833
-  __TEXT.__objc_stubs: 0x49c0
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0xd48
+  __TEXT.__objc_methname: 0x52c7
+  __TEXT.__objc_methtype: 0x844
+  __TEXT.__objc_stubs: 0x4b40
+  __DATA_CONST.__got: 0x388
+  __DATA_CONST.__const: 0xd70
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15a0
+  __DATA_CONST.__objc_selrefs: 0x1748
   __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__objc_arraydata: 0x148
+  __DATA_CONST.__objc_arraydata: 0x178
   __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x1660
-  __AUTH_CONST.__objc_const: 0x23c0
+  __AUTH_CONST.__cfstring: 0x1720
+  __AUTH_CONST.__objc_const: 0x1db8
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0xa8
   __DATA.__objc_ivar: 0x130
   __DATA.__data: 0x4a8
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 699
-  Symbols:   1023
-  CStrings:  1540
+  Functions: 721
+  Symbols:   1044
+  CStrings:  1569
 
Symbols:
+ _OBJC_CLASS_$_HCSettings
CStrings:
+ "Active call request with paired call device: %@ for call: %@"
+ "B40@0:8@16@24@32"
+ "Call connected notification: %{private}@"
+ "Call not yet connected. Ignoring request for call %@ in status %d"
+ "Emergency RTT (EmergencyRTTSupported) supported %@ - %d = %@ -- %d"
+ "Emergency relay supported: TU supports: %d, continuity: %d"
+ "EmergencyRTTSupported"
+ "Found paired device"
+ "RTT (RTTSupported) supported %@ - %d = %@"
+ "RTT (ttyIMSSupported) supported %@ - %d = %@ -- %d"
+ "RTTContinuityEmergencyRTTIsSupportedPreference"
+ "RTTEmergencyCloudRelayNumberKey"
+ "RTTSupported"
+ "Relay supported? %d, Emergency relay supported? %d"
+ "Sending pairing challenge to all known devices since id (%@ / %@) could not be matched to a known device: %@"
+ "Storing relay phones: %@ for RTT, %@ for Emergency RTT"
+ "Unable to find paired device"
+ "[Emergency Relay] Checking %{private}@ in %{private}@"
+ "[Emergency Relay] Device doesn't support relay calls"
+ "[RTTRemoteCallActiveCallRequestKey] Sender didn't match. Paired device id: %@, idsID: %@, senderID: %@, senderIDS: %@"
+ "[RTTRemoteCallSendKey] Sender didn't match. Paired device id: %@, idsID: %@, senderID: %@, senderIDS: %@"
+ "_UpdateInfo"
+ "_rapportDevice:matchesID:orAlternateID:"
+ "additionalInfoForPrefenceUpdate"
+ "continuityEmergencyRTTIsSupported"
+ "controlFlags"
+ "currentSupportedTextingType: %ld"
+ "emergencyRelayRTTIsSupported"
+ "idsDeviceIdentifier"
+ "isEmergencyRTTSupported"
+ "isEmergencyRTTSupported: %d, relay: %d"
+ "isEmergencyRTTSupportedForContext:"
+ "isEmergencyRelayRTTSupported"
+ "safeStringForKey:"
+ "sendCallIDChallengeToDeviceId:orAlternateId:"
+ "senderIDS"
+ "setContinuityEmergencyRTTIsSupported:"
+ "setControlFlags:"
- "Active call request for call: %@ with paired call device: %@"
- "Call connected notification: %@"
- "Call not yet connected. Ignoring request for call %@"
- "Paired device id: %@"
- "RTT supported %@ - %d = %@ -- %d"
- "Relay supported? %d"
- "Sending pairing challenge to all known devices since id (%@) could not be matched to a known device: %@"
- "Storing relay phones: %@ for RTT"
- "sendCallIDChallengeToDeviceId:"

```
