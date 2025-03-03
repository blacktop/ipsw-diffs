## tvremoted

> `/usr/libexec/tvremoted`

```diff

-496.30.3.0.0
-  __TEXT.__text: 0xeb50
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_stubs: 0x2300
-  __TEXT.__objc_methlist: 0x9a0
+496.40.29.0.0
+  __TEXT.__text: 0xf030
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_stubs: 0x23c0
+  __TEXT.__objc_methlist: 0xed0
   __TEXT.__const: 0xca
-  __TEXT.__oslogstring: 0x1f85
+  __TEXT.__oslogstring: 0x1fdc
   __TEXT.__cstring: 0x822
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__objc_methname: 0x2fe9
+  __TEXT.__objc_methname: 0x315f
   __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methtype: 0xdc1
+  __TEXT.__objc_methtype: 0xe4f
   __TEXT.__unwind_info: 0x320
-  __DATA_CONST.__auth_got: 0x288
-  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0x678
   __DATA_CONST.__cfstring: 0x680
   __DATA_CONST.__objc_classlist: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1778
-  __DATA.__objc_selrefs: 0xb48
+  __DATA.__objc_const: 0xe78
+  __DATA.__objc_selrefs: 0xc40
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 286
-  Symbols:   2234
-  CStrings:  850
+  Functions: 295
+  Symbols:   2284
+  CStrings:  862
 
Symbols:
+ +[TVRDAssertionManager sharedInstance].cold.1
+ +[TVRDLaunchEventHandlers sharedInstance].cold.1
+ -[TVRDClientProcessConnection fetchLaunchableAppsForDeviceWithIdentifier:completion:]
+ -[TVRDClientProcessConnection launchAppForDeviceWithIdentifier:bundleID:completion:]
+ -[TVRDServer clientConnection:fetchLaunchableAppsForDeviceWithIdentifier:completion:]
+ -[TVRDServer clientConnection:launchAppForDeviceWithIdentifier:bundleID:completion:]
+ GCC_except_table77
+ GCC_except_table89
+ _OBJC_CLASS_$_TVRCButton
+ _OBJC_CLASS_$_TVRCButtonEvent
+ _TVRDIRLog.cold.1
+ _TVRDXPCLog.cold.1
+ __39-[TVRDServer _activateIRSessionManager]_block_invoke.83
+ __39-[TVRDServer _activateIRSessionManager]_block_invoke.83.cold.1
+ ___84-[TVRDServer clientConnection:launchAppForDeviceWithIdentifier:bundleID:completion:]_block_invoke
+ ___85-[TVRDServer clientConnection:fetchLaunchableAppsForDeviceWithIdentifier:completion:]_block_invoke
+ _objc_msgSend$_initWithButtonType:
+ _objc_msgSend$buttonEventForButton:eventType:
+ _objc_msgSend$clientConnection:fetchLaunchableAppsForDeviceWithIdentifier:completion:
+ _objc_msgSend$clientConnection:launchAppForDeviceWithIdentifier:bundleID:completion:
+ _objc_msgSend$fetchLaunchableAppsWithCompletion:
+ _objc_msgSend$launchAppWithBundleID:completion:
+ _objc_release_x2
+ _objc_release_x3
- GCC_except_table73
- GCC_except_table85
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.77
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.77.cold.1
CStrings:
+ "Fetching launchable apps on %{public}@"
+ "Launching app on %{public}@ bundleID=%{public}@"
+ "_initWithButtonType:"
+ "buttonEventForButton:eventType:"
+ "clientConnection:fetchLaunchableAppsForDeviceWithIdentifier:completion:"
+ "clientConnection:launchAppForDeviceWithIdentifier:bundleID:completion:"
+ "fetchLaunchableAppsForDeviceWithIdentifier:completion:"
+ "fetchLaunchableAppsWithCompletion:"
+ "launchAppForDeviceWithIdentifier:bundleID:completion:"
+ "launchAppWithBundleID:completion:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v40@0:8@\"TVRDClientProcessConnection\"16@\"NSString\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"

```
