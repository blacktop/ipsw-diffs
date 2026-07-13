## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-  __TEXT.__text: 0xe6704
+  __TEXT.__text: 0xe69a4
   __TEXT.__auth_stubs: 0x1ac0
   __TEXT.__objc_methlist: 0x8ad8
   __TEXT.__const: 0x1b70
   __TEXT.__cstring: 0x3d012
-  __TEXT.__oslogstring: 0x7ef8
+  __TEXT.__oslogstring: 0x7f93
   __TEXT.__gcc_except_tab: 0x2944
-  __TEXT.__unwind_info: 0x3030
+  __TEXT.__unwind_info: 0x3038
   __TEXT.__objc_classname: 0x90f
   __TEXT.__objc_methname: 0x1319e
   __TEXT.__objc_methtype: 0x1917

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4633
-  Symbols:   16339
-  CStrings:  30265
+  Functions: 4635
+  Symbols:   16341
+  CStrings:  30268
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_nlclslist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ -[PLSubmissions handleDRConfigUpdate:error:] : 676 -> 976
+ ___44-[PLSubmissions handleDRConfigUpdate:error:]_block_invoke.112
~ -[PLSubmissions taskingModeSetup] : 1532 -> 1552
+ -[PLSubmissions handleDRConfigUpdate:error:].cold.2
CStrings:
+ "Correcting MSS cycle interval from DRConfig: %llu cycles"
+ "DRConfig cancelled, scheduling task mode exit..."
+ "Failed to correct MSS cycle interval to %llu: %d"

```
