## deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

-322.8.0.0.0
-  __TEXT.__text: 0x3c3d8
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_stubs: 0x5360
-  __TEXT.__objc_methlist: 0x1c20
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x2578
-  __TEXT.__cstring: 0xdb01
-  __TEXT.__objc_classname: 0x214
-  __TEXT.__objc_methname: 0x6f72
-  __TEXT.__objc_methtype: 0x159b
-  __TEXT.__unwind_info: 0xbf8
-  __DATA_CONST.__auth_got: 0x7b0
-  __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0x11f0
-  __DATA_CONST.__cfstring: 0x11c0
-  __DATA_CONST.__objc_classlist: 0x58
+323.4.1.0.0
+  __TEXT.__text: 0x41690
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__objc_stubs: 0x5a00
+  __TEXT.__objc_methlist: 0x1e78
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x2948
+  __TEXT.__cstring: 0xecd2
+  __TEXT.__objc_classname: 0x22f
+  __TEXT.__objc_methname: 0x760d
+  __TEXT.__objc_methtype: 0x15e8
+  __TEXT.__unwind_info: 0xd78
+  __DATA_CONST.__auth_got: 0x7d8
+  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__const: 0x1268
+  __DATA_CONST.__cfstring: 0x1220
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_intobj: 0xd8
-  __DATA.__objc_const: 0x2528
-  __DATA.__objc_selrefs: 0x1ac8
-  __DATA.__objc_ivar: 0x258
-  __DATA.__objc_data: 0x370
-  __DATA.__data: 0x750
+  __DATA.__objc_const: 0x2858
+  __DATA.__objc_selrefs: 0x1c88
+  __DATA.__objc_ivar: 0x29c
+  __DATA.__objc_data: 0x3c0
+  __DATA.__data: 0x7c0
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 408C7B5D-ABBB-3C61-B964-3DA78A0F11D3
-  Functions: 1050
-  Symbols:   371
-  CStrings:  2778
+  UUID: B54BFA3C-B1A7-3757-9C8D-1D60B80B2AC0
+  Functions: 1158
+  Symbols:   384
+  CStrings:  2984
 
