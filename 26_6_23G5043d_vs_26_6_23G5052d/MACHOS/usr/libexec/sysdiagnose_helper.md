## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-  __TEXT.__text: 0x3b970
+  __TEXT.__text: 0x3be10
   __TEXT.__auth_stubs: 0xb90
   __TEXT.__objc_stubs: 0x1640
   __TEXT.__objc_methlist: 0x58c
   __TEXT.__const: 0x3c0
   __TEXT.__gcc_except_tab: 0x85c
   __TEXT.__oslogstring: 0x2407
-  __TEXT.__cstring: 0x30fc6
+  __TEXT.__cstring: 0x31481
   __TEXT.__objc_classname: 0xc2
   __TEXT.__objc_methtype: 0x2a9
   __TEXT.__objc_methname: 0x15cb

   - /usr/lib/libtzupdate.dylib
   Functions: 363
   Symbols:   253
-  CStrings:  4500
+  CStrings:  4517
 
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
~ sub_10000e0e8 : 22972 -> 23444
~ sub_100015134 -> sub_10001530c : 52212 -> 52924
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
+ "RD_CBDRwasFailedToRunQlc"
+ "RD_OptionalPORefreshAlignRegular"
+ "RD_OptionalPORefreshAlignRegularFailed"
+ "RD_RefreshOnSamplingQlc"
+ "RD_closedBandEvictCountQlc"

```
