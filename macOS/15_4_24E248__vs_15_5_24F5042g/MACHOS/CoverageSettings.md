## CoverageSettings

> `/System/Library/ExtensionKit/Extensions/CoverageSettings.appex/Contents/MacOS/CoverageSettings`

```diff

-432.200.0.0.0
-  __TEXT.__text: 0x196a4
-  __TEXT.__auth_stubs: 0xe90
+464.120.4.501.1
+  __TEXT.__text: 0x560c
+  __TEXT.__auth_stubs: 0x720
   __TEXT.__objc_stubs: 0xe0
-  __TEXT.__objc_methlist: 0x18c
+  __TEXT.__objc_methlist: 0x174
   __TEXT.__objc_classname: 0x1e
-  __TEXT.__objc_methname: 0x524
+  __TEXT.__objc_methname: 0x2c8
   __TEXT.__objc_methtype: 0x19
-  __TEXT.__const: 0xed8
-  __TEXT.__cstring: 0xc34
-  __TEXT.__constg_swiftt: 0x850
-  __TEXT.__swift5_typeref: 0x187b
-  __TEXT.__swift5_reflstr: 0x375
-  __TEXT.__swift5_fieldmd: 0x320
-  __TEXT.__swift5_assocty: 0x108
-  __TEXT.__swift5_capture: 0x1fc
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x44
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__swift_as_entry: 0x20
-  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__const: 0x2a8
+  __TEXT.__cstring: 0x4dc
+  __TEXT.__constg_swiftt: 0x160
+  __TEXT.__swift5_typeref: 0x1e3
+  __TEXT.__swift5_reflstr: 0xc1
+  __TEXT.__swift5_fieldmd: 0x9c
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__swift5_capture: 0xf4
+  __TEXT.__oslogstring: 0x94
+  __TEXT.__swift5_proto: 0x10
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x85
-  __TEXT.__unwind_info: 0x790
-  __TEXT.__eh_frame: 0x7f0
-  __DATA_CONST.__auth_got: 0x750
-  __DATA_CONST.__got: 0x310
-  __DATA_CONST.__auth_ptr: 0x468
-  __DATA_CONST.__const: 0x7b8
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__unwind_info: 0x230
+  __TEXT.__eh_frame: 0x1b8
+  __DATA_CONST.__auth_got: 0x398
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__auth_ptr: 0x140
+  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x958
-  __DATA.__objc_selrefs: 0x1e0
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0xfa8
-  __DATA.__common: 0x10
-  __DATA.__bss: 0x9e0
-  - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
+  __DATA.__objc_const: 0x480
+  __DATA.__objc_selrefs: 0x100
+  __DATA.__objc_data: 0xa0
+  __DATA.__data: 0x2b8
+  __DATA.__common: 0x20
+  __DATA.__bss: 0x228
   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/Versions/A/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI
+  - /System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/NDOUI
   - /System/Library/PrivateFrameworks/NewDeviceOutreach.framework/Versions/A/NewDeviceOutreach
   - /System/Library/PrivateFrameworks/NewDeviceOutreachMacUI.framework/Versions/A/NewDeviceOutreachMacUI
   - /System/Library/PrivateFrameworks/Settings.framework/Versions/A/Settings

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 592
-  Symbols:   127
-  CStrings:  151
+  Functions: 133
+  Symbols:   100
+  CStrings:  73
 
Symbols:
+ _OBJC_CLASS_$_NDORequestProperties
+ _OBJC_CLASS_$_NDOUniversalLinkUtilities
- _OBJC_CLASS_$_NDODevice
- _OBJC_CLASS_$_NDODeviceInfo
- _OBJC_CLASS_$_NDODeviceSection
- _OBJC_CLASS_$_NSCachedURLResponse
- _OBJC_CLASS_$_NSImage
- _OBJC_CLASS_$_NSURLCache
- _OBJC_CLASS_$_NSURLSession
- _OBJC_CLASS_$_NSURLSessionConfiguration
- __Block_copy
- __Block_release
- __NSConcreteStackBlock
- _free
- _malloc
- _swift_allocateGenericValueMetadata
- _swift_arrayInitWithCopy
- _swift_continuation_await
- _swift_continuation_init
- _swift_continuation_resume
- _swift_defaultActor_deallocate
- _swift_defaultActor_destroy
- _swift_defaultActor_initialize
- _swift_endAccess
- _swift_errorRelease
- _swift_getAtKeyPath
- _swift_getForeignTypeMetadata
- _swift_getGenericMetadata
- _swift_getObjCClassMetadata
- _swift_isUniquelyReferenced_nonNull_bridgeObject
- _swift_storeEnumTagMultiPayload
CStrings:
+ "Cannot create AMS request, loading coverage central"
+ "Creating universal AMSUI view controller with path: %s"
+ "_amsSheetViewModel"
+ "amsViewModel"
+ "com.apple.NewDeviceOutreach"
+ "isValidPath:"
+ "revealElementKey: %s"
+ "x-apple-auth-token"
- " deepLinkParams: "
- " followup up for "
- "$defaultActor"
- "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/NewDeviceOutreachMac_Extension/CoverageSettingsPane_macOS/CCCoverageSettingsPaneModel.swift"
- "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/NewDeviceOutreachMac_Extension/CoverageSettingsPane_macOS/Device.swift"
- "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
- "Already have sheet presented. Ignoring showAMSUISheet request."
- "Failed to dismiss"
- "Not APS supported!"
- "SOMETHING_WENT_WRONG"
- "SOMETHING_WENT_WRONG_DESCRIPTION"
- "URLCache"
- "Updating warranty from NDOCoverageViewModel"
- "_TtC16CoverageSettings13DeviceSection"
- "_TtC16CoverageSettings6Device"
- "_TtCC16CoverageSettings25CoverageSettingsPaneModel15DeviceInfoCache"
- "_acOfferLabel"
- "_amsSetup"
- "_cancelShowDetailsSheet"
- "_coverageLabel"
- "_deepLinkParams"
- "_detailSheetModel"
- "_deviceInfoDict"
- "_didWillSelect"
- "_displayingDetailsForDevice"
- "_isLoadingDetails"
- "_isSheetPresented"
- "_list"
- "_originalRevealElementKey"
- "_presentDetailsSheet"
- "_sections"
- "_showAMSSheet"
- "_showEmptyContentError"
- "_warranty"
- "allLocalDevices"
- "amsDone(_:params:setup:)"
- "cachedResponseForRequest:"
- "configuration"
- "coverageDetailsView()"
- "coverageHasACLogo"
- "coverageLocalizedLabel"
- "data"
- "defaultDevice"
- "defaultSessionConfiguration"
- "device"
- "deviceImageUrl"
- "deviceList"
- "dict"
- "dismissFollowUpForSerialNumber:completion:"
- "getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:"
- "id"
- "initWithData:"
- "initWithResponse:data:"
- "isAPSSupported"
- "isAPSSupportedOverrideWithServerValue:"
- "isAppleID"
- "isVisibleInCC"
- "label"
- "labelVerbatim"
- "name"
- "ndoDevice"
- "pairedBTDevices"
- "productPlaceholderImage"
- "refresh(usingPolicy:withParams:salesInfoReply:)"
- "revealElement(forKey:)"
- "serialNumber"
- "sessionWithConfiguration:"
- "setURLCache:"
- "showAMSUISheet(_:)"
- "showCoverageDetails_link"
- "showSales is false, dropping link"
- "sourceFromDeviceType"
- "storeCachedResponse:forRequest:"
- "ulWebURLOverride:"
- "ulWebURLOverride: "
- "usingDeviceList policy: "
- "uuid"
- "v12@?0B8"
- "v16@?0@\"NSArray\"8"
- "v16@?0@\"NSString\"8"
- "v32@?0@\"NSString\"8@\"NSArray\"16@\"NSString\"24"
- "warranty"
- "willSelect(revealElementKey:)"

```
