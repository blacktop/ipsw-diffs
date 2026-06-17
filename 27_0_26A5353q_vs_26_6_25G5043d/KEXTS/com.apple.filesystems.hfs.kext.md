## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

-747.0.0.0.0
-  __TEXT.__const: 0x1ab0 sha256:4652793ff646a5edbd6b9f471ac186d6eb3c939e5d331af0af5dc029cc1de5c6
-  __TEXT.__cstring: 0xab31 sha256:22bd778a06a52cb6d94d0d44ab5d45f1ac5db8207c72939e8dccfbb0755001b0
-  __TEXT_EXEC.__text: 0x4e6fc sha256:e21e4cd78acaa6f305888635d8e5936a2ef83019f3030ad41ee92db7e34eca86
+715.160.7.0.0
+  __TEXT.__const: 0x1ab8 sha256:49921178fe6c172468afd40bcb57991b7b2c7702e5dc947a0f83e1d7d6bf7059
+  __TEXT.__cstring: 0xa8bd sha256:029d2f281127c98c19f25ac546a4fbf19f6435482c71f302c49f5e320a5b972d
+  __TEXT_EXEC.__text: 0x4e754 sha256:0824e599d33063894e3fb6bb46ee07552ea926e117e09a98148145bc01e1834c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x4d0 sha256:8536fe1606a764f60a8d1c0168cb3d17d4956c7259456f7b2871d041d0697671
+  __DATA.__data: 0x4d0 sha256:b1ece6d6463d2acd61ee97fc01564916bfee7f58771490de5ad8b4246754da45
   __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA.__bss: 0x1a4 sha256:de1da8f3791deb5ea5a11c9a67179b1e240aa14979524a3cc28add0e3612c0fe
-  __DATA_CONST.__mod_init_func: 0x8 sha256:43bafce95dca5a0050564367f6f4ec15451f2b82cb7e837d2fe45e03fc103aac
-  __DATA_CONST.__mod_term_func: 0x8 sha256:e52a43026b4b91b5b16482fd289ae78bb7d36f39ca33113109a350d044a521a4
-  __DATA_CONST.__const: 0x1340 sha256:ad1acc91ab2561dc3e14a4243ad4086228327724376171215c7cb7abf5307464
-  __DATA_CONST.__kalloc_type: 0x2cc0 sha256:19b0273cc50b1f408f1af4584ecffbc780e314c244123f1a809718d972f4ac93
-  __DATA_CONST.__kalloc_var: 0x5f0 sha256:ebd1fd2558508f962214d88f257e974469de7f50d2f8306d836a98e4dd5a4821
-  __DATA_CONST.__auth_got: 0xc20 sha256:79b37d284f2e5b72f5b945afd875c427353d0438c293f5838b0e95e7a8bcd46f
-  __DATA_CONST.__got: 0x68 sha256:0ac51ac3dfa0fef80a80f7258018057ccf47ec7f445d73c7a81b7980dddafb9a
-  __DATA_CONST.__auth_ptr: 0x8 sha256:2b0adcb32fe34114e602cac7b1308c50cfbe1661a6f1a22d89c87b614ed1527e
-  UUID: C828A752-750F-3B79-9728-A151E7D2E89A
-  Functions: 509
-  Symbols:   1567
-  CStrings:  865
+  __DATA_CONST.__auth_got: 0xc38 sha256:9a141d610ded23b2f0f5950516aa816b74863a73a0508ea3e1738ac9cb03f6b6
+  __DATA_CONST.__got: 0x68 sha256:9a99db0bc725d2dd74ab3b0a5b3e12aeb53fb23f8324ee67d385d1ae094199eb
+  __DATA_CONST.__auth_ptr: 0x8 sha256:7fbad2fc6e39c7a90813d620581409d1c584f92c20e9814e98cc764cefc4d76b
+  __DATA_CONST.__mod_init_func: 0x8 sha256:c62f59bc4b5a01de3462d06c5dc224694860aa5e57b2ca37e5302fc9fbc8d7e1
+  __DATA_CONST.__mod_term_func: 0x8 sha256:bf45becf68a82f1e0740237b3e4fa09fbfd5dc46582c90852d1e0a1e4360c9a3
+  __DATA_CONST.__const: 0x1340 sha256:7e02e758fef67a09f950e70c4c1370ff9f7ba06f58077d7c40e23c3cc5db06ee
+  __DATA_CONST.__kalloc_type: 0x2cc0 sha256:72dd8cc2d7e087099031f5af272d1010ffefad85787011538de22a904c5f4bd1
+  __DATA_CONST.__kalloc_var: 0x5f0 sha256:c4d4ff1f19ecd7c2039ec57e4f0c822127752101db9ff00dbcbfe3335e24b259
+  UUID: EC9A8DA8-7130-38D6-BF3C-BCC23B1C9766
+  Functions: 510
+  Symbols:   1571
+  CStrings:  856
 
