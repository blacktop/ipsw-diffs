## OSAnalyticsPrivate

> `/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/Versions/A/OSAnalyticsPrivate`

```diff

-1056.0.22.0.0
-  __TEXT.__text: 0x1a708
-  __TEXT.__objc_methlist: 0xde0
+1056.40.8.0.0
+  __TEXT.__text: 0x1a8e4
+  __TEXT.__objc_methlist: 0xe38
   __TEXT.__const: 0x12a
   __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__cstring: 0x153e
-  __TEXT.__oslogstring: 0x26cc
+  __TEXT.__cstring: 0x15ce
+  __TEXT.__oslogstring: 0x271c
   __TEXT.__swift5_typeref: 0x41
   __TEXT.__swift5_capture: 0x10
   __TEXT.__unwind_info: 0x428

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb8
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc48
+  __DATA_CONST.__objc_selrefs: 0xc78
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x118
   __DATA_CONST.__got: 0x298
-  __AUTH_CONST.__const: 0x570
-  __AUTH_CONST.__cfstring: 0x2400
-  __AUTH_CONST.__objc_const: 0x2390
+  __AUTH_CONST.__const: 0x540
+  __AUTH_CONST.__cfstring: 0x24c0
+  __AUTH_CONST.__objc_const: 0x2420
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH_CONST.__objc_dictobj: 0x168
+  __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x648
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x48
+  __AUTH.__objc_data: 0x98
   __DATA.__objc_ivar: 0x18c
   __DATA.__data: 0x418
   __DATA.__bss: 0x28

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 386
-  Symbols:   1164
-  CStrings:  563
+  Functions: 391
+  Symbols:   1176
+  CStrings:  573
 
Symbols:
+ +[PCCUtilities diagnosticPipelineLogs]
+ +[PCCUtilities diagnosticPipelineRoot]
+ +[PCCUtilities isDiagnosticPipelineLog:]
+ +[PCCUtilities isSysdiagnose:]
+ +[PCCUtilities sysdiagnoseRoot]
+ -[PCCEndpoint modelIdentifierForDevice:]
+ -[PCCEndpoint productVersionForDevice:]
+ _OBJC_CLASS_$_PCCUtilities
+ _OBJC_METACLASS_$_PCCUtilities
+ __OBJC_$_CLASS_METHODS_PCCUtilities
+ __OBJC_CLASS_RO_$_PCCUtilities
+ __OBJC_METACLASS_RO_$_PCCUtilities
+ _objc_msgSend$diagnosticPipelineRoot
+ _objc_msgSend$floatValue
+ _objc_msgSend$modelIdentifierForDevice:
+ _objc_msgSend$productVersionForDevice:
+ _objc_msgSend$sysdiagnoseRoot
- -[PCCProxiedDevice isOnDeviceLog:]
- __36-[PCCProxiedDevice generateLogList:]_block_invoke
- ___block_descriptor_49_e8_32s40s_e15_v16?0"NSURL"8l
- _objc_msgSend$isOnDeviceLog:
- _objc_msgSend$rename:
CStrings:
+ "%@ for device %@: model=%{public}@ productVersion=%{public}@ -> %{public}s"
+ "%@ for device %@: productVersion=%{public}@ -> %{public}s"
+ "/private/var/mobile/Library/Logs/DiagnosticPipeline"
+ "<nil>"
+ "Adding xattr to incoming file %@: %@"
+ "AppleTV"
+ "Proxy syncing diagnostic pipeline logs is not supported on macOS"
+ "Proxy syncing sysdiagnoses is not supported on macOS"
+ "SKIPPING (pre-Rizz Apple TV)"
+ "SKIPPING (pre-Rizz)"
+ "gz"
+ "memgraph"
+ "reportType"
+ "supported"
- "Adding xattr %@: %@"
- "Including diagnostic pipeline logs in log list"
- "Including sysdiagnoses in log list"
- "Not including diagnostic pipeline logs in log list: DRGetAllLogFileURLs unavailable on current platform"
```
