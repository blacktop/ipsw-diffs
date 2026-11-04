## kbdebug

> `/usr/bin/kbdebug`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-9127.1.13.1.105
+9127.2.6.0.0
   __TEXT.__text: 0x9b0
   __TEXT.__auth_stubs: 0x210
   __TEXT.__objc_stubs: 0x200
-  __TEXT.__objc_methlist: 0x17c
+  __TEXT.__objc_methlist: 0x194
   __TEXT.__const: 0x8
-  __TEXT.__objc_methname: 0x3c7
+  __TEXT.__objc_methname: 0x3ec
   __TEXT.__cstring: 0x142
   __TEXT.__objc_classname: 0x2f
   __TEXT.__objc_methtype: 0x1bb

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x110
   __DATA_CONST.__got: 0x28
-  __DATA.__objc_const: 0x158
-  __DATA.__objc_selrefs: 0x108
+  __DATA.__objc_const: 0x160
+  __DATA.__objc_selrefs: 0x110
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60

   - /usr/lib/libobjc.A.dylib
   Functions: 23
   Symbols:   47
-  CStrings:  81
+  CStrings:  82
 
CStrings:
+ "queue_dismissKeyboardWithCompletion:"
```
