## icloudmailagent

> `/usr/libexec/icloudmailagent`

```diff

-2025.0.26.1.0
-  __TEXT.__text: 0x304dc
-  __TEXT.__auth_stubs: 0x1600
+2025.0.28.0.0
+  __TEXT.__text: 0x3076c
+  __TEXT.__auth_stubs: 0x1610
   __TEXT.__objc_stubs: 0x80
   __TEXT.__objc_methlist: 0x60c
   __TEXT.__const: 0x1c7a
-  __TEXT.__oslogstring: 0x1b5d
-  __TEXT.__cstring: 0xcf2
+  __TEXT.__oslogstring: 0x1bad
+  __TEXT.__cstring: 0xd32
   __TEXT.__objc_methname: 0xf6a
   __TEXT.__constg_swiftt: 0x940
   __TEXT.__swift5_typeref: 0x9fb

   __TEXT.__swift_as_ret: 0x54
   __TEXT.__unwind_info: 0xb48
   __TEXT.__eh_frame: 0x14d8
-  __DATA_CONST.__auth_got: 0xb08
+  __DATA_CONST.__auth_got: 0xb10
   __DATA_CONST.__got: 0x510
   __DATA_CONST.__auth_ptr: 0x458
-  __DATA_CONST.__const: 0x1508
+  __DATA_CONST.__const: 0x1510
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1EF672A4-C05D-3911-AC3F-6763ED8F997D
+  UUID: 2FB72780-4EEB-3EAA-90A0-BBF76D9CBB0B
   Functions: 895
-  Symbols:   7209
-  CStrings:  491
+  Symbols:   7213
+  CStrings:  494
 
Symbols:
+ _$sSo13os_log_type_ta0A0E4infoABvgZ
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_icloudmailagent
Functions:
~ _$s15icloudmailagent21MCCSecretAgentServiceC25isCategorizationSupported9forLocale10completionySS_ySb_s5Error_pSgtXEtF047$s10ObjectiveC8ObjCBoolVSo7NSErrorCSgIyByy_Sbs5K12_pSgIegyg_TR0M1C0oP0VSo0R0CSgIyByy_Tf1ncn_nTf4ndg_n : 296 -> 500
~ _$s15icloudmailagent25CategorizationSyncManagerC11syncAllowed33_D3B0FCFF93C920EE1A43E2A9ED08676CLL13callingMethodSbSS_tFTf4nd_n : 872 -> 1324
CStrings:
+ "@\"NSXPCListener\""
+ "CategorySyncEnabled"
+ "Mail Account bag value missing: CategorySyncEnabled, defaulting to enabled"

```
