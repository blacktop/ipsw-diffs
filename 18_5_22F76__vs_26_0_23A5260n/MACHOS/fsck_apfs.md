## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0x4cb74
-  __TEXT.__auth_stubs: 0x930
-  __TEXT.__cstring: 0x187ba
-  __TEXT.__const: 0x8104
-  __TEXT.__unwind_info: 0xa30
-  __DATA_CONST.__auth_got: 0x498
+2632.0.15.0.1
+  __TEXT.__text: 0x52de0
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__cstring: 0x19348
+  __TEXT.__const: 0x85f8
+  __TEXT.__unwind_info: 0xb48
+  __DATA_CONST.__auth_got: 0x5c8
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0x560
+  __DATA_CONST.__auth_ptr: 0x68
+  __DATA_CONST.__const: 0x610
   __DATA_CONST.__cfstring: 0x200
-  __DATA.__data: 0xed4
-  __DATA.__bss: 0x1c864
-  __DATA.__common: 0xab1
+  __DATA.__data: 0xef0
+  __DATA.__bss: 0x1e1e9
+  __DATA.__common: 0xac9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: CD0873CE-8CE5-337C-BCD8-BBBE794B49D0
-  Functions: 824
-  Symbols:   164
-  CStrings:  1866
+  UUID: AF2ACC82-F447-3478-A535-58865AA24A2F
+  Functions: 938
+  Symbols:   202
+  CStrings:  1940
 
