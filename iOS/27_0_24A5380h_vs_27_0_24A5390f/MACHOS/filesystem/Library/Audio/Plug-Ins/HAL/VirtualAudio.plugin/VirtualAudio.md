## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__dof_VirtualAu`
- `__TEXT.__dof_Aggregate`
- `__TEXT.__dof_VirtualA0`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__common`

```diff

-1450.0.0.0.0
-  __TEXT.__text: 0x52de7c
+1451.108.1.0.0
+  __TEXT.__text: 0x52efb8
   __TEXT.__realtime: 0x145e4
   __TEXT.__auth_stubs: 0x2890
   __TEXT.__objc_stubs: 0xfa0
   __TEXT.__init_offsets: 0x102c
   __TEXT.__objc_methlist: 0x2c0
-  __TEXT.__const: 0xb1410
-  __TEXT.__cstring: 0x36bec
-  __TEXT.__gcc_except_tab: 0x5f704
+  __TEXT.__const: 0xb13e0
+  __TEXT.__cstring: 0x36be6
+  __TEXT.__gcc_except_tab: 0x5f834
   __TEXT.__swift5_typeref: 0x12b
   __TEXT.__swift5_capture: 0x168
-  __TEXT.__oslogstring: 0x55de4
+  __TEXT.__oslogstring: 0x56013
   __TEXT.__objc_methname: 0xdad
   __TEXT.__objc_classname: 0x9d
   __TEXT.__objc_methtype: 0x422

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x14500
+  __TEXT.__unwind_info: 0x14520
   __TEXT.__eh_frame: 0x730
   __DATA_CONST.__const: 0x294c8
   __DATA_CONST.__cfstring: 0x2f60

   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0x2b8
   __DATA.__data: 0x5b0
-  __DATA.__bss: 0x25648
+  __DATA.__bss: 0x25678
   __DATA.__common: 0x18
   - /AppleInternal/Library/Frameworks/AudioCapture.framework/AudioCapture
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12357
+  Functions: 12360
   Symbols:   804
-  CStrings:  12076
+  CStrings:  12081
 
CStrings:
+ "%25s:%-5d - Forcing Change for %s: cached route references a removed port."
+ "%25s:%-5d Bluetooth device %u: skip %s at publish (VA will drive HW volume on this device at the current PME state)"
+ "%25s:%-5d Clamped input volume control maximum to %f for call certification."
+ "%25s:%-5d LP+HP mic coexistence barred: forcing %s onto the codec HP mic (another VAD holds it; product lacks supports-concurrent-hp-lp-mics)."
+ "%25s:%-5d creating a Puffin input port with name \"%s\" and UID \"%s\""
+ "@@ Strips Jul 13 2026 21:40:16"
+ "Concurrent LP and HP built-in mic on a product lacking supports-concurrent-hp-lp-mics — LP mic VAD(s): %{public}s; HP mic VAD(s): %{public}s. One capture path will be silenced."
- "%25s:%-5d Bluetooth device %u: skip %s at publish (VA policy will drive HW volume on this device)"
- "@@ Strips Jun 27 2026 22:18:31"
```
