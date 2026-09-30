## com.apple.driver.ApplePearlSEPDriver

> `com.apple.driver.ApplePearlSEPDriver`

```diff

-877.100.21.0.0
+877.120.2.0.0
   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0xa992
-  __TEXT.__os_log: 0x498f
-  __TEXT_EXEC.__text: 0x3d2bc
+  __TEXT.__cstring: 0xadd0
+  __TEXT.__os_log: 0x4abd
+  __TEXT_EXEC.__text: 0x3df94
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcd
   __DATA.__common: 0x1d8

   __DATA_CONST.__got: 0x150
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x2050
+  __DATA_CONST.__const: 0x2058
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: AA4F1DA6-8096-30EB-91AB-CEB192E770F4
-  Functions: 655
+  UUID: 29B24457-7BA7-3882-80D6-DEFC108BCE59
+  Functions: 664
   Symbols:   0
-  CStrings:  1677
+  CStrings:  1696
 
CStrings:
+ "%s <- _analyticsCurrentEvent: %d _proxState:%d\n"
+ "%s <- _analyticsCurrentEvent: %d _proxState:%d newState:%d \n"
+ "%s <- _proxState:%d\n"
+ "%s <- newState:%d\n"
+ "%s: Waiting for prox state to clear...\n"
+ "12111112122212121121211111111111111111111121121122222222122211222222221211121111121222211121211122222222222221122222222221221112111211222111222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222122122222222121222222222212221222222222222222212121122222222122122212211112222222211212222311122212212211111111111211222111221"
+ "ProxStateChanged"
+ "__os_warn_unused(__builtin_sub_overflow((mach_continuous_time()), (_analyticsFaceDetectEvent.analyticsFaceDetectStartTime), (&_analyticsFaceDetectEvent.analyticsFaceDetectProxStateInfo.proxClearedEndTime))) == 0 "
+ "__os_warn_unused(__builtin_sub_overflow((mach_continuous_time()), (_analyticsFaceDetectEvent.analyticsFaceDetectStartTime), (&_analyticsFaceDetectEvent.analyticsFaceDetectProxStateInfo.proxFirstSampleEndTime))) == 0 "
+ "__os_warn_unused(__builtin_sub_overflow((mach_continuous_time()), (_analyticsMatchEvent.analyticsMatchStartTime), (&_analyticsMatchEvent.analyticsMatchProxStateInfo.proxClearedEndTime))) == 0 "
+ "__os_warn_unused(__builtin_sub_overflow((mach_continuous_time()), (_analyticsMatchEvent.analyticsMatchStartTime), (&_analyticsMatchEvent.analyticsMatchProxStateInfo.proxFirstSampleEndTime))) == 0 "
+ "_proxStateUpdateTimerEventSource"
+ "analyticsProxStateChanged"
+ "analyticsProxStateHandleClear"
+ "checkProxStateAtOperationStart"
+ "clearOperationProxState"
+ "handleClearProxState"
+ "proxStateChanged"
+ "proxStateUpdateTimerHandler"
+ "selectSecureFaceDetectFlowForFdet"
- "121111121222121211212111111111111111111111211211222222221222112222222212111211111212222111212111222222222222211222222222212211121112112221112222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222212212222222212122222222221222122222222222222221212112222222212212221221111222222221121222231112221221221111111111121122211122"

```
