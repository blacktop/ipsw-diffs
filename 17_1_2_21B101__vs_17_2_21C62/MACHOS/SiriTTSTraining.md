## SiriTTSTraining

> `/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTraining`

```diff

-3301.5.1.0.0
-  __TEXT.__text: 0x305874
+3302.6.1.0.0
+  __TEXT.__text: 0x305ab4
   __TEXT.__auth_stubs: 0x6840
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x590
+  __TEXT.__objc_methlist: 0x5b8
   __TEXT.__const: 0x15a08
   __TEXT.__gcc_except_tab: 0x2d9a8
-  __TEXT.__cstring: 0x25fdd
-  __TEXT.__oslogstring: 0x13b7
+  __TEXT.__cstring: 0x25ffd
+  __TEXT.__oslogstring: 0x13ce
   __TEXT.__swift5_typeref: 0x111
   __TEXT.__constg_swiftt: 0xe4
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x10ff8
+  __TEXT.__unwind_info: 0x11000
   __TEXT.__eh_frame: 0x17c
-  __TEXT.__objc_classname: 0x11d
-  __TEXT.__objc_methname: 0x11f0
-  __TEXT.__objc_methtype: 0x842
-  __TEXT.__objc_stubs: 0x940
+  __TEXT.__objc_classname: 0x11e
+  __TEXT.__objc_methname: 0x1252
+  __TEXT.__objc_methtype: 0x879
+  __TEXT.__objc_stubs: 0x960
   __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd80
-  __DATA_CONST.__objc_selrefs: 0x4f8
+  __DATA_CONST.__objc_const: 0xdd0
+  __DATA_CONST.__objc_selrefs: 0x510
   __AUTH_CONST.__objc_const: 0x2d0
-  __AUTH_CONST.__cfstring: 0x3a0
+  __AUTH_CONST.__cfstring: 0x3c0
   __AUTH_CONST.__const: 0x4d90
   __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__auth_got: 0xfa0

   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x88
   __DATA.__objc_superrefs: 0x20
-  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x880
   __DATA.__bss: 0x840
   __DATA.__common: 0x20

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12295
-  Symbols:   19896
-  CStrings:  5266
+  Functions: 12300
+  Symbols:   19903
+  CStrings:  5274
 
Symbols:
+ -[SiriTTSTrainerSession getCurrentAssetVersion:name:reply:]
+ -[SiriTTSTrainerTask assetVersion]
+ -[SiriTTSTrainerTask setAssetVersion:]
+ OBJC_IVAR_$_SiriTTSTrainerTask._assetVersion
+ __29-[SiriTTSTrainerSession init]_block_invoke.101
+ __29-[SiriTTSTrainerSession init]_block_invoke.101.cold.1
+ __48-[SiriTTSTrainerSession uninstallTrainingAsset:]_block_invoke.122
+ __59-[SiriTTSTrainerSession getCurrentAssetVersion:name:reply:]_block_invoke.cold.1
+ __66-[SiriTTSTrainerSession installTrainingAsset:progress:completion:]_block_invoke.118
+ __70-[SiriTTSTrainerSession installedTrainingAssetsForLanguage:name:type:]_block_invoke.116
+ __72-[SiriTTSTrainerSession installableTrainingAssetsForLanguage:name:type:]_block_invoke.112
+ ___59-[SiriTTSTrainerSession getCurrentAssetVersion:name:reply:]_block_invoke
+ __block_literal_global.100
+ __block_literal_global.103
+ __block_literal_global.111
+ __block_literal_global.115
+ __block_literal_global.121
+ __block_literal_global.124
+ _objc_msgSend$getCurrentAssetVersion:name:reply:
- __29-[SiriTTSTrainerSession init]_block_invoke.99
- __29-[SiriTTSTrainerSession init]_block_invoke.99.cold.1
- __48-[SiriTTSTrainerSession uninstallTrainingAsset:]_block_invoke.120
- __66-[SiriTTSTrainerSession installTrainingAsset:progress:completion:]_block_invoke.116
- __70-[SiriTTSTrainerSession installedTrainingAssetsForLanguage:name:type:]_block_invoke.114
- __72-[SiriTTSTrainerSession installableTrainingAssetsForLanguage:name:type:]_block_invoke.110
- __block_literal_global.101
- __block_literal_global.109
- __block_literal_global.113
- __block_literal_global.119
- __block_literal_global.122
- __block_literal_global.98
CStrings:
+ "\x16a\x11"
+ "Tq,N,V_assetVersion"
+ "Vv40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\"q>32"
+ "_assetVersion"
+ "assetVersion"
+ "getCurrentAssetVersion"
+ "getCurrentAssetVersion:name:reply:"
+ "id: %@, language: %@, name: %@, trainingPath: %@, dataPath: %@, inferencePath: %@, taskStatus: %ld, trainingStatus: %ld, retryTimes: %ld, currentTaskStatusProgressValue: %ld, totalTaskStatusProgressValue: %ld, normalizedProgressValue: %f, assetVersion: %ld"
+ "setAssetVersion:"
- "\x16b"
- "id: %@, language: %@, name: %@, trainingPath: %@, dataPath: %@, inferencePath: %@, taskStatus: %ld, trainingStatus: %ld, retryTimes: %ld, currentTaskStatusProgressValue: %ld, totalTaskStatusProgressValue: %ld, normalizedProgressValue: %f"

```
