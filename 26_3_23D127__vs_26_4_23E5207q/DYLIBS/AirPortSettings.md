## AirPortSettings

> `/System/Library/PreferenceBundles/AirPortSettings.bundle/AirPortSettings`

```diff

 1175.0.0.0.0
-  __TEXT.__text: 0xaec
-  __TEXT.__auth_stubs: 0x170
+  __TEXT.__text: 0xc50
+  __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_methlist: 0xf8
   __TEXT.__cstring: 0x267
-  __TEXT.__unwind_info: 0x90
+  __TEXT.__unwind_info: 0xa8
   __TEXT.__objc_classname: 0x17
   __TEXT.__objc_methname: 0x479
   __TEXT.__objc_methtype: 0x8f

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xc0
+  __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x1c0
   __AUTH.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 126C9270-5BCB-3307-99D2-D8C1EE8B6C08
+  UUID: 013B5939-1E32-3130-A3F9-FC9E99600679
   Functions: 20
-  Symbols:   124
+  Symbols:   126
   CStrings:  111
 
Symbols:
+ _objc_release_x8
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x2
Functions:
~ -[APNetworksController initWithNibName:bundle:] : 140 -> 148
~ -[APNetworksController loadView] : 608 -> 660
~ -[APNetworksController viewDidAppear:] : 104 -> 108
~ -[APNetworksController viewDidDisappear:] : 124 -> 132
~ -[APNetworksController viewWillDisappear:] : 104 -> 108
~ -[APNetworksController handleURL:] : 436 -> 472
~ -[APNetworksController _loadHealthOverrides] : 724 -> 728
~ -[APNetworksController setHealthOverrides:] : 20 -> 80
~ -[APNetworksController setAirportController:] : 20 -> 80
~ -[APNetworksController setSettingsViewController:] : 20 -> 80
~ -[APNetworksController setDeferredURL:] : 20 -> 80

```
