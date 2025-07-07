## UserNotificationsSettings

> `/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings`

```diff

-623.0.0.0.0
-  __TEXT.__text: 0x6254
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0xa28
+628.0.0.0.0
+  __TEXT.__text: 0x66d8
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0xa54
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0x666
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__oslogstring: 0x5a0
-  __TEXT.__unwind_info: 0x248
+  __TEXT.__oslogstring: 0x5ec
+  __TEXT.__unwind_info: 0x260
   __TEXT.__objc_classname: 0x22b
-  __TEXT.__objc_methname: 0x1b60
-  __TEXT.__objc_methtype: 0x60d
-  __TEXT.__objc_stubs: 0xd60
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x2d0
+  __TEXT.__objc_methname: 0x1bb1
+  __TEXT.__objc_methtype: 0x649
+  __TEXT.__objc_stubs: 0xda0
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x538
+  __DATA_CONST.__objc_selrefs: 0x550
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__auth_got: 0x1e0
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x5e0
-  __AUTH_CONST.__objc_const: 0x1aa0
+  __AUTH_CONST.__objc_const: 0x1aa8
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x300

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7435B079-B356-3A28-B326-359801C4269F
-  Functions: 213
-  Symbols:   873
-  CStrings:  449
+  UUID: 39CDFE3B-1DC2-342D-B24D-D67B4C89D09D
+  Functions: 219
+  Symbols:   891
+  CStrings:  456
 
Symbols:
+ -[UNNotificationSettingsCenter setSourceSettings:error:]
+ -[UNUserNotificationSettingsServiceConnection setSourceSettings:]
+ GCC_except_table53
+ _OBJC_CLASS_$_NSNumber
+ ___65-[UNUserNotificationSettingsServiceConnection setSourceSettings:]_block_invoke
+ ___65-[UNUserNotificationSettingsServiceConnection setSourceSettings:]_block_invoke.19
+ ___65-[UNUserNotificationSettingsServiceConnection setSourceSettings:]_block_invoke_2
+ ___65-[UNUserNotificationSettingsServiceConnection setSourceSettings:]_block_invoke_2.cold.1
+ ___73-[UNUserNotificationSettingsServiceConnection notificationSystemSettings]_block_invoke.26
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_literal_global.21
+ ___block_literal_global.23
+ ___block_literal_global.25
+ ___block_literal_global.29
+ ___block_literal_global.31
+ _objc_msgSend$setSourceSettings:
+ _objc_msgSend$setSourceSettings:completionHandler:
+ _objc_retainAutorelease
- GCC_except_table49
- ___73-[UNUserNotificationSettingsServiceConnection notificationSystemSettings]_block_invoke.25
- ___block_literal_global.20
- ___block_literal_global.22
- ___block_literal_global.24
- ___block_literal_global.28
- ___block_literal_global.30
CStrings:
+ "B32@0:8@16o^@24"
+ "Set source settings"
+ "Set soure settings (sync) failed with error: %{public}@"
+ "setSourceSettings:"
+ "setSourceSettings:completionHandler:"
+ "setSourceSettings:error:"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"

```
