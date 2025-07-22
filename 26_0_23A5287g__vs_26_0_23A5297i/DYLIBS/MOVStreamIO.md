## MOVStreamIO

> `/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO`

```diff

-3.33.1.0.0
-  __TEXT.__text: 0x9c770
-  __TEXT.__auth_stubs: 0x13d0
+3.34.0.0.0
+  __TEXT.__text: 0x9cb78
+  __TEXT.__auth_stubs: 0x13e0
   __TEXT.__delay_stubs: 0x18c
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x65e0
+  __TEXT.__objc_methlist: 0x6618
   __TEXT.__const: 0x47b0
-  __TEXT.__cstring: 0x894f
+  __TEXT.__cstring: 0x8969
   __TEXT.__oslogstring: 0x355f
-  __TEXT.__gcc_except_tab: 0xecc4
+  __TEXT.__gcc_except_tab: 0xed44
   __TEXT.__ustring: 0x5fc
-  __TEXT.__unwind_info: 0x3528
+  __TEXT.__unwind_info: 0x3538
   __TEXT.__objc_classname: 0xf38
-  __TEXT.__objc_methname: 0xe8a1
-  __TEXT.__objc_methtype: 0x52ea
-  __TEXT.__objc_stubs: 0x95a0
+  __TEXT.__objc_methname: 0xe8e8
+  __TEXT.__objc_methtype: 0x5328
+  __TEXT.__objc_stubs: 0x95c0
   __DATA_CONST.__got: 0x7f0
   __DATA_CONST.__const: 0x9b8
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3060
+  __DATA_CONST.__objc_selrefs: 0x3070
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x2b8
-  __AUTH_CONST.__auth_got: 0xa48
+  __AUTH_CONST.__auth_got: 0xa50
   __AUTH_CONST.__const: 0x9f8
-  __AUTH_CONST.__cfstring: 0x5c00
-  __AUTH_CONST.__objc_const: 0xeab8
+  __AUTH_CONST.__cfstring: 0x5c20
+  __AUTH_CONST.__objc_const: 0xeb00
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x620
+  __DATA.__objc_ivar: 0x624
   __DATA.__data: 0xa24
   __DATA.__bss: 0x169
   __DATA_DIRTY.__objc_data: 0x1d10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DC0EAE1E-D5F6-3C59-8EF5-2DE3EEE8F0A5
-  Functions: 2731
-  Symbols:   10221
-  CStrings:  4769
+  UUID: 089AEDC2-2094-352A-84FF-A8FC5CB4042F
+  Functions: 2734
+  Symbols:   10232
+  CStrings:  4774
 
Symbols:
+ +[MOVStreamIOUtility stringFromTimeCode:dropFrame:addSubframes:]
+ -[MIODefaultFrameProcessor dealloc]
+ -[MIOWriterPixelBufferStreamInput initWithStreamId:pixelFormat:width:height:recordingConfig:]
+ _CMVideoFormatDescriptionCreate
+ _OBJC_IVAR_$_MIODefaultFrameProcessor._formatDescForEncoding
+ _OBJC_IVAR_$_MIOFrameProcessor.formatDescriptionNeedsUpdate
+ __OBJC_$_INSTANCE_VARIABLES_MIODefaultFrameProcessor
+ _objc_msgSend$stringFromTimeCode:dropFrame:addSubframes:
- _OBJC_IVAR_$_MIOFrameProcessor._formatDescriptionNeedsUpdate
CStrings:
+ "%02d:%02d:%02d%c%02d.%03d"
+ "3.34.0"
+ "@44@0:8@16I24i28i32@36"
+ "@48@0:8{CVSMPTETime=ssIIIssss}16B40B44"
+ "TB,VformatDescriptionNeedsUpdate"
+ "initWithStreamId:pixelFormat:width:height:recordingConfig:"
+ "stringFromTimeCode:dropFrame:addSubframes:"
- "3.33.1"
- "TB,V_formatDescriptionNeedsUpdate"
- "_formatDescriptionNeedsUpdate"

```
