## CompanionReturnToClockSettings

> `/System/Library/NanoPreferenceBundles/General/CompanionReturnToClockSettings.bundle/CompanionReturnToClockSettings`

```diff

-1113.5.2.0.0
-  __TEXT.__text: 0x5138
+1114.0.137.0.0
+  __TEXT.__text: 0x516c
   __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x6a4
-  __TEXT.__const: 0x78
+  __TEXT.__objc_stubs: 0xdc0
+  __TEXT.__objc_methlist: 0x748
+  __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__cstring: 0x7ed
-  __TEXT.__objc_methname: 0x12fe
+  __TEXT.__cstring: 0x734
+  __TEXT.__objc_methname: 0x13af
   __TEXT.__oslogstring: 0x27c
-  __TEXT.__objc_classname: 0x17d
-  __TEXT.__objc_methtype: 0x332
-  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__objc_classname: 0x191
+  __TEXT.__objc_methtype: 0x3fd
+  __TEXT.__unwind_info: 0x1e0
   __DATA_CONST.__auth_got: 0x1a8
-  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x210
-  __DATA_CONST.__cfstring: 0x840
+  __DATA_CONST.__cfstring: 0x7a0
   __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0xe78
-  __DATA.__objc_selrefs: 0x530
+  __DATA.__objc_const: 0x1378
+  __DATA.__objc_selrefs: 0x580
   __DATA.__objc_ivar: 0x88
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x240
+  __DATA.__data: 0x2a0
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 83138233-2B17-33F5-834D-44E88A699FD6
-  Functions: 124
-  Symbols:   106
-  CStrings:  436
+  UUID: 3DC36C0E-FE54-35FF-878F-596C61338C8B
+  Functions: 126
+  Symbols:   105
+  CStrings:  444
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ _PDRDevicePropertyKeyIsPaired
+ _PSIsRadioGroupKey
- _NRPairedDeviceRegistryDeviceDidUnpairNotification
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_CLASS_$_NSUUID
CStrings:
+ "PDRRegistryDelegate"
+ "addDelegate:"
+ "containsObject:"
+ "isPaired"
+ "registry:added:"
+ "registry:changed:properties:"
+ "registry:compatibilityStateChanged:"
+ "registry:didActivate:"
+ "registry:didDeactivate:"
+ "registry:didPair:"
+ "registry:didSetup:"
+ "registry:didUnpair:"
+ "registry:removed:"
+ "registryChanged:"
+ "removeDelegate:"
+ "v24@0:8@\"PDRRegistry\"16"
+ "v32@0:8@\"PDRRegistry\"16@\"NSUUID\"24"
+ "v32@0:8@\"PDRRegistry\"16@\"PDRDevice\"24"
+ "v32@0:8@\"PDRRegistry\"16q24"
+ "v32@0:8@16q24"
+ "v40@0:8@\"PDRRegistry\"16@\"PDRDevice\"24@\"NSSet\"32"
+ "v40@0:8@16@24@32"
- "410B4A76-885F-4715-83AF-E23513740668"
- "5A9640F0-1FE3-4019-8157-075CBFC8DBA1"
- "62AA8EC5-64FC-43D1-B856-D28D6520FA30"
- "B81E9BEF-B19B-4468-8887-44BE181472C0"
- "ED96B2DC-49DD-470D-BFE6-1F112AF20308"
- "addObserver:selector:name:object:"
- "defaultCenter"
- "initWithUUIDString:"
- "removeObserver:name:object:"

```
