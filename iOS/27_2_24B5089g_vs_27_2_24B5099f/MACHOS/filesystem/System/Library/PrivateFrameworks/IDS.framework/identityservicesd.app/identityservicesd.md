## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_acfuncs`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-2003.200.44.0.0
-  __TEXT.__text: 0xac983c
-  __TEXT.__auth_stubs: 0x7a10
-  __TEXT.__objc_stubs: 0x4aec0
-  __TEXT.__objc_methlist: 0x2cc1c
-  __TEXT.__const: 0x6f528
-  __TEXT.__gcc_except_tab: 0x24c98
-  __TEXT.__objc_methname: 0x7d6a5
-  __TEXT.__cstring: 0x5b799
-  __TEXT.__oslogstring: 0x8b303
+2003.200.61.0.0
+  __TEXT.__text: 0xacca78
+  __TEXT.__auth_stubs: 0x7a30
+  __TEXT.__objc_stubs: 0x4b260
+  __TEXT.__objc_methlist: 0x2cd74
+  __TEXT.__const: 0x6f538
+  __TEXT.__gcc_except_tab: 0x24d2c
+  __TEXT.__objc_methname: 0x7de75
+  __TEXT.__cstring: 0x5b8c9
+  __TEXT.__oslogstring: 0x8c1e3
   __TEXT.__objc_classname: 0x8c08
-  __TEXT.__objc_methtype: 0x14569
+  __TEXT.__objc_methtype: 0x14579
   __TEXT.__dlopen_cstrs: 0x148
   __TEXT.__ustring: 0xca0
   __TEXT.__swift5_typeref: 0xa5d6

   __TEXT.__swift_as_ret: 0x39c
   __TEXT.__swift_as_cont: 0x5a4
   __TEXT.__swift5_acfuncs: 0xf0
-  __TEXT.__unwind_info: 0x1fc60
-  __TEXT.__eh_frame: 0x13a14
-  __DATA_CONST.__const: 0x31788
-  __DATA_CONST.__cfstring: 0x37a80
+  __TEXT.__unwind_info: 0x1fd20
+  __TEXT.__eh_frame: 0x13a34
+  __DATA_CONST.__const: 0x31878
+  __DATA_CONST.__cfstring: 0x37b40
   __DATA_CONST.__objc_classlist: 0x1530
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x840

   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x3d18
-  __DATA_CONST.__got: 0x46e0
+  __DATA_CONST.__auth_got: 0x3d28
+  __DATA_CONST.__got: 0x46f8
   __DATA_CONST.__auth_ptr: 0x1058
-  __DATA.__objc_const: 0x53720
-  __DATA.__objc_selrefs: 0x172f0
-  __DATA.__objc_ivar: 0x3570
+  __DATA.__objc_const: 0x538d0
+  __DATA.__objc_selrefs: 0x17418
+  __DATA.__objc_ivar: 0x3598
   __DATA.__objc_data: 0xfd88
-  __DATA.__data: 0x172d0
+  __DATA.__data: 0x17300
   __DATA.__crash_info: 0x148
   __DATA.__common: 0xe10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 32916
-  Symbols:   2983
-  CStrings:  33508
+  Functions: 32978
+  Symbols:   2990
+  CStrings:  33617
 
