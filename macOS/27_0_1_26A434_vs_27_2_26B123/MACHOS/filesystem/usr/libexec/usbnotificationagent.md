## usbnotificationagent

> `/usr/libexec/usbnotificationagent`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__info_plist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_ivar`
- `__DATA.__data`

```diff

-1617.0.12.0.0
-  __TEXT.__text: 0x81c4
+1617.40.10.0.0
+  __TEXT.__text: 0x7f74
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__objc_stubs: 0x1380
-  __TEXT.__objc_methlist: 0x784
+  __TEXT.__objc_methlist: 0x79c
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0xb97
-  __TEXT.__oslogstring: 0x9e9
-  __TEXT.__objc_methname: 0x145c
-  __TEXT.__objc_classname: 0xac
-  __TEXT.__objc_methtype: 0x3cf
+  __TEXT.__cstring: 0xbac
+  __TEXT.__oslogstring: 0xa11
+  __TEXT.__objc_methname: 0x1454
+  __TEXT.__objc_classname: 0x95
+  __TEXT.__objc_methtype: 0x3d1
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__info_plist: 0x3fe
   __TEXT.__unwind_info: 0x278
-  __DATA_CONST.__const: 0x240
-  __DATA_CONST.__cfstring: 0xae0
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__const: 0x220
+  __DATA_CONST.__cfstring: 0xb00
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x258
   __DATA_CONST.__objc_arraydata: 0x3a8
   __DATA_CONST.__objc_dictobj: 0x3c0
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x260
-  __DATA_CONST.__got: 0xf0
-  __DATA.__objc_const: 0xdb0
-  __DATA.__objc_selrefs: 0x5c8
+  __DATA_CONST.__got: 0xe8
+  __DATA.__objc_const: 0xd10
+  __DATA.__objc_selrefs: 0x5d0
   __DATA.__objc_ivar: 0xa4
-  __DATA.__objc_data: 0x230
+  __DATA.__objc_data: 0x1e0
   __DATA.__data: 0xc0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 193
-  Symbols:   115
-  CStrings:  507
+  Symbols:   114
+  CStrings:  510
 
Symbols:
- _OBJC_CLASS_$_UNTimeIntervalNotificationTrigger
CStrings:
+ "%@ scheduled in %.0fs"
+ ":!"
+ "@\"USBNotificationAgentCenter\""
+ "Identifier"
+ "Notification: addNotificationRequest error: %@"
+ "Notification: failed to create presentationTimer"
+ "SOPNotification: failed to read service properties"
+ "SuppressedNotifications"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_presentationTimer"
+ "T@\"USBNotificationAgentCenter\",&,N,V_notificationCenter"
+ "TB,R,N,V_evaluated"
+ "USBNotification: User preferences suppress %@ notification for %@ (reason %u)\n"
+ "USBNotificationAgentCenter: cannot suppress without a category and identifier"
+ "USBNotificationAgentCenter: suppress future %@ notifications for %@ (reason %u)"
+ "_evaluated"
+ "_presentationTimer"
+ "d16@0:8"
+ "evaluated"
+ "event %@ suppressed for unevaluated %@"
+ "i32@0:8@16@24"
+ "notificationContent"
+ "presentationDelay"
+ "presentationTimer"
+ "resolveRedundantNotification:"
+ "schedulePresentation"
+ "setPresentationTimer:"
+ "suppressCategory:identifier:dismissReason:"
+ "suppressNotification:dismissReason:"
+ "suppressionReasonForCategory:identifier:"
+ "suppressionReasonForNotification:"
+ "v36@0:8@16@24i32"
- "@\"UNUserNotificationCenter\""
- "@52@0:8I16@20@28^?36^?44"
- "B32@0:8@16@24"
- "SOPDelayedNotification"
- "SOPDelayedNotification: invalid readyCallback"
- "SOPDelayedNotification: invalid service"
- "SOPNotification: addNotificationRequest error: %@"
- "SOPNotification: failed to create notificationTimer"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_notificationTimer"
- "T@\"UNUserNotificationCenter\",&,N,V_notificationCenter"
- "T^?,N,V_readyCallback"
- "USBNotification: User preferences suppress %@ notification for %@\n"
- "USBNotification: addNotificationRequest error: %@"
- "USBNotificationAgentCenter: suppress future %@ notifications for %@"
- "_notificationTimer"
- "_readyCallback"
- "delayed %s-%@-%@"
- "delayedSOPNotificationReady: %@"
- "initWithService:notificationCenter:dispatchQueue:interestCallback:readyCallback:"
- "isSuppressedCategory:identifier:"
- "isSuppressedNotification:"
- "notificationTimer"
- "readyCallback"
- "setNotificationTimer:"
- "setReadyCallback:"
- "suppressCategory:identifier:"
- "suppressNotification:"
- "triggerWithTimeInterval:repeats:"
```
