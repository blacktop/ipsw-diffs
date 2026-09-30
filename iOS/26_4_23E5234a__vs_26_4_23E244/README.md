# 26.4 (23E5234a) .vs 26.4 (23E244)

## Inputs

- `iPhone18,1_26.4_23E5234a_Restore.ipsw`
- `iPhone18,1_26.4_23E244_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.4 *(23E5234a)* | 25.4.0 | 12377.102.10~4 | Fri, 06Mar2026 00:08:59 PST |
| 26.4 *(23E244)* | 25.4.0 | 12377.102.10~3 | Thu, 05Mar2026 23:59:10 PST |

### Kexts

#### ❌ Removed (1)

- `com.apple.kec.AppleEncryptedArchive`

### ⬆️ Updated (7)

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
-  UUID: 6A1F7719-178A-39F6-BB33-BD06A6601ECB
+  UUID: 42F1CF30-9643-3E16-8DDF-2CF51E387D5B
   Functions: 1225
   Symbols:   0
   CStrings:  1152
Functions:
~ __ZN23AppleAOPAudioController5startEP9IOService : 472 -> 492
CStrings:
+ "20:18:49"
+ "20:19:09"
+ "Mar  9 2026"
- "23:10:43"
- "23:10:46"
- "Mar  5 2026"

```

#### com.apple.driver.AppleIDV

>  `com.apple.driver.AppleIDV`

```diff

-8.419.1.0.0
+8.420.0.0.0
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x145e
+  __TEXT.__cstring: 0x145c
   __TEXT_EXEC.__text: 0x7a98
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xe38
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 5F6F2F10-4D5B-3537-842F-5221A7B24C55
+  UUID: 88D54FFE-A543-3E22-A644-51C2AEAB2924
   Functions: 187
   Symbols:   0
   CStrings:  126
CStrings:
+ "8.420"
- "8.419.1"

```

#### com.apple.driver.corecapture

>  `com.apple.driver.corecapture`

```diff

   __TEXT.__os_log: 0x42ec
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x200e
-  __TEXT_EXEC.__text: 0x2612c
+  __TEXT_EXEC.__text: 0x260f8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x308

   __DATA_CONST.__const: 0x7010
   __DATA_CONST.__kalloc_type: 0x10c0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 36B271C8-B7B4-30A3-8065-FA682FA9C708
+  UUID: B3ABE4F3-36FE-3E02-AE16-FB949BE4E55D
   Functions: 878
   Symbols:   0
   CStrings:  660
Functions:
~ __Z34corecaptureIsDevFusedOrCSRInternalb : 120 -> 100
~ __Z29corecaptureIsDebuggbleUnifiedv : 100 -> 116
~ __ZN6CCPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptions : 6308 -> 6272
~ __Z16DefaultLogPolicyv : 100 -> 108
~ __ZN11CCIOService17ccForcePanic_ImplEbP8OSString : 188 -> 184
~ __ZN16CCPipeUserClient12initWithTaskEP4taskPvjP12OSDictionary : 356 -> 352
~ sub_fffffe000a586598 -> sub_fffffe000a57cb70 : 12 -> 8
~ sub_fffffe000a58db0c -> sub_fffffe000a5840e0 : 192 -> 188
~ sub_fffffe000a59db28 -> sub_fffffe000a5940f8 : 100 -> 96

```

#### com.apple.filesystems.apfs

>  `com.apple.filesystems.apfs`

```diff

   __TEXT.__cstring: 0x4d27e
   __TEXT_EXEC.__text: 0x147ca8
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x70c
-  __DATA.__bss: 0xd60
+  __DATA.__data: 0x704
+  __DATA.__bss: 0xd68
   __DATA_CONST.__auth_got: 0x1170
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__kalloc_type: 0x5080
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: 31CFE55A-DC5E-3FF3-9561-BF38231DD357
+  UUID: DA3A8A29-0BB4-301A-96A5-CE0CC1BFD234
   Functions: 2332
   Symbols:   0
   CStrings:  6678
CStrings:
+ "23:10:55"
- "23:10:43"

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
-  UUID: 9F711C7F-6F96-333C-9F9B-D3140E83559E
+  UUID: 4E79E206-01D8-3C68-98E4-5B3DD24D5F60
   Functions: 315
   Symbols:   0
   CStrings:  411
Functions:
~ __ZN22AppleARMDMAAudioDevice13startInternalEP9IOServicexjPKjS3_S3_S3_ : 1232 -> 1272

```

