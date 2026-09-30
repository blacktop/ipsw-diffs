## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
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
-  __TEXT.__text: 0x42815c
-  __TEXT.__auth_stubs: 0x12900
-  __TEXT.__objc_stubs: 0xa040
+442.0.0.0.0
+  __TEXT.__text: 0x428bac
+  __TEXT.__auth_stubs: 0x12950
+  __TEXT.__objc_stubs: 0xa160
   __TEXT.__init_offsets: 0xb4
-  __TEXT.__objc_methlist: 0x6acc
-  __TEXT.__gcc_except_tab: 0x2a5a4
-  __TEXT.__const: 0x8614
-  __TEXT.__oslogstring: 0x289b8
-  __TEXT.__cstring: 0x37783
+  __TEXT.__objc_methlist: 0x6b3c
+  __TEXT.__gcc_except_tab: 0x2a6dc
+  __TEXT.__const: 0x8624
+  __TEXT.__oslogstring: 0x28966
+  __TEXT.__cstring: 0x37510
   __TEXT.__objc_classname: 0x6eb
-  __TEXT.__objc_methname: 0xf72a
-  __TEXT.__objc_methtype: 0x4467
+  __TEXT.__objc_methname: 0xf877
+  __TEXT.__objc_methtype: 0x44d1
   __TEXT.__swift5_typeref: 0x572
   __TEXT.__swift5_capture: 0x60c
   __TEXT.__swift5_fieldmd: 0x130

   __TEXT.__swift_as_entry: 0xac
   __TEXT.__swift_as_ret: 0x88
   __TEXT.__swift_as_cont: 0x1dc
-  __TEXT.__unwind_info: 0x127a0
+  __TEXT.__unwind_info: 0x127e8
   __TEXT.__eh_frame: 0x1f60
-  __DATA_CONST.__const: 0xdcb0
-  __DATA_CONST.__cfstring: 0x6ce0
+  __DATA_CONST.__const: 0xddb8
+  __DATA_CONST.__cfstring: 0x6e00
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__auth_got: 0x9498
-  __DATA_CONST.__got: 0xba8
+  __DATA_CONST.__auth_got: 0x94c0
+  __DATA_CONST.__got: 0xbc8
   __DATA_CONST.__auth_ptr: 0x240
-  __DATA.__objc_const: 0x8b90
-  __DATA.__objc_selrefs: 0x3858
-  __DATA.__objc_ivar: 0x560
+  __DATA.__objc_const: 0x8b68
+  __DATA.__objc_selrefs: 0x38b0
+  __DATA.__objc_ivar: 0x558
   __DATA.__objc_data: 0x1060
   __DATA.__data: 0xa11
   __DATA.__common: 0x3eec0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 18379
-  Symbols:   24092
-  CStrings:  13500
+  Functions: 18401
+  Symbols:   24133
+  CStrings:  13532
 
