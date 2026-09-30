## Pasteboard

> `/System/Library/PrivateFrameworks/Pasteboard.framework/Pasteboard`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-9127.0.75.1.101
-  __TEXT.__text: 0x27cd4
+9127.0.78.0.0
+  __TEXT.__text: 0x27d1c
   __TEXT.__objc_methlist: 0x22a0
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x1b8c
+  __TEXT.__cstring: 0x1b97
   __TEXT.__gcc_except_tab: 0x830
   __TEXT.__oslogstring: 0x1670
   __TEXT.__ustring: 0xb0

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x220
   __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x11c0
+  __AUTH_CONST.__cfstring: 0x11e0
   __AUTH_CONST.__objc_const: 0x30c8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1071
-  Symbols:   2269
-  CStrings:  312
+  Symbols:   2271
+  CStrings:  313
 
Symbols:
+ _close
+ _mkstemps
+ _objc_msgSend$stringByAppendingString:
+ _unlink
- _mkstemp
- _objc_msgSend$stringByAppendingPathExtension:
Functions:
~ _PBTemporaryFileName : 492 -> 564
CStrings:
+ "."
+ ".%@.XXXXXX%@"
- "tmp"
```
