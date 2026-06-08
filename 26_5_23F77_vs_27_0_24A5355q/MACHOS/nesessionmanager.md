## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-2226.120.19.0.0
-  __TEXT.__text: 0xbbae8
-  __TEXT.__auth_stubs: 0x1cf0
-  __TEXT.__objc_stubs: 0x80c0
-  __TEXT.__objc_methlist: 0x3dbc
-  __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x2280
-  __TEXT.__objc_methname: 0x922c
-  __TEXT.__oslogstring: 0xfcde
-  __TEXT.__cstring: 0x54d0
-  __TEXT.__objc_classname: 0xbbc
-  __TEXT.__objc_methtype: 0x215e
-  __TEXT.__unwind_info: 0x1658
-  __DATA_CONST.__auth_got: 0xe88
-  __DATA_CONST.__got: 0x778
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1dd0
-  __DATA_CONST.__cfstring: 0x2680
-  __DATA_CONST.__objc_classlist: 0x278
-  __DATA_CONST.__objc_protolist: 0x148
+2303.0.0.0.2
+  __TEXT.__text: 0xb7088
+  __TEXT.__auth_stubs: 0x1e10
+  __TEXT.__objc_stubs: 0x8a20
+  __TEXT.__objc_methlist: 0x3fb4
+  __TEXT.__const: 0x198
+  __TEXT.__gcc_except_tab: 0x2394
+  __TEXT.__objc_methname: 0x9b2f
+  __TEXT.__oslogstring: 0x1138b
+  __TEXT.__cstring: 0x5a86
+  __TEXT.__objc_classname: 0xbc4
+  __TEXT.__objc_methtype: 0x2270
+  __TEXT.__unwind_info: 0x1720
+  __DATA_CONST.__const: 0x1e48
+  __DATA_CONST.__cfstring: 0x2a40
+  __DATA_CONST.__objc_classlist: 0x290
+  __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x218
+  __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x8158
-  __DATA.__objc_selrefs: 0x23d0
-  __DATA.__objc_ivar: 0x794
-  __DATA.__objc_data: 0x18b0
-  __DATA.__data: 0xf80
+  __DATA_CONST.__auth_got: 0xf18
+  __DATA_CONST.__got: 0x798
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x8738
+  __DATA.__objc_selrefs: 0x2640
+  __DATA.__objc_ivar: 0x7f4
+  __DATA.__objc_data: 0x19a0
+  __DATA.__data: 0x1040
   __DATA.__bss: 0x130
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SystemWake.framework/SystemWake
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A9BC23E5-C1B2-37D9-866F-C5C46B7540C0
-  Functions: 1896
-  Symbols:   687
-  CStrings:  4366
+  UUID: 907B9602-42D8-3960-844F-67E3E19E1704
+  Functions: 1956
+  Symbols:   711
+  CStrings:  4656
 
