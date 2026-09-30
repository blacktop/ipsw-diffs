## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-847.80.2.0.0
-  __TEXT.__text: 0xcb90c
-  __TEXT.__auth_stubs: 0x1660
-  __TEXT.__objc_stubs: 0xc5e0
-  __TEXT.__objc_methlist: 0x3eb4
-  __TEXT.__const: 0x300
-  __TEXT.__objc_methname: 0xf618
-  __TEXT.__oslogstring: 0xfa8e
-  __TEXT.__objc_classname: 0xc78
-  __TEXT.__objc_methtype: 0x29f0
-  __TEXT.__gcc_except_tab: 0x4394
-  __TEXT.__cstring: 0xc7b4
+868.100.2.0.0
+  __TEXT.__text: 0xc0bf0
+  __TEXT.__auth_stubs: 0x1630
+  __TEXT.__objc_stubs: 0xba40
+  __TEXT.__objc_methlist: 0x4c04
+  __TEXT.__const: 0x330
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x19b8
-  __DATA_CONST.__auth_got: 0xb40
-  __DATA_CONST.__got: 0x6c0
-  __DATA_CONST.__const: 0x22b8
-  __DATA_CONST.__cfstring: 0x7d00
-  __DATA_CONST.__objc_classlist: 0x2c0
-  __DATA_CONST.__objc_protolist: 0x100
+  __TEXT.__gcc_except_tab: 0x3ca0
+  __TEXT.__oslogstring: 0xed4d
+  __TEXT.__cstring: 0xc61f
+  __TEXT.__objc_methname: 0xe9b1
+  __TEXT.__objc_classname: 0xc28
+  __TEXT.__objc_methtype: 0x2714
+  __TEXT.__unwind_info: 0x1800
+  __DATA_CONST.__auth_got: 0xb28
+  __DATA_CONST.__got: 0x690
+  __DATA_CONST.__const: 0x2050
+  __DATA_CONST.__cfstring: 0x7b00
+  __DATA_CONST.__objc_classlist: 0x2b0
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x190
-  __DATA_CONST.__objc_intobj: 0x6a8
+  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_intobj: 0x618
   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xcb38
-  __DATA.__objc_selrefs: 0x3450
-  __DATA.__objc_ivar: 0x9b4
-  __DATA.__objc_data: 0x1b80
-  __DATA.__data: 0xc10
-  __DATA.__bss: 0x1b0
+  __DATA.__objc_const: 0xa918
+  __DATA.__objc_selrefs: 0x34d0
+  __DATA.__objc_ivar: 0x97c
+  __DATA.__objc_data: 0x1ae0
+  __DATA.__data: 0xb58
+  __DATA.__bss: 0x1b8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA7C7F4B-ED61-35A6-B839-BD8433F7B348
-  Functions: 2206
-  Symbols:   592
-  CStrings:  6970
+  UUID: 8DD194E9-65A5-3318-A451-BFBA8C856029
+  Functions: 2090
+  Symbols:   581
+  CStrings:  6687
 
