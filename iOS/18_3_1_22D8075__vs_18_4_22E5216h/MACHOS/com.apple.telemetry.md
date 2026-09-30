## com.apple.telemetry

> `/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry`

```diff

-498.0.0.0.0
-  __TEXT.__text: 0x6ee0
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x529
-  __TEXT.__oslogstring: 0x3670
-  __TEXT.__unwind_info: 0xe8
-  __DATA.__auth_got: 0x220
-  __DATA.__got: 0x48
-  __DATA.__const: 0x300
-  __DATA.__cfstring: 0x60
+498.100.2.0.0
+  __TEXT.__text: 0x7e18
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_stubs: 0x300
+  __TEXT.__const: 0x150
+  __TEXT.__gcc_except_tab: 0x234
+  __TEXT.__cstring: 0x6e8
+  __TEXT.__oslogstring: 0x39f1
+  __TEXT.__objc_classname: 0x1
+  __TEXT.__objc_methname: 0x1dd
+  __TEXT.__unwind_info: 0x150
+  __DATA.__auth_got: 0x3a0
+  __DATA.__got: 0xb8
+  __DATA.__auth_ptr: 0x8
+  __DATA.__const: 0x278
+  __DATA.__cfstring: 0x300
+  __DATA.__objc_imageinfo: 0x8
+  __DATA.__objc_selrefs: 0xc0
+  __DATA.__objc_intobj: 0x18
   __DATA.__data: 0x8
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libdscsym.dylib
+  - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsystemstats.dylib
-  Functions: 101
-  Symbols:   82
-  CStrings:  164
+  - /usr/lib/libz.1.dylib
+  Functions: 145
+  Symbols:   146
+  CStrings:  239
 
Symbols:
+ _CFDictionaryGetValue
+ _CSArchitectureGetCurrent
+ _CSArchitectureGetFamilyName
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_SABinary
+ _OBJC_CLASS_$_SABinaryLoadInfo
+ __CFCopySupplementalVersionDictionary
+ __Unwind_Resume
+ ___chkstk_darwin
+ ___objc_personality_v0
+ ___udivti3
+ __kCFSystemVersionBuildVersionKey
+ __kCFSystemVersionProductNameKey
+ __kCFSystemVersionProductVersionExtraKey
+ __kCFSystemVersionProductVersionKey
+ __systemstats_writers
+ _asprintf
+ _dscsym_mmap_dscsym_for_uuid
+ _dyld_for_each_installed_shared_cache
+ _dyld_shared_cache_copy_uuid
+ _gzclose
+ _gzopen
+ _gzwrite
+ _kCFAbsoluteTimeIntervalSince1970
+ _mach_get_times
+ _mach_timebase_info
+ _munmap
+ _objc_alloc
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend
+ _objc_release
+ _objc_release_x1
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x8
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x8
+ _objc_storeStrong
+ _strerror
+ _sysctlbyname
+ _systemstats_zipper_buffers_foreach_micro
+ _uname
+ _uuid_unparse
+ _vm_page_size
- _os_release
- _systemstats_foreach_micro
CStrings:
+ " (needs following chunk)"
+ "%s/%s.%s.bootinfo%s"
+ "%u/%u"
+ "@\"NSObject<OS_xpc_object>\"8@?0"
+ "B40@?0r^{micro_snapshot=IIQQCS}8r^{task_snapshot=IiQQQ[16C]QIiiiiiIQQ[17c]IIIQQQQ[4Q][4Q]QQQQQQQQI}16r^{thread_snapshot=IIIQQQQQiiiiccccc[3c]QQQQ[4Q][4Q]QQQQQQQQQQ[64c]}24Q32"
+ "Lost %llu PMI microstackshots between %f-%f (%.9fs)"
+ "PMI %s microstackshot generation incremented unexpectedly %u -> %u, and settings are wrong! source:%d period:%llu, should be %llu"
+ "PMI %s microstackshot generation incremented unexpectedly %u -> %u, but settings are correct"
+ "PMI %s microstackshot generation:%u source:%u period:%llu samples_recorded:%llu samples_skipped:%llu time:%llu.%0llu"
+ "PMI %s microstackshot generation:%u source:%u period:%llu samples_recorded:%llu samples_skipped:%llu time:%llu.%0llu - duplicate"
+ "PMI %s microstackshot wrong interval %llu, should be %llu"
+ "PMI %s microstackshot wrong source %d"
+ "Saved %zu microstackshots (%zu:%zu user:kernel, %d:%d bytes) (ignored %d:%d known duplicates and %d:%d likely duplicates)"
+ "UUIDString"
+ "Unable to create kernel microstackshot buffer"
+ "Unable to create user microstackshot buffer"
+ "Unable to get hw.pagesize: %{errno}d"
+ "Unable to get kern.bootargs: %d %s"
+ "Unable to get load info"
+ "Unable to get vm.pagesize: %{errno}d"
+ "Unable to map dscsym: %{errno}d"
+ "Unable to open bootinfofile %s: %{errno}d"
+ "Unable to serialize boot info: %@"
+ "__microstackshot for kernel returned error %{errno}d}"
+ "__microstackshot for kernel returned invalid buffer of size: %d"
+ "__microstackshot for user returned error %{errno}d}"
+ "__microstackshot for user returned invalid buffer of size: %d"
+ "addObject:"
+ "binary"
+ "binaryLoadInfoForLiveProcessWithPid:dataGatheringOptions:additionalCSSymbolicatorFlags:mainBinaryOut:sharedCacheOut:"
+ "boot info size overflow: %lu"
+ "boot_args"
+ "bytes"
+ "clearCaches"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "dataWithPropertyList:format:options:error:"
+ "dscsym size overflow: %zu"
+ "exclave"
+ "hw.pagesize"
+ "hw_page_size"
+ "i"
+ "initWithCapacity:"
+ "initWithFormat:"
+ "initWithUTF8String:"
+ "initWithUUIDBytes:"
+ "kern.bootargs"
+ "kernel"
+ "kernel_version"
+ "length"
+ "loadAddress"
+ "load_address"
+ "load_info_entries"
+ "load_infos"
+ "mach_timebase"
+ "machine_arch"
+ "main_binary_uuid"
+ "name"
+ "non-PMI %s microstackshot 0x%x @ %llu.%0llu"
+ "non-PMI %s microstackshot 0x%x @ %llu.%0llu - known duplicate"
+ "non-PMI %s microstackshot 0x%x @ %llu.%0llu - likely duplicate"
+ "numberWithDouble:"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedLongLong:"
+ "os_build_version"
+ "os_product_name"
+ "os_product_version"
+ "os_product_version_extra"
+ "path"
+ "pid"
+ "segment"
+ "setObject:forKeyedSubscript:"
+ "unable to get kernel string"
+ "unable to get kernel string: %{errno}d"
+ "unable to get system versions dictionary"
+ "user"
+ "uuid"
+ "v16@?0^{dyld_shared_cache_s=}8"
+ "v16@?0^{micro_stats_s=QQQQ}8"
+ "vm.pagesize"
+ "vm_page_size"
+ "walltime"
+ "wrote %lu boot info chunk %s"
+ "wrote %lu dscsym info chunk%s"
+ "wrote backwards compatibility chunk"
+ "wxb"
- "B40@?0^{micro_snapshot=IIQQCS}8^{task_snapshot=IiQQQ[16C]QIiiiiiIQQ[17c]IIIQQQQ[4Q][4Q]QQQQQQQQI}16^{thread_snapshot=IIIQQQQQiiiiccccc[3c]QQQQ[4Q][4Q]QQQQQQQQQQ[64c]}24Q32"
- "Lost %llu PMI microstackshots"
- "PMI microstackshot generation:%u source:%u period:%llu samples_recorded:%llu samples_skipped:%llu"
- "PMI microstackshot generation:%u source:%u period:%llu samples_recorded:%llu samples_skipped:%llu - duplicate"
- "Saved %zu microstackshots (ignored %d known duplicates and %d likely duplicates)"
- "Unable to create microstackshot buffer"
- "Wrong microstackshot interval %llu, should be %llu"
- "Wrong microstackshot source %d"
- "^v8@?0"
- "__microstackshot returned invalid buffer of size: %d"
- "generation incremented unexpectedly %u -> %u, and settings are wrong! source:%d period:%llu, should be %llu"
- "generation incremented unexpectedly %u -> %u, but settings are correct"
- "non-PMI microstackshot 0x%x @ %llu.%0llu"
- "non-PMI microstackshot 0x%x @ %llu.%0llu - known duplicate"
- "non-PMI microstackshot 0x%x @ %llu.%0llu - likely duplicate"

```
