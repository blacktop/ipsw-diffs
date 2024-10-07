## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-493.100.4.0.0
-  __TEXT.__text: 0x181be4
-  __TEXT.__auth_stubs: 0x1d00
-  __TEXT.__objc_stubs: 0x17200
-  __TEXT.__objc_methlist: 0x8974
+493.100.8.0.0
+  __TEXT.__text: 0x18762c
+  __TEXT.__auth_stubs: 0x1d20
+  __TEXT.__objc_stubs: 0x17840
+  __TEXT.__objc_methlist: 0x8af4
   __TEXT.__const: 0x2be0
-  __TEXT.__cstring: 0xae33
-  __TEXT.__objc_classname: 0x1817
-  __TEXT.__objc_methname: 0x20a76
-  __TEXT.__objc_methtype: 0x59bc
-  __TEXT.__gcc_except_tab: 0x2270
-  __TEXT.__oslogstring: 0x1f2b8
+  __TEXT.__cstring: 0xaf53
+  __TEXT.__objc_classname: 0x182f
+  __TEXT.__objc_methname: 0x21184
+  __TEXT.__objc_methtype: 0x59cb
+  __TEXT.__gcc_except_tab: 0x22a4
+  __TEXT.__oslogstring: 0x1f7c8
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1580
   __TEXT.__swift5_fieldmd: 0xb6c

   __TEXT.__swift5_proto: 0x118
   __TEXT.__swift5_types: 0xec
   __TEXT.__swift5_protos: 0x34
-  __TEXT.__unwind_info: 0x4f20
-  __TEXT.__eh_frame: 0x6df0
-  __DATA_CONST.__auth_got: 0xe90
-  __DATA_CONST.__got: 0x15b0
+  __TEXT.__unwind_info: 0x5188
+  __TEXT.__eh_frame: 0x76f0
+  __DATA_CONST.__auth_got: 0xea0
+  __DATA_CONST.__got: 0x1628
   __DATA_CONST.__auth_ptr: 0x4d8
-  __DATA_CONST.__const: 0xc3b0
-  __DATA_CONST.__cfstring: 0x6ca0
-  __DATA_CONST.__objc_classlist: 0x6d0
+  __DATA_CONST.__const: 0xc420
+  __DATA_CONST.__cfstring: 0x6d80
+  __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x2b0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__linkguard: 0x3e
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x24b90
-  __DATA.__objc_selrefs: 0x6d18
-  __DATA.__objc_ivar: 0x9ac
-  __DATA.__objc_data: 0x5330
+  __DATA.__objc_const: 0x24db0
+  __DATA.__objc_selrefs: 0x6eb8
+  __DATA.__objc_ivar: 0x9c4
+  __DATA.__objc_data: 0x5380
   __DATA.__data: 0x3c28
-  __DATA.__bss: 0x2170
+  __DATA.__bss: 0x2180
   __DATA.__common: 0x111
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6660
-  Symbols:   1299
-  CStrings:  9276
+  Functions: 6770
+  Symbols:   1316
+  CStrings:  9376
 
