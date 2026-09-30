## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

-715.160.6.0.0
-  __TEXT.__const: 0x1ab8 sha256:5259b009e0f129ea86ffeaf603751476f72ca03c6c1155055527a1976b89d4be
-  __TEXT.__cstring: 0xa866 sha256:8800455fb4aea6f5c33568e19ffe327b9098b94477a9a2ee6e099ef7374bbd3c
-  __TEXT_EXEC.__text: 0x4e6b8 sha256:e910b2b96cb8ee8c94cec01eec0fc6a891ff49d557651176f173e3a663fe8e7f
+715.160.7.0.0
+  __TEXT.__const: 0x1ab8 sha256:49921178fe6c172468afd40bcb57991b7b2c7702e5dc947a0f83e1d7d6bf7059
+  __TEXT.__cstring: 0xa8bd sha256:029d2f281127c98c19f25ac546a4fbf19f6435482c71f302c49f5e320a5b972d
+  __TEXT_EXEC.__text: 0x4e754 sha256:0824e599d33063894e3fb6bb46ee07552ea926e117e09a98148145bc01e1834c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x4d0 sha256:7cef76df7ceec411e100958b0a8d41825bdaf9e9074d33ff17214141c0e22ead
+  __DATA.__data: 0x4d0 sha256:b1ece6d6463d2acd61ee97fc01564916bfee7f58771490de5ad8b4246754da45
   __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA.__bss: 0x1a4 sha256:de1da8f3791deb5ea5a11c9a67179b1e240aa14979524a3cc28add0e3612c0fe
-  __DATA_CONST.__auth_got: 0xc38 sha256:4f8ba865594a55120bb67fb46c9226443d5a217a4ffc6e2598e40f13f7bc46b5
-  __DATA_CONST.__got: 0x68 sha256:083f0a2e9bb77bfbe45564e2ae73f84a5808c5fe2b3caa89e0da8c82453b1dfb
-  __DATA_CONST.__auth_ptr: 0x8 sha256:11200999171119566a197e8f4155402843af1821284f622acc39091925f16c61
-  __DATA_CONST.__mod_init_func: 0x8 sha256:41365fb0d7c5f474e1744b11c3a9e948838f9954b004541d1730c882783b6fe1
-  __DATA_CONST.__mod_term_func: 0x8 sha256:dad352e12caa1e1885b51cc89a4c0a1c57837b6a5ba9bd4333762d728b5935ee
-  __DATA_CONST.__const: 0x1340 sha256:843fbb836e78e9293d426eff12c2de8becebd1bcff41240e8d7ecc973faba857
-  __DATA_CONST.__kalloc_type: 0x2cc0 sha256:c996c994804597cb6fc4a4ffbbc65e33025e87ad9937323aba96cbb84160494b
-  __DATA_CONST.__kalloc_var: 0x5f0 sha256:be31bb12fbdf067e12bc37a14992b55c967ea3e3e2e55e983c6e2a0f8cf22d00
-  UUID: 3F8B6CAD-4D96-3102-9D8D-0068A7EFD440
+  __DATA_CONST.__auth_got: 0xc38 sha256:9a141d610ded23b2f0f5950516aa816b74863a73a0508ea3e1738ac9cb03f6b6
+  __DATA_CONST.__got: 0x68 sha256:9a99db0bc725d2dd74ab3b0a5b3e12aeb53fb23f8324ee67d385d1ae094199eb
+  __DATA_CONST.__auth_ptr: 0x8 sha256:7fbad2fc6e39c7a90813d620581409d1c584f92c20e9814e98cc764cefc4d76b
+  __DATA_CONST.__mod_init_func: 0x8 sha256:c62f59bc4b5a01de3462d06c5dc224694860aa5e57b2ca37e5302fc9fbc8d7e1
+  __DATA_CONST.__mod_term_func: 0x8 sha256:bf45becf68a82f1e0740237b3e4fa09fbfd5dc46582c90852d1e0a1e4360c9a3
+  __DATA_CONST.__const: 0x1340 sha256:7e02e758fef67a09f950e70c4c1370ff9f7ba06f58077d7c40e23c3cc5db06ee
+  __DATA_CONST.__kalloc_type: 0x2cc0 sha256:72dd8cc2d7e087099031f5af272d1010ffefad85787011538de22a904c5f4bd1
+  __DATA_CONST.__kalloc_var: 0x5f0 sha256:c4d4ff1f19ecd7c2039ec57e4f0c822127752101db9ff00dbcbfe3335e24b259
+  UUID: EC9A8DA8-7130-38D6-BF3C-BCC23B1C9766
   Functions: 510
   Symbols:   1571
