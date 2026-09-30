## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-209.14.0.1.0
-  __TEXT.__text: 0x6502c
+209.15.0.3.0
+  __TEXT.__text: 0x65004
   __TEXT.__auth_stubs: 0xd00
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0x5614

   __TEXT.__unwind_info: 0x1930
   __TEXT.__eh_frame: 0x2e8
   __TEXT.__objc_classname: 0xdd1
-  __TEXT.__objc_methname: 0xc9aa
+  __TEXT.__objc_methname: 0xc99a
   __TEXT.__objc_methtype: 0x2708
   __TEXT.__objc_stubs: 0x8420
   __DATA_CONST.__got: 0x530

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D3C65F70-0B49-39BB-9DA4-01DB721FA275
+  UUID: 15489C97-D6B1-3243-A912-F7F22FA3BCF3
   Functions: 2298
   Symbols:   7589
   CStrings:  3972
Symbols:
+ -[CCDatabaseWriter _insertLocalContentWithProvenance:contentHash:error:]
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB9nqe210106Ev
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9nqe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
+ _objc_msgSend$_insertLocalContentWithProvenance:contentHash:error:
- -[CCDatabaseWriter _insertLocalContentWithProvenance:contentHash:isNew:error:]
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB9foe210106Ev
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9foe210106Ev
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
- _objc_msgSend$_insertLocalContentWithProvenance:contentHash:isNew:error:
Functions:
~ -[CCDatabaseWriter insertItemWithSourceItemIdHash:instanceHash:contentHash:metaContent:content:isDuplicate:error:] : 212 -> 208
~ -[CCDatabaseWriter _insertLocalContentWithProvenance:contentHash:isNew:error:] -> -[CCDatabaseWriter _insertLocalContentWithProvenance:contentHash:error:] : 344 -> 312
~ -[CCDatabaseWriter updateContent:andMetaContent:sourceItemIdHash:contentHash:instanceHash:isDuplicate:error:] : 204 -> 200
CStrings:
+ "_insertLocalContentWithProvenance:contentHash:error:"
- "_insertLocalContentWithProvenance:contentHash:isNew:error:"

```
