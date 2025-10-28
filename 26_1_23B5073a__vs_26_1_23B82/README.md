# 26.1 (23B5073a) .vs 26.1 (23B82)

## IPSWs

- `iPhone18,1_26.1_23B5073a_Restore.ipsw`
- `iPhone18,1_26.1_23B82_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.1 *(23B5073a)* | 25.1.0 | 12377.42.6~13 | Thu, 16Oct2025 23:19:04 PDT |
| 26.1 *(23B82)* | 25.1.0 | 12377.42.6~55 | Thu, 23Oct2025 11:12:58 PDT |

### Kexts

#### ❌ Removed (1)

- `com.apple.kec.AppleEncryptedArchive`

### ⬆️ Updated (8)

<details>
  <summary><i>View Updated</i></summary>

#### com.apple.driver.AppleAOPAudio

>  `com.apple.driver.AppleAOPAudio`

```diff

   __TEXT.__cstring: 0xc591
   __TEXT.__const: 0x136
   __TEXT.__os_log: 0xf
-  __TEXT_EXEC.__text: 0x31c90
+  __TEXT_EXEC.__text: 0x31ca4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2f0
   __DATA.__common: 0x660
   __DATA.__bss: 0x49
-  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0xe8
   __DATA_CONST.__mod_term_func: 0xe0
   __DATA_CONST.__const: 0xb7c8
   __DATA_CONST.__kalloc_type: 0xa00
-  UUID: B7AC5ACF-97AE-3F9C-A9F7-5E8E97557019
+  UUID: A1BB3862-BC7A-33AD-852C-CDC2C54D9276
   Functions: 1223
   Symbols:   0
   CStrings:  1152
Functions:
~ sub_fffffe0008caa814 -> sub_fffffe0008c9a814 : 508 -> 528
CStrings:
+ "06:29:54"
+ "06:30:00"
+ "Oct 23 2025"
- "22:48:55"
- "22:49:01"
- "Oct 16 2025"

```

#### com.apple.driver.AppleAVE2

>  `com.apple.driver.AppleAVE2`

```diff

-905.5.1.0.0
+905.5.3.0.0
   __TEXT.__const: 0x426a0
-  __TEXT.__cstring: 0x400f2
-  __TEXT.__os_log: 0x51fbe
-  __TEXT_EXEC.__text: 0x19f90c
+  __TEXT.__cstring: 0x400f8
+  __TEXT.__os_log: 0x51fc4
+  __TEXT_EXEC.__text: 0x19f8cc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b8
   __DATA.__common: 0x130

   __DATA_CONST.__const: 0x8b60
   __DATA_CONST.__kalloc_type: 0x4900
   __DATA_CONST.__kalloc_var: 0x2030
-  UUID: 2D336D84-CE07-3F3F-8626-13B5550F7120
+  UUID: 00AA50D8-F1F9-3272-8A18-E6C4C8B5247E
   Functions: 2768
   Symbols:   0
   CStrings:  8954
Functions:
~ sub_fffffe0008dd7834 -> sub_fffffe0008dc7884 : 376 -> 360
~ sub_fffffe0008de4bc8 -> sub_fffffe0008dd4c08 : 156 -> 148
~ sub_fffffe0008e2388c -> sub_fffffe0008e138c4 : 968 -> 964
~ sub_fffffe0008e7de90 -> sub_fffffe0008e6dec4 : 2256 -> 2232
~ sub_fffffe0008f2e078 -> sub_fffffe0008f1e094 : 2668 -> 2664
~ sub_fffffe0008f5927c -> sub_fffffe0008f49294 : 52 -> 44
CStrings:
+ "%lld %d AVE %s: %s::%s:%d %s | Invalid qpAndForceIntraAddress_ %p BitDepthMinus8:%u userSliceQP:%d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | Invalid qpAndForceIntraAddress_ %p BitDepthMinus8:%u userSliceQP:%d\n\n"
+ "06:38:36"
+ "905.5.3"
+ "Oct 23 2025"
- "%lld %d AVE %s: %s:%d %s | Null qpAndForceIntraAddress_ | %p BitDepthMinus8:%u userSliceQP:%d"
- "%lld %d AVE %s: %s:%d %s | Null qpAndForceIntraAddress_ | %p BitDepthMinus8:%u userSliceQP:%d\n"
- "23:00:42"
- "905.5.1"
- "Oct 16 2025"

```

#### com.apple.driver.IOPAudioVoiceTriggerDevice

>  `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

 500.14.0.0.0
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x2d80
+  __TEXT.__cstring: 0x2d89
   __TEXT.__os_log: 0x1726
   __TEXT_EXEC.__text: 0xb108
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1750
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: 5573299E-8ED9-38B6-907C-84DF97921491
+  UUID: 59799752-935B-367E-90C9-AB00EFE5940D
   Functions: 260
   Symbols:   0
-  CStrings:  235
+  CStrings:  236
 
CStrings:
+ "06:40:37"
+ "06:40:38"
+ "Oct 23 2025"
- "23:05:48"
- "Oct 16 2025"

```

#### com.apple.driver.corecapture

>  `com.apple.driver.corecapture`

```diff

   __TEXT.__os_log: 0x421d
   __TEXT.__const: 0x130
   __TEXT.__cstring: 0x202e
-  __TEXT_EXEC.__text: 0x28bf0
+  __TEXT_EXEC.__text: 0x28c00
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x308

   __DATA_CONST.__const: 0x7008
   __DATA_CONST.__kalloc_type: 0x10c0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: CC0723EE-FC5C-3665-AE78-9AE3A525EC0C
+  UUID: 27E8C1F9-4AAF-333E-8A81-34AE8B111499
   Functions: 874
   Symbols:   0
   CStrings:  654
Functions:
~ sub_fffffe000afd504c -> sub_fffffe000afc358c : 100 -> 116

```

#### com.apple.filesystems.apfs

>  `com.apple.filesystems.apfs`

```diff

   __TEXT.__cstring: 0x4c5a6
   __TEXT_EXEC.__text: 0x159c1c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x640
-  __DATA.__bss: 0xcb0
+  __DATA.__data: 0x638
+  __DATA.__bss: 0xcb8
   __DATA_CONST.__auth_got: 0x1158
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__kalloc_type: 0x4f00
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: D441E6EA-8360-3B88-B473-5BE366E09FF0
+  UUID: C651EE58-C58C-348D-9B1C-E9439A3823BD
   Functions: 2320
   Symbols:   0
   CStrings:  6589
CStrings:
+ "06:31:07"
+ "2025/10/23"
+ "Oct 23 2025"
- "2025/10/16"
- "22:50:27"
- "Oct 16 2025"

```

#### com.apple.iokit.AppleARMIISAudio

>  `com.apple.iokit.AppleARMIISAudio`

```diff

   __TEXT.__os_log: 0x2862
   __TEXT.__cstring: 0x2e47
   __TEXT.__const: 0xc8
-  __TEXT_EXEC.__text: 0x1673c
+  __TEXT_EXEC.__text: 0x1676c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__const: 0x1150
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: 4F4BAFEC-ACBA-33E3-9AB8-4ED2FDD07E1D
-  Functions: 298
+  UUID: F0B129C9-A234-3B65-9745-C339A9CD08A8
+  Functions: 299
   Symbols:   0
   CStrings:  389
 

```

#### com.apple.kernel

>  `com.apple.kernel`

```diff

 12377.42.6.0.0
-  __TEXT.__const: 0x35180
+  __TEXT.__const: 0x350d0
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x800c4
+  __TEXT.__cstring: 0x7c876
   __TEXT.__os_log: 0x3c58f
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0x117410
+  __DATA_CONST.__const: 0x1173a0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x141c0
+  __DATA_CONST.__kalloc_type: 0x13f00
   __DATA_CONST.__assert: 0x8fc
   __DATA_CONST.__kalloc_var: 0x7b20
   __DATA_CONST.__exclaves_bt: 0x78
-  __DATA_CONST.__kern_brk_desc: 0x78
+  __DATA_CONST.__kern_brk_desc: 0x60
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x8b1f74
+  __TEXT_EXEC.__text: 0x89f8d4
   __TEXT_EXEC.__hib_text: 0xf38
   __TEXT_BOOT_EXEC.__bootcode: 0x51d0
   __KLD.__text: 0x1638

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x34c0
+  __KLDDATA.__const: 0x3490
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x17f79
-  __DATA.__lock_grp: 0x5bc8
+  __DATA.__lock_grp: 0x5b18
   __DATA.__percpu: 0x6f28
