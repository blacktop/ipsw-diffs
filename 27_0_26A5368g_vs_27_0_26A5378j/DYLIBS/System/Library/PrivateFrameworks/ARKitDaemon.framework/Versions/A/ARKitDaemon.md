## ARKitDaemon

> `/System/Library/PrivateFrameworks/ARKitDaemon.framework/Versions/A/ARKitDaemon`

```diff

-  __TEXT.__text: 0x1f324
-  __TEXT.__objc_methlist: 0x1fd4
-  __TEXT.__const: 0xd8
+  __TEXT.__text: 0x1f42c
+  __TEXT.__objc_methlist: 0x201c
+  __TEXT.__const: 0xe0
   __TEXT.__cstring: 0x1160
   __TEXT.__oslogstring: 0x3c01
   __TEXT.__gcc_except_tab: 0xcb4
-  __TEXT.__unwind_info: 0xa00
+  __TEXT.__unwind_info: 0xa10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf18
+  __DATA_CONST.__objc_selrefs: 0xf30
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x350
   __DATA_CONST.__got: 0x2c0
   __AUTH_CONST.__const: 0xc20
   __AUTH_CONST.__cfstring: 0x1080
-  __AUTH_CONST.__objc_const: 0x8320
+  __AUTH_CONST.__objc_const: 0x8370
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x2ac
+  __DATA.__objc_ivar: 0x2b0
   __DATA.__data: 0xc60
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x310

   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  Functions: 751
-  Symbols:   2393
+  Functions: 757
+  Symbols:   2404
   CStrings:  523
 
Sections:
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[ARDaemon(Testing) serviceCoordinator]
+ -[ARNetworkDeviceManager waitForOutstandingDisconnectsWithTimeout:]
+ -[ARServiceCoordinator(Testing) networkDeviceManager]
+ -[ARServiceCoordinatorConfiguration(Testing) networkDeviceManager]
+ -[ARServiceCoordinatorMacConfiguration networkDeviceManager]
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table39
+ OBJC_IVAR_$_ARNetworkDeviceManager._outstandingDisconnects
+ __OBJC_$_INSTANCE_METHODS_ARDaemon(Testing)
+ __OBJC_$_INSTANCE_METHODS_ARServiceCoordinator(InternalServiceState|Testing|ARAppConnectionLifecycleObserver|ARDaemonServiceDelegate|ARDaemonServiceListenerDelegate|StatusLogger)
+ __OBJC_$_INSTANCE_METHODS_ARServiceCoordinatorConfiguration(Testing)
+ __OBJC_CLASS_PROTOCOLS_$_ARServiceCoordinator(InternalServiceState|Testing|ARAppConnectionLifecycleObserver|ARDaemonServiceDelegate|ARDaemonServiceListenerDelegate|StatusLogger)
+ ___57-[ARNetworkDeviceManager _removeDeviceClientForDeviceID:]_block_invoke
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _dispatch_time
+ _objc_msgSend$networkDeviceManager
+ _objc_msgSend$requestDisconnectWithCompletion:
- GCC_except_table26
- GCC_except_table27
- GCC_except_table28
- GCC_except_table35
- GCC_except_table38
- __OBJC_$_INSTANCE_METHODS_ARDaemon
- __OBJC_$_INSTANCE_METHODS_ARServiceCoordinator(InternalServiceState|ARAppConnectionLifecycleObserver|ARDaemonServiceDelegate|ARDaemonServiceListenerDelegate|StatusLogger)
- __OBJC_$_INSTANCE_METHODS_ARServiceCoordinatorConfiguration
- __OBJC_$_PROP_LIST_ARDaemon
- __OBJC_$_PROP_LIST_ARServiceCoordinatorConfiguration
- __OBJC_CLASS_PROTOCOLS_$_ARServiceCoordinator(InternalServiceState|ARAppConnectionLifecycleObserver|ARDaemonServiceDelegate|ARDaemonServiceListenerDelegate|StatusLogger)
- _objc_msgSend$disconnect
Functions:
~ -[ARNetworkDeviceManager initWithAppConnectionManager:deviceIdToLoopbackPort:] : 396 -> 416
~ -[ARNetworkDeviceManager _removeDeviceClientForDeviceID:] : 1000 -> 1108
+ ___57-[ARNetworkDeviceManager _removeDeviceClientForDeviceID:]_block_invoke
~ -[ARNetworkDeviceManager _createNetworkDeviceClientWithSessionID:appConnection:] : 2040 -> 2048
+ -[ARNetworkDeviceManager waitForOutstandingDisconnectsWithTimeout:]
~ -[ARNetworkDeviceManager .cxx_destruct] : 160 -> 172
+ -[ARDaemon(Testing) serviceCoordinator]
+ -[ARServiceCoordinator(Testing) networkDeviceManager]
+ -[ARServiceCoordinatorMacConfiguration networkDeviceManager]
+ -[ARServiceCoordinatorConfiguration(Testing) networkDeviceManager]
CStrings:
+ "\xb1"
- "\xa1"

```
