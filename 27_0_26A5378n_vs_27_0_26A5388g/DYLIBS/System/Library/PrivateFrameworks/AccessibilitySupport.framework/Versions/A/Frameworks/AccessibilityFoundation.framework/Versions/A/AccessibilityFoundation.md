## AccessibilityFoundation

> `/System/Library/PrivateFrameworks/AccessibilitySupport.framework/Versions/A/Frameworks/AccessibilityFoundation.framework/Versions/A/AccessibilityFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_Accessibi`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-448.0.0.0.0
-  __TEXT.__text: 0x49900
-  __TEXT.__objc_methlist: 0x6c8c
+450.0.0.0.0
+  __TEXT.__text: 0x49a64
+  __TEXT.__objc_methlist: 0x6ca4
   __TEXT.__const: 0x2c0
   __TEXT.__cstring: 0x4d4f
   __TEXT.__oslogstring: 0xe34

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3fb8
+  __DATA_CONST.__objc_selrefs: 0x3fc8
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__got: 0x618
   __AUTH_CONST.__const: 0x1110
   __AUTH_CONST.__cfstring: 0x6a60
-  __AUTH_CONST.__objc_const: 0xb340
+  __AUTH_CONST.__objc_const: 0xb370
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1568
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x3ec
+  __DATA.__objc_ivar: 0x3f0
   __DATA.__data: 0x540
   __DATA.__bss: 0x4b0
   __DATA_DIRTY.__objc_data: 0x208

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2646
-  Symbols:   5622
+  Functions: 2648
+  Symbols:   5626
   CStrings:  998
 
Symbols:
+ -[_AXFObserverGroupIPC _observersLock]
+ -[_AXFObserverGroupIPC set_observersLock:]
+ OBJC_IVAR_$__AXFObserverGroupIPC.__observersLock
+ _objc_msgSend$_observersLock
CStrings:
+ "5"
- "4"
```
