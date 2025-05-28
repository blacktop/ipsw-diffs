## PodcastsWidget

> `/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget`

```diff

-4023.410.2.0.0
-  __TEXT.__text: 0x8b8f8
-  __TEXT.__auth_stubs: 0x1f50
+4023.510.2.0.0
+  __TEXT.__text: 0x8ae6c
+  __TEXT.__auth_stubs: 0x2010
   __TEXT.__objc_stubs: 0x12a0
   __TEXT.__objc_methlist: 0x36c
   __TEXT.__objc_classname: 0x62
-  __TEXT.__objc_methname: 0x1301
+  __TEXT.__objc_methname: 0x125f
   __TEXT.__objc_methtype: 0x94
-  __TEXT.__const: 0x2614
+  __TEXT.__const: 0x1ef4
   __TEXT.__gcc_except_tab: 0xa8
   __TEXT.__oslogstring: 0x1d3
-  __TEXT.__cstring: 0xd63
-  __TEXT.__constg_swiftt: 0x115c
-  __TEXT.__swift5_typeref: 0x955a
+  __TEXT.__cstring: 0x1163
+  __TEXT.__constg_swiftt: 0xda0
+  __TEXT.__swift5_typeref: 0x6100
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x963
-  __TEXT.__swift5_fieldmd: 0xb4c
-  __TEXT.__swift5_assocty: 0x368
-  __TEXT.__swift5_proto: 0xfc
-  __TEXT.__swift5_types: 0xf4
-  __TEXT.__swift5_capture: 0x2f0
+  __TEXT.__swift5_reflstr: 0x7c3
+  __TEXT.__swift5_fieldmd: 0x900
+  __TEXT.__swift5_assocty: 0x290
+  __TEXT.__swift5_proto: 0xc4
+  __TEXT.__swift5_types: 0xc4
+  __TEXT.__swift5_capture: 0x1a8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x16f8
-  __TEXT.__eh_frame: 0x500
-  __DATA_CONST.__auth_got: 0xfb8
-  __DATA_CONST.__got: 0x750
-  __DATA_CONST.__auth_ptr: 0x108
-  __DATA_CONST.__const: 0x2b08
+  __TEXT.__unwind_info: 0x13a0
+  __TEXT.__eh_frame: 0x4e0
+  __DATA_CONST.__auth_got: 0x1018
+  __DATA_CONST.__got: 0x748
+  __DATA_CONST.__auth_ptr: 0xf8
+  __DATA_CONST.__const: 0x23b0
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xc0
   __DATA.__objc_const: 0x9f8
-  __DATA.__objc_selrefs: 0x6f0
-  __DATA.__objc_classrefs: 0xd8
+  __DATA.__objc_selrefs: 0x6b8
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x230
-  __DATA.__data: 0x3068
-  __DATA.__bss: 0x2170
-  __DATA.__common: 0x28
+  __DATA.__data: 0x28c8
+  __DATA.__bss: 0x1a20
+  __DATA.__common: 0x60
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
+  - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1684
-  Symbols:   220
-  CStrings:  340
+  Functions: 1381
+  Symbols:   223
+  CStrings:  352
 
Symbols:
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftModelIO
+ _kMTWidgetArtworkHeight
+ _kMTWidgetArtworkWidth
+ _objc_retain_x23
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_initStaticObject
+ _swift_unknownObjectRetain_n
- _OBJC_CLASS_$_OS_dispatch_queue
- _OBJC_CLASS_$_UIFont
- _OBJC_CLASS_$_UIImageSymbolConfiguration
- _PFLocalizedString
- _objc_retain_x28
- _os_feature_enabled_use_first_time_available
- _swift_projectBox
CStrings:
+ "Can't construct Array with count < 0"
+ "Critical failure: unable to recover with image placeholder. returning episode without artwork. %s"
+ "Division by zero"
+ "Division results in an overflow"
+ "Failed to load artwork. Attempting to load placeholder: %s"
+ "Failed to load episode artwork, attempting show artwork: %s"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Unexpectedly found episode artwork without show artwork. No Fallback path available."
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"
+ "showPlayerArtworkUntilDate"
- "ContentSizeCategory"
- "Creating UpNextView with widgetFamily.%{public}s, contentSizeCategory.%{public}.s"
- "LISTEN_NOW_STATIC_PLAYING"
- "LISTEN_NOW_STATIC_SHORT_PLAYING"
- "_systemImageNamed:"
- "asyncDiskArtworkForEpisodeUuid:size:completion:"
- "boldSystemFontOfSize:"
- "clearColor"
- "configurationWithFont:"
- "imageWithConfiguration:"
- "stringForKey:"
- "upNextNowPlayingUUID"
- "v16@?0@\"UIImage\"8"

```
