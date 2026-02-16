## AlarmKitFoundation

> `/System/Library/PrivateFrameworks/AlarmKitFoundation.framework/AlarmKitFoundation`

```diff

-2303.3.1.0.0
-  __TEXT.__text: 0x638
-  __TEXT.__auth_stubs: 0x160
+2303.4.19.100.0
+  __TEXT.__text: 0x5e4
+  __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_methlist: 0x1e8
   __TEXT.__const: 0x40
   __TEXT.__unwind_info: 0x98

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0xb8
+  __AUTH_CONST.__auth_got: 0xa8
   __AUTH_CONST.__objc_const: 0x7b0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x54

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A04302C-0A02-3090-9C7B-8B425DABF459
+  UUID: E6C2DD7F-028F-3A47-8BFE-F9D302624E1A
   Functions: 36
-  Symbols:   169
+  Symbols:   167
   CStrings:  97
 
Symbols:
+ _objc_release_x25
+ _objc_retain_x19
+ _objc_retain_x25
- _objc_release_x27
- _objc_release_x9
- _objc_retain_x2
- _objc_retain_x27
- _objc_retain_x3
Functions:
~ -[AKCAlertNotification initWithIdentifier:displayTitle:hasSecondaryAction:secondaryButtonLabel:stopButtonLabel:actionUrlScheme:tintColor:bundleID:localizedAppName:] : 400 -> 372
~ -[AKCAlarmAlertNotification initWithIdentifier:scheduledFireDate:allowsSnooze:displayTitle:hasSecondaryAction:secondaryButtonLabel:stopButtonLabel:actionUrlScheme:tintColor:bundleID:localizedAppName:] : 236 -> 220
~ -[AKCAlarmAlertNotification scheduledFireDate] : 16 -> 8
~ -[AKCAlarmAlertNotification allowsSnooze] : 16 -> 8
~ -[AKCAlarmAlertNotification .cxx_destruct] : 20 -> 12
~ -[AKCTimerAlertNotification duration] : 16 -> 8
~ -[AKCAlarm initWithIdentifier:data:attributes:] : 168 -> 160

```
