## AppleSpell

> `/System/Library/Services/AppleSpell.service/Contents/MacOS/AppleSpell`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-696.0.0.0.0
-  __TEXT.__text: 0x193614
-  __TEXT.__auth_stubs: 0xd20
+697.0.0.0.0
+  __TEXT.__text: 0x1936e0
+  __TEXT.__auth_stubs: 0xd60
   __TEXT.__objc_stubs: 0x81c0
   __TEXT.__objc_methlist: 0x366c
   __TEXT.__const: 0xb7c

   __TEXT.__objc_classname: 0x3ec
   __TEXT.__objc_methtype: 0x3d3d
   __TEXT.__ustring: 0xc62
-  __TEXT.__unwind_info: 0x25c0
+  __TEXT.__unwind_info: 0x25c8
   __DATA_CONST.__const: 0x9810
   __DATA_CONST.__cfstring: 0xc120
   __DATA_CONST.__objc_classlist: 0x118

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x6a0
-  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__auth_got: 0x6c0
+  __DATA_CONST.__got: 0x490
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x4270
   __DATA.__objc_selrefs: 0x2760

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2414
-  Symbols:   371
+  Functions: 2415
+  Symbols:   376
   CStrings:  7043
 
Symbols:
+ __dispatch_source_type_signal
+ _dispatch_resume
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _signal
```
