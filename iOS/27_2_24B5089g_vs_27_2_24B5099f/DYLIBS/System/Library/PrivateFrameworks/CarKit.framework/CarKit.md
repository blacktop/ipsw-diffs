## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-807.2.0.0.0
-  __TEXT.__text: 0x6022c
-  __TEXT.__delay_stubs: 0x40
-  __TEXT.__delay_helper: 0xa4
+807.4.0.0.0
+  __TEXT.__text: 0x602a0
   __TEXT.__objc_methlist: 0x63ec
   __TEXT.__const: 0x558
   __TEXT.__gcc_except_tab: 0xa1c
-  __TEXT.__oslogstring: 0x6c86
-  __TEXT.__cstring: 0x5bbd
+  __TEXT.__oslogstring: 0x6c26
+  __TEXT.__cstring: 0x5b6d
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__constg_swiftt: 0x1a0
   __TEXT.__swift5_typeref: 0x17e

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x2608
+  __TEXT.__unwind_info: 0x2610
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__got: 0x880
   __AUTH_CONST.__const: 0x1bc0
   __AUTH_CONST.__cfstring: 0x5d80
-  __AUTH_CONST.__objc_const: 0x10390
+  __AUTH_CONST.__objc_const: 0x10370
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0xae0
+  __AUTH_CONST.__auth_got: 0xad0
   __AUTH.__objc_data: 0x1400
-  __AUTH.__data: 0x1b8
-  __DATA.__objc_ivar: 0x738
+  __AUTH.__data: 0x188
+  __DATA.__objc_ivar: 0x734
   __DATA.__data: 0x1190
   __DATA_DIRTY.__objc_data: 0x640
+  __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 3058
-  Symbols:   4762
-  CStrings:  1436
+  Symbols:   4757
+  CStrings:  1434
 
Symbols:
+ GCC_except_table122
- GCC_except_table121
- _AFIsLinwoodEnabledAndWasEverAvailable
- _AFIsLinwoodEnabledAndWasEverAvailable$delayInitStub
- _OBJC_IVAR_$_CARSession._videoPlaybackAvailable
- _dlopenHelper$AssistantServices
- _dlopenHelperFlag$AssistantServices
Functions:
~ -[CARSession videoPlaybackAvailable] : 8 -> 216
~ -[CARSession .cxx_destruct] : 164 -> 152
~ -[CRCarPlayAppPolicyEvaluator _isCampoSupported] : 304 -> 224
CStrings:
+ "SiriApp is installed"
- "/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices"
- "Linwood not enabled or was never available, hiding Campo from CarPlay"
- "SiriApp is installed and Linwood is enabled and available"
```
