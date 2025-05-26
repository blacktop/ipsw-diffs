## HID

> `/System/Library/PrivateFrameworks/HID.framework/HID`

```diff

-2008.80.3.0.1
-  __TEXT.__text: 0x7388
+2031.100.16.0.0
+  __TEXT.__text: 0x73b8
   __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_methlist: 0x1874
+  __TEXT.__objc_methlist: 0x18a4
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x1805
+  __TEXT.__cstring: 0x1833
   __TEXT.__gcc_except_tab: 0x20
   __TEXT.__oslogstring: 0x5f
   __TEXT.__unwind_info: 0x55c
   __TEXT.__objc_classname: 0x4b1
-  __TEXT.__objc_methname: 0x2b69
+  __TEXT.__objc_methname: 0x2bcd
   __TEXT.__objc_methtype: 0x5d2
   __TEXT.__objc_stubs: 0x7c0
   __DATA_CONST.__got: 0x50

   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x7b0
-  __DATA_CONST.__objc_selrefs: 0xee0
+  __DATA_CONST.__objc_selrefs: 0xf00
+  __DATA_CONST.__objc_classrefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__cfstring: 0x7a0

   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0x648
-  __DATA.__objc_classrefs: 0x58
-  __DATA.__objc_superrefs: 0x28
   __DATA.__objc_ivar: 0x6c
-  __DATA.__data: 0x1720
+  __DATA.__data: 0x1740
   __DATA_DIRTY.__objc_const: 0x368
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 571
-  Symbols:   1592
-  CStrings:  954
+  Functions: 575
+  Symbols:   1600
+  CStrings:  960
 
Symbols:
+ -[HIDEvent(HIDGameControllerEventPrivate) gameControllerButtonM1]
+ -[HIDEvent(HIDGameControllerEventPrivate) gameControllerButtonM2]
+ -[HIDEvent(HIDGameControllerEventPrivate) gameControllerButtonM3]
+ -[HIDEvent(HIDGameControllerEventPrivate) gameControllerButtonM4]
+ -[HIDEvent(HIDGameControllerEventPrivate) setGameControllerButtonM1:]
+ -[HIDEvent(HIDGameControllerEventPrivate) setGameControllerButtonM2:]
+ -[HIDEvent(HIDGameControllerEventPrivate) setGameControllerButtonM3:]
+ -[HIDEvent(HIDGameControllerEventPrivate) setGameControllerButtonM4:]
- -[HIDEvent(HIDGameControllerEventPrivate) gameControllerButtonL5]
- -[HIDEvent(HIDGameControllerEventPrivate) gameControllerButtonR5]
- -[HIDEvent(HIDGameControllerEventPrivate) setGameControllerButtonL5:]
- -[HIDEvent(HIDGameControllerEventPrivate) setGameControllerButtonR5:]
CStrings:
+ "gameControllerButtonM1"
+ "gameControllerButtonM2"
+ "gameControllerButtonM3"
+ "gameControllerButtonM4"
+ "setGameControllerButtonM1:"
+ "setGameControllerButtonM2:"
+ "setGameControllerButtonM3:"
+ "setGameControllerButtonM4:"
- "gameControllerButtonL5"
- "gameControllerButtonR5"
- "setGameControllerButtonL5:"
- "setGameControllerButtonR5:"

```
