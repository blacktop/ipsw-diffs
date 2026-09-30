## DiagnosticsSessionAvailabilityService

> `/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/XPCServices/DiagnosticsSessionAvailabilityService.xpc/DiagnosticsSessionAvailabilityService`

```diff

-795.0.0.0.0
-  __TEXT.__text: 0xa128
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x1d60
+818.0.0.0.0
+  __TEXT.__text: 0xa10c
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_stubs: 0x1d40
   __TEXT.__objc_methlist: 0xc10
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x8e6
+  __TEXT.__cstring: 0x8f9
   __TEXT.__objc_classname: 0x21e
-  __TEXT.__objc_methname: 0x2249
+  __TEXT.__objc_methname: 0x2225
   __TEXT.__objc_methtype: 0x580
-  __TEXT.__oslogstring: 0x6b2
+  __TEXT.__oslogstring: 0x6bc
   __TEXT.__gcc_except_tab: 0x41c
-  __TEXT.__unwind_info: 0x3c0
-  __DATA_CONST.__auth_got: 0x2a0
+  __TEXT.__unwind_info: 0x3b8
+  __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__const: 0x420
   __DATA_CONST.__cfstring: 0x900

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x31a0
-  __DATA.__objc_selrefs: 0x900
+  __DATA.__objc_selrefs: 0x8f8
   __DATA.__objc_ivar: 0xf8
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x360

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 285
-  Symbols:   199
-  CStrings:  657
+  Functions: 284
+  Symbols:   200
+  CStrings:  656
 
Symbols:
+ _objc_retain_x9
CStrings:
+ "-[DSDiagnosticsSessionAvailabilityService _getASTSessionStatusForTicketNumber:timeout:completion:]"
+ "AST sessionExists: %!d(MISSING), info: %!@(MISSING), error: %!@(MISSING)"
+ "_getASTSessionStatusForTicketNumber:timeout:completion:"
+ "sessionStatusForIdentities:ticketNumber:timeout:requestQueuedSuiteInfo:completionHandler:"
+ "v28@?0B8@\"ASTSessionInfo\"12@\"NSError\"20"
- "-[DSDiagnosticsSessionAvailabilityService _getASTSessionExistsForTicketNumber:timeout:completion:]"
- "AST sessionExists: %!d(MISSING), error: %!@(MISSING)"
- "_getASTSessionExistsForTicketNumber:timeout:completion:"
- "sessionExistsForIdentities:ticketNumber:completionHandler:"
- "sessionExistsForIdentities:ticketNumber:timeout:completionHandler:"
- "v20@?0B8@\"NSError\"12"

```
