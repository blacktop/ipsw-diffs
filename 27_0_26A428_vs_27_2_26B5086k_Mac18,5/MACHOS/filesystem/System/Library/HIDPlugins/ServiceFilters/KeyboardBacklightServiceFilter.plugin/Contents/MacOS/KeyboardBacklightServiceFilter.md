## KeyboardBacklightServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/KeyboardBacklightServiceFilter.plugin/Contents/MacOS/KeyboardBacklightServiceFilter`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2300.1.2.0.0
-  __TEXT.__text: 0xb03c
+2300.40.37.0.0
+  __TEXT.__text: 0xb8b8
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x1380
-  __TEXT.__objc_methlist: 0xafc
+  __TEXT.__objc_stubs: 0x14c0
+  __TEXT.__objc_methlist: 0xb44
   __TEXT.__const: 0x320
-  __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__oslogstring: 0x1381
-  __TEXT.__objc_methname: 0x16c8
-  __TEXT.__cstring: 0x60e
+  __TEXT.__gcc_except_tab: 0x238
+  __TEXT.__oslogstring: 0x137b
+  __TEXT.__objc_methname: 0x17fd
+  __TEXT.__cstring: 0x63a
   __TEXT.__objc_classname: 0x17a
-  __TEXT.__objc_methtype: 0x600
-  __TEXT.__unwind_info: 0x438
+  __TEXT.__objc_methtype: 0x645
+  __TEXT.__unwind_info: 0x480
   __DATA_CONST.__const: 0x1c0
-  __DATA_CONST.__cfstring: 0x860
+  __DATA_CONST.__cfstring: 0x880
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x2f8
-  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_got: 0x300
+  __DATA_CONST.__got: 0xc8
   __DATA.__objc_const: 0x21e0
-  __DATA.__objc_selrefs: 0x680
+  __DATA.__objc_selrefs: 0x6d8
   __DATA.__objc_ivar: 0x118
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 307
-  Symbols:   191
-  CStrings:  609
+  Functions: 316
+  Symbols:   197
+  CStrings:  625
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ ___gxx_personality_v0
+ _interpolate_value_in_table
+ _load_mapping_table_from_defaults
+ _mapping_table_is_valid
+ _save_mapping_table_to_defaults
CStrings:
+ "B28@0:8B16B20B24"
+ "Enabling device without enable pulse"
+ "_setNits:withFadeSpeed:minPWMPercentage:completion:"
+ "arrayForKey:"
+ "com.apple.CoreBrightness.BacklightDriverPWM"
+ "convertNitsToPWMPercentage:minPWMPercentage:"
+ "f24@0:8f16f20"
+ "floatValue"
+ "initWithBacklightService:configuration:"
+ "initWithConfiguration:"
+ "initWithSuiteName:"
+ "setEnabled:commit:applyEnablePulse:"
+ "setNits:withFadeSpeed:minPWMPercentage:"
+ "setObject:forKey:"
+ "synchronize"
+ "v28@0:8f16S20f24"
+ "v36@0:8f16S20f24@?28"
- "Can't talk to PWM driver. Return code = %d"
```
