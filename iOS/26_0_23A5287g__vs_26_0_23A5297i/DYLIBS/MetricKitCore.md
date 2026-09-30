## MetricKitCore

> `/System/Library/PrivateFrameworks/MetricKitCore.framework/MetricKitCore`

```diff

-294.0.0.0.0
-  __TEXT.__text: 0x167c4
+294.0.2.0.0
+  __TEXT.__text: 0x16810
   __TEXT.__auth_stubs: 0x590
   __TEXT.__objc_methlist: 0x19f4
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x7e2
-  __TEXT.__oslogstring: 0x1c8e
+  __TEXT.__cstring: 0x892
+  __TEXT.__oslogstring: 0x1c96
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__unwind_info: 0x510
   __TEXT.__objc_classname: 0x2be
-  __TEXT.__objc_methname: 0x48bc
+  __TEXT.__objc_methname: 0x4920
   __TEXT.__objc_methtype: 0x98d
-  __TEXT.__objc_stubs: 0x3940
-  __DATA_CONST.__got: 0x3a8
+  __TEXT.__objc_stubs: 0x3960
+  __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1050
+  __DATA_CONST.__objc_selrefs: 0x1058
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__objc_arraydata: 0x580
+  __DATA_CONST.__objc_arraydata: 0x598
   __AUTH_CONST.__auth_got: 0x2d8
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0x2c18
-  __AUTH_CONST.__objc_arrayobj: 0x270
+  __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_intobj: 0x78
   __DATA.__objc_ivar: 0x140
   __DATA.__data: 0x660

   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D448DC88-847D-355F-8C34-C7A560AFBEDF
+  UUID: DC100530-A884-3C85-9FD0-A9C58A406706
   Functions: 633
-  Symbols:   2345
-  CStrings:  1078
+  Symbols:   2347
+  CStrings:  1093
 
Symbols:
+ +[MXCorePayloadConstructor buildSampleDiagnosticPayloadForClient:withDateString:]
+ +[MXCorePayloadConstructor buildSamplePayloadForClient:withDateString:]
+ -[MXCore _deliverSamplePayloadForXcodeClient:]
+ -[MXCore _deliverSamplePayloadForXcodeClient:].cold.1
+ -[MXCore _deliverSamplePayloadForXcodeClient:].cold.2
+ -[MXCore _deliverSamplePayloadForXcodeClient:].cold.3
+ -[MXCore _deliverSamplePayloadForXcodeClient:].cold.4
+ -[MXCore _getSampleDiagnosticPayloadForClient:dateString:]
+ -[MXCore _getSamplePayloadForClient:dateString:]
+ -[MXCore deliverSamplePayloadForXcodeClient:]
+ -[MXSource deliverSamplePayloadForClient:]
+ _OBJC_CLASS_$_MXCrashDiagnosticObjectiveCExceptionReason
+ ___42-[MXSource deliverSamplePayloadForClient:]_block_invoke
+ ___42-[MXSource deliverSamplePayloadForClient:]_block_invoke.cold.1
+ ___42-[MXSource deliverSamplePayloadForClient:]_block_invoke.cold.2
+ ___42-[MXSource deliverSamplePayloadForClient:]_block_invoke.cold.3
+ ___46-[MXCore _deliverSamplePayloadForXcodeClient:]_block_invoke
+ _objc_msgSend$_deliverSamplePayloadForXcodeClient:
+ _objc_msgSend$_getSampleDiagnosticPayloadForClient:dateString:
+ _objc_msgSend$_getSamplePayloadForClient:dateString:
+ _objc_msgSend$buildSampleDiagnosticPayloadForClient:withDateString:
+ _objc_msgSend$buildSamplePayloadForClient:withDateString:
+ _objc_msgSend$deliverSamplePayloadForXcodeClient:
+ _objc_msgSend$initWithComposedMessage:formatString:arguments:type:className:exceptionName:
+ _objc_msgSend$initWithMetaData:applicationVersion:signpostData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:exceptionReason:signal:stackTrace:
- +[MXCorePayloadConstructor buildDummyDiagnosticPayloadForClient:withDateString:]
- +[MXCorePayloadConstructor buildDummyPayloadForClient:withDateString:]
- -[MXCore _deliverDummyPayloadForXcodeClient:]
- -[MXCore _deliverDummyPayloadForXcodeClient:].cold.1
- -[MXCore _deliverDummyPayloadForXcodeClient:].cold.2
- -[MXCore _deliverDummyPayloadForXcodeClient:].cold.3
- -[MXCore _deliverDummyPayloadForXcodeClient:].cold.4
- -[MXCore _getDummyDiagnosticPayloadForClient:dateString:]
- -[MXCore _getDummyPayloadForClient:dateString:]
- -[MXCore deliverDummyPayloadForXcodeClient:]
- -[MXSource deliverDummyPayloadForClient:]
- ___41-[MXSource deliverDummyPayloadForClient:]_block_invoke
- ___41-[MXSource deliverDummyPayloadForClient:]_block_invoke.cold.1
- ___41-[MXSource deliverDummyPayloadForClient:]_block_invoke.cold.2
- ___41-[MXSource deliverDummyPayloadForClient:]_block_invoke.cold.3
- ___45-[MXCore _deliverDummyPayloadForXcodeClient:]_block_invoke
- _objc_msgSend$_deliverDummyPayloadForXcodeClient:
- _objc_msgSend$_getDummyDiagnosticPayloadForClient:dateString:
- _objc_msgSend$_getDummyPayloadForClient:dateString:
- _objc_msgSend$buildDummyDiagnosticPayloadForClient:withDateString:
- _objc_msgSend$buildDummyPayloadForClient:withDateString:
- _objc_msgSend$deliverDummyPayloadForXcodeClient:
- _objc_msgSend$initWithMetaData:applicationVersion:signpostData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:signal:stackTrace:
Functions:
~ +[MXCorePayloadConstructor buildDummyDiagnosticPayloadForClient:withDateString:] -> +[MXCorePayloadConstructor buildSampleDiagnosticPayloadForClient:withDateString:] : 2508 -> 2584
CStrings:
+ "*** -[%@ %@]: index %@ beyond bounds for empty array"
+ "*** -[NSArray objectAtIndex:]: index 0 beyond bounds for empty array"
+ "0"
+ "Client %@ not found, ending sample payload delivery"
+ "Commencing sample delivery per request from DTServiceHub for: %@"
+ "NSArray"
+ "NSException"
+ "NSRangeException"
+ "Received sample delivery request from: %@"
+ "Rejecting sample payload delivery request"
+ "Sample diagnostic payload delivery: Failed to write diagnostic report for %@ with error: %@"
+ "Sample metric payload delivery: Failed to write metric report for %@ with error: %@"
+ "Sample payload delivery: Failed to create file directory for %@ with error: %@"
+ "Starting xcode sample payload delivery"
+ "_deliverSamplePayloadForXcodeClient:"
+ "_getSampleDiagnosticPayloadForClient:dateString:"
+ "_getSamplePayloadForClient:dateString:"
+ "buildSampleDiagnosticPayloadForClient:withDateString:"
+ "buildSamplePayloadForClient:withDateString:"
+ "deliverSamplePayloadForClient:"
+ "deliverSamplePayloadForXcodeClient:"
+ "initWithComposedMessage:formatString:arguments:type:className:exceptionName:"
+ "initWithMetaData:applicationVersion:signpostData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:exceptionReason:signal:stackTrace:"
+ "objectAtIndex:"
- "Client %@ not found, ending dummy payload delivery"
- "Commencing dummy delivery per request from DTServiceHub for: %@"
- "Dummy diagnostic payload delivery: Failed to write diagnostic report for %@ with error: %@"
- "Dummy metric payload delivery: Failed to write metric report for %@ with error: %@"
- "Dummy payload delivery: Failed to create file directory for %@ with error: %@"
- "Received dummy delivery request from: %@"
- "Rejecting dummy payload delivery request"
- "Starting xcode dummy payload delivery"
- "_deliverDummyPayloadForXcodeClient:"
- "_getDummyDiagnosticPayloadForClient:dateString:"
- "_getDummyPayloadForClient:dateString:"
- "buildDummyDiagnosticPayloadForClient:withDateString:"
- "buildDummyPayloadForClient:withDateString:"
- "deliverDummyPayloadForClient:"
- "deliverDummyPayloadForXcodeClient:"
- "initWithMetaData:applicationVersion:signpostData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:signal:stackTrace:"

```
