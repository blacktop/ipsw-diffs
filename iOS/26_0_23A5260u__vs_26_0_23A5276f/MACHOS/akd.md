## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-512.1.3.0.0
-  __TEXT.__text: 0x1aae04
-  __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_stubs: 0x19020
-  __TEXT.__objc_methlist: 0xb1f4
+514.2.0.0.0
+  __TEXT.__text: 0x1aa718
+  __TEXT.__auth_stubs: 0x1fb0
+  __TEXT.__objc_stubs: 0x18f80
+  __TEXT.__objc_methlist: 0xb204
   __TEXT.__const: 0x3fc0
-  __TEXT.__cstring: 0xc1b3
+  __TEXT.__cstring: 0xc153
   __TEXT.__objc_classname: 0x1a16
-  __TEXT.__objc_methtype: 0x60be
-  __TEXT.__gcc_except_tab: 0x249c
-  __TEXT.__objc_methname: 0x235e5
-  __TEXT.__oslogstring: 0x22028
+  __TEXT.__objc_methtype: 0x608a
+  __TEXT.__gcc_except_tab: 0x248c
+  __TEXT.__objc_methname: 0x235cd
+  __TEXT.__oslogstring: 0x21e48
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x230b
   __TEXT.__swift5_fieldmd: 0xda4

   __TEXT.__swift_as_entry: 0x390
   __TEXT.__swift_as_ret: 0x458
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0x5ee0
+  __TEXT.__unwind_info: 0x5ed8
   __TEXT.__eh_frame: 0x85d8
-  __DATA_CONST.__auth_got: 0xff0
-  __DATA_CONST.__got: 0x1838
+  __DATA_CONST.__auth_got: 0xfe8
+  __DATA_CONST.__got: 0x1830
   __DATA_CONST.__auth_ptr: 0x4e0
-  __DATA_CONST.__const: 0xd7a0
-  __DATA_CONST.__cfstring: 0x74a0
+  __DATA_CONST.__const: 0xd790
+  __DATA_CONST.__cfstring: 0x73c0
   __DATA_CONST.__objc_classlist: 0x768
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x318

   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__linkguard: 0x3e
-  __DATA.__objc_const: 0x25508
-  __DATA.__objc_selrefs: 0x79f0
-  __DATA.__objc_ivar: 0xa64
+  __DATA.__objc_const: 0x25560
+  __DATA.__objc_selrefs: 0x79c0
+  __DATA.__objc_ivar: 0xa6c
   __DATA.__objc_data: 0x56f8
   __DATA.__data: 0x3b78
   __DATA.__bss: 0x29b0

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 83C5C339-AD9C-39DA-916F-1A0D518F45DC
+  UUID: 6C180C53-BD4B-385B-A4BE-B651AD32F9CC
   Functions: 7802
-  Symbols:   1439
-  CStrings:  10948
+  Symbols:   1433
+  CStrings:  10925
 
Symbols:
+ _AKIdmsWalrusStatusKey
- _AKTrustedContactSyncOperationFromIntegerValue
- _AKURLBagKeyTrustedContactsDataSync
- _OBJC_CLASS_$_AKTrustedContactsSyncResult
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "<%@: %p : %@ : %@> attestation: %@, provisioning desired: %@, request qos: %@"
+ "@\"AKAttestationRequestData\""
+ "AKBirthdayKeychain - attempting to fetch birthday day for altdsid: %@"
+ "Adding traffic request to the pending signing request queue[%@]: %@"
+ "Birthday keychain fetch failed with keychain error: %@"
+ "Have User Birthday in fetch user info"
+ "In RecoveryOS. No device token. Returning"
+ "T@\"AKAttestationRequestData\",R,N,V_attestationRequestData"
+ "T@\"NSNumber\",R,N,V_idmsWalrusStatus"
+ "_addDeviceTokenToHeaders:completion:"
+ "_attestationRequestData"
+ "_idmsWalrusStatus"
+ "_idmsWalrusStatusChangedForAccount:userInformation:"
+ "_tq_invokeAttestationRequestWithTrafficClearance:completion:"
+ "attestationRequestData"
+ "com.apple.authkit.fetch-attestation"
+ "idmsWalrusStatus"
+ "idmsWalrusStatusForAccount:"
+ "initWithRequestData:signingBlock:"
+ "isInRecoveryPartition"
+ "setIdmsWalrusStatus:forAccount:"
- "<%@: %p : %@ : %@> provisioning desired: %@, request qos: %@"
- "@\"NSDictionary\"16@?0@\"AKTrustedContact\"8"
- "Adding traffic request to the pending signing request queue: %@"
- "Failed to performTrustedContactsDataSync due to AKCustodianDaemonService being released"
- "Failed to performTrustedContactsDataSync with error: %@\nresponse: %@"
- "Missing altDSID, abandoning IdMS performTrustedContactsDataSync."
- "Missing heartbeat token, abandoning IdMS performTrustedContactsDataSync."
- "Missing lastDataSyncTimestamp, abandoning IdMS performTrustedContactsDataSync."
- "Successfully performed TrustedContactsDataSync\nresponse: %@\ndata: %@"
- "T@\"NSString\",C,N,V_clientName"
- "There is no url for key AKURLBagKeyTrustedContactsDataSync in the URLBag. No op."
- "TrustedContactsDataSync body is being created without a last data sync timestamp for custodian context: %@"
- "Unexpected IdMS trusted contact operation response: %@"
- "_bodyForTrustedContactsDataSync"
- "_clientName"
- "_trustedContactOperationsByIDFromArray:"
- "beneficiaryContacts"
- "beneficiaryListVersion"
- "beneficiaryUUIDs"
- "custodianContacts"
- "custodianListVersion"
- "custodianUUIDs"
- "hashWrappingKeyRKC"
- "hashedWrappingKeyRKC"
- "lastDataSyncTimestamp"
- "performTrustedContactsDataSync:completion:"
- "setBeneficiaryListVersion:"
- "setBeneficiaryListVersion:forAccount:"
- "setBeneficiaryOperationsByID:"
- "setCustodianListVersion:"
- "setCustodianListVersion:forAccount:"
- "setCustodianOperationsByID:"
- "timestampOnCK"
- "v32@0:8@\"AKCustodianContext\"16@?<v@?@\"AKTrustedContactsSyncResult\"@\"NSError\">24"

```
