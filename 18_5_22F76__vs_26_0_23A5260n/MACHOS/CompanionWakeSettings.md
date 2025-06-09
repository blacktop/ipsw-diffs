## CompanionWakeSettings

> `/System/Library/NanoPreferenceBundles/General/CompanionWakeSettings.bundle/CompanionWakeSettings`

```diff

-1113.5.2.0.0
-  __TEXT.__text: 0x2de8
-  __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x3e4
+1114.0.137.0.0
+  __TEXT.__text: 0x2e4c
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0xa60
+  __TEXT.__objc_methlist: 0x478
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x30
   __TEXT.__cstring: 0x49a
-  __TEXT.__objc_methname: 0xb86
+  __TEXT.__objc_methname: 0xc4a
   __TEXT.__oslogstring: 0x17c
-  __TEXT.__objc_classname: 0xef
-  __TEXT.__objc_methtype: 0x285
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0x178
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__objc_classname: 0x103
+  __TEXT.__objc_methtype: 0x350
+  __TEXT.__unwind_info: 0x150
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x700
-  __DATA.__objc_selrefs: 0x390
+  __DATA.__objc_const: 0xa98
+  __DATA.__objc_selrefs: 0x3e8
   __DATA.__objc_ivar: 0x4c
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x120
+  __DATA.__data: 0x180
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
-  UUID: 00A3C4F1-F32F-3F1F-A689-2B69A54DBFC6
-  Functions: 59
-  Symbols:   90
-  CStrings:  283
+  UUID: D02B5081-128A-3F6A-A203-CC89C6ED3D21
+  Functions: 60
+  Symbols:   92
+  CStrings:  302
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ _PDRDevicePropertyKeyIsPaired
+ _PSIsRadioGroupKey
+ _objc_retain_x3
- _NRPairedDeviceRegistryDeviceDidUnpairNotification
- _OBJC_CLASS_$_NSNotificationCenter
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
+ "sharedInstance"
+ "v24@0:8@\"PDRRegistry\"16"
+ "v32@0:8@\"PDRRegistry\"16@\"NSUUID\"24"
+ "v32@0:8@\"PDRRegistry\"16@\"PDRDevice\"24"
+ "v32@0:8@\"PDRRegistry\"16q24"
+ "v32@0:8@16q24"
+ "v40@0:8@\"PDRRegistry\"16@\"PDRDevice\"24@\"NSSet\"32"
+ "v40@0:8@16@24@32"
- "addObserver:selector:name:object:"
- "defaultCenter"
- "removeObserver:name:object:"

```