-  __DATA.__common: 0x6ec38
+  __DATA.__common: 0x6e998
   __DATA.__bss: 0x97228
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__static_if: 0x4d30
-  __BOOTDATA.__init_entry_set: 0x12810
+  __BOOTDATA.__static_if: 0x4c70
+  __BOOTDATA.__init_entry_set: 0x12768
   __BOOTDATA.__init: 0x5b3b0
   __BOOTDATA.__static_ifinit: 0x8
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x471ae
-  UUID: 7BA91819-48D7-3E88-B51D-79B76E9A0A4B
-  Functions: 20750
+  UUID: 774E10DF-25BC-3F8A-8221-A694CD8F84C9
+  Functions: 20547
   Symbols:   0
-  CStrings:  20261
+  CStrings:  19961
 
CStrings:
+ "ucoredump"
- "\n(kern_coredump_routine) : kern_dump_record_file failed with %d\n"
- "\nBeginning coredump of %s\n"
- "\nBeginning dump of panic region of size 0x%zx\n"
- "\nCore dump took %llu cycles\n"
- " Compressed file length is %llu bytes\n"
- "%"
- "%.12s-cp"
- "%lld..\n"
- "%lu"
- "%qx:%x"
- "%s (during forwarding) returned 0x%x\n"
- "%s (passing along request) returned 0x%x\n"
- "%s kvtophys() for address %p returned NULL\n"
- "%s next stage output failed\n"
- "%s%c%s%c%s%c"
- "%s(%p, %llu, %p) : called with invalid length %llu\n"
- "%s(%p, %llu, %p) : called with too much data, %llu written, %llu left\n"
- "%s() : failed to reset the out vars : kdp_reset_output_vars(%p, %llu, true, %p) returned error 0x%x\n"
- "%s() : failed to write data (%llu bytes remaining) :%d\n"
- "%s() : failed to write legacy bin spec version : coredump_save_note_data() returned 0x%x\n"
- "%s() : failed to write mach header : kdp_core_output(%p, %lu, %p) returned error 0x%x\n"
- "%s() : failed to write main bin spec structure : coredump_save_note_data() returned 0x%x\n"
- "%s() : failed to write note %llu of %llu : kdp_core_output() returned  error 0x%x\n"
- "%s() : failed to write sw_vers string : coredump_save_note_data() returned 0x%x\n"
- "%s() : failed to write thread data : kdp_core_output() returned 0x%x\n"
- "%s() : failed to write zero fill padding : kdp_core_output(%p, %llu, NULL) returned 0x%x\n"
- "%s() : found %d expected LC_THREAD (%d)\n"
- "%s() : ran out of space to save threads with %llu of %llu remaining\n"
- "%s() called too many times, %llu note descriptions already recorded\n"
- "%s() called with invalid data_owner\n"
- "%s(): encountered unknown debug header entry %d, including anyway with name '%s'\n"
- "%s(): failed to write load binary spec structure for binary #%d ('%s'): callback returned 0x%x\n"
- "%s(0x%llx, 0x%llx, %p) : called with invalid addresses : start 0x%llx >= end 0x%llx\n"
- "%s(0x%llx, 0x%llx, %p) : called with invalid addresses for 32-bit : start 0x%llx, end 0x%llx\n"
- "%s(0x%llx, 0x%llx, %p) : coredump_save_segment_descriptions() called too many times, %llu segment descriptions already recorded\n"
- "%s(0x%llx, 0x%llx, %p) : failed to write segment %llu of %llu : kdp_core_output(%p, %lu, %p) returned  error 0x%x\n"
- "%s(0x%llx, 0x%llx, %p) : failed to write segment %llu of %llu. kdp_core_output(%p, %lu, %p) returned error %d\n"
- "%s(0x%llx, 0x%llx, %p) : ran out of space to save commands with %llu of %llu remaining\n"
- "%s-%s-%u.%u.%u.%u-%x%s"
- "%s/%s"
- "%s: Detected remote error, terminating...\n"
- "%s: Detected remote side error (state %d, waiting %d)\n"
- "%s: Detected stale/invalid seq num (state %d, waiting %d). Expected: %d, received %d\n"
- "%s: Detected stale/invalid seq num. Expected: %d, received %d\n"
- "%s: Timed out waiting for the reply (state %d, waiting %d)\n"
- "%s: cannot exclude region starting at %p with size %zu (not page aligned) @%s:%d"
- "%s: cannot exclude region starting at %p with size %zu (zero or overflowing size) @%s:%d"
- "%s: context allocation failure\n"
- "%s: no ACK from remote side: %d\n"
- "%s: no task is set\n"
- "%s: remote is not done: %d\n"
- "%s: skipping inactive task\n"
- "%s: skipping kernel because excluded regions list is locked\n"
- "%s: skipping locked task\n"
- "%s: skipping task with locked vm map\n"
- "%s: vm map traversal failed: %d\n"
- "(%s) : coredump_init failed with %d\n"
- "(%s) : coredump_save_note_description returned %d while writing binary info LC_NOTE description"
- "(%s) : get_summary failed with %d\n"
- "(%s) : header size not populated after coredump_get_summary\n"
- "(%s) : kcc_coredump_save_note_data failed with 0x%x\n"
- "(%s) : kcc_coredump_save_note_data returned without all note data written, %llu of %llu remaining\n"
- "(%s) : kcc_coredump_save_note_descriptions failed with %d\n"
- "(%s) : kcc_coredump_save_sw_vers failed with 0x%x\n"
- "(%s) : kcc_coredump_save_sw_vers_detail_cb failed with 0x%x\n"
- "(%s) : save_note_descriptions returned without all note descriptions written, %llu of %llu remaining\n"
- "(%s) : save_note_note_summary failed with %d\n"
- "(%s) : save_segment_descriptions failed with %d\n"
- "(%s) : save_segment_descriptions returned without all segment descriptions written, %llu of %llu remaining\n"
- "(%s) : save_thread_state failed with %d\n"
- "(%s) : save_thread_state returned without all thread descriptions written, %llu of %llu remaining\n"
- "(%s) compression_stream_process failed\n"
- "(%s) lz4_stage_stream failed with error 0x%x\n"
- "(%s) next stage output failed with error 0x%x\n"
- "(%s) shmem_dbg_get_buffer failed with error 0x%x\n"
- "(%s) shmem_dbg_process_buffers failed with error 0x%x\n"
- "(%s) zlib_stream_output_chunk failed with error 0x%x\n"
- "(aea_read_callback) next stage read proc returned 0x%x\n"
- "(aea_stage_outproc) aea_close() returned %d\n"
- "(aea_stage_outproc) aea_open() returned %d\n"
- "(aea_stage_outproc) aea_write() returned %zd\n"
- "(aea_stage_reset) aea_close() returned %d\n"
- "(aea_write_callback) next stage outproc returned 0x%x\n"
- "(disk_stage_read) IOPolledFileRead(%llu) returned 0x%x\n"
- "(disk_stage_read) IOPolledFileSeek(0x%llx) returned 0x%x\n"
- "(disk_stage_read) IOPolledFileWrite (during seek) returned 0x%x\n"
- "(disk_stage_read) Kickstarting IOPolledFileRead(0) returned 0x%x\n"
- "(disk_stage_write) IOPolledFileSeek(0x%llx) returned 0x%x\n"
- "(disk_stage_write) IOPolledFileWrite (during final flush) returned 0x%x\n"
- "(disk_stage_write) IOPolledFileWrite(gIOPolledCoreFileVars, %p, 0x%llx, NULL) returned 0x%x\n"
- "(disk_stage_write) disk_stage_read (during final chunk seek) returned 0x%x\n"
- "(disk_stage_write) disk_stage_read (during seek) returned 0x%x\n"
- "(do_kern_dump close) outproc(KDP_EOF, NULL, 0, 0) returned 0x%x\n"
- "(do_kern_dump coredump log) outproc(KDP_DATA, NULL, %lu, %p) returned 0x%x\n"
- "(do_kern_dump paniclog) outproc(KDP_DATA, NULL, %lu, %p) returned 0x%x\n"
- "(do_kern_dump seek begin) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(do_kern_dump seek logfile) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(do_kern_dump write public key) returned 0x%x\n"
- "(kdp_core_output) outproc(KDP_DATA, NULL, 0x%llx, %p) returned 0x%x\n"
- "(kdp_reset_output_vars) Encryption requested, is unavailable, and enforcement is active. Skipping current core.\n"
- "(kern_coredump_routine) : failed to flush final core data : kdp_core_output(%p, 0, NULL) returned 0x%x\n"
- "(kern_coredump_routine) : failed to write zero fill padding (%llu bytes remaining) : kdp_core_output(%p, %llu, NULL) returned 0x%x\n"
- "(kern_coredump_routine) : save_segment_data returned without all segment data written, %llu of %llu remaining\n"
- "(kern_dump_seek_to_next_file) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(kern_dump_update_header) outproc data flush returned 0x%x\n"
- "(kern_dump_update_header) outproc explicit flush returned 0x%x\n"
- "(kern_dump_update_header) outproc(KDP_DATA, NULL, %lu, %p) returned 0x%x\n"
- "(kern_dump_update_header) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(kern_dump_write_public_key) outproc data flush returned 0x%x\n"
- "(kern_dump_write_public_key) outproc explicit flush returned 0x%x\n"
- "(kern_dump_write_public_key) outproc(KDP_DATA, NULL, %llu, NULL) returned 0x%x\n"
- "(kern_dump_write_public_key) outproc(KDP_DATA, NULL, %u, %p) returned 0x%x\n"
- "(kern_dump_write_public_key) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(zlib_zoutput) outproc(KDP_DATA, NULL, 0x%x, %p) returned 0x%x\n"
- ".gz"
- "/cores/core.%d"
- "/private/preboot/kernelcore"
- "/private/var/cores"
- "/private/var/dextcores"
- "/private/var/vm/kernelcore"
- "100.."
- "11122221222222222222222112"
- "121212112"
- "; UUID="
- "; stext="
- "A dump server was not specified in the boot-args, terminating kernel core dump.\n"
- "Attempting connection to panic server configured at IP %s, port %d\n"
- "Boot-args specify %d MB kernel corefile\n"
- "Corefile is not yet initialized. Cannot write a coredump to disk\n"
- "Couldn't retrieve volume status. Error %d\n"
- "Done\nCoredump complete of %s, dumped %llu segments (%llu bytes), %llu threads (%llu bytes) overall uncompressed file length %llu bytes."
- "EOF Flush: Detected stale/invalid seq num. Expected: %d, received %d\n"
- "Error: No transport device registered for kernel crashdump\n"
- "Failed to %s the corefile. Error %d\n"
- "Failed to dump coprocessor cores\n"
- "Failed to dump userspace process cores\n"
- "Failed to flush panic region data : kdp_core_output(%p, 0, NULL) returned 0x%x\n"
- "Failed to open corefile of size %llu MB (low disk space)\n"
- "Failed to open corefile of size %llu MB (returned error 0x%x)\n"
- "Failed to open the corefile. Error %d\n"
- "Failed to record panic region in corefile header, kern_dump_record_file returned 0x%x\n"
- "Failed to seek to beginning of next core\n"
- "Failed to seek to panic region file offset 0x%llx, kern_dump_seek_to_next_file returned 0x%x\n"
- "Failed to write panic region to file, kdp_coreoutput(outstate, %zu, %p) returned 0x%x\n"
- "IOPolledFileFlush() returned 0x%x\n"
- "IOPolledFileFlush(0x%p) : IOStartPolledIO(0x%p, kIOPolledFlush, 0, 0, 0) returned 0x%x\n"
- "IOPolledFilePollersClose (during EOF) returned 0x%x\n"
- "IOPolledFilePollersOpen returned 0x%x\n"
- "IOPolledFilePollersSetup for corefile failed with error: 0x%x\n"
- "IOPolledFilePollersSetup(%d) error 0x%x\n"
- "IOPolledFileSeek(0x%llx) returned 0x%x\n"
- "IOPolledFileSeek(gIOPolledCoreFileVars, 0) returned 0x%x\n"
- "IOPolledFileSeek: called to seek to 0x%llx greater than file size of 0x%llx\n"
- "IOPolledFileWrite (during EOF) returned 0x%x\n"
- "IOPolledFileWrite (during seek) returned 0x%x\n"
- "IOPolledFileWrite(0x%p, 0x%p, %llu, 0x%p) : IOStartPolledIO(0x%p, kIOPolledWrite, %llu, 0x%llx, %d) returned 0x%x\n"
- "IOPolledFileWrite(gIOPolledCoreFileVars, %p, 0x%llx, NULL) returned 0x%x\n"
- "IOPolledInterface::checkForWork[%d] 0x%x\n"
- "IOPolledInterface::close[%d] 0x%x\n"
- "IOPolledInterface::ioStatus 0x%x\n"
- "IOPolledInterface::open[%d] 0x%x\n"
- "IOPolledInterface::probe[%d] 0x%x\n"
- "IOPolledInterface::startIO[%d] 0x%x\n"
- "IOPolledInterfaceActive"
- "IOPolledInterfaceStack"
- "KDPCoreStageInit"
- "Kernel map size is %llu\n"
- "Kernel timed out waiting for hardware debugger to update handshake structure."
- "LZ4 stage is not yet initialized. Cannot write a coredump to disk\n"
- "No contact in %llu seconds\n"
- "Opened corefile of size %llu MB\n"
- "Opened file %s, size %qd, extents %ld, maxio %qx ssd %d\n"
- "Original panic string:\n"
- "Preferred Block Size"
- "Recorded panic region in corefile at offset 0x%llx, compressed to %llu bytes\n"
- "Resolved %s's (or proxy's) link level address\n"
- "Routing through specified router IP %s (%u)\n"
- "Sending write request for %s\n"
- "Set a new encryption key for coredumps"
- "Setting coredump status as done!\n"
- "Skipping coredump\n"
- "Skipping panic region dump\n"
- "Skipping userspace coredump, coredump list is locked\n"
- "System dump aborted.\n"
- "Transmitting kernel state, please wait:\n"
- "Transmitting packets to link level address: %02x:%02x:%02x:%02x:%02x:%02x\n"
- "Transmitting panic log, please wait: "
- "Transmitting system log, please wait: "
- "Unable to create core header packet.\n"
- "Unable to retrieve range for root memory device %d\n"
- "Unknown format character %c in `%s'\n"
- "Volume is low on space. Not allocating kernel corefile.\n"
- "Waiting for hardware shared memory debugger, handshake structure is at virt: %p, phys %p\n"
- "We were in the middle of initializing LZ4 stage. Cannot write a coredump to disk\n"
- "We were in the middle of initializing encryption. Marking it as unavailable\n"
- "We were in the middle of initializing the disk stage. Cannot write a coredump to disk\n"
- "Writing all cores through shared memory debugger\n"
- "Writing local cores...\n"
- "ZERR %d\n"
- "Zlib stage is not initialized. Cannot write a coredump to shared memory\n"
- "Zlib stage is not initialized. Cannot write a coredump to the network\n"
- "_kdp_ipstr"
- "_panicd_corename"
- "_panicd_ip"
- "_router_ip"
- "addrable bits"
- "apple_encrypted_archive interface registration callback is already set @%s:%d"
- "buffer_stage_outproc (during flush) returned 0x%x\n"
- "buffer_stage_outproc (during forwarding) returned 0x%x\n"
- "com.apple.private.coredump-encryption-key"
- "com.apple.private.custom-coredump-location"
- "com.apple.private.enable-coredump-on-panic-seed-privacy-approved"
- "com.apple.private.security.file-unencrypt-access"
- "compression interface registration callback is already set @%s:%d"
- "coredump_encryption"
- "coredump_encryption_key"
- "coredump_init returned KERN_NODE_DOWN, skipping this core\n"
- "coredump_save_note_data"
- "coredump_save_note_description"
- "coredump_save_segment_data"
- "coredump_save_segment_data failed with %d\n"
- "coredump_save_segment_descriptions"
- "coredump_save_summary"
- "coredump_save_sw_vers"
- "coredump_save_sw_vers_legacy"
- "coredump_save_thread_state"
- "corefile path selection in device-tree is not one of the allowed values: %s, Using default %s\n"
- "corefile path selection in device-tree was set to: %s (value: %s)\n"
- "corefile_size_mb"
- "custom"
- "dumpinfo does not fit into KDP packet.\n"
- "error 0x%x from IOGetHibernationCryptKey\n"
- "error 0x%x opening polled file\n"
- "handshake structure not initialized\n"
- "hwm_user_cores"
- "inet_aton() failed interpreting %s as a panic server IP\n"
- "inet_aton() failed interpreting %s as an IP\n"
- "inline call to debugger(machine_startup)"
- "kdp panic: %s"
- "kdp_core.c"
- "kdp_core_exclude_region"
- "kdp_corefile"
- "kdp_crashdump_pkt_size"
- "kdp_ip_addr"
- "kdp_panic_dump: unexpected pending input packet"
- "kdp_poll"
- "kdp_raise_exception"
- "kdp_reply: no input packet"
- "kdp_send: no input packet"
- "kdp_send: packet too large (%u > %d)"
- "kdp_send_crashdump_data returned 0x%x\n"
- "kdp_send_crashdump_pkt failed with error %d\n"
- "kdp_set_dump_info: Skipping invalid panicd port %u (using %d)\n"
- "kern ver str"
- "kern_coredump_routine"
- "kern_dump_init"
- "kern_dump_save_note_data"
- "kern_open_file_for_direct_io took %qd ms\n"
- "kernel-core-dump-location"
- "load binary"
- "lz4_stage_outproc"
- "lz4_stage_stream"
- "main bin spec"
- "memory_backing_aware_buffer_stage_outproc"
- "misaligned file pos %qx\n"
- "octet"
- "outproc(KDP_WRQ, NULL, 0, NULL) returned 0x%x\n"
- "panic context"
- "panic_region"
- "panicd_port"
- "paniclog"
- "pid %ld (%s), uid (%u): corename is too long\n"
- "pid %ld (%s), uid (%u): unexpected end of string after %% token\n"
- "polled file major %d, minor %d, blocksize %ld, pollers %d\n"
- "preboot"
- "progress_notify_stage_outproc"
- "read from"
- "save_seg_data: pmap traversal failed: %d\n"
- "save_seg_desc: pmap traversal failed: %d\n"
- "save_summary: pmap traversal failed: %d\n"
- "secure_core: Unable to seek to the start of file: %d\n"
- "shmem_dbg_process_buffers"
- "shmem_stage_announce"
- "shmem_stage_outproc"
- "shmem_wait_for_state"
- "site.IOPolledFileIOVars"
- "site.struct kern_userspace_coredump_context"
- "site.typeof(*data)"
- "site.typeof(*region)"
- "skipping local kernel core because core file could not be opened prior to panic (mode : 0x%x, error : 0x%x)\n"
- "skipping local kernel core because the SPTM is in INTERRUPTED state and can't support core dump generation\n"
- "skipping local kernel core because the SPTM is in PANIC state and can't support core dump generation\n"
- "systemlog"
- "user_dump_init"
- "user_dump_save_seg_descriptions"
- "user_dump_save_segment_data"
- "user_dump_save_summary"
- "write to"
- "xnu"
- "xnu-"
- "zlib_stage_outproc"

