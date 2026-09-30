## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-525.326.4.0.0
-  __TEXT.__text: 0x284e94
+525.326.4.1.0
+  __TEXT.__text: 0x28d07c
   __TEXT.__auth_stubs: 0x20d0
-  __TEXT.__objc_stubs: 0x197c0
-  __TEXT.__objc_methlist: 0xb894
-  __TEXT.__const: 0x5f70
-  __TEXT.__cstring: 0xd433
-  __TEXT.__objc_classname: 0x1a47
-  __TEXT.__objc_methtype: 0x63ab
+  __TEXT.__objc_stubs: 0x19d40
+  __TEXT.__objc_methlist: 0xba3c
+  __TEXT.__const: 0x6050
+  __TEXT.__cstring: 0xd613
+  __TEXT.__objc_classname: 0x1a85
+  __TEXT.__objc_methtype: 0x63d8
   __TEXT.__gcc_except_tab: 0x3d80
-  __TEXT.__objc_methname: 0x244a5
-  __TEXT.__oslogstring: 0x23dd8
+  __TEXT.__objc_methname: 0x24b00
+  __TEXT.__oslogstring: 0x24718
   __TEXT.__dlopen_cstrs: 0x15f
-  __TEXT.__swift5_typeref: 0x2b37
-  __TEXT.__swift5_fieldmd: 0x123c
-  __TEXT.__constg_swiftt: 0x1b64
-  __TEXT.__swift5_reflstr: 0xf50
+  __TEXT.__swift5_typeref: 0x2bfd
+  __TEXT.__swift5_fieldmd: 0x1290
+  __TEXT.__constg_swiftt: 0x1be8
+  __TEXT.__swift5_reflstr: 0xf80
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0x240
-  __TEXT.__swift5_capture: 0x18dc
-  __TEXT.__swift5_protos: 0x40
-  __TEXT.__swift5_proto: 0x2b8
-  __TEXT.__swift5_types: 0x19c
+  __TEXT.__swift5_capture: 0x1914
+  __TEXT.__swift5_protos: 0x48
+  __TEXT.__swift5_proto: 0x2c0
+  __TEXT.__swift5_types: 0x1a0
   __TEXT.__swift_as_entry: 0x424
   __TEXT.__swift_as_ret: 0x518
-  __TEXT.__unwind_info: 0x62c8
+  __TEXT.__unwind_info: 0x6360
   __TEXT.__eh_frame: 0xbed0
   __DATA_CONST.__auth_got: 0x1078
-  __DATA_CONST.__got: 0x1980
-  __DATA_CONST.__auth_ptr: 0x590
-  __DATA_CONST.__const: 0x12298
-  __DATA_CONST.__cfstring: 0x7da0
-  __DATA_CONST.__objc_classlist: 0x798
+  __DATA_CONST.__got: 0x1a00
+  __DATA_CONST.__auth_ptr: 0x5a0
+  __DATA_CONST.__const: 0x12438
+  __DATA_CONST.__cfstring: 0x7e60
+  __DATA_CONST.__objc_classlist: 0x7b0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x160
-  __DATA_CONST.__objc_superrefs: 0x420
+  __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_arraydata: 0x368
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__linkguard: 0x3e
-  __DATA.__objc_const: 0x27b68
-  __DATA.__objc_selrefs: 0x7ca8
-  __DATA.__objc_ivar: 0xa98
-  __DATA.__objc_data: 0x5d30
-  __DATA.__data: 0x43b8
+  __DATA.__objc_const: 0x27ec8
+  __DATA.__objc_selrefs: 0x7e10
+  __DATA.__objc_ivar: 0xab0
+  __DATA.__objc_data: 0x5dd0
+  __DATA.__data: 0x4498
   __DATA.__bss: 0x52c0
   __DATA.__common: 0x121
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 864FB160-5CD8-31AA-ACCE-E73C0F386317
-  Functions: 8168
-  Symbols:   1500
-  CStrings:  11443
+  UUID: 3F37984F-0989-3932-9C42-7FC5178C3A54
+  Functions: 8234
+  Symbols:   1515
+  CStrings:  11562
 
