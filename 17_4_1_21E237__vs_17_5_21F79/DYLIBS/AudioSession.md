## AudioSession

> `/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`

```diff

-263.5.23.0.0
-  __TEXT.__text: 0x35968
+263.6.1.0.0
+  __TEXT.__text: 0x35cc4
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x16c8
-  __TEXT.__gcc_except_tab: 0x54e8
+  __TEXT.__objc_methlist: 0x1778
+  __TEXT.__gcc_except_tab: 0x5520
   __TEXT.__cstring: 0x20fd
   __TEXT.__const: 0x240
   __TEXT.__oslogstring: 0x2424
-  __TEXT.__unwind_info: 0x2170
+  __TEXT.__unwind_info: 0x21d4
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x27a
-  __TEXT.__objc_methname: 0x3eba
-  __TEXT.__objc_methtype: 0x1185
-  __TEXT.__objc_stubs: 0x23e0
+  __TEXT.__objc_classname: 0x2ae
+  __TEXT.__objc_methname: 0x3ee8
+  __TEXT.__objc_methtype: 0x11d8
+  __TEXT.__objc_stubs: 0x2500
   __DATA_CONST.__got: 0x868
   __DATA_CONST.__const: 0x6a8
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1110
-  __DATA_CONST.__objc_selrefs: 0x1178
+  __DATA_CONST.__objc_const: 0x1468
+  __DATA_CONST.__objc_selrefs: 0x1180
   __DATA_CONST.__objc_classrefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__cfstring: 0x1c00
-  __AUTH_CONST.__objc_const: 0x678
+  __AUTH_CONST.__objc_const: 0x6c0
   __AUTH_CONST.__const: 0x11c0
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH_CONST.__auth_got: 0x5b0
-  __AUTH.__objc_data: 0xf0
+  __AUTH.__objc_data: 0xa0
   __DATA.__got_weak: 0x8
-  __DATA.__objc_ivar: 0x68
-  __DATA.__data: 0x3a8
+  __DATA.__objc_ivar: 0x6c
+  __DATA.__data: 0x3e0
   __DATA.__common: 0x1
-  __DATA.__bss: 0xd0
-  __DATA_DIRTY.__objc_data: 0x3c0
+  __DATA.__bss: 0x48
+  __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__data: 0xb0
-  __DATA_DIRTY.__bss: 0x110
+  __DATA_DIRTY.__bss: 0x1c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D80DF1FC-C9CC-35A9-9EB9-AE59A24B2EFC
-  Functions: 1211
-  Symbols:   4249
-  CStrings:  1459
+  UUID: 286892C3-03C1-3C9B-857E-79C7DA884AE0
+  Functions: 1225
+  Symbols:   4303
+  CStrings:  1468
 
Symbols:
+ -[AVAudioSecureSession .cxx_destruct]
+ -[AVAudioSecureSession IOBufferDuration]
+ -[AVAudioSecureSession IOBufferFrameSize]
+ -[AVAudioSecureSession availableCategories]
+ -[AVAudioSecureSession availableModes]
+ -[AVAudioSecureSession category]
+ -[AVAudioSecureSession initWithIsolatedAudioUseCaseID:]
+ -[AVAudioSecureSession initWithUseCaseIdentifier:]
+ -[AVAudioSecureSession inputLatency]
+ -[AVAudioSecureSession inputSampleRate]
+ -[AVAudioSecureSession mode]
+ -[AVAudioSecureSession setActive:error:]
+ -[AVAudioSecureSession setCategory:error:]
+ -[AVAudioSecureSession setCategory:mode:options:error:]
+ _OBJC_CLASS_$_AVAudioSecureSession
+ _OBJC_IVAR_$_AVAudioSecureSession._innerSession
+ _OBJC_METACLASS_$_AVAudioSecureSession
+ __OBJC_$_INSTANCE_METHODS_AVAudioSecureSession
+ __OBJC_$_INSTANCE_VARIABLES_AVAudioSecureSession
+ __OBJC_$_PROP_LIST_AVAudioSecureSession
+ __OBJC_$_PROP_LIST_AVAudioSecureSessionProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVAudioSecureSessionProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVAudioSecureSessionProtocol
+ __OBJC_$_PROTOCOL_REFS_AVAudioSecureSessionProtocol
+ __OBJC_CLASS_PROTOCOLS_$_AVAudioSecureSession
+ __OBJC_CLASS_RO_$_AVAudioSecureSession
+ __OBJC_LABEL_PROTOCOL_$_AVAudioSecureSessionProtocol
+ __OBJC_METACLASS_RO_$_AVAudioSecureSession
+ __OBJC_PROTOCOL_$_AVAudioSecureSessionProtocol
+ _objc_msgSend$IOBufferDuration
+ _objc_msgSend$initWithIsolatedAudioUseCaseID:
+ _objc_msgSend$inputLatency
+ _objc_msgSend$inputSampleRate
+ _objc_msgSend$mode
+ _objc_msgSend$registerPublishingSessionNotifications:
+ _objc_msgSend$setActive:error:
+ _objc_msgSend$setCategory:error:
+ _objc_msgSend$setCategory:mode:options:error:
CStrings:
+ "\x01"
+ "@\"NSArray\"16@0:8"
+ "AVAudioSecureSession"
+ "AVAudioSecureSessionProtocol"
+ "B32@0:8@\"NSString\"16^@24"
+ "B48@0:8@\"NSString\"16@\"NSString\"24Q32^@40"
+ "Td,R"
+ "_innerSession"
+ "initWithUseCaseIdentifier:"

```
