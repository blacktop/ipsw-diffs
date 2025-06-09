## AppleLockdownMode

> `/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode`

```diff

-71.120.2.0.0
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x4320
-  __TEXT_EXEC.__text: 0x13b94
+80.0.0.502.1
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0x46e2
+  __TEXT_EXEC.__text: 0x1467c
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc6
-  __DATA.__common: 0x40
+  __DATA.__common: 0x38
   __DATA.__bss: 0x19
   __DATA_CONST.__auth_got: 0x110
   __DATA_CONST.__got: 0x28

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x300
-  __DATA_CONST.__kalloc_var: 0x1400
-  UUID: B9525377-BD28-3C66-9B16-4E2C9FF08BAF
-  Functions: 196
-  Symbols:   619
-  CStrings:  469
+  __DATA_CONST.__kalloc_var: 0x14a0
+  UUID: 0D83FAEC-9346-3642-BF2D-EBCD308C641D
+  Functions: 205
+  Symbols:   628
+  CStrings:  490
 
Symbols:
+ DeallocCredentialList.kalloc_type_view_1935
+ DeserializeCredentialList.kalloc_type_view_1897
+ LibCall_ACMContextCreate.kalloc_type_view_49
+ LibCall_ACMContextLoadFromImage.kalloc_type_view_1479
+ LibCall_ACMContextLoadFromImage.kalloc_type_view_1540
+ Util_AllocCredential.kalloc_type_view_214
+ Util_AllocCredential.kalloc_type_view_220
+ Util_AllocCredential.kalloc_type_view_225
+ Util_AllocCredential.kalloc_type_view_230
+ Util_AllocCredential.kalloc_type_view_235
+ Util_AllocCredential.kalloc_type_view_240
+ Util_AllocCredential.kalloc_type_view_245
+ Util_AllocCredential.kalloc_type_view_251
+ Util_AllocCredential.kalloc_type_view_256
+ Util_AllocCredential.kalloc_type_view_261
+ Util_AllocCredential.kalloc_type_view_266
+ Util_AllocCredential.kalloc_type_view_271
+ Util_AllocCredential.kalloc_type_view_284
+ Util_AllocRequirement.kalloc_type_view_336
+ Util_AllocRequirement.kalloc_type_view_341
+ Util_AllocRequirement.kalloc_type_view_346
+ Util_AllocRequirement.kalloc_type_view_351
+ Util_AllocRequirement.kalloc_type_view_356
+ Util_AllocRequirement.kalloc_type_view_361
+ Util_AllocRequirement.kalloc_type_view_366
+ Util_AllocRequirement.kalloc_type_view_371
+ Util_AllocRequirement.kalloc_type_view_376
+ Util_AllocRequirement.kalloc_type_view_381
+ Util_AllocRequirement.kalloc_type_view_386
+ Util_AllocRequirement.kalloc_type_view_392
+ Util_AllocRequirement.kalloc_type_view_399
+ Util_AllocRequirement.kalloc_type_view_422
+ Util_AllocRequirement.kalloc_type_view_427
+ Util_AllocRequirement.kalloc_type_view_432
+ Util_AllocRequirement.kalloc_type_view_437
+ Util_AllocRequirement.kalloc_type_view_442
+ Util_DeallocCredential.kalloc_type_view_133
+ Util_DeallocCredential.kalloc_type_view_138
+ Util_DeallocCredential.kalloc_type_view_142
+ Util_DeallocCredential.kalloc_type_view_146
+ Util_DeallocCredential.kalloc_type_view_150
+ Util_DeallocCredential.kalloc_type_view_154
+ Util_DeallocCredential.kalloc_type_view_158
+ Util_DeallocCredential.kalloc_type_view_163
+ Util_DeallocCredential.kalloc_type_view_167
+ Util_DeallocCredential.kalloc_type_view_171
+ Util_DeallocCredential.kalloc_type_view_175
+ Util_DeallocCredential.kalloc_type_view_179
+ Util_DeallocCredential.kalloc_type_view_191
+ Util_DeallocRequirement.kalloc_type_view_545
+ Util_DeallocRequirement.kalloc_type_view_549
+ Util_DeallocRequirement.kalloc_type_view_553
+ Util_DeallocRequirement.kalloc_type_view_557
+ Util_DeallocRequirement.kalloc_type_view_561
+ Util_DeallocRequirement.kalloc_type_view_565
+ Util_DeallocRequirement.kalloc_type_view_569
+ Util_DeallocRequirement.kalloc_type_view_573
+ Util_DeallocRequirement.kalloc_type_view_577
+ Util_DeallocRequirement.kalloc_type_view_581
+ Util_DeallocRequirement.kalloc_type_view_585
+ Util_DeallocRequirement.kalloc_type_view_590
+ Util_DeallocRequirement.kalloc_type_view_600
+ Util_DeallocRequirement.kalloc_type_view_606
+ Util_DeallocRequirement.kalloc_type_view_612
+ Util_DeallocRequirement.kalloc_type_view_616
+ Util_DeallocRequirement.kalloc_type_view_620
+ Util_DeallocRequirement.kalloc_type_view_624
+ Util_DeallocRequirement.kalloc_type_view_628
+ _LibCall_ACMContextContainsCredentialTypeEx
+ _LibCall_ACMContextCopyData
+ _LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx
+ _LibSer_ACMDeserializeEnvironmentVariableType
+ _LibSer_ACMDeserializeSEPControlCode
+ _LibSer_GetSerializedContainsCredential_GetSize
+ _LibSer_GetSerializedContainsCredential_Serialize
+ _getRequirementDataSizeForVersion
+ deserializeParameters.kalloc_type_view_196
- DeallocCredentialList.kalloc_type_view_1816
- DeserializeCredentialList.kalloc_type_view_1778
- LibCall_ACMContextCreate.kalloc_type_view_50
- LibCall_ACMContextLoadFromImage.kalloc_type_view_1447
- LibCall_ACMContextLoadFromImage.kalloc_type_view_1508
- Util_AllocCredential.kalloc_type_view_211
- Util_AllocCredential.kalloc_type_view_216
- Util_AllocCredential.kalloc_type_view_221
- Util_AllocCredential.kalloc_type_view_226
- Util_AllocCredential.kalloc_type_view_231
- Util_AllocCredential.kalloc_type_view_236
- Util_AllocCredential.kalloc_type_view_241
- Util_AllocCredential.kalloc_type_view_247
- Util_AllocCredential.kalloc_type_view_252
- Util_AllocCredential.kalloc_type_view_257
- Util_AllocCredential.kalloc_type_view_262
- Util_AllocCredential.kalloc_type_view_267
- Util_AllocCredential.kalloc_type_view_280
- Util_AllocRequirement.kalloc_type_view_333
- Util_AllocRequirement.kalloc_type_view_338
- Util_AllocRequirement.kalloc_type_view_343
- Util_AllocRequirement.kalloc_type_view_348
- Util_AllocRequirement.kalloc_type_view_353
- Util_AllocRequirement.kalloc_type_view_358
- Util_AllocRequirement.kalloc_type_view_363
- Util_AllocRequirement.kalloc_type_view_368
- Util_AllocRequirement.kalloc_type_view_373
- Util_AllocRequirement.kalloc_type_view_378
- Util_AllocRequirement.kalloc_type_view_384
- Util_AllocRequirement.kalloc_type_view_391
- Util_AllocRequirement.kalloc_type_view_398
- Util_AllocRequirement.kalloc_type_view_419
- Util_AllocRequirement.kalloc_type_view_424
- Util_AllocRequirement.kalloc_type_view_429
- Util_AllocRequirement.kalloc_type_view_434
- Util_DeallocCredential.kalloc_type_view_132
- Util_DeallocCredential.kalloc_type_view_136
- Util_DeallocCredential.kalloc_type_view_140
- Util_DeallocCredential.kalloc_type_view_144
- Util_DeallocCredential.kalloc_type_view_148
- Util_DeallocCredential.kalloc_type_view_152
- Util_DeallocCredential.kalloc_type_view_156
- Util_DeallocCredential.kalloc_type_view_161
- Util_DeallocCredential.kalloc_type_view_165
- Util_DeallocCredential.kalloc_type_view_169
- Util_DeallocCredential.kalloc_type_view_173
- Util_DeallocCredential.kalloc_type_view_177
- Util_DeallocCredential.kalloc_type_view_189
- Util_DeallocRequirement.kalloc_type_view_538
- Util_DeallocRequirement.kalloc_type_view_542
- Util_DeallocRequirement.kalloc_type_view_546
- Util_DeallocRequirement.kalloc_type_view_550
- Util_DeallocRequirement.kalloc_type_view_554
- Util_DeallocRequirement.kalloc_type_view_558
- Util_DeallocRequirement.kalloc_type_view_562
- Util_DeallocRequirement.kalloc_type_view_566
- Util_DeallocRequirement.kalloc_type_view_570
- Util_DeallocRequirement.kalloc_type_view_574
- Util_DeallocRequirement.kalloc_type_view_579
- Util_DeallocRequirement.kalloc_type_view_584
- Util_DeallocRequirement.kalloc_type_view_589
- Util_DeallocRequirement.kalloc_type_view_601
- Util_DeallocRequirement.kalloc_type_view_605
- Util_DeallocRequirement.kalloc_type_view_609
- Util_DeallocRequirement.kalloc_type_view_613
- Util_DeallocRequirement.kalloc_type_view_617
- _gAllocatedBytes
- deserializeParameters.kalloc_type_view_194
CStrings:
+ "!preflightFound || allowPreflightParameter"
+ "*resultLength >= respDataSize"
+ "ACMRequirement - ACMRequirementDataPushButton"
+ "LibCall_ACMContextContainsCredentialTypeEx"
+ "LibCall_ACMContextCopyData"
+ "LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx"
+ "LibSer_ACMDeserializeEnvironmentVariableType"
+ "LibSer_ACMDeserializeSEPControlCode"
+ "command && commandSize >= sizeof(ACMSEPControlCode)"
+ "context && outSize"
+ "context && outSize && outBuffer"
+ "cred->numCredSets <= kACMContextPoolTotalCount"
+ "inData && inSize"
+ "inSize >= sizeof(ACMEnvironmentVariable)"
+ "nonAutoDisposable requires tracking support"
+ "param.parameterData && param.parameterDataLength == sizeof(uint8_t)"
+ "requirement->type == kACMRequirementTypePushButtonPressed"
+ "requirementSize <= reqSize"
+ "site.ACMRequirement.ACMRequirementDataPushButton"
+ "sourceContextExternalForm && sourceContextExternalFormLength == sizeof(ACMHandle)"
+ "targetContextExternalForm && targetContextExternalFormLength == sizeof(ACMHandle)"
+ "trackingSupported || !nonAutoDisposableRequested"
+ "transport && context"
- "*resultLength >= dataSize"
- "cred->numCredSets <= 80"

```
