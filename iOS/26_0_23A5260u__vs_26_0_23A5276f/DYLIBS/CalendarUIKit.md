## CalendarUIKit

> `/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit`

```diff

-1269.1.0.0.0
-  __TEXT.__text: 0x22057c
-  __TEXT.__auth_stubs: 0x47c0
-  __TEXT.__objc_methlist: 0x7cb8
-  __TEXT.__const: 0x106d4
+1271.0.0.0.0
+  __TEXT.__text: 0x22442c
+  __TEXT.__auth_stubs: 0x47d0
+  __TEXT.__objc_methlist: 0x7ce8
+  __TEXT.__const: 0x106f4
   __TEXT.__cstring: 0xcc42
-  __TEXT.__oslogstring: 0x3b98
+  __TEXT.__oslogstring: 0x3b08
   __TEXT.__gcc_except_tab: 0xe20
-  __TEXT.__ustring: 0x1fc4
+  __TEXT.__ustring: 0x2042
   __TEXT.__dlopen_cstrs: 0xb1
   __TEXT.__constg_swiftt: 0x59f8
   __TEXT.__swift5_typeref: 0x1b4b2

   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0x50
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x6e90
-  __TEXT.__eh_frame: 0x4c4c
+  __TEXT.__unwind_info: 0x6ec8
+  __TEXT.__eh_frame: 0x4c54
   __TEXT.__objc_classname: 0x10b6
-  __TEXT.__objc_methname: 0x194ca
-  __TEXT.__objc_methtype: 0x24eb
-  __TEXT.__objc_stubs: 0x12440
-  __DATA_CONST.__got: 0x1a50
-  __DATA_CONST.__const: 0x1d58
+  __TEXT.__objc_methname: 0x19736
+  __TEXT.__objc_methtype: 0x2612
+  __TEXT.__objc_stubs: 0x12660
+  __DATA_CONST.__got: 0x1a70
+  __DATA_CONST.__const: 0x1d38
   __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6478
+  __DATA_CONST.__objc_selrefs: 0x6510
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__auth_got: 0x23f0
+  __AUTH_CONST.__auth_got: 0x23f8
   __AUTH_CONST.__const: 0x8e80
   __AUTH_CONST.__cfstring: 0x8780
   __AUTH_CONST.__objc_const: 0xdd68

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3A082B4A-2E7B-3F74-806E-16DACE3DBF12
-  Functions: 11109
-  Symbols:   13991
-  CStrings:  7437
+  UUID: A9BEFA92-D219-353A-80BA-1F11D42B584A
+  Functions: 11120
+  Symbols:   14012
+  CStrings:  7456
 
Symbols:
+ +[CUIKORImageUtils _frameMutatedForProximityToHourLine:]
+ +[CUIKORImageUtils backgroundImageFrameForState:]
+ +[CUIKORImageUtils calculateBackgroundImageFrame:travelTimeFrame:forState:withMargins:]
+ +[CUIKORImageUtils standardBackgroundMargins:]
+ +[CUIKOccurrenceRenderer reminderBackgroundColor:style:miniPreview:completed:darkenForAllDayArea:]
+ +[CUIKOccurrenceRenderer renderColorBlockImageWithSize:colorBarColor:backgroundColor:stripeColor:stripedImageAlpha:]
+ +[CUIKTimeIntervalTextProvider CUIKSmallCapAMPMTimezoneClarificationStringForStartDate:endDate:startTimeZone:endTimeZone:color:]
+ +[CUIKTimeIntervalTextProvider attributedAndSmallCappedDesignatorTextWithDate:calendar:color:]
+ -[CUIKORPayloadProvider _renderColorBlockImageWithState:colorBarColor:backgroundColor:stripeColor:stripedImageAlpha:]
+ -[CUIKORPayloadProvider _renderColorBlockImageWithState:forTravelTime:]
+ GCC_except_table12
+ _CGContextSetLineCap
+ _CUIKAbbreviatedEnDashDayStringForDate
+ _CUIKEnDashDayStringForDate
+ _CalCanvasPocketEventIndicatorEnabled
+ _OBJC_CLASS_$_IFColor
+ _OBJC_CLASS_$_ISIconLayerElement
+ _OBJC_CLASS_$_ISIconLayerGroup
+ _UIFontTextStyleBody
+ __CUIKShortTZString
+ ___116+[CUIKOccurrenceRenderer renderColorBlockImageWithSize:colorBarColor:backgroundColor:stripeColor:stripedImageAlpha:]_block_invoke
+ ___block_descriptor_137_e20_v16?0^{CGContext=}8l
+ ___block_literal_global.289
+ ___block_literal_global.43
+ _objc_msgSend$_frameMutatedForProximityToHourLine:
+ _objc_msgSend$_renderColorBlockImageWithState:colorBarColor:backgroundColor:stripeColor:stripedImageAlpha:
+ _objc_msgSend$_renderColorBlockImageWithState:forTravelTime:
+ _objc_msgSend$attributedAndSmallCappedDesignatorTextWithDate:calendar:color:
+ _objc_msgSend$backgroundImageFrameForState:
+ _objc_msgSend$calculateBackgroundImageFrame:travelTimeFrame:forState:withMargins:
+ _objc_msgSend$initWithSystemColor:
+ _objc_msgSend$initWithTypeIdentifier:layerGroups:
+ _objc_msgSend$preferredFontDescriptorWithTextStyle:
+ _objc_msgSend$reminderBackgroundColor:style:miniPreview:completed:darkenForAllDayArea:
+ _objc_msgSend$renderColorBlockImageWithSize:colorBarColor:backgroundColor:stripeColor:stripedImageAlpha:
+ _objc_msgSend$setFillColor:forAppearance:
+ _objc_msgSend$setHasEffects:
+ _objc_msgSend$setHasOverlappingChildSpecularsCombined:
+ _objc_msgSend$setHasSpecular:
+ _objc_msgSend$setLayers:
+ _objc_msgSend$setOpacity:
+ _objc_msgSend$setOpacity:forAppearance:
+ _objc_msgSend$setShadow:
+ _objc_msgSend$setShadowStyle:
+ _objc_msgSend$setShadowStyle:forAppearance:
+ _objc_msgSend$setTranslucency:
+ _objc_msgSend$setTranslucency:forAppearance:
+ _objc_msgSend$standardBackgroundMargins:
+ _objc_msgSend$white
- +[CUIKOccurrenceRenderer renderColorBlockImageWithThickness:backgroundColor:stripeColor:stripedImageAlpha:]
- -[CUIKORPayloadProvider _renderBackgroundImageForState:backgroundColor:]
- -[CUIKORPayloadProvider _renderColorBlockImageWithState:]
- -[CUIKORPayloadProvider _renderColorBlockImageWithState:backgroundColor:stripeColor:stripedImageAlpha:]
- -[CUIKORPayloadProvider _renderSelectedColorBlockImageWithState:]
- -[CUIKORPayloadProvider _renderUnselectedColorBlockImageWithState:]
- GCC_except_table15
- _CUIKAbbreviatedEmDashDayStringForDate
- _CUIKLongEmDashDayStringForDate
- __CUIKDurationFormatWithShortOneTimeZone
- ___107+[CUIKOccurrenceRenderer renderColorBlockImageWithThickness:backgroundColor:stripeColor:stripedImageAlpha:]_block_invoke
- ___block_descriptor_88_e20_v16?0^{CGContext=}8l
- ___block_literal_global.298
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_CalendarUIKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CalendarUIKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CalendarUIKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CalendarUIKit
- _objc_msgSend$_renderBackgroundImageForState:backgroundColor:
- _objc_msgSend$_renderColorBlockImageWithState:
- _objc_msgSend$_renderColorBlockImageWithState:backgroundColor:stripeColor:stripedImageAlpha:
- _objc_msgSend$_renderSelectedColorBlockImageWithState:
- _objc_msgSend$_renderUnselectedColorBlockImageWithState:
- _objc_msgSend$initWithTypeIdentifier:iconLayers:
- _objc_msgSend$renderColorBlockImageWithThickness:backgroundColor:stripeColor:stripedImageAlpha:
- _objc_msgSend$setHasLightEffects:
- _swift_bridgeObjectRelease_n
CStrings:
+ "%.0f:%d:%@:%lu:%@:%@:%@:%@:%@"
+ "(%@)"
+ "@40@0:8B16q20B28B32B36"
+ "@56@0:8@16@24@32@40d48"
+ "@64@0:8{CGSize=dd}16^{CGColor=}32^{CGColor=}40^{CGColor=}48d56"
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
+ "CUIKSmallCapAMPMTimezoneClarificationStringForStartDate:endDate:startTimeZone:endTimeZone:color:"
+ "CanvasPocketEventIndicatorDisabled"
+ "_frameMutatedForProximityToHourLine:"
+ "_renderColorBlockImageWithState:colorBarColor:backgroundColor:stripeColor:stripedImageAlpha:"
+ "_renderColorBlockImageWithState:forTravelTime:"
+ "attributedAndSmallCappedDesignatorTextWithDate:calendar:color:"
+ "backgroundImageFrameForState:"
+ "calculateBackgroundImageFrame:travelTimeFrame:forState:withMargins:"
+ "initWithSystemColor:"
+ "initWithTypeIdentifier:layerGroups:"
+ "preferredFontDescriptorWithTextStyle:"
+ "reminderBackgroundColor:style:miniPreview:completed:darkenForAllDayArea:"
+ "renderColorBlockImageWithSize:colorBarColor:backgroundColor:stripeColor:stripedImageAlpha:"
+ "setFillColor:forAppearance:"
+ "setHasEffects:"
+ "setHasOverlappingChildSpecularsCombined:"
+ "setHasSpecular:"
+ "setLayers:"
+ "setOpacity:"
+ "setOpacity:forAppearance:"
+ "setShadow:"
+ "setShadowStyle:"
+ "setShadowStyle:forAppearance:"
+ "setTranslucency:"
+ "setTranslucency:forAppearance:"
+ "standardBackgroundMargins:"
+ "v72@0:8^{CGRect={CGPoint=dd}{CGSize=dd}}16^{CGRect={CGPoint=dd}{CGSize=dd}}24@32{UIEdgeInsets=dddd}40"
+ "white"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@16"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "{UIEdgeInsets=dddd}20@0:8B16"
- "%.0f:%ld:%@:%lu:%@:%@:%@:%@:%@"
- "%@ (%@) to %@ (%@)"
- "%@ to %@ (%@)"
- "@48@0:8@16@24@32d40"
- "@48@0:8d16^{CGColor=}24^{CGColor=}32d40"
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
- "CreateFamilyCalendarViewModel"
- "Detail duration format no 'from'"
- "Detail duration format no 'from' with '-'"
- "RedactionReasons"
- "_renderBackgroundImageForState:backgroundColor:"
- "_renderColorBlockImageWithState:"
- "_renderColorBlockImageWithState:backgroundColor:stripeColor:stripedImageAlpha:"
- "_renderSelectedColorBlockImageWithState:"
- "_renderUnselectedColorBlockImageWithState:"
- "from %@ to %@"
- "initWithTypeIdentifier:iconLayers:"
- "renderColorBlockImageWithThickness:backgroundColor:stripeColor:stripedImageAlpha:"

```
