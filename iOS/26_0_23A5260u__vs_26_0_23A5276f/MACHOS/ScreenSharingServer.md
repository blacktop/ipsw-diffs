## ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

-112.0.0.0.0
-  __TEXT.__text: 0x3f49c
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x4240
-  __TEXT.__objc_methlist: 0x1b2c
-  __TEXT.__const: 0xda
-  __TEXT.__objc_methname: 0x58ab
-  __TEXT.__cstring: 0xac8e
-  __TEXT.__oslogstring: 0x6bf2
-  __TEXT.__objc_classname: 0x288
-  __TEXT.__objc_methtype: 0x2ea6
-  __TEXT.__gcc_except_tab: 0x234
-  __TEXT.__unwind_info: 0x530
-  __DATA_CONST.__auth_got: 0x710
-  __DATA_CONST.__got: 0x3c0
-  __DATA_CONST.__const: 0x658
+113.0.0.0.0
+  __TEXT.__text: 0x40174
+  __TEXT.__auth_stubs: 0xe50
+  __TEXT.__objc_stubs: 0x43e0
+  __TEXT.__objc_methlist: 0x1c74
+  __TEXT.__const: 0xe2
+  __TEXT.__objc_methname: 0x5c76
+  __TEXT.__cstring: 0xaf9e
+  __TEXT.__oslogstring: 0x6e44
+  __TEXT.__objc_classname: 0x2c8
+  __TEXT.__objc_methtype: 0x3084
+  __TEXT.__gcc_except_tab: 0x3e0
+  __TEXT.__unwind_info: 0x548
+  __DATA_CONST.__auth_got: 0x738
+  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__const: 0x660
   __DATA_CONST.__cfstring: 0x1ce0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x148
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x2430
-  __DATA.__objc_selrefs: 0x1550
-  __DATA.__objc_ivar: 0x1e0
+  __DATA.__objc_const: 0x25d0
+  __DATA.__objc_selrefs: 0x1600
+  __DATA.__objc_ivar: 0x1f0
   __DATA.__objc_data: 0x410
-  __DATA.__data: 0x4d0
+  __DATA.__data: 0x590
   __DATA.__bss: 0x338
   __DATA.__common: 0x19
   - /System/Library/Frameworks/Accounts.framework/Accounts
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
-  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/ChatKit.framework/ChatKit
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi

   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GameKitServices.framework/GameKitServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: BFD9E252-2301-3288-BD26-61470347F8AB
-  Functions: 590
-  Symbols:   365
-  CStrings:  3418
+  UUID: 0DFE23ED-B442-343C-9C82-E99C0BC0BBDF
+  Functions: 605
+  Symbols:   369
+  CStrings:  3489
 