Symbols:
+ _AKPDPStateHeaderKey
+ _AKPDPStateKey
+ _AKPasswordVersionHeaderKey
+ _AKPasswordVersionKey
+ _AKSRPIterationCountKey
+ _AKSRPIterationHeaderKey
+ _AKSRPProtocolHeaderKey
+ _AKSRPProtocolKey
+ _AKSRPSaltHeaderKey
+ _AKSRPSaltKey
+ _AKURLBagKeyPDPComplete
+ _AKURLBagKeyPDPMigration
+ _AKURLBagKeyPDPNativeIntermission
+ _AKWSCUUIDKey
+ _OBJC_CLASS_$_AKPDPContext
CStrings:
+ "%s: PDP Repair invoked unexpectedly in LuckC."
+ "-[AKPDPRequestController repairPDPStateForContext:authenticationResults:completion:]"
+ "AKPDPNativeIntermissionRequestProvider"
+ "AKPDPRequestController"
+ "Adding passwordVersion to request body"
+ "Adding pdpState to request body"
+ "Cleared password from PDP request body for security"
+ "Configured PDP native intermission request body"
+ "Couldn't find AuthKit account for altDSID: %@"
+ "Created PDP native intermission request to URL: %@"
+ "Did not receive wscUUID in passkey verification response"
+ "Error fetching AuthKitAccount %@"
+ "Failed to create PDP native intermission request"
+ "HTTP Date from passkey verification response - %s"
+ "Invalid context type for PDP native intermission"
+ "Invalid context type for PDP native intermission request"
+ "Invalid type for passwordVersion value: %@"
+ "Invalid type for pdpState value: %@"
+ "Invalid type for srpIteration value: %@"
+ "Invalid type for srpProtocol value: %@"
+ "Invalid type for srpSalt value: %@"
+ "Missing raw password for PDP native intermission request"
+ "Missing/unparsable Date in Response"
+ "Not Setting _shouldRequestToArmDeviceToAllowPCSKeyUpload, authKitAccount is nil"
+ "Not Setting _shouldRequestToArmDeviceToAllowPCSKeyUpload, isPDPEligible is NO"
+ "PDP Repair: Failed to check account state with error... %@"
+ "PDP Repair: Failed with error... %@"
+ "PDP Repair: Starting for context: %@"
+ "PDP Repair: State Eligible, proceeding with repair..."
+ "PDP Repair: State Ineligible, bailing..."
+ "PDP Repair: Success!"
+ "PDP native intermission completed successfully"
+ "PDP native intermission failed with status code: %ld"
+ "PDP native intermission request failed: %@"
+ "PDP not eligible, couldn't fetch PDP health"
+ "PDP parameters cannot be mixed with other user information properties"
+ "PDP request (urlKey=%@) failed! HTTP resposne=%@"
+ "PDP request (urlKey=%@) succeeded! HTTP resposne=%@"
+ "PDPEligible and isFirstPartyWebLogin. Continuing to check PDP Health..."
+ "Raw password is required for PDP native intermission"
+ "Received wscUUID in passkey verification response - %s"
+ "Saved web session details successfully."
+ "Saved web session details. Error - %@."
+ "Server returned status code %ld"
+ "Setting _shouldRequestToArmDeviceToAllowPCSKeyUpload, isPDPHealthy: %d"
+ "Skipped IDMS account update as requested by context (appProvidedContext=%ld, altDSID=%{mask.hash}@)"
+ "Skipping IDMS account update and token persistence as requested by context (appProvidedContext=%ld, altDSID=%{mask.hash}@)"
+ "Skipping service token provisioning and persistence - context configured to skip account updates (shouldUpdatePersistentServiceTokens=%@, _shouldSkipAccountUpdates=%@, appProvidedContext=%ld, altDSID=%{mask.hash}@)"
+ "T@\"NSNumber\",R,N,V_passwordVersion"
+ "T@\"NSNumber\",R,N,V_pdpState"
+ "T@\"NSNumber\",R,N,V_srpIteration"
+ "T@\"NSString\",R,N,V_srpProtocol"
+ "T@\"NSString\",R,N,V_srpSalt"
+ "_TtC3akd28AppleIDPasskeyArmingProvider"
+ "_clearPasswordFromRequestBody"
+ "_isPDPEligible: %d"
+ "_isPDPEligible: NO"
+ "_isPDPEligible: YES"
+ "_passwordVersion"
+ "_passwordVersionChangedForAccount:userInformation:"
+ "_pdpRequestWithAltDSID:URLKey:completion:"
+ "_pdpRequestWithAltDSID:URLKey:serviceController:completion:"
+ "_pdpState"
+ "_pdpStateChangedForAccount:userInformation:"
+ "_performPDPNativeIntermissionRequestWithContext:completion:"
+ "_performRepairWithContext:completionHandler:"
+ "_srpIteration"
+ "_srpProtocol"
+ "_srpProtocolChangedForAccount:userInformation:"
+ "_srpSalt"
+ "_updatePDPStateWithRawValue:"
+ "_updatePasswordVersionWithRawValue:"
+ "_updateSRPIterationWithRawValue:"
+ "_updateSRPProtocolWithRawValue:"
+ "_updateSRPSaltWithRawValue:"
+ "_validatePDPContextAndConfigureBody"
+ "ak_addJSONResponseAcceptHeader"
+ "armingProvider"
+ "contextForAltDSID:"
+ "contextWithAuthResults:"
+ "createPDPLivenessDictionaryWithContext:error:"
+ "initWithPDPContext:"
+ "is PDP Healthy: %d"
+ "isPDPEligibleForAccount:"
+ "isPDPHealthyForCDPContext:completion:"
+ "passwordVersion"
+ "passwordVersionForAccount:"
+ "pcsKeyProvider"
+ "pdpEligible"
+ "pdpRequestWithAltDSID:URLKey:completion:"
+ "pdpState"
+ "pdpStateValueForAccount:"
+ "performPDPNativeIntermissionWithPDPContext:completion:"
+ "performPdpCompleteKeyDropWithAltDSID:completion:"
+ "performPdpMigrationWithAltDSID:completion:"
+ "rawPassword"
+ "repairPDPStateForContext:authenticationResults:completion:"
+ "repairPDPStateWithCompletion:"
+ "setPDPState:forAccount:"
+ "setPasswordVersion:"
+ "setPasswordVersion:forAccount:"
+ "setPdpState:"
+ "setSRPProtocol:forAccount:"
+ "setSrpProtocol:"
+ "setType:"
+ "srpIteration"
+ "srpProtocol"
+ "srpProtocolForAccount:"
+ "srpSalt"
+ "stateControllerWithContext:"
+ "v32@0:8@\"AKPDPContext\"16@?<v@?B@\"NSError\">24"
+ "v32@?0q8@\"NSDictionary\"16@\"NSError\"24"
+ "validatePDPIdentitiesWithContext:completion:"
- "Not required to set _shouldRequestToArmDeviceToAllowPCSKeyUpload"

```
