## TextUnderstanding

> `/System/Library/PrivateFrameworks/TextUnderstanding.framework/TextUnderstanding`

```diff

-109.0.0.0.0
-  __TEXT.__text: 0xd3c0c
-  __TEXT.__auth_stubs: 0x10c0
+113.0.0.0.0
+  __TEXT.__text: 0xd54f4
+  __TEXT.__auth_stubs: 0x10d0
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x17ac8
-  __TEXT.__cstring: 0x1b72
-  __TEXT.__swift5_typeref: 0x488f
-  __TEXT.__constg_swiftt: 0x3698
-  __TEXT.__swift5_reflstr: 0x23af
-  __TEXT.__swift5_fieldmd: 0x51a0
-  __TEXT.__swift5_proto: 0x18b0
-  __TEXT.__swift5_types: 0x620
+  __TEXT.__const: 0x17d88
+  __TEXT.__cstring: 0x1b92
+  __TEXT.__swift5_typeref: 0x492b
+  __TEXT.__constg_swiftt: 0x3720
+  __TEXT.__swift5_reflstr: 0x244f
+  __TEXT.__swift5_fieldmd: 0x524c
+  __TEXT.__swift5_proto: 0x18d4
+  __TEXT.__swift5_types: 0x630
   __TEXT.__swift5_assocty: 0x228
-  __TEXT.__oslogstring: 0x4c0
+  __TEXT.__oslogstring: 0x5e0
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x4660
-  __TEXT.__eh_frame: 0x3780
-  __TEXT.__objc_methname: 0xead
-  __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0xa0
+  __TEXT.__unwind_info: 0x4718
+  __TEXT.__eh_frame: 0x37b0
+  __TEXT.__objc_methname: 0xef4
+  __DATA_CONST.__got: 0x318
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x540
+  __DATA_CONST.__objc_selrefs: 0x558
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x860
-  __AUTH_CONST.__const: 0x8308
+  __AUTH_CONST.__auth_got: 0x868
+  __AUTH_CONST.__const: 0x83c8
   __AUTH_CONST.__objc_const: 0x120
-  __DATA.__data: 0x36a8
-  __DATA.__bss: 0x2a800
+  __DATA.__data: 0x3738
+  __DATA.__bss: 0x2ac80
   __DATA_DIRTY.__data: 0x24c8
   __DATA_DIRTY.__bss: 0x6680
   __DATA_DIRTY.__common: 0x8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/DocumentUnderstandingClient
+  - /System/Library/PrivateFrameworks/EmailCore.framework/EmailCore
   - /System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport
   - /System/Library/PrivateFrameworks/TextUnderstandingFoundation.framework/TextUnderstandingFoundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 77F11E06-F9F4-32FD-8BD3-B051C83D2C86
-  Functions: 8195
-  Symbols:   133
-  CStrings:  394
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 3E9398DA-9B26-39FB-8913-12DB90323AB7
+  Functions: 8253
+  Symbols:   139
+  CStrings:  402
 
Symbols:
+ _ECMessageHeaderKeyHMEAddress
+ _OBJC_CLASS_$_ECTagValueList
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftsimd
+ _objc_retain_x22
CStrings:
+ "Failed to parse HME header with ECTagValueList: %@"
+ "HME header missing required 'f' parameter (actual receiver email)"
+ "HME header missing required 'p' parameter (HME receiver address)"
+ "HME header missing required 's' parameter (actual sender email)"
+ "schemaorgGeocoded"
+ "setRelatedUniqueIdentifier:"
+ "tagValueListFromString:error:"
+ "valueForTag:"

```
