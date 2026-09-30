## PDSAgent

> `/System/Library/PrivateFrameworks/PDSAgent.framework/Versions/A/PDSAgent`

```diff

-1926.400.131.1.1
-  __TEXT.__text: 0x1d088
+1926.500.181.0.0
+  __TEXT.__text: 0x1dd4c
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x1d74
+  __TEXT.__objc_methlist: 0x23b4
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x1077
   __TEXT.__gcc_except_tab: 0x430
   __TEXT.__oslogstring: 0xcd1
-  __TEXT.__unwind_info: 0x760
+  __TEXT.__unwind_info: 0x780
   __TEXT.__objc_classname: 0x393
   __TEXT.__objc_methname: 0x4631
   __TEXT.__objc_methtype: 0x1010

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12a8
+  __DATA_CONST.__objc_selrefs: 0x1448
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0x6e0
   __AUTH_CONST.__cfstring: 0x14e0
-  __AUTH_CONST.__objc_const: 0x52a0
+  __AUTH_CONST.__objc_const: 0x4708
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x5f0

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 803827E3-A9BC-3E9C-8B04-48BDA4975D90
-  Functions: 714
-  Symbols:   1899
+  UUID: 8E5C5036-77F4-32B3-BFF8-832F1BC8B705
+  Functions: 765
+  Symbols:   1973
   CStrings:  1509
 
Symbols:
+ -[PDSCDCacheContainer _updateAllEntriesWithState:toState:withError:].cold.1
+ -[PDSCDCacheContainer _updateAllEntriesWithState:toState:withError:].cold.2
+ -[PDSCDCacheContainer _updateEntryState:forUser:clientID:withError:].cold.1
+ -[PDSCDCacheContainer initWithContainingPath:].cold.1
+ -[PDSCDCacheContainer initWithContainingPath:].cold.2
+ -[PDSCoordinator initWithQueue:serverBag:requestQueue:kvStoreBlock:entryStoreBlock:pushTokenBlock:systemMonitor:pushHandler:].cold.1
+ -[PDSCoordinator initWithQueue:serverBag:requestQueue:kvStoreBlock:entryStoreBlock:pushTokenBlock:systemMonitor:pushHandler:].cold.2
+ -[PDSCoordinator initWithQueue:serverBag:requestQueue:kvStoreBlock:entryStoreBlock:pushTokenBlock:systemMonitor:pushHandler:].cold.3
+ -[PDSCoordinator initWithQueue:serverBag:requestQueue:kvStoreBlock:entryStoreBlock:pushTokenBlock:systemMonitor:pushHandler:].cold.4
+ -[PDSCoordinator initWithQueue:serverBag:requestQueue:kvStoreBlock:entryStoreBlock:pushTokenBlock:systemMonitor:pushHandler:].cold.5
+ -[PDSCoordinator initWithQueue:serverBag:requestQueue:kvStoreBlock:entryStoreBlock:pushTokenBlock:systemMonitor:pushHandler:].cold.6
+ -[PDSDaemon initWithConfiguration:].cold.1
+ -[PDSDaemon initWithConfiguration:].cold.2
+ -[PDSDaemon initWithConfiguration:].cold.3
+ -[PDSDaemon initWithConfiguration:].cold.4
+ -[PDSDaemon initWithConfiguration:].cold.5
+ -[PDSDaemonListener initWithClientIDs:entryStore:userTracker:].cold.1
+ -[PDSDaemonListener initWithClientIDs:entryStore:userTracker:].cold.2
+ -[PDSDaemonListener initWithClientIDs:entryStore:userTracker:].cold.3
+ -[PDSDaemonListener initWithClientIDs:entryStore:userTracker:].cold.4
+ -[PDSDaemonRemoteVendor initWithQueue:daemonListenerVendor:].cold.1
+ -[PDSDaemonRemoteVendor initWithQueue:daemonListenerVendor:].cold.2
+ -[PDSEntryStore initWithCache:].cold.1
+ -[PDSHeartbeatTracker initWithDelegate:queue:kvStoreBlock:serverBag:].cold.1
+ -[PDSHeartbeatTracker initWithDelegate:queue:kvStoreBlock:serverBag:].cold.2
+ -[PDSHeartbeatTracker initWithDelegate:queue:kvStoreBlock:serverBag:].cold.3
+ -[PDSHeartbeatTracker initWithDelegate:queue:kvStoreBlock:serverBag:].cold.4
+ -[PDSInternalDaemonListener initWithKVStore:].cold.1
+ -[PDSQueueProxy initWithTarget:queue:mode:].cold.1
+ -[PDSQueueProxy initWithTarget:queue:mode:].cold.2
+ -[PDSRequest initWithEntries:requestInfo:].cold.1
+ -[PDSRequest initWithEntries:requestInfo:].cold.2
+ -[PDSRequestQueue _machineID].cold.1
+ -[PDSRequestQueue initWithMessageDelivery:userTracker:queue:pushTokenBlock:entryStoreBlock:].cold.1
+ -[PDSRequestQueue initWithMessageDelivery:userTracker:queue:pushTokenBlock:entryStoreBlock:].cold.2
+ -[PDSRequestQueue initWithMessageDelivery:userTracker:queue:pushTokenBlock:entryStoreBlock:].cold.3
+ -[PDSRequestQueue initWithMessageDelivery:userTracker:queue:pushTokenBlock:entryStoreBlock:].cold.4
+ -[PDSRequestQueue initWithMessageDelivery:userTracker:queue:pushTokenBlock:entryStoreBlock:].cold.5
+ -[PDSResponse initWithStatus:statusByUser:ttl:].cold.1
+ -[PDSUserTracker _accountForUser:withError:].cold.1
+ -[PDSUserTracker initWithAccountStoreBlock:].cold.1
+ -[PDSUserTracker tokenAndIdentifier:forUser:withError:].cold.1
+ -[PDSUserTracker validUser:withError:].cold.1
+ -[PDSXPCClient initWithConnection:interfaceVendor:daemonListenerVendor:queue:].cold.1
+ -[PDSXPCClient initWithConnection:interfaceVendor:daemonListenerVendor:queue:].cold.2
+ -[PDSXPCClient initWithConnection:interfaceVendor:daemonListenerVendor:queue:].cold.3
+ -[PDSXPCClient initWithConnection:interfaceVendor:daemonListenerVendor:queue:].cold.4
+ -[PDSXPCServer initWithServiceName:listenerVendor:interfaceVendor:daemonListenerVendor:queue:workloop:].cold.1
+ -[PDSXPCServer initWithServiceName:listenerVendor:interfaceVendor:daemonListenerVendor:queue:workloop:].cold.2
+ -[PDSXPCServer initWithServiceName:listenerVendor:interfaceVendor:daemonListenerVendor:queue:workloop:].cold.3
+ -[PDSXPCServer initWithServiceName:listenerVendor:interfaceVendor:daemonListenerVendor:queue:workloop:].cold.4
+ -[PDSXPCServer initWithServiceName:listenerVendor:interfaceVendor:daemonListenerVendor:queue:workloop:].cold.5
+ -[PDSXPCServer initWithServiceName:listenerVendor:interfaceVendor:daemonListenerVendor:queue:workloop:].cold.6
+ PDSCurrentServerEnvironment.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1

```
