## AccessibilityUIService

> `/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService`

```diff

-  __TEXT.__text: 0x1eb2c
-  __TEXT.__objc_methlist: 0x1bec
-  __TEXT.__const: 0x840
+  __TEXT.__text: 0x1f2e4
+  __TEXT.__objc_methlist: 0x1c04
+  __TEXT.__const: 0x850
   __TEXT.__constg_swiftt: 0x184
   __TEXT.__swift5_typeref: 0x1d7
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__cstring: 0x152e
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x44
-  __TEXT.__oslogstring: 0x1216
+  __TEXT.__oslogstring: 0x13c4
   __TEXT.__swift5_reflstr: 0xb5
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x48

   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x20
   __TEXT.__gcc_except_tab: 0x488
-  __TEXT.__unwind_info: 0x898
+  __TEXT.__unwind_info: 0x8a8
   __TEXT.__eh_frame: 0x408
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1858
+  __DATA_CONST.__objc_selrefs: 0x1868
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x4f8
+  __DATA_CONST.__got: 0x508
   __AUTH_CONST.__const: 0x4b0
   __AUTH_CONST.__cfstring: 0xaa0
   __AUTH_CONST.__objc_const: 0x27f0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x880
-  __AUTH.__objc_data: 0x530
+  __AUTH_CONST.__auth_got: 0x888
+  __AUTH.__objc_data: 0x260
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x18c
   __DATA.__data: 0x690
   __DATA.__common: 0x18
-  __DATA.__bss: 0x920
-  __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0x38
+  __DATA.__bss: 0x910
+  __DATA_DIRTY.__objc_data: 0x640
+  __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 735
-  Symbols:   2706
-  CStrings:  296
+  Functions: 739
+  Symbols:   2720
+  CStrings:  300
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__data : content changed
Symbols:
+ -[AXUIDisplayManager _attemptFlushOfQueuedAddBlocksForSceneClientIdentifier:requireActiveScene:]
+ -[AXUIDisplayManager _postAccessibilityShortcutBannerWithTitle:subtitleText:]
+ GCC_except_table418
+ GCC_except_table435
+ _AXProcessIsSpringBoard
+ _AXSpringBoardActionKeyAccessibilityShortcutBannerSubtitle
+ _AXSpringBoardActionKeyAccessibilityShortcutBannerTitle
+ ___77-[AXUIDisplayManager _postAccessibilityShortcutBannerWithTitle:subtitleText:]_block_invoke
+ ___96-[AXUIDisplayManager _attemptFlushOfQueuedAddBlocksForSceneClientIdentifier:requireActiveScene:]_block_invoke
+ _objc_msgSend$_attemptFlushOfQueuedAddBlocksForSceneClientIdentifier:requireActiveScene:
+ _objc_msgSend$_canShowWhileLocked
+ _objc_msgSend$_postAccessibilityShortcutBannerWithTitle:subtitleText:
- GCC_except_table414
- GCC_except_table431
CStrings:
+ "Deferring add-block flush for client '%{public}@' — %lu queued, no active scene yet (best scene: %p, activationState: %ld)"
+ "Fallback flush timer fired for client '%{public}@' but blocks already drained (likely by activation early-flush)"
+ "Fallback flush timer fired for client '%{public}@' — flushing %lu queued block(s) without active scene check"
+ "Flushing %lu queued add block(s) for client '%{public}@' (requireActiveScene=%d)"

```