Symbols:
+ _OBJC_CLASS_$_CMLPrivacyPassToken
+ _OBJC_CLASS_$_NEKeychainItem
+ _OBJC_CLASS_$_NERegexURLParser
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_PBCodable
+ _OBJC_METACLASS_$_PBCodable
+ _PBDataWriterWriteStringField
+ _PBReaderReadString
+ _PBReaderSkipValueWithTag
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ ___strlcpy_chk
+ _access
+ _bzero
+ _dispatch_assert_queue$V2
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _ftruncate
+ _kSCPropNetIPSecSharedSecretEncryption
+ _msync
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x9
- _OBJC_CLASS_$_NEURLParser
- _objc_release_x2
CStrings:
+ "%@ %@"
+ "%@ Mission Critical Match: 5G slice availability (%s) entitlement availablility (%s) for app [%@]"
+ "%@ Mission Critical service changed to %s"
+ "%@ PTT slice capability did change"
+ "%@ [wifiMatch: %s] [cellMatch: %s] [ethMatch: %s] [mcxMatch: %s]"
+ "%@ failed to get PTT slicing capability status, error: %@, bundleId: %@"
+ "%@ failed to get app record for [%@], error: %@"
+ "%@ failed to register for PTT slicing capability updates, error: %@, bundleId: %@"
+ "%@ no application identifier provided"
+ "%@ received app installation change notification"
+ "%@: %s - Canceling reporting timer"
+ "%@: %s - Changed owner for mmap file for URL filter report %@"
+ "%@: %s - Created new mmap file for URL filter report %@"
+ "%@: %s - Failed to chown mmap file for URL filter report %@ <errno %d - %s>"
+ "%@: %s - Failed to create reporting timer source"
+ "%@: %s - Failed to open/create mmap file for URL filter report %@ <errno %d - %s>"
+ "%@: %s - Failed to remove mmap file for URL filter report %@ <errno %d - %s>"
+ "%@: %s - Failed to retrieve privacy token for report: %@"
+ "%@: %s - Failed to send blocked URLs report: %@"
+ "%@: %s - Filter not active, skipping report"
+ "%@: %s - No reporting URL configured, skipping report"
+ "%@: %s - Opened existing mmap file for URL filter report %@"
+ "%@: %s - Removed mmap file for URL filter report %@"
+ "%@: %s - Report interval is %f, not setting up reporting timer"
+ "%@: %s - Sending blocked URLs report in protobuf format to %@"
+ "%@: %s - Setting up reporting timer with interval %f seconds"
+ "%@: %s - Successfully created repeating reporting timer with %f second interval"
+ "%@: %s - Successfully sent blocked URLs report"
+ "%@: %s - Using test report endpoint %@"
+ "%@: %s - init report using mmap file %@"
+ "%@: %s - removing mmap file for URL filter report %@"
+ "%@: Added Authorization header with PrivateToken + base64 token (length: %lu)"
+ "%@: Bloom filter has no mmap data to post"
+ "%@: Bloom filter has no mmap memory content to clear"
+ "%@: Bundle ID truncated from %d to %d characters: %s"
+ "%@: Cannot reinitialize - mmap not properly set up"
+ "%@: Clearing mmap memory content (%u entries)"
+ "%@: Collected %lu unique URLs for JSON serialization"
+ "%@: Collected %lu unique URLs for protobuf serialization"
+ "%@: Corrupted file - currentCount (%u) > maxEntries (%u). Reinitializing file."
+ "%@: Creating new mmap file"
+ "%@: Deregister App Push Session: %@"
+ "%@: Existing file has invalid magic number (0x%llx), reinitializing"
+ "%@: Extending existing mmap file from %zu to %zu bytes"
+ "%@: Failed to create JSON data: %@"
+ "%@: Failed to mmap file: %s"
+ "%@: Failed to open mmap file %@: %s"
+ "%@: Failed to post mmap data: %@"
+ "%@: Failed to process binary auth token data (raw length: %lu)"
+ "%@: Failed to resize mmap file: %s"
+ "%@: Failed to serialize protobuf data"
+ "%@: Failed to sync cleared mmap data to disk: %s"
+ "%@: Failed to sync reinitialized mmap data to disk: %s"
+ "%@: Found existing mmap file with size %zu bytes (expected: %zu bytes)"
+ "%@: Found valid existing mmap file with %u entries (max: %u, version: %u)"
+ "%@: Generated JSON data with %lu URLs (%lu bytes)"
+ "%@: Generated protobuf data with %lu URLs (%lu bytes) using ProtocolBuffer framework"
+ "%@: Initialized mmap file %@ with %u max entries, current count: %u"
+ "%@: Invalid mmap magic number, file may be corrupted"
+ "%@: Invalid mmap magic number, returning empty JSON data"
+ "%@: Invalid mmap magic number, skipping mmap entries"
+ "%@: Max entries mismatch - file has %u, expected %u. Reinitializing file."
+ "%@: No auth token provided for request"
+ "%@: No mmap data to post"
+ "%@: Posting %lu bytes of %@ data to %@ using %@ protocol (privacyProxyFailClosed %d)"
+ "%@: Processing auth token with length: %lu bytes"
+ "%@: Reinitializing mmap file content"
+ "%@: Reporting disabled - device unsupervised"
+ "%@: Server returned error code: %ld"
+ "%@: Successfully cleared mmap memory content and synced to disk"
+ "%@: Successfully posted mmap data. Response code: %ld"
+ "%@: URL truncated from %d to %d characters"
+ "%@: Unsupported mmap version %u, expected %u"
+ "%@: Version mismatch - file has version %u, expected %u. Reinitializing file."
+ "%@: WARNING: Existing file is larger than expected (%zu > %zu bytes). This may indicate version mismatch or corruption."
+ "%@: found DDM sourced persistent reference for password"
+ "%@: found DDM sourced persistent reference for shared secret"
+ "%@: handleNewRequest - Allow neagent requests"
+ "%@: handleNewRequest - regular expression parse result is nil - allow <parsed groupnames %@>"
+ "%@: mmap file is full (%u entries), will overwrite latest entry (LIFO)"
+ "%@: mmap not initialized, cannot clear content"
+ "%@: mmap not initialized, cannot write blocked URL"
+ "%@: mmap not initialized, returning empty JSON data"
+ "%@: msync warning: %s"
+ "%@[%@]:%s: applyIncludeAllNetworks failed"
+ "%lu"
+ "%s: Adding %@ policy for %s traffic to bypass includeAllNetworks"
+ "%s: Adding policy %@ for local networks for %s (priority %d)"
+ "-[NEPIRChecker initializeMmapFile]"
+ "-[NEPolicySession(AlwaysOnVPN) addIPFamilyExceptionWithOrder:includeAllNetworks:result:]"
+ "-[NEPolicySession(AlwaysOnVPN) addLocalNetworksExceptionWithOrder:skipOrder:priority:includeAllNetworks:excludeLocalNetworks:policyIDList:]"
+ "-[NEPolicySession(AlwaysOnVPN) addServiceExceptionsWithOrder:configuration:networkSettings:IMSUseIPSec:dropAllLevel:isHighPriority:]"
+ "-[NEPolicySession(AlwaysOnVPN) evaluateConfiguration:networkSettings:startOrder:IMSUseIPSec:dropAllLevel:captiveNetworkPlugins:]"
+ "-[NESMPolicySession setTunnelDataPoliciesForInterfaceName:outgoingInterfaceName:hasDNS:hasProxy:hasIncludeAllNetworks:hasExcludeLocalNetworks:hasExcludeCellularServices:hasExcludeDeviceCommunication:]_block_invoke"
+ "-[NESMURLFilterSession filterReportCleanup]"
+ "-[NESMURLFilterSession filterReportSetup]"
+ "-[NEURLFilterEngine cancelReportingTimer]"
+ "-[NEURLFilterEngine sendBlockedURLsReport:]"
+ "-[NEURLFilterEngine sendBlockedURLsReport:]_block_invoke"
+ "-[NEURLFilterEngine sendBlockedURLsReport:]_block_invoke_2"
+ "-[NEURLFilterEngine setConfiguration:completionHandler:]_block_invoke_2"
+ "-[NEURLFilterEngine setupReportingTimer]"
+ "-[NEURLFilterEngine startFilterWithCompletionHandler:]_block_invoke_2"
+ ".well-known/masque/udp"
+ "/private/var/db/urlPrefilter/com.apple.networkextension.url-prefilter-data.report."
+ "@\"<NEMissionCriticalServiceMonitorDelegate>\""
+ "@\"NEMissionCriticalServiceMonitor\""
+ "@24@0:8^{_NSZone=}16"
+ "@36@0:8@16@24i32"
+ "Authorization"
+ "Begin opportunistic fallback advisory"
+ "Begin prefer fallback advisory"
+ "Content-Length"
+ "Content-Type"
+ "ENTITLED"
+ "Ignoring invalid PvD configuration for relay %@"
+ "Installing VPN Service Exceptions <CellularServices> for NEPolicySessionPriorityPrivilegedTunnel"
+ "Installing VPN Service Exceptions <DeviceCommunication> for NEPolicySessionPriorityPrivilegedTunnel"
+ "Installing VPN Service Exceptions <LocalNetworks> <ipfamily %d> for NEPolicySessionPriorityPrivilegedTunnel"
+ "Installing VPN Service Exceptions <VoiceMail> for NEPolicySessionPriorityPrivilegedTunnel"
+ "Installing VPN icmpv6 Exceptions - policies at NEPolicySessionPriorityPrivilegedTunnel"
+ "Installing enforceRoutes Exceptions <LocalNetworks> for NEPolicySessionPriorityPrivilegedTunnel"
+ "Invalid URL scheme. Only HTTP and HTTPS are supported"
+ "Invalid format. Use 'json' or 'protobuf'"
+ "NEBlockedURLEntry"
+ "NEMissionCriticalServiceMonitor"
+ "NEMissionCriticalServiceMonitorDelegate"
+ "NEURLFilterReport"
+ "NOT ENTITLED"
+ "NSCopying"
+ "POST"
+ "PrivateToken token=%@"
+ "PvD: Ports are not currently supported in proxy-match rules: %@"
+ "PvD: Proxy identifier %@ does not handle both TCP and UDP"
+ "PvD: Referenced proxy %@ did not have 2 entries: %@"
+ "PvD: Two proxies do not have matching ALPN values: %@"
+ "PvD: connect-udp proxy URI path must contain '.well-known/masque/udp/{target_host}/{target_port}': %@"
+ "PvD: ignore fallback proxy identifiers %@"
+ "PvD: invalid \"proxies\" key value: %@"
+ "PvD: match rules refer to different identifiers %@ != %@"
+ "Server returned status %ld"
+ "T@\"NSDate\",&,N,V_timestamp"
+ "T@\"NSString\",C,N,V_sourceBundleId"
+ "T@\"NSString\",C,N,V_url"
+ "Ti,N,V_sourcePID"
+ "URLWithString:"
+ "URLWithString:relativeToURL:"
+ "[]"
+ "^v"
+ "^{ne_pir_blocked_url_entry=[512c][128c]iSSQ}"
+ "^{ne_pir_blocked_url_header=QIIII}"
+ "_advisoryMode"
+ "_appHasMissionCriticalMatch"
+ "_applicationIdentifier"
+ "_bundleIdentifier"
+ "_filterReportFilePath"
+ "_isEntitled"
+ "_isMCXNetworkSliceAvailable"
+ "_isMCXServiceMatched"
+ "_mcxMonitor"
+ "_mmapEntries"
+ "_mmapFileDescriptor"
+ "_mmapFilePath"
+ "_mmapFileSize"
+ "_mmapHeader"
+ "_mmapMemory"
+ "_queueIdentityKey"
+ "_reportingTimer"
+ "_setError"
+ "_setPrivacyProxyFailClosed:"
+ "_sourceBundleId"
+ "_sourcePID"
+ "_timestamp"
+ "_url"
+ "_urls"
+ "absoluteURL"
+ "advisoryMode"
+ "allocWithZone:"
+ "alpn"
+ "application/json"
+ "application/x-protobuf"
+ "base64EncodedStringWithOptions:"
+ "clearMmapMemoryContent"
+ "com.apple.developer.media-device-extension"
+ "com.apple.developer.networking.slicing.appcategory"
+ "com.apple.nesessionmanager.opportunisticFallback.%@"
+ "com.apple.nesessionmanager.preferFallback.%@"
+ "connect-udp"
+ "containsString:"
+ "copyWithZone:"
+ "data"
+ "dataUsingEncoding:"
+ "dataWithJSONObject:options:error:"
+ "dateWithTimeIntervalSince1970:"
+ "dictionaryRepresentation"
+ "didReceiveMissionCriticalServiceMatchChange:"
+ "ephemeralSessionConfiguration"
+ "fetchPrivacyPassTokenForGroup:dispatchQueue:completionHandler:"
+ "file-read*"
+ "getBytes:range:"
+ "getCachedBlockedURLs"
+ "getPTTSlicingCapabilityForBundleId:completion:"
+ "hasError"
+ "http"
+ "https"
+ "https-connect"
+ "includeAllNetworksEnabled"
+ "initWithBytes:length:encoding:"
+ "initWithDDMPersistentReference:"
+ "initWithDelegate:queue:h3URL:h2URL:identityRef:additionalHTTPHeaders:cachedPvDConfig:"
+ "initWithURL:sourceBundleId:sourcePID:"
+ "matchMissionCriticalService"
+ "matched"
+ "matchingStringsForURLString:options:domainLevels:pathSegments:queryParameters:componentPlaceHolder:parsePattern:parseGroupNames:parseDelimitor:"
+ "mc-9500"
+ "not matched"
+ "parsingCaseSensitive"
+ "parsingDomainLevels"
+ "parsingEnumerateDomainHierarchy"
+ "parsingEnumeratePathHierarchy"
+ "parsingExcludeDomain"
+ "parsingExcludeFragment"
+ "parsingExcludeIntermediates"
+ "parsingExcludePath"
+ "parsingExcludeQuery"
+ "parsingExcludeScheme"
+ "parsingExcludeWWW"
+ "parsingGroupNames"
+ "parsingPathSegments"
+ "parsingQueryNames"
+ "parsingRegularExpression"
+ "passwordReference"
+ "ports"
+ "position"
+ "postMmapDataToEndpoint:format:authorizationToken:completionHandler:"
+ "profileSource"
+ "proxy"
+ "pttSlicingCapabilityDidChange:"
+ "readFrom:"
+ "reportEndpoint"
+ "reportFormat"
+ "reportInterval"
+ "requestWithURL:cachePolicy:timeoutInterval:"
+ "scheme"
+ "sessionWithConfiguration:"
+ "setAdvisoryMode:"
+ "setHTTPBody:"
+ "setHTTPMethod:"
+ "setObject:forKey:"
+ "setPosition:"
+ "setReportEndpoint:"
+ "setReportInterval:"
+ "setSourceBundleId:"
+ "setSourcePID:"
+ "setTimeoutIntervalForRequest:"
+ "setTimeoutIntervalForResource:"
+ "setTimestamp:"
+ "setUrl:"
+ "setValue:forHTTPHeaderField:"
+ "sharedSecretReference"
+ "slicingStatusNameChanged:name:"
+ "sortedArrayUsingSelector:"
+ "sourceBundleId"
+ "sourcePID"
+ "testReportURL"
+ "timestamp"
+ "updatePTTSlicingCapabilityBundleIds:completion:"
+ "uppercaseString"
+ "url"
+ "urls"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v48@0:8@\"NSURL\"16q24@\"NSData\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@16q24@32@?40"
+ "writeTo:"
- "%@ [wifiMatch: %s] [cellMatch: %s] [ethMatch: %s]"
- "-[NEPolicySession(AlwaysOnVPN) addLocalNetworksExceptionWithOrder:skipOrder:priority:policyIDList:]"
- "-[NEPolicySession(AlwaysOnVPN) addServiceExceptionsWithOrder:configuration:IMSUseIPSec:dropAllLevel:isHighPriority:]"
- "-[NEPolicySession(AlwaysOnVPN) evaluateConfiguration:startOrder:IMSUseIPSec:dropAllLevel:captiveNetworkPlugins:]"
- "-[NESMPolicySession setTunnelDataPoliciesForInterfaceName:outgoingInterfaceName:hasDNS:hasProxy:hasExcludeLocalNetworks:hasExcludeCellularServices:hasExcludeDeviceCommunication:]_block_invoke"
- "PvD contents: %@"
- "Updating policies due to PvD configuration change for %@"
- "_weakFallback"
- "file-read-data"
- "file-read-metadata"
- "initWithDelegate:queue:url:identityRef:additionalHTTPHeaders:cachedPvDConfig:"
- "matchingStringsForURL:"
- "setWeakAdvisory:"
- "weakAdvisory"

```
