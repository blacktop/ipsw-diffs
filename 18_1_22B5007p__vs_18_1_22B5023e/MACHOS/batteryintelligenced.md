## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

-91.0.0.0.0
-  __TEXT.__text: 0x1ca04
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_stubs: 0x2260
-  __TEXT.__objc_methlist: 0x1098
-  __TEXT.__cstring: 0x14e1
-  __TEXT.__objc_classname: 0x2b9
-  __TEXT.__objc_methtype: 0x4e4
-  __TEXT.__const: 0x178
-  __TEXT.__oslogstring: 0x292a
-  __TEXT.__objc_methname: 0x2b50
-  __TEXT.__gcc_except_tab: 0x1b0
+94.0.0.0.0
+  __TEXT.__text: 0x1d9b4
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__objc_stubs: 0x2360
+  __TEXT.__objc_methlist: 0x1138
+  __TEXT.__cstring: 0x153e
+  __TEXT.__objc_classname: 0x2d5
+  __TEXT.__objc_methtype: 0x506
+  __TEXT.__const: 0x188
+  __TEXT.__oslogstring: 0x2baa
+  __TEXT.__objc_methname: 0x2c83
+  __TEXT.__gcc_except_tab: 0x18c
   __TEXT.__info_plist: 0x48f
-  __TEXT.__unwind_info: 0x4b8
-  __DATA_CONST.__auth_got: 0x370
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x688
-  __DATA_CONST.__cfstring: 0x1d80
-  __DATA_CONST.__objc_classlist: 0xd8
+  __TEXT.__unwind_info: 0x4c8
+  __DATA_CONST.__auth_got: 0x3c0
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0x6b8
+  __DATA_CONST.__cfstring: 0x1de0
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__objc_arraydata: 0x338
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__objc_arrayobj: 0x288
-  __DATA_CONST.__objc_intobj: 0xa38
-  __DATA.__objc_const: 0x39c8
-  __DATA.__objc_selrefs: 0xa00
-  __DATA.__objc_ivar: 0x19c
-  __DATA.__objc_data: 0x870
+  __DATA_CONST.__objc_intobj: 0x558
+  __DATA_CONST.__objc_dictobj: 0x50
+  __DATA.__objc_const: 0x3b28
+  __DATA.__objc_selrefs: 0xa48
+  __DATA.__objc_ivar: 0x1a0
+  __DATA.__objc_data: 0x910
   __DATA.__data: 0x188
-  __DATA.__bss: 0x138
+  __DATA.__bss: 0x150
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 553
-  Symbols:   172
-  CStrings:  1131
+  Functions: 565
+  Symbols:   184
+  CStrings:  1171
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDictionary
+ __xpc_event_key_name
+ _clock_gettime_nsec_np
+ _time
+ _xpc_connection_send_message
+ _xpc_dictionary_create
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_remote_connection
+ _xpc_dictionary_get_string
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_date
+ _xpc_dictionary_set_string
+ _xpc_dictionary_set_uint64
+ _xpc_set_event
- _dispatch_after
- _dispatch_time
CStrings:
+ "Aborting inference: %!u(MISSING) %!u(MISSING)"
+ "Acknowledged %!@(MISSING)"
+ "Additional params for TT80 inference: %!@(MISSING)"
+ "Alarm set after %!g(MISSING) seconds for %!@(MISSING)!"
+ "BIXPCAlarm"
+ "BIXPCAlarm"
+ "Connected state changed during inference time to %!u(MISSING)"
+ "Date"
+ "Deleted alarms: %!@(MISSING) and %!@(MISSING)."
+ "Incorrect alarm clock type.  XPC alarm not set."
+ "Latest values for TT80 features: [%!@(MISSING) %!@(MISSING) %!@(MISSING) %!@(MISSING) %!@(MISSING)]"
+ "Monotonic"
+ "Running TT80 inference!"
+ "Setting/deleting TT80 alarm depending on current state at the start of listener."
+ "Setting/deleting TT80 alarm depending on current state when we get notified while the daemon is running."
+ "ShouldWake"
+ "Super init failed for TimeTo80Listener"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_collectionQueue"
+ "TimeTo80Listener"
+ "TimeTo80Listener"
+ "Type"
+ "Uptime"
+ "Walltime"
+ "XPC alarm triggered for %!@(MISSING)"
+ "_collectionQueue"
+ "collectionQueue"
+ "com.apple.alarm"
+ "deleteAlarmWithName:"
+ "getNameForEvent:"
+ "handleAlarmForEvent:"
+ "isEqualToNumber:"
+ "postInternalNotification"
+ "removeEvent:"
+ "runTT80ModelwithParams:andSetupNextAlarm:"
+ "second last row for TT80 features: [%!@(MISSING) %!@(MISSING) %!@(MISSING) %!@(MISSING) %!@(MISSING)]"
+ "setAlarmWithName:withClock:afterSeconds:wakeUpAP:"
+ "setCollectionQueue:"
+ "setupConnectionListenerForTT80"
+ "takeLatestSMCValuesInFeatures"
+ "tt80RunAtPlugin"
+ "tt80RunDuringChargingSession"
+ "v12@?0C8"
+ "v28@0:8@16B24"
+ "v40@0:8@16i24d28B36"
+ "xpc_dictionary_create return nil. XPC alarm not set. "
+ "xpc_object event is nil"
- "Aborting inference: %!u(MISSING) %!u(MISSING) %!u(MISSING)"
- "Unable to retrieve golden wRdc."
- "com.apple.batteryintelligenced.tt80.doinference"
- "com.apple.batteryintelligenced.tt80.waitinference"
- "distantPast"
- "tt80estimator"
- "tt80listener"

```
