## audioanalyticsd

> `/usr/libexec/audioanalyticsd`

```diff

-223.110.0.0.0
-  __TEXT.__text: 0x34784
-  __TEXT.__auth_stubs: 0x1640
-  __TEXT.__objc_methlist: 0xbc
-  __TEXT.__const: 0x9a8
-  __TEXT.__objc_methname: 0x643
+223.115.0.0.0
+  __TEXT.__text: 0x347d0
+  __TEXT.__auth_stubs: 0x16c0
+  __TEXT.__objc_stubs: 0x80
+  __TEXT.__objc_methlist: 0x124
+  __TEXT.__const: 0x9b0
+  __TEXT.__objc_methname: 0x6f2
   __TEXT.__cstring: 0xedc
   __TEXT.__swift5_typeref: 0x76c
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x48
-  __TEXT.__oslogstring: 0x1caa
-  __TEXT.__swift5_capture: 0x50c
-  __TEXT.__objc_classname: 0x1f
-  __TEXT.__objc_methtype: 0xe9
+  __TEXT.__oslogstring: 0x1d3a
+  __TEXT.__swift5_capture: 0x528
+  __TEXT.__objc_classname: 0x32
+  __TEXT.__objc_methtype: 0x148
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x7d8
-  __TEXT.__eh_frame: 0x598
-  __DATA_CONST.__auth_got: 0xb20
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__auth_ptr: 0x2c0
-  __DATA_CONST.__const: 0x11a0
-  __DATA_CONST.__objc_classlist: 0x40
+  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__eh_frame: 0x560
+  __DATA_CONST.__auth_got: 0xb68
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__auth_ptr: 0x2f8
+  __DATA_CONST.__const: 0x12a8
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0xec8
-  __DATA.__objc_selrefs: 0x200
-  __DATA.__objc_data: 0x370
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0xff8
+  __DATA.__objc_selrefs: 0x240
+  __DATA.__objc_ivar: 0xc
+  __DATA.__objc_data: 0x3c0
   __DATA.__data: 0xd08
   __DATA.__common: 0x68
-  __DATA.__bss: 0x900
+  __DATA.__bss: 0x910
   - /AppleInternal/Library/Frameworks/AudioAnalyticsInternal.framework/AudioAnalyticsInternal
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase
   - /System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal

   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 708
-  Symbols:   551
-  CStrings:  341
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 723
+  Symbols:   573
+  CStrings:  369
 
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ __NSConcreteGlobalBlock
+ __dispatch_main_q
+ __dispatch_source_type_signal
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _dispatch_once
+ _dispatch_resume
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_suspend
+ _objc_opt_new
+ _objc_release_x1
+ _objc_storeStrong
CStrings:
+ "\x01"
+ "@\"NSObject<OS_dispatch_source>\""
+ "@20@0:8i16"
+ "@?16@0:8"
+ "B"
+ "CLISignalHandler"
+ "Exit requested, and timeout reached. Calling exit."
+ "Got SIGTERM. Should die within 2 seconds."
+ "Listening for SIGTERM."
+ "T@?,C,N"
+ "TB,N,V_enabled"
+ "Ti,R,N,V_signal"
+ "_dispatch_source"
+ "_enabled"
+ "_signal"
+ "addObject:"
+ "enabled"
+ "executionBlock"
+ "i"
+ "i16@0:8"
+ "initWithSignal:"
+ "removeObject:"
+ "setEnabled:"
+ "setExecutionBlock:"
+ "signal"
+ "v20@0:8B16"
+ "v24@0:8@?16"

```
