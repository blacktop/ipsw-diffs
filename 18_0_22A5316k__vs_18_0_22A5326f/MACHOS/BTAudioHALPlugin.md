## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

```diff

-180.55.1.0.0
-  __TEXT.__text: 0x6780c
+180.60.1.0.0
+  __TEXT.__text: 0x67ba0
   __TEXT.__auth_stubs: 0x1130
-  __TEXT.__objc_stubs: 0x1900
+  __TEXT.__objc_stubs: 0x1920
   __TEXT.__init_offsets: 0x98
   __TEXT.__objc_methlist: 0x8f8
   __TEXT.__gcc_except_tab: 0x1ac0
-  __TEXT.__const: 0x172c
-  __TEXT.__cstring: 0x3ec7
-  __TEXT.__oslogstring: 0x1025a
+  __TEXT.__const: 0x173c
+  __TEXT.__cstring: 0x3ef6
+  __TEXT.__oslogstring: 0x10357
   __TEXT.__objc_classname: 0x130
-  __TEXT.__objc_methname: 0x2b73
+  __TEXT.__objc_methname: 0x2b84
   __TEXT.__objc_methtype: 0x1199
-  __TEXT.__unwind_info: 0x1748
+  __TEXT.__unwind_info: 0x1758
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__auth_got: 0x8a8
-  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__got: 0x2a0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x39a0
-  __DATA_CONST.__cfstring: 0x1000
+  __DATA_CONST.__cfstring: 0x1060
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x1dd0
-  __DATA.__objc_selrefs: 0x7f0
+  __DATA.__objc_selrefs: 0x7f8
   __DATA.__objc_ivar: 0xf8
   __DATA.__objc_data: 0x320
   __DATA.__data: 0xb08
-  __DATA.__bss: 0xae20
+  __DATA.__bss: 0xae30
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 2197
-  Symbols:   434
-  CStrings:  2186
+  Functions: 2200
+  Symbols:   435
+  CStrings:  2194
 
Symbols:
+ _kMXSystemControllerNotificationKey_SystemVolumeDidChange_Reason
CStrings:
+ "Dropping Volume update becuase there is one already in flight %!{(MISSING)public}@: manualVolumeUpdate: %!@(MISSING) Adaptive Volume: %!@(MISSING)"
+ "ExplicitVolumeChange"
+ "HFPStereo no HFPStereo pending, pendingConfig %!u(MISSING), currentCodec %!u(MISSING)"
+ "HFPstereo SetDefaultHfpStereoFormat skipped"
+ "Not-Supported"
+ "Route changing in while eSCO is active, transport %!s(MISSING)"
+ "Route changing update OoB link, transport %!s(MISSING)"
+ "active"
+ "getPropertyData: not enough space for the return value of kBluetoothAudioDevicePropertyStereoHFPAllowed"
+ "idle"
+ "isEqualToNumber:"
- "Dropping Volume update becuase there is one already in flight %!{(MISSING)public}@: %!@(MISSING))"
- "HFPStereo no HFPStereo pending, pendingConfig %!u(MISSING), codec %!u(MISSING)"
- "Route changing in while eSCO is active"

```
