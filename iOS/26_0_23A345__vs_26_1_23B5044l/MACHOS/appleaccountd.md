## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1034.1.1.0.0
-  __TEXT.__text: 0x306670
-  __TEXT.__auth_stubs: 0x28d0
+1037.0.0.0.0
+  __TEXT.__text: 0x3025e8
+  __TEXT.__auth_stubs: 0x28c0
   __TEXT.__objc_methlist: 0xecc
-  __TEXT.__objc_methname: 0x4a08
+  __TEXT.__objc_methname: 0x498f
   __TEXT.__objc_classname: 0x23c
   __TEXT.__objc_methtype: 0x1675
-  __TEXT.__cstring: 0x9203
-  __TEXT.__swift5_typeref: 0x671c
+  __TEXT.__cstring: 0x8fe3
+  __TEXT.__swift5_typeref: 0x6690
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xe1a0
-  __TEXT.__constg_swiftt: 0xb500
-  __TEXT.__swift5_reflstr: 0x5952
-  __TEXT.__swift5_fieldmd: 0x5848
-  __TEXT.__swift5_builtin: 0x258
-  __TEXT.__swift5_assocty: 0x788
-  __TEXT.__swift5_proto: 0xa28
-  __TEXT.__swift5_types: 0x550
-  __TEXT.__swift5_capture: 0x5b88
-  __TEXT.__oslogstring: 0x1c2a9
-  __TEXT.__swift_as_entry: 0x3f8
-  __TEXT.__swift_as_ret: 0x538
+  __TEXT.__const: 0xdf20
+  __TEXT.__constg_swiftt: 0xb46c
+  __TEXT.__swift5_reflstr: 0x5892
+  __TEXT.__swift5_fieldmd: 0x57e0
+  __TEXT.__swift5_builtin: 0x230
+  __TEXT.__swift5_assocty: 0x728
+  __TEXT.__swift5_proto: 0xa14
+  __TEXT.__swift5_types: 0x544
+  __TEXT.__swift5_capture: 0x5b58
+  __TEXT.__oslogstring: 0x1bf89
+  __TEXT.__swift_as_entry: 0x3e8
+  __TEXT.__swift_as_ret: 0x528
   __TEXT.__swift5_protos: 0x1fc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6d20
-  __TEXT.__eh_frame: 0xd82c
-  __DATA_CONST.__auth_got: 0x1468
-  __DATA_CONST.__got: 0xfb8
-  __DATA_CONST.__auth_ptr: 0x1190
-  __DATA_CONST.__const: 0x11c90
+  __TEXT.__unwind_info: 0x6c88
+  __TEXT.__eh_frame: 0xd68c
+  __DATA_CONST.__auth_got: 0x1460
+  __DATA_CONST.__got: 0xf78
+  __DATA_CONST.__auth_ptr: 0x1180
+  __DATA_CONST.__const: 0x11b18
   __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x1b100
-  __DATA.__objc_selrefs: 0x1540
+  __DATA.__objc_const: 0x1b120
+  __DATA.__objc_selrefs: 0x1518
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x2f98
-  __DATA.__data: 0x11da0
+  __DATA.__data: 0x11d70
   __DATA.__objc_stublist: 0x68
-  __DATA.__bss: 0xf600
+  __DATA.__bss: 0xf380
   __DATA.__common: 0x430
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 81E17541-220A-3486-A551-B8E9072ECB1A
-  Functions: 8705
-  Symbols:   1344
-  CStrings:  3787
+  UUID: D1B29E39-2CB3-3210-A79F-3BCC6B4CC77A
+  Functions: 8658
+  Symbols:   1335
+  CStrings:  3755
 
Symbols:
- _kAAAnalyticsEDPPasswordVersionDoesMatch
- _kAAAnalyticsEdpHealth
- _kAAAnalyticsEdpPrimaryRecordHealth
- _kAAAnalyticsEdpRecoveryRecordHealth
- _kAAAnalyticsEdpRemainingPrimaryRecordAttempts
- _kAAAnalyticsEdpRemainingRecoveryRecordAttempts
- _kPCSGuitarfishTelemetryFlags
- _kPCSGuitarfishTelemetryRecordPasswordVersion
- _swift_continuation_resume
CStrings:
+ "%s - PDP was never enabled on this account."
+ "_TtC13appleaccountd15PDPAndADPChecks"
+ "_TtC13appleaccountd19PDPAndADPChecksMock"
+ "_TtC13appleaccountd24PDPAndADPCheckingFactory"
+ "_pdpAdpHealthChecks"
+ "performPDPHealthCheckCalled"
+ "performPDPHealthCheckStubbedError"
- "%s - EDP HealthCheck started."
- "%s - EDP health state is reported as error"
- "%s - EDP health state is reported as good"
- "%s - EDP needs full repair, posting CDP+EDP repair CFU."
- "%s - EDP only repair, posting just EDP repair CFU."
- "%s - EDP was never enabled on this account."
- "%s - Failed to obtain EDP health state: %s"
- "%s - Failed to post CDP+EDP repair CFU: %s"
- "%s - Failed to post EDP only repair CFU: %s"
- "%s - Failed to tear down EDP repair only CFU: %s"
- "%s - received a unused state, this will be removed in future."
- "%s - trying to tear down existing EDP repair only CFUs."
- "Invalid EDP Health State!"
- "Missing context, reporting EDPState.error"
- "Missing primary context, returning EDP enabled as false"
- "Posting a single consolidated FYI notification."
- "TEMP_ICLOUD_DATA_ACCESS_ALL"
- "Using Health Check interval - One Week"
- "_TtC13appleaccountd24EDPAndADPCheckingFactory"
- "_TtC13appleaccountd39EnhancedAndAdvancedDataProtectionChecks"
- "_TtC13appleaccountd43EnhancedAndAdvancedDataProtectionChecksMock"
- "_edpAdpHealthChecks"
- "appleaccountd/AdvancedAndEnhancedDataProtectionChecks.swift"
- "contextForCDPEDPStateRepair"
- "contextForEDPStateRepair"
- "edpAttemptsRemainingPrimary"
- "edpAttemptsRemainingRecovery"
- "edpHealthPrimary"
- "edpHealthRecovery"
- "edpState"
- "initWithBool:"
- "localPasswordVersion"
- "performEDPHealthCheck(telemetryFlowID:primaryAccount:)"
- "performEDPHealthCheckCalled"
- "performEDPHealthCheckStubbedError"
- "primaryRecordAttemptsRemaining"
- "recoveryTokenRecordAttemptsRemaining"
- "v32@?0q8@\"NSDictionary\"16@\"NSError\"24"
- "validateEDPIdentitiesWithContext:completion:"

```
