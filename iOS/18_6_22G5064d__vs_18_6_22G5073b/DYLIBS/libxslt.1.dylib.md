## libxslt.1.dylib

> `/usr/lib/libxslt.1.dylib`

```diff

-21.8.0.0.0
-  __TEXT.__text: 0x2277c
+21.10.0.0.0
+  __TEXT.__text: 0x228e4
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__cstring: 0x7191
+  __TEXT.__cstring: 0x7198
   __TEXT.__const: 0xc0
-  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__unwind_info: 0x4e0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x228
   __AUTH_CONST.__auth_got: 0x6e8

   __DATA_DIRTY.__bss: 0x40
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: BAF62296-9F38-34C5-B233-987255C439C4
-  Functions: 388
-  Symbols:   816
+  UUID: CFE06179-852F-3DAA-B6DC-474927AAE84D
+  Functions: 390
+  Symbols:   819
   CStrings:  892
 
Symbols:
+ _xsltRVTListCreate
+ _xsltReleaseRVTList
Functions (modified):
~ _xsltFreeTransformContext : 496 -> 516
~ _xsltReleaseLocalRVTs : 296 -> 272
~ _xsltCreateRVT : 144 -> 156
~ _xsltRegisterTmpRVT : 128 -> 144
~ _xsltRegisterLocalRVT : 136 -> 152
~ _xsltReleaseRVT : 272 -> 148
~ _xsltRegisterPersistRVT : 100 -> 120
~ _xsltFreeRVTs : 224 -> 212
~ _xsltFreeStackElem : 360 -> 376
~ _xsltEvalVariable : 708 -> 720

Functions (added):
+ _xsltRVTListCreate
+ _xsltReleaseRVTList
CStrings:
+ "xsltRVTListCreate: malloc failed\n"
- "localRVT not head of list\n"

```
