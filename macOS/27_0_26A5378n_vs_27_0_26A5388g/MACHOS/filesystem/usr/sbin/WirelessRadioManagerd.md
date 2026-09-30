## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-1786.16.0.0.0
-  __TEXT.__text: 0x95304
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_stubs: 0x14d60
-  __TEXT.__objc_methlist: 0xb5e4
+1786.17.0.0.0
+  __TEXT.__text: 0x953c4
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__objc_stubs: 0x14e40
+  __TEXT.__objc_methlist: 0xb62c
   __TEXT.__const: 0x2fd0
-  __TEXT.__objc_methname: 0x2592b
+  __TEXT.__objc_methname: 0x259f5
   __TEXT.__objc_classname: 0x7a3
-  __TEXT.__objc_methtype: 0x5678
-  __TEXT.__cstring: 0x3182f
+  __TEXT.__objc_methtype: 0x5667
+  __TEXT.__cstring: 0x318d3
   __TEXT.__gcc_except_tab: 0xd30
   __TEXT.__dlopen_cstrs: 0x43
   __TEXT.__oslogstring: 0xbd
-  __TEXT.__unwind_info: 0x1938
+  __TEXT.__unwind_info: 0x1930
   __DATA_CONST.__const: 0x2450
-  __DATA_CONST.__cfstring: 0x1ca40
+  __DATA_CONST.__cfstring: 0x1ca60
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x2e0
-  __DATA_CONST.__objc_arraydata: 0x1ee8
+  __DATA_CONST.__objc_arraydata: 0x1f08
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_intobj: 0x21d8
-  __DATA_CONST.__objc_arrayobj: 0x648
-  __DATA_CONST.__auth_got: 0x660
+  __DATA_CONST.__objc_arrayobj: 0x660
+  __DATA_CONST.__auth_got: 0x668
   __DATA_CONST.__got: 0x530
   __DATA.__objc_const: 0x11b58
-  __DATA.__objc_selrefs: 0x6e30
+  __DATA.__objc_selrefs: 0x6e68
   __DATA.__objc_ivar: 0x14b0
   __DATA.__objc_data: 0x19a0
   __DATA.__data: 0x2f8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3986
-  Symbols:   355
-  CStrings:  10514
+  Functions: 3992
+  Symbols:   356
+  CStrings:  10521
 
Symbols:
+ _notify_cancel
CStrings:
+ "BTCS_ %s B40B (UL>2370): blocking BT channels 0-19"
+ "BTCS_ %s B7: blocking BT channels 0-19"
+ "LTEWiFiTimeSharingBand41Ch1013"
+ "WCM_Session Stewie test inject ignored (STEWIE/SKIPPER feature not compiled)"
+ "invalidateDiscoveryAndDeviceManager"
+ "sendBBCoexP2PSensorState: AWDL state: 0x%x, NAN state: 0x%x, combined P2P state changed: (0x%x -> 0x%x), update to BB"
+ "sendBBCoexP2PSensorState: AWDL state: 0x%x, NAN state: 0x%x, combined P2P state: 0x%x, no change in state. Skip the update to BB"
+ "sendBBCoexP2PSensorState:state:"
+ "updateCoexRxGainMode:force:"
+ "updateEpaDisallowed:force:"
+ "updatePreferredAFHMap:force:"
+ "updatePreferredBTCSAFHMap:force:"
+ "updatePreferredHFBTChannelMap:force:"
+ "updateWCI2Mode:force:"
- "BTCS_ %s B20: no BT channel masking"
- "BTCS_ %s B40B (UL>2370): blocking BT channels 0-29"
- "BTCS_ %s B7: no BT channel masking"
- "sendBBCoexP2PSensorState: AWDL state: 0x%x, NAN state: 0x%x, combined P2P state: 0x%x"
- "sendBBCoexP2PSensorState: WiFi Reset/PowerOn event, reset AWDL/NAN state"
- "sendBBCoexP2PSensorState:state:WiFiReset:"
- "v28@0:8I16I20B24"
```
