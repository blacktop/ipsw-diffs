## CoreRCPlugin

> `/System/Library/HIDPlugins/SessionFilters/CoreRCPlugin.plugin/CoreRCPlugin`

```diff

-254.120.2.0.0
-  __TEXT.__text: 0x3d6c
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_stubs: 0x7a0
+267.0.0.0.0
+  __TEXT.__text: 0x395c
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_stubs: 0x780
   __TEXT.__objc_methlist: 0x484
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x2b3
-  __TEXT.__oslogstring: 0x73d
-  __TEXT.__objc_methname: 0xc2e
+  __TEXT.__gcc_except_tab: 0x50
+  __TEXT.__cstring: 0x2d0
+  __TEXT.__oslogstring: 0x65a
+  __TEXT.__objc_methname: 0xb82
   __TEXT.__objc_classname: 0xc3
-  __TEXT.__objc_methtype: 0x555
-  __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0x420
+  __TEXT.__objc_methtype: 0x591
+  __TEXT.__unwind_info: 0x140
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__cfstring: 0x440
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0xb78
-  __DATA.__objc_selrefs: 0x390
-  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_const: 0x790
+  __DATA.__objc_selrefs: 0x398
+  __DATA.__objc_ivar: 0x4c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EF55F658-0F6E-33B8-8D48-5A2A4D308C26
-  Functions: 71
-  Symbols:   121
-  CStrings:  353
+  UUID: CECF5BBF-7964-3E89-8BCF-095CF7C2FECA
+  Functions: 68
+  Symbols:   114
+  CStrings:  340
 
Symbols:
+ __Unwind_Resume
+ ___objc_personality_v0
+ _kCABrightnessSyncNotificationHotplugState
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_release_x27
+ _objc_retain_x26
- _IOAllowPowerChange
- _IORegisterForSystemPower
- __dispatch_source_type_timer
- __powerNotificationCallback
- _dispatch_resume
- _dispatch_set_context
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _dispatch_source_set_timer
- _kCABrightnessSyncNotificationFromHotplug
- _objc_release_x9
- _objc_retainBlock
- _objc_retain_x25
CStrings:
+ "@\"<CABrightnessControl>\""
+ "_brightnessControl"
+ "cecBus:rxMessageReceived:"
+ "cecBus:txMessageSent:error:"
+ "count"
+ "syncNotificationHotplugState"
+ "unregisterSyncNotificationBlocks"
+ "v32@0:8@\"CoreCECBus\"16@\"CECMessage\"24"
+ "v40@0:8@\"CoreCECBus\"16@\"CECMessage\"24@\"NSError\"32"
- "#"
- "@\"NSObject<OS_dispatch_source>\""
- "@?"
- "Cancelling debounce, sleeping now becuase of IOPM sleep"
- "CoreRCDisplayPowerNotification in IOPM callback"
- "Error IORegisterForSystemPower failed"
- "Error failed to create dispatch timer"
- "Sending debounced sleep"
- "Sending debounced wake"
- "_debounceTimer"
- "_isPMSleep"
- "_lastNotificationWasWake"
- "_pmConnect"
- "_pmNotifier"
- "_pmPortRef"
- "_powerNotificationDebounceTime"
- "_sleepCallback"
- "_waitingForDebounce"
- "_wakeCallback"
- "deboucePowerNotification"
- "handlePowerNotificationWithService:messageType:messageArgument:"
- "powerNotificationDebounceTime"
- "v32@0:8I16I20^v24"

```
