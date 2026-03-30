## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

```diff

-1360.100.5.0.0
-  __TEXT.__cstring: 0x281e
+1360.120.2.0.0
+  __TEXT.__cstring: 0x28ca
   __TEXT.__const: 0x26
-  __TEXT_EXEC.__text: 0xbefc
+  __TEXT_EXEC.__text: 0xc024
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x320
   __DATA.__common: 0xc0
-  __DATA.__bss: 0x130
+  __DATA.__bss: 0x138
   __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x10

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf00
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: CE23EAD8-4831-3453-AF80-9EF8EF773AD2
+  UUID: A9C9F1C8-9F10-36B9-AA8E-F0B878B8B89C
   Functions: 167
   Symbols:   0
-  CStrings:  354
+  CStrings:  359
 
Functions:
~ __ZN18AppleDialogSPMIPMU5startEP9IOService : 3144 -> 3200
~ sub_fffffe000927fe64 -> sub_fffffe0009321dac : 148 -> 204
~ __ZN18AppleDialogSPMIPMU18registerPMCallbackEv : 340 -> 352
~ __ZN18AppleDialogSPMIPMU18_readConfigurationEP9IOService : 3260 -> 3412
~ __GLOBAL__sub_I_AppleDialogSPMIPMU.cpp : 320 -> 340
CStrings:
+ "%s::%sAppleDialogPMU:: Enabled AAPC (info-has_aapc in EDT)\n"
+ "%s::%sAppleDialogPMU:: No info-has_aapc in EDT\n"
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 18:33:31 Mar 20 2026\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 18:33:31 Mar 20 2026\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 18:33:31 Mar 20 2026\n"
+ "%s::start: %s _pmuNub: %p built 18:33:31 Mar 20 2026\n"
+ "1211111212221212112222222211211111222222121111112122222111"
+ "Automatic Restart On Power Connect"
+ "IOPMUBootAAPC"
+ "info-has_aapc"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 20:57:29 Mar  8 2026\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 20:57:29 Mar  8 2026\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 20:57:29 Mar  8 2026\n"
- "%s::start: %s _pmuNub: %p built 20:57:29 Mar  8 2026\n"
- "121111121222121211222222221121111122222121111112122222111"

```
