## com.apple.driver.AppleAuthCP

> `com.apple.driver.AppleAuthCP`

```diff

-186.40.3.0.0
+186.60.2.0.0
   __TEXT.__const: 0x7c
-  __TEXT.__cstring: 0x2cc2
+  __TEXT.__cstring: 0x2e23
   __TEXT.__os_log: 0x16da
-  __TEXT_EXEC.__text: 0x1a524
+  __TEXT_EXEC.__text: 0x1a680
   __TEXT_EXEC.__auth_stubs: 0x490
   __DATA.__data: 0x188
   __DATA.__common: 0x240

   __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x18
-  Functions: 639
+  Functions: 638
   Symbols:   0
-  CStrings:  463
+  CStrings:  469
 
Functions:
~ __ZN16AppleAuthCPRelay5startEP9IOService : 1656 -> 1664
~ __ZN16AppleAuthCPRelay17_sendCommandGatedEhP6OSDataPP8OSObject : 936 -> 1168
~ __ZN16AppleAuthCPRelay28_processDeferredCommandGatedEv : 668 -> 788
~ ____ZN16AppleAuthCPRelay14_receiveActionEP25AppleAuthCPRelayInterfaceihP8OSObject_block_invoke : 256 -> 356
- __ZN16AppleAuthCPRelay17_sendCommandGatedEhP6OSDataPP8OSObject.cold.3
CStrings:
+ "%s:%s CMD=0x%x component busy, response deferred\n"
+ "%s:%s CMD=0x%x replacing outstanding deferred CMD=0x%x\n"
+ "%s:%s CMD=0x%x response dropped, no command pending (status = 0x%x, deferredCommand = 0x%x)\n"
+ "%s:%s deferred signature received, notified clients\n"
+ "%s:%s no handler for deferred CMD=0x%x, response dropped\n"
+ "%s:%s processing deferred CMD=0x%x (status = 0x%x)\n"
+ "_receiveAction_block_invoke"
- "%s:%s processing deferred CMD=0x%x \n"
```
