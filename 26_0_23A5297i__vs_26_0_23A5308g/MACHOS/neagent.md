## neagent

> `/usr/libexec/neagent`

```diff

-2191.0.0.0.0
-  __TEXT.__text: 0x13a30
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x19c0
-  __TEXT.__objc_methlist: 0xfa8
+2204.0.0.0.1
+  __TEXT.__text: 0x151f0
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_stubs: 0x1a80
+  __TEXT.__objc_methlist: 0x1008
   __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x290
-  __TEXT.__objc_methname: 0x2381
-  __TEXT.__oslogstring: 0x2c57
-  __TEXT.__cstring: 0xeb7
+  __TEXT.__gcc_except_tab: 0x348
+  __TEXT.__objc_methname: 0x244e
+  __TEXT.__oslogstring: 0x2fdf
+  __TEXT.__cstring: 0x10c4
   __TEXT.__objc_classname: 0x31b
-  __TEXT.__objc_methtype: 0xd47
-  __TEXT.__unwind_info: 0x330
-  __DATA_CONST.__auth_got: 0x3d0
+  __TEXT.__objc_methtype: 0xd9f
+  __TEXT.__unwind_info: 0x370
+  __DATA_CONST.__auth_got: 0x3e8
   __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x4b0
-  __DATA_CONST.__cfstring: 0x440
+  __DATA_CONST.__const: 0x500
+  __DATA_CONST.__cfstring: 0x460
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA.__objc_const: 0x1cb8
-  __DATA.__objc_selrefs: 0xa10
-  __DATA.__objc_ivar: 0x12c
+  __DATA.__objc_const: 0x1d28
+  __DATA.__objc_selrefs: 0xa48
+  __DATA.__objc_ivar: 0x138
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x840
   __DATA.__bss: 0x90

   - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A2D17CB6-59E3-3781-B662-B07FB7C9EFBB
-  Functions: 290
-  Symbols:   174
-  CStrings:  918
+  UUID: 2A484005-B76E-3A7A-AE98-CEFD03BF28F9
+  Functions: 305
+  Symbols:   177
+  CStrings:  954
 
Symbols:
+ _NECopySigningIdentifierForPIDwithAuditToken
+ _xpc_connection_get_audit_token
+ _xpc_connection_get_pid
CStrings:
+ "%@: %s - Connection time out scheduled <interval %d secs> for %@"
+ "%@: %s - Connection timed out <interval %d secs> for %@"
+ "%@: %s - Connection timeout canceled for %@"
+ "%@: %s - Failed to bringup filter before timeout of %d seconds"
+ "%@: %s - Failed to start connection timer"
+ "%@: %s - Failed to startFilter <%@>"
+ "%@: %s - Filter bringup timed out <interval %d secs>"
+ "%@: %s - Filter bringup timeout scheduled <interval %d secs>"
+ "%@: %s - Updating config %@"
+ "%@: %s - update configuration %@"
+ "%@: handleNewRequest - Allow ciphermld requests"
+ "%@: handleNewRequest - FINAL RESULT <failClosed> - filter is not up yet"
+ "%@: handleNewRequest - FINAL RESULT <failClosed> - no prefilter setup yet"
+ "%@: handleNewRequest - FINAL RESULT <failClosed> - request timed out"
+ "%@: handleNewRequest - FINAL RESULT <failOpened> - filter is not up yet"
+ "%@: handleNewRequest - FINAL RESULT <failOpened> - no prefilter setup yet"
+ "%@: handleNewRequest - FINAL RESULT <failOpened> - request timed out"
+ "-[NEAgentURLFilterExtension setFilterBringupTimeout]"
+ "-[NEAgentURLFilterExtension setFilterBringupTimeout]_block_invoke"
+ "-[NEAgentURLFilterExtension updateConfiguration:]_block_invoke"
+ "-[NEPIRChecker start:responseQueue:completionHandler:]"
+ "-[NEPIRChecker start:responseQueue:completionHandler:]_block_invoke"
+ "-[NEURLFilterEngine cancelConnectionTimer:]"
+ "-[NEURLFilterEngine handleNewRequest:connection:filloutReply:completionHandler:]"
+ "-[NEURLFilterEngine handleNewRequest:connection:filloutReply:completionHandler:]_block_invoke"
+ "-[NEURLFilterEngine setConfiguration:completionHandler:]_block_invoke"
+ "-[NEURLFilterEngine setupConnectionTimer:timeoutHandler:]"
+ "-[NEURLFilterEngine setupConnectionTimer:timeoutHandler:]_block_invoke"
+ "-[NEURLFilterEngine startFilterWithCompletionHandler:]_block_invoke"
+ "_active"
+ "_filterBringupTimer"
+ "_pendingConnectionTimers"
+ "allValues"
+ "code"
+ "com.apple.ciphermld"
+ "domain"
+ "isActive"
+ "numberWithUnsignedLong:"
+ "setConfiguration:completionHandler:"
+ "start:responseQueue:completionHandler:"
+ "startFilterWithCompletionHandler:"
+ "v40@0:8@\"NEURLFilterConfiguration\"16@\"NSObject<OS_dispatch_queue>\"24@?<v@?@\"NSError\">32"
- "%@: handleNewRequest - no prefilter / filter setup yet"
- "-"
- "-[NEPIRChecker start:responseQueue:]"
- "-[NEPIRChecker start:responseQueue:]_block_invoke"
- "-[NEURLFilterEngine handleNewRequest:filloutReply:completionHandler:]"
- "-[NEURLFilterEngine handleNewRequest:filloutReply:completionHandler:]_block_invoke"
- "-[NEURLFilterEngine startFilter]_block_invoke"
- "startFilter"

```
