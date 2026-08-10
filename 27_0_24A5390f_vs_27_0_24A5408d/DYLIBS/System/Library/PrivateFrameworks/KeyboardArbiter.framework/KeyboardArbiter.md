## KeyboardArbiter

> `/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-9127.0.79.1.102
-  __TEXT.__text: 0x1faac
-  __TEXT.__objc_methlist: 0x1954
+9127.0.84.1.102
+  __TEXT.__text: 0x1f8e4
+  __TEXT.__objc_methlist: 0x1944
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x1996
-  __TEXT.__oslogstring: 0x2388
-  __TEXT.__gcc_except_tab: 0x9a8
-  __TEXT.__unwind_info: 0x700
+  __TEXT.__cstring: 0x19bf
+  __TEXT.__oslogstring: 0x2404
+  __TEXT.__gcc_except_tab: 0x994
+  __TEXT.__unwind_info: 0x708
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x958
+  __DATA_CONST.__const: 0x978
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1270
+  __DATA_CONST.__objc_selrefs: 0x1278
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x80
-  __DATA_CONST.__got: 0x2f0
+  __DATA_CONST.__got: 0x2e8
   __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__cfstring: 0xe40
-  __AUTH_CONST.__objc_const: 0x2be8
+  __AUTH_CONST.__objc_const: 0x2bb8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30

   __DATA.__data: 0x7e0
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x6e0
-  __DATA_DIRTY.__bss: 0xf0
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 486
-  Symbols:   1687
-  CStrings:  346
+  Symbols:   1686
+  CStrings:  349
 
Symbols:
+ -[_UIKeyboardArbiter _handleForPID:]
+ -[_UIKeyboardArbiter handleRepresentsEventDeferringTarget:]
+ -[_UIKeyboardArbiterAdvisorAction abortForUsageViolation:]
+ -[_UIKeyboardArbiterClientHandle keyboardSceneHostComponent]
+ -[_UIKeyboardArbiterOmniscientDelegateAction abortForUsageViolation:]
+ GCC_except_table131
+ GCC_except_table137
+ GCC_except_table173
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table46
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table67
+ GCC_except_table95
+ ___36-[_UIKeyboardArbiter _handleForPID:]_block_invoke
+ ___block_descriptor_36_e40_B16?0"_UIKeyboardArbiterClientHandle"8l
+ _objc_msgSend$_handleForPID:
+ _objc_msgSend$abort
+ _objc_msgSend$bs_firstObjectPassingTest:
+ _objc_msgSend$handleRepresentsEventDeferringTarget:
+ _objc_msgSend$keyboardSceneHostComponent
- -[_UIKeyboardArbiterClientHandle pointIsWithinKeyboardContent:onCompletion:]
- -[_UIKeyboardArbiterClientHandle setAllVisibleFrames:]
- -[_UIKeyboardArbiterInputUIClientSceneComponent setVisibleKeyboardFrames:]
- GCC_except_table129
- GCC_except_table135
- GCC_except_table170
- GCC_except_table174
- GCC_except_table176
- GCC_except_table195
- GCC_except_table196
- GCC_except_table47
- GCC_except_table64
- GCC_except_table66
- GCC_except_table68
- GCC_except_table96
- _.str
- _OBJC_CLASS_$_UIPeripheralHost
- ___54-[_UIKeyboardArbiter setActiveInputDestinationHandle:]_block_invoke_3
- ___54-[_UIKeyboardArbiterClientHandle setAllVisibleFrames:]_block_invoke
- ___74-[_UIKeyboardArbiterInputUIClientSceneComponent setVisibleKeyboardFrames:]_block_invoke
- _objc_msgSend$inputUIComponent
- _objc_msgSend$pointIsWithinKeyboardContent:
- _objc_msgSend$setAllVisibleFrames:
- _objc_msgSend$setVisibleKeyboardFrames:
- _objc_msgSend$visibleKeyboardFrames
CStrings:
+ "B16@?0@\"_UIKeyboardArbiterClientHandle\"8"
+ "KeyboardArbiter could not find a keyboard scene for app scene %@"
+ "KeyboardArbiter has no scene identity for client handle %@"
```
