## SensitiveContentAnalysisML

> `/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML`

```diff

-93.5.5.0.0
-  __TEXT.__text: 0x59fcc
+93.5.7.0.0
+  __TEXT.__text: 0x5a0c0
   __TEXT.__auth_stubs: 0x1f40
-  __TEXT.__objc_methlist: 0x17d4
-  __TEXT.__const: 0x3018
-  __TEXT.__gcc_except_tab: 0x4e38
+  __TEXT.__objc_methlist: 0x1804
+  __TEXT.__const: 0x3148
+  __TEXT.__gcc_except_tab: 0x4e40
   __TEXT.__cstring: 0x2e56
-  __TEXT.__oslogstring: 0xe30
+  __TEXT.__oslogstring: 0xe50
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__swift5_typeref: 0x602
   __TEXT.__swift5_fieldmd: 0x3ac

   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x90
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x22f8
+  __TEXT.__unwind_info: 0x2300
   __TEXT.__eh_frame: 0x1604
   __TEXT.__objc_classname: 0x341
-  __TEXT.__objc_methname: 0x349b
-  __TEXT.__objc_methtype: 0x2ea5
-  __TEXT.__objc_stubs: 0x2c60
+  __TEXT.__objc_methname: 0x34e9
+  __TEXT.__objc_methtype: 0x2eaf
+  __TEXT.__objc_stubs: 0x2c80
   __DATA_CONST.__got: 0x510
   __DATA_CONST.__const: 0x668
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd70
+  __DATA_CONST.__objc_selrefs: 0xd80
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x1f8
   __AUTH_CONST.__auth_got: 0xfb8
   __AUTH_CONST.__const: 0x2438
   __AUTH_CONST.__cfstring: 0x1500
-  __AUTH_CONST.__objc_const: 0x3a08
+  __AUTH_CONST.__objc_const: 0x3a68
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH.__objc_data: 0xe0
   __AUTH.__data: 0x108
-  __DATA.__objc_ivar: 0x290
-  __DATA.__data: 0x510
+  __DATA.__objc_ivar: 0x298
+  __DATA.__data: 0x3f8
   __DATA.__bss: 0x1f30
   __DATA_DIRTY.__objc_data: 0x12a8
   __DATA_DIRTY.__data: 0x310

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: AF82F2E2-1FAD-39F5-BED2-2EF212130EE5
-  Functions: 2091
-  Symbols:   5098
-  CStrings:  1544
+  UUID: F93AF1A2-4255-38B0-8DB3-6144997928E5
+  Functions: 2095
+  Symbols:   5109
+  CStrings:  1549
 
Symbols:
+ -[SCMLImageSanitizerRequest setUserRequestID:]
+ -[SCMLImageSanitizerRequest userRequestID]
+ -[SCMLTextSanitizerRequest setUserRequestID:]
+ -[SCMLTextSanitizerRequest userRequestID]
+ _OBJC_IVAR_$_SCMLImageSanitizerRequest._userRequestID
+ _OBJC_IVAR_$_SCMLTextSanitizerRequest._userRequestID
+ _objc_msgSend$userRequestID
Functions:
+ -[SCMLTextSanitizerRequest userRequestID]
+ -[SCMLTextSanitizerRequest .cxx_destruct]
~ -[SCMLImageSanitizer sanitizeRequestAsynchronously:completionHandler:] : 1052 -> 1092
+ -[SCMLImageSanitizerRequest userRequestID]
+ -[SCMLImageSanitizerRequest .cxx_destruct]
~ -[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:] : 1372 -> 1424
CStrings:
+ "@\"NSUUID\""
+ "Begin sanitizePixelBuffer inst=%p width=%zu height=%zu attr=%s style=%u userRequestID=%@"
+ "Begin sanitizeText: inst=%p attr=%s %{sensitive}@ userRequestID=%@"
+ "T@\"NSUUID\",&,N,V_userRequestID"
+ "_userRequestID"
+ "setUserRequestID:"
+ "userRequestID"
- "!"
- "Begin sanitizePixelBuffer inst=%p width=%zu height=%zu attr=%s style=%u"
- "Begin sanitizeText: inst=%p attr=%s %{sensitive}@"

```
