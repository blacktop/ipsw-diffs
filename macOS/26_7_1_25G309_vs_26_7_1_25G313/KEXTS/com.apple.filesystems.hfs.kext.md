## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

-715.160.9.700.5
+715.160.9.702.4
   __TEXT.__const: 0x1ac0
-  __TEXT.__cstring: 0xab6a
-  __TEXT_EXEC.__text: 0x4e874
+  __TEXT.__cstring: 0xab3a
+  __TEXT_EXEC.__text: 0x4e8ec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

   __DATA_CONST.__kalloc_var: 0x5f0
   Functions: 511
   Symbols:   1573
-  CStrings:  866
+  CStrings:  868
 
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
~ _replay_journal : 4716 -> 4824
~ _hfs_swap_BTNode : 5316 -> 5328
CStrings:
+ "\n"
+ "0x%.8x"
+ "jnl: "
- "jnl: 0x%.8x 0x%.8x 0x%.8x 0x%.8x  0x%.8x 0x%.8x 0x%.8x 0x%.8x\n"
```
