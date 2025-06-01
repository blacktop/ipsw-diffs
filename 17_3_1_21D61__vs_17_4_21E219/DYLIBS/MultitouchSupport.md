## MultitouchSupport

> `/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport`

```diff

-7100.38.0.0.0
-  __TEXT.__text: 0x1b5b0
-  __TEXT.__auth_stubs: 0xd90
+7140.17.0.0.0
+  __TEXT.__text: 0x1cc1c
+  __TEXT.__auth_stubs: 0xdb0
   __TEXT.__objc_methlist: 0x184
-  __TEXT.__const: 0x1f7c
-  __TEXT.__cstring: 0x153f
-  __TEXT.__oslogstring: 0xd56
-  __TEXT.__tpad_act_plist: 0x61e6
-  __TEXT.__unwind_info: 0x610
+  __TEXT.__const: 0x1f88
+  __TEXT.__cstring: 0x15e8
+  __TEXT.__oslogstring: 0xfc6
+  __TEXT.__tpad_act_plist: 0x5af1
+  __TEXT.__unwind_info: 0x648
   __TEXT.__objc_classname: 0x49
-  __TEXT.__objc_methname: 0x658
+  __TEXT.__objc_methname: 0x684
   __TEXT.__objc_methtype: 0x591
-  __TEXT.__objc_stubs: 0x500
+  __TEXT.__objc_stubs: 0x540
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xa20
-  __DATA_CONST.__objc_selrefs: 0x1c8
-  __AUTH_CONST.__cfstring: 0xf40
+  __DATA_CONST.__objc_selrefs: 0x1d8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__cfstring: 0xf60
   __AUTH_CONST.__objc_const: 0xd8
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x6e0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x48
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x1c0
   __DATA.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F89F53CC-0FA8-3FFF-902E-1190EAD545F8
-  Functions: 610
-  Symbols:   1294
-  CStrings:  569
+  UUID: 6B0C14AE-47E9-3B35-9417-31F738A499C0
+  Functions: 625
+  Symbols:   1326
+  CStrings:  588
 
Symbols:
+ _MTActuatorChangeHostClickControl
+ _MTActuatorRelinquishHostClickControl
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSNumber
+ __MTActuationLoadActuationsFromPropertyListV2orV3
+ ___block_descriptor_tmp.215
+ _calloc
+ _codecGetFooterID
+ _codecReadHeader
+ _codecResetModel
+ _codecWriteHeader
+ _malloc
+ _mt_UncompressTouchpadCodecV1Force
+ _mt_UncompressTouchpadCodecV1Image
+ _mt_UncompressTouchpadCodecV1Touch
+ _objc_msgSend$intValue
+ _objc_msgSend$numberWithInt:
+ _touchpadCodecCreate
+ _touchpadCodecDecodeImage
+ _touchpadCodecDestroy
+ _touchpadGetInfoWithCompressedBuffer
- ___block_descriptor_tmp.213
CStrings:
+ "Buffer too small to uncompress image to %d bytes! (Buffer is only %u)\n"
+ "Error parsing click playlist, failed to create default waveform for actuationID=%@"
+ "Error parsing click playlist, failed to create silent waveform for actuationID=%@"
+ "Error parsing click playlist, revision %@ and default not found"
+ "Error parsing click playlist, unable to determine actuation id(%d) or default waveform not defined(%d)"
+ "Error parsing click playlist, unknown version"
+ "Failed to decompress touchpad codec v1 compressed image. Failed with error(0x%X)\n"
+ "Failed to load actuations from plist - Invalid plist reference"
+ "Invalid force sensor index\n"
+ "MTActuator Error: Could not %s host click control. Status = 0x%08x\n"
+ "Silent"
+ "T@\"NSString\",?,R,C"
+ "Touchpad codec v1 failed to create codec\n"
+ "Touchpad codec v1 failed to decode the provided image\n"
+ "Uncompressed image buffer(%zu) was too small to handle expected number of force bytes(%d)\n"
+ "Version"
+ "i"
+ "intValue"
+ "numberWithInt:"
+ "relinquish"
+ "request"
- "ActuationID:%d"
- "MTActuator Error: Could not request host click control. Status = 0x%08x\n"
- "Using the default waveform array"

```
