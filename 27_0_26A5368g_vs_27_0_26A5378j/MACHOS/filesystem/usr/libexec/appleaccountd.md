## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-  __TEXT.__text: 0x3cf7a8
+  __TEXT.__text: 0x3d24c4
   __TEXT.__auth_stubs: 0x2f60
-  __TEXT.__objc_stubs: 0x49e0
+  __TEXT.__objc_stubs: 0x4a20
   __TEXT.__objc_methlist: 0xe18
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x119d0
-  __TEXT.__constg_swiftt: 0xbae4
-  __TEXT.__swift5_typeref: 0x6f87
-  __TEXT.__swift5_builtin: 0x26c
-  __TEXT.__swift5_reflstr: 0x6115
-  __TEXT.__swift5_fieldmd: 0x6004
-  __TEXT.__swift5_assocty: 0x840
-  __TEXT.__swift5_proto: 0xb78
-  __TEXT.__swift5_types: 0x5c8
+  __TEXT.__const: 0x11b60
+  __TEXT.__constg_swiftt: 0xbb2c
+  __TEXT.__swift5_typeref: 0x6fb1
+  __TEXT.__swift5_builtin: 0x280
+  __TEXT.__swift5_reflstr: 0x6135
+  __TEXT.__swift5_fieldmd: 0x602c
+  __TEXT.__swift5_assocty: 0x870
+  __TEXT.__swift5_proto: 0xb90
+  __TEXT.__swift5_types: 0x5cc
   __TEXT.__objc_classname: 0x2aad
-  __TEXT.__objc_methtype: 0x1e1e
-  __TEXT.__objc_methname: 0x6f25
-  __TEXT.__swift5_capture: 0x6258
+  __TEXT.__objc_methtype: 0x1e14
+  __TEXT.__objc_methname: 0x6f95
+  __TEXT.__swift5_capture: 0x6268
   __TEXT.__swift5_protos: 0x1f8
-  __TEXT.__oslogstring: 0x1f1ed
-  __TEXT.__cstring: 0x4209
+  __TEXT.__oslogstring: 0x1f50d
+  __TEXT.__cstring: 0x4269
   __TEXT.__swift5_acfuncs: 0xa0
-  __TEXT.__swift_as_entry: 0x580
-  __TEXT.__swift_as_ret: 0x738
-  __TEXT.__swift_as_cont: 0xf78
+  __TEXT.__swift_as_entry: 0x588
+  __TEXT.__swift_as_ret: 0x744
+  __TEXT.__swift_as_cont: 0xf90
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x7c38
-  __TEXT.__eh_frame: 0x11f8c
-  __DATA_CONST.__const: 0x132a0
+  __TEXT.__unwind_info: 0x7c80
+  __TEXT.__eh_frame: 0x120c4
+  __DATA_CONST.__const: 0x13320
   __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x180

   __DATA_CONST.__auth_got: 0x17b8
   __DATA_CONST.__got: 0x12c0
   __DATA_CONST.__auth_ptr: 0x14a0
-  __DATA.__objc_const: 0x1bfe8
-  __DATA.__objc_selrefs: 0x1600
+  __DATA.__objc_const: 0x1c008
+  __DATA.__objc_selrefs: 0x1610
   __DATA.__objc_data: 0x2f30
   __DATA.__data: 0x12e28
   __DATA.__objc_stublist: 0x68
-  __DATA.__bss: 0x12180
+  __DATA.__bss: 0x12480
   __DATA.__common: 0x490
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9621
+  Functions: 9643
   Symbols:   1579
-  CStrings:  3976
+  CStrings:  3990
 
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
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__objc_stublist : content changed
~ __DATA.__common : content changed
Symbols:
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
