## ContinuousRecordingsDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ContinuousRecordingsDiagnosticExtension.appex/ContinuousRecordingsDiagnosticExtension`

```diff

-9150.2.0.0.0
-  __TEXT.__text: 0x820
-  __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_stubs: 0x280
-  __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x174
-  __TEXT.__oslogstring: 0xf6
+9170.34.1.0.0
+  __TEXT.__text: 0x964
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__objc_stubs: 0x300
+  __TEXT.__objc_methlist: 0x50
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x192
+  __TEXT.__oslogstring: 0x191
   __TEXT.__objc_classname: 0x28
-  __TEXT.__objc_methname: 0x250
-  __TEXT.__objc_methtype: 0x1b
+  __TEXT.__objc_methname: 0x28d
+  __TEXT.__objc_methtype: 0x23
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x118
-  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0xc0
+  __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_arraydata: 0x50
+  __DATA_CONST.__objc_dictobj: 0x50
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0x58
   __DATA.__objc_const: 0xa8
-  __DATA.__objc_selrefs: 0xa8
+  __DATA.__objc_selrefs: 0xc8
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
+  - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4FDF668C-B5B0-3FFF-B6C8-3F8AACD61F94
-  Functions: 9
-  Symbols:   95
-  CStrings:  49
+  UUID: A2200ABC-5D4F-30B2-8F15-A674FA00182E
+  Functions: 12
+  Symbols:   108
+  CStrings:  62
 
Symbols:
+ -[ContinuousRecordingsDiagnosticExtension countActiveRecordingDevices]
+ -[ContinuousRecordingsDiagnosticExtension countActiveRecordingDevices].cold.1
+ _OBJC_CLASS_$_HIDManager
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OUTLINED_FUNCTION_0
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$count
+ _objc_msgSend$countActiveRecordingDevices
+ _objc_msgSend$devices
+ _objc_msgSend$setDeviceMatching:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x23
CStrings:
+ "DeviceUsage"
+ "DeviceUsagePage"
+ "Failed to create HIDManager for device matching"
+ "Found %lu active recording device(s)"
+ "No active recording devices found, skipping force flush"
+ "Q16@0:8"
+ "Sending force flush command to %lu HID continuous recording device(s)"
+ "Successfully force flushed %lu HID continuous recording device(s)"
+ "Timed out waiting for force flush from all HID continuous recording device(s)"
+ "count"
+ "countActiveRecordingDevices"
+ "devices"
+ "i"
+ "setDeviceMatching:"
- "Failed to force flush HID continuous recording session filter"
- "Sending force flush command to HID continuous recording session filter"
- "Successfully force flushed HID continuous recording session filter"

```
