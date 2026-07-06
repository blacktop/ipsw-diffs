## KeyboardBacklightServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/KeyboardBacklightServiceFilter.plugin/Contents/MacOS/KeyboardBacklightServiceFilter`

```diff

-  __TEXT.__text: 0xa8e0
+  __TEXT.__text: 0xb1f0
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x12e0
-  __TEXT.__objc_methlist: 0xad4
-  __TEXT.__const: 0x318
+  __TEXT.__objc_stubs: 0x1380
+  __TEXT.__objc_methlist: 0xafc
+  __TEXT.__const: 0x320
   __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__oslogstring: 0x114b
-  __TEXT.__objc_methname: 0x165c
+  __TEXT.__oslogstring: 0x1381
+  __TEXT.__objc_methname: 0x16c8
   __TEXT.__cstring: 0x60e
   __TEXT.__objc_classname: 0x17a
   __TEXT.__objc_methtype: 0x600
-  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__unwind_info: 0x2f8
   __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__cfstring: 0x860
   __DATA_CONST.__objc_classlist: 0x68

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__auth_got: 0x2f8
-  __DATA_CONST.__got: 0xa8
-  __DATA.__objc_const: 0x21c0
-  __DATA.__objc_selrefs: 0x658
-  __DATA.__objc_ivar: 0x114
+  __DATA_CONST.__got: 0xc0
+  __DATA.__objc_const: 0x21e0
+  __DATA.__objc_selrefs: 0x680
+  __DATA.__objc_ivar: 0x118
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x180
   __DATA.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 297
-  Symbols:   190
-  CStrings:  665
+  Functions: 307
+  Symbols:   191
+  CStrings:  681
 
Sections:
~ __TEXT.__objc_methtype : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _OBJC_CLASS_$_NSScanner
CStrings:
+ "Load hardware range: min=%llu, max=%llu"
+ "_loadHardwareRange"
+ "_loadHardwareRange: pwm-frequency still unavailable."
+ "_pwmFrequencyLoaded"
+ "_updateHardwareRangeWithClock:"
+ "_updateHardwareRangeWithClock: _frequency is 0, cannot compute hardware range"
+ "_updateHardwareRangeWithClock: period is 0 (clock=%llu, freq=%llu), cannot compute hardware range"
+ "boot Nits: %@ → %.2f%% → %.2f nits"
+ "boot Nits: failed to open IODeviceTree:/options"
+ "boot Nits: failed to parse hex value from NVRAM string: %@"
+ "boot Nits: no boot DC found in NVRAM"
+ "bootNits"
+ "enablePulseRoutine: device already enabled, skipping"
+ "initWithData:encoding:"
+ "initWithString:"
+ "pwm-frequency not yet available; using default clock %llu"
+ "scanHexInt:"
+ "useEnablePulse=YES; skipping initial setNits"
- "PWM min, max = %llu, %llu (period = %llu)"
- "unsignedLongLongValue"

```