Symbols:
+ -[THThreadNetworkCredentialsKeychainBackingStore adminCodePromptContent:secondsRemaining:]
+ -[THThreadNetworkCredentialsKeychainBackingStore displayCredentialShareErrorDialog]
+ -[THThreadNetworkCredentialsKeychainBackingStore enableCredentialSharingModeForExtendedPANID:completion:]
+ -[THThreadNetworkCredentialsKeychainBackingStore findmDNSScanMatchingNetworkNameSupportingEPSKCForExtendedPANID:completion:]
+ -[THThreadNetworkCredentialsKeychainBackingStore handleCredentialShareErrorWithCode:completion:]
+ -[THThreadNetworkCredentialsKeychainBackingStore handleResponseFromNotification:]
+ -[THThreadNetworkCredentialsKeychainBackingStore retrieveAllActiveDataSetRecordsWithFlag:completion:]
+ -[THThreadNetworkCredentialsKeychainBackingStore showNotificationWithAdminCode:]
+ -[THThreadNetworkCredentialsStoreLocalClient enableCredentialSharingModeForExtendedPANID:completion:]
+ -[THThreadNetworkCredentialsStoreLocalClient findmDNSScanMatchingNetworkNameSupportingEPSKCForExtendedPANID:completion:]
+ -[ThreadNetworkManagerInstance disableCredentialShare]
+ -[ThreadNetworkManagerInstance lastKnownJoinedTimeStamp]
+ -[ThreadNetworkManagerInstance logSelfHealNetworkSwitchInfoFromPersistence]
+ -[ThreadNetworkManagerInstance setLastKnownJoinedTimeStamp:]
+ -[ThreadNetworkManagerInstance updateLastKnownJoinedSignatureAndPersistwithRecord]
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-bf50cc1082d126c8b81f918a106c77da.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-eb08d1394b76732470f854b68c620469.o)
+ GCC_except_table343
+ OBJC_IVAR_$_THThreadNetworkCredentialsKeychainBackingStore._activeCountdown
+ OBJC_IVAR_$_THThreadNetworkCredentialsKeychainBackingStore._activeNotification
+ OBJC_IVAR_$_ThreadNetworkManagerInstance._lastKnownJoinedTimeStamp
+ _CFUserNotificationCancel
+ _CFUserNotificationCreate
+ _CFUserNotificationReceiveResponse
+ _CFUserNotificationUpdate
+ _OBJC_CLASS_$_NSBundle
+ _OUTLINED_FUNCTION_31
+ __101-[THThreadNetworkCredentialsStoreLocalClient enableCredentialSharingModeForExtendedPANID:completion:]_block_invoke_2
+ __105-[THThreadNetworkCredentialsKeychainBackingStore enableCredentialSharingModeForExtendedPANID:completion:]_block_invoke
+ __120-[THThreadNetworkCredentialsStoreLocalClient findmDNSScanMatchingNetworkNameSupportingEPSKCForExtendedPANID:completion:]_block_invoke_2
+ __124-[THThreadNetworkCredentialsKeychainBackingStore findmDNSScanMatchingNetworkNameSupportingEPSKCForExtendedPANID:completion:]_block_invoke
+ __80-[THThreadNetworkCredentialsKeychainBackingStore showNotificationWithAdminCode:]_block_invoke
+ __81-[THThreadNetworkCredentialsKeychainBackingStore handleResponseFromNotification:]_block_invoke
+ __ZN2ot5Posix18HardwareIdentifier28isIpadCCMappingVendor2Ver100Ev
+ __ZN2ot5Posix18HardwareIdentifier28isIpadCCMappingVendor2Ver101Ev
+ __ZN2ot5Posix18HardwareIdentifier28isIpadCCMappingVendor2Ver102Ev
+ ___101-[THThreadNetworkCredentialsKeychainBackingStore retrieveAllActiveDataSetRecordsWithFlag:completion:]_block_invoke
+ ___101-[THThreadNetworkCredentialsStoreLocalClient enableCredentialSharingModeForExtendedPANID:completion:]_block_invoke
+ ___101-[THThreadNetworkCredentialsStoreLocalClient enableCredentialSharingModeForExtendedPANID:completion:]_block_invoke_2
+ ___105-[THThreadNetworkCredentialsKeychainBackingStore enableCredentialSharingModeForExtendedPANID:completion:]_block_invoke
+ ___120-[THThreadNetworkCredentialsStoreLocalClient findmDNSScanMatchingNetworkNameSupportingEPSKCForExtendedPANID:completion:]_block_invoke
+ ___120-[THThreadNetworkCredentialsStoreLocalClient findmDNSScanMatchingNetworkNameSupportingEPSKCForExtendedPANID:completion:]_block_invoke_2
+ ___124-[THThreadNetworkCredentialsKeychainBackingStore findmDNSScanMatchingNetworkNameSupportingEPSKCForExtendedPANID:completion:]_block_invoke
+ ___80-[THThreadNetworkCredentialsKeychainBackingStore showNotificationWithAdminCode:]_block_invoke
+ ___80-[THThreadNetworkCredentialsKeychainBackingStore showNotificationWithAdminCode:]_block_invoke_2
+ ___81-[THThreadNetworkCredentialsKeychainBackingStore handleResponseFromNotification:]_block_invoke
+ ___82-[ThreadNetworkManagerInstance updateLastKnownJoinedSignatureAndPersistwithRecord]_block_invoke
+ ___83-[THThreadNetworkCredentialsKeychainBackingStore displayCredentialShareErrorDialog]_block_invoke
+ ___block_descriptor_32_e8_v12?0B8l
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_56_e8_32s40w_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48r56w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48r56w
+ ___copy_helper_block_e8_32s40w
+ ___destroy_helper_block_e8_32s40s48r56w
+ ___destroy_helper_block_e8_32s40w
+ _dispatch_source_set_cancel_handler
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationAlternateButtonTitleKey
+ _kThreadCredentialShareAODSharedMsg
+ _kThreadCredentialShareDisableMsg
+ _kThreadCredentialShareEnableMsg
+ _objc_msgSend$adminCodePromptContent:secondsRemaining:
+ _objc_msgSend$disableCredentialShare
+ _objc_msgSend$displayCredentialShareErrorDialog
+ _objc_msgSend$enableCredentialSharingModeForExtendedPANID:completion:
+ _objc_msgSend$findmDNSScanMatchingNetworkNameSupportingEPSKCForExtendedPANID:completion:
+ _objc_msgSend$handleCredentialShareErrorWithCode:completion:
+ _objc_msgSend$handleResponseFromNotification:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$localizedStringWithFormat:
+ _objc_msgSend$logSelfHealNetworkSwitchInfoFromPersistence
+ _objc_msgSend$mainBundle
+ _objc_msgSend$retrieveAllActiveDataSetRecordsWithFlag:completion:
+ _objc_msgSend$showNotificationWithAdminCode:
+ _objc_msgSend$updateLastKnownJoinedSignatureAndPersistwithRecord
- -[THThreadNetworkCredentialsKeychainBackingStore displayCredentialShareErrorDialogWithMessage:]
- -[THThreadNetworkCredentialsKeychainBackingStore enableCredentialSharingModeWithExtendedPANId:completion:]
- -[THThreadNetworkCredentialsKeychainBackingStore findmDNSScanMatchingNetworkNameSupportingEPSKCwithExtendedPANId:completion:]
- -[THThreadNetworkCredentialsKeychainBackingStore handleCredentialShareError:completion:]
- -[THThreadNetworkCredentialsStoreLocalClient enableCredentialSharingModeWithExtendedPANId:completion:]
- -[THThreadNetworkCredentialsStoreLocalClient findmDNSScanMatchingNetworkNameSupportingEPSKCwithExtendedPANId:completion:]
- -[ThreadNetworkManagerInstance updateLastKnownJoinedNetworkSignature]
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-3fb81d28199aa42cedd0b00bad8ece89.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-b8e413fc65f9de460ccac6ac82793f1f.o)
- GCC_except_table275
- OBJC_IVAR_$_THThreadNetworkCredentialsKeychainBackingStore._receivedAdminCode
- OBJC_IVAR_$_THThreadNetworkCredentialsKeychainBackingStore._receivedEpskcState
- OBJC_IVAR_$_THThreadNetworkCredentialsKeychainBackingStore._receivedEpskcStateStartedTimestamp
- OBJC_IVAR_$_THThreadNetworkCredentialsKeychainBackingStore._receivedEpskcTimeout
- OBJC_IVAR_$_THThreadNetworkCredentialsKeychainBackingStore._receivedEpskcXpanId
- __102-[THThreadNetworkCredentialsStoreLocalClient enableCredentialSharingModeWithExtendedPANId:completion:]_block_invoke_2
- __106-[THThreadNetworkCredentialsKeychainBackingStore enableCredentialSharingModeWithExtendedPANId:completion:]_block_invoke
- __121-[THThreadNetworkCredentialsStoreLocalClient findmDNSScanMatchingNetworkNameSupportingEPSKCwithExtendedPANId:completion:]_block_invoke_2
- __125-[THThreadNetworkCredentialsKeychainBackingStore findmDNSScanMatchingNetworkNameSupportingEPSKCwithExtendedPANId:completion:]_block_invoke
- __ZN2ot5Posix18HardwareIdentifier24isCCMappingVendor2Ver100Ev
- __ZN2ot5Posix18HardwareIdentifier24isCCMappingVendor2Ver101Ev
- ___102-[THThreadNetworkCredentialsStoreLocalClient enableCredentialSharingModeWithExtendedPANId:completion:]_block_invoke
- ___102-[THThreadNetworkCredentialsStoreLocalClient enableCredentialSharingModeWithExtendedPANId:completion:]_block_invoke_2
- ___106-[THThreadNetworkCredentialsKeychainBackingStore enableCredentialSharingModeWithExtendedPANId:completion:]_block_invoke
- ___121-[THThreadNetworkCredentialsStoreLocalClient findmDNSScanMatchingNetworkNameSupportingEPSKCwithExtendedPANId:completion:]_block_invoke
- ___121-[THThreadNetworkCredentialsStoreLocalClient findmDNSScanMatchingNetworkNameSupportingEPSKCwithExtendedPANId:completion:]_block_invoke_2
- ___125-[THThreadNetworkCredentialsKeychainBackingStore findmDNSScanMatchingNetworkNameSupportingEPSKCwithExtendedPANId:completion:]_block_invoke
- ___69-[ThreadNetworkManagerInstance updateLastKnownJoinedNetworkSignature]_block_invoke
- ___95-[THThreadNetworkCredentialsKeychainBackingStore displayCredentialShareErrorDialogWithMessage:]_block_invoke
- ___96-[THThreadNetworkCredentialsKeychainBackingStore retrieveAllActiveDataSetRecordsWithCompletion:]_block_invoke
- ___97-[THThreadNetworkCredentialsKeychainBackingStore displayCredentialShareSuccessDialogWithMessage:]_block_invoke
- _objc_msgSend$displayCredentialShareErrorDialogWithMessage:
- _objc_msgSend$enableCredentialSharingModeWithExtendedPANId:completion:
- _objc_msgSend$findmDNSScanMatchingNetworkNameSupportingEPSKCwithExtendedPANId:completion:
- _objc_msgSend$handleCredentialShareError:completion:
- _objc_msgSend$updateLastKnownJoinedNetworkSignature
CStrings:
+ " Morty_Version: V0.442"
+ "%@\n\n%@\n\n%@"
+ "%@| %@| %@| %@"
+ "%s CREDShare: failed to enable cred share, err=%d"
+ "(nil)"
+ "-[THThreadNetworkCredentialsStoreLocalClient enableCredentialSharingModeForExtendedPANID:completion:]_block_invoke_2"
+ "-[THThreadNetworkCredentialsStoreLocalClient findmDNSScanMatchingNetworkNameSupportingEPSKCForExtendedPANID:completion:]_block_invoke_2"
+ "-[ThreadNetworkManagerInstance updateLastKnownJoinedSignatureAndPersistwithRecord]"
+ "@\"NSDate\""
+ "AODShared"
+ "CREDShare: cancel result %s"
+ "CREDShare: failed to stop, err=%d"
+ "CredShare Enabled:Cmd failed;errorCode:%d"
+ "CredShare: %@ has no TXT record data."
+ "CredShare: AODShared received from tvOS, auto-dismissing prompt"
+ "CredShare: Admin code expected, but empty."
+ "CredShare: Cancel requested - stopping ephemeral key\n"
+ "CredShare: Cancel requested from iOS"
+ "CredShare: Checking endpoint[%lu]: %@"
+ "CredShare: CredShare Enabled: message detected!"
+ "CredShare: DisableCS message sent successfully"
+ "CredShare: Displaying error dialog - Title: '%@'"
+ "CredShare: Displaying success dialog - Message: '%{private}@'"
+ "CredShare: Endpoint[%lu]: %@"
+ "CredShare: Ephemeral key stopped, state: %s\n"
+ "CredShare: Exiting with credShareReceiveError"
+ "CredShare: Extracted Admin Code: '%@', ePSKcState: '%@', ePSKcTimeout: %u"
+ "CredShare: Failed to allocate baFinder"
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
+ "KEY_SHARE_DESCRIPTION_PLEASE"
+ "KEY_SHARE_ERROR_DESCRIPTION"
+ "KEY_SHARE_ERROR_OK_BUTTON"
+ "KEY_SHARE_ERROR_TITLE"
+ "KEY_SHARE_PASSCODE_EXPIRY"
+ "KEY_SHARE_TITLE_PLEASE"
+ "No filtering needed. Returning found records"
+ "OT_ERROR_PARSE <<frame_unpack>>"
+ "OT_ERROR_PARSE <<mac_data_unpack>>"
+ "OT_ERROR_PARSE <<receiveError>>"
+ "OT_ERROR_PARSE <<receiveErrorOutOfRange>>"
+ "Persisted self-heal-from network record: %@, info: %@, timestamp: %s"
+ "Request to fetch all active dataset records. Filter active only: %s"
+ "Self heal TN switch - previously persisted record: %s, signature: %s, timestamp: %s; last known joined record: %@, last known joined signature: %@, last known joined timestamp: %s"
+ "SelfHealFromNetworkTimestamp"
+ "T@\"NSDate\",&,V_lastKnownJoinedTimeStamp"
+ "TNM: DisableCS message detected! Cancelling credential share..."
+ "TNM: ERROR - Failed to cancel credential share"
+ "TNM: Successfully cancel credential share"
+ "^{__CFUserNotification=}"
+ "_activeCountdown"
+ "_activeNotification"
+ "_lastKnownJoinedTimeStamp"
+ "adminCodePromptContent:secondsRemaining:"
+ "com.corethreadradio.credsharetimer"
+ "disableCredentialShare"
+ "displayCredentialShareErrorDialog"
+ "ePSKcState:"
+ "enableCredentialSharingModeForExtendedPANID:completion:"
+ "findmDNSScanMatchingNetworkNameSupportingEPSKCForExtendedPANID:completion:"
+ "handleCredentialShareErrorWithCode:completion:"
+ "handleResponseFromNotification:"
+ "lastKnownJoinedTimeStamp"
+ "localizedStringForKey:value:table:"
+ "localizedStringWithFormat:"
+ "logSelfHealNetworkSwitchInfoFromPersistence"
+ "mainBundle"
+ "retrieveAllActiveDataSetRecordsWithFlag:completion:"
+ "setLastKnownJoinedTimeStamp:"
+ "showNotificationWithAdminCode:"
+ "updateLastKnownJoinedSignatureAndPersistwithRecord"
+ "v24@0:8^{__CFUserNotification=}16"
+ "v28@0:8B16@?<v@?@\"NSSet\"@\"NSError\">20"
+ "v32@0:8q16@?24"
+ "\xb9+"
- " Morty_Version: V0.438"
- "%s:%d: CredShare: %@ has no TXT record data."
- "%s:%d: CredShare: Failed to allocate baFinder"
- "%s:%d: CredShare: Failed to parse TXT record for service %@."
- "%s:%d: CredShare: Service %@ does not have bit 11 set in sb field."
- "%s:%d: CredShare: Service %@ has invalid version: %@."
- "%s:%d: CredShare: Service %@ xpanId mismatch. Service xp: %@, Expected: %@"
- "%s:%d: Persisted self-heal-from network record: %@, info: %@"
- "%s:%d: Self heal timer switching Thread network - Persist last known TN credential and network signture.)"
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
- "-[ThreadNetworkManagerInstance updateLastKnownJoinedNetworkSignature]"
- "Failed to establish Rapport connection to any endpoint"
- "Failed to find Apple Border Router"
- "Failed to send EnableCS message to Border Router"
- "Missing required fields (AdminCode, ePSKcState, or ePSKcTimeout)"
- "No matching endpoint found for services supporting EPSKC"
- "Request to fetch all active dataset records"
- "Thread Administration One-Time Passcode"
- "Thread Credential Sharing Error"
- "Unable to find border router supporting EPSKC"
- "_receivedAdminCode"
- "_receivedEpskcState"
- "_receivedEpskcStateStartedTimestamp"
- "_receivedEpskcTimeout"
- "_receivedEpskcXpanId"
- "displayCredentialShareErrorDialogWithMessage:"
- "enableCredentialSharingModeWithExtendedPANId:completion:"
- "findmDNSScanMatchingNetworkNameSupportingEPSKCwithExtendedPANId:completion:"
- "handleCredentialShareError:completion:"
- "updateLastKnownJoinedNetworkSignature"
- "\xb9*"
```
