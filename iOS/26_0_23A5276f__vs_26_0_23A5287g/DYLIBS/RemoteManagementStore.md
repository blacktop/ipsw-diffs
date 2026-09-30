## RemoteManagementStore

> `/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore`

```diff

-579.0.0.0.0
-  __TEXT.__text: 0x3a260
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x22d0
+580.0.0.0.0
+  __TEXT.__text: 0x3a8d0
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__objc_methlist: 0x2360
   __TEXT.__const: 0x3fc
   __TEXT.__cstring: 0x1126
-  __TEXT.__oslogstring: 0x3397
+  __TEXT.__oslogstring: 0x33b7
   __TEXT.__gcc_except_tab: 0x3c0
   __TEXT.__swift5_typeref: 0x2bf
   __TEXT.__swift5_fieldmd: 0xa8

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x8
-  __TEXT.__swift5_capture: 0x108
+  __TEXT.__swift5_capture: 0x118
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0xe70
-  __TEXT.__eh_frame: 0xac0
+  __TEXT.__unwind_info: 0xe88
+  __TEXT.__eh_frame: 0xae8
   __TEXT.__objc_classname: 0x68d
-  __TEXT.__objc_methname: 0x6db0
-  __TEXT.__objc_methtype: 0x1654
-  __TEXT.__objc_stubs: 0x4200
+  __TEXT.__objc_methname: 0x6f69
+  __TEXT.__objc_methtype: 0x1679
+  __TEXT.__objc_stubs: 0x4380
   __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0xee0
+  __DATA_CONST.__const: 0xf30
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14b8
+  __DATA_CONST.__objc_selrefs: 0x1520
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x658
-  __AUTH_CONST.__const: 0x6e8
+  __AUTH_CONST.__auth_got: 0x660
+  __AUTH_CONST.__const: 0x710
   __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x34b8
+  __AUTH_CONST.__objc_const: 0x35d8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x98
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x18c
+  __DATA.__objc_ivar: 0x1a4
   __DATA.__data: 0x5d0
   __DATA.__bss: 0x540
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3EBA079F-939F-3631-8F0B-2F0CC33C1188
-  Functions: 1301
-  Symbols:   3820
-  CStrings:  1675
+  UUID: 6FA397CC-592D-3A5D-9488-6FA79F1C3780
+  Functions: 1316
+  Symbols:   3864
+  CStrings:  1704
 
Symbols:
+ -[RMConfigurationMultipleApplicator _endProcessingWithSuccess:configurations:storesByIdentifier:scope:completionHandler:]
+ -[RMConfigurationMultipleApplicator installFail]
+ -[RMConfigurationMultipleApplicator installSuccess]
+ -[RMConfigurationMultipleApplicator removeFail]
+ -[RMConfigurationMultipleApplicator removeSuccess]
+ -[RMConfigurationMultipleApplicator retryOnce]
+ -[RMConfigurationMultipleApplicator retrying]
+ -[RMConfigurationMultipleApplicator setInstallFail:]
+ -[RMConfigurationMultipleApplicator setInstallSuccess:]
+ -[RMConfigurationMultipleApplicator setRemoveFail:]
+ -[RMConfigurationMultipleApplicator setRemoveSuccess:]
+ -[RMConfigurationMultipleApplicator setRetryOnce:]
+ -[RMConfigurationMultipleApplicator setRetrying:]
+ _OBJC_IVAR_$_RMConfigurationMultipleApplicator._installFail
+ _OBJC_IVAR_$_RMConfigurationMultipleApplicator._installSuccess
+ _OBJC_IVAR_$_RMConfigurationMultipleApplicator._removeFail
+ _OBJC_IVAR_$_RMConfigurationMultipleApplicator._removeSuccess
+ _OBJC_IVAR_$_RMConfigurationMultipleApplicator._retryOnce
+ _OBJC_IVAR_$_RMConfigurationMultipleApplicator._retrying
+ ___121-[RMConfigurationMultipleApplicator _endProcessingWithSuccess:configurations:storesByIdentifier:scope:completionHandler:]_block_invoke
+ ___121-[RMConfigurationMultipleApplicator _endProcessingWithSuccess:configurations:storesByIdentifier:scope:completionHandler:]_block_invoke.cold.1
+ ___block_descriptor_72_e8_32s40s48s56bs_e27_v24?0"NSSet"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ _block_copy_helper.20
+ _block_copy_helper.34
+ _block_copy_helper.37
+ _block_copy_helper.62
+ _block_copy_helper.65
+ _block_copy_helper.80
+ _block_copy_helper.83
+ _block_copy_helper.89
+ _block_copy_helper.93
+ _block_descriptor.22
+ _block_descriptor.36
+ _block_descriptor.39
+ _block_descriptor.64
+ _block_descriptor.67
+ _block_descriptor.82
+ _block_descriptor.85
+ _block_descriptor.91
+ _block_descriptor.95
+ _block_destroy_helper.21
+ _block_destroy_helper.35
+ _block_destroy_helper.38
+ _block_destroy_helper.63
+ _block_destroy_helper.66
+ _block_destroy_helper.81
+ _block_destroy_helper.84
+ _block_destroy_helper.90
+ _block_destroy_helper.94
+ _objc_msgSend$_endProcessingWithSuccess:configurations:storesByIdentifier:scope:completionHandler:
+ _objc_msgSend$installFail
+ _objc_msgSend$installSuccess
+ _objc_msgSend$removeFail
+ _objc_msgSend$removeSuccess
+ _objc_msgSend$retryOnce
+ _objc_msgSend$retrying
+ _objc_msgSend$setInstallFail:
+ _objc_msgSend$setInstallSuccess:
+ _objc_msgSend$setRemoveFail:
+ _objc_msgSend$setRemoveSuccess:
+ _objc_msgSend$setRetrying:
- -[RMConfigurationMultipleApplicator _endProcessingWithSuccess:scope:completionHandler:]
- ___87-[RMConfigurationMultipleApplicator _endProcessingWithSuccess:scope:completionHandler:]_block_invoke
- ___87-[RMConfigurationMultipleApplicator _endProcessingWithSuccess:scope:completionHandler:]_block_invoke.cold.1
- _block_copy_helper.15
- _block_copy_helper.29
- _block_copy_helper.32
- _block_copy_helper.57
- _block_copy_helper.60
- _block_copy_helper.75
- _block_copy_helper.78
- _block_copy_helper.84
- _block_copy_helper.88
- _block_descriptor.17
- _block_descriptor.31
- _block_descriptor.34
- _block_descriptor.59
- _block_descriptor.62
- _block_descriptor.77
- _block_descriptor.80
- _block_descriptor.86
- _block_descriptor.90
- _block_destroy_helper.16
- _block_destroy_helper.30
- _block_destroy_helper.33
- _block_destroy_helper.58
- _block_destroy_helper.61
- _block_destroy_helper.76
- _block_destroy_helper.79
- _block_destroy_helper.85
- _block_destroy_helper.89
CStrings:
+ "Q"
+ "Retrying applicator sync operation."
+ "TB,N,V_retryOnce"
+ "TB,N,V_retrying"
+ "TQ,N,V_installFail"
+ "TQ,N,V_installSuccess"
+ "TQ,N,V_removeFail"
+ "TQ,N,V_removeSuccess"
+ "_endProcessingWithSuccess:configurations:storesByIdentifier:scope:completionHandler:"
+ "_installFail"
+ "_installSuccess"
+ "_removeFail"
+ "_removeSuccess"
+ "_retryOnce"
+ "_retrying"
+ "installFail"
+ "installSuccess"
+ "removeFail"
+ "removeSuccess"
+ "retryOnce"
+ "retrying"
+ "setInstallFail:"
+ "setInstallSuccess:"
+ "setRemoveFail:"
+ "setRemoveSuccess:"
+ "setRetryOnce:"
+ "setRetrying:"
+ "v24@0:8Q16"
+ "v52@0:8B16@20@28q36@?44"

```
