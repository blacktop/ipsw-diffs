## Diagnostic-8246

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246`

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
-  __TEXT.__text: 0x4c60
-  __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_stubs: 0x1660
-  __TEXT.__objc_methlist: 0x6ac
+1374.2.1.0.0
+  __TEXT.__text: 0x50f0
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_stubs: 0x18e0
+  __TEXT.__objc_methlist: 0x74c
   __TEXT.__const: 0x60
-  __TEXT.__objc_methname: 0x1802
+  __TEXT.__objc_methname: 0x1b47
   __TEXT.__cstring: 0x1c8
   __TEXT.__objc_classname: 0xc5
-  __TEXT.__objc_methtype: 0x41e
+  __TEXT.__objc_methtype: 0x52e
   __TEXT.__oslogstring: 0x52d
   __TEXT.__unwind_info: 0x140
   __DATA_CONST.__const: 0x130

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x108
-  __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0x1e8
-  __DATA.__objc_const: 0xaf8
-  __DATA.__objc_selrefs: 0x760
-  __DATA.__objc_ivar: 0x7c
+  __DATA_CONST.__auth_got: 0x208
+  __DATA_CONST.__got: 0x1f0
+  __DATA.__objc_const: 0xbe8
+  __DATA.__objc_selrefs: 0x800
+  __DATA.__objc_ivar: 0x90
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x180
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 126
-  Symbols:   144
-  CStrings:  441
+  Functions: 139
+  Symbols:   147
+  CStrings:  478
 
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
+ "screen"
+ "setConstant:"
+ "setInstructionLeadingConstraint:"
+ "setInstructionTopConstraint:"
+ "setInstructionTrailingConstraint:"
+ "setLatchedSafeAreaBounds:"
+ "setLatchedSafeAreaInsets:"
+ "trailingAnchor"
+ "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "v48@0:8{UIEdgeInsets=dddd}16"
+ "window"
+ "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
+ "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
+ "{UIEdgeInsets=dddd}16@0:8"
- "8"
- "safeAreaLayoutGuide"
- "setActive:"
```
