## com.apple.fskit.msdos

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos`

```diff

-747.120.3.0.0
-  __TEXT.__text: 0x3432c
+788.0.0.0.0
+  __TEXT.__text: 0x34a38
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0x3ae0
-  __TEXT.__objc_methlist: 0x1fa4
+  __TEXT.__objc_stubs: 0x3b40
+  __TEXT.__objc_methlist: 0x1ff4
   __TEXT.__const: 0x4e1d
-  __TEXT.__cstring: 0x3d97
-  __TEXT.__gcc_except_tab: 0x1634
-  __TEXT.__objc_methname: 0x4486
-  __TEXT.__oslogstring: 0x28ec
+  __TEXT.__cstring: 0x3d96
+  __TEXT.__gcc_except_tab: 0x162c
+  __TEXT.__objc_methname: 0x457f
+  __TEXT.__oslogstring: 0x28e7
   __TEXT.__objc_classname: 0x274
-  __TEXT.__objc_methtype: 0x1760
-  __TEXT.__unwind_info: 0x970
+  __TEXT.__objc_methtype: 0x178d
+  __TEXT.__unwind_info: 0x988
   __DATA_CONST.__auth_got: 0x470
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xfe0
+  __DATA_CONST.__const: 0x1038
   __DATA_CONST.__cfstring: 0x5e0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA.__objc_const: 0x36d8
-  __DATA.__objc_selrefs: 0x1280
-  __DATA.__objc_ivar: 0x1cc
+  __DATA.__objc_const: 0x3738
+  __DATA.__objc_selrefs: 0x12b0
+  __DATA.__objc_ivar: 0x1d0
   __DATA.__objc_data: 0x7d0
   __DATA.__data: 0xa88
   __DATA.__common: 0x8c

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D97D18FC-D0AB-3B65-8621-B8DA1728167B
-  Functions: 1076
+  UUID: 3D7644E8-AFD6-3439-AF60-F70BE58D66E0
+  Functions: 1088
   Symbols:   347
-  CStrings:  1803
+  CStrings:  1813
 
CStrings:
+ "%s: Failed to clean dirty bit, error %@"
+ "+[Utilities metaWriteToDevice:from:startingAt:length:forceSyncWrite:]"
+ "-[FATManager setDirtyBitValue:forceWriteToDisk:replyHandler:]_block_invoke"
+ "@36@0:8^v16q24B32"
+ "@52@0:8@16^v24q32Q40B48"
+ "Calculated zero cache blocks\n"
+ "TC,V_dirtyBitValueOnDisk"
+ "_dirtyBitValueOnDisk"
+ "dirtyBitValueOnDisk"
+ "enableOpenUnlinkEmulation"
+ "metaWriteToDevice:from:startingAt:length:forceSyncWrite:"
+ "metaWriteToFATs:startingAt:"
+ "metaWriteToFATs:startingAt:forceSyncWrite:"
+ "setDirtyBitValue:forceWriteToDisk:replyHandler:"
+ "setDirtyBitValueOnDisk:"
+ "setEnableOpenUnlinkEmulation:"
+ "v32@0:8C16B20@?24"
- "%s: Failed to read dirty bit value, error %@"
- "+[Utilities metaWriteToDevice:from:startingAt:length:]"
- "-[FATManager setDirtyBitValue:replyHandler:]_block_invoke"
- "-[FATVolume synchronizeWithFlags:replyHandler:]_block_invoke_2"
- "metaWriteToDevice:from:startingAt:length:"
- "setDirtyBitValue:replyHandler:"
- "v28@0:8C16@?20"

```
