## com.apple.kernel

> `com.apple.kernel`

```diff

-11417.140.66.0.0
-  __TEXT.__const: 0x348b0
+11417.140.69.0.0
+  __TEXT.__const: 0x34820
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x76a7a
+  __TEXT.__cstring: 0x73567
   __TEXT.__os_log: 0x2a76b
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0xabdf8
+  __DATA_CONST.__const: 0xabbf8
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x13980
+  __DATA_CONST.__kalloc_type: 0x136c0
   __DATA_CONST.__kalloc_var: 0x7ee0
   __DATA_CONST.__assert: 0x1cc
   __DATA_CONST.__exclaves_bt: 0x60
-  __DATA_CONST.__kern_brk_desc: 0x78
+  __DATA_CONST.__kern_brk_desc: 0x60
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xcc8
-  __TEXT_EXEC.__text: 0x82e594
+  __TEXT_EXEC.__text: 0x81aa40
   __TEXT_BOOT_EXEC.__bootcode: 0x514c
   __KLD.__text: 0x1638
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x2af8
+  __KLDDATA.__const: 0x2b68
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x185c1
-  __DATA.__lock_grp: 0x5a68
+  __DATA.__data: 0x17d81
+  __DATA.__lock_grp: 0x59b8
   __DATA.__percpu: 0x6e90
-  __DATA.__common: 0x5bd70
-  __DATA.__bss: 0x96258
+  __DATA.__common: 0x5ba90
+  __DATA.__bss: 0x96268
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x11238
+  __BOOTDATA.__init_entry_set: 0x11160
   __BOOTDATA.__init: 0x5b180
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x466fd
-  UUID: BE79611C-05EB-33C0-A8BC-E14C214994F1
-  Functions: 20198
+  UUID: C3774576-A524-30FC-A09E-5E55CB6475F1
+  Functions: 19990
   Symbols:   0
-  CStrings:  17900
+  CStrings:  17616
 
CStrings:
+ "unrestricted-subsystem-root"
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
- "%s-%s-%u.%u.%u.%u-%x%s"
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
- "11122221222222222222222112"
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
