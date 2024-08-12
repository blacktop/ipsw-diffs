## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3400.154.4.0.0
-  __TEXT.__text: 0x368b40
-  __TEXT.__auth_stubs: 0x3430
-  __TEXT.__objc_stubs: 0x44c60
-  __TEXT.__objc_methlist: 0x1d29c
-  __TEXT.__const: 0x10b68
-  __TEXT.__gcc_except_tab: 0x4768
-  __TEXT.__cstring: 0x50dd7
-  __TEXT.__oslogstring: 0x3dbf8
-  __TEXT.__objc_classname: 0x51b4
-  __TEXT.__objc_methname: 0x5cac5
-  __TEXT.__objc_methtype: 0xedc0
-  __TEXT.__dlopen_cstrs: 0x97a
+3401.10.1.1.1
+  __TEXT.__text: 0x36a1e0
+  __TEXT.__auth_stubs: 0x3450
+  __TEXT.__objc_stubs: 0x44fa0
+  __TEXT.__objc_methlist: 0x1d364
+  __TEXT.__const: 0x10998
+  __TEXT.__gcc_except_tab: 0x480c
+  __TEXT.__cstring: 0x51024
+  __TEXT.__oslogstring: 0x3e328
+  __TEXT.__objc_classname: 0x51b3
+  __TEXT.__objc_methname: 0x5cf59
+  __TEXT.__objc_methtype: 0xee2f
+  __TEXT.__dlopen_cstrs: 0x9ce
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xa338
-  __TEXT.__eh_frame: 0xf38
-  __DATA_CONST.__auth_got: 0x1a28
-  __DATA_CONST.__got: 0x3af0
+  __TEXT.__unwind_info: 0xa3a0
+  __TEXT.__eh_frame: 0xe70
+  __DATA_CONST.__auth_got: 0x1a38
+  __DATA_CONST.__got: 0x3af8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x15270
-  __DATA_CONST.__cfstring: 0x12460
+  __DATA_CONST.__const: 0x15030
+  __DATA_CONST.__cfstring: 0x12500
   __DATA_CONST.__objc_classlist: 0xd28
   __DATA_CONST.__objc_catlist: 0x630
   __DATA_CONST.__objc_protolist: 0x6d8

   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x3ceb8
-  __DATA.__objc_selrefs: 0x13bd8
-  __DATA.__objc_ivar: 0x25cc
+  __DATA.__objc_const: 0x3d018
+  __DATA.__objc_selrefs: 0x13cb8
+  __DATA.__objc_ivar: 0x25ec
   __DATA.__objc_data: 0x8390
-  __DATA.__data: 0x5ff0
-  __DATA.__bss: 0xe40
+  __DATA.__data: 0x6048
+  __DATA.__bss: 0xe38
   __DATA.__common: 0x48
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation
+  - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/ContactsAssistantServices.framework/ContactsAssistantServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14351
-  Symbols:   2874
-  CStrings:  26891
+  Functions: 14399
+  Symbols:   2877
+  CStrings:  26967
 
