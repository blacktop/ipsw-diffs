## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

-57.0.0.0.0
-  __TEXT.__text: 0x231b8
-  __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_stubs: 0xa60
+58.0.0.0.0
+  __TEXT.__text: 0x2229c
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_stubs: 0xa80
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x324
-  __TEXT.__gcc_except_tab: 0x26e4
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x5ace
-  __TEXT.__objc_classname: 0x55
-  __TEXT.__objc_methname: 0xba1
+  __TEXT.__gcc_except_tab: 0x2660
+  __TEXT.__const: 0x248
+  __TEXT.__cstring: 0x5c87
+  __TEXT.__objc_classname: 0x50
+  __TEXT.__objc_methname: 0xbd8
   __TEXT.__objc_methtype: 0x65d
   __TEXT.__oslogstring: 0x99e
-  __TEXT.__unwind_info: 0x748
-  __DATA_CONST.__auth_got: 0x450
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0x558
-  __DATA_CONST.__cfstring: 0x3d20
+  __TEXT.__unwind_info: 0x790
+  __DATA_CONST.__const: 0x578
+  __DATA_CONST.__cfstring: 0x3d60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x638
-  __DATA.__objc_selrefs: 0x3a8
-  __DATA.__objc_ivar: 0x68
+  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__got: 0x350
+  __DATA.__objc_const: 0x678
+  __DATA.__objc_selrefs: 0x3b0
+  __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6240F70-9E5D-3640-8BD6-344FCD88909B
-  Functions: 481
-  Symbols:   420
-  CStrings:  1465
+  UUID: F5A16297-5952-3C9D-AF8A-D00DCE6B77A8
+  Functions: 486
+  Symbols:   417
+  CStrings:  1481
 
Symbols:
+ _cleanIOServiceConnection
+ _initializeIOServiceConnectionWithName
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x3
+ _objc_retain_x8
+ _performCommand
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x28
- _strlen
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Pearl_Kernel/PearlSupport/PearlSupportUtils.m"
+ "/System/Library/MediaCapture/ISP.mediacapture"
+ "AppleCamera"
+ "AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n"
+ "CENTAUR projector version detected"
+ "ISPCaptureDeviceCreate"
+ "MIRAGE projector version detected"
+ "_connect != ((io_object_t) 0)"
+ "connect"
+ "dataInfo->setCount <= (4)"
+ "m_isCentaur"
+ "m_isMirage"
+ "outConnect"
+ "serviceName"
+ "stringByAppendingPathComponent:"
- "%s%s"

```
