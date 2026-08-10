## MobileMailUI

> `/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3897.100.8.2.5
-  __TEXT.__text: 0x4e444
-  __TEXT.__objc_methlist: 0x517c
-  __TEXT.__gcc_except_tab: 0x983c
+3901.100.1.2.7
+  __TEXT.__text: 0x4ec5c
+  __TEXT.__objc_methlist: 0x5314
+  __TEXT.__gcc_except_tab: 0x9938
   __TEXT.__cstring: 0x349c
   __TEXT.__ustring: 0x318
-  __TEXT.__const: 0x84f4
+  __TEXT.__const: 0x8514
   __TEXT.__oslogstring: 0x2397
   __TEXT.__dlopen_cstrs: 0x97
   __TEXT.__swift5_typeref: 0x2a2

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x28
-  __TEXT.__unwind_info: 0x2a08
+  __TEXT.__unwind_info: 0x2a80
   __TEXT.__eh_frame: 0x1b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1378
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41a0
+  __DATA_CONST.__objc_selrefs: 0x4250
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0xe8
-  __DATA_CONST.__got: 0xb48
+  __DATA_CONST.__got: 0xb50
   __AUTH_CONST.__const: 0x730
   __AUTH_CONST.__cfstring: 0x31a0
-  __AUTH_CONST.__objc_const: 0x7d48
+  __AUTH_CONST.__objc_const: 0x8028
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__auth_got: 0x898
-  __AUTH.__objc_data: 0x9c0
+  __AUTH.__objc_data: 0xa60
   __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x4bc
+  __DATA.__objc_ivar: 0x4dc
   __DATA.__data: 0x1158
   __DATA.__bss: 0x48
   __DATA.__common: 0x78

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1737
-  Symbols:   5078
+  Functions: 1767
+  Symbols:   5145
   CStrings:  682
 
Symbols:
+ +[MFPopoverConfiguration new]
+ +[MFPopoverConfigurationRequest new]
+ -[MFMessageDisplayMetrics mailActionCardPreferredHeightForRegularOnlyEnvironment]
+ -[MFMessageDisplayMetrics mailCardMinimumPopoverLayoutMargin]
+ -[MFMessageDisplayMetrics popoverConfigurationForRequest:]
+ -[MFPopoverConfiguration applyToViewController:]
+ -[MFPopoverConfiguration initWithCoder:]
+ -[MFPopoverConfiguration initWithPreferredContentSize:popoverLayoutMargins:]
+ -[MFPopoverConfiguration init]
+ -[MFPopoverConfiguration popoverLayoutMargins]
+ -[MFPopoverConfiguration preferredContentSize]
+ -[MFPopoverConfiguration setPopoverLayoutMargins:]
+ -[MFPopoverConfiguration setPreferredContentSize:]
+ -[MFPopoverConfigurationRequest .cxx_destruct]
+ -[MFPopoverConfigurationRequest approximateMinimumHeightNeededForAccessibilityContentSizeCategory]
+ -[MFPopoverConfigurationRequest containerSize]
+ -[MFPopoverConfigurationRequest initWithCoder:]
+ -[MFPopoverConfigurationRequest initWithContainerSize:presentingViewSize:popoverLayoutMargins:approximateMinimumHeightNeededForAccessibilityContentSizeCategory:sourceItem:containerTraitCollection:]
+ -[MFPopoverConfigurationRequest initWithContainerSize:presentingViewSize:popoverLayoutMargins:approximateMinimumHeightNeededForAccessibilityContentSizeCategory:sourceItem:isInRegularOnlyEnvironment:]
+ -[MFPopoverConfigurationRequest init]
+ -[MFPopoverConfigurationRequest isInRegularOnlyEnvironment]
+ -[MFPopoverConfigurationRequest popoverLayoutMargins]
+ -[MFPopoverConfigurationRequest presentingViewSize]
+ -[MFPopoverConfigurationRequest setApproximateMinimumHeightNeededForAccessibilityContentSizeCategory:]
+ -[MFPopoverConfigurationRequest setContainerSize:]
+ -[MFPopoverConfigurationRequest setIsInRegularOnlyEnvironment:]
+ -[MFPopoverConfigurationRequest setPopoverLayoutMargins:]
+ -[MFPopoverConfigurationRequest setPresentingViewSize:]
+ -[MFPopoverConfigurationRequest setSourceItem:]
+ -[MFPopoverConfigurationRequest sourceItem]
+ _OBJC_CLASS_$_MFPopoverConfiguration
+ _OBJC_CLASS_$_MFPopoverConfigurationRequest
+ _OBJC_IVAR_$_MFPopoverConfiguration._popoverLayoutMargins
+ _OBJC_IVAR_$_MFPopoverConfiguration._preferredContentSize
+ _OBJC_IVAR_$_MFPopoverConfigurationRequest._approximateMinimumHeightNeededForAccessibilityContentSizeCategory
+ _OBJC_IVAR_$_MFPopoverConfigurationRequest._containerSize
+ _OBJC_IVAR_$_MFPopoverConfigurationRequest._isInRegularOnlyEnvironment
+ _OBJC_IVAR_$_MFPopoverConfigurationRequest._popoverLayoutMargins
+ _OBJC_IVAR_$_MFPopoverConfigurationRequest._presentingViewSize
+ _OBJC_IVAR_$_MFPopoverConfigurationRequest._sourceItem
+ _OBJC_METACLASS_$_MFPopoverConfiguration
+ _OBJC_METACLASS_$_MFPopoverConfigurationRequest
+ __OBJC_$_CLASS_METHODS_MFPopoverConfiguration
+ __OBJC_$_CLASS_METHODS_MFPopoverConfigurationRequest
+ __OBJC_$_INSTANCE_METHODS_MFPopoverConfiguration
+ __OBJC_$_INSTANCE_METHODS_MFPopoverConfigurationRequest
+ __OBJC_$_INSTANCE_VARIABLES_MFPopoverConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_MFPopoverConfigurationRequest
+ __OBJC_$_PROP_LIST_MFPopoverConfiguration
+ __OBJC_$_PROP_LIST_MFPopoverConfigurationRequest
+ __OBJC_CLASS_RO_$_MFPopoverConfiguration
+ __OBJC_CLASS_RO_$_MFPopoverConfigurationRequest
+ __OBJC_METACLASS_RO_$_MFPopoverConfiguration
+ __OBJC_METACLASS_RO_$_MFPopoverConfigurationRequest
+ _objc_msgSend$approximateMinimumHeightNeededForAccessibilityContentSizeCategory
+ _objc_msgSend$containerSize
+ _objc_msgSend$initWithContainerSize:presentingViewSize:popoverLayoutMargins:approximateMinimumHeightNeededForAccessibilityContentSizeCategory:sourceItem:isInRegularOnlyEnvironment:
+ _objc_msgSend$initWithPreferredContentSize:popoverLayoutMargins:
+ _objc_msgSend$isInRegularOnlyEnvironment
+ _objc_msgSend$mailActionCardPreferredHeightForRegularOnlyEnvironment
+ _objc_msgSend$mailCardMinimumPopoverLayoutMargin
+ _objc_msgSend$popoverLayoutMargins
+ _objc_msgSend$preferredContentSize
+ _objc_msgSend$presentingViewSize
+ _objc_msgSend$setCanOverlapSourceViewRect:
+ _objc_msgSend$setPopoverLayoutMargins:
+ _objc_msgSend$setPreferredContentSize:
```
