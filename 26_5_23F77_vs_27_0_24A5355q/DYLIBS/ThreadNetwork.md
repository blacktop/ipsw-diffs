## ThreadNetwork

> `/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`

```diff

-335.0.200.0.0
-  __TEXT.__text: 0xd440
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0xbe8
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x113d
-  __TEXT.__oslogstring: 0x5fc
-  __TEXT.__gcc_except_tab: 0x164
-  __TEXT.__unwind_info: 0x338
-  __TEXT.__objc_classname: 0x180
-  __TEXT.__objc_methname: 0x242b
-  __TEXT.__objc_methtype: 0x880
-  __TEXT.__objc_stubs: 0x1080
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x2b0
+431.0.2.0.0
+  __TEXT.__text: 0xe7b8
+  __TEXT.__objc_methlist: 0xd50
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x160c
+  __TEXT.__oslogstring: 0xa8a
+  __TEXT.__gcc_except_tab: 0x190
+  __TEXT.__unwind_info: 0x3a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x468
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x610
+  __DATA_CONST.__objc_selrefs: 0x7a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x4e0
-  __AUTH_CONST.__objc_const: 0x1aa0
+  __AUTH_CONST.__cfstring: 0x800
+  __AUTH_CONST.__objc_const: 0x1b98
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xe8
+  __DATA.__objc_ivar: 0xf8
   __DATA.__data: 0x130
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B233D5CA-13B8-3EC4-A95C-0783D33C7785
-  Functions: 316
-  Symbols:   1143
-  CStrings:  541
+  UUID: 20FB08B2-B9F4-3D8A-AFC1-94FFE3D559F9
+  Functions: 358
+  Symbols:   1315
+  CStrings:  275
 
Symbols:
+ -[THClient CAInitDispatchQueue]
+ -[THClient CAInitDispatchQueue].cold.1
+ -[THClient apiCAQueue]
+ -[THClient currentEnvironment]
+ -[THClient enableCredentialSharingMode:]
+ -[THClient enableCredentialSharingModeInternally:]
+ -[THClient getAppAccessGroup]
+ -[THClient getAppBundleID]
+ -[THClient getAppName]
+ -[THClient getAppName].cold.1
+ -[THClient getAppTeamID]
+ -[THClient getTheProxyWithNwSignatureCompletion:]
+ -[THClient logAPIMetric:withError:isSuccess:isInternal:]
+ -[THClient logAPIMetric:withError:isSuccess:isInternal:].cold.1
+ -[THClient mAppBundleID]
+ -[THClient mAppName]
+ -[THClient mAppTeamID]
+ -[THClient rapportBrowseForPreferredNetworkWithCompletion:]
+ -[THClient rapportConnectForPreferredNetworkWithCompletion:]
+ -[THClient rapportSendForPreferredNetworkWithMessage:completion:]
+ -[THClient retrieveNetworkSignatureWithCompletion:]
+ -[THClient setApiCAQueue:]
+ -[THClient setMAppBundleID:]
+ -[THClient setMAppName:]
+ -[THClient setMAppTeamID:]
+ -[THClient startThreadBRScanInternally:]
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table6
+ GCC_except_table63
+ _AnalyticsSendEventLazy
+ _NSLog
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_IVAR_$_THClient._apiCAQueue
+ _OBJC_IVAR_$_THClient._mAppBundleID
+ _OBJC_IVAR_$_THClient._mAppName
+ _OBJC_IVAR_$_THClient._mAppTeamID
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemDelete
+ ___31-[THClient connectToXPCService]_block_invoke.85
+ ___31-[THClient connectToXPCService]_block_invoke.85.cold.1
+ ___40-[THClient enableCredentialSharingMode:]_block_invoke
+ ___40-[THClient enableCredentialSharingMode:]_block_invoke.150
+ ___40-[THClient enableCredentialSharingMode:]_block_invoke.cold.1
+ ___40-[THClient startThreadBRScanInternally:]_block_invoke
+ ___40-[THClient startThreadBRScanInternally:]_block_invoke_2
+ ___49-[THClient getTheProxyWithNwSignatureCompletion:]_block_invoke
+ ___49-[THClient getTheProxyWithNwSignatureCompletion:]_block_invoke.cold.1
+ ___50-[THClient enableCredentialSharingModeInternally:]_block_invoke
+ ___50-[THClient enableCredentialSharingModeInternally:]_block_invoke.143
+ ___50-[THClient enableCredentialSharingModeInternally:]_block_invoke.cold.1
+ ___51-[THClient retrieveNetworkSignatureWithCompletion:]_block_invoke
+ ___52-[THClient clientProxyWithErrorHandler:pingService:]_block_invoke.86
+ ___56-[THClient logAPIMetric:withError:isSuccess:isInternal:]_block_invoke
+ ___56-[THClient logAPIMetric:withError:isSuccess:isInternal:]_block_invoke.81
+ ___56-[THClient logAPIMetric:withError:isSuccess:isInternal:]_block_invoke.cold.1
+ ___59-[THClient rapportBrowseForPreferredNetworkWithCompletion:]_block_invoke
+ ___60-[THClient rapportConnectForPreferredNetworkWithCompletion:]_block_invoke
+ ___65-[THClient rapportSendForPreferredNetworkWithMessage:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e52_v40?0"NSData"8"NSData"16"NSString"24"NSError"32ls32l8
+ ___block_descriptor_40_e8_32s_e26_"NSMutableDictionary"8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e27_v24?0"NSSet"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSUUID"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e67_v24?0"THThreadNetworkCredentialsActiveDataSetRecord"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls40l8s32l8
+ ___block_descriptor_54_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_literal_global.106
+ ___block_literal_global.109
+ ___block_literal_global.117
+ ___block_literal_global.119
+ ___block_literal_global.89
+ ___block_literal_global.97
+ ___kCFBooleanTrue
+ _kSecAttrAccessGroup
+ _kSecAttrAccount
+ _kSecAttrService
+ _kSecClass
+ _kSecClassGenericPassword
+ _kSecReturnAttributes
+ _kSecValueData
+ _objc_claimAutoreleasedReturnValue
+ _objc_getProperty
+ _objc_msgSend$CAInitDispatchQueue
+ _objc_msgSend$alphanumericCharacterSet
+ _objc_msgSend$apiCAQueue
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$code
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$ctcsServerEnableCredentialSharingModeInternallyWithCompletion:
+ _objc_msgSend$ctcsServerEnableCredentialSharingModeWithCompletion:
+ _objc_msgSend$ctcsServerRapportBrowseForPreferredNetworkWithCompletion:
+ _objc_msgSend$ctcsServerRapportConnectForPreferredNetworkWithCompletion:
+ _objc_msgSend$ctcsServerRapportSendForPreferredNetworkWithMessage:completion:
+ _objc_msgSend$ctcsServerStartThreadBRScanInternallyWithCompletion:
+ _objc_msgSend$currentEnvironment
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dictionary
+ _objc_msgSend$firstObject
+ _objc_msgSend$getAppAccessGroup
+ _objc_msgSend$getAppBundleID
+ _objc_msgSend$getAppName
+ _objc_msgSend$getAppTeamID
+ _objc_msgSend$getTheProxyWithNwSignatureCompletion:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$invertedSet
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$logAPIMetric:withError:isSuccess:isInternal:
+ _objc_msgSend$mAppBundleID
+ _objc_msgSend$mAppName
+ _objc_msgSend$mAppTeamID
+ _objc_msgSend$mainBundle
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$retrieveNetworkSignatureWithCompletion:
+ _objc_msgSend$setMAppBundleID:
+ _objc_msgSend$setMAppName:
+ _objc_msgSend$setMAppTeamID:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_retain_x8
+ _objc_setProperty_atomic
+ _objc_sync_enter
+ _objc_sync_exit
- GCC_except_table26
- GCC_except_table32
- GCC_except_table35
- GCC_except_table5
- GCC_except_table52
- _OUTLINED_FUNCTION_7
- ___31-[THClient connectToXPCService]_block_invoke.7
- ___31-[THClient connectToXPCService]_block_invoke.7.cold.1
- ___52-[THClient clientProxyWithErrorHandler:pingService:]_block_invoke.8
- ___block_literal_global.11
- ___block_literal_global.17
- ___block_literal_global.28
- ___block_literal_global.31
- ___block_literal_global.39
- ___block_literal_global.41
CStrings:
+ "%s:Client:Connection - deallocated..."
+ "%s:Client:THClient.CAapi.queue - deallocated..."
+ "%s:Client:thread safe property queue - deallocated..."
+ "-[THClient enableCredentialSharingMode:]"
+ "-[THClient enableCredentialSharingMode:]_block_invoke"
+ "-[THClient enableCredentialSharingModeInternally:]"
+ "-[THClient enableCredentialSharingModeInternally:]_block_invoke"
+ "-[THClient getTheProxyWithNwSignatureCompletion:]"
+ "-[THClient getTheProxyWithNwSignatureCompletion:]_block_invoke"
+ "-[THClient rapportBrowseForPreferredNetworkWithCompletion:]"
+ "-[THClient rapportConnectForPreferredNetworkWithCompletion:]"
+ "-[THClient rapportSendForPreferredNetworkWithMessage:completion:]"
+ "-[THClient retrieveNetworkSignatureWithCompletion:]"
+ "-[THClient retrieveNetworkSignatureWithCompletion:]_block_invoke"
+ "-[THClient startThreadBRScanInternally:]"
+ "-[THClient startThreadBRScanInternally:]_block_invoke_2"
+ "."
+ ".beta"
+ ".beta."
+ ".debug"
+ ".debug."
+ ".dev"
+ ".dev."
+ ".staging"
+ ".staging."
+ "@\"NSMutableDictionary\"8@?0"
+ "CAInitDispatchQueue failed to initialize"
+ "CAInitDispatchQueue initialized successfully, getAppName: %@, AppTeamID: %@, AppBundleID: %@"
+ "CFBundleName"
+ "Client: %s - Retrieve Network Signature proxy check"
+ "Client: %s:%d - BR scan completed with %lu names, error: %@"
+ "Client: %s:%d - Credential Sharing Mode adminCode: %@, error: %@"
+ "Client: %s:%d - Enabling Credential Sharing Mode"
+ "Client: %s:%d - Proxy Call Back with error %@"
+ "Client: %s:%d - Retrieve Network Signature calling server proxy API"
+ "Client: %s:%d - Starting Thread BR mDNS scan"
+ "Client:Couldn't get flagstoneTHClientAPIInfo, as apiCAQueue queue object not initialized"
+ "Client:Triggered com.apple.Flagstone.flagstoneTHClientAPIInfo"
+ "Client:apiCAQueue not initialized,skipping analytics"
+ "Could not retrieve bundle ID, returning Unknown environment"
+ "Failed to get main bundle"
+ "NA"
+ "Rapport: Client: %s:%d - Initiating Rapport Browse for Credential Share"
+ "Rapport: Client: %s:%d - Initiating Rapport Connect for Credential Share"
+ "Rapport: Client: %s:%d - Initiating Rapport Send for Preferred Network with message"
+ "Success"
+ "THClient.CAapi.queue"
+ "[accessGroup] Keychain error %d"
+ "__teamid_local__"
+ "accessGroup:%@"
+ "api_current_environment"
+ "api_enum"
+ "api_is_internal"
+ "api_is_success"
+ "api_return_error_code"
+ "api_return_error_message"
+ "app_bundleID"
+ "app_name"
+ "app_teamID"
+ "com.apple.Flagstone.flagstoneTHClientAPIInfo"
+ "getAppName return null"
+ "getAppTeamID return null,as accessGroup is null"
+ "probe"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v40@?0@\"NSData\"8@\"NSData\"16@\"NSString\"24@\"NSError\"32"
- "%s : Client: Connection - deallocated..."
- "%s : Client: thread safe property queue - deallocated..."
- ".cxx_destruct"
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSString\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"THCredentials\""
- "@\"THNetworkSignature\""
- "@\"THThreadNetwork\""
- "@\"THThreadNetworkBorderAgent\""
- "@\"THThreadNetworkCredentials\""
- "@\"THThreadNetworkCredentialsActiveDataSetRecord\""
- "@\"THThreadNetworkCredentialsDataSet\""
- "@\"THThreadNetworkCredentialsStoreLocalClient\"16@0:8"
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8q16"
- "@28@0:8@?16B24"
- "@32@0:8@16@24"
- "@32@0:8q16@24"
- "@40@0:8@?16d24^@32"
- "@40@0:8q16@24@32"
- "@48@0:8@16@24@32@40"
- "@56@0:8*16i24*28i36@40@48"
- "@60@0:8@16@24@32C40@44@52"
- "@64@0:8@16@24@32@40@48@56"
- "@72@0:8@16@24@32C40@44@52@60B68"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "@92@0:8@16@24@32@40@48@56C64@68@76@84"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "BackingStoreDS"
- "C"
- "C16@0:8"
- "CTCSCreateXPCTransportInterface"
- "CTCSExpectedXPCInterfaceClassesForAllActiveDataSetRecords"
- "CTCSGetExpectedClassesForOptionsOverXPCInterface"
- "CTCSSetExpectedClassesForXPCBrokerInterface:"
- "CTCSXPCServiceProtocol"
- "NSCoding"
- "NSSecureCoding"
- "PANID"
- "PSKC"
- "PSKc"
- "T@\"NSData\",C,N,V_PANID"
- "T@\"NSData\",C,N,V_PSKc"
- "T@\"NSData\",C,N,V_dataSetArray"
- "T@\"NSData\",C,N,V_masterKey"
- "T@\"NSData\",R,N,V_PSKC"
- "T@\"NSData\",R,N,V_activeOperationalDataSet"
- "T@\"NSData\",R,N,V_borderAgentID"
- "T@\"NSData\",R,N,V_discriminatorId"
- "T@\"NSData\",R,N,V_extendedPANID"
- "T@\"NSData\",R,N,V_ipv4NwSignature"
- "T@\"NSData\",R,N,V_ipv4Signature"
- "T@\"NSData\",R,N,V_ipv6NwSignature"
- "T@\"NSData\",R,N,V_ipv6Signature"
- "T@\"NSData\",R,N,V_networkKey"
- "T@\"NSData\",R,N,V_panID"
- "T@\"NSDate\",R,N,V_creationDate"
- "T@\"NSDate\",R,N,V_lastModificationDate"
- "T@\"NSString\",C,N,V_passPhrase"
- "T@\"NSString\",C,N,V_userInfo"
- "T@\"NSString\",R,N,V_keychainAccessGroup"
- "T@\"NSString\",R,N,V_networkName"
- "T@\"NSString\",R,N,V_wifiPassword"
- "T@\"NSString\",R,N,V_wifiSSID"
- "T@\"NSUUID\",R,N,V_uniqueIdentifier"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "T@\"THCredentials\",R,N,V_credentialsRecord"
- "T@\"THNetworkSignature\",R,N,V_networkSignature"
- "T@\"THThreadNetwork\",R,N,V_network"
- "T@\"THThreadNetworkBorderAgent\",R,N,V_borderAgent"
- "T@\"THThreadNetworkCredentials\",&,N,V_credentials"
- "T@\"THThreadNetworkCredentials\",R,N,V_credentials"
- "T@\"THThreadNetworkCredentialsActiveDataSetRecord\",R,N,V_credentialsDataSetRecord"
- "T@\"THThreadNetworkCredentialsDataSet\",&,N,V_credentialsDataSet"
- "T@\"THThreadNetworkCredentialsDataSet\",R,N,V_credentialsDataSet"
- "TB,N,V_isActiveDevice"
- "TB,R"
- "TC,N,V_channel"
- "THCredentials"
- "THNetworkSignature"
- "THPreferredNetworkEntry"
- "THPreferredThreadNetwork"
- "THThreadNetwork"
- "THThreadNetworkBorderAgent"
- "THThreadNetworkCredentials"
- "THThreadNetworkCredentialsActiveDataSetRecord"
- "THThreadNetworkCredentialsDataSet"
- "THThreadNetworkCredentialsStoreRecord"
- "T^{dispatch_queue_s=},N,V_threadSafePropertyQueue"
- "ThreadCredentialsServerError"
- "XPCInterface"
- "^{dispatch_queue_s=}"
- "^{dispatch_queue_s=}16@0:8"
- "_PANID"
- "_PSKC"
- "_PSKc"
- "_activeOperationalDataSet"
- "_borderAgent"
- "_borderAgentID"
- "_channel"
- "_creationDate"
- "_credentials"
- "_credentialsDataSet"
- "_credentialsDataSetRecord"
- "_credentialsRecord"
- "_dataSetArray"
- "_discriminatorId"
- "_extendedPANID"
- "_ipv4NwSignature"
- "_ipv4Signature"
- "_ipv6NwSignature"
- "_ipv6Signature"
- "_isActiveDevice"
- "_isConnected"
- "_keychainAccessGroup"
- "_lastModificationDate"
- "_masterKey"
- "_network"
- "_networkKey"
- "_networkName"
- "_networkSignature"
- "_panID"
- "_passPhrase"
- "_threadSafePropertyQueue"
- "_uniqueIdentifier"
- "_userInfo"
- "_wifiPassword"
- "_wifiSSID"
- "_xpcConnection"
- "activeOperationalDataSet"
- "addObject:"
- "arrayWithCapacity:"
- "asynchronousRemoteObjectProxyWithErrorHandler:"
- "borderAgent"
- "borderAgentID"
- "callStackSymbols"
- "channel"
- "charValue"
- "checkPreferredNetworkForActiveOperationalDataset:completion:"
- "clientProxyWithErrorHandler:"
- "clientProxyWithErrorHandler:pingService:"
- "connectToXPCService"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countNonAppleRecordsWithCompletion:"
- "countPreferredFrozenRecordsWithCompletion:"
- "creationDate"
- "credentialsDataSet"
- "credentialsDataSetRecord"
- "credentialsRecord"
- "ctcsAddPreferredNetworkWithCompletionInternally:extendedPANId:borderAgentID:ipV4NwSignature:ipv6NwSignature:wifiSSID:wifiPassword:completion:"
- "ctcsCleanKeychainThreadNetworksWithCompletion:"
- "ctcsCleanPreferredAndFrozenThreadNetworksWithCompletion:"
- "ctcsDeleteActiveDataSetRecordWithUniqueIdentifier:completion:"
- "ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:"
- "ctcsDeletePreferredNetworkWithCompletion:"
- "ctcsIsPreferredNetworkForActiveOperationalDataset:completion:"
- "ctcsRetrieveActiveDataSetRecordWithUniqueIdentifier:completion:"
- "ctcsRetrieveOrGeneratePreferredNetworkInternallyWithCompletion:"
- "ctcsRetrievePreferredNetworkInternallyWithCompletion:"
- "ctcsServerAddPreferredNetworkWithCompletionInternally:extendedPANId:borderAgentID:ipV4NwSignature:ipv6NwSignature:wifiSSID:wifiPassword:completion:"
- "ctcsServerCleanKeychainThreadNetworksWithCompletion:"
- "ctcsServerCleanPreferredAndFrozenThreadNetworksWithCompletion:"
- "ctcsServerCountNonAppleRecordsWithCompletion:"
- "ctcsServerCountPreferredFrozenRecordsWithCompletion:"
- "ctcsServerDeleteActiveDataSetRecordForThreadBorderAgent:completion:"
- "ctcsServerDeleteActiveDataSetRecordWithUniqueIdentifier:completion:"
- "ctcsServerDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:"
- "ctcsServerDeletePreferredNetworkWithCompletion:"
- "ctcsServerRetrieveActiveDataSetRecordForThreadBorderAgent:completion:"
- "ctcsServerRetrieveActiveDataSetRecordInternallyWithXPANId:completion:"
- "ctcsServerRetrieveActiveDataSetRecordWithUniqueIdentifier:completion:"
- "ctcsServerRetrieveActiveDataSetRecordWithXPANId:completion:"
- "ctcsServerRetrieveAllActiveDataSetRecordsWithActiveFlag:completion:"
- "ctcsServerRetrieveIsPreferredNetworkAvailable:"
- "ctcsServerRetrieveListOfPreferredNetworkEntriesInternallyWithCompletion:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:"
- "ctcsServerRetrieveOrGeneratePreferredNetworkInternallyWithCompletion:"
- "ctcsServerRetrievePreferredNetworkInternallyOnMdnsAndSigWithCompletion:"
- "ctcsServerRetrievePreferredNetworkInternallyWithCompletion:"
- "ctcsServerRetrievePreferredNetworkWithCompletion:"
- "ctcsServerRetrievePreferredNetworkWithNoScanWithCompletion:"
- "ctcsServerStoreCachedAODasPreferredNetwork:completion:"
- "ctcsServerStoreThreadNetworkCredentialActiveDataSet:credentialsDataSet:completion:"
- "ctcsServerStoreThreadNetworkCredentialActiveDataSetInternally:network:credentialsDataSet:waitForSync:completion:"
- "ctcsStoreThreadNetworkCredentialActiveDataSetInternally:network:credentialsDataSet:waitForSync:completion:"
- "ctcsUpdatePreferredNetworkInternallyWithCompletion:"
- "ctcsValidateAODInternally:completion:"
- "dataSetArray"
- "dataWithBytes:length:"
- "dealloc"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "deleteCredentialsForBorderAgent:completion:"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "discriminatorId"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "extendedPANID"
- "getConnectionEntitlementValidity"
- "getConnectionEntitlementValidity:"
- "getTheProxyWithBoolCompletion:"
- "getTheProxyWithErrorParameterCompletion:"
- "getTheProxyWithPrefEntryCompletion:"
- "getTheProxyWithRecordCompletion:"
- "getTheProxyWithResultBlockCompletion:"
- "getTheProxyWithSetOfTHCredsParameterCompletion:"
- "getTheProxyWithTHCredsAndUuidParametersCompletion:"
- "getTheProxyWithTHCredsParameterCompletion:"
- "handleXPCConnectionInterrupted"
- "handleXPCConnectionInvalidated"
- "init"
- "initCommon"
- "initCommon:"
- "initPrefEntry:extendedPANID:ipv4Signature:ipv6Signature:wifiSSID:creationDate:lastModificationDate:credentialsRecord:"
- "initSignaturesWithArrays:ipv4BytesLen:ipv6Bytes:ipv6BytesLen:wifSSID:wifiPassword:"
- "initThreadCredentials:extendedPANID:borderAgentID:activeOperationalDataSet:PSKC:networkKey:channel:panID:creationDate:lastModificationDate:"
- "initWithBaDiscrId:"
- "initWithBorderAgent:credentialsDataSet:network:credentials:uniqueIdentifier:keychainAccessGroup:creationDate:lastModificationDate:"
- "initWithCoder:"
- "initWithDataSetArray:userInfo:"
- "initWithKeychainAccessGroup:"
- "initWithMachServiceName:options:"
- "initWithMasterKey:passPhrase:PSKc:channel:PANID:userInfo:"
- "initWithMasterKey:passPhrase:PSKc:channel:PANID:userInfo:credentialDataSet:isActiveDevice:"
- "initWithName:extendedPANID:"
- "initWithNetwork:credentials:uniqueIdentifier:keychainAccessGroup:creationDate:lastModificationDate:"
- "initWithSignatures:ipv6NwSignature:wifSSID:wifiPassword:"
- "initWithThreadNetwork:networkSignature:credentialsDataSetRecord:creationDate:lastModificationDate:userInfo:"
- "interfaceWithProtocol:"
- "invalidate"
- "ipv4NwSignature"
- "ipv4Signature"
- "ipv6NwSignature"
- "ipv6Signature"
- "isActiveDevice"
- "isConnected"
- "isConnectionValid:"
- "isConnectionValid:completion:"
- "isPreferredNetworkAvailableWithCompletion:"
- "keychainAccessGroup"
- "lastModificationDate"
- "length"
- "masterKey"
- "network"
- "networkKey"
- "networkName"
- "networkSignature"
- "numberWithDouble:"
- "numberWithUnsignedChar:"
- "panID"
- "passPhrase"
- "performXPCRequestBlock:timeout:error:"
- "ping:"
- "pingXPCService"
- "pingXPCServiceWithClientProxy:completion:"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "retrieveActiveDataSetRecordInternallyForExtendedPANID:completion:"
- "retrieveAllActiveCredentials:"
- "retrieveAllCredentials:"
- "retrieveCredentialsForBorderAgent:completion:"
- "retrieveCredentialsForExtendedPANID:completion:"
- "retrieveCredentialsForUUID:completion:"
- "retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:"
- "retrieveOrGeneratePreferredNetworkInternally:"
- "retrievePreferredCredentials:"
- "retrievePreferredCredentialsInternally:"
- "retrievePreferredNetworkInternallyOnMdnsAndSig:"
- "retrievePreferredNetworkWithNoScan:"
- "setChannel:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCredentials:"
- "setCredentialsDataSet:"
- "setDataSetArray:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsActiveDevice:"
- "setIsConnected:"
- "setMasterKey:"
- "setPANID:"
- "setPSKc:"
- "setPassPhrase:"
- "setRemoteObjectInterface:"
- "setThreadSafePropertyQueue:"
- "setUserInfo:"
- "setWithArray:"
- "setWithObjects:"
- "setXpcConnection:"
- "storeCachedAODasPreferredNetwork:completion:"
- "storeCredentialsForBorderAgent:activeOperationalDataSet:completion:"
- "storeCredentialsForBorderAgentInternally:networkName:extendedPANId:activeOperationalDataSet:completion:"
- "storeError:"
- "storeError:description:"
- "storeError:underlyingError:"
- "storeError:underlyingError:description:"
- "stringWithFormat:"
- "supportsSecureCoding"
- "synchronousClientProxyWithErrorHandler:"
- "synchronousRemoteObjectProxy"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "threadSafePropertyQueue"
- "uniqueIdentifier"
- "updatePreferredCredentialsInternally:"
- "updateUserInfo:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"THThreadNetworkCredentialsActiveDataSetRecord\"@\"NSError\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?Q@\"NSError\">16"
- "v24@0:8^{dispatch_queue_s=}16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSSet\"@\"NSError\">20"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSUUID\"@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"THThreadNetworkCredentialsActiveDataSetRecord\"@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?B>24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"THThreadNetworkCredentialsActiveDataSetRecord\"@\"NSError\">24"
- "v32@0:8@\"THThreadNetworkBorderAgent\"16@?<v@?@\"THThreadNetworkCredentialsActiveDataSetRecord\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSUUID\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v52@0:8@\"THThreadNetworkBorderAgent\"16@\"THThreadNetwork\"24@\"THThreadNetworkCredentialsDataSet\"32B40@?<v@?@\"NSUUID\"@\"NSError\">44"
- "v52@0:8@16@24@32B40@?44"
- "v56@0:8@16@24@32@40@?48"
- "v60@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@\"NSString\"40B48@?<v@?@\"NSSet\"@\"NSError\">52"
- "v60@0:8@16@24@32@40B48@?52"
- "v64@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSString\"48@?<v@?@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "v80@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSData\"48@\"NSString\"56@\"NSString\"64@?<v@?@\"NSError\">72"
- "v80@0:8@16@24@32@40@48@56@64@?72"
- "validateAODInternally:completion:"
- "wifiPassword"
- "wifiSSID"
- "xpcConnection"

```
