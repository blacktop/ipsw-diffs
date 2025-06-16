## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-3437.120.20.0.0
-  __TEXT.__text: 0x2f1af4
+3437.140.4.0.0
+  __TEXT.__text: 0x2f1cb0
   __TEXT.__auth_stubs: 0x1b60
   __TEXT.__objc_methlist: 0x1909c
   __TEXT.__const: 0x4d8
-  __TEXT.__cstring: 0x7a493
-  __TEXT.__oslogstring: 0x3aeaf
-  __TEXT.__gcc_except_tab: 0x19a80
+  __TEXT.__cstring: 0x7a45d
+  __TEXT.__oslogstring: 0x3aec5
+  __TEXT.__gcc_except_tab: 0x19ab0
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x9998
+  __TEXT.__unwind_info: 0x99a0
   __TEXT.__objc_classname: 0x269f
-  __TEXT.__objc_methname: 0x411de
+  __TEXT.__objc_methname: 0x411f9
   __TEXT.__objc_methtype: 0x882e
   __TEXT.__objc_stubs: 0x2cae0
   __DATA_CONST.__got: 0x16f8
-  __DATA_CONST.__const: 0x8e10
+  __DATA_CONST.__const: 0x8e38
   __DATA_CONST.__objc_classlist: 0x988
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x270

   __AUTH_CONST.__auth_got: 0xdc0
   __AUTH_CONST.__const: 0x2958
   __AUTH_CONST.__cfstring: 0x22040
-  __AUTH_CONST.__objc_const: 0x3b298
+  __AUTH_CONST.__objc_const: 0x3b2b8
   __AUTH_CONST.__objc_intobj: 0xb40
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH.__objc_data: 0x2490
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1ec8
+  __DATA.__objc_ivar: 0x1ecc
   __DATA.__data: 0x2630
   __DATA.__bss: 0x240
   __DATA_DIRTY.__objc_data: 0x3ac0

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6E65F3BF-C098-3C0F-A052-E0B2A0C8D1EE
-  Functions: 13121
-  Symbols:   42898
-  CStrings:  26902
+  UUID: 9667FA27-6B3B-3C2A-B479-BDE42CFF60A1
+  Functions: 13123
+  Symbols:   42906
+  CStrings:  26903
 
Symbols:
+ -[BRCSharingAcceptFlowOperation _isAccountRestricted_step].cold.3
+ -[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively_step].cold.3
+ -[BRCStageRegistry _purgeAllUploadsWithIncludeActiveItems:].cold.2
+ -[BRCStageRegistry markUploadActiveForStageID:]
+ -[BRCStageRegistry(FPFSAdditions) cloneFileURL:toUploadStageID:liveStageFilename:error:]
+ GCC_except_table150
+ GCC_except_table168
+ GCC_except_table175
+ GCC_except_table204
+ GCC_except_table207
+ _OBJC_IVAR_$_BRCSharingAcceptFlowOperation._appBundleID
+ ___43-[BRCStageRegistry _removeUnusedXattrBlobs]_block_invoke.128
+ ___88-[BRCStageRegistry(FPFSAdditions) cloneFileURL:toUploadStageID:liveStageFilename:error:]_block_invoke
+ ___block_descriptor_40_e8_32s_e34_B32?0"NSString"8"NSString"16Q24ls32l8
+ ___block_descriptor_41_e8_32s_e34_B32?0"NSString"8"NSString"16Q24ls32l8
+ ___block_descriptor_64_e8_32s40s48r_e23_B16?0"PQLConnection"8lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e8_i12?0i8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48bs56r64r72r_e47_v24?0"NSFileProviderItemVersion"8"NSError"16lr56l8s32l8s40l8r64l8r72l8s48l8
+ ___block_literal_global.127
+ _objc_msgSend$cloneFileURL:toUploadStageID:liveStageFilename:error:
+ _objc_msgSend$markUploadActiveForStageID:
- -[BRCStageRegistry _garbageCollectUploads]
- -[BRCStageRegistry(FPFSAdditions) cloneURLToLiveStage:liveStageFilename:error:]
- GCC_except_table170
- GCC_except_table174
- GCC_except_table202
- ___43-[BRCStageRegistry _removeUnusedXattrBlobs]_block_invoke.127
- ___65-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke.cold.1
- ___79-[BRCStageRegistry(FPFSAdditions) cloneURLToLiveStage:liveStageFilename:error:]_block_invoke
- ___block_descriptor_40_e8_32s_e27_B24?0"BRFileObjectID"8Q16ls32l8
- ___block_descriptor_57_e8_32s40s48r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16ls32l8s40l8r48l8
- ___block_descriptor_65_e8_32s40s48r56r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16lr48l8s32l8s40l8r56l8
- ___block_descriptor_80_e8_32s40bs48r56r64r72r_e47_v24?0"NSFileProviderItemVersion"8"NSError"16lr48l8r56l8s32l8r64l8r72l8s40l8
- _objc_msgSend$_garbageCollectUploads
- _objc_msgSend$cloneURLToLiveStage:liveStageFilename:error:
CStrings:
+ "-[BRCStageRegistry(FPFSAdditions) cloneFileURL:toUploadStageID:liveStageFilename:error:]"
+ "-[BRCStageRegistry(FPFSAdditions) cloneFileURL:toUploadStageID:liveStageFilename:error:]_block_invoke"
+ "B32@?0@\"NSString\"8@\"NSString\"16Q24"
+ "[CRIT] Assertion failed: _appBundleID%@"
+ "[DEBUG] Purged %lld bytes%@"
+ "_appBundleID"
+ "cloneFileURL:toUploadStageID:liveStageFilename:error:"
+ "cu-%@"
+ "markUploadActiveForStageID:"
- "-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke"
- "-[BRCStageRegistry(FPFSAdditions) cloneURLToLiveStage:liveStageFilename:error:]"
- "-[BRCStageRegistry(FPFSAdditions) cloneURLToLiveStage:liveStageFilename:error:]_block_invoke"
- "B24@?0@\"BRFileObjectID\"8Q16"
- "[DEBUG] removing staged file for upload: %@%@"
- "_garbageCollectUploads"
- "cloneURLToLiveStage:liveStageFilename:error:"
- "cu_%@"

```
