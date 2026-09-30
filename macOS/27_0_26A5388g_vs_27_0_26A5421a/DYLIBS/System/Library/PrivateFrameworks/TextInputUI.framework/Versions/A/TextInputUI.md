## TextInputUI

> `/System/Library/PrivateFrameworks/TextInputUI.framework/Versions/A/TextInputUI`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-9127.0.79.0.0
-  __TEXT.__text: 0x332d0
-  __TEXT.__objc_methlist: 0x1ef4
+9127.0.84.0.0
+  __TEXT.__text: 0x33564
+  __TEXT.__objc_methlist: 0x1eec
   __TEXT.__const: 0xbe8
   __TEXT.__cstring: 0x1b6f
-  __TEXT.__oslogstring: 0x1e8a
+  __TEXT.__oslogstring: 0x1f2a
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x5e8
-  __TEXT.__constg_swiftt: 0x7e4
+  __TEXT.__constg_swiftt: 0x7ec
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_reflstr: 0x3b5
   __TEXT.__swift5_fieldmd: 0x478

   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x518
-  __AUTH_CONST.__const: 0xf50
+  __DATA_CONST.__got: 0x520
+  __AUTH_CONST.__const: 0xef0
   __AUTH_CONST.__cfstring: 0x1220
-  __AUTH_CONST.__objc_const: 0x3b70
+  __AUTH_CONST.__objc_const: 0x3b80
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x60

   __DATA.__data: 0x7b0
   __DATA.__bss: 0x8d0
   __DATA.__common: 0x120
-  __DATA_DIRTY.__objc_data: 0xae8
+  __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__data: 0x258
   __DATA_DIRTY.__bss: 0x208
   __DATA_DIRTY.__common: 0x68

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/LocalAuthentication.framework/Versions/A/LocalAuthentication
   - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/PrivateFrameworks/Calculate.framework/Versions/A/Calculate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1240
-  Symbols:   2009
-  CStrings:  358
+  Functions: 1236
+  Symbols:   2006
+  CStrings:  360
 
Symbols:
+ -[TUICandidateGeneratorInstallContext .cxx_destruct]
+ -[TUICandidateGeneratorInstallContext setTextComposerWrapper:]
+ -[TUICandidateGeneratorInstallContext textComposerWrapper]
+ OBJC_IVAR_$_TUICandidateGeneratorInstallContext._textComposerWrapper
+ _OBJC_CLASS_$_LAContext
+ __OBJC_$_INSTANCE_VARIABLES_TUICandidateGeneratorInstallContext
+ __OBJC_$_PROP_LIST_TUICandidateGeneratorInstallContext
+ _objc_msgSend$canEvaluatePolicy:error:
+ _objc_msgSend$setTextComposerWrapper:
+ _objc_msgSend$textComposerWrapper
- -[TUIKeyboardCandidateMultiplexer internalSharedClientWrapper]
- -[TUIKeyboardCandidateMultiplexer setInternalSharedClientWrapper:]
- -[TUISmartReplyGenerator createLocalTextComposerClientIfNeeded]
- OBJC_IVAR_$_TUIKeyboardCandidateMultiplexer._internalSharedClientWrapper
- __113-[TUIKeyboardCandidateMultiplexer _queueOnly_resultAccumulatorForContext:type:enabledCandidateSources:isDelayed:]_block_invoke
- __113-[TUIKeyboardCandidateMultiplexer _queueOnly_resultAccumulatorForContext:type:enabledCandidateSources:isDelayed:]_block_invoke_2
- ___block_descriptor_52_8_32s40s_e5_v8?0l
- ___block_descriptor_52_8_32s40w_e5_v8?0l
- ___copy_helper_block_8_32s40w
- ___destroy_helper_block_8_32s40w
- _objc_msgSend$createLocalTextComposerClientIfNeeded
- _objc_msgSend$internalSharedClientWrapper
- _objc_msgSend$setOnContainerUpdate:
CStrings:
+ "6"
+ "Cancelled smart reply generation due to text composer client being nil."
+ "Suppressing GLP search candidate: cannot evaluate authentication"
- "7"
```
