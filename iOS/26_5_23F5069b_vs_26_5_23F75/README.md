# 26.5 (23F5069b) .vs 26.5 (23F75)

## Inputs

- `iPhone18,1_26.5_23F5069b_Restore.ipsw`
- `iPhone18,1_26.5_23F75_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.5 *(23F5069b)* | 25.5.0 | 12377.122.4~2 | Thu, 23Apr2026 21:27:42 PDT |
| 26.5 *(23F75)* | 25.5.0 | 12377.122.4~1 | Thu, 23Apr2026 20:42:24 PDT |

### Kexts

#### ❌ Removed (1)

- `com.apple.kec.AppleEncryptedArchive`

### ⬆️ Updated (6)

<details>
  <summary><i>View Updated</i></summary>

#### com.apple.driver.AppleAOPAudio

>  `com.apple.driver.AppleAOPAudio`

```diff

   __TEXT.__cstring: 0xc591
   __TEXT.__const: 0x136
   __TEXT.__os_log: 0xf
-  __TEXT_EXEC.__text: 0x2eee8
+  __TEXT_EXEC.__text: 0x2eefc
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
-  UUID: 3E71A86B-2DBF-3F83-B567-9AD2DCEF019E
+  UUID: AECB1D76-5FE9-33CA-BE32-D23EC826784F
   Functions: 1225
   Symbols:   0
   CStrings:  1152
Functions:
~ __ZN23AppleAOPAudioController5startEP9IOService : 472 -> 492
CStrings:
+ "20:24:56"
+ "20:24:59"
- "21:03:40"
- "21:03:51"

```

#### com.apple.driver.corecapture

>  `com.apple.driver.corecapture`

```diff

   __TEXT.__os_log: 0x4336
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x200e
-  __TEXT_EXEC.__text: 0x26180
+  __TEXT_EXEC.__text: 0x2614c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x308

   __DATA_CONST.__const: 0x7010
   __DATA_CONST.__kalloc_type: 0x10c0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 3F86FA48-39A3-3DBE-AE0D-18777FC6F4DF
+  UUID: 0E29FEFB-34F6-39D4-9367-AD4E5A81CEA4
   Functions: 878
   Symbols:   0
   CStrings:  661
Functions:
~ __Z34corecaptureIsDevFusedOrCSRInternalb : 120 -> 100
~ __Z29corecaptureIsDebuggbleUnifiedv : 100 -> 116
~ __ZN6CCPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptions : 6308 -> 6272
~ sub_fffffe000a5855c4 -> __Z16DefaultLogPolicyv : 100 -> 108
~ __ZN11CCIOService17ccForcePanic_ImplEbP8OSString : 188 -> 184
~ __ZN16CCPipeUserClient12initWithTaskEP4taskPvjP12OSDictionary : 356 -> 352
~ sub_fffffe000a588de8 -> sub_fffffe000a583380 : 12 -> 8
~ sub_fffffe000a59035c -> sub_fffffe000a58a8f0 : 192 -> 188
~ sub_fffffe000a5a03cc -> sub_fffffe000a59a95c : 100 -> 96

```

#### com.apple.filesystems.apfs

>  `com.apple.filesystems.apfs`

```diff

   __TEXT.__cstring: 0x4d4b8
   __TEXT_EXEC.__text: 0x148324
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x70c
-  __DATA.__bss: 0xd48
+  __DATA.__data: 0x704
+  __DATA.__bss: 0xd50
   __DATA_CONST.__auth_got: 0x1180
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__kalloc_type: 0x5080
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: 951C49ED-1762-3AE6-8594-FD5F36431280
+  UUID: E3DBAAF2-F3E3-33DD-909C-BEF5BDAF4AA8
   Functions: 2334
   Symbols:   0
   CStrings:  6692
CStrings:
+ "20:25:36"
- "21:04:12"

