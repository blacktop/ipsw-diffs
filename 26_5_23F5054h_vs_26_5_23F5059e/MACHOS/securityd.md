## securityd

> `/usr/libexec/securityd`

```diff

-61901.120.56.0.1
-  __TEXT.__text: 0x27fd5c
-  __TEXT.__auth_stubs: 0x4200
-  __TEXT.__objc_stubs: 0x1d020
-  __TEXT.__objc_methlist: 0x158a0
-  __TEXT.__const: 0x921
-  __TEXT.__cstring: 0x216e8
-  __TEXT.__objc_methname: 0x2d1f2
-  __TEXT.__oslogstring: 0x2ed9f
+61901.120.60.0.0
+  __TEXT.__text: 0x280b58
+  __TEXT.__auth_stubs: 0x4210
+  __TEXT.__objc_stubs: 0x1d060
+  __TEXT.__objc_methlist: 0x158c0
+  __TEXT.__const: 0x919
+  __TEXT.__cstring: 0x21755
+  __TEXT.__objc_methname: 0x2d298
+  __TEXT.__oslogstring: 0x2ee52
   __TEXT.__swift5_typeref: 0x378
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__objc_classname: 0x25a3
-  __TEXT.__objc_methtype: 0xa8f2
+  __TEXT.__objc_methtype: 0xa947
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_reflstr: 0xc3
   __TEXT.__swift5_capture: 0x1bc

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__gcc_except_tab: 0xb5b0
+  __TEXT.__gcc_except_tab: 0xb5d4
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6f08
+  __TEXT.__unwind_info: 0x6f18
   __TEXT.__eh_frame: 0xa58
-  __DATA_CONST.__auth_got: 0x2110
-  __DATA_CONST.__got: 0x1390
+  __DATA_CONST.__auth_got: 0x2118
+  __DATA_CONST.__got: 0x13b0
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x14580
+  __DATA_CONST.__const: 0x145a8
   __DATA_CONST.__cfstring: 0x1bd40
   __DATA_CONST.__objc_classlist: 0x8f0
   __DATA_CONST.__objc_catlist: 0x68

   __DATA_CONST.__objc_arraydata: 0x400
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x232f8
-  __DATA.__objc_selrefs: 0x95a0
+  __DATA.__objc_const: 0x23300
+  __DATA.__objc_selrefs: 0x95b8
   __DATA.__objc_ivar: 0x1a64
   __DATA.__objc_data: 0x5c58
   __DATA.__data: 0x3098

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B57FF54C-4048-3A19-87D1-A780F5C66213
-  Functions: 9790
-  Symbols:   1858
-  CStrings:  19995
+  UUID: 5139DA5C-5CDB-3A41-9371-47C508E099D3
+  Functions: 9798
+  Symbols:   1863
+  CStrings:  20005
 
Symbols:
+ _CFStringCreateWithBytesNoCopy
+ _kCFAllocatorMalloc
+ _kSecurityRTCEventNameEscrowRepairGenerateRecordPasscodeChanged
+ _kSecurityRTCEventNameEscrowRepairGenerateRecordPasscodeUnlocked
+ _kSecurityRTCFieldSEPBasedEscrowRepairRateLimitDaysLeft
+ _kSecurityRTCFieldSEPBasedEscrowRepairState
- _kSecurityRTCEventNameEscrowRepairGenerateRecord
CStrings:
+ "-[CuttlefishXPCWrapper fetchEgoBottleIDWithSpecificUser:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:daysLeftOnRateLimit:rateLimitState:reply:]_block_invoke"
+ "0123456789ABCDEF"
+ "B40@0:8@\"<OTSecureBackupEnablerProtocol>\"16@\"OTSerializedPlistEscrowRecord\"24^@32"
+ "B56@0:8q16@24@32@40^@48"
+ "effectiveRateLimitState:passcodeGeneration:intendedBottleID:computedDaysLeftOnRateLimit:error:"
+ "failed to create cached escrow record: %@"
+ "failed to determine intended bottleID"
+ "fetchEgoBottleID:"
+ "fetchEgoBottleIDWithSpecificUser:reply:"
+ "fetched ego bottle ID: %@"
+ "generateCachedEscrowRecordForReason:passcodeGeneration:dependencies:cuttlefishXPCWrapper:error:"
+ "not rate limited (state: %ld)"
+ "octagon-escrowcheck: failed to fetch bottle ID: %@"
+ "octagon: error fetching ego bottle ID: %@"
+ "q56@0:8@16@24@32^q40^@48"
+ "requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:daysLeftOnRateLimit:rateLimitState:reply:"
+ "unable to determine rate limit state: %@"
+ "v32@0:8@\"<OTSecureBackupEnablerProtocol>\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v88@0:8@\"TPSpecificUser\"16B24Q28@\"NSArray\"36B44@\"NSString\"48@\"NSString\"56q64q72@?<v@?@\"OTEscrowCheckCallResult\"@\"NSError\">80"
+ "v88@0:8@16B24Q28@36B44@48@56q64q72@?80"
- "-[CuttlefishXPCWrapper requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:daysLeftOnRateLimit:reply:]_block_invoke"
- "B40@0:8@16@\"OTSerializedPlistEscrowRecord\"24^@32"
- "B48@0:8q16@24@32^@40"
- "checkEscrowRepairRateLimit:error:"
- "failed to validate/create cached escrow record: %@"
- "q32@0:8@16^@24"
- "rate limit ignored due to version check"
- "requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:daysLeftOnRateLimit:reply:"
- "v32@0:8@16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v80@0:8@\"TPSpecificUser\"16B24Q28@\"NSArray\"36B44@\"NSString\"48@\"NSString\"56q64@?<v@?@\"OTEscrowCheckCallResult\"@\"NSError\">72"
- "v80@0:8@16B24Q28@36B44@48@56q64@?72"
- "validateOrCreateStoredEscrowRecordForReason:usingDependencies:cuttlefishXPCWrapper:error:"

```
