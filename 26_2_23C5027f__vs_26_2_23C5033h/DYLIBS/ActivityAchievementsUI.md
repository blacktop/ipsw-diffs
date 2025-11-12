## ActivityAchievementsUI

> `/System/Library/PrivateFrameworks/ActivityAchievementsUI.framework/ActivityAchievementsUI`

```diff

-2026.2.2.0.0
-  __TEXT.__text: 0x378dc
+2026.2.4.0.0
+  __TEXT.__text: 0x37980
   __TEXT.__auth_stubs: 0x1560
-  __TEXT.__objc_methlist: 0x1880
+  __TEXT.__objc_methlist: 0x1888
   __TEXT.__const: 0x7f0
   __TEXT.__cstring: 0x13ba
   __TEXT.__oslogstring: 0xeb9

   __TEXT.__unwind_info: 0xc18
   __TEXT.__eh_frame: 0x884
   __TEXT.__objc_classname: 0x23d
-  __TEXT.__objc_methname: 0x66b5
-  __TEXT.__objc_methtype: 0xef6
-  __TEXT.__objc_stubs: 0x4860
-  __DATA_CONST.__got: 0x4f0
+  __TEXT.__objc_methname: 0x670e
+  __TEXT.__objc_methtype: 0xee5
+  __TEXT.__objc_stubs: 0x4880
+  __DATA_CONST.__got: 0x4e8
   __DATA_CONST.__const: 0x550
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1890
+  __DATA_CONST.__objc_selrefs: 0x18a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x2a8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 96D0A795-A82F-3C3C-95CD-6496F5862AD8
-  Functions: 1216
-  Symbols:   2708
-  CStrings:  1624
+  UUID: 8F299D67-0B86-3B60-818B-F6740D704631
+  Functions: 1217
+  Symbols:   2711
+  CStrings:  1625
 
Symbols:
+ -[AAUIBadgeImageFactory earnedBadgeRenderer]
+ -[AAUIBadgeImageFactory setEarnedBadgeRenderer:]
+ -[AAUIBadgeImageFactory setUnearnedBadgeRenderer:]
+ -[AAUIBadgeImageFactory unearnedBadgeRenderer]
+ -[AAUIMetalBadgeRenderer setRenderingFrame:]
+ _OBJC_IVAR_$_AAUIBadgeImageFactory._earnedBadgeRenderer
+ _OBJC_IVAR_$_AAUIBadgeImageFactory._unearnedBadgeRenderer
+ ___block_literal_global.322
+ ___block_literal_global.392
+ ___block_literal_global.395
+ ___block_literal_global.450
+ ___block_literal_global.748
+ ___block_literal_global.750
+ ___block_literal_global.754
+ _objc_msgSend$activateBackground:
+ _objc_msgSend$earnedBadgeRenderer
+ _objc_msgSend$setRenderingFrame:
+ _objc_msgSend$unearnedBadgeRenderer
- -[AAUIBadgeImageFactory earnedBadgeView]
- -[AAUIBadgeImageFactory setEarnedBadgeView:]
- -[AAUIBadgeImageFactory setUnearnedBadgeView:]
- -[AAUIBadgeImageFactory unearnedBadgeView]
- _OBJC_IVAR_$_AAUIBadgeImageFactory._earnedBadgeView
- _OBJC_IVAR_$_AAUIBadgeImageFactory._unearnedBadgeView
- ___block_literal_global.313
- ___block_literal_global.382
- ___block_literal_global.385
- ___block_literal_global.441
- ___block_literal_global.736
- ___block_literal_global.739
- ___block_literal_global.741
- _objc_msgSend$earnedBadgeView
- _objc_msgSend$initUsingEarnedShader:
- _objc_msgSend$unearnedBadgeView
Functions:
~ -[AAUIBadgeImageFactory init] : 224 -> 308
+ -[AAUIMetalBadgeRenderer setRenderingFrame:]
~ -[AAUIMetalBadgeRenderer _drawFrameWithDrawable:] : 332 -> 348
~ -[AAUIBadgeImageFactory _queue_generateImageForConfiguration:size:stackType:isRTL:unearned:] : 344 -> 348
CStrings:
+ "T@\"AAUIMetalBadgeRenderer\",&,N,V_earnedBadgeRenderer"
+ "T@\"AAUIMetalBadgeRenderer\",&,N,V_unearnedBadgeRenderer"
+ "_earnedBadgeRenderer"
+ "_unearnedBadgeRenderer"
+ "activateBackground:"
+ "earnedBadgeRenderer"
+ "setEarnedBadgeRenderer:"
+ "setRenderingFrame:"
+ "setUnearnedBadgeRenderer:"
+ "unearnedBadgeRenderer"
- "@\"AAUIBadgeView\""
- "T@\"AAUIBadgeView\",&,N,V_earnedBadgeView"
- "T@\"AAUIBadgeView\",&,N,V_unearnedBadgeView"
- "_earnedBadgeView"
- "_unearnedBadgeView"
- "earnedBadgeView"
- "setEarnedBadgeView:"
- "setUnearnedBadgeView:"
- "unearnedBadgeView"

```
