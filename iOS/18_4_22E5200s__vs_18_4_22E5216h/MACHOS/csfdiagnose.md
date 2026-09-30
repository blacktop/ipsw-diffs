## csfdiagnose

> `/usr/bin/csfdiagnose`

```diff

-301.22.4.9.0
-  __TEXT.__text: 0x14628
-  __TEXT.__auth_stubs: 0xcb0
+301.22.4.13.0
+  __TEXT.__text: 0x13730
+  __TEXT.__auth_stubs: 0xb80
   __TEXT.__const: 0x1332
-  __TEXT.__cstring: 0x11e0
-  __TEXT.__swift5_typeref: 0x4ee
+  __TEXT.__cstring: 0xf71
+  __TEXT.__swift5_typeref: 0x4a9
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_fieldmd: 0x580
+  __TEXT.__swift5_fieldmd: 0x598
   __TEXT.__constg_swiftt: 0x378
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_reflstr: 0x21c
+  __TEXT.__swift5_reflstr: 0x22c
   __TEXT.__swift5_capture: 0x34
-  __TEXT.__objc_methname: 0x11d
+  __TEXT.__objc_methname: 0xfb
   __TEXT.__swift5_proto: 0x158
   __TEXT.__swift5_types: 0x60
-  __TEXT.__swift_as_entry: 0x14
-  __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0x570
-  __TEXT.__eh_frame: 0x998
-  __DATA_CONST.__auth_got: 0x658
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__auth_ptr: 0x1b8
-  __DATA_CONST.__const: 0xce0
+  __TEXT.__swift_as_entry: 0x10
+  __TEXT.__swift_as_ret: 0x24
+  __TEXT.__unwind_info: 0x510
+  __TEXT.__eh_frame: 0x820
+  __DATA_CONST.__auth_got: 0x5c0
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__auth_ptr: 0x1a0
+  __DATA_CONST.__const: 0xcb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x68
-  __DATA.__data: 0x808
-  __DATA.__common: 0x188
+  __DATA.__objc_selrefs: 0x60
+  __DATA.__data: 0x810
+  __DATA.__common: 0x1b8
   __DATA.__bss: 0x2b00
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 455
-  Symbols:   343
-  CStrings:  95
+  Functions: 434
+  Symbols:   317
+  CStrings:  81
 
Symbols:
+ _$s25CloudSubscriptionFeatures12FeatureCacheC03allC07forDSID15allowAnySession9ignoreTTLSayAA0aD0CGSSSg_S2btF
+ _$s25CloudSubscriptionFeatures20FrameworkDiagnosticsV13DiagnosticKeyO13coreTelephonyyA2EmFWC
+ _$s25CloudSubscriptionFeatures23CoreTelephonyDiagnosticVMa
+ _$s25CloudSubscriptionFeatures23CoreTelephonyDiagnosticVMn
+ _$s25CloudSubscriptionFeatures23CoreTelephonyDiagnosticVSEAAMc
+ _$s25CloudSubscriptionFeatures23CoreTelephonyDiagnosticVSeAAMc
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _$s25CloudSubscriptionFeatures12FeatureCacheC03allC07forDSID9ignoreTTLSayAA0aD0CGSSSg_SbtF
- _$s25CloudSubscriptionFeatures13ReleaseReasonO8rawValueSSvg
- _$s25CloudSubscriptionFeatures13ReleaseReasonOMa
- _$s25CloudSubscriptionFeatures13ReleaseReasonOMn
- _$s25CloudSubscriptionFeatures17AvailabilityModelV19shouldReleaseModelsAA0G6ReasonOSgyYaF
- _$s25CloudSubscriptionFeatures17AvailabilityModelV19shouldReleaseModelsAA0G6ReasonOSgyYaFTu
- _$s25CloudSubscriptionFeatures6AssetsC6sharedAA0D15StatusProviding_pvgZ
- _$s25CloudSubscriptionFeatures6AssetsCMa
- _$s25CloudSubscriptionFeatures8FollowUpC17hasEngagedWithCFUSbvgZ
- _$s25CloudSubscriptionFeatures8FollowUpC19IneligibilityReasonO17hadPreviousAccessyA2EmFWC
- _$s25CloudSubscriptionFeatures8FollowUpC19IneligibilityReasonO8rawValueSSvg
- _$s25CloudSubscriptionFeatures8FollowUpC19IneligibilityReasonOMa
- _$s25CloudSubscriptionFeatures8FollowUpC19IneligibilityReasonOMn
- _$s25CloudSubscriptionFeatures8FollowUpC19IneligibilityReasonOSHAAMc
- _$s25CloudSubscriptionFeatures8FollowUpC19IneligibilityReasonOSQAAMc
- _$s25CloudSubscriptionFeatures8FollowUpC20ineligibilityReasons10oldFeature03newI0ShyAC19IneligibilityReasonOGAA0aI0CSg_ALtYaFTjTu
- _$sSH13_rawHashValue4seedS2i_tFTj
- _$sSQ2eeoiySbx_xtFZTj
- _$sSa11descriptionSSvg
- _$ss11_SetStorageC8allocate8capacityAByxGSi_tFZ
- _$ss11_SetStorageCMn
- _$ss5NeverOMn
- ___stack_chk_fail
- ___stack_chk_guard
- __swiftEmptySetSingleton
- _bzero
- _objc_release_x22
- _swift_continuation_resume
- _swift_deallocClassInstance
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
- _swift_retain
- _swift_slowDealloc
- _swift_stdlib_isStackAllocationSafe
CStrings:
- "<Skipping asset check, pass --full to include asset status>"
- "Are assets finished downloading? "
- "Determining user asset eligibility."
- "Device should release assets with reason: "
- "Device should start asset download."
- "Enough device storage to download? "
- "Has user engaged with the CFU? "
- "ModelCatalog Integration"
- "Note: CFU showing will be contingent on whether the device previously had access."
- "Unable to initialize followup object."
- "User is fully eligible to see CFU."
- "User is ineligible with CFU with reasons: "
- "assetStatusWithCompletionHandler:"
- "v16@?0B8B12"

```
