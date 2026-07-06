## DataDeliveryServices

> `/System/Library/PrivateFrameworks/DataDeliveryServices.framework/Versions/A/DataDeliveryServices`

```diff

-  __TEXT.__text: 0x2d54c
+  __TEXT.__text: 0x2d70c
   __TEXT.__objc_methlist: 0x2a64
   __TEXT.__const: 0x188
   __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__cstring: 0x169c
-  __TEXT.__oslogstring: 0x3d7e
-  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__cstring: 0x1690
+  __TEXT.__oslogstring: 0x3dc0
+  __TEXT.__unwind_info: 0xbd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1608
+  __DATA_CONST.__objc_selrefs: 0x1610
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__got: 0x330
+  __DATA_CONST.__got: 0x338
   __AUTH_CONST.__const: 0x1200
   __AUTH_CONST.__cfstring: 0x1960
   __AUTH_CONST.__objc_const: 0x8e10

   __DATA.__bss: 0x32
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x140
+  __DATA_DIRTY.__bss: 0x148
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1083
-  Symbols:   2979
-  CStrings:  760
+  Symbols:   2983
+  CStrings:  761
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ DDS_IS_INTERNAL_INSTALL.is_internal_install
+ _OBJC_CLASS_$_RBSAcquisitionCompletionAttribute
+ _objc_msgSend$attributeWithCompletionPolicy:
+ _os_variant_has_internal_content
Functions:
~ _DDS_IS_INTERNAL_INSTALL : 52 -> 56
~ ___DDS_IS_INTERNAL_INSTALL_block_invoke : 4 -> 40
~ -[DDSUAFManager _createRunningBoardAssertion] : 504 -> 544
~ -[DDSManager beginUpdateCycleForAssetType:forced:discretionaryDownload:] : 628 -> 740
~ -[DDSManager triggerUpdate] : 908 -> 1076
~ ___34-[DDSManager handleNewAssertions:]_block_invoke : 1008 -> 1096
CStrings:
+ "FinishTaskNow"
+ "Skip update cycle due to UAF migration for asset type: %{public}@"
- "FinishTaskUninterruptable"

```
