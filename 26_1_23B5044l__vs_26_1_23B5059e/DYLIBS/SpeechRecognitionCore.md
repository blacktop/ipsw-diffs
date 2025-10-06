## SpeechRecognitionCore

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore`

```diff

-6.3.67.0.0
-  __TEXT.__text: 0x113b4
-  __TEXT.__auth_stubs: 0xf10
+6.3.68.1.0
+  __TEXT.__text: 0x11524
+  __TEXT.__auth_stubs: 0xf60
   __TEXT.__objc_methlist: 0x6b4
-  __TEXT.__cstring: 0x13a8
+  __TEXT.__cstring: 0x13f8
   __TEXT.__gcc_except_tab: 0x1034
   __TEXT.__const: 0xea
-  __TEXT.__oslogstring: 0x440
+  __TEXT.__oslogstring: 0x470
   __TEXT.__ustring: 0xc
   __TEXT.__swift5_typeref: 0x28
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__unwind_info: 0x938
+  __TEXT.__unwind_info: 0x940
   __TEXT.__objc_classname: 0x115
   __TEXT.__objc_methname: 0xe90
   __TEXT.__objc_methtype: 0x520
   __TEXT.__objc_stubs: 0x7c0
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x448
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x468
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x410
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x798
-  __AUTH_CONST.__const: 0x4d0
-  __AUTH_CONST.__cfstring: 0xbc0
+  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__const: 0x4f0
+  __AUTH_CONST.__cfstring: 0xc20
   __AUTH_CONST.__objc_const: 0xcc0
   __AUTH.__objc_data: 0x1e0
   __AUTH.__data: 0x180

   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8A40E797-3014-3DFF-8530-B9A47A6D48A6
-  Functions: 453
-  Symbols:   1443
-  CStrings:  615
+  UUID: 4D4E3206-B5DF-328F-8DFE-DA55CFCDD846
+  Functions: 454
+  Symbols:   1453
+  CStrings:  623
 
Symbols:
+ GCC_except_table42
+ GCC_except_table49
+ _CFBooleanGetTypeID
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ _TCCAccessPreflight
+ _TCCAccessRequest
+ ____ZN5RXXPC11ClientEventEPU24objcproto13OS_xpc_object8NSObject_block_invoke.130
+ ____ZN5RXXPC19EstablishConnectionEv_block_invoke.125
+ ____ZN5RXXPC19EstablishConnectionEv_block_invoke.126
+ ____ZN5RXXPC19EstablishConnectionEv_block_invoke.127
+ ____ZN5RXXPC19EstablishConnectionEv_block_invoke.128
+ ___block_descriptor_32_e8_v12?0C8l
+ ___block_literal_global.133
+ ___block_literal_global.79
+ _kTCCServiceMicrophone
- GCC_except_table39
- GCC_except_table50
- ____ZN5RXXPC11ClientEventEPU24objcproto13OS_xpc_object8NSObject_block_invoke.117
- ____ZN5RXXPC19EstablishConnectionEv_block_invoke.113
- ____ZN5RXXPC19EstablishConnectionEv_block_invoke.114
- ____ZN5RXXPC19EstablishConnectionEv_block_invoke.115
- ___block_literal_global.120
Functions:
~ __ZN5RXXPC19EstablishConnectionEv : 2192 -> 2372
+ ____ZN5RXXPC19EstablishConnectionEv_block_invoke
CStrings:
+ "NO"
+ "PeerConnection: TCC service granted: %{public}@"
+ "YES"
+ "com.apple.private.voicecontrol.speechrecognition.api"
+ "v12@?0C8"

```
