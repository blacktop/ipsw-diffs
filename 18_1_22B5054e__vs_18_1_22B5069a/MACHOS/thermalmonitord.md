## thermalmonitord

> `/usr/libexec/thermalmonitord`

```diff

-1981.40.4.0.0
-  __TEXT.__text: 0x567ac
-  __TEXT.__auth_stubs: 0x1430
-  __TEXT.__objc_stubs: 0x5180
-  __TEXT.__objc_methlist: 0x3e3c
+1981.40.7.0.0
+  __TEXT.__text: 0x57e70
+  __TEXT.__auth_stubs: 0x1410
+  __TEXT.__objc_stubs: 0x5360
+  __TEXT.__objc_methlist: 0x3eec
   __TEXT.__const: 0x1cc8
   __TEXT.__objc_classname: 0x10d7
-  __TEXT.__objc_methtype: 0x1894
-  __TEXT.__objc_methname: 0x86ff
-  __TEXT.__cstring: 0x4c11
+  __TEXT.__objc_methtype: 0x19e9
+  __TEXT.__objc_methname: 0x88a5
+  __TEXT.__cstring: 0x4c33
   __TEXT.__gcc_except_tab: 0x428
-  __TEXT.__oslogstring: 0x88a0
+  __TEXT.__oslogstring: 0x916e
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x1120
-  __DATA_CONST.__auth_got: 0xa30
-  __DATA_CONST.__got: 0x588
+  __TEXT.__unwind_info: 0x1148
+  __DATA_CONST.__auth_got: 0xa20
+  __DATA_CONST.__got: 0x580
   __DATA_CONST.__const: 0x1460
-  __DATA_CONST.__cfstring: 0x6180
+  __DATA_CONST.__cfstring: 0x61c0
   __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x1c8
-  __DATA.__objc_const: 0xcd68
-  __DATA.__objc_selrefs: 0x1958
-  __DATA.__objc_ivar: 0xaa0
+  __DATA.__objc_const: 0xce28
+  __DATA.__objc_selrefs: 0x19e0
+  __DATA.__objc_ivar: 0xab8
   __DATA.__objc_data: 0x2e40
   __DATA.__data: 0x3c8
   __DATA.__bss: 0x80f4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1982
-  Symbols:   419
-  CStrings:  3661
+  Functions: 2016
+  Symbols:   416
+  CStrings:  3729
 
Symbols:
- _XPC_ACTIVITY_CHECK_IN
- _xpc_activity_get_state
- _xpc_activity_register
CStrings:
+ "<Error> ERROR: Persistence LTS Counter uninitialized after reset."
+ "<Error> ERROR: getNVRAMCounter requested on non-NVRAM supported device"
+ "<Error> ERROR: getNVRAMVer requested on non-NVRAM supported device"
+ "<Error> ERROR: nvramDataValid requested on non-NVRAM supported device"
+ "<Error> ERROR: nvramUpgradeStateV3 Could not create LTS State IS Rev copy"
+ "<Error> ERROR: nvramUpgradeStateV3 requested on non-NVRAM supported device"
+ "<Error> ERROR: readNVRAM Could not create LTS State Common struct copy"
+ "<Error> ERROR: readNVRAM Could not create LTS State IS Rev copy"
+ "<Error> ERROR: readNVRAM Could not create LTS State IS copy"
+ "<Error> ERROR: readNVRAM requested but path to NVRAM does not exist!"
+ "<Error> ERROR: readNVRAM requested on non-NVRAM supported device!"
+ "<Error> Failed saving LTS state to NVRam"
+ "<Error> Failed to allocate memory for integrator State\n"
+ "<Error> Failed to allocate memory for integrator State Revision\n"
+ "<Error> Failed to allocate memory for ltsStateCommon struct\n"
+ "<Error> Failed to allocate memory for ltsStateV3 struct\n"
+ "<Error> Failed to create is rev key for die %!u(MISSING) loop %!u(MISSING)\n"
+ "<Error> Failed to create revision key for die %!u(MISSING) loop %!u(MISSING)\n"
+ "<Error> Failed to save IS revision for lts-ctrl-%!u(MISSING)-%!u(MISSING)-is-rev\n"
+ "<Error> Failed to update LTS Integrator State Revision!\n"
+ "<Error> Failed to update LTS Integrator State!\n"
+ "<Error> Failed to update the LTS State Common Struct from PMP\n"
+ "<Error> Failed to update! Cleaning up ltsStateData"
+ "<Error> NVRAM version %!u(MISSING), but NVRAM length of %!l(MISSING)d is mismatched - version will be invalidated"
+ "<Error> Unknown Persistence version %!d(MISSING)! Will revert to current supported version"
+ "<Error> initializeLTSPersistence: Failed to reset Persistence Counter"
+ "<Error> initializeLTSPersistence: Failed to update persistence files!"
+ "<Error> readNVRAM: Failed to read LTS State from NVRam"
+ "<Error> updatePersistenceLTSState: Failed to get updated LTS state"
+ "<Notice> Copied LTS IS data from PMP"
+ "<Notice> LTS data from NAND contains %!l(MISSING)lu years of accumulated IS"
+ "<Notice> LTS data from NVRAM contains %!l(MISSING)lu years of accumulated IS"
+ "<Notice> LTS getNANDCounter: NAND counter does not exist"
+ "<Notice> LTS getNANDVer: NAND version does not exist"
+ "<Notice> LTS getNVRAMCounter: NVRAM counter %!d(MISSING)"
+ "<Notice> LTS getNVRAMCounter: NVRAM counter does not exist"
+ "<Notice> LTS getNVRAMVer: NVRAM version %!d(MISSING)"
+ "<Notice> LTS getNVRAMVer: NVRAM version does not exist"
+ "<Notice> LTS nandDataValid: NAND data is %!s(MISSING)"
+ "<Notice> LTS nvramDataValid: NVRAM DATA does not exist"
+ "<Notice> LTS nvramDataValid: NVRAM data is %!s(MISSING)"
+ "<Notice> LTS nvramUpgradeStateV3: NVRAM DATA does not exist"
+ "<Notice> NAND version %!d(MISSING) mismatch - will be updated to version %!d(MISSING)"
+ "<Notice> NVRAM Length %!l(MISSING)d less than required %!l(MISSING)d, cannot acquire IS data"
+ "<Notice> NVRAM data is INVALID and will be reset"
+ "<Notice> NVRAM version %!d(MISSING) mismatch - will be updated to version %!d(MISSING)"
+ "<Notice> NVRAM will be updated"
+ "<Notice> No valid NVRam and NAND data. Nothing to send to PMP"
+ "<Notice> PMP update with LTS State complete"
+ "<Notice> Resolved persistence: Version: %!d(MISSING), Counter: %!d(MISSING), PMP Data Source: %!d(MISSING)"
+ "<Notice> Retrieving initial data from PMP and storing in NAND & NVRAM"
+ "B24@0:8^{ltsStateCommon=IIII}16"
+ "B24@0:8^{ltsStateV3=^{ltsStateCommon}^Q^I}16"
+ "B32@0:8^{ltsStateV3=^{ltsStateCommon}^Q^I}16^{__CFString=}24"
+ "INVALID"
+ "LTSStatePersistencePerIpRevision"
+ "UpdateLTSStateCommonFromPMP:"
+ "VALID"
+ "^{ltsStateV3=^{ltsStateCommon}^Q^I}16@0:8"
+ "_currNvramLTSStateV3"
+ "_hasNvram"
+ "_initializeNvram"
+ "_isRevDict"
+ "_nvramLength"
+ "_resolvedLTSPersistence"
+ "appendData:"
+ "copyUpdatedLTSState"
+ "getNANDCounter"
+ "getNANDVer"
+ "getNVRAMCounter"
+ "getNVRAMVer"
+ "initializeLTSPersistence"
+ "isNandDataValid"
+ "isNvramDataValid"
+ "lts-ctrl-%!u(MISSING)-%!u(MISSING)-is-rev"
+ "mutableCopy"
+ "nvramUpgradeStateV2toV3"
+ "readNVRAM"
+ "resolvePersistentLTSState"
+ "safeFreeUpdatedLTSState:"
+ "saveLTSStateToNand:"
+ "updateLTSStateISFromPMP:"
+ "updateLTSStateISRev:"
+ "updatePersistenceLTSState:"
+ "v24@0:8^{ltsStateV3=^{ltsStateCommon}^Q^I}16"
+ "writeV3PersistedStateNvram:path:"
+ "{ltsPersistenceData=\"current_version\"I\"current_count\"I\"pmp_data_source\"i}"
+ "{ltsStateV3=\"ltsStateCommonPtr\"^{ltsStateCommon}\"integratorStatePtr\"^Q\"integratorStateRevPtr\"^I}"
- "<Error> Failed to allocate memory for integrator state. size: %!z(MISSING)u\n"
- "<Error> Failed to read LTS State from NVRam"
- "<Error> LTS data from NAND contains %!l(MISSING)lu years of accumulated IS! Ignoring the data"
- "<Error> LTS data from NVRam has invalid data. Ignoring the data."
- "<Error> LTS data from Nand has invalid version %!d(MISSING). Ignoring the data."
- "<Error> NVRam and NAND data is invalid. Nothing to send to PMP"
- "<Error> NVRam data length %!l(MISSING)u does not match expected length %!l(MISSING)u bytes. Die count:%!d(MISSING) Loop count:%!d(MISSING)"
- "<Error> Retrieving initial data from PMP and storing in NAND & NVRAM"
- "<Notice> Activity Run. Updating NVRAM"
- "<Notice> Activity checking in"
- "<Notice> Copied LTS state data from PMP"
- "<Notice> Failed to read 'counter' from disk. On-disk file is missing\n"
- "<Notice> Initalizing PMP LTS state counter"
- "<Notice> NVRam contains more recent version of LTS Stats"
- "B32@0:8^{ltsState=IIII[0Q]}16Q24"
- "Q24@0:8^^{ltsState}16"
- "com.apple.thermalMonitor.1weekTask"
- "copyLTSStateFromPMP:"
- "saveLTSStateToNand:dataSize:"
- "updateNvramLTSState"

```
