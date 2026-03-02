## libCoreFSCache.dylib

> `/System/Library/Frameworks/OpenGLES.framework/libCoreFSCache.dylib`

```diff

-351.1.0.0.0
-  __TEXT.__text: 0x5850
-  __TEXT.__auth_stubs: 0x310
+352.0.0.0.0
+  __TEXT.__text: 0x5dec
+  __TEXT.__auth_stubs: 0x350
   __TEXT.__const: 0xb0
   __TEXT.__cstring: 0x29a
-  __TEXT.__oslogstring: 0xae0
-  __TEXT.__unwind_info: 0x138
+  __TEXT.__oslogstring: 0xb9a
+  __TEXT.__unwind_info: 0x140
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x58
-  __AUTH_CONST.__auth_got: 0x188
+  __AUTH_CONST.__auth_got: 0x1a8
   __AUTH_CONST.__const: 0x30
   __AUTH_CONST.__cfstring: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 124D4B2A-3DAC-379A-83C1-91A09A1FC0C7
+  UUID: 37B8DF0F-EEC0-3292-908E-1AE94F35FFEA
   Functions: 122
-  Symbols:   289
-  CStrings:  79
+  Symbols:   293
+  CStrings:  84
 
Symbols:
+ __os_log_impl
+ _mach_absolute_time
+ _mach_timebase_info
+ _open_data_file.cold.6
+ _usleep
- _fscache_open_worker.cold.19
CStrings:
+ "@ %s(): fscache_element_get_data() failed with error = %d"
+ "@ %s(): msync() failed with errno = %d"
+ "Bad key_size in attributes!"
+ "Bad version in attributes!"
+ "Edits file is corrupted."
+ "Edits file is corrupted. Element index invalid."
+ "Edits file is corrupted. Element key mismatch."
+ "Edits file is corrupted. Unknown edit type."
+ "FSCache (is_data_file_invalid): file descriptor points to %s"
+ "FSCache (is_data_file_invalid): fstat failed on data file with errno = %d"
+ "FSCache: Error deleting tmp list file. Disabling cache updates."
+ "FSCache: Error opening tmp list file. Disabling cache updates."
+ "FSCache: Error renaming list file. Disabling cache updates."
+ "FSCache: Error writing edit. Disabling cache updates."
+ "FSCache: Error writing updated list file. Disabling cache updates."
+ "FSCache: file descriptor points to %s"
+ "FSCache: invalid element offset %li when map size is %li"
+ "FSCache: num_elems in maps is %d"
+ "FSCache: num_elems in maps is %d but map size only allows for %lu elements"
+ "Invalidating cache"
+ "cvms: fsetattrlist failed to set protection class %u for data file: errno = %d (%s)"
+ "failed to add file guard. errno = %d"
+ "failed to create a bigger file, errno = %d"
+ "failed to remove file guard. errno = %d"
+ "fclose failed for data file: errno = %d"
+ "fclose failed for list file: errno = %d"
+ "fflush failed for list file: errno = %d"
+ "flock failed for data file on first attempt (will retry)"
+ "flock failed for data file: errno = %d"
+ "flock failed to lock list file (%s): errno = %d"
+ "flock failed to unlock data file: errno = %d"
+ "flock failed to unlock list file: errno = %d"
+ "flock unexpectedly failed with EAGAIN %u times for data file over %u ms"
+ "fopen failed for data file: errno = %d (%s)"
+ "fopen failed for list file: errno = %d"
+ "fsetxattr failed to set com.apple.runningboard.can-suspend-locked on the data file (%s): errno = %d"
+ "fsetxattr failed to set com.apple.runningboard.can-suspend-locked on the list file (%s): errno = %d"
+ "ftruncate failed for list file: errno = %d"
+ "fwrite failed for list file, errno = %d"
+ "list file already locked (%s)"
+ "mmap failed for heap: errno = %d"
+ "munmap failed for heap: errno = %d"
+ "reset_cache(): failed to get file path for data_file. errno = %d (%s)"
+ "reset_cache(): failed to get file path for list_file. errno = %d (%s)"
+ "reset_cache(): fscache_open failed with %d (%s)"
- "@ %s(): fscache_element_get_data() failed with error = %d\n"
- "@ %s(): msync() failed with errno = %d\n"
- "Bad key_size in attributes!\n"
- "Bad version in attributes!\n"
- "Edits file is corrupted.\n"
- "Edits file is corrupted. Element index invalid.\n"
- "Edits file is corrupted. Element key mismatch.\n"
- "Edits file is corrupted. Unknown edit type.\n"
- "Errors found! Invalidating cache...\n"
- "FSCache (is_data_file_invalid): file descriptor points to %s\n"
- "FSCache (is_data_file_invalid): fstat failed on data file with errno = %d\n"
- "FSCache: Error deleting tmp list file. Disabling cache updates.\n"
- "FSCache: Error opening tmp list file. Disabling cache updates.\n"
- "FSCache: Error renaming list file. Disabling cache updates.\n"
- "FSCache: Error writing edit. Disabling cache updates.\n"
- "FSCache: Error writing updated list file. Disabling cache updates.\n"
- "FSCache: file descriptor points to %s\n"
- "FSCache: invalid element offset %li when map size is %li\n"
- "FSCache: num_elems in maps is %d\n"
- "FSCache: num_elems in maps is %d but map size only allows for %lu elements\n"
- "cvms: fsetattrlist failed to set protection class %u for data file: errno = %d (%s)\n"
- "failed to create a bigger file, errno = %d\n"
- "fclose failed for data file: errno = %d\n"
- "fclose failed for list file: errno = %d\n"
- "fflush failed for list file: errno = %d\n"
- "flock failed for data file: errno = %d (%s)\n"
- "flock failed to lock list file (%s): errno = %d\n"
- "flock failed to unlock data file: errno = %d\n"
- "flock failed to unlock list file: errno = %d\n"
- "fopen failed for data file: errno = %d (%s)\n"
- "fopen failed for list file: errno = %d\n"
- "fsetxattr failed to set com.apple.runningboard.can-suspend-locked on the data file (%s): errno = %d\n"
- "fsetxattr failed to set com.apple.runningboard.can-suspend-locked on the list file (%s): errno = %d\n"
- "ftruncate failed for list file: errno = %d\n"
- "fwrite failed for list file\n"
- "mmap failed for heap: errno = %d\n"
- "munmap failed for heap: errno = %d\n"
- "reset_cache(): failed to get file path for data_file. errno = %d (%s)\n"
- "reset_cache(): failed to get file path for list_file. errno = %d (%s)\n"
- "reset_cache(): fscache_open failed with %d (%s)\n"

```