```

#### com.apple.iokit.AppleARMIISAudio

>  `com.apple.iokit.AppleARMIISAudio`

```diff

   __TEXT.__os_log: 0x2973
   __TEXT.__cstring: 0x3194
   __TEXT.__const: 0xa8
-  __TEXT_EXEC.__text: 0x15204
+  __TEXT_EXEC.__text: 0x1522c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1a8
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__const: 0x1158
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: 5609EB32-40F8-3798-BDDE-5BAF719FDF75
+  UUID: 0C8205FF-E939-3F68-A460-56B136CB8A92
   Functions: 315
   Symbols:   0
   CStrings:  411
Functions:
~ __ZN22AppleARMDMAAudioDevice13startInternalEP9IOServicexjPKjS3_S3_S3_ : 1232 -> 1272

```

#### com.apple.kernel

>  `com.apple.kernel`

```diff

 12377.122.4.0.0
-  __TEXT.__const: 0x363d0
+  __TEXT.__const: 0x36310
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x88592
+  __TEXT.__cstring: 0x84c42
   __TEXT.__os_log: 0x3ded0
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x119da0
-  __DATA_CONST.__kalloc_type: 0x14640
+  __DATA_CONST.__const: 0x119d30
+  __DATA_CONST.__kalloc_type: 0x14300
   __DATA_CONST.__assert: 0xc58
   __DATA_CONST.__kalloc_var: 0x78f0
   __DATA_CONST.__exclaves_bt: 0x78
-  __DATA_CONST.__kern_brk_desc: 0x78
+  __DATA_CONST.__kern_brk_desc: 0x60
   __DATA_CONST.__mod_init_func: 0x2d8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x8b6be8
+  __TEXT_EXEC.__text: 0x8a34cc
   __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0x1460
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x3740
+  __KLDDATA.__const: 0x3710
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x17ff9
-  __DATA.__lock_grp: 0x5b70
+  __DATA.__lock_grp: 0x5ac0
   __DATA.__percpu: 0x7870
-  __DATA.__common: 0x77778
-  __DATA.__bss: 0xa3dc8
+  __DATA.__common: 0x775d8
+  __DATA.__bss: 0xa3db8
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x135f0
+  __BOOTDATA.__init_entry_set: 0x13548
   __BOOTDATA.__init: 0x5b5c8
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4804e
-  UUID: 14DEDADF-FDEF-33B3-BB62-CD57869A86A4
-  Functions: 21334
+  UUID: 53C3D1F3-B5BC-3B22-9A9E-46D18080E59E
+  Functions: 21127
   Symbols:   0
-  CStrings:  20747
+  CStrings:  20441
 
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
- "(%s) coredump size limit exceeded: attempted %llu bytes, limit is %llu bytes\n"
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
- "(disk_stage_write) coredump size limit exceeded: attempted %llu bytes, limit is %llu bytes\n"
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
- "11222211111111111"
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
- "Failed to dump coprocessor cores with error: %d\n"
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
- "core"
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
- "disk_stage_outproc"
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
- "site.struct kern_coredump_core"
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

 2680.120.12.0.0
   __TEXT.__os_log: 0x2272
-  __TEXT.__const: 0x1cab91
+  __TEXT.__const: 0x1cac21
   __TEXT.__cstring: 0x72d6
   __TEXT_EXEC.__text: 0x38ab8
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x3858
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: 0FCEC51F-B242-3930-B4FA-071E06C62FED
+  UUID: 58F3BE22-6099-3D96-B22F-DBA3D67DDE65
   Functions: 652
   Symbols:   0
   CStrings:  1344

```


</details>

## MachO

### 🆕 NEW (2)

- `/System/Library/AccessibilityBundles/NTKPride2026FaceBundle.axbundle/NTKPride2026FaceBundle`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2026FaceBundleFaceBundle.bundle/NTKPride2026FaceBundleFaceBundle`

### ❌ Removed (2)

- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/usr/libexec/memoryanalyticsd`

### ⬆️ Updated (139)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/CheckerBoard.app/CheckerBoard](MACHOS/CheckerBoard.md)
- [/Applications/DiagnosticsReporter.app/DiagnosticsReporter](MACHOS/DiagnosticsReporter.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004](MACHOS/Diagnostic-7004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185](MACHOS/Diagnostic-8185.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268](MACHOS/Diagnostic-8268.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340](MACHOS/Diagnostic-8340.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343](MACHOS/Diagnostic-8343.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006](MACHOS/Diagnostic-9006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008](MACHOS/Diagnostic-9008.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010](MACHOS/Diagnostic-9010.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9012.appex/Diagnostic-9012](MACHOS/Diagnostic-9012.md)
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
- [/System/ExclaveKit/System/Library/Frameworks/T8150_IR_ISP_EK_Component.framework/T8150_IR_ISP_EK_Component_asan](MACHOS/T8150_IR_ISP_EK_Component_asan.md)
- [/System/ExclaveKit/System/Library/Frameworks/T8150_RGB_ISP_EK_Component.framework/T8150_RGB_ISP_EK_Component_asan](MACHOS/T8150_RGB_ISP_EK_Component_asan.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/T8150_CoreAAClientKit.framework/T8150_CoreAAClientKit_asan](MACHOS/T8150_CoreAAClientKit_asan.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/T8150_ExclaveISPSharedLib_exclavekit.framework/T8150_ExclaveISPSharedLib_exclavekit_asan](MACHOS/T8150_ExclaveISPSharedLib_exclavekit_asan.md)
- [/System/Library/AccessibilityBundles/NTKCustomization.axbundle/NTKCustomization](MACHOS/NTKCustomization.md)
- [/System/Library/AccessibilityBundles/NTKUltraCubeFaceBundleCompanion.axbundle/NTKUltraCubeFaceBundleCompanion](MACHOS/NTKUltraCubeFaceBundleCompanion.md)
- [/System/Library/AccessibilityBundles/NanoTimeKitCompanion.axbundle/NanoTimeKitCompanion](MACHOS/NanoTimeKitCompanion.md)
- [/System/Library/Assistant/Plugins/activity.assistantBundle/activity](MACHOS/activity.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_fullsize_archive_bin.metallib](MACHOS/portrait_filters_fullsize_archive_bin.metallib.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/HangHUD.app/HangHUD](MACHOS/HangHUD.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard](MACHOS/SpringBoard.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/CloudWorker.appex/CloudWorker](MACHOS/CloudWorker.md)
- [/System/Library/ExtensionKit/Extensions/InferenceExtension.appex/InferenceExtension](MACHOS/InferenceExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseAVExtension.appex/LighthouseAVExtension](MACHOS/LighthouseAVExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseAVShadowEval.appex/LighthouseAVShadowEval](MACHOS/LighthouseAVShadowEval.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/Frameworks/ImageIO.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested](MACHOS/CircleJoinRequested.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/Security.framework/swcagent](MACHOS/swcagent.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/DigitalTouchBalloonProvider.bundle/DigitalTouchBalloonProvider](MACHOS/DigitalTouchBalloonProvider.md)
- [/System/Library/NanoTimeKit/FaceBundles/KaleidoscopeFaceBundle.bundle/NTKKaleidoscopeShaders.metallib](MACHOS/NTKKaleidoscopeShaders.metallib.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKPride2025FaceBundle.bundle/NTKPride2025FaceBundle](MACHOS/NTKPride2025FaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKWarlockFaceBundle.bundle/warlock.metallib](MACHOS/warlock.metallib.md)
- [/System/Library/PreferenceBundles/HomeSettings.bundle/HomeSettings](MACHOS/HomeSettings.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](MACHOS/KeyboardSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PrivateFrameworks/ACTFramework.framework/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
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
- [/System/Library/PrivateFrameworks/DialogEngine.framework/catutil](MACHOS/catutil.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd](MACHOS/ecosystemanalyticsd.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension](MACHOS/HangLogsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension](MACHOS/PerformanceLoggingDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IconRendering.framework/binary.metallib](MACHOS/binary.metallib.md)
- [/System/Library/PrivateFrameworks/JetCore.framework/Support/jetpackassetd](MACHOS/jetpackassetd.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/NanoUniverse.framework/NUNICalliopeShadersCompanion.metallib](MACHOS/NUNICalliopeShadersCompanion.metallib.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService](MACHOS/PersonalizedSensingService.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/metal_libraries/binary.metallib](MACHOS/binary.metallib.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/ColourConstancyV1.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/STF.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/STF.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/SmartStyleV1.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/VideoDeghostingV3.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/Freeform.app/Frameworks/TSMediaLibrary.framework/TSMediaLibrary](MACHOS/TSMediaLibrary.md)
- [/private/var/staged_system_apps/KaleidoscopePosterApp.app/Extensions/KaleidoscopePoster.appex/NTKKaleidoscopeShaders.metallib](MACHOS/NTKKaleidoscopeShaders.metallib.md)
- [/private/var/staged_system_apps/PridePosterApp.app/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/checkpointd](MACHOS/checkpointd.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/perfdiagsselfenabled](MACHOS/perfdiagsselfenabled.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/signpost_reporter](MACHOS/signpost_reporter.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/uarpassetmanagerd](MACHOS/uarpassetmanagerd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

### Sandbox Profiles

- [Sandbox Profiles DIFF](Sandbox.md)

## Firmware

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H18.im4p

>  `AppleAVE2FW_H18.im4p`

```diff

   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA._rtk_patchbay: 0x211
