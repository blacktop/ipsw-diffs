## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

```diff

-1360.120.2.0.0
-  __TEXT.__cstring: 0x28ca
-  __TEXT.__const: 0x26
-  __TEXT_EXEC.__text: 0xc024
+1371.0.0.0.0
+  __TEXT.__const: 0x36
+  __TEXT.__cstring: 0x2bd8
+  __TEXT_EXEC.__text: 0xcbe4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x320
-  __DATA.__common: 0xc0
-  __DATA.__bss: 0x138
-  __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0x118
+  __DATA.__common: 0xe8
+  __DATA.__bss: 0x140
+  __DATA_CONST.__mod_init_func: 0x18
+  __DATA_CONST.__mod_term_func: 0x18
+  __DATA_CONST.__const: 0x14f0
+  __DATA_CONST.__kalloc_type: 0x180
+  __DATA_CONST.__auth_got: 0x268
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__mod_init_func: 0x10
-  __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xf00
-  __DATA_CONST.__kalloc_type: 0x140
-  UUID: 1FEA728F-AB0F-3C16-BDB8-59BA71815F21
-  Functions: 167
+  UUID: 71B93739-AF80-3B7F-8D2D-D861C4D1B13A
+  Functions: 192
   Symbols:   0
-  CStrings:  359
+  CStrings:  378
 
CStrings:
+ "\"UPSI test panic in PMU kext at boot stage 0x%x\" @%s:%d"
+ "%s::%sAppleDialogPMU:: Enabled MCURST (info-has_mcurst in EDT)\n"
+ "%s::%sAppleDialogPMU:: No info-has_mcurst in EDT\n"
+ "%s::%sAppleDialogPMU:: info-has_mcurst in EDT but function-arm_peripheral_reset not specified\n"
+ "%s::%sArm of Peripheral MCU Reset failed\n"
+ "%s::%sPMU-LPM: Unable to write phra LPM log (%x)\n\n"
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 22:46:09 May 27 2026\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 22:46:09 May 27 2026\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 22:46:10 May 27 2026\n"
+ "%s::start: %s _pmuNub: %p built 22:46:10 May 27 2026\n"
+ "/chosen"
+ "12111112122212121"
+ "1211111212221212112222222211211111122222212111111212222211122"
+ "AppleDialogSPMIPMU: UPSI injecting action 0x%llx at boot stage 0x%x\n"
+ "AppleDialogSPMIPMU: UPSI injection configured - stage=0x%llx, action=0x%llx\n"
+ "AppleDialogSPMIPMU: Unknown UPSI action 0x%llx - ignoring\n"
+ "AppleDialogSPMIPMU: pmu offwake\n"
+ "AppleDialogSPMIPMUNub"
+ "IOPMURequestMCUReset"
+ "_handlePEHaltRestart"
+ "function-arm_peripheral_reset"
+ "info-has_mcurst"
+ "injection_action"
+ "injection_stage"
+ "site.AppleDialogSPMIPMUNub"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 20:24:20 Apr 23 2026\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 20:24:20 Apr 23 2026\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 20:24:20 Apr 23 2026\n"
- "%s::start: %s _pmuNub: %p built 20:24:20 Apr 23 2026\n"
- "1211111212221212112222222211211111222222121111112122222111"
- "pmu offwake\n"

```
