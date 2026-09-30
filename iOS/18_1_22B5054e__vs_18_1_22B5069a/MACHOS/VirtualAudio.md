## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1267.207.30.1.0
-  __TEXT.__text: 0x4b1884
-  __TEXT.__auth_stubs: 0x2580
+1267.209.30.3.0
+  __TEXT.__text: 0x4b3378
+  __TEXT.__auth_stubs: 0x25d0
   __TEXT.__objc_stubs: 0x9e0
   __TEXT.__init_offsets: 0x4c4
   __TEXT.__objc_methlist: 0x384
-  __TEXT.__const: 0xb0f0e
-  __TEXT.__gcc_except_tab: 0x56530
-  __TEXT.__oslogstring: 0x4dd79
-  __TEXT.__cstring: 0x27ee2
-  __TEXT.__objc_methname: 0xde2
+  __TEXT.__const: 0xb106e
+  __TEXT.__gcc_except_tab: 0x56664
+  __TEXT.__oslogstring: 0x4df2a
+  __TEXT.__cstring: 0x27e04
+  __TEXT.__objc_methname: 0xde7
   __TEXT.__objc_classname: 0xa8
   __TEXT.__objc_methtype: 0xc31
-  __TEXT.__swift5_typeref: 0xf6
-  __TEXT.__swift5_capture: 0x154
-  __TEXT.__constg_swiftt: 0x110
+  __TEXT.__swift5_typeref: 0x133
+  __TEXT.__swift5_capture: 0x158
+  __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c
   __TEXT.__swift5_fieldmd: 0x68
   __TEXT.__swift5_proto: 0x8

   __TEXT.__dof_VirtualAu: 0x303
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0xfdc0
-  __TEXT.__eh_frame: 0x7b8
-  __DATA_CONST.__auth_got: 0x12d8
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x24088
-  __DATA_CONST.__cfstring: 0x3be0
+  __TEXT.__unwind_info: 0xfe88
+  __TEXT.__eh_frame: 0x7a8
+  __DATA_CONST.__auth_got: 0x1300
+  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__auth_ptr: 0x78
+  __DATA_CONST.__const: 0x24208
+  __DATA_CONST.__cfstring: 0x3c00
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0xde0
   __DATA.__objc_selrefs: 0x388
   __DATA.__objc_ivar: 0x2c
-  __DATA.__objc_data: 0x3c0
+  __DATA.__objc_data: 0x3a8
   __DATA.__data: 0x508
-  __DATA.__bss: 0x20960
+  __DATA.__bss: 0x20a00
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10130
-  Symbols:   748
-  CStrings:  10781
+  Functions: 10172
+  Symbols:   750
+  CStrings:  10785
 
Symbols:
+ __swiftEmptyDictionarySingleton
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _swift_getAtKeyPath
+ _swift_getKeyPath
+ _swift_runtimeSupportsNoncopyableTypes
- _malloc_size
- _swift_arrayInitWithCopy
- _swift_beginAccess
- _swift_endAccess
CStrings:
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE: \"Should be called from the VirtualAudio queue!\""
+ "%!s(MISSING):%!d(MISSING) Adding model manager monitor observer %!s(MISSING) (hash %!z(MISSING)u)"
+ "%!s(MISSING):%!d(MISSING) Did not find observer %!z(MISSING)u"
+ "%!s(MISSING):%!d(MISSING) Failed to add model manager monitor observer for chain at %!z(MISSING)u to central callback handler"
+ "%!s(MISSING):%!d(MISSING) Lockout time complete. Disabling mitigation."
+ "%!s(MISSING):%!d(MISSING) Mitigation is required again. Cancelling any existing lockout."
+ "%!s(MISSING):%!d(MISSING) No more observers, unregistered monitor"
+ "%!s(MISSING):%!d(MISSING) Removing observer %!z(MISSING)u"
+ "%!s(MISSING):%!d(MISSING) Using timeout of %!u(MISSING)"
+ "@@ Strips Sep 30 2024 22:40:44"
+ "GMTimeoutOverride"
+ "ModelManagerMonitor:: exception while executing Task...%!@(MISSING)"
+ "VA ModelManagerMonitor:: adding observer %!l(MISSING)d"
+ "VA ModelManagerMonitor:: remaining observers count %!l(MISSING)d"
+ "VA ModelManagerMonitor::unregister_from_inference_monitor"
+ "register_for_inference_monitor_eventsWithHash:eventCallback:completionHandler:"
+ "v16@?0Q8"
+ "v32@0:8Q16@?<v@?>24"
+ "v40@0:8Q16@?<v@?B>24@?<v@?Q>32"
- "%!s(MISSING):%!d(MISSING) Adding model manager monitor observer %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) Central model manager inference handler is destroyed"
- "%!s(MISSING):%!d(MISSING) Failed to add model manager monitor observer for chain %!s(MISSING) to central callback handler"
- "@@ Strips Sep 18 2024 13:53:08"
- "Fatal error"
- "Swift/UnsafePointer.swift"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "VA ModelManagerMonitor:: exception while executing Task...%!@(MISSING)"
- "VA ModelManagerMonitor:: removing observer[%!l(MISSING)d]"
- "register_for_inference_monitor_eventsWithEventCallback:completionHandler:"
- "v16@?0q8"
- "v32@0:8@?<v@?B>16@?<v@?q>24"
- "v32@0:8q16@?<v@?>24"

```
