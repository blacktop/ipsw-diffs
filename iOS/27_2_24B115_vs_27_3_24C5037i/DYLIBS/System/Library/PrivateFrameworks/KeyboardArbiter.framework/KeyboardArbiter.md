## KeyboardArbiter

> `/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter`

```diff

-9127.1.13.1.110
-  __TEXT.__text: 0x1f1d8
-  __TEXT.__objc_methlist: 0x1944
+9127.2.6.1.101
+  __TEXT.__text: 0x1f2ac
+  __TEXT.__objc_methlist: 0x1958
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x19bf
-  __TEXT.__oslogstring: 0x2404
+  __TEXT.__cstring: 0x1acc
+  __TEXT.__oslogstring: 0x2455
   __TEXT.__gcc_except_tab: 0x994
-  __TEXT.__unwind_info: 0x850
+  __TEXT.__unwind_info: 0x860
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x978
+  __DATA_CONST.__const: 0x9a0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1278
+  __DATA_CONST.__objc_selrefs: 0x1290
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__got: 0x2e8
-  __AUTH_CONST.__const: 0x2a0
+  __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__cfstring: 0xe40
-  __AUTH_CONST.__objc_const: 0x2bb8
+  __AUTH_CONST.__objc_const: 0x2be0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x1cc
+  __DATA.__objc_ivar: 0x1d0
   __DATA.__data: 0x7e0
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0x100

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 486
-  Symbols:   1198
-  CStrings:  349
+  Functions: 489
+  Symbols:   1203
+  CStrings:  354
 
Symbols:
+ -[_UIKeyboardArbiterClientHandle releaseProcessAssertionWithQueue:]
+ -[_UIKeyboardArbiterClientHandle requestDismissalOfFocusedKeyboard]
+ _OBJC_IVAR_$__UIKeyboardArbiterClientHandle._remoteKeepAliveLingerGeneration
+ ___67-[_UIKeyboardArbiterClientHandle releaseProcessAssertionWithQueue:]_block_invoke
+ ___67-[_UIKeyboardArbiterClientHandle requestDismissalOfFocusedKeyboard]_block_invoke
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_52_e8_32s_e17_v16?0"NSError"8ls32l8
- -[_UIKeyboardArbiterClientHandle releaseProcessAssertion]
- ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
CStrings:
+ "%s  [%@] released process assertion (count=%lu)"
+ "%s  [%@] requested process assertion (count=%lu)"
+ "%s  runOperations: %s for %@"
+ "-[_UIKeyboardArbiter runOperations:onHandler:fromFunction:]"
+ "-[_UIKeyboardArbiterClientHandle releaseProcessAssertionWithQueue:]"
+ "-[_UIKeyboardArbiterClientHandle requestDismissalOfFocusedKeyboard]"
+ "-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]"
+ "Activating client handle: %{public}@(%d) lockState:%d focusContext:%@, sceneLayer:%@"
+ "RX %{public}@(%d) requestDismissalOfFocusedKeyboard"
+ "runOperations: %s Failed to access %@(%d) remote service: %@"
- "Activating client handle: %{public}@(%d) focusContext:%@, sceneLayer:%@"
- "[%@] released process assertion (count=%lu)"
- "[%@] requested process assertion (count=%lu)"
- "runOperations: %s Failed to access %@ remote service: %@"
- "runOperations: %s for %@"
```
