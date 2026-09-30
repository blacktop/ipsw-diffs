## deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

-324.20.1.1.1
-  __TEXT.__text: 0x730a0
-  __TEXT.__auth_stubs: 0x1c90
-  __TEXT.__objc_stubs: 0x6d20
-  __TEXT.__objc_methlist: 0x2380
+324.23.0.0.0
+  __TEXT.__text: 0x73ae4
+  __TEXT.__auth_stubs: 0x1cb0
+  __TEXT.__objc_stubs: 0x6e60
+  __TEXT.__objc_methlist: 0x23b0
   __TEXT.__const: 0x15d2
-  __TEXT.__cstring: 0x11784
+  __TEXT.__cstring: 0x11a84
   __TEXT.__objc_classname: 0x415
-  __TEXT.__gcc_except_tab: 0x32c0
-  __TEXT.__objc_methname: 0x9017
-  __TEXT.__objc_methtype: 0x1a5a
+  __TEXT.__gcc_except_tab: 0x3324
+  __TEXT.__objc_methname: 0x914a
+  __TEXT.__objc_methtype: 0x1a6a
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__swift5_typeref: 0x878
   __TEXT.__swift5_fieldmd: 0x3c8

   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x16a0
+  __TEXT.__unwind_info: 0x1680
   __TEXT.__eh_frame: 0x850
-  __DATA_CONST.__auth_got: 0xe58
-  __DATA_CONST.__got: 0x770
+  __DATA_CONST.__auth_got: 0xe68
+  __DATA_CONST.__got: 0x768
   __DATA_CONST.__auth_ptr: 0x268
-  __DATA_CONST.__const: 0x2040
-  __DATA_CONST.__cfstring: 0x1d00
+  __DATA_CONST.__const: 0x20d8
+  __DATA_CONST.__cfstring: 0x1d60
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA.__objc_const: 0x32c0
-  __DATA.__objc_selrefs: 0x2280
+  __DATA.__objc_selrefs: 0x22e0
   __DATA.__objc_ivar: 0x2b0
   __DATA.__objc_data: 0x870
   __DATA.__data: 0x1230

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CE94C43E-3C27-3F0E-A2EB-D4DCE0AD1B01
-  Functions: 2093
-  Symbols:   774
-  CStrings:  3686
+  UUID: D353CE69-404F-3ABF-9021-2284E9745B12
+  Functions: 2095
+  Symbols:   776
+  CStrings:  3726
 
Symbols:
+ _DADeviceConnectedStatusToString
+ _DAExtensionProcessStateToString
+ __swift_FORCE_LOAD_$_swiftSpatial
- _OBJC_CLASS_$_DAExtensionEvent
CStrings:
+ "    %@: %@"
+ "### HandleEventLifecycle: %@"
+ "%@ (%@)"
+ "%@ <%p>"
+ "-[DADaemonServer startExtensionsIfNeeded:error:]_block_invoke_3"
+ "-[DADaemonServer startExtensionsIfNeeded:error:]_block_invoke_4"
+ "-[DAExtensionCoordinator _handleEvent:]_block_invoke_2"
+ "-[DAExtensionCoordinator _handleEventDataProvider:]_block_invoke"
+ "-[DAExtensionCoordinator _handleEventKeyExchange:]_block_invoke"
+ "-[DAExtensionCoordinator _handleEventLifecycle:]"
+ "-[DAExtensionCoordinator _handleEventLifecycle:]_block_invoke"
+ "-[DAExtensionCoordinator _handleEventTransportLocal:]_block_invoke"
+ "-[DAExtensionCoordinator _reportEventToSession:session:]"
+ "-[DAExtensionCoordinator resumeExtensionWithType:capabilityFlag:]"
+ "-[DAExtensionCoordinator suspendExtensionWithType:capabilityFlag:]"
+ "-[DAExtensionCoordinator updateWithDAEvent:]"
+ "Capability flags changed: %@ -> %@"
+ "Coordinator invalidated, map updated: %@"
+ "CoordinatorMap"
+ "EXCapabilities"
+ "EXExtensionCapabilities"
+ "Extension add reuse: %@"
+ "ExtensionCoordinator event: %@, %@"
+ "Invalidating (%@): %@"
+ "Other capabilities running on extension: %@"
+ "ReportEvent: %@, Session %@"
+ "Resuming %@"
+ "Resuming extension for capability %@: %@"
+ "SessionEnded on %@"
+ "Skip running %@: capability flags %@ do not contain %@"
+ "Suspending extension for capability %@: %@"
+ "Suspending: %@"
+ "TestExtensionBundleID: '%@' -> '%@'"
+ "Updated: %@"
+ "Updating connection status: %@ -> %@"
+ "_handleEventLifecycle:"
+ "_prefTestExtensionBundleID"
+ "_removeExtensionWithType:"
+ "_xpcReportDAExtensionEvent:"
+ "enrolledFlags"
+ "eventFlags"
+ "launch"
+ "launchExtensionWithType:capabilityFlag:"
+ "missing extension with type %@: %@"
+ "processState"
+ "resumeCapabilitiesWithFlags:"
+ "resumeExtensionWithType:capabilityFlag:"
+ "setExtensionCapability:"
+ "suspend"
+ "suspendCapabilitiesWithFlags:"
+ "suspendExtensionWithType:capabilityFlag:"
+ "testExtensionBundle"
+ "updateWithDAEvent:"
+ "v32@0:8q16Q24"
+ "v32@?0@\"NSString\"8@\"DAExtension\"16^B24"
+ "v32@?0@\"NSString\"8@\"DAExtensionCoordinator\"16^B24"
- "### ExtensionActivated: %@"
- "### ExtensionInvalidated: %@"
- "-[DAExtensionCoordinator _handleEvent:]_block_invoke"
- "-[DAExtensionCoordinator _handleEventDataProvider:]_block_invoke_2"
- "-[DAExtensionCoordinator _handleEventExtensionActivated:]_block_invoke_2"
- "-[DAExtensionCoordinator _handleEventExtensionInterrupted:]_block_invoke_2"
- "-[DAExtensionCoordinator _handleEventExtensionInvalidated:]_block_invoke_2"
- "-[DAExtensionCoordinator _handleEventKeyExchange:]_block_invoke_2"
- "-[DAExtensionCoordinator _handleEventTransportLocal:]_block_invoke_2"
- "Extension add reuse: %@, total %d"
- "ExtensionCoordinator event: %@"
- "HandleEventKeyReply: %@"
- "Skip running %@: capability flags do not contain %@"
- "TextExtensions: %s -> %s"
- "_handleEventExtensionActivated:"
- "_handleEventExtensionInterrupted:"
- "_handleEventExtensionInvalidated:"
- "_prefTestExtensions"
- "testExtensions"

```
