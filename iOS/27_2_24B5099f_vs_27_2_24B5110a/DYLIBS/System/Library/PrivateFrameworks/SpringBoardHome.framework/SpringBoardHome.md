## SpringBoardHome

> `/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome`

```diff

-226.2.9.0.0
-  __TEXT.__text: 0x37dae8
-  __TEXT.__objc_methlist: 0x3ee5c
-  __TEXT.__const: 0x7fe4
+226.2.11.201.0
+  __TEXT.__text: 0x37e7cc
+  __TEXT.__objc_methlist: 0x3eeac
+  __TEXT.__const: 0x7ff4
   __TEXT.__cstring: 0x18cc3
   __TEXT.__gcc_except_tab: 0x43a4
-  __TEXT.__oslogstring: 0xf840
+  __TEXT.__oslogstring: 0xfab0
   __TEXT.__dlopen_cstrs: 0xb84
   __TEXT.__ustring: 0x476
   __TEXT.__constg_swiftt: 0x12e8

   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x13208
+  __TEXT.__unwind_info: 0x13258
   __TEXT.__eh_frame: 0xed8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0xbc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cc58
+  __DATA_CONST.__objc_selrefs: 0x1cc90
   __DATA_CONST.__objc_protorefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0xe90
   __DATA_CONST.__objc_arraydata: 0x6e0
-  __DATA_CONST.__got: 0x2480
+  __DATA_CONST.__got: 0x24b8
   __AUTH_CONST.__const: 0x7a30
   __AUTH_CONST.__cfstring: 0x16f60
   __AUTH_CONST.__objc_const: 0x591b0

   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__auth_got: 0x1da8
+  __AUTH_CONST.__auth_got: 0x1da0
   __AUTH.__objc_data: 0xb670
   __AUTH.__data: 0xc80
   __DATA.__objc_ivar: 0x3dd4
-  __DATA.__data: 0x9798
+  __DATA.__data: 0x97d8
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x18b0
   __DATA_DIRTY.__data: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24877
-  Symbols:   33733
-  CStrings:  4601
+  Functions: 24895
+  Symbols:   33738
+  CStrings:  4606
 
Symbols:
+ +[SBHIconStateUnarchiver _todayListRepresentationFromRepresentation:]
+ -[SBFolderView _pageIndexForListInModelFolder:]
+ -[SBHWidgetContainerViewSnapshotResizeCoordinator _setResizableViewFrameIfPossible:]
+ -[SBIconView _insertCustomIconImageViewController:]
+ -[SBIconView _insertDelayedCustomImageViewIfPossible]
+ -[SBIconView _notifyObserversDidChangeCustomImageViewController:]
+ -[SBIconView insertCustomIconImageViewWhenPossible]
+ GCC_except_table171
+ GCC_except_table271
+ GCC_except_table274
+ GCC_except_table375
+ GCC_except_table387
+ GCC_except_table395
+ GCC_except_table423
+ GCC_except_table611
+ GCC_except_table668
+ GCC_except_table709
+ GCC_except_table99
+ _SBHScrollViewIsValidContentOffset
+ ___51-[SBIconView _insertCustomIconImageViewController:]_block_invoke
- GCC_except_table170
- GCC_except_table200
- GCC_except_table207
- GCC_except_table270
- GCC_except_table273
- GCC_except_table372
- GCC_except_table386
- GCC_except_table392
- GCC_except_table422
- GCC_except_table607
- GCC_except_table664
- GCC_except_table705
- GCC_except_table98
- ___61-[SBIconView setCustomIconImageViewController:clearingOwner:]_block_invoke
- _os_variant_has_internal_ui
CStrings:
+ "<%{public}@> Delaying insertion of custom icon image view controller %{public}@ until it's inside %{public}@"
+ "<%{public}@> Inserting delayed custom icon image view controller %{public}@"
+ "<%{public}@> Skipping widget view update; invalid widgetSize:%@"
+ "Custom icon image view controller %{public}@ has no superview; waiting for icon view %{public}@ to insert it"
+ "Ignoring invalid contentOffset %{public}@ for %{public}@; current contentOffset: %{public}@, bounds: %{public}@, contentSize: %{public}@, adjustedContentInset: %{public}@, pan state: %ld, pan translation: %{public}@, pan velocity: %{public}@"
+ "Skipping snapshot resize frame update; transform %{public}@ frame %{public}@ on %{public}@"
- "<SBHWidgetStackScrollView:%@> received invalid contentOffset:%@"
```
