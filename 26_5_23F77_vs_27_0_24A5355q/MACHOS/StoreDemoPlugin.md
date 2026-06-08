## StoreDemoPlugin

> `/System/Library/SpringBoardPlugins/StoreDemoPlugin.servicebundle/StoreDemoPlugin`

```diff

-1611.120.9.0.0
-  __TEXT.__text: 0xbecc
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_stubs: 0x2660
-  __TEXT.__objc_methlist: 0xd1c
+1865.0.0.0.0
+  __TEXT.__text: 0xb794
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0x2880
+  __TEXT.__objc_methlist: 0xd9c
   __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__oslogstring: 0x121a
-  __TEXT.__cstring: 0xb9f
-  __TEXT.__objc_classname: 0x15b
-  __TEXT.__objc_methname: 0x2a63
-  __TEXT.__objc_methtype: 0x4a8
-  __TEXT.__unwind_info: 0x390
-  __DATA_CONST.__auth_got: 0x330
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x3b0
-  __DATA_CONST.__cfstring: 0xa60
+  __TEXT.__gcc_except_tab: 0x174
+  __TEXT.__oslogstring: 0x1418
+  __TEXT.__cstring: 0xd0f
+  __TEXT.__objc_classname: 0x138
+  __TEXT.__objc_methname: 0x2d8f
+  __TEXT.__objc_methtype: 0x41a
+  __TEXT.__unwind_info: 0x2f0
+  __DATA_CONST.__const: 0x3d8
+  __DATA_CONST.__cfstring: 0xaa0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xde0
-  __DATA.__objc_selrefs: 0xd18
-  __DATA.__objc_ivar: 0x84
+  __DATA_CONST.__auth_got: 0x398
+  __DATA_CONST.__got: 0x240
+  __DATA.__objc_const: 0xe70
+  __DATA.__objc_selrefs: 0xda0
+  __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x300
+  __DATA.__data: 0x2a0
   __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3337F07E-2E35-3984-B2C9-B46773A396D4
-  Functions: 286
-  Symbols:   198
-  CStrings:  856
+  UUID: AF78DD6F-AF94-325E-BB45-1147D513CEEB
+  Functions: 304
+  Symbols:   213
+  CStrings:  896
 
Symbols:
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFStringCompare
+ _OBJC_CLASS_$_FBSDisplayLayoutMonitorConfiguration
+ _handleSecondaryScreenSaverAppChangedNotification
+ _objc_claimAutoreleasedReturnValue
+ _objc_getProperty
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x23
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
+ _objc_setProperty_atomic
CStrings:
+ "%s"
+ "%s - No ScreenSaver app available. RBSProcessMonitor not initialized"
+ "%s - called"
+ "-[MSDScreenSaverManager _createProcessMonitor]"
+ "-[MSDScreenSaverManager _handleSecondaryScreenSaverAppChangedNotification]_block_invoke"
+ "-[MSDScreenSaverManager setSecondaryScreenSaverAppID:]"
+ "@\"FBSDisplayLayoutMonitor\""
+ "App with bundle ID %{public}@ does not exist on device. Failed to set it as the Secondary Screensaver App"
+ "Building RBSProcessPredicate for process %{public}@"
+ "Device in Screensaver Launch Mode: %{bool}d, screensaver: %{public}@, will not launch screen saver."
+ "DeviceSupportsAlwaysOnTime"
+ "DisableAssetDownload"
+ "MSDScreenSaverManager never received the demo state from demod. Continuing anyway..."
+ "Received notification: %{public}s"
+ "Secondary Screen saver app is %{public}@"
+ "T@\"FBSDisplayLayoutMonitor\",&,V_displayLayoutMonitor"
+ "T@\"NSString\",&,N,V_secondaryScreenSaverAppID"
+ "TB,V_isInRetailDeviceUpdatingContentMode"
+ "TB,V_isInScreenSaverLaunchMode"
+ "_closeRunningAppsAllowList"
+ "_createProcessMonitor"
+ "_displayLayoutMonitor"
+ "_getProcessPredicatesForScreenSaverProcessMonitor"
+ "_handleSecondaryScreenSaverAppChangedNotification"
+ "_isInRetailDeviceUpdatingContentMode"
+ "_isInScreenSaverLaunchMode"
+ "_layoutMonitorDidUpdateDisplayLayout:"
+ "_registerForSecondaryScreenSaverAppChangedNotifications"
+ "_secondaryScreenSaverAppID"
+ "arrayWithArray:"
+ "com.apple.MobileStoreDemo.SecondaryScreenSaverApp"
+ "configurationForDefaultMainDisplayMonitor"
+ "disableAssetDownload"
+ "displayLayoutMonitor"
+ "getSecondaryScreenSaverAppBundleID"
+ "isInRetailDeviceUpdatingContentMode"
+ "isInRetailDeviceUpdatingContentMode: %{bool}d"
+ "isInScreenSaverLaunchMode"
+ "isInScreenSaverLaunchMode: %{bool}d"
+ "secondaryScreenSaverAppID"
+ "setDisplayLayoutMonitor:"
+ "setIsInRetailDeviceUpdatingContentMode:"
+ "setIsInScreenSaverLaunchMode:"
+ "setNeedsUserInteractivePriority:"
+ "setSecondaryScreenSaverAppID:"
+ "setTransitionHandler:"
+ "v32@?0@\"FBSDisplayLayoutMonitor\"8@\"FBSDisplayLayout\"16@\"FBSDisplayLayoutTransitionContext\"24"
- "Device in mode %d, screensaver: %{public}@, will not launch screen saver."
- "FBSDisplayLayoutObserver"
- "j8/Omm6s1lsmTDFsXjsBfA"
- "layoutMonitor:didUpdateDisplayLayout:"
- "layoutMonitor:didUpdateDisplayLayout:withContext:"
- "sharedMonitorForDisplayType:"
- "v32@0:8@\"FBSDisplayLayoutMonitor\"16@\"FBSDisplayLayout\"24"
- "v40@0:8@\"FBSDisplayLayoutMonitor\"16@\"FBSDisplayLayout\"24@\"FBSDisplayLayoutTransitionContext\"32"
- "v40@0:8@16@24@32"

```
