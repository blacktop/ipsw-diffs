## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-921.120.3.0.0
-  __TEXT.__text: 0xc30cc
-  __TEXT.__auth_stubs: 0x1870
-  __TEXT.__objc_stubs: 0xc540
-  __TEXT.__objc_methlist: 0x4e74
-  __TEXT.__const: 0x275
+964.0.0.502.1
+  __TEXT.__text: 0xbcc30
+  __TEXT.__auth_stubs: 0x1970
+  __TEXT.__objc_stubs: 0xcc20
+  __TEXT.__objc_methlist: 0x501c
+  __TEXT.__const: 0x285
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x3f08
-  __TEXT.__oslogstring: 0x10a42
-  __TEXT.__cstring: 0xd4a2
-  __TEXT.__objc_methname: 0xf974
-  __TEXT.__objc_classname: 0xc81
-  __TEXT.__objc_methtype: 0x2a19
-  __TEXT.__unwind_info: 0x1ab0
-  __DATA_CONST.__auth_got: 0xc48
-  __DATA_CONST.__got: 0x6e8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x20e8
-  __DATA_CONST.__cfstring: 0x8300
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __TEXT.__gcc_except_tab: 0x35a4
+  __TEXT.__oslogstring: 0x110f2
+  __TEXT.__cstring: 0xdcf2
+  __TEXT.__objc_methname: 0xff49
+  __TEXT.__objc_classname: 0xc2e
+  __TEXT.__objc_methtype: 0x2a75
+  __TEXT.__unwind_info: 0x1970
+  __DATA_CONST.__const: 0x22b0
+  __DATA_CONST.__cfstring: 0x8b00
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x188
-  __DATA_CONST.__objc_arraydata: 0xe8
-  __DATA_CONST.__objc_arrayobj: 0xf0
-  __DATA_CONST.__objc_intobj: 0x678
+  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_arrayobj: 0x108
+  __DATA_CONST.__objc_intobj: 0x6a8
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xaee8
-  __DATA.__objc_selrefs: 0x37e8
-  __DATA.__objc_ivar: 0x9e4
-  __DATA.__objc_data: 0x1bd0
+  __DATA_CONST.__auth_got: 0xcc8
+  __DATA_CONST.__got: 0x708
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0xb0a0
+  __DATA.__objc_selrefs: 0x39b0
+  __DATA.__objc_ivar: 0x9e8
+  __DATA.__objc_data: 0x1c70
   __DATA.__data: 0xb48
-  __DATA.__bss: 0x1f0
+  __DATA.__bss: 0x220
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0DDA454E-6CEC-3B5F-A45D-C3FD2FEA6BAD
-  Functions: 2102
-  Symbols:   627
-  CStrings:  7134
+  UUID: 27AAEAB4-17AB-37F6-B493-169EBD48A350
+  Functions: 2152
+  Symbols:   647
+  CStrings:  7376
 
