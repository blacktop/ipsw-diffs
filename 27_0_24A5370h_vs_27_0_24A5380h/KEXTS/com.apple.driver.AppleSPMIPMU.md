## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

```diff

   __TEXT.__const: 0x36
-  __TEXT.__cstring: 0x2bd8
-  __TEXT_EXEC.__text: 0xcbf4
+  __TEXT.__cstring: 0x2be7
+  __TEXT_EXEC.__text: 0xcbec
   __TEXT_EXEC.__auth_stubs: 0x4d0
   __DATA.__data: 0x320
   __DATA.__common: 0xe8
   __DATA.__bss: 0x140
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x14f0
+  __DATA_CONST.__const: 0x1520
   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x10
   Functions: 192
   Symbols:   0
-  CStrings:  378
+  CStrings:  381
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Functions:
~ __ZN18AppleDialogSPMIPMU23_resetLpemInRestoreModeEv : 364 -> 368
~ __ZN18AppleDialogSPMIPMU21_updateBootPropertiesEb : 2140 -> 2148
~ __ZN18AppleDialogSPMIPMU17_writeLpemLogDataEv : 508 -> 488
CStrings:
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 20:59:17 Jun 30 2026\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 20:59:17 Jun 30 2026\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 20:59:18 Jun 30 2026\n"
+ "%s::start: %s _pmuNub: %p built 20:59:18 Jun 30 2026\n"
+ "B2CA"
+ "B2PD"
+ "B2VT"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 19:34:29 Jun 18 2026\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 19:34:29 Jun 18 2026\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 19:34:30 Jun 18 2026\n"
- "%s::start: %s _pmuNub: %p built 19:34:30 Jun 18 2026\n"

```
