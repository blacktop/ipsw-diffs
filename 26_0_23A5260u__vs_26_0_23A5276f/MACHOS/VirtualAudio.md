## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1359.2.30.3.0
-  __TEXT.__text: 0x4f37e0
-  __TEXT.__auth_stubs: 0x2680
+1364.102.2.1.0
+  __TEXT.__text: 0x4f2380
+  __TEXT.__auth_stubs: 0x26d0
   __TEXT.__objc_stubs: 0xa00
   __TEXT.__init_offsets: 0x4d4
   __TEXT.__objc_methlist: 0x134
-  __TEXT.__const: 0xb0ae2
-  __TEXT.__gcc_except_tab: 0x5c7ac
-  __TEXT.__cstring: 0x284bc
+  __TEXT.__const: 0xb0ada
+  __TEXT.__gcc_except_tab: 0x5c3f0
+  __TEXT.__cstring: 0x284ca
   __TEXT.__objc_classname: 0x34
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_capture: 0x158
-  __TEXT.__oslogstring: 0x4d57e
+  __TEXT.__oslogstring: 0x4d60a
   __TEXT.__objc_methname: 0x723
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x10bf0
+  __TEXT.__unwind_info: 0x10c28
   __TEXT.__eh_frame: 0x778
-  __DATA_CONST.__auth_got: 0x1358
+  __DATA_CONST.__auth_got: 0x1380
   __DATA_CONST.__got: 0x4d8
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x26ab8
+  __DATA_CONST.__const: 0x26b28
   __DATA_CONST.__cfstring: 0x2d60
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 893B19AB-3D04-361F-AA96-CCA263D6DAB9
-  Functions: 11048
-  Symbols:   771
-  CStrings:  11199
+  UUID: 56E065AD-0855-379C-AFE3-AA6B68732CB0
+  Functions: 11059
+  Symbols:   772
+  CStrings:  11204
 
Symbols:
+ _CADSPGraphGetProperty
+ _CADSPGraphSetProperty
+ _CADSPRealTimeErrorCreateWithRealTimeSafeAllocator
+ _CADSPRealTimeErrorGetCode
+ _CADSPRealTimeErrorRelease
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "%25s:%-5d ASSERTION FAILURE: \"unable to lock stream\""
+ "%25s:%-5d Active port %u, type %u for device %lu"
+ "%25s:%-5d Adding non null IOProc listener for VAD %u."
+ "%25s:%-5d Applying conditional tuning for use case %u element %u"
+ "%25s:%-5d Bluetooth device expired, not calling async device function."
+ "%25s:%-5d Conditional tuning returned an invalid CFDictionary. Removing"
+ "%25s:%-5d Failed to find fallback device UID: %s"
+ "%25s:%-5d Product %s use DSP graph v2. Enabled system wide? %d. Enabled for product in VA? %d"
+ "@@ Strips Jun 18 2025 21:04:33"
+ "will"
+ "will not"
- "%25s:%-5d Active port %u, type %u"
- "%25s:%-5d Adding IsRunning listener for VAD %u."
- "%25s:%-5d Conditional tuning returned an invalid CFDictionary. Skipping"
- "%25s:%-5d Disallowing HFP port in simulated activation command due to device activation reason %s"
- "%25s:%-5d Failed to add fallback device because the top device on the stack does not match fallback device UID: %s"
- "@@ Strips May 30 2025 20:34:23"

```
