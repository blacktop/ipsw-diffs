## libPN548_API.dylib

> `/usr/lib/libPN548_API.dylib`

```diff

-353.4.0.0.0
-  __TEXT.__text: 0x40288
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__const: 0x6c4
-  __TEXT.__cstring: 0xa2f1
-  __TEXT.__oslogstring: 0x7160
-  __TEXT.__unwind_info: 0x578
+354.19.0.0.0
+  __TEXT.__text: 0x4065c
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__const: 0x700
+  __TEXT.__cstring: 0xa4c5
+  __TEXT.__oslogstring: 0x7314
+  __TEXT.__unwind_info: 0x540
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x13e0
-  __AUTH_CONST.__auth_got: 0x658
-  __AUTH_CONST.__const: 0x298
+  __DATA_CONST.__const: 0x1408
+  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__const: 0x2d0
   __AUTH_CONST.__cfstring: 0x6c0
   __DATA.__data: 0x18
   __DATA.__bss: 0x21

   - /usr/lib/libNFC_HAL.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  Functions: 405
-  Symbols:   329
-  CStrings:  1733
+  Functions: 392
+  Symbols:   334
+  CStrings:  1748
 
Symbols:
+ _NFDriverInvalidateProhibitTimer
+ _NFHardwareSkipSpmiReconfig
+ _dispatch_after
+ _dispatch_get_global_queue
+ _phLibNfc_Mgt_InvalidateSeRmProhibitTimer
CStrings:
+ "%s:%i ***WARNING*** Express mode is requested; express won't work under this config!!!"
+ "%s:%i Compensation applied, poll phase duration (ms): %d"
+ "%s:%i Failed to set ECP Frame"
+ "%s:%i Failed to set serial log state : %u"
+ "%s:%i Invalid prohibit timer ID - command not supported"
+ "%s:%i No compensation applied due to underflow, poll phase duration (ms): %d"
+ "%s:%i Queuing exit due to timeout"
+ "%s:%i Running build from (B&I) Stockholm_Base-354.19"
+ "%s:%i Warning : Standby disabled - skipping enablement."
+ "%s:%i Warning : Standby disabled."
+ "%s:%i timerID=%s, remaining=%dms"
+ "%s:%i wantsFieldDetect=%d wantsPolling=%d wantsExpress=%d eSE=%d host=%d wantsEcpUpdate=%d"
+ "%{public}s:%i ***WARNING*** Express mode is requested; express won't work under this config!!!"
+ "%{public}s:%i Compensation applied, poll phase duration (ms): %d"
+ "%{public}s:%i Failed to set ECP Frame"
+ "%{public}s:%i Failed to set serial log state : %u"
+ "%{public}s:%i Invalid prohibit timer ID - command not supported"
+ "%{public}s:%i No compensation applied due to underflow, poll phase duration (ms): %d"
+ "%{public}s:%i Queuing exit due to timeout"
+ "%{public}s:%i Running build from (B&I) Stockholm_Base-354.19"
+ "%{public}s:%i Warning : Standby disabled - skipping enablement."
+ "%{public}s:%i Warning : Standby disabled."
+ "%{public}s:%i timerID=%s, remaining=%dms"
+ "%{public}s:%i wantsFieldDetect=%d wantsPolling=%d wantsExpress=%d eSE=%d host=%d wantsEcpUpdate=%d"
+ "ECP Frame"
+ "NFDriverInvalidateProhibitTimer"
+ "NFDriverRedactLogging"
+ "_NFDriverDisableStandby"
- "%s:%i LPCD Reference:0x%X, AGC Measured:0x%X"
- "%s:%i RM SE init required"
- "%s:%i RM prohibit timer activated"
- "%s:%i Running build from (B&I) Stockholm_Base-353.4"
- "%s:%i timerID=%s, remaning=%dms"
- "%s:%i wantsFieldDetect=%d wantsPolling=%d wantsExpress=%d eSE=%d host=%d"
- "%{public}s:%i LPCD Reference:0x%X, AGC Measured:0x%X"
- "%{public}s:%i RM SE init required"
- "%{public}s:%i RM prohibit timer activated"
- "%{public}s:%i Running build from (B&I) Stockholm_Base-353.4"
- "%{public}s:%i timerID=%s, remaning=%dms"
- "%{public}s:%i wantsFieldDetect=%d wantsPolling=%d wantsExpress=%d eSE=%d host=%d"
- "Unknown"

```
