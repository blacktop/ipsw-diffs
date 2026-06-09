## fsck_exfat

> `/System/Library/Filesystems/exfat.fs/fsck_exfat`

```diff

-522.100.20.0.0
-  __TEXT.__text: 0xa428 sha256:9b8a2fc5685439bc7d88899868fa3f9b5375807407f6eaf0f2389ef813b18ea2
-  __TEXT.__auth_stubs: 0x570 sha256:ec2880e82aa2ecc54d0cfb0ec3ad9a71bb19c274b92f0cef0e032a9948011765
-  __TEXT.__const: 0x252 sha256:26c12a6e365dc8c469ee3bcc3a3932ef19addfaa02dc72cd4048022604830d5e
-  __TEXT.__cstring: 0x2c84 sha256:cf4bf48d231cde2c23a6cc694af362c24911b6ed3694bdf168e502d757a4b240
+560.0.0.0.0
+  __TEXT.__text: 0xcb58 sha256:133c63e2e82596dcf2895a81806beb9000c952d427a7611b88e2c4a5e39bc38b
+  __TEXT.__auth_stubs: 0x610 sha256:e2fc0a89518dd212059e20caddc4061df44c3e5d0ed5c5c1e503a535c9f0a0ef
+  __TEXT.__const: 0x280 sha256:7195e34e7a90870ffff0ddff2f76c8fd46296f6f84d44a153c5c8cbdde2dda6b
+  __TEXT.__cstring: 0x35af sha256:d2c1737503a3887025d60985b2d4439cb6e7d8929ccc2c27b53cf93a3b4a2e93
   __TEXT.__oslogstring: 0x18 sha256:2f5c8452cad40caa630676517b32db7e8fcfb932e3a11025367ea5ca22d86503
-  __TEXT.__unwind_info: 0x1e8 sha256:b1687a1835c2826dad40e2ddc655c80d099c41ed613cb4008034be35af071dd4
-  __DATA_CONST.__auth_got: 0x2b8 sha256:456be6a9b899807b3732656049644322c2c8025ec0c03020ca31f700da1d7bbd
-  __DATA_CONST.__got: 0x58 sha256:25afb9b0b906bd9c5f7732344905bf5dd9a421d4fd3749c59b76be05978c73f8
-  __DATA_CONST.__auth_ptr: 0x18 sha256:888a93d59bac400530a132c634b2887fd3829950ad9d3783a35390c321dbb486
-  __DATA_CONST.__const: 0x218 sha256:ab9fdb8ce9c187627d47eff38683a1859ea760724ccbd8149abc911dde4864f6
-  __DATA_CONST.__cfstring: 0x60 sha256:257d8705212c2afb68c0f91c2df18cae4d90fb3464b772e1e4be03dc00bff00f
-  __DATA.__data: 0x28f8 sha256:1d0efac5c3b9cee45d7de0bc696f4006bab109d0f4f5da04f4c98056a0a419f2
-  __DATA.__bss: 0x2018 sha256:ec2e41443e26887c775950b27df7e8a3795ebbcaf0d86003c83190dac8326600
-  __DATA.__common: 0x180 sha256:c5d34530d2bfbc26a3ee82ca838775bcd550bbfccfe980f40b9ccfa89e880895
+  __TEXT.__unwind_info: 0x228 sha256:a0555a1cea7e3a0c158e64ad0b93d486b3be9b66d25ab0b187efac386ac384b9
+  __DATA_CONST.__const: 0x370 sha256:dada4950d8f4edd05161b617b4eee6a1619a693624c5de33dc95c5e1674342ab
+  __DATA_CONST.__cfstring: 0x60 sha256:9b8be7d213708c82a88c8fa11be7b91126dc6d9e1debb4520124b32b56f3b901
+  __DATA_CONST.__auth_got: 0x308 sha256:baa46f60448f9f3b7a6a662b8bd92eff8f7635f57c05944d3b14b09ef007f050
+  __DATA_CONST.__got: 0x60 sha256:e10e482ee9a16a703abd9edd24f418f4c38f8b4cf66d20b8b5840e26d4be6703
+  __DATA_CONST.__auth_ptr: 0x18 sha256:7b854965b460885758126eedfc04607d0d292d8af4aa422f784d857cc9f61976
+  __DATA.__data: 0x2948 sha256:51fe304e6c2904152e3b7036e9a7b9d9bcf16999bec1d96334f84665522cadf4
+  __DATA.__thread_vars: 0x60 sha256:de9272231c8a7b10543afb7cc63235a0bacdf29960d698450be9b40335492779
+  __DATA.__thread_bss: 0x40 sha256:f5a5fd42d16a20302798ef6ed309979b43003d2320d9f0e8ea9831a92759fb4b
+  __DATA.__bss: 0xa4 sha256:4b22ee6807a2e4ddfd1bf16851609a7a009f4c6bd5aeb78162f121cb89492f02
+  __DATA.__common: 0x248 sha256:62ec1707572ac5078d31a687a5d23de0c6d2a58d3462efb7039957548a7986cc
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