-  CStrings:  855
+  CStrings:  856
 
Symbols:
+ abort_transaction.kalloc_type_view_4591
+ abort_transaction.kalloc_type_view_4614
+ finish_end_transaction.kalloc_type_view_4171
+ finish_end_transaction.kalloc_type_view_4295
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
- abort_transaction.kalloc_type_view_4565
- abort_transaction.kalloc_type_view_4588
- finish_end_transaction.kalloc_type_view_4145
- finish_end_transaction.kalloc_type_view_4269
- journal_allocate_transaction.kalloc_type_view_2538
- journal_allocate_transaction.kalloc_type_view_2542
- journal_close.kalloc_type_view_2355
- journal_create.kalloc_type_view_1759
- journal_create.kalloc_type_view_1866
- journal_modify_block_end.kalloc_type_view_2893
- journal_open.kalloc_type_view_1924
- journal_open.kalloc_type_view_2134
- replay_journal.kalloc_type_view_1527
- replay_journal.kalloc_type_view_1538
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
- "/AppleInternal/Library/BuildRoots/4~CPlcugC4SRNFIRT5_0b4VcfsPxXIdsjjkZX1SNc/Library/Caches/com.apple.xbs/TemporaryDirectory.L5Fjva/Sources/hfs/core/VolumeAllocation.c"
- "/AppleInternal/Library/BuildRoots/4~CPlcugC4SRNFIRT5_0b4VcfsPxXIdsjjkZX1SNc/Library/Caches/com.apple.xbs/TemporaryDirectory.L5Fjva/Sources/hfs/core/hfs_attrlist.c"
- "/AppleInternal/Library/BuildRoots/4~CPlcugC4SRNFIRT5_0b4VcfsPxXIdsjjkZX1SNc/Library/Caches/com.apple.xbs/TemporaryDirectory.L5Fjva/Sources/hfs/core/hfs_btreeio.c"
- "/AppleInternal/Library/BuildRoots/4~CPlcugC4SRNFIRT5_0b4VcfsPxXIdsjjkZX1SNc/Library/Caches/com.apple.xbs/TemporaryDirectory.L5Fjva/Sources/hfs/core/hfs_cnode.c"
- "/AppleInternal/Library/BuildRoots/4~CPlcugC4SRNFIRT5_0b4VcfsPxXIdsjjkZX1SNc/Library/Caches/com.apple.xbs/TemporaryDirectory.L5Fjva/Sources/hfs/core/hfs_hotfiles.c"
- "/AppleInternal/Library/BuildRoots/4~CPlcugC4SRNFIRT5_0b4VcfsPxXIdsjjkZX1SNc/Library/Caches/com.apple.xbs/TemporaryDirectory.L5Fjva/Sources/hfs/core/hfs_journal.c"
- "/AppleInternal/Library/BuildRoots/4~CPlcugC4SRNFIRT5_0b4VcfsPxXIdsjjkZX1SNc/Library/Caches/com.apple.xbs/TemporaryDirectory.L5Fjva/Sources/hfs/core/hfs_readwrite.c"
- "/AppleInternal/Library/BuildRoots/4~CPlcugC4SRNFIRT5_0b4VcfsPxXIdsjjkZX1SNc/Library/Caches/com.apple.xbs/TemporaryDirectory.L5Fjva/Sources/hfs/core/hfs_vfsops.c"
- "/AppleInternal/Library/BuildRoots/4~CPlcugC4SRNFIRT5_0b4VcfsPxXIdsjjkZX1SNc/Library/Caches/com.apple.xbs/TemporaryDirectory.L5Fjva/Sources/hfs/core/hfs_vfsutils.c"
- "2222221211111222211112122211121122222222222222222222"

```
