## Lookup

> `/System/Library/PrivateFrameworks/Lookup.framework/Versions/A/Lookup`

```diff

-312.0.0.0.0
-  __TEXT.__text: 0xebe0
+312.1.0.0.0
+  __TEXT.__text: 0xec08
   __TEXT.__auth_stubs: 0x400
   __TEXT.__delay_helper: 0x29c
-  __TEXT.__objc_methlist: 0xacc
+  __TEXT.__objc_methlist: 0x1254
+  __TEXT.__const: 0x98
   __TEXT.__gcc_except_tab: 0x4f4
-  __TEXT.__const: 0x90
   __TEXT.__cstring: 0xd3f
   __TEXT.__ustring: 0x16
   __TEXT.__unwind_info: 0x3e8

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc60
+  __DATA_CONST.__objc_selrefs: 0xfc0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__const: 0x3d0
   __AUTH_CONST.__cfstring: 0xbc0
-  __AUTH_CONST.__objc_const: 0x2450
+  __AUTH_CONST.__objc_const: 0x1608
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED05308E-5674-3805-850D-4ACAAFB6DC49
+  UUID: 14B1C90F-A984-3BF7-828C-399E5FA053F9
   Functions: 260
   Symbols:   1122
   CStrings:  948
Functions:
~ -[LULookupDefinitionModule lookupAnimationControllerForString:range:options:originProvider:inView:] : 1108 -> 1100
~ ___62+[LULogging logType:method:arguments:returnKeys:returnValues:]_block_invoke : 196 -> 204
~ __62+[LULogging logType:method:arguments:returnKeys:returnValues:]_block_invoke.32 : 196 -> 204
~ +[LULogging shouldLog:] : 220 -> 212
~ -[LUPresenter animationControllerForTerm:relativeToRect:ofView:options:] : 1508 -> 1512
~ -[LULookupRemoteViewController burnViewBridge] : 168 -> 164
~ -[LUPresenter commonLUPresenterTeardown] : 28 -> 32
~ +[LUPresenter positioningView:andRect:forTerm:atLocation:options:] : 1376 -> 1392
~ -[LULookupDefinitionModule showDefinitionByHotKey] : 376 -> 380
~ -[LULookupDefinitionModule showDefinitionForString:range:options:originProvider:inView:] : 1544 -> 1536
~ _LUCanConnectToService : 68 -> 72
~ +[LUTextAccessor rangeOfTermInString:containingOffset:] : 932 -> 936
~ -[LUAccessibilityTextAccessor termForRange:textOrigin:] : 1808 -> 1804
~ __TSMDocumentAccessGetLength : 196 -> 188
~ _GetAttributedStringForRange : 1088 -> 1080
~ -[LUWebFrameViewTextAccessor termForRange:textOrigin:] : 2668 -> 2692
~ +[LUWebFrameViewTextAccessor paragraphContainingNode:] : 912 -> 916
~ +[LUWebFrameViewTextAccessor DOMRangeFromNSRange:domNode:representation:] : 2684 -> 2700
~ +[LULookupDefinitionModule tokenRangeForString:range:options:] : 752 -> 744

```
