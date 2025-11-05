## AirTrafficHost

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/AirTrafficHost.framework/Versions/A/AirTrafficHost`

```diff

-4024.300.19.0.0
-  __TEXT.__text: 0x332a8
+4024.500.19.0.0
+  __TEXT.__text: 0x33274
   __TEXT.__auth_stubs: 0x770
   __TEXT.__cstring: 0x23af
   __TEXT.__const: 0x67a0
-  __TEXT.__unwind_info: 0x280
+  __TEXT.__unwind_info: 0x290
   __DATA_CONST.__auth_got: 0x3b8
-  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xdf8
   __DATA_CONST.__cfstring: 0x740
   __DATA.__data: 0x1c8

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/MobileDevice.framework/Versions/A/MobileDevice
   - /usr/lib/libSystem.B.dylib
-  UUID: 9FF88F8A-E8F2-3E4A-A421-5DC3D2826773
-  Functions: 220
-  Symbols:   288
+  UUID: 99B10081-71BF-366E-BD08-E3AA4802D002
+  Functions: 221
+  Symbols:   289
   CStrings:  289
 
Symbols:
+ ATHostGetLogCategory.cold.1
Functions:
~ _ATHostConnectionSendSyncRequest : 484 -> 480
~ __ATHostConnectionProcessLocalCloudDownloadRequestHandler : 1256 -> 1244
~ _ATHostGetLogCategory : 84 -> 68
~ __ATHostMessageLinkDeviceObserverCallback : 208 -> 204
~ _ATHostMessageLinkDestroy : 256 -> 252
~ __ATHostMessageLinkDeviceSocketObserverCallback : 168 -> 156
~ __ATHostMessageLinkSendNextMessage : 464 -> 460
~ __ATHostDeviceObserverStart : 332 -> 336
~ _ATHostDeviceObserverDestroy : 276 -> 264
~ __ATHostDeviceObserverHandleDeviceNotification : 628 -> 624
~ __ATHostAMDeviceEnqueueDataForWriting : 296 -> 300
~ __ATHostMDSocketHandleClose : 140 -> 128
~ __readDictionary : 612 -> 608
~ _ATProcessLinkSetupParent : 380 -> 400
~ __ATHostDeviceNotificationObserverSecureListenCallback : 404 -> 392
~ _ATHostDeviceNotificationObserverDestroy : 208 -> 204
~ _ATHostAdvertiserStartWakeupService : 708 -> 712
+ ATHostGetLogCategory.cold.1

```