-  __DATA.__data: 0x1710
+  __DATA.__data: 0x1708
   __DATA._rtk_mtab: 0x320
   __DATA._rtk_power: 0x3b8
   __DATA.__gxf_data: 0x10

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc6840
-  UUID: 5FABEFE6-492F-342A-9453-2F3BDBE88DCA
+  UUID: 56269784-8481-3A8B-ADAD-505A3333C9F1
   Functions: 1218
   Symbols:   1704
   CStrings:  2645
CStrings:
+ "Caller is /Library/Caches/com.apple.xbs/954EBAC5-3E8D-4A15-A932-5B1AA318B4B3/TemporaryDirectory.hwLmGf/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:751"
+ "Caller is /Library/Caches/com.apple.xbs/954EBAC5-3E8D-4A15-A932-5B1AA318B4B3/TemporaryDirectory.hwLmGf/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:756"
- "Caller is /Library/Caches/com.apple.xbs/006E2569-CC16-4140-9564-FFE86B4BB636/TemporaryDirectory.MkvXuW/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:751"
- "Caller is /Library/Caches/com.apple.xbs/006E2569-CC16-4140-9564-FFE86B4BB636/TemporaryDirectory.MkvXuW/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:756"

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

 1148.120.6.0.0
-  __TEXT.__text: 0x5d5bc4
+  __TEXT.__text: 0x5d5ba4
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__cstring: 0x48ed1
   __TEXT.__const: 0x112ee4

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: FB3DEDF5-CBEA-3162-9088-DF9AC3C4E6EC
+  UUID: 3904C8B0-7BC5-34DC-B016-3A7595639353
   Functions: 23506
   Symbols:   1
   CStrings:  6796
Functions:
~ sub_8594e94 : 904 -> 808
~ sub_8595cbc -> sub_8595c5c : 1020 -> 1084
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CNpgugDt6TcCZQtcm_yHFmMdDEvaL-W1C6QCUb0/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CNphugC56fPfrd222FAslcDcQmeMSteQirzs0Og/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CNpiugCiRHE6poFl0dLlI5zoC7XXP-o6880ZHJo/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
+ "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
+ "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
+ "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"
- "/AppleInternal/Library/BuildRoots/4~CNmaugCh0lE8N4uCgL28jvA81EaKLexEHacC0_Y/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CNmcugAqkCeqfyg5AJ2JsMT74qyQjC9UflCD6OU/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CNmdugD_iTWR82e-oH4aNiminZou4isq0Dx8jD4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
- "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
- "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
- "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.5 *(23F5069b)* | mBoot-18000.120.36 |
| 26.5 *(23F75)* | mBoot-18000.120.36 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.5 *(23F5069b)* | 624.2.5.10.4 |
| 26.5 *(23F75)* | 624.2.5.10.4 |

