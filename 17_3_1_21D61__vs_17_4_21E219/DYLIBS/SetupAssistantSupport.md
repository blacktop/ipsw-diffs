## SetupAssistantSupport

> `/System/Library/PrivateFrameworks/SetupAssistantSupport.framework/SetupAssistantSupport`

```diff

-453.0.0.0.0
-  __TEXT.__text: 0x11dd0
+454.0.0.0.0
+  __TEXT.__text: 0x121c4
   __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x143c
+  __TEXT.__objc_methlist: 0x148c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0xd2d
+  __TEXT.__cstring: 0xd45
   __TEXT.__oslogstring: 0x9c2
   __TEXT.__gcc_except_tab: 0x210
   __TEXT.__dlopen_cstrs: 0x5ed
   __TEXT.__unwind_info: 0x428
   __TEXT.__objc_classname: 0x2d7
-  __TEXT.__objc_methname: 0x3c33
-  __TEXT.__objc_methtype: 0x654
+  __TEXT.__objc_methname: 0x3d1f
+  __TEXT.__objc_methtype: 0x66f
   __TEXT.__objc_stubs: 0x3100
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0x820
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2398
-  __DATA_CONST.__objc_selrefs: 0xec8
-  __AUTH_CONST.__cfstring: 0xfa0
+  __DATA_CONST.__objc_const: 0x2418
+  __DATA_CONST.__objc_selrefs: 0xef0
+  __DATA_CONST.__objc_classrefs: 0x208
+  __DATA_CONST.__objc_superrefs: 0x50
+  __AUTH_CONST.__cfstring: 0xfc0
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x3b8
-  __DATA.__objc_classrefs: 0x208
-  __DATA.__objc_superrefs: 0x50
-  __DATA.__objc_ivar: 0x1a4
+  __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x140
   __DATA_DIRTY.__const: 0x40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 537
-  Symbols:   2147
-  CStrings:  1077
+  Functions: 544
+  Symbols:   2163
+  CStrings:  1087
 
Symbols:
+ -[SASExpressSettings hasProductVersion]
+ -[SASExpressSettings hasSiriVoiceTriggerEnabled]
+ -[SASExpressSettings productVersion]
+ -[SASExpressSettings setHasSiriVoiceTriggerEnabled:]
+ -[SASExpressSettings setProductVersion:]
+ -[SASExpressSettings setSiriVoiceTriggerEnabled:]
+ -[SASExpressSettings siriVoiceTriggerEnabled]
+ OBJC_IVAR_$_SASExpressSettings._productVersion
+ OBJC_IVAR_$_SASExpressSettings._siriVoiceTriggerEnabled
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.288
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.288.cold.1
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.289
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.289.cold.1
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.293
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.293.cold.1
+ ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.317
+ ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.318
+ ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.318.cold.1
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.264
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.264.cold.1
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.265
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.265.cold.1
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.269
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.269.cold.1
- ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.293
- ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.294
- ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.294.cold.1
CStrings:
+ "\x01\x12\x15\x12"
+ "T@\"NSString\",&,N,V_productVersion"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_siriVoiceTriggerEnabled"
+ "_siriVoiceTriggerEnabled"
+ "hasProductVersion"
+ "hasSiriVoiceTriggerEnabled"
+ "setHasSiriVoiceTriggerEnabled:"
+ "setSiriVoiceTriggerEnabled:"
+ "siriVoiceTriggerEnabled"
+ "{?=\"appearanceMode\"b1\"displayZoomOption\"b1\"appAnalyticsOptIn\"b1\"deviceAnalyticsOptIn\"b1\"fileVaultEnabled\"b1\"findMyOptIn\"b1\"locationServicesOptIn\"b1\"screenTimeEnabled\"b1\"siriDataSharingOptIn\"b1\"siriOptIn\"b1\"siriVoiceTriggerEnabled\"b1\"softwareUpdateAutoDownloadEnabled\"b1\"softwareUpdateAutoUpdateEnabled\"b1\"unlockWithWatchEnabled\"b1}"
- "\x01\x12\x14\x12"
- "{?=\"appearanceMode\"b1\"displayZoomOption\"b1\"appAnalyticsOptIn\"b1\"deviceAnalyticsOptIn\"b1\"fileVaultEnabled\"b1\"findMyOptIn\"b1\"locationServicesOptIn\"b1\"screenTimeEnabled\"b1\"siriDataSharingOptIn\"b1\"siriOptIn\"b1\"softwareUpdateAutoDownloadEnabled\"b1\"softwareUpdateAutoUpdateEnabled\"b1\"unlockWithWatchEnabled\"b1}"

```
