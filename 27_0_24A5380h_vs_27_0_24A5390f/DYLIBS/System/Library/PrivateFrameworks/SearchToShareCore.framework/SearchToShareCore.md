## SearchToShareCore

> `/System/Library/PrivateFrameworks/SearchToShareCore.framework/SearchToShareCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
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
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-3400.1.6.28.0
-  __TEXT.__text: 0x9399c
-  __TEXT.__objc_methlist: 0x49ac
+3400.1.6.30.0
+  __TEXT.__text: 0x93d58
+  __TEXT.__objc_methlist: 0x4a1c
   __TEXT.__const: 0x4f84
-  __TEXT.__cstring: 0x23a1
+  __TEXT.__cstring: 0x22e1
   __TEXT.__gcc_except_tab: 0x558
   __TEXT.__oslogstring: 0x805
   __TEXT.__constg_swiftt: 0x14b0

   __TEXT.__swift_as_entry: 0x84
   __TEXT.__swift_as_ret: 0x80
   __TEXT.__swift_as_cont: 0xc0
-  __TEXT.__unwind_info: 0x2ae8
+  __TEXT.__unwind_info: 0x2b08
   __TEXT.__eh_frame: 0x1524
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1120
   __DATA_CONST.__objc_classlist: 0x250
-  __DATA_CONST.__objc_catlist: 0x88
+  __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f88
+  __DATA_CONST.__objc_selrefs: 0x2fd8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x400
   __DATA_CONST.__got: 0x9f0
   __AUTH_CONST.__const: 0x3a68
-  __AUTH_CONST.__cfstring: 0x1c20
-  __AUTH_CONST.__objc_const: 0xc968
+  __AUTH_CONST.__cfstring: 0x1b40
+  __AUTH_CONST.__objc_const: 0xc9a8
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4007
-  Symbols:   4467
-  CStrings:  408
+  Functions: 4015
+  Symbols:   4485
+  CStrings:  401
 
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
+ _objc_msgSend$adjustedContentInset
+ _objc_msgSend$safeAreaInsets
+ _objc_msgSend$safeAreaLayoutGuide
+ _objc_msgSend$searchBarCancelButtonClicked:
+ _objc_msgSend$updateCancelButtonForVerticalBarPresent:
- GCC_except_table26
CStrings:
- "H:|-(contentInsetsLeft)-[_label]-(contentInsetsRight)-|"
- "V:|-(contentInsetsTop)-[_label]-(contentInsetsBottom)-|"
- "_label"
- "contentInsetsBottom"
- "contentInsetsLeft"
- "contentInsetsRight"
- "contentInsetsTop"
```
