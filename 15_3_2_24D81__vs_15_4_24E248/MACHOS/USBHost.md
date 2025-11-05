## USBHost

> `/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/Contents/MacOS/USBHost`

```diff

-1025.80.3.0.1
-  __TEXT.__text: 0x1cd44
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0xfb8
+1043.100.30.0.0
+  __TEXT.__text: 0x1d190
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x1310
   __TEXT.__const: 0x160
   __TEXT.__oslogstring: 0x2de0
-  __TEXT.__cstring: 0x18be
+  __TEXT.__cstring: 0x18d0
   __TEXT.__gcc_except_tab: 0x560
-  __TEXT.__unwind_info: 0x488
+  __TEXT.__unwind_info: 0x4b8
   __TEXT.__objc_classname: 0x237
-  __TEXT.__objc_methname: 0x3801
-  __TEXT.__objc_methtype: 0x9ba
-  __TEXT.__objc_stubs: 0x2240
+  __TEXT.__objc_methname: 0x39be
+  __TEXT.__objc_methtype: 0x9cf
+  __TEXT.__objc_stubs: 0x2280
   __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0x638
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb10
+  __DATA_CONST.__objc_selrefs: 0xc88
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x418
+  __AUTH_CONST.__auth_got: 0x420
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x1380
-  __AUTH_CONST.__objc_const: 0x2ba0
+  __AUTH_CONST.__cfstring: 0x13a0
+  __AUTH_CONST.__objc_const: 0x2730
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x240
+  __DATA.__objc_ivar: 0x250
   __DATA.__data: 0x330
   __DATA.__bss: 0xa0
   __DATA.__common: 0x24

   - /System/Library/PrivateFrameworks/CoreAccessories.framework/Versions/A/CoreAccessories
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8793DCCF-D851-3D0D-8B96-4BEFB981213A
-  Functions: 564
-  Symbols:   4435
-  CStrings:  1369
+  UUID: 6CCD72E7-027D-33A5-A393-093CEB58B138
+  Functions: 584
+  Symbols:   4527
+  CStrings:  1390
 
Symbols:
+ +[ACCUserDefaults sharedDefaultsIapd].cold.1
+ +[ACCUserDefaults sharedDefaultsLogging].cold.1
+ +[ACCUserDefaults sharedDefaults].cold.1
+ +[AccessoryEAInterface initializeSessionClose].cold.3
+ +[AccessoryUSBBillboardDevice parentServiceVidPid:].cold.2
+ -[ACCUserNotification allowLockScreenDismissal]
+ -[ACCUserNotification iconConfiguration]
+ -[ACCUserNotification lockScreenMessage]
+ -[ACCUserNotification lockScreenTitle]
+ -[ACCUserNotification setAllowLockScreenDismissal:]
+ -[ACCUserNotification setIconConfiguration:]
+ -[ACCUserNotification setLockScreenMessage:]
+ -[ACCUserNotification setLockScreenTitle:]
+ -[ACCUserNotification updateBackingUserNotification]
+ -[ACCUserNotificationManager dismissAllNotifications]
+ -[ACCUserNotificationManager updateNotification:]
+ -[iAP2EASession initWithProtocol:endpointUUID:eaSessionUUID:].cold.3
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/ACCTransportIOAccessoryManagerNotifications.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/ACCUserDefaults.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/ACCUserNotification.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/ACCUserNotificationManager.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/ACCUserNotifications.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/AccessoryEAInterface.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/AccessoryIAPInterface.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/AccessoryTransportUSBHostPlugin.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/AccessoryUSBBillboardDevice.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/AccessoryUSBCDCInterface.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/acc_platform_system_info.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/logging_signposts.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/logging_transport_plugins.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/logging_wrapper.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/system_info.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/usb_util.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/Accessory_Frameworks/CoreAccessories/
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/Transport_Plugins/Common/
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/Transport_Plugins/IOAccessoryManager/
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/Transport_Plugins/USBHost/
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/accessoryd/Platform_Implementations/
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Common/Common_C/
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Common/Common_CF/
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Common/Common_ObjC/
+ OBJC_IVAR_$_ACCUserNotification._allowLockScreenDismissal
+ OBJC_IVAR_$_ACCUserNotification._iconConfiguration
+ OBJC_IVAR_$_ACCUserNotification._lockScreenMessage
+ OBJC_IVAR_$_ACCUserNotification._lockScreenTitle
+ _CFUserNotificationUpdate
+ _objc_msgSend$iconConfiguration
+ _objc_msgSend$updateBackingUserNotification
+ systemInfo_isDeveloperBuild.cold.1
+ systemInfo_isInternalBuild.cold.1
- -[ACCUserNotificationManager dismisssAllNotifications]
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/ACCTransportIOAccessoryManagerNotifications.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/ACCUserDefaults.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/ACCUserNotification.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/ACCUserNotificationManager.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/ACCUserNotifications.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/AccessoryEAInterface.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/AccessoryIAPInterface.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/AccessoryTransportUSBHostPlugin.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/AccessoryUSBBillboardDevice.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/AccessoryUSBCDCInterface.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/acc_platform_system_info.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/logging_signposts.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/logging_transport_plugins.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/logging_wrapper.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/system_info.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/USBHost.build/Objects-normal/arm64e/usb_util.o
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/Accessory_Frameworks/CoreAccessories/
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/Transport_Plugins/Common/
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/Transport_Plugins/IOAccessoryManager/
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/Transport_Plugins/USBHost/
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/accessoryd/Platform_Implementations/
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Common/Common_C/
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Common/Common_CF/
- /AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Sources/CoreAccessories/Common/Common_ObjC/
- _OUTLINED_FUNCTION_8
CStrings:
+ "IconConfiguration"
+ "T@\"NSDictionary\",C,N,V_iconConfiguration"
+ "T@\"NSString\",C,N,V_lockScreenMessage"
+ "T@\"NSString\",C,N,V_lockScreenTitle"
+ "TB,N,V_allowLockScreenDismissal"
+ "_allowLockScreenDismissal"
+ "_iconConfiguration"
+ "_lockScreenMessage"
+ "_lockScreenTitle"
+ "allowLockScreenDismissal"
+ "dismissAllNotifications"
+ "iconConfiguration"
+ "lockScreenMessage"
+ "lockScreenTitle"
+ "setAllowLockScreenDismissal:"
+ "setIconConfiguration:"
+ "setLockScreenMessage:"
+ "setLockScreenTitle:"
+ "updateBackingUserNotification"
+ "updateNotification:"
+ "v24@0:8@\"NSString\"16"
- "dismisssAllNotifications"

```