Symbols:
+ _OBJC_CLASS_$_NENetworkAgentSessionFileHandle
+ _OBJC_CLASS_$_NWNetworkAgentSession
+ _nw_proxy_hop_set_use_pqtls
+ _nw_settings_get_pqtls_enabled
- _CLLocationCoordinate2DMake
- _OBJC_CLASS_$_NEAppProxyProvider
- _OBJC_CLASS_$_NEAppProxyTCPFlow
- _OBJC_CLASS_$_NENetworkAgentRegistrationFileHandle
- _OBJC_CLASS_$_NPAppProxyFlowBridge
- _OBJC_CLASS_$_NPLocation
- _OBJC_CLASS_$_NPUsageReport
- _OBJC_CLASS_$_NPWaldo
- _OBJC_CLASS_$_NSPAppRule
- _OBJC_CLASS_$_NSPManager
- _OBJC_METACLASS_$_NEAppProxyProvider
- _geohashToLatitudeLongitude
- _getSigningIdentifier
- _nw_path_create_default_evaluator
- _objc_setProperty_atomic_copy
CStrings:
+ "-[NSPConfigurationManager fetchPrivacyProxyConfigurationFile:eTag:accessToken:reason:completionHandler:]"
+ "-[NSPPrivacyProxyMultiHopFallbackNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopNextHopsArray:secondProxyHopNextHopsArray:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:firstProxyHopUsesX25519:secondProxyHopUsesX25519:firstProxyHopUsesPQTLS:secondProxyHopUsesPQTLS:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:shouldFailOpen:allowGeohash:geohashOverride:enableDNSFilteringHint:fallbackSupportsUDPProxying:configEpoch:]"
+ "-[NSPPrivacyProxyMultiHopNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopNextHopsArray:secondProxyHopNextHopsArray:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:firstProxyHopUsesX25519:secondProxyHopUsesX25519:firstProxyHopUsesPQTLS:secondProxyHopUsesPQTLS:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:allowGeohash:geohashOverride:enableDNSFilteringHint:preferredPathPatterns:alternateAgentUUIDs:fallbackProxyConfigHash:fallbackSupportsUDPProxying:configEpoch:]"
+ "-[NSPPrivacyProxyObliviousHopsFallbackNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:usesX25519:usesPQTLS:tokenAgentUUID:proxyHopUsesStandardToken:shouldFailOpen:obliviousConfig:obliviousPath:obliviousHTTPType:]"
+ "-[NSPPrivacyProxyObliviousHopsNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:usesX25519:usesPQTLS:tokenAgentUUID:proxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:obliviousConfig:obliviousPath:obliviousHTTPType:fallbackProxyConfigHash:]"
+ "-[NSPPrivacyProxyProxiedContentNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:firstProxyHopUsesPQTLS:secondProxyHopUsesPQTLS:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:resolvedAddresses:fallbackAgentUUID:fallbackProxyConfigHash:isPrivacyProxy:]"
+ "-[NSPPrivacyProxySingleHopFallbackNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:usesX25519:usesPQTLS:tokenAgentUUID:proxyHopUsesStandardToken:shouldFailOpen:configEpoch:]"
+ "-[NSPPrivacyProxySingleHopNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:usesX25519:usesPQTLS:tokenAgentUUID:proxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:fallbackProxyConfigHash:configEpoch:]"
+ "-[NSPPrivacyProxyTokenRegistration initWithAgentUUID:agentDescription:delegate:isRegistered:]"
+ "@\"NWNetworkAgentSession\""
+ "Algorithms"
+ "Configuration start and end dates are not valid"
+ "Failed to find a supported challenge, no key found in configuration for issuer name"
+ "Failed to find a supported challenge, tried to use system client but not entitled"
+ "Failed to register %@ proxy agent (%@) with hash %@"
+ "Failed to update %@ proxy agent (%@) with hash %@"
+ "Got request to fetch a new configuration from our configuration server"
+ "Handling a request for a copy of the current configuration"
+ "NSPServerErrorReason"
+ "NetworkServiceProxy Agents"
+ "No key found in configuration for issuer name"
+ "Not validating configuration signature due to internal CLI setting"
+ "Permission denied, not able to use system-configured token keys without entitlement"
+ "Received success indication from %s (%@) for %@ agent on interface %@"
+ "Received success indication from %s for \"%@\" agent"
+ "Received success indication from %s for content-specific %@ agent on interface %@"
+ "Received success indication from %s for content-specific %@ resolver agent on interface %@"
+ "Received success indication from %s for oblivious %@ agent on interface %@"
+ "Setting uses PQTLS on first hop!"
+ "Starting and not using configuration settings on disk due lack of config or signature"
+ "Token keys not validated by transparency checks"
+ "_agentSession"
+ "allHTTPHeaderFields"
+ "allowPQTLS"
+ "configServerHeaders"
+ "configuration server headers changed to %@"
+ "createConfigFetchURLWithPath"
+ "fetchNewConfigurationWithCompletionHandler:"
+ "https://mask-api.icloud.com/v4_5/fetchConfigFile"
+ "ignore configuration signature %d"
+ "ignoreSignature"
+ "initWithFileDescriptor:queue:"
+ "initWithNetworkAgentClass:session:"
+ "initWithNetworkAgentSession:name:"
+ "initWithQueue:"
+ "matchesMap:proxyArray:"
+ "mergeHTTPHeaders:headerOverrides:"
+ "overrideConfigServerPath"
+ "resetConfigurationInternalSettings:"
+ "saveInternalOptions:"
+ "setAllHTTPHeaderFields:"
+ "setConfigServerHeaders:"
+ "setIgnoreSignature:"
+ "setOverrideConfigServerPath:"
+ "user-configured server path changed to %@"
+ "usesPQTLS"
+ "usesX25519"
+ "v20@?0B8q12"
- "%@ forcePathChange called"
- "%@ looking for DNS network agent registration file handle with agent UUID %@"
- "%@ looking for bootstrap DNS network agent registration file handle with agent UUID %@"
- "%@ looking for resolver agent registration file handle with agent UUID %@"
- "%@ startProxyWithOptions"
- "%@ stopProxyWithReason"
- "%@ updating registered DNS network agent [%@]"
- "%@ updating registered bootstrap DNS network agent [%@]"
- "%@: Failed to resolve downloaded Waldo"
- "%@: Handling a usage report from %@"
- "%@: One sample probing finished with success: %d"
- "%@: Probing finished with success: %d"
- "%@: Refreshing Waldo because there are no edges or because the timestamp reported by the client (%u) is not equal to the current timestamp (%u)"
- "%@: failed to dup the DNS network agent registration file handle [%@], error: %s"
- "%@: failed to dup the bootstrap DNS network agent registration file handle [%@], error: %s"
- "%@: failed to dup the resolver agent registration file handle [%@], error: %s"
- "%@: failed to resolve new edge set"
- "%@: failed to set the registered DNS network agent [%@]"
- "%@: failed to set the registered bootstrap DNS network agent [%@]"
- "%@: failed to set the registered resolver agent [%@]"
- "%@: re-using existing DNS network agent registration file handle [%@]"
- "%@: re-using existing bootstrap DNS network agent registration file handle [%@]"
- "%@: re-using existing resolver agent registration file handle [%@]"
- "-[NSPConfigurationManager fetchPrivacyProxyConfigurationFile:interface:eTag:accessToken:reason:completionHandler:]"
- "-[NSPPrivacyProxyMultiHopFallbackNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopNextHopsArray:secondProxyHopNextHopsArray:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:firstProxyHopUsesX25519:secondProxyHopUsesX25519:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:shouldFailOpen:allowGeohash:geohashOverride:enableDNSFilteringHint:fallbackSupportsUDPProxying:configEpoch:]"
- "-[NSPPrivacyProxyMultiHopNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopNextHopsArray:secondProxyHopNextHopsArray:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:firstProxyHopUsesX25519:secondProxyHopUsesX25519:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:allowGeohash:geohashOverride:enableDNSFilteringHint:preferredPathPatterns:alternateAgentUUIDs:fallbackProxyConfigHash:fallbackSupportsUDPProxying:configEpoch:]"
- "-[NSPPrivacyProxyObliviousHopsFallbackNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:usesX25519:tokenAgentUUID:proxyHopUsesStandardToken:shouldFailOpen:obliviousConfig:obliviousPath:obliviousHTTPType:]"
- "-[NSPPrivacyProxyObliviousHopsNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:usesX25519:tokenAgentUUID:proxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:obliviousConfig:obliviousPath:obliviousHTTPType:fallbackProxyConfigHash:]"
- "-[NSPPrivacyProxyProxiedContentNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:resolvedAddresses:fallbackAgentUUID:fallbackProxyConfigHash:isPrivacyProxy:]"
- "-[NSPPrivacyProxySingleHopFallbackNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:usesX25519:tokenAgentUUID:proxyHopUsesStandardToken:shouldFailOpen:configEpoch:]"
- "-[NSPPrivacyProxySingleHopNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:usesX25519:tokenAgentUUID:proxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:fallbackProxyConfigHash:configEpoch:]"
- "-[NSPPrivacyProxyTokenRegistration initWithAgentUUID:agentDescription:delegate:]"
- "@\"NPWaldo\""
- "@\"NSDictionary\"40@0:8@\"NSString\"16@\"NSString\"24^@32"
- "@\"NSMutableString\""
- "@\"NSNumber\"24@0:8@\"NPWaldo\"16"
- "@\"NSObject<OS_nw_path_evaluator>\""
- "@\"NSPConfiguration\"16@0:8"
- "@\"NSPManager\""
- "@\"NWPath\"16@0:8"
- "@?16@0:8"
- "Adding new %@ app rule"
- "Adding new edge set %@"
- "App %@ does not have a location bundle path"
- "App Rule label is nil"
- "B20@0:8B16"
- "B28@0:8@16B24"
- "Bad probing reason %ld"
- "Cannot refresh Waldo"
- "Check Only: Location change (%f meters) exceeded tolerance (%@ meters)"
- "Checking if location services are enabled for %@ using bundle %@"
- "Current location is too old"
- "Current location might have moved substantially, should check location"
- "Current results for %@ have not yet expired"
- "Edge set \"%@\" does not exist"
- "Edge set identifier (%p) is nil"
- "Edge set identifier is nil"
- "Expiring cached location in %ld seconds at (%@)"
- "FAIL %@ %@\n"
- "Failed to convert a message to a dictionary"
- "Failed to decode the usage report: %@"
- "Failed to establish trust with edge set %@"
- "Failed to find an edge set for %@"
- "Failed to parse JSON data into a JSON object: %@"
- "Failed to remove edge set %@: %@"
- "Failed to sort edges with completionHandler, no waldoInfo"
- "Failed to sort edges with location, no waldoInfo"
- "Fetching Waldo"
- "Force"
- "Found existing proxy registration for %@"
- "Found existing proxy registration for %@ (%@)"
- "Got authorization status %d for bundle %@"
- "Got geohash %@ from the X-POI header"
- "Got response headers: %@"
- "Handling a usage report"
- "Handling establish trust for %@"
- "Handling fetch app rule for label %@"
- "Handling fetch configuration"
- "Handling fetch edge set for %@"
- "Handling request for current state for %@ %@"
- "Handling set app rule for %@"
- "Handling set edge set for %@"
- "Handling set test latency map %@"
- "Including location information in telemetry"
- "Last location check was %f seconds ago (interval is %@), should check location"
- "Last location check was %f seconds ago, do not check location"
- "Last valid location was timestamped %f seconds ago (threshold %@), exceeded TTL"
- "Last valid location was timestamped %f seconds ago (threshold %@), within TTL"
- "Location change (%f meters) exceeded tolerance (%@ meters), sorting edges by distance"
- "Location change (%f meters) is within tolerance (%@ meters), no need to re-sort edges"
- "Location change resulted in new view, closet edge is %@"
- "Location change resulted in same view, closet edge is %@"
- "Location expiration date passed, invalidate cached location"
- "Location expiration set, should check location"
- "Looking for existing proxy agent registration for %@"
- "Mapped connection endpoint %@ to edge %@"
- "Merging default with current edge set for %@"
- "Merging new edge with current edge set for %@"
- "Merging new settings into default %@ app rule"
- "Merging new settings into existing %@ app rule"
- "MessageResult"
- "MessageType"
- "Moved %f meters since last location"
- "NPWaldoDelegate"
- "NPWaldoLocationManager"
- "NSPManagerDelegate"
- "NSPServerAppLabel"
- "NSPServerAppRule"
- "NSPServerAppRules"
- "NSPServerEdgeSetIdentifier"
- "NSPServerEndpoint"
- "NSPServerTelemetryService"
- "NSPServerTelemetryURL"
- "NSPServerTestLatencyMap"
- "NSPServerUsageData"
- "NSPServerWaldoInfo"
- "NSPServerWaldoInfos"
- "Network last used %@, location expiration %@"
- "NetworkServiceProxyProvider"
- "No configuration, cannot refresh Waldo"
- "Not allowed to get current location"
- "Not including location information in telemetry"
- "Parsed JSON object is not a dictionary"
- "Received HTTP response code %ld for %@, not parsing JSON"
- "Received invalid message"
- "Removing %@ app rule"
- "Replacing %@ app rule with the default %@ app rule"
- "Request for %@ resulted in error: %@"
- "Request for %@ was cancelled"
- "RequestLog"
- "SUCCESS %@ %ld\n"
- "Starting Tuscany refresh"
- "T@\"CLLocation\",&,V_latestGeohashLocation"
- "T@\"CLLocation\",&,V_latestLocation"
- "T@\"NPWaldo\",W,V_waldoInfo"
- "T@?,C,V_locationCompletionHandler"
- "Td,R"
- "Tuscany refresh failed"
- "Tuscany refresh succeeded"
- "Valid current location %@"
- "Waldo is disabled, re-establishing trust"
- "Waldo refresh is already pending"
- "X-Modified"
- "X-POI"
- "_currentNetworkCharacteristics"
- "_defaultEvaluator"
- "_isWaldoRequestPending"
- "_latestGeohashLocation"
- "_locationCompletionHandler"
- "_manager"
- "_nwContext"
- "_nwContextIdlnessCheckTimer"
- "_requestLog"
- "_setupOnce"
- "_waldoInfo"
- "agentFlags"
- "appRules"
- "cachedLocation"
- "cancelProbes"
- "com.apple.networkserviceproxy.applyConfiguration"
- "com.apple.networkserviceproxy.establishTrust"
- "com.apple.networkserviceproxy.fetchHostsFiles"
- "com.apple.networkserviceproxy.refreshWaldo"
- "compareByDistance:"
- "config"
- "connection"
- "copyCurrentGeohash"
- "copyCurrentGeohashFromServer"
- "copyEdgeSelectionTelemetry"
- "copyStateForClient:withPeerEndpoint:outWaldoInfo:"
- "copyStateIncludeDistance:"
- "createConfigFetchURLWithPath:timestamp:"
- "currentNetworkInfo"
- "currentNetworkLastUsed"
- "currentPath"
- "dataTaskWithURL:completionHandler:"
- "defaultPath"
- "deferCommit"
- "dislocation"
- "distanceFromLocation:"
- "edgeContainingOnRamp:"
- "edgeSelection"
- "edgeSetIdentifier"
- "edgeSets"
- "edges"
- "edgesGeneration"
- "establishTrustWithCompletionHandler:"
- "establishTrustWithEdgeSetForIdentifier:completionHandler:"
- "evaluateEnableRatios"
- "exceededLocationTTL"
- "fetchAppRuleForLabel:completionHandler:"
- "fetchEdgeSetForIdentifier:completionHandler:"
- "fetchStateForClient:withPeerEndpoint:completionHandler:"
- "generation"
- "geohash"
- "getEdgeSetForAppRule:"
- "getEdgeSetForSigningIdentifier:"
- "handleAppMessage:completionHandler:"
- "handleNewFlow:"
- "handleNewLocation:"
- "handleUsageReport:"
- "handleUsageReport:fromClient:"
- "hasEdges"
- "hasNetworkPath"
- "ingestTestLatencyMap:local:completionHandler:"
- "initWithAppProxyFlow:nwContext:"
- "initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:"
- "initWithDictionary:"
- "initWithIdentifier:timestamp:fromDictionary:source:"
- "initWithLatitude:longitude:"
- "initWithLatitude:longtitude:timestamp:"
- "initWithNetworkAgentClass:"
- "initWithNetworkAgentRegistration:sessionType:configurationIdentifier:agentUUID:"
- "initWithNetworkAgentRegistration:sessionType:configurationIdentifier:agentUUID:name:"
- "initWithSigningIdentifier:fallbackReason:"
- "initWithTimestamp:fromDictionary:waldoSource:"
- "initWithWaldo:"
- "isValid"
- "keybag"
- "latestGeohashLocation"
- "latestLocation"
- "latitude"
- "link"
- "linkLatenciesAllSignatures:"
- "location"
- "locationBundlePath"
- "locationCheckInterval"
- "locationCheckTimestamp"
- "locationCompletionHandler"
- "locationExpiration"
- "locationManager"
- "locationTTL"
- "locationToleranceDistance"
- "longtitude"
- "matchSigningIdentifier"
- "matchesMap:"
- "merge:missingSettingsOnly:"
- "network context idleness check timer fired"
- "network context is idle, releasing shared network transaction"
- "peer"
- "privacyProxyURLSession"
- "probeSize"
- "propertyListWithData:options:format:error:"
- "refreshWaldoNowWithCompletionHandler:"
- "removeDayPassesFromKernel"
- "removeFromKeychain"
- "reportUsage message does not contain a usage report"
- "reportUsage:fromClient:"
- "requireTFO"
- "resolveWithCompletionHandler:"
- "saveToKeychain"
- "sessionType"
- "setAgentFlags:"
- "setAppRule:forLabel:completionHandler:"
- "setAppRules:"
- "setCachedLocation:"
- "setCurrentGeohash:"
- "setCurrentLatitude:longitude:timestamp:"
- "setCurrentNetworkCharacteristics:"
- "setDistance:"
- "setEdgeSet:forIdentifier:completionHandler:"
- "setEdgeSets:"
- "setEdges:"
- "setEdgesGeneration:"
- "setIndex:"
- "setKeybagGeneration:"
- "setLastFallbackReason:"
- "setLatestGeohashLocation:"
- "setLatestLocation:"
- "setLocationCheckTimestamp:"
- "setLocationCompletionHandler:"
- "setLocationExpiration:"
- "setLocationManager:"
- "setShouldSave:"
- "setTimestamp:"
- "setUsedEdgesGeneration:"
- "setWaldoInfo:"
- "sharedManager"
- "shouldCheckLocation"
- "sortEdgesByDistanceWithCompletionHandler:"
- "sortEdgesByDistanceWithNewLocation:checkOnly:"
- "sortedArrayUsingSelector:"
- "source"
- "startProxyWithOptions:completionHandler:"
- "stopProxyWithReason:completionHandler:"
- "stopWithCompletionHandler:"
- "stripWhitespace:"
- "surfaced_at"
- "tag"
- "teardownNetworkAgent"
- "telemetryService"
- "telemetryURL"
- "timestamp"
- "unarchivedObjectOfClass:fromData:error:"
- "useGeohashFromServer"
- "v16@?0@\"NSString\"8"
- "v16@?0B8B12"
- "v16@?0Q8"
- "v20@?0@\"NSError\"8B16"
- "v24@0:8@\"NPWaldo\"16"
- "v24@?0@\"NSURLResponse\"8@\"NSData\"16"
- "v28@0:8@\"NPWaldo\"16B24"
- "v32@0:8@\"NPUsageReport\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\">24"
- "v32@0:8q16@?24"
- "v36@?0B8@\"NSDictionary\"12@\"NSNumber\"20@\"NSString\"28"
- "v40@0:8@\"NPWaldo\"16@\"NSString\"24@?<v@?@\"NSString\">32"
- "v40@0:8@\"NSPAppRule\"16@\"NSString\"24@?<v@?@\"NSString\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSDictionary\"@\"NSString\"@\"NSURL\">32"
- "v40@0:8d16d24@32"
- "v64@0:8@\"NPWaldo\"16@\"NSURL\"24@\"NSDate\"32@\"NSURLSession\"40@?<v@?@\"NSURLResponse\"@\"NSData\">48@?<v@?@\"NSError\"B>56"
- "v64@0:8@16@24@32@40@?48@?56"
- "waldo:didFinishProbingWithSuccess:"
- "waldo:didFinishSampleProbingWithSuccess:"
- "waldo:fetchDayPassForURL:ifExpired:session:dataHandler:completionHandler:"
- "waldoDidSaveToKeychain:"
- "waldoGetCurrentConfiguration"
- "waldoInfo"
- "waldoNeedsPolicyReset"
- "waldoRequiresTFO:"
- "waldoTimestamp"

```
