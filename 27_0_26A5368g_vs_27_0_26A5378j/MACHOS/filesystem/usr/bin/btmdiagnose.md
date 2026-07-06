## btmdiagnose

> `/usr/bin/btmdiagnose`

```diff

-  __TEXT.__text: 0x25398
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_stubs: 0x3540
-  __TEXT.__objc_methlist: 0x1714
+  __TEXT.__text: 0x25860
+  __TEXT.__auth_stubs: 0xa20
+  __TEXT.__objc_stubs: 0x35a0
+  __TEXT.__objc_methlist: 0x171c
   __TEXT.__const: 0x122
   __TEXT.__gcc_except_tab: 0x418
-  __TEXT.__objc_methname: 0x418e
-  __TEXT.__cstring: 0x1763
-  __TEXT.__oslogstring: 0x1ca2
+  __TEXT.__objc_methname: 0x41c7
+  __TEXT.__cstring: 0x1793
+  __TEXT.__oslogstring: 0x1dbc
   __TEXT.__objc_classname: 0x176
   __TEXT.__objc_methtype: 0xfb1
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x5a
-  __TEXT.__unwind_info: 0x778
+  __TEXT.__unwind_info: 0x768
   __TEXT.__eh_frame: 0x260
   __DATA_CONST.__const: 0x800
   __DATA_CONST.__cfstring: 0x1ac0

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA_CONST.__auth_got: 0x510
-  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__auth_got: 0x520
+  __DATA_CONST.__got: 0x2a0
   __DATA_CONST.__auth_ptr: 0x48
   __DATA.__objc_const: 0x2370
-  __DATA.__objc_selrefs: 0x11a8
+  __DATA.__objc_selrefs: 0x11b8
   __DATA.__objc_ivar: 0x170
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x430

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 682
-  Symbols:   267
-  CStrings:  1551
+  Functions: 681
+  Symbols:   269
+  CStrings:  1559
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
CStrings:
+ "%s: error loading version %ld store data at %{public}@: %{public}@"
+ "%s: error saving user store for user %{public}@: %{public}@"
+ "%s: failed to save the upgraded store."
+ "%s: removed %ld record(s) for user %{public}@"
+ "%s: skipping user %{public}@ due to error loading user store: %{public}@"
+ "%s: upgraded store saved to %{public}@."
+ "+[BTMStore upgradeDatabase:version:]"
+ "newV17StoreFromV16StoreAtURL:error:"
+ "removeObjectAtIndex:"
- "BTMStoreV16 loadItemsWithError: %{public}@"

```
