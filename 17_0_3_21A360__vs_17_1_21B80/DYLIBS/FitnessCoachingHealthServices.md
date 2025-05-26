## FitnessCoachingHealthServices

> `/System/Library/PrivateFrameworks/FitnessCoachingHealthServices.framework/FitnessCoachingHealthServices`

```diff

-133.0.0.0.0
-  __TEXT.__text: 0xb138
+137.3.0.0.0
+  __TEXT.__text: 0xb8b0
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x9bc
+  __TEXT.__objc_methlist: 0x9ec
   __TEXT.__const: 0x68
-  __TEXT.__oslogstring: 0x1e9b
-  __TEXT.__cstring: 0x2ea
+  __TEXT.__oslogstring: 0x2007
+  __TEXT.__cstring: 0x341
   __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__unwind_info: 0x3a4
-  __TEXT.__objc_classname: 0x337
-  __TEXT.__objc_methname: 0x29d3
+  __TEXT.__unwind_info: 0x3c0
+  __TEXT.__objc_classname: 0x339
+  __TEXT.__objc_methname: 0x2ab7
   __TEXT.__objc_methtype: 0xa12
-  __TEXT.__objc_stubs: 0x2380
+  __TEXT.__objc_stubs: 0x2460
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x36b0
-  __DATA_CONST.__objc_selrefs: 0x9d8
+  __DATA_CONST.__objc_const: 0x36d0
+  __DATA_CONST.__objc_selrefs: 0xa10
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__objc_const: 0x480
-  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__cfstring: 0x380
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__const: 0x80

   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x190
   __DATA.__objc_superrefs: 0x70
-  __DATA.__objc_ivar: 0x110
+  __DATA.__objc_ivar: 0x114
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x4b0

   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 265
-  Symbols:   1306
-  CStrings:  701
+  Functions: 275
+  Symbols:   1336
+  CStrings:  719
 
Symbols:
+ -[FCGoalProgressCoordinator _onqueue_unscheduleEventIdentifiers:]
+ -[FCGoalProgressStore clearScheduledEventIdentifiers]
+ -[FCGoalProgressStore scheduledEventIdentifiers]
+ -[FCGoalProgressStore scheduledEventIdentifiers].cold.1
+ -[FCGoalProgressStore storeScheduledEventIdentifiers:]
+ -[FCGoalProgressStore storeScheduledEventIdentifiers:].cold.1
+ _OBJC_IVAR_$_FCGoalProgressCoordinator._typicalDayModelLoaded
+ ___54-[FCGoalProgressCoordinator _onqueue_rescheduleEvents]_block_invoke.232
+ ___54-[FCGoalProgressCoordinator _onqueue_rescheduleEvents]_block_invoke_2
+ ___block_descriptor_40_e29_B24?0"NSString"8"NSDate"16l
+ ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32s_e33_v32?0"NSString"8"NSDate"16^B24ls32l8
+ _objc_msgSend$_onqueue_unscheduleEventIdentifiers:
+ _objc_msgSend$clearScheduledEventIdentifiers
+ _objc_msgSend$hk_filter:
+ _objc_msgSend$propertyListValueForKey:error:
+ _objc_msgSend$scheduledEventIdentifiers
+ _objc_msgSend$setPropertyListValue:forKey:error:
+ _objc_msgSend$storeScheduledEventIdentifiers:
- ___block_descriptor_48_e8_32s_e33_v32?0"NSString"8"NSDate"16^B24ls32l8
CStrings:
+ "\x04\x13\x11"
+ "AQ"
+ "B16@?0@\"NSString\"8"
+ "B24@?0@\"NSString\"8@\"NSDate\"16"
+ "Canceling scheduled event identifier %@"
+ "Failed to fetch scheduled goal progress event identifiers %{public}@, error %{public}@"
+ "Failed to store scheduled goal progress event identifiers %{public}@, error %{public}@"
+ "Loaded typical day model"
+ "Rescheduling goal progress if needed"
+ "Rescheduling now that typical day model has loaded"
+ "Typical day model has not loaded yet"
+ "_onqueue_unscheduleEventIdentifiers:"
+ "_typicalDayModelLoaded"
+ "clearScheduledEventIdentifiers"
+ "goalProgressScheduledEventIdentifiers"
+ "hk_filter:"
+ "propertyListValueForKey:error:"
+ "scheduledEventIdentifiers"
+ "setPropertyListValue:forKey:error:"
+ "storeScheduledEventIdentifiers:"
- "\x04\x14"
- "AA"

```
