## com.apple.driver.AppleOLYHAL

> `com.apple.driver.AppleOLYHAL`

```diff

-531.1.0.0.0
+511.1.0.0.0
   __TEXT.__const: 0x1ef0 sha256:49eb8adb2c880a6f86ede57072ec766bec0de9d07550aa620ee61e62b6e2de32
-  __TEXT.__cstring: 0x4973 sha256:d1899405d4bb5a3df2c6aef08abd1b79cb995ea7f62bf319cee731f633b82b77
-  __TEXT_EXEC.__text: 0x1d5dc sha256:b6bbfa4029294c0fc9243e30fdb5088ce88a054fbb668ddc4f66829ec6a7b960
+  __TEXT.__cstring: 0x49d3 sha256:9a5bde48f2bfa09ebfcb9f49115a78f10b13e9273c9b7f8d631e85c5c21edb50
+  __TEXT_EXEC.__text: 0x1cff0 sha256:5081011cc92ca1a29e9a16ae94bd595ba0a204ff101cf3c89659a29479858b1a
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x18c sha256:32ef9c59976097249e0681b65c36444bf6e6c3652b1cbd57484172ff31652b2d
+  __DATA.__data: 0x18c sha256:447bd7c66d507097af4ceba894630870c4e5aae1d0daa2663ef09f3b37031c66
   __DATA.__common: 0x170 sha256:71818ecc26433c32172dd9a3544657971c7078daa2257da7c3c303e08693cb23
   __DATA.__bss: 0xc sha256:15ec7bf0b50732b49f8228e07d24365338f9e3ab994b00af08e5a3bffe55fd8b
-  __DATA_CONST.__mod_init_func: 0x38 sha256:1eb11cf6680aee37ad101cc514b4dac11a7c875edc22922f36f39d51aba7ea75
-  __DATA_CONST.__mod_term_func: 0x38 sha256:2e106d4bfe8070b0fe7bf34ebca9c9fb489d6e3ee060daca6b653230b647daad
-  __DATA_CONST.__const: 0x2020 sha256:a4e392ef848847ab44c69d3d124ed9815f0bb643147c0eed41c033c070384b92
-  __DATA_CONST.__kalloc_type: 0x600 sha256:467e240091b46e92d70d6ad5cc81b2c1fb86d4c2f16127f78e8c3f692e329c11
-  __DATA_CONST.__auth_got: 0x3c8 sha256:ea8c387effa95761ee15a20727bdc7f59436401700a81d21fd527bd8c43d0bd6
-  __DATA_CONST.__got: 0xf8 sha256:7a168cbb8b405a8dea811513d5f0e4c55874d3f43a9b00041150b615d7c7be66
-  UUID: 2E1F0627-9404-39DE-B533-F22B6B3CF865
+  __DATA_CONST.__auth_got: 0x3d0 sha256:25381adfc74f691b9b195e45f8e390e33f9e2a9cf076eb8176d8b124f658e821
+  __DATA_CONST.__got: 0xf8 sha256:c1d50a0b9c6ae928a941c3da196492d06fafcb81a18aace895bd4287d351d08f
+  __DATA_CONST.__mod_init_func: 0x38 sha256:829691b4a58452150767235404f28b694378e484d14ebe569fa8728a9d83fafa
+  __DATA_CONST.__mod_term_func: 0x38 sha256:b7acdd1ba1157a42958f33f1d97e2745fbf1795abac7c345534f36292cd4499c
+  __DATA_CONST.__const: 0x2088 sha256:b450a230e62ffbf6a0ab3154535feeea0aa382dda13396c831629d891d857980
+  __DATA_CONST.__kalloc_type: 0x600 sha256:93c37d3507f7a09a7ff8a61436e2638a617ddd39f63a7e973f2c43de57c2eccf
+  UUID: F3692180-EF49-380D-A3C8-8D09ED16C509
   Functions: 572
-  Symbols:   1094
-  CStrings:  516
+  Symbols:   1097
+  CStrings:  520
 
Symbols:
+ _ZN32AppleOLYHALPortInterfacePCIeAMFM27resetPortActionHandlerGatedEv.cold.2
+ __ZN28AppleOLYHALPortInterfacePCIe17abortOngoingResetEv
+ __ZN28AppleOLYHALPortInterfacePCIe19isFLRRecoveryFailedEv
+ __ZN32AppleOLYHALPortInterfacePCIeAMFM17abortOngoingResetEv
+ __ZN32AppleOLYHALPortInterfacePCIeAMFM19isFLRRecoveryFailedEv
+ __ZNK9IOService10isInactiveEv
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_445
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_451
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM23processAMFMMessageGatedEjPvmE21kalloc_type_view_1225
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_479
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_481
+ ____ZN11AppleOLYHAL20updateDextSpawnCountEv_block_invoke_2
+ ____ZN32AppleOLYHALPortInterfacePCIeAMFM17abortOngoingResetEv_block_invoke
+ ____ZN32AppleOLYHALPortInterfacePCIeAMFM19isFLRRecoveryFailedEv_block_invoke
+ __block_descriptor_tmp.117
+ __block_descriptor_tmp.123
+ __block_descriptor_tmp.134
+ __block_descriptor_tmp.139
+ __block_descriptor_tmp.145
+ __block_descriptor_tmp.159
+ __block_descriptor_tmp.167
+ __block_descriptor_tmp.227
+ __block_descriptor_tmp.40
+ __block_descriptor_tmp.43
- _OUTLINED_FUNCTION_4
- _ZN32AppleOLYHALPortInterfacePCIeAMFM27processAMFMPreparePCIeErrorEPvm.cold.1
- __ZN28AppleOLYHALPortInterfacePCIe16requestChipResetEb
- __ZN28AppleOLYHALPortInterfacePCIe21setDextStateSuspendedEb
- __ZN32AppleOLYHALPortInterfacePCIeAMFM16requestChipResetEb
- __ZN32AppleOLYHALPortInterfacePCIeAMFM27processAMFMPreparePCIeErrorEPvm
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_471
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_477
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM23processAMFMMessageGatedEjPvmE21kalloc_type_view_1352
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_506
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_508
- ___ZN32AppleOLYHALPortInterfacePCIeAMFM16requestChipResetEb_block_invoke.cold.1
- ____ZN32AppleOLYHALPortInterfacePCIeAMFM16requestChipResetEb_block_invoke
- __block_descriptor_tmp.118
- __block_descriptor_tmp.121
- __block_descriptor_tmp.124
- __block_descriptor_tmp.130
- __block_descriptor_tmp.135
- __block_descriptor_tmp.141
- __block_descriptor_tmp.151
- __block_descriptor_tmp.163
- __block_descriptor_tmp.223
CStrings:
+ "\"%s:%u:\" \"!fPendingErrorHandling\" @%s:%d"
+ "\"%s:%u:\" \"(fClientStatus != kClientCrashed)\" @%s:%d"
+ "%s::%s: Bus layer reset in quiesce, skip PreparePCIeError\n"
+ "%s::%s: Dext terminated due to graceful reboot.\n"
+ "%s::%s: Handling Dext Crash with delayed powercycle\n"
+ "%s::%s: Starting delayed powercycle\n"
+ "%s::%s: port on failed after link down\n"
+ "%s::%s: unlocking pending error handling thread\n"
+ "12111122111112222"
+ "12111122111112222111221111221"
+ "serviceNotifier_block_invoke"
+ "updateDextSpawnCount_block_invoke_2"
- "\"kAMFMPreparePCIeError is handled by processAMFMPreparePCIeError outside fCommandGate. We shouldn't be here\" @%s:%d"
- "%s::%s: Bus layer reset in progress (%u), skip PreparePCIeError\n"
- "%s::%s: Dext recovery is paused. skip PreparePCIeError\n"
- "%s::%s: Invalid argSize %lu, expected at least %lu\n"
- "121111221111122221"
- "121111221111122221111221111221"
- "processAMFMPreparePCIeError"
- "requestChipReset_block_invoke"

```
