## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-  __TEXT.__text: 0x7e75e0
+  __TEXT.__text: 0x7e9e1c
   __TEXT.__auth_stubs: 0x4cb0
-  __TEXT.__objc_methlist: 0x23964
-  __TEXT.__const: 0x5f5a0
-  __TEXT.__dlopen_cstrs: 0x937
-  __TEXT.__cstring: 0x2b46b
+  __TEXT.__objc_methlist: 0x23a74
+  __TEXT.__const: 0x5f5d0
+  __TEXT.__dlopen_cstrs: 0x98b
+  __TEXT.__cstring: 0x2b61e
   __TEXT.__swift5_typeref: 0x7569
-  __TEXT.__swift5_reflstr: 0x3dc4
+  __TEXT.__swift5_reflstr: 0x3dd4
   __TEXT.__swift5_assocty: 0xff0
   __TEXT.__constg_swiftt: 0x5bcc
   __TEXT.__swift5_builtin: 0x3ac

   __TEXT.__swift5_capture: 0x3cb4
   __TEXT.__swift5_mpenum: 0x8c
   __TEXT.__swift5_protos: 0x114
-  __TEXT.__oslogstring: 0x31ec2
-  __TEXT.__gcc_except_tab: 0x5948
+  __TEXT.__oslogstring: 0x32034
+  __TEXT.__gcc_except_tab: 0x5a50
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0x13ef0
-  __TEXT.__eh_frame: 0x18964
-  __TEXT.__objc_classname: 0x5c36
-  __TEXT.__objc_methname: 0x48fbd
-  __TEXT.__objc_methtype: 0x9334
-  __TEXT.__objc_stubs: 0x31240
+  __TEXT.__unwind_info: 0x13f80
+  __TEXT.__eh_frame: 0x1897c
+  __TEXT.__objc_classname: 0x5c44
+  __TEXT.__objc_methname: 0x492fd
+  __TEXT.__objc_methtype: 0x93eb
+  __TEXT.__objc_stubs: 0x31540
   __DATA_CONST.__got: 0x1b80
-  __DATA_CONST.__const: 0xcac8
-  __DATA_CONST.__objc_classlist: 0x1568
+  __DATA_CONST.__const: 0xcba8
+  __DATA_CONST.__objc_classlist: 0x1570
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x468
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf8c8
+  __DATA_CONST.__objc_selrefs: 0xf9a0
   __DATA_CONST.__objc_protorefs: 0x230
-  __DATA_CONST.__objc_superrefs: 0xce8
+  __DATA_CONST.__objc_superrefs: 0xcf0
   __DATA_CONST.__objc_arraydata: 0x5f8
   __AUTH_CONST.__auth_got: 0x2670
   __AUTH_CONST.__const: 0x2f1e8
-  __AUTH_CONST.__cfstring: 0x22be0
-  __AUTH_CONST.__objc_const: 0x3e448
+  __AUTH_CONST.__cfstring: 0x22c80
+  __AUTH_CONST.__objc_const: 0x3e588
   __AUTH_CONST.__objc_intobj: 0xc90
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0xa098
+  __AUTH.__objc_data: 0xa0e8
   __AUTH.__data: 0x2c58
   __DATA.__objc_ivar: 0x1958
-  __DATA.__data: 0x7fb8
-  __DATA.__bss: 0x1f810
+  __DATA.__data: 0x7fc8
+  __DATA.__bss: 0x1f820
   __DATA.__common: 0xb68
-  __DATA_DIRTY.__objc_ivar: 0x6d4
+  __DATA_DIRTY.__objc_ivar: 0x6e0
   __DATA_DIRTY.__objc_data: 0x5b08
