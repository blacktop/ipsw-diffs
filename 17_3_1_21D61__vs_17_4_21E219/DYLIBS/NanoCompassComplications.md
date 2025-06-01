## NanoCompassComplications

> `/System/Library/NanoTimeKit/ComplicationBundles/NanoCompassComplications.bundle/NanoCompassComplications`

```diff

-524.3.9.0.0
-  __TEXT.__text: 0x35118
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_methlist: 0x329c
-  __TEXT.__const: 0x434
-  __TEXT.__oslogstring: 0x34cf
-  __TEXT.__cstring: 0x35b8
+524.5.15.0.0
+  __TEXT.__text: 0x35214
+  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__objc_methlist: 0x326c
+  __TEXT.__const: 0x474
+  __TEXT.__oslogstring: 0x3463
+  __TEXT.__cstring: 0x3698
   __TEXT.__ustring: 0xde
   __TEXT.__gcc_except_tab: 0x908
   __TEXT.__dlopen_cstrs: 0xbc
-  __TEXT.__constg_swiftt: 0x10c
-  __TEXT.__swift5_typeref: 0x58
-  __TEXT.__swift5_fieldmd: 0x64
-  __TEXT.__swift5_types: 0x10
+  __TEXT.__constg_swiftt: 0x148
+  __TEXT.__swift5_typeref: 0x5e
+  __TEXT.__swift5_fieldmd: 0x74
+  __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_reflstr: 0xf
   __TEXT.__unwind_info: 0xea0
   __TEXT.__objc_classname: 0x909
-  __TEXT.__objc_methname: 0x7dee
-  __TEXT.__objc_methtype: 0x10ca
-  __TEXT.__objc_stubs: 0x67e0
+  __TEXT.__objc_methname: 0x7c30
+  __TEXT.__objc_methtype: 0x1092
+  __TEXT.__objc_stubs: 0x66a0
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__const: 0xcb0
-  __DATA_CONST.__objc_classlist: 0x260
+  __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6308
-  __DATA_CONST.__objc_selrefs: 0x1ef8
-  __DATA_CONST.__objc_arraydata: 0xa58
-  __AUTH_CONST.__objc_doubleobj: 0x390
-  __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__cfstring: 0x2a20
+  __DATA_CONST.__objc_const: 0x62c0
+  __DATA_CONST.__objc_selrefs: 0x1ea8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x4c0
+  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_arraydata: 0xa38
+  __AUTH_CONST.__cfstring: 0x2a40
   __AUTH_CONST.__const: 0x5f0
-  __AUTH_CONST.__objc_const: 0x1a60
+  __AUTH_CONST.__objc_doubleobj: 0x350
+  __AUTH_CONST.__objc_const: 0x1aa8
   __AUTH_CONST.__objc_intobj: 0x270
+  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x258
-  __AUTH_CONST.__auth_got: 0x558
-  __AUTH.__objc_data: 0x18d0
-  __AUTH.__data: 0x110
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x4b8
-  __DATA.__objc_superrefs: 0x190
-  __DATA.__objc_ivar: 0x488
-  __DATA.__data: 0x650
+  __AUTH_CONST.__auth_got: 0x588
+  __AUTH.__objc_data: 0x1988
+  __AUTH.__data: 0x138
+  __DATA.__objc_ivar: 0x480
+  __DATA.__data: 0x658
   __DATA.__bss: 0x758
-  __DATA.__common: 0x30
+  __DATA.__common: 0x38
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6E16CE1A-5B90-33FC-BD24-1B7EDCAF1312
-  Functions: 1396
-  Symbols:   633
-  CStrings:  2778
+  UUID: 37BD5EF7-668D-3E54-9B08-40E10A94495E
+  Functions: 1395
+  Symbols:   636
+  CStrings:  2768
 
Symbols:
+ _OBJC_CLASS_$__TtC24NanoCompassComplications21UnitLengthPreferences
+ _OBJC_METACLASS_$__TtC24NanoCompassComplications21UnitLengthPreferences
+ ___chkstk_darwin
CStrings:
+ "%s: We have a waypoint without a UUID, skipping.  Label is %@"
+ "+[WaypointsComplicationDataSource complicationDescriptors]"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIFontDescriptor\",?,C,N"
+ "T@\"_TtC24NanoCompassComplications21UnitLengthPreferences\",N,R"
+ "TB,N,V_displayTilde"
+ "Td,?,N"
+ "_TtC24NanoCompassComplications21UnitLengthPreferences"
+ "_displayTilde"
+ "also nil"
+ "displayTilde"
+ "setDisplayTilde:"
+ "shared"
+ "usesMetric"
+ "\x84"
- "Current unit is meter: %@. Raw precision is %f and rounded precision is %f. Raw altitude is %f and rounded altitude is %f. Raw accuracy is %f and rounded accuracy is %@."
- "T@\"NSNumber\",&,N,V_absoluteAltitudePrecision"
- "T@\"UIFontDescriptor\",C,N"
- "TB,N,V_displayTildeForApp"
- "TB,N,V_displayTildeForComplication"
- "Td,N"
- "_absoluteAltitudePrecision"
- "_convertMeterInFeet:"
- "_displayTildeForApp"
- "_displayTildeForComplication"
- "_getCloserValue:low:high:"
- "_getRoundedAccuracy:byUnit:"
- "_getRoundedPrecisionWithValue:multiplier:"
- "_getRoundedValue:byRoundedPrecision:"
- "_populateRoundedValue"
- "absoluteAltitudePrecision"
- "d24@0:8d16"
- "d28@0:8d16B24"
- "d32@0:8d16d24"
- "d40@0:8d16d24d32"
- "displayTildeForApp"
- "displayTildeForComplication"
- "objectAtIndex:"
- "setAbsoluteAltitudePrecision:"
- "setDisplayTildeForApp:"
- "setDisplayTildeForComplication:"
- "usesMetricSystem"
- "\x85"

```