### Dylibs

#### ⬆️ Updated (147)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/Moments.axbundle/Moments](DYLIBS/Moments.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/FoundationModels.framework/FoundationModels](DYLIBS/FoundationModels.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/Frameworks/PushKit.framework/PushKit](DYLIBS/PushKit.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUnity2025FaceBundle.bundle/NTKUnity2025FaceBundle](DYLIBS/NTKUnity2025FaceBundle.md)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing](DYLIBS/ASEProcessing.md)
- [/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings](DYLIBS/AUDeveloperSettings.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppStoreComponentsDaemonKit.framework/AppStoreComponentsDaemonKit](DYLIBS/AppStoreComponentsDaemonKit.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal](DYLIBS/AppleMediaServicesKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIKitInternal.framework/AppleMediaServicesUIKitInternal](DYLIBS/AppleMediaServicesUIKitInternal.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/CentauriDiagnostic.framework/CentauriDiagnostic](DYLIBS/CentauriDiagnostic.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer](DYLIBS/CiderAudioServer.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI](DYLIBS/CloudDocsUI.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera](DYLIBS/CompanionCamera.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore](DYLIBS/CoordinationCore.md)
- [/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon](DYLIBS/CoreCaptureDaemon.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition](DYLIBS/CoreRecognition.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
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
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager](DYLIBS/HeadphoneManager.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettingsUI.framework/HeadphoneSettingsUI](DYLIBS/HeadphoneSettingsUI.md)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/ImagePlaygroundInternal.framework/ImagePlaygroundInternal](DYLIBS/ImagePlaygroundInternal.md)
- [/System/Library/PrivateFrameworks/IntelligenceEngine.framework/IntelligenceEngine](DYLIBS/IntelligenceEngine.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/JetCore.framework/JetCore](DYLIBS/JetCore.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/KeyboardSettings.framework/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback](DYLIBS/KeyboardSettingsFeedback.md)
- [/System/Library/PrivateFrameworks/LighthouseServicesAnalyticsFramework.framework/LighthouseServicesAnalyticsFramework](DYLIBS/LighthouseServicesAnalyticsFramework.md)
- [/System/Library/PrivateFrameworks/MDM.framework/MDM](DYLIBS/MDM.md)
- [/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport](DYLIBS/MTLToolsDeviceSupport.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon](DYLIBS/MobileAssetDaemon.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MomentsIntelligence.framework/MomentsIntelligence](DYLIBS/MomentsIntelligence.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/Sentry.framework/Sentry](DYLIBS/Sentry.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligenceCore.framework/VisualIntelligenceCore](DYLIBS/VisualIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/VisualIntelligenceUI.framework/VisualIntelligenceUI](DYLIBS/VisualIntelligenceUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/VideoCodecs/VCPHEVC.videocodec](DYLIBS/VCPHEVC.videocodec.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib.md)
- [/usr/lib/libchannel.dylib](DYLIBS/libchannel.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)

</details>

## Files

### 🆕 New

