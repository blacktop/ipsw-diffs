# 26.2 (23C5044b) .vs 26.2 (23C52)

## IPSWs

- `iPhone18,1_26.2_23C5044b_Restore.ipsw`
- `iPhone18,1_26.2_23C52_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.2 *(23C5044b)* | 25.2.0 | 12377.62.9~13 | Wed, 12Nov2025 22:20:37 PST |
| 26.2 *(23C52)* | 25.2.0 | 12377.62.10~1 | Tue, 18Nov2025 21:11:04 PST |

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
-  UUID: 94B8D816-150A-32FD-9C24-2927C06F3263
+  UUID: CE2690D9-4B26-30AF-AE99-68898AB6F7BD
   Functions: 1223
   Symbols:   0
   CStrings:  1152
Functions:
~ __ZN23AppleAOPAudioController5startEP9IOService : 508 -> 528
CStrings:
+ "20:53:54"
+ "20:54:07"
+ "Nov 18 2025"
- "21:37:38"
- "21:37:48"
- "Nov 12 2025"

```

#### com.apple.driver.AppleUSBXDCIARM

>  `com.apple.driver.AppleUSBXDCIARM`

```diff

-847.62.1.0.0
+847.62.2.0.0
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x40ff
-  __TEXT.__os_log: 0x7403
-  __TEXT_EXEC.__text: 0x4224c
+  __TEXT.__cstring: 0x4123
+  __TEXT.__os_log: 0x7431
+  __TEXT_EXEC.__text: 0x421c4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0
-  __DATA_CONST.__auth_got: 0x330
+  __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
   __DATA_CONST.__const: 0x6ae0
   __DATA_CONST.__kalloc_type: 0x2c0
-  UUID: 111BE0A0-23FA-385E-A396-2185E2275DE4
+  UUID: ECCEBDCA-3D7D-37A3-97DB-7651B6B923ED
   Functions: 379
   Symbols:   0
-  CStrings:  333
+  CStrings:  331
 
Functions:
~ sub_fffffe000ab5626c -> sub_fffffe000ab4082c : 272 -> 264
~ sub_fffffe000ab5709c -> sub_fffffe000ab41654 : 532 -> 428
~ __ZN15AppleUSBXDCIARM15updatePortStateEj : 4184 -> 4232
~ __ZN15AppleUSBXDCIARM19cableChangeOccurredEP18IOTimerEventSource : 2004 -> 1936
~ __ZN15AppleUSBXDCIARM17hardwareExceptionEiPKc : 1452 -> 1448
CStrings:
+ "%s@%s: %s::%s: Port-%s@%d %s: connected: %d -> %d (no IOPortTransportState)\n"
+ "%s@%s: %s::%s: Port-%s@%d %s: connected: %d -> %d (tunneled: %d, role: %s, trm: %d:%d)\n"
+ "%s@%s: %s::%s: event did not change USB2 connected (%d) or USB3 connected (%d)\n"
- "%s@%s: %s::%s: Port-%s@%d %s: connected: %d (no IOPortTransportState)\n"
- "%s@%s: %s::%s: Port-%s@%d %s: connected: %d (tunneled: %d, role: %s, trm: %d:%d)\n"
- "%s@%s: %s::%s: Unauthorized protocol - %s %s\n"
- "USB2"
- "USB3"

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
-  UUID: 69605105-8CF1-3E28-9EE5-8C0D080EB165
+  UUID: C66EE8CE-7869-38FB-A6B9-103ACB18DEED
   Functions: 260
   Symbols:   0
-  CStrings:  235
+  CStrings:  236
 
CStrings:
+ "21:05:25"
+ "21:05:26"
+ "Nov 18 2025"
- "21:55:12"
- "Nov 12 2025"

```

#### com.apple.driver.corecapture

>  `com.apple.driver.corecapture`

