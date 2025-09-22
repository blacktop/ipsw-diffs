## AudioAccessoryAssetManagement

> `/System/Library/PrivateFrameworks/AudioAccessoryAssetManagement.framework/AudioAccessoryAssetManagement`

```diff

-30.59.1.9.0
-  __TEXT.__text: 0x1e04
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_methlist: 0x42c
+31.5.2.1.2
+  __TEXT.__text: 0x2354
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_methlist: 0x458
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0xac7
-  __TEXT.__unwind_info: 0x110
-  __TEXT.__objc_classname: 0xf2
-  __TEXT.__objc_methname: 0xd52
-  __TEXT.__objc_methtype: 0x6b4
-  __TEXT.__objc_stubs: 0x4a0
-  __DATA_CONST.__got: 0x58
+  __TEXT.__cstring: 0xcd3
+  __TEXT.__unwind_info: 0x128
+  __TEXT.__objc_classname: 0xf3
+  __TEXT.__objc_methname: 0xebe
+  __TEXT.__objc_methtype: 0x6e1
+  __TEXT.__objc_stubs: 0x600
+  __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e0
+  __DATA_CONST.__objc_selrefs: 0x340
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x120
+  __AUTH_CONST.__auth_got: 0x130
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x548
-  __DATA.__objc_ivar: 0x34
+  __AUTH_CONST.__cfstring: 0x160
+  __AUTH_CONST.__objc_const: 0x590
+  __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x70

   - /System/Library/Frameworks/Translation.framework/Translation
   - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D69481AD-D63A-3610-ACB7-9821DB51E051
-  Functions: 72
-  Symbols:   308
-  CStrings:  242
+  UUID: 26A1A2D8-D3D1-31B8-9697-60069BC19636
+  Functions: 81
+  Symbols:   348
+  CStrings:  276
 
Symbols:
+ -[AudioAccessoryAssetManagementClient _invalidateXPCServiceAssertion]
+ -[AudioAccessoryAssetManagementClient _takeXPCServiceAssertion]
+ -[AudioAccessoryAssetManagementClient _takeXPCServiceAssertion].cold.1
+ -[AudioAccessoryAssetManagementClient _takeXPCServiceAssertion].cold.2
+ -[AudioAccessoryAssetManagementClient _takeXPCServiceAssertion].cold.3
+ -[AudioAccessoryAssetManagementClient _takeXPCServiceAssertion].cold.4
+ -[AudioAccessoryAssetManagementClient _takeXPCServiceAssertion].cold.5
+ -[AudioAccessoryAssetManagementClient _takeXPCServiceAssertion].cold.6
+ -[AudioAccessoryAssetManagementClient pidOfDownloadTranslationAssetsXPCService:]
+ -[AudioAccessoryAssetManagementClient pidOfDownloadTranslationAssetsXPCService:].cold.1
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSProcessHandle
+ _OBJC_CLASS_$_RBSProcessIdentifier
+ _OBJC_CLASS_$_RBSTarget
+ _OBJC_IVAR_$_AudioAccessoryAssetManagementClient._downloadTranslationAssetsPid
+ _OBJC_IVAR_$_AudioAccessoryAssetManagementClient._processAssertion
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_literal_global.156
+ ___block_literal_global.42
+ ___block_literal_global.47
+ ___block_literal_global.50
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _objc_msgSend$_invalidateXPCServiceAssertion
+ _objc_msgSend$_takeXPCServiceAssertion
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$downloadTranslationAssets:localeIdentifiers:useCellular:showDownloadCompleteNotification:bundleIdentifier:completion:
+ _objc_msgSend$handleForIdentifier:error:
+ _objc_msgSend$identifierWithPid:
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_msgSend$isValid
+ _objc_msgSend$mainBundle
+ _objc_msgSend$targetWithProcessIdentifier:
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
- ___121-[AudioAccessoryAssetManagementClient downloadTranslationAssets:useCellular:showDownloadCompleteNotification:completion:]_block_invoke_4
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
- ___block_literal_global.130
- ___block_literal_global.18
- ___block_literal_global.23
- ___block_literal_global.26
- _dispatch_after
- _dispatch_time
- _objc_msgSend$_killConnection:
- _objc_msgSend$downloadTranslationAssets:localeIdentifiers:useCellular:showDownloadCompleteNotification:completion:
CStrings:
+ "-[AudioAccessoryAssetManagementClient _takeXPCServiceAssertion]"
+ "-[AudioAccessoryAssetManagementClient pidOfDownloadTranslationAssetsXPCService:]"
+ "@\"RBSAssertion\""
+ "Assertion acquired successfully"
+ "AudioAccessoryAssetManagement"
+ "Failed acquiring the assertion with error %@"
+ "Giving runtime to XPCService"
+ "_downloadTranslationAssetsPid"
+ "_downloadTranslationAssetsPid is 0 returning"
+ "_invalidateXPCServiceAssertion"
+ "_processAssertion"
+ "_takeXPCServiceAssertion"
+ "acquireWithError:"
+ "arrayWithObjects:count:"
+ "attributeWithDomain:name:"
+ "bundleIdentifier"
+ "com.apple.audioAccessoryAssetManagement"
+ "downloadTranslationAssets:localeIdentifiers:useCellular:showDownloadCompleteNotification:bundleIdentifier:completion:"
+ "handleForIdentifier:error:"
+ "i"
+ "identifierWithPid:"
+ "initWithExplanation:target:attributes:"
+ "isValid"
+ "mainBundle"
+ "pidOfDownloadTranslationAssetsXPCService:"
+ "pidOfDownloadTranslationAssetsXPCService: %ld"
+ "processHandle is nil returning with error %@"
+ "processIdentifier is nil returning"
+ "target is nil returning"
+ "targetWithProcessIdentifier:"
+ "unknown"
+ "v20@0:8i16"
+ "v56@0:8@\"AudioAccessoryAssetManagementClient\"16@\"NSArray\"24B32B36@\"NSString\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24B32B36@40@?48"
- "_killConnection:"
- "downloadTranslationAssets:localeIdentifiers:useCellular:showDownloadCompleteNotification:completion:"
- "v48@0:8@\"AudioAccessoryAssetManagementClient\"16@\"NSArray\"24B32B36@?<v@?@\"NSError\">40"
- "v48@0:8@16@24B32B36@?40"

```
