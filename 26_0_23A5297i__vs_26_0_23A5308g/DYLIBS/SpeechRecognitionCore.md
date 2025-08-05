## SpeechRecognitionCore

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore`

```diff

-6.3.62.0.0
-  __TEXT.__text: 0x11214
+6.3.64.0.0
+  __TEXT.__text: 0x112a0
   __TEXT.__auth_stubs: 0xf10
   __TEXT.__objc_methlist: 0x6b4
   __TEXT.__cstring: 0x13a8

   __TEXT.__objc_methtype: 0x520
   __TEXT.__objc_stubs: 0x780
   __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x438
+  __DATA_CONST.__const: 0x448
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH.__objc_data: 0x1e0
   __AUTH.__data: 0x180
   __DATA.__objc_ivar: 0x80
-  __DATA.__data: 0x490
+  __DATA.__data: 0x498
   __DATA.__bss: 0xe8
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 502E03BF-0E0A-3086-A765-2ACBB3544BFF
+  UUID: 1BEDED59-336B-3E7B-8EAB-8F86E1891D67
   Functions: 453
-  Symbols:   1434
-  CStrings:  612
+  Symbols:   1439
+  CStrings:  613
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_SpeechRecognitionCore
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_SpeechRecognitionCore
+ _kRDKeyCommandPriority
Functions:
~ _RXGetAssetFallbackLocales : 232 -> 244
~ __Z25RXCFInit_RXLanguageObjectPKv : 100 -> 104
~ __ZN16RXLanguageObjectC1Ev : 84 -> 88
~ __ZN16RXLanguageObject12CopyPropertyEj : 960 -> 988
~ __ZN16RXLanguageObject11SetPropertyEjPKv : 832 -> 908
~ __ZN16RXLanguageObjectC2Ev : 84 -> 88
~ __ZN16RXLanguageObject9SerializeEPU24objcproto13OS_xpc_object8NSObjectP19RXRecognitionSystem : 524 -> 548
~ __ZL25RDCopyInfoDictWithInfoURLPK7__CFURL : 204 -> 192
CStrings:
+ "priority"

```
