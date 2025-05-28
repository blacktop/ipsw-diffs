## libAppleArchive.dylib

> `/usr/lib/libAppleArchive.dylib`

```diff

-398.0.0.0.0
-  __TEXT.__text: 0x771f0
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__cstring: 0xfd7d
-  __TEXT.__const: 0x8ec
+405.100.1.0.0
+  __TEXT.__text: 0x844b4
+  __TEXT.__auth_stubs: 0xed0
+  __TEXT.__cstring: 0x114ce
+  __TEXT.__const: 0x922
   __TEXT.__oslogstring: 0x21
-  __TEXT.__unwind_info: 0xc70
+  __TEXT.__unwind_info: 0xd8c
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0xc0
-  __AUTH_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0xd8
+  __AUTH_CONST.__auth_ptr: 0x40
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__const: 0x70
-  __AUTH_CONST.__auth_got: 0x750
+  __AUTH_CONST.__auth_got: 0x768
   __DATA.__data: 0x8
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
-  Functions: 992
-  Symbols:   1954
-  CStrings:  2581
+  Functions: 1088
+  Symbols:   2146
+  CStrings:  2828
 
Symbols:
+ _AAJSONInputStreamClose
+ _AAJSONInputStreamOpen
+ _AAJSONInputStreamRead
+ _BXDiff5Data_free
+ _ForkOutputStreamCancel
+ _ForkOutputStreamClose
+ _ForkOutputStreamPWrite
+ _ForkOutputStreamWrite
+ _InSituStreamCancel
+ _InSituStreamClose
+ _InSituStreamPRead
+ _InSituStreamPWrite
+ _InSituStreamSimulate
+ _InSituTruncate
+ _IntervalStreamCancel
+ _IntervalStreamClose
+ _IntervalStreamPRead
+ _IntervalStreamRead
+ _IntervalStreamSeek
+ _RawImageDiff
+ _RawImagePatchInternal
+ _SegmentStreamCancel
+ _SegmentStreamClose
+ _SegmentStreamCreate
+ _SegmentStreamPRead
+ _SegmentStreamPWrite
+ _SegmentStreamSimulate
+ _SimStreamClose
+ _SimStreamPRead
+ _SimStreamPWrite
+ _SimStreamSimulate
+ _aaArchiveFileOutputStreamOpenAtWithState
+ _aaAssetDecryptionStreamOpenWithState
+ _aaByteStreamSimulate
+ _aaCacheStreamCancel
+ _aaCacheStreamClose
+ _aaCacheStreamOpen
+ _aaCacheStreamPRead
+ _aaCacheStreamPWrite
+ _aaCacheStreamRead
+ _aaCacheStreamSeek
+ _aaCacheStreamTruncate
+ _aaCacheStreamWrite
+ _aaForkInputStreamOpen
+ _aaForkOutputStreamOpen
+ _aaInSituStreamOpen
+ _aaIntervalInputStreamOpen
+ _aaSegmentStreamOpen
+ _aggregate_copy_fork
+ _aggregate_identical_forks
+ _apfs_scan_diskimage
+ _cacheFlush
+ _cachePageEvict
+ _cachePageGet
+ _cachePageReadFromDisk
+ _calloc
+ _ccaes_ctr_crypt_mode
+ _cchkdf
+ _cchmac_final
+ _cchmac_init
+ _cchmac_update
+ _ccsha256_di
+ _compare_copy_fork_3
+ _compare_copy_fork_4
+ _compare_copy_fork_5
+ _compare_digest_tasks
+ _compare_extents_by_position
+ _compare_forks_by_extent
+ _compare_forks_by_position
+ _controls_combo_enforce_copy_fork_boundary
+ _ctrl_reader_get
+ _feof
+ _ferror
+ _fread
+ _free_page
+ _io_preallocate
+ _io_set_nocache
+ _jsonPushLabel
+ _jsonPushValue
+ _load_variants
+ _malloc
+ _patch_write_controls
+ _pc_array_aggregate
+ _pc_array_compare
+ _pc_array_indirect_sort
+ _pc_array_sort
+ _pc_log_info
+ _pclose
+ _popen
+ _rand
+ _rawimg_add_fork
+ _rawimg_add_volume
+ _rawimg_create_with_path
+ _rawimg_create_with_stream
+ _rawimg_destroy
+ _rawimg_digest_worker
+ _rawimg_force_in_place
+ _rawimg_force_in_place.pass_name
+ _rawimg_free_chunks
+ _rawimg_get_digests
+ _rawimg_save_to_stream
+ _rawimg_set_fork_types
+ _rawimg_show
+ _rawimg_verify
+ _realloc
+ _remap_page
+ _restoreThreadErrorContext
+ _saveThreadErrorContext
+ _segment_find
+ _serializeHexString
+ _strcasecmp
+ _strtoull
+ _valloc
- _CCCryptorCreateWithMode
- _CCCryptorFinal
- _CCCryptorGetOutputLength
- _CCCryptorRelease
- _CCCryptorUpdate
- _CCDeriveKey
- _CCHmacFinal
- _CCHmacInit
- _CCHmacUpdate
- _CCKDFParametersCreateHkdf
- _CCKDFParametersDestroy
- _malloc_type_calloc
- _malloc_type_malloc
- _malloc_type_realloc
- _malloc_type_valloc
CStrings:
+ "    - %s stream: %llu bytes\n"
+ "  - Variants:   %d\n  - Flags:      %llx\n  - # controls: %llu\n  - Patch size: %llu bytes\n    - Metadata: %llu bytes\n    - Controls: %llu bytes\n"
+ "  In-place: %s\n"
+ "  Input %zu: %s\n"
+ "  Metadata: %llu bytes\n  Controls: %llu bytes\n"
+ "  Output: %s\n"
+ "  Patch: %s\n"
+ " fork | %64s | algo |       size | compressed | V | C\n"
+ "%12llu final patch size\n"
+ "%5zu | %s | %4d | %10llu | %10llu | %d | %d\n"
+ "%i dangling reads"
+ "%s \"%s\""
+ "%s stream: %llu bytes -> %llu bytes\n"
+ "%s variant <%s> | %llu bytes | %zu extents | %zu forks (%llu/%llu) | digest=%s\n"
+ "%s%s/%s"
+ "%s-%zd.dmg"
+ "%s.json"
+ "%s/%s"
+ "(stream based)"
+ "*full replacement*"
+ ".dmg"
+ "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AACacheStream.c"
+ "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
+ "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/APFS/APFS.c"
+ "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiff.c"
+ "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiffInPlace.c"
+ "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageOutputStream.c"
+ "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImagePatch.c"
+ "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageStreams.c"
+ "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/InSituStream.c"
+ "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/RawImage.c"
+ "/System/Library/Filesystems/apfs.fs/Contents/Resources"
+ "AAByteStreamPRead"
+ "AADecompressionInputStreamOpen"
+ "AAJSONInputStreamOpen"
+ "AAJSONInputStreamRead"
+ "CacheStream: read ops %zu/%zu, write ops %zu/%zu\n"
+ "Diff"
+ "Dropping %llu bytes at %llu, needed=%llu bytes, type %s\n"
+ "Dropping copy fork with %llu bytes, needed=%llu bytesx\n"
+ "EOF reached"
+ "ForceInPlace %d: excess_pages=%d/%d, converted bytes=%llu, %zu controls\n"
+ "ForceInPlace: %zu controls. Dropped %llu bytes to stay within budget.\n"
+ "ForkOutputStreamClose"
+ "ForkOutputStreamPWrite"
+ "ForkOutputStreamWrite"
+ "HKDF"
+ "HMACDerive_SHA256"
+ "ImageDiff\n"
+ "ImageDiff: Constructed %zd combo controls.\n"
+ "ImageDiff: Processed copy forks: %zd controls\n"
+ "ImageDiff: Removed non-unique input variant <%s>.\n"
+ "ImagePatch\n  Input:        %s\n  Output:       %s\n  Patch:        %s\n  CryptexCache: %s\n"
+ "ImagePatch: Digest match. Copy input to output.\n"
+ "ImagePatch: Digest match. Output already correct.\n"
+ "ImagePatch: Digest match. Output reconstructed.\n"
+ "ImagePatch: No variant found"
+ "ImagePatch: Patch not created with in place. No bound on needed excess space."
+ "ImagePatch: Patching with excess space <= %d bytes.\n"
+ "ImagePatch: Preallocation failed."
+ "InSituStream: pages: %i file, %i written, %i remapped, %i free, %i excess (%iK)\n"
+ "InSituStreamClose"
+ "InSituStreamPRead"
+ "InSituStreamPWrite"
+ "InSituStreamSimulate"
+ "Input"
+ "Literal"
+ "MASTERING_TOOLCHAIN_DIR"
+ "Output"
+ "PC_APFS_DISKIMAGE_MAP"
+ "RawImageDiff"
+ "RawImagePatchInternal"
+ "SIZE MISMATCH"
+ "SegmentStreamCreate"
+ "SegmentStreamPRead"
+ "SegmentStreamPWrite"
+ "SegmentStreamSimulate"
+ "SimStream: pages: %i file, %i written, %i free, %i excess (%iK)\n"
+ "SimStreamClose"
+ "SimStreamSimulate"
+ "aaArchiveFileOutputStreamOpenAtWithState"
+ "aaAssetDecryptionStreamOpenWithState"
+ "aaByteStreamSimulate"
+ "aaCacheStreamClose"
+ "aaCacheStreamOpen"
+ "aaCacheStreamPRead"
+ "aaCacheStreamPWrite"
+ "aaCacheStreamSeek"
+ "aaCacheStreamTruncate"
+ "aaFileStreamGetFD"
+ "aaForkInputStreamOpen"
+ "aaForkOutputStreamOpen"
+ "aaInSituStreamOpen"
+ "aaIntervalInputStreamOpen"
+ "aaSegmentStreamOpen"
+ "aaSegmentStreamProcess"
+ "aaSimStreamOpen"
+ "aaStrdup"
+ "add_fork"
+ "alloc buf"
+ "alloc holes"
+ "allocate_page"
+ "apfs_diskimage_map"
+ "apfs_scan_diskimage"
+ "bad algo"
+ "bad chunk"
+ "bad chunk info"
+ "bad chunk order"
+ "bad controls"
+ "bad duplicate"
+ "bad extent"
+ "bad extent pos"
+ "bad extent size"
+ "bad flags"
+ "bad fork"
+ "bad fork size"
+ "bad header"
+ "bad image"
+ "bad index"
+ "bad interval"
+ "bad map"
+ "bad page"
+ "bad seek"
+ "bad variant"
+ "bad write mode"
+ "cache too big"
+ "cacheFlush"
+ "cachePageEvict"
+ "cachePageGet"
+ "cachePageReadFromDisk"
+ "cacheRead"
+ "cacheWrite"
+ "callback signaled abort"
+ "chunk error"
+ "chunk out of bounds"
+ "compressed content"
+ "compressed fork"
+ "compression"
+ "compression_decode_buffer"
+ "control sequence broken"
+ "control_reader_create"
+ "controls_append_copy_forks"
+ "controls_combo_enforce_copy_fork_boundary"
+ "controls_create_with_variants"
+ "copy fork"
+ "copy fork not found"
+ "could not locate the apfs diskimage map tool"
+ "creating compression stream %s"
+ "ctrl_reader_create"
+ "ctrl_reader_get"
+ "data missing"
+ "data not locked"
+ "digest"
+ "digest mismatch"
+ "duplicate fork"
+ "empty controls"
+ "encryption"
+ "extents"
+ "extents overlapping"
+ "false"
+ "fcntl"
+ "file + excess != written + free"
+ "file < written"
+ "file not empty"
+ "file not open"
+ "files"
+ "fork chunks"
+ "fork footer"
+ "fork header"
+ "fork_realign"
+ "fork_write_index"
+ "image size mismatch"
+ "init"
+ "invalid JSON state"
+ "invalid char %c %s"
+ "invalid image map JSON"
+ "io_preallocate"
+ "io_set_nocache"
+ "io_set_nocache %s"
+ "jsonPushLabel"
+ "jsonPushValue"
+ "length"
+ "load_variants"
+ "loading AFSC stream state"
+ "lstat"
+ "max level reached"
+ "merge_controls"
+ "no chunk info"
+ "no chunks found"
+ "no digest info"
+ "no digests found"
+ "no fork extents"
+ "no free pages"
+ "no possible conversions"
+ "no segment found"
+ "non fork"
+ "not implemented"
+ "null"
+ "offset"
+ "parseAPFSJSON"
+ "patch_apply"
+ "patch_read_header"
+ "patch_read_variants"
+ "patch_write"
+ "patch_write_controls"
+ "patch_write_metadata"
+ "patch_write_stream"
+ "pc_array_compress"
+ "pc_array_indirect_sort"
+ "pending compressed fork"
+ "preallocating %llu B"
+ "preallocation %llu/%llu B took %0.2f seconds (# of calls=%i)"
+ "preallocation failed"
+ "r"
+ "rawimg_add_fork"
+ "rawimg_compact"
+ "rawimg_create_with_file"
+ "rawimg_create_with_path"
+ "rawimg_create_with_stream"
+ "rawimg_digest_worker"
+ "rawimg_force_in_place"
+ "rawimg_get_digests"
+ "rawimg_init_algorithm"
+ "rawimg_load_chunks_from_stream"
+ "rawimg_query_forks"
+ "rawimg_remove_fork_duplicates"
+ "rawimg_save_to_stream"
+ "rawimg_set_fork_types"
+ "rawimg_verify"
+ "read error: %zd"
+ "reading from tool pipe"
+ "realign_fork"
+ "realignment failed"
+ "remap_page"
+ "segment out of range"
+ "segment_add"
+ "segment_decode_to_buffer"
+ "snprintf"
+ "stat"
+ "storeFileContents %s"
+ "stream not compatible"
+ "stream not compatible\n"
+ "temp stream open"
+ "too little excess"
+ "too many excess pages"
+ "too many tasks"
+ "too many variants"
+ "too much data"
+ "too much padding"
+ "true"
+ "uncompressed_size"
+ "unexpected read call"
+ "virtual fork"
+ "volumes"
+ "writing tool output"
- "AEAD can't operate in-place"
- "CCDeriveKey"
- "CCKDFParametersCreateHkdf"
- "Cryptor creation"
- "Encryption"
- "Too many chunks"
- "creating compression stream"
- "need to build full path, then open fstream"

```
