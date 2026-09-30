## PhotosUI

> `/System/Library/Frameworks/PhotosUI.framework/PhotosUI`

```diff

-742.0.141.0.0
-  __TEXT.__text: 0x26eb4
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x2958
-  __TEXT.__const: 0x1670
-  __TEXT.__swift5_typeref: 0x452
+750.11.101.0.0
+  __TEXT.__text: 0x25788
+  __TEXT.__auth_stubs: 0xbf0
+  __TEXT.__objc_methlist: 0x2fc4
+  __TEXT.__const: 0x18a0
+  __TEXT.__swift5_typeref: 0x42a
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__cstring: 0x3f9c
+  __TEXT.__cstring: 0x3fb1
   __TEXT.__constg_swiftt: 0x710
-  __TEXT.__swift5_reflstr: 0x48a
+  __TEXT.__swift5_reflstr: 0x46a
   __TEXT.__swift5_fieldmd: 0x504
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_assocty: 0x258
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0xf0
   __TEXT.__swift5_types: 0x80
-  __TEXT.__gcc_except_tab: 0x2e8
+  __TEXT.__gcc_except_tab: 0x2f0
   __TEXT.__oslogstring: 0xbec
-  __TEXT.__unwind_info: 0xe18
-  __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x720
-  __TEXT.__objc_methname: 0x8388
+  __TEXT.__unwind_info: 0xd90
+  __TEXT.__eh_frame: 0x48
+  __TEXT.__objc_classname: 0x71e
+  __TEXT.__objc_methname: 0x82f2
   __TEXT.__objc_methtype: 0x1395
-  __TEXT.__objc_stubs: 0x5060
-  __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0xb88
+  __TEXT.__objc_stubs: 0x50a0
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0xbc8
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b88
+  __DATA_CONST.__objc_selrefs: 0x1c70
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x610
+  __AUTH_CONST.__auth_got: 0x608
   __AUTH_CONST.__auth_ptr: 0x170
   __AUTH_CONST.__const: 0x910
-  __AUTH_CONST.__cfstring: 0x1e40
-  __AUTH_CONST.__objc_const: 0x5f20
+  __AUTH_CONST.__cfstring: 0x1e20
+  __AUTH_CONST.__objc_const: 0x53b8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x12c0
-  __AUTH.__data: 0x400
-  __DATA.__objc_ivar: 0x2a0
+  __AUTH.__objc_data: 0x12a0
+  __AUTH.__data: 0x408
+  __DATA.__objc_ivar: 0x29c
   __DATA.__data: 0xed0
-  __DATA.__bss: 0x1ea0
   __DATA.__common: 0x241
+  __DATA.__bss: 0x1ea0
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1693
-  Symbols:   1363
-  CStrings:  1999
+  Functions: 1692
+  Symbols:   1356
+  CStrings:  1997
 
Symbols:
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ __swift_FORCE_LOAD_$_swiftCompression
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_retain_x27
- _objc_retain_x28
- _swift_isUniquelyReferenced_nonNull_native
CStrings:
+ "-[PHPickerResult _initWithItemProvider:itemIdentifier:]"
+ "PHPickerConfigurationCoderPreselectedItemIdentifiersKey"
+ "PHPickerConfigurationCoderSearchTextKey"
+ "Q45"
+ "T@\"NSArray\",C,N"
+ "T@\"NSArray\",C,N,V_preselectedItemIdentifiers"
+ "T@\"NSString\",C,N,V__searchText"
+ "__searchText"
+ "_initWithItemProvider:itemIdentifier:"
+ "_preselectedItemIdentifiers"
+ "_searchText"
+ "configuration.photoLibrary || configuration.preselectedAssetIdentifiers.count == 0 || configuration.preselectedItemIdentifiers.count == 0"
+ "configuration.preselectedItemIdentifiers != nil"
+ "preselectedItemIdentifiers"
+ "setPreselectedItemIdentifiers:"
+ "set_searchText:"
- "\x16"
- "-[PHPickerResult _initWithItemProvider:assetIdentifier:]"
- "PHPickerCollectionConfigurationCoderPreselectedIdentifiersKey"
- "PHPickerConfigurationCoderFollowupPeopleConfigurationsKey"
- "PHPickerConfigurationCoderPreselectedAssetIdentifiersKey"
- "R35"
- "T@\"NSArray\",C,N,S_setFollowupPeopleConfigurations:,V__followupPeopleConfigurations"
- "T@\"NSArray\",C,N,V_preselectedAssetIdentifiers"
- "T@\"NSArray\",C,N,V_preselectedIdentifiers"
- "__followupPeopleConfigurations"
- "_followupPeopleConfigurations"
- "_initWithItemProvider:assetIdentifier:"
- "_preselectedAssetIdentifiers"
- "_preselectedIdentifiers"
- "_setFollowupPeopleConfigurations:"
- "configuration.photoLibrary || configuration.preselectedAssetIdentifiers.count == 0"
- "preselectedIdentifiers"
- "setPreselectedIdentifiers:"

```
