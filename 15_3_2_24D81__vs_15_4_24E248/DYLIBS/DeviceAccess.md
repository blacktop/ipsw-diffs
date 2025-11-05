## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/Versions/A/DeviceAccess`

```diff

-313.1.0.0.0
-  __TEXT.__text: 0x25390
+314.11.0.0.0
+  __TEXT.__text: 0x26e98
   __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x1f14
-  __TEXT.__cstring: 0x49a7
-  __TEXT.__gcc_except_tab: 0x6c0
-  __TEXT.__const: 0x1ea
+  __TEXT.__objc_methlist: 0x2014
+  __TEXT.__cstring: 0x49c7
+  __TEXT.__gcc_except_tab: 0x6c8
+  __TEXT.__const: 0x22a
   __TEXT.__swift5_typeref: 0x119
   __TEXT.__oslogstring: 0x17d
   __TEXT.__swift5_capture: 0x1c

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x818
+  __TEXT.__unwind_info: 0x910
   __TEXT.__objc_classname: 0x309
-  __TEXT.__objc_methname: 0x4487
-  __TEXT.__objc_methtype: 0x719
-  __TEXT.__objc_stubs: 0x2720
+  __TEXT.__objc_methname: 0x44fc
+  __TEXT.__objc_methtype: 0x72e
+  __TEXT.__objc_stubs: 0x2740
   __DATA_CONST.__got: 0x268
   __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1050
+  __DATA_CONST.__objc_selrefs: 0x1068
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xb8
   __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0xbb8
-  __AUTH_CONST.__cfstring: 0x1a60
-  __AUTH_CONST.__objc_const: 0x3c08
+  __AUTH_CONST.__cfstring: 0x1aa0
+  __AUTH_CONST.__objc_const: 0x3ac8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x960
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x33c
+  __DATA.__objc_ivar: 0x340
   __DATA.__data: 0x7a8
   __DATA.__common: 0x8
   __DATA.__bss: 0x150

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B3752BEA-8CAD-32D3-B777-48105961243D
-  Functions: 865
-  Symbols:   2008
-  CStrings:  1878
+  UUID: B9B75414-D22A-376C-A25F-168B542C0013
+  Functions: 1051
+  Symbols:   2207
+  CStrings:  1891
 
Symbols:
+ +[DADeviceAccessAnalytics markSessionActivationForPid:atTime:].cold.1
+ +[DADeviceAccessAnalytics markSessionActivationForPid:atTime:].cold.2
+ +[DADeviceAccessAnalytics markSessionInvalidationForPid:atTime:].cold.1
+ +[DADeviceAccessAnalytics markState:deviceID:shared:discovery:flags:sourceApp:atTime:errorCode:].cold.1
+ +[DADeviceAccessAnalytics markState:deviceID:shared:discovery:flags:sourceApp:atTime:errorCode:].cold.2
+ +[DADeviceAccessAnalytics sendAnalytics:forEvent:].cold.1
+ +[DADeviceAccessAnalytics sendAnalyticsInfo:forEvent:withDeviceIdentifier:].cold.1
+ +[DASession diagnosticShow:endpoint:error:].cold.1
+ +[DASession getDevicesWithFlags:session:error:].cold.1
+ +[DASession getPartialIPsWithAppBundleID:error:].cold.1
+ +[DASession getPartialIPsWithAppBundleID:error:].cold.2
+ +[DASession getPartialIPsWithAuditToken:error:].cold.1
+ +[DASession networkingAllowedWithUUID:error:].cold.1
+ +[DASession processAllowedWithAuditToken:error:].cold.1
+ +[DASession setPartialIPsForAppBundleID:partialIPs:error:].cold.1
+ +[DASession setPartialIPsWithAuditToken:partialIPs:error:].cold.1
+ +[DASession setState:device:session:simulateApp:error:].cold.1
+ -[DAAppContext initWithCoder:].cold.1
+ -[DADevice bluetoothAppearance]
+ -[DADevice initWithCoder:].cold.1
+ -[DADevice initWithPersistentDictionaryRepresentation:error:].cold.1
+ -[DADevice initWithXPCObject:error:].cold.1
+ -[DADevice initWithXPCObject:error:].cold.2
+ -[DADevice setBluetoothAppearance:]
+ -[DADeviceAppAccessInfo initWithCoder:].cold.1
+ -[DADeviceAppAccessInfo initWithPersistentDictionaryRepresentation:error:].cold.1
+ -[DADeviceResolver _addEndpoint:].cold.1
+ -[DADeviceResolver _addEndpoint:].cold.2
+ -[DADeviceResolver _ensureInitialized].cold.1
+ -[DADeviceResolver _ensureInitialized].cold.2
+ -[DADeviceResolver _ensureInitialized].cold.3
+ -[DADeviceResolver _ensureInitialized].cold.4
+ -[DADeviceResolver _ensureInitialized].cold.5
+ -[DADeviceResolver _ensureInitialized].cold.6
+ -[DADeviceResolver _ensureInitialized].cold.7
+ -[DADeviceResolver _ensureInitialized].cold.8
+ -[DADeviceResolver _ensureInitialized].cold.9
+ -[DADeviceResolver _groupEndpoint:matchedEndpoint:].cold.1
+ -[DADeviceResolver _invalidated].cold.1
+ -[DADeviceResolver _removeEndpoint:].cold.1
+ -[DADeviceResolver _removeEndpoint:].cold.2
+ -[DADeviceResolver _removeEndpoint:].cold.3
+ -[DADeviceResolver _reportEvent:].cold.1
+ -[DADeviceResolver _selectEndpoint:].cold.1
+ -[DADeviceResolver _selectEndpoint:].cold.2
+ -[DADeviceResolver _selectEndpoint:].cold.3
+ -[DADeviceResolver _selectEndpoint:].cold.4
+ -[DADeviceResolver _selectEndpoint:].cold.5
+ -[DADeviceResolver _startResolvingBonjourFullName:interfaceIndex:endpoint:].cold.1
+ -[DADeviceResolver _startResolvingBonjourFullName:interfaceIndex:endpoint:].cold.2
+ -[DADeviceResolver _startResolvingBonjourName:type:interfaceIndex:endpoint:].cold.1
+ -[DADeviceResolver _startResolvingEndpoint:].cold.1
+ -[DADeviceResolver _startResolvingHostname:interfaceIndex:endpoint:].cold.1
+ -[DADeviceResolver _startResolvingHostname:interfaceIndex:endpoint:].cold.2
+ -[DADeviceSettings initWithXPCObject:error:].cold.1
+ -[DADeviceStateRecord discoveryTimeIntervelBetweenState:].cold.1
+ -[DADeviceStateRecord stateTransitionAsString:].cold.1
+ -[DADeviceStateRecord timeIntervelBetweenState:].cold.1
+ -[DADiscovery _activateDirect].cold.1
+ -[DADiscovery _activateDirect].cold.2
+ -[DADiscovery _activateDirect].cold.3
+ -[DADiscovery _activateXPCStart:].cold.1
+ -[DADiscovery _interrupted].cold.1
+ -[DADiscovery _invalidated].cold.1
+ -[DADiscovery _reportEvent:].cold.1
+ -[DADiscovery _startExtensions:bundleID:entitlement:completion:].cold.1
+ -[DADiscovery _updateNEPolicy:remove:].cold.1
+ -[DADiscovery _updateNEPolicy:remove:].cold.10
+ -[DADiscovery _updateNEPolicy:remove:].cold.11
+ -[DADiscovery _updateNEPolicy:remove:].cold.12
+ -[DADiscovery _updateNEPolicy:remove:].cold.13
+ -[DADiscovery _updateNEPolicy:remove:].cold.14
+ -[DADiscovery _updateNEPolicy:remove:].cold.15
+ -[DADiscovery _updateNEPolicy:remove:].cold.16
+ -[DADiscovery _updateNEPolicy:remove:].cold.17
+ -[DADiscovery _updateNEPolicy:remove:].cold.2
+ -[DADiscovery _updateNEPolicy:remove:].cold.3
+ -[DADiscovery _updateNEPolicy:remove:].cold.4
+ -[DADiscovery _updateNEPolicy:remove:].cold.5
+ -[DADiscovery _updateNEPolicy:remove:].cold.6
+ -[DADiscovery _updateNEPolicy:remove:].cold.7
+ -[DADiscovery _updateNEPolicy:remove:].cold.8
+ -[DADiscovery _updateNEPolicy:remove:].cold.9
+ -[DADiscovery _xpcReceivedDAEvent:].cold.1
+ -[DADiscovery _xpcReceivedDAEvent:].cold.2
+ -[DADiscovery _xpcReceivedDAEvent:].cold.3
+ -[DADiscovery _xpcReceivedDAEvent:].cold.4
+ -[DADiscovery _xpcReceivedDeviceEvent:].cold.1
+ -[DADiscovery _xpcReceivedMessage:].cold.1
+ -[DADiscovery finishMigration].cold.1
+ -[DADiscovery initWithConfiguration:error:].cold.1
+ -[DADiscovery initWithConfigurations:error:].cold.1
+ -[DADiscovery xpcReceivedMessage:].cold.1
+ -[DADiscovery xpcReceivedMessage:].cold.2
+ -[DADiscovery xpcReceivedMessage:].cold.3
+ -[DADiscoveryConfiguration initWithCoder:].cold.1
+ -[DADiscoveryExtension _activate].cold.1
+ -[DADiscoveryExtension _activate].cold.2
+ -[DADiscoveryExtension _activate].cold.3
+ -[DADiscoveryExtension _activate].cold.4
+ -[DADiscoveryExtension _interrupted].cold.1
+ -[DADiscoveryExtension _invalidate].cold.1
+ -[DADiscoveryExtension _invalidated].cold.1
+ -[DAEndpoint initWithPersistentDictionaryRepresentation:error:].cold.1
+ -[DAEvent initWithCoder:].cold.1
+ -[DAEventDevice initWithCoder:].cold.1
+ -[DAEventDevices initWithCoder:].cold.1
+ -[DASession _activateStart:].cold.1
+ -[DASession _interrupted].cold.1
+ -[DASession _invalidated].cold.1
+ -[DASession _reportEvent:].cold.1
+ -[DASession _xpcListenerEvent:].cold.1
+ -[DASession _xpcListenerEvent:].cold.2
+ -[DASession _xpcReceivedDAEvent:].cold.1
+ -[DASession _xpcReceivedDAEvent:].cold.2
+ -[DASession _xpcReceivedMessage:].cold.1
+ -[DASession appContext].cold.1
+ -[DASession appIsUsingDeviceAccess].cold.1
+ -[DASession getPartialIPsWithAuditToken:completionHandler:].cold.1
+ -[DASession setPartialIPsWithAuditToken:partialIPs:completionHandler:].cold.1
+ -[DASession xpcReceivedMessage:].cold.1
+ -[DASession xpcReceivedMessage:].cold.2
+ -[DASession xpcReceivedMessage:].cold.3
+ -[DASimulatedDeviceClient _invalidated].cold.1
+ -[DASimulatedDeviceDiscovery _bluetoothEnsureStarted].cold.1
+ -[DASimulatedDeviceDiscovery _bluetoothEnsureStopped].cold.1
+ -[DASimulatedDeviceDiscovery _bonjourEnsureStarted].cold.1
+ -[DASimulatedDeviceDiscovery _bonjourEnsureStopped].cold.1
+ -[DASimulatedDeviceDiscovery _invalidated].cold.1
+ -[DASimulatedDeviceServer _activate].cold.1
+ -[DASimulatedDeviceServer _invalidated].cold.1
+ -[DAUserAlert _autoInvalidate].cold.1
+ -[DAUserAlert _invalidated].cold.1
+ -[DAUserAlert dealloc].cold.1
+ OBJC_IVAR_$_DADevice._bluetoothAppearance
+ _CFDictionaryGetInt64Ranged
+ _NSDecodeSInt64RangedIfPresent
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ __23-[DADiscovery activate]_block_invoke.cold.1
+ __23-[DASession invalidate]_block_invoke.cold.1
+ __25-[DADiscovery invalidate]_block_invoke.cold.1
+ __25-[DAUserAlert invalidate]_block_invoke.cold.1
+ __29-[DADiscovery migrateDevices]_block_invoke.cold.1
+ __30-[DADeviceResolver invalidate]_block_invoke.cold.1
+ __30-[DADiscovery finishMigration]_block_invoke.cold.1
+ __33-[DADevice descriptionWithLevel:]_block_invoke.283
+ __33-[DADiscoveryExtension _activate]_block_invoke.643.cold.1
+ __33-[DADiscoveryExtension _activate]_block_invoke_3.cold.1
+ __35-[DASimulatedDeviceClient activate]_block_invoke.cold.1
+ __35-[DASimulatedDeviceServer activate]_block_invoke.cold.1
+ __36-[DADiscovery invalidateWithReason:]_block_invoke.cold.1
+ __36-[DADiscovery invalidateWithReason:]_block_invoke_2.cold.1
+ __37-[DASimulatedDeviceClient invalidate]_block_invoke.cold.1
+ __37-[DASimulatedDeviceServer invalidate]_block_invoke.cold.1
+ __38-[DASimulatedDeviceDiscovery activate]_block_invoke.cold.1
+ __40-[DASimulatedDeviceDiscovery invalidate]_block_invoke.cold.1
+ __45-[DAUserAlert activateWithCompletionHandler:]_block_invoke.cold.1
+ __45-[DAUserAlert activateWithCompletionHandler:]_block_invoke.cold.2
+ __46-[DASession diagnosticShow:completionHandler:]_block_invoke.cold.1
+ __46-[DASession diagnosticShow:completionHandler:]_block_invoke_2.cold.1
+ __47-[DADiscoveryExtension reportEventToExtension:]_block_invoke.cold.1
+ __47-[DAUserAlert _responseCallback:responseFlags:]_block_invoke.cold.1
+ __50-[DASession removeDeviceAccess:completionHandler:]_block_invoke_2.cold.1
+ __53-[DASimulatedDeviceDiscovery _bluetoothEnsureStarted]_block_invoke_2.cold.1
+ __57-[DASession getBluetoothAccessInfoWithCompletionHandler:]_block_invoke.cold.1
+ __59-[DASession setState:device:simulateApp:completionHandler:]_block_invoke.cold.1
+ __59-[DASession setState:device:simulateApp:completionHandler:]_block_invoke_2.cold.1
+ __61-[DADiscovery setState:device:simulateApp:completionHandler:]_block_invoke.cold.1
+ __61-[DADiscovery setState:device:simulateApp:completionHandler:]_block_invoke_2.cold.1
+ __61-[DASession setDeviceAppAccessInfo:device:completionHandler:]_block_invoke.cold.1
+ __61-[DASession setDeviceAppAccessInfo:device:completionHandler:]_block_invoke_2.cold.1
+ __63-[DADiscovery setDeviceAppAccessInfo:device:completionHandler:]_block_invoke.cold.1
+ __63-[DADiscovery setDeviceAppAccessInfo:device:completionHandler:]_block_invoke_2.cold.1
+ __66-[DADiscovery respondToBluetoothPairingRequest:completionHandler:]_block_invoke.cold.1
+ __66-[DADiscovery respondToBluetoothPairingRequest:completionHandler:]_block_invoke_2.cold.1
+ __67-[DADiscovery _findExtensionPoint:bundleID:entitlement:completion:]_block_invoke_2.cold.1
+ __70-[DASession setPartialIPsForAppBundleID:partialIPs:completionHandler:]_block_invoke_2.cold.1
+ __96+[DADeviceAccessAnalytics markState:deviceID:shared:discovery:flags:sourceApp:atTime:errorCode:]_block_invoke_2.cold.1
+ __DAXPCDecodeNSArrayOfCBUUID_block_invoke.cold.1
+ _objc_msgSend$numberWithUnsignedShort:
+ initCBDiscovery.cold.1
- __33-[DADevice descriptionWithLevel:]_block_invoke.275
- _swift_arrayDestroy
CStrings:
+ "S"
+ "S16@0:8"
+ "TS,N,V_bluetoothAppearance"
+ "_bluetoothAppearance"
+ "bluetoothAppearance"
+ "btAp"
+ "btAp %hu"
+ "btNC %lu"
+ "numberWithUnsignedShort:"
+ "setBluetoothAppearance:"
+ "v20@0:8S16"
- "btNC %ld"

```
