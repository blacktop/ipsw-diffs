## OnDeviceDaemon

> `/System/Library/PrivateFrameworks/OnDeviceDaemon.framework/Versions/A/OnDeviceDaemon`

```diff

-3.0.59.0.0
-  __TEXT.__text: 0x5134
+3.1.10.0.0
+  __TEXT.__text: 0x52b4
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x3d8
-  __TEXT.__swift5_typeref: 0x1c2
+  __TEXT.__const: 0x3d0
+  __TEXT.__swift5_typeref: 0x1c3
   __TEXT.__swift5_fieldmd: 0xfc
   __TEXT.__constg_swiftt: 0x228
   __TEXT.__swift5_reflstr: 0x9a

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x24
-  __TEXT.__cstring: 0x32b
-  __TEXT.__swift5_capture: 0x44
-  __TEXT.__unwind_info: 0x220
-  __TEXT.__eh_frame: 0x340
+  __TEXT.__cstring: 0x1cb
+  __TEXT.__swift5_capture: 0x54
+  __TEXT.__oslogstring: 0x196
+  __TEXT.__unwind_info: 0x258
+  __TEXT.__eh_frame: 0x3b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0xb0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x318
+  __AUTH_CONST.__const: 0x368
   __AUTH_CONST.__objc_const: 0x220
-  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__auth_got: 0x408
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x140
-  __DATA.__data: 0x1f8
-  __DATA_DIRTY.__data: 0x1a0
+  __DATA.__data: 0x230
+  __DATA_DIRTY.__data: 0x148
   __DATA_DIRTY.__bss: 0x80
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 116
-  Symbols:   191
-  CStrings:  23
+  Functions: 127
+  Symbols:   201
+  CStrings:  24
 
Symbols:
+ ___swift__destructor
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ __os_log_impl
+ __swiftImmortalRefCount
+ _memcpy
+ _os_log_type_enabled
+ _swift_beginAccess
+ _swift_release_n
+ _swift_retain_n
+ _swift_unknownObjectRetain
+ _symbolic _____ 2os6LoggerV
+ _symbolic ______p s5ErrorP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- ___swift_destroy_boxed_opaque_existential_1
- _symbolic _____ 18OnDeviceFoundation8OSLoggerV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 18OnDeviceFoundation10LogMessageV
- _symbolic ypSg
CStrings:
+ "%{public}s"
+ "Failed to obtain process audit token: %{public}d. Entitlement checks will deny all."
+ "⚙️ Initializing sandbox for %{public}s"
+ "✅ Activated: %{public}s"
+ "💥 Daemon run loop exited, result=%{public}d"
+ "🟢 Starting daemon with %{public}ld services"
- ". Entitlement checks will deny all."
- "Failed to obtain process audit token: "
- "⚙️ Initializing sandbox for "
- "💥 Daemon run loop exited, result="
- "🟢 Starting daemon with "
```
