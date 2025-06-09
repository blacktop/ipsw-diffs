## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-2063.120.19.0.0
-  __TEXT.__text: 0x96f48
-  __TEXT.__auth_stubs: 0x1af0
-  __TEXT.__objc_stubs: 0x7420
-  __TEXT.__objc_methlist: 0x3234
-  __TEXT.__const: 0x168
-  __TEXT.__gcc_except_tab: 0x1c98
-  __TEXT.__oslogstring: 0xbd24
-  __TEXT.__objc_methname: 0x8432
-  __TEXT.__cstring: 0x41c7
-  __TEXT.__objc_classname: 0x909
-  __TEXT.__objc_methtype: 0x1d49
-  __TEXT.__unwind_info: 0x12c0
-  __DATA_CONST.__auth_got: 0xd88
-  __DATA_CONST.__got: 0x6c0
+2167.0.0.0.2
+  __TEXT.__text: 0xaf0bc
+  __TEXT.__auth_stubs: 0x1c90
+  __TEXT.__objc_stubs: 0x7fa0
+  __TEXT.__objc_methlist: 0x3cfc
+  __TEXT.__const: 0x188
+  __TEXT.__gcc_except_tab: 0x2238
+  __TEXT.__objc_methname: 0x90ec
+  __TEXT.__oslogstring: 0xeb71
+  __TEXT.__cstring: 0x5121
+  __TEXT.__objc_classname: 0xba9
+  __TEXT.__objc_methtype: 0x207b
+  __TEXT.__unwind_info: 0x1618
+  __DATA_CONST.__auth_got: 0xe58
+  __DATA_CONST.__got: 0x788
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1a40
-  __DATA_CONST.__cfstring: 0x2240
-  __DATA_CONST.__objc_classlist: 0x1e8
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__const: 0x1d58
+  __DATA_CONST.__cfstring: 0x2700
+  __DATA_CONST.__objc_classlist: 0x270
+  __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x67b0
-  __DATA.__objc_selrefs: 0x2098
-  __DATA.__objc_ivar: 0x644
-  __DATA.__objc_data: 0x1310
-  __DATA.__data: 0xc18
-  __DATA.__bss: 0xf0
+  __DATA.__objc_const: 0x7fe8
+  __DATA.__objc_selrefs: 0x2388
+  __DATA.__objc_ivar: 0x77c
+  __DATA.__objc_data: 0x1860
+  __DATA.__data: 0xf80
+  __DATA.__bss: 0x130
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork
+  - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2ACABDD6-51E5-387A-81EF-42DA9F7C84A5
-  Functions: 1554
-  Symbols:   640
-  CStrings:  3721
+  UUID: 67B2CBA3-C776-3FED-A2A2-F7BA422B3EBD
+  Functions: 1863
+  Symbols:   683
+  CStrings:  4274
 
