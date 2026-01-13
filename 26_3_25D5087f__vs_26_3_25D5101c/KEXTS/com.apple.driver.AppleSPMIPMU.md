## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

```diff

-1360.80.2.0.0
-  __TEXT.__cstring: 0x25cf
+1360.80.3.0.0
+  __TEXT.__cstring: 0x2649
   __TEXT.__const: 0x26
-  __TEXT_EXEC.__text: 0xcb08
+  __TEXT_EXEC.__text: 0xce98
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x320
   __DATA.__common: 0xc0

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x17c0
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 90223A73-6EC4-33A0-BB9C-5A73A8D12960
-  Functions: 155
-  Symbols:   604
-  CStrings:  350
+  UUID: DA0D2146-EDB3-3273-8154-B286FF1D1B2E
+  Functions: 156
+  Symbols:   605
+  CStrings:  353
 
Symbols:
+ __ZN18AppleDialogSPMIPMU19_createLpemCtrlDictEv
Functions:
~ __ZN18AppleDialogSPMIPMU5startEP9IOService : 3616 -> 3656
+ __ZN18AppleDialogSPMIPMU19_createLpemCtrlDictEv
~ __ZN18AppleDialogSPMIPMU4stopEP9IOService : 56 -> 128
~ __ZN18AppleDialogSPMIPMU13_setLpemStateEhhhhhhh : 504 -> 444
~ __ZN18AppleDialogSPMIPMU21_updateBootPropertiesEb : 2952 -> 2892
~ __ZN18AppleDialogSPMIPMU13_lpemCtrlDictEhhhhhhh : 1136 -> 980
CStrings:
+ "%s::%sFailed to create/initialize LPEM control dictionary\n"
+ "%s::%sLPEM control dictionary is uninitialized\n"
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 18:49:17 Jan  4 2026\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 18:49:17 Jan  4 2026\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 18:49:17 Jan  4 2026\n"
+ "%s::start: %s _pmuNub: %p built 18:49:17 Jan  4 2026\n"
+ "/AppleInternal/Library/BuildRoots/4~CGCqugD1Xvrcq8puBs-DB-eERanSl01uuZELwA4/Library/Caches/com.apple.xbs/Sources/AppleDialogPMU/SPMI/AppleDialogSPMIPMU.cpp"
+ "121111121222121211222222221121111122222121111112122222111"
+ "_lpemCtrlDict"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 22:43:45 Dec  5 2025\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 22:43:45 Dec  5 2025\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 22:43:45 Dec  5 2025\n"
- "%s::start: %s _pmuNub: %p built 22:43:45 Dec  5 2025\n"
- "/AppleInternal/Library/BuildRoots/4~CD2zugDT5TepYY7uxEE4IV_Hp0yRUXCadKWOeoo/Library/Caches/com.apple.xbs/Sources/AppleDialogPMU/SPMI/AppleDialogSPMIPMU.cpp"
- "12111112122212121122222222112111112222212111111212222211"

```
