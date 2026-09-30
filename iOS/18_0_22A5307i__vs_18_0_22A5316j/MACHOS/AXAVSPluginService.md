## AXAVSPluginService

> `/System/Library/AccessibilityBundles/AXAVSPluginService.axuiservice/AXAVSPluginService`

```diff

-3132.8.0.0.0
-  __TEXT.__text: 0x428
-  __TEXT.__auth_stubs: 0x130
-  __TEXT.__objc_stubs: 0x140
-  __TEXT.__objc_methlist: 0x5c
-  __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__objc_methname: 0x55d
-  __TEXT.__cstring: 0x48
-  __TEXT.__oslogstring: 0x43
+3134.3.0.0.0
+  __TEXT.__text: 0xb68
+  __TEXT.__auth_stubs: 0x220
+  __TEXT.__objc_stubs: 0x3e0
+  __TEXT.__objc_methlist: 0x154
+  __TEXT.__const: 0x10
+  __TEXT.__gcc_except_tab: 0x44
+  __TEXT.__objc_methname: 0x82f
+  __TEXT.__oslogstring: 0xc5
+  __TEXT.__cstring: 0x78
+  __TEXT.__objc_classname: 0x45
+  __TEXT.__objc_methtype: 0x343
   __TEXT.__ustring: 0xa
-  __TEXT.__objc_classname: 0x28
-  __TEXT.__objc_methtype: 0x2d1
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0xa8
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x50
+  __TEXT.__unwind_info: 0xd0
+  __DATA_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__cfstring: 0x40
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x5d0
-  __DATA.__objc_selrefs: 0x78
-  __DATA.__objc_data: 0x50
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0x738
+  __DATA.__objc_selrefs: 0x138
+  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9
-  Symbols:   33
-  CStrings:  91
+  Functions: 33
+  Symbols:   54
+  CStrings:  139
 
Symbols:
+ _AXLogCommon
+ _AXPerformBlockAsynchronouslyOnMainThread
+ _OBJC_CLASS_$_AXPluginDisplayOnMonitor
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_UIDevice
+ _OBJC_METACLASS_$_AXPluginDisplayOnMonitor
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __dispatch_main_q
+ __os_log_error_impl
+ _notify_cancel
+ _notify_get_state
+ _notify_is_valid_token
+ _notify_register_dispatch
+ _objc_alloc_init
+ _objc_autoreleaseReturnValue
+ _objc_release_x8
+ _objc_retainBlock
+ _objc_retain_x22
+ _objc_storeStrong
+ _objc_storeWeak
CStrings:
+ "\x01"
+ "\x11"
+ ".cxx_destruct"
+ "@\"<AXPluginDisplayOnMonitorDelegate>\""
+ "@\"AXPluginDisplayOnMonitor\""
+ "AXPluginDisplayOnMonitor"
+ "B"
+ "Display status ambiguous: notify_get_state status %!@(MISSING) != NOTIFY_STATUS_OK and state == %!@(MISSING)"
+ "Fail to register for screen state change"
+ "T@\"<AXPluginDisplayOnMonitorDelegate>\",W,N,V_delegate"
+ "T@\"AXPluginDisplayOnMonitor\",&,N,V_displayOnMonitor"
+ "TB,N,GisDisplayOn,V_displayOn"
+ "Ti,N,V_notifyToken"
+ "_delegate"
+ "_deviceSupportsVoiceTriggersWhileDisplayOff"
+ "_displayOn"
+ "_displayOnMonitor"
+ "_notifyToken"
+ "_queryIsDisplayOn"
+ "_registerForSpringboardNotifications"
+ "_startMonitoring"
+ "_stopMonitoring"
+ "_unregisterForSpringboardNotifications"
+ "_updateDisplayOnState"
+ "batteryState"
+ "com.apple.springboard.hasBlankedScreen"
+ "currentDevice"
+ "dealloc"
+ "delegate"
+ "displayOn"
+ "displayOnMonitor"
+ "displayOnMonitor:didReceiveDisplayOnStateChanged:"
+ "i"
+ "i16@0:8"
+ "isBatteryMonitoringEnabled"
+ "isDisplayOn"
+ "notifyToken"
+ "numberWithInt:"
+ "numberWithUnsignedLongLong:"
+ "setBatteryMonitoringEnabled:"
+ "setDelegate:"
+ "setDisplayOn:"
+ "setDisplayOnMonitor:"
+ "setNotifyToken:"
+ "v12@?0i8"
+ "v20@0:8B16"
+ "v20@0:8i16"
+ "v28@0:8@16B24"

```
