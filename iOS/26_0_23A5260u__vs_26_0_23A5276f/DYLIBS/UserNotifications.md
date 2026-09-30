## UserNotifications

> `/System/Library/Frameworks/UserNotifications.framework/UserNotifications`

```diff

-616.0.1.0.0
-  __TEXT.__text: 0x2f978
+623.0.0.0.0
+  __TEXT.__text: 0x2fc34
   __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x3680
-  __TEXT.__cstring: 0x336d
+  __TEXT.__objc_methlist: 0x3698
+  __TEXT.__cstring: 0x33c6
   __TEXT.__const: 0xd0
   __TEXT.__oslogstring: 0x2092
   __TEXT.__gcc_except_tab: 0x26c
   __TEXT.__dlopen_cstrs: 0x8a
-  __TEXT.__unwind_info: 0xcd0
-  __TEXT.__objc_classname: 0x99a
-  __TEXT.__objc_methname: 0x9605
-  __TEXT.__objc_methtype: 0x1268
+  __TEXT.__unwind_info: 0xce0
+  __TEXT.__objc_classname: 0x9ad
+  __TEXT.__objc_methname: 0x9637
+  __TEXT.__objc_methtype: 0x1279
   __TEXT.__objc_stubs: 0x4fe0
   __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0xaf0
+  __DATA_CONST.__const: 0xb08
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bf8
+  __DATA_CONST.__objc_selrefs: 0x1c00
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x33c0
+  __AUTH_CONST.__cfstring: 0x3420
   __AUTH_CONST.__objc_const: 0xa498
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x2d0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4740582-0518-3F31-8F04-ABED4A996A04
-  Functions: 1330
-  Symbols:   4649
-  CStrings:  2593
+  UUID: BBAD9FB8-CAAF-3576-9956-D26CF624E465
+  Functions: 1332
+  Symbols:   4656
+  CStrings:  2602
 
Symbols:
+ +[UNNotificationIcon iconWithDateComponents:calendarIdentifier:format:]
+ +[UNNotificationIcon(DEPRECATED) iconAtPath:]
+ +[UNNotificationIcon(DEPRECATED) iconNamed:]
+ +[UNNotificationIcon(DEPRECATED_Private) iconAtPath:shouldSuppressMask:]
+ +[UNNotificationIcon(DEPRECATED_Private) iconNamed:shouldSuppressMask:]
+ +[UNNotificationIcon(DEPRECATED_Private) iconWithData:]
+ -[UNNotificationIcon dateComponents]
+ _UNNotificationIconCalendarKey
+ _UNNotificationIconDateComponentsKey
+ _UNNotificationIconDateFormatKey
+ __OBJC_$_CLASS_METHODS_UNNotificationIcon(DEPRECATED|DEPRECATED_Private)
- +[UNNotificationIcon iconAtPath:]
- +[UNNotificationIcon iconAtPath:shouldSuppressMask:]
- +[UNNotificationIcon iconNamed:]
- +[UNNotificationIcon iconNamed:shouldSuppressMask:]
- +[UNNotificationIcon iconWithData:]
- __OBJC_$_CLASS_METHODS_UNNotificationIcon
CStrings:
+ "@40@0:8@16@24q32"
+ "DEPRECATED_Private"
+ "NotificationIconCalendarKey"
+ "NotificationIconDateComponents"
+ "NotificationIconDateFormatKey"
+ "iconWithDateComponents:calendarIdentifier:format:"

```
