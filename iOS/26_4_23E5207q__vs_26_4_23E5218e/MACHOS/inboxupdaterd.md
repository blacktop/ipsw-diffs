## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

-176.100.32.0.0
-  __TEXT.__text: 0x7c670
+176.100.41.0.0
+  __TEXT.__text: 0x7c87c
   __TEXT.__auth_stubs: 0x1330
-  __TEXT.__objc_stubs: 0x7340
-  __TEXT.__objc_methlist: 0x3710
-  __TEXT.__cstring: 0x451f
-  __TEXT.__objc_methname: 0x749f
+  __TEXT.__objc_stubs: 0x7360
+  __TEXT.__objc_methlist: 0x3728
+  __TEXT.__cstring: 0x4531
+  __TEXT.__objc_methname: 0x7509
   __TEXT.__objc_classname: 0x593
   __TEXT.__objc_methtype: 0x1382
-  __TEXT.__const: 0x6f78
-  __TEXT.__oslogstring: 0x83b7
-  __TEXT.__gcc_except_tab: 0x1850
+  __TEXT.__const: 0x6f98
+  __TEXT.__oslogstring: 0x8531
+  __TEXT.__gcc_except_tab: 0x1864
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1e70
+  __TEXT.__unwind_info: 0x1e78
   __DATA_CONST.__auth_got: 0x9a8
   __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xcdc0
-  __DATA_CONST.__cfstring: 0x3c20
+  __DATA_CONST.__const: 0xcdc8
+  __DATA_CONST.__cfstring: 0x3c40
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_intobj: 0x18c0
-  __DATA_CONST.__objc_arraydata: 0x490
-  __DATA_CONST.__objc_arrayobj: 0x570
+  __DATA_CONST.__objc_intobj: 0x18f0
+  __DATA_CONST.__objc_arraydata: 0x498
+  __DATA_CONST.__objc_arrayobj: 0x588
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x8218
-  __DATA.__objc_selrefs: 0x2140
-  __DATA.__objc_ivar: 0x38c
+  __DATA.__objc_const: 0x8248
+  __DATA.__objc_selrefs: 0x2150
+  __DATA.__objc_ivar: 0x390
   __DATA.__objc_data: 0xd20
   __DATA.__data: 0x1ce0
   __DATA.__bss: 0x138

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 54D5FE05-926A-3579-AF70-9559918A14BF
-  Functions: 3558
+  UUID: 263AA3EB-5EF1-3CE2-9A62-2001C4491B14
+  Functions: 3559
   Symbols:   441
-  CStrings:  3653
+  CStrings:  3658
 
CStrings:
+ "%{public}@: Received command %{public}ld at state %{public}ld; resetting idle timer..."
+ "%{public}@: Received command %{public}ld at state %{public}ld; resetting install timer..."
+ "%{public}@: changing device state from %{public}lu to %{public}lu"
+ "%{public}@: state changed from %{public}lu to %{public}lu"
+ "Acquired power assertion ID: %{public}u"
+ "All BT payload received: %{public}ld/%{public}hu"
+ "Attempting to connect to WiFi (attempt %{public}lu)..."
+ "Bluetooth server listening on 0x%{public}hx"
+ "Current ongoing operation code is %{public}lu"
+ "Current system time is %{public}lu; setting system time to %{public}lu"
+ "DataCollector: start to collect thermal data every %{public}ld seconds"
+ "Diagnostics operation, verifying tag: %{public}c%{public}c%{public}c%{public}c "
+ "Failed to read info for key: %{public}@; ret: 0x%{public}X; smc ret: 0x%{public}X"
+ "Ignoring tag: %{public}c%{public}c%{public}c%{public}c of type: 0x%{public}x..."
+ "MulticastKeysBlob"
+ "Reading BT payload: %{public}ld/%{public}hu"
+ "Received Command %{public}ld over BT"
+ "Setting device to LPM mode; scanWindow = 0x%{public}X; scanInterval = 0x%{public}X"
+ "Setting system time stamp: %{public}lu"
+ "Software update download phase: %{public}@; progress: %{public}f; normalized progress: %{public}f; time remaining: %{public}lf"
+ "Starting Idle timer with %{public}lfs timeout..."
+ "T@\"NSData\",&,N,V_multicastKeysBlob"
+ "Update operation, verifying tag: %{public}c%{public}c%{public}c%{public}c "
+ "Verifying tag: %{public}c%{public}c%{public}c%{public}c of type: 0x%{public}x..."
+ "Waiting %{public}ds for network connection..."
+ "_multicastKeysBlob"
+ "initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:"
+ "multicastKeysBlob"
+ "setMulticastKeysBlob:"
- "%@: Received command %ld at state %ld; resetting idle timer..."
- "%@: Received command %ld at state %ld; resetting install timer..."
- "%{public}@: changing device state from %lu to %lu"
- "%{public}@: state changed from %lu to %lu"
- "Acquired power assertion ID: %u"
- "All BT payload received: %ld/%hu"
- "Attempting to connect to WiFi (attempt %lu)..."
- "Bluetooth server listening on 0x%hx"
- "Current ongoing operation code is %lu"
- "Current system time is %lu; setting system time to %lu"
- "DataCollector: start to collect thermal data every %ld seconds"
- "Diagnostics operation, verifying tag: %c%c%c%c "
- "Failed to read info for key: %{public}@; ret: 0x%X; smc ret: 0x%X"
- "Ignoring tag: %c%c%c%c of type: 0x%x..."
- "Reading BT payload: %ld/%hu"
- "Received Command %ld over BT"
- "Setting device to LPM mode; scanWindow = 0x%X; scanInterval = 0x%X"
- "Setting system time stamp: %lu"
- "Software update download phase: %{public}@; progress: %f; normalized progress: %f; time remaining: %lf"
- "Starting Idle timer with %lfs timeout..."
- "Update operation, verifying tag: %c%c%c%c "
- "Verifying tag: %c%c%c%c of type: 0x%x..."
- "Waiting %ds for network connection..."
- "inboxupdaterd started"
- "initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:"

```
