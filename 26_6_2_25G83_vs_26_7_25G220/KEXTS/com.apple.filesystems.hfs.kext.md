## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

-715.160.9.0.0
-  __TEXT.__const: 0x1ab8
-  __TEXT.__cstring: 0xa909
-  __TEXT_EXEC.__text: 0x4e778
+715.160.9.700.5
+  __TEXT.__const: 0x1ac0
+  __TEXT.__cstring: 0xab6a
+  __TEXT_EXEC.__text: 0x4e874
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10
   __DATA.__bss: 0x1a4
-  __DATA_CONST.__auth_got: 0xc38
+  __DATA_CONST.__auth_got: 0xc40
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x8

   __DATA_CONST.__kalloc_type: 0x2cc0
   __DATA_CONST.__kalloc_var: 0x5f0
   Functions: 511
-  Symbols:   1572
-  CStrings:  857
+  Symbols:   1573
+  CStrings:  866
 
Symbols:
+ _IOMallocZeroDataShareable
+ abort_transaction.kalloc_type_view_4619
+ abort_transaction.kalloc_type_view_4642
+ finish_end_transaction.kalloc_type_view_4199
+ finish_end_transaction.kalloc_type_view_4323
+ journal_allocate_transaction.kalloc_type_view_2592
+ journal_allocate_transaction.kalloc_type_view_2596
+ journal_close.kalloc_type_view_2409
+ journal_create.kalloc_type_view_1774
+ journal_create.kalloc_type_view_1888
+ journal_modify_block_end.kalloc_type_view_2947
+ journal_open.kalloc_type_view_1946
+ journal_open.kalloc_type_view_2188
+ replay_journal.kalloc_type_view_1542
+ replay_journal.kalloc_type_view_1553
- abort_transaction.kalloc_type_view_4591
- abort_transaction.kalloc_type_view_4614
- finish_end_transaction.kalloc_type_view_4171
- finish_end_transaction.kalloc_type_view_4295
- journal_allocate_transaction.kalloc_type_view_2564
- journal_allocate_transaction.kalloc_type_view_2568
- journal_close.kalloc_type_view_2381
- journal_create.kalloc_type_view_1769
- journal_create.kalloc_type_view_1884
- journal_modify_block_end.kalloc_type_view_2919
- journal_open.kalloc_type_view_1942
- journal_open.kalloc_type_view_2160
- replay_journal.kalloc_type_view_1537
- replay_journal.kalloc_type_view_1548
Functions:
~ _journal_create : 948 -> 924
~ _journal_open : 1764 -> 1932
~ _replay_journal : 4692 -> 4716
~ _journal_modify_block_start : 1628 -> 1616
~ _hfs_swap_BTNode : 5220 -> 5316
CStrings:
+ "\"hfs_swap_HFSPlusBTInternalNode: invalid free space offset (%X)\\n\" @%s:%d"
+ "\"hfs_swap_HFSPlusBTInternalNode: invalid record count (0x%04X)\\n\" @%s:%d"
+ "\"hfs_swap_HFSPlusBTInternalNode: invalid record offset (record #%d)\\n\" @%s:%d"
+ "hfs_swap_HFSPlusBTInternalNode: invalid free space offset (%X)\n"
+ "hfs_swap_HFSPlusBTInternalNode: invalid record count (0x%04X)\n"
+ "hfs_swap_HFSPlusBTInternalNode: invalid record offset (record #%d)\n"
+ "jnl %s: open: blhdr_size (%d) >= journal size (%lld)\n"
+ "jnl %s: open: blhdr_size (%d) not a multiple of block_info size (%zu)\n"
+ "jnl: %s: replay_journal: unable to allocate %d bytes for blhdr\n"
```
