## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-936.42.1.0.0
-  __TEXT.__text: 0x6c4d0
+936.60.10.0.0
+  __TEXT.__text: 0x6cb4c
   __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x5488
+  __TEXT.__objc_methlist: 0x54a0
   __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0x74c
-  __TEXT.__cstring: 0x12987
+  __TEXT.__gcc_except_tab: 0x76c
+  __TEXT.__cstring: 0x12a07
   __TEXT.__oslogstring: 0x4132
-  __TEXT.__unwind_info: 0x174c
+  __TEXT.__unwind_info: 0x1764
   __TEXT.__objc_classname: 0x5f1
-  __TEXT.__objc_methname: 0x102c3
-  __TEXT.__objc_methtype: 0x108f
-  __TEXT.__objc_stubs: 0x6c60
+  __TEXT.__objc_methname: 0x1032f
+  __TEXT.__objc_methtype: 0x10a3
+  __TEXT.__objc_stubs: 0x6ca0
   __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x1bb0
+  __DATA_CONST.__const: 0x1c00
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x6bc0
-  __DATA_CONST.__objc_selrefs: 0x2830
+  __DATA_CONST.__objc_selrefs: 0x2840
   __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__cfstring: 0xd600
+  __AUTH_CONST.__cfstring: 0xd640
   __AUTH_CONST.__const: 0x5e0
   __AUTH_CONST.__objc_const: 0x2010
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43C65C21-6D09-342E-9556-301FD130852E
-  Functions: 2589
-  Symbols:   7582
-  CStrings:  6148
+  UUID: 26EF245E-7FA8-3AAB-9BAB-1F9F55E8F56A
+  Functions: 2595
+  Symbols:   7596
+  CStrings:  6155
 
Symbols:
+ -[MAXpcManager progressCallbacksForAssetType:assetId:withPurpose:]
+ -[MAXpcManager restoreProgressCallbacks:assetType:assetId:withPurpose:]
+ GCC_except_table26
+ _ASNonUserInitiatedDownloadsAllowedForAssetType
+ _MANonUserInitiatedDownloadsAllowedForAssetType
+ __MAclientSendGetNonUserInitiatedDownloadsAllowedForAssetType
+ ___66-[MAXpcManager progressCallbacksForAssetType:assetId:withPurpose:]_block_invoke
+ ___71-[MAXpcManager restoreProgressCallbacks:assetType:assetId:withPurpose:]_block_invoke
+ ___Block_byref_object_copy_.933
+ ___Block_byref_object_dispose_.934
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80bs88r_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8s48l8s56l8s64l8s72l8r88l8s80l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8r80l8
+ ___block_literal_global.1052
+ ___block_literal_global.811
+ _objc_msgSend$progressCallbacksForAssetType:assetId:withPurpose:
+ _objc_msgSend$restoreProgressCallbacks:assetType:assetId:withPurpose:
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke_4
- ___Block_byref_object_copy_.930
- ___Block_byref_object_dispose_.931
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_80_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8
- ___block_descriptor_97_e8_32s40s48s56s64bs72r_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8s48l8s56l8r72l8s64l8
- ___block_literal_global.1049
- ___block_literal_global.808
CStrings:
+ "%@ mobileassetd connection interrupted - retrying sync message: %@"
+ "Re-registering %lu progress callbacks"
+ "_MAclientSendGetNonUserInitiatedDownloadsAllowedForAssetType"
+ "progressCallbacksForAssetType:assetId:withPurpose:"
+ "restoreProgressCallbacks:assetType:assetId:withPurpose:"
+ "v48@0:8@16@24@32@40"
- "MAGetNonUserInitiatedDownloadsAllowed"

```
