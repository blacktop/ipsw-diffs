## AppleIDSetupUI

> `/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI`

```diff

-128.1.1.0.0
-  __TEXT.__text: 0x176860
+129.125.3.0.0
+  __TEXT.__text: 0x178218
   __TEXT.__objc_methlist: 0x26cc
-  __TEXT.__const: 0xd7f4
-  __TEXT.__cstring: 0x4e89
+  __TEXT.__const: 0xd944
+  __TEXT.__cstring: 0x4f09
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__constg_swiftt: 0x56a4
-  __TEXT.__swift5_typeref: 0xef16
+  __TEXT.__constg_swiftt: 0x5704
+  __TEXT.__swift5_typeref: 0xef28
   __TEXT.__swift5_builtin: 0x1cc
-  __TEXT.__swift5_reflstr: 0x3ec2
-  __TEXT.__swift5_fieldmd: 0x3588
+  __TEXT.__swift5_reflstr: 0x3fc2
+  __TEXT.__swift5_fieldmd: 0x3620
   __TEXT.__swift5_assocty: 0xc20
-  __TEXT.__swift5_proto: 0x4b8
-  __TEXT.__swift5_types: 0x3b0
-  __TEXT.__oslogstring: 0xb6ad
-  __TEXT.__swift_as_entry: 0x458
-  __TEXT.__swift_as_ret: 0x424
-  __TEXT.__swift_as_cont: 0x8dc
+  __TEXT.__swift5_proto: 0x4c0
+  __TEXT.__swift5_types: 0x3b8
+  __TEXT.__oslogstring: 0xb95d
+  __TEXT.__swift_as_entry: 0x474
+  __TEXT.__swift_as_ret: 0x454
+  __TEXT.__swift_as_cont: 0x908
   __TEXT.__swift5_capture: 0x2cd8
   __TEXT.__swift5_protos: 0x70
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x6900
-  __TEXT.__eh_frame: 0xb0d8
+  __TEXT.__unwind_info: 0x69d8
+  __TEXT.__eh_frame: 0xb410
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x498
-  __DATA_CONST.__objc_classlist: 0x300
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__got: 0x14f0
-  __AUTH_CONST.__const: 0xa920
+  __DATA_CONST.__got: 0x14e8
+  __AUTH_CONST.__const: 0xa9b0
   __AUTH_CONST.__cfstring: 0xae0
-  __AUTH_CONST.__objc_const: 0x11928
+  __AUTH_CONST.__objc_const: 0x11ac0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x2520
-  __AUTH.__objc_data: 0x5168
-  __AUTH.__data: 0x3b20
+  __AUTH_CONST.__auth_got: 0x2510
+  __AUTH.__objc_data: 0x5158
+  __AUTH.__data: 0x3c10
   __DATA.__objc_ivar: 0x50
-  __DATA.__data: 0x5728
+  __DATA.__data: 0x5708
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x308
   __DATA_DIRTY.__data: 0x160

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7233
-  Symbols:   3881
-  CStrings:  1281
+  Functions: 7268
+  Symbols:   3887
+  CStrings:  1289
 
Symbols:
+ __DATA__TtC14AppleIDSetupUI28AgeVerificationConfiguration
+ __IVARS__TtC14AppleIDSetupUI28AgeVerificationConfiguration
+ __METACLASS_DATA__TtC14AppleIDSetupUI28AgeVerificationConfiguration
+ _associated conformance 14AppleIDSetupUI19AgeVerificationModeOSHAASQ
+ _symbolic _____ 14AppleIDSetupUI19AgeVerificationModeO
+ _symbolic _____ 14AppleIDSetupUI28AgeVerificationConfigurationC
+ _symbolic _____Sg 14AppleIDSetupUI28AgeVerificationConfigurationC
+ _symbolic ______p 14AppleIDSetupUI16AKDeviceProtocolP
+ _symbolic ______pXp 14AppleIDSetupUI27AISSelfieFaceIDTaskProtocolP
+ _symbolic ______pXp 14AppleIDSetupUI36PASAgeVerificationControllerProtocolP
- _symbolic _____Sg 12AppleIDSetup19AgeAssuranceContextC
- _symbolic ______p 12AppleIDSetup25AISScreenTimeShimProtocolP
- _symbolic ______pSg 14AppleIDSetupUI27AISSelfieFaceIDTaskProtocolP
- _symbolic ______pXpSg 14AppleIDSetupUI36PASAgeVerificationControllerProtocolP
CStrings:
+ "AgeAssuranceFlowPresenter - background Face ID verification failed; applying WCF/CS - %@"
+ "AgeAssuranceFlowPresenter - background Face ID verification succeeded; account verified, no restrictions applied"
+ "AgeAssuranceFlowPresenter - background mode could not verify without UI; applying WCF/CS"
+ "AgeAssuranceFlowPresenter - background mode resolved a regulatory step; applying WCF/CS without presenting AVK UI"
+ "AgeAssuranceFlowPresenter - background mode: presenter unexpectedly nil"
+ "AgeVerificationPresenter - createWithAuthResponse called without authResponse"
+ "AgeVerificationPresenter.createRegulatoryStep - bag is nil, cannot build regulatory fallback step"
+ "AgeVerificationPresenter.prepareVerificationUI - background mode: re-throwing selfie failure to caller"
+ "Applied WCF/CS account restrictions in background - %{bool}d"
+ "Applying WCF/CS account restrictions in background"
+ "Failed to apply account restrictions in background with error: %@"
+ "WCF/CS restrictions reported not applied without an error"
+ "WCF/CS restrictions reported not applied without an error for no-account flow"
+ "WCF/CS restrictions were not applied"
- "AgeAssuranceFlowPresenter - restrictions-only flow detected, applying background restrictions"
- "Applying background restrictions for unverified adult via ScreenTime shim"
- "Applying restrictions for no-account scenario"
- "Failed to apply background restrictions with error: %@"
- "Successfully applied background restrictions"
- "Successfully applied restrictions for no-account scenario - %{bool}d"
```