#### com.apple.kernel

>  `com.apple.kernel`

```diff

 12377.102.10.0.0
-  __TEXT.__const: 0x36150
+  __TEXT.__const: 0x36080
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x8843d
+  __TEXT.__cstring: 0x84aed
   __TEXT.__os_log: 0x3dd23
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x119d48
-  __DATA_CONST.__kalloc_type: 0x14540
+  __DATA_CONST.__const: 0x119cd8
+  __DATA_CONST.__kalloc_type: 0x14200
   __DATA_CONST.__assert: 0xc58
   __DATA_CONST.__kalloc_var: 0x78f0
   __DATA_CONST.__exclaves_bt: 0x78
-  __DATA_CONST.__kern_brk_desc: 0x78
+  __DATA_CONST.__kern_brk_desc: 0x60
   __DATA_CONST.__mod_init_func: 0x2d8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x8b3e40
+  __TEXT_EXEC.__text: 0x8a0720
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
-  __DATA.__lock_grp: 0x5b18
+  __DATA.__lock_grp: 0x5a68
   __DATA.__percpu: 0x7870
-  __DATA.__common: 0x77778
-  __DATA.__bss: 0xa3588
+  __DATA.__common: 0x775d8
+  __DATA.__bss: 0xa3578
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x135a8
+  __BOOTDATA.__init_entry_set: 0x13500
   __BOOTDATA.__init: 0x5b568
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x48024
-  UUID: 8A400573-143C-3FC7-A6D3-B881A2B3C271
-  Functions: 21315
+  UUID: DBD79AEF-148B-33AC-8B5D-3563CED1D8F3
+  Functions: 21108
   Symbols:   0
-  CStrings:  20734
+  CStrings:  20428
 
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

 2680.100.174.0.0
   __TEXT.__os_log: 0x2272
-  __TEXT.__const: 0x1c8b79
+  __TEXT.__const: 0x1c8c69
   __TEXT.__cstring: 0x72d6
   __TEXT_EXEC.__text: 0x38ab0
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x3858
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: 957C4C5B-CBC2-35A9-8044-9AF58582E492
+  UUID: 209BBFC5-A48D-3F9A-8EB9-30D41C4B74CB
   Functions: 651
   Symbols:   0
   CStrings:  1344

```


</details>

## MachO

### ❌ Removed (2)

- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/usr/libexec/memoryanalyticsd`

### ⬆️ Updated (174)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
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
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/SupportFlow.app/SupportFlow](MACHOS/SupportFlow.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/Vehicle.app/Vehicle](MACHOS/Vehicle.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/ExclaveKit/System/Library/Frameworks/T8150_IR_ISP_EK_Component.framework/T8150_IR_ISP_EK_Component_asan](MACHOS/T8150_IR_ISP_EK_Component_asan.md)
- [/System/ExclaveKit/System/Library/Frameworks/T8150_RGB_ISP_EK_Component.framework/T8150_RGB_ISP_EK_Component_asan](MACHOS/T8150_RGB_ISP_EK_Component_asan.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/T8150_ExclaveISPSharedLib_exclavekit.framework/T8150_ExclaveISPSharedLib_exclavekit_asan](MACHOS/T8150_ExclaveISPSharedLib_exclavekit_asan.md)
- [/System/Library/Assistant/Plugins/activity.assistantBundle/activity](MACHOS/activity.md)
- [/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod](MACHOS/usbaudiod.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_fullsize_archive_bin.metallib](MACHOS/portrait_filters_fullsize_archive_bin.metallib.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/FullKeyboardAccess.app/FullKeyboardAccess](MACHOS/FullKeyboardAccess.md)
- [/System/Library/CoreServices/HangHUD.app/HangHUD](MACHOS/HangHUD.md)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard](MACHOS/SpringBoard.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/ADAskForExceptionExtension.appex/ADAskForExceptionExtension](MACHOS/ADAskForExceptionExtension.md)
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension.md)
- [/System/Library/ExtensionKit/Extensions/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider](MACHOS/AmbientPhotoFramePosterProvider.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/CloudWorker.appex/CloudWorker](MACHOS/CloudWorker.md)
- [/System/Library/ExtensionKit/Extensions/InferenceExtension.appex/InferenceExtension](MACHOS/InferenceExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseAVExtension.appex/LighthouseAVExtension](MACHOS/LighthouseAVExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseAVShadowEval.appex/LighthouseAVShadowEval](MACHOS/LighthouseAVShadowEval.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/Space.metallib](MACHOS/Space.metallib.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance.md)
- [/System/Library/Frameworks/CoreImage.framework/redeye_repair_archive_bin.metallib](MACHOS/redeye_repair_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/DigitalTouchBalloonProvider.bundle/DigitalTouchBalloonProvider](MACHOS/DigitalTouchBalloonProvider.md)
- [/System/Library/NanoTimeKit/FaceBundles/KaleidoscopeFaceBundle.bundle/NTKKaleidoscopeShaders.metallib](MACHOS/NTKKaleidoscopeShaders.metallib.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAlaskanFaceBundleCompanion.bundle/NTKAlaskanFaceBundleCompanion](MACHOS/NTKAlaskanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKColorAnalogFaceBundleCompanion.bundle/NTKColorAnalogFaceBundleCompanion](MACHOS/NTKColorAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCrosswindFaceBundleCompanion.bundle/NTKCrosswindFaceBundleCompanion](MACHOS/NTKCrosswindFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKDolomiteFaceBundleCompanion.bundle/NTKDolomiteFaceBundleCompanion](MACHOS/NTKDolomiteFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExactitudesFaceBundle.bundle/NTKExactitudesFaceBundle](MACHOS/NTKExactitudesFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExtraLargeFaceBundleCompanion.bundle/NTKExtraLargeFaceBundleCompanion](MACHOS/NTKExtraLargeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKKuiperFaceBundleCompanion.bundle/NTKKuiperFaceBundleCompanion](MACHOS/NTKKuiperFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKProteusFaceBundleCompanion.bundle/NTKProteusFaceBundleCompanion](MACHOS/NTKProteusFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKWarlockFaceBundle.bundle/NTKWarlockFaceBundle](MACHOS/NTKWarlockFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKZeusFaceBundleCompanion.bundle/NTKZeusFaceBundleCompanion](MACHOS/NTKZeusFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/HomeSettings.bundle/HomeSettings](MACHOS/HomeSettings.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](MACHOS/KeyboardSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PrivateFrameworks/ACTFramework.framework/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
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
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd](MACHOS/nanosystemsettingsd.md)
- [/System/Library/PrivateFrameworks/NanoUniverse.framework/NUNICalliopeShadersCompanion.metallib](MACHOS/NUNICalliopeShadersCompanion.metallib.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService](MACHOS/PersonalizedSensingService.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/metal_libraries/binary.metallib](MACHOS/binary.metallib.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/VideoProcessors/CCPortrait.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/ColourConstancyV1.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/STF.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/SmartStyleV1.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/VideoDeghostingV3.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SpotlightIndexExtension.appex/com.apple.mobilenotes.SpotlightIndexExtension](MACHOS/com.apple.mobilenotes.SpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/usr/bin/footprint](MACHOS/footprint.md)
- [/usr/bin/vm_stat](MACHOS/vm_stat.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/accessorysensormgrd](MACHOS/accessorysensormgrd.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/checkpointd](MACHOS/checkpointd.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/debugserver](MACHOS/debugserver.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/heartratecoordinatord](MACHOS/heartratecoordinatord.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/perfdiagsselfenabled](MACHOS/perfdiagsselfenabled.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/signpost_reporter](MACHOS/signpost_reporter.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/sysmond](MACHOS/sysmond.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/uarpassetmanagerd](MACHOS/uarpassetmanagerd.md)
- [/usr/libexec/uarpd](MACHOS/uarpd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/BTLEServer](MACHOS/BTLEServer.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (6)

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
-  UUID: 0C1D9ED4-B050-331C-9C80-7CA53D4D40DE
+  UUID: 14B82C0D-DDD7-379C-B25E-AF9F55AF20DB
   Functions: 1218
   Symbols:   1704
   CStrings:  2645
CStrings:
+ "Caller is /Library/Caches/com.apple.xbs/58C61ECF-C38D-408E-94A7-30E24FB899FC/TemporaryDirectory.EiTSni/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:751"
+ "Caller is /Library/Caches/com.apple.xbs/58C61ECF-C38D-408E-94A7-30E24FB899FC/TemporaryDirectory.EiTSni/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:756"
- "Caller is /Library/Caches/com.apple.xbs/C3FD5FD8-D776-42BD-81D3-7805D32DDDD0/TemporaryDirectory.Shz8k0/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:751"
- "Caller is /Library/Caches/com.apple.xbs/C3FD5FD8-D776-42BD-81D3-7805D32DDDD0/TemporaryDirectory.Shz8k0/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:756"

```

