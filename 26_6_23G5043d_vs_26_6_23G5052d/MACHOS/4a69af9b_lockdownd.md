## lockdownd

> `/usr/libexec/lockdownd`

```diff

-  __TEXT.__text: 0xaac74
+  __TEXT.__text: 0xab114
   __TEXT.__auth_stubs: 0x1db0
   __TEXT.__objc_stubs: 0x15c0
   __TEXT.__objc_methlist: 0x180
-  __TEXT.__cstring: 0x3c127
+  __TEXT.__cstring: 0x3c68d
   __TEXT.__const: 0x10fc0
   __TEXT.__gcc_except_tab: 0xaf0
   __TEXT.__objc_methname: 0xf22

   - /usr/lib/libz.1.dylib
   Functions: 918
   Symbols:   637
-  CStrings:  7492
+  CStrings:  7516
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ sub_10008f5b0 : 22972 -> 23444
~ sub_1000965fc -> sub_1000967d4 : 52212 -> 52924
CStrings:
+ "ASPFTLParseBufferToCxt: RD_CBDR_requested(1342) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_CBDRwasFailedToRun(1340) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_CBDRwasFailedToRunQlc(1635) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_OptionalPORefresh(1352) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_OptionalPORefreshAlignRegular(1735) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_OptionalPORefreshAlignRegularFailed(1736) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_OptionalPORefreshFailed(1503) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_OptionalPORefreshHotBand(1433) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_OptionalPORefreshHotBandFailed(1504) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_RefreshOnSampling(1341) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_RefreshOnSamplingQlc(1636) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_closedBandEvictCountQlc(1634) cannot add 1 element to context"
+ "RD_CBDR_requested"
+ "RD_CBDRwasFailedToRun"
+ "RD_CBDRwasFailedToRunQlc"
+ "RD_OptionalPORefresh"
+ "RD_OptionalPORefreshAlignRegular"
+ "RD_OptionalPORefreshAlignRegularFailed"
+ "RD_OptionalPORefreshFailed"
+ "RD_OptionalPORefreshHotBand"
+ "RD_OptionalPORefreshHotBandFailed"
+ "RD_RefreshOnSampling"
+ "RD_RefreshOnSamplingQlc"
+ "RD_closedBandEvictCountQlc"

```
