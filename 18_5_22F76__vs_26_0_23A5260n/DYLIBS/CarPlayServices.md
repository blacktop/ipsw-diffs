## CarPlayServices

> `/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices`

```diff

-385.24.1.0.0
-  __TEXT.__text: 0x111e8
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x107c
-  __TEXT.__const: 0x246
-  __TEXT.__cstring: 0xd04
-  __TEXT.__gcc_except_tab: 0x194
-  __TEXT.__oslogstring: 0xa61
-  __TEXT.__swift5_typeref: 0x9b
-  __TEXT.__swift5_reflstr: 0x95
-  __TEXT.__swift5_assocty: 0x30
-  __TEXT.__constg_swiftt: 0xac
-  __TEXT.__swift5_fieldmd: 0x9c
-  __TEXT.__swift5_proto: 0x18
-  __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x5a8
-  __TEXT.__eh_frame: 0x180
+512.2.4.0.0
+  __TEXT.__text: 0x14660
+  __TEXT.__auth_stubs: 0x890
+  __TEXT.__objc_methlist: 0x122c
+  __TEXT.__const: 0x48e
+  __TEXT.__cstring: 0xee4
+  __TEXT.__gcc_except_tab: 0x208
+  __TEXT.__oslogstring: 0xafb
+  __TEXT.__swift5_typeref: 0x111
+  __TEXT.__swift5_reflstr: 0xb1
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__constg_swiftt: 0x128
+  __TEXT.__swift5_fieldmd: 0xec
+  __TEXT.__swift5_proto: 0x3c
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__unwind_info: 0x680
+  __TEXT.__eh_frame: 0xd8
   __TEXT.__objc_classname: 0x35a
-  __TEXT.__objc_methname: 0x2b72
+  __TEXT.__objc_methname: 0x2c6d
   __TEXT.__objc_methtype: 0x70e
-  __TEXT.__objc_stubs: 0x1b80
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x740
-  __DATA_CONST.__objc_classlist: 0x90
+  __TEXT.__objc_stubs: 0x1bc0
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x790
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa28
+  __DATA_CONST.__objc_selrefs: 0xaa0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x460
-  __AUTH_CONST.__const: 0x518
-  __AUTH_CONST.__cfstring: 0x960
-  __AUTH_CONST.__objc_const: 0x4560
-  __AUTH.__objc_data: 0xe0
-  __AUTH.__data: 0x50
+  __AUTH_CONST.__auth_got: 0x458
+  __AUTH_CONST.__const: 0x730
+  __AUTH_CONST.__cfstring: 0x9c0
+  __AUTH_CONST.__objc_const: 0x4930
+  __AUTH.__objc_data: 0x3f0
+  __AUTH.__data: 0xb0
   __DATA.__objc_ivar: 0x108
-  __DATA.__data: 0x698
-  __DATA.__bss: 0x398
-  __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__bss: 0x78
+  __DATA.__data: 0x740
+  __DATA.__bss: 0x840
+  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
+  - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 68DC573D-A84C-3409-9816-EFED7FBA9AEA
-  Functions: 494
-  Symbols:   1640
-  CStrings:  826
+  UUID: 597AB1BF-E5EF-359B-B58F-36FF41A5F086
+  Functions: 592
+  Symbols:   1707
+  CStrings:  865
 
Symbols:
+ -[CRSIconLayoutController refreshWidgetStateForVehicleID:]
+ -[CRSIconLayoutService refreshWidgetStateForVehicleID:]
+ GCC_except_table38
+ GCC_except_table4
+ _CRSNowPlayingIconIdentifier
+ _CRSWidgetLayoutStateChangedNotification
+ _OBJC_CLASS_$_CHSWidget
+ _OBJC_CLASS_$_CRSWidgetStack
+ _OBJC_CLASS_$_CRSWidgetStackRow
+ _OBJC_CLASS_$_NSValue
+ _OBJC_METACLASS_$_CRSWidgetStack
+ _OBJC_METACLASS_$_CRSWidgetStackRow
+ __CLASS_METHODS_CRSWidgetStack
+ __CLASS_METHODS_CRSWidgetStackRow
+ __CLASS_PROPERTIES_CRSWidgetStack
+ __CLASS_PROPERTIES_CRSWidgetStackRow
+ __DATA_CRSWidgetStack
+ __DATA_CRSWidgetStackRow
+ __INSTANCE_METHODS_CRSWidgetStack
+ __INSTANCE_METHODS_CRSWidgetStackRow
+ __IVARS_CRSWidgetStack
+ __IVARS_CRSWidgetStackRow
+ __METACLASS_DATA_CRSWidgetStack
+ __METACLASS_DATA_CRSWidgetStackRow
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSIconLayoutServerToClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSIconLayoutServerToClientInterface
+ __PROPERTIES_CRSWidgetStack
+ __PROPERTIES_CRSWidgetStackRow
+ __PROTOCOLS_CRSWidgetStack
+ __PROTOCOLS_CRSWidgetStack.6
+ __PROTOCOLS_CRSWidgetStackRow
+ __PROTOCOLS_CRSWidgetStackRow.7
+ ___31-[CRSIconLayoutController init]_block_invoke.70
+ ___55-[CRSIconLayoutService refreshWidgetStateForVehicleID:]_block_invoke
+ ___58-[CRSIconLayoutController refreshWidgetStateForVehicleID:]_block_invoke
+ ___85-[CRSIconLayoutController exportIconStateForCertificateSerial:categories:completion:]_block_invoke.132
+ ___block_descriptor_40_e8_32w_e42_v16?0"<BSServiceConnectionConfiguring>"8lw32l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s56l8s40l8s48l8
+ ___block_literal_global.141
+ ___block_literal_global.72
+ ___block_literal_global.82
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_memcpy0_1
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_CarPlayServices
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_CarPlayServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CarPlayServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CarPlayServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CarPlayServices
+ _associated conformance So14CRSWidgetStackC15CarPlayServicesE4KeysOSHACSQ
+ _associated conformance So17CRSWidgetStackRowC15CarPlayServicesE4KeysOSHACSQ
+ _associated conformance So25CRSWidgetSuggestionSourceVSHSCSQ
+ _objc_msgSend$listener
+ _objc_msgSend$refreshWidgetStateForVehicleID:
+ _objc_msgSend$setWidgetState:initiatedBy:
+ _swift_bridgeObjectRelease_n
+ _swift_getForeignTypeMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _symbolic SaySo7NSValueCG
+ _symbolic SaySo7NSValueCGSg
+ _symbolic Si
+ _symbolic So14CRSWidgetStackC
+ _symbolic So17CRSWidgetStackRowC
+ _symbolic _____ So14CRSWidgetStackC15CarPlayServicesE4KeysO
+ _symbolic _____ So17CRSWidgetStackRowC15CarPlayServicesE4KeysO
+ _symbolic _____ So25CRSWidgetSuggestionSourceV
- ___31-[CRSIconLayoutController init]_block_invoke.64
- ___85-[CRSIconLayoutController exportIconStateForCertificateSerial:categories:completion:]_block_invoke.129
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_literal_global.135
- ___block_literal_global.66
- ___block_literal_global.79
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_CarPlayServices
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_CarPlayServices
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_CarPlayServices
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_CarPlayServices
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_CarPlayServices
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_CarPlayServices
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_CarPlayServices
- _memcmp
- _objc_msgSend$setWidgetState:
- _objc_release_x28
- _swift_retain
- _symbolic SSSg
CStrings:
+ "@40@0:8@16@24q32"
+ "@48@0:8B16B20B24B28@32@40"
+ "CRSWidgetLayoutStateChangedNotification"
+ "CRSWidgetStack"
+ "CRSWidgetStackRow"
+ "CarPlayServices.CRSWidgetStack"
+ "CarPlayServices.CRSWidgetStackRow"
+ "Invalidating listener! %@"
+ "Received request to fetch widget state for vehicle: %{public}@"
+ "Requesting to refresh widget state for vehicle: %{public}@"
+ "Sending request to refresh widget state for vehicle: %{public}@"
+ "T@\"CHSWidget\",N,R,VchsWidget"
+ "T@\"NSArray\",N,C"
+ "TB,N,R,VshowWallpaper"
+ "TB,N,R,VsmartRotate"
+ "Tq,N,R,VsuggestionSource"
+ "_viewAreas"
+ "_widgets"
+ "chsWidget"
+ "com.apple.application-icon.now-playing"
+ "containsValueForKey:"
+ "decodeIntegerForKey:"
+ "encodeInteger:forKey:"
+ "initWithID:chsWidget:suggestionSource:"
+ "initWithID:widgets:"
+ "initWithShowWidgets:showWallpaper:showSuggestions:smartRotate:widgetStackRows:viewAreas:"
+ "initWithStacks:"
+ "refreshWidgetStateForVehicleID:"
+ "replacingViewAreas:"
+ "replacingWidgets:"
+ "setWidgetState:initiatedBy:"
+ "set_viewAreas:"
+ "set_widgets:"
+ "showWallpaper"
+ "smartRotate"
+ "stacks"
+ "suggestionSource"
+ "vehicleID"
+ "viewAreas"
+ "widget"
+ "widgetStackRows"
- "@32@0:8B16B20@24"
- "@56@0:8@16@24@32@40@48"
- "Received request for widget state for vehicle: %{public}@"
- "T@\"NSData\",N,R"
- "containerBundleIdentifier"
- "extensionBundleIdentifier"
- "initWithID:kind:extensionBundleIdentifier:containerBundleIdentifier:intentData:"
- "initWithShowWidgets:showSuggestions:widgets:"
- "intentData"
- "kind"
- "setWidgetState:"

```