Symbols:
+ _AFBTCarHeadunitsConnectedInLast24Hours
+ _AFDeviceSupportsSystemAssistantExperience
+ _OBJC_CLASS_$_ODDSiriSchemaODDAppleIntelligenceProperties
+ _SASetRequestOriginStatusValidValue
+ _objc_copyStruct
- _AFBTHeadunitsConnectedInLast24Hours
- _kCLLocationAccuracyBestForNavigation
CStrings:
+ "\x03)\x15"
+ "\x04\x15\x14\x121#"
+ "%!@(MISSING) {allowsAWDL = %!l(MISSING)ld, allowsBLE = %!l(MISSING)ld, allowsInfraWiFi = %!l(MISSING)ld, allowsBTPipe = %!l(MISSING)ld, allowsForceBLE = %!l(MISSING)ld, allowsForceAWDL = %!l(MISSING)ld, noL2Cap = %!l(MISSING)ld}"
+ "%!s(MISSING) AVSystemController subscription complete"
+ "%!s(MISSING) Announcement request ended and the queue is empty and/or we are waiting for user input before reading the next announcement"
+ "%!s(MISSING) Clearing location sent to server"
+ "%!s(MISSING) Currently waiting for explicit user input"
+ "%!s(MISSING) Deferring Audio session deactivation since we are waiting for user input"
+ "%!s(MISSING) Disable Bluetooth L2Cap connection"
+ "%!s(MISSING) Failed to fetch bluetooth controller info when logging bluetooth status: %!@(MISSING)"
+ "%!s(MISSING) Ignoring activation failures caused by gesture invocation, associated with request UUID: %!@(MISSING)"
+ "%!s(MISSING) Not sending location to server because location age difference %!g(MISSING) is less than or equal to %!g(MISSING)"
+ "%!s(MISSING) Not sending location to server because running full UOD"
+ "%!s(MISSING) Not sending location to server for server request because location is too old. Max age %!@(MISSING)"
+ "%!s(MISSING) Not starting announcement: request has already been started"
+ "%!s(MISSING) Not starting announcement: waiting for user input"
+ "%!s(MISSING) Request (UUID: %!@(MISSING)) cancelled as a result of a gesture-based follow-up"
+ "%!s(MISSING) Sending location to server because because it's running on stationary device"
+ "%!s(MISSING) Sending location to server because it asked us for location update"
+ "%!s(MISSING) Sending location to server because location altitude has changed for more than 50 centimeters"
+ "%!s(MISSING) Sending location to server because never sent it to server during this session"
+ "%!s(MISSING) Sending location to server because new location accuracy %!g(MISSING) is better than old %!g(MISSING)"
+ "%!s(MISSING) Sending location to server because new location is further than 10m from previously sent"
+ "%!s(MISSING) Sending location to server because of needsToSendLocation override"
+ "%!s(MISSING) [_reallyHandleNewStartRequest] Dismissing Siri with reason AFDismissalAssetsNotReady"
+ "%!s(MISSING) [_reallyHandleNewStartRequest] Dismissing Siri with reason AFDismissalAssetsNotReadySAE"
+ "%!s(MISSING) [_sendStartSpeechCommandWithSpeechManager] Dismissing Siri with reason AFDismissalAssetsNotReady"
+ "%!s(MISSING) [_sendStartSpeechCommandWithSpeechManager] Dismissing Siri with reason AFDismissalAssetsNotReadySAE"
+ "%!s(MISSING) current state: %!@(MISSING), waitingForUserInput: %!d(MISSING)"
+ "%!s(MISSING) notifyObserver didChangeStateFrom: %!l(MISSING)lu to: %!l(MISSING)lu"
+ "+[ADCommandCenter _fetchBluetoothState]"
+ "-[ADCommandCenter _cancelCurrentRequestForReason:andError:successorInfo:]"
+ "-[ADCompanionService getDevicesDiscoveredNearbyForUserID:]_block_invoke"
+ "-[ADCompanionService getDevicesDiscoveredTypeCountForUserID:]"
+ "-[ADExternalNotificationRequestHandler notifyObserver:didChangeStateFrom:to:]"
+ "-[ADExternalNotificationRequestHandler requestLifecycleObserver:requestWasCancelledWithInfo:forReason:origin:client:successorInfo:]"
+ "-[ADExternalNotificationRequestHandler requestLifecycleObserver:requestWasCancelledWithInfo:forReason:origin:client:successorInfo:]_block_invoke"
+ "-[ADLocationManager shouldSendLocationToServer:forAceCommand:]"
+ "-[ADRequestLifecycleObserver requestWasCancelledWithInfo:forReason:origin:client:successorInfo:]"
+ "-[AFSiriHeadphonesMonitor _init]_block_invoke_2"
+ "2"
+ "@72@0:8q16q24q32q40q48q56q64"
+ "ADInstrumentationDeviceDiscoveryQueue"
+ "ADRapportLinkTransportOptions::noL2Cap"
+ "ADReplaceRequestDelegateReason"
+ "Class getICLibraryAuthServiceClientTokenProviderClass(void)_block_invoke"
+ "MobileAssistantDaemons-3401.10.1.1.1"
+ "T@\"CLLocation\",&,V_locationSentToServer"
+ "TB,N,V_doNotClearLocationManagerDelegateForUnitTests"
+ "TB,V_allowAdHocSendingLocationToServer"
+ "TB,V_isNavigating"
+ "TB,V_needsToSendLocation"
+ "Tq,R,N,V_noL2Cap"
+ "TryItCompleted"
+ "T{ADLocationManagerState=Biq},V_currentState"
+ "_allowAdHocSendingLocationToServer"
+ "_cancelCurrentRequestForReason:andError:successorInfo:"
+ "_doNotClearLocationManagerDelegateForUnitTests"
+ "_fetchBluetoothState"
+ "_gestureInterruptedRequestUUID"
+ "_getAppleIntelligenceProperties"
+ "_getIsAppleIntelligenceEnabled"
+ "_getIsSiriTryItCompleted"
+ "_locationSentToServer"
+ "_locationSentToServerLock"
+ "_noL2Cap"
+ "_orchBluetoothStateEnumFromBluetoothState:"
+ "_sessionWasAnnouncement"
+ "_waitForUserInputAfterReading"
+ "allowAdHocSendingLocationToServer"
+ "bluetoothState"
+ "com.apple.SiriCarouselAlert"
+ "controllerInfoAndReturnError:"
+ "createSetRequestOrigin"
+ "currentState"
+ "distanceFromLocation:"
+ "doNotClearLocationManagerDelegateForUnitTests"
+ "getNoL2Cap"
+ "home:didUpdateDismissedWalletKeyUWBUnlockOnboarding:"
+ "initWithAllowsAWDL:allowsBLE:allowsInfraWiFi:allowsBTPipe:allowsForceBLE:allowsForceAWDL:noL2Cap:"
+ "isWifiEnabled"
+ "locationSentToServer"
+ "noL2Cap"
+ "publisherWithUseCase:options:"
+ "requestLifecycleObserver:requestWasCancelledWithInfo:forReason:origin:client:successorInfo:"
+ "requestWasCancelledWithInfo:forReason:origin:client:successorInfo:"
+ "setAllowAdHocSendingLocationToServer:"
+ "setAppleIntelligence:"
+ "setBluetoothState:"
+ "setCurrentState:"
+ "setDoNotClearLocationManagerDelegateForUnitTests:"
+ "setIsAppleIntelligenceEnabled:"
+ "setIsNavigating:"
+ "setIsSiriTryItCompleted:"
+ "setIsWifiEnabled:"
+ "setLocationSentToServer:"
+ "setNoL2Cap:"
+ "setUsesPeerManagedSync:"
+ "shouldSendLocationToServer:forAceCommand:"
+ "v32@0:8{ADLocationManagerState=Biq}16"
+ "v64@0:8@\"ADRequestLifecycleObserver\"16@\"AFRequestInfo\"24q32q40@\"<ADCommandCenterClient>\"48@\"AFRequestInfo\"56"
+ "v64@0:8@16@24q32q40@48@56"
+ "{ADLocationManagerState=Biq}16@0:8"
+ "{_mutationFlags=\"isDirty\"b1\"hasAllowsAWDL\"b1\"hasAllowsBLE\"b1\"hasAllowsInfraWiFi\"b1\"hasAllowsBTPipe\"b1\"hasAllowsForceBLE\"b1\"hasAllowsForceAWDL\"b1\"hasNoL2Cap\"b1}"
- "\x03)\x14"
- "\x041\x14\x14\x12!\""
- "%!@(MISSING) {allowsAWDL = %!l(MISSING)ld, allowsBLE = %!l(MISSING)ld, allowsInfraWiFi = %!l(MISSING)ld, allowsBTPipe = %!l(MISSING)ld, allowsForceBLE = %!l(MISSING)ld, allowsForceAWDL = %!l(MISSING)ld}"
- "%!s(MISSING) Deferring Audio session deactivation since it has been requested"
- "%!s(MISSING) Request has already been started"
- "%!s(MISSING) Should send location for desired accuracy %!l(MISSING)f %!@(MISSING)"
- "%!s(MISSING) current state: %!@(MISSING)"
- "-[ADCommandCenter _cancelCurrentRequestForReason:andError:]"
- "-[ADCompanionService getDevicesDiscoveredNearbyForUserID:]"
- "-[ADExternalNotificationRequestHandler audioSessionDidEnd]"
- "-[ADExternalNotificationRequestHandler requestLifecycleObserver:requestWasCancelledWithInfo:forReason:origin:client:]_block_invoke"
- "-[ADLocationManager _shouldSendLocationUpdate:fromLocation:forCommand:]"
- "-[ADRequestLifecycleObserver requestWasCancelledWithInfo:forReason:origin:client:]"
- "58"
- "@64@0:8q16q24q32q40q48q56"
- "Ignoring expired item %!@(MISSING)"
- "MobileAssistantDaemons-3400.154.4"
- "TB,N,V_needsToSendLocation"
- "_cancelCurrentRequestForReason:andError:"
- "_shouldDeferAudioSessionActivationForRequest"
- "_shouldSendLocationUpdate:fromLocation:forCommand:"
- "audioSessionDidEnd"
- "initWithAllowsAWDL:allowsBLE:allowsInfraWiFi:allowsBTPipe:allowsForceBLE:allowsForceAWDL:"
- "publisherWithUseCase:"
- "requestLifecycleObserver:requestWasCancelledWithInfo:forReason:origin:client:"
- "requestWasCancelledWithInfo:forReason:origin:client:"
- "v56@0:8@\"ADRequestLifecycleObserver\"16@\"AFRequestInfo\"24q32q40@\"<ADCommandCenterClient>\"48"
- "v56@0:8@16@24q32q40@48"
- "{_mutationFlags=\"isDirty\"b1\"hasAllowsAWDL\"b1\"hasAllowsBLE\"b1\"hasAllowsInfraWiFi\"b1\"hasAllowsBTPipe\"b1\"hasAllowsForceBLE\"b1\"hasAllowsForceAWDL\"b1}"

```
