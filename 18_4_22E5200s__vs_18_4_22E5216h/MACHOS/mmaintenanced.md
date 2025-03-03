## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-158.100.10.502.1
-  __TEXT.__text: 0x1a4d8
-  __TEXT.__auth_stubs: 0x1260
+158.100.14.0.0
+  __TEXT.__text: 0x1c034
+  __TEXT.__auth_stubs: 0x12d0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x122a
-  __TEXT.__oslogstring: 0x24b3
-  __TEXT.__cstring: 0x18e8
+  __TEXT.__const: 0x124a
+  __TEXT.__oslogstring: 0x2673
+  __TEXT.__cstring: 0x1b28
   __TEXT.__gcc_except_tab: 0x7d0
-  __TEXT.__objc_methname: 0x1b5
-  __TEXT.__swift5_typeref: 0x70
+  __TEXT.__swift5_typeref: 0x9e
+  __TEXT.__objc_methname: 0x1db
   __TEXT.__swift5_capture: 0x78
   __TEXT.__constg_swiftt: 0x44
   __TEXT.__swift5_fieldmd: 0x50

   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_reflstr: 0x24
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__unwind_info: 0x818
+  __TEXT.__unwind_info: 0x838
   __TEXT.__eh_frame: 0x208
-  __DATA_CONST.__auth_got: 0x938
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0xf80
+  __DATA_CONST.__auth_got: 0x970
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__auth_ptr: 0x80
+  __DATA_CONST.__const: 0x1018
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0xb8
-  __DATA.__data: 0xec8
-  __DATA.__bss: 0x170
+  __DATA.__objc_selrefs: 0xc8
+  __DATA.__data: 0xed8
+  __DATA.__bss: 0x190
   __DATA.__common: 0x40
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 532
-  Symbols:   429
-  CStrings:  451
+  Functions: 541
+  Symbols:   441
+  CStrings:  473
 
Symbols:
+ _$sSD10FoundationE19_bridgeToObjectiveCSo12NSDictionaryCyF
+ _$sSS4hash4intoys6HasherVz_tF
+ _$sSSN
+ _$sSSSHsWP
+ _$sSi10FoundationEySiSo8NSNumberChcfC
+ _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
+ _$ss18_DictionaryStorageCMn
+ _$ss27_stringCompareWithSmolCheck__9expectingSbs11_StringGutsV_ADs01_G16ComparisonResultOtF
+ _AnalyticsSendEvent
+ _OBJC_CLASS_$_NSObject
+ __swiftEmptyDictionarySingleton
+ _objc_release_x25
+ _objc_retain_x23
+ _objc_retain_x26
+ _swift_beginAccess
+ _swift_initStackObject
+ _swift_retain
- _$sSo8NSNumberC10FoundationE14booleanLiteralABSb_tcfC
- _$ss5Int64V10FoundationE10truncatingABSo8NSNumberCh_tcfC
- _objc_release_x28
- _objc_release_x8
- _objc_retain_x21
CStrings:
+ "COREOS_VM_OBJECT_COPY_DELAYED_NO_WAIT"
+ "Failed to get existing value for %s, errno = %d"
+ "Failed to get sweep count value with errno %d"
+ "Failed to get total freed mb value with errno %d"
+ "Failed to get total kill count value with errno %d"
+ "Failed to set %s with factor %s (%@), errno = %d"
+ "Failing to save default value for %s, skipping trial factor, errno = %d"
+ "IdleReaperTelemetry"
+ "Recieved notification of vm-object-copy-delayed-no-wait trial update"
+ "Sweep Count = %u | total reaper kills = %u | total freed mb = %u"
+ "com.apple.memory-maintenance.report-idle-reaper-telemetry"
+ "com.apple.memorytools.stats.long_idle"
+ "com.apple.trial.NamespaceUpdate.COREOS_VM_OBJECT_COPY_DELAYED_NO_WAIT"
+ "evaluation_count"
+ "initWithInteger:"
+ "initWithUnsignedInt:"
+ "kern.memorystatus.reaper_stats_sweep_count"
+ "kern.memorystatus.reaper_stats_total_freed_mb"
+ "kern.memorystatus.reaper_stats_total_kills"
+ "long_idle_kill_count"
+ "reclaimed_kb_per_eval"
+ "total_reclaimed_kb"
+ "vm.vm_object_copy_delayed_paging_wait_disable"
- "Failed to set %s with factor %s (%@) with errno %d"

```