Symbols:
+ _hfs_getencodingbias
+ _hfs_pickencoding
+ _hfs_setencodingbias
+ _hfs_setencodingbits
+ abort_transaction.kalloc_type_view_4591
+ abort_transaction.kalloc_type_view_4614
+ cat_acquire_cnid.kalloc_type_view_268
+ cat_acquire_cnid.kalloc_type_view_271
+ cat_acquire_cnid.kalloc_type_view_275
+ cat_acquire_cnid.kalloc_type_view_276
+ cat_check_link_ancestry.kalloc_type_view_1882
+ cat_check_link_ancestry.kalloc_type_view_1909
+ cat_create.kalloc_type_view_1042
+ cat_create.kalloc_type_view_1109
+ cat_createlink.kalloc_type_view_2214
+ cat_createlink.kalloc_type_view_2289
+ cat_findname.kalloc_type_view_587
+ cat_findname.kalloc_type_view_591
+ cat_findname.kalloc_type_view_615
+ cat_findname.kalloc_type_view_616
+ cat_getentriesattr.kalloc_type_view_2635
+ cat_getentriesattr.kalloc_type_view_2756
+ cat_idlookup.kalloc_type_view_638
+ cat_idlookup.kalloc_type_view_641
+ cat_idlookup.kalloc_type_view_688
+ cat_idlookup.kalloc_type_view_689
+ cat_insertfilethread.kalloc_type_view_527
+ cat_insertfilethread.kalloc_type_view_560
+ cat_lookup.kalloc_type_view_483
+ cat_lookup.kalloc_type_view_507
+ cat_lookup_dirlink.kalloc_type_view_4098
+ cat_lookup_dirlink.kalloc_type_view_4101
+ cat_lookup_dirlink.kalloc_type_view_4139
+ cat_lookup_dirlink.kalloc_type_view_4141
+ cat_lookup_lastlink.kalloc_type_view_2093
+ cat_lookup_lastlink.kalloc_type_view_2172
+ cat_lookup_siblinglinks.kalloc_type_view_2038
+ cat_lookup_siblinglinks.kalloc_type_view_2069
+ cat_lookupbykey.kalloc_type_view_1005
+ cat_lookupbykey.kalloc_type_view_1006
+ cat_lookupbykey.kalloc_type_view_778
+ cat_lookupbykey.kalloc_type_view_780
+ cat_lookuplink.kalloc_type_view_1994
+ cat_rename.kalloc_type_view_1159
+ cat_rename.kalloc_type_view_1163
+ cat_rename.kalloc_type_view_1168
+ cat_rename.kalloc_type_view_1188
+ cat_rename.kalloc_type_view_1199
+ cat_rename.kalloc_type_view_1205
+ cat_rename.kalloc_type_view_1209
+ cat_rename.kalloc_type_view_1406
+ cat_rename.kalloc_type_view_1408
+ cat_rename.kalloc_type_view_1410
+ cat_resolvelink.kalloc_type_view_3573
+ cat_resolvelink.kalloc_type_view_3595
+ cat_update_siblinglinks.kalloc_type_view_1965
+ cat_update_siblinglinks.kalloc_type_view_1975
+ finish_end_transaction.kalloc_type_view_4171
+ finish_end_transaction.kalloc_type_view_4295
+ getkey.kalloc_type_view_3638
+ getkey.kalloc_type_view_3641
+ getkey.kalloc_type_view_3675
+ getkey.kalloc_type_view_3676
+ hfs_remove_orphans.kalloc_type_view_1731
+ hfs_remove_orphans.kalloc_type_view_1952
+ journal_allocate_transaction.kalloc_type_view_2564
+ journal_allocate_transaction.kalloc_type_view_2568
+ journal_close.kalloc_type_view_2381
+ journal_create.kalloc_type_view_1769
+ journal_create.kalloc_type_view_1884
+ journal_modify_block_end.kalloc_type_view_2919
+ journal_open.kalloc_type_view_1942
+ journal_open.kalloc_type_view_2160
+ replay_journal.kalloc_type_view_1537
+ replay_journal.kalloc_type_view_1548
- abort_transaction.kalloc_type_view_4586
- abort_transaction.kalloc_type_view_4609
- cat_acquire_cnid.kalloc_type_view_291
- cat_acquire_cnid.kalloc_type_view_294
- cat_acquire_cnid.kalloc_type_view_298
- cat_acquire_cnid.kalloc_type_view_299
- cat_check_link_ancestry.kalloc_type_view_1906
- cat_check_link_ancestry.kalloc_type_view_1933
- cat_create.kalloc_type_view_1065
- cat_create.kalloc_type_view_1132
- cat_createlink.kalloc_type_view_2238
- cat_createlink.kalloc_type_view_2313
- cat_findname.kalloc_type_view_610
- cat_findname.kalloc_type_view_614
- cat_findname.kalloc_type_view_638
- cat_findname.kalloc_type_view_639
- cat_getentriesattr.kalloc_type_view_2659
- cat_getentriesattr.kalloc_type_view_2780
- cat_idlookup.kalloc_type_view_661
- cat_idlookup.kalloc_type_view_664
- cat_idlookup.kalloc_type_view_711
- cat_idlookup.kalloc_type_view_712
- cat_insertfilethread.kalloc_type_view_550
- cat_insertfilethread.kalloc_type_view_583
- cat_lookup.kalloc_type_view_506
- cat_lookup.kalloc_type_view_530
- cat_lookup_dirlink.kalloc_type_view_4122
- cat_lookup_dirlink.kalloc_type_view_4125
- cat_lookup_dirlink.kalloc_type_view_4163
- cat_lookup_dirlink.kalloc_type_view_4165
- cat_lookup_lastlink.kalloc_type_view_2117
- cat_lookup_lastlink.kalloc_type_view_2196
- cat_lookup_siblinglinks.kalloc_type_view_2062
- cat_lookup_siblinglinks.kalloc_type_view_2093
- cat_lookupbykey.kalloc_type_view_1028
- cat_lookupbykey.kalloc_type_view_1029
- cat_lookupbykey.kalloc_type_view_801
- cat_lookupbykey.kalloc_type_view_803
- cat_lookuplink.kalloc_type_view_2042
- cat_rename.kalloc_type_view_1182
- cat_rename.kalloc_type_view_1186
- cat_rename.kalloc_type_view_1191
- cat_rename.kalloc_type_view_1211
- cat_rename.kalloc_type_view_1222
- cat_rename.kalloc_type_view_1228
- cat_rename.kalloc_type_view_1232
- cat_rename.kalloc_type_view_1430
- cat_rename.kalloc_type_view_1432
- cat_rename.kalloc_type_view_1434
- cat_resolvelink.kalloc_type_view_3597
- cat_resolvelink.kalloc_type_view_3619
- cat_update_siblinglinks.kalloc_type_view_1989
- cat_update_siblinglinks.kalloc_type_view_1999
- finish_end_transaction.kalloc_type_view_4166
- finish_end_transaction.kalloc_type_view_4290
- getkey.kalloc_type_view_3662
- getkey.kalloc_type_view_3665
- getkey.kalloc_type_view_3699
- getkey.kalloc_type_view_3700
- hfs_remove_orphans.kalloc_type_view_1744
- hfs_remove_orphans.kalloc_type_view_1965
- journal_allocate_transaction.kalloc_type_view_2559
- journal_allocate_transaction.kalloc_type_view_2563
- journal_close.kalloc_type_view_2376
- journal_create.kalloc_type_view_1764
- journal_create.kalloc_type_view_1871
- journal_modify_block_end.kalloc_type_view_2914
- journal_open.kalloc_type_view_1929
- journal_open.kalloc_type_view_2155
- replay_journal.kalloc_type_view_1532
- replay_journal.kalloc_type_view_1543
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRehugBydM89hn0whEOuUXLM1aciUeolHu9lCSc/Library/Caches/com.apple.xbs/TemporaryDirectory.EG2uBh/Sources/hfs/core/VolumeAllocation.c"
+ "/AppleInternal/Library/BuildRoots/4~CRehugBydM89hn0whEOuUXLM1aciUeolHu9lCSc/Library/Caches/com.apple.xbs/TemporaryDirectory.EG2uBh/Sources/hfs/core/hfs_attrlist.c"
+ "/AppleInternal/Library/BuildRoots/4~CRehugBydM89hn0whEOuUXLM1aciUeolHu9lCSc/Library/Caches/com.apple.xbs/TemporaryDirectory.EG2uBh/Sources/hfs/core/hfs_btreeio.c"
+ "/AppleInternal/Library/BuildRoots/4~CRehugBydM89hn0whEOuUXLM1aciUeolHu9lCSc/Library/Caches/com.apple.xbs/TemporaryDirectory.EG2uBh/Sources/hfs/core/hfs_cnode.c"
+ "/AppleInternal/Library/BuildRoots/4~CRehugBydM89hn0whEOuUXLM1aciUeolHu9lCSc/Library/Caches/com.apple.xbs/TemporaryDirectory.EG2uBh/Sources/hfs/core/hfs_hotfiles.c"
+ "/AppleInternal/Library/BuildRoots/4~CRehugBydM89hn0whEOuUXLM1aciUeolHu9lCSc/Library/Caches/com.apple.xbs/TemporaryDirectory.EG2uBh/Sources/hfs/core/hfs_journal.c"
+ "/AppleInternal/Library/BuildRoots/4~CRehugBydM89hn0whEOuUXLM1aciUeolHu9lCSc/Library/Caches/com.apple.xbs/TemporaryDirectory.EG2uBh/Sources/hfs/core/hfs_readwrite.c"
+ "/AppleInternal/Library/BuildRoots/4~CRehugBydM89hn0whEOuUXLM1aciUeolHu9lCSc/Library/Caches/com.apple.xbs/TemporaryDirectory.EG2uBh/Sources/hfs/core/hfs_vfsops.c"
+ "/AppleInternal/Library/BuildRoots/4~CRehugBydM89hn0whEOuUXLM1aciUeolHu9lCSc/Library/Caches/com.apple.xbs/TemporaryDirectory.EG2uBh/Sources/hfs/core/hfs_vfsutils.c"
+ "22222212111112222111121222111211222222222222222222222"
+ "jnl: %s: replay_journal: block number 0x%llx out of range (device has 0x%llx blocks)\n"
- "\"hfs_swap_HFSPlusBTInternalNode: invalid free space offset (%X)\\n\" @%s:%d"
- "\"hfs_swap_HFSPlusBTInternalNode: invalid record count (0x%04X)\\n\" @%s:%d"
- "\"hfs_swap_HFSPlusBTInternalNode: invalid record offset (record #%d)\\n\" @%s:%d"
- "/AppleInternal/Library/BuildRoots/4~CQdcugDlkmcnoZa48KyfebJ7rrYrBggVrB2aAH8/Library/Caches/com.apple.xbs/TemporaryDirectory.RD3dPv/Sources/hfs/core/VolumeAllocation.c"
- "/AppleInternal/Library/BuildRoots/4~CQdcugDlkmcnoZa48KyfebJ7rrYrBggVrB2aAH8/Library/Caches/com.apple.xbs/TemporaryDirectory.RD3dPv/Sources/hfs/core/hfs_attrlist.c"
- "/AppleInternal/Library/BuildRoots/4~CQdcugDlkmcnoZa48KyfebJ7rrYrBggVrB2aAH8/Library/Caches/com.apple.xbs/TemporaryDirectory.RD3dPv/Sources/hfs/core/hfs_btreeio.c"
- "/AppleInternal/Library/BuildRoots/4~CQdcugDlkmcnoZa48KyfebJ7rrYrBggVrB2aAH8/Library/Caches/com.apple.xbs/TemporaryDirectory.RD3dPv/Sources/hfs/core/hfs_cnode.c"
- "/AppleInternal/Library/BuildRoots/4~CQdcugDlkmcnoZa48KyfebJ7rrYrBggVrB2aAH8/Library/Caches/com.apple.xbs/TemporaryDirectory.RD3dPv/Sources/hfs/core/hfs_hotfiles.c"
- "/AppleInternal/Library/BuildRoots/4~CQdcugDlkmcnoZa48KyfebJ7rrYrBggVrB2aAH8/Library/Caches/com.apple.xbs/TemporaryDirectory.RD3dPv/Sources/hfs/core/hfs_journal.c"
- "/AppleInternal/Library/BuildRoots/4~CQdcugDlkmcnoZa48KyfebJ7rrYrBggVrB2aAH8/Library/Caches/com.apple.xbs/TemporaryDirectory.RD3dPv/Sources/hfs/core/hfs_readwrite.c"
- "/AppleInternal/Library/BuildRoots/4~CQdcugDlkmcnoZa48KyfebJ7rrYrBggVrB2aAH8/Library/Caches/com.apple.xbs/TemporaryDirectory.RD3dPv/Sources/hfs/core/hfs_vfsops.c"
- "/AppleInternal/Library/BuildRoots/4~CQdcugDlkmcnoZa48KyfebJ7rrYrBggVrB2aAH8/Library/Caches/com.apple.xbs/TemporaryDirectory.RD3dPv/Sources/hfs/core/hfs_vfsutils.c"
- "2222221211111222211112122211121122222222222222222222"
- "hfs_ValidateHFSPlusVolumeHeader: invalid free block count (0x%X), greater than total block count (0x%X) \n"
- "hfs_swap_HFSPlusBTInternalNode: invalid free space offset (%X)\n"
- "hfs_swap_HFSPlusBTInternalNode: invalid record count (0x%04X)\n"
- "hfs_swap_HFSPlusBTInternalNode: invalid record offset (record #%d)\n"
- "jnl %s: open: blhdr_size (%d) >= journal size (%lld)\n"
- "jnl %s: open: blhdr_size (%d) not a multiple of block_info size (%zu)\n"
- "jnl: %s: replay_journal: unable to allocate %d bytes for blhdr\n"

```
