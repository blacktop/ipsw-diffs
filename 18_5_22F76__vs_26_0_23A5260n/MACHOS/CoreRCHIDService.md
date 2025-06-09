## CoreRCHIDService

> `/System/Library/PrivateFrameworks/CoreRC.framework/PlugIns/CoreRCHIDService.plugin/CoreRCHIDService`

```diff

-254.120.2.0.0
-  __TEXT.__text: 0x17d0
+267.0.0.0.0
+  __TEXT.__text: 0x1c64
   __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_stubs: 0x400
-  __TEXT.__objc_methlist: 0x3dc
+  __TEXT.__objc_stubs: 0x540
+  __TEXT.__objc_methlist: 0x3f4
   __TEXT.__const: 0x48
+  __TEXT.__cstring: 0x634
   __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methname: 0x7a0
+  __TEXT.__objc_methname: 0x8b0
   __TEXT.__objc_methtype: 0x48f
-  __TEXT.__cstring: 0x565
-  __TEXT.__unwind_info: 0xc0
+  __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x120
+  __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x8d0
-  __DATA.__objc_selrefs: 0x238
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA.__objc_const: 0x5f8
+  __DATA.__objc_selrefs: 0x290
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x3c8

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5EC693D6-ED4B-3D07-A066-A681FCC99672
-  Functions: 53
-  Symbols:   61
-  CStrings:  205
+  UUID: 53C20AD5-00B9-3CF8-94E4-53F8DBB905E9
+  Functions: 57
+  Symbols:   64
+  CStrings:  232
 
Symbols:
+ _OBJC_CLASS_$_CoreIRBus
+ _OBJC_CLASS_$_NSConstantDictionary
+ _gLogCategory_CoreRCDevice
Functions:
+ sub_d9c
+ sub_2004
+ sub_2624
+ sub_26ec
CStrings:
+ "-[CoreRCHIDService(CoreRC) addIRMappingWithValue:]"
+ "Error adding IR mapping %@"
+ "addDeviceWithType:matching:learningSession:error:"
+ "addIRMappingWithValue:"
+ "addIRMappingwithValue: %@\n"
+ "addMappingWithProtocolID:options:commandToMap:command:repeat:"
+ "added device %@ (%@)"
+ "buses"
+ "command"
+ "corerccommand"
+ "debug"
+ "endLearning"
+ "integerValue"
+ "isLocalDevice"
+ "isReceiver"
+ "kCoreIRLearningSessionReasonLearning"
+ "objectForKeyedSubscript:"
+ "protocol"
+ "repeat"
+ "setOSDName:error:"
+ "startLearningSessionWithReason:error:"

```