Symbols:
+ _OBJC_CLASS_$_CMLClientConfig
+ _OBJC_CLASS_$_CMLKeywordPIRClient
+ _OBJC_CLASS_$_CMLNetworkManager
+ _OBJC_CLASS_$_CMLUseCaseConfig
+ _OBJC_CLASS_$_CMLUseCaseGroup
+ _OBJC_CLASS_$_CMLUseCaseGroupManager
+ _OBJC_CLASS_$_CMLUseCaseStatus
+ _OBJC_CLASS_$_CWFInterface
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_NEBloomFilter
+ _OBJC_CLASS_$_NEHotspotAuthenticationProviderHost
+ _OBJC_CLASS_$_NEHotspotEvaluationProviderHost
+ _OBJC_CLASS_$_NEPvDConfiguration
+ _OBJC_CLASS_$_NEPvDFetcher
+ _OBJC_CLASS_$_NERelayConfiguration
+ _OBJC_CLASS_$_NEURLFilterControlProviderHost
+ _OBJC_CLASS_$_NEURLParser
+ _OBJC_METACLASS_$_NEBloomFilter
+ _chmod
+ _chown
+ _fstat
+ _mkdir
+ _mmap
+ _munmap
+ _nw_interface_get_name
+ _nw_interface_get_type
+ _nw_interface_shallow_compare
+ _nw_path_copy_interface
+ _nw_path_get_status
+ _nw_path_monitor_cancel
+ _nw_path_monitor_create
+ _nw_path_monitor_set_queue
+ _nw_path_monitor_set_update_handler
+ _nw_path_monitor_start
+ _nw_proxy_hop_set_allow_redirects
+ _open
+ _remove
+ _rename
+ _sandbox_check
+ _sandbox_extension_consume
+ _sandbox_extension_release
+ _xpc_array_get_count
+ _xpc_connection_create
+ _xpc_endpoint_create
- _OBJC_CLASS_$_LSBundleRecord
CStrings:
+ "%@ The device %s supervised"
+ "%@ Wi-Fi SSID match status changed from '%@' to '%@'"
+ "%@ adding policy %@"
+ "%@ configuration changed"
+ "%@ dealloc"
+ "%@ dealloced"
+ "%@ didInitializeWithUUIDs [%@]"
+ "%@ didStartWithPID, pid: [%d]"
+ "%@ disabling Wi-Fi WoW"
+ "%@ enabling Wi-Fi WoW"
+ "%@ failed to install hotspot provider policies"
+ "%@ handleAppsUninstalled"
+ "%@ handleAppsUpdateBegins"
+ "%@ handleAppsUpdateEnding"
+ "%@ handleAppsUpdateEnds"
+ "%@ handleCancel"
+ "%@ handleDisposeWithCompletionHandler"
+ "%@ handleExtensionExit"
+ "%@ handleInitWithCompletionHandler"
+ "%@ hotspot provider failed to start, error: %@"
+ "%@ hotspot provider failed to stop, error: %@"
+ "%@ hotspot provider started, session is active now"
+ "%@ hotspot session is already active, unable to process start message request"
+ "%@ hotspot session is not active, unable to process stop message request"
+ "%@ initialized hotspot session"
+ "%@ initializing plugin for hotspot authentication provider"
+ "%@ initializing plugin for hotspot evaluation provider"
+ "%@ installing hotspot provider policies for Wi-Fi interface: [%@] \t\t\t\tprovider machOUUIDs: %@ \t\t\t\tapp machOUUIDs: %@ \t\t\t\tSafari domains: %@"
+ "%@ installing policies for [%@]"
+ "%@ machOUUIDs For BundleIdentifier [%@]: %@"
+ "%@ machOUUIDsForBundleIdentifiers failed. error: %@"
+ "%@ network path monitor update handler received nil interface"
+ "%@ network path monitor update handler received path status over [%s] is [%@]"
+ "%@ network path over [%s] is not satisfied"
+ "%@ network path over [%s] is satisfied"
+ "%@ packet filtering is disabled and the packet filter provider is running, stopping the provider"
+ "%@ packet filtering is enabled but the packet filter provider is not running, starting the provider"
+ "%@ pluginDidAcknowledgeSleep"
+ "%@ private LTE network match status changed from '%@' to '%@'"
+ "%@ provider failed to start, error: %@"
+ "%@ provider sent a request to stop for ethernet"
+ "%@ received request to handle start message for hotspot session"
+ "%@ received request to handle stop message for hotspot session"
+ "%@ received request to stop provider for ethernet"
+ "%@ requesting install"
+ "%@ sending stop message to hotspot authentication provider"
+ "%@ sending stop message to hotspot evaluation provider"
+ "%@ successfully installed hotspot provider policies"
+ "%@ unable to create hotspot provider policies"
+ "%@ uninstalling policies for [%@]"
+ "%@%@"
+ "%@.%@"
+ "%@: %s"
+ "%@: %s - %@"
+ "%@: %s - Changed owner for mmap file for URL prefilter %@"
+ "%@: %s - Created temporary mmap file for bloom filter %@"
+ "%@: %s - Extension cancelWithError %@"
+ "%@: %s - Extension died unexpectedly"
+ "%@: %s - FOR TEST - Skip registration - (group <%@> use case <%@> PrivacyProxyFailOpen <%d> serverURL <%@>"
+ "%@: %s - Failed first fetch of pre-filter data"
+ "%@: %s - Failed to change mode for URL prefilter directory %s <errno %d - %s>"
+ "%@: %s - Failed to chown mmap file for URL prefilter %@ <errno %d - %s>"
+ "%@: %s - Failed to consume sandbox extension from provider: [%d] %s"
+ "%@: %s - Failed to create NEURLFilterProviderHost"
+ "%@: %s - Failed to create URL prefilter directory %s <errno %d - %s>"
+ "%@: %s - Failed to create mmap file for URL prefilter %@ <errno %d - %s>"
+ "%@: %s - Failed to get extension process identity"
+ "%@: %s - Failed to get file stats for file %s: [%d] %s"
+ "%@: %s - Failed to open file %s: [%d] %s"
+ "%@: %s - Failed to register for the %s notification"
+ "%@: %s - Failed to release sandbox extension from provider: [%d] %s"
+ "%@: %s - Failed to remove mmap file for URL prefilter %@ <errno %d - %s>"
+ "%@: %s - Failed to rename mmap file for URL prefilter %@ <errno %d - %s>"
+ "%@: %s - Failed to save first fetch of pre-filter data"
+ "%@: %s - Failed to set the state for the %s notification (status %d)"
+ "%@: %s - Failed to setup provider"
+ "%@: %s - Failed to start provider"
+ "%@: %s - Failed to update session with fetched pre-filter data"
+ "%@: %s - Failed to update session with first fetch of pre-filter data"
+ "%@: %s - Fetched null pre-filter data - skip"
+ "%@: %s - No read permission to file %s: [%d] %s"
+ "%@: %s - PIR cache reset completed <%s : %lu>"
+ "%@: %s - PIR cache reset failed <%@>"
+ "%@: %s - PIR refetch params completed <%s : %lu>"
+ "%@: %s - PIR refetch params failed <%@>"
+ "%@: %s - PIR status returned <%s : %lu>"
+ "%@: %s - PIR status returned error <%@>"
+ "%@: %s - PIR status returned nil status"
+ "%@: %s - Periodic Prefilter fetch <interval %d secs>"
+ "%@: %s - Received response - useCase: %@ for <%@>: result %@"
+ "%@: %s - Register with PIR Server (group <%@> use case <%@> PrivacyProxyFailOpen <%d> serverURL <%@> privacyPassIssuer <%@>"
+ "%@: %s - Removed mmap file for URL prefilter %@"
+ "%@: %s - URL Filter Provider has %s entitlement"
+ "%@: %s - URL Filter Provider is missing the required NetworkExtension entitlement"
+ "%@: %s - URL filter configuration invalid <%@>"
+ "%@: %s - Updated mmap file for URL prefilter %@"
+ "%@: %s - Validation failed"
+ "%@: %s - completed registration with PIR for Group %@ usecase %@"
+ "%@: %s - completed unregistration with PIR for Group %@"
+ "%@: %s - enter"
+ "%@: %s - enter %@"
+ "%@: %s - failed to register with PIR for Group %@ usecase %@"
+ "%@: %s - failed to unregister with PIR for Group %@"
+ "%@: %s - fetchPreFilterDataWithCompletion - data <%lu bytes>, file %@, sb_extension <%s>, numberOfBits %d, numberOfHashes  %d, murmurSeed %d, error %@"
+ "%@: %s - fetchPreFilterDataWithCompletion - data <%lu bytes>, file %@, sb_extension <%s>, numberOfBits %d, numberOfHashes %d, murmurSeed %d, error %@"
+ "%@: %s - fetchPreFilterDataWithCompletion - failed to save prefilter data to file"
+ "%@: %s - fetching URL Fitler PIR parameters"
+ "%@: %s - getPrefilter using mmap file %@"
+ "%@: %s - mmap failed for file %s: [%d] %s"
+ "%@: %s - nil connection"
+ "%@: %s - nil engine"
+ "%@: %s - pluginType %@ pluginClass %ld pluginInfo %@"
+ "%@: %s - read mmap <fd %d, size %lld> for file %s"
+ "%@: %s - removing mmap file for URL prefilter %@"
+ "%@: %s - request returned error: %@"
+ "%@: %s - request returned with wrong number of results: %@"
+ "%@: %s - resetting URL Fitler PIR cache"
+ "%@: %s - retrieve entitlement"
+ "%@: %s - savePrefilterData <%u bytes of data> bits %u hashes %u seed %u - using mmap file %@"
+ "%@: %s - setupWithCompletion result %d"
+ "%@: %s - sleepWithCompletion completed <result %d>"
+ "%@: %s - startWithCompletion result %d <%@>"
+ "%@: %s - stopWithReason result %d <%@>"
+ "%@: %s - updatePrefilterWithCompletionHandler - result %d"
+ "%@: %s - valid response data <%lu bytes>"
+ "%@: %s - wakeWithCompletion completed <result %d>"
+ "%@: %s: enter"
+ "%@: (authentication provider) stopWithReason result %d"
+ "%@: (evaluation provider) stopWithReason result %d"
+ "%@: <%@> Register URL Filter Session: %@"
+ "%@: Creating a url filter plugin with class %ld"
+ "%@: Deregister URL Filter Session: %@"
+ "%@: Failed to create a NEProcessIdentity object"
+ "%@: Failed to derive the process identity, no vendor connection available"
+ "%@: Failed to initialize the packet filter plugin"
+ "%@: Received a URL Filter fetch server params request from %@"
+ "%@: Received a URL Filter reset cache request from %@"
+ "%@: Register Hotspot Session: %@"
+ "%@: Rejecting un-entitled XPC client"
+ "%@: Validating"
+ "%@: creating a hotspot plugin with class %ld"
+ "%@: didProviderExit: disposing "
+ "%@: didReceiveProviderError: error: %@"
+ "%@: entitlement validation failed"
+ "%@: failed to create a NEProcessIdentity object"
+ "%@: failed to find the hotspot provider bundle identifier"
+ "%@: failed to find xpc connection with the hotspot provider"
+ "%@: failed to get extension process identity"
+ "%@: failed to setup hotspot authentication provider"
+ "%@: failed to setup hotspot evaluation provider"
+ "%@: failed to start hotspot authentication provider"
+ "%@: failed to start hotspot evaluation provider"
+ "%@: failed to start with error: %@"
+ "%@: failed to stop hotspot authentication provider"
+ "%@: failed to stop hotspot evaluation provider"
+ "%@: finding hotspot provider's entitlement"
+ "%@: found new hotspot providers %@"
+ "%@: getURLFilterClientConnection returns nil endpoint"
+ "%@: handleNewRequest - FINAL RESULT <failClosed> - request returned error: %@"
+ "%@: handleNewRequest - FINAL RESULT <failOpened> - request returned error: %@"
+ "%@: handleNewRequest - NOT A STRING"
+ "%@: handleNewRequest - failed to parse url"
+ "%@: handleNewRequest - no prefilter / filter setup yet"
+ "%@: handleNewRequest - no url"
+ "%@: hotspot provider cancelWithError %@"
+ "%@: hotspot provider died unexpectedly"
+ "%@: hotspot provider has [%s] entitlement"
+ "%@: hotspot provider is missing the required NetworkExtension entitlement"
+ "%@: plugin %@ disposed, requesting uninstall ..."
+ "%@: plugin %@ started with pid %d"
+ "%@: pluginType: [%@] pluginClass: [%ld] pluginInfo: [%@]"
+ "%@: received extension process identity"
+ "%@: received extension process identity (pid: %u)"
+ "%@: rejecting un-entitled hotspot provider"
+ "%@: setting up hotspot authentication provider"
+ "%@: setting up hotspot evaluation provider"
+ "%@: setupWithCompletion result %d"
+ "%@: sleepWithCompletion completed for hotspot authentication \t\t\t\t\t\t\tprovider, result: %s"
+ "%@: sleepWithCompletion completed for hotspot evaluation \t\t\t\t\t\t\tprovider, result: %s"
+ "%@: sleepWithCompletionHandler"
+ "%@: startProvider"
+ "%@: startWithCompletion, result: %s"
+ "%@: startWithConfiguration: %@"
+ "%@: stopWithReason, result: %s"
+ "%@: unable to derive the process identity, no hotspot provider xpc connection"
+ "%@: uninstalled"
+ "%@: uninstalling session"
+ "%@: updateConfiguration"
+ "%@: validating hotspot provider entitlement"
+ "%@: validation failed"
+ "%@: wakeWithCompletion completed, result %s"
+ "%@: wakeup"
+ "%@[%@][%d]"
+ "%@[%@][inactive]"
+ "%s: URLCHECK: FILTER: SENDING REQ - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FILTER: SENDING REQ - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: CACHED ALLOWED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: CACHED ALLOWED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: CACHED BLOCKED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: CACHED BLOCKED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: FILTER ALLOWED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: FILTER ALLOWED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: FILTER BLOCKED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: FILTER BLOCKED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: PREFILTER ALLOWED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: PREFILTER ALLOWED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: HANDLING URL CHECK REQ - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: HANDLING URL CHECK REQ - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: PREFILTER SUBURL CHECK: ALLOWED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: PREFILTER SUBURL CHECK: ALLOWED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: PREFILTER SUBURL CHECK: BLOCKED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: PREFILTER SUBURL CHECK: BLOCKED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ ")"
+ "-"
+ "-[NEAgentURLFilterExtension cancelWithError:]"
+ "-[NEAgentURLFilterExtension copyValueForEntitlement:]"
+ "-[NEAgentURLFilterExtension dealloc]"
+ "-[NEAgentURLFilterExtension extensionDidStop]"
+ "-[NEAgentURLFilterExtension fetchURLFilterServerParameters]_block_invoke"
+ "-[NEAgentURLFilterExtension getURLFilterClientConnectionWithCompletionHandler:completionHandler:]_block_invoke"
+ "-[NEAgentURLFilterExtension handleAppsUninstalled:]_block_invoke"
+ "-[NEAgentURLFilterExtension handleAppsUpdateBegins:]_block_invoke"
+ "-[NEAgentURLFilterExtension handleCancel]_block_invoke"
+ "-[NEAgentURLFilterExtension handleDisposeWithCompletionHandler:]"
+ "-[NEAgentURLFilterExtension handleXPCError]"
+ "-[NEAgentURLFilterExtension initWithPluginType:pluginClass:pluginInfo:queue:factory:]"
+ "-[NEAgentURLFilterExtension resetURLFilterCache]_block_invoke"
+ "-[NEAgentURLFilterExtension savePrefilterData:fileURL:sandboxExtension:numberOfBits:numberOfHashes:murmurSeed:]"
+ "-[NEAgentURLFilterExtension schedulePrefilterFetch]_block_invoke"
+ "-[NEAgentURLFilterExtension sleepWithCompletionHandler:]_block_invoke_2"
+ "-[NEAgentURLFilterExtension startURLFilter]_block_invoke"
+ "-[NEAgentURLFilterExtension startWithConfiguration:completionHandler:]"
+ "-[NEAgentURLFilterExtension startWithConfiguration:completionHandler:]_block_invoke"
+ "-[NEAgentURLFilterExtension updatePrefilterWithCompletionHandler:]"
+ "-[NEAgentURLFilterExtension validateExtension]"
+ "-[NEAgentURLFilterExtension wakeup]_block_invoke_2"
+ "-[NEPIRChecker check:sourceAppBundleId:responseQueue:redactSensitiveLogs:completionHandler:]"
+ "-[NEPIRChecker check:sourceAppBundleId:responseQueue:redactSensitiveLogs:completionHandler:]_block_invoke"
+ "-[NEPIRChecker fetchServerParameters]_block_invoke"
+ "-[NEPIRChecker resetPIRCache]_block_invoke"
+ "-[NEPIRChecker start:responseQueue:]"
+ "-[NEPIRChecker start:responseQueue:]_block_invoke"
+ "-[NEPIRChecker stop]"
+ "-[NESMURLFilterSession handleFetchServerParamsMessage:]"
+ "-[NESMURLFilterSession handleResetCacheMessage:]"
+ "-[NESMURLFilterSession pluginDidRequestUpdatePrefilter:]"
+ "-[NESMURLFilterSession postPrefilterChange]"
+ "-[NESMURLFilterSession prefilterCleanup]"
+ "-[NESMURLFilterSession prefilterSetup]"
+ "-[NESMURLFilterSession setState:]"
+ "-[NEURLFilterEngine acceptNewClientConnection:]"
+ "-[NEURLFilterEngine fetchConnectionWithCompletionHandler:]_block_invoke"
+ "-[NEURLFilterEngine fetchFilterServerParameters]_block_invoke"
+ "-[NEURLFilterEngine getPrefilter]_block_invoke"
+ "-[NEURLFilterEngine handleNewRequest:filloutReply:completionHandler:]"
+ "-[NEURLFilterEngine handleNewRequest:filloutReply:completionHandler:]_block_invoke"
+ "-[NEURLFilterEngine init]"
+ "-[NEURLFilterEngine resetCache]_block_invoke"
+ "-[NEURLFilterEngine startFilter]_block_invoke"
+ "-[NEURLFilterEngine stopFilter]_block_invoke"
+ "-[NEURLFilterPlugin acceptAgentClients]"
+ "-[NEURLFilterPlugin setStatus:error:]"
+ "-[NEURLFilterPlugin updatePrefilterWithCompletionHandler:]"
+ "/private/var/db/urlPrefilter"
+ "/private/var/db/urlPrefilter/com.apple.networkextension.url-prefilter-data."
+ "/private/var/db/urlPrefilter/com.apple.networkextension.url-prefilter-data.temp."
+ "<nil url>"
+ "@\"<NEMembershipChecker>\""
+ "@\"<NEPluginManagerObjectFactory>\""
+ "@\"NEHotspotAuthenticationProviderHost\""
+ "@\"NEHotspotEvaluationProviderHost\""
+ "@\"NEHotspotPlugin\""
+ "@\"NEPvDFetcher\""
+ "@\"NESMURLFilterSession\""
+ "@\"NESMURLFilterSessionState\""
+ "@\"NEURLFilterConfiguration\""
+ "@\"NEURLFilterControlProviderHost\""
+ "@\"NEURLFilterEngine\""
+ "@\"NEURLFilterPlugin\""
+ "@\"NSObject<OS_nw_interface>\""
+ "@\"NSObject<OS_nw_path_monitor>\""
+ "@\"NSXPCInterface\""
+ "ACTIVE"
+ "App for plugin type %@ has been uninstalled, stopping"
+ "B24@0:8@\"NEURLFilterPlugin\"16"
+ "B28@0:8@\"NSString\"16B24"
+ "B28@0:8@16B24"
+ "B32@0:8@\"NEURLFilterConfiguration\"16@\"NSObject<OS_dispatch_queue>\"24"
+ "Detected that the primary cellular interface changed: %@ => %@"
+ "Detected that the primary physical interface changed: %@ => %@"
+ "Detected that the primary wifi interface changed: %@ => %@"
+ "Extensions %@ has been updated, idling"
+ "Extensions %@ is being updated"
+ "Extensions %@ is being updated, stopping"
+ "FAIL"
+ "Failed to create a reply (%p) or a connection to send it over (%p) when sending the URL filter connection to the client"
+ "Failed to get a valid XPC endpoint from the URL filter plugin"
+ "Filter App updating - ignore extension failure/exit for %@"
+ "Filter extension exit timer expired for %@ - notify that extension failed"
+ "Generated relay config from PvD: %@"
+ "INACTIVE"
+ "NEAgentHotspotExtension"
+ "NEAgentURLFilterErrorDomain"
+ "NEAgentURLFilterExtension"
+ "NEBloomFilterChecker"
+ "NEExtensionBaseHostDelegate"
+ "NEHotspotPlugin"
+ "NEHotspotPluginDelegate"
+ "NEHotspotPluginDriver"
+ "NEHotspotPluginManager"
+ "NEMembershipChecker"
+ "NEMembershipCheckerErrorDomain"
+ "NEPIRChecker"
+ "NEPvDFetcherDelegate"
+ "NESMFilterSessionStateStartPacketPlugin"
+ "NESMFilterSessionStateStopPacketPlugin"
+ "NESMHotspotSession"
+ "NESMURLFilterSession"
+ "NESMURLFilterSession.m"
+ "NESMURLFilterSessionState"
+ "NESMURLFilterSessionStateIdle"
+ "NESMURLFilterSessionStateRunning"
+ "NESMURLFilterSessionStateStarting"
+ "NESMURLFilterSessionStateStopping"
+ "NESMURLFilterSessionStateUpdating"
+ "NEURLFilterEngine"
+ "NEURLFilterEngine queue"
+ "NEURLFilterPlugin"
+ "NEURLFilterPluginDelegate"
+ "NEURLFilterPluginDriver"
+ "NEURLFilterPluginManager"
+ "PID"
+ "Posted to %s"
+ "PvD configuration updated for relay %@"
+ "Received a request for a new URL filter connection from client pid %d"
+ "Reply dictionary is NULL when handling a source new request"
+ "T@\"NEURLFilterConfiguration\",&,N,V_urlConfiguration"
+ "URL"
+ "URL Filter Extension not initialized."
+ "URLPrefiltered"
+ "Updating policies due to PvD configuration change for %@"
+ "[wifiMatch: %s] [cellMatch: %s] [ethMatch: %s]"
+ "_appBundleIdentifier"
+ "_appsUpdateEnding"
+ "_appsUpdateStarted"
+ "_clientListener"
+ "_clientListenerEndpoint"
+ "_currentHotspotProviders"
+ "_currentPrimaryInterface"
+ "_evaluationPlugin"
+ "_extensionProcessIdentity"
+ "_extensionUUIDs"
+ "_filter"
+ "_host"
+ "_hostForAuthenticationProvider"
+ "_hostForEvaluationProvider"
+ "_hotspotPolicySession"
+ "_isEligibleForRuntime"
+ "_managerObjectFactory"
+ "_managerProtocol"
+ "_mmapFilename"
+ "_nwPathMonitor"
+ "_pendingConnections"
+ "_pendingDisposeCompletion"
+ "_pirCache"
+ "_pirGroupName"
+ "_pirPrivacyProxyFailOpen"
+ "_pirSkipRegistration"
+ "_pirUseCase"
+ "_prefilter"
+ "_prefilterFetchTimer"
+ "_prefilterFilePath"
+ "_prefilterTempFilePath"
+ "_pvdFetcher"
+ "_registered"
+ "_relayPvDConfig"
+ "_sendFailedTimer"
+ "_sessionrType"
+ "_urlConfiguration"
+ "_urlFilterEngine"
+ "_urlFilterSession"
+ "_urlfilterStatus"
+ "activate"
+ "alpn"
+ "app for plugin type [%@] has been uninstalled"
+ "app-proxy"
+ "app-push"
+ "appBundleIdentifier"
+ "auditToken"
+ "authenticationProviderBundleIdentifier"
+ "cancelWithError:"
+ "check:redactSensitiveLogs:"
+ "check:sourceAppBundleId:responseQueue:redactSensitiveLogs:completionHandler:"
+ "checkValidityAndCollectErrors:"
+ "cleanupExportedObject"
+ "com.apple.developer.wifi-aware"
+ "com.apple.mobilesafari"
+ "com.apple.nehelper.tracker-info-ready"
+ "com.apple.nesessionmanager.prefilter-ready"
+ "configUpdated:"
+ "configureGroupWithName:useCaseGroup:error:"
+ "connect-udp"
+ "contains:"
+ "content-filter"
+ "controlProviderBundleIdentifier"
+ "copySecIdentityRef"
+ "didProviderExit:"
+ "didReceiveUnmatchEthernet"
+ "didReceiveUnmatchEthernet:"
+ "disposing hotspot authentication provider"
+ "disposing hotspot evaluation provider"
+ "dns-proxy"
+ "entitlements"
+ "evaluationProviderBundleIdentifier"
+ "excludeDomains"
+ "excludeSubnets"
+ "extensible-sso"
+ "extensions %@ has been updated, idling"
+ "failed to load current configurations, error: %@"
+ "fetchConnectionWithCompletionHandler:"
+ "fetchFilterServerParameters"
+ "fetchPrefilterDataWithCompletion:"
+ "fetchServerParameters"
+ "fetchURLFilterServerParameters"
+ "file-read-data"
+ "file-read-metadata"
+ "get-task-allow"
+ "getExtensionConnection"
+ "getPrefilter"
+ "getURLFilterClientConnectionWithCompletionHandler:completionHandler:"
+ "handleFetchServerParamsMessage:"
+ "handleHotspotProviderError:"
+ "handleHotspotProviderStopped"
+ "handleResetCacheMessage:"
+ "handleXPCError"
+ "hotspot"
+ "hotspot provider software updating - ignore extension failure/exit for %@"
+ "hotspot-provider"
+ "hotspot-session-type"
+ "https-connect"
+ "identity"
+ "initFromFile:"
+ "initWithBase64EncodedString:options:"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithClientConfig:dispatchQueue:"
+ "initWithDelegate:queue:url:identityRef:"
+ "initWithKeyExpirationMinutes:keyRotationBeforeExpirationMinutes:useCases:networkConfig:"
+ "initWithPID:auditToken:"
+ "initWithString:"
+ "initWithType:endpoint:issuer:authenticationToken:privacyProxyFailOpen:"
+ "initWithType:maxShards:cacheElementCount:cacheEntryMinutesToLive:"
+ "initWithUseCase:sourceApplicationBundleIdentifier:"
+ "initialize:"
+ "initializing HostForAuthenticationProvider"
+ "initializing HostForEvaluationProvider"
+ "invalid"
+ "isDNSFailoverAllowed"
+ "legacy"
+ "loadConfigurationsWithCompletionQueue:handler:"
+ "machOUUIDsForBundleIdentifiers:error:"
+ "matchEthernet"
+ "matchSubnets"
+ "matchingStringsForURL:"
+ "mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:"
+ "objectForKey:ofClass:"
+ "packet-filter"
+ "packet-tunnel"
+ "pirAuthenticationToken"
+ "pirGroupName"
+ "pirPrivacyPassIssuerURL"
+ "pirPrivacyProxyFailOpen"
+ "pirServerURL"
+ "pirSkipRegistration"
+ "pirUseCase"
+ "pluginDidRequestUpdatePrefilter:"
+ "prefilterFetchInterval"
+ "present"
+ "processIdentifier"
+ "proxies"
+ "proxy"
+ "rawDictionary"
+ "received load notification for hotspot configuration"
+ "redactSensitiveLogs"
+ "refreshConfigForced:"
+ "removeObjectsInArray:"
+ "reportHotspotError:"
+ "requestDataByStringKeywords:completionHandler:"
+ "requestStatusForClientConfig:options:completionHandler:"
+ "resetCache"
+ "resetURLFilterCache"
+ "safariDomains"
+ "satisfiable"
+ "satisfied"
+ "separateDomainsFromFQDNs:domains:fqdns:"
+ "setAllowFailover:"
+ "setExcludedDomains:"
+ "setMatchFQDNs:"
+ "setUrlConfiguration:"
+ "setupWithCompletion:"
+ "sharedManager"
+ "shouldFailClosed"
+ "sleepWithCompletion:"
+ "start:responseQueue:"
+ "startAuthenticationProvider"
+ "startEvaluationProvider"
+ "startURLFilter"
+ "startWithCompletion:"
+ "starting hotspot authentication provider"
+ "starting hotspot evaluation provider"
+ "stop"
+ "stopFilter"
+ "stopWithReason:completion:"
+ "timeIntervalSinceReferenceDate"
+ "unmatchEthernet"
+ "unsatisfied"
+ "updatePrefilterWithCompletionHandler:"
+ "url-filter"
+ "url-filter-provider"
+ "url.filtering"
+ "urlConfiguration"
+ "urlFilter"
+ "v16@?0@\"NSObject<OS_nw_path>\"8"
+ "v24@0:8@\"NEHotspotPlugin\"16"
+ "v24@0:8@\"NEPvDConfiguration\"16"
+ "v24@0:8@\"NEURLFilterPlugin\"16"
+ "v24@?0@\"CMLUseCaseStatus\"8@\"NSError\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v32@0:8@\"NEHotspotPlugin\"16@\"NSError\"24"
+ "v32@?0@8Q16^B24"
+ "v40@0:8@\"NEURLFilterPlugin\"16q24q32"
+ "v52@0:8@\"NSArray\"16@\"NSString\"24@\"NSObject<OS_dispatch_queue>\"32B40@?<v@?B@\"NSError\">44"
+ "v52@0:8@16@24@32B40@?44"
+ "v52@?0@\"NSData\"8@\"NSURL\"16@\"NSString\"24I32I36I40@\"NSError\"44"
+ "valueForEntitlement:"
+ "verdict"
+ "wakeWithCompletion:"
- "%@ Wi-Fi SSID match status changed from '%@' to '%@' [ref count:%u]"
- "%@ applied scoping policy"
- "%@ configuration changed [ref count:%u]"
- "%@ failed to add policy for %@ [interface:%@]"
- "%@ failed to add policy: %@"
- "%@ failed to get MachO UUIDs for [%@]"
- "%@ failed to get bundle record for [%@], error: %@"
- "%@ failed to set the scoping policy"
- "%@ private LTE network match status changed from '%@' to '%@' [ref count:%u]"
- "%@ provider failed to start"
- "%@ removed scoping policies"
- "%@ requesting install for LTE match [ref count:%u]"
- "%@ requesting install for Wi-Fi match [ref count:%u]"
- "%@ setting up the scoping policies for [%@]:[%@]"
- "%@ successfully added policy: %@"
- "%@: startProvider (reference count [%d])"
- "%@[%d]"
- "%@[inactive]"
- "Changing primary cellular interface: %@ => %@"
- "Changing primary physical interface: %@ => %@"
- "Changing primary wifi interface: %@ => %@"
- "_refCount"
- "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
- "machOUUIDs"
- "v32@?0@\"NSUUID\"8Q16^B24"

```
