## neagent

> `/usr/libexec/neagent`

```diff

-2063.120.19.0.0
-  __TEXT.__text: 0x3cc4
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x868
-  __TEXT.__const: 0x28
-  __TEXT.__objc_classname: 0x1dc
-  __TEXT.__objc_methname: 0x119a
-  __TEXT.__objc_methtype: 0x8d5
-  __TEXT.__oslogstring: 0x54d
-  __TEXT.__cstring: 0x17c
-  __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__auth_got: 0x220
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x200
-  __DATA_CONST.__cfstring: 0x180
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x80
+2167.0.0.0.2
+  __TEXT.__text: 0x1354c
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_stubs: 0x1920
+  __TEXT.__objc_methlist: 0xf48
+  __TEXT.__const: 0xc0
+  __TEXT.__gcc_except_tab: 0x278
+  __TEXT.__objc_methname: 0x2301
+  __TEXT.__oslogstring: 0x2b70
+  __TEXT.__cstring: 0xea2
+  __TEXT.__objc_classname: 0x31b
+  __TEXT.__objc_methtype: 0xd3e
+  __TEXT.__unwind_info: 0x320
+  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__const: 0x4b0
+  __DATA_CONST.__cfstring: 0x440
+  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0xc38
-  __DATA.__objc_selrefs: 0x520
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__objc_data: 0x190
-  __DATA.__data: 0x600
-  __DATA.__bss: 0x50
+  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA.__objc_const: 0x1c80
+  __DATA.__objc_selrefs: 0x9d8
+  __DATA.__objc_ivar: 0x128
+  __DATA.__objc_data: 0x4b0
+  __DATA.__data: 0x840
+  __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AppSSO.framework/AppSSO
+  - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2BBC40F8-B86C-3394-B1D4-378BB26ED6CC
-  Functions: 87
-  Symbols:   99
-  CStrings:  352
+  UUID: 78DCDBAE-49CE-3B60-A75C-A06F5808E7EE
+  Functions: 284
+  Symbols:   174
+  CStrings:  906
 
Symbols:
+ _NECreateTimerSource
+ _OBJC_CLASS_$_CMLClientConfig
+ _OBJC_CLASS_$_CMLKeywordPIRClient
+ _OBJC_CLASS_$_CMLNetworkManager
+ _OBJC_CLASS_$_CMLUseCaseConfig
+ _OBJC_CLASS_$_CMLUseCaseGroup
+ _OBJC_CLASS_$_CMLUseCaseGroupManager
+ _OBJC_CLASS_$_CMLUseCaseStatus
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_NEHotspotAuthenticationProviderHost
+ _OBJC_CLASS_$_NEHotspotEvaluationProviderHost
+ _OBJC_CLASS_$_NEProcessIdentity
+ _OBJC_CLASS_$_NEURLFilterControlProviderHost
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSXPCListenerEndpoint
+ __Block_object_dispose
+ __Unwind_Resume
+ ___error
+ ___objc_personality_v0
+ __xpc_type_connection
+ __xpc_type_dictionary
+ __xpc_type_string
+ _arc4random
+ _bzero
+ _close
+ _dispatch_source_cancel
+ _fstat
+ _ftruncate
+ _isa_nsnumber
+ _log
+ _malloc_type_malloc
+ _memcpy
+ _mmap
+ _msync
+ _munmap
+ _ne_log_large_obj
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_sync_enter
+ _objc_sync_exit
+ _open
+ _pow
+ _sandbox_check
+ _sandbox_extension_consume
+ _sandbox_extension_release
+ _strerror
+ _strerror_r
+ _strlen
+ _strncpy
+ _xpc_array_apply
+ _xpc_array_get_count
+ _xpc_connection_cancel
+ _xpc_connection_create
+ _xpc_connection_resume
+ _xpc_connection_send_message
+ _xpc_connection_set_event_handler
+ _xpc_connection_set_target_queue
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_array
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_int64
+ _xpc_dictionary_get_string
+ _xpc_dictionary_set_int64
+ _xpc_endpoint_create
+ _xpc_get_type
+ _xpc_string_get_string_ptr
CStrings:
+ ""
+ " "
+ "#%@"
+ "%@ - initFromFile: Invalid params"
+ "%@ - initFromFile: failed to get bloom filter data from mmap file %@"
+ "%@ - initFromFile: retrieved bloom filter data from mmap file %@"
+ "%@ - initWithBitMap: Invalid params"
+ "%@ - initWithData: Invalid params"
+ "%@ - initWithData: failed to save bloom filter data to mmap file"
+ "%@ - initWithData: saved bloom filter data to mmap file"
+ "%@ - initWithNumberOfItems: Invalid params"
+ "%@ dealloc"
+ "%@ handleAppsUninstalled"
+ "%@ handleAppsUpdateBegins"
+ "%@ handleAppsUpdateEnding"
+ "%@ handleAppsUpdateEnds"
+ "%@ handleCancel"
+ "%@ handleDisposeWithCompletionHandler"
+ "%@ handleExtensionExit"
+ "%@ handleInitWithCompletionHandler"
+ "%@ received request to stop provider for ethernet"
+ "%@%@"
+ "%@.%@"
+ "%@: %s"
+ "%@: %s - %@"
+ "%@: %s - Extension cancelWithError %@"
+ "%@: %s - Extension died unexpectedly"
+ "%@: %s - FOR TEST - Skip registration - (group <%@> use case <%@> PrivacyProxyFailOpen <%d> serverURL <%@>"
+ "%@: %s - Failed first fetch of pre-filter data"
+ "%@: %s - Failed to consume sandbox extension from provider: [%d] %s"
+ "%@: %s - Failed to create NEURLFilterProviderHost"
+ "%@: %s - Failed to get extension process identity"
+ "%@: %s - Failed to get file stats for file %s: [%d] %s"
+ "%@: %s - Failed to open file %s: [%d] %s"
+ "%@: %s - Failed to release sandbox extension from provider: [%d] %s"
+ "%@: %s - Failed to save first fetch of pre-filter data"
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
+ "%@: %s - URL Filter Provider has %s entitlement"
+ "%@: %s - URL Filter Provider is missing the required NetworkExtension entitlement"
+ "%@: %s - URL filter configuration invalid <%@>"
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
+ "%@: %s - getPrefilter using mmap file %@"
+ "%@: %s - mmap failed for file %s: [%d] %s"
+ "%@: %s - nil connection"
+ "%@: %s - nil engine"
+ "%@: %s - pluginType %@ pluginClass %ld pluginInfo %@"
+ "%@: %s - read mmap <fd %d, size %lld> for file %s"
+ "%@: %s - request returned error: %@"
+ "%@: %s - request returned with wrong number of results: %@"
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
+ "%@: Failed to create a NEProcessIdentity object"
+ "%@: Failed to derive the process identity, no vendor connection available"
+ "%@: Rejecting un-entitled XPC client"
+ "%@: Validating"
+ "%@: entitlement validation failed"
+ "%@: failed to create a NEProcessIdentity object"
+ "%@: failed to find xpc connection with the hotspot provider"
+ "%@: failed to get extension process identity"
+ "%@: failed to setup hotspot authentication provider"
+ "%@: failed to setup hotspot evaluation provider"
+ "%@: failed to start hotspot authentication provider"
+ "%@: failed to start hotspot evaluation provider"
+ "%@: failed to stop hotspot authentication provider"
+ "%@: failed to stop hotspot evaluation provider"
+ "%@: finding hotspot provider's entitlement"
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
+ "%@: startWithCompletion, result: %s"
+ "%@: startWithConfiguration: %@"
+ "%@: stopWithReason, result: %s"
+ "%@: unable to derive the process identity, no hotspot provider xpc connection"
+ "%@: updateConfiguration"
+ "%@: validating hotspot provider entitlement"
+ "%@: validation failed"
+ "%@: wakeWithCompletion completed, result %s"
+ "%@: wakeup"
+ "%d"
+ "%s: NEBloomFilter - <pid %d> Failed to get file stats for file %s: [%d] %s"
+ "%s: NEBloomFilter - <pid %d> Failed to open file %s: [%d] %s"
+ "%s: NEBloomFilter - <pid %d> No read permission to file %s"
+ "%s: NEBloomFilter - <pid %d> format version (%llu) does not equal the current version (%u)"
+ "%s: NEBloomFilter - <pid %d> invalid file size %lld for file %s"
+ "%s: NEBloomFilter - <pid %d> invalid mmap file size <%d> <bitmapSize %d data_memory_offset %d>"
+ "%s: NEBloomFilter - <pid %d> magic number (%llx) does not equal the expected value (%llx)"
+ "%s: NEBloomFilter - <pid %d> mmap failed for file %s: [%d] %s"
+ "%s: NEBloomFilter - <pid %d> mmap failed to malloc for filename %s: [%d] %s"
+ "%s: NEBloomFilter - <pid %d> no update needed for %s"
+ "%s: NEBloomFilter - <pid %d> read from mmap <numberOfBits %d numberOfHashes %d murmurSeed %d bitmapSize %d>"
+ "%s: NEBloomFilter - <pid %d> read mmap <fd %d, size %lld> for file %s"
+ "%s: NEBloomFilter - <pid %d> update done for %s"
+ "%s: NEBloomFilter - Failed mmap file <%s> <fd %d, size %d>"
+ "%s: NEBloomFilter - Failed msync: [%d] %s"
+ "%s: NEBloomFilter - done msync"
+ "%s: NEBloomFilter - failed to ftruncate mmap file <%s> to %d bytes <errno %d - %s>"
+ "%s: NEBloomFilter - failed to open mmap file %s <errno %d - %s>"
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
+ "*"
+ "*48@0:8r*16*24I32I36I40I44"
+ "+[NEBloomFilter mmapFromFile:bloomFilter:]"
+ "+[NEBloomFilter mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:]"
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
+ "."
+ "/"
+ "/private/var/db/urlPrefilter/com.apple.networkextension.url-prefilter-data."
+ "/private/var/db/urlPrefilter/com.apple.networkextension.url-prefilter-data.temp."
+ "2"
+ "://"
+ "<nil url>"
+ "?%@"
+ "@\"<NEMembershipChecker>\""
+ "@\"NEBitVector\""
+ "@\"NEHotspotAuthenticationProviderHost\""
+ "@\"NEHotspotEvaluationProviderHost\""
+ "@\"NEProcessIdentity\""
+ "@\"NEURLFilterConfiguration\""
+ "@\"NEURLFilterControlProviderHost\""
+ "@\"NEURLFilterEngine\""
+ "@\"NSArray\""
+ "@\"NSData\""
+ "@\"NSMutableDictionary\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@\"NSObject<OS_xpc_object>\""
+ "@\"NSXPCInterface\""
+ "@\"NSXPCListenerEndpoint\""
+ "@24@0:8@16"
+ "@24@0:8r*16"
+ "@28@0:8I16d20"
+ "@32@0:8*16I24I28"
+ "@44@0:8@16I24I28I32@36"
+ "ACTIVE"
+ "App for plugin type %@ has been uninstalled, stopping"
+ "B"
+ "B24@0:8q16"
+ "B24@?0Q8@\"NSObject<OS_xpc_object>\"16"
+ "B28@0:8@\"NSString\"16B24"
+ "B28@0:8@16B24"
+ "B32@0:8@\"NEURLFilterConfiguration\"16@\"NSObject<OS_dispatch_queue>\"24"
+ "B32@0:8r*16^{ne_bloom_filter={ne_bloom_filter_header=QQIIII}^v*^vId}24"
+ "B36@0:8*16I24q28"
+ "B44@0:8*16I24I28I32r*36"
+ "Extensions %@ has been updated, idling"
+ "Extensions %@ is being updated"
+ "Extensions %@ is being updated, stopping"
+ "FAIL"
+ "FALSE"
+ "Filter App updating - ignore extension failure/exit for %@"
+ "Filter extension exit timer expired for %@ - notify that extension failed"
+ "I"
+ "I16@0:8"
+ "I20@0:8I16"
+ "I24@0:8@16"
+ "I24@0:8r*16"
+ "I28@0:8@16I24"
+ "I28@0:8r*16I24"
+ "INACTIVE"
+ "NEAgentHotspotExtension"
+ "NEAgentURLFilterErrorDomain"
+ "NEAgentURLFilterExtension"
+ "NEBitVector"
+ "NEBloomFilter"
+ "NEBloomFilterChecker"
+ "NEExtensionBaseHostDelegate"
+ "NEFNVHash"
+ "NEHotspotPluginDriver"
+ "NEHotspotPluginManager"
+ "NEMembershipChecker"
+ "NEMembershipCheckerErrorDomain"
+ "NEMurmurHash3"
+ "NEPIRChecker"
+ "NEURLFilterEngine"
+ "NEURLFilterEngine queue"
+ "NEURLFilterPluginDriver"
+ "NEURLFilterPluginManager"
+ "NEURLParser"
+ "PID"
+ "Reply dictionary is NULL when handling a source new request"
+ "T@\"NEURLFilterConfiguration\",&,N,V_urlConfiguration"
+ "T@\"NSData\",&,N,V_bitVectorBuffer"
+ "TI,N,V_murmurSeed"
+ "TI,N,V_numberOfBits"
+ "TI,N,V_numberOfHashes"
+ "TI,N,V_numberOfItems"
+ "TRUE"
+ "Td,N,V_falsePositiveTolerance"
+ "URL"
+ "URL Filter Extension not initialized."
+ "URLPrefiltered"
+ "UTF8String"
+ "_appBundleIdentifier"
+ "_appsUpdateEnding"
+ "_appsUpdateStarted"
+ "_bitCount"
+ "_bitVector"
+ "_bitVectorBuffer"
+ "_bitmap"
+ "_bitmapSize"
+ "_clientListener"
+ "_clientListenerEndpoint"
+ "_extensionIdentifier"
+ "_extensionProcessIdentity"
+ "_extensionUUIDs"
+ "_falsePositiveTolerance"
+ "_filter"
+ "_host"
+ "_hostForAuthenticationProvider"
+ "_hostForEvaluationProvider"
+ "_listenerEndpoint"
+ "_managerProtocol"
+ "_mmapFilename"
+ "_murmurSeed"
+ "_numberOfBits"
+ "_numberOfHashes"
+ "_numberOfItems"
+ "_pendingConnections"
+ "_pendingDisposeCompletion"
+ "_pirCache"
+ "_pirGroupName"
+ "_pirPrivacyProxyFailOpen"
+ "_pirSkipRegistration"
+ "_pirUseCase"
+ "_prefilter"
+ "_prefilterFetchTimer"
+ "_registered"
+ "_sendFailedTimer"
+ "_sessionrType"
+ "_setEndpoint:"
+ "_started"
+ "_urlConfiguration"
+ "_urlFilterEngine"
+ "acceptAgentClients"
+ "addObjectsFromArray:"
+ "allObjects"
+ "app for plugin type [%@] has been uninstalled"
+ "appBundleIdentifier"
+ "appendFormat:"
+ "appendString:"
+ "array"
+ "auditToken"
+ "authenticationProviderBundleIdentifier"
+ "bitVectorBuffer"
+ "bytes"
+ "cancelWithError:"
+ "check:redactSensitiveLogs:"
+ "check:sourceAppBundleId:responseQueue:redactSensitiveLogs:completionHandler:"
+ "checkValidityAndCollectErrors:"
+ "cleanupExportedObject"
+ "clearAllBits"
+ "com.apple.developer.networking.networkextension"
+ "command"
+ "componentsJoinedByString:"
+ "componentsSeparatedByString:"
+ "configureGroupWithName:useCaseGroup:error:"
+ "contains:"
+ "containsWithBitmap:numberOfBits:numberOfHashes:murmurSeed:value:"
+ "controlProviderBundleIdentifier"
+ "d"
+ "d16@0:8"
+ "d28@0:8I16I20I24"
+ "dataWithLength:"
+ "dealloc"
+ "didReceiveUnmatchEthernet"
+ "entitlements"
+ "error"
+ "errorWithDomain:code:userInfo:"
+ "evaluationProviderBundleIdentifier"
+ "extension-identifier"
+ "extensions %@ has been updated, idling"
+ "falsePositiveTolerance"
+ "fetchConnectionWithCompletionHandler:"
+ "fetchFilterServerParameters"
+ "fetchPrefilterDataWithCompletion:"
+ "fetchServerParameters"
+ "fetchURLFilterServerParameters"
+ "file-read-data"
+ "file-read-metadata"
+ "fragment"
+ "get-task-allow"
+ "getBitAtIndex:"
+ "getBitAtIndexWithBitmap:bitCount:index:"
+ "getByteCount:"
+ "getExtensionConnection"
+ "getFalsePositiveProbability:numberOfBits:numberOfHashes:"
+ "getNumberOfBits:falsePositiveTolerance:"
+ "getNumberOfHashes:numberOfBits:"
+ "getPrefilter"
+ "getURLFilterClientConnectionWithCompletionHandler:completionHandler:"
+ "handleHotspotProviderError:"
+ "handleHotspotProviderStopped"
+ "handleXPCError"
+ "hasPrefix:"
+ "hasSuffix:"
+ "hash:"
+ "hash:seed:"
+ "hashWithString:"
+ "hashWithString:seed:"
+ "host"
+ "hotspot"
+ "hotspot provider software updating - ignore extension failure/exit for %@"
+ "hotspot-provider"
+ "hotspot-session-type"
+ "i"
+ "i24@0:8I16i20"
+ "i28@0:8I16d20"
+ "initFromFile:"
+ "initWithBase64EncodedString:options:"
+ "initWithBitMap:bitmapSize:bitCount:"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithBytes:length:"
+ "initWithClientConfig:dispatchQueue:"
+ "initWithData:numberOfBits:numberOfHashes:murmurSeed:mmapFilename:"
+ "initWithFormat:"
+ "initWithKeyExpirationMinutes:keyRotationBeforeExpirationMinutes:useCases:networkConfig:"
+ "initWithNumberOfItems:falsePositiveTolerance:"
+ "initWithPID:auditToken:"
+ "initWithString:"
+ "initWithType:endpoint:issuer:authenticationToken:privacyProxyFailOpen:"
+ "initWithType:maxShards:cacheElementCount:cacheEntryMinutesToLive:"
+ "initWithUTF8String:"
+ "initWithUseCase:sourceApplicationBundleIdentifier:"
+ "initialize:"
+ "initializing HostForAuthenticationProvider"
+ "initializing HostForEvaluationProvider"
+ "insert:"
+ "insertWithBitmap:numberOfBits:numberOfHashes:murmurSeed:value:"
+ "intValue"
+ "length"
+ "lengthOfBytesUsingEncoding:"
+ "matchingStringsForURL:"
+ "mmapFromFile:bloomFilter:"
+ "mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:"
+ "murmurSeed"
+ "nil"
+ "numberOfBits"
+ "numberOfHashes"
+ "numberOfItems"
+ "numberWithBool:"
+ "objectAtIndexedSubscript:"
+ "objectForKey:ofClass:"
+ "path"
+ "pathComponents"
+ "pid"
+ "pirAuthenticationToken"
+ "pirGroupName"
+ "pirPrivacyPassIssuerURL"
+ "pirPrivacyProxyFailOpen"
+ "pirServerURL"
+ "pirSkipRegistration"
+ "pirUseCase"
+ "prefilterFetchInterval"
+ "present"
+ "printBits"
+ "processIdentifier"
+ "query"
+ "rangeOfString:"
+ "redactSensitiveLogs"
+ "removeAllObjects"
+ "reportHotspotError:"
+ "requestDataByStringKeywords:completionHandler:"
+ "requestStatusForClientConfig:options:completionHandler:"
+ "resetCache"
+ "resetURLFilterCache"
+ "setBitAtIndex:toValue:"
+ "setBitAtIndexWithBitmap:bitCount:index:toValue:"
+ "setBitVectorBuffer:"
+ "setFalsePositiveTolerance:"
+ "setMurmurSeed:"
+ "setNumberOfBits:"
+ "setNumberOfHashes:"
+ "setNumberOfItems:"
+ "setObject:forKeyedSubscript:"
+ "setQueue:"
+ "setUrlConfiguration:"
+ "setWithCapacity:"
+ "setupWithCompletion:"
+ "sharedManager"
+ "shouldFailClosed"
+ "sleepWithCompletion:"
+ "start:responseQueue:"
+ "startAuthenticationProvider"
+ "startEvaluationProvider"
+ "startFilter"
+ "startURLFilter"
+ "startWithCompletion:"
+ "status"
+ "stop"
+ "stopFilter"
+ "stopWithReason:completion:"
+ "string"
+ "stringByAppendingPathComponent:"
+ "stringByAppendingString:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "stringWithFormat:"
+ "stringWithUTF8String:"
+ "subarrayWithRange:"
+ "substringFromIndex:"
+ "unmatchEthernet"
+ "updatePrefilterWithCompletionHandler:"
+ "url-filter-provider"
+ "url.filtering"
+ "urlConfiguration"
+ "urlFilter"
+ "uuid"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "v16@?0@\"NSXPCListenerEndpoint\"8"
+ "v20@0:8I16"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8d16"
+ "v24@?0@\"CMLUseCaseStatus\"8@\"NSError\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v28@0:8i16@?20"
+ "v28@0:8i16@?<v@?@\"NSXPCListenerEndpoint\"@\"NSData\">20"
+ "v28@0:8q16B24"
+ "v32@0:8q16@\"NSError\"24"
+ "v32@0:8q16@24"
+ "v40@0:8*16I24q28B36"
+ "v44@0:8*16I24I28I32r*36"
+ "v52@0:8@\"NSArray\"16@\"NSString\"24@\"NSObject<OS_dispatch_queue>\"32B40@?<v@?B@\"NSError\">44"
+ "v52@0:8@16@24@32B40@?44"
+ "v52@?0@\"NSData\"8@\"NSURL\"16@\"NSString\"24I32I36I40@\"NSError\"44"
+ "verdict"
+ "wakeWithCompletion:"
+ "www."

```
