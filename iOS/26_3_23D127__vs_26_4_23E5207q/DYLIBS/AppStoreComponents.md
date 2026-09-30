## AppStoreComponents

> `/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents`

```diff

-8.3.1.0.0
-  __TEXT.__text: 0x8df24
-  __TEXT.__auth_stubs: 0x18b0
-  __TEXT.__objc_methlist: 0x8644
-  __TEXT.__const: 0x1fa4
-  __TEXT.__cstring: 0x3d12
-  __TEXT.__oslogstring: 0x2fdd
-  __TEXT.__gcc_except_tab: 0xa04
+8.4.11.0.0
+  __TEXT.__text: 0x92da4
+  __TEXT.__auth_stubs: 0x1830
+  __TEXT.__objc_methlist: 0x8634
+  __TEXT.__const: 0x2174
+  __TEXT.__cstring: 0x365b
+  __TEXT.__oslogstring: 0x2fac
+  __TEXT.__gcc_except_tab: 0x9ac
   __TEXT.__dlopen_cstrs: 0x14f
-  __TEXT.__constg_swiftt: 0x700
-  __TEXT.__swift5_typeref: 0x450
-  __TEXT.__swift5_fieldmd: 0xc58
+  __TEXT.__constg_swiftt: 0x7a0
+  __TEXT.__swift5_typeref: 0x470
+  __TEXT.__swift5_fieldmd: 0xd40
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0xdc0
-  __TEXT.__swift5_assocty: 0x1e0
-  __TEXT.__swift5_proto: 0x108
-  __TEXT.__swift5_types: 0xac
+  __TEXT.__swift5_reflstr: 0xed0
+  __TEXT.__swift5_assocty: 0x1f8
+  __TEXT.__swift5_proto: 0x120
+  __TEXT.__swift5_types: 0xbc
   __TEXT.__swift5_capture: 0x220
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x2580
-  __TEXT.__objc_classname: 0x113e
-  __TEXT.__objc_methname: 0x11d8c
-  __TEXT.__objc_methtype: 0x330b
-  __TEXT.__objc_stubs: 0xc900
+  __TEXT.__unwind_info: 0x25e0
+  __TEXT.__objc_classname: 0x1402
+  __TEXT.__objc_methname: 0x12053
+  __TEXT.__objc_methtype: 0x35f7
+  __TEXT.__objc_stubs: 0xc9c0
   __DATA_CONST.__got: 0x830
-  __DATA_CONST.__const: 0x18e0
+  __DATA_CONST.__const: 0x18f0
   __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ca0
+  __DATA_CONST.__objc_selrefs: 0x3ce0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x418
+  __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0xc68
-  __AUTH_CONST.__const: 0x1d90
-  __AUTH_CONST.__cfstring: 0x49e0
-  __AUTH_CONST.__objc_const: 0xed20
+  __AUTH_CONST.__auth_got: 0xc28
+  __AUTH_CONST.__const: 0x1eb8
+  __AUTH_CONST.__cfstring: 0x4aa0
+  __AUTH_CONST.__objc_const: 0xee90
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x5b0
-  __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x804
-  __DATA.__data: 0x1c40
-  __DATA.__bss: 0x1b10
+  __AUTH.__data: 0x180
+  __DATA.__objc_ivar: 0x818
+  __DATA.__data: 0x1d90
+  __DATA.__bss: 0x1e10
   __DATA.__common: 0x160
-  __DATA_DIRTY.__objc_data: 0x25f0
-  __DATA_DIRTY.__data: 0x9a8
-  __DATA_DIRTY.__bss: 0x918
+  __DATA_DIRTY.__objc_data: 0x25a0
+  __DATA_DIRTY.__data: 0x9e0
+  __DATA_DIRTY.__bss: 0x920
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3CFA8F94-F6C8-3A67-9049-D1FAE177B3DF
-  Functions: 3654
-  Symbols:   10734
-  CStrings:  4985
+  UUID: 4920F330-E71E-34EF-80C9-F863118E68E2
+  Functions: 3692
+  Symbols:   10769
+  CStrings:  4996
 
Symbols:
+ +[ASCEligibility isFreeform:]
+ +[ASCIconTextOfferMetadata supportsSecureCoding]
+ +[ASCOfferMetadata offerMetadataWithTitle:subtitle:imageName:]
+ +[ASCOfferMetadata resumeMetadata:]
+ -[ASCAppOffer initWithID:titles:subtitles:flags:ageRating:metrics:baseBuyParams:metricsBuyParams:metricsOverlay:additionalHeaders:preflightPackageURL:bundleID:itemName:vendorName:capabilities:]
+ -[ASCAppOffer metricsOverlay]
+ -[ASCIconTextOfferMetadata .cxx_destruct]
+ -[ASCIconTextOfferMetadata animationName]
+ -[ASCIconTextOfferMetadata baseImageName]
+ -[ASCIconTextOfferMetadata description]
+ -[ASCIconTextOfferMetadata encodeWithCoder:]
+ -[ASCIconTextOfferMetadata hash]
+ -[ASCIconTextOfferMetadata imageNameForSize:]
+ -[ASCIconTextOfferMetadata initWithCoder:]
+ -[ASCIconTextOfferMetadata initWithCoder:].cold.1
+ -[ASCIconTextOfferMetadata initWithCoder:].cold.2
+ -[ASCIconTextOfferMetadata initWithTitle:subtitle:imageName:animationName:]
+ -[ASCIconTextOfferMetadata isEqual:]
+ -[ASCIconTextOfferMetadata isIconOnly]
+ -[ASCIconTextOfferMetadata isTextAndIcon]
+ -[ASCIconTextOfferMetadata isTextOnly]
+ -[ASCIconTextOfferMetadata subtitle]
+ -[ASCIconTextOfferMetadata title]
+ -[ASCOfferButton backgroundView]
+ -[ASCOfferMetadata isIconOnly]
+ -[ASCOfferMetadata isTextAndIcon]
+ -[ASCOfferMetadata isTextOnly]
+ _ASCLockupContextSpringboard
+ _OBJC_CLASS_$_ASCIconTextOfferMetadata
+ _OBJC_IVAR_$_ASCAppOffer._metricsOverlay
+ _OBJC_IVAR_$_ASCIconTextOfferMetadata._animationName
+ _OBJC_IVAR_$_ASCIconTextOfferMetadata._baseImageName
+ _OBJC_IVAR_$_ASCIconTextOfferMetadata._subtitle
+ _OBJC_IVAR_$_ASCIconTextOfferMetadata._title
+ _OBJC_IVAR_$_ASCOfferButton._backgroundView
+ _OBJC_IVAR_$_ASCOfferMetadata._icon
+ _OBJC_IVAR_$_ASCOfferMetadata._iconAndText
+ _OBJC_IVAR_$_ASCOfferMetadata._text
+ _OBJC_METACLASS_$_ASCIconTextOfferMetadata
+ __DATA__TtCV18AppStoreComponents19OfferIconTextLayoutP33_1F83811E3697D778D7120C3C0CEC42757Storage
+ __IVARS__TtCV18AppStoreComponents19OfferIconTextLayoutP33_1F83811E3697D778D7120C3C0CEC42757Storage
+ __METACLASS_DATA__TtCV18AppStoreComponents19OfferIconTextLayoutP33_1F83811E3697D778D7120C3C0CEC42757Storage
+ __OBJC_$_CLASS_METHODS_ASCIconTextOfferMetadata
+ __OBJC_$_INSTANCE_METHODS_ASCIconTextOfferMetadata
+ __OBJC_$_INSTANCE_VARIABLES_ASCIconTextOfferMetadata
+ __OBJC_$_INSTANCE_VARIABLES_ASCOfferMetadata
+ __OBJC_$_PROP_LIST_ASCIconTextOfferMetadata
+ __OBJC_CLASS_RO_$_ASCIconTextOfferMetadata
+ __OBJC_METACLASS_RO_$_ASCIconTextOfferMetadata
+ ___block_literal_global.55
+ ___block_literal_global.59
+ ___block_literal_global.63
+ _associated conformance 18AppStoreComponents19OfferIconTextLayoutV21BackgroundContentModeOSHAASQ
+ _objc_msgSend$configurationWithPointSize:weight:
+ _objc_msgSend$hasContent
+ _objc_msgSend$init
+ _objc_msgSend$initWithID:titles:subtitles:flags:ageRating:metrics:baseBuyParams:metricsBuyParams:metricsOverlay:additionalHeaders:preflightPackageURL:bundleID:itemName:vendorName:capabilities:
+ _objc_msgSend$initWithTitle:subtitle:imageName:animationName:
+ _objc_msgSend$isFreeform:
+ _objc_msgSend$isIconOnly
+ _objc_msgSend$isTextAndIcon
+ _objc_msgSend$isTextOnly
+ _objc_msgSend$metricsOverlay
+ _objc_msgSend$offerIconTextLayoutForSize:titleBackgroundView:titleView:imageView:topPadding:
+ _objc_msgSend$offerMetadataWithTitle:subtitle:imageName:
+ _objc_msgSend$systemImageNamed:withConfiguration:
+ _symbolic _____ 18AppStoreComponents19OfferIconTextLayoutV
+ _symbolic _____ 18AppStoreComponents19OfferIconTextLayoutV21BackgroundContentModeO
+ _symbolic _____ 18AppStoreComponents19OfferIconTextLayoutV7MetricsV
+ _symbolic _____ 18AppStoreComponents19OfferIconTextLayoutV7Storage33_1F83811E3697D778D7120C3C0CEC4275LLC
+ _type_layout_string 18AppStoreComponents19OfferIconTextLayoutV
+ _type_layout_string 18AppStoreComponents19OfferIconTextLayoutV7MetricsV
- +[ASCIconOfferMetadata supportsSecureCoding]
- +[ASCOfferMetadata iconMetadataWithImageName:animationName:]
- +[ASCTextOfferMetadata supportsSecureCoding]
- -[ASCAppOffer initWithID:titles:subtitles:flags:ageRating:metrics:baseBuyParams:metricsBuyParams:additionalHeaders:preflightPackageURL:bundleID:itemName:vendorName:capabilities:]
- -[ASCIconOfferMetadata .cxx_destruct]
- -[ASCIconOfferMetadata animationName]
- -[ASCIconOfferMetadata baseImageName]
- -[ASCIconOfferMetadata description]
- -[ASCIconOfferMetadata encodeWithCoder:]
- -[ASCIconOfferMetadata hash]
- -[ASCIconOfferMetadata imageNameForSize:]
- -[ASCIconOfferMetadata initWithBaseImageName:animationName:]
- -[ASCIconOfferMetadata initWithCoder:]
- -[ASCIconOfferMetadata initWithCoder:].cold.1
- -[ASCIconOfferMetadata initWithCoder:].cold.2
- -[ASCIconOfferMetadata isEqual:]
- -[ASCIconOfferMetadata isIcon]
- -[ASCTextOfferMetadata .cxx_destruct]
- -[ASCTextOfferMetadata description]
- -[ASCTextOfferMetadata encodeWithCoder:]
- -[ASCTextOfferMetadata hash]
- -[ASCTextOfferMetadata initWithCoder:]
- -[ASCTextOfferMetadata initWithCoder:].cold.1
- -[ASCTextOfferMetadata initWithTitle:subtitle:]
- -[ASCTextOfferMetadata isEqual:]
- -[ASCTextOfferMetadata isText]
- -[ASCTextOfferMetadata subtitle]
- -[ASCTextOfferMetadata title]
- _OBJC_CLASS_$_ASCIconOfferMetadata
- _OBJC_CLASS_$_ASCTextOfferMetadata
- _OBJC_IVAR_$_ASCIconOfferMetadata._animationName
- _OBJC_IVAR_$_ASCIconOfferMetadata._baseImageName
- _OBJC_IVAR_$_ASCTextOfferMetadata._subtitle
- _OBJC_IVAR_$_ASCTextOfferMetadata._title
- _OBJC_METACLASS_$_ASCIconOfferMetadata
- _OBJC_METACLASS_$_ASCTextOfferMetadata
- __OBJC_$_CLASS_METHODS_ASCIconOfferMetadata
- __OBJC_$_CLASS_METHODS_ASCTextOfferMetadata
- __OBJC_$_INSTANCE_METHODS_ASCIconOfferMetadata
- __OBJC_$_INSTANCE_METHODS_ASCTextOfferMetadata
- __OBJC_$_INSTANCE_VARIABLES_ASCIconOfferMetadata
- __OBJC_$_INSTANCE_VARIABLES_ASCTextOfferMetadata
- __OBJC_$_PROP_LIST_ASCIconOfferMetadata
- __OBJC_$_PROP_LIST_ASCTextOfferMetadata
- __OBJC_CLASS_RO_$_ASCIconOfferMetadata
- __OBJC_CLASS_RO_$_ASCTextOfferMetadata
- __OBJC_METACLASS_RO_$_ASCIconOfferMetadata
- __OBJC_METACLASS_RO_$_ASCTextOfferMetadata
- ___118-[ASCWorkspace(ASCAppLaunchTrampolineWorkspace) openApplicationWithBundleIdentifier:payloadURL:universalLinkRequired:]_block_invoke.cold.2
- ___118-[ASCWorkspace(ASCAppLaunchTrampolineWorkspace) openApplicationWithBundleIdentifier:payloadURL:universalLinkRequired:]_block_invoke.cold.3
- ___118-[ASCWorkspace(ASCAppLaunchTrampolineWorkspace) openApplicationWithBundleIdentifier:payloadURL:universalLinkRequired:]_block_invoke.cold.4
- ___block_literal_global.56
- ___block_literal_global.60
- __swiftImmortalRefCount
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_AppStoreComponents
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$iconMetadataWithImageName:animationName:
- _objc_msgSend$initWithBaseImageName:animationName:
- _objc_msgSend$initWithID:titles:subtitles:flags:ageRating:metrics:baseBuyParams:metricsBuyParams:additionalHeaders:preflightPackageURL:bundleID:itemName:vendorName:capabilities:
- _objc_msgSend$initWithTitle:subtitle:
- _objc_msgSend$isIcon
- _objc_msgSend$isText
- _objc_msgSend$textMetadataWithTitle:subtitle:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "@136@0:8@16@24@32q40@48@56@64@72@80@88@96@104@112@120@128"
+ "@56@0:8@16@24@32@40d48"
+ "ASCIconTextOfferMetadata"
+ "Could not decode ASCIconTextOfferMetadata because baseImageName and title were missing"
+ "T@\"ASCOfferButtonBackgroundImageView\",R,N,V_backgroundView"
+ "T@\"NSDictionary\",R,C,N,V_metricsOverlay"
+ "TB,R,N,GisIconOnly,V_icon"
+ "TB,R,N,GisTextAndIcon,V_iconAndText"
+ "TB,R,N,GisTextOnly,V_text"
+ "_TtCV18AppStoreComponents19OfferIconTextLayoutP33_1F83811E3697D778D7120C3C0CEC42757Storage"
+ "_iconAndText"
+ "_metricsOverlay"
+ "com.apple.AppSubscriptionsDemo"
+ "com.apple.UnifiedMessagingKitSampleApp"
+ "com.apple.freeform"
+ "configurationWithPointSize:weight:"
+ "icloud.and.arrow.down"
+ "iconAndText"
+ "initWithID:titles:subtitles:flags:ageRating:metrics:baseBuyParams:metricsBuyParams:metricsOverlay:additionalHeaders:preflightPackageURL:bundleID:itemName:vendorName:capabilities:"
+ "initWithTitle:subtitle:imageName:animationName:"
+ "isFreeform:"
+ "isIconOnly"
+ "isTextAndIcon"
+ "isTextOnly"
+ "metricsOverlay"
+ "offerIconTextLayoutForSize:titleBackgroundView:titleView:imageView:topPadding:"
+ "offerMetadataWithTitle:subtitle:imageName:"
+ "resumeMetadata:"
+ "springboard"
+ "systemImageNamed:withConfiguration:"
- "@128@0:8@16@24@32q40@48@56@64@72@80@88@96@104@112@120"
- "ASCIconOfferMetadata"
- "ASCTextOfferMetadata"
- "Could not decode ASCIconOfferMetadata because baseImageName was missing"
- "Could not decode ASCTextOfferMetadata because title was missing"
- "TB,R,N,GisIcon"
- "TB,R,N,GisText"
- "iconMetadataWithImageName:animationName:"
- "initWithBaseImageName:animationName:"
- "initWithID:titles:subtitles:flags:ageRating:metrics:baseBuyParams:metricsBuyParams:additionalHeaders:preflightPackageURL:bundleID:itemName:vendorName:capabilities:"
- "initWithTitle:subtitle:"

```
