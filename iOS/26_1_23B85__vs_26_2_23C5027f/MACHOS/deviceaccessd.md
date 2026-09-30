## deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

-321.9.0.0.0
-  __TEXT.__text: 0x35d2c
-  __TEXT.__auth_stubs: 0xe10
-  __TEXT.__objc_stubs: 0x4ce0
-  __TEXT.__objc_methlist: 0x1ab8
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x1fd8
-  __TEXT.__objc_methname: 0x6927
-  __TEXT.__objc_classname: 0x1ff
-  __TEXT.__objc_methtype: 0x14c8
-  __TEXT.__cstring: 0xc10a
-  __TEXT.__unwind_info: 0xac0
-  __DATA_CONST.__auth_got: 0x718
-  __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0xf40
-  __DATA_CONST.__cfstring: 0x10e0
-  __DATA_CONST.__objc_classlist: 0x50
+322.6.2.0.0
+  __TEXT.__text: 0x3c058
+  __TEXT.__auth_stubs: 0xf40
+  __TEXT.__objc_stubs: 0x5340
+  __TEXT.__objc_methlist: 0x1c00
+  __TEXT.__const: 0xd0
+  __TEXT.__gcc_except_tab: 0x2598
+  __TEXT.__cstring: 0xd9d7
+  __TEXT.__objc_classname: 0x214
+  __TEXT.__objc_methname: 0x6f34
+  __TEXT.__objc_methtype: 0x158a
+  __TEXT.__unwind_info: 0xbf8
+  __DATA_CONST.__auth_got: 0x7b0
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__const: 0x11f0
+  __DATA_CONST.__cfstring: 0x11c0
+  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0xd8
-  __DATA.__objc_const: 0x2328
-  __DATA.__objc_selrefs: 0x1910
-  __DATA.__objc_ivar: 0x234
-  __DATA.__objc_data: 0x320
-  __DATA.__data: 0x6e0
+  __DATA.__objc_const: 0x2520
+  __DATA.__objc_selrefs: 0x1ab8
+  __DATA.__objc_ivar: 0x258
+  __DATA.__objc_data: 0x370
+  __DATA.__data: 0x750
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/PrivateFrameworks/AccessorySetupKitCore.framework/AccessorySetupKitCore
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BEB2F496-1F23-32B3-899A-AEBC0AEBD759
-  Functions: 969
-  Symbols:   345
-  CStrings:  2551
+  UUID: C66212F2-2117-3197-B093-35DDA3A9F7A4
+  Functions: 1053
+  Symbols:   371
+  CStrings:  2770
 
