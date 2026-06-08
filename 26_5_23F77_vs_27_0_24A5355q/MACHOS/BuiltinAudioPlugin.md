## BuiltinAudioPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BuiltinAudioPlugin.driver/BuiltinAudioPlugin`

```diff

-140.4.0.0.0
+200.14.0.0.0
   __TEXT.__text: 0x12b0
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__objc_stubs: 0x240
+  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__objc_stubs: 0x260
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x2c
-  __TEXT.__cstring: 0x24b
-  __TEXT.__const: 0x18
-  __TEXT.__oslogstring: 0x6a
-  __TEXT.__gcc_except_tab: 0x178
-  __TEXT.__objc_classname: 0x14
+  __TEXT.__objc_methlist: 0x44
+  __TEXT.__cstring: 0x261
+  __TEXT.__const: 0x20
+  __TEXT.__oslogstring: 0x74
+  __TEXT.__gcc_except_tab: 0x198
+  __TEXT.__objc_classname: 0x26
   __TEXT.__objc_methtype: 0x8
-  __TEXT.__objc_methname: 0x12d
+  __TEXT.__objc_methname: 0x13d
   __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0x60
-  __DATA_CONST.__cfstring: 0x2e0
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__cfstring: 0x300
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x90
-  __DATA.__objc_data: 0x50
+  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x140
+  __DATA.__objc_const: 0x120
+  __DATA.__objc_selrefs: 0x98
+  __DATA.__objc_data: 0xa0
   __DATA.__data: 0x8
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6594035D-FD56-374E-B74D-742C22346C58
-  Functions: 8
-  Symbols:   82
-  CStrings:  77
+  UUID: 181D6485-2E45-30A7-AB0E-7671CA14C0FD
+  Functions: 9
+  Symbols:   88
+  CStrings:  81
 
Symbols:
+ _OBJC_CLASS_$_BuiltinAudioConfig
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSObject
+ _OBJC_METACLASS_$_BuiltinAudioConfig
+ _kASDTIOA2ConfigKeyAllowExclavesOutputBufferSkip
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
CStrings:
+ "%@: No devices for this platform; not: '%@'"
+ "200.14"
+ "BuiltinAudioConfig"
+ "Secure MCA Loopback"
+ "bytes"
+ "initWithBytes:length:encoding:"
+ "mainBundle"
- "%s: No devices for this platform."
- "140.4"
- "bundleID"
- "initWithData:encoding:"

```
