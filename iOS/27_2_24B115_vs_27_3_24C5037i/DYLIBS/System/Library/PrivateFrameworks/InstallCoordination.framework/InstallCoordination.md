## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-849.40.7.0.2
-  __TEXT.__text: 0x6f390
-  __TEXT.__objc_methlist: 0x4c88
+849.60.8.0.0
+  __TEXT.__text: 0x6f6a0
+  __TEXT.__objc_methlist: 0x4d20
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x10b76
+  __TEXT.__cstring: 0x10b10
   __TEXT.__oslogstring: 0x89f4
-  __TEXT.__gcc_except_tab: 0x1f78
+  __TEXT.__gcc_except_tab: 0x1fc4
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x24b8
+  __TEXT.__unwind_info: 0x24d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1fd0
-  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__const: 0x1fb0
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2500
+  __DATA_CONST.__objc_selrefs: 0x2540
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x120
-  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__got: 0x538
   __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__cfstring: 0x6560
-  __AUTH_CONST.__objc_const: 0xd670
+  __AUTH_CONST.__objc_const: 0xd7e8
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__auth_got: 0x608
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x278
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x288
   __DATA_DIRTY.__objc_data: 0x1540
   __DATA_DIRTY.__data: 0xb18
   __DATA_DIRTY.__bss: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2310
-  Symbols:   3236
+  Functions: 2322
+  Symbols:   3256
   CStrings:  1951
 
Symbols:
+ +[IXManagedAppTracker sharedTracker]
+ -[IXManagedAppTracker .cxx_destruct]
+ -[IXManagedAppTracker _onQueue_subscribeWithError:]
+ -[IXManagedAppTracker init]
+ -[IXManagedAppTracker managedAppBundleIdentifiersWithError:]
+ -[IXManagedAppTracker managedAppBundleIdentifiers]
+ -[IXManagedAppTracker queue]
+ -[IXManagedAppTracker reSubscribeCount]
+ -[IXManagedAppTracker setManagedAppBundleIdentifiers:]
+ -[IXManagedAppTracker setReSubscribeCount:]
+ -[IXManagedAppTracker setSubscription:]
+ -[IXManagedAppTracker startTrackingWithError:]
+ -[IXManagedAppTracker subscription]
+ GCC_except_table12
+ _OBJC_CLASS_$_IXManagedAppTracker
+ _OBJC_IVAR_$_IXManagedAppTracker._managedAppBundleIdentifiers
+ _OBJC_IVAR_$_IXManagedAppTracker._queue
+ _OBJC_IVAR_$_IXManagedAppTracker._reSubscribeCount
+ _OBJC_IVAR_$_IXManagedAppTracker._subscription
+ _OBJC_METACLASS_$_IXManagedAppTracker
+ __OBJC_$_CLASS_METHODS_IXManagedAppTracker
+ __OBJC_$_CLASS_PROP_LIST_IXManagedAppTracker
+ __OBJC_$_INSTANCE_METHODS_IXManagedAppTracker
+ __OBJC_$_INSTANCE_VARIABLES_IXManagedAppTracker
+ __OBJC_$_PROP_LIST_IXManagedAppTracker
+ __OBJC_CLASS_RO_$_IXManagedAppTracker
+ __OBJC_METACLASS_RO_$_IXManagedAppTracker
+ ___36+[IXManagedAppTracker sharedTracker]_block_invoke
+ ___46-[IXManagedAppTracker startTrackingWithError:]_block_invoke
+ ___51-[IXManagedAppTracker _onQueue_subscribeWithError:]_block_invoke
+ ___51-[IXManagedAppTracker _onQueue_subscribeWithError:]_block_invoke_2
+ ___51-[IXManagedAppTracker _onQueue_subscribeWithError:]_block_invoke_3
+ ___60-[IXManagedAppTracker managedAppBundleIdentifiersWithError:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e20_v24?0q8"NSError"16ls32l8w40l8
+ ___block_descriptor_48_e8_32s40w_e28_v16?0"MDFManagedAppEvent"8ls32l8w40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ _sharedTracker.onceToken
+ _sharedTracker.sharedTracker
- +[IXAppInstallCoordinator(IXAppReplacement) _onQueue_subscribeToManagedAppEventsWithError:]
- +[IXAppInstallCoordinator(IXAppReplacement) managedAppBundleIdentifiersWithError:]
- __ManagedAppQueue
- __ManagedAppQueue.onceToken
- __ManagedAppQueue.queue
- ___82+[IXAppInstallCoordinator(IXAppReplacement) managedAppBundleIdentifiersWithError:]_block_invoke
- ___91+[IXAppInstallCoordinator(IXAppReplacement) _onQueue_subscribeToManagedAppEventsWithError:]_block_invoke
- ___91+[IXAppInstallCoordinator(IXAppReplacement) _onQueue_subscribeToManagedAppEventsWithError:]_block_invoke_2
- ___91+[IXAppInstallCoordinator(IXAppReplacement) _onQueue_subscribeToManagedAppEventsWithError:]_block_invoke_3
- ___99+[IXAppInstallCoordinator(IXAppReplacement) prepareForAppReplacementSourceLookupWithOptions:error:]_block_invoke
- ____ManagedAppQueue_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_40_e8_32s_e28_v16?0"MDFManagedAppEvent"8ls32l8
- ___block_descriptor_48_e5_v8?0l
- ___block_descriptor_48_e8_32s_e20_v24?0q8"NSError"16ls32l8
- ___block_descriptor_56_e8_32r40r_e5_v8?0lr32l8r40l8
- _sManagedAppBundleIdentifiers
- _sManagedAppSubscription
- _sReSubscribeCount
CStrings:
+ "-[IXManagedAppTracker _onQueue_subscribeWithError:]_block_invoke"
+ "-[IXManagedAppTracker _onQueue_subscribeWithError:]_block_invoke_3"
+ "-[IXManagedAppTracker managedAppBundleIdentifiersWithError:]"
- "+[IXAppInstallCoordinator(IXAppReplacement) _onQueue_subscribeToManagedAppEventsWithError:]_block_invoke"
- "+[IXAppInstallCoordinator(IXAppReplacement) _onQueue_subscribeToManagedAppEventsWithError:]_block_invoke_3"
- "+[IXAppInstallCoordinator(IXAppReplacement) managedAppBundleIdentifiersWithError:]"
```
