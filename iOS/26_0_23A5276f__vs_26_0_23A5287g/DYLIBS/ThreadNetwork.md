## ThreadNetwork

> `/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`

```diff

-325.0.0.0.0
-  __TEXT.__text: 0xe7e8
+328.0.0.0.0
+  __TEXT.__text: 0xc9dc
   __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0xb20
+  __TEXT.__objc_methlist: 0xbb8
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x14ec
-  __TEXT.__oslogstring: 0x4d1
-  __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__unwind_info: 0x3c0
-  __TEXT.__objc_classname: 0x164
-  __TEXT.__objc_methname: 0x21e8
-  __TEXT.__objc_methtype: 0x83a
-  __TEXT.__objc_stubs: 0xf60
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x2c8
+  __TEXT.__cstring: 0xfac
+  __TEXT.__oslogstring: 0x4f6
+  __TEXT.__gcc_except_tab: 0x164
+  __TEXT.__unwind_info: 0x310
+  __TEXT.__objc_classname: 0x180
+  __TEXT.__objc_methname: 0x2379
+  __TEXT.__objc_methtype: 0x864
+  __TEXT.__objc_stubs: 0x1040
+  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__const: 0x288
   __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x598
+  __DATA_CONST.__objc_selrefs: 0x5f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __AUTH_CONST.__auth_got: 0x228
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x4c0
-  __AUTH_CONST.__objc_const: 0x1a50
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0x4e0
+  __AUTH_CONST.__objc_const: 0x1a90
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0x130

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6E1B7D43-B98B-3C8E-8DCD-43FBF2FA0810
-  Functions: 344
-  Symbols:   1196
-  CStrings:  522
+  UUID: 7CDCAEA8-416D-3D37-9D06-02CC52FE9974
+  Functions: 306
+  Symbols:   1128
+  CStrings:  524
 
Symbols:
+ +[NSError(ThreadCredentialsServerError) storeError:]
+ +[NSError(ThreadCredentialsServerError) storeError:description:]
+ +[NSError(ThreadCredentialsServerError) storeError:underlyingError:]
+ +[NSError(ThreadCredentialsServerError) storeError:underlyingError:description:]
+ -[THClient getTheProxyWithBoolCompletion:]
+ -[THClient getTheProxyWithErrorParameterCompletion:]
+ -[THClient getTheProxyWithPrefEntryCompletion:]
+ -[THClient getTheProxyWithRecordCompletion:]
+ -[THClient getTheProxyWithResultBlockCompletion:]
+ -[THClient getTheProxyWithSetOfTHCredsParameterCompletion:]
+ -[THClient getTheProxyWithTHCredsAndUuidParametersCompletion:]
+ -[THClient getTheProxyWithTHCredsParameterCompletion:]
+ GCC_except_table26
+ GCC_except_table35
+ GCC_except_table43
+ GCC_except_table46
+ GCC_except_table5
+ GCC_except_table52
+ _NSUnderlyingErrorKey
+ _ThreadCredentialsStoreErrorDomain
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSError_$_ThreadCredentialsServerError
+ __OBJC_$_CATEGORY_NSError_$_ThreadCredentialsServerError
+ ___42-[THClient getTheProxyWithBoolCompletion:]_block_invoke
+ ___42-[THClient getTheProxyWithBoolCompletion:]_block_invoke.cold.1
+ ___44-[THClient getTheProxyWithRecordCompletion:]_block_invoke
+ ___44-[THClient getTheProxyWithRecordCompletion:]_block_invoke.cold.1
+ ___47-[THClient getTheProxyWithPrefEntryCompletion:]_block_invoke
+ ___47-[THClient getTheProxyWithPrefEntryCompletion:]_block_invoke.cold.1
+ ___49-[THClient getTheProxyWithResultBlockCompletion:]_block_invoke
+ ___49-[THClient getTheProxyWithResultBlockCompletion:]_block_invoke.cold.1
+ ___52-[THClient getTheProxyWithErrorParameterCompletion:]_block_invoke
+ ___52-[THClient getTheProxyWithErrorParameterCompletion:]_block_invoke.cold.1
+ ___54-[THClient getTheProxyWithTHCredsParameterCompletion:]_block_invoke
+ ___54-[THClient getTheProxyWithTHCredsParameterCompletion:]_block_invoke.cold.1
+ ___59-[THClient getTheProxyWithSetOfTHCredsParameterCompletion:]_block_invoke
+ ___59-[THClient getTheProxyWithSetOfTHCredsParameterCompletion:]_block_invoke.cold.1
+ ___62-[THClient getTheProxyWithTHCredsAndUuidParametersCompletion:]_block_invoke
+ ___62-[THClient getTheProxyWithTHCredsAndUuidParametersCompletion:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_73_e8_32s40bs48r56r64w_e5_v8?0lw64l8r48l8r56l8s40l8s32l8
+ ___block_literal_global.39
+ ___block_literal_global.41
+ _objc_msgSend$getTheProxyWithBoolCompletion:
+ _objc_msgSend$getTheProxyWithErrorParameterCompletion:
+ _objc_msgSend$getTheProxyWithPrefEntryCompletion:
+ _objc_msgSend$getTheProxyWithRecordCompletion:
+ _objc_msgSend$getTheProxyWithResultBlockCompletion:
+ _objc_msgSend$getTheProxyWithSetOfTHCredsParameterCompletion:
+ _objc_msgSend$getTheProxyWithTHCredsAndUuidParametersCompletion:
+ _objc_msgSend$getTheProxyWithTHCredsParameterCompletion:
+ _objc_msgSend$storeError:underlyingError:description:
- GCC_except_table13
- GCC_except_table15
- GCC_except_table18
- GCC_except_table21
- GCC_except_table3
- GCC_except_table42
- GCC_except_table45
- GCC_except_table6
- GCC_except_table8
- ___115-[THClient storeCredentialsForBorderAgentInternally:networkName:extendedPANId:activeOperationalDataSet:completion:]_block_invoke.59
- ___115-[THClient storeCredentialsForBorderAgentInternally:networkName:extendedPANId:activeOperationalDataSet:completion:]_block_invoke.cold.1
- ___118-[THClient ctcsStoreThreadNetworkCredentialActiveDataSetInternally:network:credentialsDataSet:waitForSync:completion:]_block_invoke.40
- ___118-[THClient ctcsStoreThreadNetworkCredentialActiveDataSetInternally:network:credentialsDataSet:waitForSync:completion:]_block_invoke.cold.1
- ___129-[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]_block_invoke.67
- ___129-[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]_block_invoke.cold.1
- ___148-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:]_block_invoke.88
- ___148-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:]_block_invoke.88.cold.1
- ___153-[THClient ctcsAddPreferredNetworkWithCompletionInternally:extendedPANId:borderAgentID:ipV4NwSignature:ipv6NwSignature:wifiSSID:wifiPassword:completion:]_block_invoke.87
- ___153-[THClient ctcsAddPreferredNetworkWithCompletionInternally:extendedPANId:borderAgentID:ipV4NwSignature:ipv6NwSignature:wifiSSID:wifiPassword:completion:]_block_invoke.87.cold.1
- ___22-[THClient initCommon]_block_invoke
- ___23-[THClient initCommon:]_block_invoke
- ___35-[THClient retrieveAllCredentials:]_block_invoke.78
- ___35-[THClient retrieveAllCredentials:]_block_invoke.cold.1
- ___41-[THClient retrieveAllActiveCredentials:]_block_invoke.89
- ___41-[THClient retrieveAllActiveCredentials:]_block_invoke.cold.1
- ___41-[THClient retrievePreferredCredentials:]_block_invoke.80
- ___41-[THClient retrievePreferredCredentials:]_block_invoke.cold.1
- ___44-[THClient getConnectionEntitlementValidity]_block_invoke.39
- ___44-[THClient getConnectionEntitlementValidity]_block_invoke.39.cold.1
- ___45-[THClient getConnectionEntitlementValidity:]_block_invoke.38
- ___45-[THClient getConnectionEntitlementValidity:]_block_invoke.38.cold.1
- ___45-[THClient validateAODInternally:completion:]_block_invoke.66
- ___45-[THClient validateAODInternally:completion:]_block_invoke.cold.1
- ___47-[THClient retrievePreferredNetworkWithNoScan:]_block_invoke.91
- ___47-[THClient retrievePreferredNetworkWithNoScan:]_block_invoke.cold.1
- ___49-[THClient updatePreferredCredentialsInternally:]_block_invoke.65
- ___49-[THClient updatePreferredCredentialsInternally:]_block_invoke.cold.1
- ___50-[THClient retrieveCredentialsForUUID:completion:]_block_invoke.85
- ___50-[THClient retrieveCredentialsForUUID:completion:]_block_invoke.cold.1
- ___51-[THClient retrievePreferredCredentialsInternally:]_block_invoke.84
- ___51-[THClient retrievePreferredCredentialsInternally:]_block_invoke.cold.1
- ___53-[THClient ctcsDeletePreferredNetworkWithCompletion:]_block_invoke.47
- ___53-[THClient ctcsDeletePreferredNetworkWithCompletion:]_block_invoke.cold.1
- ___54-[THClient isPreferredNetworkAvailableWithCompletion:]_block_invoke.90
- ___54-[THClient isPreferredNetworkAvailableWithCompletion:]_block_invoke.cold.1
- ___55-[THClient deleteCredentialsForBorderAgent:completion:]_block_invoke.75
- ___55-[THClient deleteCredentialsForBorderAgent:completion:]_block_invoke.cold.1
- ___56-[THClient storeCachedAODasPreferredNetwork:completion:]_block_invoke.77
- ___56-[THClient storeCachedAODasPreferredNetwork:completion:]_block_invoke.77.cold.1
- ___57-[THClient retrieveCredentialsForBorderAgent:completion:]_block_invoke.79
- ___57-[THClient retrieveCredentialsForBorderAgent:completion:]_block_invoke.cold.1
- ___57-[THClient retrieveOrGeneratePreferredNetworkInternally:]_block_invoke.83
- ___57-[THClient retrieveOrGeneratePreferredNetworkInternally:]_block_invoke.cold.1
- ___58-[THClient ctcsCleanKeychainThreadNetworksWithCompletion:]_block_invoke.49
- ___58-[THClient ctcsCleanKeychainThreadNetworksWithCompletion:]_block_invoke.cold.1
- ___59-[THClient retrieveCredentialsForExtendedPANID:completion:]_block_invoke.81
- ___59-[THClient retrieveCredentialsForExtendedPANID:completion:]_block_invoke.cold.1
- ___59-[THClient retrievePreferredNetworkInternallyOnMdnsAndSig:]_block_invoke.82
- ___59-[THClient retrievePreferredNetworkInternallyOnMdnsAndSig:]_block_invoke.cold.1
- ___65-[THClient ctcsRetrievePreferredNetworkInternallyWithCompletion:]_block_invoke.45
- ___65-[THClient ctcsRetrievePreferredNetworkInternallyWithCompletion:]_block_invoke.cold.1
- ___68-[THClient ctcsCleanPreferredAndFrozenThreadNetworksWithCompletion:]_block_invoke.48
- ___68-[THClient ctcsCleanPreferredAndFrozenThreadNetworksWithCompletion:]_block_invoke.cold.1
- ___72-[THClient checkPreferredNetworkForActiveOperationalDataset:completion:]_block_invoke.86
- ___72-[THClient checkPreferredNetworkForActiveOperationalDataset:completion:]_block_invoke.86.cold.1
- ___73-[THClient ctcsDeleteActiveDataSetRecordWithUniqueIdentifier:completion:]_block_invoke.42
- ___73-[THClient ctcsDeleteActiveDataSetRecordWithUniqueIdentifier:completion:]_block_invoke.cold.1
- ___75-[THClient ctcsRetrieveActiveDataSetRecordWithUniqueIdentifier:completion:]_block_invoke.43
- ___75-[THClient ctcsRetrieveActiveDataSetRecordWithUniqueIdentifier:completion:]_block_invoke.cold.1
- ___75-[THClient ctcsRetrieveOrGeneratePreferredNetworkInternallyWithCompletion:]_block_invoke.46
- ___75-[THClient ctcsRetrieveOrGeneratePreferredNetworkInternallyWithCompletion:]_block_invoke.cold.1
- ___77-[THClient retrieveActiveDataSetRecordInternallyForExtendedPANID:completion:]_block_invoke.60
- ___77-[THClient retrieveActiveDataSetRecordInternallyForExtendedPANID:completion:]_block_invoke.cold.1
- ___79-[THClient storeCredentialsForBorderAgent:activeOperationalDataSet:completion:]_block_invoke.76
- ___79-[THClient storeCredentialsForBorderAgent:activeOperationalDataSet:completion:]_block_invoke.76.cold.1
- ___block_descriptor_40_e17_v16?0"NSError"8l
- ___block_descriptor_48_e8_32r40w_e5_v8?0lw40l8r32l8
- ___block_descriptor_48_e8_32r_e20_v20?0B8"NSError"12lr32l8
- ___block_descriptor_56_e8_32s40r48w_e5_v8?0lw48l8r40l8s32l8
- _objc_msgSend$isConnectionValid:
- _objc_msgSend$isConnectionValid:completion:
CStrings:
+ "-[THClient getTheProxyWithBoolCompletion:]_block_invoke"
+ "-[THClient getTheProxyWithErrorParameterCompletion:]_block_invoke"
+ "-[THClient getTheProxyWithPrefEntryCompletion:]_block_invoke"
+ "-[THClient getTheProxyWithRecordCompletion:]_block_invoke"
+ "-[THClient getTheProxyWithResultBlockCompletion:]_block_invoke"
+ "-[THClient getTheProxyWithSetOfTHCredsParameterCompletion:]_block_invoke"
+ "-[THClient getTheProxyWithTHCredsAndUuidParametersCompletion:]_block_invoke"
+ "-[THClient getTheProxyWithTHCredsParameterCompletion:]_block_invoke"
+ "@24@0:8q16"
+ "@32@0:8q16@24"
+ "@40@0:8q16@24@32"
+ "ThreadCredentialsServerError"
+ "ThreadCredentialsStore"
+ "XPC Client - isConnected: %@"
+ "XPC Client - set connected: %@"
+ "getTheProxyWithBoolCompletion:"
+ "getTheProxyWithErrorParameterCompletion:"
+ "getTheProxyWithPrefEntryCompletion:"
+ "getTheProxyWithRecordCompletion:"
+ "getTheProxyWithResultBlockCompletion:"
+ "getTheProxyWithSetOfTHCredsParameterCompletion:"
+ "getTheProxyWithTHCredsAndUuidParametersCompletion:"
+ "getTheProxyWithTHCredsParameterCompletion:"
+ "storeError:"
+ "storeError:underlyingError:"
+ "storeError:underlyingError:description:"
+ "synchronousRemoteObjectProxyWithErrorHandler: %@"
- "-[THClient ctcsCleanKeychainThreadNetworksWithCompletion:]_block_invoke"
- "-[THClient ctcsCleanPreferredAndFrozenThreadNetworksWithCompletion:]_block_invoke"
- "-[THClient ctcsDeleteActiveDataSetRecordWithUniqueIdentifier:completion:]_block_invoke"
- "-[THClient ctcsDeletePreferredNetworkWithCompletion:]_block_invoke"
- "-[THClient ctcsRetrieveActiveDataSetRecordWithUniqueIdentifier:completion:]_block_invoke"
- "-[THClient ctcsRetrieveOrGeneratePreferredNetworkInternallyWithCompletion:]_block_invoke"
- "-[THClient ctcsRetrievePreferredNetworkInternallyWithCompletion:]_block_invoke"
- "-[THClient ctcsStoreThreadNetworkCredentialActiveDataSetInternally:network:credentialsDataSet:waitForSync:completion:]_block_invoke"
- "-[THClient deleteCredentialsForBorderAgent:completion:]_block_invoke"
- "-[THClient retrieveActiveDataSetRecordInternallyForExtendedPANID:completion:]_block_invoke"
- "-[THClient retrieveAllActiveCredentials:]_block_invoke"
- "-[THClient retrieveAllCredentials:]_block_invoke"
- "-[THClient retrieveCredentialsForBorderAgent:completion:]_block_invoke"
- "-[THClient retrieveCredentialsForExtendedPANID:completion:]_block_invoke"
- "-[THClient retrieveCredentialsForUUID:completion:]_block_invoke"
- "-[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]_block_invoke"
- "-[THClient retrieveOrGeneratePreferredNetworkInternally:]_block_invoke"
- "-[THClient retrievePreferredCredentials:]_block_invoke"
- "-[THClient retrievePreferredCredentialsInternally:]_block_invoke"
- "-[THClient retrievePreferredNetworkInternallyOnMdnsAndSig:]_block_invoke"
- "-[THClient retrievePreferredNetworkWithNoScan:]_block_invoke"
- "-[THClient storeCredentialsForBorderAgentInternally:networkName:extendedPANId:activeOperationalDataSet:completion:]_block_invoke"
- "-[THClient updatePreferredCredentialsInternally:]_block_invoke"
- "-[THClient validateAODInternally:completion:]_block_invoke"
- "CTCS XPC Client - isConnected: %@"
- "remoteObjectProxyWithErrorHandler: %@"

```
