## CoreThreadCommissionerServiced

> `/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced`

```diff

-335.0.17.0.0
-  __TEXT.__text: 0x573c8
+335.0.19.0.0
+  __TEXT.__text: 0x59978
   __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_stubs: 0x3220
-  __TEXT.__objc_methlist: 0x20a8
-  __TEXT.__cstring: 0x8016
-  __TEXT.__objc_methname: 0x56ab
+  __TEXT.__objc_stubs: 0x32a0
+  __TEXT.__objc_methlist: 0x2144
+  __TEXT.__cstring: 0x88c1
+  __TEXT.__objc_methname: 0x575d
   __TEXT.__objc_classname: 0x2ea
-  __TEXT.__objc_methtype: 0x165d
+  __TEXT.__objc_methtype: 0x16a8
   __TEXT.__const: 0x138
-  __TEXT.__gcc_except_tab: 0x1cf4
-  __TEXT.__oslogstring: 0x92e1
-  __TEXT.__unwind_info: 0x1090
+  __TEXT.__gcc_except_tab: 0x1fac
+  __TEXT.__oslogstring: 0x9954
+  __TEXT.__unwind_info: 0x1100
   __DATA_CONST.__auth_got: 0x568
   __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xce0
-  __DATA_CONST.__cfstring: 0x1300
+  __DATA_CONST.__const: 0xd30
+  __DATA_CONST.__cfstring: 0x1380
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA.__objc_const: 0x2c10
-  __DATA.__objc_selrefs: 0x11b0
+  __DATA.__objc_const: 0x2c88
+  __DATA.__objc_selrefs: 0x11d0
   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x430

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A721401B-67A6-3548-BCCA-400588E341E2
-  Functions: 1321
+  UUID: 28B9CC01-57E2-321E-8DF7-5B312C595D02
+  Functions: 1345
   Symbols:   262
-  CStrings:  2593
+  CStrings:  2660
 
CStrings:
+ " Server: %s Check for User Permission ...\n"
+ "%s creds are NULL #MOS !!"
+ "%s, 3P credentials fetched are:"
+ "%s, Failed to fetch credentials or no records found"
+ "%s, Request to count 3P active dataset records."
+ "%s, Request to count frozen preferred network records."
+ "%s, Total credentials: %lu, 3P saved Border Agent credentials: %lu"
+ "%s: Failed to count non-Apple records"
+ "%s: Freezing Preferred Network : %@"
+ "%s: No 3P credentials found, proceeding with deletion"
+ "%s: Request to fetch active dataset record with xpanid %@"
+ "%s: Request to validate network with MDNS %@, BA ID: %@"
+ "%s: Server: Got response from Store ...\n"
+ "%s: Server: Got response from Store, count: %lu, error: %@\n"
+ "%s: Server: Got response from Store, error : %@, preferred network available? %d \n"
+ "%s: Server: Retrieving Preferred Network for Internal Clients ...\n"
+ "%s: Server: Retrieving or generate Preferred Network for Internal Clients ...\n"
+ "%s: Server: checking if preferred network is available ...\n"
+ "%s: Server: counting 3P saved Border Agent credentials...\n"
+ "%s: Server: counting frozen preferred network records...\n"
+ "%s: Silently ignoring deletion request due to %lu 3P credential(s) present"
+ "%s: WiFi is off, error: %@"
+ "%s:%d: Deleting below frozen records from com.apple.frozen.network failed"
+ "%s:%d: Deleting frozen record, Deletion result :(err=%d)"
+ "%s:%d: Failed to create black list record to verify."
+ "%s:%d: Failed to create query to delete frozen thread networks"
+ "%s:%d: No Frozen Preferred Networks in Database "
+ "-[CTCSXPCService ctcsServerCountNonAppleRecordsWithCompletion:]"
+ "-[CTCSXPCService ctcsServerCountNonAppleRecordsWithCompletion:]_block_invoke_2"
+ "-[CTCSXPCService ctcsServerCountPreferredFrozenRecordsWithCompletion:]"
+ "-[CTCSXPCService ctcsServerCountPreferredFrozenRecordsWithCompletion:]_block_invoke_2"
+ "-[CTCSXPCService ctcsServerRetrieveActiveDataSetRecordInternallyWithXPANId:completion:]"
+ "-[CTCSXPCService ctcsServerRetrieveActiveDataSetRecordInternallyWithXPANId:completion:]_block_invoke"
+ "-[CTCSXPCService ctcsServerRetrieveActiveDataSetRecordInternallyWithXPANId:completion:]_block_invoke_2"
+ "-[CTCSXPCService ctcsServerRetrieveIsPreferredNetworkAvailable:]"
+ "-[CTCSXPCService ctcsServerRetrieveIsPreferredNetworkAvailable:]_block_invoke_2"
+ "-[CTCSXPCService ctcsServerRetrievePreferredNetworkInternallyOnMdnsAndSigWithCompletion:]"
+ "-[CTCSXPCService ctcsServerRetrievePreferredNetworkInternallyOnMdnsAndSigWithCompletion:]_block_invoke_2"
+ "-[CTCSXPCService ctcsServerRetrievePreferredNetworkInternallyWithCompletion:]"
+ "-[CTCSXPCService ctcsServerRetrievePreferredNetworkInternallyWithCompletion:]_block_invoke_2"
+ "-[CTCSXPCService ctcsServerRetrievePreferredNetworkWithNoScanWithCompletion:]_block_invoke"
+ "-[CTCSXPCService ctcsServerRetrievePreferredNetworkWithNoScanWithCompletion:]_block_invoke_2"
+ "-[CTCSXPCService ctcsServerStoreThreadNetworkCredentialActiveDataSet:credentialsDataSet:completion:]_block_invoke"
+ "-[THThreadNetworkCredentialsKeychainBackingStore countNonAppleRecordsWithCompletion:]_block_invoke"
+ "-[THThreadNetworkCredentialsKeychainBackingStore countPreferredFrozenRecordsWithCompletion:]_block_invoke"
+ "-[THThreadNetworkCredentialsKeychainBackingStore deletePreferredNetworkWithCompletion:]"
+ "-[THThreadNetworkCredentialsKeychainBackingStore retrieveActiveDataSetRecordOnMdnsWithExtendedPANId:completion:]_block_invoke"
+ "-[THThreadNetworkCredentialsKeychainBackingStore retrieveActiveDataSetRecordWithExtendedPANId:completion:]_block_invoke"
+ "-[THThreadNetworkCredentialsStoreLocalClient storeThreadNetworkCredentialActiveDataSet:network:credentialsDataSet:waitForSync:completion:]"
+ "@\"THThreadNetworkCredentials\"24@0:8@\"NSData\"16"
+ "Failed to access backing store"
+ "Failed to count 3P saved Border Agent records; Backing store is nil"
+ "Failed to count frozen preferred network records; Backing store is nil"
+ "Failed to find any frozen preferred network"
+ "Server: %s Check for User Permission ...\n"
+ "Server: %s Checking whether dataset matches to preferred network... \n"
+ "Server: %s Failed to get record, error: %@ \n"
+ "Server: %s Failed to return record (%d), error: %@ \n"
+ "Server: %s Failed to return record, error: %@ \n"
+ "Server: %s Failed to return record, no user consent \n"
+ "Server: %s Failed to store the record, error %@ \n"
+ "Server: %s Got response from Store ...\n"
+ "Server: %s Respose from store with records count %lu, error: %@ \n"
+ "Server: %s Retrieving Network with extended panid %@\n"
+ "Server: %s Returning record successfully, error: %@ \n"
+ "Server: %s Successfully parsed network credentials"
+ "Server: %s Successfully stored the record with UUID %@, error %@ \n"
+ "Server: %s, borderAgentID: %@"
+ "Server: %s:%d: Got response from Store, data set belongs to preferred network?: %d"
+ "countNonAppleRecordsWithCompletion:"
+ "countPreferredFrozenRecordsWithCompletion:"
+ "ctcsServerCountNonAppleRecordsWithCompletion:"
+ "ctcsServerCountPreferredFrozenRecordsWithCompletion:"
+ "v24@0:8@?<v@?Q@\"NSError\">16"
+ "v24@?0Q8@\"NSError\"16"
- "%s: Request to validate network with MDNS %@"
- "-[CTCSXPCService ctcsIsPreferredNetworkForActiveOperationalDataset:completion:]_block_invoke_2"
- "Request to fetch active dataset record with xpanid %@"
- "Server: %s Checking whether dataset matches to preferred network... %@, %s, %s \n"
- "Server: %s:%d: Got response from Store isPreferred: %d"
- "Server: Check for User Permission ...\n"
- "Server: Got response from Store, error : %@\n"
- "Server: Retrieving Network with extended panid %@\n"
- "Server: Retrieving Network with extended panid Internally %@\n"
- "Server: Retrieving Preferred Network for Internal Clients ...\n"
- "Server: Retrieving or generate Preferred Network for Internal Clients ...\n"
- "Server: checking if preferred network is available ...\n"

```
