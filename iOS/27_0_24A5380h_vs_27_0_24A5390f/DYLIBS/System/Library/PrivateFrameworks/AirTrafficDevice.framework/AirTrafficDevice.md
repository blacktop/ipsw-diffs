## AirTrafficDevice

> `/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-4026.100.74.0.0
-  __TEXT.__text: 0x1f161c
-  __TEXT.__objc_methlist: 0x37b0
+4026.110.81.1.0
+  __TEXT.__text: 0x1f1934
+  __TEXT.__objc_methlist: 0x37d0
   __TEXT.__dlopen_cstrs: 0x202
   __TEXT.__const: 0x1e1e8
   __TEXT.__gcc_except_tab: 0xad8
-  __TEXT.__cstring: 0x2aee
-  __TEXT.__oslogstring: 0x7177
+  __TEXT.__cstring: 0x2b36
+  __TEXT.__oslogstring: 0x7260
   __TEXT.__unwind_info: 0x14d0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29c8
+  __DATA_CONST.__objc_selrefs: 0x29e0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0xe8
-  __DATA_CONST.__got: 0x880
+  __DATA_CONST.__got: 0x888
   __AUTH_CONST.__const: 0x118a8
-  __AUTH_CONST.__cfstring: 0x2e00
-  __AUTH_CONST.__objc_const: 0x6248
+  __AUTH_CONST.__cfstring: 0x2e40
+  __AUTH_CONST.__objc_const: 0x6258
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0x650
   __DATA.__objc_ivar: 0x4b0
   __DATA.__data: 0x17a8
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0x138
   __DATA.__common: 0xb20
   __DATA_DIRTY.__objc_data: 0x11d0
   __DATA_DIRTY.__data: 0x60
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1679
-  Symbols:   4107
-  CStrings:  982
+  Symbols:   4112
+  CStrings:  986
 
Symbols:
+ _NSDebugDescriptionErrorKey
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ATSyncClient
+ _objc_msgSend$changeCountSinceRevision:
+ _objc_msgSend$currentMaxAllowedSyncChanges
+ _objc_msgSend$unsignedLongValue
Functions:
~ -[ATDeviceSyncManager _initiateSyncForDataClass:onMessageLink:] : 1208 -> 1348
~ ___63-[ATDeviceSyncManager _initiateSyncForDataClass:onMessageLink:]_block_invoke : 680 -> 756
~ -[ATDeviceSyncManager _handleBeginSyncSessionRequest:onMessageLink:] : 1312 -> 1888
CStrings:
+ "%{public}@: Handling request to begin sync session for data class '%{public}@'. params = %{public}@"
+ "%{public}@: Not starting sync for dataclass '%{public}@' because the number of incoming changes exceeds the current limit. (%u > %u)"
+ "Number of pending changes exceeds the current limit"
+ "_PendingChangeCount"
```
