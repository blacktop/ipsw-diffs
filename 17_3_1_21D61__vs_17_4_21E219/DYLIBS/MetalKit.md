## MetalKit

> `/System/Library/Frameworks/MetalKit.framework/MetalKit`

```diff

-161.0.0.0.0
-  __TEXT.__text: 0x100d0
+163.0.0.0.0
+  __TEXT.__text: 0x10224
   __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_methlist: 0xd84
   __TEXT.__const: 0xc48
-  __TEXT.__cstring: 0x1689
+  __TEXT.__cstring: 0x1783
   __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__unwind_info: 0x484
+  __TEXT.__unwind_info: 0x488
   __TEXT.__objc_classname: 0x267
-  __TEXT.__objc_methname: 0x32db
+  __TEXT.__objc_methname: 0x330d
   __TEXT.__objc_methtype: 0xd16
-  __TEXT.__objc_stubs: 0x28c0
+  __TEXT.__objc_stubs: 0x2900
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x3e8
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3458
-  __DATA_CONST.__objc_selrefs: 0xc60
-  __AUTH_CONST.__cfstring: 0xe20
+  __DATA_CONST.__objc_selrefs: 0xc70
+  __DATA_CONST.__objc_classrefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x98
+  __AUTH_CONST.__cfstring: 0xe60
   __AUTH_CONST.__objc_const: 0x750
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__auth_got: 0x428
   __AUTH.__data: 0x20
-  __DATA.__objc_classrefs: 0x168
-  __DATA.__objc_superrefs: 0x98
   __DATA.__objc_ivar: 0x1f8
   __DATA.__data: 0xb08
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/TextureIO.framework/TextureIO
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AD0C6688-9DC1-3212-A079-EEDA3760BFB9
-  Functions: 396
-  Symbols:   1676
-  CStrings:  1072
+  UUID: 4AA15121-7684-3E1B-A58C-F82E470B3D47
+  Functions: 397
+  Symbols:   1680
+  CStrings:  1081
 
Symbols:
+ -[MTKTextureLoaderPVR3 initWithData:options:error:].cold.1
+ _objc_msgSend$isMacCatalystApp
+ _objc_msgSend$isiOSAppOnMac
CStrings:
+ "-[MTKTextureLoaderPVR3 initWithData:options:error:]"
+ "KTX metadata size exceeds metadata region size"
+ "PVR header metadata size too large"
+ "T@\"NSString\",?,R,C"
+ "[MTKTextureLoaderPVR3 isPVR3File:data] && \"This function should not be reachable\""
+ "false && \"Expected 3 bytes of orientation data\""
+ "isMacCatalystApp"
+ "isiOSAppOnMac"
- "dataSize == 3"

```
