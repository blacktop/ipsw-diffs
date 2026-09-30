## ARKitDaemon

> `/System/Library/PrivateFrameworks/ARKitDaemon.framework/ARKitDaemon`

```diff

-631.5.7.0.0
-  __TEXT.__text: 0xdc04
+631.6.0.0.0
+  __TEXT.__text: 0xeb98
   __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_methlist: 0xf24
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0x15c7
+  __TEXT.__oslogstring: 0x1c16
   __TEXT.__cstring: 0x9e2
-  __TEXT.__gcc_except_tab: 0x638
+  __TEXT.__gcc_except_tab: 0x668
   __TEXT.__unwind_info: 0x538
   __TEXT.__objc_classname: 0x462
   __TEXT.__objc_methname: 0x2f1e

   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x3d0
-  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__cfstring: 0x9c0
   __AUTH_CONST.__objc_const: 0x5e98
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x820
   __DATA.__objc_ivar: 0x170
   __DATA.__data: 0x8a0
-  __DATA.__bss: 0x120
+  __DATA.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 372
-  Symbols:   623
-  CStrings:  906
+  Functions: 380
+  Symbols:   631
+  CStrings:  927
 
Symbols:
+ _os_variant_has_internal_content
- _objc_retain_x24
CStrings:
+ "Error: %{public}@ <%p>: %@ does not define a daemon service interface. Implement the 'daemonServiceInterface'"
+ "Error: %{public}@ <%p>: %@ does not define a remote service class. Implement the 'remoteServiceClass' function and point it to its remote"
+ "Error: %{public}@ <%p>: %@ does not define a remote service interface. Implement the 'remoteServiceInterface'"
+ "Error: %{public}@ <%p>: Could not create a process handle for pid %d"
+ "Error: %{public}@ <%p>: Could not create timer"
+ "Error: %{public}@ <%p>: Could not find a process identifier for pid %d"
+ "Error: %{public}@ <%p>: Duplicate service names are not allowed: <%@:%@>"
+ "Error: %{public}@ <%p>: Error removing service %@: %@"
+ "Error: %{public}@ <%p>: Error setting up service: %@"
+ "Error: %{public}@ <%p>: Failed to accept connection for service: %@"
+ "Error: %{public}@ <%p>: Failed to create control."
+ "Error: %{public}@ <%p>: Failed to create service for service name: %@"
+ "Error: %{public}@ <%p>: Failed to create the dispatch source for monitoring memory pressure."
+ "Error: %{public}@ <%p>: Failed to find service class for service name: %@"
+ "Error: %{public}@ <%p>: No batched services available. Skipping algorithm configuration update."
+ "Error: %{public}@ <%p>: No services to be added from %@ to %@"
+ "Error: %{public}@ <%p>: Rejecting service %{public}@ for pid %d, exceeds maximum services of type per client (%ld)"
+ "Error: %{public}@ <%p>: Service '%@' removed for unknown client with ID: %@"
+ "Error: %{public}@ <%p>: Timer already exists."
+ "Error: %{public}@ <%p>: Unable to create the heartbeat timer"
+ "Error: %{public}@: Received an unexpected memory pressure condition value: %lu"

```
