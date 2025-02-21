## fsck_exfat

> `/System/Library/Filesystems/exfat.fs/fsck_exfat`

```diff

-463.60.8.0.0
-  __TEXT.__text: 0x9090
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__cstring: 0x2771
-  __TEXT.__const: 0x219
-  __TEXT.__unwind_info: 0x1d0
-  __DATA_CONST.__auth_got: 0x278
+488.100.9.0.0
+  __TEXT.__text: 0x96c0
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__cstring: 0x29df
+  __TEXT.__const: 0x251
+  __TEXT.__unwind_info: 0x1c0
+  __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__const: 0x220
   __DATA_CONST.__cfstring: 0x60
-  __DATA.__data: 0x2380
+  __DATA.__data: 0x23d0
   __DATA.__bss: 0xec610
-  __DATA.__common: 0x160
+  __DATA.__common: 0x168
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   Functions: 165
-  Symbols:   94
-  CStrings:  318
+  Symbols:   100
+  CStrings:  346
 
Symbols:
+ _CFSetGetCount
+ _analytics_send_event_lazy
+ _clock_gettime_nsec_np
+ _kCFTypeSetCallBacks
+ _strcmp
+ _xpc_dictionary_create
+ _xpc_dictionary_set_uint64
- _kCFTypeDictionaryKeyCallBacks
CStrings:
+ "%s-%d"
+ "%s/shadow-%s"
+ "%s/shadow-fd-%d"
+ "/.Trashes"
+ "Tried to allocate space, but there are no available clusters."
+ "Tried to truncate cluster chain, but encountered a conflict."
+ "Usage: fsck_exfat [-d] [-f] [-p | -q | -y | -n] [-S directory] [-g | -x] device\n"
+ "^v8@?0"
+ "cluster_size"
+ "com.apple.filesystems.fsck_exfat_telemetry"
+ "fsck_duration_ms"
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
+ "trouble creating metadata shadow file at %s"
+ "volume_size"
+ "volume_space_used_percentage"
- "%s-%s"
- "%s-fd-%d"
- "Usage: fsck_exfat [-d] [-f] [-p | -q | -y | -n] [-S path_prefix] [-g | -x] device\n"
- "trouble creating metadata shadow file %s"

```
