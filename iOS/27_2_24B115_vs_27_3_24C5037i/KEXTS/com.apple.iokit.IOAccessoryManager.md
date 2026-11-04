## com.apple.iokit.IOAccessoryManager

> `com.apple.iokit.IOAccessoryManager`

```diff

-1068.40.6.0.0
+1068.60.2.0.0
   __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0x11078
-  __TEXT.__os_log: 0x121fe
-  __TEXT_EXEC.__text: 0xe0c6c
+  __TEXT.__cstring: 0x111c5
+  __TEXT.__os_log: 0x12409
+  __TEXT_EXEC.__text: 0xe1458
   __TEXT_EXEC.__auth_stubs: 0xbb0
   __DATA.__data: 0x7e8
   __DATA.__common: 0x16b8
   __DATA_CONST.__mod_init_func: 0x348
   __DATA_CONST.__mod_term_func: 0x340
-  __DATA_CONST.__const: 0x2ac98
+  __DATA_CONST.__const: 0x2acd8
   __DATA_CONST.__kalloc_type: 0x2500
   __DATA_CONST.__auth_got: 0x5d8
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__auth_ptr: 0x20
-  Functions: 5013
+  Functions: 5019
   Symbols:   0
-  CStrings:  2963
+  CStrings:  2975
 
CStrings:
+ "%s::%s(): ConfigStream info changed\n"
+ "%s:IOAccessoryConfigStreamInterface::%s accessory info strings are final \n"
+ "%s:IOAccessoryHIDDeviceInterface::%s deferring endpoint publication, ConfigStream enumerating (deadline %d s) \n"
+ "%s:IOAccessoryHIDDeviceInterface::%s publishing %u endpoint(s), ConfigStream complete=%d, deadlineReached=%d \n"
+ "12111112122212121121211122111211112"
+ "IOAccessoryConfigStreamEnumerationComplete"
+ "[ERROR] %s:IOAccessoryHIDDeviceInterface::%s could not arm ConfigStream deadline, publishing now \n"
+ "[ERROR] %s:IOAccessoryHIDDeviceInterface::%s could not create ConfigStream deadline timer \n"
+ "[ERROR] %s:IOAccessoryHIDDeviceInterface::%s failed to publish endpoints! ret %#x \n"
+ "[ERROR] %s:IOAccessoryHIDDeviceInterface::configStreamDeadline ConfigStream did not finish enumerating within %d s, publishing anyway \n"
+ "_armEndpointPublishGated"
+ "_publishEndpointsGated"
+ "_signalAccessoryInfoComplete"
+ "start_block_invoke_5"
+ "start_block_invoke_6"
- "121111121222121211212111221112112"
- "_handleStartGated_block_invoke_2"
- "start_block_invoke_3"
```
