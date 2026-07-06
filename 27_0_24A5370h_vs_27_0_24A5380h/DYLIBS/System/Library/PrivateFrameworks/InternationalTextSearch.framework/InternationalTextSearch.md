## InternationalTextSearch

> `/System/Library/PrivateFrameworks/InternationalTextSearch.framework/InternationalTextSearch`

```diff

   __TEXT.__text: 0x1af4
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x2eb
-  __TEXT.__unwind_info: 0xd8
+  __TEXT.__unwind_info: 0xd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
Functions:
~ _ITSGetCollationContextForDatabaseConnectionHandle -> _ITSRegisterSQLiteICUTokenizer : 116 -> 328
~ _ITSCollationContextFreeContextForDatabaseHandle -> _ITSSetCollationContextForDatabaseConnectionHandle : 120 -> 140
~ _ITSSetCollationContextForDatabaseConnectionHandle -> _ITSCollationContextFreeContextForDatabaseHandle : 140 -> 120
~ _ITSRegisterSQLiteICUTokenizer -> _ITSGetCollationContextForDatabaseConnectionHandle : 328 -> 116

```
