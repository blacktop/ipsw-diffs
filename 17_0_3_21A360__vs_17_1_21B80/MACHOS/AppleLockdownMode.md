## AppleLockdownMode

> `/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode`

```diff

-62.0.0.0.0
+65.0.0.0.0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x4250
-  __TEXT_EXEC.__text: 0x12e4c
+  __TEXT.__cstring: 0x444e
+  __TEXT_EXEC.__text: 0x13b64
   __TEXT_EXEC.__auth_stubs: 0x230
   __DATA.__data: 0xc6
   __DATA.__common: 0x40

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x300
-  __DATA_CONST.__kalloc_var: 0x1360
-  UUID: D825FB44-51E1-3BC5-B404-F305EC6F21FC
-  Functions: 159
-  Symbols:   595
-  CStrings:  453
+  __DATA_CONST.__kalloc_var: 0x1400
+  UUID: FEA88028-AED7-3B63-A4AC-7CABC9EA70AD
+  Functions: 168
+  Symbols:   606
+  CStrings:  465
 
Symbols:
+ DeallocCredentialList.kalloc_type_view_1780
+ DeserializeCredentialList.kalloc_type_view_1742
+ LibCall_ACMContextLoadFromImage.kalloc_type_view_1445
+ LibCall_ACMContextLoadFromImage.kalloc_type_view_1506
+ Util_AllocCredential.kalloc_type_view_210
+ Util_AllocCredential.kalloc_type_view_215
+ Util_AllocCredential.kalloc_type_view_220
+ Util_AllocCredential.kalloc_type_view_225
+ Util_AllocCredential.kalloc_type_view_230
+ Util_AllocCredential.kalloc_type_view_235
+ Util_AllocCredential.kalloc_type_view_240
+ Util_AllocCredential.kalloc_type_view_246
+ Util_AllocCredential.kalloc_type_view_251
+ Util_AllocCredential.kalloc_type_view_256
+ Util_AllocCredential.kalloc_type_view_261
+ Util_AllocCredential.kalloc_type_view_266
+ Util_AllocCredential.kalloc_type_view_278
+ Util_AllocRequirement.kalloc_type_view_329
+ Util_AllocRequirement.kalloc_type_view_334
+ Util_AllocRequirement.kalloc_type_view_339
+ Util_AllocRequirement.kalloc_type_view_344
+ Util_AllocRequirement.kalloc_type_view_349
+ Util_AllocRequirement.kalloc_type_view_354
+ Util_AllocRequirement.kalloc_type_view_359
+ Util_AllocRequirement.kalloc_type_view_364
+ Util_AllocRequirement.kalloc_type_view_369
+ Util_AllocRequirement.kalloc_type_view_374
+ Util_AllocRequirement.kalloc_type_view_379
+ Util_AllocRequirement.kalloc_type_view_392
+ Util_AllocRequirement.kalloc_type_view_400
+ Util_AllocRequirement.kalloc_type_view_408
+ Util_AllocRequirement.kalloc_type_view_413
+ Util_AllocRequirement.kalloc_type_view_418
+ Util_AllocRequirement.kalloc_type_view_423
+ Util_AllocRequirement.kalloc_type_view_428
+ Util_DeallocCredential.kalloc_type_view_188
+ Util_DeallocRequirement.kalloc_type_view_530
+ Util_DeallocRequirement.kalloc_type_view_534
+ Util_DeallocRequirement.kalloc_type_view_538
+ Util_DeallocRequirement.kalloc_type_view_542
+ Util_DeallocRequirement.kalloc_type_view_546
+ Util_DeallocRequirement.kalloc_type_view_550
+ Util_DeallocRequirement.kalloc_type_view_554
+ Util_DeallocRequirement.kalloc_type_view_558
+ Util_DeallocRequirement.kalloc_type_view_562
+ Util_DeallocRequirement.kalloc_type_view_566
+ Util_DeallocRequirement.kalloc_type_view_570
+ Util_DeallocRequirement.kalloc_type_view_579
+ Util_DeallocRequirement.kalloc_type_view_585
+ Util_DeallocRequirement.kalloc_type_view_591
+ Util_DeallocRequirement.kalloc_type_view_595
+ Util_DeallocRequirement.kalloc_type_view_599
+ Util_DeallocRequirement.kalloc_type_view_603
+ Util_DeallocRequirement.kalloc_type_view_607
+ _LibCall_ACMSEPControl
+ _LibSer_SEPControlResponse_Deserialize
+ _LibSer_SEPControlResponse_GetSize
+ _LibSer_SEPControlResponse_Serialize
+ _LibSer_SEPControl_Deserialize
+ _LibSer_SEPControl_GetSize
+ _LibSer_SEPControl_Serialize
+ _Util_getSubrequirement
+ _Util_getSubrequirementOfType
- DeallocCredentialList.kalloc_type_view_1772
- DeserializeCredentialList.kalloc_type_view_1734
- LibCall_ACMContextLoadFromImage.kalloc_type_view_1424
- LibCall_ACMContextLoadFromImage.kalloc_type_view_1485
- Util_AllocCredential.kalloc_type_view_209
- Util_AllocCredential.kalloc_type_view_214
- Util_AllocCredential.kalloc_type_view_219
- Util_AllocCredential.kalloc_type_view_224
- Util_AllocCredential.kalloc_type_view_229
- Util_AllocCredential.kalloc_type_view_234
- Util_AllocCredential.kalloc_type_view_239
- Util_AllocCredential.kalloc_type_view_245
- Util_AllocCredential.kalloc_type_view_250
- Util_AllocCredential.kalloc_type_view_255
- Util_AllocCredential.kalloc_type_view_260
- Util_AllocCredential.kalloc_type_view_265
- Util_AllocCredential.kalloc_type_view_276
- Util_AllocRequirement.kalloc_type_view_327
- Util_AllocRequirement.kalloc_type_view_332
- Util_AllocRequirement.kalloc_type_view_337
- Util_AllocRequirement.kalloc_type_view_342
- Util_AllocRequirement.kalloc_type_view_347
- Util_AllocRequirement.kalloc_type_view_352
- Util_AllocRequirement.kalloc_type_view_357
- Util_AllocRequirement.kalloc_type_view_362
- Util_AllocRequirement.kalloc_type_view_367
- Util_AllocRequirement.kalloc_type_view_372
- Util_AllocRequirement.kalloc_type_view_378
- Util_AllocRequirement.kalloc_type_view_393
- Util_AllocRequirement.kalloc_type_view_401
- Util_AllocRequirement.kalloc_type_view_406
- Util_AllocRequirement.kalloc_type_view_411
- Util_AllocRequirement.kalloc_type_view_416
- Util_AllocRequirement.kalloc_type_view_421
- Util_DeallocCredential.kalloc_type_view_187
- Util_DeallocRequirement.kalloc_type_view_523
- Util_DeallocRequirement.kalloc_type_view_527
- Util_DeallocRequirement.kalloc_type_view_531
- Util_DeallocRequirement.kalloc_type_view_535
- Util_DeallocRequirement.kalloc_type_view_539
- Util_DeallocRequirement.kalloc_type_view_543
- Util_DeallocRequirement.kalloc_type_view_547
- Util_DeallocRequirement.kalloc_type_view_551
- Util_DeallocRequirement.kalloc_type_view_555
- Util_DeallocRequirement.kalloc_type_view_559
- Util_DeallocRequirement.kalloc_type_view_563
- Util_DeallocRequirement.kalloc_type_view_568
- Util_DeallocRequirement.kalloc_type_view_580
- Util_DeallocRequirement.kalloc_type_view_584
- Util_DeallocRequirement.kalloc_type_view_588
- Util_DeallocRequirement.kalloc_type_view_592
- Util_DeallocRequirement.kalloc_type_view_596
CStrings:
+ "*resultLength >= dataSize"
+ "ACMRequirement - ACMRequirementDataRatchet"
+ "LibCall_ACMSEPControl"
+ "handle && parameters && parametersCount && command && commandSize"
+ "index < kofnData->subrequirementsCount"
+ "req->type == kACMRequirementTypeKofN"
+ "requirement->dataLength >= sizeof(ACMRequirementDataRatchet)"
+ "requirement->type == kACMRequirementTypeRatchet"
+ "responseData && responseDataSize"
+ "site.ACMRequirement.ACMRequirementDataRatchet"
+ "size >= sizeof(ACMHandle) + sizeof(uint32_t) + sizeof(uint32_t)"
+ "size >= sizeof(uint32_t)"

```
