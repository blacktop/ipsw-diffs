## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__auth_got`
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
-  __TEXT.__text: 0xbba04
+  __TEXT.__text: 0xbbabc
   __TEXT.__auth_stubs: 0x2370
   __TEXT.__objc_methlist: 0x150
-  __TEXT.__cstring: 0xf0e0
+  __TEXT.__cstring: 0xf12d
   __TEXT.__const: 0x10608
   __TEXT.__dlopen_cstrs: 0x57
   __TEXT.__oslogstring: 0x5321

   - /usr/lib/system/libkxld.dylib
   Functions: 3854
   Symbols:   4628
-  CStrings:  2976
+  CStrings:  2982
 
Functions:
~ ___IOHIDEventTypeDescriptorAmbientLightSensor : 256 -> 440
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RkW0aw/Sources/IOAVFamily_user/IOAV.cpp"
+ "ColorComponent0:"
+ "ColorComponent1:"
+ "ColorComponent2:"
+ "ColorSpace:"
+ "OSKEXT_BUILD_DATE 15:10:29 Jul 11 2026"
+ "Undefined"
+ "XYZ"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.s62cQM/Sources/IOAVFamily_user/IOAV.cpp"
- "OSKEXT_BUILD_DATE 01:50:08 Jun 17 2026"
```
