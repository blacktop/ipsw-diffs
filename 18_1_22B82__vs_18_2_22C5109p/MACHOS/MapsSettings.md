## MapsSettings

> `/System/Library/PreferenceBundles/MapsSettings.bundle/MapsSettings`

```diff

-2864.31.7.31.22
-  __TEXT.__text: 0x35038
+2864.32.8.22.15
+  __TEXT.__text: 0x35964
   __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_stubs: 0x7800
-  __TEXT.__objc_methlist: 0x3128
-  __TEXT.__const: 0x458
-  __TEXT.__cstring: 0xaa5f
-  __TEXT.__oslogstring: 0xf1a
-  __TEXT.__gcc_except_tab: 0x418
+  __TEXT.__objc_stubs: 0x7820
+  __TEXT.__objc_methlist: 0x3150
+  __TEXT.__const: 0x480
+  __TEXT.__cstring: 0xad1b
+  __TEXT.__oslogstring: 0x10ff
+  __TEXT.__gcc_except_tab: 0x3e4
   __TEXT.__objc_classname: 0x758
-  __TEXT.__objc_methname: 0xb4e6
+  __TEXT.__objc_methname: 0xb4fb
   __TEXT.__objc_methtype: 0x15b1
   __TEXT.__unwind_info: 0xcf0
   __DATA_CONST.__auth_got: 0x5e8
   __DATA_CONST.__got: 0x670
   __DATA_CONST.__const: 0x12230
-  __DATA_CONST.__cfstring: 0x8b80
+  __DATA_CONST.__cfstring: 0x8c00
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x118
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x2f8
   __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__objc_intobj: 0x918
   __DATA_CONST.__objc_doubleobj: 0x360
   __DATA_CONST.__objc_floatobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x1e0
-  __DATA.__objc_const: 0x6798
+  __DATA.__objc_const: 0x67b8
   __DATA.__objc_selrefs: 0x2b28
-  __DATA.__objc_ivar: 0x26c
+  __DATA.__objc_ivar: 0x270
   __DATA.__objc_data: 0x1090
   __DATA.__data: 0x3640
   __DATA.__bss: 0x730

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2151
+  Functions: 2154
   Symbols:   1556
-  CStrings:  3441
+  CStrings:  3472
 
CStrings:
+ "!_didPrepare && !_didAnimate && !_didComplete"
+ "-[GroupAnimation _childAnimationsDidComplete]"
+ "-[GroupAnimation _leaveCompletionWaitDispatchGroupWithReason:]"
+ "-[GroupAnimation addChildAnimation:]"
+ "-[GroupAnimation animate]"
+ "-[GroupAnimation complete:]"
+ "-[GroupAnimation prepare]"
+ "-[GroupAnimation runInCurrentContext]"
+ "-[GroupAnimation runWithoutAnimation]"
+ "[%!p(MISSING)] cannot leave childAnimationCompletionGroup, never entered"
+ "[%!{(MISSING)public}@] Deallocating"
+ "[%!{(MISSING)public}@] Initializing"
+ "[%!{(MISSING)public}p] %!s(MISSING)"
+ "[%!{(MISSING)public}p] %!s(MISSING):%!@(MISSING)"
+ "[%!{(MISSING)public}p] %!s(MISSING):%!d(MISSING)"
+ "[%!{(MISSING)public}p] Deallocating"
+ "[%!{(MISSING)public}p] Initializing"
+ "[%!{(MISSING)public}p] Not ready to complete yet"
+ "[%!{(MISSING)public}p] animating"
+ "[%!{(MISSING)public}p] child animation completion group notify block running"
+ "[%!{(MISSING)public}p] complete:%!d(MISSING)"
+ "[%!{(MISSING)public}p] creating child completion animation group"
+ "[%!{(MISSING)public}p] entering completion wait group for reason: %!@(MISSING)"
+ "[%!{(MISSING)public}p] executed all completion blocks"
+ "[%!{(MISSING)public}p] executing completion block: %!@(MISSING)"
+ "[%!{(MISSING)public}p] leaving completion wait group for reason: %!@(MISSING)"
+ "[%!{(MISSING)public}p] preparing"
+ "[%!{(MISSING)public}p] ready to complete, but waiting on child animations"
+ "[%!{(MISSING)public}p] runWithDelay:%!l(MISSING)f initialVelocity:%!l(MISSING)f options:%!l(MISSING)u"
+ "[%!{(MISSING)public}p] runWithDuration:%!l(MISSING)f delay:%!l(MISSING)fs options:%!l(MISSING)u"
+ "[%!{(MISSING)public}p] runWithDuration:%!l(MISSING)fs delay:%!l(MISSING)fs springDamping:%!l(MISSING)f initialVelocity:%!l(MISSING)f options:%!l(MISSING)u"
+ "[%!{(MISSING)public}p] waiting for _waitBlock"
+ "[%!{(MISSING)public}p] will execute %!l(MISSING)u completions"
+ "[self _hasPrepared] && !_didAnimate"
+ "[self _hasPrepared] && _didAnimate && !_didComplete"
+ "_childAnimationCompletionGroup != nil"
+ "_initiatingWaitBlock"
+ "cannot call -animate if -prepare or -animate was already called"
+ "cannot call -complete: if no other phase already ran"
+ "cannot call -prepare if any phase already ran"
- "[%!{(MISSING)public}@] animating"
- "[%!{(MISSING)public}@] complete:%!d(MISSING)"
- "[%!{(MISSING)public}@] entering completion wait group for reason: %!@(MISSING)"
- "[%!{(MISSING)public}@] leaving completion wait group for reason: %!@(MISSING)"
- "[%!{(MISSING)public}@] preparing"
- "[%!{(MISSING)public}@] ready to complete, but waiting on child animations"
- "[%!{(MISSING)public}@] runWithDelay:%!l(MISSING)f initialVelocity:%!l(MISSING)f options:%!l(MISSING)u"
- "[%!{(MISSING)public}@] runWithDuration:%!l(MISSING)f delay:%!l(MISSING)fs options:%!l(MISSING)u"
- "[%!{(MISSING)public}@] runWithDuration:%!l(MISSING)fs delay:%!l(MISSING)fs springDamping:%!l(MISSING)f initialVelocity:%!l(MISSING)f options:%!l(MISSING)u"

```
