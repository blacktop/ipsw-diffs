## SiriSharedUI

> `/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI`

```diff

-3610.10.1.0.0
-  __TEXT.__text: 0x1616c8
-  __TEXT.__objc_methlist: 0x8a8c
+3610.17.2.0.0
+  __TEXT.__text: 0x161fec
+  __TEXT.__objc_methlist: 0x8aec
   __TEXT.__const: 0x8f44
-  __TEXT.__cstring: 0x9dca
-  __TEXT.__oslogstring: 0x1afa
+  __TEXT.__cstring: 0x9e5a
+  __TEXT.__oslogstring: 0x1b3a
   __TEXT.__gcc_except_tab: 0x46c
   __TEXT.__ustring: 0x1a
   __TEXT.__dlopen_cstrs: 0x58

   __TEXT.__swift_as_ret: 0xb0
   __TEXT.__swift_as_cont: 0x1f0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5c18
+  __TEXT.__unwind_info: 0x5c30
   __TEXT.__eh_frame: 0x2d28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x390
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5440
+  __DATA_CONST.__objc_selrefs: 0x5478
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0xd0
   __DATA_CONST.__got: 0x1750
-  __AUTH_CONST.__const: 0x6448
+  __AUTH_CONST.__const: 0x6468
   __AUTH_CONST.__cfstring: 0x1180
-  __AUTH_CONST.__objc_const: 0xf5f8
+  __AUTH_CONST.__objc_const: 0xf768
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0x2468
+  __AUTH_CONST.__auth_got: 0x2480
   __AUTH.__objc_data: 0x4868
   __AUTH.__data: 0x30e0
-  __DATA.__objc_ivar: 0x5f8
+  __DATA.__objc_ivar: 0x620
   __DATA.__data: 0x5900
   __DATA.__common: 0x2a0
   __DATA_DIRTY.__objc_data: 0xd10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7566
-  Symbols:   5404
-  CStrings:  1048
+  Functions: 7575
+  Symbols:   5426
+  CStrings:  1051
 
Symbols:
+ -[SiriSharedUICompactUserUtteranceView _flushPendingStreamingTextApply]
+ -[SiriSharedUICompactUserUtteranceView _scheduleStreamingTextApplyWithWords:showEditImage:carousel:preferredLeadingIconBundleIdentifier:]
+ -[SiriSharedUICompactUserUtteranceView setStreamingTextDeferWindow:]
+ -[SiriSharedUICompactUserUtteranceView streamingTextDeferWindow]
+ GCC_except_table21
+ GCC_except_table30
+ _MGGetLogicalDeviceDisplayCount
+ _OBJC_IVAR_$_SiriSharedUICompactUserUtteranceView._hasPendingStreamingTextApply
+ _OBJC_IVAR_$_SiriSharedUICompactUserUtteranceView._lastAppliedStreamingTransitionFadesGlyphs
+ _OBJC_IVAR_$_SiriSharedUICompactUserUtteranceView._lastAppliedStreamingWords
+ _OBJC_IVAR_$_SiriSharedUICompactUserUtteranceView._lastStreamingTextApplyTime
+ _OBJC_IVAR_$_SiriSharedUICompactUserUtteranceView._pendingStreamingCarousel
+ _OBJC_IVAR_$_SiriSharedUICompactUserUtteranceView._pendingStreamingLeadingIconBundleIdentifier
+ _OBJC_IVAR_$_SiriSharedUICompactUserUtteranceView._pendingStreamingShowEditImage
+ _OBJC_IVAR_$_SiriSharedUICompactUserUtteranceView._pendingStreamingWords
+ _OBJC_IVAR_$_SiriSharedUICompactUserUtteranceView._streamingTextApplyGeneration
+ _OBJC_IVAR_$_SiriSharedUICompactUserUtteranceView._streamingTextDeferWindow
+ _SRUIClassifyUtteranceWordsTransition
+ _SiriSharedUIDeviceIsV68.isV68
+ _SiriSharedUIDeviceIsV68.onceToken
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PHPickerViewControllerDelegate
+ ___137-[SiriSharedUICompactUserUtteranceView _scheduleStreamingTextApplyWithWords:showEditImage:carousel:preferredLeadingIconBundleIdentifier:]_block_invoke
+ ___SiriSharedUIDeviceIsV68_block_invoke
+ _dispatch_after
+ _dispatch_time
+ _swift_release_x10
- GCC_except_table12
- GCC_except_table19
- GCC_except_table29
- _MGGetProductType
CStrings:
+ "%s user utterance deferring setWords by %f to let fade-out finish"
+ "-[SiriSharedUICompactUserUtteranceView _scheduleStreamingTextApplyWithWords:showEditImage:carousel:preferredLeadingIconBundleIdentifier:]"
+ "\xd1"
```
