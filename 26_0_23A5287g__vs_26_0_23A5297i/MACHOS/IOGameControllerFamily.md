## IOGameControllerFamily

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily`

```diff

-13.0.32.0.0
+13.0.36.0.0
   __TEXT.__const: 0x470
   __TEXT.__cstring: 0xeac
-  __TEXT.__os_log: 0x1b11
-  __TEXT_EXEC.__text: 0x1ab80
+  __TEXT.__os_log: 0x1b00
+  __TEXT_EXEC.__text: 0x1ac60
   __TEXT_EXEC.__auth_stubs: 0x520
   __DATA.__data: 0xc8
   __DATA.__common: 0x240

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x4d30
   __DATA_CONST.__kalloc_type: 0x7c0
-  UUID: 67126AE6-3667-330A-8FF7-C015BFEAF29E
-  Functions: 615
-  Symbols:   830
-  CStrings:  278
+  UUID: E5265455-EDF9-37FD-BD4C-F403B2817A1A
+  Functions: 614
+  Symbols:   829
+  CStrings:  276
 
Symbols:
+ _IOCircularDataQueueMemorySize
- _OUTLINED_FUNCTION_24
CStrings:
+ "[%#010llx] #INPUT Queue Enqueue failed."
+ "[%#010llx] PSVR2SenseDeviceHIDEventServerUserClient::start(<PSVR2SenseDevice %#010llx>) for pid %i, %s"
- "[%#010llx] #INPUT Queue Enqueue failed"
- "[%#010llx] #INPUT Queue Reset -> %llu"
- "[%#010llx] Clear 'PSVR2HeldInHand'"
- "[%#010llx] Set 'PSVR2HeldInHand': Not permitted"

```
