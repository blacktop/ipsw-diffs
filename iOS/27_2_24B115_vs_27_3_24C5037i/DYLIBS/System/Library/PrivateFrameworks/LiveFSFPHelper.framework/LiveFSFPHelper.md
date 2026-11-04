## LiveFSFPHelper

> `/System/Library/PrivateFrameworks/LiveFSFPHelper.framework/LiveFSFPHelper`

```diff

-974.40.12.0.0
-  __TEXT.__text: 0x19468
+974.60.5.0.0
+  __TEXT.__text: 0x1966c
   __TEXT.__objc_methlist: 0x16a4
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0xf30
-  __TEXT.__cstring: 0x175e
-  __TEXT.__oslogstring: 0x1b0a
-  __TEXT.__unwind_info: 0x9e0
+  __TEXT.__gcc_except_tab: 0xf5c
+  __TEXT.__cstring: 0x1790
+  __TEXT.__oslogstring: 0x1b84
+  __TEXT.__unwind_info: 0x9e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__got: 0x238
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x2ea8
+  __AUTH_CONST.__objc_const: 0x2ec8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x1ac
+  __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x480
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 556
-  Symbols:   1008
-  CStrings:  341
+  Functions: 558
+  Symbols:   1009
+  CStrings:  345
 
Symbols:
+ _OBJC_IVAR_$_LiveFSFPEnumeratorHelper._pinnedDirContents
Functions:
~ -[LiveFSFPEnumeratorDataContainer loadContents] : 520 -> 636
~ -[LiveFSFPEnumeratorHelper invalidate] : 256 -> 268
~ -[LiveFSFPEnumeratorHelper reallyEnumerateItemsForObserver:startingAtPage:] : 1476 -> 1652
~ -[LiveFSFPEnumeratorHelper .cxx_destruct] : 92 -> 100
+ -[LiveFSFPEnumeratorDataContainer loadContents].cold.1
+ -[LiveFSFPEnumeratorHelper reallyEnumerateItemsForObserver:startingAtPage:].cold.4
CStrings:
+ "%s: nameTree/dateTree diverged after load (%lu vs %lu)"
+ "-[LiveFSFPEnumeratorDataContainer loadContents]"
+ "Q"
+ "enumerator helper[%p]: page's tree is stale, returning PageExpired"
```
