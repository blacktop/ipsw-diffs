## BuiltinAudioPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BuiltinAudioPlugin.driver/BuiltinAudioPlugin`

```diff

-100.6.0.0.0
-  __TEXT.__text: 0x10d0
+140.4.0.0.0
+  __TEXT.__text: 0x12b0
   __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_stubs: 0x240
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__cstring: 0x1dd
+  __TEXT.__cstring: 0x24b
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x6a
-  __TEXT.__gcc_except_tab: 0x17c
+  __TEXT.__gcc_except_tab: 0x178
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x8
   __TEXT.__objc_methname: 0x12d
   __TEXT.__unwind_info: 0x98
   __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0x60
-  __DATA_CONST.__cfstring: 0x260
+  __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_intobj: 0x78
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x90
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x8
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 977144FC-349C-3A36-885D-442AF8C63994
+  UUID: 5913CF1A-9B0B-3A75-AB69-E565AC9053E2
   Functions: 8
-  Symbols:   80
-  CStrings:  69
+  Symbols:   82
+  CStrings:  77
 
Symbols:
+ _kASDTIOA2ConfigKeyExclavesOutputBufferName
+ _kASDTIOA2ConfigKeyIsolatedOutputUseCaseID
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
Functions:
~ _BuiltinAudioFactory : 296 -> 304
~ sub_f2c -> sub_f34 : 160 -> 176
~ sub_fcc -> sub_fe4 : 372 -> 376
~ sub_1140 -> sub_115c : 584 -> 632
~ sub_1388 -> sub_13d4 : 2764 -> 3168
CStrings:
+ "140.4"
+ "Receiver"
+ "Speaker"
+ "com.apple.inbound_buffer.receiver_outputstream"
+ "com.apple.inbound_buffer.speaker_outputstream"
- "100.6"

```
