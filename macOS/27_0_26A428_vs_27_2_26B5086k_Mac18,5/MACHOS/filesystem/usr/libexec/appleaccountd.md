## appleaccountd

> `/usr/libexec/appleaccountd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__objc_classname`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__objc_stublist`

```diff

-1067.0.0.0.0
-  __TEXT.__text: 0x3bdf84
-  __TEXT.__auth_stubs: 0x3370
-  __TEXT.__objc_stubs: 0x4b00
+1069.125.4.0.0
+  __TEXT.__text: 0x3c257c
+  __TEXT.__auth_stubs: 0x33a0
+  __TEXT.__objc_stubs: 0x4ba0
   __TEXT.__objc_methlist: 0xee8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x11e30
-  __TEXT.__constg_swiftt: 0xbc70
-  __TEXT.__swift5_typeref: 0x72ed
+  __TEXT.__const: 0x11f80
+  __TEXT.__constg_swiftt: 0xbd18
+  __TEXT.__swift5_typeref: 0x7353
   __TEXT.__swift5_builtin: 0x280
-  __TEXT.__swift5_reflstr: 0x6205
-  __TEXT.__swift5_fieldmd: 0x60f0
+  __TEXT.__swift5_reflstr: 0x62a5
+  __TEXT.__swift5_fieldmd: 0x61b0
   __TEXT.__swift5_assocty: 0x870
   __TEXT.__swift5_proto: 0xb94
-  __TEXT.__swift5_types: 0x5d4
+  __TEXT.__swift5_types: 0x5dc
   __TEXT.__objc_classname: 0x2b3d
-  __TEXT.__objc_methname: 0x7225
-  __TEXT.__objc_methtype: 0x1f04
-  __TEXT.__swift5_capture: 0x6430
+  __TEXT.__objc_methname: 0x7315
+  __TEXT.__objc_methtype: 0x1f24
+  __TEXT.__swift5_capture: 0x64d4
   __TEXT.__swift5_protos: 0x200
-  __TEXT.__oslogstring: 0x1fcdd
-  __TEXT.__cstring: 0x43a9
+  __TEXT.__oslogstring: 0x200bd
+  __TEXT.__cstring: 0x43d9
   __TEXT.__swift5_acfuncs: 0xa0
-  __TEXT.__swift_as_entry: 0x5c8
-  __TEXT.__swift_as_ret: 0x7a0
-  __TEXT.__swift_as_cont: 0x102c
+  __TEXT.__swift_as_entry: 0x5d4
+  __TEXT.__swift_as_ret: 0x7b0
+  __TEXT.__swift_as_cont: 0x1040
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x9a48
-  __TEXT.__eh_frame: 0x1294c
-  __DATA_CONST.__const: 0x137e8
+  __TEXT.__unwind_info: 0x9b28
+  __TEXT.__eh_frame: 0x12aa4
+  __DATA_CONST.__const: 0x13960
   __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd0
-  __DATA_CONST.__auth_got: 0x19c0
+  __DATA_CONST.__auth_got: 0x19d8
   __DATA_CONST.__got: 0x1488
-  __DATA_CONST.__auth_ptr: 0x1568
-  __DATA.__objc_const: 0x1cff0
-  __DATA.__objc_selrefs: 0x1670
+  __DATA_CONST.__auth_ptr: 0x1590
+  __DATA.__objc_const: 0x1d070
+  __DATA.__objc_selrefs: 0x1698
   __DATA.__objc_data: 0x2ff8
-  __DATA.__data: 0x13150
+  __DATA.__data: 0x132b0
   __DATA.__objc_stublist: 0x68
-  __DATA.__common: 0x498
+  __DATA.__common: 0x4c0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /System/Library/PrivateFrameworks/StorageContainersPrivate.framework/Versions/A/StorageContainersPrivate
   - /System/Library/PrivateFrameworks/XPCDistributed.framework/Versions/A/XPCDistributed
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9805
-  Symbols:   1709
-  CStrings:  4041
+  Functions: 9851
+  Symbols:   1713
+  CStrings:  4063
 
Symbols:
+ _$s14XPCDistributed9XPCSystemC7SessionC15RemoteInterfaceV10auditTokenSo0F8_token_taSgvg
+ _$s20IntelligencePlatform19PersonEntityTagTypeOMn
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateWithAuditToken
CStrings:
+ "%s - AutoHeal: CRK not exists on OT, But, Recovery Info Record has an RKC. canRepairUntrustedCRK gate is off. Aborting repair."
+ "%s - AutoHeal: CRK not exists on OT, Recovery Info Record has an RKC, but canRepairCustodian config read failed: %@. Emitting crkRepairNotAllowed with underlying error."
+ "%s - Could not ask CoreCDP to retire a stale PDP repair CFU: %s"
+ "Failed to resolve client bundle ID: could not create SecTask from audit token"
+ "Failed to resolve client bundle ID: could not read signing identifier from audit token"
+ "Failed to resolve client bundle ID: no remote invocation origin for the current XPC call"
+ "Failed to resolve client bundle ID: remote invocation origin has no audit token"
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
- "Using Health Check interval - One Week"
- "_TtC13appleaccountd26CustodianMegadomeSuggester"
- "canRepairCustodian"
- "process(_:originalStatus:postCFU:telemetryFlowID:flow:)"
```
