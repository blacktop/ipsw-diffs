## mobile_diagnostics_relay

> `/usr/libexec/mobile_diagnostics_relay`

```diff

-47.0.0.0.0
-  __TEXT.__text: 0x12b5c
+49.0.0.0.0
+  __TEXT.__text: 0x12748
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_stubs: 0x1720
-  __TEXT.__objc_methlist: 0xa94
-  __TEXT.__gcc_except_tab: 0x5ac
-  __TEXT.__objc_methname: 0x1b80
-  __TEXT.__cstring: 0x35e7
+  __TEXT.__objc_stubs: 0x1740
+  __TEXT.__objc_methlist: 0xa84
+  __TEXT.__gcc_except_tab: 0x4e0
+  __TEXT.__objc_methname: 0x1b88
+  __TEXT.__cstring: 0x35c2
   __TEXT.__objc_classname: 0x137
   __TEXT.__objc_methtype: 0x893
-  __TEXT.__const: 0x48
+  __TEXT.__const: 0x40
   __TEXT.__oslogstring: 0x22
   __TEXT.__ustring: 0x1b0
-  __TEXT.__unwind_info: 0x478
+  __TEXT.__unwind_info: 0x468
   __DATA_CONST.__auth_got: 0x650
-  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x660
   __DATA_CONST.__cfstring: 0x27a0
   __DATA_CONST.__objc_classlist: 0x58

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4F6FB9AC-4DC1-387E-A980-65EA056D3C74
-  Functions: 305
-  Symbols:   272
-  CStrings:  1175
+  UUID: 9523B449-1101-3C73-96DA-9BCB4B7986F7
+  Functions: 303
+  Symbols:   269
+  CStrings:  1174
 
Symbols:
+ _NSFileProtectionNone
- _CHHapticEventParameterIDAudioPitch
- _CHHapticEventParameterIDAudioVolume
- _CHHapticEventTypeAudioContinuous
- _NSFileProtectionCompleteUnlessOpen
CStrings:
+ "CHHapticEngine reset"
+ "stopWithCompletionHandler:"
- "-[HapticPlayer playAudioForTimes:]"
- "Audio times should > 0"
- "playAudioForTimes:"

```
