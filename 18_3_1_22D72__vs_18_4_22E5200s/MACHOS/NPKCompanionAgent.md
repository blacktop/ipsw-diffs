## NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

```diff

-1216.6.2.0.0
-  __TEXT.__text: 0x40aac
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_stubs: 0x73c0
-  __TEXT.__objc_methlist: 0x2270
-  __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0x1298
-  __TEXT.__cstring: 0x22e2
-  __TEXT.__objc_methname: 0xb544
-  __TEXT.__oslogstring: 0x8dd9
+1216.16.0.0.0
+  __TEXT.__text: 0x41af4
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_stubs: 0x76a0
+  __TEXT.__objc_methlist: 0x3238
+  __TEXT.__const: 0xf8
+  __TEXT.__gcc_except_tab: 0x129c
+  __TEXT.__cstring: 0x23f6
+  __TEXT.__objc_methname: 0xb902
+  __TEXT.__oslogstring: 0x9077
   __TEXT.__objc_classname: 0x6c1
-  __TEXT.__objc_methtype: 0x3252
-  __TEXT.__unwind_info: 0xda8
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x6a0
-  __DATA_CONST.__const: 0x1dd0
-  __DATA_CONST.__cfstring: 0x1120
+  __TEXT.__objc_methtype: 0x3356
+  __TEXT.__unwind_info: 0xdb0
+  __DATA_CONST.__auth_got: 0x690
+  __DATA_CONST.__got: 0x6c8
+  __DATA_CONST.__const: 0x1df8
+  __DATA_CONST.__cfstring: 0x1140
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x7618
-  __DATA.__objc_selrefs: 0x2418
+  __DATA.__objc_const: 0x59d0
+  __DATA.__objc_selrefs: 0x2680
   __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0xc00

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1083
-  Symbols:   433
-  CStrings:  2552
+  Functions: 1093
+  Symbols:   440
+  CStrings:  2598
 
Symbols:
+ _NPKIDVRemoteDeviceSessionError
+ _NPKRadioTechnologySupportedByPairedDevice
+ _OBJC_CLASS_$_PKIdentityProvisioningSupplementalData
+ _OBJC_CLASS_$_PKPaymentService
+ _OBJC_CLASS_$_PKPendingIdentityCredential
+ _OBJC_CLASS_$_PKPendingProvisioningReceipt
+ _OBJC_CLASS_$_PKShareablePassMetadata
CStrings:
+ "-[NPDCompanionPassLibrary archivePassWithUniqueID:handler:]"
+ "-[NPDCompanionPassLibrary getPassesWithReaderIdentifier:handler:]"
+ "-[NPDCompanionPassLibrary passUniqueIDsMatchingSearchTerm:completion:]"
+ "Debug: Read payment pass with unique ID %@ from URL %@ and called updateDevicePaymentApplicationsWithSecureElementIdentifiers with %@"
+ "E6F0AB1C-320C-4941-9948-D2EAE7BA9A51"
+ "Error: Expected to be provided a reader identifier for consideration."
+ "Error: Fail to inform `passd` of finished background provisioning"
+ "Error: Missing attestation at given pending provisioning: %@"
+ "Error: Unexpected pending provisioning class: %@"
+ "Notice: Applied subcredentials %@\n to pass with unique id %@\n applet %@\n"
+ "Notice: Checking reader identifier for companion payment pass with unique id %@"
+ "Notice: Checking whether watch has payment pass with reader identifier %@"
+ "Notice: Companion pass added with unique ID %@ readerIdentifier %@. Checking for reminder %@"
+ "Notice: Found pass %@ with reader identifier %@"
+ "Notice: Request add pending provisioning"
+ "Notice: Request for bridged client info with completion %@"
+ "Notice: Returning bridgedClientInfo: %{private}@"
+ "Notice: using legacy path to add pending provisioning identity pass"
+ "Warning: Could not find device paring ID for IDVD Target device Identifier:%@"
+ "Warning: Expected only one pending provisioning for legacy identity using the first one"
+ "accountKeyIdentifier"
+ "addPendingProvisionings:completion:"
+ "addPendingProvisionings:identityTargetDeviceIdentifier:completion:"
+ "addRemoteDevicePendingProvisioningReceipt:"
+ "archivePassWithUniqueID:handler:"
+ "attestations"
+ "bridgedClientInfo"
+ "bridgedClientInfoWithCompletion:"
+ "cardConfigurationIdentifier"
+ "credentialIdentifier"
+ "dataRepresentation"
+ "deviceParingIDWithIDVRemoteDeviceID:"
+ "failedReceiptWithPendingProvisioning:error:"
+ "hasWatchPaymentPassWithReaderIdentifier:"
+ "initWithProvisioningCredentialIdentifier:cardConfigurationIdentifier:sharingInstanceIdentifier:"
+ "legacyIdentityProvisioning:targetDeviceIdentifier:completion:"
+ "noteCompanionPaymentPassActivatedWithUniqueID:readerIdentifier:"
+ "noteCompanionPaymentPassAddedWithUniqueID:readerIdentifier:"
+ "passActivationState"
+ "passSerialNumber"
+ "passUniqueIDsMatchingSearchTerm:completion:"
+ "passesWithReaderIdentifier:completion:"
+ "provisionCredentialWithType:metadata:credentialIdentifier:attestations:supplementalData:completion:"
+ "provisioningCredentialIdentifier"
+ "readerIdentifierForCompanionPaymentPassWithUniqueID:"
+ "remoteDeviceParingIDFor:"
+ "remoteSuccessReceiptWithPendingProvisioning:"
+ "setAccountKeyIdentifier:"
+ "setPassSerialNumber:"
+ "setPassTypeIdentifier:"
+ "sharingInstanceIdentifier"
+ "shouldUseLegacyIdentityProvisioning"
+ "successReceiptWithPendingProvisioning:passUniqueID:"
+ "v24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
+ "v24@?0@\"PKSecureElementPass\"8@\"NSError\"16"
+ "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v64@0:8Q16@\"PKShareablePassMetadata\"24@\"NSString\"32@\"PKIdentityProvisioningAttestations\"40@\"NSData\"48@?<v@?@\"PKSecureElementPass\"@\"NSError\">56"
+ "v64@0:8Q16@24@32@40@48@?56"
- "Error: Expected to be provided a paired terminal identifier for consideration."
- "Notice: Checking paired terminal identifier for companion payment pass with unique id %@"
- "Notice: Checking whether watch has payment pass with paired terminal identifier %@"
- "Notice: Companion pass added with unique ID %@ pairedTerminalIdentifier %@. Checking for reminder %@"
- "Notice: Found pass %@ with paired terminal identifier %@"
- "Notice: updated subcredentials for pass %@ to be %@"
- "hasWatchPaymentPassWithPairedTerminalIdentifier:"
- "noteCompanionPaymentPassActivatedWithUniqueID:pairedTerminalIdentifier:"
- "noteCompanionPaymentPassAddedWithUniqueID:pairedTerminalIdentifier:"
- "pairedTerminalIdentifierForCompanionPaymentPassWithUniqueID:"
- "paymentPassWithPairedTerminalIdentifier:completion:"
- "subcredentialsForPassWithUniqueID:"

```
