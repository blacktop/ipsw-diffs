## AudioServerDriverTransports_IOP

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/AudioServerDriverTransports_IOP`

```diff

-200.54.0.0.0
-  __TEXT.__text: 0xd26c
+220.21.0.0.0
+  __TEXT.__text: 0xdcfc
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0xa88
-  __TEXT.__gcc_except_tab: 0xf64
+  __TEXT.__objc_methlist: 0xa90
+  __TEXT.__gcc_except_tab: 0x11f0
   __TEXT.__const: 0x120
-  __TEXT.__oslogstring: 0xd9b
-  __TEXT.__cstring: 0xe6d
-  __TEXT.__unwind_info: 0x730
+  __TEXT.__oslogstring: 0xdc5
+  __TEXT.__cstring: 0xe79
+  __TEXT.__unwind_info: 0x6e0
   __TEXT.__objc_classname: 0x32e
-  __TEXT.__objc_methname: 0x116c
+  __TEXT.__objc_methname: 0x11fb
   __TEXT.__objc_methtype: 0x93e
-  __TEXT.__objc_stubs: 0x1180
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0xb0
+  __TEXT.__objc_stubs: 0x1200
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x580
+  __DATA_CONST.__objc_selrefs: 0x5a8
   __DATA_CONST.__objc_superrefs: 0x90
   __AUTH_CONST.__auth_got: 0x340
-  __AUTH_CONST.__const: 0x208
+  __AUTH_CONST.__const: 0x228
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x18f8
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0x120
+  __DATA.__data: 0x128
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x5a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 438
-  Symbols:   685
-  CStrings:  532
+  Functions: 425
+  Symbols:   670
+  CStrings:  539
 
Symbols:
+ _ASDTIOPLogType
+ __NSConcreteGlobalBlock
+ __ZN4ASDT8Exclaves11AudioBuffer4ReadEPhjjRNS0_6Sensor6StatusE
+ __ZN4ASDT8Exclaves13StatusTracker4PushERKNS1_6UpdateE
+ __ZN8ASDTTime16machAbsoluteTimeEv
+ __os_log_debug_impl
+ _dispatch_once
+ _os_log_create
- __ZN4ASDT8Exclaves11NamedBuffer4ReadEPhjj
- __ZNSt11logic_errorC2EPKc
- __ZNSt12length_errorD1Ev
- __ZTISt12length_error
- __ZTVSt12length_error
- __ZdlPv
- __Znwm
- _memmove
- _strlen
CStrings:
+ "%!@(MISSING):%!@(MISSING): Failed to setup non-secure input path."
+ "%!@(MISSING):%!@(MISSING): Stream not active for ioThread start."
+ "IOP"
+ "allocExclavesAudioBuffer:"
+ "asdtIOThreadChangeEvent"
+ "asdtIOThreadChangeIsolatedUseCase"
+ "asdtIOThreadUseCaseIsFirstOrWasLast"
+ "com.apple.audio.ASDT"
+ "exclavesAudioBuffer"
+ "exclavesSensorManager"
+ "freeExclavesAudioBuffer"
+ "ioThreadStateChange:"
+ "statusTracker"
- "%!@(MISSING):%!@(MISSING): Cannot update stream format while active."
- "allocExclavesNamedBuffer:"
- "basic_string"
- "exclavesBuffer"
- "freeExclavesNamedBuffer"
- "setIsActive:"

```
