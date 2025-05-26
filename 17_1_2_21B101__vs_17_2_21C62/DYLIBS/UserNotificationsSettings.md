## UserNotificationsSettings

> `/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings`

```diff

-491.2.1.0.0
-  __TEXT.__text: 0x49ec
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x5cc
+491.8.0.0.0
+  __TEXT.__text: 0x4acc
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__objc_methlist: 0x5d4
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x48a
+  __TEXT.__cstring: 0x4a5
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__oslogstring: 0x52a
-  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__unwind_info: 0x1c4
   __TEXT.__objc_classname: 0x1c8
-  __TEXT.__objc_methname: 0x1458
-  __TEXT.__objc_methtype: 0x4ed
-  __TEXT.__objc_stubs: 0xae0
+  __TEXT.__objc_methname: 0x149c
+  __TEXT.__objc_methtype: 0x4f0
+  __TEXT.__objc_stubs: 0xb00
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x15d0
-  __DATA_CONST.__objc_selrefs: 0x3a8
-  __AUTH_CONST.__cfstring: 0x480
+  __DATA_CONST.__objc_const: 0x1600
+  __DATA_CONST.__objc_selrefs: 0x3b0
+  __AUTH_CONST.__cfstring: 0x4a0
   __AUTH_CONST.__objc_const: 0x3f0
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__auth_got: 0x1c0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xa0
+  __DATA.__objc_classrefs: 0xa8
   __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x300
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 161
-  Symbols:   692
-  CStrings:  334
+  Functions: 162
+  Symbols:   698
+  CStrings:  338
 
Symbols:
+ -[UNNotificationSource bundlePath]
+ -[UNNotificationSource initWithIdentifier:isHidden:displayName:icon:settings:bundlePath:]
+ _OBJC_CLASS_$_NSData
+ _OBJC_IVAR_$_UNNotificationSource._bundlePath
+ _objc_msgSend$bundlePath
+ _objc_msgSend$initWithIdentifier:isHidden:displayName:icon:settings:bundlePath:
+ _objc_retain_x23
- -[UNNotificationSource initWithIdentifier:isHidden:displayName:icon:settings:]
- _objc_msgSend$initWithIdentifier:isHidden:displayName:icon:settings:
CStrings:
+ "\x15"
+ "<%@: %p; identifier: %@ isHidden: %@, displayName: %@, icon: %@, source settings: %@, bundlePath: %@>"
+ "@60@0:8@16B24@28@36@44@52"
+ "T@\"NSString\",R,C,N,V_bundlePath"
+ "_bundlePath"
+ "bundlePath"
+ "initWithIdentifier:isHidden:displayName:icon:settings:bundlePath:"
- "\x14"
- "<%@: %p; identifier: %@ isHidden: %@, displayName: %@, icon: %@, source settings: %@>"
- "@52@0:8@16B24@28@36@44"
- "initWithIdentifier:isHidden:displayName:icon:settings:"

```
