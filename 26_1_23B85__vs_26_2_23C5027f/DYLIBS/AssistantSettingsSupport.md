## AssistantSettingsSupport

> `/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport`

```diff

-3505.22.1.11.1
-  __TEXT.__text: 0x5208c
+3510.4.2.0.0
+  __TEXT.__text: 0x52120
   __TEXT.__auth_stubs: 0x1be0
-  __TEXT.__objc_methlist: 0x2a24
+  __TEXT.__objc_methlist: 0x2a3c
   __TEXT.__const: 0x1264
   __TEXT.__gcc_except_tab: 0x808
-  __TEXT.__cstring: 0x6bcd
+  __TEXT.__cstring: 0x6bdd
   __TEXT.__oslogstring: 0x1941
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x3dc

   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift_as_entry: 0x90
   __TEXT.__swift_as_ret: 0x9c
-  __TEXT.__unwind_info: 0x1528
+  __TEXT.__unwind_info: 0x1530
   __TEXT.__eh_frame: 0x11a4
   __TEXT.__objc_classname: 0x68d
-  __TEXT.__objc_methname: 0x8656
+  __TEXT.__objc_methname: 0x86a4
   __TEXT.__objc_methtype: 0xcc5
-  __TEXT.__objc_stubs: 0x6800
+  __TEXT.__objc_stubs: 0x6820
   __DATA_CONST.__got: 0x9f0
-  __DATA_CONST.__const: 0xd00
+  __DATA_CONST.__const: 0xd30
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21a8
+  __DATA_CONST.__objc_selrefs: 0x21b8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0xe00
   __AUTH_CONST.__const: 0x11f0
   __AUTH_CONST.__cfstring: 0x3f60
-  __AUTH_CONST.__objc_const: 0x4480
+  __AUTH_CONST.__objc_const: 0x44a0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x1418
   __AUTH.__data: 0x2a0
-  __DATA.__objc_ivar: 0x2d0
+  __DATA.__objc_ivar: 0x2d4
   __DATA.__data: 0xb58
   __DATA.__bss: 0xed8
   __DATA.__common: 0x88

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
+  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F178B7C1-AE58-3DA6-ADC7-B088A503B882
-  Functions: 1702
-  Symbols:   4236
-  CStrings:  2965
+  UUID: 4D58135E-1358-3F4A-80E1-F0A8F7F755EA
+  Functions: 1704
+  Symbols:   4254
+  CStrings:  2968
 
Symbols:
+ +[ASTNetworkReachability hasCellOnlyNetworkConnection]
+ -[AssistantController handleGmCFUWithConfirmation]
+ GCC_except_table186
+ GCC_except_table188
+ GCC_except_table199
+ GCC_except_table209
+ _OBJC_IVAR_$_AssistantActivationController._talkToSiriSpecifier
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftCallKit_$_AssistantSettingsSupport
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_AssistantSettingsSupport
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_AssistantSettingsSupport
+ __swift_FORCE_LOAD_$_swiftMapKit
+ __swift_FORCE_LOAD_$_swiftMapKit_$_AssistantSettingsSupport
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage_$_AssistantSettingsSupport
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_FORCE_LOAD_$_swiftVideoToolbox_$_AssistantSettingsSupport
+ _objc_msgSend$handleGmCFUWithConfirmation
- GCC_except_table185
- GCC_except_table187
- GCC_except_table198
- GCC_except_table208
Functions:
+ +[ASTNetworkReachability hasCellOnlyNetworkConnection]
~ -[AssistantActivationController specifiers] : 1104 -> 1144
~ -[AssistantActivationController .cxx_destruct] : 240 -> 260
~ -[AssistantController handleGmCFU] : 424 -> 4
+ -[AssistantController handleGmCFUWithConfirmation]
CStrings:
+ "-[AssistantController handleGmCFUWithConfirmation]"
+ "_talkToSiriSpecifier"
+ "handleGmCFUWithConfirmation"
+ "hasCellOnlyNetworkConnection"
+ "\xb1"
- "\t"
- "-[AssistantController handleGmCFU]"
- "\xa1"

```
