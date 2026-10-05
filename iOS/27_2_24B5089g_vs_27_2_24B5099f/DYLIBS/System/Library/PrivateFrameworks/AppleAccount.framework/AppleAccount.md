## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_reflstr`

```diff

-1069.125.4.0.0
-  __TEXT.__text: 0x19c31c
+1069.125.7.0.0
+  __TEXT.__text: 0x19c830
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xb5a4
-  __TEXT.__cstring: 0x11532
-  __TEXT.__const: 0x10db0
-  __TEXT.__oslogstring: 0x13aad
+  __TEXT.__objc_methlist: 0xb59c
+  __TEXT.__cstring: 0x11552
+  __TEXT.__const: 0x10d60
+  __TEXT.__oslogstring: 0x13bdd
   __TEXT.__gcc_except_tab: 0x1bf8
   __TEXT.__dlopen_cstrs: 0x325
-  __TEXT.__swift5_typeref: 0x3a66
-  __TEXT.__constg_swiftt: 0x2a74
+  __TEXT.__swift5_typeref: 0x3a46
+  __TEXT.__constg_swiftt: 0x2a50
   __TEXT.__swift5_reflstr: 0x163a
-  __TEXT.__swift5_fieldmd: 0x2654
+  __TEXT.__swift5_fieldmd: 0x262c
   __TEXT.__swift5_builtin: 0x190
-  __TEXT.__swift5_assocty: 0x3d8
-  __TEXT.__swift5_proto: 0xc74
-  __TEXT.__swift5_types: 0x350
+  __TEXT.__swift5_assocty: 0x3f0
+  __TEXT.__swift5_proto: 0xc70
+  __TEXT.__swift5_types: 0x34c
   __TEXT.__swift5_mpenum: 0x6c
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_acfuncs: 0x1a4

   __TEXT.__swift_as_ret: 0x29c
   __TEXT.__swift_as_cont: 0x510
   __TEXT.__swift5_capture: 0x848
-  __TEXT.__unwind_info: 0x81f0
-  __TEXT.__eh_frame: 0x77a0
+  __TEXT.__unwind_info: 0x8200
+  __TEXT.__eh_frame: 0x77d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5260
+  __DATA_CONST.__objc_selrefs: 0x5278
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x590
   __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__got: 0x1168
-  __AUTH_CONST.__const: 0xd3a0
+  __DATA_CONST.__got: 0x1160
+  __AUTH_CONST.__const: 0xd460
   __AUTH_CONST.__cfstring: 0xd760
-  __AUTH_CONST.__objc_const: 0x26c18
+  __AUTH_CONST.__objc_const: 0x26bd8
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1508
+  __AUTH_CONST.__auth_got: 0x1500
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xbf4
-  __DATA.__data: 0x281c
+  __DATA.__objc_ivar: 0xbf0
+  __DATA.__data: 0x27fc
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x5cb0
   __DATA_DIRTY.__data: 0x3000

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9163
-  Symbols:   10033
-  CStrings:  3750
+  Functions: 9170
+  Symbols:   10029
+  CStrings:  3758
 
Symbols:
+ +[AALoginAccountRequest urlBagKey]
+ +[AARegisterRequest urlBagKey]
+ +[AAUpdateProvisioningRequest urlBagKey]
+ -[AADeviceList _deviceListRequestForURL:]
+ -[AARequest initWithURLConfig:]
+ -[AARequest urlConfig]
+ GCC_except_table121
+ _OBJC_CLASS_$_AKURLCachePolicyContext
+ _OBJC_IVAR_$_AARequest._urlConfig
+ _associated conformance 12AppleAccount31ProximityCustodianRecoveryErrorO10Foundation13CustomNSErrorAAs0F0
+ _associated conformance 12AppleAccount31ProximityCustodianRecoveryErrorO23SessionFailedCodingKeys33_655F54776971284348CFD24E395A41ABLLOSHAASQ
+ _associated conformance 12AppleAccount31ProximityCustodianRecoveryErrorO23SessionFailedCodingKeys33_655F54776971284348CFD24E395A41ABLLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 12AppleAccount31ProximityCustodianRecoveryErrorO23SessionFailedCodingKeys33_655F54776971284348CFD24E395A41ABLLOs0I3KeyAAs28CustomDebugStringConvertible
+ _symbolic _____ 12AppleAccount31ProximityCustodianRecoveryErrorO23SessionFailedCodingKeys33_655F54776971284348CFD24E395A41ABLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12AppleAccount31ProximityCustodianRecoveryErrorO23SessionFailedCodingKeys33_655F54776971284348CFD24E395A41ABLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12AppleAccount31ProximityCustodianRecoveryErrorO23SessionFailedCodingKeys33_655F54776971284348CFD24E395A41ABLLO
- -[AALoginAccountRequest urlString]
- -[AARegisterRequest urlString]
- -[AAURLConfiguration(Deprecated) fetchAccountSettingsURL]
- -[AAURLConfiguration(Deprecated) loginAccountURL]
- -[AAURLConfiguration(Deprecated) signInURL]
- -[AAUpdateProvisioningRequest urlString]
- GCC_except_table119
- _OBJC_IVAR_$_AALoginAccountRequest._urlConfig
- _OBJC_IVAR_$_AAUpdateProvisioningRequest._urlConfig
- _associated conformance 12AppleAccount31ProximityCustodianRecoveryErrorO17GenericCodingKeys33_655F54776971284348CFD24E395A41ABLLOSHAASQ
- _associated conformance 12AppleAccount31ProximityCustodianRecoveryErrorO17GenericCodingKeys33_655F54776971284348CFD24E395A41ABLLOs0H3KeyAAs23CustomStringConvertible
- _associated conformance 12AppleAccount31ProximityCustodianRecoveryErrorO17GenericCodingKeys33_655F54776971284348CFD24E395A41ABLLOs0H3KeyAAs28CustomDebugStringConvertible
- _associated conformance 12AppleAccount31ProximityCustodianRecoveryErrorO17UnknownCodingKeys33_655F54776971284348CFD24E395A41ABLLOs0H3KeyAAs23CustomStringConvertible
- _associated conformance 12AppleAccount31ProximityCustodianRecoveryErrorO17UnknownCodingKeys33_655F54776971284348CFD24E395A41ABLLOs0H3KeyAAs28CustomDebugStringConvertible
- _symbolic _____ 12AppleAccount31ProximityCustodianRecoveryErrorO17GenericCodingKeys33_655F54776971284348CFD24E395A41ABLLO
- _symbolic _____ 12AppleAccount31ProximityCustodianRecoveryErrorO17UnknownCodingKeys33_655F54776971284348CFD24E395A41ABLLO
- _symbolic _____y_____G s22KeyedDecodingContainerV 12AppleAccount31ProximityCustodianRecoveryErrorO17GenericCodingKeys33_655F54776971284348CFD24E395A41ABLLO
- _symbolic _____y_____G s22KeyedDecodingContainerV 12AppleAccount31ProximityCustodianRecoveryErrorO17UnknownCodingKeys33_655F54776971284348CFD24E395A41ABLLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 12AppleAccount31ProximityCustodianRecoveryErrorO17GenericCodingKeys33_655F54776971284348CFD24E395A41ABLLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 12AppleAccount31ProximityCustodianRecoveryErrorO17UnknownCodingKeys33_655F54776971284348CFD24E395A41ABLLO
CStrings:
+ "AASignInFlowController: Sign in - server backoff suppressed the login request"
+ "Avatar optimized for upload"
+ "Fetched identity from remote service"
+ "Received identity change notification for unregistered account: %{private,mask.hash}@"
+ "Starting observation with initial update if different from known identity"
+ "Starting observation with no initial update"
+ "generic"
+ "navigatedBack"
+ "userCancelled"
- "Received identity change notification for unregistered account: %@"
```