```diff

   __TEXT.__os_log: 0x4257
   __TEXT.__const: 0x130
   __TEXT.__cstring: 0x2050
-  __TEXT_EXEC.__text: 0x28e5c
+  __TEXT_EXEC.__text: 0x28e24
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x308

   __DATA_CONST.__const: 0x7010
   __DATA_CONST.__kalloc_type: 0x10c0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 7243C9C1-E794-3EB4-86C6-9E992BA2D982
+  UUID: D45F88D3-029B-333F-B98A-0094BB267B32
   Functions: 877
   Symbols:   0
   CStrings:  657
Functions:
~ __ZN11CCIOService17ccForcePanic_ImplEbP8OSString : 120 -> 100
~ sub_fffffe000afe8220 -> sub_fffffe000afd274c : 100 -> 116
~ __ZN6CCPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptions : 7192 -> 7152
~ sub_fffffe000afec450 -> sub_fffffe000afd6964 : 100 -> 108
~ __ZN11CCIOService17ccForcePanic_ImplEbP8OSString : 196 -> 192
~ __ZN16CCPipeUserClient12initWithTaskEP4taskPvjP12OSDictionary : 372 -> 368
~ sub_fffffe000aff0344 -> sub_fffffe000afda858 : 12 -> 8
~ sub_fffffe000aff81ac -> sub_fffffe000afe26bc : 192 -> 188
~ sub_fffffe000b009550 -> sub_fffffe000aff3a5c : 100 -> 96

```

#### com.apple.filesystems.apfs

>  `com.apple.filesystems.apfs`

```diff

   __TEXT.__cstring: 0x4c59e
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
-  UUID: 3126D8D4-7C33-38B7-817F-8004426BE26D
+  UUID: 837175BE-6928-3BC7-ACFF-E4381BB07017
   Functions: 2320
   Symbols:   0
   CStrings:  6589
CStrings:
+ "2025/11/18"
+ "20:55:39"
+ "Nov 18 2025"
- "2025/11/12"
- "21:39:15"
- "Nov 12 2025"

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
-  UUID: CEF8A3FF-C310-3017-92E5-00E7598AC800
-  Functions: 298
+  UUID: F23AF9A2-FD2D-30C8-A06A-C73530FB3FB8
+  Functions: 299
   Symbols:   0
   CStrings:  389
 
Functions:
+ sub_fffffe0008cd6ed0
~ __ZN22AppleARMDMAAudioDevice13startInternalEP9IOServicexjPKjS3_S3_S3_ : 1280 -> 1300

```

#### com.apple.kernel

>  `com.apple.kernel`

```diff

-12377.62.9.0.0
-  __TEXT.__const: 0x35450
+12377.62.10.0.0
+  __TEXT.__const: 0x353a0
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x80266
+  __TEXT.__cstring: 0x7ca18
   __TEXT.__os_log: 0x3c5cb
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0x1177a8
+  __DATA_CONST.__const: 0x117738
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x14200
+  __DATA_CONST.__kalloc_type: 0x13f40
   __DATA_CONST.__assert: 0x8fc
   __DATA_CONST.__kalloc_var: 0x7b20
   __DATA_CONST.__exclaves_bt: 0x78
-  __DATA_CONST.__kern_brk_desc: 0x78
+  __DATA_CONST.__kern_brk_desc: 0x60
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x8b45c4
+  __TEXT_EXEC.__text: 0x8a1ea8
   __TEXT_EXEC.__hib_text: 0xf38
   __TEXT_BOOT_EXEC.__bootcode: 0x51d0
   __KLD.__text: 0x1638

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x3488
+  __KLDDATA.__const: 0x3458
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x17f79
-  __DATA.__lock_grp: 0x5bc8
+  __DATA.__lock_grp: 0x5b18
   __DATA.__percpu: 0x6f28
-  __DATA.__common: 0x6ec78
+  __DATA.__common: 0x6e9d8
   __DATA.__bss: 0x97228
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__static_if: 0x4d30
-  __BOOTDATA.__init_entry_set: 0x12990
+  __BOOTDATA.__static_if: 0x4c70
+  __BOOTDATA.__init_entry_set: 0x128e8
   __BOOTDATA.__init: 0x5b3c8
   __BOOTDATA.__static_ifinit: 0x8
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x471ae
-  UUID: 51F5806A-8A8E-362F-959A-A5BE0D80A1A0
-  Functions: 20763
+  UUID: F6D0BE58-5B4C-39B5-89D6-8CCE7D005882
+  Functions: 20560
   Symbols:   0
-  CStrings:  20283
+  CStrings:  19983
 
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

 2680.60.11.0.0
   __TEXT.__os_log: 0x2287
-  __TEXT.__const: 0x1db831
+  __TEXT.__const: 0x1db8b1
   __TEXT.__cstring: 0x713e
   __TEXT_EXEC.__text: 0x37c24
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x3818
   __DATA_CONST.__kalloc_type: 0xac0
   __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: C46EAE0B-1755-360F-84D9-97950D60AE40
+  UUID: BE623128-815C-3BF7-886D-4EA8DA524759
   Functions: 657
   Symbols:   0
   CStrings:  1327

```


