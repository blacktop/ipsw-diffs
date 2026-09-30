## terminusd

> `/usr/libexec/terminusd`

```diff

-  __TEXT.__text: 0x1f8a04
-  __TEXT.__auth_stubs: 0x3e90
-  __TEXT.__objc_stubs: 0x93a0
-  __TEXT.__objc_methlist: 0x5bdc
-  __TEXT.__const: 0x71c
+  __TEXT.__text: 0x1fc2a4
+  __TEXT.__auth_stubs: 0x3ef0
+  __TEXT.__objc_stubs: 0x94c0
+  __TEXT.__objc_methlist: 0x5c04
+  __TEXT.__const: 0x72c
   __TEXT.__swift5_typeref: 0x4ce
-  __TEXT.__cstring: 0x50cb9
-  __TEXT.__swift5_capture: 0x460
-  __TEXT.__objc_methtype: 0x443f
-  __TEXT.__oslogstring: 0x2d7e
+  __TEXT.__cstring: 0x5167c
+  __TEXT.__swift5_capture: 0x4a4
+  __TEXT.__objc_methtype: 0x44ab
+  __TEXT.__oslogstring: 0x2dee
   __TEXT.__constg_swiftt: 0x1f8
   __TEXT.__swift5_reflstr: 0x8b
   __TEXT.__swift5_fieldmd: 0xf0
   __TEXT.__objc_classname: 0x148e
-  __TEXT.__objc_methname: 0x136f5
+  __TEXT.__objc_methname: 0x138f5
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x18

   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift_as_cont: 0xdc
-  __TEXT.__gcc_except_tab: 0x61fc
-  __TEXT.__unwind_info: 0x3130
+  __TEXT.__gcc_except_tab: 0x61f4
+  __TEXT.__unwind_info: 0x3170
   __TEXT.__eh_frame: 0xe90
-  __DATA_CONST.__const: 0x4d08
-  __DATA_CONST.__cfstring: 0xdb80
+  __DATA_CONST.__const: 0x4e60
+  __DATA_CONST.__cfstring: 0xdf00
   __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1a0

   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x1f58
-  __DATA_CONST.__got: 0xda0
+  __DATA_CONST.__auth_got: 0x1f88
+  __DATA_CONST.__got: 0xef0
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA.__objc_const: 0x19ab8
-  __DATA.__objc_selrefs: 0x2ed0
-  __DATA.__objc_ivar: 0x1fb0
+  __DATA.__objc_const: 0x19c00
+  __DATA.__objc_selrefs: 0x2f10
+  __DATA.__objc_ivar: 0x1fd4
   __DATA.__objc_data: 0x3800
-  __DATA.__data: 0x1918
-  __DATA.__bss: 0xcb8
+  __DATA.__data: 0x1938
+  __DATA.__bss: 0xcd8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3992
-  Symbols:   1530
-  CStrings:  13450
+  Functions: 4019
+  Symbols:   1544
+  CStrings:  13558
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__common : content changed
Symbols:
+ _$s9WiFiAware10WAEndpointV19performanceForecastSDyAA17WAPerformanceModeOAA0gF0VGvg
+ _$s9WiFiAware17WAPerformanceModeOSHAAMc
+ _$s9WiFiAware17WAPerformanceModeOSQAAMc
+ _$s9WiFiAware21WAPerformanceForecastV14signalStrengthSdSgvg
+ _$s9WiFiAware21WAPerformanceForecastVMa
+ _CFUserNotificationCreate
+ _CFUserNotificationReceiveResponse
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _createStringFromNRQuickRelayPresence
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationAlternateButtonTitleKey
+ _kCFUserNotificationDefaultButtonTitleKey
+ _nrXPCKeyDevicePreferencesQuickRelayPresence
+ _xpc_event_publisher_fire_with_reply
- _$ss5NeverON
- _$ss5NeverOs5ErrorsWP
- _swift_willThrowTypedImpl
CStrings:
+ "%llu-%@"
+ "%s%.30s:%-4d %@ Wi-Fi Aware consecutive failure count: %lu -> %lu"
+ "%s%.30s:%-4d %@: Wi-Fi Aware suppressed; not setting up a NAN datapath"
+ "%s%.30s:%-4d %@: rejecting Wi-Fi Aware activate request since we are a multicast source; distribution will flow over Wi-Fi"
+ "%s%.30s:%-4d %@: rejecting Wi-Fi Aware probe request, we are a multicast source"
+ "%s%.30s:%-4d %@: sending a Wi-Fi Aware deactivate request"
+ "%s%.30s:%-4d Already pairing with device %@, ignoring discovery update"
+ "%s%.30s:%-4d Cancel Wi-Fi Aware Probing operation; RSSI: %f"
+ "%s%.30s:%-4d NRDTriggerTapToRadar: CFUserNotificationCreate failed: %d"
+ "%s%.30s:%-4d NRDTriggerTapToRadar: suppressed for %@ (rate-limited)"
+ "%s%.30s:%-4d Not accepting Wi-Fi Aware connection to %@: device is a multicast source"
+ "%s%.30s:%-4d Not establishing Wi-Fi Aware since it is not supported."
+ "%s%.30s:%-4d Not marking %@ as my distributee: reachable over wired"
+ "%s%.30s:%-4d Probed Wi-Fi Aware RSSI %f for %@"
+ "%s%.30s:%-4d Probing with %@ has succeeded, cancel Wi-Fi Aware"
+ "%s%.30s:%-4d Skipping Wi-Fi Aware bring-up with distributor: device is a multicast source"
+ "%s%.30s:%-4d Tearing down Wi-Fi Aware link with %@: device is a multicast source"
+ "%s%.30s:%-4d Waiting for the browser to cancel the operation, RSSI: %f"
+ "%s%.30s:%-4d Wi-Fi Aware probing succeeded with %@"
+ "%s%.30s:%-4d [XPC event: %@] receive XPC reply for %@ : %@"
+ "%s%.30s:%-4d setQuickRelayPresence: %@ -> %@"
+ "+[NRXPCEventManager postAppSvcListenEventForASName:]_block_invoke"
+ ", WA-probed"
+ "-[NRApplicationServiceManager processActiveServiceQueriesIfNeeded]_block_invoke_2"
+ "-[NRApplicationServiceManager processIncomingRemotePayloadRequestForDeviceID:requestOptions:]"
+ "-[NRApplicationServiceManager serviceDiscoveryClient:didRequestRemotePayloadForDevice:requestOptions:completion:]"
+ "-[NRBabelManager neighbourWiFiAwareDidDisconnect:errored:]"
+ "-[NRBabelManager releaseWiFiAwareDataPathWithDistributor]"
+ "-[NRBabelManager startWiFiAwareConnectionWithDistributee:probingOnly:]"
+ "-[NRBabelNeighbour setConsecutiveWiFiAwareFailures:]"
+ "-[NRBabelNeighbour startWiFiAwareConnectionProbingOnly:]"
+ "-[NRBabelNeighbour startWiFiAwareConnectionProbingOnly:]_block_invoke"
+ "-[NRDDeviceConductor requestRemotePayloadForASClient:requestOptions:]"
+ "-[NRDDeviceConductor setQuickRelayPresence:forConnection:]"
+ "-[NRDiscoveryClient addWiFiAwareDeviceEndpointWithDeviceID:instanceName:rssi:]"
+ "-[NRDiscoveryClient client:didProbeRSSI:forDeviceID:serviceName:]"
+ "-[NRLinkDirector setQuickRelayPresence:forConnection:nrUUID:]"
+ "212336"
+ "21:23:18"
+ "675393"
+ "914.0.14.502.2"
+ "@44@0:8Q16@24@32B40"
+ "Classification"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Description"
+ "Dismiss"
+ "File Radar"
+ "Jun 30 2026"
+ "Keywords"
+ "NRDTTRLastPromptTime"
+ "NRDTriggerTapToRadar"
+ "NRDTriggerTapToRadar_block_invoke_2"
+ "Not Applicable"
+ "Other Bug"
+ "Reproducibility"
+ "Title"
+ "URL"
+ "Wi-Fi Aware probe success"
+ "[%@] terminusd reported issues"
+ "_appSvcRequiresPriorityDonation"
+ "_consecutiveWiFiAwareFailures"
+ "_lastNeighbourProbedMyWaRSSITimestamp"
+ "_lastWaRSSIProbingTimestamp"
+ "_pendingRemotePayloadRequestOptions"
+ "_quickRelayPresence"
+ "_quickRelayPresenceConnectionID"
+ "_receivedRemotePayloadRequestOptions"
+ "_sdQueryQueue"
+ "_waProbingOnly"
+ "all"
+ "an error occurred in waiting state: %@"
+ "an unknown issue (type %u)"
+ "browserWithService:delegate:delegateQueue:probingOnly:"
+ "client:didProbeRSSI:forDeviceID:serviceName:"
+ "com.apple.terminusd.ttr"
+ "data stall"
+ "data stalled over %sOutput"
+ "defaultWorkspace"
+ "discovered Wi-Fi Aware endpoint for device %llu with RSSI %f"
+ "discovered endpoint has no realtime signalStrength forecast"
+ "got nil lastWaRSSIProbingTimestamp and non-nil lastWaRSSI for neighbour %@"
+ "neighbourWiFiAwareDidDisconnect:errored:"
+ "openURL:configuration:completionHandler:"
+ "probingOnly"
+ "produceRemotePayloadForScopes:requestOptions:completionHandler:"
+ "queryItemWithName:value:"
+ "requestRemotePayloadForASClient:requestOptions:"
+ "setIsCurrentRouteThroughPrimaryAssistDevice:"
+ "setQueryItems:"
+ "tap-to-radar://new"
+ "terminusd detected a %@. Tap 'File Radar' to capture a sysdiagnose."
+ "terminusd detected an issue"
+ "terminusd has detected a connectivity issue - %@ (type: %@)\n\nPlease attach a sysdiagnose taken near the time of this prompt."
+ "terminusd.ASM.SDQuery"
+ "timeIntervalSinceReferenceDate"
+ "v28@0:8@\"NRBabelNeighbour\"16B24"
+ "v32@0:8@\"NRApplicationServiceClient\"16@\"NSData\"24"
+ "v48@0:8@\"NRWiFiAwareClient\"16d24Q32@\"NSString\"40"
+ "v48@0:8@16d24Q32@40"
- "%s%.30s:%-4d Already pairing with device %@"
- "%s%.30s:%-4d Cancel Wi-Fi Aware Probing connection; RSSI: %f"
- "%s%.30s:%-4d Waiting for the browser to cancel the connection, RSSI: %f"
- "-[NRApplicationServiceManager processActiveServiceQueriesIfNeeded]_block_invoke"
- "-[NRApplicationServiceManager processIncomingRemotePayloadRequestForDeviceID:]"
- "-[NRApplicationServiceManager serviceDiscoveryClient:didRequestRemotePayloadForDevice:completion:]"
- "-[NRBabelManager neighbourWiFiAwareDidDisconnect:]"
- "-[NRBabelManager startWiFiAwareConnectionWithDistributee:]"
- "-[NRBabelNeighbour startWiFiAwareConnection]"
- "-[NRBabelNeighbour startWiFiAwareConnection]_block_invoke"
- "-[NRDDeviceConductor requestRemotePayloadForASClient:]"
- "19:49:34"
- "914.0.1.0.4"
- "Jun 18 2026"
- "_lastWaRSSITimestamp"
- "browserWithService:delegate:delegateQueue:"
- "got nil lastWaRSSITimestamp and non-nil lastWaRSSI for neighbour %@"
- "neighbourWiFiAwareDidDisconnect:"
- "produceRemotePayloadForScopes:completionHandler:"
- "requestRemotePayloadForASClient:"
- "v24@0:8@\"NRApplicationServiceClient\"16"

```