Symbols:
+ _IDSGroupSessionInEndpointContextDataKey
+ _IDSGroupSessionInviteDeclineReasonKey
+ _IDSSessionRemoteDestinationSameAccountKey
+ _OBJC_CLASS_$_IDSTailspinCapture
+ _OBJC_CLASS_$_RPAccessPolicyClient
+ _nw_endpoint_create_application_service_with_alias
+ _nw_endpoint_get_device_id
CStrings:
+ "%@: client %@ updateEndpointAttributes failed with Error: %@"
+ "%@: client %@ updateEndpointAttributes storing evaluator:%@, responding with endpoints: %@"
+ "Attempting phone number account repair after Apple ID iCloud registration success"
+ "Could not find a valid payload for mode %ld { total: %lu, otherMode: %lu, unusable: %lu, noKey: %lu, alreadySent: %lu, currentDate: %@ }"
+ "Deferring QuickSwitch authentication, waiting on the linked DS auth cert {deferredFor: %.1fs, limit: %.0fs, registration: %@}"
+ "IDSServiceConnector"
+ "IDSServiceConnectorTailspinTimeout"
+ "IDSTailspinCapture monitoring enabled for service connector connections with timeout: %ld"
+ "Ignoring out-of-range payload refresh headroom fraction from server bag. { value: %f }"
+ "Linked DS auth cert still missing after %.1fs -- sending the QuickSwitch authentication anyway: %@"
+ "Matched device by publicIdentifier {identifier: %{private}@, effectiveIdentifier: %{private}@}"
+ "No phone number account worth repairing after Apple ID iCloud registration success"
+ "Provisioned payload is no longer usable. { provisionedPayload: %@, usableUntil: %@, currentDate: %@ }"
+ "QuickSwitch authentication is missing the linked DS credential, but no Apple ID authentication is queued to produce one -- sending anyway: %@"
+ "Received inEndpointContext: %@"
+ "Repaired no phone number account -- leaving the throttle unarmed"
+ "Repaired phone number accounts, arming throttle for %.0fs"
+ "Sending inEndpointContext: %@"
+ "T@\"NSMutableDictionary\",&,N,V_serviceNameToPermittedDeviceID"
+ "T@\"NSMutableDictionary\",&,N,V_serviceNameToRPAccessPolicyClient"
+ "T@\"NSMutableDictionary\",&,N,V_sessionIDToAgentClient"
+ "T@\"NSMutableDictionary\",&,N,V_sessionIDToInviterDestination"
+ "TB,N,V_containsLinkedDSCredential"
+ "TB,N,V_containsQuickSwitchRequest"
+ "Td,N,V_lastAppleIDTriggeredPhoneRepairInterval"
+ "Throttling phone number account repair after Apple ID iCloud registration success {lastRepair: %.0fs ago, throttle: %.0fs, retryIn: %.0fs}"
+ "We have a payload we can no longer publish with, should reprovision"
+ "_cleanUpAccessPolicyCacheForSession:"
+ "_cleanUpAccessPolicyCacheForSession: %@"
+ "_cleanUpAccessPolicyCacheForSession: nil sessionID, nothing to clean!"
+ "_containsLinkedDSCredential"
+ "_containsQuickSwitchRequest"
+ "_declineIncomingInvitationWithOptions: cannot decline session: %@ groupID: %@ inviterURI: %@ localURI: %@ account: %@"
+ "_declineIncomingInvitationWithOptions: declining session: %@ group: %@ to: %@ with reason: %lu"
+ "_declineIncomingInvitationWithOptions:fromDestination:account:reason:"
+ "_declineNotPermittedInvitationWithOptions:fromDestination:account:"
+ "_deferAuthentication:"
+ "_determinePolicyActionWithOptions: No deviceID found for session: %@!"
+ "_determinePolicyActionWithOptions: No serviceName found for session: %@!"
+ "_determinePolicyActionWithOptions: No sessionID found!"
+ "_determinePolicyActionWithOptions: deviceID: %@ not permitted to accept the incoming session!"
+ "_determinePolicyActionWithOptions: deviceID: %@ permitted to accept the incoming session!"
+ "_determinePolicyActionWithOptions:inEndpoint:fromDestination:account:registrationCompletionBlock:"
+ "_isStaleProvisionedPayload:"
+ "_isUsableProvisionedPayload:atDate:"
+ "_lastAppleIDTriggeredPhoneRepairInterval"
+ "_linkedDSCredentialDeferralStart"
+ "_nextProvisionCheckInterval"
+ "_payloadRefreshHeadroomFraction"
+ "_queuedAppleIDAuthentication"
+ "_repairPhoneNumberAccountsAfterAppleIDRegistrationSuccess"
+ "_serviceConnectorTailspinEnabled"
+ "_serviceConnectorTailspinTimeoutInSeconds"
+ "_serviceNameToPermittedDeviceID"
+ "_serviceNameToRPAccessPolicyClient"
+ "_sessionIDToAgentClient"
+ "_sessionIDToInviterDestination"
+ "_shouldDeferAuthentication:forRegistration:"
+ "_shouldKickPhoneNumberAccountAfterAppleIDRegistrationSuccess:"
+ "_terminateOngoingSessionsForService: access revoked for deviceID: %@ on service: %@, terminating session: %@"
+ "_terminateOngoingSessionsForService: missing serviceName: %@ or deviceID: %@"
+ "_terminateOngoingSessionsForService: service: %@ is not access policy protected, nothing to terminate"
+ "_terminateOngoingSessionsForService: session: %@ belongs to deviceID: %@, not the revoked one, skipping"
+ "_terminateOngoingSessionsForService: session: %@ has no inEndpointContext, skipping"
+ "_terminateOngoingSessionsForService: updateEndpointAttributes failed for session: %@ with error: %@"
+ "_terminateOngoingSessionsForService: updateEndpointAttributes returned nil deviceID for session: %@!"
+ "_terminateOngoingSessionsForService:revokedDeviceID:"
+ "_terminateSessionWithRevokedAccess:"
+ "_terminateSessionWithRevokedAccess: no agent client for session: %@, cannot report EPROCUNAVAIL!"
+ "_terminateSessionWithRevokedAccess: reporting EPROCUNAVAIL for session: %@"
+ "_terminateSessionWithRevokedAccess: session: %@ is already gone"
+ "_usableUntilDateForProvisionedPayload:"
+ "activateWithPolicy failed to activate for service: %@ with error: %@"
+ "activateWithPolicy successfully activated for service: %@"
+ "activateWithPolicy:forService:completion:"
+ "capture:"
+ "containsLinkedDSCredential"
+ "containsQuickSwitchRequest"
+ "controlFlags"
+ "declineOptions"
+ "dummyEndpoint"
+ "endpointContextForService failed with Error: %@"
+ "endpointContextForService inviting destinations: %@"
+ "endpointContextForService:trustCircles:completion:"
+ "internalStartConnectionWithEndpoint:service:parameters:serviceConnector:trafficClass:priority:isASQUIC:shouldMonitor:completionHandler:"
+ "lastAppleIDTriggeredPhoneRepairInterval"
+ "nw_service_connector_start_request has not returned after %lds for %@ - capturing tailspin"
+ "phone-registration-appleid-trigger-throttle-seconds"
+ "processIncomingGroupSessionMessage:publicKey:client:fromDestination:registrationCompletionBlock:"
+ "qs-max-linked-ds-credential-deferral-seconds"
+ "remote destination belongs to self account"
+ "remote destination does not belongs to self account"
+ "resolve_handler: client %@ remote declined invitation with reason: %@, message: %@ from destination: %@"
+ "run: skipping, not an internal install or disabled via server bag"
+ "serviceNameToPermittedDeviceID"
+ "serviceNameToRPAccessPolicyClient"
+ "sessionIDToAgentClient"
+ "sessionIDToInviterDestination"
+ "setAccessPermittedHandler added: %@ for service: %@, permitted count: %lu"
+ "setAccessPermittedHandler:"
+ "setAccessRevokedHandler removed: %@ for service: %@, permitted count: %lu"
+ "setAccessRevokedHandler:"
+ "setAccessRevokedHandler: %@ was not permitted for service: %@, nothing to remove"
+ "setContainsLinkedDSCredential:"
+ "setContainsQuickSwitchRequest:"
+ "setControlFlags:"
+ "setInvalidationHandler service: %@ "
+ "setLastAppleIDTriggeredPhoneRepairInterval:"
+ "setServiceNameToPermittedDeviceID:"
+ "setServiceNameToRPAccessPolicyClient:"
+ "setSessionIDToAgentClient:"
+ "setSessionIDToInviterDestination:"
+ "shared-channels-cp-payload-refresh-headroom-fraction"
+ "updateEndpointAttributes failed with error: %@"
+ "updateEndpointAttributes:forService:usingContext:completion:"
+ "v24@?0@\"NSObject<OS_nw_endpoint>\"8@\"NSError\"16"
+ "v48@0:8@16@24@32Q40"
+ "v76@0:8@16r*24@32@40i48q52B60B64@?68"
- "Could not find a valid payload"
- "Provisioned payload is expired. { provisionedPayload: %@, currentDate: %@ }"
- "We have an expired payload, should reprovision"
- "_isExpiredProvisionedPayload:"
- "internalStartConnectionWithEndpoint:service:parameters:serviceConnector:trafficClass:priority:isASQUIC:completionHandler:"
- "processIncomingGroupSessionMessage:publicKey:client:registrationCompletionBlock:"
- "resolve_handler: client %@ remote declined invitation, message: %@ from destination: %@"
- "run: skipping, disabled via server bag"
- "v72@0:8@16r*24@32@40i48q52B60@?64"
```
