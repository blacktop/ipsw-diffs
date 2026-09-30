## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2171.120.44.0.1
-  __TEXT.__text: 0x9fcd8
+2171.140.7.0.0
+  __TEXT.__text: 0xa0340
   __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x76cc
+  __TEXT.__objc_methlist: 0x76ec
   __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x1485d
-  __TEXT.__oslogstring: 0xb941
+  __TEXT.__cstring: 0x148ce
+  __TEXT.__oslogstring: 0xba40
   __TEXT.__gcc_except_tab: 0x750
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x16e0
-  __TEXT.__objc_classname: 0x700
-  __TEXT.__objc_methname: 0x14c53
-  __TEXT.__objc_methtype: 0xf66
-  __TEXT.__objc_stubs: 0xe3a0
-  __DATA_CONST.__got: 0x888
-  __DATA_CONST.__const: 0x2260
+  __TEXT.__unwind_info: 0x16e8
+  __TEXT.__objc_classname: 0x701
+  __TEXT.__objc_methname: 0x14cd5
+  __TEXT.__objc_methtype: 0xf79
+  __TEXT.__objc_stubs: 0xe3e0
+  __DATA_CONST.__got: 0x890
+  __DATA_CONST.__const: 0x2268
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4210
+  __DATA_CONST.__objc_selrefs: 0x4228
   __DATA_CONST.__objc_superrefs: 0x1c0
-  __DATA_CONST.__objc_arraydata: 0xa8
+  __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x460
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x12340
-  __AUTH_CONST.__objc_const: 0xa190
-  __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__cfstring: 0x12420
+  __AUTH_CONST.__objc_const: 0xa1c0
+  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x944
+  __DATA.__objc_ivar: 0x948
   __DATA.__data: 0x360
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0xc80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E2545C7-0D53-3729-A1D9-5B597A1AFE9E
-  Functions: 2936
-  Symbols:   9947
-  CStrings:  8690
+  UUID: 828F47C8-0EC2-38C9-8E96-339468F7CA57
+  Functions: 2939
+  Symbols:   9958
+  CStrings:  8713
 
Symbols:
+ +[MAAutoAsset(SUCoreBorderMAAutoAsset) _generateSimulatedResults:bytes:huge:]
+ -[SUCoreDescriptor preSUStagingMaxSize]
+ -[SUCoreDescriptor setPreSUStagingMaxSize:]
+ GCC_except_table70
+ GCC_except_table77
+ _KSUAssetPreSUStagingMaxSizeKey
+ _OBJC_IVAR_$_SUCoreDescriptor._preSUStagingMaxSize
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1067
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1071
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1078
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1128
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1129
+ _kMobileSoftwareUpdatePreSUStagingMaxSizeKey
+ _objc_msgSend$_generateSimulatedResults:bytes:huge:
+ _objc_msgSend$preSUStagingMaxSize
- GCC_except_table69
- GCC_except_table76
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1064
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1068
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1075
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1125
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1126
CStrings:
+ "%{public}@ Ignore PSUS assets because required=%llu, optional=%llu, max=%llu"
+ "%{public}@ Using PSUS max size from preferences: %llu"
+ "%{public}@ [PreSUStaging] optional asset to stage: %{public}@"
+ "%{public}@ [PreSUStaging] required asset to stage: %{public}@"
+ "EncodedUIv2"
+ "PSUSMaxSize"
+ "PreSUStagingMaxSize"
+ "TQ,N,V_preSUStagingMaxSize"
+ "_generateSimulatedResults:bytes:huge:"
+ "_preSUStagingMaxSize"
+ "huge"
+ "optional-asset1-v2"
+ "optional-asset2-v2"
+ "preSUStagingMaxSize"
+ "required-asset1-v2"
+ "required-asset2-v2"
+ "setPreSUStagingMaxSize:"
+ "v36@0:8^@16^@24B32"
- "EncodedUI"

```
