## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-936.60.10.0.0
-  __TEXT.__text: 0x17a2dc
+936.80.3.0.0
+  __TEXT.__text: 0x17a520
   __TEXT.__auth_stubs: 0x1290
-  __TEXT.__objc_methlist: 0xc230
-  __TEXT.__const: 0xb60
-  __TEXT.__cstring: 0x3c095
+  __TEXT.__objc_methlist: 0xc260
+  __TEXT.__const: 0xb50
+  __TEXT.__cstring: 0x3c249
   __TEXT.__oslogstring: 0x21389
   __TEXT.__gcc_except_tab: 0x1440
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x22f8
   __TEXT.__eh_frame: 0x7c
   __TEXT.__objc_classname: 0xb34
-  __TEXT.__objc_methname: 0x2b71f
+  __TEXT.__objc_methname: 0x2b843
   __TEXT.__objc_methtype: 0x290e
-  __TEXT.__objc_stubs: 0x19680
+  __TEXT.__objc_stubs: 0x19700
   __DATA_CONST.__got: 0x308
   __DATA_CONST.__const: 0x2100
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xddf8
-  __DATA_CONST.__objc_selrefs: 0x6fd0
+  __DATA_CONST.__objc_const: 0xde58
+  __DATA_CONST.__objc_selrefs: 0x6ff0
   __DATA_CONST.__objc_arraydata: 0x810
-  __AUTH_CONST.__cfstring: 0x26860
+  __AUTH_CONST.__cfstring: 0x26960
   __AUTH_CONST.__objc_const: 0x3048
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__const: 0xa00

   __AUTH.__objc_data: 0x780
   __DATA.__objc_classrefs: 0x6a0
   __DATA.__objc_superrefs: 0x270
-  __DATA.__objc_ivar: 0xf80
+  __DATA.__objc_ivar: 0xf88
   __DATA.__data: 0xd30
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x1860

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimg4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4892
-  Symbols:   15879
-  CStrings:  12329
+  Functions: 4896
+  Symbols:   15893
+  CStrings:  12346
 
Symbols:
+ -[ControlManager allowSTExtractorPluginLoadFromDownloadedMABrain]
+ -[ControlManager setAllowSTExtractorPluginLoadFromDownloadedMABrain:]
+ -[DownloadManager setTrainName:]
+ -[DownloadManager trainName]
+ GCC_except_table227
+ _OBJC_IVAR_$_ControlManager._allowSTExtractorPluginLoadFromDownloadedMABrain
+ _OBJC_IVAR_$_DownloadManager._trainName
+ ___block_literal_global.700
+ _objc_msgSend$allowSTExtractorPluginLoadFromDownloadedMABrain
+ _objc_msgSend$getCString:maxLength:encoding:
+ _objc_msgSend$setAllowSTExtractorPluginLoadFromDownloadedMABrain:
+ _objc_msgSend$setTrainName:
- GCC_except_table225
- ___block_literal_global.688
CStrings:
+ "\x1f\x02\x1a"
+ "-[ASAssetMetadataUpdatePolicy trainName]_block_invoke"
+ "AEA extractor will be loaded from the system volume because the base OS doesn't support loading it from the MA brain cryptex."
+ "DawnD"
+ "DownloadManager returned a valid train name"
+ "Setting train name on DownloadManger to %@"
+ "Starting built-in MobileAsset brain built Dec 20 2023 18:39:24"
+ "Starting downloaded MobileAsset brain (version: %@) built Dec 20 2023 18:39:24"
+ "T@\"NSString\",&,N,V_trainName"
+ "TB,N,V_allowSTExtractorPluginLoadFromDownloadedMABrain"
+ "Train name not passed in via options"
+ "Using train name(%s) from download manager"
+ "Using train name(%s) from legacy method"
+ "_allowSTExtractorPluginLoadFromDownloadedMABrain"
+ "_trainName"
+ "allow-st-extractor-plugin"
+ "allowSTExtractorPluginLoadFromDownloadedMABrain"
+ "getCString:maxLength:encoding:"
+ "mobileassetd-trainname"
+ "setAllowSTExtractorPluginLoadFromDownloadedMABrain:"
+ "setTrainName:"
- "\x1f\x02\x19"
- "DawnC"
- "Starting built-in MobileAsset brain built Nov 12 2023 07:43:21"
- "Starting downloaded MobileAsset brain (version: %@) built Nov 12 2023 07:43:21"

```
