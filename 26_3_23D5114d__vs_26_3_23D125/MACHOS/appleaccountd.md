## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1037.325.2.0.0
-  __TEXT.__text: 0x3209b4
-  __TEXT.__auth_stubs: 0x2960
+1037.325.3.0.0
+  __TEXT.__text: 0x325070
+  __TEXT.__auth_stubs: 0x2970
   __TEXT.__objc_methlist: 0xedc
-  __TEXT.__objc_methname: 0x4a1c
+  __TEXT.__objc_methname: 0x4aae
   __TEXT.__objc_classname: 0x23c
   __TEXT.__objc_methtype: 0x1675
-  __TEXT.__cstring: 0x9273
-  __TEXT.__swift5_typeref: 0x6990
-  __TEXT.__const: 0x101a0
+  __TEXT.__cstring: 0x9423
+  __TEXT.__swift5_typeref: 0x6a0c
+  __TEXT.__const: 0x10440
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xb788
-  __TEXT.__swift5_reflstr: 0x5d92
-  __TEXT.__swift5_fieldmd: 0x5b6c
-  __TEXT.__swift5_builtin: 0x244
-  __TEXT.__swift5_assocty: 0x770
-  __TEXT.__swift5_proto: 0xac4
-  __TEXT.__swift5_types: 0x570
-  __TEXT.__swift5_capture: 0x5c90
-  __TEXT.__oslogstring: 0x1ca29
-  __TEXT.__swift_as_entry: 0x420
-  __TEXT.__swift_as_ret: 0x58c
+  __TEXT.__constg_swiftt: 0xb84c
+  __TEXT.__swift5_reflstr: 0x5e92
+  __TEXT.__swift5_fieldmd: 0x5bec
+  __TEXT.__swift5_builtin: 0x26c
+  __TEXT.__swift5_assocty: 0x7d0
+  __TEXT.__swift5_proto: 0xad8
+  __TEXT.__swift5_types: 0x57c
+  __TEXT.__swift5_capture: 0x5cc0
+  __TEXT.__oslogstring: 0x1cd59
+  __TEXT.__swift_as_entry: 0x430
+  __TEXT.__swift_as_ret: 0x59c
   __TEXT.__swift5_protos: 0x208
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x7138
-  __TEXT.__eh_frame: 0xe64c
-  __DATA_CONST.__auth_got: 0x14b0
-  __DATA_CONST.__got: 0xfb0
-  __DATA_CONST.__auth_ptr: 0x11d8
-  __DATA_CONST.__const: 0x12328
+  __TEXT.__unwind_info: 0x71f8
+  __TEXT.__eh_frame: 0xe824
+  __DATA_CONST.__auth_got: 0x14b8
+  __DATA_CONST.__got: 0xff8
+  __DATA_CONST.__auth_ptr: 0x11e8
+  __DATA_CONST.__const: 0x124a0
   __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x1ba98
-  __DATA.__objc_selrefs: 0x1540
+  __DATA.__objc_const: 0x1bab8
+  __DATA.__objc_selrefs: 0x1570
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x3110
-  __DATA.__data: 0x12280
+  __DATA.__data: 0x12300
   __DATA.__objc_stublist: 0x68
-  __DATA.__bss: 0x10780
+  __DATA.__bss: 0x10a00
   __DATA.__common: 0x450
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7FF54EA3-62CC-370F-94BF-F4ECB3E8DA67
-  Functions: 8968
-  Symbols:   1352
-  CStrings:  3811
+  UUID: FD486D2E-F9F8-3490-94E3-AEA2EBACB5B3
+  Functions: 9018
+  Symbols:   1362
+  CStrings:  3843
 
Symbols:
+ _kAAAnalyticsPdpEligibility
+ _kAAAnalyticsPdpHealth
+ _kAAAnalyticsPdpPasswordVersionDoesMatch
+ _kAAAnalyticsPdpPrimaryRecordHealth
+ _kAAAnalyticsPdpRecoveryRecordHealth
+ _kAAAnalyticsPdpRemainingPrimaryRecordAttempts
+ _kAAAnalyticsPdpRemainingRecoveryRecordAttempts
+ _kPCSGuitarfishTelemetryFlags
+ _kPCSGuitarfishTelemetryRecordPasswordVersion
+ _swift_continuation_resume
CStrings:
+ "%s - Failed to obtain PDP health state: %s"
+ "%s - Failed to post CDP+PDP repair CFU: %s"
+ "%s - Failed to post PDP only repair CFU: %s"
+ "%s - Failed to tear down PDP repair only CFU: %s"
+ "%s - PDP HealthCheck started."
+ "%s - PDP health state is reported as error"
+ "%s - PDP health state is reported as good"
+ "%s - PDP needs full repair, posting CDP+PDP repair CFU."
+ "%s - PDP only repair, posting just PDP repair CFU."
+ "%s - received a unused state, this will be removed in future."
+ "%s - trying to tear down existing PDP repair only CFUs."
+ "Invalid PDP Health State!"
+ "Missing context, reporting PDPState.error"
+ "Missing primary context, returning PDP enabled as false"
+ "Uploading PCS keys for DBR account without FYI notification."
+ "Using Health Check interval - One Week"
+ "appleaccountd/PDPAndADPChecks.swift"
+ "contextForCDPPDPStateRepair"
+ "contextForPDPStateRepair"
+ "initWithBool:"
+ "localPasswordVersion"
+ "pdpAttemptsRemainingPrimary"
+ "pdpAttemptsRemainingRecovery"
+ "pdpHealthPrimary"
+ "pdpHealthRecovery"
+ "pdpState"
+ "pdpStateValueForAccount:"
+ "performPDPHealthCheck(telemetryFlowID:primaryAccount:)"
+ "primaryRecordAttemptsRemaining"
+ "recoveryTokenRecordAttemptsRemaining"
+ "v32@?0q8@\"NSDictionary\"16@\"NSError\"24"
+ "validatePDPIdentitiesWithContext:completion:"

```
