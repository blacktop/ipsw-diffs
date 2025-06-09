## NanoLeash

> `/System/Library/PrivateFrameworks/NanoLeash.framework/NanoLeash`

```diff

-137.0.0.0.0
-  __TEXT.__text: 0x9130
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0xf1c
-  __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__cstring: 0xc76
-  __TEXT.__dlopen_cstrs: 0x52
+138.0.0.0.0
+  __TEXT.__text: 0x8e34
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_methlist: 0xeec
+  __TEXT.__cstring: 0xbe5
+  __TEXT.__const: 0xc0
   __TEXT.__oslogstring: 0xa3d
-  __TEXT.__unwind_info: 0x308
-  __TEXT.__objc_classname: 0x23e
-  __TEXT.__objc_methname: 0x23e5
+  __TEXT.__gcc_except_tab: 0x8c
+  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__objc_classname: 0x22f
+  __TEXT.__objc_methname: 0x23fa
   __TEXT.__objc_methtype: 0xec3
-  __TEXT.__objc_stubs: 0x13c0
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x2e8
-  __DATA_CONST.__objc_classlist: 0x70
+  __TEXT.__objc_stubs: 0x1460
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c0
+  __DATA_CONST.__objc_selrefs: 0x9d8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x330
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x4a0
-  __AUTH_CONST.__objc_const: 0x1c78
+  __AUTH_CONST.__auth_got: 0x2f8
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0x460
+  __AUTH_CONST.__objc_const: 0x1be8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x460
+  __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x310
-  __DATA.__bss: 0x68
   __DATA.__common: 0x8
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7BE9600B-0643-31D3-90D4-34DF0B3A1968
-  Functions: 275
-  Symbols:   1142
-  CStrings:  720
+  UUID: 5A41B0FA-16FF-3F75-B245-5D62183C174E
+  Functions: 265
+  Symbols:   1094
+  CStrings:  713
 
Symbols:
+ _objc_msgSend$_setError
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
- +[NFMWiFiManager sharedManager]
- +[NFMWiFiManager sharedManager].cold.1
- -[NFMWiFiManager setHoldWiFiAssertion:]
- -[NFMWiFiManager setHoldWiFiAssertion:].cold.1
- -[NFMWiFiManager setHoldWiFiAssertion:].cold.2
- -[NFMWiFiManager setHoldWiFiAssertion:].cold.3
- GCC_except_table2
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _MobileWiFiLibrary
- _MobileWiFiLibraryCore.frameworkLibrary
- _NSLog
- _OBJC_CLASS_$_NFMWiFiManager
- _OBJC_METACLASS_$_NFMWiFiManager
- __Block_object_dispose
- __OBJC_$_CLASS_METHODS_NFMWiFiManager
- __OBJC_$_INSTANCE_METHODS_NFMWiFiManager
- __OBJC_CLASS_RO_$_NFMWiFiManager
- __OBJC_METACLASS_RO_$_NFMWiFiManager
- ___31+[NFMWiFiManager sharedManager]_block_invoke
- ___MobileWiFiLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___getWiFiManagerClientCreateSymbolLoc_block_invoke
- ___getWiFiManagerClientGetTypeSymbolLoc_block_invoke
- ___getWiFiManagerClientSetTypeSymbolLoc_block_invoke
- ___wifiManager
- __sl_dlopen
- _abort_report_np
- _audit_stringMobileWiFi
- _dlerror
- _dlsym
- _free
- _getWiFiManagerClientCreateSymbolLoc.ptr
- _getWiFiManagerClientGetTypeSymbolLoc.ptr
- _getWiFiManagerClientSetTypeSymbolLoc.ptr
- _kCFAllocatorDefault
- _sharedManager.__sharedManager
- _sharedManager.onceToken
CStrings:
+ "_setError"
+ "getBytes:range:"
+ "hasError"
+ "position"
+ "setPosition:"
- "########### Released WiFi Assertion"
- "########### Took WiFi Assertion"
- "%s"
- "NFMWiFiManager"
- "WiFiManagerClientCreate"
- "WiFiManagerClientGetType"
- "WiFiManagerClientSetType"
- "setHoldWiFiAssertion:"
- "sharedManager"
- "softlink:r:path:/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi"

```
