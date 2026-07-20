## AXHapticMusicServer

> `/System/Library/AccessibilityBundles/AXHapticMusicServer.axuiservice/AXHapticMusicServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3234.5.0.0.0
-  __TEXT.__text: 0x2b6c8
-  __TEXT.__auth_stubs: 0x10e0
+3237.1.0.0.0
+  __TEXT.__text: 0x2bccc
+  __TEXT.__auth_stubs: 0x10f0
   __TEXT.__objc_stubs: 0xb20
   __TEXT.__objc_methlist: 0x3fc
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__const: 0xb30
-  __TEXT.__cstring: 0x5cb
+  __TEXT.__cstring: 0x5eb
   __TEXT.__swift5_typeref: 0x625
-  __TEXT.__oslogstring: 0x1368
-  __TEXT.__swift5_capture: 0x718
+  __TEXT.__oslogstring: 0x1398
+  __TEXT.__swift5_capture: 0x728
   __TEXT.__objc_methtype: 0x5a5
   __TEXT.__objc_methname: 0x14cd
   __TEXT.__objc_classname: 0xef

   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x54
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0x5e0
+  __TEXT.__unwind_info: 0x5f0
   __TEXT.__eh_frame: 0x530
-  __DATA_CONST.__const: 0x1ae0
+  __DATA_CONST.__const: 0x1b30
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__auth_got: 0x880
-  __DATA_CONST.__got: 0x2d8
+  __DATA_CONST.__auth_got: 0x888
+  __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__auth_ptr: 0x180
   __DATA.__objc_const: 0x970
   __DATA.__objc_selrefs: 0x490

   __DATA.__bss: 0xdc0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
+  - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreHaptics.framework/CoreHaptics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 647
-  Symbols:   267
-  CStrings:  419
+  Functions: 654
+  Symbols:   269
+  CStrings:  421
 
Symbols:
+ _AXApplicationAccessibilityEnabled
+ _kAXSHapticMusicPreferenceDidChangeNotification
CStrings:
+ "Haptic Music enabled state changed to: %{bool}d"
+ "haptic music enabled change"
```