</details>

## MachO

### ❌ Removed (2)

- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/usr/libexec/memoryanalyticsd`

### ⬆️ Updated (181)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/CheckerBoard.app/CheckerBoard](MACHOS/CheckerBoard.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
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
- [/Applications/HomeUIService.app/HomeUIService](MACHOS/HomeUIService.md)
- [/Applications/KaleidoscopePosterApp.app/Extensions/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster.md)
- [/Applications/KaleidoscopePosterApp.app/Extensions/KaleidoscopePoster.appex/NTKKaleidoscopeShaders.metallib](MACHOS/NTKKaleidoscopeShaders.metallib.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService](MACHOS/SoftwareUpdateUIService.md)
- [/Applications/SystemVoiceAssistant.app/SystemVoiceAssistant](MACHOS/SystemVoiceAssistant.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/System/Library/AccessibilityBundles/GAXBackboardServer.bundle/GAXBackboardServer](MACHOS/GAXBackboardServer.md)
- [/System/Library/Assistant/Plugins/activity.assistantBundle/activity](MACHOS/activity.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/HangHUD.app/HangHUD](MACHOS/HangHUD.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard](MACHOS/SpringBoard.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/AmbientSettingsAppIntentsExtension.appex/AmbientSettingsAppIntentsExtension](MACHOS/AmbientSettingsAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/CloudWorker.appex/CloudWorker](MACHOS/CloudWorker.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin](MACHOS/FedStatsMLHostPlugin.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA](MACHOS/FedStatsMLHostPluginClassA.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/FedStatsMLHostPluginClassB](MACHOS/FedStatsMLHostPluginClassB.md)
- [/System/Library/ExtensionKit/Extensions/InferenceExtension.appex/InferenceExtension](MACHOS/InferenceExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseAVExtension.appex/LighthouseAVExtension](MACHOS/LighthouseAVExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseAVShadowEval.appex/LighthouseAVShadowEval](MACHOS/LighthouseAVShadowEval.md)
- [/System/Library/ExtensionKit/Extensions/MCUIAppIntents.appex/MCUIAppIntents](MACHOS/MCUIAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/NewDeviceOutreachIntents_iOS.appex/NewDeviceOutreachIntents_iOS](MACHOS/NewDeviceOutreachIntents_iOS.md)
- [/System/Library/ExtensionKit/Extensions/NotificationsSettingsExtension.appex/NotificationsSettingsExtension](MACHOS/NotificationsSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/PFLASLAppEmbedding.appex/PFLASLAppEmbedding](MACHOS/PFLASLAppEmbedding.md)
- [/System/Library/ExtensionKit/Extensions/PFLASLArcadeRanking.appex/PFLASLArcadeRanking](MACHOS/PFLASLArcadeRanking.md)
- [/System/Library/ExtensionKit/Extensions/PFLASLArcadeRetention.appex/PFLASLArcadeRetention](MACHOS/PFLASLArcadeRetention.md)
- [/System/Library/ExtensionKit/Extensions/PFLASLExperimental.appex/PFLASLExperimental](MACHOS/PFLASLExperimental.md)
- [/System/Library/ExtensionKit/Extensions/PFLCSLAppStore.appex/PFLCSLAppStore](MACHOS/PFLCSLAppStore.md)
- [/System/Library/ExtensionKit/Extensions/PFLCSLAppStore2.appex/PFLCSLAppStore2](MACHOS/PFLCSLAppStore2.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/SiriTurnRestatementExtension.appex/SiriTurnRestatementExtension](MACHOS/SiriTurnRestatementExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/Frameworks/CoreImage.framework/photo_style_archive_bin.metallib](MACHOS/photo_style_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/redeye_repair_archive_bin.metallib](MACHOS/redeye_repair_archive_bin.metallib.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/WatchKit.framework/Support/companionappd](MACHOS/companionappd.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/DigitalTouchBalloonProvider.bundle/DigitalTouchBalloonProvider](MACHOS/DigitalTouchBalloonProvider.md)
- [/System/Library/NanoTimeKit/FaceBundles/KaleidoscopeFaceBundle.bundle/NTKKaleidoscopeShaders.metallib](MACHOS/NTKKaleidoscopeShaders.metallib.md)
- [/System/Library/PreferenceBundles/AmbientSettings.bundle/AmbientSettings](MACHOS/AmbientSettings.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](MACHOS/KeyboardSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PreferenceBundles/Privacy/ClipServicesSettings.bundle/ClipServicesSettings](MACHOS/ClipServicesSettings.md)
- [/System/Library/PreferenceBundles/StorageSettings.bundle/StorageSettings](MACHOS/StorageSettings.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/VisionCompanionSettings.bundle/VisionCompanionSettings](MACHOS/VisionCompanionSettings.md)
- [/System/Library/PreferenceBundles/VoiceMemosSettings.bundle/VoiceMemosSettings](MACHOS/VoiceMemosSettings.md)
- [/System/Library/PrivateFrameworks/ACTFramework.framework/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/PrivateFrameworks/ACTFramework.framework/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/deflicker-binary-applegpu_g18p.metallib](MACHOS/deflicker-binary-applegpu_g18p.metallib.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/deflicker-binary.metallib](MACHOS/deflicker-binary.metallib.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/activityawardsd](MACHOS/activityawardsd.md)
- [/System/Library/PrivateFrameworks/AmbientUI.framework/PlugIns/InfographPoster.appex/InfographPoster](MACHOS/InfographPoster.md)
- [/System/Library/PrivateFrameworks/AppConduit.framework/Support/appconduitd](MACHOS/appconduitd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/BWPreviewStitcherNodeCoreImageArchive_bin.metallib](MACHOS/BWPreviewStitcherNodeCoreImageArchive_bin.metallib.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/FRSVCoreImageArchive_bin.metallib](MACHOS/FRSVCoreImageArchive_bin.metallib.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/PlugIns/com.apple.CloudDocsUI.CloudSharing.appex/com.apple.CloudDocsUI.CloudSharing](MACHOS/com.apple.CloudDocsUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/Support/companioncamerad](MACHOS/companioncamerad.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/default-binaryarchive.metallib](MACHOS/default-binaryarchive.metallib.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/mxi-binaryarchive.metallib](MACHOS/mxi-binaryarchive.metallib.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced](MACHOS/CoreThreadCommissionerServiced.md)
- [/System/Library/PrivateFrameworks/CoreTime.framework/TimeSources/LinkSource.bundle/LinkSource](MACHOS/LinkSource.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd](MACHOS/ecosystemanalyticsd.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension](MACHOS/HangLogsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension](MACHOS/PerformanceLoggingDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/Support/homeeventsd](MACHOS/homeeventsd.md)
- [/System/Library/PrivateFrameworks/JetCore.framework/Support/jetpackassetd](MACHOS/jetpackassetd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/NanoBackup.framework/nanobackupd](MACHOS/nanobackupd.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/companionfindlocallyd](MACHOS/companionfindlocallyd.md)
- [/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/nanoprefsyncd](MACHOS/nanoprefsyncd.md)
- [/System/Library/PrivateFrameworks/NanoUniverse.framework/NUNICalliopeShadersCompanion.metallib](MACHOS/NUNICalliopeShadersCompanion.metallib.md)
- [/System/Library/PrivateFrameworks/PairedUnlock.framework/pairedunlockd](MACHOS/pairedunlockd.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService](MACHOS/PersonalizedSensingService.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/Versions/A/Resources/privacyaccountingd](MACHOS/privacyaccountingd.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/Support/subridged](MACHOS/subridged.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin](MACHOS/SoftwareUpdateServicesUIPlugin.md)
- [/System/Library/PrivateFrameworks/TCC.framework/Support/tccd](MACHOS/tccd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/metal_libraries/binary.metallib](MACHOS/binary.metallib.md)
- [/System/Library/PrivateFrameworks/Weather.framework/Support/nanoweatherprefsd](MACHOS/nanoweatherprefsd.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/Settings/DefaultApps/DefaultCallingAppsSettings.plugin/DefaultCallingAppsSettings](MACHOS/DefaultCallingAppsSettings.md)
- [/System/Library/SyncBundles/Apps.syncBundle/Apps](MACHOS/Apps.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/ColourConstancyV1.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/DepthProcessorV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/STF.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/SmartStyleV1.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/Calculator.app/PlugIns/CalculatorWidget.appex/CalculatorWidget](MACHOS/CalculatorWidget.md)
- [/private/var/staged_system_apps/MobileNotes.app/Extensions/NotesAppMigrationExtension.appex/NotesAppMigrationExtension](MACHOS/NotesAppMigrationExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/RecordWidgetExtension.appex/RecordWidgetExtension](MACHOS/RecordWidgetExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosSettingsWidgetExtension.appex/VoiceMemosSettingsWidgetExtension](MACHOS/VoiceMemosSettingsWidgetExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/usr/lib/libmobileassetd.dylib](MACHOS/libmobileassetd.dylib.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/checkpointd](MACHOS/checkpointd.md)
- [/usr/libexec/companion_proxy](MACHOS/companion_proxy.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/fmflocatord](MACHOS/fmflocatord.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/mobileassetd](MACHOS/mobileassetd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/perfdiagsselfenabled](MACHOS/perfdiagsselfenabled.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/resourcegrabberd](MACHOS/resourcegrabberd.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/sensorkitd](MACHOS/sensorkitd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/signpost_reporter](MACHOS/signpost_reporter.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/terminusd](MACHOS/terminusd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/tzd](MACHOS/tzd.md)
- [/usr/libexec/uarpassetmanagerd](MACHOS/uarpassetmanagerd.md)
- [/usr/libexec/wcd](MACHOS/wcd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (1)

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
-  UUID: 8F96AA2E-2AAC-3589-8449-7D270552A5D8
+  UUID: AF935BA4-F481-3022-AC11-B5A297C06BEC
   Functions: 1212
   Symbols:   1703
   CStrings:  2640

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.2 *(23C5044b)* | iBoot-13822.62.4 |
| 26.2 *(23C52)* | iBoot-13822.62.5 |

#### 🆕 NEW (1)

<details>
  <summary><i>View NEW</i></summary>

##### `iboot_blob33.bin`
  - `root@Nov 08 2025@17:57:48~.release`

</details>

#### ❌ Removed (1)

<details>
  <summary><i>View Removed</i></summary>

##### `iboot_blob33.bin`
  - `root@Nov 11 2025@22:21:25~.release`

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.2 *(23C5044b)* | 623.1.14.10.6 |
| 26.2 *(23C52)* | 623.1.14.10.9 |

### Dylibs

#### 🆕 NEW (2)

- `/System/Library/PrivateFrameworks/DownloadAssertions.framework/DownloadAssertions`
- `/System/Library/PrivateFrameworks/DownloadObtainer.framework/DownloadObtainer`

#### ⬆️ Updated (208)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/Moments.axbundle/Moments](DYLIBS/Moments.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/AddressBookUI.framework/AddressBookUI](DYLIBS/AddressBookUI.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/Frameworks/PushKit.framework/PushKit](DYLIBS/PushKit.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings](DYLIBS/BluetoothSettings.md)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing](DYLIBS/ASEProcessing.md)
- [/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings](DYLIBS/AUDeveloperSettings.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon](DYLIBS/ActivityAchievementsDaemon.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsCore.framework/ActivityAwardsCore](DYLIBS/ActivityAwardsCore.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/ActivityAwardsServices](DYLIBS/ActivityAwardsServices.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon](DYLIBS/AdPlatformsCommon.md)
- [/System/Library/PrivateFrameworks/AmbientUI.framework/AmbientUI](DYLIBS/AmbientUI.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppSystemSettingsUI.framework/AppSystemSettingsUI](DYLIBS/AppSystemSettingsUI.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery](DYLIBS/AppleMediaDiscovery.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIKitInternal.framework/AppleMediaServicesUIKitInternal](DYLIBS/AppleMediaServicesUIKitInternal.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/BrookServices.framework/BrookServices](DYLIBS/BrookServices.md)
- [/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard](DYLIBS/BulletinBoard.md)
- [/System/Library/PrivateFrameworks/CentauriDiagnostic.framework/CentauriDiagnostic](DYLIBS/CentauriDiagnostic.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer](DYLIBS/CiderAudioServer.md)
- [/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices](DYLIBS/ClipServices.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI](DYLIBS/CloudDocsUI.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera](DYLIBS/CompanionCamera.md)
- [/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync](DYLIBS/CompanionSync.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore](DYLIBS/CoordinationCore.md)
- [/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon](DYLIBS/CoreCaptureDaemon.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/DesignLibrary.framework/DesignLibrary](DYLIBS/DesignLibrary.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon](DYLIBS/DiagnosticExtensionsDaemon.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/EchoRelay.framework/EchoRelay](DYLIBS/EchoRelay.md)
- [/System/Library/PrivateFrameworks/FMCore.framework/FMCore](DYLIBS/FMCore.md)
- [/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore](DYLIBS/FedStatsPluginCore.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices](DYLIBS/FrontBoardServices.md)
- [/System/Library/PrivateFrameworks/FusionTracker.framework/FusionTracker](DYLIBS/FusionTracker.md)
- [/System/Library/PrivateFrameworks/GPUToolsReplay.framework/GPUToolsReplay](DYLIBS/GPUToolsReplay.md)
- [/System/Library/PrivateFrameworks/GameStoreKit.framework/GameStoreKit](DYLIBS/GameStoreKit.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HangTracerSettingsClient.framework/HangTracerSettingsClient](DYLIBS/HangTracerSettingsClient.md)
- [/System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager](DYLIBS/HeadphoneManager.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettings.framework/HeadphoneSettings](DYLIBS/HeadphoneSettings.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettingsUI.framework/HeadphoneSettingsUI](DYLIBS/HeadphoneSettingsUI.md)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
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
- [/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor](DYLIBS/KnowledgeMonitor.md)
- [/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling](DYLIBS/LanguageModeling.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LighthouseServicesAnalyticsFramework.framework/LighthouseServicesAnalyticsFramework](DYLIBS/LighthouseServicesAnalyticsFramework.md)
- [/System/Library/PrivateFrameworks/MDM.framework/MDM](DYLIBS/MDM.md)
- [/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport](DYLIBS/MTLToolsDeviceSupport.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MomentsIntelligence.framework/MomentsIntelligence](DYLIBS/MomentsIntelligence.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/NanoLeash](DYLIBS/NanoLeash.md)
- [/System/Library/PrivateFrameworks/NanoMailKitServer.framework/NanoMailKitServer](DYLIBS/NanoMailKitServer.md)
- [/System/Library/PrivateFrameworks/NanoSmartStackControlUI.framework/NanoSmartStackControlUI](DYLIBS/NanoSmartStackControlUI.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/ODDIFramework.framework/ODDIFramework](DYLIBS/ODDIFramework.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PostSiriEngagement.framework/PostSiriEngagement](DYLIBS/PostSiriEngagement.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore](DYLIBS/PrivacyDisclosureCore.md)
- [/System/Library/PrivateFrameworks/ProDisplayLibrary.framework/ProDisplayLibrary](DYLIBS/ProDisplayLibrary.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine](DYLIBS/RelevanceEngine.md)
- [/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/PrivateFrameworks/SOS.framework/SOS](DYLIBS/SOS.md)
- [/System/Library/PrivateFrameworks/SchoolTime.framework/SchoolTime](DYLIBS/SchoolTime.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SensingAlgsPadHostServiceJ8xx.framework/SensingAlgsPadHostServiceJ8xx](DYLIBS/SensingAlgsPadHostServiceJ8xx.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensingAlgsTouchButtonHost.framework/SensingAlgsTouchButtonHost](DYLIBS/SensingAlgsTouchButtonHost.md)
- [/System/Library/PrivateFrameworks/Sentry.framework/Sentry](DYLIBS/Sentry.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTaskEngagement.framework/SiriTaskEngagement](DYLIBS/SiriTaskEngagement.md)
- [/System/Library/PrivateFrameworks/SiriTurnRestatement.framework/SiriTurnRestatement](DYLIBS/SiriTurnRestatement.md)
- [/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager](DYLIBS/SiriTurnTakingManager.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI](DYLIBS/SoftwareUpdateServicesUI.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices.md)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore](DYLIBS/StatusKitAgentCore.md)
- [/System/Library/PrivateFrameworks/StorageData.framework/StorageData](DYLIBS/StorageData.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligenceUI.framework/VisualIntelligenceUI](DYLIBS/VisualIntelligenceUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/Widgets.framework/Widgets](DYLIBS/Widgets.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/VideoCodecs/VCPHEVC.videocodec](DYLIBS/VCPHEVC.videocodec.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib.md)
- [/usr/lib/libchannel.dylib](DYLIBS/libchannel.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/system/libsystem_containermanager.dylib](DYLIBS/libsystem_containermanager.dylib.md)

</details>

## Files

### 🆕 New

#### filesystem (110)

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
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/7f50a81a71f8ff6cebbf2d151474b0256a253146.asset/AssetData/empty.txt`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/7f50a81a71f8ff6cebbf2d151474b0256a253146.asset/Info.plist`
- `/System/Library/PrivateFrameworks/DownloadAssertions.framework/Info.plist`
- `/System/Library/PrivateFrameworks/DownloadAssertions.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/DownloadObtainer.framework/Info.plist`
- `/System/Library/PrivateFrameworks/DownloadObtainer.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/FMFindingUI.framework/Localizable-Grape.loctable`
- `/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/DeviceConfig-Seed.loctable`
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
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/084ef9be68e105fdfbe048a3e0efb392.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/5ecacdfc08da459d58519c0fec680a8b.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/af4c52bd88a7c8caaadf6c9b6722ee40.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/4da5a9761d11dbeeace29e2e42d31d61.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/90edb30cd97638d3fe825b252fa528a3.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/1bb2dc3633d794ad3d4533eeed2404b6.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/087a376701052c059f234ccc980d7524.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/b7161dded8798a557d6a57613107570d.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/b8ae88c2fd48b1e9bba177e5f795fe8b.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/162a9b6d9f15c656f0f711855b88fec7.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/f71054a891c3a526dac5fda27fe66beb.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/c4d1f39cf275b95cefa675694a8dec6d.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/ca24774caba9bd12f39a73f30deb98e1.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/3e7d533ba723ac71bd981a6b3d6a6268.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/9e3a3bb54faddddc78e3438c495c6585.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/ddbef13b7813d9d1ab7365512e37dd13.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/37c9c7c5cd932b934e7abdc05b37c0b8.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/491628fb457f4954e5f54133d52cbde2.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/8020e3c614d7343ab40090850e0ee283.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/0c1629d90331b6c14f29146b27147595.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/efad1cd3cb87143d416c4dc1e257ca07.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/ae736d76972349d00f8cc894d85f142c.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/bbc88b2733887b51c39914c5edcd4d7d.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/f74fa3674dc6ad647638748349cfcd47.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/187adc95324db6ccf53764386082c35a.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/a3de17c0ee64c28f867d55bdb25ae152.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/00a2d2bfd6c9dd476424fb6230629a8b.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/3b909b3911c18d534d80fe341dc57469.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/e84a785195dd0f1e3fd7ebbb2efabeba.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/fc6fe5d465832ed972f1fdf11e061114.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/d8d17c4cdb21d6dd1e8cb0c4517280ce.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/f89b72cb414bf33cb31e905941fa66df.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/79155b29325b2f75776cb7c83ac0700e.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/231295046ec8168080cf8c242cf8589e.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/c2d17dad2be26171f37e1c6a8a9e68ed.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/45349a08c9faa635b5701584f48b618c.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/41efc1385351077befb07f237539a8ae.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/47ea81e090a25f37451ac0749191311d.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/6b966696b3476d0f349d2b0ab50fbece.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/2e343987a16d060ea6d26ace0a7ef609.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/5eccb21eb195a83f018e7a6144062c23.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/68ae1947a538f1fe6c82823e2798c1c6.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/fbbfd5ea577e81fd9ec4365e7cadefbf.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/00125f0caea0c126b9bfbfb320640342.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/876601cfe0e129013afa46b766a0dcb2.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/e51b9661e91912d37fff17a66f0e84a9.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/b8860b94b639e7fd2839c07bdda7f3a0.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/0af6b34440bc9c91d0f3740025930e9e.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/69012ea16ea153c5ceb350db24b24024.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/a856c53dc391d2b250d09c82f26426bb.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/9515841e1495859ae9f41265b0f5a48e.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/d8860ce91cc128c0af5d292a73058bd7.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/cbff1442ad29648a4e883cf34e4ca19c.version`
- `/usr/standalone/firmware/nfrestore/firmware/fw/SN450V_FW_A1_01_01_009_rev164126.bin`
- `/usr/standalone/firmware/nfrestore/firmware/rf/SN450V_FW_A1_01_01_009_rev164126.plist`
- `/usr/standalone/firmware/nfrestore/firmware/rf/SN450V_FW_A1_01_01_809_rev164319.plist`

