## dietappleh16camerad

> `/usr/libexec/dietappleh16camerad`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-6.201.0.0.0
-  __TEXT.__text: 0x1af20
-  __TEXT.__auth_stubs: 0xef0
+6.203.1.0.0
+  __TEXT.__text: 0x1b754
+  __TEXT.__auth_stubs: 0xf20
   __TEXT.__objc_stubs: 0x4e0
   __TEXT.__const: 0x15c0
-  __TEXT.__cstring: 0x3288
-  __TEXT.__gcc_except_tab: 0x478
-  __TEXT.__oslogstring: 0x223b
+  __TEXT.__cstring: 0x32cd
+  __TEXT.__gcc_except_tab: 0x474
+  __TEXT.__oslogstring: 0x2366
   __TEXT.__objc_methname: 0x343
-  __TEXT.__unwind_info: 0x790
-  __DATA_CONST.__const: 0x9b68
+  __TEXT.__unwind_info: 0x7c0
+  __DATA_CONST.__const: 0x9b88
   __DATA_CONST.__cfstring: 0x1460
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x788
+  __DATA_CONST.__auth_got: 0x7a0
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_selrefs: 0x138

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 397
-  Symbols:   291
-  CStrings:  631
+  Functions: 412
+  Symbols:   294
+  CStrings:  640
 
Symbols:
+ _os_variant_allows_internal_security_policies
+ _os_variant_has_internal_content
+ _xpc_connection_send_message_with_reply
CStrings:
+ "%s - assistant failed to load setfiles: 0x%08x\n"
+ "%s - received async error reply: %s\n"
+ "%s: CloseInterfaceToSavageCam without a matching open\n"
+ "6.203.1"
+ "H16ISPServicesRemote: SetProperty %d (reply=0x%08X)\n"
+ "H16ISPServicesRemote: SetProperty %d (sent)\n"
+ "H16ISPServicesRemote: SetProperty (async) %d (reply=0x%08X)\n"
+ "ISP_BuildAndLoadSetfile"
+ "LoadSetfiles"
+ "sendMessageAsync_block_invoke"
- "6.201"
```
