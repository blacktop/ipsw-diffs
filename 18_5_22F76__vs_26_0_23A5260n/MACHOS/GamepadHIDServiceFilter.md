## GamepadHIDServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/GamepadHIDServiceFilter.plugin/GamepadHIDServiceFilter`

```diff

-12.5.2.0.0
-  __TEXT.__text: 0x2388
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0x580
+13.0.28.0.0
+  __TEXT.__text: 0x36a4
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_stubs: 0x540
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x5ac
-  __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__cstring: 0x209
-  __TEXT.__oslogstring: 0x291
-  __TEXT.__objc_methname: 0xcca
-  __TEXT.__objc_classname: 0x27f
-  __TEXT.__objc_methtype: 0x8b5
-  __TEXT.__unwind_info: 0x110
-  __DATA_CONST.__auth_got: 0x1a8
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x1f8
-  __DATA_CONST.__cfstring: 0x260
+  __TEXT.__objc_methlist: 0x574
+  __TEXT.__const: 0x68
+  __TEXT.__gcc_except_tab: 0x3d4
+  __TEXT.__cstring: 0x17f
+  __TEXT.__oslogstring: 0x4db
+  __TEXT.__objc_methname: 0xc0c
+  __TEXT.__objc_classname: 0x280
+  __TEXT.__objc_methtype: 0xbbc
+  __TEXT.__unwind_info: 0x1e0
+  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0x240
+  __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x7c0
-  __DATA.__objc_selrefs: 0x3b0
-  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_const: 0x770
+  __DATA.__objc_selrefs: 0x378
+  __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x720
-  __DATA.__bss: 0xa9
+  __DATA.__bss: 0xb9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation
   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 44412538-5215-358A-9A07-D66244FA1FD2
-  Functions: 95
-  Symbols:   81
-  CStrings:  312
+  UUID: 69CB4ABF-DD8C-3F8A-8D0C-9980D07FDA5F
+  Functions: 115
+  Symbols:   95
+  CStrings:  281
 
Symbols:
+ _CFRelease
+ _IOHIDEventAppendEvent
+ _IOHIDEventCreateVendorDefinedEvent
+ _IOHIDEventGetVendorDefinedData
+ _IOHIDEventSetIntegerValue
+ _OBJC_CLASS_$_NSMutableArray
+ __ZSt9terminatev
+ ___cxa_begin_catch
+ ___gxx_personality_v0
+ __dispatch_source_type_timer
+ __os_activity_initiate
+ __os_log_debug_impl
+ _dispatch_activate
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _mach_absolute_time
+ _mach_timebase_info
+ _objc_enumerationMutation
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_unsafeClaimAutoreleasedReturnValue
- _IORegistryEntryCreateCFProperty
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSDateInterval
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSUUID
- ___kCFBooleanFalse
- ___kCFBooleanTrue
- ___objc_personality_v0
- _objc_release_x9
- _objc_retainBlock
CStrings:
+ "-> [%#x] Apply configuration."
+ "-> [%#x] Press sequence [%zu] handle event (down: %zd) -> State:%d Count:%d Next:%f"
+ "-> [%#x] Press sequence [%zu] handle tick -> State:%d Count:%d Next:%f"
+ "-> [%#x] Press sequence [%zu] not passing event: Disabled."
+ "-> [%#x] Press sequence [%zu] not passing event: Pending gesture recognizer(s)."
+ "-> [%#x] Press sequence [%zu] not passing event: Press count threshold not met."
+ "-> [%#x] Press sequence [%zu] pass event %@"
+ "-> [%#x] Press sequence [%zu] recognized 1x long press!"
+ "-> [%#x] Press sequence [%zu] recognized 1x short press!"
+ "-> [%#x] Press sequence [%zu] recognized 2x long press!"
+ "-> [%#x] Press sequence [%zu] recognized 2x short press!"
+ "-> [%#x] Press sequence [%zu] recognized 3x long press!"
+ "-> [%#x] Press sequence [%zu] recognized 3x short press!"
+ "-> [%#x] Press sequence [%zu] wakeup in %f seconds."
+ "-> [%#x] Press sequence reset -> [%zu]"
+ ".cxx_construct"
+ "@\"HIDEvent\""
+ "@\"HIDEvent\"32@0:8@\"HIDEvent\"16@\"HIDConnection\"24"
+ "Activate"
+ "Cancel"
+ "I"
+ "Resume Connection To Game Controller Daemon"
+ "_dispatchQueue"
+ "_driverService"
+ "_driverServiceID"
+ "_eventDispatcher"
+ "_eventService"
+ "_eventServiceID"
+ "_homeButton"
+ "_lastGameControllerEvent"
+ "_menuButton"
+ "_optionsButton"
+ "_setQueue:"
+ "children"
+ "copy"
+ "countByEnumeratingWithState:objects:count:"
+ "filterEvent:forClient:"
+ "filterSetProperty:forKey:forClient:"
+ "handleButton:gesture:"
+ "matchService %@ options:%@ -> %d score:%ld"
+ "options"
+ "q"
+ "requestIdleDisconnect:"
+ "sendPressForButton:"
+ "setConfiguration:forButton:"
+ "setOptions:"
+ "setTimestamp:"
+ "updateGameControllerEvent:"
+ "v20@0:8I16"
+ "v28@0:8I16Q20"
+ "v28@0:8Q16I24"
+ "v40@0:8^@16@\"NSString\"24@\"HIDConnection\"32"
+ "v40@0:8^@16@24@32"
+ "{Button=\"usage\"I\"configuration\"(GCGameIntentButtonConfiguration=\"raw\"Q\"\"{?=\"enableFilter\"b1\"shortPressGestureEnabled\"b1\"longPressGestureEnabled\"b1\"doubleShortPressGestureEnabled\"b1\"doubleLongPressGestureEnabled\"b1\"tripleShortPressGestureEnabled\"b1\"tripleLongPressGestureEnabled\"b1\"passEvents\"b1\"passAfterPressCount\"b8\"passAsGameControllerEvent\"b8\"passAfterGestureRecognizersFail\"b1})\"pressSequence\"{PressSequenceRecognizer=\"_currentPressIndex\"C\"_lastPressLength\"C\"_state\"C\"_currentPressState\"{?=\"pressEventTimestamp\"d\"releaseEventTimestamp\"d\"updateTimestamp\"d}}\"timerSource\"@\"NSObject<OS_dispatch_source>\"\"bufferedEvents\"@\"NSMutableArray\"\"report\"{?=\"down\"B\"timestamp\"Q}\"completedPressSequences\"Q}"
- "@\"HIDConnection\""
- "@\"HIDDevice\""
- "@\"NSDate\""
- "@\"NSString\""
- "@20@0:8I16"
- "FilterName"
- "Game intent gesture (long) recognized"
- "Game intent gesture (short) recognized"
- "PhysicalDeviceUniqueID"
- "Product"
- "SerialNumber"
- "ServiceFilterDebug"
- "T@\"<HIDEventDispatcher>\",W,V_dispatcher"
- "T@\"HIDConnection\",W,V_client"
- "T@\"HIDDevice\",R,N,V_device"
- "T@\"HIDEventService\",W,V_service"
- "TQ,N,V_regID"
- "Transport"
- "UUID"
- "UUIDString"
- "_activated"
- "_client"
- "_clientAdded"
- "_device"
- "_dispatcher"
- "_identifier"
- "_queue"
- "_regID"
- "_service"
- "_serviceID"
- "_shouldRunGameIntentGestureRecognizer"
- "_timeGameIntentButtonPressed"
- "_vendorName"
- "activated"
- "cancel calling cancel handler"
- "cancelHandler"
- "client"
- "clientAdded"
- "clientNotification %@ added: %d"
- "date"
- "device"
- "dispatchQueue"
- "dispatcher"
- "duration"
- "iAP"
- "identifierForService:"
- "initWithService: %@, registryID = %llu, authenticated = %@"
- "initWithStartDate:endDate:"
- "isEqualToString:"
- "listening for XPC daemon"
- "matchService %@ options: %@ score: %ld"
- "now"
- "numberWithBool:"
- "regID"
- "requestIdleDiconnect:"
- "service"
- "setCancelHandler %p"
- "setClient:"
- "setDispatchQueue %p"
- "setDispatcher:"
- "setEnableGlobalGameControllerFunctionality:"
- "setEnableGlobalGameControllerFunctionality: %d"
- "setEventDispatcher %@"
- "setObject:forKeyedSubscript:"
- "setRegID:"
- "setService:"
- "triggerGameIntentWithEvent:"
- "v24@0:8Q16"
- "v24@0:8q16"
- "\xc3"

```
