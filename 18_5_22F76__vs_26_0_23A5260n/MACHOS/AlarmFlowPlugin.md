## AlarmFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin`

```diff

-3405.17.1.0.0
-  __TEXT.__text: 0x1127f8
-  __TEXT.__auth_stubs: 0x3630
+3500.25.1.0.0
+  __TEXT.__text: 0xfe66c
+  __TEXT.__auth_stubs: 0x3600
   __TEXT.__objc_methlist: 0x284
-  __TEXT.__const: 0x3504
-  __TEXT.__cstring: 0x299d
-  __TEXT.__swift5_typeref: 0x1796
+  __TEXT.__const: 0x3cc0
+  __TEXT.__cstring: 0x2a3d
+  __TEXT.__swift5_typeref: 0x1764
   __TEXT.__objc_methname: 0x9a3
   __TEXT.__objc_classname: 0xaf
   __TEXT.__objc_methtype: 0x1a8
-  __TEXT.__swift_as_entry: 0x46c
-  __TEXT.__swift_as_ret: 0x670
+  __TEXT.__swift_as_entry: 0x3e8
+  __TEXT.__swift_as_ret: 0x5ec
   __TEXT.__constg_swiftt: 0x2f80
   __TEXT.__swift5_fieldmd: 0x1944
   __TEXT.__swift5_types: 0x18c
-  __TEXT.__oslogstring: 0x6f85
+  __TEXT.__oslogstring: 0x6ee5
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_proto: 0x1f4
   __TEXT.__swift5_reflstr: 0x1783
   __TEXT.__swift5_assocty: 0x500
   __TEXT.__swift5_capture: 0x114
-  __TEXT.__unwind_info: 0x2fb0
-  __TEXT.__eh_frame: 0x9eb0
-  __DATA_CONST.__auth_got: 0x1b18
-  __DATA_CONST.__got: 0xac8
-  __DATA_CONST.__auth_ptr: 0xf70
-  __DATA_CONST.__const: 0x1bc0
+  __TEXT.__unwind_info: 0x27b0
+  __TEXT.__eh_frame: 0x8e70
+  __DATA_CONST.__auth_got: 0x1b00
+  __DATA_CONST.__got: 0xaa0
+  __DATA_CONST.__auth_ptr: 0xe48
+  __DATA_CONST.__const: 0x1b40
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc0

   __DATA.__objc_const: 0x1d68
   __DATA.__objc_selrefs: 0x4d8
   __DATA.__objc_data: 0xa08
-  __DATA.__data: 0x5298
+  __DATA.__data: 0x49c0
   __DATA.__common: 0x490
   __DATA.__bss: 0x3580
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer

   - /System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/SiriVirtualDeviceResolution
   - /System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E97D9082-0EAD-3A59-A126-54D8E959C7A3
-  Functions: 2451
-  Symbols:   185
-  CStrings:  924
+  UUID: 41DD84ED-A1B5-3E80-8F22-3929D4718450
+  Functions: 2296
+  Symbols:   177
+  CStrings:  927
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_release_x9
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _free
- _malloc
- _swift_unknownObjectRelease_n
- _swift_unknownObjectRetain_n
CStrings:
+ "CreateAlarmIntent"
+ "DeleteAlarmIntent"
+ "DismissAlarmHalIntent"
+ "SnoozeAlarmHalIntent"
+ "UpdateAlarmIntent"
- "Sleep alarm attribute is not nil, but sleep alarm doesn't exist."
- "Unable to recognize the alarm intent %@. Returning default verb of .unknown"

```
