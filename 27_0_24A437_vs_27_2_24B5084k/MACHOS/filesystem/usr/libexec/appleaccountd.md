## appleaccountd

> `/usr/libexec/appleaccountd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__objc_classname`
- `__TEXT.__cstring`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__objc_stublist`

```diff

-1067.0.0.0.0
-  __TEXT.__text: 0x3cabfc
-  __TEXT.__auth_stubs: 0x37d0
-  __TEXT.__objc_stubs: 0x4d40
+1069.125.4.0.0
+  __TEXT.__text: 0x3ceee0
+  __TEXT.__auth_stubs: 0x3810
+  __TEXT.__objc_stubs: 0x4de0
   __TEXT.__objc_methlist: 0xf80
-  __TEXT.__objc_methname: 0x77d5
+  __TEXT.__objc_methname: 0x78b5
   __TEXT.__objc_classname: 0x2e9d
   __TEXT.__cstring: 0x46a9
-  __TEXT.__objc_methtype: 0x2024
+  __TEXT.__objc_methtype: 0x2044
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x13350
-  __TEXT.__constg_swiftt: 0xc5f4
-  __TEXT.__swift5_typeref: 0x7993
+  __TEXT.__const: 0x133b0
+  __TEXT.__constg_swiftt: 0xc680
+  __TEXT.__swift5_typeref: 0x79eb
   __TEXT.__swift5_builtin: 0x2bc
   __TEXT.__swift5_reflstr: 0x66d5
-  __TEXT.__swift5_fieldmd: 0x6638
-  __TEXT.__swift5_assocty: 0x950
-  __TEXT.__swift5_proto: 0xc74
-  __TEXT.__swift5_types: 0x638
-  __TEXT.__swift5_capture: 0x65fc
-  __TEXT.__oslogstring: 0x20ccd
+  __TEXT.__swift5_fieldmd: 0x66a0
+  __TEXT.__swift5_assocty: 0x938
+  __TEXT.__swift5_proto: 0xc68
+  __TEXT.__swift5_types: 0x63c
+  __TEXT.__swift5_capture: 0x66a0
+  __TEXT.__oslogstring: 0x210ad
   __TEXT.__swift5_protos: 0x22c
-  __TEXT.__swift_as_entry: 0x674
-  __TEXT.__swift_as_ret: 0x87c
-  __TEXT.__swift_as_cont: 0x11c4
+  __TEXT.__swift_as_entry: 0x680
+  __TEXT.__swift_as_ret: 0x88c
+  __TEXT.__swift_as_cont: 0x11d8
   __TEXT.__swift5_acfuncs: 0xb4
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xa258
-  __TEXT.__eh_frame: 0x146cc
-  __DATA_CONST.__const: 0x13f60
+  __TEXT.__unwind_info: 0xa310
+  __TEXT.__eh_frame: 0x14824
+  __DATA_CONST.__const: 0x14048
   __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x1bf0
+  __DATA_CONST.__auth_got: 0x1c10
   __DATA_CONST.__got: 0x1580
-  __DATA_CONST.__auth_ptr: 0x1678
-  __DATA.__objc_const: 0x1e0f0
-  __DATA.__objc_selrefs: 0x1720
+  __DATA_CONST.__auth_ptr: 0x16a0
+  __DATA.__objc_const: 0x1e170
+  __DATA.__objc_selrefs: 0x1748
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x3360
-  __DATA.__data: 0x14300
+  __DATA.__data: 0x14480
   __DATA.__objc_stublist: 0x68
-  __DATA.__common: 0x4b8
+  __DATA.__common: 0x4e0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/StorageContainersPrivate.framework/StorageContainersPrivate
   - /System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10245
-  Symbols:   1815
-  CStrings:  4184
+  Functions: 10281
+  Symbols:   1820
+  CStrings:  4205
 
Symbols:
+ _$s14XPCDistributed9XPCSystemC7SessionC15RemoteInterfaceV10auditTokenSo0F8_token_taSgvg
+ _$s20IntelligencePlatform19PersonEntityTagTypeOMn
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateWithAuditToken
+ _objc_retain_x1
CStrings:
+ "%s - AutoHeal: CRK not exists on OT, But, Recovery Info Record has an RKC. canRepairUntrustedCRK gate is off. Aborting repair."
+ "%s - AutoHeal: CRK not exists on OT, Recovery Info Record has an RKC, but canRepairCustodian config read failed: %@. Emitting crkRepairNotAllowed with underlying error."
+ "%s - Could not ask CoreCDP to retire a stale PDP repair CFU: %s"
+ "Failed to resolve client bundle ID: could not create SecTask from audit token"
+ "Failed to resolve client bundle ID: could not read signing identifier from audit token"
+ "Failed to resolve client bundle ID: no remote invocation origin for the current XPC call"
+ "Failed to resolve client bundle ID: remote invocation origin has no audit token"
+ "RC upsell eligibility - reporting failure: cohort=%@, errorCode=%ld"
+ "Repair-eligibility config read from URL bag failed: %@. Continuing to TTR."
+ "UrlBagProvider - %s has unexpected type %s; treating as URL-bag anomaly."
+ "UrlBagProvider - canRepairCustodianV2 absent from urlbag; defaulting to false."
+ "UrlBagProvider - canRepairCustodianV2 has unexpected type %s; defaulting to false."
+ "UrlBagProvider - failed to read %s from URL bag: %@."
+ "_TtC13appleaccountd17MegadomeSuggester"
+ "canRepairCustodianV2"
+ "configurationValueForKey:fromCache:completion:"
+ "defaults"
+ "initWithDouble:"
+ "initWithHandle:contact:source:"
+ "isSyncAction"
+ "policy"
+ "process(_:originalStatus:postCFU:telemetryFlowID:flow:isSyncAction:)"
+ "retirementTimeout"
+ "setClientBundleID:"
+ "setIntelligenceScore:"
+ "v24@?0@8@\"NSError\"16"
+ "validateReachability"
+ "🔔 Internal build: %s override is set to: %s"
- "%s - AutoHeal: CRK not exists on OT, But, Recovery Info Record has an RKC. decoupleCRK is not enabled. Aborting repair."
- "RC upsell eligibility - reporting failure: cohort=%@, errorCode=%ld (%s)"
- "Using Health Check interval - One Week"
- "_TtC13appleaccountd26CustodianMegadomeSuggester"
- "canRepairCustodian"
- "com.apple.appleaccount.rcUpsellEligibility"
- "process(_:originalStatus:postCFU:telemetryFlowID:flow:)"
```
