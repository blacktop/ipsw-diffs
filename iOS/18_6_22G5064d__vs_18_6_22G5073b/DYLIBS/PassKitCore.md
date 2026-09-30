## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1591.7.1.0.0
-  __TEXT.__text: 0x7bfdc4
+1591.7.3.0.0
+  __TEXT.__text: 0x7c0308
   __TEXT.__auth_stubs: 0x49f0
-  __TEXT.__objc_methlist: 0x6a324
+  __TEXT.__objc_methlist: 0x6a34c
   __TEXT.__const: 0x224a0
   __TEXT.__cstring: 0x67b35
   __TEXT.__swift5_typeref: 0x539c
   __TEXT.__swift5_capture: 0x3924
-  __TEXT.__oslogstring: 0x340a6
+  __TEXT.__oslogstring: 0x340ed
   __TEXT.__constg_swiftt: 0x4a84
   __TEXT.__swift5_fieldmd: 0x4e60
   __TEXT.__swift5_reflstr: 0x403d

   __TEXT.__swift5_types2: 0x4
   __TEXT.__gcc_except_tab: 0x7488
   __TEXT.__ustring: 0x1ed6
-  __TEXT.__unwind_info: 0x1b1e0
+  __TEXT.__unwind_info: 0x1b200
   __TEXT.__eh_frame: 0x5814
   __TEXT.__objc_classname: 0xf8fa
-  __TEXT.__objc_methname: 0xc7982
+  __TEXT.__objc_methname: 0xc7a24
   __TEXT.__objc_methtype: 0x16ec5
-  __TEXT.__objc_stubs: 0x580e0
+  __TEXT.__objc_stubs: 0x58100
   __DATA_CONST.__got: 0x45a8
   __DATA_CONST.__const: 0x201b8
   __DATA_CONST.__objc_classlist: 0x3980
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x598
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22458
+  __DATA_CONST.__objc_selrefs: 0x22460
   __DATA_CONST.__objc_protorefs: 0x240
   __DATA_CONST.__objc_superrefs: 0x2d98
   __DATA_CONST.__objc_arraydata: 0x3108
   __AUTH_CONST.__auth_got: 0x2508
   __AUTH_CONST.__const: 0x1cdd8
   __AUTH_CONST.__cfstring: 0x6e0e0
-  __AUTH_CONST.__objc_const: 0xc1540
+  __AUTH_CONST.__objc_const: 0xc1580
   __AUTH_CONST.__objc_arrayobj: 0xac8
   __AUTH_CONST.__objc_intobj: 0x11a0
   __AUTH_CONST.__objc_dictobj: 0x1e50

   __AUTH.__data: 0x3578
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x64a0
+  __DATA.__objc_ivar: 0x64a4
   __DATA.__data: 0x83b0
   __DATA.__bss: 0x172c0
   __DATA.__common: 0x220

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 50BD1001-BEAB-324E-81FC-380F601B2405
-  Functions: 48883
-  Symbols:   126520
-  CStrings:  65958
+  UUID: 6A603460-0B38-39C4-B9F6-4AD1AA887708
+  Functions: 48889
+  Symbols:   126536
+  CStrings:  65962
 
Symbols:
+ -[PKAppletSubcredentialManagementSession setAccountAttestation:forUpgradeCredential:withCompletion:]
+ -[PKDAManager setAccountAttestation:forUpgradeCredential:withCompletion:]
+ -[PKWebServiceMerchantTokensFeature .cxx_destruct]
+ -[PKWebServiceMerchantTokensFeature credentialTypesRequiringDPANNotifications]
+ _OBJC_IVAR_$_PKWebServiceMerchantTokensFeature._credentialTypesRequiringDPANNotifications
+ __OBJC_$_INSTANCE_VARIABLES_PKWebServiceMerchantTokensFeature
+ __OBJC_$_PROP_LIST_PKWebServiceMerchantTokensFeature
+ ___100-[PKAppletSubcredentialManagementSession setAccountAttestation:forUpgradeCredential:withCompletion:]_block_invoke
+ ___73-[PKDAManager setAccountAttestation:forUpgradeCredential:withCompletion:]_block_invoke
+ ___73-[PKDAManager setAccountAttestation:forUpgradeCredential:withCompletion:]_block_invoke_2
+ _objc_msgSend$setAccountAttestation:forUpgradeCredential:withCompletion:
- -[PKPaymentWebServiceConfiguration credentialTypesRequiringDPANNotifications]
Functions (modified):
~ -[PKWebServiceMerchantTokensFeature initWithDictionary:region:] : 68 -> 172
~ -[PKPaymentWebService paymentProvisioningNonceOfType:completion:] : 412 -> 556

Functions (added):
+ sub_190f9493c
+ sub_190fb9204
+ -[PKWebServiceMerchantTokensFeature credentialTypesRequiringDPANNotifications]
+ -[PKWebServiceMerchantTokensFeature .cxx_destruct]
+ [3 functions added in block]
+ -[PKAppletSubcredentialManagementSession setAccountAttestation:forUpgradeCredential:withCompletion:]
+ ___100-[PKAppletSubcredentialManagementSession setAccountAttestation:forUpgradeCredential:withCompletion:]_block_invoke

Functions (removed):
- sub_19125d5a4
- sub_1912aa0cc
- -[PKPaymentWebServiceConfiguration credentialTypesRequiringDPANNotifications]
CStrings:
+ "Failed to get provisioning nonce, deviceID unavailable for context: %@"
+ "T@\"NSSet\",R,C,N,V_credentialTypesRequiringDPANNotifications"
+ "_credentialTypesRequiringDPANNotifications"
+ "setAccountAttestation:forUpgradeCredential:withCompletion:"

```
