## com.apple.iokit.IOUSBDeviceFamily

> `com.apple.iokit.IOUSBDeviceFamily`

```diff

-847.100.26.0.0
-  __TEXT.__cstring: 0x2bc1
+891.0.0.0.0
+  __TEXT.__cstring: 0x33f8
   __TEXT.__const: 0x260
-  __TEXT.__os_log: 0x1b09
-  __TEXT_EXEC.__text: 0x27bd8
+  __TEXT.__os_log: 0x21fc
+  __TEXT_EXEC.__text: 0x2accc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x218
   __DATA.__bss: 0x28
-  __DATA_CONST.__auth_got: 0x378
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x3760
   __DATA_CONST.__kalloc_type: 0x6c0
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: A94C7679-13B8-3B9A-9DCB-4593704E1DE0
-  Functions: 730
+  __DATA_CONST.__auth_got: 0x380
+  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__auth_ptr: 0x8
+  UUID: EDFEB4BD-9419-3050-91A4-7596060C3050
+  Functions: 739
   Symbols:   0
-  CStrings:  489
+  CStrings:  553
 
CStrings:
+ "%s@%s: %s::%s: %d function(s) failed to register within timeout\n"
+ "%s@%s: %s::%s: Activating ncmAuxOnly fallback configuration\n"
+ "%s@%s: %s::%s: Added failed function to BOS descriptor: %s (string index %d)\n"
+ "%s@%s: %s::%s: All functions registered - cancelling timeout timer\n"
+ "%s@%s: %s::%s: Already in ncmAuxOnly fallback mode but %d function(s) still failed to register - giving up\n"
+ "%s@%s: %s::%s: Creating failed functions capability descriptor for %d failed functions\n"
+ "%s@%s: %s::%s: Driver registration timeout triggered\n"
+ "%s@%s: %s::%s: Failed functions capability descriptor size limit reached\n"
+ "%s@%s: %s::%s: Failed to allocate FD capability descriptor\n"
+ "%s@%s: %s::%s: Failed to allocate config dictionary\n"
+ "%s@%s: %s::%s: Failed to allocate configurations array\n"
+ "%s@%s: %s::%s: Failed to allocate interfaces array\n"
+ "%s@%s: %s::%s: Failed to build fallback device description - unable to proceed with fallback configuration\n"
+ "%s@%s: %s::%s: Failed to copy device description\n"
+ "%s@%s: %s::%s: Failed to create config attributes\n"
+ "%s@%s: %s::%s: Failed to create config description\n"
+ "%s@%s: %s::%s: Failed to create fallback USB device: 0x%x\n"
+ "%s@%s: %s::%s: Failed to create interface name strings\n"
+ "%s@%s: %s::%s: Failed to get current device description\n"
+ "%s@%s: %s::%s: Found failed NCM interface: %s\n"
+ "%s@%s: %s::%s: NCM interfaces are in the failed functions list - cannot fallback to NCM-only configuration. Giving up with %d function(s) unregistered\n"
+ "%s@%s: %s::%s: No failed functions to add to BOS descriptor\n"
+ "%s@%s: %s::%s: Successfully added failed functions capability descriptor to BOS (length=%d)\n"
+ "%s@%s: %s::%s: Successfully built fallback device description\n"
+ "%s@%s: %s::%s: Successfully created ncmAuxOnly fallback configuration\n"
+ "%s@%s: %s::%s: Unregistered function: %s\n"
+ "12111112122212121112122122222221221222211212111111121212222211222222222222222222222222222222222222222222222222222222222222222112222222222"
+ "A745B2DF-FB29-4E45-844D-BEFD6D125F9A"
+ "AppleUSBNCM"
+ "AppleUSBNCMControlAux"
+ "AppleUSBNCMDataAux"
+ "Fallback Configuration - ncmAux"
+ "activateFallbackConfiguration"
+ "addFailedFunctionsCapabilityDescriptor"
+ "buildFallbackDeviceDescription"
+ "handleUnregisteredFunctionsTimeout"
+ "hasFailedNCMFunctions"
+ "ncmAuxOnly_fallback"
+ "recordFailedFunctions"
- "12111112122212121112122122222221221222211212111111121222221222222222222222222222222222222222222222222222222222222222222222112222222222"

```
