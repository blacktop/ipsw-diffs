## transparencyd

> `/usr/libexec/transparencyd`

```diff

-1218.60.60.502.1
-  __TEXT.__text: 0x2110e0
-  __TEXT.__auth_stubs: 0x2da0
-  __TEXT.__objc_stubs: 0x1b1c0
-  __TEXT.__objc_methlist: 0x1252c
-  __TEXT.__cstring: 0x10f70
+1218.60.64.0.0
+  __TEXT.__text: 0x2133cc
+  __TEXT.__auth_stubs: 0x2df0
+  __TEXT.__objc_stubs: 0x1b360
+  __TEXT.__objc_methlist: 0x125fc
+  __TEXT.__cstring: 0x11030
   __TEXT.__objc_classname: 0x2bb9
-  __TEXT.__objc_methname: 0x21472
-  __TEXT.__objc_methtype: 0x701b
-  __TEXT.__const: 0x5fa8
+  __TEXT.__objc_methname: 0x21535
+  __TEXT.__objc_methtype: 0x6fd6
+  __TEXT.__const: 0x5fb8
   __TEXT.__gcc_except_tab: 0x4b04
-  __TEXT.__oslogstring: 0x10a02
-  __TEXT.__swift5_typeref: 0x19b6
+  __TEXT.__oslogstring: 0x10a82
+  __TEXT.__swift5_typeref: 0x19c0
   __TEXT.__swift5_reflstr: 0xeda
   __TEXT.__swift5_assocty: 0x2d0
-  __TEXT.__constg_swiftt: 0x21ec
-  __TEXT.__swift5_fieldmd: 0x15f4
+  __TEXT.__constg_swiftt: 0x2230
+  __TEXT.__swift5_fieldmd: 0x1600
   __TEXT.__swift5_proto: 0x410
   __TEXT.__swift5_types: 0x1a4
-  __TEXT.__swift5_capture: 0xd38
+  __TEXT.__swift5_capture: 0xd74
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x8290
-  __TEXT.__eh_frame: 0x3360
-  __DATA_CONST.__auth_got: 0x16e0
-  __DATA_CONST.__got: 0xe10
+  __TEXT.__unwind_info: 0x8328
+  __TEXT.__eh_frame: 0x3438
+  __DATA_CONST.__auth_got: 0x1708
+  __DATA_CONST.__got: 0xe20
   __DATA_CONST.__auth_ptr: 0x538
-  __DATA_CONST.__const: 0x13f68
-  __DATA_CONST.__cfstring: 0xd7e0
+  __DATA_CONST.__const: 0x14060
+  __DATA_CONST.__cfstring: 0xd820
   __DATA_CONST.__objc_classlist: 0xc50
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x390

   __DATA_CONST.__objc_arraydata: 0x1b0
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_arrayobj: 0x1e0
-  __DATA.__objc_const: 0x30218
-  __DATA.__objc_selrefs: 0x7ed8
-  __DATA.__objc_ivar: 0x1060
-  __DATA.__objc_data: 0x8e10
-  __DATA.__data: 0x8488
+  __DATA.__objc_const: 0x302c8
+  __DATA.__objc_selrefs: 0x7f20
+  __DATA.__objc_ivar: 0x1068
+  __DATA.__objc_data: 0x8ea0
+  __DATA.__data: 0x84b8
   __DATA.__thread_vars: 0x48
   __DATA.__thread_bss: 0xc
-  __DATA.__bss: 0x8e18
-  __DATA.__common: 0x3d0
+  __DATA.__bss: 0x8e28
+  __DATA.__common: 0x3d8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12137
-  Symbols:   1343
-  CStrings:  11193
+  Functions: 12192
+  Symbols:   1350
+  CStrings:  11213
 
Symbols:
+ _$s10Foundation13__DataStorageC5bytes6lengthACSVSg_Sitcfc
+ _$s10Foundation13__DataStorageCMa
+ _$s10Foundation3URLV13DirectoryHintO02isC0yA2EmFWC
+ _$s10Foundation4DataV14RangeReferenceCMa
+ _$s10Foundation4DataV19base64EncodedString7optionsSSSo27NSDataBase64EncodingOptionsV_tF
+ _$sSayxG10Foundation15ContiguousBytesABs5UInt8VRszlMc
+ _swift_stdlib_random
CStrings:
+ "\x0f\x05\x1f"
+ "/\x0f\x0f\t"
+ "@\"<EligibilitySupportProtocol>\""
+ "@\"<IDSReportingProtocol>\""
+ "@\"_TtC13transparencyd28KTEligibilityStatusReporting\""
+ "Did not store eligiblity result, status reporting object is nil"
+ "Error initializing eligibility status reporter %!@(MISSING)"
+ "State Machine not initialized yet, can't run eligibility commands"
+ "T@\"<EligibilitySupportProtocol>\",&,V_eligibilitySupport"
+ "T@\"<IDSReportingProtocol>\",&,V_idsReporting"
+ "T@\"NSURL\",N,C"
+ "T@\"_TtC13transparencyd28KTEligibilityStatusReporting\",&,V_eligibilityStatusReporter"
+ "T@\"_TtC13transparencyd28KTEligibilityStatusReporting\",&,V_statusReporting"
+ "Timeout closing eligibility db"
+ "_eligibilitySupport"
+ "_idsReporting"
+ "closeDatabaseWithCompletionHandler:"
+ "databaseDir"
+ "eligibilitySupport"
+ "error closing eligibility db %!@(MISSING)"
+ "idsReporting"
+ "setDatabaseDir:"
+ "setEligibilitySupport:"
+ "setIdsReporting:"
+ "shouldSetInternalHeader"
+ "temporaryDirectory"
+ "v28@0:8B16@?<v@?@\"NSError\">20"
+ "v32@0:8@\"NSNumber\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8d16@?<v@?@\"NSError\">24"
- "\x0f\x05\x1e"
- "/\x0f\x0f\b"
- "@\"<KTEligibilityStatusReportingProtocol>\""
- "@\"<KTEligibilityStatusReportingProtocol><KTEligibilityStatusReportingProtocolTesting>\""
- "@\"<_TtP13transparencyd36KTEligibilityStatusReportingProtocol_>\""
- "Error opening eligibility database %!{(MISSING)public}@"
- "T@\"<KTEligibilityStatusReportingProtocol>\",&,V_eligibilityStatusReporter"
- "T@\"<KTEligibilityStatusReportingProtocol><KTEligibilityStatusReportingProtocolTesting>\",&,V_statusReporting"
- "T@\"<_TtP13transparencyd36KTEligibilityStatusReportingProtocol_>\",&,V_eligibilityStatusReporter"
- "transparencydEligibilityMultiSampler"
- "v32@0:8@\"NSNumber\"16@?<v@?B>24"

```
