## AAAFoundation

> `/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation`

```diff

-51.0.0.0.0
-  __TEXT.__text: 0xd954
+53.0.0.0.0
+  __TEXT.__text: 0xda84
   __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x1178
+  __TEXT.__objc_methlist: 0x11a8
   __TEXT.__const: 0x80
   __TEXT.__oslogstring: 0x94d
-  __TEXT.__cstring: 0xb96
+  __TEXT.__cstring: 0xc06
   __TEXT.__gcc_except_tab: 0x14c
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0x4a0
-  __TEXT.__objc_classname: 0x25e
-  __TEXT.__objc_methname: 0x2ee4
+  __TEXT.__objc_classname: 0x25f
+  __TEXT.__objc_methname: 0x2f8e
   __TEXT.__objc_methtype: 0x777
-  __TEXT.__objc_stubs: 0x2320
+  __TEXT.__objc_stubs: 0x23a0
   __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x850
+  __DATA_CONST.__const: 0x858
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2418
-  __DATA_CONST.__objc_selrefs: 0xd48
+  __DATA_CONST.__objc_const: 0x2478
+  __DATA_CONST.__objc_selrefs: 0xd70
   __AUTH_CONST.__objc_const: 0x40
-  __AUTH_CONST.__cfstring: 0xa40
+  __AUTH_CONST.__cfstring: 0xaa0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x458
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x140
   __DATA.__objc_superrefs: 0x68
-  __DATA.__objc_ivar: 0x128
+  __DATA.__objc_ivar: 0x130
   __DATA.__data: 0x2a8
   __DATA.__bss: 0xc0
   __DATA_DIRTY.__const: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7CA4A3AC-4802-31EB-BCC4-5EA33049269D
-  Functions: 483
-  Symbols:   1921
-  CStrings:  983
+  UUID: 0FC22025-1A56-35A6-AE82-6CE90B91CB02
+  Functions: 487
+  Symbols:   1936
+  CStrings:  998
 
Symbols:
+ -[AAFAnalyticsEvent setTopLevelError:]
+ -[AAFAnalyticsEvent topLevelError]
+ -[AAFTapToRadarRequest fullDiagnostic]
+ -[AAFTapToRadarRequest setFullDiagnostic:]
+ _OBJC_IVAR_$_AAFAnalyticsEvent._topLevelError
+ _OBJC_IVAR_$_AAFTapToRadarRequest._fullDiagnostic
+ __AFTTRAutoDiagnosticsFullLogArchive
+ _objc_msgSend$fullDiagnostic
+ _objc_msgSend$setAutoDiagnostics:
+ _objc_msgSend$setTopLevelError:
+ _objc_msgSend$topLevelError
CStrings:
+ "\x061"
+ "\x1d"
+ "<%@: %p> EventName: [%@], EventError: [%@], ReportData: %@, EventCategory: [%@]"
+ "<%@: %p> EventName: [%@], ReportData: %@, EventCategory: [%@]"
+ "T@\"NSError\",C,N,V_topLevelError"
+ "TB,V_fullDiagnostic"
+ "_fullDiagnostic"
+ "_topLevelError"
+ "full-log-archive"
+ "fullDiagnostic"
+ "setAutoDiagnostics:"
+ "setFullDiagnostic:"
+ "setTopLevelError:"
+ "topLevelError"
- "\x06"
- "\r"
- "<%@: %p> EventName: [%@], EventCategory: [%@], ReportData: %@"

```
