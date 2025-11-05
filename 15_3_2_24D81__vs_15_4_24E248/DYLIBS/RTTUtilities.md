## RTTUtilities

> `/System/Library/PrivateFrameworks/RTTUtilities.framework/Versions/A/RTTUtilities`

```diff

-456.6.3.0.0
-  __TEXT.__text: 0x20820
+456.8.7.0.0
+  __TEXT.__text: 0x2163c
   __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x1504
+  __TEXT.__objc_methlist: 0x1870
   __TEXT.__const: 0xe0
   __TEXT.__gcc_except_tab: 0xb10
-  __TEXT.__cstring: 0x120e
-  __TEXT.__oslogstring: 0x2249
+  __TEXT.__cstring: 0x1296
+  __TEXT.__oslogstring: 0x2501
   __TEXT.__dlopen_cstrs: 0xa3
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x7d8
+  __TEXT.__unwind_info: 0x818
   __TEXT.__objc_classname: 0x244
-  __TEXT.__objc_methname: 0x4657
-  __TEXT.__objc_methtype: 0x6a7
-  __TEXT.__objc_stubs: 0x4000
-  __DATA_CONST.__got: 0x2d0
+  __TEXT.__objc_methname: 0x47ae
+  __TEXT.__objc_methtype: 0x6b8
+  __TEXT.__objc_stubs: 0x4180
+  __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1318
+  __DATA_CONST.__objc_selrefs: 0x1490
   __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__objc_arraydata: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x300
-  __AUTH_CONST.__const: 0xde0
-  __AUTH_CONST.__cfstring: 0x1240
-  __AUTH_CONST.__objc_const: 0x2138
+  __AUTH_CONST.__const: 0xe10
+  __AUTH_CONST.__cfstring: 0x1300
+  __AUTH_CONST.__objc_const: 0x1be0
   __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x114

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F74B0DE-92D6-3265-B9C4-C7ED07362EA7
-  Functions: 646
-  Symbols:   1800
-  CStrings:  1485
+  UUID: 1431AEBD-D4DB-3B3E-BACC-52C6C4862D07
+  Functions: 670
+  Symbols:   1836
+  CStrings:  1520
 
Symbols:
+ +[RTTController sharedController].cold.1
+ +[RTTDatabaseManager sharedManager].cold.1
+ +[RTTNanoSettings sharedInstance].cold.1
+ +[RTTServer sharedInstance].cold.1
+ +[RTTSettings sharedInstance].cold.1
+ +[RTTTelephonyUtilities isEmergencyRTTSupportedForContext:]
+ +[RTTTelephonyUtilities isEmergencyRTTSupported]
+ +[RTTTelephonyUtilities isEmergencyRelayRTTSupported]
+ +[RTTTelephonyUtilities sharedCallCenter].cold.1
+ +[RTTTelephonyUtilities sharedUtilityProvider].cold.1
+ -[RTTRemoteCall _rapportDevice:matchesID:orAlternateID:]
+ -[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]
+ -[RTTSettings _registerForNotification:].cold.1
+ -[RTTSettings _selectorMap].cold.1
+ -[RTTSettings continuityEmergencyRTTIsSupported]
+ -[RTTSettings setContinuityEmergencyRTTIsSupported:]
+ -[RTTTelephonyUtilities emergencyRelayRTTIsSupported]
+ -[RTTTelephonyUtilities isEmergencyRTTSupportedForContext:]
+ -[RTTTelephonyUtilities isRTTSupportedForContext:]
+ -[RTTTelephonyUtilities ttyMeContact].cold.1
+ GCC_except_table57
+ GCC_except_table65
+ GCC_except_table70
+ GCC_except_table76
+ GCC_except_table88
+ GCC_except_table92
+ GCC_except_table95
+ _OBJC_CLASS_$_HCSettings
+ __30-[RTTSettings cannedResponses]_block_invoke.176
+ __34-[RTTSettings setCannedResponses:]_block_invoke.187
+ __44-[RTTRemoteCall responseForRequest:options:]_block_invoke.293
+ __44-[RTTRemoteCall responseForRequest:options:]_block_invoke.293.cold.1
+ __48-[RTTTelephonyUtilities iCloudAccountDidChange:]_block_invoke.121
+ __51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.116
+ __51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.118
+ __61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke.282
+ ___61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke
+ ___61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40s48s_e38_B32?0"RPCompanionLinkDevice"8Q16^B24l
+ ___block_descriptor_64_e8_32s40s48s56s_e15_v32?0816^B24l
+ ___copy_helper_block_e8_32s40s48s56s
+ ___destroy_helper_block_e8_32s40s48s56s
+ __block_literal_global.122
+ __block_literal_global.179
+ __block_literal_global.339
+ __block_literal_global.345
+ __block_literal_global.84
+ __block_literal_global.89
+ _objc_msgSend$_rapportDevice:matchesID:orAlternateID:
+ _objc_msgSend$additionalInfoForPrefenceUpdate
+ _objc_msgSend$continuityEmergencyRTTIsSupported
+ _objc_msgSend$controlFlags
+ _objc_msgSend$emergencyRelayRTTIsSupported
+ _objc_msgSend$idsDeviceIdentifier
+ _objc_msgSend$isEmergencyRTTSupported
+ _objc_msgSend$isEmergencyRTTSupportedForContext:
+ _objc_msgSend$isEmergencyRelayRTTSupported
+ _objc_msgSend$safeStringForKey:
+ _objc_msgSend$sendCallIDChallengeToDeviceId:orAlternateId:
+ _objc_msgSend$setContinuityEmergencyRTTIsSupported:
+ _objc_msgSend$setControlFlags:
+ sharedInstance.Settings.336
+ sharedInstance.onceToken.337
- -[RTTRemoteCall sendCallIDChallengeToDeviceId:]
- GCC_except_table53
- GCC_except_table54
- GCC_except_table62
- GCC_except_table67
- GCC_except_table73
- GCC_except_table85
- GCC_except_table89
- GCC_except_table93
- __30-[RTTSettings cannedResponses]_block_invoke.167
- __34-[RTTSettings setCannedResponses:]_block_invoke.178
- __44-[RTTRemoteCall responseForRequest:options:]_block_invoke.288
- __47-[RTTRemoteCall sendCallIDChallengeToDeviceId:]_block_invoke.282
- __48-[RTTTelephonyUtilities iCloudAccountDidChange:]_block_invoke.109
- __51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.104
- __51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.106
- ___47-[RTTRemoteCall sendCallIDChallengeToDeviceId:]_block_invoke
- ___47-[RTTRemoteCall sendCallIDChallengeToDeviceId:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s48s_e15_v32?0816^B24l
- __block_literal_global.117
- __block_literal_global.170
- __block_literal_global.328
- __block_literal_global.334
- __block_literal_global.81
- __block_literal_global.86
- _objc_msgSend$sendCallIDChallengeToDeviceId:
- sharedInstance.Settings.325
- sharedInstance.onceToken.326
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
