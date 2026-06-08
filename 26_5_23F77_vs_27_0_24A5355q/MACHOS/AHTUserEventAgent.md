## AHTUserEventAgent

> `/System/Library/UserEventPlugins/AHTUserEventAgent.plugin/AHTUserEventAgent`

```diff

-9140.6.0.0.0
-  __TEXT.__text: 0x60b4
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x52c
-  __TEXT.__cstring: 0xb92
-  __TEXT.__objc_classname: 0x9e
+10100.34.0.0.0
+  __TEXT.__text: 0x57d4
+  __TEXT.__auth_stubs: 0x590
+  __TEXT.__objc_stubs: 0xb00
+  __TEXT.__objc_methlist: 0x514
+  __TEXT.__cstring: 0xb6b
+  __TEXT.__objc_classname: 0x92
   __TEXT.__objc_methtype: 0x368
-  __TEXT.__objc_methname: 0xd02
+  __TEXT.__objc_methname: 0xcba
   __TEXT.__const: 0x240
-  __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__oslogstring: 0x620
-  __TEXT.__unwind_info: 0x1f0
-  __DATA.__auth_got: 0x2e8
-  __DATA.__got: 0x98
+  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__oslogstring: 0x5c6
+  __TEXT.__unwind_info: 0x1b0
   __DATA.__const: 0x1d8
   __DATA.__cfstring: 0xba0
   __DATA.__objc_classlist: 0x28
   __DATA.__objc_catlist: 0x8
   __DATA.__objc_protolist: 0x10
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xc10
+  __DATA.__objc_const: 0xbe0
   __DATA.__objc_selrefs: 0x3f0
   __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0x190
   __DATA.__objc_intobj: 0x4e0
   __DATA.__data: 0x3e0
   __DATA.__objc_arraydata: 0x10
   __DATA.__objc_arrayobj: 0x18
+  __DATA.__auth_got: 0x2d8
+  __DATA.__got: 0xa0
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C7764C78-EB08-339D-88DE-C856B1E8709B
-  Functions: 146
-  Symbols:   151
-  CStrings:  518
+  UUID: ADE84F33-A897-3555-B12E-FC59E613EEB0
+  Functions: 138
+  Symbols:   150
+  CStrings:  512
 
Symbols:
+ _OBJC_CLASS_$_AHTBootLoader
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x25
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "Added bootloader %@ for parent node: %@ memory dump support %s"
+ "T@\"AHTDeviceMatchingNotification\",&,N,V_bootloaderAdded"
+ "_bootloaderAdded"
+ "bootloaderAdded"
+ "device"
+ "interface"
+ "setBootloaderAdded:"
- "Added Device %@ bootloader %@ memory dump support %s"
- "Added Interface %@ bootloader %@ memory dump support %s"
- "AppleHIDTransportDevice"
- "AppleHIDTransportInterface"
- "Cannot create InterfaceMatchingNotification"
- "T@\"AHTDeviceMatchingNotification\",&,N,V_deviceAdded"
- "T@\"AHTDeviceMatchingNotification\",&,N,V_interfaceAdded"
- "_deviceAdded"
- "_interfaceAdded"
- "deviceAdded"
- "interfaceAdded"
- "setDeviceAdded:"
- "setInterfaceAdded:"

```