Symbols:
+ _CBPairingInfoLocalLTK
+ _CBPairingInfoLocalLTKType
+ _CFUUIDCreateFromString
+ _DAExtensionInvalidateReasonToString
+ _OBJC_CLASS_$_ASAccessoryAssetDescriptor
+ _OBJC_CLASS_$_ASAccessoryExperenceRequest
+ _OBJC_CLASS_$_ASAccessoryExperienceLauncher
+ _OBJC_CLASS_$_DAExtensionCoordinator
+ _TCCAccessResetForAccessoryUUID
+ _kTCCServiceAccessoryWiFiNetworkSharing
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _tcc_authorization_record_get_authorization_right
+ _tcc_authorization_record_get_service
+ _tcc_authorization_record_get_subject_identity
+ _tcc_authorization_set_with_accessory_uuid
+ _tcc_events_filter_create_with_criteria
+ _tcc_events_subscribe
+ _tcc_events_unsubscribe
+ _tcc_identity_create
+ _tcc_identity_get_identifier
+ _tcc_identity_get_type
+ _tcc_server_create
+ _tcc_server_message_get_authorization_records_by_identity
+ _tcc_service_get_CF_name
+ _xpc_bool_create
CStrings:
+ "### AddToKeychain %@: %@"
+ "### ConnectionEventDidOccur missing identifier: %@"
+ "### Failed to add to keychain %@: %@"
+ "### FetchFromKeychain %@ '%@': %@"
+ "### LaunchInteractionWithDevice: %@"
+ "### RemoveFromKeychain %@: %@"
+ "### RemovedDevice invalid device identifier: %@"
+ "### ReportServicesChanged invalid device identifier: %@"
+ "### StartDaemonExtensionSession failed: %@"
+ "### StartExtensions failed: %@"
+ "### StopExtensions failed with nil device identifier"
+ "### StopExtensions failed with nil session"
+ "### StopExtensionsIfNeeded: %@"
+ "### _updateDeviceStateForBluetooth prox pairing device, needs pairing   %@"
+ "### appBundleInfoAccessoryOptions proxSupport %@ "
+ "### runProximitySetupWithDiscovery skip: cannot find prox device to onboard"
+ "### runProximitySetupWithDiscovery skip: prox appID missing"
+ "### runProximitySetupWithDiscovery skip: prox config missing"
+ "### updateDADevicesWithInstalledApps proxSupport %@ "
+ "-[DADaemonServer _activate]_block_invoke_10"
+ "-[DADaemonServer _deviceHasAuthorizedExtensionFeature:bundleID:]"
+ "-[DADaemonServer _getAccessoryAuthorizationForDeviceID:]"
+ "-[DADaemonServer _getAccessoryAuthorizationForDeviceID:]_block_invoke"
+ "-[DADaemonServer _handleKeyExchangeEvent:]"
+ "-[DADaemonServer _reportDeviceAccessoryServicesChanged:]"
+ "-[DADaemonServer _reportRemovedDevice:appID:discovery:]"
+ "-[DADaemonServer _resetAllAccessoryServicesForDeviceIdentifier:]"
+ "-[DADaemonServer _setTCCServiceForAccessory:auth:uuid:]_block_invoke"
+ "-[DADaemonServer _startDaemonExtensionSession:error:]"
+ "-[DADaemonServer _startDaemonExtensionSession:error:]_block_invoke"
+ "-[DADaemonServer _startDaemonExtensionSession:error:]_block_invoke_2"
+ "-[DADaemonServer getDevicesWithFlags:appID:pid:]"
+ "-[DADaemonServer getDevicesWithFlags:appID:pid:]_block_invoke"
+ "-[DADaemonServer getDevicesWithFlags:appID:pid:]_block_invoke_4"
+ "-[DADaemonServer receivedDeviceInProximity:serviceData:]"
+ "-[DADaemonServer receivedDeviceInProximity:serviceData:]_block_invoke"
+ "-[DADaemonServer receivedDeviceInProximity:serviceData:]_block_invoke_2"
+ "-[DADaemonServer runProximitySetupWithDiscovery:]"
+ "-[DADaemonServer setUpTCCNotificationForServices]"
+ "-[DADaemonServer setUpTCCNotificationForServices]_block_invoke"
+ "-[DADaemonServer setUpTCCNotificationForServices]_block_invoke_3"
+ "-[DADaemonServer startExtensionsIfNeeded:device:error:]"
+ "-[DADaemonServer startExtensionsIfNeeded:device:error:]_block_invoke"
+ "-[DADaemonServer stopExtensionsIfNeeded:deviceID:reason:error:]"
+ "-[DADaemonServer stopExtensionsIfNeeded:deviceID:reason:error:]_block_invoke"
+ "-[DADaemonXPCConnection _xpcDASessionLaunchInteractionWithDevice:]"
+ "-[DADaemonXPCConnection _xpcDASessionLaunchInteractionWithDevice:]_block_invoke"
+ "-[DAKeychainManager _addToKeychain:error:]_block_invoke"
+ "-[DAKeychainManager _fetchFromKeychain:type:error:]_block_invoke"
+ "-[DAKeychainManager _removeFromKeychain:error:]_block_invoke"
+ "-[DAWiFiScanner pairingRequestCompletedForDataSession:pairingKeyStoreID:deviceID:]"
+ "-[DAWiFiScanner pairingRequestCompletedForPublisher:pairingKeyStoreID:deviceID:]"
+ "@\"CUKeychainManager\""
+ "@\"DAKeychainManager\""
+ "@36@0:8Q16@24i32"
+ "Accessory services changed: %@ "
+ "AccessoryExperienceEvent %@\n"
+ "AccessoryExperienceSession %@ error %@\n"
+ "AccessoryName"
+ "Activate: %@, from %@ for session %@"
+ "Added to keychain %@"
+ "B32@0:8@16^@24"
+ "B48@0:8@16@24Q32^@40"
+ "C24@0:8@16"
+ "C40@0:8@16Q24@32"
+ "CompanyID"
+ "DAKeychainManager"
+ "DaemonExtensionSession event: %@"
+ "Device Image"
+ "Device cannot be nil"
+ "Device has authorized extension feature: %@"
+ "Extension add reuse: %@, total %d"
+ "Extension add start: %@"
+ "Extension coordinator reuse: %@"
+ "Got aonloc XPC event: %@"
+ "Image"
+ "Invalid DeviceID"
+ "Keychain codable class keychain type failed %@"
+ "Keychain codable class type failed %@"
+ "LaunchInteractionWithDevice: %@"
+ "ModelID"
+ "NSAccessorySetupProximityServices"
+ "Needs activate"
+ "No authorized extension feature, missing access info: %@"
+ "No authorized extension feature, missing bundle identifier: %@"
+ "No authorized extension feature, missing services: %@"
+ "No authorized extension feature, not authorized (info): %@"
+ "No authorized extension feature, not authorized (service): %@"
+ "Not an accessory UUID"
+ "ProximityPairingToken"
+ "Q24@0:8Q16"
+ "Reason cannot be nil"
+ "RemovedDevice found existing coordinator: %@ "
+ "RemovedDevice sending event to coordinator: %@ "
+ "ReportServicesChanged device is not connected: %@"
+ "ReportServicesChanged no connected device map: %@"
+ "ReportServicesChanged sending event to coordinator: %@ "
+ "SesLI"
+ "Set '%@' TCCServiceForAccessory authorization:%llu for deviceID: %@"
+ "Set '%@' TCCServiceForAccessory not successful for deviceID: %@ error:%@ "
+ "Start extension for session: %@"
+ "Starting daemon extension for: %@"
+ "StopExtensionsIfNeeded (%@) for %@"
+ "Subscribed to TCC event: %s"
+ "TCC authorization was previously: %lu and now it's removed for deviceIdentifier:%@ serviceName:%@"
+ "Unable to determine accessory UUID"
+ "Unable to determine subject identity for service"
+ "Unknown interaction type"
+ "Unsubscribed to TCC event: %s"
+ "XPC create reply failed"
+ "[WiFi] DeviceID is INVALID"
+ "[WiFi] pairingRequestCompletedForDataSession pairingKeyStoreID='%@', deviceID='%lld'"
+ "[WiFi] pairingRequestCompletedForPublisher Added paired device with deviceID='%lld' pairingUUID='%@'"
+ "_addToKeychain:error:"
+ "_connectedDeviceMap"
+ "_convertToTCCAuth:"
+ "_deviceHasAuthorizedExtensionFeature:bundleID:"
+ "_extensionCoordinatorMap"
+ "_fetchFromKeychain:type:error:"
+ "_getAccessoryAuthorizationForDeviceID `%@` success auth services dict:%@, CFUUID: %@"
+ "_getAccessoryAuthorizationForDeviceID error:%@, CFUUID: %@"
+ "_getAccessoryAuthorizationForDeviceID has missing deviceUUID"
+ "_getAccessoryAuthorizationForDeviceID:"
+ "_handleKeyExchangeEvent:"
+ "_keychainManager"
+ "_lock"
+ "_proxBundleID"
+ "_proxDevicesReceived"
+ "_proxInfoDict"
+ "_removeFromKeychain:error:"
+ "_resetAllAccessoryServicesForDeviceIdentifier not successful"
+ "_resetAllAccessoryServicesForDeviceIdentifier success for CFUUID: %@"
+ "_resetAllAccessoryServicesForDeviceIdentifier:"
+ "_setTCCServiceForAccessory:auth:uuid:"
+ "_startDaemonExtensionSession:error:"
+ "_tccDispatchQueue"
+ "_xpcDASessionLaunchInteractionWithDevice:"
+ "addItem:flags:error:"
+ "addSession:"
+ "addToKeychain:error:"
+ "btuuid"
+ "codable class is nil"
+ "codable object class is nil"
+ "codable object is nil"
+ "com.apple.deviceaccess.tccd.events"
+ "com.apple.proximity.launch"
+ "com.apple.proximity.launch %s"
+ "com.apple.proximity.launch btUUID %@ and serviceData %@"
+ "com.apple.proximity.launch failed due to no service data"
+ "copyItemMatchingItem:flags:error:"
+ "cryptoInfo"
+ "customProperty:"
+ "dictionary representation is nil"
+ "dictionaryRepresentation"
+ "direct"
+ "dvIT"
+ "failed to add keychain item, %@"
+ "failed to copy matching item, %@"
+ "failed to remove matching item, %@"
+ "fetchFromKeychain:type:error:"
+ "getDevicesWithFlags:appID:pid:"
+ "getExtensionPidByType:transport:"
+ "init return obj, %@"
+ "initWithBluetoothIdentifier:pairedCTKD:appConfirmsAuth:pairingRequired:btSCPairing:"
+ "initWithDevice:bundleID:"
+ "initWithDictionary:error:"
+ "initWithIdentifier:secrets:type:"
+ "initWithSymbolName:isTemplate:accessibilityLabel:"
+ "initWithType:device:assetDescriptor:"
+ "invalid identifier"
+ "invalidateWithReason:"
+ "keychain codable object is nil"
+ "keychainType"
+ "launchExperienceWithRequest:eventHandler:completion:"
+ "nil bundle identifier %@"
+ "nil device"
+ "nil device identifier: %@"
+ "no authorized extension feature: %@"
+ "numberWithUnsignedLongLong:"
+ "ppServiceData"
+ "publicKey"
+ "receivedDeviceInProximity: found CBPeripheral, %@"
+ "receivedDeviceInProximity: found btDevcie is already paired %@"
+ "receivedDeviceInProximity: found btDevcie, %@ with modelID %@ _proxInfoDict %@"
+ "receivedDeviceInProximity: found device, %@ for bundle ID %@ and asset %@"
+ "receivedDeviceInProximity:serviceData:"
+ "removeFromKeychain:error:"
+ "removeItemMatchingItem:flags:error:"
+ "removeSession:"
+ "removing TCC accessory for all services failed for deviceID:, %@"
+ "retrievePairingInfoForPeripheral:"
+ "runProximitySetupWithDiscovery:"
+ "runProximitySetupWithDiscovery: for device, %@"
+ "saveDeviceAccessoryServiceInfo: error in resetting TCC accessory wifi network sharing %@"
+ "saveDeviceAccessoryServiceInfo: error in setting the TCC accessory wifi network sharing authorization %@."
+ "secrets"
+ "secrets dictionary is nil"
+ "secureConnectionPairing"
+ "sessionSet"
+ "setAccessoryKey:"
+ "setAllowsBluetoothPairing:"
+ "setCryptoInfo:"
+ "setDeviceFlags:"
+ "setOverrideBundleID:"
+ "setSecrets:"
+ "setUpTCCNotificationForServices"
+ "sharedInstance"
+ "slcR"
+ "startExtensionsIfNeeded:device:error:"
+ "stopExtensionsIfNeeded:deviceID:reason:error:"
+ "substringWithRange:"
+ "update"
+ "v16@?0@\"ASAccessoryExperienceEvent\"8"
+ "v16@?0^{__CFError=}8"
+ "v24@?0@\"ASAccessoryExperienceSession\"8@\"NSError\"16"
+ "v24@?0@\"NSObject<OS_tcc_authorization_record>\"8^{__CFError=}16"
+ "v24@?0Q8@\"NSObject<OS_tcc_authorization_record>\"16"
+ "v32@0:8@16^@24"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "-[DADaemonServer getDevicesWithFlags:appID:]"
- "-[DADaemonServer getDevicesWithFlags:appID:]_block_invoke"
- "-[DADaemonServer getDevicesWithFlags:appID:]_block_invoke_4"
- "No keyStoreID"
- "[WiFi] Session keyStoreID is INVALID"
- "[WiFi] confirmedForPeerDataAddress pairingUUID='%@', deviceID='%lld'"
- "[WiFi] dataConfirmedForHandle Added paired device with deviceID='%lld' pairingUUID='%@'"
- "initWithBluetoothIdentifier:pairedCTKD:appConfirmsAuth:pairingRequired:"

```
