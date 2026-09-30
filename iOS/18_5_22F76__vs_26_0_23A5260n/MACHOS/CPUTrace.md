## CPUTrace

> `/System/Library/Trace/Providers/CPUTrace.bundle/CPUTrace`

```diff

-84.100.20.0.0
-  __TEXT.__text: 0x3d40
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_stubs: 0x580
+130.0.0.0.0
+  __TEXT.__text: 0x3f58
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_stubs: 0x5c0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x258
+  __TEXT.__objc_methlist: 0x270
   __TEXT.__const: 0x51
-  __TEXT.__cstring: 0x694
-  __TEXT.__objc_methname: 0x638
+  __TEXT.__cstring: 0x73e
+  __TEXT.__objc_methname: 0x6d1
   __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methtype: 0x1fa
-  __TEXT.__gcc_except_tab: 0x2c0
+  __TEXT.__objc_methtype: 0x206
+  __TEXT.__gcc_except_tab: 0x2dc
   __TEXT.__unwind_info: 0x1f8
-  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__auth_got: 0x420
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x150
-  __DATA_CONST.__cfstring: 0x660
+  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__cfstring: 0x740
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x510
-  __DATA.__objc_selrefs: 0x1e0
-  __DATA.__objc_ivar: 0x4c
+  __DATA_CONST.__objc_arraydata: 0x20
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA.__objc_const: 0x570
+  __DATA.__objc_selrefs: 0x1f8
+  __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xd0
   __DATA.__bss: 0x24

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libhwtrace.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 21958088-FDDE-31F1-9E2E-D79008B63236
-  Functions: 86
-  Symbols:   176
-  CStrings:  232
+  UUID: E37C7151-EA94-3E29-9045-BD0EA1FE6A2F
+  Functions: 88
+  Symbols:   179
+  CStrings:  254
 
Symbols:
+ _CPUTraceProviderOptionDecodeCompression
+ _CPUTraceProviderOptionTraceBufferSize
+ _hwtrace_recording_save_options_set_decode_compression
+ _objc_retainAutorelease
- __Znwm
CStrings:
+ "("
+ "@\"NSString\""
+ "LZ4"
+ "LZ4_RAW"
+ "LZFSE"
+ "T@\"NSNumber\",R,&,V_traceBufferSize"
+ "T@\"NSString\",R,C,V_decodeCompression"
+ "UTF8String"
+ "Unsupported compression algorithm: \"%@\". Supported algorithms: %@"
+ "_decodeCompression"
+ "_traceBufferSize"
+ "decode-compression"
+ "decode-compression requires decode to be enabled"
+ "decodeCompression"
+ "trace-buffer-size"
+ "traceBufferSize"
- "&"

```
