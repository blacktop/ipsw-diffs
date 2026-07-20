## SearchToShareCore

> `/System/iOSSupport/System/Library/PrivateFrameworks/SearchToShareCore.framework/Versions/A/SearchToShareCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-3400.1.6.28.0
-  __TEXT.__text: 0x9d804
-  __TEXT.__objc_methlist: 0x4af4
+3400.1.6.30.0
+  __TEXT.__text: 0x9daa4
+  __TEXT.__objc_methlist: 0x4b64
   __TEXT.__const: 0x5504
   __TEXT.__cstring: 0x24d1
   __TEXT.__gcc_except_tab: 0x558

   __TEXT.__swift_as_entry: 0x84
   __TEXT.__swift_as_ret: 0x80
   __TEXT.__swift_as_cont: 0xc0
-  __TEXT.__unwind_info: 0x2dc0
+  __TEXT.__unwind_info: 0x2de0
   __TEXT.__eh_frame: 0x173c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1120
   __DATA_CONST.__objc_classlist: 0x260
-  __DATA_CONST.__objc_catlist: 0x88
+  __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f88
+  __DATA_CONST.__objc_selrefs: 0x2fc0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x3f8
   __DATA_CONST.__got: 0xa78
   __AUTH_CONST.__const: 0x3c58
   __AUTH_CONST.__cfstring: 0x1c60
-  __AUTH_CONST.__objc_const: 0xcdd0
+  __AUTH_CONST.__objc_const: 0xce10
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x30

   - /System/Library/PrivateFrameworks/CoreParsec.framework/Versions/A/CoreParsec
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/Versions/A/SearchFoundation
   - /System/iOSSupport/System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI
+  - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/UIKit
   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4258
-  Symbols:   4598
+  Functions: 4266
+  Symbols:   4613
   CStrings:  421
 
Symbols:
+ +[UITraitCollection(STSVerticalBar) sts_isVerticalBarPresent:]
+ +[UITraitCollection(STSVerticalBar) sts_systemTraitsAffectingVerticalBar]
+ -[STSSearchBrowserHeaderView updateCancelButtonForVerticalBarPresent:]
+ -[STSSearchBrowserRootViewController _sts_closeBarButtonItemTapped:]
+ -[STSSearchBrowserRootViewController _sts_makeCloseBarButtonItem]
+ -[STSSearchBrowserRootViewController _sts_registerForVerticalBarTraitChanges]
+ -[STSSearchBrowserRootViewController _sts_syncCancelAffordanceForCurrentTraits]
+ -[STSSearchBrowserRootViewController viewDidLoad]
+ GCC_except_table31
+ _OBJC_CLASS_$_UITraitCollection
+ __OBJC_$_CATEGORY_CLASS_METHODS_UITraitCollection_$_STSVerticalBar
+ __OBJC_$_CATEGORY_UITraitCollection_$_STSVerticalBar
+ _objc_msgSend$_sts_registerForVerticalBarTraitChanges
+ _objc_msgSend$_sts_syncCancelAffordanceForCurrentTraits
+ _objc_msgSend$searchBarCancelButtonClicked:
+ _objc_msgSend$updateCancelButtonForVerticalBarPresent:
- GCC_except_table26
```
