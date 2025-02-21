## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-382.1.0.0.0
-  __TEXT.__text: 0xe2830
+385.9.0.0.0
+  __TEXT.__text: 0xe7828
   __TEXT.__auth_stubs: 0x1700
-  __TEXT.__objc_methlist: 0x5608
-  __TEXT.__const: 0x2d8
-  __TEXT.__cstring: 0x16625
-  __TEXT.__oslogstring: 0xb188
-  __TEXT.__gcc_except_tab: 0x9a5c
+  __TEXT.__objc_methlist: 0x5a5c
+  __TEXT.__const: 0x338
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x2020
-  __TEXT.__objc_classname: 0xa81
-  __TEXT.__objc_methname: 0xc9fd
-  __TEXT.__objc_methtype: 0x173c
-  __TEXT.__objc_stubs: 0x7820
-  __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x33b8
-  __DATA_CONST.__objc_classlist: 0x3d8
+  __TEXT.__cstring: 0x16b37
+  __TEXT.__oslogstring: 0xbabd
+  __TEXT.__gcc_except_tab: 0x9b74
+  __TEXT.__unwind_info: 0x2048
+  __TEXT.__objc_classname: 0xaae
+  __TEXT.__objc_methname: 0xcdd1
+  __TEXT.__objc_methtype: 0x1791
+  __TEXT.__objc_stubs: 0x7920
+  __DATA_CONST.__got: 0x3c8
+  __DATA_CONST.__const: 0x34a0
+  __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26f8
+  __DATA_CONST.__objc_selrefs: 0x27b8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x290
-  __DATA_CONST.__objc_arraydata: 0x170
+  __DATA_CONST.__objc_superrefs: 0x298
+  __DATA_CONST.__objc_arraydata: 0x1b8
   __AUTH_CONST.__auth_got: 0xb98
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x9e0
-  __AUTH_CONST.__cfstring: 0xb460
-  __AUTH_CONST.__objc_const: 0xf528
+  __AUTH_CONST.__const: 0xa60
+  __AUTH_CONST.__cfstring: 0xb9a0
+  __AUTH_CONST.__objc_const: 0xf6d0
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__objc_arrayobj: 0x1b0
+  __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH.__thread_vars: 0x60
-  __AUTH.__thread_bss: 0x19
-  __DATA.__objc_ivar: 0xc00
+  __AUTH.__thread_bss: 0x20
+  __DATA.__objc_ivar: 0xc58
   __DATA.__data: 0x5c4
   __DATA.__crash_info: 0x40
+  __DATA.__bss: 0x50
   __DATA.__common: 0x498
-  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_ivar: 0x44
-  __DATA_DIRTY.__objc_data: 0x2670
-  __DATA_DIRTY.__bss: 0x440
+  __DATA_DIRTY.__objc_data: 0x2710
+  __DATA_DIRTY.__bss: 0x438
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2696
-  Symbols:   3203
-  CStrings:  6361
+  Functions: 2718
+  Symbols:   3266
+  CStrings:  6487
 
