## HomeWidget

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget`

```diff

-963.2.10.1.1
-  __TEXT.__text: 0x9e0ac
-  __TEXT.__auth_stubs: 0x25c0
+982.0.0.1.3
+  __TEXT.__text: 0xadb38
+  __TEXT.__auth_stubs: 0x2900
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x3272
-  __TEXT.__cstring: 0x2407
-  __TEXT.__constg_swiftt: 0xde8
-  __TEXT.__swift5_typeref: 0x615e
+  __TEXT.__const: 0x390a
+  __TEXT.__cstring: 0x24c7
+  __TEXT.__swift5_typeref: 0x6376
+  __TEXT.__constg_swiftt: 0xed4
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0xd47
-  __TEXT.__swift5_fieldmd: 0xd1c
-  __TEXT.__swift5_types: 0xd8
-  __TEXT.__objc_methname: 0xa68
-  __TEXT.__oslogstring: 0x174d
+  __TEXT.__swift5_reflstr: 0xd1c
+  __TEXT.__swift5_fieldmd: 0xde0
+  __TEXT.__swift5_types: 0xf4
+  __TEXT.__objc_methname: 0xa32
+  __TEXT.__oslogstring: 0x17cb
   __TEXT.__swift5_assocty: 0x4c8
-  __TEXT.__swift5_capture: 0x258
+  __TEXT.__swift5_capture: 0x240
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_proto: 0x200
+  __TEXT.__swift5_proto: 0x268
   __TEXT.__objc_classname: 0x2f
   __TEXT.__objc_methtype: 0x174
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x1928
-  __TEXT.__eh_frame: 0x2c5c
-  __DATA_CONST.__auth_got: 0x12e0
-  __DATA_CONST.__got: 0x9d0
-  __DATA_CONST.__auth_ptr: 0xd58
-  __DATA_CONST.__const: 0x14c8
+  __TEXT.__unwind_info: 0x1c70
+  __TEXT.__eh_frame: 0x35ac
+  __DATA_CONST.__auth_got: 0x1480
+  __DATA_CONST.__got: 0xa68
+  __DATA_CONST.__auth_ptr: 0xdf0
+  __DATA_CONST.__const: 0x1708
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0xa70
-  __DATA.__objc_selrefs: 0x318
+  __DATA.__objc_const: 0xa30
+  __DATA.__objc_selrefs: 0x300
   __DATA.__objc_data: 0xd8
-  __DATA.__data: 0x2a98
-  __DATA.__common: 0x208
-  __DATA.__bss: 0x4158
+  __DATA.__data: 0x2c98
+  __DATA.__bss: 0x4e58
+  __DATA.__common: 0x1f0
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/Home.framework/Home
   - /System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel
   - /System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2
+  - /System/Library/PrivateFrameworks/HomeWidgetIntents.framework/HomeWidgetIntents
   - /System/Library/PrivateFrameworks/IntentsFoundation.framework/IntentsFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1911
-  Symbols:   224
-  CStrings:  481
+  Functions: 2121
+  Symbols:   219
+  CStrings:  483
 
Symbols:
+ _swift_getAssociatedTypeWitness
- _HMAccessoryCategoryTypeAppleTV
- _HMAccessoryCategoryTypeHomePod
- _HMAccessoryCategoryTypeSpeaker
- _swift_weakDestroy
- _swift_weakInit
- _swift_weakLoadStrong
CStrings:
+ "%!s(MISSING) Error subscribing to Matter monitor: %!@(MISSING)"
+ "%!s(MISSING) No matching HMHome found in entities"
+ "%!s(MISSING) WidgetDataModel.home=%!s(MISSING)"
+ "%!s(MISSING) Write attempted on a Native Matter device without client support."
+ "%!s(MISSING) for accessory %!s(MISSING) - MatterDevice: %!s(MISSING)"
+ "Created entity with widgetInfo: %!s(MISSING) - endpoints: %!s(MISSING) statusString: %!s(MISSING)"
+ "Invalid number of keys found, expected one."
+ "_grabExistingDataModel()"
+ "_setupDataModel(coverages:)"
+ "monitorAttributesAndUpdateEntities(entities:for:homeManager:)"
+ "sortedHomes"
+ "warmup"
+ "writeRequestsFor(matterAccessory:)"
- "%!s(MISSING) HFHomeKitDispatcher.home=%!@(MISSING)"
- "%!s(MISSING) Unable to build valid HMHomeManager"
- "Calendar.current failed to build Date and will treat call as timeout"
- "Finished lazy loading of [HMHome]: count=%!l(MISSING)d"
- "_homeManager"
- "hf_isCamera"
- "hf_isNetworkRouter"
- "hf_visibleAccessories"
- "home"
- "homePodVariant"
- "task"

```
