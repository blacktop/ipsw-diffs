## rapportd

> `/usr/libexec/rapportd`

```diff

-550.8.1.0.0
-  __TEXT.__text: 0xad510
-  __TEXT.__auth_stubs: 0x15d0
-  __TEXT.__objc_stubs: 0xe300
-  __TEXT.__objc_methlist: 0x6264
-  __TEXT.__cstring: 0x262c4
-  __TEXT.__objc_classname: 0x95e
-  __TEXT.__objc_methname: 0x1415d
-  __TEXT.__objc_methtype: 0x369c
-  __TEXT.__const: 0x1d78
-  __TEXT.__gcc_except_tab: 0x160c
+580.4.2.0.0
+  __TEXT.__text: 0xaf140
+  __TEXT.__auth_stubs: 0x15e0
+  __TEXT.__objc_stubs: 0xe480
+  __TEXT.__objc_methlist: 0x6324
+  __TEXT.__cstring: 0x2677b
+  __TEXT.__objc_classname: 0x960
+  __TEXT.__objc_methname: 0x14545
+  __TEXT.__objc_methtype: 0x36be
+  __TEXT.__const: 0x1e38
+  __TEXT.__gcc_except_tab: 0x162c
   __TEXT.__oslogstring: 0x1a8
-  __TEXT.__unwind_info: 0x1cf4
-  __DATA_CONST.__auth_got: 0xaf8
+  __TEXT.__unwind_info: 0x1d10
+  __DATA_CONST.__auth_got: 0xb00
   __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x3918
-  __DATA_CONST.__cfstring: 0x4fa0
+  __DATA_CONST.__const: 0x39a0
+  __DATA_CONST.__cfstring: 0x5120
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_classrefs: 0x458
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_intobj: 0x330
+  __DATA_CONST.__objc_arraydata: 0x58
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xd500
-  __DATA.__objc_selrefs: 0x41c0
-  __DATA.__objc_ivar: 0xcdc
+  __DATA.__objc_const: 0xd600
+  __DATA.__objc_selrefs: 0x4238
+  __DATA.__objc_ivar: 0xcf4
   __DATA.__objc_data: 0x1310
   __DATA.__data: 0x1e40
-  __DATA.__bss: 0x3c0
+  __DATA.__bss: 0x400
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2849
-  Symbols:   477
-  CStrings:  7789
+  Functions: 2871
+  Symbols:   480
+  CStrings:  7855
 
Symbols:
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantDictionary
+ _os_variant_has_internal_content
CStrings:
+ "\x11\x15\x12X#\x11\x13$\x13\"\x11\x12\x12\x12\x14\x11\x11\x14\x15\x15\x12=\x14\x11A\x11\x11\x18"
+ "\x1a"
+ " I "
+ " Nm "
+ "\"\x13\x14"
+ "%@ -> %@\n"
+ "%~@ -> %~@\n"
+ "'%@'"
+ "'%~@'"
+ ", AID "
+ ", Hm "
+ ", MeDev F "
+ ", Nm "
+ ", WiFi "
+ ", isKnownIdentity %@, supportsApplicationLabel %@"
+ ", isUnsupportedApplicationLabel '%d'"
+ "-[RPNFCTransactionController invalidateTransaction:]"
+ "-[RPNearFieldDaemonController _createValidationPayload]"
+ "-[RPNearFieldDaemonController _supportsApplicationLabel:]"
+ "-[RPNearFieldDaemonController transactionController:requestMessageForType:]"
+ "1.1"
+ "580.4.2"
+ "@24@0:8B16B20"
+ "@32@0:8@16Q24"
+ "@56@0:8@16B24@28@36@44B52"
+ "@72@0:8@16@24@32@40B48@52B60B64B68"
+ "Auth AWDL Pairing Mode device changed: %@\n"
+ "Auth AWDL Pairing Mode device found: %@\n"
+ "Auth AWDL Pairing Mode device lost because pairing mode flag lost: %@\n"
+ "Auth AWDL Pairing Mode device lost: %@\n"
+ "ConnectionDate %@\n"
+ "Error %@\n"
+ "HomeKit SelfAccessory accountID: "
+ "HomeKit SelfAccessory homeKitUserIdentifiers: "
+ "ID %@\n"
+ "PersonalIDSDeviceIdentifier (me device) changed: "
+ "Pref: '%@' = '%~@'\n"
+ "Prune friend account identity with empty identifier: %@\n"
+ "RPNFCTransaction\n"
+ "RPNearFieldTap ID %{mask}, appLabel %@, appDomain %@, date %@ sameAccount %d CNID %@"
+ "RPSupportsApplicationLabelKey"
+ "Received non-accept response from all devices for selected person: %{mask}@\n"
+ "RemoteAuthenticationMessage %@\n"
+ "RemoteIdentity %@\n"
+ "RemoteValidationMessage %@\n"
+ "Remove identity %@"
+ "Role %@\n"
+ "Save identity %@"
+ "State %@\n"
+ "T@\"NSNumber\",R,N,V_supportsApplicationLabel"
+ "T@\"NSString\",R,N,V_applicationDomain"
+ "T@\"RPTransportServiceHandoverMessage\",&,N,V_localAuthenticationMessage"
+ "T@\"RPTransportServiceHandoverMessage\",&,N,V_localValidationMessage"
+ "TB,R,N,V_isUnsupportedApplicationLabel"
+ "TapEvent %@\n"
+ "_applicationDomain"
+ "_authenticatedAWDLPairingModeDevices"
+ "_convertToLegacyApplicationLabelIfNeeded:forVersion:"
+ "_convertToUpdatedApplicationLabelIfNeeded:forVersion:"
+ "_isUnsupportedApplicationLabel"
+ "_legacyApplicationLabels"
+ "_localAuthenticationMessage"
+ "_localValidationMessage"
+ "_supportsApplicationLabel"
+ "_supportsApplicationLabel:"
+ "_xpcConnections:withControlFlags:"
+ "airdrop"
+ "applicationDomain"
+ "applicationLabel:%@ is supported.\n"
+ "com.apple.airdrop"
+ "com.apple.airdrop.gamecenter"
+ "com.apple.airdrop.sharesheet"
+ "com.apple.boop.SNAP"
+ "createTapEventWithApplicationLabel:singleBandAWDLModeRequested:pkData:bonjourListenerUUID:identity:isUnsupportedApplicationLabel:"
+ "createValidationPayloadWithKnownIdentity:supportsApplicationLabel:"
+ "creating validation payload with a nil current transaction."
+ "error: authentication request message is nil."
+ "error: response for request message is nil: %@"
+ "error: validation request message is nil."
+ "failed to invalidate current transaction:%@ - mismatching\n"
+ "findAuthAWDLPairingModeDeviceForIdentifier:"
+ "gamecenter"
+ "initWithIdentifier:applicationLabel:pkData:bonjourListenerUUID:isSameAccount:contactID:forceSingleBandAWDLMode:knownIdentity:isUnsupportedApplicationLabel:"
+ "initWithKnownIdentity:supportsApplicationLabel:"
+ "invalidate transaction:%@\n"
+ "invalidateTransaction:"
+ "isUnsupportedApplicationLabel"
+ "localAuthenticationMessage"
+ "localValidationMessage"
+ "privateLoggingEnabled"
+ "setLocalAuthenticationMessage:"
+ "setLocalValidationMessage:"
+ "supportedApplicationLabels"
+ "supportsApplicationLabel"
+ "type:%d version:%@ applicationLabel:%@\n"
+ "updateTrustStatusFlagsWithIdentity:"
- "\x11\x14\x12X#\x11\x13$\x13\"\x11\x12\x12\x12\x14\x11\x11\x14\x15\x15\x12=\x14\x11A\x11\x11\x18"
- "\"\x13\x12"
- ", AID '%@'"
- ", Hm '%@'"
- ", MeDev F<%.8@> I<%.8@> '%@'"
- ", WiFi '%@'"
- ", isKnownIdentity %@"
- "550.8.1"
- "@52@0:8@16B24@28@36@44"
- "@68@0:8@16@24@32@40B48@52B60B64"
- "ConnectionDate %@"
- "Error %@"
- "HomeKit SelfAccessory accountID: %@\n"
- "HomeKit SelfAccessory homeKitUserIdentifiers: %@\n"
- "ID %@"
- "PersonalIDSDeviceIdentifier (me device) changed: %@ -> %@\n"
- "RPNearFieldTap ID %{mask}, appLabel %@, date %@ sameAccount %d CNID %@"
- "Received non-accept response from all devices for selected person: %@\n"
- "RemoteAuthenticationMessage %@"
- "RemoteIdentity %@"
- "RemoteValidationMessage %@"
- "Role %@"
- "State %@"
- "T@\"NSString\",R,C,N"
- "TapEvent %@"
- "createTapEventWithApplicationLabel:singleBandAWDLModeRequested:pkData:bonjourListenerUUID:identity:"
- "createValidationPayloadWithKnownIdentity:"
- "currentApplicationLabel"
- "initWithIdentifier:applicationLabel:pkData:bonjourListenerUUID:isSameAccount:contactID:forceSingleBandAWDLMode:knownIdentity:"
- "initWithKnownIdentity:"

```
