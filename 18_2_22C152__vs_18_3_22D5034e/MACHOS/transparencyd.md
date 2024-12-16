## transparencyd

> `/usr/libexec/transparencyd`

```diff

-1218.60.67.0.0
-  __TEXT.__text: 0x213dcc
-  __TEXT.__auth_stubs: 0x2df0
-  __TEXT.__objc_stubs: 0x1b380
-  __TEXT.__objc_methlist: 0x125fc
-  __TEXT.__cstring: 0x11120
-  __TEXT.__objc_classname: 0x2bb9
-  __TEXT.__objc_methname: 0x21535
-  __TEXT.__objc_methtype: 0x6fca
-  __TEXT.__const: 0x5fb8
+1218.80.17.0.0
+  __TEXT.__text: 0x2161d4
+  __TEXT.__auth_stubs: 0x2e30
+  __TEXT.__objc_stubs: 0x1b460
+  __TEXT.__objc_methlist: 0x1267c
+  __TEXT.__cstring: 0x113e7
+  __TEXT.__objc_classname: 0x2bda
+  __TEXT.__objc_methname: 0x216bc
+  __TEXT.__objc_methtype: 0x6fec
+  __TEXT.__const: 0x5fe8
   __TEXT.__gcc_except_tab: 0x4b44
-  __TEXT.__oslogstring: 0x10af2
-  __TEXT.__swift5_typeref: 0x19c0
-  __TEXT.__swift5_reflstr: 0xeda
+  __TEXT.__oslogstring: 0x109d8
+  __TEXT.__swift5_typeref: 0x1a00
+  __TEXT.__swift5_reflstr: 0xf2a
   __TEXT.__swift5_assocty: 0x2d0
-  __TEXT.__constg_swiftt: 0x223c
-  __TEXT.__swift5_fieldmd: 0x160c
+  __TEXT.__constg_swiftt: 0x2254
+  __TEXT.__swift5_fieldmd: 0x1624
   __TEXT.__swift5_proto: 0x410
   __TEXT.__swift5_types: 0x1a4
-  __TEXT.__swift5_capture: 0xd78
+  __TEXT.__swift5_capture: 0xdec
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x8338
-  __TEXT.__eh_frame: 0x3438
-  __DATA_CONST.__auth_got: 0x1708
-  __DATA_CONST.__got: 0xe28
-  __DATA_CONST.__auth_ptr: 0x548
-  __DATA_CONST.__const: 0x14088
-  __DATA_CONST.__cfstring: 0xd8c0
-  __DATA_CONST.__objc_classlist: 0xc50
+  __TEXT.__unwind_info: 0x8410
+  __TEXT.__eh_frame: 0x35c8
+  __DATA_CONST.__auth_got: 0x1728
+  __DATA_CONST.__got: 0xe30
+  __DATA_CONST.__auth_ptr: 0x538
+  __DATA_CONST.__const: 0x141e8
+  __DATA_CONST.__cfstring: 0xda00
+  __DATA_CONST.__objc_classlist: 0xc58
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x390
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x1b0
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_arrayobj: 0x1e0
-  __DATA.__objc_const: 0x302a0
-  __DATA.__objc_selrefs: 0x7f20
-  __DATA.__objc_ivar: 0x1068
-  __DATA.__objc_data: 0x8ef0
-  __DATA.__data: 0x84b8
+  __DATA.__objc_const: 0x304a0
+  __DATA.__objc_selrefs: 0x7f80
+  __DATA.__objc_ivar: 0x1070
+  __DATA.__objc_data: 0x8f68
+  __DATA.__data: 0x8510
   __DATA.__thread_vars: 0x48
   __DATA.__thread_bss: 0xc
-  __DATA.__bss: 0x8e38
-  __DATA.__common: 0x3e0
+  __DATA.__bss: 0x8e48
+  __DATA.__common: 0x3e8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12199
-  Symbols:   1351
-  CStrings:  11221
+  Functions: 12245
+  Symbols:   1356
+  CStrings:  11250
 
Symbols:
+ _$s10Foundation4DateV8advanced2byACSd_tF
+ _$sSd10FoundationE19_bridgeToObjectiveCSo8NSNumberCyF
+ _$ss6HasherV5_hash4seed_S2i_s6UInt64VtFZ
+ _OBJC_CLASS_$_NSNumberFormatter
+ _swift_projectBox
CStrings:
+ "\"\x15\x12"
+ "/\x0f\x0f\n"
+ "@\"NSNumber\"16@0:8"
+ "An IDS server bag update happened but 'KTEligibilityServerReporting' feature flag is not enabled"
+ "Config bag key value pair invalid format"
+ "Config bag value missing brackets"
+ "Config bag value missing colon"
+ "Error parsing eligibility config bag value %{public}@"
+ "Found failures, returning aggregate result of false"
+ "IDS version is not present in the config values"
+ "Most recent sample is missing, returning aggregate result of false"
+ "SELECT\n   element,\n   success,\n   eligibilityDate,\n   errorString,\n   errorCode\nFROM Eligibility\nWHERE element = ?\nAND eligibilityDate > ?\nORDER BY eligibilityDate ASC"
+ "SELECT\n   element,\n   success,\n   eligibilityDate,\n   errorString,\n   errorCode\nFROM Eligibility\nWHERE element = ?\nORDER BY eligibilityDate DESC"
+ "Server says don't report"
+ "Td,VoctagonEligibilityTimeout"
+ "TransparencyIDSConfigBagSupport"
+ "ckv-reliability-present-rate"
+ "ckv-reliability-report-interval"
+ "ckv-reliability-sample-interval"
+ "ckv-reliability-sample-number"
+ "componentsSeparatedByString:"
+ "containsString:"
+ "elgDays"
+ "eligibility"
+ "eligibilityPresentRate"
+ "eligibilityReportInterval"
+ "eligibilitySampleInterval"
+ "eligibilitySampleNumber"
+ "getCachedOctagonStatus:"
+ "getContinuousDaysOfSuccessWithElement:completionHandler:"
+ "initWithPath:idsReporting:eligibilitySupport:configBag:error:"
+ "numberFromString:"
+ "octagonEligibilityTimeout"
+ "parseConfigInput:forVersion:error:"
+ "presentRate"
+ "recOverride"
+ "reportResultWithSuccess:startFrom:interval:completionHandler:"
+ "requiredSuccessfulDays"
+ "setNumberStyle:"
+ "setOctagonEligibilityTimeout:"
+ "timeBetweenReportsDays"
+ "triggerCheckCKKSOctagonEligibilityWithCompletion:"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v48@0:8@\"NSNumber\"16d24@\"NSNumber\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@16d24@32@?40"
+ "value is not a number"
+ "{"
+ "\xa1"
- "'\x12"
- "/\x0f\x0f\t"
- "An IDS server bag update happened but 'KTEnableKillSwitch' feature flag is not enabled"
- "At least one missing element. Returning aggregate result of false"
- "Eligible30"
- "Eligible60"
- "Ignoring result for element %s and result %s since there is an existing sample"
- "No elements or elements have failures. Returning aggregate result of false"
- "No entries for given element %{public}s. Returning aggregate result of false"
- "No success in the last sample for element %{public}s. Returning aggregate result of false"
- "SELECT\n   element,\n   success,\n   eligibilityDate,\n   errorString,\n   errorCode\nFROM Eligibility\nWHERE element LIKE ?\nAND eligibilityDate > ?\nORDER BY eligibilityDate ASC"
- "Storing element %s with result %s since no previous result was found"
- "getCachedOctagonStatus"
- "initWithPath:idsReporting:eligibilitySupport:error:"
- "rec"
- "reportResultWithSuccess:startFrom:completionHandler:"
- "triggerCheckCKKSOctagonEligibility"
- "v40@0:8@\"NSNumber\"16d24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@16d24@?32"
- "\x91"

```
