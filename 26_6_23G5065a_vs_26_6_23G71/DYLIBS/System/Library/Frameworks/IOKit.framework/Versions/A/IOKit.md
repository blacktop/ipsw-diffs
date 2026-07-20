## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

 100231.120.3.0.0
-  __TEXT.__text: 0xa273c
+  __TEXT.__text: 0xa27f4
   __TEXT.__auth_stubs: 0x2130
   __TEXT.__objc_methlist: 0x150
   __TEXT.__const: 0x104a4
   __TEXT.__oslogstring: 0x5302
-  __TEXT.__cstring: 0xbc56
+  __TEXT.__cstring: 0xbca3
   __TEXT.__unwind_info: 0x21b0
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methname: 0xa3

   - /usr/lib/libz.1.dylib
   Functions: 3533
   Symbols:   3949
-  CStrings:  2574
+  CStrings:  2580
 
Functions:
~ ___IOHIDEventTypeDescriptorAmbientLightSensor : 256 -> 440
CStrings:
+ "ColorComponent0:"
+ "ColorComponent1:"
+ "ColorComponent2:"
+ "ColorSpace:"
+ "OSKEXT_BUILD_DATE 15:23:06 Jul 11 2026"
+ "Undefined"
+ "XYZ"
- "OSKEXT_BUILD_DATE 00:01:49 Jul  3 2026"
```
