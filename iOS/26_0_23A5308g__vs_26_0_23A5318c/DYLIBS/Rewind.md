## Rewind

> `/System/Library/PrivateFrameworks/Rewind.framework/Rewind`

```diff

-61.0.0.0.0
-  __TEXT.__text: 0x5d14
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__const: 0x278
-  __TEXT.__cstring: 0x567
-  __TEXT.__constg_swiftt: 0x378
-  __TEXT.__swift5_typeref: 0x128
-  __TEXT.__swift5_reflstr: 0x94
-  __TEXT.__swift5_fieldmd: 0x138
+61.1.0.0.0
+  __TEXT.__text: 0x6774
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_methlist: 0x14c
+  __TEXT.__const: 0x18a
+  __TEXT.__cstring: 0x74f
+  __TEXT.__constg_swiftt: 0x1b0
+  __TEXT.__swift5_typeref: 0x120
+  __TEXT.__swift5_reflstr: 0x4c
+  __TEXT.__swift5_fieldmd: 0x9c
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__oslogstring: 0x1ce
   __TEXT.__swift_as_entry: 0x4
-  __TEXT.__oslogstring: 0x11e
-  __TEXT.__unwind_info: 0x1e8
-  __TEXT.__eh_frame: 0x78
-  __TEXT.__objc_methname: 0x63
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__unwind_info: 0x200
+  __TEXT.__eh_frame: 0xf0
+  __TEXT.__objc_classname: 0x10
+  __TEXT.__objc_methname: 0xc4
+  __TEXT.__objc_methtype: 0x41
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x88
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x340
-  __AUTH_CONST.__const: 0x2a8
-  __AUTH_CONST.__objc_const: 0x4a0
-  __AUTH.__data: 0x4f8
-  __DATA.__data: 0x98
+  __DATA_CONST.__objc_selrefs: 0x80
+  __DATA_CONST.__objc_protorefs: 0x8
+  __AUTH_CONST.__auth_got: 0x3c8
+  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__objc_const: 0x448
+  __AUTH.__objc_data: 0x70
+  __AUTH.__data: 0x2b0
+  __DATA.__data: 0x158
   __DATA.__common: 0x18
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
+  - /System/Library/PrivateFrameworks/IntelligencePlatformQuery.framework/IntelligencePlatformQuery
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 999479D7-00EC-3403-8944-A4952472C3BA
-  Functions: 168
-  Symbols:   85
-  CStrings:  40
+  UUID: 695B6C22-1539-3427-B65A-37F55BAA694D
+  Functions: 162
+  Symbols:   96
+  CStrings:  62
 
Symbols:
+ _OBJC_CLASS_$_ContactHandleInteractionFeaturesDataFrame
+ _OBJC_CLASS_$_NSObject
+ _OBJC_METACLASS_$_ContactHandleInteractionFeaturesDataFrame
+ _OBJC_METACLASS_$_NSObject
+ __swift_stdlib_reportUnimplementedInitializer
+ _objc_autoreleaseReturnValue
+ _objc_msgSendSuper2
+ _objc_release_x26
+ _objc_retain
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x23
+ _swift_arrayDestroy
+ _swift_getObjCClassFromMetadata
- _objc_release_x24
- _objc_release_x27
- _objc_retain_x24
CStrings:
+ "%@"
+ ".cxx_destruct"
+ "@\"MLMultiArray\"16@0:8"
+ "@\"NSArray\"16@0:8"
+ "@\"NSNumber\"16@0:8"
+ "@16@0:8"
+ "@24@0:8@16"
+ "Binding %s"
+ "ContactHandleInteractionFeaturesDataFrame"
+ "Executed query successfully for %s"
+ "Executing %s for handle %s"
+ "Executing query for handle %s"
+ "Getting contact handle features for handle %s"
+ "Rewind.ContactHandleInteractionFeaturesDataFrame"
+ "RewindDataFrame"
+ "SELECT\n    intentClass,\n    bundleId,\n    groupIdentifier,\n    COALESCE(? - MAX(CASE WHEN interactionDirection = 2 THEN absoluteTimestamp END), -1) AS timeSinceLastOutgoingInteraction,\n    COALESCE(? - MAX(CASE WHEN interactionDirection = 3 THEN absoluteTimestamp END), -1) AS timeSinceLastIncomingInteraction,\n    COUNT(CASE WHEN interactionDirection = 2 THEN 1 END) AS numberOfOutgoingInteractions,\n    COUNT(CASE WHEN interactionDirection = 3 THEN 1 END) AS numberOfIncomingInteractions \nFROM\n    \"App.Intent\" \nWHERE\n    (intentClass = 'INSendMessageIntent'\n    AND groupIdentifier = 'iMessage;-;' || ?) \nOR (intentClass = 'INSendMessageIntent'\n    AND groupIdentifier = 'SMS;-;' || ?) \nOR (intentClass = 'INSendMessageIntent'\n    AND groupIdentifier = 'RCS;-;' || ?) \nOR (intentClass = 'INSendMessageIntent'\n    AND groupIdentifier = 'any;-;' || ?) \nOR (intentClass = 'INStartCallIntent'\n    AND groupIdentifier = ?) \nGROUP BY\n    groupIdentifier;"
+ "init()"
+ "initWithHandle:"
+ "initWithInteger:"
+ "loadData"
+ "numColumns"
+ "numRows"
+ "numberOfIncomingInteractions"
+ "numberOfOutgoingInteractions"
+ "savedResultSet"
+ "timeSinceLastIncomingInteraction"
+ "timeSinceLastOutgoingInteraction"
+ "toDict"
+ "toMLMultiArray"
+ "v16@0:8"
- "            SELECT\n                intentClass,\n                bundleId,\n                groupIdentifier,\n                COALESCE("
- " - MAX(absoluteTimestamp), 5184000) AS timeSinceLastInteraction,\n                COUNT(*) AS numberOfInteractions\n            FROM\n                \"App.Intent\"\n            WHERE\n                intentClass = 'INSendMessageIntent'\n                AND groupIdentifier = 'protocol;-;"
- "'\n            GROUP BY\n                groupIdentifier\n            ORDER BY\n                numberOfInteractions,\n                timeSinceLastInteraction;"
- "_TtC6Rewind20RewindDataFrameGroup"
- "_TtC6Rewind41ContactHandleInteractionFeaturesDataFrame"
- "groups"
- "numberOfInteractions"
- "queryTemplate"
- "timeSinceLastInteraction"

```
