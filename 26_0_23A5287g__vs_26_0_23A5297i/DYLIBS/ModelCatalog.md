## ModelCatalog

> `/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog`

```diff

-214.1.0.0.0
-  __TEXT.__text: 0x2471bc
-  __TEXT.__auth_stubs: 0x1b80
+217.0.0.0.0
+  __TEXT.__text: 0x24b2f8
+  __TEXT.__auth_stubs: 0x1ba0
   __TEXT.__objc_methlist: 0x7b8
-  __TEXT.__const: 0x41efc
-  __TEXT.__cstring: 0x26f5e
-  __TEXT.__swift5_typeref: 0x8aa6
-  __TEXT.__oslogstring: 0x1b1d
-  __TEXT.__constg_swiftt: 0x92e4
-  __TEXT.__swift5_reflstr: 0x39b3
-  __TEXT.__swift5_fieldmd: 0x19cb0
+  __TEXT.__cstring: 0x270ee
+  __TEXT.__swift5_typeref: 0x8be2
+  __TEXT.__swift5_fieldmd: 0x19e58
+  __TEXT.__const: 0x4263c
+  __TEXT.__constg_swiftt: 0x9420
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_proto: 0x4d00
-  __TEXT.__swift5_types: 0xfec
-  __TEXT.__swift5_capture: 0x8180
+  __TEXT.__swift5_reflstr: 0x39a3
+  __TEXT.__swift5_protos: 0x15c
+  __TEXT.__swift5_types: 0x100c
+  __TEXT.__oslogstring: 0x1cfd
+  __TEXT.__swift5_proto: 0x4d7c
+  __TEXT.__swift5_capture: 0x8240
   __TEXT.__swift_as_entry: 0x150
   __TEXT.__swift_as_ret: 0x118
-  __TEXT.__swift5_assocty: 0x4f78
-  __TEXT.__swift5_protos: 0x154
+  __TEXT.__swift5_assocty: 0x4fc0
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0xdaa0
-  __TEXT.__eh_frame: 0x11d4c
+  __TEXT.__unwind_info: 0xd7d8
+  __TEXT.__eh_frame: 0x11ed4
   __TEXT.__objc_classname: 0x39
-  __TEXT.__objc_methname: 0xcbc
+  __TEXT.__objc_methname: 0xccb
   __TEXT.__objc_methtype: 0x100
-  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__got: 0x400
   __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f8
+  __DATA_CONST.__objc_selrefs: 0x400
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xdc0
-  __AUTH_CONST.__const: 0x79778
+  __AUTH_CONST.__auth_got: 0xdd0
+  __AUTH_CONST.__const: 0x79f38
   __AUTH_CONST.__objc_const: 0x14f0
   __AUTH.__objc_data: 0x500
   __AUTH.__data: 0x3558
-  __DATA.__data: 0x9168
-  __DATA.__bss: 0x8db00
-  __DATA.__common: 0x40
+  __DATA.__data: 0x92a8
+  __DATA.__bss: 0x8ea00
+  __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x508
   __DATA_DIRTY.__data: 0x1f20
   __DATA_DIRTY.__common: 0x88

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
+  - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C8B6BB67-8FA1-3BEF-B2A8-B7CA9E88B390
-  Functions: 31233
-  Symbols:   241
-  CStrings:  2815
+  UUID: A6B4E7E7-1F3E-3C97-8CFF-B09CE95C9026
+  Functions: 31407
+  Symbols:   244
+  CStrings:  2828
 
Symbols:
+ _OBJC_CLASS_$__PASDeviceState
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
CStrings:
+ "CatalogClient: assetDeliveryReady %{bool}d"
+ "InstructFMApiThirdPartyCompileDraft"
+ "Invalid configuration for com.apple.fm.language.instruct_3b.fm_api_third_party_compile.draft: "
+ "LLMCompileDraftBundle draftModel is wrong type"
+ "LLMCompileDraftBundle missing 'draft_model' key from json: "
+ "LLMCompileDraftBundle missing LLMDraftModel with id "
+ "Not posting generative experiences ready notification because asset delivery is not ready"
+ "Not posting generative experiences ready notification because the device is not class c unlocked"
+ "Process.valueForEntitlement could not cast value to expected output type"
+ "Process.valueForEntitlement could not create security task"
+ "Process.valueForEntitlement did not find value for entitlement: %s"
+ "TokenGeneration.LLMCompileDraft"
+ "com.apple.fm.language.instruct_3b.fm_api_third_party_compile.draft"
+ "isClassCLocked"
- "com.apple.coremotion.fitness"

```
