## SpatialHIDServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/SpatialHIDServiceFilter.plugin/Contents/MacOS/SpatialHIDServiceFilter`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-14.0.21.0.0
-  __TEXT.__text: 0x27c8
-  __TEXT.__auth_stubs: 0x290
+14.0.24.0.0
+  __TEXT.__text: 0x2b9c
+  __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_stubs: 0x540
-  __TEXT.__objc_methlist: 0x3d8
-  __TEXT.__const: 0x40
+  __TEXT.__objc_methlist: 0x3f0
+  __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x58
   __TEXT.__cstring: 0x112
-  __TEXT.__oslogstring: 0x91c
-  __TEXT.__objc_methname: 0x81a
+  __TEXT.__oslogstring: 0x92e
+  __TEXT.__objc_methname: 0x8d5
   __TEXT.__objc_classname: 0x6a
-  __TEXT.__objc_methtype: 0x796
-  __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__const: 0xd0
+  __TEXT.__objc_methtype: 0x7b8
+  __TEXT.__unwind_info: 0x118
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x158
-  __DATA_CONST.__got: 0x58
-  __DATA.__objc_const: 0x510
-  __DATA.__objc_selrefs: 0x2d0
-  __DATA.__objc_ivar: 0x44
+  __DATA_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x60
+  __DATA.__objc_const: 0x5f8
+  __DATA.__objc_selrefs: 0x2d8
+  __DATA.__objc_ivar: 0x60
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x180
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/HID.framework/Versions/A/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 77
-  Symbols:   64
-  CStrings:  233
+  Functions: 86
+  Symbols:   73
+  CStrings:  244
 
Symbols:
+ __dispatch_source_type_timer
+ _dispatch_assert_queue$V2
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _mach_absolute_time
+ _mach_timebase_info
CStrings:
+ "@\"NSObject<OS_dispatch_source>\""
+ "End Haptics"
+ "[%#llx] Commit continuous waveform failed: %@"
+ "[%#llx] End haptics failed: %@"
+ "_hapticActiveContinuousIntensity"
+ "_hapticActiveContinuousWaveform"
+ "_hapticPendingIntensity"
+ "_hapticPendingWaveform"
+ "_hapticPumpDirty"
+ "_hapticPumpTimer"
+ "_lastHapticCommitTime"
+ "_onqueue_pumpHaptic"
+ "endHaptics"
+ "q"
- "Stop Haptics"
- "[%#llx] Set haptic motor [%zu] (sequence=%llu) failed: %@"
- "stopHaptics"
```
