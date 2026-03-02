## AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

-7624.1.13.10.2
-  __TEXT.__text: 0x203b4
-  __TEXT.__auth_stubs: 0x1490
-  __TEXT.__objc_stubs: 0x2120
-  __TEXT.__objc_methlist: 0x9e4
-  __TEXT.__cstring: 0x9f8
-  __TEXT.__const: 0x5c2
-  __TEXT.__objc_methname: 0x3779
-  __TEXT.__oslogstring: 0xa41
-  __TEXT.__objc_classname: 0x153
-  __TEXT.__objc_methtype: 0x129e
+7624.1.14.10.4
+  __TEXT.__text: 0x226b0
+  __TEXT.__auth_stubs: 0x1510
+  __TEXT.__objc_stubs: 0x23e0
+  __TEXT.__objc_methlist: 0xa50
+  __TEXT.__cstring: 0xa38
+  __TEXT.__const: 0x5e2
+  __TEXT.__objc_methname: 0x38fd
+  __TEXT.__oslogstring: 0xa61
+  __TEXT.__objc_classname: 0x181
+  __TEXT.__objc_methtype: 0x12a9
   __TEXT.__gcc_except_tab: 0x13c
   __TEXT.__constg_swiftt: 0x90
-  __TEXT.__swift5_typeref: 0x4e9
+  __TEXT.__swift5_typeref: 0x553
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0xc

   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x38
-  __TEXT.__unwind_info: 0x6b0
-  __TEXT.__eh_frame: 0xad8
-  __DATA_CONST.__auth_got: 0xa58
-  __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__auth_ptr: 0x178
+  __TEXT.__unwind_info: 0x6e0
+  __TEXT.__eh_frame: 0xb40
+  __DATA_CONST.__auth_got: 0xa98
+  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__auth_ptr: 0x180
   __DATA_CONST.__const: 0xcc0
-  __DATA_CONST.__cfstring: 0x1c0
+  __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0xbe0
-  __DATA.__objc_selrefs: 0xa90
+  __DATA.__objc_const: 0xc28
+  __DATA.__objc_selrefs: 0xb50
   __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0x180
-  __DATA.__data: 0x5c0
+  __DATA.__data: 0x640
   __DATA.__bss: 0x350
   __DATA.__common: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F550C3ED-9FEB-3A30-9CE4-EB9292786AD7
-  Functions: 492
-  Symbols:   548
-  CStrings:  645
+  UUID: EAEEA741-765B-3688-8B5C-4DB3245F73EF
+  Functions: 504
+  Symbols:   561
+  CStrings:  678
 
Symbols:
+ _$s26AuthenticationServicesCore46ASCPublicKeyCredentialAssertionExtensionInputsC9LargeBlobV9OperationO5writeyAG10Foundation4DataVcAGmFWC
+ _$s26AuthenticationServicesCore47ASCPublicKeyCredentialAssertionExtensionOutputsC9LargeBlobV15OperationResultO5writeyAGSb_tcAGmFWC
+ _$s26AuthenticationServicesCore49ASCPublicKeyCredentialRegistrationExtensionInputsC9LargeBlobV18SupportRequirementO8requiredyA2GmFWC
+ _$s26AuthenticationServicesCore49ASCPublicKeyCredentialRegistrationExtensionInputsC9LargeBlobV18SupportRequirementO9preferredyA2GmFWC
+ _$s26AuthenticationServicesCore49ASCPublicKeyCredentialRegistrationExtensionInputsC9LargeBlobV18SupportRequirementOMa
+ _$s26AuthenticationServicesCore49ASCPublicKeyCredentialRegistrationExtensionInputsC9LargeBlobV18supportRequirementAE07SupportM0Ovg
+ _$s26AuthenticationServicesCore49ASCPublicKeyCredentialRegistrationExtensionInputsC9LargeBlobVMa
+ _$s26AuthenticationServicesCore49ASCPublicKeyCredentialRegistrationExtensionInputsC9LargeBlobVMn
+ _$s26AuthenticationServicesCore49ASCPublicKeyCredentialRegistrationExtensionInputsC9largeBlobAC05LargeK0VSgvgTj
+ _$s26AuthenticationServicesCore50ASCPublicKeyCredentialRegistrationExtensionOutputsC9LargeBlobV11isSupportedAESb_tcfC
+ _$sSo13os_log_type_ta0A0E5faultABvgZ
+ _NSClassFromString
+ _swift_unknownObjectRelease_n
CStrings:
+ "@\"NSData\"16@0:8"
+ "T@\"NSData\",C,N"
+ "Unknown largeBlob operation"
+ "_WKAuthenticationExtensionsLargeBlobInputs"
+ "_WKAuthenticationPRFInputValues"
+ "_WKAuthenticationPRFInputValuesStaging"
+ "appid"
+ "blob"
+ "eval"
+ "initWithRelyingPartyIdentifier:attestationObject:rawClientDataJSON:credentialID:transports:extensionOutputsCBOR:attachment:extensions:"
+ "initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:extensions:"
+ "largeBlob"
+ "prfEnabled"
+ "prfFirst"
+ "prfSalt1"
+ "prfSalt2"
+ "prfSecond"
+ "setAppID:"
+ "setEval:"
+ "setEvalByCredential:"
+ "setLargeBlob:"
+ "setPrf:"
+ "setPrfSalt1:"
+ "setPrfSalt2:"
+ "setRead:"
+ "setSupport:"
+ "setWrite:"
+ "supported"
+ "v24@0:8@\"NSData\"16"
+ "wkExtensionInputsFromASCAssertionExtensions:"
+ "wkExtensionInputsFromASCRegistrationExtensions:"
+ "wkLargeBlobInputs"
+ "wkPRFInputs"
+ "written"
- "extensionsCBORForWebKit"
- "initWithRelyingPartyIdentifier:attestationObject:rawClientDataJSON:credentialID:transports:extensionOutputsCBOR:attachment:"
- "initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:"

```
