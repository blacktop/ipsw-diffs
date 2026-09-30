## IntlPreferences

> `/System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
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
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA.__data`

```diff

-494.3.0.0.0
-  __TEXT.__text: 0x1b92c
-  __TEXT.__objc_methlist: 0x11ac
+494.6.0.0.0
+  __TEXT.__text: 0x1b9c4
+  __TEXT.__objc_methlist: 0x11bc
   __TEXT.__const: 0x1f0
   __TEXT.__cstring: 0x12e5
   __TEXT.__oslogstring: 0xeca

   __TEXT.__dlopen_cstrs: 0x20a
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x76
-  __TEXT.__unwind_info: 0x5e0
+  __TEXT.__unwind_info: 0x5e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1090
+  __DATA_CONST.__objc_selrefs: 0x1098
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x300

   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x600
-  __AUTH.__objc_data: 0x690
+  __AUTH_CONST.__auth_got: 0x610
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x190
   __DATA.__bss: 0x1d8
-  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 464
-  Symbols:   1406
+  Functions: 465
+  Symbols:   1410
   CStrings:  335
 
Symbols:
+ +[IntlUtility persistRejectedLanguage:]
+ GCC_except_table95
+ GCC_except_table99
+ _CFArrayGetTypeID
+ _CFGetTypeID
+ _objc_msgSend$persistRejectedLanguage:
- GCC_except_table94
- GCC_except_table98
Functions:
+ +[IntlUtility persistRejectedLanguage:]
~ +[IntlUtility rejectDiscoveredLanguage:clearFollowUp:] : 276 -> 124
```
