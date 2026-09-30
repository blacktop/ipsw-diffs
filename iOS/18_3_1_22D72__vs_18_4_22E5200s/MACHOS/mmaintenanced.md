## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-158.80.2.0.0
-  __TEXT.__text: 0x18764
-  __TEXT.__auth_stubs: 0x1130
+158.100.10.502.1
+  __TEXT.__text: 0x1a4d8
+  __TEXT.__auth_stubs: 0x1260
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x1184
-  __TEXT.__oslogstring: 0x20c3
-  __TEXT.__cstring: 0x1718
-  __TEXT.__gcc_except_tab: 0x748
-  __TEXT.__objc_methname: 0xe9
-  __TEXT.__swift5_typeref: 0x64
+  __TEXT.__const: 0x122a
+  __TEXT.__oslogstring: 0x24b3
+  __TEXT.__cstring: 0x18e8
+  __TEXT.__gcc_except_tab: 0x7d0
+  __TEXT.__objc_methname: 0x1b5
+  __TEXT.__swift5_typeref: 0x70
   __TEXT.__swift5_capture: 0x78
-  __TEXT.__constg_swiftt: 0x28
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__constg_swiftt: 0x44
+  __TEXT.__swift5_fieldmd: 0x50
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift5_reflstr: 0x24
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__unwind_info: 0x818
   __TEXT.__eh_frame: 0x208
-  __DATA_CONST.__auth_got: 0x8a0
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0xd80
+  __DATA_CONST.__auth_got: 0x938
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__auth_ptr: 0x68
+  __DATA_CONST.__const: 0xf80
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x60
-  __DATA.__data: 0xeb0
-  __DATA.__bss: 0x48
+  __DATA.__objc_selrefs: 0xb8
+  __DATA.__data: 0xec8
+  __DATA.__bss: 0x170
   __DATA.__common: 0x40
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/KRExperiments.framework/KRExperiments
   - /System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 504
-  Symbols:   406
-  CStrings:  412
+  Functions: 532
+  Symbols:   429
+  CStrings:  451
 
Symbols:
+ _$sSH13_rawHashValue4seedS2i_tFTq
+ _$sSH4hash4intoys6HasherVz_tFTq
+ _$sSH9hashValueSivgTq
+ _$sSHMp
+ _$sSHSQTb
+ _$sSQ2eeoiySbx_xtFZTq
+ _$sSQMp
+ _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
+ _$sSo8NSNumberC10FoundationE14booleanLiteralABSb_tcfC
+ _$ss018_bridgeAnyObjectToB0yypyXlSgF
+ _$ss20__StaticArrayStorageCN
+ _$ss5Int64V10FoundationE10truncatingABSo8NSNumberCh_tcfC
+ _$ss5Int64V10FoundationE19_bridgeToObjectiveCSo8NSNumberCyF
+ _$ss5Int64VN
+ _$ss6HasherV5_seedABSi_tcfC
+ _$ss6HasherV8_combineyySuF
+ _$ss6HasherV9_finalizeSiyF
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_TRIClient
+ _PrewarmingExperimentUpdated
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEED2Ev
+ __ZTTNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEE
+ __swiftImmortalRefCount
+ _objc_retain_x19
+ _objc_retain_x21
+ _os_release
+ _os_transaction_create
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_getWitnessTable
- _$s10Foundation4DateVMn
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEED2Ev
- __ZTTNSt3__114basic_ofstreamIcNS_11char_traitsIcEEEE
- __ZTVNSt3__114basic_ofstreamIcNS_11char_traitsIcEEEE
- _objc_release_x25
CStrings:
+ "%s: Preperation of 'get_init_time_query' failed, rc: %d"
+ "%s: failed to execute the query: %s"
+ "%s: failed to open time_table database, rc: %d"
+ "%s: sqlite3_step return rc: %d"
+ "COREOS_GMPOWER_VM_TUNING_PAGE_SHORTAGE_THRESHOLDS"
+ "CREATE TABLE IF NOT EXISTS time_table (ID INTEGER PRIMARY KEY, time INT);"
+ "Failed to create UserDefaults for %s"
+ "Failed to find trial factor for name %s in namespace %s"
+ "Failed to get existing value for %s"
+ "Failed to remove default value for %s, may be sticky"
+ "Failed to set %s with factor %s (%@) with errno %d"
+ "Failed to set default value for %s, skipping"
+ "Failing to save default value for %s, skipping trial factor"
+ "First trial enablement, storing default values for %s"
+ "INSERT INTO time_table('time') VALUES(?);"
+ "Preperation of 'insert_time_record_query' failed, rc: %d"
+ "Processing trial namespace update"
+ "QuartersCount"
+ "Recieved notification of idle reaper trial update"
+ "Recieved notification of prewarming experiment update"
+ "SELECT name FROM sqlite_master WHERE type='table' AND name='time_table';"
+ "SELECT time FROM time_table;"
+ "Successfully set %s to value of %@"
+ "Trial factor %s is disabled and no default value is specified, skipping"
+ "Trial factor %s is disabled but a default value is specified, resetting"
+ "addSuiteNamed:"
+ "booleanValue"
+ "clientWithIdentifier:"
+ "com.apple.memory-maintenance.idle-reaper"
+ "com.apple.trial.NamespaceUpdate.COREOS_FAST_PREWARMING"
+ "com.apple.trial.NamespaceUpdate.COREOS_GMPOWER_VM_TUNING_PAGE_SHORTAGE_THRESHOLDS"
+ "get_time_from_db"
+ "initWithLongLong:"
+ "initWithSuiteName:"
+ "init_time_handling"
+ "init_time_table"
+ "insert_initialization_time"
+ "kern.memorystatus.reaper_enabled"
+ "kern.memorystatus.reaper_max_priority"
+ "kern.memorystatus.reaper_min_age_secs"
+ "kern.memorystatus.reaper_reap_relaunch_mask"
+ "kern.memorystatus.reaper_rescan_secs"
+ "kern.memorystatus.reaper_threshold_mb"
+ "levelForFactor:withNamespaceName:"
+ "longValue"
+ "objectForKey:"
+ "reaper_max_priority"
+ "reaper_min_age_secs"
+ "reaper_reap_relaunch_mask"
+ "reaper_rescan_secs"
+ "reaper_threshold_mb"
+ "removeObjectForKey:"
+ "setObject:forKey:"
+ "standardUserDefaults"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "initialize"
- "invalid Collection: less than 'count' elements in collection"
- "ok"

```
