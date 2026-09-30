## com.apple.driver.AppleGameControllerPersonality

> `com.apple.driver.AppleGameControllerPersonality`

```diff

-  __TEXT.__cstring: 0x22b
-  __TEXT.__os_log: 0x76
-  __TEXT_EXEC.__text: 0x1a64
+  __TEXT.__cstring: 0x235
+  __TEXT.__os_log: 0xc0
+  __TEXT_EXEC.__text: 0x1d94
   __TEXT_EXEC.__auth_stubs: 0x140
   __DATA.__data: 0xc8
   __DATA.__common: 0x88
   __DATA.__bss: 0x10
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x1510
+  __DATA_CONST.__const: 0x1388
   __DATA_CONST.__kalloc_type: 0xc0
   __DATA_CONST.__auth_got: 0xa0
   __DATA_CONST.__got: 0x70
-  Functions: 58
+  Functions: 57
   Symbols:   0
-  CStrings:  29
+  CStrings:  28
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
CStrings:
+ "AppleGCHIDUserEventDriver::handleStart(<IOHIDInterface %#010llx>)"
+ "AppleGCHIDUserEventDriver::probe(<IOHIDDevice %#010llx>)"
+ "AppleGCIOHIDEventDriverPropertyMerger"
+ "AppleGCIOHIDEventDriverPropertyMerger::probe(<IOHIDDevice %#010llx>)"
+ "Built-In"
+ "GameControllerCapabilities"
+ "GameControllerEligible"
+ "GameControllerSupport"
+ "GameControllerType"
+ "site.AppleGCIOHIDEventDriverPropertyMerger"
- "AppleGCHIDEventDummyService"
- "AppleGCHIDEventDummyService::probe()"
- "AppleGCHIDEventDummyService::probe() matched!"
- "AppleGCHIDUserEventDriver::probe()"
- "GameControllerSupportedHIDDevice"
- "GamepadHIDServiceSupport"
- "HIDRMOverride"
- "HIDServiceSupport"
- "Register"
- "com.apple."
- "site.AppleGCHIDEventDummyService"

```
