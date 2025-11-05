## DoubleAgent

> `/System/Library/PrivateFrameworks/DoubleAgent.framework/Versions/A/DoubleAgent`

```diff

 30.0.0.0.0
-  __TEXT.__text: 0x427c
+  __TEXT.__text: 0x42b0
   __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_methlist: 0x29c
+  __TEXT.__objc_methlist: 0x3f4
   __TEXT.__const: 0x98
   __TEXT.__cstring: 0x305
   __TEXT.__oslogstring: 0x47e
-  __TEXT.__unwind_info: 0x110
+  __TEXT.__unwind_info: 0x118
   __TEXT.__objc_classname: 0x47
   __TEXT.__objc_methname: 0x876
   __TEXT.__objc_methtype: 0x5b5

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x200
+  __DATA_CONST.__objc_selrefs: 0x2a0
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x100
   __AUTH_CONST.__const: 0xb0
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x770
+  __AUTH_CONST.__objc_const: 0x4f8
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 541B79CE-A989-3B91-989B-ACED493F8887
-  Functions: 99
-  Symbols:   226
+  UUID: AB501E4A-ECA8-3BC6-82E6-40D795961449
+  Functions: 100
+  Symbols:   227
   CStrings:  220
 
Symbols:
+ doubleagent_std_log.cold.1
Functions:
~ -[AppleDoubleParser isXattrNameValid:] : 116 -> 112
~ -[AppleDoubleParser lookupXattrNamed:reply:] : 484 -> 488
~ -[AppleDoubleParser listXattrs:] : 620 -> 616
~ -[AppleDoubleParser allocateXattrNamed:sized:how:reply:] : 2140 -> 2128
~ -[AppleDoubleParser removeXattrNamed:reply:] : 1796 -> 1804
~ -[AppleDoubleParser shiftDataDownAtOffset:length:delta:error:] : 444 -> 440
~ -[AppleDoubleParser shiftDataUpAtOffset:length:delta:error:] : 460 -> 444
~ -[AppleDoubleParser fillEmptyAppleDoubleFile:] : 296 -> 292
~ -[AppleDoubleParser writeHeaderToDiskUpToLength:error:] : 296 -> 288
~ -[AppleDoubleParser parseFileHeader:] : 360 -> 372
~ -[AppleDoubleParser parseFinderInfoAndResourceFork:] : 640 -> 636
~ -[AppleDoubleParser parseAttrHeader:] : 612 -> 620
~ -[AppleDoubleParser createAttrHeaderIfNeeded:] : 564 -> 568
~ -[AppleDoubleParser initWithFileDescriptor:fileSize:isAllocateXattr:] : 968 -> 972
~ _OUTLINED_FUNCTION_0 : 32 -> 20
~ _OUTLINED_FUNCTION_2 : 20 -> 16
~ _doubleagent_std_log : 84 -> 68
~ -[AppleDoubleParser allocateXattrNamed:sized:how:reply:].cold.1 : 140 -> 148
~ -[AppleDoubleParser removeXattrNamed:reply:].cold.1 : 140 -> 132
~ -[AppleDoubleParser removeXattrNamed:reply:].cold.2 : 116 -> 132
~ -[AppleDoubleParser removeXattrNamed:reply:].cold.3 : 132 -> 116
~ -[AppleDoubleParser removeXattrNamed:reply:].cold.4 : 132 -> 148
~ -[AppleDoubleParser shiftDataDownAtOffset:length:delta:error:].cold.1 : 132 -> 148
~ -[AppleDoubleParser shiftDataDownAtOffset:length:delta:error:].cold.2 : 140 -> 148
~ -[AppleDoubleParser shiftDataDownAtOffset:length:delta:error:].cold.3 : 140 -> 132
~ -[AppleDoubleParser shiftDataUpAtOffset:length:delta:error:].cold.1 : 132 -> 148
~ -[AppleDoubleParser shiftDataUpAtOffset:length:delta:error:].cold.2 : 140 -> 148
~ -[AppleDoubleParser shiftDataUpAtOffset:length:delta:error:].cold.3 : 140 -> 132
~ -[AppleDoubleParser fillEmptyAppleDoubleFile:].cold.1 : 140 -> 148
~ -[AppleDoubleParser updateFileSize:].cold.1 : 164 -> 156
~ -[AppleDoubleParser readRawHeader:].cold.1 : 132 -> 148
~ -[AppleDoubleParser readRawHeader:].cold.2 : 140 -> 132
~ -[AppleDoubleParser writeHeaderToDiskUpToLength:error:].cold.1 : 140 -> 156
~ -[AppleDoubleParser writeHeaderToDiskUpToLength:error:].cold.2 : 156 -> 148
~ -[AppleDoubleParser parseFinderInfoAndResourceFork:].cold.1 : 80 -> 148
~ -[AppleDoubleParser parseFinderInfoAndResourceFork:].cold.2 : 140 -> 80
~ -[AppleDoubleParser createAttrHeaderIfNeeded:].cold.1 : 140 -> 132
~ -[AppleDoubleParser createAttrHeaderIfNeeded:].cold.3 : 132 -> 148

```
