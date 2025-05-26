## AppleCVHWA

> `/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA`

```diff

-3.2.8.0.0
-  __TEXT.__text: 0x8c9b0
+3.2.9.0.0
+  __TEXT.__text: 0x8c930
   __TEXT.__auth_stubs: 0xc00
-  __TEXT.__const: 0x2b19
-  __TEXT.__gcc_except_tab: 0x343c
-  __TEXT.__cstring: 0x78a1
-  __TEXT.__oslogstring: 0x13b9
-  __TEXT.__unwind_info: 0x19ec
+  __TEXT.__const: 0x2af9
+  __TEXT.__gcc_except_tab: 0x342c
+  __TEXT.__cstring: 0x79b8
+  __TEXT.__oslogstring: 0x14f8
+  __TEXT.__unwind_info: 0x19f8
   __TEXT.__eh_frame: 0xc4
   __TEXT.__objc_methname: 0x25
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1877
-  Symbols:   412
-  CStrings:  619
+  Functions: 1876
+  Symbols:   419
+  CStrings:  626
 
Symbols:
+ __ZNSt19bad_optional_accessD1Ev
+ __ZTISt19bad_optional_access
+ __ZTVSt19bad_optional_access
+ __xpc_error_connection_interrupted
+ __xpc_error_connection_invalid
+ __xpc_error_termination_imminent
+ __xpc_type_dictionary
CStrings:
+ "(conn_info->conn == nullptr) && \"Cannot create new XPC connection -- old connection is non-NULL\""
+ "(daemon_client_.conn == nullptr && daemon_client_.client_id == 0) && \"Client should not try to reconnect when both connection and client ID \" \"are non-zero\""
+ "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/VisionHWAccelerationServicesUtils/src/VisionHWAServicesXPCUtils.cpp"
+ "Failed to execute symbol lookup on daemon -- daemon may have restarted. Trying to reconnect."
+ "Failed to load program -- Aborting."
+ "Lost connection to daemon"
+ "Offload call failed with transient error -- number of retries left: %d."
+ "ReconnectSession: Failed to create a new XPC connection"
+ "ReconnectSession: Failed to create an ISP session with buffers -- error code %u"
+ "ReplyChecker XPC error: %s"
+ "ReplyChecker error: XPC connection interrupted"
+ "ReplyChecker error: XPC connection invalid"
+ "ReplyChecker error: XPC connection termination imminent"
+ "Symbol lookup on daemon failed repeatedly -- Aborting."
+ "VisionHWAClient error: malformed reply from daemon"
- "Cancelled the existing XPC/Daemon client connection"
- "Expected XPC reply to be a dictionary, but got XPC_TYPE_ERROR"
- "Failed to create a new XPC/Daemon Client connection"
- "Failed to create an ISP session with buffers in XPCServer: error code %u"
- "XPC Connection was reset -- number of retries left: %d."
- "XPC reply error: %{public}s"
- "incomplete offload call -- function symbol not found"
- "incomplete offload call -- return symbol not found"

```
