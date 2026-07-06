## PrintCore

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/PrintCore.framework/Versions/A/PrintCore`

```diff

-  __TEXT.__text: 0x58b3c
+  __TEXT.__text: 0x58af4
   __TEXT.__objc_methlist: 0x790
   __TEXT.__const: 0xdb9
   __TEXT.__oslogstring: 0x145b
   __TEXT.__cstring: 0x9b7f
   __TEXT.__gcc_except_tab: 0x3520
-  __TEXT.__unwind_info: 0x1938
+  __TEXT.__unwind_info: 0x1940
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1779
-  Symbols:   3172
+  Functions: 1780
+  Symbols:   3173
   CStrings:  2259
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ _PJCCreateTicketListFromPPD : 500 -> 484
~ _getMatchedMediaNameFromPaperInfo : 452 -> 464
~ __ZL11isRollMediaP17OpaquePMTicketRefPcm : 216 -> 224
~ __ZN12PrinterQuery29CreatePPDWithModifiedDefaultsEPK10__CFStringPK14__CFDictionary : 1364 -> 1372
~ __ZN7PSQuery20startProcessWithDataEPKcm : 2080 -> 2064
~ __ZN9SNMPQuery10DoOIDQueryEPPKc : 1048 -> 1036
~ __ZL4trimPc : 196 -> 172
~ __ZN9SNMPQuery15InstallableOIDSEP10ppd_file_s : 696 -> 680
~ _CPLCreateOptions : 3976 -> 3984
~ _CPLCreateOptionsStr : 976 -> 960
~ __ZL12findNextWordPcPS_h : 832 -> 824
+ _OUTLINED_FUNCTION_4
~ printToolAgent.cold.1 : 124 -> 108
~ printToolAgentMsg.cold.1 : 124 -> 108
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/AutoSetup.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/CUPSPrinter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/CUPS_CPL.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PJCPageFormat.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PJCPaper.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PJCPrintLoop.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PJCPrintSettings.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PJCPrinter.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PJCSession.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PJCUtilities.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PJCWorkflow.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PMApplication.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PMFindFolder.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PMPPD.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PMTicket.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/PSParser.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/SNMPQuery.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/TicketInternal.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSJKD0/Sources/PrintingCore/execio.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/AutoSetup.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/CUPSPrinter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/CUPS_CPL.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PJCPageFormat.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PJCPaper.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PJCPrintLoop.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PJCPrintSettings.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PJCPrinter.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PJCSession.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PJCUtilities.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PJCWorkflow.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PMApplication.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PMFindFolder.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PMPPD.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PMTicket.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/PSParser.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/SNMPQuery.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/TicketInternal.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IFBN7d/Sources/PrintingCore/execio.c"

```
