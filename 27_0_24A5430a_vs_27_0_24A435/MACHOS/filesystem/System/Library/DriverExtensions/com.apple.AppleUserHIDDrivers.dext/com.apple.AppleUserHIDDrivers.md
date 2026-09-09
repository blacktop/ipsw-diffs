## com.apple.AppleUserHIDDrivers

> `/System/Library/DriverExtensions/com.apple.AppleUserHIDDrivers.dext/com.apple.AppleUserHIDDrivers`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

   __TEXT.__const: 0x2b0
   __TEXT.__oslogstring: 0x345
   __TEXT.__cstring: 0x2a3
-  __DATA_CONST.__const: 0x910
+  __DATA_CONST.__const: 0x930
   __DATA_CONST.__osclassinfo: 0x10
   __DATA_CONST.__auth_got: 0x140
   __DATA_CONST.__got: 0x48

   - /System/DriverKit/System/Library/Frameworks/USBDriverKit.framework/USBDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
   Functions: 62
-  Symbols:   217
+  Symbols:   221
   CStrings:  35
 
Symbols:
+ __ZN24AppleUserHIDEventService22handleHingeAngleReportEyj
+ __ZN24AppleUserHIDEventService22parseHingeAngleElementEP12IOHIDElement
+ __ZThn96_N24AppleUserHIDEventService22handleHingeAngleReportEyj
+ __ZThn96_N24AppleUserHIDEventService22parseHingeAngleElementEP12IOHIDElement
```
