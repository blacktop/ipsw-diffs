## libmalloc_exclaves_introspector

> `/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector`

```diff

-812.100.31.0.0
-  __TEXT.__text: 0x43cc sha256:a088c1f892f765a32d052dbb9ec390da335428293b84759172079abe8decb7b4
-  __TEXT.__auth_stubs: 0x200 sha256:1911514121a81d9aeca7534e6186917df8f3a4f7c93b152f36fae92107351438
+883.0.0.0.0
+  __TEXT.__text: 0x4520 sha256:54b1b46f65bf45e2f6820cf29e4da88c6e1ada83bff1735ab3dd1b2de470dda9
   __TEXT.__const: 0x7b sha256:e9066719d803de45974ac4f88ecf2085f2b9e389dad44e61557277f97b8f1a0e
-  __TEXT.__cstring: 0x20ff sha256:d0294064d9724b83ea1e1bafd867835b15cec23f4acae7f50c071a92c64245af
-  __TEXT.__unwind_info: 0xf8 sha256:8f9b06d6b9d5d48aa71808a128d6ac0651c4e82ddbcfc4f21f9d900fa720417a
-  __DATA_CONST.__got: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
-  __DATA_CONST.__const: 0x270 sha256:096a8ad19c0b922e1a4cda284cd945bdda56b52822609ae198cf118c5c33808c
-  __AUTH_CONST.__auth_got: 0x100 sha256:5341e6b2646979a70e57653007a1f310169421ec9bdd9f1a5648f75ade005af1
-  __AUTH_CONST.__const: 0x130 sha256:44ae3c3dd5b51c9d3a070a46512b2535a6d949c8101ef9f894eb5adc1d1e9ccf
+  __TEXT.__cstring: 0x2191 sha256:8e68966b6c19e91229a301f06c68efa74a1023ce550f08ced8ab8a074b59e05a
+  __TEXT.__unwind_info: 0xf0 sha256:8009572081c636ae66f7a6263469eefc5c3b25a61ba3efd713cc00d27115083d
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x2a0 sha256:1cac649c1442fb5fef4715049348285ede9f320a210d8d705de763874ba92bf2
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x130 sha256:72d301477866b73fa96c9a3efaf82bbc6d8447b1a108819ac54ca92ca97436a9
+  __AUTH_CONST.__auth_got: 0x108 sha256:44b8aa4d28701168922acf61435ea4bb442f97b0b14ad7a2510ed68874ee2a72
   __DATA.__crash_info: 0x148 sha256:6da6349e97370e8d430272961ce52dff296ff7c22208bd465045a16f557b12e4
   __DATA.__bss: 0x11 sha256:0a88111852095cae045340ea1f0b279944b2a756a213d9b50107d7489771e159
   __DATA.__common: 0x4 sha256:df3f619804a92fdb4057192dc43dd748ea778adc52bc498ce80524c014b81119
   - /usr/lib/libSystem.B.dylib
-  UUID: 0DAAB8E8-0093-3140-890F-CF3F4C3384A9
-  Functions: 48
-  Symbols:   162
-  CStrings:  268
+  UUID: 9CF7F864-F315-325E-BC62-2C41C799A435
+  Functions: 47
+  Symbols:   161
+  CStrings:  270
 
Symbols:
+ _memcpy
- _xzm_segment_table_foreach
Functions:
~ _mfm_unlock : sha256 e517ff719199dc516ee38ab08da968b53e289b8b9301e782663e973c1813c197 -> fbfe99f645a75da506918c10b18614d7a29ea9bbdb6c316470d7846fbbb12882
~ _mfm_reinit_lock : sha256 7ada4cdd3e254c6fe026e035838fcf84fe7834dd60b1db2c008f1ea510aacfe2 -> ad892cb2f731992c5de3321907463ef38d3e32329869c40bfe1d9f9b4a079bcc
~ _mfmi_enumerator : 576 -> 584
~ _mfmi_print_self : sha256 db8efffdcea329ecd2adc601d74cc791ef064da81d3c66011545b24288f978a2 -> 3c3e5372860e5abdd7c7b98bb6a68848851653e32ccd53465455a27beb822150
~ _mfmi_force_lock : sha256 371851211ebd5b5a11e68761ecf8188bdf24a2fa5ece28cd2701ba6317bf9c95 -> 18a044d61be8b2a0e05b118d98808916b054a884bc5f3c675564a594c4e7bc78
~ _mfmi_force_unlock : sha256 f185fe6cdcb962a568ab6025f62f2fc594fde6a89cac3b1bb3caa64acdbf864b -> 5b6067351a72b6fc70e057de1efa835c4aa6a9c9fbab5231d80922f94b27ef4e
~ _mfmi_statistics_self : sha256 ea215b5f497c1e1eeb7bbec720bfbb47737da0d83d57f17bf93245f15db9259b -> 685b35447c19e0562db2ac59caa1343692cb4eb1f479c5b55035883d4c7996db
~ _mfmi_locked : sha256 790fa8794176389ec831de96dfc765fe4f2a92e1896717d754733373c82b90df -> a4ae37c72ff1c923f14d7faf9891948c997559cc583bd8a19c5fa886a74fc68d
~ _mfmi_reinit_lock : sha256 7ada4cdd3e254c6fe026e035838fcf84fe7834dd60b1db2c008f1ea510aacfe2 -> ad892cb2f731992c5de3321907463ef38d3e32329869c40bfe1d9f9b4a079bcc
~ _mfmi_print_task : sha256 a7656c2844fe3c031590754f2b688ac63a8e3f928ba0cccfce4ef45ea3ef2ce3 -> 2f24db970dbdf0db2a5d1b44b6b2b6595171f6763b01d5f87d16e1332bf18d21
~ _mfmi_statistics_task : sha256 ed2c0ce65c3904bbfa4ec6570bcf282290e36ddb9926e746b40edf8d04fa15f5 -> b374d17bad3293416f07b23284fe4301b6c3a569bec8bf8a70758811cc603a50
~ _mfmi_read_zone : sha256 7d9a384bfad5b3a789889d67ab94c8c3b82e931c725b78dcd524e831a0162b6e -> b7ac11f50e1416db95114a233e7bae95530b6637f6d1730fdb9415d1da1d7924
~ __malloc_default_reader : sha256 631486142d44de20538a441269f5af9d039b1b475f8ef67b115c391cd4302db9 -> fd8d72beafd617cd457a80b70d5198e60a40782cbb96cc5abd36a736a8342b23
~ _print_mfm_arena : 992 -> 1008
~ _xzm_segment_group_segment_foreach_span : 356 -> 412
- _xzm_segment_table_foreach
~ _xzm_ptr_in_use_enumerator : sha256 93a5f02e456c72fbf06ac07c06841f7c07ea438e95c81128a2d9c2b445595136 -> 3287ee01eaf406d153fea7653669e66a4fecbbe685200463b8138fbe100915ab
~ _xzm_print_task : 5052 -> 5168
~ __xzm_introspect_map_zone_and_main : sha256 26d52fc028d44ea56d68eab4acf6b1e775aab29f1468337f78923ffdf3d15676 -> 93b470babe454658b418e9d09ffda6ff0abb7c798bfc6a809e4bbc8b1bba85ca
~ __xzm_introspect_enumerate : 816 -> 860
~ ___xzm_ptr_in_use_enumerator_block_invoke_4 : sha256 7dbdde6c6bdc74854176eaf70d343f32a9ebccb787caf36747ec62535366c1f9 -> a9ff13fa227b9a842e9a30075fff1dc2aa12b4120ace48850fc8292d7e5bc9b2
~ __malloc_default_reader : sha256 1bca26eed94301b8cac405ae8c285c6a5fccedc8aaf14216a7bd256608de780d -> b13df06b0a6e1d56a5619a3abf73894f7d704d7e152a104d02770b986b442d7b
~ ____xzm_introspect_enumerate_block_invoke : 332 -> 516
~ ____xzm_introspect_enumerate_block_invoke_2 : 1404 -> 1408
~ ___xzm_print_block_invoke : 632 -> 628
~ ___xzm_print_block_invoke_2 : 512 -> 480
~ ___xzm_print_block_invoke_3 : 284 -> 268
~ ___xzm_print_block_invoke_4 : 1356 -> 1464
~ ___xzm_print_block_invoke_5 : 552 -> 560
~ __malloc_default_debug_sleep_time : sha256 d8aba7240ebe4bae493722a02eaa6a7a2f8eeacab03d32bb58e06a27089ab4dd -> 800bd8806f6f193d2d19c26f0342b2b154046e92c8ac637bdff975936551fecb
~ _malloc_print_configure : sha256 c8e4f2a0057517332b30066337a0d361724cc387d56583dfb7a533fe0c62b86e -> 252f06a80c952310a5b0300483acc9e98e1aa5b85aa336a5365370aa4239390c
~ _malloc_vreport : sha256 bbb1e5e9b0e0f2fd5b05b4c382f9e745fe00cab1e97f8a03770367a6a443779a -> 94240401102aeb42693c0cfedde8c6ea942980e183c89df41b6ec81faa1fe197
~ __malloc_put : sha256 856cbd946e96d1f7c486db913052577585763d5f81aff363714d77ccf96d0966 -> d0183689d9c18f454e980a09a07fb9f947f2bb3880dffb2b78e894858d32abc9
~ _malloc_report : sha256 1d257e4a33f428b7078b9734fd982dc6f9671575222a14759acf82cae81cf119 -> 38705b79b2a6cd1a3cb2753c1d1894b473b4c36ad738327de50129104905cfa5
~ _malloc_report_simple : sha256 731189c6798fbc76d792bfdfaf22567406aeebc0b973b24fefbde11a7efaf7ed -> 4023b8683253ac0217b0e20ba140d586dd97be5af96c1b3ca338ca6fda19f61a
~ _malloc_zone_error : sha256 c4f4297f726fc621a2a5ff87abdb0a59915224a8633224102e4e6a0a18a7bce7 -> bc691de62623a37f7e0a4b0e711ec5730e06f05ade8f74eccb62c9bc3ba41f01
~ __xzm_introspect_map_zone_and_main.cold.1 : sha256 b097f934b82817c0d60e08a2c19047b5d2d1764527bb9fa617892b2419aba0f1 -> 4c924ffe80818f0b9e9ad7af6a9376139653f95a6efb6e075e663e72d0ec467e
~ __xzm_introspect_map_zone_and_main.cold.2 : sha256 b74e86cc6de06995d27e59578f88b9b99f443a673281c8ae37202e4c62ffa3cc -> df553a085ae9a5d001c7af70775b6e88f5c9d9a9870b811ee3702488b549e3fe
CStrings:
+ "\n}"
+ "            \"type\": \"%s\",\n"
+ "        \"huge_alloc_counter\": \"%u\", \n"
+ "        \"is_pristine\": %d,\n"
+ "        \"on_multi_segment\": %d\n"
+ "        \"on_partial_list\": %d,\n"
+ "        \"user_slices\": %u,\n"
+ "\"bin_step\": %d, \n"
+ "\"narrow_bucketing\": %d, \n"
+ "%s    \"segment_group\": %lu, \n"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/6409CED4-6942-4E87-A58C-A4235E3C0398/TemporaryDirectory.BWaVby/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:960)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/6409CED4-6942-4E87-A58C-A4235E3C0398/TemporaryDirectory.BWaVby/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:958)"
+ "guard_object"
+ "i20@?0^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}8I16"
+ "i24@?0Q8^v16"
+ "i32@?0Q8^{xzm_segment_s={?={?=[2Q]}{?=^{xzm_segment_s}^^{xzm_segment_s}}^{xzm_segment_group_s}IIICI^v^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}}16r*24"
+ "i44@?0Q8^{xzm_segment_s={?={?=[2Q]}{?=^{xzm_segment_s}^^{xzm_segment_s}}^{xzm_segment_group_s}IIICI^v^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}24I32Q36"
+ "i68@?0Q8^{xzm_segment_s={?={?=[2Q]}{?=^{xzm_segment_s}^^{xzm_segment_s}}^{xzm_segment_group_s}IIICI^v^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}24I32Q36(xzm_gxzone_u=^{xzm_gzone_s}^{xzm_xzone_s})44^{?=QQ}52Q60"
- "            \"type\": %u,\n"
- "        \"is_pristine\": %d\n"
- "        \"on_multi_segment\": %d,\n"
- "        \"slot_slices\": %u,\n"
- "    }\n"
- "\"%d\": {\n"
- "\"%p\": {\n"
- "%s    \"segment_group\": \"%s\", \n"
- ", "
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/FB491110-B229-4C38-BCD3-DF25C3C71EE8/TemporaryDirectory.J5DpC0/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:838)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/FB491110-B229-4C38-BCD3-DF25C3C71EE8/TemporaryDirectory.J5DpC0/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:836)"
- "i16@?0Q8"
- "i20@?0^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}8I16"
- "i32@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}16r*24"
- "i44@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}24I32Q36"
- "i68@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}24I32Q36(xzm_gxzone_u=^{xzm_gzone_s}^{xzm_xzone_s})44^{?=QQ}52Q60"

```
