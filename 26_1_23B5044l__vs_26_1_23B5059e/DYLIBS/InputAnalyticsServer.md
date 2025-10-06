## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-108.0.0.0.0
-  __TEXT.__text: 0x45544
+111.0.0.0.0
+  __TEXT.__text: 0x461fc
   __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x39bc
-  __TEXT.__const: 0x2e0
-  __TEXT.__cstring: 0x3649
-  __TEXT.__oslogstring: 0x46e6
-  __TEXT.__gcc_except_tab: 0x690
+  __TEXT.__objc_methlist: 0x39c4
+  __TEXT.__const: 0x2f0
+  __TEXT.__cstring: 0x3689
+  __TEXT.__oslogstring: 0x4d83
+  __TEXT.__gcc_except_tab: 0x694
   __TEXT.__swift5_typeref: 0x10d
   __TEXT.__swift5_capture: 0x98
   __TEXT.__constg_swiftt: 0x4c

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0xcf8
+  __TEXT.__unwind_info: 0xcc0
   __TEXT.__eh_frame: 0x310
   __TEXT.__objc_classname: 0x834
-  __TEXT.__objc_methname: 0x8ac4
+  __TEXT.__objc_methname: 0x8aee
   __TEXT.__objc_methtype: 0xc16
-  __TEXT.__objc_stubs: 0x6be0
+  __TEXT.__objc_stubs: 0x6c00
   __DATA_CONST.__got: 0xed8
-  __DATA_CONST.__const: 0xe80
+  __DATA_CONST.__const: 0xe58
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1de8
+  __DATA_CONST.__objc_selrefs: 0x1df0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x180
-  __DATA_CONST.__objc_arraydata: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__auth_got: 0x658
   __AUTH_CONST.__const: 0xd38
-  __AUTH_CONST.__cfstring: 0x3ae0
+  __AUTH_CONST.__cfstring: 0x3b20
   __AUTH_CONST.__objc_const: 0x6740
   __AUTH_CONST.__objc_intobj: 0xcf0
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH.__objc_data: 0x888
+  __AUTH.__objc_data: 0x6a8
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x4b4
   __DATA.__data: 0x3b0
-  __DATA.__bss: 0x1b8
-  __DATA_DIRTY.__objc_data: 0xde8
+  __DATA.__bss: 0xe0
+  __DATA_DIRTY.__objc_data: 0xfc8
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x290
+  __DATA_DIRTY.__bss: 0x368
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Anvil.framework/Anvil
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
-  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService
   - /System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C1F9971B-D19A-3E65-950A-C4C799A6302F
-  Functions: 1625
-  Symbols:   597
-  CStrings:  2975
+  UUID: 18A8956F-ECB7-348F-802F-83454C26EA81
+  Functions: 1614
+  Symbols:   596
+  CStrings:  3011
 
Symbols:
- _AnalyticsSendEventLazy
CStrings:
+ "%{private}@ periodic24HourEvents called. Will call %{private}@"
+ "[%lu/%lu] Calling %{private}@"
+ "[%lu/%lu] Session Manager: %{private}@"
+ "com.apple.CharacterPaletteIM"
+ "com.apple.CharacterPicker.RemoteGenerationViewService"
+ "enumerateAnalyticsWithShouldDonateBiome:"
+ "isGenerativeModelsAvailable called"
+ "isGenerativeModelsAvailableForSmartReply called"
+ "isGenmojiSession:"
+ "periodic24HourEvents: ADM available:%{private}lu"
+ "periodic24HourEvents: Genmoji available:%{private}lu"
+ "periodic24HourEvents: SR available:%{private}lu"
+ "periodic24HourEvents: WT available:%{private}lu"
+ "periodic24HourEvents: at obtained"
+ "periodic24HourEvents: called"
+ "periodic24HourEvents: completed"
+ "periodic24HourEvents: ds initialized"
+ "periodic24HourEvents: ds obtained"
+ "periodic24HourEvents: querying availability"
+ "periodic24HourEvents: starting"
+ "periodic24HourEventsWithModelAvailability: %{private}x"
+ "periodic24HourEventsWithModelAvailability: Creation %{private}x"
+ "periodic24HourEventsWithModelAvailability: Reporting postfix %{private}@"
+ "periodic24HourEventsWithModelAvailability: Usage %{private}x"
+ "periodic24HourEventsWithModelAvailability: accessing ds"
+ "periodic24HourEventsWithModelAvailability: assembling payload"
+ "periodic24HourEventsWithModelAvailability: called"
+ "periodic24HourEventsWithModelAvailability: completed"
+ "periodic24HourEventsWithModelAvailability: dfts grabbed"
+ "periodic24HourEventsWithModelAvailability: ds complete"
+ "periodic24HourEventsWithModelAvailability: enumerating features"
+ "periodic24HourEventsWithModelAvailability: feature %{private}lu"
+ "periodic24HourEventsWithModelAvailability: feature:%{private}lu"
+ "periodic24HourEventsWithModelAvailability: fetched cf"
+ "periodic24HourEventsWithModelAvailability: fetched uf"
+ "periodic24HourEventsWithModelAvailability: fetching cf"
+ "periodic24HourEventsWithModelAvailability: fetching me"
+ "periodic24HourEventsWithModelAvailability: fetching uf"
+ "periodic24HourEventsWithModelAvailability: grabbing daterange"
+ "periodic24HourEventsWithModelAvailability: grabbing dfts"
+ "periodic24HourEventsWithModelAvailability: grabbing ucp"
+ "periodic24HourEventsWithModelAvailability: published"
+ "reportThirdPartyKeyboardAdoption: Enabled %{private}d, Default %{private}d"
- "@\"NSDictionary\"8@?0"
- "isGenmojiSession"
- "periodic24HourEvents: ADM available:%lu"
- "periodic24HourEvents: Genmoji available:%lu"
- "periodic24HourEvents: SR available:%lu"
- "periodic24HourEvents: WT available:%lu"
- "periodic24HourEventsWithModelAvailability: %x"
- "periodic24HourEventsWithModelAvailability: Usage %x"
- "reportThirdPartyKeyboardAdoption: Enabled %d, Default %d"

```
