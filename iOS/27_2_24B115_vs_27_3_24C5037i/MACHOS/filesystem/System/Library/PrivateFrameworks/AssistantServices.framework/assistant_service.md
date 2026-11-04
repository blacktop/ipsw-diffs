## assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3605.31.1.11.2
-  __TEXT.__text: 0x894c
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_stubs: 0x15a0
+3610.11.2.0.0
+  __TEXT.__text: 0x8b98
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_stubs: 0x1600
   __TEXT.__objc_methlist: 0xaac
-  __TEXT.__const: 0x48
+  __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x98
   __TEXT.__cstring: 0x13f0
-  __TEXT.__oslogstring: 0xc6f
-  __TEXT.__objc_methname: 0x19b6
+  __TEXT.__oslogstring: 0xd23
+  __TEXT.__objc_methname: 0x19da
   __TEXT.__objc_classname: 0x1f6
   __TEXT.__objc_methtype: 0x889
   __TEXT.__unwind_info: 0x350

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__auth_got: 0x328
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__got: 0x130
   __DATA.__objc_const: 0x11c8
-  __DATA.__objc_selrefs: 0x748
+  __DATA.__objc_selrefs: 0x758
   __DATA.__objc_ivar: 0xa4
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x668

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 192
-  Symbols:   144
-  CStrings:  595
+  Symbols:   148
+  CStrings:  599
 
Symbols:
+ _AFPeerInfoGetCompactDescription
+ _AFRemotePeerCommandDispositionForAceCommand
+ _kAFRemotePeerDeliveredCommandKey
+ _kAFRemotePeerDeliveredCommandValue
Functions:
~ sub_100001f64 : 656 -> 1244
CStrings:
+ "%s Refusing command %{public}@ (bundle = %{public}@) from peer %@"
+ "%s Running command %{public}@ (bundle = %{public}@) from peer %@ (owned by current user %d, delivered by peer %d)"
+ "isDeviceOwnedByCurrentUser"
+ "userInfo"
```
