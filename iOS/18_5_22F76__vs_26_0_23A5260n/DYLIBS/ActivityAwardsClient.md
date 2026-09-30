## ActivityAwardsClient

> `/System/Library/PrivateFrameworks/ActivityAwardsClient.framework/ActivityAwardsClient`

```diff

-612.6.0.0.0
-  __TEXT.__text: 0x4af8
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0x2ec
+643.0.1.0.0
+  __TEXT.__text: 0x5538
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_methlist: 0x30c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x10b
+  __TEXT.__cstring: 0x168
   __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__oslogstring: 0x53e
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__oslogstring: 0x743
+  __TEXT.__unwind_info: 0x1b8
   __TEXT.__objc_classname: 0x60
-  __TEXT.__objc_methname: 0x7fa
-  __TEXT.__objc_methtype: 0x22c
+  __TEXT.__objc_methname: 0x88a
+  __TEXT.__objc_methtype: 0x23e
   __TEXT.__objc_stubs: 0x520
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x2e0
+  __DATA_CONST.__const: 0x2f0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x290
+  __DATA_CONST.__objc_selrefs: 0x2a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1b0
+  __AUTH_CONST.__auth_got: 0x1d0
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0xc0
+  __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x670
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/ActivityAchievements.framework/ActivityAchievements
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5290C3F7-FE4D-3E53-B38B-AB4AA617356A
-  Functions: 111
-  Symbols:   419
-  CStrings:  169
+  UUID: D56664F7-43D2-34D6-95C2-0A7B55E1F54A
+  Functions: 123
+  Symbols:   449
+  CStrings:  183
 
Symbols:
+ -[AACAwardsClient achievementsForTemplateNames:completion:]
+ -[AACAwardsClient achievementsForTemplateNames:completion:].cold.1
+ -[AACAwardsClient anniversaryAchievementsForDate:templateNames:completion:]
+ -[AACAwardsClient anniversaryAchievementsForDate:templateNames:completion:].cold.1
+ -[AACAwardsClient earnedAchievementsForDateInterval:completion:]
+ -[AACAwardsClient earnedAchievementsForDateInterval:completion:].cold.1
+ GCC_except_table18
+ _AACXPCEndpointAwardsMonthlyChallengeQuery
+ _AACXPCEndpointAwardsTemplateNamesQuery
+ _ACHCodableFromAnniversaryRequest
+ _ACHCodableFromDateInterval
+ _ACHCodableFromTemplateNameArray
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.351
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.352
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.361
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.361.cold.1
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.362
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.362.cold.1
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.363
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.363.cold.1
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke_2.353
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke_2.353.cold.1
+ ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.371
+ ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.371.cold.1
+ ___55-[AACXPCClient _serverQueue_initializeDaemonConnection]_block_invoke.343
+ ___55-[AACXPCClient _serverQueue_initializeDaemonConnection]_block_invoke.343.cold.1
+ ___59-[AACAwardsClient achievementsForTemplateNames:completion:]_block_invoke
+ ___59-[AACAwardsClient achievementsForTemplateNames:completion:]_block_invoke.cold.1
+ ___61-[AACXPCClient sendSynchronousRequest:payload:resultHandler:]_block_invoke.350
+ ___64-[AACAwardsClient earnedAchievementsForDateInterval:completion:]_block_invoke
+ ___64-[AACAwardsClient earnedAchievementsForDateInterval:completion:]_block_invoke.cold.1
+ ___75-[AACAwardsClient anniversaryAchievementsForDate:templateNames:completion:]_block_invoke
+ ___75-[AACAwardsClient anniversaryAchievementsForDate:templateNames:completion:]_block_invoke.cold.1
+ ___block_literal_global.345
+ ___block_literal_global.373
+ _objc_retain_x4
- GCC_except_table12
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.348
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.349
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.358
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.358.cold.1
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.359
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.359.cold.1
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.360
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.360.cold.1
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke_2.350
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke_2.350.cold.1
- ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.362
- ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.362.cold.1
- ___55-[AACXPCClient _serverQueue_initializeDaemonConnection]_block_invoke.340
- ___55-[AACXPCClient _serverQueue_initializeDaemonConnection]_block_invoke.340.cold.1
- ___61-[AACXPCClient sendSynchronousRequest:payload:resultHandler:]_block_invoke.347
- ___block_literal_global.342
- ___block_literal_global.364
CStrings:
+ "AAC_XPC_Endpoint_Awards_Monthly_Challenge_Query"
+ "AAC_XPC_Endpoint_Awards_Template_Names_Query"
+ "Calling sendRequest from client for achievementsForTemplateNames"
+ "Calling sendRequest from client for anniversaryAchievementsForDateComponents:templateNames:"
+ "Calling sendRequest from client for earnedInstancesForDateInterval"
+ "Got result back from sending sendRequest from client for achievementsForTemplateNames"
+ "Got result back from sending sendRequest from client for allEarnedAchievementsForDateInterval"
+ "Got result back from sending sendRequest from client for anniversaryAchievementsForDateComponents:templateNames:"
+ "achievementsForTemplateNames:completion:"
+ "anniversaryAchievementsForDate:templateNames:completion:"
+ "earnedAchievementsForDateInterval:completion:"
+ "v40@0:8@16@24@?32"

```
