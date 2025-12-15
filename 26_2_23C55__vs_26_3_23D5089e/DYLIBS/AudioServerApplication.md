## AudioServerApplication

> `/System/Library/PrivateFrameworks/AudioServerApplication.framework/AudioServerApplication`

```diff

-1110.2.0.0.0
-  __TEXT.__text: 0x11c54
+1130.8.0.0.0
+  __TEXT.__text: 0x11e24
   __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x12b4
+  __TEXT.__objc_methlist: 0x1314
   __TEXT.__const: 0x38
-  __TEXT.__oslogstring: 0x1349
-  __TEXT.__cstring: 0x107b
-  __TEXT.__unwind_info: 0x390
+  __TEXT.__oslogstring: 0x13cf
+  __TEXT.__cstring: 0x10d3
+  __TEXT.__unwind_info: 0x3a0
   __TEXT.__objc_classname: 0x100
-  __TEXT.__objc_methname: 0x292e
+  __TEXT.__objc_methname: 0x2b49
   __TEXT.__objc_methtype: 0x5dc
-  __TEXT.__objc_stubs: 0x1ba0
+  __TEXT.__objc_stubs: 0x1c00
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa88
+  __DATA_CONST.__objc_selrefs: 0xac8
   __DATA_CONST.__objc_superrefs: 0x80
   __AUTH_CONST.__auth_got: 0x270
-  __AUTH_CONST.__cfstring: 0x1420
-  __AUTH_CONST.__objc_const: 0x17b0
+  __AUTH_CONST.__cfstring: 0x1460
+  __AUTH_CONST.__objc_const: 0x1848
   __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_ivar: 0x74
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4484F8F6-5B0B-347C-8AF8-737ACA279873
-  Functions: 410
-  Symbols:   1278
-  CStrings:  952
+  UUID: 8451161E-F33D-3C40-9600-721FAA581F12
+  Functions: 418
+  Symbols:   1301
+  CStrings:  972
 
Symbols:
+ -[ASAAudioDevice externalVoiceActivityDetectEnable]
+ -[ASAAudioDevice externalVoiceActivityDetected]
+ -[ASAAudioDevice externalVoiceActivityDetectionEnable]
+ -[ASAAudioDevice setExternalVoiceActivityDetectEnable:]
+ -[ASAAudioDevice setExternalVoiceActivityDetected:]
+ -[ASAAudioDevice setExternalVoiceActivityDetectionEnable:]
+ -[ASAAudioDevice supportsExternalVoiceActivityDetectEnable]
+ -[ASAAudioDevice supportsExternalVoiceActivityDetectionEnable]
+ _OBJC_IVAR_$_ASAAudioDevice._externalVoiceActivityDetectEnable
+ _OBJC_IVAR_$_ASAAudioDevice._externalVoiceActivityDetected
+ _OBJC_IVAR_$_ASAAudioDevice._supportsExternalVoiceActivityDetectEnable
+ __OBJC_$_INSTANCE_VARIABLES_ASAAudioDevice
+ _objc_msgSend$externalVoiceActivityDetectEnable
+ _objc_msgSend$externalVoiceActivityDetected
+ _objc_msgSend$supportsExternalVoiceActivityDetectEnable
CStrings:
+ "%@|    ExternalVoiceActivityDetectEnable: %@\n"
+ "%@|    ExternalVoiceActivityDetected: %@\n"
+ "Could not read ExternalVoiceActivityDetectionEnable property\n"
+ "Could not set kAudioDevicePropertyExternalVoiceActivityDetectionEnable\n"
+ "TB,N,V_externalVoiceActivityDetectEnable"
+ "TB,N,V_externalVoiceActivityDetected"
+ "TB,R,N,V_supportsExternalVoiceActivityDetectEnable"
+ "_externalVoiceActivityDetectEnable"
+ "_externalVoiceActivityDetected"
+ "_supportsExternalVoiceActivityDetectEnable"
+ "externalVoiceActivityDetectEnable"
+ "externalVoiceActivityDetected"
+ "externalVoiceActivityDetectionEnable"
+ "setExternalVoiceActivityDetectEnable:"
+ "setExternalVoiceActivityDetected:"
+ "setExternalVoiceActivityDetectionEnable:"
+ "supportsExternalVoiceActivityDetectEnable"
+ "supportsExternalVoiceActivityDetectionEnable"

```
