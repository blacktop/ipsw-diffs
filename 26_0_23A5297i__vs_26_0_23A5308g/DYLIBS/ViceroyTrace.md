## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2145.57.1.0.0
-  __TEXT.__text: 0xad0ac
+2145.61.1.0.0
+  __TEXT.__text: 0xad0c4
   __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_methlist: 0x8cb0
+  __TEXT.__objc_methlist: 0x8cc0
   __TEXT.__const: 0x2478
-  __TEXT.__cstring: 0xe8a7
+  __TEXT.__cstring: 0xe8e6
   __TEXT.__oslogstring: 0xc5ce
   __TEXT.__gcc_except_tab: 0x3d4
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x16a8
+  __TEXT.__unwind_info: 0x16b0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x1ba09
-  __TEXT.__objc_methtype: 0x2423
-  __TEXT.__objc_stubs: 0xecc0
+  __TEXT.__objc_methname: 0x1ba39
+  __TEXT.__objc_methtype: 0x2441
+  __TEXT.__objc_stubs: 0xece0
   __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0xd88
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4290
+  __DATA_CONST.__objc_selrefs: 0x4298
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x220
   __AUTH_CONST.__auth_got: 0x6d8

   __AUTH_CONST.__cfstring: 0xdd20
   __AUTH_CONST.__objc_const: 0x16778
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0x480
+  __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x2000
   __DATA.__data: 0x738
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x60
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1040
   __DATA_DIRTY.__data: 0x78
-  __DATA_DIRTY.__bss: 0x92
+  __DATA_DIRTY.__bss: 0xaa
   __DATA_DIRTY.__common: 0x22
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 32FF3AAE-B514-3356-965B-EF5188A364F9
-  Functions: 3951
-  Symbols:   13008
-  CStrings:  9220
+  UUID: 90B318C5-3D69-3310-8646-ACBCD451796D
+  Functions: 3952
+  Symbols:   13011
+  CStrings:  9223
 
Symbols:
+ -[VCRateControlMachineLearningLocalTrainingDataProducer checkCountQuery:withDatabase:minValue:maxValue:]
+ _objc_msgSend$checkCountQuery:withDatabase:minValue:maxValue:
CStrings:
+ "-[VCRateControlMachineLearningLocalTrainingDataProducer checkCountQuery:withDatabase:minValue:maxValue:]"
+ "B40@0:8*16^{sqlite3=}24i32i36"
+ "SELECT COUNT(*) FROM Feedback WHERE trainingValue > 0;"
+ "checkCountQuery:withDatabase:minValue:maxValue:"
- "-[VCRateControlMachineLearningLocalTrainingDataProducer shouldGenerateTrainingDataWithDatabase:]"

```
