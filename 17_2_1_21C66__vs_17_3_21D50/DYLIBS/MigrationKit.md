## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-17.2.5.0.0
-  __TEXT.__text: 0x301a4
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_methlist: 0x343c
+17.3.4.0.0
+  __TEXT.__text: 0x30650
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_methlist: 0x34bc
   __TEXT.__const: 0x44c
-  __TEXT.__cstring: 0x3011
-  __TEXT.__oslogstring: 0x2345
+  __TEXT.__cstring: 0x3025
+  __TEXT.__oslogstring: 0x236e
   __TEXT.__gcc_except_tab: 0xc24
-  __TEXT.__unwind_info: 0xcd0
+  __TEXT.__unwind_info: 0xce0
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x803
-  __TEXT.__objc_methname: 0x6ea0
-  __TEXT.__objc_methtype: 0xf58
-  __TEXT.__objc_stubs: 0x6de0
+  __TEXT.__objc_classname: 0x810
+  __TEXT.__objc_methname: 0x6f4e
+  __TEXT.__objc_methtype: 0xf78
+  __TEXT.__objc_stubs: 0x6e80
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x5c0
-  __DATA_CONST.__objc_classlist: 0x328
+  __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6a48
-  __DATA_CONST.__objc_selrefs: 0x1dd8
+  __DATA_CONST.__objc_const: 0x6ad8
+  __DATA_CONST.__objc_selrefs: 0x1e10
   __DATA_CONST.__objc_arraydata: 0x480
-  __AUTH_CONST.__objc_intobj: 0xc00
-  __AUTH_CONST.__cfstring: 0x4520
-  __AUTH_CONST.__objc_const: 0x1e98
+  __AUTH_CONST.__objc_intobj: 0xc18
+  __AUTH_CONST.__cfstring: 0x4580
+  __AUTH_CONST.__objc_const: 0x1f28
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x610
-  __AUTH.__objc_data: 0x1f40
-  __DATA.__objc_classrefs: 0x508
+  __AUTH_CONST.__auth_got: 0x630
+  __AUTH.__objc_data: 0x1f90
+  __DATA.__objc_classrefs: 0x510
   __DATA.__objc_superrefs: 0x250
-  __DATA.__objc_ivar: 0x578
+  __DATA.__objc_ivar: 0x584
   __DATA.__data: 0x540
   __DATA.__bss: 0x1b0
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary
+  - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
+  - /System/Library/PrivateFrameworks/Netrb.framework/Netrb
   - /System/Library/PrivateFrameworks/StoreServices.framework/StoreServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 6D22C982-D38D-3866-8D46-E72790F2C1CA
-  Functions: 1332
-  Symbols:   5181
-  CStrings:  3194
+  UUID: 8DD764E7-0162-31FA-A54F-BAF10832EBB5
+  Functions: 1343
+  Symbols:   5221
+  CStrings:  3214
 
Symbols:
+ +[MKAPIServer clean]
+ +[MKAPIServer clean].cold.1
+ -[MKAPIServer preferredChannel]
+ -[MKAPIServer setPreferredChannel:]
+ -[MKDevice deviceName]
+ -[MKDevice setDeviceName:]
+ -[MKGETStatusRouter preferredChannel]
+ -[MKGETStatusRouter setPreferredChannel:]
+ -[MKWiFiDevice channel:]
+ -[MKWiFiDevice currentNetwork]
+ GCC_except_table18
+ GCC_except_table23
+ GCC_except_table27
+ GCC_except_table33
+ GCC_except_table38
+ _OBJC_CLASS_$_MKWiFiDevice
+ _OBJC_IVAR_$_MKAPIServer._preferredChannel
+ _OBJC_IVAR_$_MKDevice._deviceName
+ _OBJC_IVAR_$_MKGETStatusRouter._preferredChannel
+ _OBJC_METACLASS_$_MKWiFiDevice
+ _WiFiDeviceClientCopyCurrentNetwork
+ _WiFiManagerClientCreate
+ _WiFiManagerClientGetDevice
+ _WiFiNetworkGetChannel
+ __OBJC_$_CLASS_METHODS_MKAPIServer
+ __OBJC_$_INSTANCE_METHODS_MKWiFiDevice
+ __OBJC_CLASS_RO_$_MKWiFiDevice
+ __OBJC_METACLASS_RO_$_MKWiFiDevice
+ _objc_msgSend$channel:
+ _objc_msgSend$currentNetwork
+ _objc_msgSend$deviceName
+ _objc_msgSend$setDeviceName:
+ _objc_msgSend$setPreferredChannel:
- GCC_except_table20
- GCC_except_table25
- GCC_except_table28
- GCC_except_table37
CStrings:
+ "\x1f\t!"
+ "$"
+ "@24@0:8^{__WiFiDeviceClient=}16"
+ "MKWiFiDevice"
+ "T@\"NSString\",C,N,V_deviceName"
+ "Tq,N,V_preferredChannel"
+ "_deviceName"
+ "_preferredChannel"
+ "ap1"
+ "channel:"
+ "clean"
+ "could not delete the workspace. error=%@"
+ "currentNetwork"
+ "deviceName"
+ "device_name"
+ "en0"
+ "preferredChannel"
+ "setDeviceName:"
+ "setPreferredChannel:"
- "\x1f\t\x11"
- "#"

```
