# 18.2 (22C5142a) .vs 18.2 (22C150)

## IPSWs

- `iPhone17,1_18.2_22C5142a_Restore.ipsw`
- `iPhone17,1_18.2_22C150_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.2 *(22C5142a)* | 24.2.0 | 11215.62.3~2 | Thu, 14Nov2024 22:18:12 PST |
| 18.2 *(22C150)* | 24.2.0 | 11215.62.3~1 | Thu, 14Nov2024 22:55:26 PST |

### Kexts

#### ❌ Removed (1)

- `com.apple.kec.AppleEncryptedArchive`

#### ⬆️ Updated (8)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.AppleAOPAudio`

```diff

   __TEXT.__cstring: 0xc591
   __TEXT.__const: 0x136
   __TEXT.__os_log: 0xf
-  __TEXT_EXEC.__text: 0x32934
+  __TEXT_EXEC.__text: 0x32948
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2f0
   __DATA.__common: 0x660
   __DATA.__bss: 0x49
-  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0xe8
CStrings:
+ "20:55:13"
+ "20:55:28"
+ "Nov 21 2024"
- "22:51:57"
- "22:51:58"
- "Nov 14 2024"

```

>  `com.apple.driver.AppleAVD`

```diff

 808.0.0.0.0
-  __TEXT.__const: 0x9a8c9
-  __TEXT.__cstring: 0x5277
-  __TEXT.__os_log: 0x12f18
-  __TEXT_EXEC.__text: 0x45658
+  __TEXT.__const: 0xc5ac9
+  __TEXT.__os_log: 0x143ec
+  __TEXT.__cstring: 0x5391
+  __TEXT_EXEC.__text: 0x4bd48
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12dc
   __DATA.__common: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x2d60
-  __DATA_CONST.__kalloc_var: 0xbe0
-  __DATA_CONST.__kalloc_type: 0x2600
-  Functions: 1426
+  __DATA_CONST.__const: 0x3270
+  __DATA_CONST.__kalloc_type: 0x2a00
+  __DATA_CONST.__kalloc_var: 0xc80
+  Functions: 1576
   Symbols:   0
-  CStrings:  1459
+  CStrings:  1472

CStrings:
+ "%s(): DKey physical addr = 0x%llx\n"
+ "122211112112112"
+ "CAvdApCommHibiscus"
+ "CAvdApCommThyme"
+ "CAvdMcpuHibiscus"
+ "CAvdMcpuThyme"
+ "site.CAvdApCommHibiscus"
+ "site.CAvdApCommThyme"
+ "site.CAvdMcpuHibiscus"
+ "site.CAvdMcpuThyme"
+ "site.CAvdWrapCtrlHibiscus"
+ "site.CPriorityQueueHibiscus"
+ "site.CPriorityQueueThyme"

```

>  `com.apple.driver.AppleOLYHAL`

```diff

 405.16.0.0.0
   __TEXT.__const: 0x7a8
   __TEXT.__cstring: 0x4607
-  __TEXT_EXEC.__text: 0x1ca2c
+  __TEXT_EXEC.__text: 0x1ca44
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

```

>  `com.apple.driver.corecapture`

```diff

   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x1ec9
   __TEXT.__os_log: 0x4094
-  __TEXT_EXEC.__text: 0x26f08
+  __TEXT_EXEC.__text: 0x26f14
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x2e0

```

>  `com.apple.filesystems.apfs`

```diff

 2317.60.23.0.1
   __TEXT.__const: 0x790
-  __TEXT.__cstring: 0x48a06
+  __TEXT.__cstring: 0x489fd
   __TEXT_EXEC.__text: 0x13b2a8
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x698
+  __DATA.__data: 0x690
   __DATA.__bss: 0xc60
   __DATA_CONST.__auth_got: 0x10e0
   __DATA_CONST.__got: 0x1b0

   __DATA_CONST.__kalloc_var: 0x28a0
   Functions: 2278
   Symbols:   0
-  CStrings:  6311
+  CStrings:  6310

CStrings:
+ "22:46:25"
- "22:54:28"
- "22:54:29"

```

>  `com.apple.iokit.AppleARMIISAudio`

```diff

   __TEXT.__os_log: 0x282b
   __TEXT.__cstring: 0x2e33
   __TEXT.__const: 0xa8
-  __TEXT_EXEC.__text: 0x15a8c
+  __TEXT_EXEC.__text: 0x15ac4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

```

>  `com.apple.kernel`

