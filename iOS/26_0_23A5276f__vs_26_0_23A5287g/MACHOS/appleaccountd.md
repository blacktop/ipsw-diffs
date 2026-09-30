## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1027.0.0.0.0
-  __TEXT.__text: 0x2fa858
-  __TEXT.__auth_stubs: 0x28c0
+1030.0.0.0.0
+  __TEXT.__text: 0x2fecc8
+  __TEXT.__auth_stubs: 0x28e0
   __TEXT.__objc_methlist: 0xe9c
-  __TEXT.__objc_methname: 0x47dc
+  __TEXT.__objc_methname: 0x4839
   __TEXT.__objc_classname: 0x222
   __TEXT.__objc_methtype: 0x15fd
-  __TEXT.__cstring: 0x9074
-  __TEXT.__swift5_typeref: 0x65d3
+  __TEXT.__cstring: 0x90e4
+  __TEXT.__swift5_typeref: 0x6627
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xdf0c
-  __TEXT.__constg_swiftt: 0xb270
-  __TEXT.__swift5_reflstr: 0x5844
-  __TEXT.__swift5_fieldmd: 0x5754
+  __TEXT.__const: 0xe04c
+  __TEXT.__constg_swiftt: 0xb314
+  __TEXT.__swift5_reflstr: 0x5854
+  __TEXT.__swift5_fieldmd: 0x57d8
   __TEXT.__swift5_builtin: 0x244
-  __TEXT.__swift5_assocty: 0x758
-  __TEXT.__swift5_proto: 0xa10
-  __TEXT.__swift5_types: 0x53c
-  __TEXT.__oslogstring: 0x1b756
+  __TEXT.__swift5_assocty: 0x770
+  __TEXT.__swift5_proto: 0xa24
+  __TEXT.__swift5_types: 0x548
+  __TEXT.__oslogstring: 0x1bbf6
   __TEXT.__swift5_protos: 0x1fc
-  __TEXT.__swift5_capture: 0x5afc
-  __TEXT.__swift_as_entry: 0x3c0
-  __TEXT.__swift_as_ret: 0x4f8
+  __TEXT.__swift5_capture: 0x5b30
+  __TEXT.__swift_as_entry: 0x3cc
+  __TEXT.__swift_as_ret: 0x504
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x64b0
-  __TEXT.__eh_frame: 0xcf10
-  __DATA_CONST.__auth_got: 0x1460
-  __DATA_CONST.__got: 0xf20
-  __DATA_CONST.__auth_ptr: 0x1158
-  __DATA_CONST.__const: 0x11860
+  __TEXT.__unwind_info: 0x6b18
+  __TEXT.__eh_frame: 0xd1b0
+  __DATA_CONST.__auth_got: 0x1470
+  __DATA_CONST.__got: 0xf30
+  __DATA_CONST.__auth_ptr: 0x1168
+  __DATA_CONST.__const: 0x11ac8
   __DATA_CONST.__objc_classlist: 0x558
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x178

   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x1a5f8
-  __DATA.__objc_selrefs: 0x1498
+  __DATA.__objc_selrefs: 0x14b0
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x2e38
-  __DATA.__data: 0x118e0
+  __DATA.__data: 0x11910
   __DATA.__objc_stublist: 0x68
-  __DATA.__bss: 0xf300
+  __DATA.__bss: 0xf580
   __DATA.__common: 0x418
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EEA14E1F-C7CA-3711-9D0C-A1C098C6B55D
-  Functions: 8555
-  Symbols:   1320
-  CStrings:  3712
+  UUID: 3D8F47E4-AC8E-3DAD-B007-E7201E79C24F
+  Functions: 8599
+  Symbols:   1326
+  CStrings:  3734
 
Symbols:
+ _$s17_StringProcessing5RegexV06_regexA07versionACyxGSS_SitcfC
+ _$s17_StringProcessing5RegexV10firstMatch2inAC0E0Vyx_GSgSS_tKF
+ _$s17_StringProcessing5RegexV5MatchVMn
+ _$s17_StringProcessing5RegexVMn
+ _$sSsN
+ _kAAAnalyticsIdmsWalrusStatus
+ _swift_stdlib_random
- _$s10Foundation4DateV1goiySbAC_ACtFZ
CStrings:
+ "%s is 0 or negative in the url bag: %ld"
+ "Client is missing attestation entitlement"
+ "Couldn't find configuration container at %s in the url bag"
+ "Couldn't find configuration value at %s in the url bag, %s"
+ "CustodianRecord has no keyCreatedOnBuild, defaulting to unknown setup version, custodianID: %s"
+ "CustodianRecord.keyCreatedOnBuild %s has new format, confirmed LuckCheer+, custodianID: %s"
+ "CustodianRecord.keyCreatedOnBuild %s has old format, confirmed pre-LuckCheer, custodianID: %s"
+ "Date.now: %s, record created on: %s, grace period: %f, is past grace period: %{bool}d, custodianID: %s"
+ "Date.now: %s, record created on: %s, recent period: %f, is in recent period: %{bool}d, custodianID: %s"
+ "Determining record setup age..."
+ "Failed to save account property for user acknowledgment of misconfigured age prompt"
+ "Failed to save account when clearing user acknowledge migration prompt"
+ "Inferring record setup version..."
+ "Internal build: %s doesn't have override, checking in url bag"
+ "Internal build: using %s override"
+ "No recent period configured, assuming setup is recent"
+ "Not tearing down stale setup for custodianID: %s"
+ "Record is not CustodianRecord, defaulting to unknown setup version"
+ "Record setup age: %s, custodianID: %s"
+ "Stale setup tear-down %s because setup version is pre-LuckCheer, probability: %f"
+ "Stale setup tear-down disabled because setup version is pre-LuckCheer, probability: nil"
+ "Stale setup tear-down enabled because setup version is LuckCheer+"
+ "finalizeSetup(with:finalization:flow:altDSID:flowID:)"
+ "idmsWalrusStatusForAccount:"
+ "luckCheer"
+ "preLuckCheer"
+ "preLuckCheerStaleSetupTeardownProbabilityPercent"
+ "qualifiedBuildVersion"
+ "recentSetupGracePeriodMultiplier"
+ "saveVerifiedAccount:withCompletionHandler:"
+ "🔔 Internal build: %s override is set to: %ld"
- "Couldn't find a grace period key in the url bag, %s"
- "Couldn't find configuration key in the url bag"
- "Data.now: %s, record created on: %s, grace period: %ld, is past grace period: %{bool}d, custodianID: %s"
- "Grace period is 0 or negative in the url bag: %ld"
- "Internal build: grace period doesn't have overrides, checking in url bag"
- "Internal build: using grace period overrides"
- "cachedGracePeriod"
- "finalizeSetup(with:finalization:altDSID:flowID:)"
- "🔔 Internal build: grace period override is set to: %ld"

```
