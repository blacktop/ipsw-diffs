## hangreporter

> `/usr/libexec/hangreporter`

```diff

-  __TEXT.__text: 0x40014
+  __TEXT.__text: 0x404b4
   __TEXT.__auth_stubs: 0xee0
   __TEXT.__objc_stubs: 0x2d40
   __TEXT.__objc_methlist: 0xfa4
   __TEXT.__const: 0x298
-  __TEXT.__cstring: 0x31063
+  __TEXT.__cstring: 0x315c9
   __TEXT.__oslogstring: 0x4b03
   __TEXT.__gcc_except_tab: 0xc00
   __TEXT.__objc_methname: 0x530d

   - /usr/lib/libz.1.dylib
   Functions: 701
   Symbols:   329
-  CStrings:  5745
+  CStrings:  5769
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100023e50 : 22972 -> 23444
~ sub_100029afc -> sub_100029cd4 : 52212 -> 52924
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
