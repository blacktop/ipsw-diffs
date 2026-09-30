## AudioServerApplication

> `/System/Library/PrivateFrameworks/AudioServerApplication.framework/AudioServerApplication`

```diff

-1110.1.0.0.0
-  __TEXT.__text: 0x118c0
+1110.2.0.0.0
+  __TEXT.__text: 0x11c54
   __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x1294
+  __TEXT.__objc_methlist: 0x12b4
   __TEXT.__const: 0x38
-  __TEXT.__oslogstring: 0x11f1
-  __TEXT.__cstring: 0x1069
-  __TEXT.__unwind_info: 0x388
+  __TEXT.__oslogstring: 0x1349
+  __TEXT.__cstring: 0x107b
+  __TEXT.__unwind_info: 0x390
   __TEXT.__objc_classname: 0x100
-  __TEXT.__objc_methname: 0x2857
-  __TEXT.__objc_methtype: 0x5bf
-  __TEXT.__objc_stubs: 0x1b80
+  __TEXT.__objc_methname: 0x292e
+  __TEXT.__objc_methtype: 0x5dc
+  __TEXT.__objc_stubs: 0x1ba0
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa70
+  __DATA_CONST.__objc_selrefs: 0xa88
   __DATA_CONST.__objc_superrefs: 0x80
   __AUTH_CONST.__auth_got: 0x270
-  __AUTH_CONST.__cfstring: 0x1400
-  __AUTH_CONST.__objc_const: 0x17a0
+  __AUTH_CONST.__cfstring: 0x1420
+  __AUTH_CONST.__objc_const: 0x17b0
   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0x68
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 783DBE87-5BE4-3E22-9EA9-0E92F5B3962C
-  Functions: 407
-  Symbols:   1271
-  CStrings:  941
+  UUID: E896F410-5990-3337-BC73-A360D8A2188B
+  Functions: 410
+  Symbols:   1278
+  CStrings:  952
 
Symbols:
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:withIsolatedUseCaseID:]
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:withIsolatedUseCaseID:].cold.1
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:withIsolatedUseCaseID:].cold.2
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:withIsolatedUseCaseID:].cold.3
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:withIsolatedUseCaseID:].cold.4
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:withIsolatedUseCaseID:]
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:withIsolatedUseCaseID:].cold.1
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:withIsolatedUseCaseID:].cold.2
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:withIsolatedUseCaseID:].cold.3
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:withIsolatedUseCaseID:].cold.4
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:withIsolatedUseCaseID:].cold.5
+ -[ASAAudioDevice isolatedUseCaseID]
+ _objc_msgSend$initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:withIsolatedUseCaseID:
+ _objc_msgSend$initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:withIsolatedUseCaseID:
- -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:].cold.1
- -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:].cold.2
- -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:].cold.3
- -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:].cold.4
- -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:].cold.1
- -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:].cold.2
- -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:].cold.3
- -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:].cold.4
- -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:].cold.5
- _objc_msgSend$initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:
CStrings:
+ "@64@0:8@16@24@32@40@48B56I60"
+ "ASAAggregateDevice initWithDevices with ASAAudioDevice and Isolated usercase ID name = %@"
+ "ASAAggregateDevice initWithDevices with ASAAudioDevice name = %@"
+ "ASAAggregateDevice initWithDevices with device UID"
+ "ASAAggregateDevice initWithDevices with device UID and Isolated usercase ID name = %@"
+ "Could not read Device isolate use case ID property\n"
+ "initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:withIsolatedUseCaseID:"
+ "initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:withIsolatedUseCaseID:"
+ "isolated use case"
+ "isolatedUseCaseID"

```