Symbols:
+ _CCCryptorCreateWithMode
+ _CCCryptorDecryptDataBlock
+ _CCCryptorEncryptDataBlock
+ _CCCryptorRelease
+ _FSKitCheckContainerStart
+ _FSKitCheckDone
+ _FSKitCheckStart
+ _FSKitCheckUpdate
+ _abort
+ _calloc
+ _ccaes_cbc_decrypt_mode
+ _ccaes_cbc_encrypt_mode
+ _cccbc_clear_iv
+ _cccbc_init
+ _cccbc_update
+ _ccder_blob_decode_len
+ _ccder_blob_decode_range
+ _ccder_blob_decode_tag
+ _ccder_blob_decode_tl
+ _ccder_blob_encode_implicit_raw_octet_string
+ _ccder_blob_encode_implicit_uint64
+ _ccder_blob_encode_tl
+ _ccder_sizeof
+ _ccder_sizeof_implicit_uint64
+ _ccder_sizeof_raw_octet_string
+ _cchkdf
+ _cchmac
+ _ccn_read_uint
+ _ccpbkdf2_hmac
+ _ccrng
+ _dup
+ _mach_continuous_time
+ _mach_timebase_info
+ _nanosleep
+ _os_variant_has_internal_content
+ _panic
+ _read
+ _uuid_generate
CStrings:
+ "       -X            report progress to FSKit\n"
+ "       -r <num>      read password for encrypted external volume from file descriptor <num>\n"
+ "%s (%llu+%llu): %s records entry %u contains invalid keybag\n"
+ "%s (%llu+%llu): %s records entry %u contains invalid range %llu+%llu\n"
+ "%s (%llu+%llu): %s records entry %u does not contain a range (size %u)\n"
+ "%s (%llu+%llu): UUID %s of entry %u (tag %u) does not reference any volume\n"
+ "%s (%llu+%llu): UUID %s of entry %u (tag %u) is not the container UUID %s\n"
+ "%s (%llu+%llu): UUID of entry %u is null\n"
+ "%s (%llu+%llu): block range isn't a valid keybag, aborting\n"
+ "%s (%llu+%llu): block range isn't a valid keybag, skipping checks\n"
+ "%s (%llu+%llu): entry %u has 'unknown' tag type\n"
+ "%s (%llu+%llu): entry %u has blob size %u > maximum blob size %u\n"
+ "%s (%llu+%llu): entry %u has blob size == 0\n"
+ "%s (%llu+%llu): entry %u has invalid blob\n"
+ "%s (%llu+%llu): entry %u has invalid blob range %llu+%llu\n"
+ "%s (%llu+%llu): entry %u has invalid padding\n"
+ "%s (%llu+%llu): entry %u has size %u > maximum size %u\n"
+ "%s (%llu+%llu): entry %u has size %u > remaining size %u (keybag size %u)\n"
+ "%s (%llu+%llu): entry %u with size %u brings total size %u beyond object size %u\n"
+ "%s (%llu+%llu): failed to allocate memory\n"
+ "%s (%llu+%llu): failed to get keybag data: %s\n"
+ "%s (%llu+%llu): failed to put keybag: %s\n"
+ "%s (%llu+%llu): invalid padding\n"
+ "%s (%llu+%llu): number of bytes %u does not match sum of all entries %u\n"
+ "%s (%llu+%llu): number of bytes %u exceeds object size %u\n"
+ "%s (%llu+%llu): number of entries %u exceeds object capacity %lu\n"
+ "%s (%llu+%llu): number of keys %u does not match number of entries found %u\n"
+ "%s (%llu+%llu): oti_ke_blob_cksum (0x%llx) is invalid for blob\n"
+ "%s (%llu+%llu): oti_ke_blob_len (%u) is too large\n"
+ "%s (%llu+%llu): size is too large\n"
+ "%s (%llu+%llu): unknown version %u\n, skipping checks\n"
+ "%s (%llu+%llu): version cannot be 0\n"
+ "%s (id %llu): unknown flags (0x%hx / known flags are: 0x%hx)\n"
+ "%s (id %llu): unknown flags (0x%x / known flags are: 0x%x)\n"
+ "%s (id %llu): unknown flags: (0x%02x / known flags are: 0x%02x)\n"
+ "%s (id %llu): unknown internal_flags (0x%llx / known flags are: 0x%llx)\n"
+ "%s (id %llu): xf %u/%u: %s: found in an unsupported volume\n"
+ "%s (id %llu): xf %u/%u: %s: invalid clonegroup_id (%llu), less than MIN_CLONEGROUP_ID (%u)\n"
+ "%s (id %llu): xf %u/%u: %s: invalid extended field size %u for type %u, expected %u"
+ "%s (id %llu): xf %u/%u: %s: invalid extended field size %u for type %u, expected %u\n"
+ "%s:%d: %s failed (E%d)\n"
+ "%s:%d: CCCryptorCreateWithMode failed (E%d)\n"
+ "%s:%d: Zero'ing excess data to %s: paddr %lld, completed %lld, remaining %zu\n"
+ "%s:%d: lib_get_file_vault_services failed (E%d)\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s %s unlock %s (%d)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sdump %s (len = %zd)%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sresult: %d; oti: %d; passcode_change: %d; cf: 0x%x; of: 0x%x; nf: 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Internal Error: Null KEK, file radar%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Internal Error: Null VEK, file radar%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s error %d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode blob%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode kek%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode vek%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to generate valid kek group uuid after 16 attempts%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s icloud recovery key%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s institutional recovery key%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek and unmanaged vek device protection mismatch vek:%x, kek:%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek constraint violation 1%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek constraint violation 2%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek failed to unwrap vek; mix-n-match?%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s personal recovery key%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s sep managed vek cannot have flag_no_ephdm%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unknown blob type %i%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unsupported vek type for sys disable%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unsupported vek type for sys enable%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s user uuid unexpectedly match new kek uuid%s\n"
+ "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "2632.0.15.0.1"
+ ":"
+ "AKS_FV_service"
+ "CLONEGROUP_EXT_TYPE_ATTRIBUTION_TAG"
+ "CLONEGROUP_EXT_TYPE_DIR_STATS_KEY"
+ "Can't read/write encrypted data to/from block 0!"
+ "Checking the clone group tree."
+ "Clone group tree is invalid."
+ "Decryption"
+ "Encryption"
+ "Failed to allocate memory for keybag\n"
+ "Failed to close password file descriptor: %s\n"
+ "Failed to get keybag : %s\n"
+ "Failed to get keybag entry with tag %d for volume %s\n"
+ "Failed to get password for encrypted volume from provided file descriptor: %s\n"
+ "Failed to unwrap encrypted volume keybag using the provided password: %s\n"
+ "Fix apfs_clonegroup_next_id(oid 0x%llx, xid 0x%llx)? "
+ "INO_EXT_TYPE_CLONEGROUP_ID"
+ "Invalid file descriptor passed\n"
+ "Keybag size is too large\n"
+ "NX jumpstart record range is invalid: 0x%llx+%llu\n"
+ "OTI"
+ "OTI blob"
+ "OTI keybag"
+ "REQUIRE_func"
+ "Remove entry with invalid blob range? "
+ "Remove entry with invalid blob? "
+ "Remove entry with invalid keybag? "
+ "Unset unknown flags? (0x%llx) "
+ "_bind_unmanaged_vek"
+ "_cmd_handle_vek"
+ "_create_kek_data"
+ "_enable_user_kek"
+ "_unlock_result"
+ "aks"
+ "apfs superblock at index %u: unknown clone group tree flags: 0x%x\n"
+ "apfs_clonegroup_next_id is not valid (expected %llu, actual %llu)\n"
+ "b:cCdE:fFglnMopqr:sSWxXyZTD"
+ "block 0 superblock"
+ "clone group mapping record exists for (group_id %llu, private_id %llu, file_id %llu), but no inode refers to it\n"
+ "clone group tree (id %llu): invalid key length (%u)\n"
+ "clone group tree: group_id (%llu) is invalid\n"
+ "clone group tree: invalid key length (%u)\n"
+ "clone group tree: unknown type (%u)\n"
+ "clone mapping (private_id %llu, file_id %llu): unknown flags (0x%x / known flags are: 0x%x)\n"
+ "clonegroup"
+ "clonegroup (group id %llu, private_id %llu, file id %llu): can't register for cross checks: %d (%s)\n"
+ "clonegroup (group id %llu, private_id %llu, file id %llu): inum is invalid\n"
+ "clonegroup (group id %llu, private_id %llu, file id %llu): invalid physical_size (%llu)\n"
+ "clonegroup (group id %llu, private_id %llu, file id %llu): invalid value length (%u)\n"
+ "clonegroup (group id %llu, private_id %llu, file id %llu): invalid xfields\n"
+ "clonegroup (group id %llu, private_id %llu, file id %llu): private_id is invalid\n"
+ "clonegroup (group id %llu, private_id %llu, file id %llu): unknown flags (0x%x / known flags are: 0x%x)"
+ "clonegroup_tree: "
+ "com.apple.FSKit"
+ "container keybag"
+ "decrypt"
+ "dump_bytes_internal"
+ "encrypt"
+ "error (%d) getting cab %u @ %lld\n"
+ "error (%d) getting cib %d bitmap %d @ %lld\n"
+ "error (%d) getting cib %u @ %lld\n"
+ "error (%d) getting cib bitmap %d @ %lld\n"
+ "failed"
+ "failed to enqueue clone group mapping (group_id %llu, private_id %llu, file_id %llu) for deletion: %s\n"
+ "failed to initialize the clone group tree: %s\n"
+ "failed to initialize the clone-group tree: %s\n"
+ "failed to register the clonegroup tree in the fsck memory storage\n"
+ "failed to register the purgeable tree in the fsck memory storage\n"
+ "found EFI jumpstart record of unknown version %d (max known: %d)\n"
+ "found clone group tree in invalid volume format\n"
+ "found clone mapping in an unsupported volume format\n"
+ "found orphan clone group mapping: (group_id %llu, private_id %llu, file_id %llu)\n"
+ "fv_decode_kek_blob_opts"
+ "fv_decrypt_vek"
+ "fv_encode_vek_blob"
+ "fv_get_blob_state"
+ "fv_kek_global_policy_eval"
+ "fv_rewrap_kek"
+ "invalid EFI jumpstart record file length: %d\n"
+ "invalid EFI jumpstart record number of extents: %d\n"
+ "kek group"
+ "media keybag"
+ "missing clone group record for file_id %llu\n"
+ "nx_fusion_wbc should be empty but isn't\n"
+ "option -X is specified but FSKit is not present, ignoring\n"
+ "purgeable inode (id %llu) was unexpectedly registered twice\n"
+ "sm : free queue tree has sfq_count (%llu) greater than available block count (%llu)\n"
+ "snapshot fsroot / file key rolling / doc-id / clone group tree corruptions are not repaired; they'll go away once the snapshot is deleted\n"
+ "spaceman cab count %u is inconsistent with cib count %u and cibs per cab %u\n"
+ "spaceman chunk count %llu is inconsistent with block count %llu and blocks per chunk %u\n"
+ "spaceman cib count %u is inconsistent with chunk count %llu and chunks per cib %u\n"
+ "spaceman datazone current boundaries (%llu -> %llu) is not a valid address range on disk\n"
+ "spaceman datazone duplicate zone id (%hu) for allocation zones at indices (%hu, %hu)\n"
+ "spaceman datazone invalid previous boundary index (%hu)\n"
+ "spaceman datazone previous boundaries (%llu -> %llu) is not a valid address range on disk\n"
+ "spaceman datazone unknown zone id (%hu)\n"
+ "spaceman datazone zone id is zero but other fields are initialized\n"
+ "spaceman free count %llu does not match sum of free counts %llu\n"
+ "spaceman free count is too large: %llu > %llu\n"
+ "spaceman tier2 fields should be empty but they aren't\n"
+ "successful"
+ "the EFI jumpstart entry has length %u but occupies %llu blocks of size %u\n"
+ "the EFI jumpstart record magic number is invalid: 0x%x\n"
+ "unknown keybag"
+ "unlock"
+ "usage: fsck_apfs [ [-q | -n | -y] [-r num] [-l] [-s] [-W] [-S] [-o] [-b num] [-c] [-C] [-d]\n\t\t[-E path] [-F | -M] [-g | -x] [-X] [-T [-D]] ] device\n"
+ "user"
+ "userfs_data_cryptor"
+ "vek group"
+ "verification/reading of the EFI jumpstart record failed\n"
+ "volume keybag"
- "%lld bytes of space on the main tier are unaccounted for\n"
- "%s (id %llu): invalid internal_flags (0x%llx / valid-flags are: 0x%llx)\n"
- "%s (id %llu): unknown flags (0x%hx)\n"
- "%s (id %llu): unknown flags (0x%x / valid-flags: 0x%x)\n"
- "%s (id %llu): unknown flags (0x%x)\n"
- "%s keybag (%llu+%llu): UUID %s of entry %u (tag %u) does not reference any volume\n"
- "%s keybag (%llu+%llu): UUID %s of entry %u (tag %u) is not the container UUID %s\n"
- "%s keybag (%llu+%llu): UUID of entry %u is null\n"
- "%s keybag (%llu+%llu): block range isn't a valid keybag, aborting\n"
- "%s keybag (%llu+%llu): block range isn't a valid keybag, skipping checks\n"
- "%s keybag (%llu+%llu): entry %u has 'unknown' tag type\n"
- "%s keybag (%llu+%llu): entry %u has invalid padding\n"
- "%s keybag (%llu+%llu): entry %u has size %u > maximum size %u\n"
- "%s keybag (%llu+%llu): entry %u has size %u > remaining size %u (keybag size %u)\n"
- "%s keybag (%llu+%llu): entry %u with size %u brings total size %u beyond object size %u\n"
- "%s keybag (%llu+%llu): failed to allocate memory\n"
- "%s keybag (%llu+%llu): failed to get keybag: %s\n"
- "%s keybag (%llu+%llu): failed to put keybag: %s\n"
- "%s keybag (%llu+%llu): invalid padding\n"
- "%s keybag (%llu+%llu): number of bytes %u does not match sum of all entries %u\n"
- "%s keybag (%llu+%llu): number of bytes %u exceeds object size %u\n"
- "%s keybag (%llu+%llu): number of entries %u exceeds object capacity %lu\n"
- "%s keybag (%llu+%llu): number of keys %u does not match number of entries found %u\n"
- "%s keybag (%llu+%llu): size is too large\n"
- "%s keybag (%llu+%llu): unknown version %u\n, skipping checks\n"
- "%s keybag (%llu+%llu): unlock records entry %u contains invalid range %llu+%llu\n"
- "%s keybag (%llu+%llu): unlock records entry %u does not contain a range (size %u)\n"
- "%s keybag (%llu+%llu): version cannot be 0\n"
- "...Decrementing fwp_dirtyInRC by %llu, new value: %llu\n"
- "...Elevating a Dirty mapping [0x%llx -> 0x%llx, %llu]\n"
- "2332.120.31.0.2"
- "Checking the Fusion data structures."
- "Checking the fusion superblock."
- "Dirty"
- "Failed to elevate the content for Dirty mapping [0x%llx -> 0x%llx, %llu]: %s\n"
- "Fix an orphaned %s MT mapping [0x%llx -> 0x%llx, %llu]? "
- "Fix corrupt 2nd-tier device container superblock? "
- "Fix orphaned MT mappings? "
- "Found a partially orphaned %s mapping [0x%llx -> 0x%llx, %llu], where [0x%llx -> 0x%llx, %llu] region is not backed by WBCL.\nThis is currently not supported, skipping\n"
- "Fusion data structures are invalid."
- "Fusion superblock is invalid."
- "Fusion with FS block size (%u) != container device block size (%u)\n"
- "MT mapping (0x%llx -> 0x%llx, %llu, %c%s) is not completely referenced\n"
- "RCStash: The stashed range is invalid: 0x%llx+%llu\n"
- "Secondary"
- "T"
- "Tenant"
- "Unable to write WBC Instance object (LBA 0x%llx): %s\n"
- "Unset invalid flags? (0x%llx) "
- "b:cCdE:fFglnMopqsSWxyZTD"
- "clone mapping (private_id %llu, file_id %llu): unknown flags (0x%x)\n"
- "error (%d) getting cab %u @ %lld on device %d\n"
- "error (%d) getting cib %d bitmap %d @ %lld on device %d\n"
- "error (%d) getting cib %u @ %lld on device %d\n"
- "error (%d) getting cib bitmap %d @ %lld on device %d\n"
- "failed to allocate %zd bytes for APFS Fusion data\n"
- "failed to initialize the Fusion MT tree: %s\n"
- "failed to initialize the fusion middle tree: %s\n"
- "fusion caches"
- "fusion metadata"
- "fusion middle tree: WBC mapping must have only the Dirty (0x%x) flag set (0x%llx -> 0x%llx:%llu Flags:0x%x)\n"
- "fusion middle tree: bogus combination of flags. Dirty (0x%x) and Tenant (0x%x) flags are mutually exclusive (0x%llx -> 0x%llx:%llu Flags:0x%x)\n"
- "fusion middle tree: invalid \"from\" range 0x%llx:%llu\n"
- "fusion middle tree: invalid \"to\" range 0x%llx:%llu\n"
- "fusion middle tree: invalid key length %u (expected %lu)\n"
- "fusion middle tree: invalid value length %u (expected %lu)\n"
- "fusion mt: W2RC dirty blocks count (%llu) is smaller than number of dirty blocks found in MT (%llu)\n"
- "fusion mt: total RC blocks count (%llu) is smaller than number of blocks found in MT (%llu)\n"
- "fusion wbc: WBC list OIDs are not consistent: Head: 0x%llx, Tail: 0x%llx\n"
- "fusion wbc: WBC list chunk (oid 0x%llx) has incorrect tailOffset %llu, should be >%llu, >=%llu, and <=%llu\n"
- "fusion wbc: WBC list chunk (oid 0x%llx) has invalid first index %u\n"
- "fusion wbc: WBC list chunk (oid 0x%llx) has invalid last index %u\n"
- "fusion wbc: WBC list chunk (oid 0x%llx) has max entries %u != %u\n"
- "fusion wbc: WBC list entry 0x%llx+%llu is intersecting the WBC range 0x%llx+%llu\n"
- "fusion wbc: WBC list entry has invalid target range (0x%llx->0x%llx+%llu), Tier2: 0x%llx+%llu\n"
- "fusion wbc: WBC list entry has target range 0x%llx+%llu which is outside of Tier2 size\n"
- "fusion wbc: WBC list head OID 0x%llx is not in the WBC range\n"
- "fusion wbc: WBC list object OID 0x%llx is not in the WBC range\n"
- "fusion wbc: WBC list tail OID 0x%llx is not in the WBC range\n"
- "fusion wbc: bogus index combination in WBC list chunk (oid 0x%llx): %u starts after %u\n"
- "fusion wbc: expected %llu W2RC dirty blocks but found %llu\n"
- "fusion wbc: expected %u list chunks but found %u\n"
- "fusion wbc: stable head offset (%llu) is greater than tail (%llu)\n"
- "fusion_mid_tree: "
- "main superblock"
- "media"
- "nx_fusion_mt_oid is invalid\n"
- "nx_fusion_wbc range is invalid: 0x%llx+%llu\n"
- "nx_fusion_wbc_oid is invalid\n"
- "physical metadata object (0x%llx + %llu) type %u subtype %u) is on Tier2 and inside the MT mapped range\n"
- "recovery extent #%llu: invalid Fusion prange (0x%llx+%llu)\n"
- "sm : free queue tree TIER (%s) has sfq_count (%llu) greater than available block count (%llu)\n"
- "snapshot fsroot / file key rolling / doc-id tree corruptions are not repaired; they'll go away once the snapshot is deleted\n"
- "spaceman %s cab count %u is inconsistent with cib count %u and cibs per cab %u\n"
- "spaceman %s chunk count %llu is inconsistent with block count %llu and blocks per chunk %u\n"
- "spaceman %s cib count %u is inconsistent with chunk count %llu and chunks per cib %u\n"
- "spaceman %s datazone current boundaries (%llu -> %llu) is not a valid address range on disk\n"
- "spaceman %s datazone duplicate zone id (%hu) for allocation zones at indices (%hu, %hu)\n"
- "spaceman %s datazone invalid previous boundary index (%hu)\n"
- "spaceman %s datazone previous boundaries (%llu -> %llu) is not a valid address range on disk\n"
- "spaceman %s datazone unknown zone id (%hu)\n"
- "spaceman %s datazone zone id is zero but other fields are initialized\n"
- "spaceman %s free count %llu does not match sum of free counts %llu\n"
- "spaceman %s free count is too large: %llu > %llu\n"
- "tier2"
- "tier2 superblock"
- "usage: fsck_apfs [ [-q | -n | -y] [-l] [-s] [-W] [-S] [-o] [-b num] [-c] [-C] [-d]\n\t\t[-E path] [-F | -M] [-g | -x] [-T [-D]] ] device\n"
- "wbc"
- "wbcl"

```
