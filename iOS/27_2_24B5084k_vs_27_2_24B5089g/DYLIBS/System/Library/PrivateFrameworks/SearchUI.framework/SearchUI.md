## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-685.1.2.0.0
-  __TEXT.__text: 0xef5e8
+685.1.3.0.0
+  __TEXT.__text: 0xef5c0
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0x124d8
+  __TEXT.__objc_methlist: 0x124e8
   __TEXT.__const: 0x3ac4
-  __TEXT.__cstring: 0x3b79
+  __TEXT.__cstring: 0x3b59
   __TEXT.__oslogstring: 0x2915
   __TEXT.__gcc_except_tab: 0xa58
   __TEXT.__ustring: 0x9c

   __TEXT.__swift_as_cont: 0x1c8
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5680
+  __TEXT.__unwind_info: 0x5678
   __TEXT.__eh_frame: 0x2334
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x410
   __DATA_CONST.__objc_protolist: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa2e8
+  __DATA_CONST.__objc_selrefs: 0xa2e0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x6f8
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x2578
-  __AUTH_CONST.__const: 0x2b28
-  __AUTH_CONST.__cfstring: 0x3420
+  __DATA_CONST.__got: 0x2570
+  __AUTH_CONST.__const: 0x2ae8
+  __AUTH_CONST.__cfstring: 0x33e0
   __AUTH_CONST.__objc_const: 0x1e0e8
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x1920
-  __AUTH.__objc_data: 0x4800
-  __AUTH.__data: 0x7f0
+  __AUTH.__objc_data: 0x36b0
+  __AUTH.__data: 0x4c0
   __DATA.__objc_ivar: 0xd00
-  __DATA.__data: 0x3384
-  __DATA.__common: 0xe8
-  __DATA_DIRTY.__objc_data: 0x3208
-  __DATA_DIRTY.__data: 0x4b0
-  __DATA_DIRTY.__bss: 0xcd8
-  __DATA_DIRTY.__common: 0x40
+  __DATA.__data: 0x2fec
+  __DATA.__common: 0xe0
+  __DATA_DIRTY.__objc_data: 0x4358
+  __DATA_DIRTY.__data: 0xb50
+  __DATA_DIRTY.__bss: 0x1128
+  __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVKit.framework/AVKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7027
-  Symbols:   15832
-  CStrings:  833
+  Functions: 7024
+  Symbols:   15825
+  CStrings:  831
 
Symbols:
+ +[SearchUIUtilities isCurrentProcessHostingSpotlight]
+ -[SearchUICardSectionView contentViewLayoutMargins]
+ -[SearchUICardSectionView updateSecondaryCommandViewAlignmentInsets]
+ _objc_msgSend$contentViewLayoutMargins
+ _objc_msgSend$isCurrentProcessHostingSpotlight
+ _objc_msgSend$updateSecondaryCommandViewAlignmentInsets
- +[SearchUIUtilities isCampoProcess]
- +[SearchUIUtilities isSpotlightProcess]
- _OBJC_CLASS_$_NSProcessInfo
- ___35+[SearchUIUtilities isCampoProcess]_block_invoke
- ___39+[SearchUIUtilities isSpotlightProcess]_block_invoke
- _isCampoProcess.isCampoProcess
- _isCampoProcess.onceToken
- _isSpotlightProcess.isSpotlightProcess
- _isSpotlightProcess.onceToken
- _objc_msgSend$isCampoProcess
- _objc_msgSend$isSpotlightProcess
- _objc_msgSend$processInfo
- _objc_msgSend$processName
CStrings:
- "Campo"
- "com.apple.Spotlight"
```
