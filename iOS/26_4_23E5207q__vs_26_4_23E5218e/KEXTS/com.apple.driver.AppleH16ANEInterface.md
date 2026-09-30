## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-9.510.2.0.0
+9.510.3.0.0
   __TEXT.__const: 0xd50
   __TEXT.__cstring: 0x11307
-  __TEXT.__os_log: 0x36e65
-  __TEXT_EXEC.__text: 0x1098a4
+  __TEXT.__os_log: 0x36f2e
+  __TEXT_EXEC.__text: 0x109a94
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4350
   __DATA.__common: 0x680

   __DATA_CONST.__const: 0xcbf8
   __DATA_CONST.__kalloc_type: 0x3b00
   __DATA_CONST.__kalloc_var: 0x3200
-  UUID: D3FBC5B6-8907-36B0-B321-324D20C82479
+  UUID: AD79BDE1-F070-33F9-B5CA-FD5E911B06A1
   Functions: 3577
   Symbols:   0
-  CStrings:  4470
+  CStrings:  4473
 
Functions:
~ __ZN11ANEHWDevice26aneExclaveInterruptHandlerEP22IOInterruptEventSourcei : 1152 -> 1648
CStrings:
+ "%s: %s: Added error token (UUID=0) for Exclave notification\n"
+ "/Library/Caches/com.apple.xbs/E208659B-7545-4563-9C74-1A2F43F20C63/TemporaryDirectory.tdASkp/Sources/AppleH11ANEInterface/ANEResource/ANEProgramRTResource.h"
+ "/Library/Caches/com.apple.xbs/E208659B-7545-4563-9C74-1A2F43F20C63/TemporaryDirectory.tdASkp/Sources/AppleH11ANEInterface/ANEScheduler/ANEEvent.cpp"
+ "/Library/Caches/com.apple.xbs/E208659B-7545-4563-9C74-1A2F43F20C63/TemporaryDirectory.tdASkp/Sources/AppleH11ANEInterface/aneexclave/ANELoader/src/ZinComputeProgramLoader.cpp"
+ "[ERROR] %s: %s: Exclave ITQ error: 0x%x (code: %u), ITQ reg: 0x%x, queue: %lld/%d\n"
+ "[ERROR] %s: %s: Invalid ITQ interrupt to AP (ITQ reg = 0x%x)\n"
+ "[ERROR] %s: %s: Token queue full - dropping %d completions!\n"
- "%s: %s: Too many pending requests, query deferred until next ITQ\n"
- "/Library/Caches/com.apple.xbs/9233B11A-3790-4E45-AF72-9B62140F6FD0/TemporaryDirectory.XuNeG8/Sources/AppleH11ANEInterface/ANEResource/ANEProgramRTResource.h"
- "/Library/Caches/com.apple.xbs/9233B11A-3790-4E45-AF72-9B62140F6FD0/TemporaryDirectory.XuNeG8/Sources/AppleH11ANEInterface/ANEScheduler/ANEEvent.cpp"
- "/Library/Caches/com.apple.xbs/9233B11A-3790-4E45-AF72-9B62140F6FD0/TemporaryDirectory.XuNeG8/Sources/AppleH11ANEInterface/aneexclave/ANELoader/src/ZinComputeProgramLoader.cpp"

```