Symbols:
+ _AKEDPStateHeaderKey
+ _AKEDPStateKey
+ _AKIdMSEDPTokenIdKey
+ _AKPasswordVersionHeaderKey
+ _AKPasswordVersionKey
+ _AKSRPIterationCountKey
+ _AKSRPIterationHeaderKey
+ _AKSRPProtocolHeaderKey
+ _AKSRPProtocolKey
+ _AKSRPSaltHeaderKey
+ _AKSRPSaltKey
+ _AKURLBagKeyEDPComplete
+ _AKURLBagKeyEDPMigration
+ _AKURLBagKeyRemoveEDPToken
+ _AKURLBagKeyStoreEDPToken
+ _CFPreferencesGetAppBooleanValue
+ _SecCertificateCopyExtensionValue
CStrings:
+ "\x01E)/\x0e\x1f\x0f\x03"
+ "AKEDPRequestController"
+ "Couldn't find AuthKit account for altDSID: %!@(MISSING)"
+ "Created attestation data = %!@(MISSING) with error = %!@(MISSING)"
+ "Current DCRT missing required OID:%!@(MISSING), renew DCRT"
+ "EDP Repair: Failed to check account state with error... %!@(MISSING)"
+ "EDP Repair: Failed with error... %!@(MISSING)"
+ "EDP Repair: Starting for context: %!@(MISSING)"
+ "EDP Repair: State Eligible, proceeding with repair..."
+ "EDP Repair: State Ineligible, bailing..."
+ "EDP Repair: Success!"
+ "EDP not eligible, couldn't fetch EDP health"
+ "EDP request (urlKey=%!@(MISSING)) failed! HTTP resposne=%!@(MISSING)"
+ "EDP request (urlKey=%!@(MISSING)) succeeded! HTTP resposne=%!@(MISSING)"
+ "EDPEligible and isFirstPartyWebLogin. Continuing to check EDP Health..."
+ "Error %!d(MISSING) deleting OS bound key from keychain"
+ "Error fetching AuthKitAccount %!@(MISSING)"
+ "Error getting DCRT from MobileActivation Engine: %!{(MISSING)public}@"
+ "Ignoring companion device and proceeding with silent auth"
+ "Invalid type for edpState value: %!@(MISSING)"
+ "Invalid type for passwordVersion value: %!@(MISSING)"
+ "Invalid type for srpIteration value: %!@(MISSING)"
+ "Invalid type for srpProtocol value: %!@(MISSING)"
+ "Invalid type for srpSalt value: %!@(MISSING)"
+ "Not Setting _shouldRequestToArmDeviceToAllowPCSKeyUpload, authKitAccount is nil"
+ "Not Setting _shouldRequestToArmDeviceToAllowPCSKeyUpload, isEDPEligible is NO"
+ "OID %!@(MISSING) is mising in the certificate"
+ "OID %!@(MISSING) is present in the certificate"
+ "Renewed DCRT also missing required OID:%!@(MISSING), returning error %!l(MISSING)d"
+ "Setting _shouldRequestToArmDeviceToAllowPCSKeyUpload, isEDPHealthy: %!d(MISSING)"
+ "T@\"NSNumber\",R,N,V_edpState"
+ "T@\"NSNumber\",R,N,V_passwordVersion"
+ "T@\"NSNumber\",R,N,V_srpIteration"
+ "T@\"NSString\",R,N,V_srpProtocol"
+ "T@\"NSString\",R,N,V_srpSalt"
+ "Unable to confirm this device was activated, skipping APS Token fetch."
+ "Vv32@0:8@16@24"
+ "_edpRequestWithAltDSID:URLKey:completion:"
+ "_edpRequestWithAltDSID:URLKey:serviceController:completion:"
+ "_edpState"
+ "_edpStateChangedForAccount:userInformation:"
+ "_getDCRTWithContext:renewDCRT:completion:"
+ "_idmsEDPTokenIdChangedForAccount:userInformation:"
+ "_initiateEDPRepairForAuthenticationContext:authResults:"
+ "_isEDPEligible: %!d(MISSING)"
+ "_issueDCRT:completion:"
+ "_passwordVersion"
+ "_passwordVersionChangedForAccount:userInformation:"
+ "_performRepairWithContext:completionHandler:"
+ "_renewDCRTWithContext:completion:"
+ "_srpIteration"
+ "_srpProtocol"
+ "_srpProtocolChangedForAccount:userInformation:"
+ "_srpSalt"
+ "_updateEDPStateWithRawValue:"
+ "_updatePasswordVersionWithRawValue:"
+ "_updateSRPIterationWithRawValue:"
+ "_updateSRPProtocolWithRawValue:"
+ "_updateSRPSaltWithRawValue:"
+ "com.apple.authkit.edpRepair-iForgot"
+ "contextForAltDSID:"
+ "contextWithAuthResults:"
+ "createEDPLivenessDictionaryWithContext:error:"
+ "dcrtRenewalAttempted:"
+ "didConfirmDeviceWasActivated"
+ "edpRequestWithAltDSID:URLKey:completion:"
+ "edpState"
+ "edpStateForAccount:"
+ "edpStateValueForAccount:"
+ "idmsEDPTokenId"
+ "idmsEDPTokenIdForAccount:"
+ "is EDP Healthy: %!d(MISSING)"
+ "isEDPHealthyForCDPContext:completion:"
+ "kMAOptionsBAAOIDKeyUsageProperties"
+ "kMAOptionsIgnoreExistingDCRT"
+ "keyType"
+ "overideImage4MForTesting"
+ "overrideAttestedDataForOSVersionForTesting"
+ "overrideDCRTCertForTesting"
+ "passwordVersion"
+ "passwordVersionForAccount:"
+ "performEdpCompleteKeyDropWithAltDSID:completion:"
+ "performEdpMigrationWithAltDSID:completion:"
+ "performRemoveEdpTokenWithAltDSID:completion:"
+ "repairEDPStateForContext:authenticationResults:completion:"
+ "repairEDPStateWithCompletion:"
+ "requiredOIDPresentInCertificates:"
+ "setDCRTRenewalAttempted:forAccount:"
+ "setEDPState:forAccount:"
+ "setEdpState:"
+ "setIdMSEDPTokenId:forAccount:"
+ "setIdmsEDPTokenId:"
+ "setPasswordVersion:"
+ "setPasswordVersion:forAccount:"
+ "setSRPProtocol:forAccount:"
+ "setSrpProtocol:"
+ "srpIteration"
+ "srpProtocol"
+ "srpProtocolForAccount:"
+ "srpSalt"
+ "stateControllerWithContext:"
+ "tamperAttestedDataForOSVersion"
+ "tamperDCRT"
+ "tamperImage4M"
+ "v32@?0q8@\"NSDictionary\"16@\"NSError\"24"
+ "validateEDPIdentitiesWithContext:completion:"
- "\x01E)/\x0e\x1f\r"
- "Created attestation data = %!@(MISSING)"
- "Deleted OS bound key with error %!d(MISSING)"
- "Error getting DCRT from MobileActivation Engine: %!@(MISSING)"
- "Not required to set _shouldRequestToArmDeviceToAllowPCSKeyUpload"
- "_getDCRTWithContext:completion:"

```
