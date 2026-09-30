## com.apple.accessoryd.matching

> `/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching`

```diff

-1119.0.0.502.1
-  __TEXT.__text: 0x3861c
-  __TEXT.__auth_stubs: 0xfd0
+1123.0.0.0.0
+  __TEXT.__text: 0x38750
+  __TEXT.__auth_stubs: 0xfe0
   __TEXT.__objc_stubs: 0x47c0
   __TEXT.__objc_methlist: 0x1e84
   __TEXT.__cstring: 0x4852
-  __TEXT.__objc_methname: 0x61df
+  __TEXT.__objc_methname: 0x620c
   __TEXT.__objc_classname: 0x26c
   __TEXT.__objc_methtype: 0xaaa
   __TEXT.__const: 0x200
   __TEXT.__oslogstring: 0x3b88
-  __TEXT.__gcc_except_tab: 0x334
+  __TEXT.__gcc_except_tab: 0x4a4
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x910
-  __DATA.__auth_got: 0x7f8
+  __TEXT.__unwind_info: 0x918
+  __DATA.__auth_got: 0x800
   __DATA.__got: 0x2f0
   __DATA.__auth_ptr: 0x18
   __DATA.__const: 0xed0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: ED8AE600-B06C-3F3D-88CD-D16D0396BA4F
-  Functions: 1287
-  Symbols:   7292
-  CStrings:  2745
+  UUID: 3A6E5CDE-0B01-38B3-A77D-B3F4534BABA2
+  Functions: 1286
+  Symbols:   7291
+  CStrings:  2747
 
Symbols:
+ -[TRMPort _updatePropertiesFromService].cold.1
+ -[TRMPort _updatePropertiesFromService].cold.2
+ GCC_except_table7
+ _objc_setProperty_atomic
+ _updatePropertiesFromService.onceToken
+ _updatePropertiesFromService.propertyFilter
CStrings:
+ "T@\"<TRMPortDelegate>\",R,W,V_delegate"
+ "T@\"NSArray\",&,V_transportsUnauthorized"
+ "T@\"NSDictionary\",&,V_servicePropertiesFiltered"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
+ "T@\"NSString\",&,V_connectionUUID"
+ "T@\"NSString\",&,V_deviceDescription"
+ "T@\"NSString\",&,V_portDescription"
+ "T@\"NSString\",&,V_portTypeDescription"
+ "T@\"NSString\",&,V_userAuthorizationStatusDescription"
+ "TB,V_authorizationPending"
+ "TB,V_authorizationRequired"
+ "TB,V_builtIn"
+ "TB,V_connectionActive"
+ "TB,V_interestNotificationsStarted"
+ "TB,V_isInactive"
+ "TB,V_userAuthorizationPending"
+ "TI,V_ioNotification"
+ "TI,V_service"
+ "TQ,V_registryEntryID"
+ "T^{IONotificationPort=},V_ioNotificationPort"
+ "Ti,V_portNumber"
+ "Ti,V_portType"
+ "Ti,V_userAuthorizationStatus"
- "T@\"<TRMPortDelegate>\",R,W,N,V_delegate"
- "T@\"NSArray\",&,N,V_transportsUnauthorized"
- "T@\"NSDictionary\",&,N,V_servicePropertiesFiltered"
- "T@\"NSString\",&,N,V_connectionUUID"
- "T@\"NSString\",&,N,V_deviceDescription"
- "T@\"NSString\",&,N,V_portDescription"
- "T@\"NSString\",&,N,V_portTypeDescription"
- "T@\"NSString\",&,N,V_userAuthorizationStatusDescription"
- "TB,N,V_authorizationPending"
- "TB,N,V_authorizationRequired"
- "TB,N,V_builtIn"
- "TB,N,V_connectionActive"
- "TB,N,V_interestNotificationsStarted"
- "TB,N,V_isInactive"
- "TB,N,V_userAuthorizationPending"
- "TI,N,V_ioNotification"
- "TI,N,V_service"
- "TQ,N,V_registryEntryID"
- "Ti,N,V_portNumber"
- "Ti,N,V_portType"
- "Ti,N,V_userAuthorizationStatus"

```
