## Install

> `/System/Library/PrivateFrameworks/Install.framework/Versions/A/Install`

```diff

-  __TEXT.__text: 0x6f474
-  __TEXT.__objc_methlist: 0x7970
+  __TEXT.__text: 0x6f42c
+  __TEXT.__objc_methlist: 0x7968
   __TEXT.__const: 0x450
-  __TEXT.__cstring: 0xcf0f
+  __TEXT.__cstring: 0xcf05
   __TEXT.__gcc_except_tab: 0x7cc
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x1d60

   __DATA_CONST.__objc_selrefs: 0x4358
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3b0
-  __DATA_CONST.__got: 0x858
+  __DATA_CONST.__got: 0x860
   __AUTH_CONST.__const: 0x388
-  __AUTH_CONST.__cfstring: 0xafe0
+  __AUTH_CONST.__cfstring: 0xafc0
   __AUTH_CONST.__objc_const: 0xaa70
-  __AUTH_CONST.__auth_got: 0xfe0
+  __AUTH_CONST.__auth_got: 0xfd8
   __AUTH.__objc_data: 0x2c60
   __AUTH.__data: 0xc50
   __DATA.__objc_ivar: 0x7cc

   - /usr/lib/libxar.1.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2666
-  Symbols:   7003
-  CStrings:  3452
+  Functions: 2665
+  Symbols:   7002
+  CStrings:  3450
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table82
+ _OBJC_CLASS_$_PKArchitectureMatcher
+ _objc_msgSend$hostCanRunAnyOf:
- -[IFDistXMLDocument(DistributionPrivate) _currentArchitectureString]
- GCC_except_table83
- _NXGetLocalArchInfo
- _objc_msgSend$_currentArchitectureString
Functions:
~ _RSAddTokenValue : 148 -> 160
~ _RSSetTokenValue : 388 -> 396
~ _GetEntryName : 108 -> 112
~ -[IFDistXMLDocument(DistributionPrivate) _validateHardwareArchitecture] : 232 -> 212
- -[IFDistXMLDocument(DistributionPrivate) _currentArchitectureString]
CStrings:
- "_unknown_"

```
