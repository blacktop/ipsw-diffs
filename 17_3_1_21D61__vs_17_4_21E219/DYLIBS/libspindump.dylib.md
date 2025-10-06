## libspindump.dylib

> `/usr/lib/libspindump.dylib`

```diff

-341.1.0.0.0
-  __TEXT.__text: 0x37c4
-  __TEXT.__auth_stubs: 0x350
+357.0.0.0.0
+  __TEXT.__text: 0x37d8
+  __TEXT.__auth_stubs: 0x3d0
   __TEXT.__const: 0x58
-  __TEXT.__oslogstring: 0xabf
-  __TEXT.__cstring: 0x341
-  __TEXT.__unwind_info: 0xe4
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x110
-  __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__auth_got: 0x1a8
+  __TEXT.__oslogstring: 0xa7b
+  __TEXT.__cstring: 0x3c4
+  __TEXT.__unwind_info: 0xf8
+  __TEXT.__objc_classname: 0x1
+  __TEXT.__objc_methname: 0x6b
+  __TEXT.__objc_stubs: 0xe0
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__const: 0xb0
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0x38
+  __DATA_CONST.__objc_classrefs: 0x10
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x40
+  __AUTH_CONST.__auth_got: 0x1f0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x50
-  __DATA_DIRTY.__const: 0xc0
+  __DATA.__bss: 0x68
+  __DATA_DIRTY.__const: 0x20
   __DATA_DIRTY.__bss: 0x238
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
-  UUID: 1BFDC2B1-FC20-3A7C-A75F-B7F2C4B3D7A6
-  Functions: 75
-  Symbols:   233
-  CStrings:  87
+  - /usr/lib/libobjc.A.dylib
+  UUID: C0660672-A065-3BBF-A85D-F80443DF26A1
+  Functions: 76
+  Symbols:   257
+  CStrings:  99
 
Symbols:
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSString
+ _SPCheckHIDResponseTime.lastTelemetryHIDEventEndTimestamp_MachAbs
+ ___SPCheckHIDResponseTime_block_invoke
+ ___SPCheckHIDResponseTime_block_invoke.cold.1
+ ___SPSubmitHIDTelemetry_block_invoke
+ ___block_descriptor_32_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32b_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_descriptor_44_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_48_e30_"NSObject<OS_xpc_object>"8?0l
+ ___block_literal_global.34
+ ___block_literal_global.37
+ ___block_literal_global.39
+ ___block_literal_global.53
+ ___block_literal_global.56
+ ___block_literal_global.58
+ ___udivti3
+ __kCFBundleShortVersionStringKey
+ _analytics_is_event_used
+ _analytics_send_event_lazy
+ _dispatch_after
+ _dispatch_time
+ _gDurationHandlingHIDEvents_MachAbs
+ _gNumHIDEvents
+ _kCFBundleVersionKey
+ _objc_alloc
+ _objc_msgSend
+ _objc_msgSend$UTF8String
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$length
+ _objc_msgSend$mainBundle
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_release_x21
+ _objc_retain_x21
+ _objc_retain_x22
- _SPReportCPUWakeupsResource.cold.1
- _SPReportCPUWakeupsResource.cold.2
- ___block_descriptor_tmp
- ___block_descriptor_tmp.24
- ___block_descriptor_tmp.36
- ___block_descriptor_tmp.38
- ___block_descriptor_tmp.41
- ___block_descriptor_tmp.46
- ___block_descriptor_tmp.50
- ___block_descriptor_tmp.53
- ___block_literal_global.40
- ___block_literal_global.43
- ___block_literal_global.48
- ___block_literal_global.52
- ___block_literal_global.55
CStrings:
+ "%@ (%@)"
+ "@\"NSObject<OS_xpc_object>\"8@?0"
+ "HID statistics: %llums to handle %llu events (%llums/event)"
+ "UTF8String"
+ "bundleIdentifier"
+ "bundle_id"
+ "bundle_version"
+ "com.apple.libspindump.hid_response_statistics"
+ "hid_event_count"
+ "infoDictionary"
+ "initWithFormat:"
+ "length"
+ "mainBundle"
+ "ns"
+ "objectForKeyedSubscript:"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
- "Reporting %{public}swakeups for %{public}s [%d] causing %lld cpu wakeups over the last %.0f seconds"
- "Reporting wakeups for pid 0"
- "v16@?0^v8"
- "wakeups"
- "wakeups_limit"

```
