## GenericHID

> `/System/Library/ScreenReader/BrailleDrivers/GenericHID.brailledriver/GenericHID`

```diff

-424.4.8.0.0
-  __TEXT.__text: 0x4074
+424.4.11.0.0
+  __TEXT.__text: 0x42a8
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x574
+  __TEXT.__objc_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x58c
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x1fb
-  __TEXT.__objc_classname: 0x8f
-  __TEXT.__objc_methname: 0xb7a
-  __TEXT.__objc_methtype: 0x2ac
-  __TEXT.__oslogstring: 0x421
+  __TEXT.__cstring: 0x1fc
+  __TEXT.__objc_classname: 0x90
+  __TEXT.__objc_methname: 0xbfc
+  __TEXT.__objc_methtype: 0x2b8
+  __TEXT.__oslogstring: 0x4f7
   __TEXT.__unwind_info: 0x108
   __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x110
-  __DATA_CONST.__cfstring: 0x1a0
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x250
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x108
-  __DATA.__objc_const: 0x840
-  __DATA.__objc_selrefs: 0x430
-  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_const: 0x870
+  __DATA.__objc_selrefs: 0x448
+  __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1f0
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6562C66F-83A4-3B4D-B86F-2BBA1DD078A1
-  Functions: 70
+  UUID: 9D79EF23-9D24-3D4C-AA7F-434B7460CA8C
+  Functions: 72
   Symbols:   97
-  CStrings:  283
+  CStrings:  293
 
CStrings:
+ ""
+ "@\"NSNumber\""
+ "Enqueued braille input event (total pending: %lu)"
+ "Failed to send braille output to device (result: 0x%x)"
+ "Received HID input callback - usagePage: 0x%x, usage: 0x%x"
+ "Registered HID input value callback for braille device"
+ "Returning %lu braille input events to caller"
+ "Sent screen reader identifier to braille device (result: %d)"
+ "T@\"NSNumber\",&,N,V_shouldForceLinearOutput"
+ "_shouldForceLinearOutput"
+ "boolValue"
+ "setShouldForceLinearOutput:"
+ "shouldForceLinearOutput"
- "Failed to set value for display cell element (result %@)"
- "Reported back screen reader: %@"
- "value callback: %d %d"

```
