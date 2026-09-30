## AGXGPURawCounterBundle

> `/System/Library/Extensions/AGXGPURawCounterBundle.bundle/Contents/MacOS/AGXGPURawCounterBundle`

```diff

-324.6.0.0.0
-  __TEXT.__text: 0x23f0
+325.34.1.0.0
+  __TEXT.__text: 0x23d0
   __TEXT.__auth_stubs: 0x120
   __TEXT.__objc_methlist: 0x1d0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x363
   __TEXT.__oslogstring: 0x4d
-  __TEXT.__unwind_info: 0xb0
+  __TEXT.__unwind_info: 0xa8
   __TEXT.__objc_classname: 0x49
   __TEXT.__objc_methname: 0x717
   __TEXT.__objc_methtype: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A4381AE0-E1CF-3477-9633-D4DBD25B8FC1
+  UUID: 080FA393-757E-3DEB-BBAA-70B80BD820EC
   Functions: 36
   Symbols:   160
   CStrings:  183
Functions:
~ -[AGXGPURawCounterSource pollCountersAtBufferIndex:withBlock:] : 1084 -> 1080
~ -[AGXGPURawCounterSource requestTriggers:firstErrorIndex:] : 628 -> 624
~ -[AGXGPURawCounterSource setEnabled:] : 124 -> 116
~ -[AGXGPURawCounterSource initWithSourceGroup:impl:] : 1188 -> 1192
~ -[AGXGPURawCounterSourceGroup subDivideCounterList:withOptions:] : 1744 -> 1736
~ -[AGXGPURawCounterSourceGroup initWithAcceleratorPort:] : 1628 -> 1616

```
