## CoreThreadCommissionerServiced

> `/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-438.0.0.0.0
-  __TEXT.__text: 0x78330
-  __TEXT.__auth_stubs: 0x1400
-  __TEXT.__objc_stubs: 0x3840
-  __TEXT.__objc_methlist: 0x2564
-  __TEXT.__cstring: 0xa693
-  __TEXT.__objc_methname: 0x6195
+442.0.0.0.0
+  __TEXT.__text: 0x797f8
+  __TEXT.__auth_stubs: 0x1450
+  __TEXT.__objc_stubs: 0x3920
+  __TEXT.__objc_methlist: 0x2604
+  __TEXT.__cstring: 0xa533
+  __TEXT.__objc_methname: 0x62f5
   __TEXT.__objc_classname: 0x357
-  __TEXT.__objc_methtype: 0x1925
-  __TEXT.__const: 0x742
-  __TEXT.__gcc_except_tab: 0x1bb4
-  __TEXT.__oslogstring: 0xb343
+  __TEXT.__objc_methtype: 0x19f5
+  __TEXT.__const: 0x762
+  __TEXT.__gcc_except_tab: 0x1d34
+  __TEXT.__oslogstring: 0xb328
   __TEXT.__swift5_typeref: 0x4c2
   __TEXT.__swift5_capture: 0x418
   __TEXT.__swift5_fieldmd: 0xac

   __TEXT.__swift_as_entry: 0x6c
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x154
-  __TEXT.__unwind_info: 0x1a30
+  __TEXT.__unwind_info: 0x1af8
   __TEXT.__eh_frame: 0x15c0
-  __DATA_CONST.__const: 0x1930
-  __DATA_CONST.__cfstring: 0x1cc0
+  __DATA_CONST.__const: 0x1ab8
+  __DATA_CONST.__cfstring: 0x1ce0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__auth_got: 0xa18
-  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__auth_got: 0xa40
+  __DATA_CONST.__got: 0x4c0
   __DATA_CONST.__auth_ptr: 0x138
-  __DATA.__objc_const: 0x31a0
-  __DATA.__objc_selrefs: 0x1388
-  __DATA.__objc_ivar: 0xcc
+  __DATA.__objc_const: 0x31c0
+  __DATA.__objc_selrefs: 0x13d0
+  __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x600
   __DATA.__data: 0x700
   __DATA.__bss: 0x1c8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1892
-  Symbols:   522
-  CStrings:  2855
+  Functions: 1933
+  Symbols:   530
+  CStrings:  2878
 
Symbols:
+ _CFUserNotificationCancel
+ _CFUserNotificationCreate
+ _CFUserNotificationReceiveResponse
+ _CFUserNotificationUpdate
+ _dispatch_source_set_cancel_handler
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationAlternateButtonTitleKey
CStrings:
+ "%@\n\n%@\n\n%@"
+ "%s: %d: Internal keychainAccessGroup: %@ .\n"
+ "%s:%d: Error: Invalid team id provided. Reverting to default internal store"
+ "%s:%d: Error: completion block is nil"
+ "%s:%d: Failed to retrieve application record. Error: %@"
+ "-[CTCSXPCService BackingStoreDSInternallyForTeamID:]"
+ "-[CTCSXPCService checkShareEntitlement]"
+ "-[CTCSXPCService ctcsServerEnableCredentialSharingModeForExtendedPANID:completion:]"
+ "-[CTCSXPCService ctcsServerEnableCredentialSharingModeInternallyForExtendedPANID:completion:]"
+ "-[CTCSXPCService ctcsServerRetrieveActiveCredentialsForNearbyNetworksInternallyWithCompletion:]"
+ "-[CTCSXPCService ctcsServerRetrieveActiveCredentialsForNearbyNetworksInternallyWithCompletion:]_block_invoke"
+ "-[CTCSXPCService ctcsServerRetrieveActiveCredentialsForNearbyNetworksInternallyWithCompletion:]_block_invoke_2"
+ "-[CTCSXPCService ctcsServerRetrieveActiveCredentialsForNearbyNetworksWithCompletion:]"
+ "-[CTCSXPCService ctcsServerRetrieveActiveCredentialsForNearbyNetworksWithCompletion:]_block_invoke"
+ "-[CTCSXPCService ctcsServerStoreThreadNetworkCredentialActiveDataSetInternally:network:credentialsDataSet:teamID:waitForSync:completion:]"
+ "-[THThreadNetworkCredentialsStoreLocalClient enableCredentialSharingModeForExtendedPANID:completion:]_block_invoke_2"
+ "-[THThreadNetworkCredentialsStoreLocalClient findmDNSScanMatchingNetworkNameSupportingEPSKCForExtendedPANID:completion:]_block_invoke_2"
+ "AODShared"
+ "BackingStoreDSInternallyForTeamID:"
+ "CredShare: %@ has no TXT record data."
+ "CredShare: AODShared received from tvOS, auto-dismissing prompt"
+ "CredShare: Admin code expected, but empty."
+ "CredShare: Checking endpoint[%lu]: %@"
+ "CredShare: CredShare Enabled: message detected!"
+ "CredShare: DisableCS message sent successfully"
+ "CredShare: Displaying error dialog - Title: '%@'"
+ "CredShare: Displaying success dialog - Message: '%{private}@'"
+ "CredShare: Endpoint[%lu]: %@"
+ "CredShare: Exiting with credShareReceiveError"
+ "CredShare: Extracted Admin Code: '%@', ePSKcState: '%@', ePSKcTimeout: %u"
+ "CredShare: Failed to allocate baFinder"
+ "CredShare: Failed to enable Credential Sharing Mode internally; Missing entitlement"
+ "CredShare: Failed to enable Credential Sharing Mode; Missing entitlement"
+ "CredShare: Failed to parse TXT record for service %@."
+ "CredShare: Failed to send DisableCS message"
+ "CredShare: Invalid extendedPANID size %lu, expected %d"
+ "CredShare: Matched[%lu] - Service: '%@', Endpoint: %@"
+ "CredShare: Message missing ';ePSKcState:' marker: '%@'"
+ "CredShare: Message missing ';ePSKcTimeout:' marker: '%@'"
+ "CredShare: Message missing 'AdminCode:' marker: '%@'"
+ "CredShare: Rapport: Error - message is nil or empty"
+ "CredShare: Rapport: Rapport Browse initiated successfully"
+ "CredShare: Rapport: Rapport Connect Send initiated successfully"
+ "CredShare: Rapport: Rapport Send completed successfully"
+ "CredShare: Rapport: Request to initiate Rapport Browse for Credtial Share"
+ "CredShare: Rapport: Request to initiate Rapport Connect for Credtial Share"
+ "CredShare: Rapport: Request to send message via Rapport: '%@'"
+ "CredShare: Rapport: Sending message to all connected peers on tvOS"
+ "CredShare: Rapport: Starting Network Manager Browsing on iOS"
+ "CredShare: Rapport: Starting Network Manager Connecting and Sending on iOS"
+ "CredShare: Received other message: '%@'"
+ "CredShare: Request to enable credential sharing mode"
+ "CredShare: Server: - Missing entitlement %s"
+ "CredShare: Server: Missing entitlement %s"
+ "CredShare: Service %@ does not have bit 11 set in sb field."
+ "CredShare: Service %@ has invalid version: %@."
+ "CredShare: Service %@ xpanId mismatch. Service xp: %@, Expected: %@"
+ "CredShare: Setting NetworkManagerThreadSwiftBridge delegate to self"
+ "CredShare: Step 1 - Starting Rapport browse with 5 second duration"
+ "CredShare: Step 1 Complete - Received %lu endpoints from Rapport browse"
+ "CredShare: Step 1 Failed - endpointsArray is null from Rapport browse"
+ "CredShare: Step 2 - Starting mDNS scan for services supporting EPSKC"
+ "CredShare: Step 2 Complete - Found %lu valid service names"
+ "CredShare: Step 2 Failed - mDNS scan error: %@"
+ "CredShare: Step 3 - Found %lu matching endpoint(s)"
+ "CredShare: Step 3 - MATCH FOUND! ServiceName '%@' matches endpoint[%lu]"
+ "CredShare: Step 3 - Matching service names with endpoints"
+ "CredShare: Step 3 - No matching endpoint found"
+ "CredShare: Step 3 Complete - Found %lu matching endpoint(s)"
+ "CredShare: Step 3 Failed - No matching endpoint found for any valid service"
+ "CredShare: Step 4 - Attempting connection %lu/%lu to service '%@', endpoint: %@"
+ "CredShare: Step 4 - Attempting to connect to matched endpoints via Rapport"
+ "CredShare: Step 4 - Connection attempt %lu/%lu failed for service '%@'"
+ "CredShare: Step 4 Complete - Rapport connection established on attempt %lu/%lu to service '%@': %@"
+ "CredShare: Step 4 Failed - All %lu connection attempts failed"
+ "CredShare: Step 5 - Sending 'EnableCS' message to established connection"
+ "CredShare: Step 5 Complete - EnableCS message sent successfully"
+ "CredShare: Step 5 Failed - Could not send EnableCS message"
+ "CredShare: Step 6 - Waiting for Admin Code response via delegate..."
+ "CredShare: This prompt was replaced by a newer one; leaving the connection for it"
+ "CredShare: Timer expired"
+ "CredShare: User chose Cancel - sending DisableCS to Border Router"
+ "CredShare: ValidServiceName[%lu]: %@"
+ "CredShare: didReceiveNetworkMessage called with: '%@'"
+ "Credential sharing failed"
+ "DisableCS"
+ "Fetched all active dataset records. Total count: %lu"
+ "Filtered by active only records. Total count after filter: %lu"
+ "KEY_SHARE_CANCEL_BUTTON"
+ "KEY_SHARE_ERROR_DESCRIPTION"
+ "KEY_SHARE_ERROR_OK_BUTTON"
+ "KEY_SHARE_ERROR_TITLE"
+ "KEY_SHARE_PASSCODE_EXPIRY"
+ "NO"
+ "No filtering needed. Returning found records"
+ "Request to fetch all active dataset records. Filter active only: %s"
+ "Server: %s Failed did not return any records, error: %@ \n"
+ "Server: %s Failed will not return records, no user consent \n"
+ "Server: %s Returning records successfully, error: %@ \n"
+ "YES"
+ "^{__CFUserNotification=}"
+ "_activeCountdown"
+ "_activeNotification"
+ "adminCodePromptContent:secondsRemaining:"
+ "checkShareEntitlement"
+ "com.apple.developer.networking.share-thread-network-credentials"
+ "com.corethreadradio.credsharetimer"
+ "ctcsServerEnableCredentialSharingModeForExtendedPANID:completion:"
+ "ctcsServerEnableCredentialSharingModeInternallyForExtendedPANID:completion:"
+ "ctcsServerRetrieveActiveCredentialsForNearbyNetworksInternallyWithCompletion:"
+ "ctcsServerRetrieveActiveCredentialsForNearbyNetworksWithCompletion:"
+ "ctcsServerStoreThreadNetworkCredentialActiveDataSetInternally:network:credentialsDataSet:teamID:waitForSync:completion:"
+ "displayCredentialShareErrorDialog"
+ "enableCredentialSharingModeForExtendedPANID:completion:"
+ "findmDNSScanMatchingNetworkNameSupportingEPSKCForExtendedPANID:completion:"
+ "handleCredentialShareErrorWithCode:completion:"
+ "handleResponseFromNotification:"
+ "retrieveAllActiveDataSetRecordsWithFlag:completion:"
+ "showNotificationWithAdminCode:"
+ "v24@0:8^{__CFUserNotification=}16"
+ "v32@0:8q16@?24"
+ "v60@0:8@\"THThreadNetworkBorderAgent\"16@\"THThreadNetwork\"24@\"THThreadNetworkCredentialsDataSet\"32@\"NSString\"40B48@?<v@?@\"NSUUID\"@\"NSError\">52"
- "%s: %d: Apple internal keychainAccessGroup: %@ .\n"
- "%s:%d: CredShare: %@ has no TXT record data."
- "%s:%d: CredShare: Failed to allocate baFinder"
- "%s:%d: CredShare: Failed to parse TXT record for service %@."
- "%s:%d: CredShare: Service %@ does not have bit 11 set in sb field."
- "%s:%d: CredShare: Service %@ has invalid version: %@."
- "%s:%d: CredShare: Service %@ xpanId mismatch. Service xp: %@, Expected: %@"
- "%s:%d:CredShare: Admin code expected, but empty."
- "%s:%d:CredShare: Check 1 - Elapsed time (%.0f sec) > timeout (%u sec). Resetting state to 'Stopped'."
- "%s:%d:CredShare: Check 2 - State is 'Started' and within timeout window."
- "%s:%d:CredShare: Checking endpoint[%lu]: %@"
- "%s:%d:CredShare: CredShare Enabled: message detected!"
- "%s:%d:CredShare: Current state: '%@', Timeout: %u sec, Elapsed time: %.0f sec, Cached xpanId: %@, Requested xpanId: %@"
- "%s:%d:CredShare: Displaying error dialog - Title: '%@', Message: '%@'"
- "%s:%d:CredShare: Displaying success dialog - Title: '%@', Message: '%{private}@'"
- "%s:%d:CredShare: Edge case - ePSKcState started but admin code missing. We should restart process to get admin code"
- "%s:%d:CredShare: Endpoint[%lu]: %@"
- "%s:%d:CredShare: Exiting with error code -6"
- "%s:%d:CredShare: Extracted Admin Code: '%@', ePSKcState: '%@', ePSKcTimeout: %u"
- "%s:%d:CredShare: Invalid xpanId size %lu, expected %d"
- "%s:%d:CredShare: Matched[%lu] - Service: '%@', Endpoint: %@"
- "%s:%d:CredShare: Message missing ';ePSKcState:' marker: '%@'"
- "%s:%d:CredShare: Message missing ';ePSKcTimeout:' marker: '%@'"
- "%s:%d:CredShare: Message missing 'AdminCode:' marker: '%@'"
- "%s:%d:CredShare: Rapport: Error - message is nil or empty"
- "%s:%d:CredShare: Rapport: Rapport Browse initiated successfully"
- "%s:%d:CredShare: Rapport: Rapport Connect Send initiated successfully"
- "%s:%d:CredShare: Rapport: Rapport Send completed successfully"
- "%s:%d:CredShare: Rapport: Request to initiate Rapport Browse for Credtial Share"
- "%s:%d:CredShare: Rapport: Request to initiate Rapport Connect for Credtial Share"
- "%s:%d:CredShare: Rapport: Request to send message via Rapport: '%@'"
- "%s:%d:CredShare: Rapport: Sending message to all connected peers on tvOS"
- "%s:%d:CredShare: Rapport: Starting Network Manager Browsing on iOS"
- "%s:%d:CredShare: Rapport: Starting Network Manager Connecting and Sending on iOS"
- "%s:%d:CredShare: Received other message: '%@'"
- "%s:%d:CredShare: Recorded timestamp for 'Started' state: %.0f"
- "%s:%d:CredShare: Request to enable credential sharing mode"
- "%s:%d:CredShare: Returning cached values. Original timeout: %u sec, Elapsed: %.0f sec, Remaining: %u sec"
- "%s:%d:CredShare: Setting NetworkManagerThreadSwiftBridge delegate to self"
- "%s:%d:CredShare: Step 1 - Starting Rapport browse with 5 second duration"
- "%s:%d:CredShare: Step 1 Complete - Received %lu endpoints from Rapport browse"
- "%s:%d:CredShare: Step 1 Failed - endpointsArray is null from Rapport browse"
- "%s:%d:CredShare: Step 2 - Starting mDNS scan for services supporting EPSKC"
- "%s:%d:CredShare: Step 2 Complete - Found %lu valid service names"
- "%s:%d:CredShare: Step 2 Failed - mDNS scan error: %@"
- "%s:%d:CredShare: Step 3 - Found %lu matching endpoint(s)"
- "%s:%d:CredShare: Step 3 - MATCH FOUND! ServiceName '%@' matches endpoint[%lu]"
- "%s:%d:CredShare: Step 3 - Matching service names with endpoints"
- "%s:%d:CredShare: Step 3 - No matching endpoint found"
- "%s:%d:CredShare: Step 3 Complete - Found %lu matching endpoint(s)"
- "%s:%d:CredShare: Step 3 Failed - No matching endpoint found for any valid service"
- "%s:%d:CredShare: Step 4 - Attempting connection %lu/%lu to service '%@', endpoint: %@"
- "%s:%d:CredShare: Step 4 - Attempting to connect to matched endpoints via Rapport"
- "%s:%d:CredShare: Step 4 - Connection attempt %lu/%lu failed for service '%@'"
- "%s:%d:CredShare: Step 4 Complete - Rapport connection established on attempt %lu/%lu to service '%@': %@"
- "%s:%d:CredShare: Step 4 Failed - All %lu connection attempts failed"
- "%s:%d:CredShare: Step 5 - Sending 'EnableCS' message to established connection"
- "%s:%d:CredShare: Step 5 Complete - EnableCS message sent successfully"
- "%s:%d:CredShare: Step 5 Failed - Could not send EnableCS message"
- "%s:%d:CredShare: Step 6 - Waiting for Admin Code response via delegate..."
- "%s:%d:CredShare: ValidServiceName[%lu]: %@"
- "%s:%d:CredShare: didReceiveNetworkMessage called with: '%@'"
- "-[CTCSXPCService BackingStoreDSInternally]"
- "-[CTCSXPCService ctcsServerEnableCredentialSharingModeInternallyWithExtendedPANId:completion:]"
- "-[CTCSXPCService ctcsServerEnableCredentialSharingModeWithExtendedPANId:completion:]"
- "-[CTCSXPCService ctcsServerStoreThreadNetworkCredentialActiveDataSetInternally:network:credentialsDataSet:waitForSync:completion:]"
- "-[THThreadNetworkCredentialsKeychainBackingStore displayCredentialShareErrorDialogWithMessage:]_block_invoke"
- "-[THThreadNetworkCredentialsKeychainBackingStore displayCredentialShareSuccessDialogWithMessage:]_block_invoke"
- "-[THThreadNetworkCredentialsKeychainBackingStore enableCredentialSharingModeWithExtendedPANId:completion:]_block_invoke"
- "-[THThreadNetworkCredentialsKeychainBackingStore findmDNSScanMatchingNetworkNameSupportingEPSKCwithExtendedPANId:completion:]_block_invoke"
- "-[THThreadNetworkCredentialsKeychainBackingStore matchServiceNamesWithEndpoints:validServiceNames:matchedServiceNames:matchedEndpoints:]"
- "-[THThreadNetworkCredentialsKeychainBackingStore rapportBrowseForPreferredNetworkWithCompletion:]_block_invoke"
- "-[THThreadNetworkCredentialsKeychainBackingStore rapportConnectForPreferredNetworkWithCompletion:]_block_invoke"
- "-[THThreadNetworkCredentialsKeychainBackingStore rapportSendForPreferredNetworkWithMessage:completion:]_block_invoke"
- "-[THThreadNetworkCredentialsStoreLocalClient enableCredentialSharingModeWithExtendedPANId:completion:]_block_invoke_2"
- "-[THThreadNetworkCredentialsStoreLocalClient findmDNSScanMatchingNetworkNameSupportingEPSKCwithExtendedPANId:completion:]_block_invoke_2"
- "Failed to establish Rapport connection to any endpoint"
- "Failed to find Apple Border Router"
- "Failed to send EnableCS message to Border Router"
- "Missing required fields (AdminCode, ePSKcState, or ePSKcTimeout)"
- "No matching endpoint found for services supporting EPSKC"
- "Request to fetch all active dataset records"
- "Server: Check for User Permission ...\n"
- "Started"
- "Stopped"
- "Thread Administration One-Time Passcode"
- "Thread Credential Sharing Error"
- "Unable to find border router supporting EPSKC"
- "_receivedAdminCode"
- "_receivedEpskcState"
- "_receivedEpskcStateStartedTimestamp"
- "_receivedEpskcTimeout"
- "_receivedEpskcXpanId"
- "ctcsServerEnableCredentialSharingModeInternallyWithExtendedPANId:completion:"
- "ctcsServerEnableCredentialSharingModeWithExtendedPANId:completion:"
- "displayCredentialShareErrorDialogWithMessage:"
- "enableCredentialSharingModeWithExtendedPANId:completion:"
- "findmDNSScanMatchingNetworkNameSupportingEPSKCwithExtendedPANId:completion:"
- "handleCredentialShareError:completion:"
```
