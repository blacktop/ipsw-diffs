## SystemPolicy

> `/System/Library/PrivateFrameworks/SystemPolicy.framework/Versions/A/SystemPolicy`

```diff

-  __TEXT.__text: 0x1900c
-  __TEXT.__objc_methlist: 0x1988
+  __TEXT.__text: 0x19378
+  __TEXT.__objc_methlist: 0x19a8
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x1804
+  __TEXT.__cstring: 0x1825
   __TEXT.__gcc_except_tab: 0x1bc
   __TEXT.__oslogstring: 0x1544
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x7e0
+  __TEXT.__unwind_info: 0x7e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf50
+  __DATA_CONST.__objc_selrefs: 0xf78
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x490
+  __DATA_CONST.__objc_arraydata: 0x4a0
   __DATA_CONST.__got: 0x2e0
   __AUTH_CONST.__const: 0x910
   __AUTH_CONST.__cfstring: 0x2220
-  __AUTH_CONST.__objc_const: 0x3760
-  __AUTH_CONST.__objc_arrayobj: 0x198
+  __AUTH_CONST.__objc_const: 0x37e0
+  __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x498
-  __DATA.__objc_ivar: 0x2a0
+  __AUTH_CONST.__auth_got: 0x4a0
+  __DATA.__objc_ivar: 0x2ac
   __DATA.__data: 0x248
   __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0xb40

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 808
-  Symbols:   1944
-  CStrings:  731
+  Functions: 812
+  Symbols:   1956
+  CStrings:  732
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[PolicyScanTarget hasUnsealedInfoPlist]
+ -[PolicyScanTarget infoPlistHash]
+ -[PolicyScanTarget setHasUnsealedInfoPlist:]
+ OBJC_IVAR_$_PolicyScanTarget._hasUnsealedInfoPlist
+ OBJC_IVAR_$_PolicyScanTarget._infoPlistHash
+ OBJC_IVAR_$_PolicyScanTarget._unsealedInfoPlistChecked
+ _CC_SHA256
+ _cdInfoSlot
+ _isInfoPlistConsistencyEnforcementEnabled
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$hasUnsealedInfoPlist
+ _objc_msgSend$stringByAppendingString:
CStrings:
+ "InfoPlistConsistencyEnforcement"

```
