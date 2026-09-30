## com.apple.PerformanceTrace.PerformanceTraceService

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/Versions/A/XPCServices/com.apple.PerformanceTrace.PerformanceTraceService.xpc/Contents/MacOS/com.apple.PerformanceTrace.PerformanceTraceService`

```diff

-200.2.0.0.0
-  __TEXT.__text: 0xcf28
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x16c0
-  __TEXT.__objc_methlist: 0x564
+218.2.0.0.0
+  __TEXT.__text: 0xd79c
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_stubs: 0x1740
+  __TEXT.__objc_methlist: 0x7a0
   __TEXT.__const: 0x11c
-  __TEXT.__gcc_except_tab: 0x33c
-  __TEXT.__objc_methname: 0x17d7
-  __TEXT.__oslogstring: 0xbd0
-  __TEXT.__cstring: 0x1666
+  __TEXT.__gcc_except_tab: 0x34c
+  __TEXT.__objc_methname: 0x18c2
+  __TEXT.__oslogstring: 0xc5f
+  __TEXT.__cstring: 0x16de
   __TEXT.__objc_classname: 0xb9
-  __TEXT.__objc_methtype: 0x43d
+  __TEXT.__objc_methtype: 0x448
   __TEXT.__unwind_info: 0x220
-  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x718
-  __DATA_CONST.__cfstring: 0x12e0
+  __DATA_CONST.__const: 0x738
+  __DATA_CONST.__cfstring: 0x1360
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x150
-  __DATA_CONST.__objc_arraydata: 0xf0
-  __DATA_CONST.__objc_arrayobj: 0x138
-  __DATA.__objc_const: 0xe78
-  __DATA.__objc_selrefs: 0x638
-  __DATA.__objc_ivar: 0x84
+  __DATA_CONST.__objc_arraydata: 0xb0
+  __DATA_CONST.__objc_arrayobj: 0xf0
+  __DATA.__objc_const: 0xb48
+  __DATA.__objc_selrefs: 0x6f0
+  __DATA.__objc_ivar: 0x8c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x300
+  __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 20C9A1B3-F587-36B5-A354-C165391D7761
-  Functions: 240
-  Symbols:   181
-  CStrings:  754
+  UUID: B56498E1-FD2F-3239-A243-5AD7519686AC
+  Functions: 243
+  Symbols:   183
+  CStrings:  773
 
Symbols:
+ _NSLog
+ _os_variant_has_internal_content
CStrings:
+ "%@ is not an array of strings."
+ "%@ is not an array type."
+ "%s.%llu"
+ "--plan"
+ "@\"NSArray\""
+ "A#E"
+ "Failed to extract valid notification name for trace record run"
+ "Starting PerformanceTrace (legacy) for %{public}@ [%d]"
+ "Starting PerformanceTrace for %{public}@ [%d]"
+ "Stopping Performance Trace for %{public}@ [%d]"
+ "Stopping PerformanceTrace (legacy) for %{public}@ [%d]"
+ "T@\"NSArray\",&,N,V_traceRecordArgs"
+ "T@\"NSString\",&,N,V_traceRecordEndNotificationName"
+ "_traceRecordArgs"
+ "_traceRecordEndNotificationName"
+ "setTraceRecordArgs:"
+ "setTraceRecordEndNotificationName:"
+ "traceRecordArgs"
+ "traceRecordArgs: %@"
+ "traceRecordEndNotificationName"
- "--Logging:disable-logs"
- "--Logging:enable-signposts"
- "A#C"
- "Starting PerformanceTrace"
- "Starting PerformanceTrace (legacy)"
- "Stopping Performance Trace"
- "Stopping PerformanceTrace (legacy)"

```
