## ThreadNetwork

> `/System/Library/Frameworks/ThreadNetwork.framework/Versions/A/ThreadNetwork`

```diff

-265.0.53.0.0
-  __TEXT.__text: 0xe328
+275.0.104.0.0
+  __TEXT.__text: 0xffc0
   __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_methlist: 0x788
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x1366
-  __TEXT.__oslogstring: 0x49a
+  __TEXT.__objc_methlist: 0xb20
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x14ec
+  __TEXT.__oslogstring: 0x4d1
   __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__unwind_info: 0x380
-  __TEXT.__objc_classname: 0x11e
-  __TEXT.__objc_methname: 0x1c8a
-  __TEXT.__objc_methtype: 0x725
-  __TEXT.__objc_stubs: 0xda0
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__unwind_info: 0x3d8
+  __TEXT.__objc_classname: 0x164
+  __TEXT.__objc_methname: 0x21e8
+  __TEXT.__objc_methtype: 0x83a
+  __TEXT.__objc_stubs: 0xf60
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x98
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x508
+  __DATA_CONST.__objc_selrefs: 0x598
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x58
   __AUTH_CONST.__auth_got: 0x140
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x3a0
-  __AUTH_CONST.__objc_const: 0x1638
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0xa0
+  __AUTH_CONST.__cfstring: 0x4c0
+  __AUTH_CONST.__objc_const: 0x1a50
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0x130
   __DATA.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 54DFF5D2-83CD-3908-9047-B144988061C0
-  Functions: 317
-  Symbols:   723
-  CStrings:  456
+  UUID: A6CB5F2F-8742-332C-99A0-9C76C8FC4FD1
+  Functions: 362
+  Symbols:   845
+  CStrings:  522
 
Symbols:
+ +[THNetworkSignature supportsSecureCoding]
+ +[THPreferredNetworkEntry supportsSecureCoding]
+ +[THPreferredThreadNetwork supportsSecureCoding]
+ +[XPCInterface CTCSCreateXPCTransportInterface].cold.1
+ +[XPCInterface CTCSExpectedXPCInterfaceClassesForAllActiveDataSetRecords].cold.1
+ +[XPCInterface CTCSGetExpectedClassesForOptionsOverXPCInterface].cold.1
+ -[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:]
+ -[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]
+ -[THNetworkSignature .cxx_destruct]
+ -[THNetworkSignature encodeWithCoder:]
+ -[THNetworkSignature initSignaturesWithArrays:ipv4BytesLen:ipv6Bytes:ipv6BytesLen:wifSSID:wifiPassword:]
+ -[THNetworkSignature initWithCoder:]
+ -[THNetworkSignature initWithSignatures:ipv6NwSignature:wifSSID:wifiPassword:]
+ -[THNetworkSignature ipv4NwSignature]
+ -[THNetworkSignature ipv6NwSignature]
+ -[THNetworkSignature wifiPassword]
+ -[THNetworkSignature wifiSSID]
+ -[THPreferredNetworkEntry .cxx_destruct]
+ -[THPreferredNetworkEntry creationDate]
+ -[THPreferredNetworkEntry credentialsRecord]
+ -[THPreferredNetworkEntry encodeWithCoder:]
+ -[THPreferredNetworkEntry extendedPANID]
+ -[THPreferredNetworkEntry initPrefEntry:extendedPANID:ipv4Signature:ipv6Signature:wifiSSID:creationDate:lastModificationDate:credentialsRecord:]
+ -[THPreferredNetworkEntry initWithCoder:]
+ -[THPreferredNetworkEntry ipv4Signature]
+ -[THPreferredNetworkEntry ipv6Signature]
+ -[THPreferredNetworkEntry lastModificationDate]
+ -[THPreferredNetworkEntry networkName]
+ -[THPreferredNetworkEntry wifiSSID]
+ -[THPreferredThreadNetwork .cxx_destruct]
+ -[THPreferredThreadNetwork creationDate]
+ -[THPreferredThreadNetwork credentialsDataSetRecord]
+ -[THPreferredThreadNetwork encodeWithCoder:]
+ -[THPreferredThreadNetwork initWithCoder:]
+ -[THPreferredThreadNetwork initWithThreadNetwork:networkSignature:credentialsDataSetRecord:creationDate:lastModificationDate:userInfo:]
+ -[THPreferredThreadNetwork lastModificationDate]
+ -[THPreferredThreadNetwork networkSignature]
+ -[THPreferredThreadNetwork network]
+ -[THPreferredThreadNetwork setUserInfo:]
+ -[THPreferredThreadNetwork updateUserInfo:]
+ -[THPreferredThreadNetwork userInfo]
+ DispatchXPCConnectionQueueIfNecessaryAndWait.cold.1
+ DispatchXPCConnectionQueueIfNecessaryAndWait.cold.2
+ DispatchXPCConnectionQueueIfNecessaryAndWait.cold.3
+ OBJC_IVAR_$_THNetworkSignature._ipv4NwSignature
+ OBJC_IVAR_$_THNetworkSignature._ipv6NwSignature
+ OBJC_IVAR_$_THNetworkSignature._wifiPassword
+ OBJC_IVAR_$_THNetworkSignature._wifiSSID
+ OBJC_IVAR_$_THPreferredNetworkEntry._creationDate
+ OBJC_IVAR_$_THPreferredNetworkEntry._credentialsRecord
+ OBJC_IVAR_$_THPreferredNetworkEntry._extendedPANID
+ OBJC_IVAR_$_THPreferredNetworkEntry._ipv4Signature
+ OBJC_IVAR_$_THPreferredNetworkEntry._ipv6Signature
+ OBJC_IVAR_$_THPreferredNetworkEntry._lastModificationDate
+ OBJC_IVAR_$_THPreferredNetworkEntry._networkName
+ OBJC_IVAR_$_THPreferredNetworkEntry._wifiSSID
+ OBJC_IVAR_$_THPreferredThreadNetwork._creationDate
+ OBJC_IVAR_$_THPreferredThreadNetwork._credentialsDataSetRecord
+ OBJC_IVAR_$_THPreferredThreadNetwork._lastModificationDate
+ OBJC_IVAR_$_THPreferredThreadNetwork._network
+ OBJC_IVAR_$_THPreferredThreadNetwork._networkSignature
+ OBJC_IVAR_$_THPreferredThreadNetwork._userInfo
+ THLogHandleForCategory.cold.1
+ ThreadNetworkLoggingCategory.cold.1
+ _OBJC_CLASS_$_THNetworkSignature
+ _OBJC_CLASS_$_THPreferredNetworkEntry
+ _OBJC_CLASS_$_THPreferredThreadNetwork
+ _OBJC_METACLASS_$_THNetworkSignature
+ _OBJC_METACLASS_$_THPreferredNetworkEntry
+ _OBJC_METACLASS_$_THPreferredThreadNetwork
+ __129-[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]_block_invoke.75
+ __129-[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]_block_invoke.cold.1
+ __148-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:]_block_invoke.98
+ __148-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:]_block_invoke.98.cold.1
+ __148-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:]_block_invoke.cold.1
+ __153-[THClient ctcsAddPreferredNetworkWithCompletionInternally:extendedPANId:borderAgentID:ipV4NwSignature:ipv6NwSignature:wifiSSID:wifiPassword:completion:]_block_invoke.97
+ __153-[THClient ctcsAddPreferredNetworkWithCompletionInternally:extendedPANId:borderAgentID:ipV4NwSignature:ipv6NwSignature:wifiSSID:wifiPassword:completion:]_block_invoke.97.cold.1
+ __35-[THClient retrieveAllCredentials:]_block_invoke.88
+ __41-[THClient retrieveAllActiveCredentials:]_block_invoke.99
+ __41-[THClient retrievePreferredCredentials:]_block_invoke.90
+ __47-[THClient retrievePreferredNetworkWithNoScan:]_block_invoke.101
+ __50-[THClient retrieveCredentialsForUUID:completion:]_block_invoke.95
+ __51-[THClient retrievePreferredCredentialsInternally:]_block_invoke.94
+ __54-[THClient isPreferredNetworkAvailableWithCompletion:]_block_invoke.100
+ __55-[THClient deleteCredentialsForBorderAgent:completion:]_block_invoke.85
+ __56-[THClient storeCachedAODasPreferredNetwork:completion:]_block_invoke.87
+ __56-[THClient storeCachedAODasPreferredNetwork:completion:]_block_invoke.87.cold.1
+ __57-[THClient retrieveCredentialsForBorderAgent:completion:]_block_invoke.89
+ __57-[THClient retrieveOrGeneratePreferredNetworkInternally:]_block_invoke.93
+ __59-[THClient retrieveCredentialsForExtendedPANID:completion:]_block_invoke.91
+ __59-[THClient retrievePreferredNetworkInternallyOnMdnsAndSig:]_block_invoke.92
+ __72-[THClient checkPreferredNetworkForActiveOperationalDataset:completion:]_block_invoke.96
+ __72-[THClient checkPreferredNetworkForActiveOperationalDataset:completion:]_block_invoke.96.cold.1
+ __79-[THClient storeCredentialsForBorderAgent:activeOperationalDataSet:completion:]_block_invoke.86
+ __79-[THClient storeCredentialsForBorderAgent:activeOperationalDataSet:completion:]_block_invoke.86.cold.1
+ __DispatchXPCConnectionQueueIfNecessaryAndWait_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS_THNetworkSignature
+ __OBJC_$_CLASS_METHODS_THPreferredNetworkEntry
+ __OBJC_$_CLASS_METHODS_THPreferredThreadNetwork
+ __OBJC_$_CLASS_PROP_LIST_THNetworkSignature
+ __OBJC_$_CLASS_PROP_LIST_THPreferredNetworkEntry
+ __OBJC_$_CLASS_PROP_LIST_THPreferredThreadNetwork
+ __OBJC_$_INSTANCE_METHODS_THNetworkSignature
+ __OBJC_$_INSTANCE_METHODS_THPreferredNetworkEntry
+ __OBJC_$_INSTANCE_METHODS_THPreferredThreadNetwork
+ __OBJC_$_INSTANCE_VARIABLES_THNetworkSignature
+ __OBJC_$_INSTANCE_VARIABLES_THPreferredNetworkEntry
+ __OBJC_$_INSTANCE_VARIABLES_THPreferredThreadNetwork
+ __OBJC_$_PROP_LIST_THNetworkSignature
+ __OBJC_$_PROP_LIST_THPreferredNetworkEntry
+ __OBJC_$_PROP_LIST_THPreferredThreadNetwork
+ __OBJC_CLASS_PROTOCOLS_$_THNetworkSignature
+ __OBJC_CLASS_PROTOCOLS_$_THPreferredNetworkEntry
+ __OBJC_CLASS_PROTOCOLS_$_THPreferredThreadNetwork
+ __OBJC_CLASS_RO_$_THNetworkSignature
+ __OBJC_CLASS_RO_$_THPreferredNetworkEntry
+ __OBJC_CLASS_RO_$_THPreferredThreadNetwork
+ __OBJC_METACLASS_RO_$_THNetworkSignature
+ __OBJC_METACLASS_RO_$_THPreferredNetworkEntry
+ __OBJC_METACLASS_RO_$_THPreferredThreadNetwork
+ ___129-[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]_block_invoke
+ ___148-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:]_block_invoke
+ __block_literal_global.68
+ _objc_msgSend$credentialsDataSetRecord
+ _objc_msgSend$credentialsRecord
+ _objc_msgSend$ctcsServerDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:
+ _objc_msgSend$ctcsServerRetrieveListOfPreferredNetworkEntriesInternallyWithCompletion:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$initPrefEntry:extendedPANID:ipv4Signature:ipv6Signature:wifiSSID:creationDate:lastModificationDate:credentialsRecord:
+ _objc_msgSend$initWithSignatures:ipv6NwSignature:wifSSID:wifiPassword:
+ _objc_msgSend$initWithThreadNetwork:networkSignature:credentialsDataSetRecord:creationDate:lastModificationDate:userInfo:
+ _objc_msgSend$ipv4NwSignature
+ _objc_msgSend$ipv4Signature
+ _objc_msgSend$ipv6NwSignature
+ _objc_msgSend$ipv6Signature
+ _objc_msgSend$networkSignature
+ _objc_msgSend$wifiPassword
+ _objc_msgSend$wifiSSID
+ dispatch_get_xpc_connection_queue.cold.1
- -[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:]
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- __118-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:]_block_invoke.93
- __118-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:]_block_invoke.93.cold.1
- __118-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:]_block_invoke.cold.1
- __153-[THClient ctcsAddPreferredNetworkWithCompletionInternally:extendedPANId:borderAgentID:ipV4NwSignature:ipv6NwSignature:wifiSSID:wifiPassword:completion:]_block_invoke.92
- __153-[THClient ctcsAddPreferredNetworkWithCompletionInternally:extendedPANId:borderAgentID:ipV4NwSignature:ipv6NwSignature:wifiSSID:wifiPassword:completion:]_block_invoke.92.cold.1
- __35-[THClient retrieveAllCredentials:]_block_invoke.78
- __41-[THClient retrieveAllActiveCredentials:]_block_invoke.94
- __41-[THClient retrievePreferredCredentials:]_block_invoke.85
- __47-[THClient retrievePreferredNetworkWithNoScan:]_block_invoke.96
- __50-[THClient retrieveCredentialsForUUID:completion:]_block_invoke.90
- __51-[THClient retrievePreferredCredentialsInternally:]_block_invoke.89
- __54-[THClient isPreferredNetworkAvailableWithCompletion:]_block_invoke.95
- __55-[THClient deleteCredentialsForBorderAgent:completion:]_block_invoke.75
- __56-[THClient storeCachedAODasPreferredNetwork:completion:]_block_invoke.77
- __56-[THClient storeCachedAODasPreferredNetwork:completion:]_block_invoke.77.cold.1
- __57-[THClient retrieveCredentialsForBorderAgent:completion:]_block_invoke.84
- __57-[THClient retrieveOrGeneratePreferredNetworkInternally:]_block_invoke.88
- __59-[THClient retrieveCredentialsForExtendedPANID:completion:]_block_invoke.86
- __59-[THClient retrievePreferredNetworkInternallyOnMdnsAndSig:]_block_invoke.87
- __72-[THClient checkPreferredNetworkForActiveOperationalDataset:completion:]_block_invoke.91
- __72-[THClient checkPreferredNetworkForActiveOperationalDataset:completion:]_block_invoke.91.cold.1
- __79-[THClient storeCredentialsForBorderAgent:activeOperationalDataSet:completion:]_block_invoke.76
- __79-[THClient storeCredentialsForBorderAgent:activeOperationalDataSet:completion:]_block_invoke.76.cold.1
- ___118-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:]_block_invoke
- __block_literal_global.64
- _objc_msgSend$ctcsServerDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:
CStrings:
+ "-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:]_block_invoke"
+ "-[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]"
+ "-[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]_block_invoke"
+ "@\"THCredentials\""
+ "@\"THNetworkSignature\""
+ "@\"THThreadNetworkCredentialsActiveDataSetRecord\""
+ "@48@0:8@16@24@32@40"
+ "@56@0:8*16i24*28i36@40@48"
+ "Client: %s:%d - Read list of Preferred Network Entries"
+ "Failed to retrieve Preferred Network Entry"
+ "T@\"NSData\",R,N,V_ipv4NwSignature"
+ "T@\"NSData\",R,N,V_ipv4Signature"
+ "T@\"NSData\",R,N,V_ipv6NwSignature"
+ "T@\"NSData\",R,N,V_ipv6Signature"
+ "T@\"NSString\",R,N,V_wifiPassword"
+ "T@\"NSString\",R,N,V_wifiSSID"
+ "T@\"THCredentials\",R,N,V_credentialsRecord"
+ "T@\"THNetworkSignature\",R,N,V_networkSignature"
+ "T@\"THThreadNetworkCredentialsActiveDataSetRecord\",R,N,V_credentialsDataSetRecord"
+ "THNetworkSignature"
+ "THPreferredNetworkEntry"
+ "THPreferredThreadNetwork"
+ "_credentialsDataSetRecord"
+ "_credentialsRecord"
+ "_ipv4NwSignature"
+ "_ipv4Signature"
+ "_ipv6NwSignature"
+ "_ipv6Signature"
+ "_networkSignature"
+ "_wifiPassword"
+ "_wifiSSID"
+ "credentialsDataSetRecord"
+ "credentialsRecord"
+ "creds"
+ "ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:"
+ "ctcsServerDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:"
+ "ctcsServerRetrieveListOfPreferredNetworkEntriesInternallyWithCompletion:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:"
+ "dataWithBytes:length:"
+ "initPrefEntry:extendedPANID:ipv4Signature:ipv6Signature:wifiSSID:creationDate:lastModificationDate:credentialsRecord:"
+ "initSignaturesWithArrays:ipv4BytesLen:ipv6Bytes:ipv6BytesLen:wifSSID:wifiPassword:"
+ "initWithSignatures:ipv6NwSignature:wifSSID:wifiPassword:"
+ "initWithThreadNetwork:networkSignature:credentialsDataSetRecord:creationDate:lastModificationDate:userInfo:"
+ "ipv4"
+ "ipv4NwSignature"
+ "ipv4Signature"
+ "ipv6"
+ "ipv6NwSignature"
+ "ipv6Signature"
+ "networkSignature"
+ "passwd"
+ "retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:"
+ "sig"
+ "ssid"
+ "ui"
+ "updateUserInfo:"
+ "v60@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@\"NSString\"40B48@?<v@?@\"NSSet\"@\"NSError\">52"
+ "v60@0:8@16@24@32@40B48@?52"
+ "v64@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSString\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24@32@40@48@?56"
+ "wifiPassword"
+ "wifiSSID"
+ "wifissid"
- "-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:]_block_invoke"
- "ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:"
- "ctcsServerDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:"
- "v48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"

```
