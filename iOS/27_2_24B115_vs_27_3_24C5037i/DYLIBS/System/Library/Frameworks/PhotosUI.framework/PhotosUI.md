## PhotosUI

> `/System/Library/Frameworks/PhotosUI.framework/PhotosUI`

```diff

-916.57.153.0.0
-  __TEXT.__text: 0x4460c
-  __TEXT.__objc_methlist: 0x401c
-  __TEXT.__const: 0x30c8
+920.7.110.0.0
+  __TEXT.__text: 0x44a74
+  __TEXT.__objc_methlist: 0x4074
+  __TEXT.__const: 0x30d8
   __TEXT.__constg_swiftt: 0xe04
   __TEXT.__swift5_typeref: 0xd1a
-  __TEXT.__swift5_reflstr: 0xbe1
-  __TEXT.__swift5_fieldmd: 0xcc0
   __TEXT.__swift5_builtin: 0x168
+  __TEXT.__swift5_reflstr: 0xbe6
+  __TEXT.__swift5_fieldmd: 0xcc0
   __TEXT.__swift5_assocty: 0x348
-  __TEXT.__cstring: 0x4d63
-  __TEXT.__oslogstring: 0x1449
-  __TEXT.__swift5_capture: 0x5a0
   __TEXT.__swift5_proto: 0x1a0
   __TEXT.__swift5_types: 0x128
+  __TEXT.__cstring: 0x4e17
+  __TEXT.__oslogstring: 0x1665
+  __TEXT.__swift5_capture: 0x5a0
   __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x3c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift_as_ret: 0xc
-  __TEXT.__gcc_except_tab: 0x290
-  __TEXT.__unwind_info: 0x21e8
+  __TEXT.__gcc_except_tab: 0x294
+  __TEXT.__unwind_info: 0x2210
   __TEXT.__eh_frame: 0x8b4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2248
+  __DATA_CONST.__objc_selrefs: 0x2260
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x688
+  __DATA_CONST.__got: 0x680
   __AUTH_CONST.__const: 0x2358
-  __AUTH_CONST.__cfstring: 0x22e0
-  __AUTH_CONST.__objc_const: 0x7368
+  __AUTH_CONST.__cfstring: 0x2340
+  __AUTH_CONST.__objc_const: 0x7400
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xb98
+  __AUTH_CONST.__auth_got: 0xbc0
   __AUTH.__objc_data: 0x2110
-  __AUTH.__data: 0x808
-  __DATA.__objc_ivar: 0x33c
-  __DATA.__data: 0x1d68
+  __AUTH.__data: 0x818
+  __DATA.__objc_ivar: 0x348
+  __DATA.__data: 0x1d80
   __DATA.__common: 0x241
   __DATA_DIRTY.__objc_data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3096
-  Symbols:   3042
-  CStrings:  574
+  Functions: 3102
+  Symbols:   3051
+  CStrings:  578
 
Symbols:
+ -[PHPickerConfiguration _setTertiaryButtonType:]
+ -[PHPickerConfiguration _tertiaryButtonType]
+ -[PHPickerUpdateConfiguration _didSetTertiaryButtonType]
+ -[PHPickerUpdateConfiguration _setTertiaryButtonType:]
+ -[PHPickerUpdateConfiguration _tertiaryButtonType]
+ GCC_except_table100
+ GCC_except_table19
+ GCC_except_table3
+ GCC_except_table492
+ GCC_except_table502
+ GCC_except_table505
+ GCC_except_table507
+ GCC_except_table52
+ GCC_except_table674
+ GCC_except_table765
+ GCC_except_table770
+ GCC_except_table774
+ GCC_except_table778
+ GCC_except_table955
+ _OBJC_IVAR_$_PHPickerConfiguration.__tertiaryButtonType
+ _OBJC_IVAR_$_PHPickerUpdateConfiguration.__didSetTertiaryButtonType
+ _OBJC_IVAR_$_PHPickerUpdateConfiguration.__tertiaryButtonType
+ _PLCurrentLibraryLogTag
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PHPickerViewControllerDelegate_Private
- GCC_except_table157
- GCC_except_table368
- GCC_except_table399
- GCC_except_table404
- GCC_except_table408
- GCC_except_table412
- GCC_except_table430
- GCC_except_table500
- GCC_except_table523
- GCC_except_table880
- GCC_except_table890
- GCC_except_table893
- GCC_except_table895
- GCC_except_table974
- _OUTLINED_FUNCTION_90
CStrings:
+ "%{public}s%s Error %@"
+ "%{public}s%s Unable to copy data with error: %@"
+ "%{public}s%s Unable to copy from %@ to %@ %@"
+ "%{public}s%s Unable to create crop rect %@"
+ "%{public}s%s Unable to create debug sidecar files %@"
+ "%{public}s%s Unable to create edited image %@"
+ "%{public}s%s Unable to create fullScreenImage %@"
+ "%{public}s%s Unable to create image %@"
+ "%{public}s%s Unable to create live photo - %@"
+ "%{public}sCan't find item provider representation for the progress URL."
+ "%{public}sCan't find progress URL or its sandbox extension token."
+ "%{public}sCopied to URL (%@) (loadInPlaceFileRepresentationForTypeIdentifier:)"
+ "%{public}sCopying URL (%@) because (old SDK: %ld, explicit: %ld) (loadInPlaceFileRepresentationForTypeIdentifier:)"
+ "%{public}sCouldn't present cloud sync controls; view controller is nil."
+ "%{public}sError getting synchronous remote object proxy: %@"
+ "%{public}sFailed to access application key window, unable to present library picker"
+ "%{public}sFailed to access application top most view controller, unable to present library picker"
+ "%{public}sFailed to determine root view controller"
+ "%{public}sIgnored progress updates for local progress (%@) because it's already cancelled."
+ "%{public}sLimited library picker done"
+ "%{public}sLimited library picker requires PHAuthorizationStatusLimited"
+ "%{public}sNo matching local progress is found for remote progress (%@) with UUID (%@)."
+ "%{public}sPHPickerViewControllerDelegate doesn't respond to picker:didFinishPicking:"
+ "%{public}sPUPhotosFileProviderItemProvider: loadDataRepresentationForTypeIdentifier: %@"
+ "%{public}sPUPhotosFileProviderItemProvider: loadFileRepresentationForTypeIdentifier: %@"
+ "%{public}sPUPhotosFileProviderItemProvider: loadInPlaceFileRepresentationForTypeIdentifier: %@"
+ "%{public}sPUPhotosFileProviderItemProvider: loadObjectOfClass: %@"
+ "%{public}sPUPickerAssetMediaSubtypeFilter: invalid filter type: %ld"
+ "%{public}sPUPickerAssetMediaTypeFilter: invalid media type: %ld"
+ "%{public}sPUPickerAssetPlaybackStyleFilter: invalid playback style: %ld"
+ "%{public}sPUPickerCompoundFilter: invalid filter type: %ld"
+ "%{public}sPUPickerCompoundFilter: invalid subfilter: %@"
+ "%{public}sPUPickerCompoundFilter: invalid subfilters count: %lu"
+ "%{public}sPUPickerGroupsPeopleQuantityFilter: invalid member count range: [%ld, %ld]"
+ "%{public}sPUPickerItemIdentifiersFilter: invalid asset identifier count: %ld"
+ "%{public}sPUPickerOtherFilter: invalid filter type: %ld"
+ "%{public}sPreparing to show limited library picker"
+ "%{public}sPresented limited library dismissed"
+ "%{public}sPresented limited library picker"
+ "%{public}sReceived invalid object (%@) or keypath (%@) for the progress context."
+ "%{public}sShowing picker unavailable UI (reason: %@) with error: %@"
+ "%{public}sShowing picker unavailable UI (updated) (reason: %@) with error: %@"
+ "%{public}s[Limited Library Picker] picker: %@ didFinishPicking: %@"
+ "%{public}s[Limited Library Picker] presentationControllerDidDismiss: %@"
+ "%{public}sloadInPlaceFileRepresentationForTypeIdentifier: is not supported. Use loadFileRepresentationForTypeIdentifier: instead."
+ "%{public}slower selection limit is negative"
+ "%{public}sprimary button type is negative"
+ "%{public}ssecondary button type is negative"
+ "%{public}sselection limit is negative"
+ "%{public}stertiary button type is negative"
+ "PHPickerConfigurationCoderTertiaryButtonTypeKey"
+ "PHPickerUpdateConfigurationCoderDidSetTertiaryButtonTypeKey"
+ "PHPickerUpdateConfigurationCoderTertiaryButtonTypeKey"
+ "QEg"
+ "configuration._tertiaryButtonType >= 0"
- "%s Error %@"
- "%s Unable to copy data with error: %@"
- "%s Unable to copy from %@ to %@ %@"
- "%s Unable to create crop rect %@"
- "%s Unable to create debug sidecar files %@"
- "%s Unable to create edited image %@"
- "%s Unable to create fullScreenImage %@"
- "%s Unable to create image %@"
- "%s Unable to create live photo - %@"
- "CFBundleDisplayName"
- "Can't find item provider representation for the progress URL."
- "Can't find progress URL or its sandbox extension token."
- "Copied to URL (%@) (loadInPlaceFileRepresentationForTypeIdentifier:)"
- "Copying URL (%@) because (old SDK: %ld, explicit: %ld) (loadInPlaceFileRepresentationForTypeIdentifier:)"
- "Couldn't present cloud sync controls; view controller is nil."
- "Error getting synchronous remote object proxy: %@"
- "Failed to access application key window, unable to present library picker"
- "Failed to access application top most view controller, unable to present library picker"
- "Failed to determine root view controller"
- "Ignored progress updates for local progress (%@) because it's already cancelled."
- "Limited library picker done"
- "Limited library picker requires PHAuthorizationStatusLimited"
- "No matching local progress is found for remote progress (%@) with UUID (%@)."
- "PHPickerViewControllerDelegate doesn't respond to picker:didFinishPicking:"
- "PUPhotosFileProviderItemProvider: loadDataRepresentationForTypeIdentifier: %@"
- "PUPhotosFileProviderItemProvider: loadFileRepresentationForTypeIdentifier: %@"
- "PUPhotosFileProviderItemProvider: loadInPlaceFileRepresentationForTypeIdentifier: %@"
- "PUPhotosFileProviderItemProvider: loadObjectOfClass: %@"
- "PUPickerAssetMediaSubtypeFilter: invalid filter type: %ld"
- "PUPickerAssetMediaTypeFilter: invalid media type: %ld"
- "PUPickerAssetPlaybackStyleFilter: invalid playback style: %ld"
- "PUPickerCompoundFilter: invalid filter type: %ld"
- "PUPickerCompoundFilter: invalid subfilter: %@"
- "PUPickerCompoundFilter: invalid subfilters count: %lu"
- "PUPickerGroupsPeopleQuantityFilter: invalid member count range: [%ld, %ld]"
- "PUPickerItemIdentifiersFilter: invalid asset identifier count: %ld"
- "PUPickerOtherFilter: invalid filter type: %ld"
- "Preparing to show limited library picker"
- "Presented limited library dismissed"
- "Presented limited library picker"
- "QEW"
- "Received invalid object (%@) or keypath (%@) for the progress context."
- "Showing picker unavailable UI (reason: %@) with error: %@"
- "Showing picker unavailable UI (updated) (reason: %@) with error: %@"
- "[Limited Library Picker] picker: %@ didFinishPicking: %@"
- "[Limited Library Picker] presentationControllerDidDismiss: %@"
- "loadInPlaceFileRepresentationForTypeIdentifier: is not supported. Use loadFileRepresentationForTypeIdentifier: instead."
- "lower selection limit is negative"
- "primary button type is negative"
- "secondary button type is negative"
- "selection limit is negative"
```