```diff

 11215.62.3.0.0
-  __TEXT.__const: 0x34270
+  __TEXT.__const: 0x341b0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x72dd0
+  __TEXT.__cstring: 0x6f8a3
   __TEXT.__os_log: 0x276f6
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2c8
-  __DATA_CONST.__const: 0xa63b8
+  __DATA_CONST.__const: 0xa61b8
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x13680
+  __DATA_CONST.__kalloc_type: 0x133c0
   __DATA_CONST.__kalloc_var: 0x7e90
   __DATA_CONST.__exclaves_bt: 0x60
-  __DATA_CONST.__brk_desc: 0x78
+  __DATA_CONST.__brk_desc: 0x60
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc68
-  __TEXT_EXEC.__text: 0x7f3350
+  __TEXT_EXEC.__text: 0x7dfe34
   __TEXT_BOOT_EXEC.__bootcode: 0x4cd8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x18441
-  __DATA.__lock_grp: 0x5908
+  __DATA.__data: 0x17c41
+  __DATA.__lock_grp: 0x5858
   __DATA.__percpu: 0x6e30
-  __DATA.__common: 0x586e0
+  __DATA.__common: 0x58400
   __DATA.__bss: 0x95748
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x10c20
+  __BOOTDATA.__init_entry_set: 0x10b18
   __BOOTDATA.__init: 0x5b138
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x45b4f
-  Functions: 20495
+  Functions: 20282
   Symbols:   0
-  CStrings:  17257
+  CStrings:  16972

CStrings:
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
- "%s-%s-%d.%d.%d.%d-%x%s"
- "%s/%s"
- "%s: cannot exclude region starting at %p with size %zu (not page aligned) @%s:%d"
- "%s: cannot exclude region starting at %p with size %zu (zero or overflowing size) @%s:%d"
- "%s: context allocation failure\n"
- "%s: no task is set\n"
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
- "111222212222222222222112"
- "121212112"
- "; UUID="
- "; stext="
- "A dump server was not specified in the boot-args, terminating kernel core dump.\n"
- "Attempting connection to panic server configured at IP %s, port %d\n"
- "Boot-args specify %d MB kernel corefile\n"
- "Corefile is not yet initialized. Cannot write a coredump to disk\n"
- "Couldn't retrieve volume status. Error %d\n"
- "Detected remote error, terminating...\n"
- "Detected stale/invalid seq num. Expected: %d, received %d\n"
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
- "No contact in %d seconds\n"
- "Opened corefile of size %llu MB\n"
- "Opened file %s, size %qd, extents %ld, maxio %qx ssd %d\n"
- "Original panic string:\n"
- "Preferred Block Size"
- "Recorded panic region in corefile at offset 0x%llx, compressed to %llu bytes\n"
- "Resolved %s's (or proxy's) link level address\n"
- "Routing through specified router IP %s (%d)\n"
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
- "coredump"
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
- "corefile"
- "corefile path selection in device-tree is not one of the allowed values: %s, Using default %s\n"
- "corefile path selection in device-tree was set to: %s (value: %s)\n"
- "corefile_size_mb"
- "custom"
- "drivercorefile"
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
- "kdp_send: packet too large (%d > %u)"
- "kdp_send_crashdump_data returned 0x%x\n"
- "kdp_send_crashdump_pkt failed with error %d\n"
- "kdp_set_dump_info: Skipping invalid panicd port %d (using %d)\n"
- "kern ver str"
- "kern_coredump_routine"
- "kern_dump_init"
- "kern_dump_save_note_data"
- "kern_open_file_for_direct_io took %qd ms\n"
- "kernel-core-dump-location"
- "load binary"
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
- "site.IOPolledFileIOVars"
- "site.struct kern_userspace_coredump_context"
- "site.typeof(*data)"
- "site.typeof(*region)"
- "skipping local kernel core because core file could not be opened prior to panic (mode : 0x%x, error : 0x%x)\n"
- "skipping local kernel core because the SPTM is in INTERRUPTED state and can't support core dump generation\n"
- "skipping local kernel core because the SPTM is in PANIC state and can't support core dump generation\n"
- "sugid_coredump"
- "systemlog"
- "user_dump_init"
- "user_dump_save_seg_descriptions"
- "user_dump_save_segment_data"
- "user_dump_save_summary"
- "write to"
- "xnu"
- "xnu-"

```

>  `com.apple.security.sandbox`

```diff

 2401.60.113.0.0
-  __TEXT.__const: 0x18e4e9
+  __TEXT.__const: 0x18e559
   __TEXT.__cstring: 0x70d3
   __TEXT.__os_log: 0x20a1
   __TEXT_EXEC.__text: 0x3174c

```

</details>

## MachO

### 🆕 NEW (2)

- `/System/Library/ExtensionKit/Extensions/ConditionalEngineAppIntentsExtension.appex/ConditionalEngineAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/ConditionalEngineLighthouseExtension.appex/ConditionalEngineLighthouseExtension`

### ❌ Removed (2)

- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/usr/libexec/memoryanalyticsd`

### ⬆️ Updated (322)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/ActivityProgressUI.app/ActivityProgressUI](MACHOS/ActivityProgressUI.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/Applications/AutoSettings.app/AutoSettings](MACHOS/AutoSettings.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsReporter.app/DiagnosticsReporter](MACHOS/DiagnosticsReporter.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004](MACHOS/Diagnostic-7004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185](MACHOS/Diagnostic-8185.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268](MACHOS/Diagnostic-8268.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340](MACHOS/Diagnostic-8340.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343](MACHOS/Diagnostic-8343.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006](MACHOS/Diagnostic-9006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008](MACHOS/Diagnostic-9008.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010](MACHOS/Diagnostic-9010.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods](MACHOS/SystemReport-AirPods.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-BatteryCase.appex/SystemReport-BatteryCase](MACHOS/SystemReport-BatteryCase.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport](MACHOS/SystemReport.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/HealthENLauncher.app/HealthENLauncher](MACHOS/HealthENLauncher.md)
- [/Applications/HomeCaptiveViewService.app/HomeCaptiveViewService](MACHOS/HomeCaptiveViewService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/MTLReplayer.app/Frameworks/MTLReplayController.framework/MTLReplayController](MACHOS/MTLReplayController.md)
- [/Applications/MagnifierAngel.app/MagnifierAngel](MACHOS/MagnifierAngel.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/Sidecar.app/Sidecar](MACHOS/Sidecar.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/System/ExclaveKit/System/Library/Frameworks/MobileAssetExclaveComponent.framework/MobileAssetExclaveComponent](MACHOS/MobileAssetExclaveComponent.md)
- [/System/ExclaveKit/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](MACHOS/SoundAnalysis.md)
- [/System/ExclaveKit/System/Library/Frameworks/T8140_IR_ISP_EK_Component.framework/T8140_IR_ISP_EK_Component](MACHOS/T8140_IR_ISP_EK_Component.md)
- [/System/ExclaveKit/System/Library/Frameworks/Vision.framework/Vision](MACHOS/Vision.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](MACHOS/CollectionsInternal.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/SpeakerRecognitionKit.framework/SpeakerRecognitionKit](MACHOS/SpeakerRecognitionKit.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam](MACHOS/Tightbeam.md)
- [/System/ExclaveKit/usr/lib/swift/libswiftCore.dylib](MACHOS/libswiftCore.dylib.md)
- [/System/Library/Accounts/Notification/GroupKitAccountNotification.bundle/GroupKitAccountNotification](MACHOS/GroupKitAccountNotification.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CAMRootFlowPlugin.bundle/CAMRootFlowPlugin](MACHOS/CAMRootFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Assistant/Plugins/activity.assistantBundle/activity](MACHOS/activity.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/HangHUD.app/HangHUD](MACHOS/HangHUD.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/MobileAsset.migrator/MobileAsset](MACHOS/MobileAsset.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DisplayAndBrightnessSettingsExtension.appex/DisplayAndBrightnessSettingsExtension](MACHOS/DisplayAndBrightnessSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents](MACHOS/FamilyIntents.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension](MACHOS/GenerativeAssistantExtension.md)
- [/System/Library/ExtensionKit/Extensions/KeyboardSettingsExtension.appex/KeyboardSettingsExtension](MACHOS/KeyboardSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MKRemoteUI.appex/MKRemoteUI](MACHOS/MKRemoteUI.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin](MACHOS/PrivateEvolutionPlugin.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension](MACHOS/ScreenTimeAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension](MACHOS/SearchToolExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/DigitalTouchBalloonProvider.bundle/DigitalTouchBalloonProvider](MACHOS/DigitalTouchBalloonProvider.md)
- [/System/Library/NanoPreferenceBundles/General/CSLCompanionLiveActivitiesSettings.bundle/CSLCompanionLiveActivitiesSettings](MACHOS/CSLCompanionLiveActivitiesSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/CompanionAutoLaunchSettings](MACHOS/CompanionAutoLaunchSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings](MACHOS/AirDropSettings.md)
- [/System/Library/PreferenceBundles/AppClipDeveloperSettings.bundle/AppClipDeveloperSettings](MACHOS/AppClipDeveloperSettings.md)
- [/System/Library/PreferenceBundles/DefaultAppsSettingsUIPlugin.bundle/DefaultAppsSettingsUIPlugin](MACHOS/DefaultAppsSettingsUIPlugin.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/VoiceControlSettings.bundle/VoiceControlSettings](MACHOS/VoiceControlSettings.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/PlugIns/com.apple.CloudDocsUI.CloudSharing.appex/com.apple.CloudDocsUI.CloudSharing](MACHOS/com.apple.CloudDocsUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced](MACHOS/CoreThreadCommissionerServiced.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd](MACHOS/ecosystemanalyticsd.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient](MACHOS/finhealthclient.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension](MACHOS/HangLogsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension](MACHOS/PerformanceLoggingDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService](MACHOS/IDSBlastDoorService.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd](MACHOS/installcoordinationd.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview](MACHOS/com.apple.MLKit.MLPackagePreview.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService](MACHOS/PersonalizedSensingService.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Helpers/ProtectedCloudKeySyncing](MACHOS/ProtectedCloudKeySyncing.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/PlugIns/AppLaunchIntentExtension.appex/AppLaunchIntentExtension](MACHOS/AppLaunchIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService](MACHOS/SiriHeadlessService.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/PlugIns/VideoIntentExtension.appex/VideoIntentExtension](MACHOS/VideoIntentExtension.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension](MACHOS/WidgetConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriLinkSuggestionsPlugin.bundle/SiriLinkSuggestionsPlugin](MACHOS/SiriLinkSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriNotebookSuggestionsPlugin.bundle/SiriNotebookSuggestionsPlugin](MACHOS/SiriNotebookSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/ResponseGenerationUIPlugin.bundle/ResponseGenerationUIPlugin](MACHOS/ResponseGenerationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/SystemPlugin](MACHOS/SystemPlugin.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsContent.appex/FindMyNotificationsContent](MACHOS/FindMyNotificationsContent.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessWidget.appex/FitnessWidget](MACHOS/FitnessWidget.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformWidgetKitExtension.appex/FreeformWidgetKitExtension](MACHOS/FreeformWidgetKitExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgets.appex/JournalWidgets](MACHOS/JournalWidgets.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileCal.app/PlugIns/CalendarWidgetExtension.appex/CalendarWidgetExtension](MACHOS/CalendarWidgetExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Photos.app/Photos](MACHOS/Photos.md)
- [/private/var/staged_system_apps/Photos.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsTranscripts.framework/PodcastsTranscripts](MACHOS/PodcastsTranscripts.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsClassKitExtension.appex/PodcastsClassKitExtension](MACHOS/PodcastsClassKitExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget](MACHOS/PodcastsWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/TranslationWidgetsExtension.appex/TranslationWidgetsExtension](MACHOS/TranslationWidgetsExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/checkpointd](MACHOS/checkpointd.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mobileassetd](MACHOS/mobileassetd.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/perfdiagsselfenabled](MACHOS/perfdiagsselfenabled.md)
- [/usr/libexec/photosfaced](MACHOS/photosfaced.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/signpost_reporter](MACHOS/signpost_reporter.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (7)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H17.im4p

>  `AppleAVE2FW_H17.im4p`

```diff

   __TEXT._rtk_mtab: 0x2d0
   __TEXT.__constructor: 0x0
   __DATA.__const: 0x2a20
