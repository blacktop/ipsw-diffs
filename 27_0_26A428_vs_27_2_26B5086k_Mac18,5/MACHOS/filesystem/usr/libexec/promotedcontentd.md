## promotedcontentd

> `/usr/libexec/promotedcontentd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`

```diff

-557.1.32.0.0
-  __TEXT.__text: 0x33e7b0
-  __TEXT.__auth_stubs: 0x5830
-  __TEXT.__objc_stubs: 0x19980
+557.2.8.0.0
+  __TEXT.__text: 0x3418dc
+  __TEXT.__auth_stubs: 0x5900
+  __TEXT.__objc_stubs: 0x199c0
   __TEXT.__objc_methlist: 0x151e0
-  __TEXT.__const: 0x7437a
+  __TEXT.__const: 0x7465a
   __TEXT.__gcc_except_tab: 0x12a0
-  __TEXT.__cstring: 0x15615
-  __TEXT.__objc_methname: 0x26d4d
-  __TEXT.__oslogstring: 0x1065c
-  __TEXT.__objc_classname: 0x4ba7
-  __TEXT.__objc_methtype: 0x514d
-  __TEXT.__constg_swiftt: 0x6184
-  __TEXT.__swift5_typeref: 0x41ae
-  __TEXT.__swift5_reflstr: 0x3636
-  __TEXT.__swift5_fieldmd: 0x4778
+  __TEXT.__cstring: 0x15715
+  __TEXT.__objc_methname: 0x26e4d
+  __TEXT.__oslogstring: 0x1080c
+  __TEXT.__objc_classname: 0x4d27
+  __TEXT.__objc_methtype: 0x519d
+  __TEXT.__constg_swiftt: 0x6320
+  __TEXT.__swift5_typeref: 0x4246
+  __TEXT.__swift5_reflstr: 0x3796
+  __TEXT.__swift5_fieldmd: 0x4920
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x3a8
-  __TEXT.__swift5_proto: 0x7d8
-  __TEXT.__swift5_types: 0x594
-  __TEXT.__swift5_capture: 0xfa8
-  __TEXT.__swift5_protos: 0x124
+  __TEXT.__swift5_proto: 0x7f8
+  __TEXT.__swift5_types: 0x5ac
+  __TEXT.__swift5_capture: 0xfc8
+  __TEXT.__swift5_protos: 0x128
   __TEXT.__swift_as_entry: 0xd0
   __TEXT.__swift_as_ret: 0xf8
   __TEXT.__swift_as_cont: 0x244
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x82d8
+  __TEXT.__unwind_info: 0x8398
   __TEXT.__eh_frame: 0x45f4
-  __DATA_CONST.__const: 0x163c8
+  __DATA_CONST.__const: 0x16578
   __DATA_CONST.__cfstring: 0xf340
-  __DATA_CONST.__objc_classlist: 0xfe8
+  __DATA_CONST.__objc_classlist: 0x1010
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0xa50
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x2c28
-  __DATA_CONST.__got: 0x1830
-  __DATA_CONST.__auth_ptr: 0x1538
-  __DATA.__objc_const: 0x2b308
-  __DATA.__objc_selrefs: 0x9378
+  __DATA_CONST.__auth_got: 0x2c90
+  __DATA_CONST.__got: 0x1860
+  __DATA_CONST.__auth_ptr: 0x1560
+  __DATA.__objc_const: 0x2b6c0
+  __DATA.__objc_selrefs: 0x9388
   __DATA.__objc_ivar: 0x1458
-  __DATA.__objc_data: 0x97b8
-  __DATA.__data: 0xd8e8
+  __DATA.__objc_data: 0x9878
+  __DATA.__data: 0xdd78
   __DATA.__common: 0xc30
   - /AppleInternal/Library/Frameworks/TestHookService.framework/Versions/A/TestHookService
   - /AppleInternal/Library/Frameworks/TestHookShared.framework/Versions/A/TestHookShared

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11373
-  Symbols:   2193
-  CStrings:  11508
+  Functions: 11426
+  Symbols:   2195
+  CStrings:  11534
 
Symbols:
+ _APSimulateCrashNoKillProcessWithoutABCReport
+ _AnalyticsSendEventLazy
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Database config saved to UserDefaults. busyTimeout: %ld, coreAnalyticsThresholdMs: %ld"
+ "Database config saved to UserDefaults. busyTimeout: %ld, coreAnalyticsThresholdMs: %ld, slowQueryThresholdMs: %ld"
+ "Database.CoreAnalyticsThresholdMs"
+ "Database.SlowQueryThresholdMs"
+ "Depositing age noising application diagnostic sample %s"
+ "Error: Config download failed"
+ "Error: Config extraction failed"
+ "Triaging age noising application diagnostics for actual birth year: %{sensitive}s, noised birth year: %{sensitive}s, eligibility: %s"
+ "[SLPFlagCheck] Captured incrementalityAppStoreSLP=%{public}d at request time"
+ "_TtC16promotedcontentd20DatabaseConfigSyncer"
+ "_TtC16promotedcontentd39TracingAgeNoisingApplicationDiagnostics"
+ "_TtC16promotedcontentd40NullAgeNoisingApplicationDiagnosticDepot"
+ "_TtC16promotedcontentd42DepositingAgeNoisingApplicationDiagnostics"
+ "_TtC16promotedcontentd43TracingAgeNoisingApplicationDiagnosticDepot"
+ "_TtC16promotedcontentd49CoreAnalyticsAgeNoisingApplicationDiagnosticDepot"
+ "_TtC16promotedcontentd51PredeterminedAgeNoisingQualifierConfigurationSource"
+ "accountInfo"
+ "actualBirthYearAvailable"
+ "ageNoisingApplicationDiagnosticDepot"
+ "ageNoisingConfiguration"
+ "com.apple.adplatforms.agenoising.application"
+ "depot"
+ "incrementalityAppStoreSLPEnabled"
+ "isInternalBuild"
+ "noisedBirthYearAvailable"
+ "promotedcontentd.DatabaseConfigSyncer"
+ "randomGenerator"
+ "setFlagEnabledAtRequest:"
+ "tracedDepot"
+ "tracedDiagnostics"
- "Database busy timeout saved to UserDefaults: %ld"
- "_TtC16promotedcontentd25DatabaseBusyTimeoutSyncer"
- "_TtC16promotedcontentd45DefaultAgeNoisingQualifierConfigurationSource"
- "promotedcontentd.DatabaseBusyTimeoutSyncer"
- "storefrontIDSource"
```
