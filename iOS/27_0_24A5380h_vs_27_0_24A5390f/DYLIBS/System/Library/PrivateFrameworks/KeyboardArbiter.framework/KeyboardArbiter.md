## KeyboardArbiter

> `/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-9127.0.75.1.101
-  __TEXT.__text: 0x1f7bc
+9127.0.79.1.102
+  __TEXT.__text: 0x1faac
   __TEXT.__objc_methlist: 0x1954
-  __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x1998
-  __TEXT.__oslogstring: 0x22dc
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0x1996
+  __TEXT.__oslogstring: 0x2388
   __TEXT.__gcc_except_tab: 0x9a8
   __TEXT.__unwind_info: 0x700
   __TEXT.__objc_stubs: 0x0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 486
-  Symbols:   1685
-  CStrings:  344
+  Symbols:   1687
+  CStrings:  346
 
Symbols:
+ _NSStringFromCGRect
+ _objc_retain_x26
Functions:
~ ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke_2 : 180 -> 432
~ ___58-[_UIKeyboardArbiter processWithPID:foreground:suspended:]_block_invoke : 2288 -> 2520
~ ___58-[_UIKeyboardArbiter processWithPID:foreground:suspended:]_block_invoke.286 : 148 -> 400
~ ___45-[_UIKeyboardArbiter configureNewConnection:]_block_invoke.326 : 968 -> 984
CStrings:
+ "-[_UIKeyboardArbiter processWithPID:foreground:suspended:]_block_invoke"
+ "TX %{public}@(%d) queue_keyboardChanged (source:%{public}@ onScreen:%s frame:%{public}@"
+ "processWithPID:%d foreground:%s suspended:%s (%{public}@ wasRunning:%s isRunning:%s"
- "-[_UIKeyboardArbiter processWithPID:foreground:suspended:]_block_invoke_2"
```
