## AppleSpell

> `/System/Library/Services/AppleSpell.service/Contents/MacOS/AppleSpell`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-693.0.0.0.0
-  __TEXT.__text: 0x193248
+695.0.0.0.0
+  __TEXT.__text: 0x193614
   __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_stubs: 0x8180
-  __TEXT.__objc_methlist: 0x3624
+  __TEXT.__objc_stubs: 0x81c0
+  __TEXT.__objc_methlist: 0x366c
   __TEXT.__const: 0xb7c
-  __TEXT.__cstring: 0xc492
-  __TEXT.__gcc_except_tab: 0xa34
-  __TEXT.__objc_methname: 0xd8ad
+  __TEXT.__cstring: 0xc52c
+  __TEXT.__gcc_except_tab: 0xa7c
+  __TEXT.__objc_methname: 0xda11
   __TEXT.__oslogstring: 0x4d8
   __TEXT.__objc_classname: 0x3ec
   __TEXT.__objc_methtype: 0x3d3d
   __TEXT.__ustring: 0xc62
-  __TEXT.__unwind_info: 0x13a8
+  __TEXT.__unwind_info: 0x13c0
   __DATA_CONST.__const: 0x9810
-  __DATA_CONST.__cfstring: 0xc0e0
+  __DATA_CONST.__cfstring: 0xc120
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__auth_got: 0x6a0
   __DATA_CONST.__got: 0x488
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x4260
-  __DATA.__objc_selrefs: 0x2740
+  __DATA.__objc_const: 0x4270
+  __DATA.__objc_selrefs: 0x2760
   __DATA.__objc_ivar: 0x45c
   __DATA.__objc_data: 0xaf0
   __DATA.__data: 0x971e

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2410
+  Functions: 2414
   Symbols:   371
-  CStrings:  7037
+  CStrings:  7043
 
CStrings:
+ "_proxySuggestCompletionsForPartialWordRange:inString:language:identifier:"
+ "_proxySuggestCompletionsForPartialWordRange:inString:language:identifier:options:"
+ "_xpc_proxySuggestCompletionsForPartialWordRange:inString:language:identifier:completionHandler:"
+ "_xpc_proxySuggestCompletionsForPartialWordRange:inString:language:identifier:options:completionHandler:"
+ "server %p _xpc_proxySuggestCompletionsForPartialWordRange %@ <%@> language %@ <%@>"
+ "server %p _xpc_proxySuggestCompletionsForPartialWordRange returning %@"
```
