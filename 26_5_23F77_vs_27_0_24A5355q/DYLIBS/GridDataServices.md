## GridDataServices

> `/System/Library/PrivateFrameworks/GridDataServices.framework/GridDataServices`

```diff

-72.0.0.0.0
-  __TEXT.__text: 0x7b7c
-  __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_methlist: 0x740
+74.0.0.0.0
+  __TEXT.__text: 0x7a94
+  __TEXT.__objc_methlist: 0x7c0
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x852
-  __TEXT.__oslogstring: 0x828
-  __TEXT.__gcc_except_tab: 0x22c
-  __TEXT.__unwind_info: 0x298
-  __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x15a6
-  __TEXT.__objc_methtype: 0x317
-  __TEXT.__objc_stubs: 0x11e0
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x1e8
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__cstring: 0x8ba
+  __TEXT.__oslogstring: 0x9a2
+  __TEXT.__gcc_except_tab: 0x188
+  __TEXT.__unwind_info: 0x258
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1f8
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d0
+  __DATA_CONST.__objc_selrefs: 0x730
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x208
+  __DATA_CONST.__got: 0x150
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0xca0
-  __AUTH_CONST.__objc_const: 0xe60
+  __AUTH_CONST.__cfstring: 0xd20
+  __AUTH_CONST.__objc_const: 0x12e0
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x78
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x7c
   __DATA.__data: 0x120
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 941BA95A-8126-3C00-98EF-CB803A837998
-  Functions: 175
-  Symbols:   755
-  CStrings:  604
+  UUID: 96A786EC-4DD8-3307-A1B3-57371D124568
+  Functions: 182
+  Symbols:   808
+  CStrings:  293
 
Symbols:
+ -[GDSServerConnectionSessionDelegate .cxx_destruct]
+ -[GDSServerConnectionSessionDelegate URLSession:didReceiveChallenge:completionHandler:]
+ -[GDSServerConnectionSessionDelegate init]
+ -[GDSServerConnectionSessionDelegate keyStorePassword]
+ -[GDSServerConnectionSessionDelegate keyStorePath]
+ -[GDSServerConnectionSessionDelegate loadIdentityFromKeystore]
+ -[GDSServerConnectionSessionDelegate log]
+ -[GDSServerConnectionSessionDelegate setLog:]
+ -[_GDSManager setFakeServerKeyStorePassword:]
+ -[_GDSManager setFakeServerKeyStorePath:]
+ _NSURLAuthenticationMethodClientCertificate
+ _OBJC_CLASS_$_GDSServerConnectionSessionDelegate
+ _OBJC_CLASS_$_NSURLCredential
+ _OBJC_IVAR_$_GDSServerConnectionSessionDelegate._log
+ _OBJC_METACLASS_$_GDSServerConnectionSessionDelegate
+ _SecPKCS12Import
+ __OBJC_$_INSTANCE_METHODS_GDSServerConnectionSessionDelegate
+ __OBJC_$_INSTANCE_VARIABLES_GDSServerConnectionSessionDelegate
+ __OBJC_$_PROP_LIST_GDSServerConnectionSessionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_GDSServerConnectionSessionDelegate
+ __OBJC_CLASS_RO_$_GDSServerConnectionSessionDelegate
+ __OBJC_METACLASS_RO_$_GDSServerConnectionSessionDelegate
+ ___45+[_GDSServerConnection fetchConfigWithError:]_block_invoke.150
+ ___45+[_GDSServerConnection fetchConfigWithError:]_block_invoke.150.cold.1
+ ___55-[_GDSServerConnection fetchBalancingAuthorityPolygons]_block_invoke.201
+ ___57-[_GDSServerConnection fetchMarginalEmissionForecastFor:]_block_invoke.211
+ ___65-[_GDSServerConnection fetchCarbonIntensityHistoryForBA:from:to:]_block_invoke.244
+ ___block_descriptor_72_e8_32s40s48r56r64r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8r48l8s40l8r56l8r64l8
+ ___block_literal_global.116
+ ___block_literal_global.203
+ ___block_literal_global.213
+ ___block_literal_global.246
+ ___block_literal_global.97
+ _kGDSFakeServerKeyStorePassword
+ _kGDSFakeServerKeyStorePath
+ _kSecImportExportPassphrase
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$authenticationMethod
+ _objc_msgSend$credentialForTrust:
+ _objc_msgSend$credentialWithIdentity:certificates:persistence:
+ _objc_msgSend$dataWithContentsOfFile:
+ _objc_msgSend$firstObject
+ _objc_msgSend$keyStorePassword
+ _objc_msgSend$keyStorePath
+ _objc_msgSend$loadIdentityFromKeystore
+ _objc_msgSend$protectionSpace
+ _objc_msgSend$serverTrust
+ _objc_msgSend$setLog:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x6
+ _objc_retain_x8
- GCC_except_table66
- _OUTLINED_FUNCTION_4
- ___45+[_GDSServerConnection fetchConfigWithError:]_block_invoke.144
- ___45+[_GDSServerConnection fetchConfigWithError:]_block_invoke.144.cold.1
- ___55-[_GDSServerConnection fetchBalancingAuthorityPolygons]_block_invoke.194
- ___57-[_GDSServerConnection fetchMarginalEmissionForecastFor:]_block_invoke.204
- ___65-[_GDSServerConnection fetchCarbonIntensityHistoryForBA:from:to:]_block_invoke.237
- ___block_descriptor_72_e8_32s40s48r56r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8r48l8s40l8r56l8
- ___block_literal_global.110
- ___block_literal_global.196
- ___block_literal_global.206
- ___block_literal_global.239
- ___block_literal_global.91
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "Error importing P12 file. Status: %d"
+ "Error: failed to read P12 file at path"
+ "Found keyStorePath and keyStorePassword, extracting identity..."
+ "Identity and certificate data read successfully"
+ "P12 file successfully imported"
+ "Received authentication challenge"
+ "Setting the fake server keyStore password."
+ "Setting the fake server keyStore path."
+ "chain"
+ "fakeServerKeyStorePassword"
+ "fakeServerKeyStorePath"
+ "identity"
+ "mTLS client certificate challenge received"
+ "serverConnectionDelegate"
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSUserDefaults\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32d40"
- "@56@0:8@16@24@32@40@48"
- "@72@0:8@16@24d32d40d48d56@64"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "HMACSignedRequest:secret:secretVersion:"
- "HMAC_SHA256Digest:key:"
- "HTTPBody"
- "HTTPMethod"
- "ID"
- "JSONObjectWithData:options:error:"
- "NSObject"
- "NSURLSessionDelegate"
- "Q16@0:8"
- "SHA256_HashStringFromData:"
- "T#,R"
- "T@\"NSDate\",&,N,V_configFetchDate"
- "T@\"NSDate\",R,N,V_fetchDate"
- "T@\"NSDate\",R,N,V_generationDate"
- "T@\"NSDate\",R,N,V_lastUpdatedDate"
- "T@\"NSDictionary\",&,N,V_currentMarginalForecast"
- "T@\"NSDictionary\",R,N,V_forecastMap"
- "T@\"NSDictionary\",R,N,V_historicalMap"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_os_log>\",&,N,V_log"
- "T@\"NSString\",&,N,V_clientID"
- "T@\"NSString\",&,N,V_locBundlePath"
- "T@\"NSString\",&,N,V_serverURL"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSUUID\",R,N,V_ID"
- "T@\"NSUserDefaults\",&,N,V_defaults"
- "T@\"NSUserDefaults\",&,N,V_fakeDataDefaults"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "TB,N,V_isCASupported"
- "TB,N,V_isCECSupported"
- "TQ,R"
- "Td,N,V_configVersion"
- "Td,R,N,V_latEnd"
- "Td,R,N,V_latStart"
- "Td,R,N,V_longEnd"
- "Td,R,N,V_longStart"
- "Td,R,N,V_refetchInterval"
- "URL"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "UTF8String"
- "UUID"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_GDSBalancingAuthority"
- "_GDSBalancingAuthorityOutput"
- "_GDSEmissionForecast"
- "_GDSEmissionHistory"
- "_GDSHMACGenerator"
- "_GDSManager"
- "_GDSManagerProtocol"
- "_GDSServerConnection"
- "_ID"
- "_clientID"
- "_configFetchDate"
- "_configVersion"
- "_connection"
- "_currentMarginalForecast"
- "_defaults"
- "_fakeDataDefaults"
- "_fetchDate"
- "_forecastMap"
- "_generationDate"
- "_historicalMap"
- "_identifier"
- "_isCASupported"
- "_isCECSupported"
- "_lastUpdatedDate"
- "_latEnd"
- "_latStart"
- "_locBundlePath"
- "_log"
- "_longEnd"
- "_longStart"
- "_name"
- "_queue"
- "_refetchInterval"
- "_serverURL"
- "addObject:"
- "addObjectsFromArray:"
- "addValue:forHTTPHeaderField:"
- "allHTTPHeaderFields"
- "appendFormat:"
- "array"
- "arrayForKey:"
- "arrayWithObjects:count:"
- "autorelease"
- "base64EncodedStringWithOptions:"
- "boolValue"
- "bucketedEpochTimeStamp"
- "bytes"
- "cStringUsingEncoding:"
- "carbonIntensityHistoryForBA:from:to:"
- "checkServerConfiguration"
- "class"
- "clientID"
- "code"
- "components:fromDate:"
- "componentsJoinedByString:"
- "componentsWithString:"
- "configFetchDate"
- "conformsToProtocol:"
- "connection"
- "coordinate"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryCode"
- "createSessionConfiguration"
- "currentBalancingAuthority"
- "currentCalendar"
- "currentEstimates"
- "currentMarginalForecast"
- "d"
- "d16@0:8"
- "dataFromLocation:"
- "dataTaskWithRequest:completionHandler:"
- "dataUsingEncoding:"
- "dataWithJSONObject:options:error:"
- "date"
- "dateByAddingTimeInterval:"
- "dateFormatter"
- "dateFromString:"
- "dateStringFromDate:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "defaultSessionConfiguration"
- "defaults"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "distantPast"
- "doubleValue"
- "encodeStringToBase64:"
- "errorWithDomain:code:userInfo:"
- "fakeDataDefaults"
- "fetchBalancingAuthority"
- "fetchBalancingAuthorityFromLocation:"
- "fetchBalancingAuthorityPolygons"
- "fetchCarbonIntensityHistoryForBA:from:to:"
- "fetchConfigWithError:"
- "fetchDate"
- "fetchEstimatedCountryCode"
- "fetchMarginalEmissionForecastFor:"
- "finishTasksAndInvalidate"
- "fixMarginalEmissionForecast:"
- "forecastMap"
- "generateURLRequest:secretVersion:signature:content:timestamp:"
- "generationDate"
- "getFakeMarginalEmissionForecast"
- "getFakeSecret"
- "getFakeSecretVersion"
- "getFakeServerURL"
- "getRequestForEndpoint:withData:keySequence:"
- "handleNewConfig:"
- "hash"
- "historicalMap"
- "identifier"
- "init"
- "initWithBytes:length:"
- "initWithForecast:generatedAt:fetchedAt:refetchInterval:"
- "initWithHistoricalData:fetchedAt:"
- "initWithID:locationBundlePath:"
- "initWithID:name:updateDate:"
- "initWithIdentifier:name:latitudeStart:latitudeEnd:longitudeStart:longitudeEnd:updateDate:"
- "initWithLocaleIdentifier:"
- "initWithMachServiceName:options:"
- "initWithSuiteName:"
- "initWithTimeInterval:sinceDate:"
- "initWithUUIDString:"
- "interfaceWithProtocol:"
- "invalidate"
- "isCASupported"
- "isCECSupported"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastKnownEstimates"
- "lastUpdatedDate"
- "latEnd"
- "latStart"
- "latestBalancingAuthority"
- "latestBalancingAuthorityWithError:"
- "latestMarginalEmissionForecast"
- "length"
- "loadBalancingAuthorityStatus"
- "loadConfigState"
- "loadNumberForPreferenceKey:"
- "loadRegistrations"
- "loadStringForPreferenceKey:"
- "locBundlePath"
- "log"
- "longEnd"
- "longStart"
- "lowercaseString"
- "managerWithID:locationBundlePath:"
- "minute"
- "mutableCopy"
- "now"
- "numberWithDouble:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "osBuildVersion"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postRequestForEndpoint:withData:"
- "query"
- "queryItemWithName:value:"
- "queryItemsMetaParams"
- "queue"
- "refetchInterval"
- "registerClientID:locationBundlePath:"
- "registerClientID:locationBundlePath:handler:"
- "release"
- "removeObjectForKey:"
- "requestWithURL:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "saveBalancingAuthority:"
- "saveBalancingAuthorityStatus:"
- "saveRegisteration:bundlePath:"
- "second"
- "self"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "setClientID:"
- "setConfigFetchDate:"
- "setConfigVersion:"
- "setConnection:"
- "setCurrentMarginalForecast:"
- "setDateFormat:"
- "setDefaults:"
- "setFakeConfigURL:"
- "setFakeDataDefaults:"
- "setFakeSecret:"
- "setFakeSecretVersion:"
- "setFakeServerURL:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setIsCASupported:"
- "setIsCECSupported:"
- "setLocBundlePath:"
- "setLocale:"
- "setLog:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setQueryItems:"
- "setQueue:"
- "setRemoteObjectInterface:"
- "setRequestCachePolicy:"
- "setServerURL:"
- "setTimeZone:"
- "setValue:forHTTPHeaderField:"
- "sharedInstance"
- "stringForKey:"
- "stringFromDate:"
- "stringWithCapacity:"
- "stringWithFormat:"
- "stringWithString:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "timeIntervalSince1970"
- "timeIntervalSinceNow"
- "timeIntervalSinceReferenceDate"
- "timeZoneWithAbbreviation:"
- "triggerBAUpdateWithHandler:"
- "unFixMarginalEmissionForecast"
- "unSetFakeConfigURL"
- "unSetFakeSecret"
- "unSetFakeSecretVersion"
- "unSetFakeServerURL"
- "updateBAClientID:handler:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@16@24@?32"
- "zone"

```
