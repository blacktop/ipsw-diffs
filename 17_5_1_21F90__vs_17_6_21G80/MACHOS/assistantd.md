## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3305.24.1.0.0
-  __TEXT.__text: 0x346768
-  __TEXT.__auth_stubs: 0x32d0
-  __TEXT.__objc_stubs: 0x424c0
-  __TEXT.__objc_methlist: 0x1c2dc
-  __TEXT.__const: 0x104e8
-  __TEXT.__gcc_except_tab: 0x2d08
-  __TEXT.__cstring: 0x4dd09
-  __TEXT.__objc_classname: 0x4ffa
-  __TEXT.__objc_methname: 0x592ae
-  __TEXT.__objc_methtype: 0xe737
-  __TEXT.__oslogstring: 0x3a051
+3306.26.2.0.0
+  __TEXT.__text: 0x34afd8
+  __TEXT.__auth_stubs: 0x32e0
+  __TEXT.__objc_stubs: 0x42a00
+  __TEXT.__objc_methlist: 0x1c59c
+  __TEXT.__const: 0x10520
+  __TEXT.__gcc_except_tab: 0x2ce4
+  __TEXT.__cstring: 0x4e320
+  __TEXT.__objc_classname: 0x5049
+  __TEXT.__objc_methname: 0x59aca
+  __TEXT.__objc_methtype: 0xe8d3
+  __TEXT.__oslogstring: 0x3b028
   __TEXT.__dlopen_cstrs: 0x848
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xac54
+  __TEXT.__unwind_info: 0xad7c
   __TEXT.__eh_frame: 0xf30
-  __DATA_CONST.__auth_got: 0x1978
-  __DATA_CONST.__got: 0x1ec0
+  __DATA_CONST.__auth_got: 0x1980
+  __DATA_CONST.__got: 0x1ed0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x153b8
-  __DATA_CONST.__cfstring: 0x11ce0
-  __DATA_CONST.__objc_classlist: 0xce8
-  __DATA_CONST.__objc_catlist: 0x628
-  __DATA_CONST.__objc_protolist: 0x6a0
+  __DATA_CONST.__const: 0x15538
+  __DATA_CONST.__cfstring: 0x11c00
+  __DATA_CONST.__objc_classlist: 0xcf8
+  __DATA_CONST.__objc_catlist: 0x630
+  __DATA_CONST.__objc_protolist: 0x6a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_classrefs: 0x2640
-  __DATA_CONST.__objc_superrefs: 0xae0
+  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_classrefs: 0x2650
+  __DATA_CONST.__objc_superrefs: 0xae8
   __DATA_CONST.__objc_arraydata: 0x3c8
   __DATA_CONST.__objc_arrayobj: 0x1b0
   __DATA_CONST.__objc_intobj: 0x7f8
   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x3b2a0
-  __DATA.__objc_selrefs: 0x12ee0
-  __DATA.__objc_ivar: 0x24a4
-  __DATA.__objc_data: 0x8110
-  __DATA.__data: 0x5d40
-  __DATA.__bss: 0xdd0
+  __DATA.__objc_const: 0x3b7c0
+  __DATA.__objc_selrefs: 0x13040
+  __DATA.__objc_ivar: 0x24c8
+  __DATA.__objc_data: 0x81b0
+  __DATA.__data: 0x5da0
+  __DATA.__bss: 0xde0
   __DATA.__common: 0x48
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13812
-  Symbols:   2815
-  CStrings:  25807
+  Functions: 13885
+  Symbols:   2818
+  CStrings:  25947
 
