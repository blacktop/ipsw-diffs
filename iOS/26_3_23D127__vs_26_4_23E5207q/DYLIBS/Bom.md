## Bom

> `/System/Library/PrivateFrameworks/Bom.framework/Bom`

```diff

-270.0.0.0.0
-  __TEXT.__text: 0x56494
-  __TEXT.__auth_stubs: 0x1840
-  __TEXT.__cstring: 0x119ea
-  __TEXT.__const: 0x1508
+276.0.0.0.0
+  __TEXT.__text: 0x5a358
+  __TEXT.__auth_stubs: 0x18d0
+  __TEXT.__cstring: 0x129f6
+  __TEXT.__const: 0x1728
   __TEXT.__oslogstring: 0x1011
-  __TEXT.__unwind_info: 0xa80
+  __TEXT.__unwind_info: 0xac8
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x9a8
-  __AUTH_CONST.__auth_got: 0xc20
+  __DATA_CONST.__const: 0x9a0
+  __AUTH_CONST.__auth_got: 0xc68
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x11c0
   __DATA.__data: 0x168

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F413EDE6-3B2A-3456-9D83-8F5D1DAADB10
-  Functions: 1051
-  Symbols:   2062
-  CStrings:  2434
+  UUID: C36E54F0-BEFA-3217-BD8D-7FFF2382ADC9
+  Functions: 1095
+  Symbols:   2156
+  CStrings:  2531
 
Symbols:
+ _BOMCopierSourceEntryNewFromFTSAgent
+ _BOMFileSetCloseOnFree
+ __MergedGlobals
+ ___drain_fts_state_block_invoke
+ __get_cpu_capabilities
+ _bom_crc32_finalize
+ _bom_crc32_update
+ _checksum_file
+ _child_allocate
+ _child_compare
+ _child_release
+ _choose_bom_crc32_type
+ _close_stack
+ _crc32_clever
+ _create_node
+ _data_stack_count
+ _data_stack_free
+ _data_stack_new
+ _data_stack_pop
+ _data_stack_push
+ _drain_fts_state
+ _dup
+ _error_message
+ _error_string
+ _fdopendir
+ _fgetattrlist
+ _fstatat
+ _fts_agent_close
+ _fts_agent_free
+ _fts_agent_new
+ _fts_agent_open
+ _fts_agent_read
+ _getattrlistbulk
+ _is_valid_utf8_string
+ _openat
+ _platform_basename_r
+ _platform_closedir
+ _platform_dup
+ _platform_errno
+ _platform_fdopendir
+ _platform_fprintf
+ _platform_fstat
+ _platform_getattrlistbulk
+ _platform_open
+ _platform_openat
+ _platform_qsort
+ _platform_readdir
+ _platform_readlinkat
+ _platform_realpath
+ _platform_snprintf
+ _platform_strerror
+ _platform_strncpy
+ _platform_vasprintf
+ _readlinkat
+ _release_fts_agent_state
+ _release_node
+ _utf8d
+ _vfprintf
- ___BOMBomNewFromDirectory_parallel_block_invoke
- _fts_compare
- _gHandler
- _gMessage
- _posix_checksum
- _release_discovery_state
CStrings:
+ "%s is not a file\n"
+ "%s is too long\n"
+ ".%s"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Bom/BOMBom.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Bom/BOMBomEnumerator.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Bom/BOMFSEnumerator.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Common/BOMBufferManager.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Common/BOMCRC32.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Common/BOMFile.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Common/BOMPatternList.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Common/BOMSystemCmds.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Copier/BOMCopier2.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Copier/BOMCopierDataAnalyzer.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Copier/BOMCopierDestination.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Copier/BOMCopierMatchRecord.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Copier/BOMCopierSource.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Copier/BOMCopierSourceEntry.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Copier/data_archive/data_archive.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Copier/data_archive/data_archive_decoder.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Copier/data_archive/data_archive_entry.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Copier/data_archive/data_stack.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Copier/data_archive/fts_agent.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/FSObject/BOMFSOArchInfo.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/FSObject/BOMFSOTypeInfo.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Storage/BOMStorage.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Storage/BOMStream.c"
+ "/Library/Caches/com.apple.xbs/A281C91D-CF7A-408A-8462-D83E73B234CA/TemporaryDirectory.cvOTAt/Sources/Bom/Storage/BOMTree.c"
+ "Actual name length doesn't match expected value\n"
+ "BOMCopierSourceEntryNewFromFTSAgent"
+ "BOM_CRC32_TYPE"
+ "CLEVER"
+ "Close cancelled"
+ "Could not F_NOCACHE: %s"
+ "Could not allocate FTS agent object: %s"
+ "Could not allocate FTS child"
+ "Could not allocate FTS child: %s"
+ "Could not allocate attribute buffer: %s\n"
+ "Could not allocate child list: %s"
+ "Could not allocate data stack object: %s"
+ "Could not allocate new FTS node: %s"
+ "Could not allocate stack node: %s"
+ "Could not close FTS agent"
+ "Could not close FTS agent: %s\n"
+ "Could not close node directory"
+ "Could not close nodes on the stack"
+ "Could not create FTS agent"
+ "Could not create FTS agent: %s\n"
+ "Could not create empty node"
+ "Could not create empty parent node"
+ "Could not create empty parent stack\n"
+ "Could not create empty root node"
+ "Could not create node stack"
+ "Could not create platform toolbox\n"
+ "Could not drain the FTS state\n"
+ "Could not drain the final FTS state: %s\n"
+ "Could not duplicate child name: %s"
+ "Could not duplicate file descriptor %s: %s"
+ "Could not duplicate node path"
+ "Could not finalize BOM CRC32 state"
+ "Could not finalize BOM CRC32 state\n"
+ "Could not free FTS agent"
+ "Could not fstat %s: %s"
+ "Could not fstatat %s: %s"
+ "Could not get bulk attributes for %s: %s\n"
+ "Could not get next FTS agent entry: %s"
+ "Could not get the next entry"
+ "Could not initialize BOM CRC32 state"
+ "Could not initialize BOM CRC32 state\n"
+ "Could not open FTS agent"
+ "Could not open FTS agent: %s\n"
+ "Could not open child %s: %s"
+ "Could not open directory %s: %s"
+ "Could not pop FTS node off the stack"
+ "Could not populate the children"
+ "Could not push current FTS node onto the stack"
+ "Could not push parent FTS node onto the stack"
+ "Could not read directory"
+ "Could not read from FTS agent: %s\n"
+ "Could not readlinkat %s: %s"
+ "Could not release node stack"
+ "Could not resolve %s: %s\n"
+ "Could not sort the children"
+ "Could not update BOM CRC32 state"
+ "Could not update BOM CRC32 state\n"
+ "Empty stack"
+ "Invalid FTS agent"
+ "Invalid FTS entry"
+ "Invalid data buffer"
+ "Invalid data buffer handle"
+ "Invalid data buffer size pointer"
+ "Invalid data stack"
+ "Invalid entry"
+ "Invalid flags"
+ "Jan 30 2026"
+ "LEGACY"
+ "NULL error"
+ "NULL error->error_message"
+ "NUMERICS"
+ "Open cancelled"
+ "Read cancelled"
+ "SIMPLE"
+ "Should not reach here"
+ "Should not reach here, either"
+ "The BOMCopierSource does not have an open FTS agent"
+ "The agent has already opened a path to traverse"
+ "The agent has not opened a path to traverse"
+ "The agent is exhausted"
+ "Unknown GP_CRC_TYPE: %s\n"
+ "Unsupported flag"
+ "child_allocate"
+ "close_stack"
+ "create_node"
+ "data_stack_count"
+ "data_stack_free"
+ "data_stack_new"
+ "data_stack_pop"
+ "data_stack_push"
+ "directory_get_next_child"
+ "fts_agent_close"
+ "fts_agent_free"
+ "fts_agent_new"
+ "fts_agent_open"
+ "fts_agent_read"
+ "get_next_entry"
+ "node_populate_children_bulk"
+ "node_populate_children_traditional"
+ "node_sort_children"
+ "path is not a UTF8 string"
+ "path is too long"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Bom/BOMBom.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Bom/BOMBomEnumerator.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Bom/BOMFSEnumerator.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMBufferManager.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMCRC32.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMFile.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMPatternList.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMSystemCmds.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopier2.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierDataAnalyzer.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierDestination.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierMatchRecord.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierSource.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierSourceEntry.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Copier/data_archive/data_archive.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Copier/data_archive/data_archive_decoder.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Copier/data_archive/data_archive_entry.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/FSObject/BOMFSOArchInfo.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/FSObject/BOMFSOTypeInfo.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Storage/BOMStorage.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Storage/BOMStream.c"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Storage/BOMTree.c"
- "Could not F_NOCACHE %s: %s"
- "Could not allocate entry node\n"
- "Could not create BOMCopierSource\n"
- "Could not get next entry: %s\n"
- "Could not make second attempt to create BOMFSObject for %s\n"
- "Could not open the FTS handle for %s: %s"
- "Jan 16 2026"
- "The BOMCopierSource does not have an open FTS handle"
- "entry_origin"
- "entry_origin: %d vs %d"

```
