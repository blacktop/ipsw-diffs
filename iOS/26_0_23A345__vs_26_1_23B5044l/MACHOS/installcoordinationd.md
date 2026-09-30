## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-775.0.0.0.0
-  __TEXT.__text: 0xa6b64
+781.0.0.0.1
+  __TEXT.__text: 0xa7ab4
   __TEXT.__auth_stubs: 0x1130
-  __TEXT.__objc_stubs: 0xafe0
-  __TEXT.__objc_methlist: 0x5d74
+  __TEXT.__objc_stubs: 0xb0a0
+  __TEXT.__objc_methlist: 0x5e04
   __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x18c65
-  __TEXT.__objc_methname: 0x10e99
+  __TEXT.__cstring: 0x18fb1
+  __TEXT.__objc_methname: 0x110c1
   __TEXT.__objc_classname: 0xa21
-  __TEXT.__objc_methtype: 0x23a7
-  __TEXT.__oslogstring: 0xdf1a
+  __TEXT.__objc_methtype: 0x23e5
+  __TEXT.__oslogstring: 0xe083
   __TEXT.__gcc_except_tab: 0x32fc
   __TEXT.__ustring: 0x1a68
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x26a8
+  __TEXT.__unwind_info: 0x26f8
   __DATA_CONST.__auth_got: 0x8a8
   __DATA_CONST.__got: 0x458
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2d38
-  __DATA_CONST.__cfstring: 0x9d60
+  __DATA_CONST.__const: 0x2d60
+  __DATA_CONST.__cfstring: 0x9dc0
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xc4d0
-  __DATA.__objc_selrefs: 0x33d8
-  __DATA.__objc_ivar: 0x4b0
+  __DATA.__objc_const: 0xc580
+  __DATA.__objc_selrefs: 0x3420
+  __DATA.__objc_ivar: 0x4b4
   __DATA.__objc_data: 0x1720
   __DATA.__data: 0x6b0
   __DATA.__crash_info: 0x148

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8DD6BBB4-7741-31ED-8C7E-52FF88C2FAD8
-  Functions: 3357
+  UUID: CAE4C5A0-52DF-3914-BF97-06376132231F
+  Functions: 3375
   Symbols:   429
-  CStrings:  6830
+  CStrings:  6863
 
CStrings:
+ "%s: Client %@ is missing OS Module operation entitlement. : %@"
+ "%s: Client %@ is missing OSModule operation entitlement. : %@"
+ "%s: Failed to register task %@ with Duet"
+ "%s: Failed to schedule install for %@; running immediately"
+ "%s: STUB: Reconciling known OSModule URLs %@ set by client %@"
+ "%s: STUB: Registering contents for OSModule at %@ by client %@"
+ "%s: STUB: Unregistering contents of OSModule at %@ by client %@"
+ "-[IXSAppInstallObserverManager _onQueue_messageMachServices:forMethod:callMethodOnProxy:exceptServices:]"
+ "-[IXSAppInstallObserverManager _onQueue_messageMachServices:forMethod:callMethodOnProxy:exceptServices:]_block_invoke"
+ "-[IXSAppInstallObserverManager _onQueue_messageXPCListenerEndpoints:forMethod:callMethodOnProxy:exceptEndpoints:]"
+ "-[IXSAppInstallObserverManager _onQueue_messageXPCListenerEndpoints:forMethod:callMethodOnProxy:exceptEndpoints:]_block_invoke"
+ "-[IXSClientConnection _remote_registerContentForOSModuleAtURL:options:completion:]"
+ "-[IXSClientConnection _remote_setKnownOSModuleURLs:options:completion:]"
+ "-[IXSClientConnection _remote_unregisterContentForOSModuleAtURL:options:completion:]"
+ "23:12:56"
+ "Client %@ is missing OS Module operation entitlement."
+ "Client %@ is missing OSModule operation entitlement."
+ "MayUninstallAppWithIdentity"
+ "Sep 16 2025"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_coordinatorQueue"
+ "_client_mayUninstallAppWithIdentity:"
+ "_coordinatorQueue"
+ "_messageInterestedServicesForMethod:callMethodOnProxy:"
+ "_onQueue_messageMachServices:forMethod:callMethodOnProxy:exceptServices:"
+ "_onQueue_messageXPCListenerEndpoints:forMethod:callMethodOnProxy:exceptEndpoints:"
+ "_remote_registerContentForOSModuleAtURL:options:completion:"
+ "_remote_setKnownOSModuleURLs:options:completion:"
+ "_remote_unregisterContentForOSModuleAtURL:options:completion:"
+ "canChangeDefaultAppForCategory:"
+ "com.apple.installcoordination.appUpdateScheduler.coordinator"
+ "com.apple.private.InstallCoordination.OSModuleOperations"
+ "coordinatorQueue"
+ "mayUninstallAppWithIdentity:"
+ "v40@0:8@\"NSSet\"16@24@?<v@?B@\"NSError\">32"
+ "v48@0:8@16Q24@?32@40"
- "%s: Posting IXAppMayUninstallNotificationName for %@"
- "-[IXSAppInstallObserverManager _messageInterestedServicesForClientIDs:forMethod:callMethodOnProxy:]_block_invoke"
- "21:58:41"
- "Aug  2 2025"
- "setValue:forKey:"

```
