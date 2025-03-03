## CoreMedia

> `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`

```diff

-3210.14.1.11.3
-  __TEXT.__text: 0x26da88
+3210.17.1.11.1
+  __TEXT.__text: 0x26d1a8
   __TEXT.__auth_stubs: 0x33a0
   __TEXT.__objc_methlist: 0x53c
   __TEXT.__const: 0x1af0
-  __TEXT.__oslogstring: 0x2b029
-  __TEXT.__cstring: 0x53e04
+  __TEXT.__oslogstring: 0x2b1c2
+  __TEXT.__cstring: 0x53f07
   __TEXT.__gcc_except_tab: 0x198
   __TEXT.__dlopen_cstrs: 0x190
-  __TEXT.__unwind_info: 0x4c80
+  __TEXT.__unwind_info: 0x4c18
   __TEXT.__objc_classname: 0xe8
   __TEXT.__objc_methname: 0x165f
   __TEXT.__objc_methtype: 0xb5b
   __TEXT.__objc_stubs: 0x13c0
   __DATA_CONST.__got: 0x528
-  __DATA_CONST.__const: 0x9ae0
+  __DATA_CONST.__const: 0x9ae8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__crash_info: 0x40
   __DATA.__common: 0x7a0
   __DATA.__bss: 0x1330
-  __DATA_DIRTY.__data: 0x2dc
-  __DATA_DIRTY.__common: 0x290
+  __DATA_DIRTY.__data: 0x2e4
+  __DATA_DIRTY.__common: 0x288
   __DATA_DIRTY.__bss: 0x17c8
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10322
-  Symbols:   14414
-  CStrings:  13605
+  Functions: 10278
+  Symbols:   14367
+  CStrings:  13614
 
Symbols:
+ _kFigXPCServerOption_AllowSecondaryConnections
- _FigBBMessageCommit
- _FigBBMessageCopyBlockBuffer
- _FigBBMessageCopyCFArray
- _FigBBMessageCopyCFData
- _FigBBMessageCopyCFDictionary
- _FigBBMessageCopyCFString
- _FigBBMessageCreate
- _FigBBMessageGetCString
- _FigBBMessageGetDataPtr
- _FigBBMessageGetFloat32
- _FigBBMessageGetInt64
- _FigBBMessageSetBlockBuffer
- _FigBBMessageSetCFArray
- _FigBBMessageSetCFData
- _FigBBMessageSetCFDictionary
- _FigBBMessageSetCFString
- _FigBBMessageSetCString
- _FigBBMessageSetDataPtr
- _FigBBMessageSetFloat32
- _FigBBMessageSetInt64
CStrings:
+ "<<<< FigNetworkHistory >>>> %s: %p: the first latency %.3f"
+ "<<<< HEVCBridge >>>> %s: vps_max_layers_minus1 %d MaxLayersMinus1 %d NumIndependentLayers %d num_add_layer_sets %d vps_max_layer_id %d"
+ "<<<< MemoryPool >>>> %s: Attempt to decrement blockInfo %p, BlockSN %016llx use count, but it's already 0"
+ "<<<< MemoryPool >>>> %s: Would decrement recipient use count for BlockSN %016llx entry %p but it's already 0"
+ "Attempt to decrement recipient use count but it's already 0"
+ "NULL subLayerExtensions"
+ "Server does not allow the creation of secondary connections"
+ "hevcbridge_updateFormatDescriptionExtensionsFromHVCC"
+ "kFigXPCError_UnsupportedOperation"
+ "xpcServerOption_AllowSecondaryConnections"
- "MessageLayout"

```