```

#### com.apple.security.sandbox

>  `com.apple.security.sandbox`

```diff

 2680.40.16.0.0
   __TEXT.__os_log: 0x2287
-  __TEXT.__const: 0x1d8301
+  __TEXT.__const: 0x1d8381
   __TEXT.__cstring: 0x713e
   __TEXT_EXEC.__text: 0x37c24
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x3810
   __DATA_CONST.__kalloc_type: 0xac0
   __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: F030C771-9430-3EE0-9F6D-4713CCCB68CF
+  UUID: AC7AB811-1AA1-3620-9642-6EBFC9F13535
   Functions: 657
   Symbols:   0
   CStrings:  1327

```


</details>

## MachO

### ❌ Removed (2)

- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/usr/libexec/memoryanalyticsd`

### ⬆️ Updated (121)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/CheckerBoard.app/CheckerBoard](MACHOS/CheckerBoard.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004](MACHOS/Diagnostic-7004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185](MACHOS/Diagnostic-8185.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268](MACHOS/Diagnostic-8268.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340](MACHOS/Diagnostic-8340.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343](MACHOS/Diagnostic-8343.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006](MACHOS/Diagnostic-9006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008](MACHOS/Diagnostic-9008.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010](MACHOS/Diagnostic-9010.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9013.appex/Diagnostic-9013](MACHOS/Diagnostic-9013.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods](MACHOS/SystemReport-AirPods.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-BatteryCase.appex/SystemReport-BatteryCase](MACHOS/SystemReport-BatteryCase.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport](MACHOS/SystemReport.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/System/Library/Assistant/Plugins/activity.assistantBundle/activity](MACHOS/activity.md)
- [/System/Library/ControlCenter/Bundles/RPControlCenterModuleHQLR.bundle/RPControlCenterModuleHQLR](MACHOS/RPControlCenterModuleHQLR.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/HangHUD.app/HangHUD](MACHOS/HangHUD.md)
- [/System/Library/DataClassMigrators/AddressBookLegacy.migrator/AddressBookLegacy](MACHOS/AddressBookLegacy.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard](MACHOS/SpringBoard.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider](MACHOS/AmbientPhotoFramePosterProvider.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/CloudWorker.appex/CloudWorker](MACHOS/CloudWorker.md)
- [/System/Library/ExtensionKit/Extensions/DisplayAndBrightnessSettingsExtension.appex/DisplayAndBrightnessSettingsExtension](MACHOS/DisplayAndBrightnessSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseAVExtension.appex/LighthouseAVExtension](MACHOS/LighthouseAVExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseAVShadowEval.appex/LighthouseAVShadowEval](MACHOS/LighthouseAVShadowEval.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseServicesAnalyticsExtension.appex/LighthouseServicesAnalyticsExtension](MACHOS/LighthouseServicesAnalyticsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/Frameworks/CoreImage.framework/redeye_repair_archive_bin.metallib](MACHOS/redeye_repair_archive_bin.metallib.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/DigitalTouchBalloonProvider.bundle/DigitalTouchBalloonProvider](MACHOS/DigitalTouchBalloonProvider.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKWarlockFaceBundle.bundle/warlock.metallib](MACHOS/warlock.metallib.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](MACHOS/KeyboardSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/PlugIns/com.apple.CloudDocsUI.CloudSharing.appex/com.apple.CloudDocsUI.CloudSharing](MACHOS/com.apple.CloudDocsUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/Support/companioncamerad](MACHOS/companioncamerad.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/default-binaryarchive.metallib](MACHOS/default-binaryarchive.metallib.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/mxi-binaryarchive.metallib](MACHOS/mxi-binaryarchive.metallib.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced](MACHOS/CoreThreadCommissionerServiced.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd](MACHOS/ecosystemanalyticsd.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension](MACHOS/HangLogsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension](MACHOS/PerformanceLoggingDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IconRendering.framework/binary.metallib](MACHOS/binary.metallib.md)
- [/System/Library/PrivateFrameworks/JetCore.framework/Support/jetpackassetd](MACHOS/jetpackassetd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/NanoUniverse.framework/NUNICalliopeShadersCompanion.metallib](MACHOS/NUNICalliopeShadersCompanion.metallib.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService](MACHOS/PersonalizedSensingService.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/metal_libraries/binary.metallib](MACHOS/binary.metallib.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF](MACHOS/AppleMCTF.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/ColourConstancyV1.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/DepthProcessorV2.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/STF.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/checkpointd](MACHOS/checkpointd.md)
- [/usr/libexec/containermanagerd_system](MACHOS/containermanagerd_system.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/meshnetd](MACHOS/meshnetd.md)
- [/usr/libexec/mobileassetd](MACHOS/mobileassetd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/perfdiagsselfenabled](MACHOS/perfdiagsselfenabled.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/signpost_reporter](MACHOS/signpost_reporter.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/uarpassetmanagerd](MACHOS/uarpassetmanagerd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H18.im4p

>  `AppleAVE2FW_H18.im4p`

```diff

   __TEXT.__chain_starts: 0x20
   __DATA.__const: 0x39b0
   __DATA._rtk_patchbay: 0x211
-  __DATA.__data: 0x1700
+  __DATA.__data: 0x16f8
   __DATA._rtk_mtab: 0x320
   __DATA._rtk_power: 0x3b8
   __DATA.__gxf_data: 0x10

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc6838
-  UUID: 8F4FAE78-617A-3F4E-A425-69223C96E234
+  UUID: 6384FE09-A6BB-36D2-BD4C-7B1380BCFA02
   Functions: 1212
   Symbols:   1702
   CStrings:  2640

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

 1116.40.43.0.0
-  __TEXT.__text: 0x56d8fc
+  __TEXT.__text: 0x56d8dc
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__cstring: 0x41cef
   __TEXT.__const: 0x106967

   __PDATA.__common: 0x2278
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: 022F3CC2-BBF3-388B-B889-04F8A34A3CDA
+  UUID: 86F72360-2DBD-3E09-9333-C869E58B6F2D
   Functions: 21189
   Symbols:   0
   CStrings:  6398
Functions:
~ sub_856173c : 328 -> 308
~ sub_8567620 -> sub_856760c : 1628 -> 1616
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B_v4ugAYzHUv2FclLHqPxw1yRQSY7UmNjVEIN8E/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.1.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~B_v4ugDxy7BEQ1Pg6PKolYyWs5dqx_f-BjOTnx0/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.1.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~B_v5ugB2nG6sa6sdKWlOVJSgmULX-X2eCNQBp0U/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.1.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "/AppleInternal/Library/BuildRoots/4~B_x4ugCck-dtyamLCGRoqfu4FCum1VjYT7hy_AI/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.1.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~B_x5ugD4XvAvn0r0H59UNMSbJpqLQV6k_qC_6A0/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.1.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~B_x6ugAI5A7YzCagUllzdht-JcUPnJoG6daYHQ4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.1.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.1 *(23B5073a)* | iBoot-13822.42.2 |
| 26.1 *(23B82)* | iBoot-13822.42.2 |

#### 🆕 NEW (1)

<details>
  <summary><i>View NEW</i></summary>

##### `iboot_blob33.bin`
  - `root@Oct 10 2025@20:38:56~.release`

</details>

#### ❌ Removed (1)

<details>
  <summary><i>View Removed</i></summary>

##### `iboot_blob33.bin`
  - `root@Oct 11 2025@06:53:01~.release`

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.1 *(23B5073a)* | 622.2.11.10.4 |
| 26.1 *(23B82)* | 622.2.11.10.8 |

### Dylibs

#### ⬆️ Updated (166)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/ConnectivityModule.axbundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/AccessibilityBundles/Moments.axbundle/Moments](DYLIBS/Moments.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/Contacts.framework/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup](DYLIBS/IdentityLookup.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/Frameworks/PushKit.framework/PushKit](DYLIBS/PushKit.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing](DYLIBS/ASEProcessing.md)
- [/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings](DYLIBS/AUDeveloperSettings.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy](DYLIBS/AddressBookLegacy.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CentauriDiagnostic.framework/CentauriDiagnostic](DYLIBS/CentauriDiagnostic.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer](DYLIBS/CiderAudioServer.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI](DYLIBS/CloudDocsUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera](DYLIBS/CompanionCamera.md)
- [/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon](DYLIBS/ContainerManagerCommon.md)
- [/System/Library/PrivateFrameworks/ContainerManagerSystem.framework/ContainerManagerSystem](DYLIBS/ContainerManagerSystem.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore](DYLIBS/CoordinationCore.md)
- [/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon](DYLIBS/CoreCaptureDaemon.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/EchoRelay.framework/EchoRelay](DYLIBS/EchoRelay.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices](DYLIBS/FrontBoardServices.md)
- [/System/Library/PrivateFrameworks/FusionTracker.framework/FusionTracker](DYLIBS/FusionTracker.md)
- [/System/Library/PrivateFrameworks/GPUToolsReplay.framework/GPUToolsReplay](DYLIBS/GPUToolsReplay.md)
- [/System/Library/PrivateFrameworks/GameStoreKit.framework/GameStoreKit](DYLIBS/GameStoreKit.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager](DYLIBS/HeadphoneManager.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettingsUI.framework/HeadphoneSettingsUI](DYLIBS/HeadphoneSettingsUI.md)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/ImagePlaygroundInternal.framework/ImagePlaygroundInternal](DYLIBS/ImagePlaygroundInternal.md)
- [/System/Library/PrivateFrameworks/IntelligenceEngine.framework/IntelligenceEngine](DYLIBS/IntelligenceEngine.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/JetCore.framework/JetCore](DYLIBS/JetCore.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/KeyboardSettings.framework/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback](DYLIBS/KeyboardSettingsFeedback.md)
- [/System/Library/PrivateFrameworks/MDM.framework/MDM](DYLIBS/MDM.md)
- [/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport](DYLIBS/MTLToolsDeviceSupport.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileContainerManager.framework/MobileContainerManager](DYLIBS/MobileContainerManager.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MomentsIntelligence.framework/MomentsIntelligence](DYLIBS/MomentsIntelligence.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices](DYLIBS/RunningBoardServices.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/Sentry.framework/Sentry](DYLIBS/Sentry.md)
- [/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligenceUI.framework/VisualIntelligenceUI](DYLIBS/VisualIntelligenceUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/VideoCodecs/VCPHEVC.videocodec](DYLIBS/VCPHEVC.videocodec.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoEncoders/H264H9.videoencoder](DYLIBS/H264H9.videoencoder.md)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder.md)
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libchannel.dylib](DYLIBS/libchannel.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/system/libsystem_containermanager.dylib](DYLIBS/libsystem_containermanager.dylib.md)

</details>

## Files

### 🆕 New

#### filesystem (163)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/AccessibilityBundles/Moments.axbundle/Accessibility-Jurassic.loctable`
- `/System/Library/AccessibilityBundles/Music.axbundle/Accessibility-AQ.loctable`
- `/System/Library/AccessibilityBundles/MusicApplication.axbundle/Accessibility-AQ.loctable`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/id.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/nl-be.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/zh-tw.cat.bin`
- `/System/Library/CoreServices/BluetoothUIService.app/Banner-PID-8215-Seed-mov/Banner-PID-8215-12-Loop.mov`
- `/System/Library/CoreServices/BluetoothUIService.app/Banner-PID-8215-Seed-mov/Banner-PID-8215-13-Loop.mov`
- `/System/Library/CoreServices/BluetoothUIService.app/Banner-PID-8229-Seed-mov/Banner-PID-8229-5-Loop.mov`
- `/System/Library/CoreServices/BluetoothUIService.app/Banner-PID-8229-Seed-mov/Banner-PID-8229-6-Loop.mov`
- `/System/Library/CoreServices/BluetoothUIService.app/Banner-PID-8230-Seed-mov/Banner-PID-8230-6-Loop.mov`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/8a5f47d6e0bb0a3e08f898f5f69fdc990a709cf4.asset/AssetData/UnitedStatesSettings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/8a5f47d6e0bb0a3e08f898f5f69fdc990a709cf4.asset/AssetData/countryInfoMap.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/8a5f47d6e0bb0a3e08f898f5f69fdc990a709cf4.asset/AssetData/settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/8a5f47d6e0bb0a3e08f898f5f69fdc990a709cf4.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f949be2b5bc29e8d9e985afc0fa7fbf4a3559fb0.asset/AssetData/settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f949be2b5bc29e8d9e985afc0fa7fbf4a3559fb0.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_MobileBluetoothAssets/6df6675e3dfe9f5158c27c1ebdbacee24a426365.asset/AssetData/device_workarounds.db`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_MobileBluetoothAssets/6df6675e3dfe9f5158c27c1ebdbacee24a426365.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/7f50a81a71f8ff6cebbf2d151474b0256a253146.asset/AssetData/empty.txt`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/7f50a81a71f8ff6cebbf2d151474b0256a253146.asset/Info.plist`
- `/System/Library/PrivateFrameworks/AppleDepth.framework/MLModels/Mona-H18-d23-v53-v54-v57/model.bundle/H18.bundle/main_height576_width768/main_ane/model.hwx`
- `/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/DeviceConfig-Seed.loctable`
- `/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUI-CleanupRegional.loctable`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/AudioAccessory.bundle/bg.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/AudioAccessory.bundle/kk.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/bg.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/bn.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/gu.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/kk.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/kn.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/lt.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/ml.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/mr.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/or.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/pa.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/sl.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/ta.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/te.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/ur.lproj/License.html`
- `/private/var/staged_system_apps/Freeform.app/ar.lproj/nlu.appintents/6f63780872c8b611c6d643c2bce643d4.version`
- `/private/var/staged_system_apps/Freeform.app/bg.lproj/nlu.appintents/1e780b21d7d27e8ba34af0514af1e89d.version`
- `/private/var/staged_system_apps/Freeform.app/bn.lproj/nlu.appintents/767913bd5f4e9a2e64ea2574a8973379.version`
- `/private/var/staged_system_apps/Freeform.app/ca.lproj/nlu.appintents/aaa7dfb85333afa65ac5281736c8e93d.version`
- `/private/var/staged_system_apps/Freeform.app/cs.lproj/nlu.appintents/64d74ab3a94e325885f0eb07213b610f.version`
- `/private/var/staged_system_apps/Freeform.app/da.lproj/nlu.appintents/4ed79fc059c19d35958103b46aa6a87f.version`
- `/private/var/staged_system_apps/Freeform.app/de.lproj/nlu.appintents/09b70f4c22fcc375d73a036960fdedb2.version`
- `/private/var/staged_system_apps/Freeform.app/el.lproj/nlu.appintents/20c6cc2349884fc1412b572d55ad2d75.version`
- `/private/var/staged_system_apps/Freeform.app/en.lproj/nlu.appintents/28ecc452481732542448ab5d48e4ffdd.version`
- `/private/var/staged_system_apps/Freeform.app/en_AU.lproj/nlu.appintents/eda04157b6a2a89a8095b36a7ee6bea7.version`
- `/private/var/staged_system_apps/Freeform.app/en_GB.lproj/nlu.appintents/3b9d23878a1bacd16d14ee4aeea9afcf.version`
- `/private/var/staged_system_apps/Freeform.app/en_IN.lproj/nlu.appintents/c445509e95e6d3b1929e89fc15c169be.version`
- `/private/var/staged_system_apps/Freeform.app/es.lproj/nlu.appintents/40f8e86ec07fb16cdb5bf7b8de079cd1.version`
- `/private/var/staged_system_apps/Freeform.app/es_419.lproj/nlu.appintents/a5db2fb0fd745a4d51db0ed7e63b7056.version`
- `/private/var/staged_system_apps/Freeform.app/es_US.lproj/nlu.appintents/bc45f12ac45c6fd715df3acce5791749.version`
- `/private/var/staged_system_apps/Freeform.app/fi.lproj/nlu.appintents/fa50e371f025a080c47c2c00fd9add7a.version`
- `/private/var/staged_system_apps/Freeform.app/fr.lproj/nlu.appintents/81cd271b8fd2f30d812585dcb1fc91f9.version`
- `/private/var/staged_system_apps/Freeform.app/fr_CA.lproj/nlu.appintents/312a11cb8a7eeba9136ed8fbd6ae36b6.version`
- `/private/var/staged_system_apps/Freeform.app/gu.lproj/nlu.appintents/56b7338bb761f3ffa1d961279033fa74.version`
- `/private/var/staged_system_apps/Freeform.app/he.lproj/nlu.appintents/74815bf3d9d5c1225c316789f6cfa393.version`
- `/private/var/staged_system_apps/Freeform.app/hi.lproj/nlu.appintents/20db1ed102a6c82ac7490907e3a8478e.version`
- `/private/var/staged_system_apps/Freeform.app/hr.lproj/nlu.appintents/8943516f56be7b23bca8b17c1ee5d6ac.version`
- `/private/var/staged_system_apps/Freeform.app/hu.lproj/nlu.appintents/19cf588f268f712f08f27394fcf60c1a.version`
- `/private/var/staged_system_apps/Freeform.app/id.lproj/nlu.appintents/3506b139450947f5c43e95882151acb8.version`
- `/private/var/staged_system_apps/Freeform.app/it.lproj/nlu.appintents/885726809a0c87daf0601a1486829853.version`
- `/private/var/staged_system_apps/Freeform.app/ja.lproj/nlu.appintents/bcb9e5a236b4b8437ab57aacbd1af77f.version`
- `/private/var/staged_system_apps/Freeform.app/kk.lproj/nlu.appintents/a715bc7acf1e49ea6c2b61e09669b566.version`
- `/private/var/staged_system_apps/Freeform.app/kn.lproj/nlu.appintents/62527b023cdb5d400ea0f8d8569a3544.version`
- `/private/var/staged_system_apps/Freeform.app/ko.lproj/nlu.appintents/93d02b9b4096bfee6c5da15c121a5daa.version`
- `/private/var/staged_system_apps/Freeform.app/lt.lproj/nlu.appintents/15d02d7f8ddcc84e5d311e95752e9192.version`
- `/private/var/staged_system_apps/Freeform.app/ml.lproj/nlu.appintents/4462ed1c845a29b65b507141b78245df.version`
- `/private/var/staged_system_apps/Freeform.app/mr.lproj/nlu.appintents/c376765da63469d3793c9694c5422e65.version`
- `/private/var/staged_system_apps/Freeform.app/ms.lproj/nlu.appintents/3f605f9e810cc386c0f61ed61ebd4926.version`
- `/private/var/staged_system_apps/Freeform.app/nl.lproj/nlu.appintents/06c73c29882372ea05647e8eae851f7e.version`
- `/private/var/staged_system_apps/Freeform.app/no.lproj/nlu.appintents/857929e76e72d0ea8f380ae8c8499e0a.version`
- `/private/var/staged_system_apps/Freeform.app/or.lproj/nlu.appintents/014746a36d222e33f5cc9f7e832962ed.version`
- `/private/var/staged_system_apps/Freeform.app/pa.lproj/nlu.appintents/1692e5431c5bc18b8a217cc1593be18d.version`
- `/private/var/staged_system_apps/Freeform.app/pl.lproj/nlu.appintents/42f73734db52846782519a5f86aca3c5.version`
- `/private/var/staged_system_apps/Freeform.app/pt_BR.lproj/nlu.appintents/aa75c71d6bc108a6178719f5ef202057.version`
- `/private/var/staged_system_apps/Freeform.app/ro.lproj/nlu.appintents/3a5d52d82e61d22138cffec7f51e7a2f.version`
- `/private/var/staged_system_apps/Freeform.app/ru.lproj/nlu.appintents/346873d3c7710bbc8e58140e129c19c7.version`
- `/private/var/staged_system_apps/Freeform.app/sk.lproj/nlu.appintents/adf1d418cd922907105a198b6dfd867c.version`
- `/private/var/staged_system_apps/Freeform.app/sl.lproj/nlu.appintents/6cb5c1fdd9dfad5c009826bbd543712f.version`
- `/private/var/staged_system_apps/Freeform.app/sv.lproj/nlu.appintents/a3b29cc6f9b6027f634faa4d1b05d221.version`
- `/private/var/staged_system_apps/Freeform.app/ta.lproj/nlu.appintents/462ce1edd0365a4f14f4c5f9410361bc.version`
- `/private/var/staged_system_apps/Freeform.app/th.lproj/nlu.appintents/87e25fe32868e28932e7c3a6cee90208.version`
- `/private/var/staged_system_apps/Freeform.app/tr.lproj/nlu.appintents/89a48b277d34ce6ab6927be7949c0013.version`
- `/private/var/staged_system_apps/Freeform.app/uk.lproj/nlu.appintents/61f7aeacb624f00f61f9ca720ed1c9bd.version`
- `/private/var/staged_system_apps/Freeform.app/ur.lproj/nlu.appintents/ca2b8ea122b3945c96ca6a65063de3a7.version`
- `/private/var/staged_system_apps/Freeform.app/vi.lproj/nlu.appintents/ddfd97edeb91f4a0bb82b38668082e22.version`
- `/private/var/staged_system_apps/Freeform.app/zh_CN.lproj/nlu.appintents/0a76936dea32b28120159d8568aab4e0.version`
- `/private/var/staged_system_apps/Freeform.app/zh_HK.lproj/nlu.appintents/ec091b5ebaa6c1f1068aaf1b71b08b47.version`
- `/private/var/staged_system_apps/Freeform.app/zh_TW.lproj/nlu.appintents/4681c860530f83b2533607fd7a480d02.version`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/f970cbef1b44402c8bf9425502bf8ff4.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/a79adccb08a373b3de6df5292c1604b0.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/88e999833ace06f306429e05b1aebe25.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/9f0a4c46e1fcd1a59fbac67184ff418d.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/707c6e900ed3c14117c8593f590cfdeb.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/80bafc615123c1c30c843144eaccd898.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/02ef1a710ce8422bf0ff2803415d72b8.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/1be5d5d4b968256dbfc16fd61e77a59a.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/30241ae54c05257904922e40ef4aa4b9.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/7af3979589183800d58a0068cec2382c.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/c653f3b270bfe6be83d10b3a0cfd0156.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/2f8f6abd6506db59c31f8db9bcfd8100.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/08892aae91b6cd8ad549caf3db6328ab.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/a95db3c535367bacedd0a2c3fd24506d.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/95cce0c62ba3555e5f7e0ff979bfeb21.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/01171e2e5a0ae10f1694de3a83c0d3dc.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/559b30eaefa2f55e08ddb4a5863ebe41.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/43296fe1442583247a90c518010b3bf8.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/3a9cc12af0cbaaa971eed5839e221325.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/98c91bb0a77118c6a917f95ba69a518e.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/c34ab9fc8a3b024386de1569a3991769.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/6d3e1aa4d7e40c65577c20aedb62edf2.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/611b542180d253354c0d6152e989a6e6.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/421b5d7b08d29be3ac04230c12ed25f2.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/7929eaba225d46026746c377376cd9a4.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/b586937f84d50917b91a378e2b9458ed.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/64d2898a3c2433c496a96463a58a9cf9.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/aa153e71d0e8eae8fef0da5156f16128.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/5ea70767a0e7503353d2e2f1ab6231c6.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/44aea20e024dc7b0919550a98e92c1ed.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/e490a5d9876eb1d2de9792317afb80aa.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/3b4a8d4b149bcdf040332f99e16d8a70.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/4b18f494672f8b67086964e3a4e20d1a.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/5f6a878e9fa1c50a4a4a1ec84c22faf2.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/275ebc4e59fd73029c3740916aa7995a.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/31bfbfef509453c9721990fda028ca07.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/478f2b726eb6819fc65908d74e4d1c4c.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/4a8d3d8fba33f14ae33a55dc8f19c89a.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/af31631254bfe49dbd86507a89c2ed11.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/b804f1adcf301b19ed16edc5364e4388.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/8bd6f182543bc2c4628533fb582b28c2.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/b9fdd618a1ef3f0b91373858da593f34.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/c4d091c0977cd654add5169b8046234b.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/635e9ab93c1be6ffadc5765c5f6ba90b.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/017ebaaecaff2e04da29299d96c56e63.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/8a8efebffce30e72f93ff2caaed12e68.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/2f69056368839e67464f6221220721e4.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/4e30dea4b51ecb923aef7eb36ed527bb.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/a90eae01cff045c8753ced88605a2830.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/a5a83d19bcf3866cdbe20672f6a7791a.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/b885a4667531b1d4263873f238af98b8.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/2a166b287736ca80740a565112b216d4.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Base.lproj/nlu.appintents/fe200a7bea670fc523de9e407efda68c.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/98a0ab95cd69b79b7ca598b944f27ba7.version`
- `/usr/standalone/firmware/nfrestore/firmware/fw/SN450V_FW_A1_01_01_009_rev164126.bin`
- `/usr/standalone/firmware/nfrestore/firmware/rf/SN450V_FW_A1_01_01_009_rev164126.plist`
- `/usr/standalone/firmware/nfrestore/firmware/rf/SN450V_FW_A1_01_01_809_rev164319.plist`

</details>

### ❌ Removed

#### filesystem (139)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/Frameworks/SystemConfiguration.framework/get-mobility-info`
- `/System/Library/LaunchDaemons/com.apple.memoryanalyticsd.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.FaceTime.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.Home.framework.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.IDS.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.Messages.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.MessagesEvents.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.Registration.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.StatusKit.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.Transport.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.apsd.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.calldirectory.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.callkit.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.callservicesd.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.conversationkit.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.facetime.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.identitylookup.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.incallservice.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.messagefilter.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.mobilephone.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.telephonyui.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.telephonyutilities.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.voicemail.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_MobileBluetoothAssets/8f668de574d646767214465c99c2cfcf969bfff3.asset/AssetData/device_workarounds.db`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_MobileBluetoothAssets/8f668de574d646767214465c99c2cfcf969bfff3.asset/Info.plist`
- `/System/Library/PrivateFrameworks/AppleDepth.framework/MLModels/Mona-H18-d23-v53-v54-v57/model.bundle/H18.bundle/main_height768_width768/main_ane/model.hwx`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/Info.plist`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/Home.framework/com.apple.Home.framework.plist`
- `/System/Library/PrivateFrameworks/Home.framework/com.apple.Home.plist`
- `/private/var/staged_system_apps/Freeform.app/ar.lproj/nlu.appintents/5ac65ad96ba0796e18e9a4c37fb6b607.version`
- `/private/var/staged_system_apps/Freeform.app/bg.lproj/nlu.appintents/682dce15ecceeac16fd8406e68e7cf9a.version`
- `/private/var/staged_system_apps/Freeform.app/bn.lproj/nlu.appintents/e6bb17f5437dfb6af0411cf2716a72f1.version`
- `/private/var/staged_system_apps/Freeform.app/ca.lproj/nlu.appintents/51e54960a7698571bcafee5d635cd3a3.version`
- `/private/var/staged_system_apps/Freeform.app/cs.lproj/nlu.appintents/93dc2771fe181df6d4ca5fdf9803bd39.version`
- `/private/var/staged_system_apps/Freeform.app/da.lproj/nlu.appintents/fb1149ba111511b3177b16f76990687b.version`
- `/private/var/staged_system_apps/Freeform.app/de.lproj/nlu.appintents/8062fce3cf3165bddc069ad000a478c8.version`
- `/private/var/staged_system_apps/Freeform.app/el.lproj/nlu.appintents/46ab90265ceba365cfc6d3721b310b0b.version`
- `/private/var/staged_system_apps/Freeform.app/en.lproj/nlu.appintents/46e8f7429677227903521a829b3ecfc3.version`
- `/private/var/staged_system_apps/Freeform.app/en_AU.lproj/nlu.appintents/d6ec90437f8011199dcb0fc1c5ee5068.version`
- `/private/var/staged_system_apps/Freeform.app/en_GB.lproj/nlu.appintents/2760b4bc138ffc23e6b94daae0bf2913.version`
- `/private/var/staged_system_apps/Freeform.app/en_IN.lproj/nlu.appintents/dad4913981158e6b55f68edac1fbcbaa.version`
- `/private/var/staged_system_apps/Freeform.app/es.lproj/nlu.appintents/c3019eac7703d46c15965eccdc0d2f00.version`
- `/private/var/staged_system_apps/Freeform.app/es_419.lproj/nlu.appintents/b8762ea414a77b771b9d4b269f5159ee.version`
- `/private/var/staged_system_apps/Freeform.app/es_US.lproj/nlu.appintents/53f8f86bbb2d638a7e3038e36c48d4ef.version`
- `/private/var/staged_system_apps/Freeform.app/fi.lproj/nlu.appintents/986fb43dcbef0c8e89fe1c93bdabcf52.version`
- `/private/var/staged_system_apps/Freeform.app/fr.lproj/nlu.appintents/5f136a23bc11037095a21e2e6dab7e2c.version`
- `/private/var/staged_system_apps/Freeform.app/fr_CA.lproj/nlu.appintents/df0cb3f921899f7d1f22b5a3b8fb6f06.version`
- `/private/var/staged_system_apps/Freeform.app/gu.lproj/nlu.appintents/231a62263990ac2d2eeb357ab543b625.version`
- `/private/var/staged_system_apps/Freeform.app/he.lproj/nlu.appintents/598cfd240c8327a2f37f32cf4953a0e3.version`
- `/private/var/staged_system_apps/Freeform.app/hi.lproj/nlu.appintents/dcd583d14f722900796d84a542654976.version`
- `/private/var/staged_system_apps/Freeform.app/hr.lproj/nlu.appintents/cdb12999363f3b3eb1dac882327c0786.version`
- `/private/var/staged_system_apps/Freeform.app/hu.lproj/nlu.appintents/8fa3759dfc993f243f07e43dbc4d75cc.version`
- `/private/var/staged_system_apps/Freeform.app/id.lproj/nlu.appintents/706e86f1780f1fdb4d69dcc355428be6.version`
- `/private/var/staged_system_apps/Freeform.app/it.lproj/nlu.appintents/64d085adfd2cc642d7e4b7dc4b5ed8bf.version`
- `/private/var/staged_system_apps/Freeform.app/ja.lproj/nlu.appintents/55a05810ccc04d7a89356f936ed158a0.version`
- `/private/var/staged_system_apps/Freeform.app/kk.lproj/nlu.appintents/34055074f99ed86dd2bdf9e23993a083.version`
- `/private/var/staged_system_apps/Freeform.app/kn.lproj/nlu.appintents/ccf05dcc964ea42bdc68225b75a321ad.version`
- `/private/var/staged_system_apps/Freeform.app/ko.lproj/nlu.appintents/f22b9c023bde54b0aa3b22f29447bb22.version`
- `/private/var/staged_system_apps/Freeform.app/lt.lproj/nlu.appintents/ac2eccabd83a2a70ba48b0ec75c5affb.version`
- `/private/var/staged_system_apps/Freeform.app/ml.lproj/nlu.appintents/73535b579c59bfd233eec9dba4718407.version`
- `/private/var/staged_system_apps/Freeform.app/mr.lproj/nlu.appintents/4f813c45a68da05f7dec692994034713.version`
- `/private/var/staged_system_apps/Freeform.app/ms.lproj/nlu.appintents/7f832586272ae9184c0fa8eda8d4f98e.version`
- `/private/var/staged_system_apps/Freeform.app/nl.lproj/nlu.appintents/ab46f0b863c6880a65f97b844fa31062.version`
- `/private/var/staged_system_apps/Freeform.app/no.lproj/nlu.appintents/5c1e6014125ea3a40dc70e97e4db790a.version`
- `/private/var/staged_system_apps/Freeform.app/or.lproj/nlu.appintents/0c6ed84a3bc490e3f8dadd7512ac630d.version`
- `/private/var/staged_system_apps/Freeform.app/pa.lproj/nlu.appintents/1a78c85e69bb02e3ba3226a67b3cbf08.version`
- `/private/var/staged_system_apps/Freeform.app/pl.lproj/nlu.appintents/bf1c045565a059d760fe22418c9e2af7.version`
- `/private/var/staged_system_apps/Freeform.app/pt_BR.lproj/nlu.appintents/ba6ac098d2adb426a300a3b30680f6e4.version`
- `/private/var/staged_system_apps/Freeform.app/ro.lproj/nlu.appintents/910f8d1035e8bc7c62b49ffa43e71cc8.version`
- `/private/var/staged_system_apps/Freeform.app/ru.lproj/nlu.appintents/e10d2f472f9497e79e413c961f858977.version`
- `/private/var/staged_system_apps/Freeform.app/sk.lproj/nlu.appintents/b141eb4462d03efcd121fe082dd49559.version`
- `/private/var/staged_system_apps/Freeform.app/sl.lproj/nlu.appintents/68e3554d598eed70a3df066cca16c00b.version`
- `/private/var/staged_system_apps/Freeform.app/sv.lproj/nlu.appintents/5ee0aabf1d5713e51fc9f6f12a9c273d.version`
- `/private/var/staged_system_apps/Freeform.app/ta.lproj/nlu.appintents/70a16a0f9699601adbc407fe988597db.version`
- `/private/var/staged_system_apps/Freeform.app/th.lproj/nlu.appintents/0580ddbd399c52bc69dcda5eb87f9eba.version`
- `/private/var/staged_system_apps/Freeform.app/tr.lproj/nlu.appintents/4f2c454d57799a93c1014cdc5622db07.version`
- `/private/var/staged_system_apps/Freeform.app/uk.lproj/nlu.appintents/f1a977d010c7d36d7bd22d4a7dcbfd2b.version`
- `/private/var/staged_system_apps/Freeform.app/ur.lproj/nlu.appintents/d0cbc139446f45d760987bd409f9d7a5.version`
- `/private/var/staged_system_apps/Freeform.app/vi.lproj/nlu.appintents/94dc0943260e4212a8df5c383ab53c8d.version`
- `/private/var/staged_system_apps/Freeform.app/zh_CN.lproj/nlu.appintents/c455ed5b4f2369cc363546824bce18c7.version`
- `/private/var/staged_system_apps/Freeform.app/zh_HK.lproj/nlu.appintents/5e1a0ae38e7ce608ddec9947639c1b00.version`
- `/private/var/staged_system_apps/Freeform.app/zh_TW.lproj/nlu.appintents/5fa4d84077ca6d582e2293f3cd78f630.version`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/74b3bf9df8715dd2888cee6604a383bb.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/ce5b6f77daa0aea4010fb98f376e9153.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/0c952563a64e29147a50024297ffe3a7.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/367cc40c7edb2c5680d78360bba4806b.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/24c03c5b50b471689d451cddbf75d37e.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/78b1d547e3717968f89870ebfb27fd59.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/1ae08c2408fe552328e08bf50ad52ad4.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/a07b491f3253e1f56d977b7e0031bff0.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/d3c713f0800d50fbe12bd0b305ffeaea.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/2be640189eae6daaf86f80d65513c793.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/e221bb5af8a40141d0889d6154cb959c.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/00649d3db96e892e6d2ebbddd6e8234b.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/762c0aca86a909a3bcbaee9ed87e67d5.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/73b836e446e8ca394b6c082852634b50.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/d75c1548f16b1c8806d92450a5e437b5.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/d4e6b825d11bfa81cdc8252da89470a9.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/5eb47c852e3e9e72c3595bb0ebc2490b.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/7f3f3a666de40822dc23e583f41766eb.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/9fbc78b1af4bd5d91b8eb75d36719d2e.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/a713eb2007479602ada32457c9c56b55.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/5ccf8f36168fa300e25ae408b66559db.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/0c827eaa1b61dd4093f607b70e1cbc77.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/9870cd17caf338af3334d2f32f783b9e.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/17a38bdc5678f06b5213cda045b4b4d3.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/7797c924c5fbcac2dc098b6158846ce4.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/ade4ce7da275956032a97201f81bd194.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/d7aa7b053b473e03942e40b5a5035441.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/9550ce918398d7dcbb3d46e9f373d7c4.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/01c4b5a6c168956293303de7632feb55.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/75cb30dc04a03b7252a94d20087c0514.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/94b2dfe80ca1b020c5c2b03edfec86e1.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/8c110853d906b4ead0cfccc676dbdcce.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/b45cb3d3a35dacb6ea444675deae965d.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/e634688856076e5468b690361aa6fd6f.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/c8d473d66bb04739ac8a7ac763277143.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/11cb72b77a7196f61d8824ae0f8c3676.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/0744b27ed78382cf2ead2244ce8ec20d.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/3a29f6ab31a91680a3a8fcf0bfb6d3f8.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/6c1cebfb500f021d00315c841ac9556d.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/9a0d8283325904ee5d013625f31c90d8.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/e1c8b3f773cb5385a1ca143d73f90810.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/7379f5ee2624e2d004f02caaf2b0be46.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/01df1c2089407725063d246e7dee77ac.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/33fbc17231f0f835e8d0c9996456bfa4.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/c760c152399b30f29d3d1b836ca547a7.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/3644c1f3a2ea76d6bf8d1e54e193057b.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/f7a4f75ea808e9000601eb78aa605101.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/582849a4fa7ca7f08e5af26240f368ea.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/e721857fe9bde111dad2702d2d0e6f00.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/751256afa09f24a61d9cfaad955518a3.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/8c83e0e275378c1b7a9df6e741cc76c2.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/099a0bd3ff33a779ac9ec0747c93667a.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Base.lproj/nlu.appintents/6148a4bd03a935c4f3f6c0e92f5e6c9f.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/68d8ce8e3063549b36f2ef396144811c.version`
- `/usr/libexec/memoryanalyticsd`

</details>

## Feature Flags

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### CoreTelephony.plist

>  `Domain/CoreTelephony.plist`

```diff

 		<key>DisclosureRequired</key>
 		<string>2d56a039-da9d-9afc-c249-0e18d5492708</string>
 	</dict>
-	<key>RCSPush</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>RegulatoryRestriction</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### GlobalDisclosures.plist

>  `GlobalDisclosures.plist`

```diff

 		<key>Disclosed</key>
 		<true/>
 	</dict>
+	<key>1b3196a9-6a20-4559-60fd-bb3743219ab3</key>
+	<dict>
+		<key>Disclosed</key>
+		<true/>
+	</dict>
 	<key>2298f8e4-f510-4776-b2c1-a85ea314b1f8</key>
 	<dict>
 		<key>Disclosed</key>

```


</details>

## EOF
