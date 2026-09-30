## Diagnostic-4153

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.0.27.0.0
-  __TEXT.__text: 0x8940
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_stubs: 0x2560
-  __TEXT.__objc_methlist: 0xc38
+1374.2.1.0.0
+  __TEXT.__text: 0x8dd0
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_stubs: 0x27c0
+  __TEXT.__objc_methlist: 0xcd8
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x3c1
   __TEXT.__oslogstring: 0x3bd
   __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methname: 0x2db0
-  __TEXT.__objc_methtype: 0xc72
+  __TEXT.__objc_methname: 0x30f2
+  __TEXT.__objc_methtype: 0xced
   __TEXT.__gcc_except_tab: 0x64
   __TEXT.__unwind_info: 0x1e0
   __DATA_CONST.__const: 0x1e0

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x230
-  __DATA_CONST.__got: 0x1f8
-  __DATA.__objc_const: 0x1268
-  __DATA.__objc_selrefs: 0xc80
-  __DATA.__objc_ivar: 0xe0
+  __DATA_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0x200
+  __DATA.__objc_const: 0x1358
+  __DATA.__objc_selrefs: 0xd18
+  __DATA.__objc_ivar: 0xf4
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x2a0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 207
-  Symbols:   175
-  CStrings:  730
+  Functions: 220
+  Symbols:   178
+  CStrings:  763
 
Symbols:
+ _CGRectEqualToRect
+ _UIEdgeInsetsZero
+ _objc_opt_respondsToSelector
CStrings:
+ ";"
+ "@\"NSLayoutConstraint\""
+ "T@\"NSLayoutConstraint\",&,N,V_instructionLeadingConstraint"
+ "T@\"NSLayoutConstraint\",&,N,V_instructionTopConstraint"
+ "T@\"NSLayoutConstraint\",&,N,V_instructionTrailingConstraint"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_latchedSafeAreaBounds"
+ "T{UIEdgeInsets=dddd},N,V_latchedSafeAreaInsets"
+ "_instructionLeadingConstraint"
+ "_instructionTopConstraint"
+ "_instructionTrailingConstraint"
+ "_latchedSafeAreaBounds"
+ "_latchedSafeAreaInsets"
+ "_peripheryInsets"
+ "activateConstraints:"
+ "constant"
+ "dk_instructionInsets"
+ "dk_peripheryInsets"
+ "dk_updateSafeAreaLatch"
+ "instructionLeadingConstraint"
+ "instructionTopConstraint"
+ "instructionTrailingConstraint"
+ "latchedSafeAreaBounds"
+ "latchedSafeAreaInsets"
+ "leadingAnchor"
+ "safeAreaInsets"
+ "setConstant:"
+ "setInstructionLeadingConstraint:"
+ "setInstructionTopConstraint:"
+ "setInstructionTrailingConstraint:"
+ "setLatchedSafeAreaBounds:"
+ "setLatchedSafeAreaInsets:"
+ "trailingAnchor"
+ "v48@0:8{UIEdgeInsets=dddd}16"
+ "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
+ "{UIEdgeInsets=dddd}16@0:8"
- "8"
- "safeAreaLayoutGuide"
```