Symbols:
+ _CFUserNotificationReceiveResponse
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSProcessInfo
+ __xpc_type_data
+ _arc4random
+ _dispatch_queue_create
+ _getppid
+ _kCFBundleVersionKey
+ _mach_task_self_
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_retain_x9
+ _task_info
+ _uname
+ _xpc_copy
+ _xpc_data_get_bytes_ptr
+ _xpc_data_get_length
CStrings:
+ "\n\n--- System Information ---\n"
+ "%.2f MB"
+ "%@ NetworkServiceProxy/%@"
+ "%@ added control-level proxied content policy %u"
+ "%@ adding control-level proxied content policy %@"
+ "%@ could not deserialize distnoted.matching.trusted UserInfo: %@"
+ "%@ failed to add control-level proxied content policy"
+ "%@ re-fetching configuration on applicable feature set change"
+ "%ld"
+ ", "
+ "-[NSPPrivacyTokenManager checkQuotaInnerForIssuerName:quotaService:auditToken:bundleID:accessToken:completionHandler:]"
+ "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:configurationFetchDate:configurationETag:validateTransparency:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:useOneTimeTokenBatchSize:accessToken:completionHandler:]"
+ "-[NSPPrivateAccessTokenFetcher fetchDeviceQuotaConfigurationWithQueue:completionHandler:]"
+ ".icloud.com"
+ "1737442"
+ "<no-incident-identifier>"
+ "Already evaluated incident %@, skipping"
+ "App \"%@\" is installed for feature %@"
+ "Applicable features changed to %@"
+ "B32@0:8@16^@24"
+ "Checking quota for %@"
+ "Classification"
+ "Cleaned up %lu old TTR incidents"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Configuration disk version changed, forcing a configuration fetch"
+ "Configuration feature set changed"
+ "Configuration refresh for applicable feature set change activity finished with result %@"
+ "Created TTR pop up for incident \"%@\""
+ "Deferring to untrusted handler, as restricted_distributed_notifications feature flag is off"
+ "DeleteOnDetach"
+ "Description"
+ "Dismiss"
+ "Exception while decoding TTR incidents: %@"
+ "Exception while encoding TTR incidents: %@"
+ "Failed to create TTR URL for incident \"%@\""
+ "Failed to create TTR pop up for incident \"%@\": %d"
+ "Failed to decode TTR incidents from preferences"
+ "Failed to fetch device quota configuration: %@"
+ "Failed to generate radar URL for TTR for titleSuffix: %@"
+ "Failed to get incident identifier, cannot simulate TTR"
+ "Failed to serialize diagnostic data to JSON: %@"
+ "Failed to synchronize TTR incidents to preferences"
+ "Failed to write diagnostic file: %@"
+ "Found TTR header in response: %@ (sample %@)"
+ "Found invalid TTR incident with key: %@"
+ "HTTP/1.1"
+ "Ignoring proxy match dictionary, not applicable for seed"
+ "IncludeDevicePrefixInTitle"
+ "Initialized incidents dictionary"
+ "LaunchServices"
+ "Machine: %@\n"
+ "Memory Usage: %@\n"
+ "Missing incident identifier"
+ "NSKeyedArchiver initialize failed for TTR incidents"
+ "NSKeyedUnarchiver initialize failed for TTR incidents"
+ "NSPServerQuotaConfig"
+ "NSPServerTTRIncident"
+ "NSPServerTTRProbability"
+ "NSPTapToRadarIncident"
+ "NSPTapToRadarIncidents"
+ "NSPTapToRadarUtility"
+ "No TTR header present"
+ "No TTR incidents found in preferences"
+ "No access token received for \"%@\", status %u"
+ "No app is installed for feature %@"
+ "No radar configuration found for TTR for key: %@"
+ "Not refetching configuration, new features are a subset of previous (%@)"
+ "Not selected for TTR incident \"%@\""
+ "OS: %@ %@\n"
+ "Open Tap-to-Radar"
+ "Opened TTR for incident \"%@\""
+ "Prewarming Private Access Token cache"
+ "Privacy Proxy Config"
+ "Privacy Proxy server automated TTR for incident: "
+ "Process: %@\n"
+ "Received access token for \"%@\", can use %u"
+ "Received device quota config (%zu bytes)"
+ "Received error %@ while looking up access tokenfor \"%@\", can use %u"
+ "Recorded incident: %@"
+ "Removed %lu invalid TTR incidents"
+ "Reproducibility"
+ "Returning URL for TTR: %@"
+ "SFBSIconSystemName"
+ "SFBSPresentationStyle"
+ "Seed"
+ "Selected for TTR incident \"%@\" (1 in %ld)"
+ "Serious Bug"
+ "Simulating TTR for incident %@ with probability %ld"
+ "Sometimes"
+ "Successfully loaded %lu TTR incidents from preferences"
+ "Successfully saved %lu TTR incidents to preferences"
+ "System client entitlement missing, cannot fetch quota config"
+ "T@\"NSDate\",&,N,V_timeGenerated"
+ "T@\"NSMutableDictionary\",&,N,V_incidents"
+ "This device is experiencing unique errors while talking to iCloud servers in a privacy preserving manner.  Please tap here to help us more quickly resolve this incident."
+ "Title"
+ "User %@ TTR for incident \"%@\""
+ "Using a redemption context that has been valid since %@ (%f seconds ago)"
+ "While no description is required please indicate if you have been experiencing any unexpected issues and particularly with features such as Apple Intelligence, iCloud Private Relay, or RCS functionality.  Also please indicate if you have changed geographical regions or timezones recently."
+ "_incidents"
+ "_proxiedContentControlPolicyIDs"
+ "_timeGenerated"
+ "accepted"
+ "activeProcessorCount"
+ "addDiagnosticInfoToDescription:"
+ "apple-config-features"
+ "apple-response-diag-incident"
+ "apple-response-diag-sample"
+ "applicableConfigFeatures"
+ "askForTTR:incident:"
+ "bolt.fill"
+ "bundleWithIdentifier:"
+ "cleanupOldIncidents"
+ "cloud.llm.v2"
+ "collectSystemInformation"
+ "com.apple.NetworkServiceProxyFramework"
+ "com.apple.distnoted.matching.trusted"
+ "com.apple.networkserviceproxy.featureChangeRefetch"
+ "com.apple.networkserviceproxy.featureSetChanged"
+ "com.apple.networkserviceproxy.ttr"
+ "com.apple.webkit.adattributiond"
+ "componentsJoinedByString:"
+ "context"
+ "createDiagnosticFile:filename:"
+ "createTTR:titleSuffix:"
+ "csfFeatureKey"
+ "dataWithJSONObject:options:error:"
+ "declined"
+ "default"
+ "deviceQuotaConfig"
+ "diskVersion"
+ "feature set updated to %@"
+ "featureSetChanged:"
+ "features"
+ "fetchDeviceQuotaConfigForIssuerName:quotaService:auditToken:bundleID:accessToken:completionHandler:"
+ "fetchDeviceQuotaConfigurationWithFetcher:allowRetry:completionHandler:"
+ "fetchDeviceQuotaConfigurationWithQueue:completionHandler:"
+ "fetchPrivateAccessTokenForChallenge:overrideAttester:configurationFetchDate:configurationETag:validateTransparency:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:useOneTimeTokenBatchSize:accessToken:completionHandler:"
+ "generateRadarURL:titleSuffix:"
+ "getMemoryUsage"
+ "handlePossibleTTR:response:"
+ "hasContext"
+ "hasRateLimit"
+ "hasStartTime"
+ "https://mask-api.icloud.com/v6_0/fetchConfigFile"
+ "https://mock.test/ttr"
+ "iCloud Network Privacy Issue Detected"
+ "iCloud Privacy Platform"
+ "incidents"
+ "initWithURL:statusCode:HTTPVersion:headerFields:"
+ "isCurrentDiskVersion"
+ "isSubsetOfSet:"
+ "isTTRRequired:incident:"
+ "loadIncidentsFromPreferences"
+ "machineType"
+ "memoryUsage"
+ "new"
+ "nodeName"
+ "objectForInfoDictionaryKey:"
+ "openURL:configuration:completionHandler:"
+ "operatingSystemVersionString"
+ "ottIssuer"
+ "parentProcessIdentifier"
+ "physicalMemory"
+ "prewarmTokenCache"
+ "processIdentifier"
+ "processInfo"
+ "processName"
+ "processorCount"
+ "propertyListWithData:options:format:error:"
+ "proxy configuration disk version changed"
+ "radarParams"
+ "radarURLWithResponse:response:"
+ "radarURLWithTitleSuffix:titleSuffix:"
+ "recordIncident:"
+ "redemptionContexts"
+ "responseFlags %lu"
+ "restricted_distributed_notifications"
+ "saveIncidentsToPreferences"
+ "setApplicableConfigFeatures:"
+ "setApplicableFeatures:"
+ "setIncidents:"
+ "setTimeGenerated:"
+ "setupWithPath:"
+ "sharedUtility"
+ "simulate TTR failed due to missing entitlement for %s"
+ "simulatePrivacyProxyTapToRadar:probability:withCompletionHandler:"
+ "startTime"
+ "stringByAppendingPathComponent:"
+ "systemName"
+ "systemRelease"
+ "systemVersion"
+ "tap-to-radar"
+ "timeGenerated"
+ "timestamp"
+ "timestampString"
+ "v152@0:8@16@24@32@40B48B52@56@64@72@80@88@96I104@108@116B124B128B132@136@?144"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v40@0:8@\"NSString\"16q24@?<v@?@\"NSError\">32"
+ "v40@0:8@16q24@?32"
+ "v40@?0@\"NSPPrivacyProxySuccessResponse\"8q16@\"NSString\"24@\"NSString\"32"
+ "validateIncidentsIntegrity"
+ "writeToFile:options:error:"
- "%@ added MPTCP converter proxy policy %lu"
- "%@ adding MPTCP converter proxy policy %@"
- "%@ failed to add MPTCP converter proxy policy"
- "-[NSPPrivacyTokenManager checkCostQuotaForIssuerName:quotaService:auditToken:bundleID:accessToken:completionHandler:]"
- "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:]"
- "Checking cost quota for %@"
- "MPTCPProxyStatus"
- "No access token received, status %u"
- "Private Relay is enabled"
- "Received access token, can use %u"
- "Received error %@ while looking up access token, can use %u"
- "Setup Failure"
- "_isMPTCPConverterProxy"
- "_mptcpProxyPolicyIDs"
- "addPoliciesForMPTCPConverterProxy:"
- "divertSocketToControlUnit:"
- "failed to add policies for MPTCP converter proxy"
- "failed to setup proxying to MPTCP converter proxy"
- "failed to start proxying to MPTCP converter proxy due to missing entitlement for %s"
- "failed to stop proxying to MPTCP converter proxy due to missing entitlement for %s"
- "fetchPrivateAccessTokenForChallenge:overrideAttester:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:"
- "flow divert provider is unavailable"
- "processing request to start proxying to MPTCP converter proxy"
- "processing request to stop proxying to MPTCP converter proxy"
- "proxy setup for MPTCP converter proxy is successful"
- "proxying to MPTCP converter proxy is already started"
- "proxying to MPTCP converter proxy is not started"
- "removePoliciesForMPTCPConverterProxy:"
- "startProxyToMPTCPConverterProxyWithCompletionHandler:"
- "stopProxyToMPTCPConverterProxyWithCompletionHandler:"
- "stopping proxying TCP socket flows to MPTCP converter proxy"
- "unable to start proxying to MPTCP converter proxy because Private Relay is enabled"
- "v128@0:8@16@24B32@36@44@52@60@68@76I84@88@96B104B108@112@?120"

```
