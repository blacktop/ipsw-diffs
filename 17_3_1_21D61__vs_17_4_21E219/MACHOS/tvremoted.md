## tvremoted

> `/usr/libexec/tvremoted`

```diff

-367.30.1.0.0
-  __TEXT.__text: 0xcdd4
+367.41.1.0.0
+  __TEXT.__text: 0xcff4
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_stubs: 0x2020
+  __TEXT.__objc_stubs: 0x2060
   __TEXT.__objc_methlist: 0x8f4
   __TEXT.__const: 0x7a
-  __TEXT.__oslogstring: 0x1afe
+  __TEXT.__oslogstring: 0x1b35
   __TEXT.__cstring: 0x73e
   __TEXT.__gcc_except_tab: 0x180
-  __TEXT.__objc_methname: 0x2ae7
+  __TEXT.__objc_methname: 0x2b31
   __TEXT.__objc_classname: 0x14a
   __TEXT.__objc_methtype: 0xb5e
   __TEXT.__unwind_info: 0x2e8
   __DATA_CONST.__auth_got: 0x288
-  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x660
   __DATA_CONST.__cfstring: 0x560
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x190
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x15d8
-  __DATA.__objc_selrefs: 0xa70
-  __DATA.__objc_classrefs: 0x188
-  __DATA.__objc_superrefs: 0x20
+  __DATA.__objc_selrefs: 0xa80
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 841BB7D2-8014-3E0D-9D1C-3D67607DEB6A
+  UUID: 5377D780-E14E-3538-AE74-1E316310B6A0
   Functions: 272
-  Symbols:   2159
-  CStrings:  817
+  Symbols:   2163
+  CStrings:  822
 
Symbols:
+ _OBJC_CLASS_$_IRNode
+ _TVRCMediaRemoteIDKey
+ __48-[TVRDIRSessionManager _activateWithCompletion:]_block_invoke.18
+ __49-[TVRDIRSessionManager session:didUpdateContext:]_block_invoke.27
+ _objc_msgSend$setAvOutpuDeviceIdentifier:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$updateNodes:
- __48-[TVRDIRSessionManager _activateWithCompletion:]_block_invoke.17
- __49-[TVRDIRSessionManager session:didUpdateContext:]_block_invoke.26
- _objc_msgSend$copy
CStrings:
+ "Device disconnected: %{public}@"
+ "Devices to be removed %@"
+ "Removing candidate %@"
+ "T@\"NSString\",?,R,C"
+ "setAvOutpuDeviceIdentifier:"
+ "setWithObject:"
+ "updateNodes:"
- "Device disconnected: %@"
- "copy"

```
