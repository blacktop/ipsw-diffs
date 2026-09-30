## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`

```diff

-190.51.1.6.0
-  __TEXT.__text: 0xb4fc0
+191.5.1.1.0
+  __TEXT.__text: 0xb5210
   __TEXT.__auth_stubs: 0x13a0
   __TEXT.__objc_methlist: 0xa0b4
   __TEXT.__const: 0x2773
   __TEXT.__oslogstring: 0x2b1b
-  __TEXT.__cstring: 0x1514b
-  __TEXT.__gcc_except_tab: 0x2f40
+  __TEXT.__cstring: 0x15182
+  __TEXT.__gcc_except_tab: 0x2f88
   __TEXT.__ustring: 0x82
   __TEXT.__unwind_info: 0x2160
   __TEXT.__eh_frame: 0x98

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00B3B947-B4B1-3AF5-8E48-1409653DED78
+  UUID: 46A54514-486F-3EE0-87CD-F86F0B284BC6
   Functions: 4248
   Symbols:   13818
-  CStrings:  10509
+  CStrings:  10511
 
Functions:
~ +[CBUserController readPrefKeys:source:error:] : 796 -> 804
~ +[CBUserController writePrefKey:value:source:error:] : 760 -> 768
~ -[CBConnection activateDirectAndReturnError:] : 1248 -> 1552
~ -[CBConnection updateWithXPCSubscriberInfo:] : 480 -> 736
~ -[CBConnection _setupIOAndReturnError:] : 728 -> 744
CStrings:
+ "Activate incoming LoD, peer %@, PSM 0x%X, sock %d"
+ "MobileBluetooth-191.5.1.1"
- "MobileBluetooth-190.51.1.6"

```
