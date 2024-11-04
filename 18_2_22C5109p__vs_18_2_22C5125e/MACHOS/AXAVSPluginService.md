## AXAVSPluginService

> `/System/Library/AccessibilityBundles/AXAVSPluginService.axuiservice/AXAVSPluginService`

```diff

-3148.6.2.0.0
-  __TEXT.__text: 0xe1c
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0x12
+3148.7.3.0.0
+  __TEXT.__text: 0x1190
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x620
+  __TEXT.__objc_methlist: 0x1c4
+  __TEXT.__const: 0x1a
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__objc_methname: 0x956
-  __TEXT.__oslogstring: 0xfd
-  __TEXT.__cstring: 0x78
+  __TEXT.__objc_methname: 0xa50
+  __TEXT.__oslogstring: 0x19d
+  __TEXT.__cstring: 0x7c
   __TEXT.__objc_classname: 0x67
   __TEXT.__objc_methtype: 0x38b
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x150
-  __DATA_CONST.__got: 0x48
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__cfstring: 0x20
+  __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x798
-  __DATA.__objc_selrefs: 0x188
+  __DATA.__objc_selrefs: 0x1e0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   __DATA.__bss: 0x1
+  - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
+  - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 43
-  Symbols:   60
-  CStrings:  157
+  Functions: 45
+  Symbols:   70
+  CStrings:  173
 
Symbols:
+ _OBJC_CLASS_$_AVAudioFile
+ _OBJC_CLASS_$_AVAudioPCMBuffer
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_NSURL
+ _mach_absolute_time
+ _objc_alloc
+ _objc_release_x23
+ _objc_release_x25
+ _objc_retain_x2
+ _objc_retain_x20
CStrings:
+ "Audio length is %!f(MISSING) seconds, will sleep for that duration"
+ "Error reading file into buffer"
+ "Finished piping audio from file to AVS"
+ "URL"
+ "Will pipe audio from file to AVS"
+ "_pipeAudioFromFile:"
+ "fileURLWithPath:"
+ "handleAudioBufferInput:time:"
+ "initForReading:commonFormat:interleaved:error:"
+ "initWithPCMFormat:frameCapacity:"
+ "length"
+ "objectForKeyedSubscript:"
+ "processingFormat"
+ "readIntoBuffer:error:"
+ "sampleRate"
+ "sleepForTimeInterval:"

```
