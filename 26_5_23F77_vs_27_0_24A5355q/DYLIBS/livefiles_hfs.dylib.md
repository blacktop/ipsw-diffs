## livefiles_hfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib`

```diff

-715.120.4.0.0
-  __TEXT.__text: 0x3db14
-  __TEXT.__auth_stubs: 0x470
+747.0.0.0.0
+  __TEXT.__text: 0x3d2a4
   __TEXT.__const: 0x4e60
-  __TEXT.__oslogstring: 0x5c74
+  __TEXT.__oslogstring: 0x5e7a
   __TEXT.__cstring: 0x26fb
-  __TEXT.__unwind_info: 0x6d8
-  __DATA_CONST.__got: 0x30
-  __AUTH_CONST.__auth_got: 0x238
-  __AUTH.__data: 0x140
+  __TEXT.__unwind_info: 0x6e0
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__data: 0x148
   __DATA.__data: 0x1948
   __DATA.__bss: 0x34
   __DATA.__common: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 20780CCF-13C3-34DB-8A7E-241DD4632C3F
-  Functions: 677
-  Symbols:   1163
-  CStrings:  738
+  UUID: BEBAE024-98CD-3998-A07F-CF9A0B4DC854
+  Functions: 676
+  Symbols:   1141
+  CStrings:  746
 
Symbols:
+ _hfs_swap_HFSPlusBTInternalNode.cold.20
+ _hfs_swap_HFSPlusBTInternalNode.cold.21
+ _hfs_swap_HFSPlusBTInternalNode.cold.22
- _OUTLINED_FUNCTION_11
CStrings:
+ "hfs_ValidateHFSPlusVolumeHeader: invalid free block count (0x%X), greater than total block count (0x%X) \n"
+ "hfs_swap_HFSPlusBTInternalNode: invalid free space offset (%X)\n"
+ "hfs_swap_HFSPlusBTInternalNode: invalid record count (0x%04X)\n"
+ "hfs_swap_HFSPlusBTInternalNode: invalid record offset (record #%d)\n"
+ "jnl: open: blhdr size looks bogus! (%d) \n"
+ "jnl: open: blhdr_size (%d) >= journal size (%lld)\n"
+ "jnl: open: blhdr_size (%d) not a multiple of block_info size (%zu)\n"
+ "replay_journal: unable to allocate %d bytes for blhdr.\n"

```
