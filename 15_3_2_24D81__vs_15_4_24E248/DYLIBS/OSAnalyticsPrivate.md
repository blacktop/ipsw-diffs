## OSAnalyticsPrivate

> `/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/Versions/A/OSAnalyticsPrivate`

```diff

-727.80.2.0.0
-  __TEXT.__text: 0x15b0c
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x8bc
+758.100.43.0.0
+  __TEXT.__text: 0x15ecc
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_methlist: 0xa9c
   __TEXT.__const: 0x108
   __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__cstring: 0x1180
-  __TEXT.__oslogstring: 0x1f49
-  __TEXT.__unwind_info: 0x338
+  __TEXT.__cstring: 0x1195
+  __TEXT.__oslogstring: 0x1fa2
+  __TEXT.__unwind_info: 0x340
   __TEXT.__objc_classname: 0x135
-  __TEXT.__objc_methname: 0x20f1
-  __TEXT.__objc_methtype: 0x7b5
-  __TEXT.__objc_stubs: 0x2080
-  __DATA_CONST.__got: 0x288
+  __TEXT.__objc_methname: 0x2115
+  __TEXT.__objc_methtype: 0x7c3
+  __TEXT.__objc_stubs: 0x20a0
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x950
+  __DATA_CONST.__objc_selrefs: 0x9e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_arraydata: 0x138
-  __AUTH_CONST.__auth_got: 0x3f0
+  __DATA_CONST.__objc_arraydata: 0xf8
+  __AUTH_CONST.__auth_got: 0x3f8
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x20e0
-  __AUTH_CONST.__objc_const: 0x1eb0
+  __AUTH_CONST.__cfstring: 0x2100
+  __AUTH_CONST.__objc_const: 0x1b50
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1781C0CB-4B89-3FCE-8DD5-7C4F4A8271BF
-  Functions: 287
-  Symbols:   990
-  CStrings:  1297
+  UUID: 615581A6-2EF4-39D0-B8C5-F0A96EEB059C
+  Functions: 289
+  Symbols:   992
+  CStrings:  1302
 
Symbols:
+ +[OSASubmitter submissionPathsWithHomeDirectory:withProxies:]
+ +[OSASubmitter submissionPathsWithHomeDirectory:withProxies:].cold.1
+ +[OSASubmitter submissionPathsWithHomeDirectory:withProxies:].cold.2
+ +[OSASubmitter submissionPathsWithHomeDirectory:withProxies:].cold.3
+ +[OSASubmitter submissionPathsWithHomeDirectory:withProxies:].cold.4
+ -[OSASubmitter submitLogsUsingPolicy:resultsCallback:].cold.2
+ OSAStabilityMonitorLogDomain.cold.1
+ _OSAIsConfiguredRSDDevice
+ _OSAIsConfiguredRSDHost
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$submissionPathsWithHomeDirectory:withProxies:
+ _objc_msgSend$submissionsDisabled
- +[OSASubmitter submissionPathsWithHomeDirectory:]
- +[OSASubmitter submissionPathsWithHomeDirectory:].cold.1
- +[OSASubmitter submissionPathsWithHomeDirectory:].cold.2
- +[OSASubmitter submissionPathsWithHomeDirectory:].cold.3
- +[OSASubmitter submissionPathsWithHomeDirectory:].cold.4
- _OSAIsDebugEnabledForRSD
- _OUTLINED_FUNCTION_3
- _objc_msgSend$initWithObjects:
- _objc_msgSend$submissionPathsWithHomeDirectory:
CStrings:
+ "@28@0:8@16B24"
+ "Submissions have been disabled. To enable submissions, run osatool re-enable-submissions"
+ "addObjectsFromArray:"
+ "submissionPathsWithHomeDirectory:withProxies:"
+ "submissions disabled"
+ "submissionsDisabled"
- "initWithObjects:"
- "submissionPathsWithHomeDirectory:"

```
