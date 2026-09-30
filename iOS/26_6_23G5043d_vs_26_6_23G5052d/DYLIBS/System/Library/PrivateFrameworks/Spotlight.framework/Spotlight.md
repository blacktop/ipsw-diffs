## Spotlight

> `/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight`

```diff

-  __TEXT.__text: 0x59e30
+  __TEXT.__text: 0x5a040
   __TEXT.__auth_stubs: 0x10d0
   __TEXT.__objc_methlist: 0x216c
-  __TEXT.__const: 0x1c0
-  __TEXT.__oslogstring: 0x2c19
-  __TEXT.__cstring: 0x2f78
-  __TEXT.__gcc_except_tab: 0x5250
+  __TEXT.__const: 0x1c8
+  __TEXT.__oslogstring: 0x2c2e
+  __TEXT.__cstring: 0x2f7a
+  __TEXT.__gcc_except_tab: 0x52e8
   __TEXT.__unwind_info: 0xf08
   __TEXT.__objc_classname: 0x235
-  __TEXT.__objc_methname: 0x952a
+  __TEXT.__objc_methname: 0x954c
   __TEXT.__objc_methtype: 0x1724
-  __TEXT.__objc_stubs: 0x8c40
+  __TEXT.__objc_stubs: 0x8c60
   __DATA_CONST.__got: 0x1360
   __DATA_CONST.__const: 0xbc0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28d0
+  __DATA_CONST.__objc_selrefs: 0x28d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x3a8
   __AUTH_CONST.__auth_got: 0x880
   __AUTH_CONST.__const: 0x6e0
-  __AUTH_CONST.__cfstring: 0x2c60
-  __AUTH_CONST.__objc_const: 0x36f8
+  __AUTH_CONST.__cfstring: 0x2c80
+  __AUTH_CONST.__objc_const: 0x3718
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x38c
+  __DATA.__objc_ivar: 0x390
   __DATA.__data: 0x280
   __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0x640

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 998
-  Symbols:   4825
-  CStrings:  2898
+  Symbols:   4827
+  CStrings:  2900
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _OBJC_IVAR_$_SPCSSearchQuery._isFilesAppDisabled
+ _objc_msgSend$isFPBundleID:
Functions:
~ -[SPCSSearchQuery addSearchResult:withFoundBundleID:] : 4228 -> 4428
~ -[SPCSSearchQuery executeQuery] : 21692 -> 22276
~ -[SPClientSession queryTaskWithContext:] : 1740 -> 1484
CStrings:
+ "[ProtectedApps][qid=%ld] FP result returned with oid path: %@"
+ "[ProtectedApps][qid=%ld] Files app is disabled"
+ "_isFilesAppDisabled"
+ "_kMDItemOIDPath"
+ "isFPBundleID:"
- "ProtectedApps"
- "[ProtectedApps] Files app disabled"
- "[ProtectedApps] Files app enabled"
- "[ProtectedApps] on"

```
