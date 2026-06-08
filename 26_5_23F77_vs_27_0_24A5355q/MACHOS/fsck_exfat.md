## fsck_exfat

> `/System/Library/Filesystems/exfat.fs/fsck_exfat`

```diff

-522.100.20.0.0
-  __TEXT.__text: 0xa428
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__const: 0x252
-  __TEXT.__cstring: 0x2c84
+560.0.0.0.0
+  __TEXT.__text: 0xcb58
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__const: 0x280
+  __TEXT.__cstring: 0x35af
   __TEXT.__oslogstring: 0x18
-  __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x218
+  __TEXT.__unwind_info: 0x228
+  __DATA_CONST.__const: 0x370
   __DATA_CONST.__cfstring: 0x60
-  __DATA.__data: 0x28f8
-  __DATA.__bss: 0x2018
-  __DATA.__common: 0x180
+  __DATA_CONST.__auth_got: 0x308
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA.__data: 0x2948
+  __DATA.__thread_vars: 0x60
+  __DATA.__thread_bss: 0x40
+  __DATA.__bss: 0xa4
+  __DATA.__common: 0x248
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
-  UUID: 68E7A06B-19A7-3443-9E01-EB0EF34A1F2F
-  Functions: 174
-  Symbols:   103
-  CStrings:  363
+  UUID: 59E55276-61EF-3547-A987-97C3F7AE51AF
+  Functions: 189
+  Symbols:   115
+  CStrings:  377
 
Symbols:
+ __Block_object_dispose
+ ___strlcpy_chk
+ __dispatch_queue_attr_concurrent
+ __tlv_bootstrap
+ _dispatch_group_async
+ _dispatch_group_create
+ _dispatch_group_wait
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dup
+ _pthread_mutex_destroy
+ _pthread_mutex_init
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
- _CFArrayRemoveAllValues
- _CFSetRemoveAllValues
- _sprintf
CStrings:
+ "%08X: %02X should be %02X"
+ "%llu total sectors; %u bytes per sector"
+ "%u clusters starting at sector %u; %u bytes per cluster"
+ "%u clusters were marked free, but referenced"
+ "%u clusters were marked used and CLUST_BAD"
+ "%u clusters were marked used, but not referenced"
+ "--- [%d] Evicted %d buffers (%u bytes; %u pages)"
+ "B16@?0^(exfat_direntry=C{exfat_direntry_volname=CC[11{uint16le=S}][8C]}{exfat_direntry_upcase=C[3C]{uint32le=I}[12C]{uint32le=I}{uint64le=Q}}{exfat_direntry_bitmap=CC[18C]{uint32le=I}{uint64le=Q}}{exfat_direntry_guid=CC{uint16le=S}{uint16le=S}{exfat_guid={uint32le=I}{uint16le=S}{uint16le=S}[8C]}[10C]}{exfat_direntry_file=CC{uint16le=S}{uint16le=S}{uint16le=S}{uint32le=I}{uint32le=I}{uint32le=I}CCCCC[7C]}{exfat_direntry_stream=CCCC{uint16le=S}[2C]{uint64le=Q}[4C]{uint32le=I}{uint64le=Q}}{exfat_direntry_filename=CC[15{uint16le=S}]}{exfat_direntry_vendor=CC{exfat_guid={uint32le=I}{uint16le=S}{uint16le=S}[8C]}[14C]}{exfat_direntry_vendor_alloc=CC{exfat_guid={uint32le=I}{uint16le=S}{uint16le=S}[8C]}[2C]{uint32le=I}{uint64le=Q}}{exfat_direntry_generic_primary=CC{uint16le=S}{uint16le=S}[14C]{uint32le=I}{uint64le=Q}}{exfat_direntry_generic_secondary=CC[18C]{uint32le=I}{uint64le=Q}})8"
+ "B20@?0^(exfat_direntry=C{exfat_direntry_volname=CC[11{uint16le=S}][8C]}{exfat_direntry_upcase=C[3C]{uint32le=I}[12C]{uint32le=I}{uint64le=Q}}{exfat_direntry_bitmap=CC[18C]{uint32le=I}{uint64le=Q}}{exfat_direntry_guid=CC{uint16le=S}{uint16le=S}{exfat_guid={uint32le=I}{uint16le=S}{uint16le=S}[8C]}[10C]}{exfat_direntry_file=CC{uint16le=S}{uint16le=S}{uint16le=S}{uint32le=I}{uint32le=I}{uint32le=I}CCCCC[7C]}{exfat_direntry_stream=CCCC{uint16le=S}[2C]{uint64le=Q}[4C]{uint32le=I}{uint64le=Q}}{exfat_direntry_filename=CC[15{uint16le=S}]}{exfat_direntry_vendor=CC{exfat_guid={uint32le=I}{uint16le=S}{uint16le=S}[8C]}[14C]}{exfat_direntry_vendor_alloc=CC{exfat_guid={uint32le=I}{uint16le=S}{uint16le=S}[8C]}[2C]{uint32le=I}{uint64le=Q}}{exfat_direntry_generic_primary=CC{uint16le=S}{uint16le=S}[14C]{uint32le=I}{uint64le=Q}}{exfat_direntry_generic_secondary=CC[18C]{uint32le=I}{uint64le=Q}})8I16"
+ "Cannot allocate a buffer for iterating dir entries"
+ "Cannot allocate a buffer for iterating the directory"
+ "Cannot allocate a buffer for processing directory"
+ "Cannot allocate a buffer for scanning the root directory"
+ "Cannot create a generated name for %s"
+ "Checking bitmap cluster %u"
+ "Could not allocate dir cluster cache buffer"
+ "Could not allocate dir cluster cache buffer data"
+ "Could not allocate dir cluster cache thread buffer"
+ "Could not dup() file descriptor"
+ "Could not get directory buffer"
+ "Could not initialize bitmap mutex"
+ "Could not initialize cache mutex"
+ "Could not initialize message mutex"
+ "Could not initialize progress mutex"
+ "Could not read directory data from disk"
+ "Could not read from disk"
+ "Could not write to disk"
+ "Directory %s"
+ "Directory /"
+ "FAT starts at sector %u; size %u sectors"
+ "FSOPS_ReadBootSector: Cluster size not supported: %u"
+ "File      %s"
+ "Found active bitmap; first cluster %u, length %llu"
+ "Found upcase table; starting cluster %u, length %llu"
+ "QUICKCHECK ONLY; CORRUPTION FOUND"
+ "QUICKCHECK ONLY; FILESYSTEM CLEAN"
+ "QUICKCHECK ONLY; FILESYSTEM DIRTY"
+ "QUICKCHECK ONLY; FILESYSTEM MARKED CORRUPT"
+ "Read      offset = 0x%012llx  length = 0x%06lx"
+ "Renaming completed in %s"
+ "Renaming failed in %s"
+ "Renaming items in %s"
+ "Root directory starts at cluster %u"
+ "The volume %s could not be verified completely and cannot be repaired."
+ "The volume %s was found corrupt and cannot be repaired."
+ "Trying to read from an invalid cluster number"
+ "Trying to write to an invalid cluster number"
+ "Write     offset = 0x%012llx  length = 0x%06x"
+ "dirsToProcess.access"
+ "fsck_exfat_process_dir"
+ "fsck_exfat_recurse.work_queue"
+ "vm.memory_pressure = %u"
+ "vm.page_free_wanted = %u"
- " * * * cannot allocate memory * * *\n"
- "%08X: %02X should be %02X\n"
- "%llu total sectors; %u bytes per sector\n"
- "%u clusters starting at sector %u; %u bytes per cluster\n"
- "%u clusters were marked free, but referenced\n"
- "%u clusters were marked used and CLUST_BAD\n"
- "%u clusters were marked used, but not referenced\n"
- "--- [%d] Evicted %d buffers (%u bytes; %u pages)\n"
- "Cannot create a generated name for %s\n"
- "Checking bitmap cluster %u\n"
- "Could not write clusters for directory %s\n"
- "Directory %s\n"
- "Directory /\n"
- "FAT starts at sector %u; size %u sectors\n"
- "FSOPS_ReadBootSector: Cluster size not supported: %u\n"
- "File      %s\n"
- "Found active bitmap; first cluster %u, length %llu\n"
- "Found upcase table; starting cluster %u, length %llu\n"
- "Hash bitmap collision: index: %u\n"
- "QUICKCHECK ONLY; CORRUPTION FOUND\n"
- "QUICKCHECK ONLY; FILESYSTEM CLEAN\n"
- "QUICKCHECK ONLY; FILESYSTEM DIRTY\n"
- "QUICKCHECK ONLY; FILESYSTEM MARKED CORRUPT\n"
- "Read      offset = 0x%012llx  length = 0x%06lx\n"
- "Renaming completed in %s\n"
- "Renaming failed in %s\n"
- "Renaming items in %s\n"
- "Root directory starts at cluster %u\n"
- "The volume %s could not be verified completely and can not be repaired."
- "The volume %s was found corrupt and can not be repaired."
- "Write     offset = 0x%012llx  length = 0x%06x\n"
- "dir->refs != 0"
- "dir->refs > 0"
- "fsck_exfat_dir_ref"
- "fsck_exfat_dir_rele"
- "fsck_exfat_recurse"
- "path != NULL"
- "vm.memory_pressure = %u\n"
- "vm.page_free_wanted = %u\n"

```
