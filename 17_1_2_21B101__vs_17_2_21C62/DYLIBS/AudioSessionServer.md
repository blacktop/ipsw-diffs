## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

```diff

-263.2.7.0.0
-  __TEXT.__text: 0x53b9c
+263.3.7.0.0
+  __TEXT.__text: 0x53dc8
   __TEXT.__auth_stubs: 0x1010
   __TEXT.__objc_methlist: 0x548
-  __TEXT.__gcc_except_tab: 0x6704
+  __TEXT.__gcc_except_tab: 0x6764
   __TEXT.__const: 0xb11
   __TEXT.__cstring: 0x3cd1
-  __TEXT.__oslogstring: 0x2d8f
+  __TEXT.__oslogstring: 0x2e47
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x23c4
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x12e
-  __TEXT.__objc_methname: 0x170b
+  __TEXT.__objc_methname: 0x1723
   __TEXT.__objc_methtype: 0x2660
-  __TEXT.__objc_stubs: 0xca0
-  __DATA_CONST.__got: 0x328
+  __TEXT.__objc_stubs: 0xcc0
+  __DATA_CONST.__got: 0x330
   __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1150
-  __DATA_CONST.__objc_selrefs: 0x5a0
+  __DATA_CONST.__objc_selrefs: 0x5a8
   __AUTH_CONST.__cfstring: 0x900
   __AUTH_CONST.__const: 0x9b8
   __AUTH_CONST.__objc_const: 0x1f8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F54832DE-F112-36C5-BEFC-3943428CD38B
+  UUID: 17994B6F-D0BF-3167-AA13-6C0DE094FD4B
   Functions: 1581
-  Symbols:   4416
-  CStrings:  1201
+  Symbols:   4418
+  CStrings:  1204
 
Symbols:
+ __ZN2as29GetSpecialMXNotificationNamesEv
+ __ZN2as6server16AudioSessionInfo25AddMXNotificationListenerEP8NSStringb
+ __ZN2as6server16AudioSessionInfo28RemoveMXNotificationListenerEP8NSString
+ _kMXSessionProperty_SubscribeToNotifications
+ _objc_msgSend$arrayWithObjects:count:
- __ZN2as6server16AudioSessionInfo25AddMXNotificationListenerEPK10__CFString
- __ZN2as6server16AudioSessionInfo28RemoveMXNotificationListenerEPK10__CFString
- _objc_retain_x28
CStrings:
+ "%25s:%-5d Session 0x%x failed to set SubscribeToNotifications for: %@ with a status: %d"
+ "%25s:%-5d Session 0x%x setting kMXSessionProperty_SubscribeToNotifications for notification: %@"
+ "arrayWithObjects:count:"

```
