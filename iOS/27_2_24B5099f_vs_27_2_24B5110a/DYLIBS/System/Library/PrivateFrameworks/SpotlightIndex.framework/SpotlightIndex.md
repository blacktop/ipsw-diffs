## SpotlightIndex

> `/System/Library/PrivateFrameworks/SpotlightIndex.framework/SpotlightIndex`

```diff

-2465.1.7.0.0
-  __TEXT.__text: 0x47c0a8
+2465.1.9.0.0
+  __TEXT.__text: 0x47c370
   __TEXT.__objc_methlist: 0x404
   __TEXT.__const: 0xa56a
-  __TEXT.__cstring: 0x2f4a4
+  __TEXT.__cstring: 0x2f524
   __TEXT.__gcc_except_tab: 0x29c
-  __TEXT.__oslogstring: 0x1e105
+  __TEXT.__oslogstring: 0x1e202
   __TEXT.__ustring: 0x2aa
   __TEXT.__dof_mds: 0x29b
   __TEXT.__unwind_info: 0x71b8

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8a58
+  __DATA_CONST.__const: 0x8a70
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x670

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 7757
-  Symbols:   10270
-  CStrings:  8085
+  Functions: 7758
+  Symbols:   10271
+  CStrings:  8090
 
Symbols:
+ GCC_except_table6758
+ _lazySetupMissingOids
- GCC_except_table6757
Functions:
~ ___setCSAttributesv1_block_invoke_2 : 736 -> 828
~ ___setCSAttributesv1_block_invoke_3 : 1252 -> 1260
~ _setCSAttributesv2 : 6900 -> 6820
~ __CIDelete : 2624 -> 2580
~ _ContentIndexDocSetResolveOIDsAndGroups_Step : 16712 -> 16780
~ ___deleteCSAttributes_block_invoke_2 : 992 -> 980
~ __CIGetOIDForDocId : 812 -> 824
~ __CIGetDocIDInfo : 960 -> 972
~ ___setCSAttributesv2_block_invoke_2 : 2256 -> 2264
~ ___deleteCSAttributes_block_invoke : 768 -> 800
~ __CIUpdateGroupAndDate : 1412 -> 1408
~ _mergeIndexData : 24736 -> 24760
~ __MergeDeletes : 1620 -> 1628
~ __CIDocIdForOID : 796 -> 808
~ __CIOidCount : 796 -> 808
~ __CIDeleteDuplicates : 1692 -> 1924
~ __CIGetGroupForDocId : 764 -> 776
~ __CIAddOids : 960 -> 972
~ __CIDeleteByOidsBulk : 1376 -> 1716
~ _ContentIndexDocSetResolveOIDs_Step : 3684 -> 3708
~ _indexCopyDeleteDocIds : 636 -> 644
~ _si_indexDeleteByOid : 268 -> 288
~ _si_delete_attributes : 320 -> 256
~ ___si_repair_sizes_block_invoke : 896 -> 920
~ _setCSAttributesv2Legacy : 6772 -> 6692
~ ___setCSAttributesv1Legacy_block_invoke_2 : 816 -> 844
+ _lazySetupMissingOids
~ ___setCSAttributesv2Legacy_block_invoke.1964 : 216 -> 200
~ ___setCSAttributesv2Legacy_block_invoke_2 : 2256 -> 2264
~ ___deleteCSAttributesLegacy_block_invoke : 772 -> 796
~ ___deleteCSAttributesLegacy_block_invoke_2 : 992 -> 980
~ ___setCSAttributesv2_block_invoke.2019 : 300 -> 200
CStrings:
+ "%s:%d: duplicate oid sweep not deleting - indexMarkDirty failed for %s, oid %lld left in place"
+ "%s:%d: orphan sweep abandoned - indexMarkDirty failed for %s, oid %lld left in place"
+ "%s:%d: orphan sweep skipped - read only index %s, oid %lld left in place"
+ "((((newIndex->coreSpotlight)?({ ((uint8_t *)newIndex->groups)[docId]; }):({ uint32_t __where=(uint32_t)docId; uint32_t __slot = __where/5; uint32_t __shift= (__where-(__slot*5))*6; uint32_t __word = ((uint32_t)(newIndex->groups[__slot])); (__word >> __shift) & 0x3F ; })) & ((((_Bool)(newIndex->coreSpotlight))) ? 0xFF : (~0x20)))) == 0"
+ "2465.1.9"
+ "_Bool processOneCS(SIRef, int64_t, oid_t, CFStringRef, CFStringRef, int, MDPlistObject, MDPlistObject, CFStringRef, size_t, CFAllocatorRef, _Bool, dispatch_group_t, si_syndication_change_s *, Boolean *)"
+ "_CIDeleteByOidsBulk"
+ "_CIDeleteDuplicates"
+ "void _si_delete_attributes_inner(SIRef, oid_t, _Bool, _Bool, _Bool, _Bool, RLEOIDMutableArrayRef, si_syndication_change_s *, uint32_t)"
- "(((newIndex->coreSpotlight?({ ((uint8_t *)newIndex->groups)[docId]; }):({ uint32_t __where=(uint32_t)docId; uint32_t __slot = __where/5; uint32_t __shift= (__where-(__slot*5))*6; uint32_t __word = ((uint32_t)(newIndex->groups[__slot])); (__word >> __shift) & 0x3F ; }))&(~0x20))) == 0"
- "2465.1.7"
- "_Bool processOneCS(SIRef, int64_t, oid_t, CFStringRef, CFStringRef, int, MDPlistObject, MDPlistObject, CFStringRef, size_t, CFAllocatorRef, _Bool, dispatch_group_t, _Bool *, Boolean *)"
- "void _si_delete_attributes_inner(SIRef, oid_t, _Bool, _Bool, _Bool, _Bool, RLEOIDMutableArrayRef, _Bool *, uint32_t)"
```
