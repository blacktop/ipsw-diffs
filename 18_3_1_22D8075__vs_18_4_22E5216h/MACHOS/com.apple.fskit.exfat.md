## com.apple.fskit.exfat

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.exfat.appex/com.apple.fskit.exfat`

```diff

-463.60.8.0.0
-  __TEXT.__text: 0xe354
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_stubs: 0x760
-  __TEXT.__objc_methlist: 0x98
-  __TEXT.__const: 0x4ca3
-  __TEXT.__cstring: 0x2e2d
-  __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__objc_methname: 0x789
-  __TEXT.__oslogstring: 0x531
-  __TEXT.__objc_classname: 0x77
-  __TEXT.__objc_methtype: 0x2e0
-  __TEXT.__unwind_info: 0x270
-  __DATA_CONST.__auth_got: 0x448
+488.100.10.0.0
+  __TEXT.__text: 0xe8bc
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_stubs: 0x7c0
+  __TEXT.__objc_methlist: 0x204
+  __TEXT.__const: 0x4cdb
+  __TEXT.__cstring: 0x303f
+  __TEXT.__gcc_except_tab: 0x150
+  __TEXT.__objc_methname: 0x79a
+  __TEXT.__oslogstring: 0x51a
+  __TEXT.__objc_classname: 0x5f
+  __TEXT.__objc_methtype: 0x328
+  __TEXT.__unwind_info: 0x278
+  __DATA_CONST.__auth_got: 0x468
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x180
-  __DATA_CONST.__cfstring: 0x4c0
+  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__cfstring: 0x4e0
   __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x4e0
-  __DATA.__objc_selrefs: 0x218
+  __DATA.__objc_const: 0x240
+  __DATA.__objc_selrefs: 0x2c8
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x3d70
+  __DATA.__data: 0x3d60
   __DATA.__bss: 0xec610
-  __DATA.__common: 0x1c8
+  __DATA.__common: 0x1d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   Functions: 237
-  Symbols:   320
-  CStrings:  499
+  Symbols:   326
+  CStrings:  526
 
Symbols:
+ _CFSetGetCount
+ _OBJC_CLASS_$_FSContainerStatus
+ _analytics_send_event_lazy
+ _clock_gettime_nsec_np
+ _fsck_exfat_send_telemetry_event
+ _fsck_exfat_telemetry_filename_length
+ _fsck_exfat_telemetry_num_files_in_dir
+ _kCFTypeSetCallBacks
+ _strcmp
+ _xpc_dictionary_create
+ _xpc_dictionary_set_uint64
- _CFStringGetNameHash
- _OBJC_CLASS_$_NSMutableIndexSet
- _kCFTypeDictionaryKeyCallBacks
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
CStrings:
+ "-f"
+ "/.Trashes"
+ "@\"NSProgress\"40@0:8@\"FSTask\"16@\"FSTaskOptions\"24^@32"
+ "Tried to allocate space, but there are no available clusters."
+ "Tried to truncate cluster chain, but encountered a conflict."
+ "^v8@?0"
+ "cluster_size"
+ "com.apple.filesystems.fsck_exfat_telemetry"
+ "containsString:"
+ "fsck_duration_ms"
+ "notReadyWithStatus:"
+ "notRecognizedProbeResult"
+ "num_appledouble_files"
+ "num_bitmap_bits_bad"
+ "num_bitmap_bits_cleared"
+ "num_bitmap_bits_set"
+ "num_bitmap_collisions"
+ "num_dirs_in_volume"
+ "num_duplicated_filenames"
+ "num_files_in_trashes"
+ "num_files_in_volume"
+ "num_huge_dirs"
+ "num_invalid_filenames"
+ "num_large_dirs"
+ "num_long_filenames"
+ "num_medium_dirs"
+ "num_medium_filenames"
+ "num_short_filenames"
+ "num_small_dirs"
+ "sector_size"
+ "setContainerStatus:"
+ "startCheckWithTask:options:error:"
+ "startFormatWithTask:options:error:"
+ "taskOptions"
+ "usableProbeResultWithName:containerID:"
+ "v40@0:8@\"FSResource\"16@\"FSTaskOptions\"24@?<v@?@\"FSVolume\"@\"NSError\">32"
+ "v40@0:8@\"FSResource\"16@\"FSTaskOptions\"24@?<v@?@\"NSError\">32"
+ "volume_size"
+ "volume_space_used_percentage"
+ "wipeResource:completionHandler:"
- "%s: Finished launching"
- "-[exfatFileSystem didFinishLaunching]"
- "-[exfatFileSystem didFinishLoading]"
- "@\"NSProgress\"40@0:8@\"FSTask\"16@\"NSArray\"24^@32"
- "FSBlockDeviceOperations"
- "addIndexesInRange:"
- "didFinishLaunching"
- "indexSet"
- "resultWithResult:name:containerID:"
- "startCheckWithTask:parameters:error:"
- "startFormatWithTask:parameters:error:"
- "v40@0:8@\"FSResource\"16@\"NSArray\"24@?<v@?@\"FSVolume\"@\"NSError\">32"
- "wipeResource:includingRanges:excludingRanges:replyHandler:"

```
