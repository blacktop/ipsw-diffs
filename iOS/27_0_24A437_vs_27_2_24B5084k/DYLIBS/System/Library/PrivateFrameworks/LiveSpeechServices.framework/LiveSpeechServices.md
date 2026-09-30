## LiveSpeechServices

> `/System/Library/PrivateFrameworks/LiveSpeechServices.framework/LiveSpeechServices`

```diff

-3240.9.0.0.0
-  __TEXT.__text: 0x5668
-  __TEXT.__objc_methlist: 0x374
-  __TEXT.__const: 0x618
+3245.7.1.0.0
+  __TEXT.__text: 0x5ffc
+  __TEXT.__objc_methlist: 0x3bc
+  __TEXT.__const: 0x628
   __TEXT.__cstring: 0x112
   __TEXT.__constg_swiftt: 0x14c
   __TEXT.__swift5_typeref: 0x1b0
-  __TEXT.__swift5_reflstr: 0x115
-  __TEXT.__swift5_fieldmd: 0x12c
+  __TEXT.__swift5_reflstr: 0x155
+  __TEXT.__swift5_fieldmd: 0x150
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x20
-  __TEXT.__swift5_capture: 0xfc
-  __TEXT.__oslogstring: 0x3b6
+  __TEXT.__swift5_capture: 0x12c
+  __TEXT.__oslogstring: 0x556
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x320
-  __TEXT.__eh_frame: 0x160
+  __TEXT.__unwind_info: 0x358
+  __TEXT.__eh_frame: 0x1d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d8
+  __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__objc_const: 0x438
-  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__const: 0x7e8
+  __AUTH_CONST.__objc_const: 0x458
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH.__objc_data: 0x90
   __DATA.__data: 0x170
-  __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__data: 0x70
+  __DATA_DIRTY.__objc_data: 0x198
+  __DATA_DIRTY.__data: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 242
-  Symbols:   275
-  CStrings:  29
+  Functions: 261
+  Symbols:   280
+  CStrings:  38
 
Symbols:
+ +[LiveSpeechServicesObjc startChatterboxAndReturnError:]
+ +[LiveSpeechServicesObjc stopChatterboxAndReturnError:]
+ _AXDeviceSupportsChatterbox
+ _objc_msgSend$startChatterboxAndReturnError:
+ _objc_msgSend$stopChatterboxAndReturnError:
CStrings:
+ "Already running Chatterbox, skip"
+ "Can't stop Chatterbox, not running"
+ "Chatterbox not supported, skip"
+ "Client received Chatterbox start success callback"
+ "Client received Chatterbox stop success callback"
+ "Client requesting Chatterbox start"
+ "Client requesting Chatterbox stop"
+ "Failed to start Chatterbox: %@"
+ "Failed to stop Chatterbox: %@"
```
