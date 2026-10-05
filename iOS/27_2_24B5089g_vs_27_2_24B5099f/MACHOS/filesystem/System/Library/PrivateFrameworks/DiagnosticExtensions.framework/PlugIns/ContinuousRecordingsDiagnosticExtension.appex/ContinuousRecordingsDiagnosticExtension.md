## ContinuousRecordingsDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ContinuousRecordingsDiagnosticExtension.appex/ContinuousRecordingsDiagnosticExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-10100.44.0.0.0
-  __TEXT.__text: 0x930
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_stubs: 0x300
-  __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x192
-  __TEXT.__oslogstring: 0x191
+10110.3.0.0.0
+  __TEXT.__text: 0xc1c
+  __TEXT.__auth_stubs: 0x260
+  __TEXT.__objc_stubs: 0x360
+  __TEXT.__objc_methlist: 0x5c
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x1e1
+  __TEXT.__oslogstring: 0x234
   __TEXT.__objc_classname: 0x28
-  __TEXT.__objc_methname: 0x28d
-  __TEXT.__objc_methtype: 0x23
+  __TEXT.__objc_methname: 0x2be
+  __TEXT.__objc_methtype: 0x2e
   __TEXT.__unwind_info: 0x90
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__auth_got: 0x138
+  __DATA_CONST.__got: 0x68
   __DATA.__objc_const: 0xa8
-  __DATA.__objc_selrefs: 0xc8
+  __DATA.__objc_selrefs: 0xe0
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 12
-  Symbols:   104
-  CStrings:  54
+  Functions: 13
+  Symbols:   112
+  CStrings:  66
 
Symbols:
+ -[ContinuousRecordingsDiagnosticExtension expectedForceFlushFinishedCount]
+ -[ContinuousRecordingsDiagnosticExtension getVersion:]
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSNumber
+ _objc_msgSend$expectedForceFlushFinishedCount
+ _objc_msgSend$getVersion:
+ _objc_msgSend$propertyForKey:
+ _objc_msgSend$unsignedIntValue
+ _objc_opt_isKindOfClass
+ _objc_release_x26
- -[ContinuousRecordingsDiagnosticExtension countActiveRecordingDevices]
- _objc_msgSend$countActiveRecordingDevices
CStrings:
+ "%@ continuous recording version %u is managed by %s"
+ "ContinuousRecordingVersion"
+ "DefaultProperties"
+ "Found %lu recording device(s): %lu legacy, HCR 2.0 daemon %s; expecting %lu force flush finished notification(s)"
+ "HCR 2.0"
+ "I24@0:8@16"
+ "No DefaultProperties for %@"
+ "Sending force flush command, expecting %lu force flush finished notification(s)"
+ "Successfully received %lu force flush finished notification(s)"
+ "absent"
+ "expectedForceFlushFinishedCount"
+ "getVersion:"
+ "legacy HCR"
+ "present"
+ "propertyForKey:"
+ "unsignedIntValue"
- "Found %lu active recording device(s)"
- "Sending force flush command to %lu HID continuous recording device(s)"
- "Successfully force flushed %lu HID continuous recording device(s)"
- "countActiveRecordingDevices"
```
