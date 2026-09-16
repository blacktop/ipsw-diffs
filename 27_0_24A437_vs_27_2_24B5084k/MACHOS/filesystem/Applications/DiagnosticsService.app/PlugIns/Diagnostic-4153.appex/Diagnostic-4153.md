## Diagnostic-4153

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.2.2.0.0
-  __TEXT.__text: 0x8d74
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0x27e0
-  __TEXT.__objc_methlist: 0xcd8
+1374.40.35.0.0
+  __TEXT.__text: 0x9058
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_stubs: 0x2820
+  __TEXT.__objc_methlist: 0xcf0
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x3e2
   __TEXT.__oslogstring: 0x3be
   __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methname: 0x3109
-  __TEXT.__objc_methtype: 0xced
+  __TEXT.__objc_methname: 0x3142
+  __TEXT.__objc_methtype: 0xd57
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__unwind_info: 0x248
   __DATA_CONST.__const: 0x1e8
   __DATA_CONST.__cfstring: 0x900
   __DATA_CONST.__objc_classlist: 0x38

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x240
+  __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x208
   __DATA.__objc_const: 0x1358
-  __DATA.__objc_selrefs: 0xd20
+  __DATA.__objc_selrefs: 0xd30
   __DATA.__objc_ivar: 0xf4
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x2a0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 219
-  Symbols:   180
-  CStrings:  767
+  Functions: 221
+  Symbols:   185
+  CStrings:  771
 
Symbols:
+ _CGRectGetHeight
+ _CGRectGetMaxX
+ _CGRectGetMaxY
+ _CGRectGetMinX
+ _CGRectGetMinY
+ _CGRectGetWidth
- _CGRectContainsPoint
CStrings:
+ "clampRectangleToDrawableBounds:"
+ "hugPointToDrawableEdges:"
+ "{CGPoint=dd}32@0:8{CGPoint=dd}16"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
```