#### filesystem (119)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/AccessibilityBundles/Moments.axbundle/Accessibility-Jurassic.loctable`
- `/System/Library/AccessibilityBundles/Music.axbundle/Accessibility-AQ.loctable`
- `/System/Library/AccessibilityBundles/MusicApplication.axbundle/Accessibility-AQ.loctable`
- `/System/Library/AccessibilityBundles/NTKPride2026FaceBundle.axbundle/Accessibility.loctable`
- `/System/Library/AccessibilityBundles/NTKPride2026FaceBundle.axbundle/Info.plist`
- `/System/Library/AccessibilityBundles/NTKPride2026FaceBundle.axbundle/InfoPlist.loctable`
- `/System/Library/AccessibilityBundles/NTKPride2026FaceBundle.axbundle/NTKPride2026FaceBundle`
- `/System/Library/AccessibilityBundles/NTKPride2026FaceBundle.axbundle/_CodeSignature/CodeResources`
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
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2026FaceBundleFaceBundle.bundle/FaceColors.loctable`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2026FaceBundleFaceBundle.bundle/Info.plist`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2026FaceBundleFaceBundle.bundle/Localizable.loctable`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2026FaceBundleFaceBundle.bundle/NTKPride2026FaceBundleFaceBundle`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2026FaceBundleFaceBundle.bundle/Pride2026.color.plist`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2026FaceBundleFaceBundle.bundle/_CodeSignature/CodeResources`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2026FaceBundleFaceBundle.bundle/config.json`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2026FaceBundleFaceBundle.bundle/default.metallib`
- `/System/Library/Posters/DownloadablePosterAppMetadata/com.apple.PridePoster.dpmb/Resources/iPad/com.apple.PridePoster.PridePosterExtension/632d987dd034ab5983d3dd9040b4ac0d8ca10f588e2b561cc1aff55c64caf2b4/titleStyleConfiguration.plist`
- `/System/Library/Posters/DownloadablePosterAppMetadata/com.apple.PridePoster.dpmb/Resources/iPad/com.apple.PridePoster.PridePosterExtension/LandscapeLeft/632d987dd034ab5983d3dd9040b4ac0d8ca10f588e2b561cc1aff55c64caf2b4.jpeg`
- `/System/Library/Posters/DownloadablePosterAppMetadata/com.apple.PridePoster.dpmb/Resources/iPad/com.apple.PridePoster.PridePosterExtension/Portrait/632d987dd034ab5983d3dd9040b4ac0d8ca10f588e2b561cc1aff55c64caf2b4.jpeg`
- `/System/Library/Posters/DownloadablePosterAppMetadata/com.apple.PridePoster.dpmb/Resources/iPhone/com.apple.PridePoster.PridePosterExtension/632d987dd034ab5983d3dd9040b4ac0d8ca10f588e2b561cc1aff55c64caf2b4/titleStyleConfiguration.plist`
- `/System/Library/Posters/DownloadablePosterAppMetadata/com.apple.PridePoster.dpmb/Resources/iPhone/com.apple.PridePoster.PridePosterExtension/Portrait/632d987dd034ab5983d3dd9040b4ac0d8ca10f588e2b561cc1aff55c64caf2b4.jpeg`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f949be2b5bc29e8d9e985afc0fa7fbf4a3559fb0.asset/AssetData/settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f949be2b5bc29e8d9e985afc0fa7fbf4a3559fb0.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/7f50a81a71f8ff6cebbf2d151474b0256a253146.asset/AssetData/empty.txt`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/7f50a81a71f8ff6cebbf2d151474b0256a253146.asset/Info.plist`
- `/System/Library/PrivateFrameworks/AXNTKUtilities.framework/Accessibility-pride2026.loctable`
- `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/AssetPaths-Seed.plist`
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
- `/private/var/staged_system_apps/PridePosterApp.app/Extensions/PridePosterExtension.appex/Lens.loctable`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/c134e91f559410641dc501983e26285d.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/3cf5994409c7dfe227a279d06e9b7bff.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/8f9011a6187385e48f97d0dc5c8478aa.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/c96a0e6095c8e2d511c9a9ef4eb533e5.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/856e4f70c96185a2b5f14c2ab62e1a27.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/6d152fd15c16b28eb9c1b9b484554999.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/ae763065052f53407faf0924ee9c1b6a.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/5b9062503eff7a5f0dfcc91139b633db.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/26c48ab46b48e4846eab582eba67fa93.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/ab2ba88f56a61f1a0a87b28ca15b362f.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/e7ea9361193daaaceb25869a7b84b006.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/134ae157f8cb542d76a5a621fd96251b.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/3a3559973b3aad23625089edbac6d08b.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/67f2efb32578651ad71bb6f0c1fe1091.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/3c2f94a3f3a505bf674785c49598bb08.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/187e65366596b9b3a25963faf34d85f0.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/d5c1339c39767fffe428b6e36b2c2cbc.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/f218df5b07db068da4700a278dea5e71.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/0a88334c5c63e76217ebd4fc93bf0445.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/e3d2b0a62fb383fcc555ec30299ca091.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/a070125fd6f2cf14639f2accd70c8f6d.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/090beb7f756a385939c293f124a9fb88.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/8f18b8ce6a599cc198dc7e7d5672ae15.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/9002d7ec0ed0905f112f3b6ad1a5a492.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/8331ce2fed6a44e5eafff5d457aea287.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/d5dbab73d038916fda749ac3da652feb.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/4f856e48350261fe3e216e4685941b51.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/3434df2a642e0a0bd18b3f5fa4d52d65.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/b80394d5ed0625e5ffb6eca292f3b1b5.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/770eaa8849e901109a923d94a06f3615.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/0145083fbb70826b2a72b7ed79d0acf8.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/c5e9486a1aa349d27cde8910bc1cd40e.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/0fd0988a372a3988a2b7e18da6f326cd.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/d3e4bc8a7d533fafb812798a6d419ba1.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/3a294a9616b0fa24ec2d9748dc449e1b.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/6157c4673d62d686690f750bfd6b3974.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/62561048a37b769e35d0e9b4848ab0d7.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/9ff591bb182d98c7d97aa6408df4216a.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/876644633d5dd1fa82e905c3ffb7a05e.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/773df3ec93a68393ee750b680e254bb8.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/182c28dce9a75fec9b4e7d95c1df6714.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/d13c57afdf72109e7342d3d1fa6aff07.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/35c705fb6858b8bfe066763700dc79e7.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/e6685992785735e5cbcb49090e8dee20.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/61daa7ceb7cdb7b07ef5d8ac1028480b.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/19fb3b01036a347dee46621d5d563b5a.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/188e845c94f8324db173fca103bd8ff0.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/100adb43158bea97b200e1083f49d968.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/ea093016b782c0e36056ef333002ee15.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/08dec0f13ba91d75f364b3d5cda446be.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/d054dc3fa8ec6bdd4d43e5e5d5158ad0.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/07b32f83a169630d385a259a40d3c94f.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/001847e837b889bce423051cb67d080c.version`

</details>

### ❌ Removed

#### filesystem (87)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/Frameworks/SystemConfiguration.framework/get-mobility-info`
- `/System/Library/LaunchDaemons/com.apple.memoryanalyticsd.plist`
- `/System/Library/Posters/DownloadablePosterAppMetadata/com.apple.PridePoster.dpmb/Resources/iPad/com.apple.PridePoster.PridePosterExtension/364f583eec28f26a61e8d762d50d41b8ba5da040b3fe55f6f4c0972ddd7106e2/titleStyleConfiguration.plist`
- `/System/Library/Posters/DownloadablePosterAppMetadata/com.apple.PridePoster.dpmb/Resources/iPad/com.apple.PridePoster.PridePosterExtension/LandscapeLeft/364f583eec28f26a61e8d762d50d41b8ba5da040b3fe55f6f4c0972ddd7106e2.jpeg`
- `/System/Library/Posters/DownloadablePosterAppMetadata/com.apple.PridePoster.dpmb/Resources/iPad/com.apple.PridePoster.PridePosterExtension/Portrait/364f583eec28f26a61e8d762d50d41b8ba5da040b3fe55f6f4c0972ddd7106e2.jpeg`
- `/System/Library/Posters/DownloadablePosterAppMetadata/com.apple.PridePoster.dpmb/Resources/iPhone/com.apple.PridePoster.PridePosterExtension/364f583eec28f26a61e8d762d50d41b8ba5da040b3fe55f6f4c0972ddd7106e2/titleStyleConfiguration.plist`
- `/System/Library/Posters/DownloadablePosterAppMetadata/com.apple.PridePoster.dpmb/Resources/iPhone/com.apple.PridePoster.PridePosterExtension/Portrait/364f583eec28f26a61e8d762d50d41b8ba5da040b3fe55f6f4c0972ddd7106e2.jpeg`
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
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/119f15b8ec5040d6a0f0b6bbc32f5036.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/674d6e82b6ef395e0b1ef8a7f42b53e2.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/28b6b5fe865e83d71004920bf59a96c1.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/abaa3eaeb9c2c83507aa72808cbc5ac9.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/c346abb47f39bdf5ea74c783db797c56.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/ca4b7fc3cb8942fe7cf706a5d8d725fa.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/4ee37489e3dc6e1495e47f92922bc474.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/47ed763d4da852053d3e0df403a32a15.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/e5ef47b714388efe15152efd0470d448.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/5c3a49cf0895c034c54be0b2934c516f.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/6bbf19e88f32263e9312eddb48411583.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/816af27423827af6c4b139fb9dc9934c.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/4674653c311ed103b62d1fb2c5cb47a2.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/f3fff939a8ea74c791518394e0ee8d47.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/3f4b911a5f15b5dee8fef84bb57f5765.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/d90ba7b3643280c39a0ef43dea75c243.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/6d599761a63725c06e50b113ffe89d45.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/4c913fe73b4302a65f8117aeda254b57.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/138ae3944360cf092d85ea0d4b1845b3.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/65a12114e41d4102b645f601cb41801f.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/ee72c4cad7f169364ca30afa7d1709e5.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/1aaa69a8d25940d633bf54a74616b43f.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/ade35c6dda359d3a30200572cdc6fc44.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/314da147ebfddde4b88b39e289cd1e9d.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/d5d2787c3a84a262b0a277da3cc8db59.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/46bc602cd95d6422a51cf178627114a3.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/f4e180cf08e15ab62b40c3251b632014.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/106a4997ced9ee975584f34b4ce5c645.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/a984c8f1520cb1d0d82a066b3533dcb7.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/dbf6be933bcf5665a9d975ff071e8f4b.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/eb87051541ba0bb4b907b5e8e3b825b2.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/69017177c45949dc449294a7c30c89f3.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/27c95577d32070c96de13deb24413994.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/54563cdd1d70f77d61cd8a27b7b52f40.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/8872a5da903f0a5ecc6d2a8008048a3a.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/0fb81a6558c785eeb8585807f596fa59.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/50945890aef7aaad97a83c5c13165e06.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/06cf9f84e81731ec98071094304d3805.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/b39a62b5afa9fa54a9acacab907c8916.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/f66f61897cf8cf662dfbdba21e7ee44c.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/c3b916396d857413d9ee273cc6c8e8e6.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/8f8d6c818f472f4eb5f33fb1be5da975.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/cbd0adb5d57d33a33e848f0a47d111bb.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/a7a39369cfe19c6eb11e82db9e542c5b.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/dc9ff4f6ec87c7366e35c1db5196be45.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/8119c8109e96bd28eff912624a0a116d.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/31a3e0939fcd5a5f3d4087e4bda2fe71.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/6cf585ca4df73c84a2cfe4da25deca37.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/a845a21c25a58174ea6fbb39435de759.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/b6f722ce771f33e8b076df87590b0445.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/85a0540beafe5adea1896c3975f76a9a.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/2420725c6a61086c83bb2ff2d13e431b.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/26c57d3b7dce55efc469fcdf238b389e.version`
- `/usr/libexec/memoryanalyticsd`

</details>

## Feature Flags

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### Home.plist

>  `Domain/Home.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>ThreadTesterExperiment</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>UWB</key>
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
