## deviceaccessd

> `filesystem/usr/libexec/deviceaccessd`

```diff

-325.7.1.1.0
-  __TEXT.__text: 0x80d6c
-  __TEXT.__auth_stubs: 0x1f10
-  __TEXT.__objc_stubs: 0x77a0
-  __TEXT.__objc_methlist: 0x24c0
-  __TEXT.__const: 0x1848
-  __TEXT.__cstring: 0x13c94
+325.12.1.0.0
+  __TEXT.__text: 0x84bf4
+  __TEXT.__auth_stubs: 0x1f20
+  __TEXT.__objc_stubs: 0x7d40
+  __TEXT.__objc_methlist: 0x2650
+  __TEXT.__const: 0x1a88
+  __TEXT.__cstring: 0x14804
   __TEXT.__objc_classname: 0x435
-  __TEXT.__gcc_except_tab: 0x3e4c
-  __TEXT.__objc_methname: 0x98da
-  __TEXT.__objc_methtype: 0x1a8a
+  __TEXT.__gcc_except_tab: 0x3fe4
+  __TEXT.__objc_methname: 0x9ffa
+  __TEXT.__objc_methtype: 0x1aea
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__swift5_typeref: 0x90a
   __TEXT.__swift5_fieldmd: 0x460

   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x18a0
+  __TEXT.__unwind_info: 0x19b8
   __TEXT.__eh_frame: 0xbe0
-  __DATA_CONST.__auth_got: 0xf98
-  __DATA_CONST.__got: 0x830
+  __DATA_CONST.__auth_got: 0xfa0
+  __DATA_CONST.__got: 0x858
   __DATA_CONST.__auth_ptr: 0x290
-  __DATA_CONST.__const: 0x2478
-  __DATA_CONST.__cfstring: 0x2180
+  __DATA_CONST.__const: 0x25d8
+  __DATA_CONST.__cfstring: 0x2200
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
-  __DATA.__objc_const: 0x3550
-  __DATA.__objc_selrefs: 0x2528
-  __DATA.__objc_ivar: 0x2dc
+  __DATA.__objc_const: 0x3620
+  __DATA.__objc_selrefs: 0x26a8
+  __DATA.__objc_ivar: 0x2f0
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x1340
   __DATA.__bss: 0xd98

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 83E7F4DA-79D5-36D3-9B5B-B9671FDAE9F6
-  Functions: 2275
-  Symbols:   841
-  CStrings:  4047
+  UUID: 88993635-96B0-39DB-8661-F880D80CC12D
+  Functions: 2371
+  Symbols:   847
+  CStrings:  4176
 
Symbols:
+ _CUPrintNSObjectMasked
+ _DAErrorDomain
+ _DAMessageNotificationsOutgoingExpirationInterval
+ _OBJC_CLASS_$_CBDiscovery
+ __xpc_error_key_description
+ __xpc_type_error
+ _getpid
+ _xpc_connection_send_message_with_reply
- _CFArrayGetTypeID
- _DAExtensionCapabilityFlagFromTCCString
CStrings:
+ "    %@"
+ "    PendingEvent: %@"
+ "### DataDeliveryFailure: %@"
+ "### DataDeliverySuccess: %@"
+ "### DeviceChanged privileged client reply timeout, device: %@, appID: %@"
+ "### Failed to persist updated ratchet state for '%@': %@"
+ "### GetDevices unavailable before first unlock"
+ "### KeyExchangeDone: failed to create internet ratchet: %@"
+ "### MessageStore cleanup for expired messages failed: %@"
+ "### Open: failed to persist ratchet state for '%@': %@"
+ "### RetryEvent: %@"
+ "### RetryEvent: destination is nil"
+ "### RetryEvent: event is nil"
+ "### RetryEvent: event messageID is nil: %@"
+ "### RetryEvent: event sessionID is nil: %@"
+ "### RetryEvent: failed to get extension with type %@: %@"
+ "### RetryEvent: transportType is nil"
+ "### RetryWithDelay: Event is nil"
+ "### RetryWithDelay: ExtensionType is nil"
+ "### RetryWithDelay: TransportType is nil"
+ "### RetryWithDelay: fetch failed for %@: %@"
+ "### RetryWithDelay: message UUID is nil"
+ "### Seal: failed to persist ratchet state for '%@': %@"
+ "### Send event with reply: no connection"
+ "### TransportEvent: %@"
+ "### TransportEventData: %@"
+ "### finalizeCurrentTask %@"
+ "### finalizeCurrentTask called before BT completed — task %@"
+ "### reportDeviceChangedWithReply: called on non-privileged connection (accessLevel %d)"
+ "%@ extension invalidated: %@"
+ "-"
+ "-[DABluetoothPairingManager _centralManager:didConnectPeripheral:]"
+ "-[DABluetoothPairingManager _centralManager:didDisconnectPeripheral:error:]"
+ "-[DABluetoothPairingManager _centralManagerDidUpdateState:]"
+ "-[DABluetoothPairingManager _pairingAgent:peerDidCompletePairing:]"
+ "-[DABluetoothPairingManager _pairingAgent:peerDidFailToCompletePairing:error:]"
+ "-[DABluetoothPairingManager _pairingAgent:peerDidRequestPairing:type:passkey:]"
+ "-[DABluetoothPairingManager _pairingAgent:peerDidUnpair:]"
+ "-[DABluetoothPairingManager _peripheral:didDiscoverServices:]"
+ "-[DABluetoothPairingManager _runNextTask]_block_invoke_5"
+ "-[DABluetoothPairingManager _runNextTask]_block_invoke_6"
+ "-[DABluetoothPairingManager finalizeCurrentTask]_block_invoke"
+ "-[DADaemonServer _createAndPersistInternetRatchetForDevice:error:]"
+ "-[DADaemonServer _openInternetMessage:forDevice:keyID:error:]"
+ "-[DADaemonServer _reportDeviceChanged:appID:discovery:]_block_invoke_3"
+ "-[DADaemonServer _sealInternetMessage:forDevice:error:]"
+ "-[DADaemonServer _updateInternetRatchetStateForDevice:keyID:updatedRatchetData:error:]"
+ "-[DADaemonServer _update]_block_invoke"
+ "-[DADaemonServer addExtensionSession:]_block_invoke_4"
+ "-[DADaemonServer addExtensionSession:]_block_invoke_5"
+ "-[DADaemonServer getDevicesWithFlags:appID:error:]"
+ "-[DADaemonServer getDevicesWithFlags:appID:error:]_block_invoke"
+ "-[DADaemonServer getDevicesWithFlags:appID:error:]_block_invoke_4"
+ "-[DADaemonXPCConnection _xpcExtensionSessionActivate:]_block_invoke_3"
+ "-[DADaemonXPCConnection _xpcSendEventWithReply:completion:]"
+ "-[DADaemonXPCConnection _xpcSendEventWithReply:completion:]_block_invoke"
+ "-[DADaemonXPCConnection reportDeviceChangedWithReply:appID:discovery:completion:]"
+ "-[DAExtensionCoordinator _extensionInvalidatedWithType:]"
+ "-[DAExtensionCoordinator _handleEvent:]"
+ "-[DAExtensionCoordinator _handleEventDataDeliveryFailure:error:]_block_invoke"
+ "-[DAExtensionCoordinator _handleEventDataDeliverySuccess:error:]_block_invoke"
+ "-[DAExtensionCoordinator _handleEventDataDeliverySuccess:error:]_block_invoke_2"
+ "-[DAExtensionCoordinator _handleEventKeyExchange:]"
+ "-[DAExtensionCoordinator _handleEventPublicKey:error:]"
+ "-[DAExtensionCoordinator _handleEventTransport:]"
+ "-[DAExtensionCoordinator _handleEventTransport:]_block_invoke"
+ "-[DAExtensionCoordinator _handleEventTransportData:error:]_block_invoke"
+ "-[DAExtensionCoordinator _retryEvent:toExtensionType:withTransportType:error:]"
+ "-[DAExtensionCoordinator _retryEvent:toExtensionType:withTransportType:error:]_block_invoke"
+ "-[DAExtensionCoordinator _retryWithDelayIfNeeded:toExtension:withTransport:afterDelay:]"
+ "-[DAExtensionCoordinator _retryWithDelayIfNeeded:toExtension:withTransport:afterDelay:]_block_invoke"
+ "@\"NSData\"24@?0@\"NSData\"8^@16"
+ "@40@0:8Q16@24^@32"
+ "@44@0:8@16@24I32^@36"
+ "A7"
+ "Added daemon session: %@"
+ "Adding extension session: %@"
+ "B36@0:8@16@24B32"
+ "B44@0:8@16I24@28^@36"
+ "Could not convert encryptedMessage string to data"
+ "Created internet ratchet with %@: %@"
+ "DABluetoothPairingManager.CB"
+ "DataDeliverySuccess: removed from store: %@"
+ "Devices unavailable before first unlock"
+ "Enrolled flags changed for DeviceID '%@', BundleID '%@': %@ -> %@"
+ "Extension coordinator reuse: %@"
+ "Extension coordinator start: %@"
+ "Extension session add start: %@"
+ "Extension session removed: %@, remaining: %d"
+ "Extension should run: Type %@, Connection %@, KED %s, CapFl %@, EnFl %@"
+ "ExtensionCoordinator event: %@"
+ "Found %@ extension identity: %@"
+ "KeyExchange: %@"
+ "Reporting pending events to: %@"
+ "RetryWithDelay: message %@ is no longer in store"
+ "RetryWithDelay: message %@ is still in store"
+ "Send event with reply error from %@: %s"
+ "Send event with reply received from %@"
+ "Skip reporting to session, extension is not running: %@"
+ "Skip reporting to session, no extension exists for %@"
+ "T@\"DADevice\",&,N,V_restrictedExtensionDevice"
+ "T@?,C,N,V_internetOpenHandler"
+ "T@?,C,N,V_internetSealHandler"
+ "TransportEvent: %@"
+ "Updated existing session: %@"
+ "[AppExtension] XPC connection for appID %@, extension point %@, device %@"
+ "[Device Decoding Error] %@%@"
+ "[RestrictedAppExtension]"
+ "_cbManagerCreationPending"
+ "_cbQueue"
+ "_centralManager:didConnectPeripheral:"
+ "_centralManager:didDisconnectPeripheral:error:"
+ "_centralManagerDidUpdateState:"
+ "_createAndPersistInternetRatchetForDevice:error:"
+ "_currentTransportExtensionType"
+ "_currentTransportType"
+ "_extensionInvalidatedWithType:"
+ "_handleEventDataDeliveryFailure:error:"
+ "_handleEventDataDeliverySuccess:error:"
+ "_handleEventPublicKey:error:"
+ "_handleEventTransport:"
+ "_handleEventTransportData:error:"
+ "_hasDeviceChangedPermission:appID:discovery:"
+ "_internetOpenHandler"
+ "_internetSealHandler"
+ "_openInternetMessage:forDevice:keyID:error:"
+ "_pairingAgent:peerDidCompletePairing:"
+ "_pairingAgent:peerDidFailToCompletePairing:error:"
+ "_pairingAgent:peerDidRequestPairing:type:passkey:"
+ "_pairingAgent:peerDidUnpair:"
+ "_peripheral:didDiscoverServices:"
+ "_restrictedExtensionDevice"
+ "_retryEvent:toExtensionType:withTransportType:error:"
+ "_retryWithDelayIfNeeded:toExtension:withTransport:afterDelay:"
+ "_sealInternetMessage:forDevice:error:"
+ "_sendEncapsulatedKey:"
+ "_startDaemonExtensionSessions"
+ "_updateInternetRatchetStateForDevice:keyID:updatedRatchetData:error:"
+ "_xpcDASessionActivate flags:%@ app:%@ extn:%@ pid:%d accessories[%lu]:%@"
+ "_xpcSendEventWithReply:completion:"
+ "capabilitiesNullable"
+ "capabilityID"
+ "createInternetRatchetWithCryptoInfo:keyID:error:"
+ "createdAt"
+ "dateByAddingTimeInterval:"
+ "devicesWithDiscoveryFlags:error:"
+ "encapsulatedKey"
+ "encryptedMessage"
+ "evRp"
+ "extensionInvalidatedWithType:"
+ "failed get extension with type: %@"
+ "failed to cast data event from super: %@"
+ "failed to cast key exchange event from super: %@"
+ "finalizeCurrentTask"
+ "finalizeCurrentTask before BT completed task %@"
+ "getBytes:length:"
+ "getDeviceForAppExtension:outDevice:"
+ "getDevicesWithFlags:appID:error:"
+ "handleEvent:"
+ "initWithBluetoothIdentifier:pairedCTKD:appConfirmsAuth:pairingRequired:btSCPairing:pairingType:"
+ "initWithDevice:data:"
+ "initWithIdentifier:internetKey:keyID:"
+ "int64ValueSafe"
+ "internetKey"
+ "internetOpenHandler"
+ "internetSealHandler"
+ "invalid event type: %@"
+ "keyID"
+ "no crypto info found for device: %@"
+ "no key for keyID in ring"
+ "no key ring for device"
+ "no outgoing messages with ID %@"
+ "openInternetMessage:ratchetData:keyID:updatedRatchetData:error:"
+ "reportDeviceChangedWithReply:appID:discovery:completion:"
+ "restrictedExtensionDevice"
+ "sealInternetMessage:ratchetData:keyID:updatedRatchetData:error:"
+ "setClientPID:"
+ "setCreatedAt:"
+ "setEventType:"
+ "setInternetOpenHandler:"
+ "setInternetSealHandler:"
+ "setRestrictedExtensionDevice:"
+ "setSupportedTransports:"
+ "stringByTrimmingCharactersInSet:"
+ "supportedTransports"
+ "v24@0:8^@16"
+ "v48@0:8@16q24Q32^@40"
+ "v48@0:8@16q24Q32d40"
+ "validateASKPermissionForDevice:appID:"
+ "whitespaceCharacterSet"
- "### KeyExchangeDone: failed to derive internet key: %@"
- "### KeyExchangeDone: failed to persist internet key ring: %@"
- "### TransportLocal: %@"
- "### _xpcReportDAEvent device %@ not allowed for session %@"
- "%@ extension should run: %s, Connected %s, KED %s"
- "-[DABluetoothPairingManager _runNextTask]_block_invoke"
- "-[DABluetoothPairingManager _runNextTask]_block_invoke_2"
- "-[DABluetoothPairingManager centralManager:didConnectPeripheral:]"
- "-[DABluetoothPairingManager centralManager:didDisconnectPeripheral:error:]"
- "-[DABluetoothPairingManager centralManagerDidUpdateState:]"
- "-[DABluetoothPairingManager pairingAgent:peerDidCompletePairing:]"
- "-[DABluetoothPairingManager pairingAgent:peerDidFailToCompletePairing:error:]"
- "-[DABluetoothPairingManager pairingAgent:peerDidRequestPairing:type:passkey:]"
- "-[DABluetoothPairingManager pairingAgent:peerDidUnpair:]"
- "-[DABluetoothPairingManager peripheral:didDiscoverServices:]"
- "-[DADaemonServer addExtensionSession:]_block_invoke_2"
- "-[DADaemonServer addExtensionSession:]_block_invoke_3"
- "-[DADaemonServer getDevicesWithFlags:appID:pid:]"
- "-[DADaemonServer getDevicesWithFlags:appID:pid:]_block_invoke"
- "-[DADaemonServer getDevicesWithFlags:appID:pid:]_block_invoke_4"
- "-[DADaemonXPCConnection reportDeviceChanged:appID:discovery:]"
- "-[DAExtensionCoordinator _extensionEnsureStartedWithType:]_block_invoke_2"
- "-[DAExtensionCoordinator _handleEvent:]_block_invoke_2"
- "-[DAExtensionCoordinator _handleEventKeyExchangeDone:error:]"
- "-[DAExtensionCoordinator _handleEventKeyReply:error:]"
- "-[DAExtensionCoordinator _handleEventMessageDeliveryStatus:error:]"
- "-[DAExtensionCoordinator _handleEventMessageDeliveryStatus:error:]_block_invoke_2"
- "-[DAExtensionCoordinator _handleEventTransportLocal:]_block_invoke"
- "-[DAExtensionCoordinator _validateCapabilityID:capabilityFlag:error:]"
- "@36@0:8Q16@24i32"
- "A5"
- "Added daemonSession: %@"
- "B36@0:8@16@24i32"
- "Checking service map with bundleID %@: { %@ : %@ }"
- "EXCapabilities"
- "EXExtensionCapabilities"
- "Enrolled capabilities changed: Old %@ -> %@"
- "Exension invalidated with type %@"
- "Extension BundleID match"
- "Extension add start: %@"
- "Extension session add start: %@, Device: %@"
- "ExtensionCoordinator event: %@, %@"
- "Found extension '%@' with capabilities for type %@: %@"
- "Message successfully sent and removed: %@"
- "RemoveExtensionSession Authorized %s, Count %d: %@"
- "Resuming %@"
- "Skip running %@: capability flags %@ do not contain %@"
- "Validated capabilityID '%@': %@"
- "[Device Decoding Error] %@"
- "_EXExtensionCapabilities"
- "_handleEventKeyReply:error:"
- "_handleEventTransportLocal:"
- "_performKeyExchange"
- "_xpcDASessionActivate flags:%@ app:%@ pid:%d accessories:%@"
- "accessoryEncapsulatedKey"
- "deriveInternetKeyWithCryptoInfo:error:"
- "failed to get extension with type %@: %@"
- "failed to get key exchange event from super: %@"
- "generateKeyPairForSuite:publicKey:privateKey:error:"
- "getDevicesWithFlags:appID:pid:"
- "initWithEventType:"
- "initWithIdentifier:internetKey:"
- "isAccessory:allowedForApp:pid:"
- "no outgoing messages for %@"
- "setPrivateKey:"
- "setPublicKey:"
- "updateSessionWithInfo:error:"

```
