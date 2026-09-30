## SoftwareUpdateSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SoftwareUpdateSubscriber.xpc/SoftwareUpdateSubscriber`

```diff

-2422.40.19.502.1
-  __TEXT.__text: 0x5348
+2422.40.31.0.4
+  __TEXT.__text: 0x535c
   __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_stubs: 0xc60
+  __TEXT.__objc_stubs: 0xca0
   __TEXT.__objc_methlist: 0x568
   __TEXT.__objc_classname: 0x17f
   __TEXT.__const: 0x28
-  __TEXT.__cstring: 0x9e9
-  __TEXT.__objc_methname: 0xea7
+  __TEXT.__cstring: 0x9d3
+  __TEXT.__objc_methname: 0xec5
   __TEXT.__oslogstring: 0x745
   __TEXT.__objc_methtype: 0x531
   __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__auth_got: 0x140
-  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__got: 0x200
   __DATA_CONST.__const: 0x28
-  __DATA_CONST.__cfstring: 0x6c0
+  __DATA_CONST.__cfstring: 0x6a0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA.__objc_const: 0x960
-  __DATA.__objc_selrefs: 0x4a8
+  __DATA.__objc_selrefs: 0x4b8
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x240

   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0C063D4E-65C0-37EA-9EA1-1095A8A72D0D
+  UUID: EE374BE8-6602-3649-BBCB-48B48EAC8F67
   Functions: 45
-  Symbols:   638
+  Symbols:   642
   CStrings:  372
 
Symbols:
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_CLASS_$_NSTimeZone
+ _objc_msgSend$localTimeZone
+ _objc_msgSend$setFormatOptions:
+ _objc_msgSend$setTimeZone:
- _objc_msgSend$setDateFormat:
Functions:
~ -[SoftwareUpdateAdapter configurationUIForConfiguration:scope:completionHandler:] : 1628 -> 1648
CStrings:
+ "localTimeZone"
+ "setFormatOptions:"
+ "setTimeZone:"
- "setDateFormat:"
- "yyyy-MM-dd'T'HH:mm:ss"

```
