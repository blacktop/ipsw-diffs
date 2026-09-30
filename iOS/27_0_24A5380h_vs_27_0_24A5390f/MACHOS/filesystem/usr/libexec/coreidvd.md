## coreidvd

> `/usr/libexec/coreidvd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__common`

```diff

-9.36.0.0.0
-  __TEXT.__text: 0x6f45cc
-  __TEXT.__auth_stubs: 0xd320
+9.38.0.0.0
+  __TEXT.__text: 0x6f61e0
+  __TEXT.__auth_stubs: 0xd310
   __TEXT.__objc_stubs: 0x7060
   __TEXT.__objc_methlist: 0x2114
-  __TEXT.__const: 0x32a00
-  __TEXT.__cstring: 0x2a7c0
-  __TEXT.__objc_classname: 0x36ce
-  __TEXT.__objc_methname: 0xdb36
+  __TEXT.__const: 0x32b20
+  __TEXT.__cstring: 0x2a930
+  __TEXT.__objc_classname: 0x370e
+  __TEXT.__objc_methname: 0xdb96
   __TEXT.__objc_methtype: 0x4a9e
-  __TEXT.__swift5_typeref: 0xc10a
-  __TEXT.__swift5_fieldmd: 0xe5b8
-  __TEXT.__constg_swiftt: 0xda68
+  __TEXT.__swift5_typeref: 0xc124
+  __TEXT.__swift5_fieldmd: 0xe644
+  __TEXT.__constg_swiftt: 0xdb38
   __TEXT.__swift5_builtin: 0x2e4
-  __TEXT.__swift5_reflstr: 0xc11e
+  __TEXT.__swift5_reflstr: 0xc1ae
   __TEXT.__swift5_assocty: 0xc58
   __TEXT.__swift5_protos: 0x1e0
-  __TEXT.__swift5_proto: 0x1e30
-  __TEXT.__swift5_types: 0xc2c
-  __TEXT.__oslogstring: 0x2e979
-  __TEXT.__swift5_capture: 0x6424
+  __TEXT.__swift5_proto: 0x1e34
+  __TEXT.__swift5_types: 0xc34
+  __TEXT.__oslogstring: 0x2e9e9
+  __TEXT.__swift5_capture: 0x64a0
   __TEXT.__swift5_mpenum: 0x98
-  __TEXT.__swift_as_entry: 0x1314
-  __TEXT.__swift_as_ret: 0x1c40
-  __TEXT.__swift_as_cont: 0x37e0
+  __TEXT.__swift_as_entry: 0x1328
+  __TEXT.__swift_as_ret: 0x1c4c
+  __TEXT.__swift_as_cont: 0x3814
   __TEXT.__swift5_acfuncs: 0x64
   __TEXT.__swift5_entry: 0x8
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__unwind_info: 0x16098
-  __TEXT.__eh_frame: 0x47c28
-  __DATA_CONST.__const: 0x24f00
+  __TEXT.__unwind_info: 0x16180
+  __TEXT.__eh_frame: 0x47ef0
+  __DATA_CONST.__const: 0x24fc0
   __DATA_CONST.__cfstring: 0xc0
-  __DATA_CONST.__objc_classlist: 0x730
+  __DATA_CONST.__objc_classlist: 0x738
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__linkguard: 0xe
-  __DATA_CONST.__auth_got: 0x69a0
-  __DATA_CONST.__got: 0x42b8
-  __DATA_CONST.__auth_ptr: 0x2410
-  __DATA.__objc_const: 0x11710
+  __DATA_CONST.__auth_got: 0x6998
+  __DATA_CONST.__got: 0x42c0
+  __DATA_CONST.__auth_ptr: 0x2418
+  __DATA.__objc_const: 0x11848
   __DATA.__objc_selrefs: 0x2598
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x37d0
-  __DATA.__data: 0x182c8
-  __DATA.__bss: 0x38530
+  __DATA.__data: 0x18418
+  __DATA.__bss: 0x385b0
   __DATA.__common: 0x722
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18844
+  Functions: 18890
   Symbols:   5967
-  CStrings:  8542
+  CStrings:  8560
 
Symbols:
+ _$s11CBORLibrary10COSE_Sign1V13CoreIDVSharedE19fromHexOrBinaryDataAC10Foundation0J0V_tKcfC
+ _$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO15documentExpiredyA2GmFWC
- _$s11CBORLibrary10COSE_Sign1V13CoreIDVSharedE11fromHexDataAC10Foundation0H0V_tKcfC
- _$s13CoreIDVShared26DaemonInternalDefaultsKeysO37enableTextUnderstandingVerboseLoggingSSvgZ
CStrings:
+ "\n- PDF417 firstName: "
+ "\n- PDF417 lastName: "
+ "\n- PDF417 postalCode: "
+ "\n- PDF417 state: "
+ "\n- PDF417 street1: "
+ "\n- TU fullAddress: "
+ "\n- TU lastName: "
+ "\n- TU postalCode: "
+ "\n- TU street (extracted): "
+ "IdentityProofingRequestManager: Attached TextUnderstanding metrics to proof-time documents (duration=%s, errorCode=%s, fuzzyMatch=%{bool}d)"
+ "IdentityProofingRequestManager: Cancelled previous TextUnderstanding task"
+ "IdentityProofingRequestManager: PDF417 decode failed for TextUnderstanding: %s"
+ "IdentityProofingRequestManager: Scheduled TextUnderstanding comparison from prepare (runs parallel with review)"
+ "IdentityProofingRequestManager: TextUnderstanding (prepare path) cancelled; not stashing result"
+ "IdentityProofingRequestManager: TextUnderstanding (prepare path) timed out or failed: %s. Continuing without result."
+ "IdentityProofingRequestManager: TextUnderstanding comparison in progress at proof time; metrics not attached"
+ "IdentityProofingRequestManager: TextUnderstanding result available but failed to attach to proof-time corrected_id_front capture metrics"
+ "TextUnderstandingIDComparator: Raw values before comparison\n- TU firstName: "
+ "_TtC8coreidvd38TextUnderstandingComparisonCoordinator"
+ "comparisonTask"
+ "generation"
+ "isComparisonRunning"
+ "pendingResult"
+ "textUnderstandingComparisonCoordinator"
- "IdentityProofingRequestManager: Cancelled previous Text Understanding task"
- "IdentityProofingRequestManager: PDF417 decode failed for Text Understanding: %s"
- "IdentityProofingRequestManager: Scheduled Text Understanding comparison from prepare (runs parallel with review)"
- "IdentityProofingRequestManager: Text Understanding (prepare path) timed out or failed: %s. Continuing without result."
- "TextUnderstandingIDComparator: Raw values before comparison\n- TU firstName: %{private}s\n- PDF417 firstName: %{private}s\n- TU lastName: %{private}s\n- PDF417 lastName: %{private}s\n- TU state: %{private}s\n- PDF417 state: %{private}s\n- TU address (fullAddress): %{private}s\n- PDF417 street1: %{private}s\n- TU postalCode: %{private}s\n- PDF417 postalCode: %{private}s"
- "textUnderstandingComparisonTask"
```
