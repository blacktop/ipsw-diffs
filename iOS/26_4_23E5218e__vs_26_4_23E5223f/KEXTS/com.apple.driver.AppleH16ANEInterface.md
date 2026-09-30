## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-9.510.3.0.0
+9.511.2.0.0
   __TEXT.__const: 0xd50
-  __TEXT.__cstring: 0x11307
-  __TEXT.__os_log: 0x36f2e
-  __TEXT_EXEC.__text: 0x109a94
+  __TEXT.__cstring: 0x1137e
+  __TEXT.__os_log: 0x370e2
+  __TEXT_EXEC.__text: 0x109e04
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4350
   __DATA.__common: 0x680

   __DATA_CONST.__const: 0xcbf8
   __DATA_CONST.__kalloc_type: 0x3b00
   __DATA_CONST.__kalloc_var: 0x3200
-  UUID: AD79BDE1-F070-33F9-B5CA-FD5E911B06A1
+  UUID: BCE0356B-5B73-3C25-9C2D-24DEB779A713
   Functions: 3577
   Symbols:   0
-  CStrings:  4473
+  CStrings:  4478
 
Functions:
~ sub_fffffe0008a38818 -> sub_fffffe000899b318 : 680 -> 688
~ sub_fffffe0008a3aff0 -> sub_fffffe000899daf8 : 284 -> 280
~ sub_fffffe0008a3b2f0 -> sub_fffffe000899ddf4 : 304 -> 300
~ __ZN11ANEHWDevice13ProgramUnloadEP18ANEProgramResourcebb : 2592 -> 3144
~ __ZN11ANEHWDevice17ANE_ProgramCreateEP20ANEProgramCreateArgsP26ANEProgramCreateArgsOutputP4taskPvPy : 2264 -> 2276
~ __ZN11ANEHWDevice51ANE_ProgramSendRequestInitialChecksAndLookups_gatedEP21ANEProgramRequestArgsP15ANESharedEventsP37ANEProgramSendRequestAdditionalParams : 8908 -> 9012
~ __ZN11ANEHWDevice8ANE_InitEv : 13524 -> 13540
~ __ZN11ANEHWDevice10ANE_deInitEv : 4056 -> 4060
~ __ZN11ANEHWDevice5startEP9IOService : 17116 -> 17124
~ __ZN11ANEHWDevice23initializeANEPropertiesEv : 1544 -> 1472
~ __ZN11ANEHWDevice26aneExclaveInterruptHandlerEP22IOInterruptEventSourcei : 1648 -> 1732
~ __ZN18ANEProgramResource23ANE_ProgramInitialSetupEP11ANEHWDeviceP20ANEProgramCreateArgsP26ANEProgramCreateArgsOutputP32ANEProgramCreateAdditionalParams : 5720 -> 5892
CStrings:
+ "\"ANE Exclave ITQ error: 0x%x detected with aneExclaveBootArgConfig bit 0 set (ITQ reg: 0x%x, queue: %lld/%d)\\n\" @%s:%d"
+ "[ERROR] %s: %s: Failed to wire kernel section buffer\n"
+ "[ERROR] %s: %s: Failed to wire mutable init section buffer\n"
+ "[ERROR] %s: %s: Failed to wire text section buffer\n"
+ "[ERROR] %s: %s: System sleep in progress, not unwiring program programHandle: 0x%llx\n"
+ "[ERROR] %s: %s: invalid procedureId: %u, kANEMaxProcedures: %u\n"
+ "[ERROR] %s: %s: waitForPendingUpdate failed for programHandle=0x%llx"
- "%s: %s: ERROR: failed to wire kernel section buffer\n"
- "%s: %s: ERROR: failed to wire text section buffer\n"

```