Symbols:
+ _CUPrintFlags64
+ _DAExtensionCapabilityFlagFromTCCString
+ _DAExtensionTypeToEntitlement
+ _DAExtensionTypeToPointIdentifier
+ _DAExtensionTypeToString
+ _OBJC_CLASS_$_DACrypto
+ _OBJC_CLASS_$_DACryptoInfo
+ _OBJC_CLASS_$_DAEventExtension
+ _OBJC_CLASS_$_DAExtension
+ _OBJC_CLASS_$_DAExtensionEventData
+ _OBJC_CLASS_$_DAExtensionEventKeyExchange
+ _OBJC_CLASS_$_DAExtensionEventLifecycle
+ _OBJC_CLASS_$_DAExtensionSession
+ _OBJC_CLASS_$_DAExtensionSessionConfiguration
- _OBJC_CLASS_$_DAExtensionCoordinator
CStrings:
+ "    %@"
+ "!6"
+ "### DAExtensionSession activate create reply failed"
+ "### DAExtensionSessionActivate failed: %@"
+ "### Extension '%@' cannot be started with missing type: %ld"
+ "### Failed to activate nil extension"
+ "### Failed to create key reply event from: %@"
+ "### Failed to generate keys: %@"
+ "### Failed to get accessory ciphersuite from %@"
+ "### Failed to get accessory crypto info from %@"
+ "### Failed to get accessory public key from %@"
+ "### Failed to get crypto info from %@"
+ "### Failed to get key exchange done event from %@"
+ "### Failed to get key exchange event from %@"
+ "### Failed to get key reply event from %@"
+ "### Failed to start %@ extension, init returned nil"
+ "### Failed to start crypto session for '%@': %@"
+ "### Failed to update session for '%@': %@"
+ "### HandleAccessoryEvent failed to decrypt: %@"
+ "### HandleEventTransportLocal device crypto info is nil: %@"
+ "### HandleEventTransportLocal encryption event data is nil: %@"
+ "### HandleEventTransportLocal encryption event device identifier is nil: %@"
+ "### HandleEventTransportLocal failed to get encryption event from parent: %@"
+ "### HandleEventTransportLocal missing capability: %@"
+ "### Init failed with nil bundle identifier"
+ "### Init failed with nil device"
+ "### Interrupted: %@"
+ "### Invalidated extension missing name: %@"
+ "### ReportEventToExtension failed: %@"
+ "### SaveDeviceAppAccessInfo: failed to create directory at URL %@: %@"
+ "### SendExtensionDataEvent failed: %@"
+ "### SendExtensionDataEvent: %@"
+ "### SetTCCForAccessory '%@' called with invalid serviceName: %@"
+ "### SetTCCForAccessory called with invalid deviceID: %@"
+ "### Unknown invalidated extension: %@"
+ "%@ extension should run"
+ "%s '%@'"
+ ", "
+ "-[DADaemonServer _deviceHasAuthorizedExtensionFeature:bundleID:]_block_invoke_2"
+ "-[DADaemonServer _setTCCServiceForAccessory:auth:uuid:]"
+ "-[DADaemonServer sendExtensionDataEvent:session:error:]"
+ "-[DADaemonServer sendExtensionDataEvent:session:error:]_block_invoke"
+ "-[DADaemonServer startExtensionsIfNeeded:error:]"
+ "-[DADaemonServer startExtensionsIfNeeded:error:]_block_invoke"
+ "-[DADaemonServer startExtensionsIfNeeded:error:]_block_invoke_2"
+ "-[DADaemonServer stopExtensionsIfNeeded:reason:error:]"
+ "-[DADaemonServer stopExtensionsIfNeeded:reason:error:]_block_invoke"
+ "-[DADaemonXPCConnection _xpcDAExtensionSessionActivate:]"
+ "-[DADaemonXPCConnection _xpcDAExtensionSessionActivate:]_block_invoke"
+ "-[DADaemonXPCConnection _xpcSendExtensionEvent:]_block_invoke"
+ "-[DAExtensionCoordinator _activateExtension:]"
+ "-[DAExtensionCoordinator _activateExtension:]_block_invoke"
+ "-[DAExtensionCoordinator _activateExtension:]_block_invoke_2"
+ "-[DAExtensionCoordinator _extensionEnsureStartedWithType:]"
+ "-[DAExtensionCoordinator _extensionIdentityForType:]"
+ "-[DAExtensionCoordinator _extensionIdentityForType:]_block_invoke"
+ "-[DAExtensionCoordinator _extensionInvalidatedWithType:]"
+ "-[DAExtensionCoordinator _extensionShouldRunWithType:]"
+ "-[DAExtensionCoordinator _handleEventKeyExchange:]"
+ "-[DAExtensionCoordinator _handleEventKeyExchangeDone:]"
+ "-[DAExtensionCoordinator _handleEventKeyReply:]"
+ "-[DAExtensionCoordinator _handleEventTransportLocal:]"
+ "-[DAExtensionCoordinator _interrupted]"
+ "-[DAExtensionCoordinator _invalidate]"
+ "-[DAExtensionCoordinator _invalidated]"
+ "-[DAExtensionCoordinator _reportEvent:notifySessions:]"
+ "-[DAExtensionCoordinator _updateEnrolledFlags]"
+ "-[DAExtensionCoordinator _updateEnrolledFlags]_block_invoke"
+ "-[DAExtensionCoordinator _update]"
+ "-[DAExtensionCoordinator activate]_block_invoke"
+ "-[DAExtensionCoordinator addSession:]"
+ "-[DAExtensionCoordinator initWithDevice:bundleID:]"
+ "-[DAExtensionCoordinator removeSession:]"
+ "-[DAExtensionCoordinator reportEventToExtension:error:]_block_invoke"
+ "-[DAKeychainManager _addToKeychain:error:]"
+ "-[DAKeychainManager _fetchFromKeychain:type:error:]"
+ "-[DAKeychainManager _removeFromKeychain:error:]"
+ "@\"DAExtensionSession\""
+ "@24@0:8q16"
+ "Activate: %@"
+ "Activating %@"
+ "Added %@"
+ "B24@0:8q16"
+ "B40@0:8@16Q24^@32"
+ "BundleID '%@'"
+ "Checking service map with bundleID %@: { %@ : %@ }"
+ "Created %@"
+ "DAExtensionCoordinator"
+ "Device '%@' has authorized extension feature: %@, Level %lu"
+ "EnrolledFlags changed: %@ -> %@"
+ "ExSA"
+ "ExSD"
+ "Existing sessions for %@"
+ "Extension already running: %@"
+ "Extension is missing attributes, skipping"
+ "Extension is missing entitlement: %@"
+ "ExtensionCoordinator event: %@"
+ "ExtensionMatchingBundleID '%@' failed: %@"
+ "Extensions [ %@ ]"
+ "Fetched from keychain %@"
+ "Found %lu extensions for '%@'"
+ "Found extension attributes '%@': %@"
+ "Found extension with BundleID '%@', extensionParentID '%@'"
+ "Ignoring extension with parent BundleID mismatch: expected '%@' vs '%@'"
+ "Invalidate: %@"
+ "InvalidateReason %@"
+ "Invalidated: %@"
+ "InvalidationHandler for type %@"
+ "Mock"
+ "No authorized extension capabilities: %@"
+ "No entitlement found for type: %@"
+ "Received accessory event with nil %@ extension"
+ "Received event: %@"
+ "Removed from keychain %@"
+ "Removed session '%@' from %@"
+ "ReportEvent: %@"
+ "Searching for extension with BundleID '%@'"
+ "SendExtensionDataEvent: %@"
+ "Session needs to be activated"
+ "Sessions %lu"
+ "Skip mismatch bundleID"
+ "Skip running %@ extension for '%@': no active sessions"
+ "T@\"DADevice\",R,N,V_device"
+ "T@\"NSMutableSet\",R,C,N,V_sessionSet"
+ "T@\"NSString\",R,C,N,V_bundleID"
+ "T@?,C,N,V_invalidationHandler"
+ "TB,N,V_mockOverride"
+ "TextExtensions: %s -> %s"
+ "Update: %@"
+ "Updated %@"
+ "_activateCalled"
+ "_activateExtension:"
+ "_activatedExtensionSession"
+ "_device"
+ "_enrolledFlags"
+ "_extensionActivatedWithType:"
+ "_extensionEnsureStartedWithType:"
+ "_extensionEnsureStoppedWithType:"
+ "_extensionIdentityForType:"
+ "_extensionInvalidatedWithType:"
+ "_extensionMap"
+ "_extensionShouldRunWithType:"
+ "_extensionWithType:"
+ "_handleEvent:"
+ "_handleEventKeyExchange:"
+ "_handleEventKeyExchangeDone:"
+ "_handleEventKeyReply:"
+ "_handleEventTransportLocal:"
+ "_interrupted"
+ "_invalidateCalled"
+ "_invalidateDone"
+ "_invalidateExtensions"
+ "_invalidateReason"
+ "_invalidated"
+ "_invalidationHandler"
+ "_mockOverride"
+ "_performKeyExchange"
+ "_prefTestExtensions"
+ "_relaunchExtensions"
+ "_reportEvent:notifySessions:"
+ "_reportEventToSession:session:"
+ "_reportEventToSessions:"
+ "_reportEventType:notifySessions:"
+ "_sessionAdded"
+ "_sessionSet"
+ "_update"
+ "_updateEnrolledFlags"
+ "_xpcDAExtensionSessionActivate:"
+ "_xpcSendExtensionEvent:"
+ "accessoryEncapsulatedKey"
+ "accessoryKey"
+ "accessoryService"
+ "attributes"
+ "capabilityFlags"
+ "ciphersuite"
+ "com.apple.dautil"
+ "create reply failed"
+ "data"
+ "decryptData:withCryptoInfo:capability:error:"
+ "destination"
+ "device is not authorized for service %@"
+ "encryptData:withCryptoInfo:capability:error:"
+ "exDE"
+ "exSe"
+ "extensionType"
+ "generateKeyPairForSuite:publicKey:privateKey:error:"
+ "getExtensionPidByType:"
+ "i24@0:8q16"
+ "initWithDevice:"
+ "initWithDevice:data:capabilityFlag:"
+ "initWithDevice:eventType:extensionType:"
+ "initWithDevice:identity:type:"
+ "initWithEventType:device:cryptoInfo:"
+ "invalidationHandler"
+ "missing bundle identifier"
+ "mockOverride"
+ "no extension coordinator for %@"
+ "no extension running for %@"
+ "no service: %@"
+ "no session"
+ "reportEventToExtension:"
+ "reportEventToExtension:error:"
+ "sendExtensionDataEvent:session:error:"
+ "session decode failed"
+ "setDestination:"
+ "setEncapsulatedKey:"
+ "setExtensionType:"
+ "setInvalidationHandler:"
+ "setMockOverride:"
+ "setPrivateKey:"
+ "setPublicKey:"
+ "setVersion:"
+ "startExtensionsIfNeeded:error:"
+ "startSessionWithInfo:error:"
+ "stopExtensionsIfNeeded:reason:error:"
+ "stopSessionWithInfo:error:"
+ "testExtensions"
+ "type"
+ "updateSessionWithInfo:error:"
+ "updateWithDACryptoInfo:"
+ "v16@?0@\"DAEventExtension\"8"
+ "v24@0:8Q16"
+ "v28@0:8q16B24"
- "### Failed to add to keychain %@: %@"
- "-[DADaemonServer _handleKeyExchangeEvent:]"
- "-[DADaemonServer _startDaemonExtensionSession:error:]_block_invoke_2"
- "-[DADaemonServer startExtensionsIfNeeded:device:error:]"
- "-[DADaemonServer startExtensionsIfNeeded:device:error:]_block_invoke"
- "-[DADaemonServer stopExtensionsIfNeeded:deviceID:reason:error:]"
- "-[DADaemonServer stopExtensionsIfNeeded:deviceID:reason:error:]_block_invoke"
- "B48@0:8@16@24Q32^@40"
- "DaemonExtensionSession event: %@"
- "Device has authorized extension feature: %@"
- "Needs activate"
- "RemovedDevice found existing coordinator: %@ "
- "RemovedDevice sending event to coordinator: %@ "
- "ReportServicesChanged sending event to coordinator: %@ "
- "_handleKeyExchangeEvent:"
- "getExtensionPidByType:transport:"
- "publicKey"
- "setAccessoryKey:"
- "setDeviceFlags:"
- "startExtensionsIfNeeded:device:error:"
- "stopExtensionsIfNeeded:deviceID:reason:error:"

```
