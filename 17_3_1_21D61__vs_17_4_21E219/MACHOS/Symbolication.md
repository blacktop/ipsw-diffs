## Symbolication

> `/System/Library/Trace/Providers/Symbolication.bundle/Symbolication`

```diff

-38.2.0.0.0
-  __TEXT.__text: 0x330
-  __TEXT.__auth_stubs: 0x100
-  __TEXT.__objc_stubs: 0xe0
-  __TEXT.__objc_methlist: 0x68
+45.0.0.0.0
+  __TEXT.__text: 0x4b0
+  __TEXT.__auth_stubs: 0x170
+  __TEXT.__objc_stubs: 0x120
+  __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xbe
-  __TEXT.__objc_methname: 0x226
-  __TEXT.__objc_classname: 0x28
-  __TEXT.__objc_methtype: 0x17c
-  __TEXT.__unwind_info: 0x6c
-  __DATA_CONST.__auth_got: 0x88
+  __TEXT.__cstring: 0x121
+  __TEXT.__objc_methname: 0x264
+  __TEXT.__objc_classname: 0x2a
+  __TEXT.__objc_methtype: 0x195
+  __TEXT.__unwind_info: 0x7c
+  __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x38
-  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x2a0
-  __DATA.__objc_selrefs: 0x78
-  __DATA.__objc_classrefs: 0x18
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x4
+  __DATA_CONST.__objc_classrefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0x2c0
+  __DATA.__objc_selrefs: 0x90
+  __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60
+  __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication
   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9
-  Symbols:   38
-  CStrings:  47
+  Functions: 12
+  Symbols:   45
+  CStrings:  57
 
Symbols:
+ _ATSSymbolicationProviderAmendMethodDownload
+ ___assert_rtn
+ _objc_release
+ _objc_release_x23
+ _objc_release_x24
+ _objc_retain
+ _objc_retain_x20
+ _objc_retain_x24
+ _objc_storeStrong
- _ATSSymbolicationProviderAmendMethodDsymForUUID
- _objc_retain_x4
CStrings:
+ "\x11"
+ ".cxx_destruct"
+ "@\"<KTProviderLogger>\""
+ "ATSSymbolicationProvider.m"
+ "Amending symbolication is not supported on this platform. Run this command on the host."
+ "Unrecognized symbolication method option: %@"
+ "^{ats_symbolication_config=III*B^?*}"
+ "_logger"
+ "download"
+ "global_logger"
+ "logger_callback"
+ "stringWithUTF8String:"
+ "warnWithMessage:"
- "The 'dsym-path' option is not supported on this platform. Run this command on the host."
- "^{ats_symbolication_config=III*B}"
- "dsymForUUID"

```
