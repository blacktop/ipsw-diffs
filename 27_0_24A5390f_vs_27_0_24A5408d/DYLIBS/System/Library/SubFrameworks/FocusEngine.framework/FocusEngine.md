## FocusEngine

> `/System/Library/SubFrameworks/FocusEngine.framework/FocusEngine`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-9127.0.79.1.102
-  __TEXT.__text: 0x306b8
-  __TEXT.__objc_methlist: 0x3950
+9127.0.84.1.102
+  __TEXT.__text: 0x306c0
+  __TEXT.__objc_methlist: 0x3958
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x3c9b
   __TEXT.__gcc_except_tab: 0x4c8

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c80
+  __DATA_CONST.__objc_selrefs: 0x1c90
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x18

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1224
-  Symbols:   3137
+  Functions: 1225
+  Symbols:   3139
   CStrings:  447
 
Symbols:
+ -[UIFocusMovementAction abortForUsageViolation:]
+ _objc_msgSend$abort
Functions:
+ -[UIFocusMovementAction abortForUsageViolation:]
```
