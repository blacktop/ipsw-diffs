## libcsfde.dylib

> `/usr/lib/libcsfde.dylib`

```diff

 566.0.0.0.0
-  __TEXT.__text: 0x8cdc
+  __TEXT.__text: 0x8c58
   __TEXT.__auth_stubs: 0xac0
   __TEXT.__cstring: 0x15c8
   __TEXT.__const: 0x30
-  __TEXT.__unwind_info: 0x218
-  __DATA_CONST.__got: 0x148
+  __TEXT.__unwind_info: 0x208
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0xe8
   __AUTH_CONST.__auth_got: 0x560
   __AUTH_CONST.__cfstring: 0xe80

   - /usr/lib/libCoreStorage.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 87EE935B-C568-3347-A752-433885570CF3
-  Functions: 151
-  Symbols:   395
+  UUID: B2EBB892-F1F5-3660-BF21-7590D1DFB8E7
+  Functions: 150
+  Symbols:   394
   CStrings:  279
 
Symbols:
+ __MergedGlobals
- _gAppleFDEKeyStoreService
- _gUserClientConnection
Functions:
~ _fde_query_context : 500 -> 520
- sub_199486450
~ _CSFDECreateKey : 264 -> 256
~ _CSFDEStorePassphraseWithBytes : 420 -> 412
~ _CSFDEGetPassphrase : 388 -> 384
~ _CSFDEGetPBKDF : 404 -> 388
~ _CSFDEEncryptData : 372 -> 368
~ _CSFDEWritePropertyCacheToFD : 440 -> 472
~ _wrapVolumeKey : 316 -> 308
~ _CSFDERemoveUserEntry : 380 -> 396
~ _CSFDEMergeRecoveryDataFromRecipe : 380 -> 368
~ _wrapKEKWithPassphrase : 328 -> 320
~ _CSFDEUnlockUserEntryWithKey : 420 -> 416
~ _unlockWithPassphrase : 376 -> 364
~ _CSFDEUnlockAnyUserEntryWithPassphraseForSMC : 440 -> 432
~ _CSFDEPrepareRevertWithKEK : 392 -> 388
- _initUserClient
~ _CSFDEunpackRecoveryRecord : 1372 -> 1360
~ _CSFDEActivateRecoveryAgentAsNeeded : 584 -> 576
~ _CSFDERequestInstitutionalRecoveryUserEntry : 1300 -> 1292
~ __doiCloudRecoveryUser : 584 -> 568
~ _processUserEntry : 792 -> 780
~ _processiCloudUserEntry : 568 -> 564
~ _CSFDEPostRecoveryData : 1020 -> 1016
~ _CSFDEGetRecoveryDataFromApple : 848 -> 844
~ _CSFDERequestPersonalRecoveryUserEntry : 232 -> 240
~ __optInToRecoveryCore : 1364 -> 1344

```
