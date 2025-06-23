## com.apple.driver.AppleEventLogHandler

> `com.apple.driver.AppleEventLogHandler`

```diff

-1774.0.4.0.0
-  __TEXT.__cstring: 0x533
-  __TEXT_EXEC.__text: 0x16dc
+1774.0.7.0.0
+  __TEXT.__cstring: 0x68b
+  __TEXT_EXEC.__text: 0x16d0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
-  __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 545EA159-60D4-3B0D-A14B-253883897D40
-  Functions: 49
+  __DATA_CONST.__kalloc_var: 0xa0
+  UUID: 6A536D09-8A2F-3E60-BE40-CC57227D7710
+  Functions: 52
   Symbols:   0
-  CStrings:  40
+  CStrings:  46
 
CStrings:
+ "\"AppleEventLogHandler: Register is locked down! AccessType=%s Address=0x%llx IntrID=%x RegMapID=%x Deferred=%s\" @%s:%d"
+ "112"
+ "12111112122212121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111112111122"
+ "AppleEventLogHandler: Register is locked down! AccessType=%s Address=0x%llx IntrID=%x RegMapID=%x Deferred=%s\n"
+ "EventLog %u: AccessType=%s Address=0x%llx\n"
+ "False"
+ "Setting EventLog panic timeout to %u ms\n"
+ "True"
+ "_eventLogPanicTimer->setTimeoutMS(_eventLogPanicTimeoutMS) == kIOReturnSuccess"
+ "_interruptFilterEventSource"
+ "_interruptFilterEventSource[i]"
+ "_regMapData"
+ "_regMapData[i].physicalAddress"
+ "_regMapData[i].regMap"
+ "_regMapData[i].virtualAddress"
+ "site.IOFilterInterruptEventSource *"
+ "site.RegMapData"
+ "void AppleEventLogHandler::_handleEventLogInterrupt(EventLogID, bool)"
- "\"AppleEventLogHandler: Register is locked down! AccessType=%s Address=0x%llx IntrID=%x RegMapID=%x\" @%s:%d"
- "121111121222121211111111111111111111111111111111111111111111111111111111111111111211111211122"
- "AppleEventLogHandler: Register is locked down! AccessType=%s Address=0x%llx IntrID=%x RegMapID=%x\n"
- "_interruptEventSource"
- "_interruptEventSource[i]"
- "_regMaps"
- "_regMaps[i]"
- "event"
- "site.Event"
- "site.IOInterruptEventSource *"
- "site.IOMemoryMap *"
- "void AppleEventLogHandler::_handleEventLogInterrupt(EventLogID)"

```
