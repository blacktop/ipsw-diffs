## ConnectivityModule

> `/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule`

```diff

-599.2.0.0.0
-  __TEXT.__text: 0xec10
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x170c
+600.1.1.0.0
+  __TEXT.__text: 0xefa4
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_methlist: 0x16fc
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__cstring: 0xfab
-  __TEXT.__oslogstring: 0x6c7
-  __TEXT.__unwind_info: 0x5e0
-  __TEXT.__objc_classname: 0x566
-  __TEXT.__objc_methname: 0x5a09
+  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__cstring: 0x102f
+  __TEXT.__dlopen_cstrs: 0x50
+  __TEXT.__oslogstring: 0x6b9
+  __TEXT.__unwind_info: 0x5f0
+  __TEXT.__objc_classname: 0x567
+  __TEXT.__objc_methname: 0x5a30
   __TEXT.__objc_methtype: 0x1272
-  __TEXT.__objc_stubs: 0x37a0
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__const: 0x4c8
+  __TEXT.__objc_stubs: 0x37e0
+  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__const: 0x500
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11c0
+  __DATA_CONST.__objc_selrefs: 0x11d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__auth_got: 0x2f8
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xf60
-  __AUTH_CONST.__objc_const: 0x3f08
+  __AUTH_CONST.__cfstring: 0xfa0
+  __AUTH_CONST.__objc_const: 0x3ed8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x17c
+  __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x780
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/Netrb.framework/Netrb
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation
   - /System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 542
-  Symbols:   218
-  CStrings:  1253
+  Functions: 544
+  Symbols:   222
+  CStrings:  1258
 
Symbols:
+ _OBJC_CLASS_$_NSAssertionHandler
+ _free
+ __sl_dlopen
+ _dlsym
+ _dlerror
- _WFSignalBarsFromScaledRSSI
CStrings:
+ "_systemImageNamed:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI"
+ "CCUIWiFiMenuModuleViewController.m"
+ "NSUInteger _WFSignalBarsFromScaledRSSI(float)"
+ "[Hotspot] Updated state [ inoperative: %!d(MISSING) enabled: %!d(MISSING) discoverable: %!d(MISSING) connections: %!d(MISSING) ]"
+ "%!s(MISSING)"
+ "void *WiFiKitUILibrary(void)"
+ "personalhotspot"
+ "currentHandler"
+ "_glyphImageForCurrentState"
+ "WFSignalBarsFromScaledRSSI"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "TB,N,GisDiscoverable,V_discoverable"
+ "personalhotspot.slash"
- "isAvailable"
- "setAvailable:"
- "TB,N,GisAvailable,V_available"
- "CONTROL_CENTER_STATUS_HOTSPOT_ON"
- "_available"
- "[Hotspot] Updated state [ inoperative: %!d(MISSING) available: %!d(MISSING) enabled: %!d(MISSING) discoverable: %!d(MISSING) connections: %!d(MISSING) ]"
- "HotspotGlyph"
- "available"
- "TB,GisDiscoverable,V_discoverable"

```