-  __DATA.__data: 0x1078
+  __DATA.__data: 0x1070
   __DATA._rtk_patchbay: 0x208
   __DATA._rtk_init_stack: 0x10000
   __DATA._rtk_irq_stack: 0x1000

```

#### exclave_DeviceServer

>  `exclave_DeviceServer`

```diff

 402.60.12.0.0
-  __TEXT.__text: 0x35a860
+  __TEXT.__text: 0x35b404
   __TEXT.__lcxx_override: 0x204
   __TEXT.__const: 0xd0b40
-  __TEXT.__cstring: 0x1ee36
+  __TEXT.__cstring: 0x1f356
   __TEXT.__swift5_typeref: 0x565c
   __TEXT.__swift5_capture: 0x33c
   __TEXT.__swift5_entry: 0x8

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__common: 0x2768
-  __DATA.__bss: 0x4e30
+  __DATA.__common: 0x2788
+  __DATA.__bss: 0x4e20
   __PDATA.__shared_cache: 0x0
   __PDATA.__mod_init_func: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 12261
+  Functions: 12265
   Symbols:   103
-  CStrings:  3695
+  CStrings:  3713

CStrings:
+ "/AppleInternal/Library/BuildRoots/cb09429a-9ee5-11ef-b491-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "Disabling metadata, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA is false."
+ "Prespecializations library: %s\n"
+ "Prespecializations library: Data at %p contains both maps. Using %s keyed map.\n"
+ "Prespecializations library: Data at %p only contains name-keyed map.\n"
+ "Prespecializations library: Data at %p only contains pointer-keyed map.\n"
+ "Prespecializations library: Descriptor table lookup of '%.*s' returned NULL pointer to descriptor pointer.\n"
+ "Prespecializations library: Did not find descriptor for key '%.*s'.\n"
+ "Prespecializations library: Failed to build demangling for node %p.\n"
+ "Prespecializations library: Failed to build demangling for simplified node %p.\n\n"
+ "Prespecializations library: Failed to build simplified mangling for node %p.\n"
+ "Prespecializations library: Found descriptor %p for key '%.*s'.\n"
+ "Prespecializations library: Hash table lookup checked %u loaded entries, %u total entries, starting data pointer %p, starting auxiliary pointer %p.\n"
+ "Prespecializations library: Looking up descriptor named '%.*s'.\n"
+ "Prespecializations library: No prespecializations map available from data at %p, disabling.\n"
+ "Prespecializations library: Returning data pointer %p\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP.\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from the option flags.\n"
+ "name"
+ "pointer"
- "/AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "Prespecializations library: Disabling, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED = %d\n"

```

#### exclave_ExclaveStackshotServer

>  `exclave_ExclaveStackshotServer`

```diff

 26.60.20.0.0
