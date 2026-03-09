## com.apple.driver.AppleUSBAudio

> `com.apple.driver.AppleUSBAudio`

```diff

-840.98.0.0.0
-  __TEXT.__cstring: 0x31aa
-  __TEXT.__const: 0x5d0
-  __TEXT_EXEC.__text: 0x70ad4
+841.2.0.0.0
+  __TEXT.__cstring: 0x332b
+  __TEXT.__const: 0x630
+  __TEXT_EXEC.__text: 0x716f0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x650

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x88
   __DATA_CONST.__mod_term_func: 0x88
-  __DATA_CONST.__const: 0x9c28
+  __DATA_CONST.__const: 0x9c50
   __DATA_CONST.__kalloc_type: 0xa00
   __DATA_CONST.__kalloc_var: 0x960
-  UUID: 8C3885AE-57DE-3A26-8FA0-312D6497687B
-  Functions: 1603
+  UUID: C19CC566-2DE0-3221-8469-837672F02485
+  Functions: 1606
   Symbols:   0
-  CStrings:  485
+  CStrings:  492
 
CStrings:
+ "Adding the voice activity detected control to interface %d"
+ "AppleUSBAudioDevice::doToggleControlChange(uVAD) to %d"
+ "AppleUSBAudioDevice::setVoiceActivityDetectState on stream %d - need to send %d to the host\n"
+ "AppleUSBAudioStream::memInterruptReceived: setting kAppleUSBAudioPropertyVoiceActivityDetectEnable to %d"
+ "secureMute"
+ "setting externalSecureMute to %d"
+ "voice activity detect enable"

```
