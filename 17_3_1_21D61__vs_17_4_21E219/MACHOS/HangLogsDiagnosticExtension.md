## HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

```diff

-281.2.0.0.0
-  __TEXT.__text: 0x9484
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_stubs: 0xc80
+288.0.0.0.0
+  __TEXT.__text: 0x971c
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_stubs: 0xcc0
   __TEXT.__objc_methlist: 0x7a4
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x13c4
-  __TEXT.__oslogstring: 0xed7
-  __TEXT.__objc_methname: 0x300d
+  __TEXT.__cstring: 0x1413
+  __TEXT.__oslogstring: 0xf12
+  __TEXT.__objc_methname: 0x3045
   __TEXT.__objc_classname: 0x5c
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__objc_methtype: 0x674
-  __TEXT.__unwind_info: 0x198
-  __DATA_CONST.__auth_got: 0x340
+  __TEXT.__unwind_info: 0x1a8
+  __DATA_CONST.__auth_got: 0x360
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x7a8
-  __DATA_CONST.__cfstring: 0x1640
+  __DATA_CONST.__const: 0x810
+  __DATA_CONST.__cfstring: 0x1680
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x1598
-  __DATA.__objc_selrefs: 0x760
-  __DATA.__objc_classrefs: 0xe0
-  __DATA.__objc_superrefs: 0x18
+  __DATA.__objc_selrefs: 0x770
   __DATA.__objc_ivar: 0x198
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x58
-  __DATA.__bss: 0x70
+  __DATA.__data: 0x68
+  __DATA.__bss: 0x90
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 221
-  Symbols:   298
-  CStrings:  761
+  Functions: 225
+  Symbols:   306
+  CStrings:  768
 
Symbols:
+ _HTCAQueue
+ _HTGetHomeDirectoryURL
+ _NSHomeDirectoryForUser
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _kHTCoreAnalyticsDiskAvailableBytes
+ _kHTCoreAnalyticsDiskAvailablePercent
+ _objc_retain_x9
+ _statfs
CStrings:
+ "Logging always-on telemetry: %@"
+ "Unable to get home dir URL"
+ "com.apple.hangtracer.coreanalytics"
+ "disk_available_bytes"
+ "disk_available_percent"
+ "fileSystemRepresentation"
+ "fileURLWithPath:isDirectory:"

```
