## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1007.100.5.0.0
-  __TEXT.__text: 0x288a58
-  __TEXT.__auth_stubs: 0x24c0
+1007.100.8.1.0
+  __TEXT.__text: 0x28ff50
+  __TEXT.__auth_stubs: 0x2500
   __TEXT.__objc_methlist: 0x614
-  __TEXT.__objc_methname: 0x400b
+  __TEXT.__objc_methname: 0x40bb
   __TEXT.__objc_classname: 0x20e
   __TEXT.__objc_methtype: 0x1429
-  __TEXT.__cstring: 0x7ea4
-  __TEXT.__swift5_typeref: 0x5e2b
+  __TEXT.__cstring: 0x8244
+  __TEXT.__swift5_typeref: 0x5efd
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xc140
-  __TEXT.__constg_swiftt: 0x9994
-  __TEXT.__swift5_reflstr: 0x4fa4
-  __TEXT.__swift5_fieldmd: 0x5068
-  __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_assocty: 0x620
-  __TEXT.__swift5_proto: 0x99c
-  __TEXT.__swift5_types: 0x4bc
-  __TEXT.__oslogstring: 0x161b6
-  __TEXT.__swift5_protos: 0x1cc
-  __TEXT.__swift5_capture: 0x5560
+  __TEXT.__const: 0xc440
+  __TEXT.__constg_swiftt: 0x9c48
+  __TEXT.__swift5_reflstr: 0x5164
+  __TEXT.__swift5_fieldmd: 0x517c
+  __TEXT.__swift5_builtin: 0x1b8
+  __TEXT.__swift5_assocty: 0x680
+  __TEXT.__swift5_proto: 0x9bc
+  __TEXT.__swift5_types: 0x4d0
+  __TEXT.__oslogstring: 0x16646
+  __TEXT.__swift5_protos: 0x1d0
+  __TEXT.__swift5_capture: 0x55c4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x51a0
-  __TEXT.__eh_frame: 0x5138
-  __DATA_CONST.__auth_got: 0x1260
-  __DATA_CONST.__got: 0xbb8
-  __DATA_CONST.__auth_ptr: 0x1e70
-  __DATA_CONST.__const: 0x10850
-  __DATA_CONST.__objc_classlist: 0x4e0
+  __TEXT.__unwind_info: 0x5308
+  __TEXT.__eh_frame: 0x54f8
+  __DATA_CONST.__auth_got: 0x1280
+  __DATA_CONST.__got: 0xc00
+  __DATA_CONST.__auth_ptr: 0x1a58
+  __DATA_CONST.__const: 0x10a40
+  __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x13a40
-  __DATA.__objc_selrefs: 0x1178
+  __DATA.__objc_const: 0x13cb8
+  __DATA.__objc_selrefs: 0x11b0
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x26e0
-  __DATA.__data: 0xf5e0
+  __DATA.__objc_data: 0x2730
+  __DATA.__data: 0xfa50
   __DATA.__objc_stublist: 0x68
-  __DATA.__bss: 0xeb80
+  __DATA.__bss: 0xee80
   __DATA.__common: 0x3d8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7638
-  Symbols:   1129
-  CStrings:  3201
+  Functions: 7730
+  Symbols:   1143
+  CStrings:  3250
 
Symbols:
+ _$ss23withCheckedContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5NeverOGXEtYalF
+ _$ss23withCheckedContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5NeverOGXEtYalFTu
+ _$ss27_bridgeAnythingToObjectiveCyyXlxlF
+ _$ss5NeverOMn
+ _kAAAnalyticsEDPPasswordVersionDoesMatch
+ _kAAAnalyticsEdpHealth
+ _kAAAnalyticsEdpPrimaryRecordHealth
+ _kAAAnalyticsEdpRecoveryRecordHealth
+ _kAAAnalyticsEdpRemainingPrimaryRecordAttempts
+ _kAAAnalyticsEdpRemainingRecoveryRecordAttempts
+ _kPCSGuitarfishTelemetryFlags
+ _kPCSGuitarfishTelemetryRecordPasswordVersion
+ _objc_retain_x5
+ _swift_continuation_resume
CStrings:
+ "%!s(MISSING) - EDP HealthCheck started."
+ "%!s(MISSING) - EDP Recovery Token Upload was attempted %!l(MISSING)d times. Will not attempt again."
+ "%!s(MISSING) - EDP Recovery Token was already uploaded to IdMS. Will not upload again."
+ "%!s(MISSING) - EDP Recovery Token was created by another device. Will not upload from this device."
+ "%!s(MISSING) - EDP health state is reported as error"
+ "%!s(MISSING) - EDP health state is reported as good"
+ "%!s(MISSING) - EDP needs full repair, posting CDP+EDP repair CFU."
+ "%!s(MISSING) - EDP only repair, posting just EDP repair CFU."
+ "%!s(MISSING) - EDP was never enabled on this account."
+ "%!s(MISSING) - Failed to obtain EDP health state: %!s(MISSING)"
+ "%!s(MISSING) - Failed to post CDP+EDP repair CFU: %!s(MISSING)"
+ "%!s(MISSING) - Failed to post EDP only repair CFU: %!s(MISSING)"
+ "%!s(MISSING) - Failed to tear down EDP repair only CFU: %!s(MISSING)"
+ "%!s(MISSING) - received a unused state, this will be removed in future."
+ "%!s(MISSING) - trying to tear down existing EDP repair only CFUs."
+ "Invalid EDP Health State!"
+ "Missing cdpContext"
+ "Missing cdpStateController"
+ "Missing context, reporting EDPState.error"
+ "Missing primary context, returning EDP enabled as false"
+ "Posting a single consolidated FYI notification."
+ "Random key could not be generated. Error - %!@(MISSING)"
+ "TEMP_ICLOUD_DATA_ACCESS_ALL"
+ "_TtC13appleaccountd24EDPAndADPCheckingFactory"
+ "_TtC13appleaccountd39EnhancedAndAdvancedDataProtectionChecks"
+ "_TtC13appleaccountd43EnhancedAndAdvancedDataProtectionChecksMock"
+ "_edpAdpHealthChecks"
+ "appleaccountd/AdvancedAndEnhancedDataProtectionChecks.swift"
+ "cdpRequestController"
+ "contextForCDPEDPStateRepair"
+ "contextForEDPStateRepair"
+ "edpAttemptsRemainingPrimary"
+ "edpAttemptsRemainingRecovery"
+ "edpHealthPrimary"
+ "edpHealthRecovery"
+ "edpRecoveryTokenUploadRetryAttempts"
+ "edpState"
+ "initWithBool:"
+ "initWithContext:"
+ "localPasswordVersion"
+ "performCDPHealthCheck(telemetryFlowID:primaryAccount:)"
+ "performCDPHealthCheckCalled"
+ "performCDPHealthCheckStubbedError"
+ "performEDPHealthCheck(telemetryFlowID:primaryAccount:)"
+ "performEDPHealthCheckCalled"
+ "performEDPHealthCheckStubbedError"
+ "primaryRecordAttemptsRemaining"
+ "recoveryTokenRecordAttemptsRemaining"
+ "uploadEDPRecoveryTokenWithCompletion:"
+ "v32@?0q8@\"NSDictionary\"16@\"NSError\"24"
+ "validateEDPIdentitiesWithContext:completion:"
- "Random key could not be generated. Error - "
- "appleaccountd/DataCryptor.swift"

```