-  __TEXT.__text: 0x36786c
+  __TEXT.__text: 0x368410
   __TEXT.__lcxx_override: 0x204
   __TEXT.__const: 0xd1840
-  __TEXT.__cstring: 0x210ab
+  __TEXT.__cstring: 0x215cb
   __TEXT.__swift5_typeref: 0x5dae
   __TEXT.__swift5_fieldmd: 0x5718
   __TEXT.__constg_swiftt: 0xa264

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0x1050b0
-  __DATA.__common: 0x2718
+  __DATA.__bss: 0x1050a0
+  __DATA.__common: 0x2738
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 12465
+  Functions: 12469
   Symbols:   0
-  CStrings:  3825
+  CStrings:  3843

CStrings:
+ "/AppleInternal/Library/BuildRoots/cb09429a-9ee5-11ef-b491-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "Disabling metadata, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA is false."
+ "Prespecializations library: %s\n"
+ "Prespecializations library: Data at %p contains both maps. Using %s keyed map.\n"
+ "Prespecializations library: Data at %p only contains name-keyed map.\n"
+ "Prespecializations library: Data at %p only contains pointer-keyed map.\n"
+ "Prespecializations library: Descriptor table lookup of '%.*s' returned NULL pointer to descriptor pointer.\n"
+ "Prespecializations library: Did not find descriptor for key '%.*s'.\n"
+ "Prespecializations library: Failed to build demangling for node %p.\n"
+ "Prespecializations library: Failed to build demangling for simplified node %p.\n\n"
+ "Prespecializations library: Failed to build simplified mangling for node %p.\n"
+ "Prespecializations library: Found descriptor %p for key '%.*s'.\n"
+ "Prespecializations library: Hash table lookup checked %u loaded entries, %u total entries, starting data pointer %p, starting auxiliary pointer %p.\n"
+ "Prespecializations library: Looking up descriptor named '%.*s'.\n"
+ "Prespecializations library: No prespecializations map available from data at %p, disabling.\n"
+ "Prespecializations library: Returning data pointer %p\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP.\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from the option flags.\n"
+ "name"
+ "pointer"
- "/AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "Prespecializations library: Disabling, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED = %d\n"

```

#### exclave_roottask

>  `exclave_roottask`

```diff

 696.60.282.0.0
-  __TEXT.__text: 0x4e9ab0
+  __TEXT.__text: 0x4e9e74
   __TEXT.__lcxx_override: 0x200
   __TEXT.__const: 0xdcb13
-  __TEXT.__cstring: 0x2dd8a
+  __TEXT.__cstring: 0x2dfea
   __TEXT.__swift5_typeref: 0x9ecc
   __TEXT.__swift5_capture: 0x1788
   __TEXT.__swift5_entry: 0x8

   __DATA.__TIGHTBEAM: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__common: 0x21f20
+  __DATA.__common: 0x21f28
   __DATA.__bss: 0x11360
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 17037
+  Functions: 17041
   Symbols:   27
-  CStrings:  5200
+  CStrings:  5209

CStrings:
+ "/AppleInternal/Library/BuildRoots/cb09429a-9ee5-11ef-b491-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "Disabling metadata, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA is false."
+ "Prespecializations library: %s\n"
+ "Prespecializations library: Data at %p contains both maps. Using %s keyed map.\n"
+ "Prespecializations library: Data at %p only contains name-keyed map.\n"
+ "Prespecializations library: Data at %p only contains pointer-keyed map.\n"
+ "Prespecializations library: No prespecializations map available from data at %p, disabling.\n"
+ "Prespecializations library: Returning data pointer %p\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP.\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from the option flags.\n"
+ "pointer"
- "/AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "Prespecializations library: Disabling, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED = %d\n"

```

#### exclave_scheduler

>  `exclave_scheduler`

```diff

 696.60.282.0.0
-  __TEXT.__text: 0x329a2c
+  __TEXT.__text: 0x329df0
   __TEXT.__lcxx_override: 0x200
-  __TEXT.__cstring: 0x1d2a0
+  __TEXT.__cstring: 0x1d500
   __TEXT.__const: 0xd1284
   __TEXT.__constg_swiftt: 0x9c48
   __TEXT.__swift5_typeref: 0x58c0

   __PDATA.__mod_init_func: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 11289
+  Functions: 11293
   Symbols:   24
-  CStrings:  3692
+  CStrings:  3702

CStrings:
+ "/AppleInternal/Library/BuildRoots/cb09429a-9ee5-11ef-b491-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "Disabling metadata, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA is false."
+ "Prespecializations library: %s\n"
+ "Prespecializations library: Data at %p contains both maps. Using %s keyed map.\n"
+ "Prespecializations library: Data at %p only contains name-keyed map.\n"
+ "Prespecializations library: Data at %p only contains pointer-keyed map.\n"
+ "Prespecializations library: No prespecializations map available from data at %p, disabling.\n"
+ "Prespecializations library: Returning data pointer %p\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP.\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from the option flags.\n"
+ "name"
+ "pointer"
- "/AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "Prespecializations library: Disabling, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED = %d\n"

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

 460.62.1.0.0
