## iosdiagnosticsd

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iosdiagnosticsd`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0xdd78
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_stubs: 0x2500
-  __TEXT.__objc_methlist: 0x1614
+1351.0.0.0.0
+  __TEXT.__text: 0xdafc
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_stubs: 0x2600
+  __TEXT.__objc_methlist: 0x16dc
+  __TEXT.__cstring: 0xc88
+  __TEXT.__objc_methname: 0x3609
+  __TEXT.__objc_classname: 0x32f
+  __TEXT.__objc_methtype: 0x110b
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x6e4
-  __TEXT.__objc_methname: 0x34a9
-  __TEXT.__oslogstring: 0xbc7
-  __TEXT.__cstring: 0xbe6
-  __TEXT.__objc_classname: 0x349
-  __TEXT.__objc_methtype: 0x10fa
-  __TEXT.__unwind_info: 0x580
-  __DATA_CONST.__auth_got: 0x310
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x598
-  __DATA_CONST.__cfstring: 0xd20
+  __TEXT.__gcc_except_tab: 0x6b8
+  __TEXT.__oslogstring: 0xdd5
+  __TEXT.__unwind_info: 0x4e8
+  __DATA_CONST.__const: 0x5d0
+  __DATA_CONST.__cfstring: 0xd60
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x4760
-  __DATA.__objc_selrefs: 0xd28
-  __DATA.__objc_ivar: 0x154
+  __DATA_CONST.__auth_got: 0x358
+  __DATA_CONST.__got: 0x268
+  __DATA.__objc_const: 0x4820
+  __DATA.__objc_selrefs: 0xd88
+  __DATA.__objc_ivar: 0x164
   __DATA.__objc_data: 0x820
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit
   - /System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F0C62D9-819F-33C9-AACA-3CBEC6D01025
-  Functions: 405
-  Symbols:   182
-  CStrings:  1072
+  UUID: 12208756-485B-3B34-ABB3-A9BBF96B9489
+  Functions: 419
+  Symbols:   195
+  CStrings:  1111
 
Symbols:
+ _IDSSendMessageOptionLocalDeliveryKey
+ _IDSSendMessageOptionWantsDeliveryStatusKey
+ _OBJC_CLASS_$_HMAccessory
+ ___kCFBooleanFalse
+ __dispatch_main_q
+ __os_feature_enabled_impl
+ _dispatch_group_notify
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x7
- _OBJC_CLASS_$_NSMutableSet
- _objc_retain_x28
CStrings:
+ "Diagnostics"
+ "HomePod"
+ "IncludeHomePods"
+ "T@\"DDIDSService\",&,N,V_homekitService"
+ "T@\"NSArray\",&,N,V_devices"
+ "T@\"NSString\",&,N,V_name"
+ "UUIDString"
+ "Unexpected DDIDSServiceType: %ld"
+ "Unknown DDIDSServiceType: %ld, using default"
+ "[DDIDSService] Initializing HomeKit Type"
+ "[DDIDSService] Initializing Paired Type"
+ "[DDIDSService] _destinationFromID [%@] %@"
+ "[DDIDSService] availableDestinationsWithCompletion %@"
+ "[DDIDSService] availableDestinationsWithCompletion (%@) got devices: %lu"
+ "[DDIDSService] connectedDevicesChanged: %lu"
+ "[DDIDSService] devicesChanged: %lu"
+ "[DDIDSService] hasDestination %@"
+ "[DDIDSService] nearbyDevicesChanged: %lu"
+ "[DDMain] Initializing"
+ "[DDMain] dispatch_once"
+ "_createDestinationFromDevice:"
+ "_devices"
+ "_homekitService"
+ "_name"
+ "_serviceName"
+ "cancelTests"
+ "com.apple.Diagnostics.Homekit.IDSDelegateQueue"
+ "com.apple.Diagnostics.Service.IDSDelegateQueue"
+ "com.apple.private.alloy.diagnosticscheckupd"
+ "device"
+ "homekitService"
+ "idsIdentifier"
+ "initWithHomePodDevice:"
+ "isEqualToHMAccessory:"
+ "setByAddingObjectsFromSet:"
+ "setDevices:"
+ "setHomekitService:"
+ "setName:"
+ "setSimpleAlertCancelHandler:"
+ "v24@0:8@?<v@?>16"
- "#"
- "com.apple.Diagnostics.IDSDelegateQueue"
- "unionSet:"

```
