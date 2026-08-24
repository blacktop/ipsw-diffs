## AddressBook

> `/System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook`

```diff

-2761.100.1.0.0
-  __TEXT.__text: 0x103994
-  __TEXT.__objc_methlist: 0x17e34
+2765.100.1.1.1
+  __TEXT.__text: 0x103944
+  __TEXT.__objc_methlist: 0x17e3c
   __TEXT.__const: 0x340
   __TEXT.__gcc_except_tab: 0x1718
   __TEXT.__cstring: 0x9bc0
   __TEXT.__ustring: 0x466
   __TEXT.__dlopen_cstrs: 0xdbe
   __TEXT.__oslogstring: 0xae8
-  __TEXT.__unwind_info: 0x54a8
+  __TEXT.__unwind_info: 0x54a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8148
-  Symbols:   19283
+  Functions: 8149
+  Symbols:   19284
   CStrings:  1657
 
Symbols:
+ -[ABPersonEntry setSearchString:]
Functions:
~ -[ABPersonListSearchController setSearchField:] : 436 -> 240
~ -[ABPersonListUIReflector processUpdatedRecord:] : 964 -> 1068
+ -[ABPersonEntry setSearchString:]
```
