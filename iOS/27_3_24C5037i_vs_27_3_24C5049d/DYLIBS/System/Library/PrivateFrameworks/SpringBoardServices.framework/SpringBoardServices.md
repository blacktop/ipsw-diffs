## SpringBoardServices

> `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`

```diff

-4637.2.11.104.0
-  __TEXT.__text: 0x7edf0
-  __TEXT.__objc_methlist: 0x9400
-  __TEXT.__cstring: 0xe8ab
-  __TEXT.__const: 0x808
-  __TEXT.__oslogstring: 0x52d7
-  __TEXT.__gcc_except_tab: 0xda4
+4637.2.17.3.0
+  __TEXT.__text: 0x801f0
+  __TEXT.__objc_methlist: 0x94a0
+  __TEXT.__cstring: 0xea4a
+  __TEXT.__const: 0x818
+  __TEXT.__oslogstring: 0x532b
+  __TEXT.__gcc_except_tab: 0xe18
   __TEXT.__dlopen_cstrs: 0x170
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x3e20
+  __TEXT.__unwind_info: 0x3eb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3928
+  __DATA_CONST.__const: 0x3a28
   __DATA_CONST.__objc_classlist: 0x738
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37a8
+  __DATA_CONST.__objc_selrefs: 0x3808
   __DATA_CONST.__objc_protorefs: 0x1e0
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x938
-  __AUTH_CONST.__const: 0x2a90
-  __AUTH_CONST.__cfstring: 0xb6a0
-  __AUTH_CONST.__objc_const: 0x28eb0
+  __DATA_CONST.__got: 0x940
+  __AUTH_CONST.__const: 0x2ab0
+  __AUTH_CONST.__cfstring: 0xb740
+  __AUTH_CONST.__objc_const: 0x28ef8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x868
   __AUTH.__objc_data: 0x3bd8
-  __DATA.__objc_ivar: 0x8d0
+  __DATA.__objc_ivar: 0x8d4
   __DATA.__data: 0x23f0
   __DATA_DIRTY.__objc_data: 0xc58
   __DATA_DIRTY.__data: 0x40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4551
-  Symbols:   8318
-  CStrings:  2238
+  Functions: 4579
+  Symbols:   8365
+  CStrings:  2251
 
Symbols:
+ -[SBSApplicationRestrictionState allowedWebClipIdentifiers]
+ -[SBSApplicationRestrictionState initWithAllowedIdentifiers:restrictedIdentifiers:allowedWebClipIdentifiers:]
+ -[SBSHomeScreenService addApplicationIconToHomeScreenIfAbsentWithBundleIdentifier:]
+ -[SBSSystemServiceClient homeScreenGridSizeForPageAtIndex:]
+ -[SBSSystemServiceClient isHomeScreenEditing]
+ -[SBSSystemServiceClient openHomeScreenFolderWithIdentifier:animated:completion:]
+ -[SBSSystemServiceClient setHomeScreenCurrentPageIndex:animated:]
+ -[SBSSystemServiceClient setHomeScreenEditing:]
+ -[SBSTestAutomationService homeScreenGridSizeForPageAtIndex:]
+ -[SBSTestAutomationService isHomeScreenEditing]
+ -[SBSTestAutomationService openHomeScreenFolderWithIdentifier:animated:completion:]
+ -[SBSTestAutomationService setHomeScreenCurrentPageIndex:animated:]
+ -[SBSTestAutomationService setHomeScreenEditing:]
+ GCC_except_table165
+ GCC_except_table169
+ GCC_except_table173
+ GCC_except_table213
+ GCC_except_table54
+ _OBJC_CLASS_$_NSLock
+ _OBJC_IVAR_$_SBSApplicationRestrictionState._allowedWebClipIdentifiers
+ _SBDisplayLayoutBacklightTransitionReasonFoldClosed
+ _SBDisplayLayoutTransitionReasonFlush
+ _SBSTestAutomationServiceErrorDomain
+ __SBSTestAutomationHomeScreenError
+ ___45-[SBSSystemServiceClient isHomeScreenEditing]_block_invoke
+ ___45-[SBSSystemServiceClient isHomeScreenEditing]_block_invoke_2
+ ___47-[SBSSystemServiceClient setHomeScreenEditing:]_block_invoke
+ ___47-[SBSSystemServiceClient setHomeScreenEditing:]_block_invoke_2
+ ___59-[SBSSystemServiceClient homeScreenGridSizeForPageAtIndex:]_block_invoke
+ ___59-[SBSSystemServiceClient homeScreenGridSizeForPageAtIndex:]_block_invoke_2
+ ___59-[SBSSystemServiceClient homeScreenGridSizeForPageAtIndex:]_block_invoke_3
+ ___65-[SBSSystemServiceClient setHomeScreenCurrentPageIndex:animated:]_block_invoke
+ ___65-[SBSSystemServiceClient setHomeScreenCurrentPageIndex:animated:]_block_invoke_2
+ ___65-[SBSSystemServiceClient setHomeScreenCurrentPageIndex:animated:]_block_invoke_3
+ ___81-[SBSSystemServiceClient openHomeScreenFolderWithIdentifier:animated:completion:]_block_invoke
+ ___81-[SBSSystemServiceClient openHomeScreenFolderWithIdentifier:animated:completion:]_block_invoke_2
+ ___81-[SBSSystemServiceClient openHomeScreenFolderWithIdentifier:animated:completion:]_block_invoke_3
+ ___83-[SBSTestAutomationService openHomeScreenFolderWithIdentifier:animated:completion:]_block_invoke
+ ___83-[SBSTestAutomationService openHomeScreenFolderWithIdentifier:animated:completion:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e31_v24?0"NSString"8"NSString"16ls32l8
+ ___block_descriptor_40_e8_32r_e13_v24?0{?=qq}8lr32l8
+ ___block_descriptor_40_e8_32r_e8_v12?0B8lr32l8
+ ___block_descriptor_56_e8_32s40bs48r_e30_v24?0"NSString"8"NSError"16ls32l8r48l8s40l8
+ _kSBSTestAutomationServiceMessageKeyHomeScreenErrorDescription
+ _kSBSTestAutomationServiceMessageKeyHomeScreenFolderIdentifier
+ _kSBSTestAutomationServiceMessageKeyHomeScreenGridColumns
+ _kSBSTestAutomationServiceMessageKeyHomeScreenGridRows
+ _kSBSTestAutomationServiceMessageKeyHomeScreenPageIndex
+ _kSBSTestAutomationServiceMessageKeySuccess
- -[SBSApplicationRestrictionState initWithAllowedIdentifiers:restrictedIdentifiers:]
- GCC_except_table194
CStrings:
+ "SBSHomeScreenService: failed add icon to home screen if absent request (no target)."
+ "SpringBoard did not finish opening the folder within 30 seconds."
+ "SpringBoard did not reply to the request to open a folder."
+ "allowedWebClipIdentifiers"
+ "com.apple.SpringBoard.backlight.transitionReason.foldClosed"
+ "com.apple.SpringBoard.transitionReason.flush"
+ "homeScreenErrorDescription"
+ "homeScreenFolderIdentifier"
+ "homeScreenGridColumns"
+ "homeScreenGridRows"
+ "homeScreenPageIndex"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v24@?0{?=qq}8"
```
