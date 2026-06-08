## tvremoted

> `/usr/libexec/tvremoted`

```diff

-548.50.8.0.0
-  __TEXT.__text: 0x11280
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_stubs: 0x2540
-  __TEXT.__objc_methlist: 0xef0
-  __TEXT.__const: 0xd2
-  __TEXT.__oslogstring: 0x23da
-  __TEXT.__cstring: 0x842
-  __TEXT.__gcc_except_tab: 0x1c8
-  __TEXT.__objc_methname: 0x316a
-  __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methtype: 0xe81
-  __TEXT.__unwind_info: 0x410
-  __DATA_CONST.__auth_got: 0x270
-  __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x660
-  __DATA_CONST.__cfstring: 0x6e0
+625.0.0.0.0
+  __TEXT.__text: 0x11174
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_stubs: 0x2620
+  __TEXT.__objc_methlist: 0xf44
+  __TEXT.__const: 0xca
+  __TEXT.__gcc_except_tab: 0x1a4
+  __TEXT.__cstring: 0xb53
+  __TEXT.__objc_methname: 0x32b1
+  __TEXT.__oslogstring: 0x26cc
+  __TEXT.__objc_classname: 0x13d
+  __TEXT.__objc_methtype: 0xfa2
+  __TEXT.__unwind_info: 0x340
+  __DATA_CONST.__const: 0x6b0
+  __DATA_CONST.__cfstring: 0x900
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0xe48
-  __DATA.__objc_selrefs: 0xc80
+  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__got: 0x218
+  __DATA.__objc_const: 0xe60
+  __DATA.__objc_selrefs: 0xcc8
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D62F8F92-7199-39E1-ACE0-825E63A03DDF
-  Functions: 319
-  Symbols:   2393
-  CStrings:  951
+  UUID: 218816E6-3AF8-34E1-9FC9-DFFACCC051EA
+  Functions: 333
+  Symbols:   164
+  CStrings:  1016
 
Symbols:
+ _NSLocalizedFailureReasonErrorKey
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ __os_feature_enabled_impl
+ __xpc_type_data
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _xpc_data_get_bytes_ptr
+ _xpc_data_get_length
+ radr://5614542
- 
- +[TVRDAssertionManager sharedInstance]
- +[TVRDAssertionManager sharedInstance].cold.1
- +[TVRDLaunchEventHandlers sharedInstance]
- +[TVRDLaunchEventHandlers sharedInstance].cold.1
- -[TVRDAssertionManager .cxx_destruct]
- -[TVRDAssertionManager _createAssertionExpirationTimer]
- -[TVRDAssertionManager _newLockScreenBehaviour]
- -[TVRDAssertionManager _setup]
- -[TVRDAssertionManager acquireLockScreenAssertion]
- -[TVRDAssertionManager assertion]
- -[TVRDAssertionManager dealloc]
- -[TVRDAssertionManager expirationTimer]
- -[TVRDAssertionManager init]
- -[TVRDAssertionManager invalidateAssertionExpirationTimer]
- -[TVRDAssertionManager isLockScreenAssertionActive]
- -[TVRDAssertionManager releaseLockScreenAssertion]
- -[TVRDAssertionManager setAssertion:]
- -[TVRDAssertionManager setExpirationTimer:]
- -[TVRDAssertionManager setSystemMonitor:]
- -[TVRDAssertionManager startAssertionExpirationTimer]
- -[TVRDAssertionManager systemMonitor]
- -[TVRDClientProcessConnection .cxx_destruct]
- -[TVRDClientProcessConnection _invalidateRemoteAlertHandle]
- -[TVRDClientProcessConnection _processNameForPid:]
- -[TVRDClientProcessConnection _removeAllIdentifiers]
- -[TVRDClientProcessConnection _removeIdentifier:]
- -[TVRDClientProcessConnection addItemForDeviceWithIdentifier:mediaIdentifier:completion:]
- -[TVRDClientProcessConnection alertHandle]
- -[TVRDClientProcessConnection beginDeviceQueryWithResponse:]
- -[TVRDClientProcessConnection cancelAuthChallengeForDeviceWithIdentifier:]
- -[TVRDClientProcessConnection closeConnectionToDeviceWithIdentifier:withType:]
- -[TVRDClientProcessConnection dealloc]
- -[TVRDClientProcessConnection delegate]
- -[TVRDClientProcessConnection description]
- -[TVRDClientProcessConnection deviceIdentifiers]
- -[TVRDClientProcessConnection enableFindingSession:forDeviceIdentifier:]
- -[TVRDClientProcessConnection enableTVRemoteOnLockscreen:forDeviceIdentifier:]
- -[TVRDClientProcessConnection endDeviceQuery]
- -[TVRDClientProcessConnection fetchActiveMREndpointUIDWithCompletion:]
- -[TVRDClientProcessConnection fetchLaunchableAppsForDeviceWithIdentifier:completion:]
- -[TVRDClientProcessConnection fetchUpNextInfoForDeviceWithIdentifier:paginationToken:completion:]
- -[TVRDClientProcessConnection fulfillAuthChallengeForDeviceWithIdentifier:withLocallyEnteredCode:]
- -[TVRDClientProcessConnection getConnectionStatusToDeviceWithIdentifier:response:]
- -[TVRDClientProcessConnection getSuggestedDevicesWithResponse:]
- -[TVRDClientProcessConnection initWithXPCConnection:delegate:]
- -[TVRDClientProcessConnection launchAppForDeviceWithIdentifier:bundleID:completion:]
- -[TVRDClientProcessConnection launchViewServiceForDeviceWithIdentifier:]
- -[TVRDClientProcessConnection markAsWatchedForDeviceWithIdentifier:mediaIdentifier:completion:]
- -[TVRDClientProcessConnection mutableIdentifiers]
- -[TVRDClientProcessConnection openConnectionToDeviceWithIdentifier:connectionContext:]
- -[TVRDClientProcessConnection playItem:deviceIdentifier:completion:]
- -[TVRDClientProcessConnection remoteAlertHandle:didInvalidateWithError:]
- -[TVRDClientProcessConnection remoteAlertHandle:didInvalidateWithError:].cold.1
- -[TVRDClientProcessConnection remoteAlertHandleDidDeactivate:]
- -[TVRDClientProcessConnection remoteObjectProxy]
- -[TVRDClientProcessConnection removeInterestForDeviceWithIdentifier:]
- -[TVRDClientProcessConnection removeItemForDeviceWithIdentifier:mediaIdentifier:completion:]
- -[TVRDClientProcessConnection sendButtonEvent:toDeviceWithIdentifier:]
- -[TVRDClientProcessConnection sendEvent:toDeviceWithIdentifier:options:response:]
- -[TVRDClientProcessConnection sendGameControllerEvent:toDeviceWithIdentifier:]
- -[TVRDClientProcessConnection sendInputReturnKeyToDeviceWithIdentifier:]
- -[TVRDClientProcessConnection sendInputText:toDeviceWithIdentifier:]
- -[TVRDClientProcessConnection sendInputTextPayload:toDeviceWithIdentifier:]
- -[TVRDClientProcessConnection sendTouchEvent:toDeviceWithIdentifier:]
- -[TVRDClientProcessConnection setAlertHandle:]
- -[TVRDClientProcessConnection setDelegate:]
- -[TVRDClientProcessConnection setMutableIdentifiers:]
- -[TVRDClientProcessConnection setXpcConnection:]
- -[TVRDClientProcessConnection updateDeviceIdentifier:to:]
- -[TVRDClientProcessConnection xpcConnection]
- -[TVRDIRSessionManager .cxx_destruct]
- -[TVRDIRSessionManager _activateWithCompletion:]
- -[TVRDIRSessionManager _candidateForDevice:createIfNeeded:]
- -[TVRDIRSessionManager _deviceClassificationFromIRClassification:]
- -[TVRDIRSessionManager _donateEventWithEventType:forDevice:]
- -[TVRDIRSessionManager _fetchServiceTokenWithCompletionHandler:]
- -[TVRDIRSessionManager _fetchServiceTokenWithCompletionHandler:].cold.1
- -[TVRDIRSessionManager _invalidate]
- -[TVRDIRSessionManager _restartIRSession]
- -[TVRDIRSessionManager _setupSession]
- -[TVRDIRSessionManager activateWithCompletion:]
- -[TVRDIRSessionManager didInteractWithDevice:]
- -[TVRDIRSessionManager filteredDeviceListHandler]
- -[TVRDIRSessionManager hasStarted]
- -[TVRDIRSessionManager identifierToCandidateMap]
- -[TVRDIRSessionManager identifierToDeviceMap]
- -[TVRDIRSessionManager init]
- -[TVRDIRSessionManager invalidate]
- -[TVRDIRSessionManager irSession]
- -[TVRDIRSessionManager pause]
- -[TVRDIRSessionManager processNewDevices:]
- -[TVRDIRSessionManager processNewDevices:].cold.1
- -[TVRDIRSessionManager processNewDevices:].cold.2
- -[TVRDIRSessionManager processNewDevices:].cold.3
- -[TVRDIRSessionManager processNewDevices:].cold.4
- -[TVRDIRSessionManager processNewDevices:].cold.5
- -[TVRDIRSessionManager query]
- -[TVRDIRSessionManager removeDevice:]
- -[TVRDIRSessionManager removeDevice:].cold.1
- -[TVRDIRSessionManager requestCurrentRecommendedDevices]
- -[TVRDIRSessionManager serviceToken]
- -[TVRDIRSessionManager session:didFailWithError:]
- -[TVRDIRSessionManager session:didFailWithError:].cold.1
- -[TVRDIRSessionManager session:didUpdateContext:]
- -[TVRDIRSessionManager setFilteredDeviceListHandler:]
- -[TVRDIRSessionManager setHasStarted:]
- -[TVRDIRSessionManager setIdentifierToCandidateMap:]
- -[TVRDIRSessionManager setIdentifierToDeviceMap:]
- -[TVRDIRSessionManager setIrSession:]
- -[TVRDIRSessionManager setQuery:]
- -[TVRDIRSessionManager setServiceToken:]
- -[TVRDIRSessionManager setSuggestedDevices:]
- -[TVRDIRSessionManager suggestedDevices]
- -[TVRDIRSessionManager updateDevice:withConnectionContext:]
- -[TVRDLaunchEventHandlers _enableTVRemoteControlCenterModule]
- -[TVRDLaunchEventHandlers _setupDistnotedHandlers]
- -[TVRDLaunchEventHandlers _setupNotificationHandlers]
- -[TVRDLaunchEventHandlers _setupNotifydHandlers]
- -[TVRDLaunchEventHandlers requestedModuleEnablement]
- -[TVRDLaunchEventHandlers setRequestedModuleEnablement:]
- -[TVRDLaunchEventHandlers setupHandlers]
- -[TVRDServer .cxx_destruct]
- -[TVRDServer _activateIRSessionManager]
- -[TVRDServer _becameInterestedInDeviceWithIdentifier:]
- -[TVRDServer _cachedDeviceForIdentifier:]
- -[TVRDServer _connectToDeviceIfNeeded:]
- -[TVRDServer _deviceForIdentifierInDeviceQuery:]
- -[TVRDServer _deviceForKeyboardController:]
- -[TVRDServer _findCachedDeviceForIdentifier:]
- -[TVRDServer _hasNowPlayingControlsForButtons:]
- -[TVRDServer _informClientCouldNotLocateDeviceWithIdentifier:]
- -[TVRDServer _interestedClientProcessConnectionsForDevice:]
- -[TVRDServer _interestedClientProcessConnectionsForDevice:].cold.1
- -[TVRDServer _invalidateIRSessionManager]
- -[TVRDServer _isButtonOfNowPlayingType:]
- -[TVRDServer _lostInterestInDeviceWithIdentifier:]
- -[TVRDServer _publishUserPresenceForDevice:]
- -[TVRDServer _startGeneralDeviceQuery]
- -[TVRDServer _stopGeneralDeviceQuery]
- -[TVRDServer _switchToCurrentUserProfileForDevice:]
- -[TVRDServer _updateClientConnectionsForDevice:oldIdentifier:]
- -[TVRDServer _updateDevicesWithRecommendations:]
- -[TVRDServer _updateDevicesWithRecommendations:].cold.1
- -[TVRDServer _updateDevicesWithRecommendations:].cold.2
- -[TVRDServer _updateDevicesWithRecommendations:].cold.3
- -[TVRDServer authChallengesByID]
- -[TVRDServer cachedDevices]
- -[TVRDServer clientConnection:addItemForDeviceWithIdentifier:mediaIdentifier:completion:]
- -[TVRDServer clientConnection:addedInterestedDeviceIdentifier:connectionContext:]
- -[TVRDServer clientConnection:cancelledAuthChallengeForDeviceIdentifier:]
- -[TVRDServer clientConnection:fetchLaunchableAppsForDeviceWithIdentifier:completion:]
- -[TVRDServer clientConnection:fetchUpNextInfoForDeviceWithIdentifier:paginationToken:completion:]
- -[TVRDServer clientConnection:isConnectedToDeviceWithIdentifier:]
- -[TVRDServer clientConnection:launchAppForDeviceWithIdentifier:bundleID:completion:]
- -[TVRDServer clientConnection:markAsWatchedForDeviceWithIdentifier:mediaIdentifier:completion:]
- -[TVRDServer clientConnection:playItem:deviceIdentifier:completion:]
- -[TVRDServer clientConnection:receivedAuthChallengeLocallyEnteredCode:forDeviceIdentifier:]
- -[TVRDServer clientConnection:reiteratedInterestInDeviceIdentifier:connectionContext:]
- -[TVRDServer clientConnection:removeItemForDeviceWithIdentifier:mediaIdentifier:completion:]
- -[TVRDServer clientConnection:removedInterestedDeviceIdentifier:]
- -[TVRDServer clientConnection:requestsEnablingFindingSession:forDeviceWithIdentifier:]
- -[TVRDServer clientConnection:requestsEnablingRemoteOnLockscreen:forDeviceWithIdentifier:]
- -[TVRDServer clientConnection:requestsSendingButtonEvent:toDeviceIdentifier:]
- -[TVRDServer clientConnection:requestsSendingEvent:toDeviceWithIdentifier:options:response:]
- -[TVRDServer clientConnection:requestsSendingGameControllerEvent:toDeviceIdentifier:]
- -[TVRDServer clientConnection:requestsSendingInputDataPayload:toDeviceIdentifier:]
- -[TVRDServer clientConnection:requestsSendingInputReturnKeyToDeviceIdentifier:]
- -[TVRDServer clientConnection:requestsSendingInputText:toDeviceIdentifier:]
- -[TVRDServer clientConnection:requestsSendingTouchEvent:toDeviceIdentifier:]
- -[TVRDServer clientConnection:requestsSuggestedDeviceWithResponse:]
- -[TVRDServer clientConnectionRequestsEndingDeviceQuery:]
- -[TVRDServer clientConnectionRequestsStartingDeviceQuery:withResponse:]
- -[TVRDServer clientConnectionSeveredConnection:]
- -[TVRDServer clientConnections]
- -[TVRDServer connectionContextByID]
- -[TVRDServer countedSetDescriptionFor:]
- -[TVRDServer dealloc]
- -[TVRDServer device:didUpdateNameFrom:]
- -[TVRDServer device:didUpdateNameFrom:].cold.1
- -[TVRDServer device:disconnectedForReason:error:]
- -[TVRDServer device:encounteredAuthenticationChallenge:]
- -[TVRDServer device:supportsFindMyRemote:]
- -[TVRDServer device:updatedAttentionState:]
- -[TVRDServer device:updatedNowPlayingInfo:]
- -[TVRDServer device:updatedPairedRemoteInfo:]
- -[TVRDServer device:updatedSiriRemoteFindingState:]
- -[TVRDServer device:updatedSupportedButtons:]
- -[TVRDServer deviceBeganConnecting:]
- -[TVRDServer deviceConnected:]
- -[TVRDServer deviceIdentifiers]
- -[TVRDServer devicePoweredOff:]
- -[TVRDServer deviceQueryDidUpdateDevices:]
- -[TVRDServer deviceQueryObservers]
- -[TVRDServer deviceSearch]
- -[TVRDServer deviceShouldAllowConnectionAuthentication:]
- -[TVRDServer generalDeviceQuery]
- -[TVRDServer identifiersRequestingConnection]
- -[TVRDServer init]
- -[TVRDServer irSessionManager]
- -[TVRDServer isScreenLocked]
- -[TVRDServer keyboardController:beganTextEditingWithAttributes:]
- -[TVRDServer keyboardController:didUpdateAttributes:]
- -[TVRDServer keyboardController:didUpdateText:]
- -[TVRDServer keyboardControllerEndedTextEditing:]
- -[TVRDServer lastConnectedDevice]
- -[TVRDServer lastConnectionTimestamp]
- -[TVRDServer listener:shouldAcceptNewConnection:]
- -[TVRDServer setAuthChallengesByID:]
- -[TVRDServer setCachedDevices:]
- -[TVRDServer setClientConnections:]
- -[TVRDServer setConnectionContextByID:]
- -[TVRDServer setDeviceIdentifiers:]
- -[TVRDServer setDeviceQueryObservers:]
- -[TVRDServer setDeviceSearch:]
- -[TVRDServer setGeneralDeviceQuery:]
- -[TVRDServer setIdentifiersRequestingConnection:]
- -[TVRDServer setIrSessionManager:]
- -[TVRDServer setIsScreenLocked:]
- -[TVRDServer setLastConnectedDevice:]
- -[TVRDServer setLastConnectionTimestamp:]
- -[TVRDServer setSystemMonitor:]
- -[TVRDServer systemMonitor]
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Binaries/TVRemoteServices/install/TempContent/Objects/TVRemoteServices.build/tvremoted.build/DerivedSources/
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Binaries/TVRemoteServices/install/TempContent/Objects/TVRemoteServices.build/tvremoted.build/Objects-normal/arm64e/Logger.o
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Binaries/TVRemoteServices/install/TempContent/Objects/TVRemoteServices.build/tvremoted.build/Objects-normal/arm64e/TVRDAssertionManager.o
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Binaries/TVRemoteServices/install/TempContent/Objects/TVRemoteServices.build/tvremoted.build/Objects-normal/arm64e/TVRDClientProcessConnection.o
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Binaries/TVRemoteServices/install/TempContent/Objects/TVRemoteServices.build/tvremoted.build/Objects-normal/arm64e/TVRDIRSessionManager.o
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Binaries/TVRemoteServices/install/TempContent/Objects/TVRemoteServices.build/tvremoted.build/Objects-normal/arm64e/TVRDLaunchEventHandlers.o
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Binaries/TVRemoteServices/install/TempContent/Objects/TVRemoteServices.build/tvremoted.build/Objects-normal/arm64e/TVRDLogging.o
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Binaries/TVRemoteServices/install/TempContent/Objects/TVRemoteServices.build/tvremoted.build/Objects-normal/arm64e/TVRDServer.o
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Binaries/TVRemoteServices/install/TempContent/Objects/TVRemoteServices.build/tvremoted.build/Objects-normal/arm64e/tvremoted.o
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Binaries/TVRemoteServices/install/TempContent/Objects/TVRemoteServices.build/tvremoted.build/Objects-normal/arm64e/tvremoted.swiftmodule
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Binaries/TVRemoteServices/install/TempContent/Objects/TVRemoteServices.build/tvremoted.build/Objects-normal/arm64e/tvremoted_vers.o
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Sources/TVRemoteServices/tvremoted/
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Sources/TVRemoteServices/tvremoted/iOS/
- /Library/Caches/com.apple.xbs/CEC54F3A-ADD6-41B1-A96A-7A23F45AEAD1/TemporaryDirectory.LrKrKr/Sources/TVRemoteServices/tvremoted/tvOS/
- GCC_except_table0
- GCC_except_table14
- GCC_except_table16
- GCC_except_table20
- GCC_except_table3
- GCC_except_table4
- GCC_except_table6
- GCC_except_table80
- GCC_except_table95
- Logger.swift
- OBJC_IVAR_$_TVRDAssertionManager._assertion
- OBJC_IVAR_$_TVRDAssertionManager._expirationTimer
- OBJC_IVAR_$_TVRDAssertionManager._systemMonitor
- OBJC_IVAR_$_TVRDClientProcessConnection._alertHandle
- OBJC_IVAR_$_TVRDClientProcessConnection._delegate
- OBJC_IVAR_$_TVRDClientProcessConnection._mutableIdentifiers
- OBJC_IVAR_$_TVRDClientProcessConnection._remoteObjectProxy
- OBJC_IVAR_$_TVRDClientProcessConnection._xpcConnection
- OBJC_IVAR_$_TVRDIRSessionManager._filteredDeviceListHandler
- OBJC_IVAR_$_TVRDIRSessionManager._hasStarted
- OBJC_IVAR_$_TVRDIRSessionManager._identifierToCandidateMap
- OBJC_IVAR_$_TVRDIRSessionManager._identifierToDeviceMap
- OBJC_IVAR_$_TVRDIRSessionManager._irSession
- OBJC_IVAR_$_TVRDIRSessionManager._query
- OBJC_IVAR_$_TVRDIRSessionManager._serviceToken
- OBJC_IVAR_$_TVRDIRSessionManager._suggestedDevices
- OBJC_IVAR_$_TVRDLaunchEventHandlers._requestedModuleEnablement
- OBJC_IVAR_$_TVRDServer._authChallengesByID
- OBJC_IVAR_$_TVRDServer._cachedDevices
- OBJC_IVAR_$_TVRDServer._clientConnections
- OBJC_IVAR_$_TVRDServer._connectionContextByID
- OBJC_IVAR_$_TVRDServer._deviceIdentifiers
- OBJC_IVAR_$_TVRDServer._deviceQueryObservers
- OBJC_IVAR_$_TVRDServer._deviceSearch
- OBJC_IVAR_$_TVRDServer._generalDeviceQuery
- OBJC_IVAR_$_TVRDServer._identifiersRequestingConnection
- OBJC_IVAR_$_TVRDServer._irSessionManager
- OBJC_IVAR_$_TVRDServer._isScreenLocked
- OBJC_IVAR_$_TVRDServer._lastConnectedDevice
- OBJC_IVAR_$_TVRDServer._lastConnectionTimestamp
- OBJC_IVAR_$_TVRDServer._systemMonitor
- TVRDAssertionManager.m
- TVRDClientProcessConnection.m
- TVRDIRSessionManager.m
- TVRDLaunchEventHandlers.m
- TVRDLogging.m
- TVRDServer.m
- _OBJC_CLASS_$_TVRDAssertionManager
- _OBJC_CLASS_$_TVRDClientProcessConnection
- _OBJC_CLASS_$_TVRDIRSessionManager
- _OBJC_CLASS_$_TVRDLaunchEventHandlers
- _OBJC_CLASS_$_TVRDServer
- _OBJC_METACLASS_$_TVRDAssertionManager
- _OBJC_METACLASS_$_TVRDClientProcessConnection
- _OBJC_METACLASS_$_TVRDIRSessionManager
- _OBJC_METACLASS_$_TVRDLaunchEventHandlers
- _OBJC_METACLASS_$_TVRDServer
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- _TVRDIRLog.cold.1
- _TVRDIRLog.log
- _TVRDIRLog.onceToken
- _TVRDXPCLog.cold.1
- _TVRDXPCLog.log
- _TVRDXPCLog.onceToken
- __18-[TVRDServer init]_block_invoke.13
- __18-[TVRDServer init]_block_invoke.14
- __18-[TVRDServer init]_block_invoke.16
- __29-[TVRDIRSessionManager pause]_block_invoke.cold.1
- __30-[TVRDAssertionManager _setup]_block_invoke.10
- __30-[TVRDAssertionManager _setup]_block_invoke.6
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.93
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.93.cold.1
- __41-[TVRDIRSessionManager _restartIRSession]_block_invoke.cold.1
- __44-[TVRDServer _publishUserPresenceForDevice:]_block_invoke.cold.1
- __48-[TVRDIRSessionManager _activateWithCompletion:]_block_invoke.18
- __49-[TVRDIRSessionManager session:didUpdateContext:]_block_invoke.27
- __49-[TVRDIRSessionManager session:didUpdateContext:]_block_invoke.cold.1
- __50-[TVRDAssertionManager acquireLockScreenAssertion]_block_invoke.37
- __50-[TVRDAssertionManager acquireLockScreenAssertion]_block_invoke.37.cold.1
- __50-[TVRDAssertionManager acquireLockScreenAssertion]_block_invoke.cold.1
- __50-[TVRDLaunchEventHandlers _setupDistnotedHandlers]_block_invoke.cold.1
- __51-[TVRDServer _switchToCurrentUserProfileForDevice:]_block_invoke.cold.1
- __54-[TVRDServer _becameInterestedInDeviceWithIdentifier:]_block_invoke.cold.1
- __61-[TVRDLaunchEventHandlers _enableTVRemoteControlCenterModule]_block_invoke.57
- __61-[TVRDLaunchEventHandlers _enableTVRemoteControlCenterModule]_block_invoke.57.cold.1
- __62-[TVRDClientProcessConnection initWithXPCConnection:delegate:]_block_invoke.2
- __62-[TVRDClientProcessConnection initWithXPCConnection:delegate:]_block_invoke.3
- __62-[TVRDClientProcessConnection initWithXPCConnection:delegate:]_block_invoke.3.cold.1
- __64-[TVRDIRSessionManager _fetchServiceTokenWithCompletionHandler:]_block_invoke_2.cold.1
- __64-[TVRDIRSessionManager _fetchServiceTokenWithCompletionHandler:]_block_invoke_2.cold.2
- __76-[TVRDServer clientConnection:requestsSendingTouchEvent:toDeviceIdentifier:]_block_invoke.cold.1
- __77-[TVRDServer clientConnection:requestsSendingButtonEvent:toDeviceIdentifier:]_block_invoke.cold.1
- __81-[TVRDServer clientConnection:addedInterestedDeviceIdentifier:connectionContext:]_block_invoke.cold.1
- __86-[TVRDServer clientConnection:requestsEnablingFindingSession:forDeviceWithIdentifier:]_block_invoke.cold.1
- __OBJC_$_CLASS_METHODS_TVRDAssertionManager
- __OBJC_$_CLASS_METHODS_TVRDLaunchEventHandlers
- __OBJC_$_INSTANCE_METHODS_TVRDAssertionManager
- __OBJC_$_INSTANCE_METHODS_TVRDClientProcessConnection
- __OBJC_$_INSTANCE_METHODS_TVRDIRSessionManager
- __OBJC_$_INSTANCE_METHODS_TVRDLaunchEventHandlers
- __OBJC_$_INSTANCE_METHODS_TVRDServer
- __OBJC_$_INSTANCE_VARIABLES_TVRDAssertionManager
- __OBJC_$_INSTANCE_VARIABLES_TVRDClientProcessConnection
- __OBJC_$_INSTANCE_VARIABLES_TVRDIRSessionManager
- __OBJC_$_INSTANCE_VARIABLES_TVRDLaunchEventHandlers
- __OBJC_$_INSTANCE_VARIABLES_TVRDServer
- __OBJC_$_PROP_LIST_NSObject
- __OBJC_$_PROP_LIST_TVRDAssertionManager
- __OBJC_$_PROP_LIST_TVRDClientProcessConnection
- __OBJC_$_PROP_LIST_TVRDIRSessionManager
- __OBJC_$_PROP_LIST_TVRDLaunchEventHandlers
- __OBJC_$_PROP_LIST_TVRDServer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_IRSessionDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBSRemoteAlertHandleObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TVRXDeviceQueryDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TVRXKeyboardControllerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__TVRXDeviceDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TVRCXPCRequestProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TVRDClientProcessConnectionDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_IRSessionDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBSRemoteAlertHandleObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_TVRCXPCRequestProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_TVRDClientProcessConnectionDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_TVRXDeviceQueryDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_TVRXKeyboardControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES__TVRXDeviceDelegate
- __OBJC_$_PROTOCOL_REFS_IRSessionDelegate
- __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_REFS_SBSRemoteAlertHandleObserver
- __OBJC_$_PROTOCOL_REFS_TVRCXPCRequestProtocol
- __OBJC_$_PROTOCOL_REFS_TVRDClientProcessConnectionDelegate
- __OBJC_$_PROTOCOL_REFS_TVRXDeviceQueryDelegate
- __OBJC_$_PROTOCOL_REFS_TVRXKeyboardControllerDelegate
- __OBJC_$_PROTOCOL_REFS__TVRXDeviceDelegate
- __OBJC_CLASS_PROTOCOLS_$_TVRDClientProcessConnection
- __OBJC_CLASS_PROTOCOLS_$_TVRDIRSessionManager
- __OBJC_CLASS_PROTOCOLS_$_TVRDServer
- __OBJC_CLASS_RO_$_TVRDAssertionManager
- __OBJC_CLASS_RO_$_TVRDClientProcessConnection
- __OBJC_CLASS_RO_$_TVRDIRSessionManager
- __OBJC_CLASS_RO_$_TVRDLaunchEventHandlers
- __OBJC_CLASS_RO_$_TVRDServer
- __OBJC_LABEL_PROTOCOL_$_IRSessionDelegate
- __OBJC_LABEL_PROTOCOL_$_NSObject
- __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
- __OBJC_LABEL_PROTOCOL_$_SBSRemoteAlertHandleObserver
- __OBJC_LABEL_PROTOCOL_$_TVRCXPCRequestProtocol
- __OBJC_LABEL_PROTOCOL_$_TVRDClientProcessConnectionDelegate
- __OBJC_LABEL_PROTOCOL_$_TVRXDeviceQueryDelegate
- __OBJC_LABEL_PROTOCOL_$_TVRXKeyboardControllerDelegate
- __OBJC_LABEL_PROTOCOL_$__TVRXDeviceDelegate
- __OBJC_METACLASS_RO_$_TVRDAssertionManager
- __OBJC_METACLASS_RO_$_TVRDClientProcessConnection
- __OBJC_METACLASS_RO_$_TVRDIRSessionManager
- __OBJC_METACLASS_RO_$_TVRDLaunchEventHandlers
- __OBJC_METACLASS_RO_$_TVRDServer
- __OBJC_PROTOCOL_$_IRSessionDelegate
- __OBJC_PROTOCOL_$_NSObject
- __OBJC_PROTOCOL_$_NSXPCListenerDelegate
- __OBJC_PROTOCOL_$_SBSRemoteAlertHandleObserver
- __OBJC_PROTOCOL_$_TVRCXPCRequestProtocol
- __OBJC_PROTOCOL_$_TVRDClientProcessConnectionDelegate
- __OBJC_PROTOCOL_$_TVRXDeviceQueryDelegate
- __OBJC_PROTOCOL_$_TVRXKeyboardControllerDelegate
- __OBJC_PROTOCOL_$__TVRXDeviceDelegate
- __TVRDIRLog
- __TVRDXPCLog
- ___18-[TVRDServer init]_block_invoke
- ___29-[TVRDIRSessionManager pause]_block_invoke
- ___30-[TVRDAssertionManager _setup]_block_invoke
- ___38+[TVRDAssertionManager sharedInstance]_block_invoke
- ___39-[TVRDServer _activateIRSessionManager]_block_invoke
- ___41+[TVRDLaunchEventHandlers sharedInstance]_block_invoke
- ___41-[TVRDIRSessionManager _restartIRSession]_block_invoke
- ___44-[TVRDServer _publishUserPresenceForDevice:]_block_invoke
- ___48-[TVRDIRSessionManager _activateWithCompletion:]_block_invoke
- ___48-[TVRDLaunchEventHandlers _setupNotifydHandlers]_block_invoke
- ___48-[TVRDServer clientConnectionSeveredConnection:]_block_invoke
- ___49-[TVRDIRSessionManager session:didUpdateContext:]_block_invoke
- ___49-[TVRDServer listener:shouldAcceptNewConnection:]_block_invoke
- ___50-[TVRDAssertionManager acquireLockScreenAssertion]_block_invoke
- ___50-[TVRDLaunchEventHandlers _setupDistnotedHandlers]_block_invoke
- ___51-[TVRDServer _switchToCurrentUserProfileForDevice:]_block_invoke
- ___54-[TVRDServer _becameInterestedInDeviceWithIdentifier:]_block_invoke
- ___55-[TVRDAssertionManager _createAssertionExpirationTimer]_block_invoke
- ___56-[TVRDServer clientConnectionRequestsEndingDeviceQuery:]_block_invoke
- ___61-[TVRDLaunchEventHandlers _enableTVRemoteControlCenterModule]_block_invoke
- ___62-[TVRDClientProcessConnection initWithXPCConnection:delegate:]_block_invoke
- ___64-[TVRDIRSessionManager _fetchServiceTokenWithCompletionHandler:]_block_invoke
- ___64-[TVRDIRSessionManager _fetchServiceTokenWithCompletionHandler:]_block_invoke_2
- ___65-[TVRDServer clientConnection:removedInterestedDeviceIdentifier:]_block_invoke
- ___67-[TVRDServer clientConnection:requestsSuggestedDeviceWithResponse:]_block_invoke
- ___68-[TVRDServer clientConnection:playItem:deviceIdentifier:completion:]_block_invoke
- ___70-[TVRDClientProcessConnection fetchActiveMREndpointUIDWithCompletion:]_block_invoke
- ___71-[TVRDServer clientConnectionRequestsStartingDeviceQuery:withResponse:]_block_invoke
- ___73-[TVRDServer clientConnection:cancelledAuthChallengeForDeviceIdentifier:]_block_invoke
- ___75-[TVRDServer clientConnection:requestsSendingInputText:toDeviceIdentifier:]_block_invoke
- ___76-[TVRDServer clientConnection:requestsSendingTouchEvent:toDeviceIdentifier:]_block_invoke
- ___77-[TVRDServer clientConnection:requestsSendingButtonEvent:toDeviceIdentifier:]_block_invoke
- ___78-[TVRDClientProcessConnection closeConnectionToDeviceWithIdentifier:withType:]_block_invoke
- ___79-[TVRDServer clientConnection:requestsSendingInputReturnKeyToDeviceIdentifier:]_block_invoke
- ___81-[TVRDServer clientConnection:addedInterestedDeviceIdentifier:connectionContext:]_block_invoke
- ___82-[TVRDServer clientConnection:requestsSendingInputDataPayload:toDeviceIdentifier:]_block_invoke
- ___84-[TVRDServer clientConnection:launchAppForDeviceWithIdentifier:bundleID:completion:]_block_invoke
- ___85-[TVRDServer clientConnection:fetchLaunchableAppsForDeviceWithIdentifier:completion:]_block_invoke
- ___85-[TVRDServer clientConnection:requestsSendingGameControllerEvent:toDeviceIdentifier:]_block_invoke
- ___86-[TVRDServer clientConnection:reiteratedInterestInDeviceIdentifier:connectionContext:]_block_invoke
- ___86-[TVRDServer clientConnection:requestsEnablingFindingSession:forDeviceWithIdentifier:]_block_invoke
- ___89-[TVRDServer clientConnection:addItemForDeviceWithIdentifier:mediaIdentifier:completion:]_block_invoke
- ___90-[TVRDServer clientConnection:requestsEnablingRemoteOnLockscreen:forDeviceWithIdentifier:]_block_invoke
- ___91-[TVRDServer clientConnection:receivedAuthChallengeLocallyEnteredCode:forDeviceIdentifier:]_block_invoke
- ___92-[TVRDServer clientConnection:removeItemForDeviceWithIdentifier:mediaIdentifier:completion:]_block_invoke
- ___92-[TVRDServer clientConnection:requestsSendingEvent:toDeviceWithIdentifier:options:response:]_block_invoke
- ___95-[TVRDServer clientConnection:markAsWatchedForDeviceWithIdentifier:mediaIdentifier:completion:]_block_invoke
- ___97-[TVRDServer clientConnection:fetchUpNextInfoForDeviceWithIdentifier:paginationToken:completion:]_block_invoke
- ____TVRDIRLog_block_invoke
- ____TVRDXPCLog_block_invoke
- ___block_descriptor_32_e17_v16?0"NSError"8l
- ___block_descriptor_32_e35_q24?0"TVRXDevice"8"TVRXDevice"16l
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_40_e8_32bs_e18_v16?0"NSString"8ls32l8
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
- ___block_descriptor_40_e8_32s_e45_"NSDictionary"16?0^{os_state_hints_s=I*II}8ls32l8
- ___block_descriptor_40_e8_32s_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8
- ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
- ___block_descriptor_40_e8_32w_e17_v16?0"NSTimer"8lw32l8
- ___block_descriptor_40_e8_32w_e33_v16?0"NSObject<OS_xpc_object>"8lw32l8
- ___block_descriptor_40_e8_32w_e36_v24?0"IRServiceToken"8"NSError"16lw32l8
- ___block_descriptor_40_e8_32w_e45_"NSDictionary"16?0^{os_state_hints_s=I*II}8lw32l8
- ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
- ___block_descriptor_48_e8_32bs40w_e36_v24?0"IRServiceToken"8"NSError"16ls32l8w40l8
- ___block_descriptor_48_e8_32s40bs_e36_v24?0"IRServiceToken"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e20_v16?0"TVRXDevice"8lw40l8s32l8
- ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global
- ___swift_reflection_version
- __block_literal_global.28
- __block_literal_global.39
- __block_literal_global.4
- __block_literal_global.8
- __swift_FORCE_LOAD_$_swiftCoreFoundation_$_tvremoted
- __swift_FORCE_LOAD_$_swiftDispatch_$_tvremoted
- __swift_FORCE_LOAD_$_swiftFoundation_$_tvremoted
- __swift_FORCE_LOAD_$_swiftObjectiveC_$_tvremoted
- __swift_FORCE_LOAD_$_swiftXPC_$_tvremoted
- __swift_FORCE_LOAD_$_swift_Builtin_float_$_tvremoted
- __swift_FORCE_LOAD_$_swiftos_$_tvremoted
- _main
- _objc_msgSend$_activateIRSessionManager
- _objc_msgSend$_activateWithCompletion:
- _objc_msgSend$_becameInterestedInDeviceWithIdentifier:
- _objc_msgSend$_cachedDeviceForIdentifier:
- _objc_msgSend$_candidateForDevice:createIfNeeded:
- _objc_msgSend$_connectToDeviceIfNeeded:
- _objc_msgSend$_createAssertionExpirationTimer
- _objc_msgSend$_deviceClassificationFromIRClassification:
- _objc_msgSend$_deviceForIdentifierInDeviceQuery:
- _objc_msgSend$_deviceForKeyboardController:
- _objc_msgSend$_donateEventWithEventType:forDevice:
- _objc_msgSend$_enableFindingSession:
- _objc_msgSend$_enableTVRemoteControlCenterModule
- _objc_msgSend$_fetchServiceTokenWithCompletionHandler:
- _objc_msgSend$_findCachedDeviceForIdentifier:
- _objc_msgSend$_informClientCouldNotLocateDeviceWithIdentifier:
- _objc_msgSend$_init
- _objc_msgSend$_initWithButtonType:
- _objc_msgSend$_interestedClientProcessConnectionsForDevice:
- _objc_msgSend$_invalidate
- _objc_msgSend$_invalidateIRSessionManager
- _objc_msgSend$_invalidateRemoteAlertHandle
- _objc_msgSend$_isButtonOfNowPlayingType:
- _objc_msgSend$_lostInterestInDeviceWithIdentifier:
- _objc_msgSend$_newLockScreenBehaviour
- _objc_msgSend$_processNameForPid:
- _objc_msgSend$_publishUserPresenceForDevice:
- _objc_msgSend$_removeAllIdentifiers
- _objc_msgSend$_removeIdentifier:
- _objc_msgSend$_restartIRSession
- _objc_msgSend$_setIdentifier:name:supportedButtons:
- _objc_msgSend$_setup
- _objc_msgSend$_setupDistnotedHandlers
- _objc_msgSend$_setupNotificationHandlers
- _objc_msgSend$_setupNotifydHandlers
- _objc_msgSend$_setupSession
- _objc_msgSend$_startGeneralDeviceQuery
- _objc_msgSend$_stopGeneralDeviceQuery
- _objc_msgSend$_switchToCurrentUserProfileForDevice:
- _objc_msgSend$_updateClientConnectionsForDevice:oldIdentifier:
- _objc_msgSend$_updateDevicesWithRecommendations:
- _objc_msgSend$aa_altDSID
- _objc_msgSend$acquireLockScreenAssertion
- _objc_msgSend$acquireSecureAppAssertionWithType:errorHandler:
- _objc_msgSend$acquireWakeToRemoteAlertAssertionWithDefinition:errorHandler:
- _objc_msgSend$activateWithCompletion:
- _objc_msgSend$activateWithContext:
- _objc_msgSend$addEvent:forCandidate:
- _objc_msgSend$addItemWithMediaIdentifier:completion:
- _objc_msgSend$addObject:
- _objc_msgSend$addObserver:selector:name:object:
- _objc_msgSend$addTimer:forMode:
- _objc_msgSend$alertHandle
- _objc_msgSend$allIdentifiers
- _objc_msgSend$allKeys
- _objc_msgSend$allObjects
- _objc_msgSend$allValues
- _objc_msgSend$alternateIdentifiers
- _objc_msgSend$ams_activeiCloudAccount
- _objc_msgSend$anyObject
- _objc_msgSend$appendString:withName:
- _objc_msgSend$applicationIsInstalled:
- _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
- _objc_msgSend$array
- _objc_msgSend$arrayOfStatesFromDevices:
- _objc_msgSend$assertion
- _objc_msgSend$attentionState
- _objc_msgSend$boolForKey:
- _objc_msgSend$boolValue
- _objc_msgSend$build
- _objc_msgSend$builderWithObject:
- _objc_msgSend$button
- _objc_msgSend$buttonEventForButton:eventType:
- _objc_msgSend$buttonType
- _objc_msgSend$cachedDevices
- _objc_msgSend$cancel
- _objc_msgSend$cancelPreviousPerformRequestsWithTarget:selector:object:
- _objc_msgSend$cancelSearchForDeviceWithIdentifier:
- _objc_msgSend$candidate
- _objc_msgSend$candidateIdentifier
- _objc_msgSend$candidateResults
- _objc_msgSend$challengeAttributes
- _objc_msgSend$challengeType
- _objc_msgSend$classification
- _objc_msgSend$clientConnection:addItemForDeviceWithIdentifier:mediaIdentifier:completion:
- _objc_msgSend$clientConnection:addedInterestedDeviceIdentifier:connectionContext:
- _objc_msgSend$clientConnection:cancelledAuthChallengeForDeviceIdentifier:
- _objc_msgSend$clientConnection:fetchLaunchableAppsForDeviceWithIdentifier:completion:
- _objc_msgSend$clientConnection:fetchUpNextInfoForDeviceWithIdentifier:paginationToken:completion:
- _objc_msgSend$clientConnection:isConnectedToDeviceWithIdentifier:
- _objc_msgSend$clientConnection:launchAppForDeviceWithIdentifier:bundleID:completion:
- _objc_msgSend$clientConnection:markAsWatchedForDeviceWithIdentifier:mediaIdentifier:completion:
- _objc_msgSend$clientConnection:playItem:deviceIdentifier:completion:
- _objc_msgSend$clientConnection:receivedAuthChallengeLocallyEnteredCode:forDeviceIdentifier:
- _objc_msgSend$clientConnection:reiteratedInterestInDeviceIdentifier:connectionContext:
- _objc_msgSend$clientConnection:removeItemForDeviceWithIdentifier:mediaIdentifier:completion:
- _objc_msgSend$clientConnection:removedInterestedDeviceIdentifier:
- _objc_msgSend$clientConnection:requestsEnablingFindingSession:forDeviceWithIdentifier:
- _objc_msgSend$clientConnection:requestsEnablingRemoteOnLockscreen:forDeviceWithIdentifier:
- _objc_msgSend$clientConnection:requestsSendingButtonEvent:toDeviceIdentifier:
- _objc_msgSend$clientConnection:requestsSendingEvent:toDeviceWithIdentifier:options:response:
- _objc_msgSend$clientConnection:requestsSendingGameControllerEvent:toDeviceIdentifier:
- _objc_msgSend$clientConnection:requestsSendingInputDataPayload:toDeviceIdentifier:
- _objc_msgSend$clientConnection:requestsSendingInputReturnKeyToDeviceIdentifier:
- _objc_msgSend$clientConnection:requestsSendingInputText:toDeviceIdentifier:
- _objc_msgSend$clientConnection:requestsSendingTouchEvent:toDeviceIdentifier:
- _objc_msgSend$clientConnection:requestsSuggestedDeviceWithResponse:
- _objc_msgSend$clientConnectionRequestsEndingDeviceQuery:
- _objc_msgSend$clientConnectionRequestsStartingDeviceQuery:withResponse:
- _objc_msgSend$clientConnectionSeveredConnection:
- _objc_msgSend$clientConnections
- _objc_msgSend$code
- _objc_msgSend$codeToEnterOnDevice
- _objc_msgSend$compare:options:
- _objc_msgSend$connect
- _objc_msgSend$connectionContextByID
- _objc_msgSend$connectionState
- _objc_msgSend$connectionType
- _objc_msgSend$containsIdentifier:
- _objc_msgSend$containsObject:
- _objc_msgSend$copy
- _objc_msgSend$count
- _objc_msgSend$countByEnumeratingWithState:objects:count:
- _objc_msgSend$countForObject:
- _objc_msgSend$countedSetDescriptionFor:
- _objc_msgSend$createServiceWithParameters:reply:
- _objc_msgSend$currentRunLoop
- _objc_msgSend$dataForKey:
- _objc_msgSend$date
- _objc_msgSend$defaultCenter
- _objc_msgSend$defaultStore
- _objc_msgSend$defaultWorkspace
- _objc_msgSend$deleteCandidate:
- _objc_msgSend$description
- _objc_msgSend$device:disconnectedForReason:error:
- _objc_msgSend$deviceBeganConnecting:
- _objc_msgSend$deviceConnected:
- _objc_msgSend$deviceIdentifiers
- _objc_msgSend$deviceQueryDidUpdateDevices:
- _objc_msgSend$deviceQueryObservers
- _objc_msgSend$deviceQueryUpdatedDiscoveredDevices:
- _objc_msgSend$deviceStateFromDevice:
- _objc_msgSend$deviceUpdatedState:
- _objc_msgSend$deviceWithState:encounteredAuthChallengeOfType:attributes:codeToEnterOnDevice:throttleSeconds:
- _objc_msgSend$devices
- _objc_msgSend$dictionary
- _objc_msgSend$dictionaryWithDictionary:
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$didInteractWithDevice:
- _objc_msgSend$disconnect
- _objc_msgSend$eventType
- _objc_msgSend$extendedDescription
- _objc_msgSend$fetchActiveEndpointWithCompletion:
- _objc_msgSend$fetchLaunchableAppsWithCompletion:
- _objc_msgSend$fetchUpNextInfoWithPaginationToken:completion:
- _objc_msgSend$filteredDeviceListHandler
- _objc_msgSend$filteredSetUsingPredicate:
- _objc_msgSend$findDeviceWithIdentifier:timeout:completion:
- _objc_msgSend$firstUnlocked
- _objc_msgSend$generalDeviceQuery
- _objc_msgSend$handleIconElementRequest:completionHandler:
- _objc_msgSend$hasPrefix:
- _objc_msgSend$hasStarted
- _objc_msgSend$identifier
- _objc_msgSend$identifierToCandidateMap
- _objc_msgSend$identifierToDeviceMap
- _objc_msgSend$idsIdentifier
- _objc_msgSend$initWithCandidateIdentifier:
- _objc_msgSend$initWithEventType:eventSubType:
- _objc_msgSend$initWithIntent:controlKind:controlType:extensionBundleIdentifier:containerBundleIdentifier:size:
- _objc_msgSend$initWithIntent:moduleIdentifier:containerBundleIdentifier:moduleSize:
- _objc_msgSend$initWithMachServiceName:
- _objc_msgSend$initWithServiceName:viewControllerClassName:
- _objc_msgSend$initWithServicePackage:
- _objc_msgSend$initWithServiceToken:
- _objc_msgSend$initWithXPCConnection:delegate:
- _objc_msgSend$integerValue
- _objc_msgSend$intersectSet:
- _objc_msgSend$intersectsSet:
- _objc_msgSend$invalidate
- _objc_msgSend$invalidateAssertionExpirationTimer
- _objc_msgSend$irSession
- _objc_msgSend$irSessionManager
- _objc_msgSend$isEqual:
- _objc_msgSend$isEqualToString:
- _objc_msgSend$isLockScreenAssertionActive
- _objc_msgSend$isManagedConfigProfileInstalled
- _objc_msgSend$isPersistOnLockScreenEnabled
- _objc_msgSend$isRunning
- _objc_msgSend$isWakeToRemoteOnLockScreenDisabled
- _objc_msgSend$keyboardController
- _objc_msgSend$launchAppWithBundleID:completion:
- _objc_msgSend$length
- _objc_msgSend$mainRunLoop
- _objc_msgSend$markAsWatchedWithMediaIdentifier:completion:
- _objc_msgSend$minusSet:
- _objc_msgSend$mutableCopy
- _objc_msgSend$mutableIdentifiers
- _objc_msgSend$name
- _objc_msgSend$negotiatedVersion
- _objc_msgSend$newHandleWithDefinition:configurationContext:
- _objc_msgSend$numberWithInt:
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$objectForKey:
- _objc_msgSend$objectForKeyedSubscript:
- _objc_msgSend$paired
- _objc_msgSend$pause
- _objc_msgSend$performSelector:withObject:afterDelay:
- _objc_msgSend$phase
- _objc_msgSend$playItem:completion:
- _objc_msgSend$predicateWithFormat:
- _objc_msgSend$processIdentifier
- _objc_msgSend$processNewDevices:
- _objc_msgSend$refreshState
- _objc_msgSend$registerObserver:
- _objc_msgSend$releaseLockScreenAssertion
- _objc_msgSend$remoteObjectProxy
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
- _objc_msgSend$removeAllObjects
- _objc_msgSend$removeDevice:
- _objc_msgSend$removeInterestForDeviceWithIdentifier:
- _objc_msgSend$removeItemWithMediaIdentifier:completion:
- _objc_msgSend$removeObject:
- _objc_msgSend$removeObjectForKey:
- _objc_msgSend$requestCurrentContext
- _objc_msgSend$requestCurrentRecommendedDevices
- _objc_msgSend$requestInterface
- _objc_msgSend$requestedModuleEnablement
- _objc_msgSend$responseInterface
- _objc_msgSend$resume
- _objc_msgSend$run
- _objc_msgSend$runWithConfiguration:
- _objc_msgSend$screenLocked
- _objc_msgSend$sendButtonEvent:
- _objc_msgSend$sendEvent:options:response:
- _objc_msgSend$sendGameControllerEvent:
- _objc_msgSend$sendReturnKey
- _objc_msgSend$sendTextActionPayload:
- _objc_msgSend$sendTouchEvent:
- _objc_msgSend$serviceToken
- _objc_msgSend$set
- _objc_msgSend$setAlertHandle:
- _objc_msgSend$setAvOutpuDeviceIdentifier:
- _objc_msgSend$setBool:forKey:
- _objc_msgSend$setClassification:
- _objc_msgSend$setDelegate:
- _objc_msgSend$setDisconnectError:
- _objc_msgSend$setDisconnectReason:
- _objc_msgSend$setExportedInterface:
- _objc_msgSend$setExportedObject:
- _objc_msgSend$setFilteredDeviceListHandler:
- _objc_msgSend$setFirstUnlockHandler:
- _objc_msgSend$setHasStarted:
- _objc_msgSend$setIdsIdentifier:
- _objc_msgSend$setInterruptionHandler:
- _objc_msgSend$setInvalidationHandler:
- _objc_msgSend$setIrSessionManager:
- _objc_msgSend$setMode:
- _objc_msgSend$setObject:forKey:
- _objc_msgSend$setObject:forKeyedSubscript:
- _objc_msgSend$setOfStatesFromDevices:
- _objc_msgSend$setRapportIdentifier:
- _objc_msgSend$setRemoteObjectInterface:
- _objc_msgSend$setRequestedModuleEnablement:
- _objc_msgSend$setScreenLockedChangedHandler:
- _objc_msgSend$setSuggestedDevices:
- _objc_msgSend$setText:
- _objc_msgSend$setUserInfo:
- _objc_msgSend$setValue:forKey:
- _objc_msgSend$setWithArray:
- _objc_msgSend$setWithObject:
- _objc_msgSend$setWithSet:
- _objc_msgSend$setupHandlers
- _objc_msgSend$sharedInstance
- _objc_msgSend$sortUsingComparator:
- _objc_msgSend$standardUserDefaults
- _objc_msgSend$start
- _objc_msgSend$startAssertionExpirationTimer
- _objc_msgSend$stateDictionary
- _objc_msgSend$stop
- _objc_msgSend$stringValue
- _objc_msgSend$stringWithFormat:
- _objc_msgSend$stringWithUTF8String:
- _objc_msgSend$substringFromIndex:
- _objc_msgSend$suggestedDevices
- _objc_msgSend$suggestedDevices:
- _objc_msgSend$systemMonitor
- _objc_msgSend$throttleSeconds
- _objc_msgSend$timeIntervalSinceNow
- _objc_msgSend$timerWithTimeInterval:repeats:block:
- _objc_msgSend$unarchivedObjectOfClass:fromData:error:
- _objc_msgSend$unregisterObserver:
- _objc_msgSend$updateCandidates:
- _objc_msgSend$updateDevice:withConnectionContext:
- _objc_msgSend$updateDeviceIdentifier:to:
- _objc_msgSend$updateNodes:
- _objc_msgSend$userEnteredCodeLocally:
- _objc_msgSend$xpcConnection
- _objc_release_x2
- _objc_release_x3
- _objc_release_x4
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _tvremotedVersionNumber
- _tvremotedVersionString
- main.cold.1
- sharedInstance.onceToken
- sharedInstance.sharedInstance
- tvremoted.m
- tvremoted_vers.c
CStrings:
+ "%{public}@"
+ "'%{public}@' topShelfInfo updated: %{public}@"
+ "Broadcasting to %{public}@, that top shelf info was updated: %{public}@"
+ "Client %{public}@ is not entitled to start/stop finding session"
+ "Client connection %{public}@ requested to send find my payload (length: %lu)"
+ "Device does not support adding items"
+ "Device does not support fetching Up Next info"
+ "Device does not support fetching launchable apps"
+ "Device does not support launching apps"
+ "Device does not support marking items as watched"
+ "Device does not support playing items"
+ "Device does not support removing items"
+ "Failed to bridge legacy stream UserInfo to NSDictionary"
+ "Find My not available for device: %@"
+ "Find My not available for device: %{public}@"
+ "Find My not available for this device"
+ "IRSessionManager was deallocated before config mode could be updated"
+ "IRSessionManager was deallocated before session could be started"
+ "Ignoring trusted stream event — restricted_distributed_notifications flag is off"
+ "Invalid entitlements"
+ "LaunchServices"
+ "Legacy stream UserInfo is missing or not XPC_TYPE_DICTIONARY"
+ "Received an application registered LaunchEvent (trusted stream)"
+ "Received nil service token without error"
+ "Received nil token without error"
+ "Trusted stream UserInfo data is empty"
+ "Trusted stream UserInfo is missing or not XPC_TYPE_DATA"
+ "Trusted stream UserInfo is not an NSDictionary"
+ "_newLockScreenBehavior"
+ "_sendFindMyPayload:response:"
+ "clientConnection:fetchLaunchableAppsForDeviceWithIdentifier:range:completion:"
+ "clientConnection:sendFindMyPayload:toDeviceIdentifier:response:"
+ "com.apple.TVRemoteApp"
+ "com.apple.TVRemoteApp.TVRemoteWidget"
+ "com.apple.TVRemoteApp.widget.button"
+ "com.apple.distnoted.matching.trusted"
+ "com.apple.private.tvremote.findmy"
+ "dataWithBytesNoCopy:length:freeWhenDone:"
+ "device:updatedTopShelfInfo:"
+ "fetchLaunchableAppsForDeviceWithIdentifier:range:completion:"
+ "fetchLaunchableAppsWithRange:completion:"
+ "isInternalInstall"
+ "isUsingNewBundleID"
+ "propertyListWithData:options:format:error:"
+ "restricted_distributed_notifications"
+ "sendFindMyPayload:toDeviceIdentifier:response:"
+ "v16@?0@\"NSDictionary\"8"
+ "v32@0:8@\"TVRXDevice\"16@\"TVRCTopShelfInfo\"24"
+ "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v48@0:8@\"NSString\"16{_NSRange=QQ}24@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@\"TVRDClientProcessConnection\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v48@0:8@16{_NSRange=QQ}24@?40"
+ "v56@0:8@\"TVRDClientProcessConnection\"16@\"NSString\"24{_NSRange=QQ}32@?<v@?@\"NSDictionary\"@\"NSError\">48"
+ "v56@0:8@16@24{_NSRange=QQ}32@?48"
+ "valueForEntitlement:"
- "Find My not avaiable for device: %@"
- "_newLockScreenBehaviour"
- "clientConnection:fetchLaunchableAppsForDeviceWithIdentifier:completion:"
- "fetchLaunchableAppsForDeviceWithIdentifier:completion:"
- "fetchLaunchableAppsWithCompletion:"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v40@0:8@\"TVRDClientProcessConnection\"16@\"NSString\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"

```
