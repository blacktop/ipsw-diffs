## SoftwareUpdateSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SoftwareUpdateSubscriber.xpc/SoftwareUpdateSubscriber`

```diff

-2171.120.44.0.1
-  __TEXT.__text: 0x533c
+2422.0.15.0.2
+  __TEXT.__text: 0x5348
   __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_stubs: 0xc80
+  __TEXT.__objc_stubs: 0xc60
   __TEXT.__objc_methlist: 0x568
   __TEXT.__objc_classname: 0x17f
   __TEXT.__const: 0x28
   __TEXT.__cstring: 0x9e9
-  __TEXT.__objc_methname: 0xeaf
+  __TEXT.__objc_methname: 0xea7
   __TEXT.__oslogstring: 0x745
   __TEXT.__objc_methtype: 0x531
   __TEXT.__unwind_info: 0xc8

   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA.__objc_const: 0x960
-  __DATA.__objc_selrefs: 0x4b0
+  __DATA.__objc_selrefs: 0x4a8
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x240

   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7ED1D2B4-B7F6-3C2D-8192-3A13BC9A9833
+  UUID: 17B70352-001B-3B29-9E5B-4EF7ED4CE59B
   Functions: 45
-  Symbols:   639
-  CStrings:  373
+  Symbols:   638
+  CStrings:  372
 
Symbols:
+ _OBJC_CLASS_$_SUUtility
+ _objc_msgSend$currentProductType
- _OBJC_CLASS_$_SUCoreDevice
- _objc_msgSend$hwModelString
- _objc_msgSend$sharedDevice
Functions:
~ -[SoftwareUpdateStatus queryForStatusWithKeyPaths:store:completionHandler:] : 1200 -> 1212
CStrings:
+ "currentProductType"
- "hwModelString"
- "sharedDevice"

```
