## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

```diff

-1360.0.0.0.0
+1360.0.1.0.0
   __TEXT.__cstring: 0x2584
   __TEXT.__const: 0x26
-  __TEXT_EXEC.__text: 0xc784
+  __TEXT_EXEC.__text: 0xc740
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x320
   __DATA.__common: 0xc0

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf00
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 4EDA282F-018E-3DD7-B584-0F83A4F50DA8
+  UUID: 41F00E89-E104-35DB-8BE1-B78C0E374CC1
   Functions: 155
   Symbols:   0
   CStrings:  350
Functions:
~ __ZN18AppleDialogSPMIPMU10_writeRegsEtPht : 340 -> 320
~ __ZN18AppleDialogSPMIPMU9_readRegsEtPht : 340 -> 320
~ __ZN18AppleDialogSPMIPMU6modRegEthh : 452 -> 424
CStrings:
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 23:37:29 Jun 16 2025\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 23:37:29 Jun 16 2025\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 23:37:29 Jun 16 2025\n"
+ "%s::start: %s _pmuNub: %p built 23:37:29 Jun 16 2025\n"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 18:50:07 May 30 2025\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 18:50:07 May 30 2025\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 18:50:07 May 30 2025\n"
- "%s::start: %s _pmuNub: %p built 18:50:07 May 30 2025\n"

```
