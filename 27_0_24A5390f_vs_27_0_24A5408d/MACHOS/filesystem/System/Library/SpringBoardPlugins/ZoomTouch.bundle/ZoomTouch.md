## ZoomTouch

> `/System/Library/SpringBoardPlugins/ZoomTouch.bundle/ZoomTouch`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-906.0.0.0.0
-  __TEXT.__text: 0x4068
+909.0.0.0.0
+  __TEXT.__text: 0x40a4
   __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_stubs: 0xda0
+  __TEXT.__objc_stubs: 0xdc0
   __TEXT.__objc_methlist: 0x434
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x5c
   __TEXT.__cstring: 0x38f
-  __TEXT.__objc_methname: 0x108a
+  __TEXT.__objc_methname: 0x10b4
   __TEXT.__objc_classname: 0x63
   __TEXT.__objc_methtype: 0x1c9
   __TEXT.__unwind_info: 0x1d8

   __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0x108
   __DATA.__objc_const: 0x738
-  __DATA.__objc_selrefs: 0x500
+  __DATA.__objc_selrefs: 0x508
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0xe0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 109
-  Symbols:   423
-  CStrings:  285
+  Symbols:   424
+  CStrings:  286
 
Symbols:
+ _objc_msgSend$setIgnoreTouchEventsForDisplayTransition:
Functions:
~ ___32-[ZOTWorkspace _setZoomEnabled:]_block_invoke_2 : 100 -> 160
CStrings:
+ "setIgnoreTouchEventsForDisplayTransition:"
```
