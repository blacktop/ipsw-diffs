## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x56d90
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__const: 0x8100
-  __TEXT.__cstring: 0xee3e
-  __TEXT.__oslogstring: 0xf17
+2332.101.1.0.0
+  __TEXT.__text: 0x57200
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__const: 0x8120
+  __TEXT.__cstring: 0xef00
+  __TEXT.__oslogstring: 0x1087
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0xa30
+  __TEXT.__unwind_info: 0xa20
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x500
-  __AUTH_CONST.__auth_got: 0x648
+  __AUTH_CONST.__auth_got: 0x680
   __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__cfstring: 0x1360
-  __AUTH.__data: 0x148
+  __AUTH.__data: 0x168
   __DATA.__data: 0xb8
   __DATA.__bss: 0x60
   __DATA.__common: 0x428

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: D1F696F1-1BAF-3D69-9A92-8B0521CA2120
-  Functions: 888
-  Symbols:   1184
-  CStrings:  1572
+  UUID: 11152D8E-297B-34BC-A6C5-0417EBF5A976
+  Functions: 883
+  Symbols:   1202
+  CStrings:  1587
 
Symbols:
+ APFSGetExclavePath.cold.1
+ APFSGetExclavePath.cold.2
+ APFSGetExclavePath.cold.3
+ APFSGetExclavePath.cold.4
+ APFSGetExclavePath.cold.5
+ APFSVolumeGeneratePersonalRecoveryKey.cold.1
+ _APFSGetExclavePath
+ _authapfs_digest
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
+ _fd_dev_hint
+ _fd_dev_hint_flush
+ _io_container_is_external
+ _nx_unmount_internal
+ _os_parse_boot_arg_string
+ _spaceman_alloc_flags_to_devs
+ _spaceman_alloc_iterate_chunks
+ _spaceman_check_available_space
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
CStrings:
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n"
+ "%s:%d: failed to allocate memory for exclave base dirs (%d base dirs were requested)"
+ "%s:%d: failed to get exclave base dirs (number of records), error %d (%s)"
+ "%s:%d: failed to get exclave base dirs after retries"
+ "%s:%d: failed to get exclave base dirs, error %d (%s)"
+ "%s:%d: fsctl failed with ENOSPC, retrying..."
+ "%s:%d: fsgetpath failed for base_dir %llu, error %d (%s)"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "-apfs_newvf_enabled"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apfs_framework/nx/fusion_mt.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apfs_framework/nx/obj.c"
+ "2332.101.1"
+ "APFSGetExclavePath"
+ "fd_dev_hint_flush"
+ "sha3_256"
+ "sha3_256_4k"
+ "sha3_384"
+ "sha3_384_4k"
+ "sha3_512"
+ "sha3_512_4k"
+ "spaceman_alloc_iterate_chunks"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "-"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_framework/nx/fusion_mt.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_framework/nx/obj.c"
- "2317.81.2"
- "no"

```