Symbols:
+ _CLLocationCoordinate2DMake
+ _kAFLocationServiceEntitlement
+ _kAFLocationServiceErrorDomain
+ _kAFLocationServiceMachServiceName
- _SASetRequestOriginStatusValidValue
CStrings:
+ "\x041\x14\x14\x12!\""
+ "\x0f\x02\x11\x12\x14\x11"
+ "%s %@ Location Service Connection Connected (pid=%d])"
+ "%s %@ Location Service Connection does not have required entitlements."
+ "%s ADLocationManager is deallocated unexpectedly when location fetch timeout was triggered"
+ "%s ADLocationManager is deallocated unexpectedly while waiting for location shifting to complete. Origin %@"
+ "%s ADPeerLocationRemote: location found for peer"
+ "%s ADPeerLocationRemote: looking up best location on behalf of peer"
+ "%s Attempting to shift from location: %{private}@"
+ "%s Authorization status changed to %d, isEnabled: %@, preciseLocationEnabled: %@"
+ "%s Authorization status is a form of 'denied' with value: %d"
+ "%s Authorization style update is not needed. Location services enabled: %@, current auth: %@, accuracy auth: %@"
+ "%s Cache-based location shifting failed"
+ "%s Cached location accuracy is not satisfying requested accuracy of %f, starting location monitoring routine"
+ "%s Cached location satisfies requested accuracy %f"
+ "%s Cancelling location update session teardown timer"
+ "%s Clearing last shifted location"
+ "%s Clearing location service cache"
+ "%s CoreLocation decline presenting authorization prompt with error: %@. This error is intentionally ignored. Currently awaiting requests count: %lu"
+ "%s Creating location snapshot from cached location"
+ "%s Device found over iWifi or destination device is a proxyHost on local device."
+ "%s Draining authorization requests with error %@"
+ "%s Draining location fetch requests with error %@"
+ "%s Ending location update session"
+ "%s Fetching location authorization via %@ is not supported when location service prompting feature is enabled"
+ "%s Full accuracy is already granted"
+ "%s Generating location snapshot for authorization status: %d, accuracy authorization: %ld"
+ "%s Generating location snapshot for location services disabled"
+ "%s Internal queue hop"
+ "%s Location fetch is skipped due to lack of authorization, status: %d"
+ "%s Location fetch is skipped due to location services being completely disabled"
+ "%s Location is already shifted"
+ "%s Location prefetch is skipped due to lack of authorization, status: %d"
+ "%s Location prefetching routine is started - grabbing assertion once"
+ "%s Location shifter needs to fetch shifter function from network"
+ "%s Location shifting is not needed"
+ "%s Location update session ended - releasing assertion"
+ "%s Location update session is already active, not trying to activate it again"
+ "%s Location update session is not active, not trying to end it"
+ "%s LocationService not handling error %{public}@"
+ "%s No cached location available to create location snapshot"
+ "%s No cached location available to shift for location snapshot"
+ "%s No cached location, starting location monitoring routine with accuracy of %f"
+ "%s Not ending location update session. UI visible: %@, location fetch requests count: %lu"
+ "%s Not forcing location update from CoreLocation because location update session is not active"
+ "%s Not requesting location authorization due to location services being completely disabled"
+ "%s Not requesting temporary accuracy authorization due to location services being completely disabled"
+ "%s Not upgrading desired accuracy of location to %.5g. Session status: %lu, current desired accuracy: %.5g"
+ "%s Received current authorizationg style request"
+ "%s Received current location request with accuracy: %.5g, timeout: %.5g"
+ "%s Received location authorization request with style: %@, timeout: %.5g"
+ "%s Received non-error response for requestTemporaryFullAccuracyAuthorizationWithPurposeKey:completion:, preciseLocationEnabled: %@"
+ "%s Received temporary accuracy authorization request with style: %@, timeout: %.5g"
+ "%s Received update authorization style: %@, timeout: %.5g"
+ "%s Received update temporary accuracy authorization, isAuthorized: %@, timeout: %.5g"
+ "%s Requesting 'always' location authorization"
+ "%s Requesting 'when in use' location authorization"
+ "%s Scheduling location update session teardown"
+ "%s Sending requestTemporaryFullAccuracyAuthorizationWithPurposeKey:completion:"
+ "%s Sending the dialog dismiss to CoreLocation"
+ "%s Shifting location failed due to error: %{public}@"
+ "%s Someone is fetching current location - grabbing assertion once"
+ "%s Starting location pre-fetching"
+ "%s Starting location shifting routine"
+ "%s Starting location update session"
+ "%s Starting location update session - grabbing assertion once"
+ "%s Starting location updates from CoreLocation"
+ "%s Starting updating location with CoreLocation"
+ "%s Stopping location updates from CoreLocation"
+ "%s Successfully performed location shifting"
+ "%s Target Device has ProxyHost status flag. Return true if local device is HomePod/HHDevice and target device is Sidekick."
+ "%s Tearing down location update session"
+ "%s Temporary accuracy update is not needed. Location services enabled: %@, current auth: %@, accuracy auth: %@"
+ "%s Temporary full accuracy request failed and it's intentionally ignored. Error: %{public}@. Currently awaiting requests count: %lu"
+ "%s UI dismissed per %@, ending location update session"
+ "%s Upgrading desired accuracy of location to %.5g"
+ "%s Using lastLocation for location snapshot"
+ "%s Using lastShiftedLocation for location snapshot"
+ "%s Will request location authorization - grabbing assertion once"
+ "%s Will request temporary full accuracy authorization - grabbing assertion once"
+ "%s isHomeHubDeviceLookingForItsHub: %@, isHubLookingForADeviceItIsHosting: %@"
+ "%s isLocalDeviceAnAudioAccessory: %@, isLocalDeviceHomeHubDevice: %@, isTargetDeviceHomeHubDevice: %@"
+ "%s prepareForAssistantEnablementInBackground is not available when location service prompting feature is enabled, TCC guardflow is in control of location authorization"
+ "%s willUseProxyCommunicationWithLocalDevice: %@, isDeviceDiscoveredOverInfraWifi: %@, shouldAllowAWDLFallback: %@, isAWDLFallbackForPersonalRequestsEnabled: %@"
+ "-[ADDaemon _locationServiceListenerShouldAcceptNewConnection:]"
+ "-[ADDailyDeviceStatusActivity buildDailyDeviceStatusHeartbeatMetricsWithSiriEnabled:onLockscreen:dictationEnabled:voiceTriggerEnabled:starkHasBeenActiveWithin24Hours:raiseToSpeakEnabled:activeAppleAudioDevices:spokenNotificationsEnabled:announceNotificationsEnabledOnHeadphones:carplayAnnounceEnablementType:isAnnounceNotificationsMutedForCarPlay:shouldSkipTriggerlessReplyConfirmation:spokenNotificationsProxCardSeen:spokenNotificationsControlCenterModuleEnabled:spokenNotificationsWhitelistSettings:announceCallsEnabled:preciseLocationEnabled:locationAccessPermission:adaptiveSiriVolumeEnabled:adaptiveSiriVolumePermanentOffsetEnabled:adaptiveSiriVolumePermanentOffsetFactor:adaptiveSiriVolumeMostRecentIntent:isRemoteDarwinVoiceTriggerEnabled:autoSendSettings:siriInCallEnablementState:hangUpEnablementState:heartbeatQueuedTime:siriVoiceTriggerSettings:isShowAppsBehindSiriEnabledOnCarPlay:isSiriCapableDigitalCarKeyAvailable:connectedBTCarHeadunits:withCompletion:]"
+ "-[ADDailyDeviceStatusActivity buildDailyDeviceStatusHeartbeatMetricsWithSiriEnabled:onLockscreen:dictationEnabled:voiceTriggerEnabled:starkHasBeenActiveWithin24Hours:raiseToSpeakEnabled:activeAppleAudioDevices:spokenNotificationsEnabled:announceNotificationsEnabledOnHeadphones:carplayAnnounceEnablementType:isAnnounceNotificationsMutedForCarPlay:shouldSkipTriggerlessReplyConfirmation:spokenNotificationsProxCardSeen:spokenNotificationsControlCenterModuleEnabled:spokenNotificationsWhitelistSettings:announceCallsEnabled:preciseLocationEnabled:locationAccessPermission:adaptiveSiriVolumeEnabled:adaptiveSiriVolumePermanentOffsetEnabled:adaptiveSiriVolumePermanentOffsetFactor:adaptiveSiriVolumeMostRecentIntent:isRemoteDarwinVoiceTriggerEnabled:autoSendSettings:siriInCallEnablementState:hangUpEnablementState:heartbeatQueuedTime:siriVoiceTriggerSettings:isShowAppsBehindSiriEnabledOnCarPlay:isSiriCapableDigitalCarKeyAvailable:connectedBTCarHeadunits:withCompletion:]_block_invoke"
+ "-[ADLocationManager _dismissTCCDialogIfNeeded]"
+ "-[ADLocationManager _generateResponseForGetRequestOriginCommand:withUnshiftedLocation:completion:]"
+ "-[ADLocationManager _generateResponseForGetRequestOriginCommand:withUnshiftedLocation:completion:]_block_invoke"
+ "-[ADLocationManager cancelLocationUpdateSessionTeardown]"
+ "-[ADLocationManager createCurrentLocationSnapshot]"
+ "-[ADLocationManager currentAuthorizationStyle:]"
+ "-[ADLocationManager currentAuthorizationStyle:]_block_invoke"
+ "-[ADLocationManager currentLocationWithAccuracy:timeout:completion:]"
+ "-[ADLocationManager currentLocationWithAccuracy:timeout:completion:]_block_invoke"
+ "-[ADLocationManager drainAuthorizationRequestCompletionsWithPossibleError:]"
+ "-[ADLocationManager drainLocationFetchRequestsWithPossibleError:]"
+ "-[ADLocationManager drainRequestsWithErrorCode:clearLocationCache:dismissDialog:]_block_invoke"
+ "-[ADLocationManager endLocationUpdateSessionIfNeeded]"
+ "-[ADLocationManager fetchLocationAuthorization:]"
+ "-[ADLocationManager fetchLocationAuthorization:]_block_invoke_2"
+ "-[ADLocationManager forceLocationUpdateFromCoreLocation]"
+ "-[ADLocationManager locationForSnapshot]"
+ "-[ADLocationManager locationManager:didUpdateLocations:]_block_invoke"
+ "-[ADLocationManager locationManagerDidChangeAuthorization:]"
+ "-[ADLocationManager prefetchCurrentLocation]_block_invoke"
+ "-[ADLocationManager requestAuthorizationWithStyle:timeout:completion:]"
+ "-[ADLocationManager requestAuthorizationWithStyle:timeout:completion:]_block_invoke"
+ "-[ADLocationManager requestTemporaryAccuracyAuthorizationWithStyle:timeout:completion:]"
+ "-[ADLocationManager requestTemporaryAccuracyAuthorizationWithStyle:timeout:completion:]_block_invoke"
+ "-[ADLocationManager scheduleAuthorizationRequestTimeoutForCompletionBlock:timeout:]_block_invoke"
+ "-[ADLocationManager scheduleLocationUpdateSessionTeardown]"
+ "-[ADLocationManager scheduleLocationUpdateSessionTeardown]_block_invoke"
+ "-[ADLocationManager sendTemporaryAccuracyAuthorizationRequestWithTimeout:completion:]"
+ "-[ADLocationManager sendTemporaryAccuracyAuthorizationRequestWithTimeout:completion:]_block_invoke"
+ "-[ADLocationManager shiftLocation:completion:]"
+ "-[ADLocationManager shiftLocation:completion:]_block_invoke"
+ "-[ADLocationManager shiftLocationUsingCachedShifterFunction:]"
+ "-[ADLocationManager shiftLocationWithTimeout:timeoutHandler:completion:]"
+ "-[ADLocationManager shiftLocationWithTimeout:timeoutHandler:completion:]_block_invoke"
+ "-[ADLocationManager startLocationPrefetchRoutine]"
+ "-[ADLocationManager startLocationUpdateSession]"
+ "-[ADLocationManager updateAuthorizationStyleWithUserSelection:timeout:completion:]"
+ "-[ADLocationManager updateAuthorizationStyleWithUserSelection:timeout:completion:]_block_invoke"
+ "-[ADLocationManager updateTemporaryAuthorizationForAccurateLocation:timeout:completion:]"
+ "-[ADLocationManager updateTemporaryAuthorizationForAccurateLocation:timeout:completion:]_block_invoke"
+ "-[ADLocationManager upgradeAccuracyIfNeeded:]"
+ "-[ADPeerLocationRemote _getBestLocationWithCompletion:]_block_invoke_2"
+ "-[RPCompanionLinkDevice(AssistantAdditions) willUseProxyCommunicationWithLocalDevice:]"
+ "18"
+ "@40@0:8@16{ADLocationManagerState=Biq}24"
+ "ADLocationService"
+ "AFLocationFetchRequest"
+ "AFLocationServiceInterface"
+ "CLLocation"
+ "MobileAssistantDaemons-3306.26.2"
+ "T@\"ADLocationManager\",R,N,V_locationManager"
+ "T@\"CLLocation\",&,V_lastLocation"
+ "T@\"CLLocation\",&,V_lastShiftedLocation"
+ "T@\"CLLocation\",R"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_dispatchQueue"
+ "Td,N,V_desiredAccuracy"
+ "Vv24@0:8@?<v@?Qq>16"
+ "Vv36@0:8B16d20@?28"
+ "Vv36@0:8B16d20@?<v@?Qq@\"NSError\">28"
+ "Vv40@0:8Q16d24@?32"
+ "Vv40@0:8Q16d24@?<v@?Qq@\"NSError\">32"
+ "Vv40@0:8d16d24@?32"
+ "Vv40@0:8d16d24@?<v@?@\"CLLocation\"@\"NSError\">32"
+ "_authorizationRequestCompletions"
+ "_desiredAccuracy"
+ "_dismissTCCDialogIfNeeded"
+ "_generateResponseForGetRequestOriginCommand:withUnshiftedLocation:completion:"
+ "_getLocationAccessPermission"
+ "_isLocationManagerReady"
+ "_isSiriLocationServicesPromptingEnabled"
+ "_lastShiftedLocation"
+ "_lastShiftedLocationLock"
+ "_locationAccessPermission"
+ "_locationFetchRequests"
+ "_locationServiceListener"
+ "_locationServiceListenerShouldAcceptNewConnection:"
+ "_locationUpdateSessionStatus"
+ "_locationUpdateSessionTeardownTimer"
+ "_setupLocationService"
+ "_setupLocationServiceListener"
+ "_siriUserInterfaceIsVisible"
+ "ad_isNewerThan:"
+ "buildDailyDeviceStatusHeartbeatMetricsWithSiriEnabled:onLockscreen:dictationEnabled:voiceTriggerEnabled:starkHasBeenActiveWithin24Hours:raiseToSpeakEnabled:activeAppleAudioDevices:spokenNotificationsEnabled:announceNotificationsEnabledOnHeadphones:carplayAnnounceEnablementType:isAnnounceNotificationsMutedForCarPlay:shouldSkipTriggerlessReplyConfirmation:spokenNotificationsProxCardSeen:spokenNotificationsControlCenterModuleEnabled:spokenNotificationsWhitelistSettings:announceCallsEnabled:preciseLocationEnabled:locationAccessPermission:adaptiveSiriVolumeEnabled:adaptiveSiriVolumePermanentOffsetEnabled:adaptiveSiriVolumePermanentOffsetFactor:adaptiveSiriVolumeMostRecentIntent:isRemoteDarwinVoiceTriggerEnabled:autoSendSettings:siriInCallEnablementState:hangUpEnablementState:heartbeatQueuedTime:siriVoiceTriggerSettings:isShowAppsBehindSiriEnabledOnCarPlay:isSiriCapableDigitalCarKeyAvailable:connectedBTCarHeadunits:withCompletion:"
+ "cancelLocationUpdateSessionTeardown"
+ "createCurrentLocationSnapshot"
+ "createLocationInUseAssertion"
+ "currentAuthorizationStyle:"
+ "currentLocationWithAccuracy:timeout:completion:"
+ "dismissLocationServiceDialogIfNeeded"
+ "dismissTCCDialogIfNeeded"
+ "dismissTCCDialogIfNeeded:"
+ "dispatchQueue"
+ "drainAuthorizationRequestCompletionsWithPossibleError:"
+ "drainLocationFetchRequestsWithPossibleError:"
+ "drainLocationServiceRequestsForNewRequestAndClearLocationCache:dismissDialog:"
+ "drainRequestsWithErrorCode:clearLocationCache:dismissDialog:"
+ "endLocationUpdateSessionIfNeeded"
+ "forceLocationUpdateFromCoreLocation"
+ "generic"
+ "hasWatchOS"
+ "initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:referenceFrame:"
+ "initWithDispatchQueue:"
+ "initWithDispatchQueue:locationManager:isSiriLocationServicesPromptingEnabled:"
+ "initWithLatitude:longitude:altitude:direction:speed:verticalAccuracy:horizontalAccuracy:preciseLocationEnabled:accessState:"
+ "initWithLocation:locationManagerState:"
+ "isSiriLocationServicesPromptingEnabled"
+ "knownLocation"
+ "lastShiftedLocation"
+ "locationForSnapshot"
+ "locationManager"
+ "prefetchCurrentLocation"
+ "referenceFrame"
+ "requestAlwaysAuthorization"
+ "requestAuthorizationWithStyle:timeout:completion:"
+ "requestTemporaryAccuracyAuthorizationWithStyle:timeout:completion:"
+ "requestTemporaryFullAccuracyAuthorizationWithPurposeKey:completion:"
+ "requestWhenInUseAuthorization"
+ "scheduleAuthorizationRequestTimeoutForCompletionBlock:timeout:"
+ "scheduleLocationFetchRequestTimeoutForRequest:timeout:"
+ "scheduleLocationUpdateSessionTeardown"
+ "sendTemporaryAccuracyAuthorizationRequestWithTimeout:completion:"
+ "setAuthorizationStatusByType:forBundlePath:"
+ "setLastLocation:"
+ "setLastShiftedLocation:"
+ "setLocationAccessPermission:"
+ "setTemporaryAuthorizationGranted:forBundle:"
+ "setTemporaryFullAccuracyAuthorizationGranted:forBundlePath:"
+ "shiftLocation:completion:"
+ "shiftLocationUsingCachedShifterFunction:"
+ "shiftLocationWithTimeout:timeoutHandler:completion:"
+ "shouldEndLocationUpdateSession"
+ "startLocationPrefetchRoutine"
+ "startLocationUpdateSession"
+ "tearDownLocationAuthorizationPromptForBundlePath:"
+ "updateAuthorizationStyleWithUserSelection:completion:"
+ "updateAuthorizationStyleWithUserSelection:timeout:completion:"
+ "updateLocationSnapshot"
+ "updateTemporaryAuthorizationForAccurateLocation:completion:"
+ "updateTemporaryAuthorizationForAccurateLocation:timeout:completion:"
+ "upgradeAccuracyIfNeeded:"
+ "v184@0:8B16B20B24B28B32B36@40B48B52q56B64B68B72B76Q80B88B92i96B100B104@108@116B124@128i136i140Q144@152B160B164@168@?176"
+ "v24@0:8@?<v@?Qq>16"
+ "v24@?0@\"CLLocation\"8@\"NSError\"16"
+ "v32@0:8@?16d24"
+ "v32@0:8q16B24B28"
+ "v32@?0Q8q16@\"NSError\"24"
+ "v40@0:8d16d24@?32"
+ "v40@0:8d16d24@?<v@?@\"CLLocation\"@\"NSError\">32"
+ "willUseProxyCommunicationWithLocalDevice:"
+ "{ADLocationManagerState=\"locationServicesEnabled\"B\"authorizationStatus\"i\"accuracyAuthorization\"q}"
- "\x05\x11!!\x12\x11#"
- "\x0f\x01\x11\x12\x14\x11"
- "%s %@ %{private}@"
- "%s '%@' - already released UI assertion, nothing to do"
- "%s '%@' - releasing assertion once"
- "%s Acquiring location-in-use assertion for reason: %@"
- "%s Attempting to shift from location: %{private}@, forceCached: %@"
- "%s CLAuthorizationStatus changed %d isEnabled %@, preciseLocationEnabled %@"
- "%s Cached location shift failed"
- "%s Device found over iWifi."
- "%s Fetching authorization status"
- "%s Given a location, but no explicit location status -- assuming we are authorized to use locations"
- "%s Got authorization status = %d enabled = %d preciseLocationEnabled = %d"
- "%s Location Services Denied for Siri"
- "%s Location shifted"
- "%s No cached location available"
- "%s No location in speechRequestOptions %@"
- "%s No location information in request options %@"
- "%s Releasing location-in-use assertion for reason: %@"
- "%s Shifting location failed due to error: %@"
- "%s Stopping location monitoring"
- "%s Target Device has ProxyHost status flag. Return true if local device is HomePod and target device is Sidekick."
- "%s Unknown status %{public}@"
- "%s Updating with location %@"
- "%s Updating with status=%@ location %@"
- "%s Using cached authorization status = %d enabled = %d preciseLocationEnabled = %d"
- "%s acquiring location-in-use assertion"
- "%s creating location-in-use assertion"
- "%s isHomeHubDeviceLookingForItsHub: %@, isHubLookingForADeviceItIsHosting: %@, isDeviceDiscoveredOverInfraWifi: %@, shouldAllowAWDLFallback: %@, isAWDLFallbackForPersonalRequestsEnabled: %@"
- "%s isLocalDeviceAnAudioAccessory: %@, isTargetDeviceHomeHubDevice: %@"
- "%s nilling out reference to location-in-use assertion"
- "%s over-releasing location assertion due to: '%@'"
- "%s releasing location-in-use assertion"
- "-[ADCommandCenter(LocationInternal) _receivedLocation:locationStatus:]"
- "-[ADDailyDeviceStatusActivity buildDailyDeviceStatusHeartbeatMetricsWithSiriEnabled:onLockscreen:dictationEnabled:voiceTriggerEnabled:starkHasBeenActiveWithin24Hours:raiseToSpeakEnabled:activeAppleAudioDevices:spokenNotificationsEnabled:announceNotificationsEnabledOnHeadphones:carplayAnnounceEnablementType:isAnnounceNotificationsMutedForCarPlay:shouldSkipTriggerlessReplyConfirmation:spokenNotificationsProxCardSeen:spokenNotificationsControlCenterModuleEnabled:spokenNotificationsWhitelistSettings:announceCallsEnabled:preciseLocationEnabled:adaptiveSiriVolumeEnabled:adaptiveSiriVolumePermanentOffsetEnabled:adaptiveSiriVolumePermanentOffsetFactor:adaptiveSiriVolumeMostRecentIntent:isRemoteDarwinVoiceTriggerEnabled:autoSendSettings:siriInCallEnablementState:hangUpEnablementState:heartbeatQueuedTime:siriVoiceTriggerSettings:isShowAppsBehindSiriEnabledOnCarPlay:isSiriCapableDigitalCarKeyAvailable:connectedBTCarHeadunits:withCompletion:]"
- "-[ADDailyDeviceStatusActivity buildDailyDeviceStatusHeartbeatMetricsWithSiriEnabled:onLockscreen:dictationEnabled:voiceTriggerEnabled:starkHasBeenActiveWithin24Hours:raiseToSpeakEnabled:activeAppleAudioDevices:spokenNotificationsEnabled:announceNotificationsEnabledOnHeadphones:carplayAnnounceEnablementType:isAnnounceNotificationsMutedForCarPlay:shouldSkipTriggerlessReplyConfirmation:spokenNotificationsProxCardSeen:spokenNotificationsControlCenterModuleEnabled:spokenNotificationsWhitelistSettings:announceCallsEnabled:preciseLocationEnabled:adaptiveSiriVolumeEnabled:adaptiveSiriVolumePermanentOffsetEnabled:adaptiveSiriVolumePermanentOffsetFactor:adaptiveSiriVolumeMostRecentIntent:isRemoteDarwinVoiceTriggerEnabled:autoSendSettings:siriInCallEnablementState:hangUpEnablementState:heartbeatQueuedTime:siriVoiceTriggerSettings:isShowAppsBehindSiriEnabledOnCarPlay:isSiriCapableDigitalCarKeyAvailable:connectedBTCarHeadunits:withCompletion:]_block_invoke"
- "-[ADDeviceProperties _populateEventMetadataForClientEvent:withCompletion:]_block_invoke"
- "-[ADGeneralProperties _getStoreFrontIdWithCompletion:]_block_invoke"
- "-[ADLocationManager _acquireLocationInUseAssertionForReason:completion:]"
- "-[ADLocationManager _generateResponseForGetRequestOriginCommand:withUnshiftedLocation:forceCachedShifting:completion:]"
- "-[ADLocationManager _generateResponseForGetRequestOriginCommand:withUnshiftedLocation:forceCachedShifting:completion:]_block_invoke"
- "-[ADLocationManager _locationManagerDidChangeAuthorization:]"
- "-[ADLocationManager _locationManager]"
- "-[ADLocationManager _releaseLocationInUseAssertionForReason:]"
- "-[ADLocationManager _stopMonitoringLocation]"
- "-[ADLocationManager updateLocationSnapshotWithCompletion:]_block_invoke"
- "-[ADLocationManager updateLocationSnapshotWithCompletion:]_block_invoke_2"
- "-[ADLocationManager updateWithLocation:locationStatus:]"
- "-[ADLocationManager updateWithLocation:locationStatus:]_block_invoke"
- "-[ADPeerLocationRemote _getBestLocationWithCompletion:]_block_invoke_3"
- "-[ADiOSAssistantProperties _getActiveSubscriptionsWithCompletion:]_block_invoke"
- "-[ADiOSAssistantProperties _getIsSpokenNotificationsControlCenterModuleEnabledWithCompletion:]_block_invoke"
- "-[ADtvOSAssistantProperties _getActiveSubscriptionsWithCompletion:]_block_invoke"
- "34"
- "@\"CLInUseAssertion\""
- "@48@0:8{?=dd}16d32@40"
- "MobileAssistantDaemons-3305.24.1"
- "_accuracyAuthorization"
- "_acquireLocationInUseAssertionForReason:completion:"
- "_bestCachedLocation"
- "_generateResponseForGetRequestOriginCommand:withUnshiftedLocation:forceCachedShifting:completion:"
- "_haveHadLocationManagerAuthorizationDelegateCallback"
- "_haveLastAuthorizationAndEnabledValues"
- "_haveVisibleAssistantUI"
- "_lastLocationAuthorizationStatus"
- "_lastLocationServicesIsEnabled"
- "_lastPreciseLocationIsEnabled"
- "_locationAuthorization"
- "_locationInUseAssertionRefCount"
- "_locationManagerDidChangeAuthorization:"
- "_receivedLocation:locationStatus:"
- "_releaseLocationInUseAssertionForReason:"
- "_setAuthorizationStatusToAuthorizedAndEnabled"
- "_setLastLocation:"
- "_shiftedLocationForGeoCoordinate2D:accuracy:originalLocation:"
- "_stopMonitoringLocation"
- "acquireLocationInUseAssertionForReason:completion:"
- "authorizationStatusForBundle:"
- "buildDailyDeviceStatusHeartbeatMetricsWithSiriEnabled:onLockscreen:dictationEnabled:voiceTriggerEnabled:starkHasBeenActiveWithin24Hours:raiseToSpeakEnabled:activeAppleAudioDevices:spokenNotificationsEnabled:announceNotificationsEnabledOnHeadphones:carplayAnnounceEnablementType:isAnnounceNotificationsMutedForCarPlay:shouldSkipTriggerlessReplyConfirmation:spokenNotificationsProxCardSeen:spokenNotificationsControlCenterModuleEnabled:spokenNotificationsWhitelistSettings:announceCallsEnabled:preciseLocationEnabled:adaptiveSiriVolumeEnabled:adaptiveSiriVolumePermanentOffsetEnabled:adaptiveSiriVolumePermanentOffsetFactor:adaptiveSiriVolumeMostRecentIntent:isRemoteDarwinVoiceTriggerEnabled:autoSendSettings:siriInCallEnablementState:hangUpEnablementState:heartbeatQueuedTime:siriVoiceTriggerSettings:isShowAppsBehindSiriEnabledOnCarPlay:isSiriCapableDigitalCarKeyAvailable:connectedBTCarHeadunits:withCompletion:"
- "dictation audio recording failed"
- "dictation speech was recognized locally"
- "dictation speech was recognized remotely"
- "dictation structured result was returned"
- "dismissed UI per %@"
- "found best location on behalf of peer"
- "initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:"
- "initWithSetRequestOrigin:"
- "locationStatus"
- "looking up best location on behalf of peer"
- "recievedLocation:locationStatus:"
- "releaseLocationInUseAssertionForReason:"
- "stopLocationUpdates"
- "stopMonitoringSignificantLocationChanges"
- "updateWithLocation:locationStatus:"
- "v16@?0@\"AFLocationSnapshot\"8"
- "v180@0:8B16B20B24B28B32B36@40B48B52q56B64B68B72B76Q80B88B92B96B100@104@112B120@124i132i136Q140@148B156B160@164@?172"
- "voice search final result was returned"

```
