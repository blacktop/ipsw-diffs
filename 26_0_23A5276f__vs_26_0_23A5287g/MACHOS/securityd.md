## securityd

> `/usr/libexec/securityd`

```diff

-61901.0.33.0.2
-  __TEXT.__text: 0x259198
-  __TEXT.__auth_stubs: 0x4250
+61901.0.46.502.1
+  __TEXT.__text: 0x258c28
+  __TEXT.__auth_stubs: 0x4260
   __TEXT.__objc_stubs: 0x1c4e0
-  __TEXT.__objc_methlist: 0x152d0
-  __TEXT.__const: 0x869
-  __TEXT.__objc_methname: 0x2c238
-  __TEXT.__cstring: 0x20db9
-  __TEXT.__oslogstring: 0x2cc40
+  __TEXT.__objc_methlist: 0x15268
+  __TEXT.__const: 0x881
+  __TEXT.__objc_methname: 0x2c1a6
+  __TEXT.__cstring: 0x20ef1
+  __TEXT.__oslogstring: 0x2cc7b
   __TEXT.__swift5_typeref: 0x37a
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_reflstr: 0xc3
-  __TEXT.__swift5_capture: 0x1ac
+  __TEXT.__swift5_capture: 0x1bc
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24

   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__dlopen_cstrs: 0x170
-  __TEXT.__gcc_except_tab: 0xb6b4
+  __TEXT.__gcc_except_tab: 0xb610
   __TEXT.__objc_classname: 0x2378
-  __TEXT.__objc_methtype: 0xa3ce
+  __TEXT.__objc_methtype: 0xa3d4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6720
-  __TEXT.__eh_frame: 0xa30
-  __DATA_CONST.__auth_got: 0x2138
+  __TEXT.__unwind_info: 0x67b0
+  __TEXT.__eh_frame: 0xa58
+  __DATA_CONST.__auth_got: 0x2140
   __DATA_CONST.__got: 0x1338
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x14000
-  __DATA_CONST.__cfstring: 0x1b060
+  __DATA_CONST.__const: 0x14028
+  __DATA_CONST.__cfstring: 0x1b0a0
   __DATA_CONST.__objc_classlist: 0x8c0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x800
-  __DATA_CONST.__objc_intobj: 0x12d8
+  __DATA_CONST.__objc_intobj: 0x12c0
   __DATA_CONST.__objc_arraydata: 0x3f8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x229f0
-  __DATA.__objc_selrefs: 0x92b0
-  __DATA.__objc_ivar: 0x1a10
+  __DATA.__objc_const: 0x228b8
+  __DATA.__objc_selrefs: 0x92a0
+  __DATA.__objc_ivar: 0x19f4
   __DATA.__objc_data: 0x5a78
   __DATA.__data: 0x22c8
   __DATA.__thread_vars: 0xc0

   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 92FF590C-D092-3B9A-A16F-9C830F6B3604
-  Functions: 9629
-  Symbols:   1775
-  CStrings:  19471
+  UUID: 370E4B79-563D-3209-8806-EE5F1965CA43
+  Functions: 9622
+  Symbols:   1776
+  CStrings:  19472
 
Symbols:
+ _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
CStrings:
+ "-[CuttlefishXPCWrapper requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:reply:]_block_invoke"
+ "CREATE INDEX IF NOT EXISTS agrp_musr_tomb_srvr_acct ON inet(agrp, musr, tomb, srvr, acct);"
+ "CREATE INDEX IF NOT EXISTS agrp_musr_tomb_svce_acct ON genp(agrp, musr, tomb, svce, acct);"
+ "CREATE INDEX IF NOT EXISTS agrp_musr_tomb_type ON inet(agrp, musr, tomb, type);"
+ "CREATE INDEX IF NOT EXISTS genpagrp_musr_tomb_acct ON genp(agrp, musr, tomb, acct);"
+ "CREATE INDEX IF NOT EXISTS inetagrp_musr_tomb_acct ON inet(agrp, musr, tomb, acct);"
+ "DROP INDEX IF EXISTS agrp_musr_tomb_srvr;"
+ "DROP INDEX IF EXISTS agrp_musr_tomb_svce;"
+ "DisablePrerecord"
+ "SecItemDb"
+ "escrow-repair-disable"
+ "escrow-repair-enable"
+ "initWithDependencies:followupHandler:isBackgroundCheck:"
+ "performEscrowCheck:"
+ "requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:reply:"
+ "v72@0:8@\"TPSpecificUser\"16B24Q28@\"NSArray\"36B44@\"NSString\"48@\"NSString\"56@?<v@?@\"OTEscrowCheckCallResult\"@\"NSError\">64"
+ "v72@0:8@16B24Q28@36B44@48@56@?64"
+ "🚨 Returning %d items for query: %@ for access group: %@"
- "-[CuttlefishXPCWrapper requestEscrowCheckWithSpecificUser:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:reply:]_block_invoke"
- "CREATE INDEX IF NOT EXISTS agrp_musr_tomb_srvr ON inet(agrp, musr, tomb, srvr);"
- "CREATE INDEX IF NOT EXISTS agrp_musr_tomb_svce ON genp(agrp, musr, tomb, svce);"
- "CuttlefishEscrowCheck"
- "TB,V_requiresEscrowCheck"
- "Unable to perform escrow check"
- "_escrowCheckError"
- "_escrowCheckResults"
- "_requiresEscrowCheck"
- "cuttlefishEscrowCheck"
- "cuttlefish_health_check_is_escrow_check"
- "escrowCheck"
- "initWithDependencies:intendedState:errorState:followupHandler:deviceInfo:isBackgroundCheck:"
- "octagon-trust-escrow-check"
- "requestEscrowCheckWithSpecificUser:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:reply:"
- "requiresEscrowCheck"
- "setRequiresEscrowCheck:"
- "v68@0:8@\"TPSpecificUser\"16Q24@\"NSArray\"32B40@\"NSString\"44@\"NSString\"52@?<v@?@\"OTEscrowCheckCallResult\"@\"NSError\">60"
- "v68@0:8@16Q24@32B40@44@52@?60"

```
