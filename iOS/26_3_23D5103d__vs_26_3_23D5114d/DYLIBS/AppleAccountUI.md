## AppleAccountUI

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI`

```diff

-553.325.2.0.0
-  __TEXT.__text: 0x256398
-  __TEXT.__auth_stubs: 0x3c10
+553.325.3.0.0
+  __TEXT.__text: 0x252ba0
+  __TEXT.__auth_stubs: 0x3bf0
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0x2d0
-  __TEXT.__objc_methlist: 0xb52c
+  __TEXT.__objc_methlist: 0xb4cc
   __TEXT.__cstring: 0xa6b9
-  __TEXT.__const: 0xbe94
+  __TEXT.__const: 0xbe84
   __TEXT.__gcc_except_tab: 0x16cc
-  __TEXT.__oslogstring: 0xe81c
+  __TEXT.__oslogstring: 0xe73c
   __TEXT.__dlopen_cstrs: 0x526
   __TEXT.__ustring: 0x4
-  __TEXT.__constg_swiftt: 0x4c04
-  __TEXT.__swift5_typeref: 0xd6ac
-  __TEXT.__swift5_reflstr: 0x2666
-  __TEXT.__swift5_fieldmd: 0x24a0
+  __TEXT.__constg_swiftt: 0x4bb4
+  __TEXT.__swift5_typeref: 0xd66c
+  __TEXT.__swift5_reflstr: 0x2636
+  __TEXT.__swift5_fieldmd: 0x2488
   __TEXT.__swift5_types: 0x454
-  __TEXT.__swift5_capture: 0x2b4c
+  __TEXT.__swift5_capture: 0x2a24
   __TEXT.__swift5_assocty: 0xc50
   __TEXT.__swift5_proto: 0x5c4
   __TEXT.__swift_as_entry: 0x108

   __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5698
+  __TEXT.__unwind_info: 0x5660
   __TEXT.__eh_frame: 0x1518
-  __TEXT.__objc_classname: 0x2247
-  __TEXT.__objc_methname: 0x1b91f
-  __TEXT.__objc_methtype: 0x5110
+  __TEXT.__objc_classname: 0x222f
+  __TEXT.__objc_methname: 0x1b89d
+  __TEXT.__objc_methtype: 0x508e
   __TEXT.__objc_stubs: 0x13c40
   __DATA_CONST.__got: 0x1c78
-  __DATA_CONST.__const: 0x3288
+  __DATA_CONST.__const: 0x3290
   __DATA_CONST.__objc_classlist: 0x7f8
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x380
+  __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68b8
-  __DATA_CONST.__objc_protorefs: 0xd0
+  __DATA_CONST.__objc_selrefs: 0x6898
+  __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x1e28
-  __AUTH_CONST.__const: 0xa018
-  __AUTH_CONST.__cfstring: 0x4ce0
-  __AUTH_CONST.__objc_const: 0x3d7b0
+  __AUTH_CONST.__auth_got: 0x1e18
+  __AUTH_CONST.__const: 0x9d20
+  __AUTH_CONST.__cfstring: 0x4d20
+  __AUTH_CONST.__objc_const: 0x3d458
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH.__objc_data: 0x6cc0
+  __AUTH.__objc_data: 0x6c60
   __AUTH.__data: 0x2a50
   __DATA.__objc_ivar: 0xbec
-  __DATA.__data: 0x5680
+  __DATA.__data: 0x55d0
   __DATA.__bss: 0xc000
   __DATA.__common: 0x4c8
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E54F6731-875D-39F9-A7D5-CD29B1039806
-  Functions: 11693
-  Symbols:   17598
-  CStrings:  8178
+  UUID: 5559088A-6356-3236-91E1-6F982C51404E
+  Functions: 11646
+  Symbols:   17580
+  CStrings:  8167
 
Symbols:
+ _block_copy_helper.41
+ _block_descriptor.43
+ _block_destroy_helper.42
+ _kAAAnalyticsEventSignInDeleteLocalData
+ _kAAAnalyticsEventSignInMergeLocalData
+ _kAAAnalyticsEventSignOutEraseFlowSelected
+ _kAAAnalyticsEventSignOutWithoutErasingSelected
- _AAUISignOutErrorDomain
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CDPWalrusStatusProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_CDPWalrusStatusProvider
- __OBJC_$_PROTOCOL_REFS_CDPWalrusStatusProvider
- __OBJC_LABEL_PROTOCOL_$_CDPWalrusStatusProvider
- __OBJC_PROTOCOL_$_CDPWalrusStatusProvider
- _block_copy_helper.107
- _block_copy_helper.42
- _block_descriptor.109
- _block_descriptor.44
- _block_destroy_helper.108
- _block_destroy_helper.43
- _flat unique So23CDPWalrusStatusProvider_p
- _kAAAnalyticsEventPrivacyRepromptClicked
- _kAAAnalyticsEventPrivacyRepromptShown
- _symbolic SuIegd_
- _symbolic SuIegr_
- _symbolic SuIegy_
- _symbolic ______pSg So23CDPWalrusStatusProviderP
CStrings:
+ "com.apple.appleaccount.signIn.deleteLocalData"
+ "com.apple.appleaccount.signIn.mergeLocalData"
+ "com.apple.appleaccount.signOutEraseFlowSelected"
+ "com.apple.appleaccount.signOutWithoutErasingSelected"
- "@\"CDPCombinedWalrusStatus\"24@0:8^@16"
- "CDPWalrusStatusProvider"
- "Failed to query CDP Walrus status: %s"
- "Missing altDSID or flow ID for telemetry"
- "Privacy reprompt clicked event sent with ADP state: %lu"
- "Privacy reprompt shown event sent with ADP state: %lu"
- "Q24@0:8^@16"
- "advancedDataProtectionState"
- "com.apple.appleaccount.privacyRepromptClicked"
- "com.apple.appleaccount.privacyRepromptShown"
- "combinedWalrusStatus:"
- "combinedWalrusStatusWithCompletion:"
- "initWithAccount:walrusStatusProvider:"
- "repairWalrusStatusWithCompletion:"
- "v24@0:8@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">16"
- "v24@0:8@?<v@?Q@\"NSError\">16"
- "walrusStatusProvider"

```
