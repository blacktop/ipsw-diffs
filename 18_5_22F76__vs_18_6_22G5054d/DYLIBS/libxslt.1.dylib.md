## libxslt.1.dylib

> `/usr/lib/libxslt.1.dylib`

```diff

-21.7.0.0.0
-  __TEXT.__text: 0x226c8
-  __TEXT.__auth_stubs: 0xdc0
-  __TEXT.__cstring: 0x713e
+21.8.0.0.0
+  __TEXT.__text: 0x2277c
+  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__cstring: 0x7191
   __TEXT.__const: 0xc0
   __TEXT.__unwind_info: 0x4d0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x228
-  __AUTH_CONST.__auth_got: 0x6e0
+  __AUTH_CONST.__auth_got: 0x6e8
   __AUTH_CONST.__const: 0x40
   __DATA.__data: 0x28
   __DATA.__bss: 0x461

   __DATA_DIRTY.__bss: 0x40
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 059FC1BF-1376-3BE4-B72F-11327090B75B
-  Functions: 387
-  Symbols:   813
-  CStrings:  890
+  UUID: BAF62296-9F38-34C5-B233-987255C439C4
+  Functions: 388
+  Symbols:   816
+  CStrings:  892
 
Symbols:
+ _xmlCopyDoc
+ _xsltCleanupSourceDoc
Functions:
~ _xsltDocumentFunction : 1484 -> 1620
+ _xsltCleanupSourceDoc
~ _xsltApplyStylesheetInternal : 2008 -> 1896
CStrings:
+ "document() : failed to copy style doc\n"
+ "document() : failed to create xsltDocument\n"

```
