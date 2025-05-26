## AmbientUI

> `/System/Library/PrivateFrameworks/AmbientUI.framework/AmbientUI`

```diff

-52.8.0.0.0
-  __TEXT.__text: 0x2da2c
+52.104.0.0.0
+  __TEXT.__text: 0x2db98
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x3424
+  __TEXT.__objc_methlist: 0x3444
   __TEXT.__const: 0x624
   __TEXT.__gcc_except_tab: 0x36c
   __TEXT.__cstring: 0x1add
-  __TEXT.__oslogstring: 0x198e
+  __TEXT.__oslogstring: 0x19cb
   __TEXT.__dlopen_cstrs: 0x110
-  __TEXT.__unwind_info: 0xe7c
+  __TEXT.__unwind_info: 0xe80
   __TEXT.__objc_classname: 0xc09
-  __TEXT.__objc_methname: 0xfd53
-  __TEXT.__objc_methtype: 0x527e
-  __TEXT.__objc_stubs: 0x9280
+  __TEXT.__objc_methname: 0xfe01
+  __TEXT.__objc_methtype: 0x52ab
+  __TEXT.__objc_stubs: 0x92a0
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0xb60
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe460
-  __DATA_CONST.__objc_selrefs: 0x2d08
+  __DATA_CONST.__objc_const: 0xe4a0
+  __DATA_CONST.__objc_selrefs: 0x2d20
+  __DATA_CONST.__objc_classrefs: 0x570
+  __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x1ca0

   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x420
-  __AUTH.__objc_data: 0xb90
-  __DATA.__objc_classrefs: 0x570
-  __DATA.__objc_superrefs: 0x148
+  __AUTH.__objc_data: 0xb40
   __DATA.__objc_ivar: 0x4a4
   __DATA.__data: 0x14a0
   __DATA.__bss: 0xf8
-  __DATA_DIRTY.__objc_data: 0x3c0
+  __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1345
-  Symbols:   5465
-  CStrings:  3146
+  Functions: 1348
+  Symbols:   5472
+  CStrings:  3152
 
Symbols:
+ -[AMUIAmbientViewController posterSwitcherViewController:requestsLastSelectedConfigurationUUIDForProviderBundleIdentifier:]
+ -[AMUIAmbientViewController posterSwitcherViewController:willSwitchFromConfiguration:interactive:]
+ -[AMUIInfographViewController iconManager:iconViewDisplaysLabel:]
+ -[AMUIInfographViewController stackConfigurationInteractionShouldDisallowLabelArea:]
+ GCC_except_table100
+ GCC_except_table128
+ GCC_except_table151
+ GCC_except_table155
+ GCC_except_table160
+ GCC_except_table74
+ GCC_except_table76
+ _objc_msgSend$posterSwitcherViewController:requestsLastSelectedConfigurationUUIDForProviderBundleIdentifier:
+ _objc_msgSend$posterSwitcherViewController:willSwitchFromConfiguration:interactive:
- -[AMUIAmbientViewController posterSwitcherViewController:requestsLastSelectedConfigurationUUIDForProviderBundleIdentfier:]
- GCC_except_table126
- GCC_except_table149
- GCC_except_table153
- GCC_except_table158
- GCC_except_table73
- GCC_except_table75
- GCC_except_table98
- _objc_msgSend$posterSwitcherViewController:requestsLastSelectedConfigurationUUIDForProviderBundleIdentfier:
CStrings:
+ "B24@0:8@\"SBHStackConfigurationInteraction\"16"
+ "T@\"NSString\",?,R,C"
+ "T@\"SBHAppLibraryVisualConfiguration\",?,R,C,N"
+ "T@\"SBHFloatingDockVisualConfiguration\",?,R,C,N"
+ "T@\"SBHFloatyFolderVisualConfiguration\",?,R,C,N"
+ "T@\"SBHFolderIconVisualConfiguration\",?,R,C,N"
+ "T@\"SBHIconAccessoryVisualConfiguration\",?,R,C,N"
+ "T@\"SBHRootFolderVisualConfiguration\",?,R,C,N"
+ "T@\"SBHSidebarVisualConfiguration\",?,R,C,N"
+ "T@\"UIViewController\",?,R,N"
+ "TB,?,R,N"
+ "TQ,?,R,N"
+ "Td,?,R,N"
+ "T{SBHIconGridSizeClassSizes={SBHIconGridSize=SS}{SBHIconGridSize=SS}{SBHIconGridSize=SS}{SBHIconGridSize=SS}{SBHIconGridSize=SS}},?,R,N"
+ "T{UIEdgeInsets=dddd},?,R,N"
+ "posterSwitcherViewController:requestsLastSelectedConfigurationUUIDForProviderBundleIdentifier:"
+ "posterSwitcherViewController:willSwitchFromConfiguration:interactive:"
+ "stackConfigurationInteractionShouldDisallowLabelArea:"
+ "switcher willSwitchFromConfiguration:%@ interactive:%{BOOL}u"
- "T@\"SBHAppLibraryVisualConfiguration\",R,C,N"
- "T@\"SBHFloatingDockVisualConfiguration\",R,C,N"
- "T@\"SBHFloatyFolderVisualConfiguration\",R,C,N"
- "T@\"SBHFolderIconVisualConfiguration\",R,C,N"
- "T@\"SBHIconAccessoryVisualConfiguration\",R,C,N"
- "T@\"SBHRootFolderVisualConfiguration\",R,C,N"
- "T@\"SBHSidebarVisualConfiguration\",R,C,N"
- "T@\"UIViewController\",R,N"
- "TB,R,N"
- "TQ,R,N"
- "T{SBHIconGridSizeClassSizes={SBHIconGridSize=SS}{SBHIconGridSize=SS}{SBHIconGridSize=SS}{SBHIconGridSize=SS}{SBHIconGridSize=SS}},R,N"
- "T{UIEdgeInsets=dddd},R,N"
- "posterSwitcherViewController:requestsLastSelectedConfigurationUUIDForProviderBundleIdentfier:"

```
