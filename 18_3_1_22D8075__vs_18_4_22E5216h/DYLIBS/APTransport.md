## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-845.6.1.0.0
-  __TEXT.__text: 0x8f258
-  __TEXT.__auth_stubs: 0x3000
-  __TEXT.__objc_methlist: 0x93c
-  __TEXT.__cstring: 0x2871e
+850.17.1.0.0
+  __TEXT.__text: 0x9ac68
+  __TEXT.__auth_stubs: 0x3010
+  __TEXT.__objc_methlist: 0xbcc
+  __TEXT.__cstring: 0x288a5
   __TEXT.__const: 0x2c8
-  __TEXT.__gcc_except_tab: 0x394
+  __TEXT.__gcc_except_tab: 0x484
   __TEXT.__oslogstring: 0x16e
-  __TEXT.__unwind_info: 0x1618
+  __TEXT.__dlopen_cstrs: 0x146
+  __TEXT.__unwind_info: 0x2518
   __TEXT.__objc_classname: 0x111
-  __TEXT.__objc_methname: 0x3135
+  __TEXT.__objc_methname: 0x3179
   __TEXT.__objc_methtype: 0xb27
-  __TEXT.__objc_stubs: 0x31a0
-  __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x3378
+  __TEXT.__objc_stubs: 0x31e0
+  __DATA_CONST.__got: 0x3a0
+  __DATA_CONST.__const: 0x33d8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd20
+  __DATA_CONST.__objc_selrefs: 0xe60
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1810
-  __AUTH_CONST.__const: 0x29f8
-  __AUTH_CONST.__cfstring: 0x56c0
-  __AUTH_CONST.__objc_const: 0x1790
+  __AUTH_CONST.__auth_got: 0x1818
+  __AUTH_CONST.__const: 0x2978
+  __AUTH_CONST.__cfstring: 0x5740
+  __AUTH_CONST.__objc_const: 0x12c8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0x2b0
+  __AUTH.__data: 0x278
   __DATA.__objc_ivar: 0x118
   __DATA.__data: 0xfb0
-  __DATA.__bss: 0x17c
+  __DATA.__bss: 0x100
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__data: 0xa18
-  __DATA_DIRTY.__bss: 0x1c0
+  __DATA_DIRTY.__data: 0xa10
+  __DATA_DIRTY.__bss: 0x230
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1853
-  Symbols:   3047
-  CStrings:  4572
+  Functions: 4272
+  Symbols:   5680
+  CStrings:  4585
 
Symbols:
+ _OBJC_CLASS_$_NSAssertionHandler
+ __sl_dlopen
+ _dlerror
+ _objc_retain_x23
- _dlopen
- _objc_retain_x22
CStrings:
+ "850.17.1"
+ "APCarPlayHelperSession.m"
+ "APCarPlayHelperWiFi.m"
+ "APSoftLinking_NearbyInteraction.h"
+ "Class getCARSessionRequestAgentClass(void)_block_invoke"
+ "Class getNIDiscoveryTokenClass(void)_block_invoke"
+ "Class getNINearbyObjectClass(void)_block_invoke"
+ "Class getNISessionClass(void)_block_invoke"
+ "Class getNISpatialBrowsingConfigurationClass(void)_block_invoke"
+ "Unable to find class %s"
+ "[%{ptr}] %s Ignoring WiFi network changed since wifiInterfaceName and wifiCurrentUUID did not change\n"
+ "[%{ptr}] %s WiFi Network changed to: %@, IsCarPlay: %s, CarPlay UUID: %@, isLinkDownDebounceInProgress: %s, interfaceName: %@\n"
+ "currentHandler"
+ "float getNINearbyObjectDistanceNotAvailable(void)"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "softlink:r:path:/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CarKit.framework/CarKit"
+ "v16@?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI*}8"
+ "void *CarKitLibrary(void)"
+ "void *NearbyInteractionLibrary(void)"
+ "void soft_CRAllowsConnectionsForWiFiUUID(NSString *, void (^)(BOOL, NSError *))"
+ "void soft_CRBluetoothIndicatesInCar(void (^)(BOOL, NSString *, NSError *))"
- "/System/Library/PrivateFrameworks/CarKit.framework/CarKit"
- "/System/Library/PrivateFrameworks/NearbyInteraction.framework/NearbyInteraction"
- "845.6.1"
- "OSStatus browser_updateBTLEBrowsing(APBrowserRef)"
- "Unhandled BTLE browsing mode %d.\n"
- "Unknown relationship to device %@: %u\n"
- "[%{ptr}] %s WiFi Network changed to: %@, IsCarPlay: %s, CarPlay UUID: %@, isLinkDownDebounceInProgress: %s\n"
- "const char *browser_getDeviceRelationshipString(CFNumberRef, APBrowserDeviceRelationship, LogCategory *)"
- "v16@?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI}8"

```
