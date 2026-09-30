## wifid

> `/usr/sbin/wifid`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 2027.32.0.0.0
-  __TEXT.__text: 0x1c38bc
+  __TEXT.__text: 0x1c3d90
   __TEXT.__auth_stubs: 0x2bf0
-  __TEXT.__objc_stubs: 0x14fc0
+  __TEXT.__objc_stubs: 0x15040
   __TEXT.__objc_methlist: 0x68b0
   __TEXT.__gcc_except_tab: 0x29b8
-  __TEXT.__const: 0xe5b
-  __TEXT.__cstring: 0x75aae
-  __TEXT.__objc_methname: 0x1b3bb
+  __TEXT.__const: 0xe6b
+  __TEXT.__cstring: 0x75c31
+  __TEXT.__objc_methname: 0x1b3fd
   __TEXT.__objc_classname: 0x85e
   __TEXT.__objc_methtype: 0x33ac
   __TEXT.__dlopen_cstrs: 0x33c
   __TEXT.__oslogstring: 0x27ef
   __TEXT.__ustring: 0x63e
-  __TEXT.__unwind_info: 0x45a8
-  __DATA_CONST.__const: 0x7c28
-  __DATA_CONST.__cfstring: 0x1c8e0
+  __TEXT.__unwind_info: 0x45b0
+  __DATA_CONST.__const: 0x7c48
+  __DATA_CONST.__cfstring: 0x1c920
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc8

   __DATA_CONST.__got: 0x1400
   __DATA_CONST.__auth_ptr: 0x160
   __DATA.__objc_const: 0xd480
-  __DATA.__objc_selrefs: 0x6398
+  __DATA.__objc_selrefs: 0x63b8
   __DATA.__objc_ivar: 0xa28
   __DATA.__objc_data: 0x1400
   __DATA.__data: 0x1130
-  __DATA.__common: 0x60
+  __DATA.__common: 0x68
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 8810
+  Functions: 8814
   Symbols:   1348
-  CStrings:  17360
+  CStrings:  17375
 
Symbols:
+ _OBJC_CLASS_$_CMAngleManager
- _kWAMessageKeyPrivateMacHomeNetwork
CStrings:
+ "%s: AB mode state updated to stateA"
+ "%s: AB mode state updated to stateB"
+ "%s: AB mode state updated to unknown"
+ "%s: WiFiManager Device AB mode callback initialization failed"
+ "%s: WiFiManager Device AB mode callback initialized"
+ "WiFiDeviceManagerSetDeviceABModeState"
+ "WiFiManager-2027.32 Aug 27 2026 20:53:32"
+ "WiFiManager-2027.32 Aug 27 2026 20:54:22"
+ "WiFiManagerScheduleWithQueue_block_invoke_18"
+ "WiFiManagerScheduleWithQueue_block_invoke_19"
+ "__WiFiManagerDeviceABModeStateChangeCallback"
+ "iPad12,1"
+ "iPad12,2"
+ "isAngleValid"
+ "isAvailable"
+ "setUnderlyingQueue:"
+ "startAngleUpdatesToQueue:handler:"
+ "stopAngleUpdates"
+ "v16@?0@\"CMAngle\"8"
- "WiFiManager-2027.32 Aug 27 2026 20:51:42"
- "WiFiManager-2027.32 Aug 27 2026 20:52:31"
- "WiFiManagerScheduleWithQueue_block_invoke_17"
- "setPrivateMacNetworkTypeHome:"
```
