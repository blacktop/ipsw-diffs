## iapd

> `/System/Library/PrivateFrameworks/IAP.framework/Support/iapd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__common`

```diff

-2185.0.0.0.0
-  __TEXT.__text: 0xed658
-  __TEXT.__auth_stubs: 0x2190
+2186.0.0.0.0
+  __TEXT.__text: 0xed820
+  __TEXT.__auth_stubs: 0x21b0
   __TEXT.__objc_stubs: 0x4b80
   __TEXT.__init_offsets: 0x20
   __TEXT.__objc_methlist: 0x1974
-  __TEXT.__gcc_except_tab: 0x7d7c
+  __TEXT.__gcc_except_tab: 0x7d90
   __TEXT.__const: 0x74f0
-  __TEXT.__cstring: 0x14ca4
+  __TEXT.__cstring: 0x14cbe
   __TEXT.__objc_methname: 0x5306
   __TEXT.__objc_classname: 0x268
   __TEXT.__objc_methtype: 0xede
-  __TEXT.__unwind_info: 0x4d68
-  __DATA_CONST.__const: 0x8930
+  __TEXT.__unwind_info: 0x4d80
+  __DATA_CONST.__const: 0x8958
   __DATA_CONST.__cfstring: 0x7460
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x10e0
+  __DATA_CONST.__auth_got: 0x10f0
   __DATA_CONST.__got: 0x9f0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x2e18

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 4274
-  Symbols:   869
+  Functions: 4278
+  Symbols:   871
   CStrings:  3152
 
Symbols:
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
CStrings:
+ "BluetoothUpdateStatus_block_invoke"
+ "PostBluetoothConnectionStatusNotificationAboutKnownDevices_block_invoke"
- "BluetoothUpdateStatus"
- "PostBluetoothConnectionStatusNotificationAboutKnownDevices"
```
