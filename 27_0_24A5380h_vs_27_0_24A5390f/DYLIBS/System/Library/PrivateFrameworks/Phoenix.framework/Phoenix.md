## Phoenix

> `/System/Library/PrivateFrameworks/Phoenix.framework/Phoenix`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__objc_ivar`

```diff

-3234.5.0.0.0
-  __TEXT.__text: 0x22b94
-  __TEXT.__objc_methlist: 0x1d5c
+3237.1.0.0.0
+  __TEXT.__text: 0x22bd4
+  __TEXT.__objc_methlist: 0x1dac
   __TEXT.__const: 0xb0
   __TEXT.__dlopen_cstrs: 0x4b
-  __TEXT.__gcc_except_tab: 0x150
-  __TEXT.__cstring: 0x249f
-  __TEXT.__oslogstring: 0x1ecb
-  __TEXT.__unwind_info: 0x8a8
+  __TEXT.__gcc_except_tab: 0x14c
+  __TEXT.__cstring: 0x242d
+  __TEXT.__oslogstring: 0x1eaf
+  __TEXT.__unwind_info: 0x8b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x700
   __DATA_CONST.__objc_classlist: 0x110
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1340
+  __DATA_CONST.__objc_selrefs: 0x1370
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__got: 0x2f8
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x18e0
-  __AUTH_CONST.__objc_const: 0x3a70
+  __AUTH_CONST.__objc_const: 0x3b10
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x348
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH.__objc_data: 0xaa0
   __DATA.__objc_ivar: 0x300
-  __DATA.__data: 0x548
+  __DATA.__data: 0x5a8
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
+  - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 622
-  Symbols:   1905
-  CStrings:  465
+  Functions: 624
+  Symbols:   1912
+  CStrings:  461
 
Symbols:
+ -[AXPhoenixDisplayStatusMonitor _startObservingAggregateBacklight]
+ -[AXPhoenixDisplayStatusMonitor _stopObservingAggregateBacklight]
+ -[AXPhoenixDisplayStatusMonitor aggregateBacklight]
+ -[AXPhoenixDisplayStatusMonitor backlight:didCompleteUpdateToState:forEvent:]
+ -[AXPhoenixDisplayStatusMonitor setAggregateBacklight:]
+ GCC_except_table479
+ GCC_except_table539
+ _BLSBacklightStateIsActive
+ _NSStringFromBLSBacklightState
+ _OBJC_CLASS_$_BLSBacklight
+ _OBJC_CLASS_$_BLSDisplayReference
+ _OBJC_IVAR_$_AXPhoenixDisplayStatusMonitor._aggregateBacklight
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BLSBacklightStateObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSBacklightStateObserving
+ __OBJC_$_PROTOCOL_REFS_BLSBacklightStateObserving
+ __OBJC_CLASS_PROTOCOLS_$_AXPhoenixDisplayStatusMonitor
+ __OBJC_LABEL_PROTOCOL_$_BLSBacklightStateObserving
+ __OBJC_PROTOCOL_$_BLSBacklightStateObserving
+ ___77-[AXPhoenixDisplayStatusMonitor backlight:didCompleteUpdateToState:forEvent:]_block_invoke
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___os_log_helper_16_2_3_8_32_8_66_8_66
+ ___os_log_helper_16_2_4_8_32_8_66_8_66_8_66
+ _objc_msgSend$_startObservingAggregateBacklight
+ _objc_msgSend$_stopObservingAggregateBacklight
+ _objc_msgSend$aggregateBacklight
+ _objc_msgSend$backlightState
+ _objc_msgSend$referenceForAggregateDisplay
+ _objc_msgSend$setAggregateBacklight:
+ _objc_msgSend$sharedBacklightForDisplay:
- -[AXPhoenixDisplayStatusMonitor _queryIsDisplayOn]
- -[AXPhoenixDisplayStatusMonitor _registerForSpringboardNotificationsWithQueue:]
- -[AXPhoenixDisplayStatusMonitor _unregisterForSpringboardNotifications]
- -[AXPhoenixDisplayStatusMonitor notifyToken]
- -[AXPhoenixDisplayStatusMonitor setNotifyToken:]
- GCC_except_table481
- GCC_except_table537
- _OBJC_IVAR_$_AXPhoenixDisplayStatusMonitor._notifyToken
- ___79-[AXPhoenixDisplayStatusMonitor _registerForSpringboardNotificationsWithQueue:]_block_invoke
- ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
- _notify_cancel
- _notify_get_state
- _notify_is_valid_token
- _notify_register_dispatch
- _objc_msgSend$_queryIsDisplayOn
- _objc_msgSend$_registerForSpringboardNotificationsWithQueue:
- _objc_msgSend$_unregisterForSpringboardNotifications
- _objc_msgSend$notifyToken
- _objc_msgSend$numberWithInt:
- _objc_msgSend$numberWithUnsignedLongLong:
- _objc_msgSend$setNotifyToken:
- _objc_retainBlock
CStrings:
+ "-[AXPhoenixDisplayStatusMonitor _startObservingAggregateBacklight]"
+ "-[AXPhoenixDisplayStatusMonitor backlight:didCompleteUpdateToState:forEvent:]_block_invoke"
+ "[PHOENIX] %s Aggregate backlight update, state=%{public}@ -> display %{public}@ (was %{public}@)"
+ "[PHOENIX] %s Observing aggregate backlight, initial state=%{public}@ -> display %{public}@"
- "-[AXPhoenixDisplayStatusMonitor _queryIsDisplayOn]"
- "-[AXPhoenixDisplayStatusMonitor _registerForSpringboardNotificationsWithQueue:]"
- "-[AXPhoenixDisplayStatusMonitor _registerForSpringboardNotificationsWithQueue:]_block_invoke"
- "[PHOENIX] %s Display status ambiguous: notify_get_state status %@ != NOTIFY_STATUS_OK and state == %@"
- "[PHOENIX] %s Fail to register for screen state change"
- "[PHOENIX] %s notify_get_state status %@ != NOTITY_STATUS_OK"
- "com.apple.springboard.hasBlankedScreen"
- "v12@?0i8"
```