#### agx_a000

>  `agx_a000`

```diff

   __TEXT.__gxf_code: 0x4c18
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__const: 0x1063
+  __TEXT.__const: 0x1053
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
   __TEXT.__cstring: 0x2291

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x59cd8
-  UUID: F1BE227E-1BE1-3A80-A368-D2C84F56491F
-  Functions: 405
+  UUID: A201F8F2-8EC7-38EB-B84D-E8F25B6C7FA0
+  Functions: 403
   Symbols:   173
   CStrings:  227
 
CStrings:
+ "Mar  6 2026 18:58:33"
- "Mar  6 2026 00:34:02"

```

#### agx_a010

>  `agx_a010`

```diff

   __TEXT.__gxf_code: 0x4c18
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__const: 0x1063
+  __TEXT.__const: 0x1053
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
   __TEXT.__cstring: 0x2347

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x59cd8
-  UUID: 18AB6F1C-ADFB-3C85-B475-9B7FC8C576C8
-  Functions: 404
+  UUID: 2EEC5D17-830A-378E-A54B-2AA78DF37B07
+  Functions: 402
   Symbols:   173
   CStrings:  229
 
CStrings:
+ "Mar  6 2026 19:06:41"
- "Mar  6 2026 00:41:31"

```

#### agx_b000

>  `agx_b000`

```diff

   __TEXT.__gxf_code: 0x4c18
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__const: 0x1063
+  __TEXT.__const: 0x1053
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
   __TEXT.__cstring: 0x2347

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x59cd8
-  UUID: BE846794-7651-32D6-BFBE-62AD4D974663
-  Functions: 404
+  UUID: 731EC34E-96F6-3ED0-8E3D-A9EC11829367
+  Functions: 402
   Symbols:   173
   CStrings:  229
 
CStrings:
+ "Mar  6 2026 19:04:23"
- "Mar  6 2026 00:39:26"

```

#### exclave_roottask

>  `exclave_roottask`

