## thermalmonitord

> `/usr/libexec/thermalmonitord`

```diff

-1947.80.2.0.0
-  __TEXT.__text: 0x53594
-  __TEXT.__auth_stubs: 0x1380
-  __TEXT.__objc_stubs: 0x4ee0
-  __TEXT.__objc_methlist: 0x3b60
+1952.100.8.0.0
+  __TEXT.__text: 0x560e0
+  __TEXT.__auth_stubs: 0x13f0
+  __TEXT.__objc_stubs: 0x50e0
+  __TEXT.__objc_methlist: 0x3c98
   __TEXT.__const: 0x1900
-  __TEXT.__objc_classname: 0xe66
-  __TEXT.__objc_methname: 0x84e1
-  __TEXT.__objc_methtype: 0x1776
-  __TEXT.__gcc_except_tab: 0x3ac
-  __TEXT.__cstring: 0x4ac1
-  __TEXT.__oslogstring: 0x7c8d
+  __TEXT.__objc_classname: 0xf10
+  __TEXT.__objc_methname: 0x868f
+  __TEXT.__objc_methtype: 0x1894
+  __TEXT.__gcc_except_tab: 0x3c4
+  __TEXT.__cstring: 0x4bbd
+  __TEXT.__oslogstring: 0x85ea
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x1050
-  __DATA_CONST.__auth_got: 0x9d8
-  __DATA_CONST.__got: 0x1b0
+  __TEXT.__unwind_info: 0x10ac
+  __DATA_CONST.__auth_got: 0xa10
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1460
-  __DATA_CONST.__cfstring: 0x6020
-  __DATA_CONST.__objc_classlist: 0x410
+  __DATA_CONST.__cfstring: 0x6120
+  __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x4c8
+  __DATA_CONST.__objc_superrefs: 0x2f0
   __DATA_CONST.__objc_intobj: 0x768
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x1c8
-  __DATA.__objc_const: 0xc210
-  __DATA.__objc_selrefs: 0x18b0
-  __DATA.__objc_classrefs: 0x498
-  __DATA.__objc_superrefs: 0x2e8
-  __DATA.__objc_ivar: 0xa7c
-  __DATA.__objc_data: 0x28a0
+  __DATA.__objc_const: 0xc5a8
+  __DATA.__objc_selrefs: 0x1928
+  __DATA.__objc_ivar: 0xa94
+  __DATA.__objc_data: 0x2a30
   __DATA.__data: 0x3c8
   __DATA.__bss: 0x7468
   __DATA.__common: 0x9e4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 488CC994-A87D-30DD-83AA-131CBE3B93B7
-  Functions: 2028
-  Symbols:   404
-  CStrings:  4292
+  UUID: CB160328-429F-320A-8EA7-3BE29014A251
+  Functions: 2091
+  Symbols:   414
+  CStrings:  4399
 
Symbols:
+ _CFDataCreate
+ _CFDataGetTypeID
+ _CFUUIDGetConstantUUIDWithBytes
+ _IOServiceNameMatching
+ _OBJC_CLASS_$_NSData
+ _XPC_ACTIVITY_CHECK_IN
+ _kCFAllocatorSystemDefault
+ _malloc_type_calloc
+ _xpc_activity_get_state
+ _xpc_activity_register
CStrings:
+ "%@:%s"
+ "<Error> %s missing!\n"
+ "<Error> Failed to allocate memory for integrator state. size: %zu\n"
+ "<Error> Failed to create CFData for key %@"
+ "<Error> Failed to create NVRam persistence path"
+ "<Error> Failed to create filer"
+ "<Error> Failed to create key for die %u loop %u\n"
+ "<Error> Failed to find %s service in the registry"
+ "<Error> Failed to get path to srvo folder. resp:%ld"
+ "<Error> Failed to get updated LTS state\n"
+ "<Error> Failed to read LTS State from NVRam"
+ "<Error> Failed to read die count for registry\n"
+ "<Error> Failed to read die count from persistant LTS Stats"
+ "<Error> Failed to read key %@"
+ "<Error> Failed to read loop count for registry\n"
+ "<Error> Failed to read loop count from persistant LTS Stats"
+ "<Error> Failed to save LTS data to file"
+ "<Error> Failed to save counter\n"
+ "<Error> Failed to save die count\n"
+ "<Error> Failed to save loop count\n"
+ "<Error> Failed to save version\n"
+ "<Error> Failed to send data for key %@ to PMP"
+ "<Error> Failed to send data to PMP: die %u loop %u"
+ "<Error> Failed to write persistent data\n"
+ "<Error> LTS data from NVRam has invalid version %d. Ignoring the data."
+ "<Error> LTS data from Nand has invalid version %d. Ignoring the data."
+ "<Error> LifetimeServoStatePersistence init failed\n"
+ "<Error> NVRam and NAND data is invalid. Nothing to send to PMP"
+ "<Error> NVRam data length %lu does not match expected length %lu bytes. Die count:%d Loop count:%d"
+ "<Error> NVRam persistence path is null"
+ "<Error> Persistent NVRAM  missing!"
+ "<Error> Persistent data is corrupted\n"
+ "<Error> Retrieving initial data from PMP and storing in NAND & NVRAM"
+ "<Error> Unexpected data size %ld bytes for key %@\n"
+ "<Error> Unexpected data type for key %@\n"
+ "<Notice> Activity Run. Updating NVRAM"
+ "<Notice> Activity checking in"
+ "<Notice> Copied LTS state data from PMP"
+ "<Notice> Failed to create CFNumber for integer %d\n"
+ "<Notice> Failed to read 'counter' from disk. On-disk file is missing\n"
+ "<Notice> Failed to read integrator state for key %@"
+ "<Notice> Failed to read value for key %@"
+ "<Notice> Initalizing PMP LTS state counter"
+ "<Notice> NVRam contains more recent version of LTS Stats"
+ "<Notice> NVRam path: %@"
+ "<Notice> Persitence filepath:%s"
+ "<Notice> Saved LTS state to NVRam"
+ "<Notice> Saved updated LTS stats data to Nand"
+ "<Notice> Sending data to PMP: die %u loop %u is: %@"
+ "<Notice> Updated PMP with saved LTS State"
+ "<Notice> dieCount:%u loopCount:%u"
+ "<Notice> sendLTSStateToPMP: dieCount:%u loopCount:%u"
+ "@\"LifetimeServoStatePersistence\""
+ "ApplePMPv2"
+ "B28@0:8I16^{__CFString=}20"
+ "B32@0:8^I16^{__CFString=}24"
+ "B32@0:8^{__CFData=}16^{__CFString=}24"
+ "B32@0:8^{ltsState=IIII[0Q]}16Q24"
+ "B40@0:8r^v16Q24^{__CFString=}32"
+ "IODeviceTree:/options"
+ "LifetimeServoStatePersistence"
+ "Q24@0:8^^{ltsState}16"
+ "T@\"NSString\",?,R,C"
+ "^{__CFData=}24@0:8^{__CFString=}16"
+ "^{__CFData=}28@0:8^{__CFString=}16B24"
+ "_ltsStateSaveInterval"
+ "_nvramPersistence"
+ "_pmpLTSStateversion"
+ "com.apple.thermalMonitor.1weekTask"
+ "com.apple.thermalmonitor.lts-ctrl-state"
+ "copyFiler"
+ "copyKeyFromPMP:is_64:"
+ "copyLTSStateFromPMP:"
+ "copyPersistedStateNvram:"
+ "copyPersistenceNvramPath"
+ "counter"
+ "dataWithBytes:length:"
+ "die %u loop %u is: %{public}@"
+ "getBytes:length:"
+ "getPMPSvc"
+ "lifetimeServoStatePersistence"
+ "lts-ctrl-%u-%u-is"
+ "lts-ctrl-%u-%u-is-inuse"
+ "lts-ctrl-die-count"
+ "lts-ctrl-loop-count"
+ "lts-persistance"
+ "needsLTSStatePersistence"
+ "readInteger:forKey:"
+ "saveLTSStateToNand:dataSize:"
+ "sendDataToPMP:forKey:"
+ "sendLTSStateToPMP"
+ "tm486ea271e6c13e89a0b7e8b50d4c2b83"
+ "tmaeef0c56a43849a743faa430c529385e"
+ "tmc2ef236d861614f6101378b7022f5718"
+ "tmc3ba61e8d834ffede58b86c1dd2780f4"
+ "updateNvramLTSState"
+ "version"
+ "writeInteger:withKey:"
+ "writePersistedStateNvram:dataSize:path:"

```
