## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3500.74.4.1.2
-  __TEXT.__text: 0x4be50
+3500.81.4.0.0
+  __TEXT.__text: 0x4bee8
   __TEXT.__auth_stubs: 0xb70
   __TEXT.__objc_methlist: 0x5f84
   __TEXT.__const: 0x808
   __TEXT.__cstring: 0x9cdd
-  __TEXT.__oslogstring: 0x6a18
+  __TEXT.__oslogstring: 0x6a5e
   __TEXT.__gcc_except_tab: 0xa48
   __TEXT.__dlopen_cstrs: 0x168
   __TEXT.__swift5_typeref: 0x102

   __TEXT.__objc_methtype: 0x22af
   __TEXT.__objc_stubs: 0x9280
   __DATA_CONST.__got: 0x6a0
-  __DATA_CONST.__const: 0x1648
+  __DATA_CONST.__const: 0x1628
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 82EA05A8-5617-3DDA-9331-024D80AB83F9
+  UUID: 7A0F21D8-CA7C-3F45-9E5B-E9989CA038B3
   Functions: 2120
-  Symbols:   7280
-  CStrings:  4471
+  Symbols:   7272
+  CStrings:  4472
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SiriActivation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SiriActivation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SiriActivation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SiriActivation
Functions:
~ -[SiriActivationService _shouldRejectActivationWithButtonIdentifier:activationAssertions:] : 240 -> 304
~ +[SASActivationDecision canActivateForCondition:] : 6156 -> 6244
CStrings:
+ "%s #activation NO: side button activation not supported during a call"

```