```diff

 1195.100.161.0.1
-  __TEXT.__text: 0x4a9be4
+  __TEXT.__text: 0x4a9ad8
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__const: 0xedb30
   __TEXT.__cstring: 0x3a9bc

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x78
-  __TEXT.__eh_frame: 0x1ce84
+  __TEXT.__eh_frame: 0x1cecc
   __DATA.__data: 0xbd78
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58

   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  UUID: E8E0D8C6-35FD-3A94-B0E9-EB2B147F2A0D
+  UUID: 31C300AA-FF7A-330E-B552-41B9204A9B26
   Functions: 17674
   Symbols:   27
   CStrings:  5883
Functions:
~ sub_c0143830 : 612 -> 528
~ sub_c0143a94 -> sub_c0143a40 : 660 -> 576
~ sub_c0143d28 -> sub_c0143c80 : 776 -> 696
~ sub_c0144030 -> sub_c0143f38 : 676 -> 584
~ sub_c01442d4 -> sub_c0144180 : 596 -> 512
~ sub_c01449e8 -> sub_c0144840 : 196 -> 200
~ sub_c0144aac -> sub_c0144908 : 236 -> 204
~ sub_c0144d2c -> sub_c0144b68 : 184 -> 168
~ sub_c0144de4 -> sub_c0144c10 : 264 -> 236
~ sub_c014557c -> sub_c014538c : 2564 -> 2792
~ sub_c04aad74 -> sub_c04aac68 : 52 -> 48
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CKc6ugBFCtwaINnCO_AFUeP5AO1JGqyfId5QTp4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
+ "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
+ "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
+ "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"
- "/AppleInternal/Library/BuildRoots/4~CKc8ugBrK6UEEMrtBEvoVwvzNTTJh7rbyoMpUy4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
- "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
- "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
- "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

 1148.102.2.0.0
-  __TEXT.__text: 0x5c27c4
+  __TEXT.__text: 0x5c2638
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__cstring: 0x488d1
   __TEXT.__const: 0x112d64

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xa8
-  __TEXT.__eh_frame: 0x32d38
+  __TEXT.__eh_frame: 0x32d40
   __DATA.__TIGHTBEAM_VT: 0x5d0
   __DATA.__TIGHTBEAM: 0x180
   __DATA.__data: 0x141f8

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: E9818650-16FC-39A7-8184-FACE8DC17E09
-  Functions: 23491
+  UUID: FA272EF1-5954-3A3B-981A-0BBD968B9E3E
+  Functions: 23482
   Symbols:   1
   CStrings:  6782
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CKc6ugBFCtwaINnCO_AFUeP5AO1JGqyfId5QTp4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdBugDpDb1f62stbsiRpO2tTtx56OZ6w_7SkBY/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdDugBXDMZz_Zxp1t6BVFjiTb28D9115blvm7U/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
+ "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
+ "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
+ "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"
- "/AppleInternal/Library/BuildRoots/4~CKc8ugBrK6UEEMrtBEvoVwvzNTTJh7rbyoMpUy4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CKdCugAbbCg5Y6ZPLAs7-VewFHjnbwDJ5xvxD4M/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CKdDugDVFJTUdwc-vewnIM7HNlS9L9Cc68CEwRg/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
- "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
- "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
- "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/38654669-3D8C-477A-8AF9-671D0460B30A/TemporaryDirectory.9FkaWh/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.4 *(23E5234a)* | mBoot-18000.102.3 |
| 26.4 *(23E244)* | mBoot-18000.102.4 |

#### ❌ Removed (1)

<details>
  <summary><i>View Removed</i></summary>

##### `iboot`
  - `dart,t6710`

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.4 *(23E5234a)* | 624.1.16.10.6 |
| 26.4 *(23E244)* | 624.1.16.10.6 |

### Dylibs

#### 🆕 NEW (1)

- `/System/Library/PrivateFrameworks/StreamingAppleTrace.framework/StreamingAppleTrace`

#### ⬆️ Updated (198)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/Moments.axbundle/Moments](DYLIBS/Moments.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth](DYLIBS/CoreBluetooth.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/FoundationModels.framework/FoundationModels](DYLIBS/FoundationModels.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/Frameworks/PushKit.framework/PushKit](DYLIBS/PushKit.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers](DYLIBS/UniformTypeIdentifiers.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKLeghornFaceBundle.bundle/NTKLeghornFaceBundle](DYLIBS/NTKLeghornFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing](DYLIBS/ASEProcessing.md)
- [/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings](DYLIBS/AUDeveloperSettings.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreComponentsDaemonKit.framework/AppStoreComponentsDaemonKit](DYLIBS/AppStoreComponentsDaemonKit.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal](DYLIBS/AppleMediaServicesKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIKitInternal.framework/AppleMediaServicesUIKitInternal](DYLIBS/AppleMediaServicesUIKitInternal.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CentauriDiagnostic.framework/CentauriDiagnostic](DYLIBS/CentauriDiagnostic.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer](DYLIBS/CiderAudioServer.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI](DYLIBS/CloudDocsUI.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera](DYLIBS/CompanionCamera.md)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore](DYLIBS/CoordinationCore.md)
- [/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon](DYLIBS/CoreCaptureDaemon.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred](DYLIBS/CoreIDCred.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](DYLIBS/CoreSpeechExclave.md)
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
- [/System/Library/PrivateFrameworks/GPUToolsCore.framework/GPUToolsCore](DYLIBS/GPUToolsCore.md)
- [/System/Library/PrivateFrameworks/GPUToolsReplay.framework/GPUToolsReplay](DYLIBS/GPUToolsReplay.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager](DYLIBS/HeadphoneManager.md)
- [/System/Library/PrivateFrameworks/HeadphoneProxFeatureService.framework/HeadphoneProxFeatureService](DYLIBS/HeadphoneProxFeatureService.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettingsUI.framework/HeadphoneSettingsUI](DYLIBS/HeadphoneSettingsUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingModeSettingsUI.framework/HearingModeSettingsUI](DYLIBS/HearingModeSettingsUI.md)
- [/System/Library/PrivateFrameworks/HearingTestUI.framework/HearingTestUI](DYLIBS/HearingTestUI.md)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities](DYLIBS/HearingUtilities.md)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
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
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement](DYLIBS/MetricMeasurement.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon](DYLIBS/MobileAssetDaemon.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MomentsIntelligence.framework/MomentsIntelligence](DYLIBS/MomentsIntelligence.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach](DYLIBS/NewDeviceOutreach.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/ProductKitCore.framework/ProductKitCore](DYLIBS/ProductKitCore.md)
- [/System/Library/PrivateFrameworks/SOS.framework/SOS](DYLIBS/SOS.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SensingAlgsTouchButtonHost.framework/SensingAlgsTouchButtonHost](DYLIBS/SensingAlgsTouchButtonHost.md)
- [/System/Library/PrivateFrameworks/Sentry.framework/Sentry](DYLIBS/Sentry.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightIndex.framework/SpotlightIndex](DYLIBS/SpotlightIndex.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TeaState.framework/TeaState](DYLIBS/TeaState.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligenceCore.framework/VisualIntelligenceCore](DYLIBS/VisualIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/VisualIntelligenceUI.framework/VisualIntelligenceUI](DYLIBS/VisualIntelligenceUI.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/VideoCodecs/VCPHEVC.videocodec](DYLIBS/VCPHEVC.videocodec.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libchannel.dylib](DYLIBS/libchannel.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/updaters/libAppleTconUARPUpdater.dylib](DYLIBS/libAppleTconUARPUpdater.dylib.md)
- [/usr/lib/usd/libusd_ms.dylib](DYLIBS/libusd_ms.dylib.md)

</details>

## Files

### 🆕 New

#### filesystem (209)

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
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/CoreTypes-0038.bundle/Info.plist`
- `/System/Library/NanoTimeKit/FaceBundles/NTKZeusFaceBundleCompanion.bundle/Zeus-SS2026.color.plist`
- `/System/Library/NanoTimeKit/FaceBundles/NTKZeusFaceBundleCompanion.bundle/ZeusBellona-SS2026.color.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/b6d1f77af36d18e8770c5b6373dca798a588ebd6.asset/AssetData/CountrySpecificCn0Settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/b6d1f77af36d18e8770c5b6373dca798a588ebd6.asset/AssetData/UnitedStatesSettings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/b6d1f77af36d18e8770c5b6373dca798a588ebd6.asset/AssetData/countryInfoMap.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/b6d1f77af36d18e8770c5b6373dca798a588ebd6.asset/AssetData/settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/b6d1f77af36d18e8770c5b6373dca798a588ebd6.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/bfb579a9106a350616a79943bb2c3b4e79d57520.asset/AssetData/CountrySpecificCn0Settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/bfb579a9106a350616a79943bb2c3b4e79d57520.asset/AssetData/UnitedStatesSettings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/bfb579a9106a350616a79943bb2c3b4e79d57520.asset/AssetData/countryInfoMap.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/bfb579a9106a350616a79943bb2c3b4e79d57520.asset/AssetData/settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/bfb579a9106a350616a79943bb2c3b4e79d57520.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f949be2b5bc29e8d9e985afc0fa7fbf4a3559fb0.asset/AssetData/settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f949be2b5bc29e8d9e985afc0fa7fbf4a3559fb0.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/7f50a81a71f8ff6cebbf2d151474b0256a253146.asset/AssetData/empty.txt`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/7f50a81a71f8ff6cebbf2d151474b0256a253146.asset/Info.plist`
- `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/AssetPaths-Seed.plist`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-PersonalizedVolumeAirPodsMaxDark.ca/index.xml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-PersonalizedVolumeAirPodsMaxDark.ca/main.caml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-PersonalizedVolumeAirPodsMaxLight.ca/index.xml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-PersonalizedVolumeAirPodsMaxLight.ca/main.caml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL18.ca/assetManifest.caml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL18.ca/assets/AirPodsMax1-2_CL-18_Translate_v14.png`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL18.ca/assets/Gradient_sq.png`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL18.ca/assets/mask.svg`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL18.ca/index.xml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL18.ca/main.caml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL19.ca/assetManifest.caml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL19.ca/assets/AirPodsMax1-2_CL-19_Translate_v14.png`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL19.ca/assets/Gradient_sq.png`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL19.ca/assets/mask.svg`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL19.ca/index.xml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL19.ca/main.caml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL20.ca/assetManifest.caml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL20.ca/assets/AirPodsMax1-2_CL-20_Translate_v14.png`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL20.ca/assets/Gradient_sq.png`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL20.ca/assets/mask.svg`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL20.ca/index.xml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL20.ca/main.caml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL21.ca/assetManifest.caml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL21.ca/assets/AirPodsMax1-2_CL-21_Translate_v14.png`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL21.ca/assets/Gradient_sq.png`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL21.ca/assets/mask.svg`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL21.ca/index.xml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL21.ca/main.caml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL22.ca/assetManifest.caml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL22.ca/assets/AirPodsMax1-2_CL-22_Translate_v14.png`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL22.ca/assets/Gradient_sq.png`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL22.ca/assets/mask.svg`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL22.ca/index.xml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-Translate-CL22.ca/main.caml`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/B515d-iOS-Localizable.loctable`
- `/System/Library/PrivateFrameworks/HeadphoneAssets.framework/Localizable-PID_8237.loctable`
- `/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/DeviceConfig-Seed.loctable`
- `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingProtection-B515d.loctable`
- `/System/Library/PrivateFrameworks/NanoTimeKit.framework/FaceColors-SS2026.color.plist`
- `/System/Library/PrivateFrameworks/NanoTimeKit.framework/FaceColors-SS2026.loctable`
- `/System/Library/PrivateFrameworks/Sharing.framework/Localizable-PID_8237.loctable`
- `/System/Library/PrivateFrameworks/StreamingAppleTrace.framework/Info.plist`
- `/System/Library/PrivateFrameworks/StreamingAppleTrace.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/ar.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/bg.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/bn.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/ca.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/cs.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/da.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/de.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/el.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/en.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/en_AU.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/en_GB.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/es.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/es_419.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/es_US.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/fi.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/fr.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/fr_CA.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/gu.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/he.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/hi.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/hr.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/hu.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/id.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/it.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/ja.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/kk.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/kn.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/ko.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/lt.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/ml.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/mr.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/ms.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/nl.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/no.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/or.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/pa.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/pl.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/pt_BR.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/pt_PT.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/ro.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/ru.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/sk.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/sl.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/sv.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/ta.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/te.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/th.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/tr.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/uk.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/ur.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/vi.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/yue_CN.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/zh_CN.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/zh_HK.lproj/Localizable-b515d.strings`
- `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/zh_TW.lproj/Localizable-b515d.strings`
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
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/1c7d866428c8fb03213e4f462d437630.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/b149d0ebc0369eb429cfe53002649fd9.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/7c621b4618a9866f4a9b9c0d3e7efc91.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/1f4f2590f71eec79f954823a0876dd5a.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/65e84983f70ad24b5ea3e456ecc8f1c3.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/16a72b18044f1fe73052c9bba17bf3c9.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/b9c201451e32b6c32ab371568bf59582.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/1f14d37c733dcab07ff9c1d903af2789.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/e675c475dc3d67f47e15a7efbda72df1.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/c34855cd200a6614b639d53aba6feffa.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/a78d5fa1059731e714482f65cfef6199.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/2c240b479b8fb0a15a284670774e0b73.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/6ab11b97be9fb855cccdfa9a5cb32017.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/4fb115d7d2dc1ff5028e2fd45a4fa640.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/ed5499c68c067a8f4a94f657be68c82d.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/4df97ca8c680cfbfabaf5ca956118041.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/275848c5f4f9801cfefc0b5fb098fb00.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/32f34ee69fb61ab8755f97cd9a6cc43f.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/3027e37e1e036852cf2597b504f2a211.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/b86c9bb886067cab2c01b830927bcc1b.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/232d0ba168b09894189d9bb2fdbc045f.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/24d0d294a202c53dad75f799c790bc95.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/83b00f6ef4985298027fd70f7097d7ad.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/b1425fdac133ee03290d1ac2cfd14048.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/c71794af9c3c76889b8722d73d6d1d62.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/0f9205629ec968dc328a38fe3aa77068.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/ba125917c75bb3903dd678b4d45bbe4c.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/c9ffef49db95dcbf7ca10f58b815ee03.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/852d862e45b7460f6c91299205cacfc4.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/60c8ec75d34a7d8ae2fabb36fd9a1e91.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/9db9030390b6d9fae08e7b0641de1816.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/904641f74606238c8cdb3157db2a2391.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/e70fb0644dad5e696ad08858a83174e6.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/7d83e0ed6d794c0146a2d9fc57274496.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/b835b8cd38dd09e54d2436b464e540d0.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/2920ed2f4a8e1e746dec3f2be6eba2c2.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/1d59fecfb0592ad236204297377cab12.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/624648f78d8714dd4786ff2fa33a714e.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/35a9945e145a5b0923502546f5294816.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/d0e044d11334c03fa0770c72d57ee870.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/c3e087fb401472017e734b5f440b56c1.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/ea9cf5ac23315eb15c14d39090c5774d.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/c1cc105c0b7ad4295a4a404d01de8a3c.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/dc458f33dacee2169b87efbac9f25662.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/93a40c7d02805ce3814c1317bbc9e4e4.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/e24c58a82b6d5707e3cc15517b291a8e.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/7c8e86e6696bd52c3afd1e2e03a3f79e.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/5bfaa21b8bc32b7e75327504d7200d66.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/f0d5a922ecc2829326b75ac612faae3a.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/e71bb8f730bbb49877c5e5f3c8d40bce.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/053ea6dedc99f819162dba1a4d12e4ce.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/2af35046e5edcab9ddf8b1c523decace.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/5fba69e8915074c68e490fa9d88ea6b4.version`

</details>

### ❌ Removed

#### filesystem (82)

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
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/Info.plist`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/Home.framework/com.apple.Home.framework.plist`
- `/System/Library/PrivateFrameworks/Home.framework/com.apple.Home.plist`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/23938c113b21e447606cd39b1049058f.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/1844dcbf25b8ee90da25ec52123bc633.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/272688d72778475a4e0df12948c929fa.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/9fbbcc5eaa708013f13b494d9a4bd6b7.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/a0e2d3c0f552ef9c6af6f2d4cfe4b903.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/bc5b449cc27206cca155a64c9657e800.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/23177957fcd7ebcce11ad258d2e207aa.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/48611ad973ddf1773bf38dba9fdf6350.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/fa1fb6a8703e01c1a1f053542d874f40.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/6bdb9cd6076d3a8e7898026d8718d112.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/19f1920cb56ac10832e20a930e2cbb55.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/2cfd5c9754f64eb49cf31c882a590978.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/4ad9fcbfe5c4cc9a12782ed8ba892212.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/93c1ac7d9afc5dcde223ea460fe4efcf.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/78c4138226c84d3c18abbf5051beffc5.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/61c3e5523504ebeaf8502933da0b216c.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/7c4fb90069ed5d9c6759aa6554a841f9.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/5bf7f28568e5bcea1696161d6c3009d4.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/89cd8fc98968cdb594dce9c30588fd35.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/98c9e81d755c98c4a5aa07ead2a26331.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/263fdaa1d32acc2ee7a9c240e3c1f408.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/e04ca72edc377bbae58871189a1a569e.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/e8b061871f694bda8ad60d311bd7c1ee.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/89b3fe61bf3f397d0ef918c6b68e8359.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/c5bb5f6c160a27f8468b1bdb3e1ffae2.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/bc935cb6200b7d56cbb98f676e8c12a2.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/d9fb533710322c3a9ddf463b13e747e2.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/f1384b866c9b06ebb4d26f4b3ab311a7.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/6ec806ac8b82a3b7a98c3da95f090ff4.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/f9b6dd3cf1d6f8768779d07de0ba4558.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/1d634bf53790a8caccb2c1d043b4486f.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/31851ae07d24b779b258f7aabd26964a.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/4a40a9353836b7e1efa8cffff493e999.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/04035b932b7a632af077bc5ffef852b6.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/0492a0d041ece292ddd57fe4f6d12677.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/8cb5ca5bf31fa23de6a46cbb6197c317.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/3f0d18256aae0f898361803a96bb2468.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/0753683449e1bf589d23432335960935.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/d4066b10caed76bb4b60f6c6b0fb44c5.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/47c6a9b22414372aa56b3ef543bfef00.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/75969732a2cd8a24c822298aa5d09ef9.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/2a33ec7e470d762a00f8d1b3f515a0c1.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/a7cc1c1926d1c3c04b508fa4510afa01.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/448a7ed0e4d65b3e050052968b039d19.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/7557fd23df9dc7f32892b36f616f5ed7.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/989b814670ac679786f7a50849facc2d.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/2521acc4aa517a38db6857bd712ebfb5.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/fabad1a63032940574d58868faf40526.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/ccaafad225bbc3aa5e8c0d2338227a93.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/a82fe55d66a9743ff5abdcf5ecb18981.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/6c769de4593acdbd6d72b2899838e94e.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/631424b67c2c27a9a39c07a027d7d84a.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/3210e8ecc970f1c3d7e19304a9673251.version`
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
