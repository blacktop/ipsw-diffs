## CalendarUIKit

> `/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit`

```diff

-1271.0.0.0.0
-  __TEXT.__text: 0x22442c
-  __TEXT.__auth_stubs: 0x47d0
-  __TEXT.__objc_methlist: 0x7ce8
-  __TEXT.__const: 0x106f4
-  __TEXT.__cstring: 0xcc42
+1274.0.0.0.0
+  __TEXT.__text: 0x2243d0
+  __TEXT.__auth_stubs: 0x47f0
+  __TEXT.__objc_methlist: 0x7a50
+  __TEXT.__const: 0x10724
+  __TEXT.__cstring: 0xcb92
   __TEXT.__oslogstring: 0x3b08
-  __TEXT.__gcc_except_tab: 0xe20
+  __TEXT.__gcc_except_tab: 0xe80
   __TEXT.__ustring: 0x2042
   __TEXT.__dlopen_cstrs: 0xb1
   __TEXT.__constg_swiftt: 0x59f8

   __TEXT.__swift5_reflstr: 0x3fea
   __TEXT.__swift5_fieldmd: 0x4a40
   __TEXT.__swift5_assocty: 0xe88
-  __TEXT.__swift5_capture: 0xf44
+  __TEXT.__swift5_capture: 0xf54
   __TEXT.__swift5_proto: 0xaac
   __TEXT.__swift5_types: 0x438
   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0x50
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x6ec8
-  __TEXT.__eh_frame: 0x4c54
-  __TEXT.__objc_classname: 0x10b6
-  __TEXT.__objc_methname: 0x19736
-  __TEXT.__objc_methtype: 0x2612
-  __TEXT.__objc_stubs: 0x12660
-  __DATA_CONST.__got: 0x1a70
-  __DATA_CONST.__const: 0x1d38
+  __TEXT.__unwind_info: 0x6f60
+  __TEXT.__eh_frame: 0x4c7c
+  __TEXT.__objc_classname: 0x1098
+  __TEXT.__objc_methname: 0x1953f
+  __TEXT.__objc_methtype: 0x256a
+  __TEXT.__objc_stubs: 0x12480
+  __DATA_CONST.__got: 0x1a60
+  __DATA_CONST.__const: 0x1d10
   __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0xd8
-  __DATA_CONST.__objc_protolist: 0x160
+  __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6510
+  __DATA_CONST.__objc_selrefs: 0x6480
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__auth_got: 0x23f8
-  __AUTH_CONST.__const: 0x8e80
-  __AUTH_CONST.__cfstring: 0x8780
-  __AUTH_CONST.__objc_const: 0xdd68
+  __AUTH_CONST.__auth_got: 0x2408
+  __AUTH_CONST.__const: 0x8ea8
+  __AUTH_CONST.__cfstring: 0x8700
+  __AUTH_CONST.__objc_const: 0xda88
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x21b0
   __AUTH.__data: 0x5080
-  __DATA.__objc_ivar: 0x70c
-  __DATA.__data: 0x6ac8
+  __DATA.__objc_ivar: 0x700
+  __DATA.__data: 0x6a68
   __DATA.__bss: 0x14fa8
   __DATA.__common: 0x900
   __DATA_DIRTY.__objc_data: 0x1418

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A9BEFA92-D219-353A-80BA-1F11D42B584A
-  Functions: 11120
-  Symbols:   14012
-  CStrings:  7456
+  UUID: 688A76DE-EDE9-3262-AD81-E35097661973
+  Functions: 11099
+  Symbols:   13943
+  CStrings:  7416
 
Symbols:
+ +[CUIKTimeTextProvider _applyFont:toString:allowSmallCaps:otherAttributes:]
+ -[CUIKOROccurrenceState initWithState:]
+ GCC_except_table48
+ __CUIKSingularDatetimeFormatWithShortOneTimeZone
+ __OBJC_$_PROP_LIST_CUIKOROccurrenceState.352
+ ___75+[CUIKTimeTextProvider _applyFont:toString:allowSmallCaps:otherAttributes:]_block_invoke
+ ___block_descriptor_57_e8_32s40s48s_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32ls32l8s40l8s48l8
+ ___block_literal_global.212
+ ___block_literal_global.65
+ _objc_msgSend$_applyFont:toString:allowSmallCaps:otherAttributes:
- +[CUIKTimeTextProvider _applyFont:toString:allowSmallCaps:]
- -[CUIKOROccurrenceState performChanges:]
- -[CUIKOROccurrenceState performChanges:].cold.1
- -[CUIKOROccurrenceState performChangesWithState:]
- -[CUIKOROccurrenceState setAllDayOverride:]
- -[CUIKOROccurrenceState setBackgroundRect:]
- -[CUIKOROccurrenceState setBirthdayCount:]
- -[CUIKOROccurrenceState setDisplayColor:]
- -[CUIKOROccurrenceState setEstimatedTextFrame:]
- -[CUIKOROccurrenceState setHorizontalSizeClass:]
- -[CUIKOROccurrenceState setIsDimmed:]
- -[CUIKOROccurrenceState setIsMiniPreviewInEventDetail:]
- -[CUIKOROccurrenceState setIsProposedTime:]
- -[CUIKOROccurrenceState setIsSelected:]
- -[CUIKOROccurrenceState setOccurrence:]
- -[CUIKOROccurrenceState setOccurrenceIsFirstVisibleDayOfEvent:]
- -[CUIKOROccurrenceState setOccurrences:]
- -[CUIKOROccurrenceState setPadding:]
- -[CUIKOROccurrenceState setTraitCollection:]
- -[CUIKOROccurrenceState setTravelTime:]
- -[CUIKOROccurrenceState setTravelTimeHeight:]
- -[CUIKOROccurrenceState setUserInterfaceStyle:]
- -[CUIKOROccurrenceState setUsesSmallText:]
- -[CUIKOROccurrenceState setVisibleHeight:]
- _OBJC_IVAR_$_CUIKOROccurrenceState._didChange
- _OBJC_IVAR_$_CUIKOROccurrenceState._isPerformingChanges
- _OBJC_IVAR_$_CUIKOROccurrenceState._padding
- __OBJC_$_CLASS_PROP_LIST_CUIKOROccurrenceState
- __OBJC_$_PROP_LIST_CUIKMutableDayOccurrenceState
- __OBJC_$_PROP_LIST_CUIKOROccurrenceState.410
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CUIKMutableDayOccurrenceState
- __OBJC_$_PROTOCOL_METHOD_TYPES_CUIKMutableDayOccurrenceState
- __OBJC_$_PROTOCOL_REFS_CUIKMutableDayOccurrenceState
- __OBJC_LABEL_PROTOCOL_$_CUIKMutableDayOccurrenceState
- __OBJC_PROTOCOL_$_CUIKMutableDayOccurrenceState
- ___49-[CUIKOROccurrenceState performChangesWithState:]_block_invoke
- ___59+[CUIKTimeTextProvider _applyFont:toString:allowSmallCaps:]_block_invoke
- ___block_descriptor_40_e8_32s_e41_v16?0"<CUIKMutableDayOccurrenceState>"8ls32l8
- ___block_descriptor_49_e8_32s40s_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32ls32l8s40l8
- ___block_literal_global.209
- ___block_literal_global.66
- _objc_msgSend$_applyFont:toString:allowSmallCaps:
- _objc_msgSend$performChanges:
- _objc_msgSend$setAllDayOverride:
- _objc_msgSend$setBackgroundRect:
- _objc_msgSend$setBirthdayCount:
- _objc_msgSend$setHorizontalSizeClass:
- _objc_msgSend$setIsDimmed:
- _objc_msgSend$setIsMiniPreviewInEventDetail:
- _objc_msgSend$setIsProposedTime:
- _objc_msgSend$setIsSelected:
- _objc_msgSend$setOccurrenceIsFirstVisibleDayOfEvent:
- _objc_msgSend$setOccurrences:
- _objc_msgSend$setOpacity:forAppearance:
- _objc_msgSend$setTraitCollection:
- _objc_msgSend$setUserInterfaceStyle:
- _objc_msgSend$setUsesSmallText:
CStrings:
+ "%@ by bike and %@ on foot"
+ "%@ by car and %@ on foot"
+ "%@ on foot and %@ by bike"
+ "%@ on foot and %@ by car"
+ "@44@0:8@16@24B32@36"
+ "It will take %@ to get to %@ using %@"
+ "It will take %@ to get to %@ using %@ by car."
+ "It will take %@ to get to %@ using %@."
+ "It will take %@ using %@ by car."
+ "It will take %@ using %@."
+ "Leave now: It will take %@ to get to %@ using %@"
+ "Leave now: It will take %@ to get to %@ using %@ by car."
+ "Leave now: It will take %@ to get to %@ using %@."
+ "Leave now: It will take %@ using %@ by car."
+ "Leave now: It will take %@ using %@."
+ "T@\"EKEvent\",R,N,V_occurrence"
+ "T@\"NSNumber\",R,N,V_allDayOverride"
+ "T@\"UIColor\",R,N,V_displayColor"
+ "T@\"UITraitCollection\",R,N,V_traitCollection"
+ "TB,R,N,V_isDimmed"
+ "TB,R,N,V_isMiniPreviewInEventDetail"
+ "TB,R,N,V_isProposedTime"
+ "TB,R,N,V_isSelected"
+ "TB,R,N,V_occurrenceIsFirstVisibleDayOfEvent"
+ "TB,R,N,V_usesSmallText"
+ "Td,R,N,V_travelTime"
+ "Td,R,N,V_travelTimeHeight"
+ "Td,R,N,V_visibleHeight"
+ "Tq,R,N,V_birthdayCount"
+ "Tq,R,N,V_horizontalSizeClass"
+ "Tq,R,N,V_userInterfaceStyle"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_backgroundRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_estimatedTextFrame"
+ "_applyFont:toString:allowSmallCaps:otherAttributes:"
+ "initWithState:"
- "%@ by bike, and %@ on foot"
- "%@ by car, and %@ on foot"
- "%@ on foot, %@ by bike, and another %@ on foot"
- "%@ on foot, %@ by car, and another %@ on foot"
- "%@ on foot, and %@ by bike"
- "%@ on foot, and %@ by car"
- "CUIKMutableDayOccurrenceState"
- "CUIKOROccurrenceState.m"
- "It will take %@ on %@ by car."
- "It will take %@ on %@."
- "It will take %@ to get to %@ on %@"
- "It will take %@ to get to %@ on %@ by car."
- "It will take %@ to get to %@ on %@."
- "Leave now: It will take %@ on %@ by car."
- "Leave now: It will take %@ on %@."
- "Leave now: It will take %@ to get to %@ on %@"
- "Leave now: It will take %@ to get to %@ on %@ by car."
- "Leave now: It will take %@ to get to %@ on %@."
- "Re-entry not currently supported"
- "T@\"EKEvent\",&,N,V_occurrence"
- "T@\"NSArray\",&,N,V_occurrences"
- "T@\"NSNumber\",&,N,V_allDayOverride"
- "T@\"UIColor\",&,N,V_displayColor"
- "T@\"UITraitCollection\",&,N"
- "T@\"UITraitCollection\",&,N,V_traitCollection"
- "TB,N,V_isDimmed"
- "TB,N,V_isMiniPreviewInEventDetail"
- "TB,N,V_isProposedTime"
- "TB,N,V_isSelected"
- "TB,N,V_occurrenceIsFirstVisibleDayOfEvent"
- "TB,N,V_usesSmallText"
- "Td,N,V_travelTime"
- "Td,N,V_travelTimeHeight"
- "Td,N,V_visibleHeight"
- "Tq,N,V_birthdayCount"
- "Tq,N,V_horizontalSizeClass"
- "Tq,N,V_userInterfaceStyle"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_backgroundRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_estimatedTextFrame"
- "T{UIEdgeInsets=dddd},N,V_padding"
- "_applyFont:toString:allowSmallCaps:"
- "_didChange"
- "_isPerformingChanges"
- "_padding"
- "performChanges:"
- "performChangesWithState:"
- "setAllDayOverride:"
- "setBackgroundRect:"
- "setBirthdayCount:"
- "setDisplayColor:"
- "setEstimatedTextFrame:"
- "setHorizontalSizeClass:"
- "setIsDimmed:"
- "setIsMiniPreviewInEventDetail:"
- "setIsProposedTime:"
- "setIsSelected:"
- "setOccurrence:"
- "setOccurrenceIsFirstVisibleDayOfEvent:"
- "setOccurrences:"
- "setOpacity:forAppearance:"
- "setTraitCollection:"
- "setUserInterfaceStyle:"
- "setUsesSmallText:"
- "v16@?0@\"<CUIKMutableDayOccurrenceState>\"8"
- "v24@0:8@\"EKEvent\"16"
- "v24@0:8@\"NSNumber\"16"
- "v24@0:8@\"UITraitCollection\"16"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v48@0:8{UIEdgeInsets=dddd}16"
- "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"

```
