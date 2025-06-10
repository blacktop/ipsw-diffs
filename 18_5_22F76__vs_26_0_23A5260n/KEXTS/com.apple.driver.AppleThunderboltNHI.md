## com.apple.driver.AppleThunderboltNHI

> `com.apple.driver.AppleThunderboltNHI`

```diff

-808.100.1.0.0
-  __TEXT.__cstring: 0xa9c3
-  __TEXT.__os_log: 0x6dad
-  __TEXT.__const: 0x28a10
-  __TEXT_EXEC.__text: 0x37c84
+817.0.0.0.0
+  __TEXT.__cstring: 0xab46
+  __TEXT.__const: 0x28a20
+  __TEXT.__os_log: 0x6e76
+  __TEXT_EXEC.__text: 0x38f7c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x280
   __DATA.__common: 0x450
-  __DATA_CONST.__auth_got: 0x3a0
-  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__auth_got: 0x3b0
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__mod_init_func: 0xd8
   __DATA_CONST.__mod_term_func: 0xd8
-  __DATA_CONST.__const: 0x6660
+  __DATA_CONST.__const: 0x66c8
   __DATA_CONST.__kalloc_type: 0x6c0
   __DATA_CONST.__kalloc_var: 0x460
-  UUID: CADE924D-3213-332D-AE4B-1A7DA33621B2
-  Functions: 895
+  UUID: FBF7881F-93E0-3EDD-8469-91035AA26633
+  Functions: 901
   Symbols:   0
-  CStrings:  919
+  CStrings:  927
 
CStrings:
+ "%lldus AppleThunderboltGenericHAL(%d)<%p>::systemWillShutdown -  dispatchAsync( processSystemWillShutdown)\n"
+ "%lldus AppleThunderboltHALGenericACIO<%p>::enableDART - bypass DART\n"
+ "%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMDozeState\n"
+ "%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMEarlySleepState\n"
+ "%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMEarlyWakeState\n"
+ "%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMLateSleepState\n"
+ "%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMPauseState\n"
+ "%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMPrePCIWakeState\n"
+ "%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMRestartState\n"
+ "%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMShutdownState\n"
+ "%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMSleepState\n"
+ "%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMWakeState\n"
+ "%lldus AppleThunderboltNHI::processSetPMState - state = 0x%08x\n"
+ "%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - global dispatch queue not found!\n"
+ "%lldus AppleThunderboltNHIGenericACIO::lateShutdownInternal - fStarted = %d fPoweredOff = %d fPMState = %d\n"
+ "%lldus AppleThunderboltNHIGenericACIO::shutdown\n"
+ "%lldus AppleThunderboltNHIGenericACIO::shutdown - skipped fStarted = %d fPoweredOff = %d\n"
+ "18:50:35"
+ "May 30 2025"
+ "state"
+ "v8@?0"
- "%lldus AppleThunderboltNHI::setPMState - kThunderboltHALPMDozeState\n"
- "%lldus AppleThunderboltNHI::setPMState - kThunderboltHALPMEarlySleepState\n"
- "%lldus AppleThunderboltNHI::setPMState - kThunderboltHALPMEarlyWakeState\n"
- "%lldus AppleThunderboltNHI::setPMState - kThunderboltHALPMLateSleepState\n"
- "%lldus AppleThunderboltNHI::setPMState - kThunderboltHALPMPauseState\n"
- "%lldus AppleThunderboltNHI::setPMState - kThunderboltHALPMPrePCIWakeState\n"
- "%lldus AppleThunderboltNHI::setPMState - kThunderboltHALPMRestartState\n"
- "%lldus AppleThunderboltNHI::setPMState - kThunderboltHALPMShutdownState\n"
- "%lldus AppleThunderboltNHI::setPMState - kThunderboltHALPMSleepState\n"
- "%lldus AppleThunderboltNHI::setPMState - kThunderboltHALPMWakeState\n"
- "%lldus AppleThunderboltNHIGenericACIO(%d)::applyTunables - \"%s\" - skip_tunable = %d, skipping tunable: offset = 0x%08x mask = 0x%08llx value=0x%08llx\n"
- "%lldus AppleThunderboltNHIGenericACIO::lateSleepInternal\n"
- "%lldus AppleThunderboltNHIGenericACIO::lateSleepInternal return\n"
- "20:15:17"
- "Apr 22 2025"

```