Symbols:
+ _CBCentralManagerOptionShowPowerAlertKey
+ _OBJC_CLASS_$_CBCentralManager
+ _OBJC_CLASS_$_FBSOrientationObserver
+ _OBJC_CLASS_$_NSRunLoop
+ _dispatch_after
+ _objc_destroyWeak
+ _objc_loadWeakRetained
+ _objc_retain_x28
+ _objc_storeWeak
- _OBJC_CLASS_$_BluetoothManager
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "-[IDSSessionEmbeddedControllerBase SSMediaStreamServerDidDie]"
+ "-[IDSSessionEmbeddedControllerBase SSMediaStreamTimeout]"
+ "-[SSAVCMediaStreamController initWithIDSSession:avcClientName:audioEncryptionKeyViewerToServer:audioEncryptionKeyServerToViewer:video1EncryptionKeyViewerToServer:video1EncryptionKeyServerToViewer:audioOffer:videoOffer:sessionID:supports60FPS:mediaStreamSessionUUID:delegate:]"
+ "-[SSAnnotationRenderer handleSafeViewAnnotation:flags:orientation:]"
+ "-[ShareSettingsInfo gatherSystemInfo]"
+ "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/SSAnnotationRenderer.m"
+ "@\"<SSAVCMediaStreamControllerDelegate>\""
+ "@\"FBSOrientationObserver\""
+ "@108@0:8@16@24@32@40@48@56@64@72@80B88@92@100"
+ "Bluetooth state is CBManagerStatePoweredOff"
+ "Bluetooth state is CBManagerStatePoweredOn"
+ "Bluetooth state is CBManagerStateResetting"
+ "Bluetooth state is CBManagerStateUnauthorized"
+ "Bluetooth state is CBManagerStateUnknown"
+ "Bluetooth state is CBManagerStateUnsupported"
+ "CBCentralManager did not update state"
+ "CBCentralManagerDelegate"
+ "RTCPTimeoutCount"
+ "SSAVCMediaStreamControllerDelegate"
+ "SSMediaStreamServerDidDie"
+ "SSMediaStreamServerDidDie - end session"
+ "SSMediaStreamTimeout"
+ "SSMediaStreamTimeout - end session"
+ "T@\"<SSAVCMediaStreamControllerDelegate>\",W,V_delegate"
+ "T@\"FBSOrientationObserver\",&,N,V_orientationObserver"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_stateSemaphore"
+ "TI,N,V_RTCPTimeoutCount"
+ "[%s:%d] Bluetooth state is CBManagerStatePoweredOff"
+ "[%s:%d] Bluetooth state is CBManagerStatePoweredOn"
+ "[%s:%d] Bluetooth state is CBManagerStateResetting"
+ "[%s:%d] Bluetooth state is CBManagerStateUnauthorized"
+ "[%s:%d] Bluetooth state is CBManagerStateUnknown"
+ "[%s:%d] Bluetooth state is CBManagerStateUnsupported"
+ "[%s:%d] CBCentralManager did not update state"
+ "[%s:%d] SSMediaStreamServerDidDie - end session"
+ "[%s:%d] SSMediaStreamTimeout - end session"
+ "[%s:%d] audio streamDidRTCPTimeOut: %p count: %u"
+ "[%s:%d] interface orientation is unknown"
+ "[%s:%d] invalid result"
+ "[%s:%d] orientation from message %ld actual orientation %ld"
+ "[%s:%d] too many RTCP timeouts"
+ "[%s:%d] video streamDidRTCPTimeOut: %p count: %u"
+ "_RTCPTimeoutCount"
+ "_delegate"
+ "_orientationObserver"
+ "_stateSemaphore"
+ "activeInterfaceOrientation"
+ "audio streamDidRTCPTimeOut: %p count: %u"
+ "centralManager:connectionEventDidOccur:forPeripheral:"
+ "centralManager:didConnectPeripheral:"
+ "centralManager:didDisconnectPeripheral:error:"
+ "centralManager:didDisconnectPeripheral:timestamp:isReconnecting:error:"
+ "centralManager:didDiscoverPeripheral:advertisementData:RSSI:"
+ "centralManager:didFailToConnectPeripheral:error:"
+ "centralManager:didUpdateANCSAuthorizationForPeripheral:"
+ "centralManager:willRestoreState:"
+ "centralManagerDidUpdateState:"
+ "currentRunLoop"
+ "dateWithTimeIntervalSinceNow:"
+ "delegate"
+ "finished init"
+ "initWithDelegate:queue:options:"
+ "initWithIDSSession:avcClientName:audioEncryptionKeyViewerToServer:audioEncryptionKeyServerToViewer:video1EncryptionKeyViewerToServer:video1EncryptionKeyServerToViewer:audioOffer:videoOffer:sessionID:supports60FPS:mediaStreamSessionUUID:delegate:"
+ "interface orientation is unknown"
+ "invalid result"
+ "main screen point width: %f height: %f  scaling: %f orientation %ld landscape: %d"
+ "orientation from message %ld actual orientation %ld"
+ "orientationObserver"
+ "runUntilDate:"
+ "setOrientationObserver:"
+ "setRTCPTimeoutCount:"
+ "setStateSemaphore:"
+ "stateSemaphore"
+ "too many RTCP timeouts"
+ "v24@0:8@\"CBCentralManager\"16"
+ "v32@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24"
+ "v32@0:8@\"CBCentralManager\"16@\"NSDictionary\"24"
+ "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSError\"32"
+ "v40@0:8@\"CBCentralManager\"16q24@\"CBPeripheral\"32"
+ "v40@0:8@16q24@32"
+ "v48@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32@\"NSNumber\"40"
+ "v52@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24d32B40@\"NSError\"44"
+ "v52@0:8@16@24d32B40@44"
+ "video streamDidRTCPTimeOut: %p count: %u"
- "##$finished init"
- "+[ShareSettingsInfo gatherSystemInfo]"
- "-[SSAVCMediaStreamController initWithIDSSession:avcClientName:audioEncryptionKeyViewerToServer:audioEncryptionKeyServerToViewer:video1EncryptionKeyViewerToServer:video1EncryptionKeyServerToViewer:audioOffer:videoOffer:sessionID:supports60FPS:mediaStreamSessionUUID:]"
- "@100@0:8@16@24@32@40@48@56@64@72@80B88@92"
- "BT is already available"
- "BT not yet available, checking SCDynamicStore"
- "[%s:%d] BT is already available"
- "[%s:%d] BT not yet available, checking SCDynamicStore"
- "[%s:%d] video streamDidRTCPTimeOut: %p"
- "available"
- "initWithIDSSession:avcClientName:audioEncryptionKeyViewerToServer:audioEncryptionKeyServerToViewer:video1EncryptionKeyViewerToServer:video1EncryptionKeyServerToViewer:audioOffer:videoOffer:sessionID:supports60FPS:mediaStreamSessionUUID:"
- "main screen width: %f height: %f  scaling: %f landscape: %d"
- "video streamDidRTCPTimeOut: %p"

```
