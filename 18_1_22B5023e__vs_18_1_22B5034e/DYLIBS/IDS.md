## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-1857.100.1.0.0
-  __TEXT.__text: 0x132bb8
-  __TEXT.__auth_stubs: 0x1b50
-  __TEXT.__objc_methlist: 0xa2d4
+1925.200.32.2.3
+  __TEXT.__text: 0x13444c
+  __TEXT.__auth_stubs: 0x1b70
+  __TEXT.__objc_methlist: 0xa42c
   __TEXT.__const: 0x428
-  __TEXT.__gcc_except_tab: 0x44d8
-  __TEXT.__oslogstring: 0x1823d
-  __TEXT.__cstring: 0xfd8f
+  __TEXT.__gcc_except_tab: 0x452c
+  __TEXT.__oslogstring: 0x18324
+  __TEXT.__cstring: 0xfee2
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
-  __TEXT.__unwind_info: 0x4998
-  __TEXT.__objc_classname: 0x17c2
-  __TEXT.__objc_methname: 0x1de48
-  __TEXT.__objc_methtype: 0x6fd5
-  __TEXT.__objc_stubs: 0x13000
+  __TEXT.__unwind_info: 0x4a00
+  __TEXT.__objc_classname: 0x17fe
+  __TEXT.__objc_methname: 0x1e183
+  __TEXT.__objc_methtype: 0x7019
+  __TEXT.__objc_stubs: 0x131c0
   __DATA_CONST.__got: 0x1108
-  __DATA_CONST.__const: 0x4d98
-  __DATA_CONST.__objc_classlist: 0x538
+  __DATA_CONST.__const: 0x4e10
+  __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1d8
+  __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6000
+  __DATA_CONST.__objc_selrefs: 0x60a0
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x430
-  __AUTH_CONST.__auth_got: 0xdb8
+  __DATA_CONST.__objc_superrefs: 0x438
+  __AUTH_CONST.__auth_got: 0xdc8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1720
-  __AUTH_CONST.__cfstring: 0x6ea0
-  __AUTH_CONST.__objc_const: 0x3b138
+  __AUTH_CONST.__cfstring: 0x6ec0
+  __AUTH_CONST.__objc_const: 0x3b970
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x1950
-  __DATA.__objc_ivar: 0xc64
-  __DATA.__data: 0x1650
-  __DATA.__bss: 0x1b04
+  __AUTH.__objc_data: 0x19a0
+  __DATA.__objc_ivar: 0xc80
+  __DATA.__data: 0x16b0
+  __DATA.__bss: 0x1b1c
   __DATA_DIRTY.__objc_data: 0x1ae0
-  __DATA_DIRTY.__bss: 0x340
+  __DATA_DIRTY.__bss: 0x330
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 6050
-  Symbols:   1479
-  CStrings:  8668
+  Functions: 6089
+  Symbols:   1481
+  CStrings:  8715
 
Symbols:
+ _notify_register_dispatch
+ _objc_release_x2
CStrings:
+ "setLock:"
+ "_name"
+ "@\"IDSDeviceStateMonitoring\""
+ "TQ,R,N,V_currentState"
+ "_setupSession:destinations:options:delegateContext:"
+ "T@\"NSString\",R,N,V_name"
+ "unRegisterForStateUpdates:"
+ "@64@0:8@16@24@32@40@48@56"
+ "-[_IDSDevice stateDidChange:]"
+ "delegateArray"
+ "-[_IDSGroupSession groupSessionDidInitialize:error:]"
+ "_delegateArray"
+ "NULL keyValueDelivery"
+ "com.apple.IDS.IDSDeviceStateMonitoring"
+ "groupSessionDidInitialize:error:"
+ "T{os_unfair_lock_s=I},N,V_lock"
+ "initWithAccount:destinations:options:delegate:queue:"
+ "-[IDSGroupSession initWithAccount:destinations:options:delegate:queue:]"
+ "for session %!@(MISSING), keyValueDelivery: %!@(MISSING)"
+ "_initWithSessionID:"
+ "initWithAccount:options:delegate:queue:"
+ "_outToken"
+ "initWithName:queue:"
+ "Initializing setting up session delegate %!p(MISSING)"
+ "_currentState"
+ "TB,R,N,V_isMonitoring"
+ "currentState"
+ "IDSGroupSessionKeyValueDelivery init: %!@(MISSING) with completionHandler: %!@(MISSING)"
+ "_isMonitoring"
+ "IDSDeviceStateMonitoring"
+ "v12@?0i8"
+ "T@\"NSMutableArray\",R,N,V_delegateArray"
+ "stateDidChange:"
+ "-[IDSGroupSession initWithAccount:options:delegate:queue:]"
+ "_setUpXPCWithCompletionHandler:"
+ "Ti,R,N,V_outToken"
+ "initWithSessionID:completionHandler:"
+ "Dispatch registration invoked - fetched state {name: %!@(MISSING), state: %!l(MISSING)u, token:%!d(MISSING), delegate count:%!l(MISSING)u}"
+ "initWithAccount:destinations:options:delegateContext:delegate:queue:"
+ "monitors"
+ "\x04\x11"
+ "IDSDeviceStateMonitoringDelegate"
+ "outToken"
+ "T@\"NSMutableDictionary\",R,N"
+ "got null keyValueDelivery for session %!@(MISSING), keyValueDelivery: %!@(MISSING)"
+ "-[_IDSGroupSession initWithAccount:destinations:options:delegateContext:delegate:queue:]"
+ "notifyDelegatesAboutNewState:token:"
+ "sharedInstanceForNotificationName:"
+ "createWithSessionID:completionHandler:"
+ "registerForStateUpdates:queue:"
+ "Dispatch registration failed {name: %!@(MISSING), status: %!u(MISSING)}"
+ "isMonitoring"
+ "v28@0:8Q16i24"
- "keyValueDelivery: %!@(MISSING)"
- "_setUpXPC"
- "Received device state note {uniqueID: %!@(MISSING), weakSelf: %!p(MISSING), nearbyID: %!@(MISSING)}"
- "_nearbyToken"
- "com.apple._IDSDevice.notification"
- "IDSGroupSessionKeyValueDelivery init: %!@(MISSING)"
- "\x03\x11"

```
