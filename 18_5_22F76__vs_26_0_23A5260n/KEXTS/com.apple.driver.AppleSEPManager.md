## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

```diff

-850.100.14.0.0
-  __TEXT.__const: 0x7187
-  __TEXT.__cstring: 0x1007b
-  __TEXT_EXEC.__text: 0x4632c
+880.0.1.0.0
+  __TEXT.__const: 0x7e37
+  __TEXT.__cstring: 0x1043e
+  __TEXT_EXEC.__text: 0x4703c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x168
   __DATA.__common: 0xc48

   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__mod_init_func: 0xc0
   __DATA_CONST.__mod_term_func: 0xc0
-  __DATA_CONST.__const: 0x9820
+  __DATA_CONST.__const: 0x99a8
   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0x50
-  UUID: D4F5BA4E-2FE8-3B84-B9EF-707325A57E50
-  Functions: 2375
+  UUID: 8EEB123D-D6EC-35F9-A8D7-836ADD81169B
+  Functions: 2389
   Symbols:   0
-  CStrings:  1401
+  CStrings:  1422
 
CStrings:
+ "\"TXM channel base address length unexpected: %u\" @%s:%d"
+ "\"txm-secure-channel-base not available with a SEP DART\" @%s:%d"
+ "\"unable to insert TXM-SEP secure channel mapping: %d\\n\" @%s:%d"
+ "\"using TXM-SEP secure channel with fixed DVA without DART\" @%s:%d"
+ "%s: Detected hardcoded TXM-SEP secure channel DVA, setting flag in init flags\n\n"
+ "%s: Didn't find hardcoded TXM-SEP secure channel DVA\n\n"
+ "%s: No SEP on during low power boot arg\n"
+ "%s: SEP on during low power: %u\n"
+ "%s: SEP on during low power: EDT %u\n"
+ "%s: SEP on during low power: boot-arg %u\n"
+ "%s: mach_absolute_time: %llu\n"
+ "%s: wait for active call, mach_absolute_time: %llu\n"
+ "%s: wait for hold call, mach_absolute_time: %llu\n"
+ "/arm-io/dart-sep"
+ "12111112122212121112121222121111111111221222112111112122221111111112122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121122222222222222222222222222222222222121"
+ "TXM-SEP secure channel: %u | %u\n"
+ "low-power-enable"
+ "registerPowerDriver(this, power_states, sizeof(power_states) / sizeof(power_states[0])) == kIOPMNoErr"
+ "sep_on_low_power"
+ "txm-secure-channel-base"
+ "void AppleSEPControl::_callActiveAsync()"
+ "void AppleSEPManager::_asyncHoldCall()"
+ "void AppleSEPManager::_configurePowerStates()"
- "1211111212221212111212122212111111111121222112111112122221111111112122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121122222222222222222222222222222222222121"
- "acquired shared page for the TXM channel\n"

```
