## identityservicesd

> `filesystem/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1969.600.2.0.0
-  __TEXT.__text: 0xa4ef3c
+1969.600.31.0.0
+  __TEXT.__text: 0xa50218
   __TEXT.__auth_stubs: 0x6eb0
-  __TEXT.__objc_stubs: 0x48fe0
-  __TEXT.__objc_methlist: 0x2b40c
+  __TEXT.__objc_stubs: 0x49240
+  __TEXT.__objc_methlist: 0x2b57c
   __TEXT.__const: 0x6c690
-  __TEXT.__gcc_except_tab: 0x27584
-  __TEXT.__objc_methname: 0x794c5
-  __TEXT.__cstring: 0x57627
-  __TEXT.__oslogstring: 0x81226
-  __TEXT.__objc_classname: 0x7c9b
+  __TEXT.__gcc_except_tab: 0x27594
+  __TEXT.__objc_methname: 0x79725
+  __TEXT.__cstring: 0x57677
+  __TEXT.__oslogstring: 0x813d6
+  __TEXT.__objc_classname: 0x7cbb
   __TEXT.__objc_methtype: 0x13c8e
   __TEXT.__ustring: 0x4ca
   __TEXT.__dlopen_cstrs: 0xea

   __TEXT.__swift5_assocty: 0x1388
   __TEXT.__swift5_acfuncs: 0xa0
   __TEXT.__swift5_mpenum: 0x68
-  __TEXT.__unwind_info: 0x166f0
+  __TEXT.__unwind_info: 0x16748
   __TEXT.__eh_frame: 0xfc84
   __DATA_CONST.__auth_got: 0x3768
   __DATA_CONST.__got: 0x4040
   __DATA_CONST.__auth_ptr: 0xdc8
-  __DATA_CONST.__const: 0x2f9c8
-  __DATA_CONST.__cfstring: 0x352c0
-  __DATA_CONST.__objc_classlist: 0x1308
+  __DATA_CONST.__const: 0x2f9f8
+  __DATA_CONST.__cfstring: 0x35380
+  __DATA_CONST.__objc_classlist: 0x1310
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x810
+  __DATA_CONST.__objc_protolist: 0x818
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x190
-  __DATA_CONST.__objc_superrefs: 0xbb0
+  __DATA_CONST.__objc_superrefs: 0xbb8
   __DATA_CONST.__objc_intobj: 0x1ab8
   __DATA_CONST.__objc_arraydata: 0x5b0
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x4cb78
-  __DATA.__objc_selrefs: 0x16888
-  __DATA.__objc_ivar: 0x33b0
-  __DATA.__objc_data: 0xe120
-  __DATA.__data: 0x13078
+  __DATA.__objc_const: 0x4cd30
+  __DATA.__objc_selrefs: 0x16928
+  __DATA.__objc_ivar: 0x33bc
+  __DATA.__objc_data: 0xe170
+  __DATA.__data: 0x130d8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1cf88
   __DATA.__common: 0xf58

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 43CC0908-56EB-3A16-AE64-5BFE2990624B
-  Functions: 29136
+  UUID: 4662B7C7-1332-3C1B-B771-DE04F7A9A29E
+  Functions: 29165
   Symbols:   2847
-  CStrings:  42752
+  CStrings:  42791
 
CStrings:
+ "%@:%ld"
+ "-ids"
+ "-rcs"
+ "22:56:04"
+ ":%ld"
+ "Already completed max number of Preflights; deactivating service { maxPreflights: %d, serviceType: %ld }"
+ "Already sent max number of SMS; deactivating service { maxSMSSends: %d, serviceType: %ld }"
+ "Apr  5 2026"
+ "Client noted registration complete. { serviceType: %@, labelID: %@ }"
+ "Haven't completed max number of Preflights yet { preflights: %d, maxPreflights: %d, serviceType: %ld }"
+ "Haven't sent max number of SMS yet { sends: %d, maxSMSSends: %d, serviceType: %ld }"
+ "IDSCredentialConfig"
+ "IDSPhoneCredentialConfig"
+ "Migrating PNR credential from plain key to IDS compound key for SIM label ID: %@"
+ "PNRServices"
+ "PNRServices disabled -- applying client-side filtering { mechanisms: %@ }"
+ "PNRServices enabled -- trusting server response without client-side filtering { mechanisms: %@ }"
+ "Phone Number Validation registration agent has sent %d SMSs { serviceType: %ld }"
+ "Phone service type request found cached PNR credential. { phoneNumber: %@, token: %@, tokenType: %@, serviceType: %@, requestID: %@ }"
+ "RCS"
+ "Received registration request response SMS { serviceType: %ld }"
+ "Registration request failed delivery { preflights: %d, sends: %d, attemptsWithoutSend: %d, serviceType: %ld }"
+ "Resetting Phone Number Preflight attempts to 0 { _numberOfPreflights : %d, serviceType: %ld }"
+ "Resetting Phone Number Validation Attempt counter from %d to 0 { serviceType: %ld }"
+ "Sending Preflight message { serviceType: %ld }"
+ "Setting preflight service type { serviceType: %ld }"
+ "TotalPreflightAttempts:%ld"
+ "TotalSMSAttempts:%ld"
+ "Unknown preflight service type: %ld"
+ "_bagValueForKey:"
+ "_isPNRServicesEnabled"
+ "_preflightAttemptsKey"
+ "_preflightStackIdentifier"
+ "_serviceSuffix"
+ "_smsAttemptsKey"
+ "clearPreflightStackForSimLabelID:serviceType:"
+ "clearPreflightStacksForServiceType:"
+ "credentialForUser:config:"
+ "encryptedRCS"
+ "initWithServerBag:serviceType:"
+ "initWithServiceType:"
+ "notePhoneNumberRegistrationResetForServiceType:"
+ "notePhoneNumberRegistrationResetForServiceType:withSimLabelID:"
+ "noteRegistrationCompleteForService:simLabelID:"
+ "setCredential:forUser:config:"
+ "setSMSSignature:mainID:serviceType:"
+ "setSMSSignatureMechanism:mainID:serviceType:"
+ "smsSignatureForID:serviceType:"
+ "smsSignatureMechanismForID:serviceType:"
+ "x-preflight-service"
- "23:33:03"
- "Already completed max number of Preflights; deactivating service { maxPreflights: %d }"
- "Already sent max number of SMS; deactivating service { maxSMSSends: %d }"
- "Haven't completed max number of Preflights yet { preflights: %d, maxPreflights: %d }"
- "Haven't sent max number of SMS yet { sends: %d, maxSMSSends: %d }"
- "IDS phone service type request found cached PNR credential. { phoneNumber: %@, token: %@, tokenType: %@, requestID: %@ }"
- "Mar 19 2026"
- "Phone Number Validation registration agent has sent %d SMSs"
- "RCS phone service type request found cached PNR credential. { phoneNumber: %@, token: %@, tokenType: %@, requestID: %@ }"
- "Received registration request response SMS"
- "Registration request failed delivery { preflights: %d, sends: %d, attemptsWithoutSend: %d }"
- "Resetting Phone Number Preflight attempts to 0 { _numberOfPreflights : %d }"
- "Resetting Phone Number Validation Attempt counter from %d to 0"
- "Sending Preflight message"
- "Sending phone number verification { mechanisms: %@ }"
- "TotalPreflightAttempts"
- "TotalSMSAttempts"
- "containsMechanismsForServiceType:"

```
