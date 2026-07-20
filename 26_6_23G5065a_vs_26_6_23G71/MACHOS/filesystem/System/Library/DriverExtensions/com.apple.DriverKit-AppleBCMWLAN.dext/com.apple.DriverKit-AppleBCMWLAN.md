## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__cstring`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

 1558.1.0.0.0
-  __TEXT.__text: 0x284370
+  __TEXT.__text: 0x284340
   __TEXT.__auth_stubs: 0x24b0
   __TEXT.__init_offsets: 0x1bc
   __TEXT.__cstring: 0x80ba8
   __TEXT.__const: 0x7eb38
   __TEXT.__oslogstring: 0x1f3b
-  __TEXT.__unwind_info: 0x5e60
+  __TEXT.__unwind_info: 0x5e58
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x1258
   __DATA_CONST.__got: 0x108
Functions:
~ __ZN27AppleBCMWLANChipManagerPCIe21isSafeToCaptureSoCRAMEv : 60 -> 4
~ __Z41AppleBCMWLAN_isVerboseDebugLoggingAllowedv : 80 -> 84
~ __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv -> __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv : 80 -> 96
~ __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv -> __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv : 96 -> 84
CStrings:
+ "Jul 11 2026 15:24:09"
- "Jul  9 2026 23:28:52"
```
