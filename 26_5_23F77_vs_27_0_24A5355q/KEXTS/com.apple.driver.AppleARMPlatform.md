## com.apple.driver.AppleARMPlatform

> `com.apple.driver.AppleARMPlatform`

```diff

-1103.100.17.0.0
-  __TEXT.__const: 0x17f8
-  __TEXT.__os_log: 0x14f3
-  __TEXT.__cstring: 0xcfac
-  __TEXT_EXEC.__text: 0x518d0
+1145.0.0.0.0
+  __TEXT.__const: 0x1ac0
+  __TEXT.__os_log: 0x14f7
+  __TEXT.__cstring: 0xd21f
+  __TEXT_EXEC.__text: 0x55234
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6c8
-  __DATA.__common: 0xcc8
+  __DATA.__common: 0xcd8
   __DATA.__bss: 0x69
-  __DATA_CONST.__auth_got: 0x668
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x128
   __DATA_CONST.__mod_term_func: 0x128
-  __DATA_CONST.__const: 0x16a80
+  __DATA_CONST.__const: 0x16af0
   __DATA_CONST.__kalloc_var: 0x370
   __DATA_CONST.__kalloc_type: 0x1580
-  UUID: F9882088-3F36-39EF-AF03-A9AAB0483DD3
-  Functions: 2170
+  __DATA_CONST.__auth_got: 0x6b0
+  __DATA_CONST.__got: 0x1f8
+  UUID: 10A5B028-BD88-3158-AC30-0A3AB0172A9C
+  Functions: 2238
   Symbols:   0
-  CStrings:  1733
+  CStrings:  1748
 
CStrings:
+ "%s:%d: Read: M$PMP %x Lower64 %llx Upper64 %llx\n\n"
+ "11212211111111111111111111111111111111111111111111111111111111111111111111111111211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122221"
+ "1211111212221212111111222121111121"
+ "1211111212221212112121111111111111111111111121111111111111111111111111111111111111111111111111111111111111111111111111111111111212112121"
+ "AppleARMFunctionData"
+ "AppleARMFunctionDextTarget"
+ "AppleARMFunctionFunction"
+ "AppleARMFunctionSymbol"
+ "B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16"
+ "IOService::init(from, gIODTPlane)"
+ "Read: M$PMP %x Lower64 %llx Upper64 %llx\n"
+ "[%s]:%s:%d:[error] No reg prop\n"
+ "[%s]:%s:%d:[error] Wrong reg data\n"
+ "[%s]:%s:%d:[error] init failed\n"
+ "[%s]:%s:%d:[error] setSPMIConfig=0x%08x\n"
+ "_spmiControllerInterface->isValidConfig(configPtr)"
+ "configPtr != nullptr"
+ "getAppleARMFunctionUserHandler"
+ "interface"
+ "logFinishCommand"
+ "logNewCommand"
+ "pData != nullptr"
+ "pData->getLength() >= sizeof(AppleARMSPMIConfig)"
- "%s:%d: Read: M$PMP %x Lower64 %x Upper64 %x\n\n"
- "112122111111111111111111111111111111111111111111111111111111111111111111211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122221"
- "121111121222121211111222121111121"
- "12111112122212121121211111111111111111111111211111111111111111111111111111111111111111111111111111111111111111111111111212112121"
- "Read: M$PMP %x Lower64 %x Upper64 %x\n"
- "ioProvider"
- "logFinishSPMICommand"
- "logNewSPMICommand"

```
