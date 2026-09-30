## NotificationCenter

> `/System/Library/Frameworks/NotificationCenter.framework/Versions/A/NotificationCenter`

```diff

-1459.3.3.404.0
-  __TEXT.__text: 0x1f74c
+1459.4.21.0.0
+  __TEXT.__text: 0x1fb5c
   __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x222c
-  __TEXT.__const: 0x368
-  __TEXT.__gcc_except_tab: 0x418
+  __TEXT.__objc_methlist: 0x2a08
+  __TEXT.__const: 0x358
+  __TEXT.__gcc_except_tab: 0x414
   __TEXT.__cstring: 0x1487
   __TEXT.__oslogstring: 0x7b4
-  __TEXT.__unwind_info: 0xa40
+  __TEXT.__unwind_info: 0xaa0
   __TEXT.__objc_classname: 0x8e4
   __TEXT.__objc_methname: 0x6f92
   __TEXT.__objc_methtype: 0x11f9

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19e0
+  __DATA_CONST.__objc_selrefs: 0x1c18
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__const: 0x8e0
   __AUTH_CONST.__cfstring: 0x1340
-  __AUTH_CONST.__objc_const: 0x6598
+  __AUTH_CONST.__objc_const: 0x5788
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1090

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DC3FA3A9-BA4E-34C5-9186-35B3E8ED8163
-  Functions: 946
-  Symbols:   2647
+  UUID: DE396AAE-DDA7-3A34-A258-4485A41B150E
+  Functions: 971
+  Symbols:   2671
   CStrings:  1961
 
Symbols:
+ +[NCRemoteViewServiceSubsystem serviceForContext:].cold.1
+ +[NCWidgetController widgetController].cold.1
+ -[NCRemotePlugIn setupPlugIn].cold.3
+ -[NCRemotePlugInManager init].cold.1
+ -[NCRemoteViewServiceSubsystem installViewControllerInWindow:].cold.1
+ -[NCRemoteViewServiceSubsystem installViewControllerInWindow:].cold.2
+ -[NCRemoteViewServiceViewController dismissAlternateViewController:fromViewController:].cold.1
+ -[NCRemoteViewServiceViewController remoteViewReadyForDisplay:block:].cold.2
+ -[NCRemoteViewServiceViewController remoteViewReadyForDisplay:block:].cold.3
+ -[NCVerticalListController endUpdates].cold.1
+ -[NCVerticalListController moveView:toIndex:animate:].cold.1
+ -[NCVerticalListController swapView:withView:].cold.1
+ -[_NCConcreteWidgetController setHasContent:forWidgetWithBundleIdentifier:].cold.1
+ ContinuousTimeGetCurrent.cold.1
+ NCDuration.cold.1
+ NCSetCocoaBinding.cold.1
+ OSLogRemotePluginSystem.cold.1
+ _NCDistributedNotificationCenter.cold.1
+ _NCNotificationCenter.cold.1
+ _NCNotificationRegisterClass.cold.1
+ _OSLogRemoteViewLogging.cold.1
+ __33-[NCRemotePlugIn _activatePlugIn]_block_invoke_2.cold.3
+ __33-[NCRemotePlugIn _activatePlugIn]_block_invoke_2.cold.4
+ __50-[NCRemoteViewHostViewController _setupRemoteView]_block_invoke_3.cold.2
+ __50-[NCRemoteViewHostViewController _setupRemoteView]_block_invoke_3.cold.3
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3

```
