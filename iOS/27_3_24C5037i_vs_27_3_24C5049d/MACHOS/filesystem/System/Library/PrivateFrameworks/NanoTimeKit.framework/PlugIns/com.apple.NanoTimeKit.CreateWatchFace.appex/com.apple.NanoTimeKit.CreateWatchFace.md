## com.apple.NanoTimeKit.CreateWatchFace

> `/System/Library/PrivateFrameworks/NanoTimeKit.framework/PlugIns/com.apple.NanoTimeKit.CreateWatchFace.appex/com.apple.NanoTimeKit.CreateWatchFace`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2483.562.8.0.0
-  __TEXT.__text: 0x3ea8
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0x12a0
-  __TEXT.__objc_methlist: 0x5a4
-  __TEXT.__objc_methname: 0x1496
+2483.562.8.4.0
+  __TEXT.__text: 0x4494
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_stubs: 0x1440
+  __TEXT.__objc_methlist: 0x61c
+  __TEXT.__objc_methname: 0x1684
   __TEXT.__objc_classname: 0x104
-  __TEXT.__objc_methtype: 0x391
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x12b
-  __TEXT.__oslogstring: 0x158
-  __TEXT.__unwind_info: 0x160
-  __DATA_CONST.__const: 0x118
+  __TEXT.__objc_methtype: 0x39e
+  __TEXT.__const: 0x58
+  __TEXT.__cstring: 0x12c
+  __TEXT.__oslogstring: 0x216
+  __TEXT.__unwind_info: 0x178
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__auth_got: 0x230
-  __DATA_CONST.__got: 0x148
-  __DATA.__objc_const: 0x918
-  __DATA.__objc_selrefs: 0x6a0
-  __DATA.__objc_ivar: 0x48
+  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0x180
+  __DATA.__objc_const: 0x9a8
+  __DATA.__objc_selrefs: 0x708
+  __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x180
   - /System/Library/Frameworks/ClockKit.framework/ClockKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 88
-  Symbols:   129
-  CStrings:  335
+  Functions: 101
+  Symbols:   139
+  CStrings:  358
 
Symbols:
+ _NTKCompanionBundleComplicationManagerDidLoadNotification
+ _NTKCompanionRemoteComplicationManagerDidLoadNotification
+ _NTKSharedWidgetComplicationProvider
+ _NTKWidgetComplicationProviderComplicationsDidChange
+ _OBJC_CLASS_$_NTKCompanionBundleComplicationSyncCoordinator
+ _OBJC_CLASS_$_NTKCompanionRemoteComplicationManager
+ _OBJC_CLASS_$_NTKCompanionWidgetComplicationManager
+ _OBJC_CLASS_$_NTKWidgetComplicationManager
+ _dispatch_after
+ _dispatch_time
+ _objc_copyWeak
+ _objc_initWeak
- _NTKSharedRemoteComplicationProvider
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "Complication managers loaded"
+ "Not showing chooser yet (viewLoaded? %d, assetsLoaded? %d, complicationsLoaded? %d)"
+ "Q"
+ "TB,N,V_chooserDisplayed"
+ "TB,N,V_complicationsLoaded"
+ "TQ,N,V_pendingComplicationManagerCount"
+ "Timed out waiting for %lu complication manager(s) to load; showing the chooser with what's available"
+ "_chooserDisplayed"
+ "_complicationManagerDidLoad:"
+ "_complicationsLoaded"
+ "_displayChooserIfReady"
+ "_finishWaitingForComplicationManagers"
+ "_pendingComplicationManagerCount"
+ "_startWaitingForComplicationManagers"
+ "chooserDisplayed"
+ "complicationsLoaded"
+ "hasLoadedRemoteWidgetDescriptors"
+ "loaded"
+ "pendingComplicationManagerCount"
+ "setChooserDisplayed:"
+ "setComplicationsLoaded:"
+ "setPendingComplicationManagerCount:"
+ "sharedInstance"
+ "v24@0:8Q16"
- "waiting for viewDidLoad"
```