</details>

### ❌ Removed

#### filesystem (85)

<details>
  <summary><i>View Files</i></summary>

- `/Applications/DisplayCal.app/Contents/Resources/kn.lproj/.dat.nosync106a.Agbh3r`
- `/System/Library/ExtensionKit/ExtensionPoints/com.apple.BrowserEngine.Development.appexpt`
- `/System/Library/Frameworks/SystemConfiguration.framework/get-mobility-info`
- `/System/Library/LaunchDaemons/com.apple.memoryanalyticsd.plist`
- `/System/Library/LaunchDaemons/com.apple.prngseedd.plist`
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
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/Info.plist`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/Home.framework/com.apple.Home.framework.plist`
- `/System/Library/PrivateFrameworks/Home.framework/com.apple.Home.plist`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/35d044563b09de446d83c3c8625da59e.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/d4ff534b935e4c3905cedceed7f2a12d.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/8f9f86d7bf249f69e75d78bc717adfbb.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/8e10c855973f9daaab49e7adef125f68.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/228e7628078dd35aa786c29df8abefa8.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/d012d3e78ea429c71d533cffac27a3b8.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/30b06c086b3b31bec5d0058281b5cbfe.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/02a3b2194528f52ee2f20369b97bfe2a.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/5bd0cb21d31d1957013db8bb6573033d.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/e6088184c07e8e8a197ded669acd147a.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/8519642ab28548f06d1ee6b96acb69f8.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/8b24f66e6b701739b3a6088b452b183a.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/dbf90c995fc678b28d8f1a739d5a127d.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/cf9e0ed5cb1ba5e749b3f5fcfe834248.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/5c9615ac9f8633632b29fe843f1be1ab.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/931d5890419c7751a1f3c7f1fa0d921e.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/5316a2f684bf634130eda4173bec7250.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/b81475dd025e8963787aa6cbb2a627f1.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/f1b97bcbb884d52d61a0c829075aef7f.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/a196cebdd51906975a6380c60409d424.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/a404af291bdc9f70d97d2c0a1ffa8eca.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/d326c42ad9df505228214e55ac248db9.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/3d1479be1080db4e785e249552e95bb6.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/1ef842b7b0c5bdebb166e1bee304bebd.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/6401f6a8c4f7e49214fc9dd0fcf6025c.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/3ada5fbdcf42bbcc57ac986ea20cbaff.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/7b8b42ccea6fa887989d18395bd6c3e3.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/1a0fb6712cafc1745c140d6be2ef9a71.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/65c1494c75ee2e76c064acb9bbe48216.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/8837d713fb6f645f2e2f5ff92528ae22.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/77c4c890c9c4560f380fbc9654a917ef.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/520f49e537354e65ab6dd822da61bc4c.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/c9a1d280c44b543d123c6d9912fb3282.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/647a98c0780da94e2b6b6c8d8f317d79.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/eaea4fef0efcba846128ff577cea968f.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/9f4993f69260bcd7b626c9cc124c513b.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/aabb4051313a500163838c8d10de963b.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/f9a661d90f5106deadc29674db8d3944.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/d4b3e4d3524c31016031e5f62e92b394.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/bd9b6a8a3697087868e9ac7d6f4973cd.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/18d307e2d863f2856f104d43f259a73c.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/3b5182ba182b81b125d729db887456ff.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/fb57f927703761d30920e3d280c6f8e2.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/e7be23e8deb0c3bfad13834624f61eb1.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/0bde3edf4bd411c0a6265758d75c0527.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/6ecf3dab9126ac8eb1b98c9abbd363ef.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/a5e67b4adcfd84dba41021e1bc488b85.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/e992e7f0c9b187c2ca88a7553c163eb6.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/e2dab6d9e99eb721554c3a6ae86b7f75.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/0f1790bffad222e6c1f8c2c1323e15d2.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/73db6c36b153517d789ac87bba166e6b.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/8c65040c19e4cc25b08fa2d0ce13cc6a.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/92d5335e2c6100d4235f3f7ef7600ff4.version`
- `/usr/libexec/memoryanalyticsd`

</details>

## Feature Flags

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAccountUI.plist

>  `Domain/AppleAccountUI.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>PrivacyReprompt</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>ShowDataclassDetailFromApps</key>
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
