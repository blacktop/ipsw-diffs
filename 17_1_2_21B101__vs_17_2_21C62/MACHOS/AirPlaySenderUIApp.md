## AirPlaySenderUIApp

> `/Applications/AirPlaySenderUIApp.app/AirPlaySenderUIApp`

```diff

-745.13.4.0.0
-  __TEXT.__text: 0x958c
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0x1b20
-  __TEXT.__objc_methlist: 0x694
+750.14.1.4.0
+  __TEXT.__text: 0xaedc
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0x1e40
+  __TEXT.__objc_methlist: 0x704
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x18c
-  __TEXT.__cstring: 0x2be3
-  __TEXT.__objc_methname: 0x2b95
-  __TEXT.__objc_classname: 0x17e
-  __TEXT.__objc_methtype: 0xd5b
-  __TEXT.__unwind_info: 0x270
-  __DATA_CONST.__auth_got: 0x2e8
+  __TEXT.__gcc_except_tab: 0x1a0
+  __TEXT.__cstring: 0x34a7
+  __TEXT.__objc_methname: 0x2ef5
+  __TEXT.__objc_classname: 0x1a2
+  __TEXT.__objc_methtype: 0xe26
+  __TEXT.__unwind_info: 0x2b4
+  __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x500
-  __DATA_CONST.__cfstring: 0x8c0
+  __DATA_CONST.__const: 0x618
+  __DATA_CONST.__cfstring: 0x9e0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1b28
-  __DATA.__objc_selrefs: 0x7e0
-  __DATA.__objc_classrefs: 0x150
+  __DATA.__objc_const: 0x1d08
+  __DATA.__objc_selrefs: 0x8b0
+  __DATA.__objc_classrefs: 0x190
   __DATA.__objc_superrefs: 0x38
-  __DATA.__objc_ivar: 0x84
+  __DATA.__objc_ivar: 0x98
   __DATA.__objc_data: 0x370
-  __DATA.__data: 0x5b0
-  __DATA.__bss: 0x30
+  __DATA.__data: 0x670
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
+  - /System/Library/PrivateFrameworks/IntelligentRouting.framework/IntelligentRouting
   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
+  - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 173
-  Symbols:   155
-  CStrings:  768
+  Functions: 192
+  Symbols:   163
+  CStrings:  856
 
Symbols:
+ _NSErrorToOSStatus
+ _OBJC_CLASS_$_IRCandidate
+ _OBJC_CLASS_$_IRConfiguration
+ _OBJC_CLASS_$_IRMediaEvent
+ _OBJC_CLASS_$_IRNode
+ _OBJC_CLASS_$_IRServiceToken
+ _OBJC_CLASS_$_IRSession
+ _OBJC_CLASS_$_IRSessionSpotOnLocationParameters
+ _OBJC_CLASS_$_NSUserDefaults
+ _SFLocalizableWAPIStringKeyForKey
- _OBJC_CLASS_$_UIDevice
- _objc_retain_x27
CStrings:
+ "\x02\x16"
+ "\x06"
+ "+[APUIRouteManager serviceToken]"
+ "-[APUIBrokerHelper _handleAuthenticationResponse:requestUUID:error:completion:]"
+ "-[APUIBrokerHelper _handleBrokerResponse:]"
+ "-[APUIBrokerHelper _handleGetInfoResponse:requestUUID:error:completion:]"
+ "-[APUIBrokerHelper _sendBrokerRequest:params:completion:]_block_invoke"
+ "-[APUIBrokerHelper init]"
+ "-[APUIRouteManager _pickRouteWithID:authString:useRemoteControl:completion:]_block_invoke_2"
+ "-[APUIRouteManager _pickRouteWithID:authString:useRemoteControl:completion:]_block_invoke_3"
+ "-[APUIRouteManager session:didSpotOnLocationComplete:]"
+ "-[APUIRouteManager startIntelligentRoutingLocationSensing]"
+ "-[APUIRouteManager startIntelligentRoutingLocationSensing]_block_invoke"
+ "-[APUISetupViewController _getSupportedNetworks:withSetupPayload:completion:]_block_invoke"
+ "-[APUISetupViewController _presentAirPlayConnectionProxCardWithSetupPayload:]_block_invoke_2"
+ "@\"APUIRouteManager\""
+ "@\"IRSession\""
+ "@\"NSDictionary\""
+ "@\"NSError\""
+ "APUIBrokerHelper"
+ "APUIBrokerHelper [%{ptr}] created."
+ "APUIBrokerHelper.notification"
+ "APUIBrokerHelper.queue"
+ "APUIBrokerHelperRequestContext"
+ "APUIRouteManager [%{ptr}] failed to get IRServiceToken."
+ "APUIRouteManager failed to get the IRServiceToken data from defaults."
+ "APUIRouteManager failed to unarchive the IRServiceToken with token data %@."
+ "APUIRouteManager.intelligentRouting"
+ "AirPlaySenderUI_WiFi"
+ "Authenticate"
+ "BrokerAuthString"
+ "BrokerGroupInfo"
+ "BrokerRequest"
+ "BrokerResponse"
+ "BrokeredDiscoveryRouteSuggestionSupport"
+ "GetInfo"
+ "IRServiceToken"
+ "IRSessionDelegate"
+ "IRSessionSpotOnLocationDelegate"
+ "IsDiscoveredWithBroker"
+ "RequestType"
+ "RequestUUID"
+ "Status"
+ "T@\"NSDictionary\",&,N,V_response"
+ "Ti,N,V_status"
+ "[%{ptr}] %s IRSession [%{ptr}] with IRServiceToken [%{ptr}]."
+ "[%{ptr}] Auth response - request %'@ succeeded with authTargetReceiverDeviceID %@\n"
+ "[%{ptr}] Broker response - no command specified\n"
+ "[%{ptr}] Broker response - no request UUID specified\n"
+ "[%{ptr}] Disabling discovery pre-warm session [%{ptr}]"
+ "[%{ptr}] Discovery broker request %@ failed with error: %#m"
+ "[%{ptr}] Failed to get brokerGroupInfo with error: %@"
+ "[%{ptr}] GetInfo response - request %'@ succeeded with brokerGroupInfo %@\n"
+ "[%{ptr}] Giving up waiting for %'@ request %@ response after %d secs"
+ "[%{ptr}] Handling discovery broker GetInfo %'@ response error: %{error} %@"
+ "[%{ptr}] Handling discovery broker authentication %'@ response error: %{error} %@"
+ "[%{ptr}] Handling discovery broker response %@"
+ "[%{ptr}] IRSession [%{ptr}] %s setSpotOnLocationWithParameters callback with error=%{error}."
+ "[%{ptr}] IRSession [%{ptr}] setSpotOnLocation completed with %{error}"
+ "[%{ptr}] IRSession [%{ptr}] setting spotOnLocation"
+ "[%{ptr}] IRSession [%{ptr}]: Adding event %@ for candidate %@"
+ "[%{ptr}] IRSession [%{ptr}]: Updating %d candidates"
+ "[%{ptr}] Sending discovery broker %'@ command %@%?{end} with param %@"
+ "[%{ptr}] Sent %'@ request: %#m"
+ "[%{ptr}] Starting discovery pre-warm for %ds with session [%{ptr}]"
+ "[%{ptr}] Stopping discovery pre-warm with session [%{ptr}]"
+ "[%{ptr}] Successfully obtained brokerGroupInfo: %@"
+ "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: Multiple network feature is enabled. Current network (%@) is not supported and is not the same network in payload, try to connect to WiFi."
+ "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: Multiple network feature is enabled. Current network (%@) is supported, try broker authentication."
+ "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: Multiple network feature is not enabled. Current network (%@) is not the same as network in payload, try to connect to WiFi"
+ "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: Multiple network feature is not enabled. Current network (%@) is the same as network in payload, try broker authentication"
+ "_getSupportedNetworks:withSetupPayload:completion:"
+ "_handleAuthenticationResponse:requestUUID:error:completion:"
+ "_handleBrokerResponse:"
+ "_handleGetInfoResponse:requestUUID:error:completion:"
+ "_irQueue"
+ "_irSession"
+ "_localizedSystemWiFiString"
+ "_response"
+ "_routeManager"
+ "_sendBrokerRequest:params:completion:"
+ "_spotOnLocationError"
+ "_spotOnLocationSemaphore"
+ "_status"
+ "addEvent:forCandidate:"
+ "airPlayProperties"
+ "allKeys"
+ "com.apple.mediaremote"
+ "containsObject:"
+ "created"
+ "dataForKey:"
+ "failed to create"
+ "getBrokerGroupInfo:completion:"
+ "initWithCandidateIdentifier:"
+ "initWithEventType:eventSubType:"
+ "initWithServiceToken:"
+ "initWithSuiteName:"
+ "isMultipleWifiFeatureEnabled"
+ "lengthOfBytesUsingEncoding:"
+ "mutableCopy"
+ "received"
+ "response"
+ "runWithConfiguration:"
+ "serviceToken"
+ "session:didFailWithError:"
+ "session:didSpotOnLocationComplete:"
+ "session:didUpdateContext:"
+ "session:suspendedWithReason:"
+ "session:suspensionReasonEnded:isNoLongerSuspended:"
+ "setAvOutpuDeviceIdentifier:"
+ "setDelegate:"
+ "setMode:"
+ "setPublicAirPlayNetwork:"
+ "setResetAllBrokerDiscoveredCandidates:"
+ "setResponse:"
+ "setSpotOnLocationWithParameters:"
+ "setStatus:"
+ "startIntelligentRoutingLocationSensing"
+ "supportedWiFiNetworkSSIDs"
+ "timed out waiting for"
+ "updateCandidates:"
+ "updateNodes:"
+ "v12@?0B8"
+ "v24@?0@\"NSError\"8@\"NSDictionary\"16"
+ "v32@0:8@\"IRSession\"16@\"NSDictionary\"24"
+ "v32@0:8@\"IRSession\"16@\"NSError\"24"
+ "v32@0:8@\"IRSession\"16q24"
+ "v32@?0@\"NSString\"8@\"NSError\"16@\"NSDictionary\"24"
+ "v36@0:8@\"IRSession\"16q24B32"
+ "v36@0:8@16q24B32"
+ "void _HandleBrokerServiceResponse(CFStringRef, CFDictionaryRef)"
- "\x01\x16"
- "\x02"
- "-[APUIBrokerAuthenticator handleAuthenticationResponse:]"
- "-[APUIBrokerAuthenticator init]"
- "-[APUIBrokerAuthenticator performBrokerAuthenticationForBrokerGroup:withBrokerAuth:completion:]_block_invoke"
- "0"
- "APUIBrokerAuthenticator"
- "APUIBrokerAuthenticator [%{ptr}] created."
- "APUIBrokerAuthenticator.notification"
- "APUIBrokerAuthenticator.queue"
- "APUIBrokerAuthenticatorRequestContext"
- "AuthError"
- "AuthRequestID"
- "AuthResponseReceived"
- "AuthString"
- "AuthenticateDiscoveryBroker"
- "T@\"NSString\",C,N,V_authTargetReceiverDeviceID"
- "Ti,N,V_authError"
- "[%{ptr}] - Discovery broker authentication request %@ failed with error: %#m"
- "[%{ptr}] - Discovery broker authentication response %@"
- "[%{ptr}] - Giving up waiting for auth request %@ response after %d secs"
- "[%{ptr}] - Sent auth command: %#m"
- "[%{ptr}] - Start discovery broker authentication request %@"
- "[%{ptr}] Auth response - no request UUID specified\n"
- "[%{ptr}] Auth response - request %@ failed with error: %#m\n"
- "[%{ptr}] Auth response - request %@ succeeded with authTargetReceiverDeviceID %@\n"
- "[%{ptr}] Auth response - request %@ succeeded, but no authTargetReceiverDeviceID specified\n"
- "[%{ptr}] Starting discovery pre-warm for %ds"
- "[%{ptr}] Stopping discovery pre-warm"
- "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: current network (%@) is not the same as network in payload, try to connect to WiFi"
- "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: current network (%@) is the same as network in payload, try broker authentication"
- "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: proactively try broker authentication on current network (%@)"
- "_authError"
- "_authTargetReceiverDeviceID"
- "authError"
- "authTargetReceiverDeviceID"
- "currentDevice"
- "handleAuthenticationResponse:"
- "localizedModel"
- "setAuthError:"
- "setAuthTargetReceiverDeviceID:"
- "setBlueAtlasNetwork:"
- "void _handleAuthResponse(CFStringRef, CFDictionaryRef)"

```
