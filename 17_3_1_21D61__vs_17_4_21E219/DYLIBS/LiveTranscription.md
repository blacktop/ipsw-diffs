## LiveTranscription

> `/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription`

```diff

-452.0.6.0.0
-  __TEXT.__text: 0xfd1c
-  __TEXT.__auth_stubs: 0x700
+452.10.0.0.0
+  __TEXT.__text: 0xff54
+  __TEXT.__auth_stubs: 0x740
   __TEXT.__objc_methlist: 0xf80
   __TEXT.__const: 0x242
   __TEXT.__cstring: 0x7ca

   __TEXT.__swift5_fieldmd: 0xc0
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x4d4
+  __TEXT.__unwind_info: 0x4f4
   __TEXT.__objc_classname: 0x250
-  __TEXT.__objc_methname: 0x3374
+  __TEXT.__objc_methname: 0x3384
   __TEXT.__objc_methtype: 0xba6
   __TEXT.__objc_stubs: 0x2960
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x448
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1de8
   __DATA_CONST.__objc_selrefs: 0xc98
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__const: 0x2e0
   __AUTH_CONST.__objc_const: 0x670
   __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x1d8
-  __DATA.__objc_superrefs: 0x68
   __DATA.__objc_ivar: 0x160
-  __DATA.__data: 0x440
+  __DATA.__data: 0x450
   __DATA.__bss: 0x2d0
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x38

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BC1CB378-CBFC-3F25-8842-B0E7A4317A5D
-  Functions: 572
-  Symbols:   1830
-  CStrings:  984
+  UUID: 1E9E2CFF-D1E0-3FEE-9926-ED4152D54719
+  Functions: 579
+  Symbols:   1838
+  CStrings:  985
 
Symbols:
+ ___37-[AXLTClient pingServiceWithHandler:]_block_invoke.288
+ ___37-[AXLTClient pingServiceWithHandler:]_block_invoke.288.cold.1
+ ___41-[AXLTClient initializeServiceConnection]_block_invoke.266
+ ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.251
+ ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.245
+ ___54-[AXLTClient stopTranscribing:targetPID:client:error:]_block_invoke.286
+ ___54-[AXLTClient stopTranscribing:targetPID:client:error:]_block_invoke.286.cold.1
+ ___54-[AXLTClient stopTranscribing:targetPID:client:error:]_block_invoke.286.cold.2
+ ___54-[AXLTClient stopTranscribing:targetPID:client:error:]_block_invoke.287
+ ___54-[AXLTClient stopTranscribing:targetPID:client:error:]_block_invoke.287.cold.1
+ ___54-[AXLTClient stopTranscribing:targetPID:client:error:]_block_invoke.287.cold.2
+ ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke.251
+ ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke_2.252
+ ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.278
+ ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.278.cold.1
+ ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.278.cold.2
+ ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.280
+ ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.280.cold.1
+ ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.280.cold.2
+ ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.282
+ ___block_literal_global.240
+ ___block_literal_global.285
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ _free
+ _malloc
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
- ___37-[AXLTClient pingServiceWithHandler:]_block_invoke.264
- ___37-[AXLTClient pingServiceWithHandler:]_block_invoke.264.cold.1
- ___41-[AXLTClient initializeServiceConnection]_block_invoke.242
- ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.227
- ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.221
- ___54-[AXLTClient stopTranscribing:targetPID:client:error:]_block_invoke.262
- ___54-[AXLTClient stopTranscribing:targetPID:client:error:]_block_invoke.262.cold.1
- ___54-[AXLTClient stopTranscribing:targetPID:client:error:]_block_invoke.262.cold.2
- ___54-[AXLTClient stopTranscribing:targetPID:client:error:]_block_invoke.263
- ___54-[AXLTClient stopTranscribing:targetPID:client:error:]_block_invoke.263.cold.1
- ___54-[AXLTClient stopTranscribing:targetPID:client:error:]_block_invoke.263.cold.2
- ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke.227
- ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke_2.228
- ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.254
- ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.254.cold.1
- ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.254.cold.2
- ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.256
- ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.256.cold.1
- ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.256.cold.2
- ___69-[AXLTClient startTranscribing:targetPID:client:callbackBlock:error:]_block_invoke.258
- ___block_literal_global.216
- ___block_literal_global.261
CStrings:
+ "T@\"NSString\",?,R,C"

```