Symbols:
+ _OBJC_CLASS_$_SABootInfo
+ _OBJC_CLASS_$_SANANDGarbageCollectionEvent
+ _OBJC_METACLASS_$_SABootInfo
+ _OBJC_METACLASS_$_SANANDGarbageCollectionEvent
+ ___snprintf_chk
- _fmod
CStrings:
+ "\x01\x15"
+ "\x03\x1f\x01\x11\x81\"!1\xa2\x11\x1f\x01\x151\xc5\x12\x13V\x82C"
+ "\x03Q"
+ "%'llu %zu/%zu %s\n"
+ "%'llu Dead reckoned %d samples\n"
+ "%'llu Ignoring PET Sample at %s due to existing PET sample at %s (%lld before most recent event with period %llu)\n\n"
+ "%-*s%.0f%% (%.2fs/%.2fs, %@)\n"
+ "%.0fs gap with no PMI microstackshots (but none missing) between %@ and %@"
+ "%.0fs gap with no PMI microstackshots between %@ and %@"
+ "%@ %@ %@ (%@) build %@, kernel %@, bootargs %@"
+ "%d load infos were null (%d non-null)"
+ "%llu missing PMI microstackshots between %@ and %@"
+ "(entire binary)"
+ "/"
+ "@48@0:8i16Q20I28^@32^@40"
+ "All %d load infos were null"
+ "B40@0:8^{?=CCQdQQQQQ}16Q24@32"
+ "Bad UUID for load info entry: %@"
+ "Captured %{iec-bytes}u of 0x%x (%{iec-bytes}lu total), waiting for needed following chunk"
+ "Found invalid chunk 0x%x length %u"
+ "GC reason:%@(%llu) %@ - %@"
+ "Ignoring systemstats backwards compatibility chunk"
+ "Including 0x%x microstackshot for %s [%d] thread 0x%llx at %@"
+ "Invalid data following boot info header (%{iec-bytes}u)"
+ "Invalid data following dscsym header (%{iec-bytes}u)"
+ "Invalid data following dscsym header (%{iec-bytes}u), lost %{iec-bytes}lu of data in the preceding chunk!"
+ "Kernel callstacks for non-kernel tasks in microstackshots is unsupported"
+ "Load info for unexpected pid %d"
+ "Load info with no pid"
+ "Low mem"
+ "Low validity bands"
+ "Microstackshot statistics:\n%llu bytes parsed (%llu ms, %llu non-ms, %llu invalid)\n%llu filtered out\n\ntotal     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ninterrupt count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ntimer     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nio        count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\npmi       count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nmacf      count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nunknown   count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)"
+ "Missing case for systemstats micro chunk %u"
+ "Must move data"
+ "NAND Garbage Collection: "
+ "No UUID for load info entry"
+ "No load address for load info entry %@ segment %@"
+ "No threads for %@, not including in report"
+ "Not dead-reckoning samples"
+ "Not including duplicate microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall, %fs for this thread)"
+ "Not including microstackshot for %s [%d] at %@ due to being too early (%fs)"
+ "Not including microstackshot for %s [%d] at %@ due to being too late (%fs)"
+ "Not including microstackshot for %s [%d] at %@ due to being wrong pid (requested %d)"
+ "Not including microstackshot for %s [%d] at %@ due to being wrong thread (0x%llx, requested 0x%llx)"
+ "Not including microstackshot for %s [%d] at %@ due to being wrong type (0x%x, requested 0x%x)"
+ "Not including microstackshot for %s [%d] at %@ due to no load info"
+ "Not including out-of-order microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall, %fs for this thread)"
+ "Out-of-order microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall) first sample for this thread"
+ "Out-of-order microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall) is still after latest microstackshot for that thread by %fs"
+ "Out-of-order microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall) is still after latest microstackshot for that thread by %fs (out of order for task)"
+ "Parsed %{iec-bytes}lu dscysm data in microstackshots stream"
+ "Parsed %{iec-bytes}lu of non-MS data, %{iec-bytes}lu of invalid data"
+ "Parsed boot info in microstackshots stream for %@"
+ "Partial microstackshot (%lu), requesting more data"
+ "Partial microstackshot (%{iec-bytes}lu), requesting more data"
+ "Previous %{iec-bytes}lu chunk 0x%x missing needed followup chunk"
+ "Resume after power loss"
+ "Room for OSLC"
+ "SABootInfo"
+ "SANANDGarbageCollectionEvent"
+ "SA_DEAD_RECKONING"
+ "SA_LOG_MICROSTACKSHOTS"
+ "SLC idle"
+ "SLC low on space"
+ "SystemStats boot info dict isn't a dictionary: %s"
+ "T@\"NSArray\",R,V_bootCycles"
+ "T@\"NSArray\",R,V_nandGarbageCollectionEvents"
+ "T@\"NSString\",R,V_bootArgs"
+ "T@\"NSString\",R,V_osBuildVersion"
+ "T@\"NSString\",R,V_osProductVersion"
+ "T@\"NSString\",R,V_osProductVersionExtra"
+ "TLC idle"
+ "TLC low on space"
+ "TQ,V_bytes_other_data"
+ "Task %@ exit at %@, but has later timestamp %@, pushing exit out"
+ "Td,R,V_wallTimeAtMachAbsZero"
+ "Unknown SABootInfo version"
+ "Unknown SANANDGarbageCollectionEvent version"
+ "Virtual card ingest"
+ "_bootCycles"
+ "_bytes_other_data"
+ "_isKernel"
+ "_lastPMIMicrostackshotSampleCount"
+ "_lastPMIMicrostackshotWallTime"
+ "_msInFlightChunkGroupData"
+ "_msInFlightChunkGroupMagic"
+ "_nandGarbageCollectionEvents"
+ "_petTimerMostRecentSampleWasDeadReckoned"
+ "_petTimerNextExpectedSampleMachAbs"
+ "_petTimerPeriodMachAbs"
+ "_reasonCode"
+ "_timestampAfterTimeAdjustments"
+ "_timestampBeforeAnyTimeAdjustments"
+ "_wallTimeAtMachAbsZero"
+ "binaryLoadInfoForLiveProcessWithPid:dataGatheringOptions:additionalCSSymbolicatorFlags:mainBinaryOut:sharedCacheOut:"
+ "bootCycles"
+ "boot_args"
+ "bufferLength %lu < serialized SABootInfo struct %lu"
+ "bufferLength %lu < serialized SANANDGarbageCollectionEvent struct %lu"
+ "bufferLength >= sizeof(*serializedBootInfo)"
+ "bufferLength >= sizeof(*serializedNANDGarbageCollectionEvent)"
+ "bytes_other_data"
+ "componentsSeparatedByString:"
+ "d32@0:8@16^Q24"
+ "deltaMachWithTimeDomainPriorityList:timeDomainUsed:"
+ "deltaSecondsWithTimeDomainPriorityList:timeDomainUsed:"
+ "hw_page_size"
+ "kernel_version"
+ "load_address"
+ "load_info_entries"
+ "load_infos"
+ "mach_timebase"
+ "machine_arch"
+ "main_binary_uuid"
+ "nandGarbageCollectionEvents"
+ "os_build_version"
+ "os_product_name"
+ "os_product_version"
+ "os_product_version_extra"
+ "q32@0:8@16^Q24"
+ "reasonCode"
+ "setBytes_other_data:"
+ "unknown(%llu)"
+ "v16@?0@\"SANANDGarbageCollectionEvent\"8"
+ "vm_page_size"
+ "wallTimeAtMachAbsZero"
+ "walltime"
- "\x011"
- "\x03\x1e\x11\x81\"A\x82\x11\x1f\x01\x151\xc5\x12\x13V\x82C"
- "0"
- "Bad PASerializedSymbolDataStore magic"
- "Microstackshot buffer doesn't contain task_snapshot after micro_snapshot"
- "Microstackshot buffer doesn't contain thread_snapshot after task_snapshot"
- "Microstackshot buffer doesn't start with micro_snapshot"
- "Microstackshot statistics:\n%llu bytes parsed (%llu bytes invalid)\n%llu filtered out\n\ntotal     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ninterrupt count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ntimer     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nio        count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\npmi       count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nmacf      count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nunknown   count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)"
- "Not including microstackshot for %s [%d] at %s due being out of order (before previous by %fs)"
- "Remaining %lu bytes do not contain any microstackshots"
- "Skipping %lu bytes until next microstackshot in the buffer"
- "_mostRecentSampleIsPET"

```
