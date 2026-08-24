## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

-750.0.0.0.0
+751.0.0.0.0
   __TEXT.__const: 0x1ab0
-  __TEXT.__cstring: 0xab88
-  __TEXT_EXEC.__text: 0x4e8c4
+  __TEXT.__cstring: 0xaba4
+  __TEXT_EXEC.__text: 0x4e94c
   __TEXT_EXEC.__auth_stubs: 0x1850
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 510
   Symbols:   1569
-  CStrings:  866
+  CStrings:  869
 
Symbols:
+ abort_transaction.kalloc_type_view_4627
+ abort_transaction.kalloc_type_view_4650
+ finish_end_transaction.kalloc_type_view_4207
+ finish_end_transaction.kalloc_type_view_4331
+ journal_allocate_transaction.kalloc_type_view_2600
+ journal_allocate_transaction.kalloc_type_view_2604
+ journal_close.kalloc_type_view_2417
+ journal_create.kalloc_type_view_1782
+ journal_create.kalloc_type_view_1896
+ journal_modify_block_end.kalloc_type_view_2955
+ journal_open.kalloc_type_view_1954
+ journal_open.kalloc_type_view_2196
+ replay_journal.kalloc_type_view_1550
+ replay_journal.kalloc_type_view_1561
- abort_transaction.kalloc_type_view_4619
- abort_transaction.kalloc_type_view_4642
- finish_end_transaction.kalloc_type_view_4199
- finish_end_transaction.kalloc_type_view_4323
- journal_allocate_transaction.kalloc_type_view_2592
- journal_allocate_transaction.kalloc_type_view_2596
- journal_close.kalloc_type_view_2409
- journal_create.kalloc_type_view_1774
- journal_create.kalloc_type_view_1888
- journal_modify_block_end.kalloc_type_view_2947
- journal_open.kalloc_type_view_1946
- journal_open.kalloc_type_view_2188
- replay_journal.kalloc_type_view_1542
- replay_journal.kalloc_type_view_1553
Functions:
~ _replay_journal : 5008 -> 5120
~ _hfs_vnop_getxattr : 920 -> 916
~ _HeadTruncateFile : 892 -> 920
CStrings:
+ "\n"
+ "0x%.8x"
+ "hfs: HeadTruncateFile: too many tail extents, marking volume inconsistent.\n"
+ "jnl: "
- "jnl: 0x%.8x 0x%.8x 0x%.8x 0x%.8x  0x%.8x 0x%.8x 0x%.8x 0x%.8x\n"
```
