## powerexperienced

> `/usr/libexec/powerexperienced`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-180.0.0.0.0
-  __TEXT.__text: 0x1b650
+182.0.0.0.0
+  __TEXT.__text: 0x1b6c0
   __TEXT.__auth_stubs: 0x6c0
   __TEXT.__objc_stubs: 0x3c00
   __TEXT.__objc_methlist: 0x259c
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x1375
+  __TEXT.__cstring: 0x137f
   __TEXT.__objc_methname: 0x443b
-  __TEXT.__oslogstring: 0x3356
+  __TEXT.__oslogstring: 0x3364
   __TEXT.__objc_classname: 0x442
   __TEXT.__objc_methtype: 0x8d3
   __TEXT.__gcc_except_tab: 0x4c
   __TEXT.__unwind_info: 0x9e8
   __DATA_CONST.__const: 0x900
-  __DATA_CONST.__cfstring: 0x1440
+  __DATA_CONST.__cfstring: 0x1460
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 878
   Symbols:   171
-  CStrings:  1484
+  CStrings:  1485
 
Functions:
~ sub_100002a50 : 2080 -> 2192
CStrings:
+ "AssistantMode changing from %@ to %@ (siriRemoteSession=%d, siriLocalSession=%d, assistantUI=%d, nanoSiriX=%d)"
+ "NanoSiriX"
+ "evaluatePowerMode: %@: %d display %d, carPlaySession %d, nFCSession %d, audioSession %d, sleepInProgress %d, wakeInProgress %d, onenessSession %d, siriAudio %d, siriRemoteSession %d, siriLocalSession %d, assistantUI %d, nanoSiriX %d, fitnessIntelligence %d, dataMigrationInProgress %d, dischargeInProgress %d, usbDeviceMode %d, pluggedIn %d (allowOnCharger: %d)"
- "AssistantMode changing from %@ to %@ (siriRemoteSession=%d, siriLocalSession=%d, assistantUI=%d, siriAudio=%d)"
- "evaluatePowerMode: %@: %d display %d, carPlaySession %d, nFCSession %d, audioSession %d, sleepInProgress %d, wakeInProgress %d, onenessSession %d, siriAudio %d, siriRemoteSession %d, siriLocalSession %d, assistantUI %d, fitnessIntelligence %d, dataMigrationInProgress %d, dischargeInProgress %d, usbDeviceMode %d, pluggedIn %d (allowOnCharger: %d)"
```
