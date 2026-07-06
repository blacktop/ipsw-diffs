## UIKitServices

> `/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`

```diff

-  __TEXT.__text: 0x21098
-  __TEXT.__objc_methlist: 0x2e8c
+  __TEXT.__text: 0x21400
+  __TEXT.__objc_methlist: 0x2f3c
   __TEXT.__const: 0x2d0
   __TEXT.__dlopen_cstrs: 0x2fc
-  __TEXT.__cstring: 0x45dc
+  __TEXT.__cstring: 0x45f1
   __TEXT.__oslogstring: 0x671
   __TEXT.__gcc_except_tab: 0x478
-  __TEXT.__unwind_info: 0xbd0
+  __TEXT.__unwind_info: 0xbe8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa20
-  __DATA_CONST.__objc_classlist: 0x250
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17d0
+  __DATA_CONST.__objc_selrefs: 0x17e0
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x1d8
-  __DATA_CONST.__objc_arraydata: 0x750
-  __DATA_CONST.__got: 0x480
-  __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x3960
-  __AUTH_CONST.__objc_const: 0x61f0
+  __DATA_CONST.__objc_superrefs: 0x1e0
+  __DATA_CONST.__objc_arraydata: 0x760
+  __DATA_CONST.__got: 0x490
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0x39c0
+  __AUTH_CONST.__objc_const: 0x6440
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x1e0
-  __AUTH_CONST.__objc_arrayobj: 0x1b0
+  __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__auth_got: 0x7d0
-  __AUTH.__objc_data: 0xf50
+  __AUTH.__objc_data: 0xfa0
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x2a4
-  __DATA.__data: 0x800
+  __DATA.__objc_ivar: 0x2b0
+  __DATA.__data: 0x860
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_ivar: 0x44
   __DATA_DIRTY.__objc_data: 0x7d0
-  __DATA_DIRTY.__bss: 0x170
+  __DATA_DIRTY.__bss: 0x180
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 998
-  Symbols:   3903
-  CStrings:  1082
+  Functions: 1008
+  Symbols:   3946
+  CStrings:  1087
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[UISDictationVariant allVariants]
+ +[UISDictationVariant variantForSecureName:]
+ +[UISDictationVariant variantForSelector:]
+ -[UISDictationVariant .cxx_destruct]
+ -[UISDictationVariant glyph]
+ -[UISDictationVariant initWithSecureName:selector:glyph:]
+ -[UISDictationVariant localizedStringForLocalization:]
+ -[UISDictationVariant secureName]
+ -[UISDictationVariant selector]
+ _OBJC_CLASS_$_UISDictationVariant
+ _OBJC_IVAR_$_UISDictationVariant._glyph
+ _OBJC_IVAR_$_UISDictationVariant._secureName
+ _OBJC_IVAR_$_UISDictationVariant._selector
+ _OBJC_METACLASS_$_UISDictationVariant
+ __OBJC_$_CLASS_METHODS_UISDictationVariant
+ __OBJC_$_CLASS_PROP_LIST_UISDictationVariant
+ __OBJC_$_INSTANCE_METHODS_UISDictationVariant
+ __OBJC_$_INSTANCE_VARIABLES_UISDictationVariant
+ __OBJC_$_PROP_LIST_UISDictationVariant
+ __OBJC_$_PROP_LIST_UISSecureVariant
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UISSecureVariant
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UISSecureVariant
+ __OBJC_$_PROTOCOL_REFS_UISSecureVariant
+ __OBJC_CLASS_PROTOCOLS_$_UISDictationVariant
+ __OBJC_CLASS_PROTOCOLS_$_UISPasteVariant
+ __OBJC_CLASS_RO_$_UISDictationVariant
+ __OBJC_LABEL_PROTOCOL_$_UISSecureVariant
+ __OBJC_METACLASS_RO_$_UISDictationVariant
+ __OBJC_PROTOCOL_$_UISSecureVariant
+ ___34+[UISDictationVariant allVariants]_block_invoke
+ _objc_msgSend$initWithSecureName:selector:glyph:
CStrings:
+ "Dictation"
+ "microphone"

```
