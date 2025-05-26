## AppleLockdownMode

> `/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode`

```diff

 65.0.0.0.0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x444e
-  __TEXT_EXEC.__text: 0x13b64
+  __TEXT.__cstring: 0x43a9
+  __TEXT_EXEC.__text: 0x13a24
   __TEXT_EXEC.__auth_stubs: 0x230
   __DATA.__data: 0xc6
   __DATA.__common: 0x40

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x300
-  __DATA_CONST.__kalloc_var: 0x1400
+  __DATA_CONST.__kalloc_var: 0x1360
   Functions: 168
-  Symbols:   606
-  CStrings:  465
+  Symbols:   604
+  CStrings:  462
 
Symbols:
+ DeallocCredentialList.kalloc_type_view_1794
+ DeserializeCredentialList.kalloc_type_view_1756
+ LibCall_ACMContextLoadFromImage.kalloc_type_view_1447
+ LibCall_ACMContextLoadFromImage.kalloc_type_view_1508
+ Util_AllocCredential.kalloc_type_view_211
+ Util_AllocCredential.kalloc_type_view_216
+ Util_AllocCredential.kalloc_type_view_221
+ Util_AllocCredential.kalloc_type_view_226
+ Util_AllocCredential.kalloc_type_view_231
+ Util_AllocCredential.kalloc_type_view_236
+ Util_AllocCredential.kalloc_type_view_241
+ Util_AllocCredential.kalloc_type_view_247
+ Util_AllocCredential.kalloc_type_view_252
+ Util_AllocCredential.kalloc_type_view_257
+ Util_AllocCredential.kalloc_type_view_262
+ Util_AllocCredential.kalloc_type_view_267
+ Util_AllocCredential.kalloc_type_view_280
+ Util_AllocRequirement.kalloc_type_view_332
+ Util_AllocRequirement.kalloc_type_view_337
+ Util_AllocRequirement.kalloc_type_view_342
+ Util_AllocRequirement.kalloc_type_view_347
+ Util_AllocRequirement.kalloc_type_view_352
+ Util_AllocRequirement.kalloc_type_view_357
+ Util_AllocRequirement.kalloc_type_view_362
+ Util_AllocRequirement.kalloc_type_view_367
+ Util_AllocRequirement.kalloc_type_view_372
+ Util_AllocRequirement.kalloc_type_view_377
+ Util_AllocRequirement.kalloc_type_view_390
+ Util_AllocRequirement.kalloc_type_view_397
+ Util_AllocRequirement.kalloc_type_view_405
+ Util_AllocRequirement.kalloc_type_view_433
+ Util_DeallocCredential.kalloc_type_view_189
+ Util_DeallocRequirement.kalloc_type_view_536
+ Util_DeallocRequirement.kalloc_type_view_540
+ Util_DeallocRequirement.kalloc_type_view_544
+ Util_DeallocRequirement.kalloc_type_view_548
+ Util_DeallocRequirement.kalloc_type_view_552
+ Util_DeallocRequirement.kalloc_type_view_556
+ Util_DeallocRequirement.kalloc_type_view_560
+ Util_DeallocRequirement.kalloc_type_view_564
+ Util_DeallocRequirement.kalloc_type_view_568
+ Util_DeallocRequirement.kalloc_type_view_572
+ Util_DeallocRequirement.kalloc_type_view_582
+ Util_DeallocRequirement.kalloc_type_view_587
+ Util_DeallocRequirement.kalloc_type_view_593
+ Util_DeallocRequirement.kalloc_type_view_611
+ Util_DeallocRequirement.kalloc_type_view_615
+ deserializeParameters.kalloc_type_view_194
- DeallocCredentialList.kalloc_type_view_1780
- DeserializeCredentialList.kalloc_type_view_1742
- LibCall_ACMContextLoadFromImage.kalloc_type_view_1445
- LibCall_ACMContextLoadFromImage.kalloc_type_view_1506
- Util_AllocCredential.kalloc_type_view_210
- Util_AllocCredential.kalloc_type_view_215
- Util_AllocCredential.kalloc_type_view_220
- Util_AllocCredential.kalloc_type_view_225
- Util_AllocCredential.kalloc_type_view_230
- Util_AllocCredential.kalloc_type_view_235
- Util_AllocCredential.kalloc_type_view_240
- Util_AllocCredential.kalloc_type_view_246
- Util_AllocCredential.kalloc_type_view_251
- Util_AllocCredential.kalloc_type_view_256
- Util_AllocCredential.kalloc_type_view_261
- Util_AllocCredential.kalloc_type_view_266
- Util_AllocCredential.kalloc_type_view_278
- Util_AllocRequirement.kalloc_type_view_329
- Util_AllocRequirement.kalloc_type_view_334
- Util_AllocRequirement.kalloc_type_view_339
- Util_AllocRequirement.kalloc_type_view_344
- Util_AllocRequirement.kalloc_type_view_349
- Util_AllocRequirement.kalloc_type_view_354
- Util_AllocRequirement.kalloc_type_view_359
- Util_AllocRequirement.kalloc_type_view_364
- Util_AllocRequirement.kalloc_type_view_369
- Util_AllocRequirement.kalloc_type_view_374
- Util_AllocRequirement.kalloc_type_view_379
- Util_AllocRequirement.kalloc_type_view_385
- Util_AllocRequirement.kalloc_type_view_392
- Util_AllocRequirement.kalloc_type_view_400
- Util_AllocRequirement.kalloc_type_view_408
- Util_DeallocCredential.kalloc_type_view_188
- Util_DeallocRequirement.kalloc_type_view_530
- Util_DeallocRequirement.kalloc_type_view_534
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
- Util_DeallocRequirement.kalloc_type_view_585
- Util_DeallocRequirement.kalloc_type_view_591
- Util_DeallocRequirement.kalloc_type_view_595
- deserializeParameters.kalloc_type_view_188
CStrings:
+ "param->parameterDataLength == 0"
+ "parametersLength + param->parameterDataLength >= parametersLength"
- "ACMRequirement - ACMRequirementDataRatchet"
- "parametersLength + param->parameterDataLength > parametersLength"
- "requirement->dataLength >= sizeof(ACMRequirementDataRatchet)"
- "requirement->type == kACMRequirementTypeRatchet"
- "site.ACMRequirement.ACMRequirementDataRatchet"

```
