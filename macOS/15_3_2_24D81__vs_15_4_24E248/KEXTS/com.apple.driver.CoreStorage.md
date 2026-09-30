## com.apple.driver.CoreStorage

> `com.apple.driver.CoreStorage`

```diff

 566.0.0.0.0
-  __TEXT.__const: 0x6f8
+  __TEXT.__const: 0x708
   __TEXT.__cstring: 0x8a21
-  __TEXT_EXEC.__text: 0xaaf7c
+  __TEXT_EXEC.__text: 0x95a64
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x870
   __DATA.__common: 0x3e0

   __DATA_CONST.__const: 0x6880
   __DATA_CONST.__kalloc_type: 0x340
   __DATA_CONST.__kalloc_var: 0xa50
-  UUID: 1F9F66F6-9F35-3502-AD31-F5201DEFEAFB
-  Functions: 2117
-  Symbols:   3033
+  UUID: 52A8207E-8550-32A4-B871-0405F079B081
+  Functions: 1725
+  Symbols:   3030
   CStrings:  983
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _ZN15move_work_queue5enqueEP9ioreq_entb.cold.1
+ __Z18bt_retain_childrenI12lvf_refc_keyEiP5btreeIT_EP7bt_nodePciP2tx
+ __Z18bt_retain_childrenI12phy_ext_addrEiP5btreeIT_EP7bt_nodePciP2tx
+ __Z18bt_retain_childrenI6lv_keyEiP5btreeIT_EP7bt_nodePciP2tx
+ __Z18bt_retain_childrenIyEiP5btreeIT_EP7bt_nodePciP2tx
+ __ZL18pv_leaks_plaintextP3lvgP10lvg_resize
- _Z13bootstrap_mlvP3lvgP16CoreStorageGroup.cold.2
- _Z17load_lfs_from_segP3lvgRK13recovery_info.cold.2
- _Z21serialize_label_attrsP3lvgP12OSDictionary.cold.1
- _ZL13dict_from_xmlP9attr_infoP3lvgPP12OSDictionary.cold.1
- _ZL13dict_from_xmlP9attr_infoP3lvgPP12OSDictionary.cold.2
- _ZL22bgt_restore_error_dataP9lv_handlePP18dk_bad_sector_info.cold.1
- _ZL26revertRequirementsCallback12phy_ext_addrPvmS0_.cold.2
- _ZN19CoreStoragePhysical10issueUnmapEjP18CoreStorageLogicalP3lvg.cold.2
- _ZN20resident_list_gclockC1EP21compositedisk_managertm.cold.2
- _ZN3lvg14lvg_grow_labelEm.cold.1
- _ZN9hashtableI13dsd_blk_chainS0_XadL_Z18hash_dsd_blk_chainRKS0_EE8equal_toIS0_E9_identityIS0_EE4growEm.cold.1
- _ZN9hashtableI15in_mem_dsd_infoS0_XadL_Z20hash_in_mem_dsd_infoRKS0_EE8equal_toIS0_E9_identityIS0_EE4growEm.cold.1
- _ZN9hashtableI27CoreStorageLogicalHashEntryS0_XadL_Z31hashCoreStorageLogicalHashEntryRKS0_EE8equal_toIS0_E9_identityIS0_EE4growEm.cold.1
- _ZN9hashtableI8dsd_infoS0_XadL_Z13hash_dsd_infoRKS0_EE8equal_toIS0_E9_identityIS0_EE4growEm.cold.1
- _ZN9hashtableIP11cache_extraS1_XadL_Z16hash_cache_extraRKS1_EE20cache_extra_equal_to9_identityIS1_EE4growEm.cold.1
- _ZN9hashtableIPKc4pairIS1_S1_EXadL_Z8hash_strRKS1_EE12str_equal_to14_extract_firstIS3_S1_EE4growEm.cold.1
- _ZN9hashtableIyyXadL_Z11hash_uint64RKyEE8equal_toIyE9_identityIyEE4growEm.cold.1
- __ZN6vectorI12pv_full_infoE15construct_itemsEmmS0_
- __ZN6vectorI13part_seg_infoE15construct_itemsEmmS0_
- __ZN9hashtableIyyXadL_Z11hash_uint64RKyEE8equal_toIyE9_identityIyEE6resizeEm
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/background.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/btree/btree_impl.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/compositedisk.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/lfs.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/lv.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/lv_readwrite.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/lvg.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/txn.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreStorage/cs_context/kernel/devio_kernel_context.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreStorage/iokit/CoreStorageGroup.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreStorage/iokit/CoreStorageLogical.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreStorage/iokit/CoreStorageReadModifyWrite.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/background.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/btree/btree_impl.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/compositedisk.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/lfs.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/lv.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/lv_readwrite.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/lvg.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreStorage/core/txn.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreStorage/cs_context/kernel/devio_kernel_context.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreStorage/iokit/CoreStorageGroup.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreStorage/iokit/CoreStorageLogical.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreStorage/iokit/CoreStorageReadModifyWrite.cpp"

```
