## BuiltinAudioPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BuiltinAudioPlugin.driver/BuiltinAudioPlugin`

```diff

-200.54.0.0.0
-  __TEXT.__text: 0xf28
+220.24.0.0.0
+  __TEXT.__text: 0xd64
   __TEXT.__auth_stubs: 0x1b0
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__oslogstring: 0x54
+  __TEXT.__cstring: 0x153
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__cstring: 0xe2
+  __TEXT.__gcc_except_tab: 0x124
   __TEXT.__objc_classname: 0x14
-  __TEXT.__objc_methname: 0x11a
   __TEXT.__objc_methtype: 0x8
+  __TEXT.__objc_methname: 0xfe
   __TEXT.__unwind_info: 0x80
   __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x20
-  __DATA_CONST.__cfstring: 0x1a0
+  __DATA_CONST.__const: 0x60
+  __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x80
+  __DATA.__objc_selrefs: 0x78
   __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x40
+  __DATA.__data: 0x8
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5
-  Symbols:   71
-  CStrings:  36
+  Functions: 7
+  Symbols:   74
+  CStrings:  39
 
Symbols:
+ _BuiltinLogType
+ _OBJC_CLASS_$_ASDTExclavesSensorAutomaticProperty
+ _OBJC_CLASS_$_ASDTExclavesStatusProperty
+ __NSConcreteGlobalBlock
+ _kASDTIOA2ConfigKeyExclavesInjectionBufferName
+ _os_log_create
- _OBJC_CLASS_$_ASDTExclavesSensorPMEnabler
- _kASDTConfigKeyDevicePMDevices
- _objc_release_x23
CStrings:
+ "Builtin"
+ "com.apple.audio.ASDT"
+ "com.apple.inbound_buffer.hpmic16_injection"
+ "com.apple.inbound_buffer.hpmic_injection"
- "configForAutoSensorProperty"

```
