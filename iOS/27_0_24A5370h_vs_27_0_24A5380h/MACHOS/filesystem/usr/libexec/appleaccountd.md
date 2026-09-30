## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-  __TEXT.__text: 0x3eaeac
-  __TEXT.__auth_stubs: 0x37c0
-  __TEXT.__objc_stubs: 0x4c80
+  __TEXT.__text: 0x3edc54
+  __TEXT.__auth_stubs: 0x37d0
+  __TEXT.__objc_stubs: 0x4cc0
   __TEXT.__objc_methlist: 0xf80
-  __TEXT.__objc_methname: 0x76a5
+  __TEXT.__objc_methname: 0x7705
   __TEXT.__objc_classname: 0x2e6d
-  __TEXT.__cstring: 0x4519
-  __TEXT.__objc_methtype: 0x201e
+  __TEXT.__cstring: 0x4579
+  __TEXT.__objc_methtype: 0x2014
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x13070
-  __TEXT.__constg_swiftt: 0xc4b0
-  __TEXT.__swift5_typeref: 0x7869
-  __TEXT.__swift5_builtin: 0x2a8
-  __TEXT.__swift5_reflstr: 0x6665
-  __TEXT.__swift5_fieldmd: 0x6590
-  __TEXT.__swift5_assocty: 0x920
-  __TEXT.__swift5_proto: 0xc54
-  __TEXT.__swift5_types: 0x62c
-  __TEXT.__swift5_capture: 0x6510
-  __TEXT.__oslogstring: 0x204fd
+  __TEXT.__const: 0x13230
+  __TEXT.__constg_swiftt: 0xc4f8
+  __TEXT.__swift5_typeref: 0x7893
+  __TEXT.__swift5_builtin: 0x2bc
+  __TEXT.__swift5_reflstr: 0x6685
+  __TEXT.__swift5_fieldmd: 0x65b8
+  __TEXT.__swift5_assocty: 0x950
+  __TEXT.__swift5_proto: 0xc6c
+  __TEXT.__swift5_types: 0x630
+  __TEXT.__swift5_capture: 0x6520
+  __TEXT.__oslogstring: 0x2081d
   __TEXT.__swift5_protos: 0x220
-  __TEXT.__swift_as_entry: 0x65c
-  __TEXT.__swift_as_ret: 0x860
-  __TEXT.__swift_as_cont: 0x119c
+  __TEXT.__swift_as_entry: 0x664
+  __TEXT.__swift_as_ret: 0x86c
+  __TEXT.__swift_as_cont: 0x11b4
   __TEXT.__swift5_acfuncs: 0xb4
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x8430
-  __TEXT.__eh_frame: 0x1451c
-  __DATA_CONST.__const: 0x13ca8
+  __TEXT.__unwind_info: 0x8480
+  __TEXT.__eh_frame: 0x1464c
+  __DATA_CONST.__const: 0x13d28
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x1be8
+  __DATA_CONST.__auth_got: 0x1bf0
   __DATA_CONST.__got: 0x1570
   __DATA_CONST.__auth_ptr: 0x1668
-  __DATA.__objc_const: 0x1dce8
-  __DATA.__objc_selrefs: 0x16f0
+  __DATA.__objc_const: 0x1dd08
+  __DATA.__objc_selrefs: 0x1700
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x3348
-  __DATA.__data: 0x141d0
+  __DATA.__data: 0x14200
   __DATA.__objc_stublist: 0x68
-  __DATA.__bss: 0x13700
+  __DATA.__bss: 0x13a00
   __DATA.__common: 0x4b8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10179
-  Symbols:   1813
-  CStrings:  4159
+  Functions: 10200
+  Symbols:   1814
+  CStrings:  4173
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_acfuncs : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__objc_stublist : content changed
~ __DATA.__common : content changed
Symbols:
+ _$sSD10FoundationE34_conditionallyBridgeFromObjectiveC_6resultSbSo12NSDictionaryC_SDyxq_GSgztFZ
+ _OBJC_CLASS_$_ACDataclassAction
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "AccountUpdatePerformer - Failed to save account with dataclass actions:%s with error: %@"
+ "AccountUpdatePerformer - No account on disk for altDSID; skipping save with dataclass actions."
+ "AccountUpdatePerformer - No dataclass actions to save (nil or empty); skipping save."
+ "Custodian handleFailedSetup failed for custodianID: %s, error: %@"
+ "Custodian not tearing down setup; teardownActionEnabled is false for custodianID: %s"
+ "DaemonAccountStore - Failed to bridge ACDataclassActions to [ACAccount.Dataclass: ACDataclassAction]."
+ "Owner handleFailedSetup failed for custodianID: %s, error: %@"
+ "Owner not tearing down setup; teardownActionEnabled is false for custodianID: %s"
+ "aa_sanitizeError:"
+ "aa_updateAccountWithProvisioningResponse:"
+ "cleanupOrphanedCustodiansV2"
+ "ownerSetupGracePeriodV2InSeconds"
+ "retainedProvider"
+ "saveAccount:withDataclassActions:completion:"
+ "teardownActionEnabled"
+ "🔔 Internal build: %s override is set to: %{bool}d"
- "aa_updateWithProvisioningResponse:"
- "cleanupOrphanedCustodians"

```
