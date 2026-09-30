## libxslt.1.dylib

> `/usr/lib/libxslt.1.dylib`

```diff

-  __TEXT.__text: 0x2203c
+  __TEXT.__text: 0x21efc
   __TEXT.__cstring: 0x72c7
   __TEXT.__const: 0xc0
   __TEXT.__unwind_info: 0x4e8

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__auth_got: 0x6e0
+  __AUTH.__data: 0x20
   __DATA.__data: 0x28
   __DATA.__bss: 0x461
   __DATA.__common: 0x14
-  __DATA_DIRTY.__data: 0x40
+  __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__bss: 0x39
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libxml2.2.dylib
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _xsltParseStylesheetAttributeSet : 1452 -> 1444
~ _xsltCompileAttr : 1280 -> 1256
~ _xsltCompilePatternInternal : 2264 -> 2232
~ _xsltCompileRelativePathPattern : 444 -> 416
~ _xsltScanNCName : 616 -> 604
~ _xsltCompileIdKeyPattern : 1512 -> 1468
~ _xsltCompileStepPattern : 1524 -> 1484
~ _xsltScanLiteral : 512 -> 504
~ _xsltApplyXSLTTemplate : 1780 -> 1772
~ _xsltDocumentElem : 3272 -> 3252
~ _xsltCopyTree : 972 -> 944
~ _xsltApplyStylesheetInternal : 1944 -> 1952
~ _xsltParseStylesheetOutput : 1480 -> 1472
~ _xsltParseStylesheetProcess : 2560 -> 2548
~ _xsltParseStylesheetExcludePrefix : 708 -> 672
~ _xsltParseStylesheetExtPrefix : 476 -> 472
~ _xsltLoadStylesheetPI : 1476 -> 1460
~ _xsltGetQNameURI : 376 -> 384
~ _xsltGetQNameURI2 : 456 -> 448
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.W0bZjE/Sources/libxslt/libxslt/libxslt/attrvt.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.W0bZjE/Sources/libxslt/libxslt/libxslt/preproc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.W0bZjE/Sources/libxslt/libxslt/libxslt/transform.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pQzt6h/Sources/libxslt/libxslt/libxslt/attrvt.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pQzt6h/Sources/libxslt/libxslt/libxslt/preproc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pQzt6h/Sources/libxslt/libxslt/libxslt/transform.c"

```