-  __DATA_DIRTY.__data: 0x1ee8
-  __DATA_DIRTY.__bss: 0x4020
+  __DATA_DIRTY.__data: 0x1ef8
+  __DATA_DIRTY.__bss: 0x4050
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 28998
-  Symbols:   57163
-  CStrings:  26229
+  Functions: 29039
+  Symbols:   57311
+  CStrings:  26291
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[AMSIDCardTask _dataFromIDCardForMinimumAge:nonce:allowedDocuments:]
+ +[AMSIDCardTask _descriptorForMinimumAge:allowedDocuments:]
+ +[AMSIDCardTask _documentTypeAllowed:allowedDocuments:]
+ +[AMSIDCardTask _hasEligibleDocumentForMinimumAge:nonce:allowedDocuments:]
+ +[AMSIDCardTask _identityController]
+ +[AMSIDCardTask _identityRequestWithDescriptor:nonce:]
+ +[AMSIDCardTask _nonceFromString:]
+ -[AMSIDCardTask .cxx_destruct]
+ -[AMSIDCardTask _performHasEligibleDocumentInDaemon]
+ -[AMSIDCardTask _performTaskInDaemon]
+ -[AMSIDCardTask allowedDocuments]
+ -[AMSIDCardTask hasEligibleDocument]
+ -[AMSIDCardTask initWithMinAge:nonce:allowedDocuments:]
+ -[AMSIDCardTask minAge]
+ -[AMSIDCardTask nonce]
+ -[AMSIDCardTask perform]
+ -[AMSIDCardTask setAllowedDocuments:]
+ -[AMSIDCardTask setMinAge:]
+ -[AMSIDCardTask setNonce:]
+ _OBJC_CLASS_$_AMSIDCardTask
+ _OBJC_METACLASS_$_AMSIDCardTask
+ __OBJC_$_CLASS_METHODS_AMSIDCardTask
+ __OBJC_$_INSTANCE_METHODS_AMSIDCardTask
+ __OBJC_$_INSTANCE_VARIABLES_AMSIDCardTask
+ __OBJC_$_PROP_LIST_AMSIDCardTask
+ __OBJC_CLASS_RO_$_AMSIDCardTask
+ __OBJC_METACLASS_RO_$_AMSIDCardTask
+ ___24-[AMSIDCardTask perform]_block_invoke
+ ___24-[AMSIDCardTask perform]_block_invoke_2
+ ___36-[AMSIDCardTask hasEligibleDocument]_block_invoke
+ ___37-[AMSIDCardTask _performTaskInDaemon]_block_invoke
+ ___37-[AMSIDCardTask _performTaskInDaemon]_block_invoke_2
+ ___52-[AMSIDCardTask _performHasEligibleDocumentInDaemon]_block_invoke
+ ___52-[AMSIDCardTask _performHasEligibleDocumentInDaemon]_block_invoke_2
+ ___69+[AMSIDCardTask _dataFromIDCardForMinimumAge:nonce:allowedDocuments:]_block_invoke
+ ___69+[AMSIDCardTask _dataFromIDCardForMinimumAge:nonce:allowedDocuments:]_block_invoke_2
+ ___74+[AMSIDCardTask _hasEligibleDocumentForMinimumAge:nonce:allowedDocuments:]_block_invoke
+ ___block_descriptor_40_e8_32s_e32_v24?0"AMSBoolean"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40r_e28_v24?0"NSData"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e32_v24?0"AMSBoolean"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s_e40_v24?0"PKIdentityDocument"8"NSError"16ls32l8
+ ___block_descriptor_72_e8_32s40s48s56s_e8_v12?0B8ls32l8s40l8s48l8s56l8
+ ___getPKIdentityAnyOfDescriptorClass_block_invoke
+ ___getPKIdentityAuthorizationControllerClass_block_invoke
+ ___getPKIdentityDriversLicenseDescriptorClass_block_invoke
+ ___getPKIdentityElementClass_block_invoke
+ ___getPKIdentityIntentToStoreClass_block_invoke
+ ___getPKIdentityNationalIDCardDescriptorClass_block_invoke
+ ___getPKIdentityPhotoIDDescriptorClass_block_invoke
+ ___getPKIdentityRequestClass_block_invoke
+ _getPKIdentityAuthorizationControllerClass.softClass
+ _getPKIdentityRequestClass.softClass
+ _objc_msgSend$_dataFromIDCardForMinimumAge:nonce:allowedDocuments:
+ _objc_msgSend$_descriptorForMinimumAge:allowedDocuments:
+ _objc_msgSend$_documentTypeAllowed:allowedDocuments:
+ _objc_msgSend$_hasEligibleDocumentForMinimumAge:nonce:allowedDocuments:
+ _objc_msgSend$_identityController
+ _objc_msgSend$_identityRequestWithDescriptor:nonce:
+ _objc_msgSend$_nonceFromString:
+ _objc_msgSend$_performHasEligibleDocumentInDaemon
+ _objc_msgSend$addElements:withIntentToStore:
+ _objc_msgSend$ageThresholdElementWithAge:
+ _objc_msgSend$allowedDocuments
+ _objc_msgSend$checkCanRequestDocument:completion:
+ _objc_msgSend$encryptedData
+ _objc_msgSend$initWithDescriptors:
+ _objc_msgSend$minAge
+ _objc_msgSend$nonce
+ _objc_msgSend$performHasEligibleDocument:nonce:allowedDocuments:completion:
+ _objc_msgSend$performIDCardTaskWithMinimumAge:nonce:allowedDocuments:completion:
+ _objc_msgSend$requestDocument:completion:
+ _objc_msgSend$setDescriptor:
+ _objc_msgSend$setMerchantIdentifier:
+ _objc_msgSend$setNonce:
+ _objc_msgSend$setRegionCode:
+ _objc_msgSend$willNotStoreIntent
CStrings:
+ "%{public}@: [%{public}@] ID Card UI was cancelled by user: %{public}@"
+ "%{public}@: [%{public}@] Request document from wallet failed: %{public}@"
+ "%{public}@Moving has eligible document task to daemon"
+ "%{public}@Moving task to daemon"
+ "%{public}@Task failed with error: %@"
+ "%{public}@Task finished successfully with ID card data"
+ "%{public}@Task finished successfully. Has ID: %d"
+ "AMSIDCardTask"
+ "JP"
+ "PKIdentityAnyOfDescriptor"
+ "PKIdentityAuthorizationController"
+ "PKIdentityDriversLicenseDescriptor"
+ "PKIdentityElement"
+ "PKIdentityIntentToStore"
+ "PKIdentityNationalIDCardDescriptor"
+ "PKIdentityPhotoIDDescriptor"
+ "PKIdentityRequest"
+ "Request document from wallet failed"
+ "T@\"NSNumber\",&,N,V_minAge"
+ "T@\"NSString\",&,N,V_nonce"
+ "TQ,N,V_allowedDocuments"
+ "User cancelled out of wallet UI"
+ "_allowedDocuments"
+ "_dataFromIDCardForMinimumAge:nonce:allowedDocuments:"
+ "_descriptorForMinimumAge:allowedDocuments:"
+ "_documentTypeAllowed:allowedDocuments:"
+ "_hasEligibleDocumentForMinimumAge:nonce:allowedDocuments:"
+ "_identityController"
+ "_identityRequestWithDescriptor:nonce:"
+ "_minAge"
+ "_nonce"
+ "_nonceFromString:"
+ "_performHasEligibleDocumentInDaemon"
+ "addElements:withIntentToStore:"
+ "ageThresholdElementWithAge:"
+ "allowedDocuments"
+ "checkCanRequestDocument says there is nothing suitable in the wallet"
+ "checkCanRequestDocument:completion:"
+ "com.apple.ams-identity-verification"
+ "encryptedData"
+ "hasEligibleDocument"
+ "initWithDescriptors:"
+ "initWithMinAge:nonce:allowedDocuments:"
+ "minAge"
+ "nonce"
+ "performHasEligibleDocument:nonce:allowedDocuments:completion:"
+ "performIDCardTaskWithMinimumAge:nonce:allowedDocuments:completion:"
+ "requestDocument:completion:"
+ "setAllowedDocuments:"
+ "setDescriptor:"
+ "setMinAge:"
+ "setNonce:"
+ "setRegionCode:"
+ "v24@?0@\"PKIdentityDocument\"8@\"NSError\"16"
+ "v48@0:8@\"NSNumber\"16@\"NSString\"24@\"NSNumber\"32@?<v@?@\"AMSBoolean\"@\"NSError\">40"
+ "v48@0:8@\"NSNumber\"16@\"NSString\"24@\"NSNumber\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "willNotStoreIntent"

```
