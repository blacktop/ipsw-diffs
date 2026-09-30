## IOGameControllerFamily_development

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily_development`

```diff

-13.0.32.0.0
+13.0.36.0.0
   __TEXT.__const: 0x470
   __TEXT.__cstring: 0x21c6
-  __TEXT.__os_log: 0x83d1
-  __TEXT_EXEC.__text: 0x2bac0
+  __TEXT.__os_log: 0x8455
+  __TEXT_EXEC.__text: 0x2bc74
   __TEXT_EXEC.__auth_stubs: 0x520
   __DATA.__data: 0xc8
   __DATA.__common: 0x268

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x5558
   __DATA_CONST.__kalloc_type: 0x800
-  UUID: BBE9FBF8-E3A5-3554-808E-9640AAD29406
-  Functions: 890
+  UUID: 00CD702E-8812-397E-B2D9-B60EB25DBF08
+  Functions: 889
   Symbols:   1993
-  CStrings:  576
+  CStrings:  577
 
Symbols:
+ _IOCircularDataQueueMemorySize
+ __ZZN40PSVR2SenseDeviceHIDEventServerUserClient5startEP9IOServiceE11_os_log_fmt_5
- _OUTLINED_FUNCTION_33
- _ZN16PSVR2SenseDevice20handleSenseInputDataEPK19PSVR2SenseInputDataR18InputReportContext.cold.2
CStrings:
+ "[%#010llx] #INPUT Queue Enqueue failed."
+ "[%#010llx] #INPUT Queue Reset (%#x // %llu): %llu -> %llu"
+ "[%#010llx] PSVR2SenseDeviceHIDEventServerUserClient::start(<PSVR2SenseDevice %#010llx>) for pid %i, %s"
+ "[%#010llx] Set 'PSVR2HeldInHand': %hhi -> %hhi"
- "[%#010llx] #INPUT Queue Enqueue failed"
- "[%#010llx] #INPUT Queue Reset -> %llu"
- "[%#010llx] Set 'PSVR2HeldInHand': %hhi"

```
