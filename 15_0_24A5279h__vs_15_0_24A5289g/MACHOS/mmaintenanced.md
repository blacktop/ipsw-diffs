## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-152.0.0.0.0
-  __TEXT.__text: 0x3fb0
-  __TEXT.__auth_stubs: 0x610
+154.0.0.0.0
+  __TEXT.__text: 0x11464
+  __TEXT.__auth_stubs: 0xa20
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0xc60
-  __TEXT.__oslogstring: 0x8c2
-  __TEXT.__cstring: 0x93f
-  __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0x160
-  __DATA_CONST.__auth_got: 0x310
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x178
+  __TEXT.__const: 0x112a
+  __TEXT.__oslogstring: 0xcd3
+  __TEXT.__cstring: 0xbb5
+  __TEXT.__gcc_except_tab: 0x53c
+  __TEXT.__swift5_typeref: 0x23
+  __TEXT.__swift5_capture: 0x38
+  __TEXT.__unwind_info: 0x638
+  __TEXT.__eh_frame: 0xf0
+  __DATA_CONST.__auth_got: 0x518
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0x9d0
   __DATA_CONST.__cfstring: 0x20
-  __DATA.__data: 0xe28
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA.__data: 0xe58
   __DATA.__common: 0x19
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication
   - /System/Library/PrivateFrameworks/KRExperiments.framework/Versions/A/KRExperiments
+  - /System/Library/PrivateFrameworks/ModelManagerServices.framework/Versions/A/ModelManagerServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
+  - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 93
-  Symbols:   157
-  CStrings:  134
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 371
+  Symbols:   244
+  CStrings:  150
 
Symbols:
+ _$s20ModelManagerServices5QueryV12loadedAssetsSayAA9AssetInfoVGvg
+ _$s20ModelManagerServices5QueryV12loadedAssetsSayAA9AssetInfoVGvgTu
+ _$s20ModelManagerServices5QueryVACycfC
+ _$s20ModelManagerServices5QueryVMa
+ _$s2os6LoggerV9logObjectSo03OS_a1_C0Cvg
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _$s2os6LoggerVMa
+ _$sScA15unownedExecutorScevgTj
+ _$sScP8rawValues5UInt8Vvg
+ _$sScPMa
+ _$sSo13os_log_type_ta0A0E5errorABvgZ
+ _$sytN
+ _CFArrayCreate
+ _CFDictionaryContainsKey
+ _CFNumberGetValue
+ __Block_copy
+ __Block_object_assign
+ __Block_object_dispose
+ __Block_release
+ __ZNKSt3__123__match_any_but_newlineIcE6__execERNS_7__stateIcEE
+ __ZNKSt3__16locale4nameEv
+ __ZNSt3__111regex_errorC1ENS_15regex_constants10error_typeE
+ __ZNSt3__111regex_errorD1Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
+ __ZNSt3__115__get_classnameEPKcb
+ __ZNSt3__119__shared_weak_count14__release_weakEv
+ __ZNSt3__119__shared_weak_countD2Ev
+ __ZNSt3__120__get_collation_nameEPKc
+ __ZNSt3__16localeC1ERKS0_
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__17collateIcE2idE
+ __ZTINSt3__111regex_errorE
+ __ZTINSt3__119__shared_weak_countE
+ __ZTVN10__cxxabiv117__class_type_infoE
+ __ZTVN10__cxxabiv120__si_class_type_infoE
+ __ZdlPvSt19__type_descriptor_t
+ __ZnwmSt19__type_descriptor_t
+ ___chkstk_darwin
+ __os_log_debug_impl
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftos
+ _close
+ _dispatch_release
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _gettimeofday
+ _kCFTypeArrayCallBacks
+ _malloc_type_malloc
+ _memchr
+ _memcmp
+ _memmove
+ _objc_release
+ _os_fault_with_payload
+ _sleep
+ _stat
+ _strcasestr
+ _strerror
+ _strlen
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_deallocObject
+ _swift_errorRelease
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_release
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _sysctl
+ _terminate_with_reason
+ _utimes
+ _xpc_dictionary_set_int64
- _host_get_special_port
CStrings:
+ "/private/var/mobile/Library/MemoryMaintenance/ane_abandonment"
+ "ANE memory abandonment not resolved by killing modelmanagerd, system memory reset likely"
+ "Memory Maintenance kill: ANE memory abandonment"
+ "ModelManagerServices"
+ "basic_string"
+ "com.apple.driver.AppleH[0-9]+ANEInterface[.DMA]*.ane[0-9]*"
+ "com.apple.memory-maintenance.ane-abandonment-check"
+ "com.apple.memorytools.stats.ane_abandonment"
+ "ended_in_maintenance_error"
+ "final_memory_usage_over_threshold"
+ "kill_resolved_abandonment"
+ "killed_modelmanagerd"
+ "memory abandonment in ane driver detected, killing modelmanagerd"
+ "memory_usage_over_threshold"
+ "modelmanagerd"
+ "v12@?0i8"

```
