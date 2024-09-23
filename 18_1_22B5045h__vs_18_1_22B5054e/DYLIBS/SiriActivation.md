## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3401.22.4.1.1
-  __TEXT.__text: 0x44e48
+3401.28.1.0.0
+  __TEXT.__text: 0x46168
   __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x4acc
+  __TEXT.__objc_methlist: 0x4c54
   __TEXT.__const: 0x722
-  __TEXT.__cstring: 0x8f3a
-  __TEXT.__oslogstring: 0x64ea
-  __TEXT.__gcc_except_tab: 0x9ac
+  __TEXT.__cstring: 0x91ca
+  __TEXT.__oslogstring: 0x662d
+  __TEXT.__gcc_except_tab: 0xa04
   __TEXT.__dlopen_cstrs: 0x168
   __TEXT.__swift5_typeref: 0xc2
   __TEXT.__swift5_reflstr: 0xf

   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x1228
+  __TEXT.__unwind_info: 0x12a8
   __TEXT.__eh_frame: 0x110
-  __TEXT.__objc_classname: 0xd9a
-  __TEXT.__objc_methname: 0xcbcf
-  __TEXT.__objc_methtype: 0x1e90
-  __TEXT.__objc_stubs: 0x8a40
-  __DATA_CONST.__got: 0x668
+  __TEXT.__objc_classname: 0xde1
+  __TEXT.__objc_methname: 0xcc97
+  __TEXT.__objc_methtype: 0x1ebd
+  __TEXT.__objc_stubs: 0x8ae0
+  __DATA_CONST.__got: 0x670
   __DATA_CONST.__const: 0x14a8
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2910
+  __DATA_CONST.__objc_selrefs: 0x2940
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x230
+  __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x4d0
   __AUTH_CONST.__auth_got: 0x5a0
   __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x41c0
-  __AUTH_CONST.__objc_const: 0x9c58
-  __AUTH_CONST.__objc_intobj: 0x840
+  __AUTH_CONST.__const: 0x560
+  __AUTH_CONST.__cfstring: 0x4280
+  __AUTH_CONST.__objc_const: 0x9f68
+  __AUTH_CONST.__objc_intobj: 0x870
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x978
+  __AUTH.__objc_data: 0xa68
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x5b4
+  __DATA.__objc_ivar: 0x5c0
   __DATA.__data: 0xe60
   __DATA.__bss: 0x480
   __DATA_DIRTY.__objc_data: 0x1220

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1887
-  Symbols:   2369
-  CStrings:  3627
+  Functions: 1921
+  Symbols:   2409
+  CStrings:  3654
 
Symbols:
+ _OBJC_METACLASS_$_SASRequestSourceTransport
+ _OBJC_CLASS_$_SASPreheatOptions
+ _OBJC_METACLASS_$_SiriQuickTypeGestureSource
+ _OBJC_CLASS_$_SiriQuickTypeGestureSource
+ _OBJC_CLASS_$_SASRequestSourceTransport
+ _OBJC_METACLASS_$_SASPreheatOptions
CStrings:
+ "SiriQuickTypeGestureSource.ActivityAssertionReason.Prepare"
+ "SASRequestSourceTransport:%!@(MISSING)"
+ "SASPreheatOptionsRequestSourceCodingKey"
+ "@32@0:8q16Q24"
+ "-[SASSignalServer prewarmForFirstTapOfQuickTypeToSiriGesture]"
+ "SiriQuickTypeGestureSource.ActivityAssertion"
+ "SASRequestSourceTransport"
+ "SASRequestSource"
+ "initWithSASRequestSource:"
+ "%!s(MISSING) #activation #quickTypeGate Cancel Quick Type-to-Siri prewarm request, current request state: %!@(MISSING)"
+ "-[SiriQuickTypeGestureSource configureConnection]_block_invoke"
+ "-[SASSignalServer cancelPrewarmForFirstTapOfQuickTypeToSiriGesture]"
+ "-[SiriQuickTypeGestureSource configureConnection]_block_invoke_2"
+ "-[SASPresentationManager preheatNextPresentationToActivateWithOptions:]"
+ "SASPreheatOptions"
+ "prewarmForFirstTapOfQuickTypeToSiriGesture"
+ "SASPreheatOptionsLockStateCodingKey"
+ "initWithRequestSource:lockState:"
+ "preheatNextPresentationToActivateWithOptions:"
+ "-[SiriActivationService prewarmForFirstTapOfQuickTypeToSiriGesture]"
+ "%!s(MISSING) #activation #quickTypeGate Quick Type-to-Siri prewarm request, current request state: %!@(MISSING)"
+ "%!s(MISSING) #activation #quickTypeGate prewarm"
+ "%!s(MISSING) #activation #preheat preheatNextPresentationToActivateWithOptions: %!@(MISSING)"
+ "<%!@(MISSING) %!p(MISSING); requestSource=%!@(MISSING); lockState=%!@(MISSING)>"
+ "-[SiriActivationService cancelPrewarmForFirstTapOfQuickTypeToSiriGesture]"
+ "Vv24@0:8@\"SASPreheatOptions\"16"
+ "%!s(MISSING) #activation #quickTypeGate cancel prewarm"
+ "prewarm"
+ "SiriQuickTypeGestureSource"
+ "preheatWithOptions:"
+ "cancelPrewarmForFirstTapOfQuickTypeToSiriGesture"
- "%!s(MISSING) #activation #preheat"
- "-[SASPresentationManager preheatNextPresentationToActivate]"
- "preheat"
- "preheatNextPresentationToActivate"

```
