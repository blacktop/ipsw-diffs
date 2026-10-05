## SpotlightIndex

> `/System/Library/PrivateFrameworks/SpotlightIndex.framework/SpotlightIndex`

```diff

-2465.1.3.0.0
-  __TEXT.__text: 0x47b844
+2465.1.7.0.0
+  __TEXT.__text: 0x47c0a8
   __TEXT.__objc_methlist: 0x404
   __TEXT.__const: 0xa56a
-  __TEXT.__cstring: 0x2f434
+  __TEXT.__cstring: 0x2f4a4
   __TEXT.__gcc_except_tab: 0x29c
-  __TEXT.__oslogstring: 0x1ddf2
+  __TEXT.__oslogstring: 0x1e105
   __TEXT.__ustring: 0x2aa
   __TEXT.__dof_mds: 0x29b
-  __TEXT.__unwind_info: 0x71b0
+  __TEXT.__unwind_info: 0x71b8
   __TEXT.__eh_frame: 0x220
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1f30
+  __AUTH_CONST.__auth_got: 0x1f38
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x18d8
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0xe98
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x4d8
-  __DATA_DIRTY.__bss: 0x9cc8
+  __DATA_DIRTY.__bss: 0x9cb8
   __DATA_DIRTY.__common: 0x2402c
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 7755
-  Symbols:   10266
-  CStrings:  8072
+  Functions: 7757
+  Symbols:   10270
+  CStrings:  8085
 
Symbols:
+ GCC_except_table6757
+ _CIIndexSetCreateWithRange.sLoggedCount
+ __CIIndexSetAddRange_Bitmap_Src_SparseDst
+ __CIIndexSetSetIndexRangeWithCache.sLoggedCount
+ _repair_journal_flush
- GCC_except_table6755
CStrings:
+ "%s:%d: Parsed v2 journal entry with faulty isFromMail size %ld"
+ "%s:%d: Repair journal: could not write the %u item batch for bundle %@; those items will not be repaired"
+ "%s:%d: Repair journal: the plist builder refused a value, most likely nesting past its depth bound; dropping the whole %u item batch for bundle %@"
+ "%s:%d: Rogue accumulated position %d at docID %d off %llu. Canceling"
+ "%s:%d: Rogue nil position at docID %d off %llu size %llu(%llu), Rogue nil count %d. Canceling _CIPositionIterate_Compressed"
+ "%s:%d: Rogue position %d at docID %d off %llu size %llu(%llu), Rogue count %d. Canceling"
+ "%s:%d: Rogue position %d at docID %d off %llu. Canceling _CIPositionIterate_Compressed"
+ "%s:%d: [CIIndexSet] CIIndexSetCreateWithRange: unrepresentable range [%u, %u], clamping"
+ "%s:%d: [CIIndexSet] _CIIndexSetSetIndexRangeWithCache: refusing unrepresentable range [%u, %u]"
+ "%s:%d: unrepresentable payloadCount (%u), marking index invalid\n"
+ "2465.1.7"
+ "<si:%s> - Playback skipping sn: %lld mrsn: %lld csn: %lld mailMigration: %d"
+ "CIIndexSetCreateWithRange"
+ "_CIIndexSetSetIndexRangeWithCache"
+ "repair_journal_batch_abandoned"
+ "repair_journal_flush"
- "%s:%d: Rogue nil position at docID %d off %llu size %llu(%llu), Rogue nil count %d. Canceling"
- "%s:%d: Rogue nil position at docID %d off %llu size %llu(%llu), Rogue nil count %d. Canceling _CIPositionIterate_NewCompressed"
- "2465.1.3"
```
