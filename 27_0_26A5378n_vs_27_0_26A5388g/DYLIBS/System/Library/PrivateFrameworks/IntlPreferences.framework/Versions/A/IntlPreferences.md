## IntlPreferences

> `/System/Library/PrivateFrameworks/IntlPreferences.framework/Versions/A/IntlPreferences`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA.__objc_ivar`
- `__DATA.__data`

```diff

-494.3.0.0.0
-  __TEXT.__text: 0x2ba88
-  __TEXT.__objc_methlist: 0x269c
+494.6.0.0.0
+  __TEXT.__text: 0x2bb24
+  __TEXT.__objc_methlist: 0x26ac
   __TEXT.__const: 0x228
   __TEXT.__gcc_except_tab: 0x334
   __TEXT.__cstring: 0x2a35

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2238
+  __DATA_CONST.__objc_selrefs: 0x2240
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x890

   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x640
-  __AUTH.__objc_data: 0x870
+  __AUTH_CONST.__auth_got: 0x650
+  __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x1cc
   __DATA.__data: 0x380
   __DATA.__bss: 0x220
-  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 826
-  Symbols:   2453
+  Functions: 827
+  Symbols:   2457
   CStrings:  610
 
Symbols:
+ +[IntlUtility persistRejectedLanguage:]
+ GCC_except_table105
+ _CFArrayGetTypeID
+ _CFGetTypeID
+ _objc_msgSend$persistRejectedLanguage:
- GCC_except_table104
Functions:
+ +[IntlUtility persistRejectedLanguage:]
~ +[IntlUtility rejectDiscoveredLanguage:clearFollowUp:] : 272 -> 116
```