-  __TEXT.__text: 0x4c2324
+  __TEXT.__text: 0x4c26e8
   __TEXT.__lcxx_override: 0x200
-  __TEXT.__cstring: 0x308ff
+  __TEXT.__cstring: 0x30b5f
   __TEXT.__const: 0xe2768
   __TEXT.__swift5_typeref: 0xdee5
   __TEXT.__swift5_reflstr: 0x9235

   __DATA.__DEVICETREE: 0x18
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__common: 0x531
+  __DATA.__common: 0x539
   __DATA.__bss: 0x8ef0
   __PDATA.__data: 0x15f0
   __PDATA.__const: 0x2190

   __PDATA.__common: 0x1fc0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 18491
+  Functions: 18495
   Symbols:   0
-  CStrings:  5142
+  CStrings:  5151

CStrings:
+ "/AppleInternal/Library/BuildRoots/cb09429a-9ee5-11ef-b491-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/AppleInternal/Library/BuildRoots/cb09429a-9ee5-11ef-b491-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "Disabling metadata, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA is false."
+ "Prespecializations library: %s\n"
+ "Prespecializations library: Data at %p contains both maps. Using %s keyed map.\n"
+ "Prespecializations library: Data at %p only contains name-keyed map.\n"
+ "Prespecializations library: Data at %p only contains pointer-keyed map.\n"
+ "Prespecializations library: No prespecializations map available from data at %p, disabling.\n"
+ "Prespecializations library: Returning data pointer %p\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP.\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from the option flags.\n"
+ "pointer"
- "/AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "Prespecializations library: Disabling, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED = %d\n"

```

#### exclave_sharedmem-v2

>  `exclave_sharedmem-v2`

```diff

 40.60.8.0.0
-  __TEXT.__text: 0x388f1c
+  __TEXT.__text: 0x389ab4
   __TEXT.__lcxx_override: 0x204
-  __TEXT.__cstring: 0x1f9c8
+  __TEXT.__cstring: 0x1fed8
   __TEXT.__const: 0xd1770
   __TEXT.__swift5_typeref: 0x5aca
   __TEXT.__swift5_reflstr: 0x1ba1

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0x4df0
-  __DATA.__common: 0x2770
+  __DATA.__bss: 0x4de0
+  __DATA.__common: 0x2790
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 12821
+  Functions: 12825
   Symbols:   0
-  CStrings:  3759
+  CStrings:  3777

CStrings:
+ "/AppleInternal/Library/BuildRoots/cb09429a-9ee5-11ef-b491-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "Disabling metadata, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA is false."
+ "Prespecializations library: %s\n"
+ "Prespecializations library: Data at %p contains both maps. Using %s keyed map.\n"
+ "Prespecializations library: Data at %p only contains name-keyed map.\n"
+ "Prespecializations library: Data at %p only contains pointer-keyed map.\n"
+ "Prespecializations library: Descriptor table lookup of '%.*s' returned NULL pointer to descriptor pointer.\n"
+ "Prespecializations library: Did not find descriptor for key '%.*s'.\n"
+ "Prespecializations library: Failed to build demangling for node %p.\n"
+ "Prespecializations library: Failed to build demangling for simplified node %p.\n\n"
+ "Prespecializations library: Failed to build simplified mangling for node %p.\n"
+ "Prespecializations library: Found descriptor %p for key '%.*s'.\n"
+ "Prespecializations library: Hash table lookup checked %u loaded entries, %u total entries, starting data pointer %p, starting auxiliary pointer %p.\n"
+ "Prespecializations library: Looking up descriptor named '%.*s'.\n"
+ "Prespecializations library: No prespecializations map available from data at %p, disabling.\n"
+ "Prespecializations library: Returning data pointer %p\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP.\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from the option flags.\n"
+ "name"
+ "pointer"
- "/AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "Prespecializations library: Disabling, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED = %d\n"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.2 *(22C5142a)* | 620.1.16.10.8 |
| 18.2 *(22C150)* | 620.1.16.10.11 |

### Dylibs

#### 🆕 NEW (4)

- `/System/Library/PrivateFrameworks/ConditionalEngineAppIntents.framework/ConditionalEngineAppIntents`
- `/System/Library/PrivateFrameworks/ConditionalEngineClient.framework/ConditionalEngineClient`
- `/System/Library/PrivateFrameworks/ConditionalEngineRuntime.framework/ConditionalEngineRuntime`
- `/System/Library/PrivateFrameworks/ConditionalEngineShared.framework/ConditionalEngineShared`

