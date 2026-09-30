## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/Versions/A/CascadeSets`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-243.0.0.0.0
-  __TEXT.__text: 0xaed6c
-  __TEXT.__objc_methlist: 0x64f4
+247.0.1.0.0
+  __TEXT.__text: 0xaf8e0
+  __TEXT.__objc_methlist: 0x6534
   __TEXT.__const: 0x3ca8
-  __TEXT.__gcc_except_tab: 0x184c
-  __TEXT.__cstring: 0x8a17
-  __TEXT.__oslogstring: 0x4d40
+  __TEXT.__gcc_except_tab: 0x1850
+  __TEXT.__cstring: 0x8a47
+  __TEXT.__oslogstring: 0x4dd0
   __TEXT.__dlopen_cstrs: 0x37a
   __TEXT.__swift5_typeref: 0xe33
   __TEXT.__constg_swiftt: 0x16bc

   __TEXT.__swift5_capture: 0x1b0
   __TEXT.__swift5_mpenum: 0xd0
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0x31e0
+  __TEXT.__unwind_info: 0x31f0
   __TEXT.__eh_frame: 0x2990
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x970
+  __DATA_CONST.__const: 0x988
   __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3170
+  __DATA_CONST.__objc_selrefs: 0x3188
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x168
-  __DATA_CONST.__got: 0x6d0
+  __DATA_CONST.__got: 0x6c8
   __AUTH_CONST.__const: 0x4eb8
-  __AUTH_CONST.__cfstring: 0x5ac0
+  __AUTH_CONST.__cfstring: 0x5b00
   __AUTH_CONST.__objc_const: 0x12168
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x558

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4635
-  Symbols:   6306
-  CStrings:  1283
+  Functions: 4640
+  Symbols:   6314
+  CStrings:  1287
 
Symbols:
+ -[CCDataResourceReadAccess resourceGenerationForSet:error:]
+ -[CCDatabaseItemRetriever _enumerateSourceItemIdHashesMatchingIndexedFieldPredicate:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateSourceItemIdHashesWithItemIdentifier:itemIdentifierType:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateSourceItemIdHashesWithSourceItemIdentifier:error:usingBlock:]
+ -[CCDatabaseWriter _compactTombstoneCountBucketRows:error:]
+ -[CCDatabaseWriter _deleteExpiredItemInstances:error:]
+ -[CCSet resourceGenerationWithUseCase:error:]
+ GCC_except_table52
+ ___102-[CCDatabaseItemRetriever _enumerateSourceItemIdHashesMatchingIndexedFieldPredicate:error:usingBlock:]_block_invoke
+ ___110-[CCDatabaseItemRetriever _enumerateSourceItemIdHashesWithItemIdentifier:itemIdentifierType:error:usingBlock:]_block_invoke
+ ___54-[CCDatabaseWriter _deleteExpiredItemInstances:error:]_block_invoke
+ ___block_descriptor_72_e8_32s40bs48r56r64r_e18_B16?0"NSNumber"8l
+ _objc_msgSend$_compactTombstoneCountBucketRows:error:
+ _objc_msgSend$_deleteExpiredItemInstances:error:
+ _objc_msgSend$_enumerateSourceItemIdHashesMatchingIndexedFieldPredicate:error:usingBlock:
+ _objc_msgSend$_enumerateSourceItemIdHashesWithItemIdentifier:itemIdentifierType:error:usingBlock:
+ _objc_msgSend$_enumerateSourceItemIdHashesWithSourceItemIdentifier:error:usingBlock:
+ _objc_msgSend$resourceGenerationForSet:error:
- -[CCDatabaseWriter _compactTombstoneCountBucketRows:]
- -[CCDatabaseWriter _deleteExpiredItemInstances:]
- _OBJC_CLASS_$__PASDeviceState
- ___48-[CCDatabaseWriter _deleteExpiredItemInstances:]_block_invoke
- ___90-[CCDatabaseItemRetriever _enumerateSourceItemIdHashesMatchingPredicate:error:usingBlock:]_block_invoke
- ___block_descriptor_56_e8_32s40r48r_e18_B16?0"NSNumber"8l
- _objc_msgSend$_compactTombstoneCountBucketRows:
- _objc_msgSend$_deleteExpiredItemInstances:
- _objc_msgSend$isDeviceUnlocked
- _objc_msgSend$removeItemAtURL:error:
CStrings:
+ "%@: Deferred after deleting %u expired item instance(s)"
+ "%@: Deferring remote device state cleanup"
+ "%@: Deferring remote device state expiry"
+ "%@: Deferring tombstone count bucket compaction"
+ "No local device site in set: %@"
+ "Successfully renamed directory at path %s into %s; cleanup deferred to prune-temporary-files"
+ "itemIdentifier"
- "Can't remove folder at %@ with error %@, isUnlocked: %hhd"
- "Successfully removed folder at %@"
- "Successfully renamed directory at path %s into %s"
```
