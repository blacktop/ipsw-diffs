## securityd

> `/usr/libexec/securityd`

```diff

-61901.0.56.0.1
-  __TEXT.__text: 0x258c64
-  __TEXT.__auth_stubs: 0x4260
-  __TEXT.__objc_stubs: 0x1c4e0
-  __TEXT.__objc_methlist: 0x15268
+61901.0.84.0.0
+  __TEXT.__text: 0x258be8
+  __TEXT.__auth_stubs: 0x4280
+  __TEXT.__objc_stubs: 0x1c5e0
+  __TEXT.__objc_methlist: 0x15210
   __TEXT.__const: 0x879
-  __TEXT.__objc_methname: 0x2c1a6
-  __TEXT.__cstring: 0x20ef1
-  __TEXT.__oslogstring: 0x2cc7b
+  __TEXT.__objc_methname: 0x2c245
+  __TEXT.__cstring: 0x20e30
+  __TEXT.__oslogstring: 0x2cf5f
   __TEXT.__swift5_typeref: 0x37a
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__constg_swiftt: 0x274

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__dlopen_cstrs: 0x170
-  __TEXT.__gcc_except_tab: 0xb610
-  __TEXT.__objc_classname: 0x2378
-  __TEXT.__objc_methtype: 0xa3d4
+  __TEXT.__gcc_except_tab: 0xb5f4
+  __TEXT.__objc_classname: 0x2360
+  __TEXT.__objc_methtype: 0xa46d
+  __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x67b0
+  __TEXT.__unwind_info: 0x6780
   __TEXT.__eh_frame: 0xa58
-  __DATA_CONST.__auth_got: 0x2140
+  __DATA_CONST.__auth_got: 0x2150
   __DATA_CONST.__got: 0x1340
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x13fe8
-  __DATA_CONST.__cfstring: 0x1b0a0
-  __DATA_CONST.__objc_classlist: 0x8c0
+  __DATA_CONST.__const: 0x13fd8
+  __DATA_CONST.__cfstring: 0x1b100
+  __DATA_CONST.__objc_classlist: 0x8b8
   __DATA_CONST.__objc_catlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x800
+  __DATA_CONST.__objc_superrefs: 0x7f8
   __DATA_CONST.__objc_intobj: 0x12c0
   __DATA_CONST.__objc_arraydata: 0x3f8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x228b8
-  __DATA.__objc_selrefs: 0x92a0
-  __DATA.__objc_ivar: 0x19f4
-  __DATA.__objc_data: 0x5a78
-  __DATA.__data: 0x22c8
+  __DATA.__objc_const: 0x227d0
+  __DATA.__objc_selrefs: 0x92b8
+  __DATA.__objc_ivar: 0x19ec
+  __DATA.__objc_data: 0x5a28
+  __DATA.__data: 0x2320
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0xe78
+  __DATA.__bss: 0xe50
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E4C84E02-B621-355F-A4F2-9D9B1E24E65F
-  Functions: 9622
-  Symbols:   1769
-  CStrings:  19472
+  UUID: CB107522-D5B0-3F75-BED0-029C4DDA02A6
+  Functions: 9605
+  Symbols:   1771
+  CStrings:  19496
 
Symbols:
+ _SOSCCIsSOSTrustAndSyncingEnabled
+ _SimulateCrash
+ _WriteStackshotReport
+ _kMKBDeviceModeSharedIPad
- _NSMachErrorDomain
- _abort_report_np
CStrings:
+ "%@-%@-fetchFailed"
+ "@\"<EscrowChecker>\""
+ "@\"CKContainer\"16@0:8"
+ "@196@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128#136#144@152@160B168B172B176@180@188"
+ "Do not have CKKSKey(%@) locally"
+ "Do not have TLK(%@) locally"
+ "Do not have TLK(%@) locally with unexpected error: %@"
+ "EscrowCheckMigration"
+ "EscrowChecker"
+ "Have TLK(%@) locally"
+ "Have TLK(%@) locally, but device is locked"
+ "No current TLK in keyset: %@"
+ "Rerolling identity"
+ "RollIdentityOnMIDRotation"
+ "RollIdentityOnMIDRotation is %s"
+ "SOS is disabled, Skipping backing up tombstones"
+ "Switching CloudKit container for CKKS & CKKSAccountStateTracker for account(%@) associated with (%@) container"
+ "T@\"<EscrowChecker>\",R,W,V_escrowChecker"
+ "T@\"CKContainer\",&"
+ "TQ,N,V_lastEscrowRepairAttempted"
+ "Unable to check haveTLKs: %@"
+ "Unable to load CKKSKey TLK: %@"
+ "_escrowChecker"
+ "_lastEscrowRepairAttempted"
+ "accountID"
+ "checkMachineID"
+ "could not fetch account state -- not checking machine id (%@)"
+ "enablePasscodeCacheFlow:"
+ "escrow check migration is disabled"
+ "escrowChecker"
+ "failed to persist escrow repair attempt date: %@"
+ "fetching machine id failed: %@"
+ "hasLastEscrowRepairAttempted"
+ "hasMachineID"
+ "haveTLKsLocally:error:"
+ "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:secureBackupAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:flowID:deviceSessionID:permittedToSendMetrics:accountIsG:accountIsW:reachabilityTracker:escrowChecker:"
+ "initWithAccountID:"
+ "lastEscrowRepairAttempted"
+ "machineID %@ -> %@"
+ "memoizedLastEscrowRepairAttempted"
+ "persistLastEscrowRepairAttempted:error:"
+ "repairReason"
+ "reroll feature flag disabled -- not rerolling"
+ "reroll feature flag enabled -- rerolling"
+ "reroll-identity"
+ "reroll_identity"
+ "secAssociateIndirectUnlockKey:handle:completion:"
+ "setHasLastEscrowRepairAttempted:"
+ "setLastEscrowRepairAttempted:"
+ "tomb = 0"
+ "updateAccount:container:"
+ "v24@0:8@\"CKContainer\"16"
+ "v28@0:8B16@?<v@?@\"OTEscrowCheckCallResult\"@\"NSError\">20"
+ "v36@0:8@\"NSString\"16I24@?<v@?i>28"
+ "v36@0:8@16I24@?28"
+ "{?=\"epoch\"b1\"lastEscrowRepairAttempted\"b1\"lastEscrowRepairTriggered\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"
+ "\xe1a"
- "@188@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128#136#144@152@160B168B172B176@180"
- "BOOL soft_SimulateCrash(pid_t, mach_exception_data_type_t, NSString *__strong)"
- "BOOL soft_WriteStackshotReport(NSString *__strong, mach_exception_data_type_t)"
- "MKBUserTypeDeviceMode"
- "OTAccountMetadataClassCAccountSettings"
- "SimulateCrash"
- "TB,N,V_w"
- "TB,N,V_webAccess"
- "TQ,N,V_lastEscrowRepairSucceeded"
- "WriteStackshotReport"
- "_lastEscrowRepairSucceeded"
- "_w"
- "clearing follow ups"
- "hasLastEscrowRepairSucceeded"
- "hasW"
- "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:secureBackupAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:flowID:deviceSessionID:permittedToSendMetrics:accountIsG:accountIsW:reachabilityTracker:"
- "kMKBDeviceModeKey"
- "kMKBDeviceModeSharedIPad"
- "lastEscrowRepairSucceeded"
- "memoizedLastEscrowRepairSucceeded"
- "persistLastEscrowRepairSucceeded:error:"
- "secGenerateIndirectUnlockKey:completion:"
- "setHasLastEscrowRepairSucceeded:"
- "setHasW:"
- "setHasWebAccess:"
- "setLastEscrowRepairSucceeded:"
- "setW:"
- "simulate_crash.m"
- "softlink:o:path:/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport"
- "softlink:o:path:/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag"
- "updatePasscodeCacheFlow:"
- "void *CrashReporterSupportLibrary(void)"
- "{?=\"epoch\"b1\"lastEscrowRepairSucceeded\"b1\"lastEscrowRepairTriggered\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"
- "{?=\"w\"b1\"webAccess\"b1}"
- "\xe1"

```