#### ⬆️ Updated (563)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/Moments.axbundle/Moments](DYLIBS/Moments.md)
- [/System/Library/AccessibilityBundles/PosterBoardFramework.axbundle/PosterBoardFramework](DYLIBS/PosterBoardFramework.md)
- [/System/Library/Accounts/Notification/SecureBackupNotification.bundle/SecureBackupNotification](DYLIBS/SecureBackupNotification.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/ClockKit.framework/ClockKit](DYLIBS/ClockKit.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/Combine.framework/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/ContactProvider.framework/ContactProvider](DYLIBS/ContactProvider.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit](DYLIBS/CoreAudioKit.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/CoreTransferable.framework/CoreTransferable](DYLIBS/CoreTransferable.md)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/EventKit.framework/EventKit](DYLIBS/EventKit.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/ImagePlayground.framework/ImagePlayground](DYLIBS/ImagePlayground.md)
- [/System/Library/Frameworks/LightweightCodeRequirements.framework/LightweightCodeRequirements](DYLIBS/LightweightCodeRequirements.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/LockedCameraCapture.framework/LockedCameraCapture](DYLIBS/LockedCameraCapture.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/PushKit.framework/PushKit](DYLIBS/PushKit.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/HighlightAlerts.healthplugin/HighlightAlerts](DYLIBS/HighlightAlerts.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing](DYLIBS/ASEProcessing.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI](DYLIBS/AXSoundDetectionUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccountsUISettings.framework/AccountsUISettings](DYLIBS/AccountsUISettings.md)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsCore.framework/ActivityAwardsCore](DYLIBS/ActivityAwardsCore.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivitySharingUI.framework/ActivitySharingUI](DYLIBS/ActivitySharingUI.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync](DYLIBS/AppPlaceholderSync.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskToDaemon.framework/AskToDaemon](DYLIBS/AskToDaemon.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistiveTouchUI.framework/AssistiveTouchUI](DYLIBS/AssistiveTouchUI.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService](DYLIBS/BusinessChatService.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI](DYLIBS/CarPlayUI.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer](DYLIBS/CiderAudioServer.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation](DYLIBS/CloudAttestation.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI](DYLIBS/CloudDocsUI.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay](DYLIBS/ComplicationDisplay.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore](DYLIBS/CoordinationCore.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon](DYLIBS/CoreCaptureDaemon.md)
- [/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV](DYLIBS/CoreIDV.md)
- [/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD](DYLIBS/CoreIDVPAD.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DarwinDirectory.framework/DarwinDirectory](DYLIBS/DarwinDirectory.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryInternal.framework/DarwinDirectoryInternal](DYLIBS/DarwinDirectoryInternal.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore](DYLIBS/DataDetectorsCore.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI](DYLIBS/DataDetectorsUI.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought](DYLIBS/DeepThought.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceExpertUI.framework/DeviceExpertUI](DYLIBS/DeviceExpertUI.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/DropletUI.framework/DropletUI](DYLIBS/DropletUI.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/EcosystemAnalytics](DYLIBS/EcosystemAnalytics.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/EmojiPoster](DYLIBS/EmojiPoster.md)
- [/System/Library/PrivateFrameworks/EnergyKit.framework/EnergyKit](DYLIBS/EnergyKit.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FPFS.framework/FPFS](DYLIBS/FPFS.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot](DYLIBS/FitnessAppRoot.md)
- [/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset](DYLIBS/FitnessAsset.md)
- [/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI](DYLIBS/FitnessCanvasUI.md)
- [/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching](DYLIBS/FitnessCoaching.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessFiltering.framework/FitnessFiltering](DYLIBS/FitnessFiltering.md)
- [/System/Library/PrivateFrameworks/FitnessProductDetail.framework/FitnessProductDetail](DYLIBS/FitnessProductDetail.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FusionTracker.framework/FusionTracker](DYLIBS/FusionTracker.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings](DYLIBS/GenerativeAssistantSettings.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesUI.framework/GenerativeExperiencesUI](DYLIBS/GenerativeExperiencesUI.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance](DYLIBS/HealthBalance.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices](DYLIBS/HealthRecordServices.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction](DYLIBS/HealthRecordsExtraction.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HearingTestUI.framework/HearingTestUI](DYLIBS/HearingTestUI.md)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAppIntents.framework/HomeAppIntents](DYLIBS/HomeAppIntents.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeAutomationUIFramework.framework/HomeAutomationUIFramework](DYLIBS/HomeAutomationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonFoundation.framework/HomeKitDaemonFoundation](DYLIBS/HomeKitDaemonFoundation.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/HomePlatformSettingsUI](DYLIBS/HomePlatformSettingsUI.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/Human.framework/Human](DYLIBS/Human.md)
- [/System/Library/PrivateFrameworks/HumanUI.framework/HumanUI](DYLIBS/HumanUI.md)
- [/System/Library/PrivateFrameworks/IMAVCore.framework/IMAVCore](DYLIBS/IMAVCore.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/IntelligenceEngine.framework/IntelligenceEngine](DYLIBS/IntelligenceEngine.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore](DYLIBS/IntelligentTrackingCore.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KeyboardSettings.framework/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback](DYLIBS/KeyboardSettingsFeedback.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/LegalAndRegulatorySettingsSupport.framework/LegalAndRegulatorySettingsSupport](DYLIBS/LegalAndRegulatorySettingsSupport.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LinkPresentationStyleSheetParsing.framework/LinkPresentationStyleSheetParsing](DYLIBS/LinkPresentationStyleSheetParsing.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport](DYLIBS/MTLToolsDeviceSupport.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/Marrs.framework/Marrs](DYLIBS/Marrs.md)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/Mercury.framework/Mercury](DYLIBS/Mercury.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/MobileAssetExclaveServices](DYLIBS/MobileAssetExclaveServices.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/Morpheus.framework/Morpheus](DYLIBS/Morpheus.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsEngagement.framework/NewsEngagement](DYLIBS/NewsEngagement.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/NotesUIServices.framework/NotesUIServices](DYLIBS/NotesUIServices.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PeopleSuggesterLighthouse](DYLIBS/PeopleSuggesterLighthouse.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace](DYLIBS/PhotosFace.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/PnROnDeviceFramework](DYLIBS/PnROnDeviceFramework.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport](DYLIBS/ProactiveDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/ProactiveShareSheetDataHarvestingLighthouse](DYLIBS/ProactiveShareSheetDataHarvestingLighthouse.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon](DYLIBS/ProximityReaderDaemon.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/RemindersIntentsFramework](DYLIBS/RemindersIntentsFramework.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensingAlgsTouchButtonHost.framework/SensingAlgsTouchButtonHost](DYLIBS/SensingAlgsTouchButtonHost.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/Sentry.framework/Sentry](DYLIBS/Sentry.md)
- [/System/Library/PrivateFrameworks/SessionAssertion.framework/SessionAssertion](DYLIBS/SessionAssertion.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings](DYLIBS/SoundsAndHapticsSettings.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShaderGraph.framework/ShaderGraph](DYLIBS/ShaderGraph.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShimGameServices.framework/ShimGameServices](DYLIBS/ShimGameServices.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCalendarUI.framework/SiriCalendarUI](DYLIBS/SiriCalendarUI.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriContactsUI.framework/SiriContactsUI](DYLIBS/SiriContactsUI.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall](DYLIBS/SiriInCall.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInferenceFlow.framework/SiriInferenceFlow](DYLIBS/SiriInferenceFlow.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/SiriNaturalLanguageGeneration](DYLIBS/SiriNaturalLanguageGeneration.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotebookUI.framework/SiriNotebookUI](DYLIBS/SiriNotebookUI.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager](DYLIBS/SiriTurnTakingManager.md)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments](DYLIBS/SiriUserSegments.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVideoUIFramework.framework/SiriVideoUIFramework](DYLIBS/SiriVideoUIFramework.md)
- [/System/Library/PrivateFrameworks/SiriWellnessIntents.framework/SiriWellnessIntents](DYLIBS/SiriWellnessIntents.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies](DYLIBS/SmartReplies.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit](DYLIBS/SportsKit.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/Stateful.framework/Stateful](DYLIBS/Stateful.md)
- [/System/Library/PrivateFrameworks/StickersUI.framework/StickersUI](DYLIBS/StickersUI.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization](DYLIBS/StocksPersonalization.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StorageUI.framework/StorageUI](DYLIBS/StorageUI.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemUIAnimationKit.framework/SystemUIAnimationKit](DYLIBS/SystemUIAnimationKit.md)
- [/System/Library/PrivateFrameworks/TDGSharing.framework/TDGSharing](DYLIBS/TDGSharing.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TeaBreeze.framework/TeaBreeze](DYLIBS/TeaBreeze.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings](DYLIBS/TeaSettings.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/TextUnderstandingShared.framework/TextUnderstandingShared](DYLIBS/TextUnderstandingShared.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt](DYLIBS/TipsTryIt.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TrustKit.framework/TrustKit](DYLIBS/TrustKit.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UINavigationKit.framework/UINavigationKit](DYLIBS/UINavigationKit.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding](DYLIBS/UIUnderstanding.md)
- [/System/Library/PrivateFrameworks/UniversalHID.framework/UniversalHID](DYLIBS/UniversalHID.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceControlUI.framework/VoiceControlUI](DYLIBS/VoiceControlUI.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger](DYLIBS/VoiceTrigger.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/VideoCodecs/VCPHEVC.videocodec](DYLIBS/VCPHEVC.videocodec.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libchannel.dylib](DYLIBS/libchannel.dylib.md)
- [/usr/lib/librealtime_safety.dylib](DYLIBS/librealtime_safety.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftCore.dylib](DYLIBS/libswiftCore.dylib.md)
- [/usr/lib/swift/libswiftSpatial.dylib](DYLIBS/libswiftSpatial.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)

</details>

### Feature Flags

#### 🆕 NEW (1)

<details>
  <summary><i>View New</i></summary>

#### ConditionalEngine.plist

>  `Domain/ConditionalEngine.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict/>
</plist>

```

</details>

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

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
