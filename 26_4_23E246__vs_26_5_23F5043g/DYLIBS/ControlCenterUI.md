## ControlCenterUI

> `/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`

```diff

-655.10.0.0.0
-  __TEXT.__text: 0xb4ff8
+655.5.1.0.0
+  __TEXT.__text: 0xb5044
   __TEXT.__auth_stubs: 0x2620
   __TEXT.__objc_methlist: 0xabd0
-  __TEXT.__const: 0x27da
+  __TEXT.__const: 0x27ca
   __TEXT.__cstring: 0x4364
   __TEXT.__gcc_except_tab: 0x874
-  __TEXT.__oslogstring: 0x41cb
+  __TEXT.__oslogstring: 0x420b
   __TEXT.__dlopen_cstrs: 0x14e
   __TEXT.__constg_swiftt: 0x2840
   __TEXT.__swift5_typeref: 0x2aa6

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 164E0707-A16E-3587-AFE2-E6E3DE87C3EE
+  UUID: 98D024FC-93A7-3C8A-9C22-E655AA2A20CE
   Functions: 4773
   Symbols:   10595
-  CStrings:  6618
+  CStrings:  6619
 
Functions:
~ -[CCUICellularDataModuleViewController didBeginContextMenuPresentationForControlTemplateView:] : 216 -> 236
~ -[CCUICellularDataModuleViewController _multipleSubscriptionsAvailable] : 560 -> 544
~ -[CCUICellularDataModuleViewController _updateContentMenuActions] : 680 -> 752
CStrings:
+ "[Cellular Data Module] Updated menu actions: 0, multipleSubscriptionsAvailable is false"
+ "[Cellular Data Module] _multipleSubscriptionsAvailable... totalSubscriptions=%lu visibleSubscriptions=%lu result=%d"
- "[Cellular Data Module] _multipleSubscriptionsAvailable... totalSubscriptions=%lu visibleSubscriptions=%lu isEnabled=%d result=%d"

```
