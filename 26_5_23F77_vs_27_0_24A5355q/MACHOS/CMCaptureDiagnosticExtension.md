## CMCaptureDiagnosticExtension

> `/System/Library/PrivateFrameworks/CMCapture.framework/PlugIns/CMCaptureDiagnosticExtension.appex/CMCaptureDiagnosticExtension`

```diff

-665.120.8.0.0
-  __TEXT.__text: 0x25c
-  __TEXT.__auth_stubs: 0x30
-  __TEXT.__objc_stubs: 0x140
+748.0.0.122.2
+  __TEXT.__text: 0x648
+  __TEXT.__auth_stubs: 0x60
+  __TEXT.__objc_stubs: 0x260
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__cstring: 0xdf
+  __TEXT.__const: 0x18
   __TEXT.__objc_classname: 0x1d
-  __TEXT.__objc_methname: 0xf8
+  __TEXT.__objc_methname: 0x17d
   __TEXT.__objc_methtype: 0x13
+  __TEXT.__cstring: 0xe3
+  __TEXT.__oslogstring: 0xb1
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x20
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__cfstring: 0xa0
+  __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x38
+  __DATA_CONST.__got: 0x40
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x60
+  __DATA.__objc_selrefs: 0xa8
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 668A97D4-F752-335A-8027-3E047080895B
+  UUID: 17C00D30-2151-3BEB-B0A5-F75D06E704D3
   Functions: 2
-  Symbols:   18
-  CStrings:  27
+  Symbols:   24
+  CStrings:  44
 
Symbols:
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ __os_log_default
+ __os_log_impl
+ _objc_alloc_init
+ _objc_autorelease
+ _os_log_type_enabled
- __os_feature_enabled_impl
Functions:
~ sub_100000a7c -> sub_100000b1c : 592 -> 1596
CStrings:
+ "   found item: %{public}@"
+ "/private/var/mobile/Library/Logs/CrashReporter"
+ "attachStackshots: checking path %{public}@"
+ "attachTailspins: checking path %{public}@"
+ "count"
+ "date"
+ "dateFromString:"
+ "hasPrefix:"
+ "ips"
+ "length"
+ "searching path: %{public}@, contents.size = %lu, error=%{public}@"
+ "setDateFormat:"
+ "stacks"
+ "stringByDeletingPathExtension"
+ "substringFromIndex:"
+ "timeIntervalSinceDate:"
+ "yyyy-MM-dd-HHmmss"
- "/private/var/mobile/tmp/CMCaptureTailspins"
- "CameraCapture"
- "cameracaptured"

```
